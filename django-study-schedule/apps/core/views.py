from django.core.exceptions import ImproperlyConfigured
import django_filters
from django.http import Http404


class UUIDViewMixin:
    uuid_url_kwarg = None
    def get_object(self, queryset=None):

        if self.uuid_url_kwarg is None:
            raise ImproperlyConfigured(
                 "UUID view %s não declarou uuid_url_kwarg" % self.__class__.__name__
                )

        if queryset is None:
            queryset = self.get_queryset()

        uuid = self.kwargs.get(self.uuid_url_kwarg)

        if uuid is not None:
            queryset = queryset.filter(uuid=uuid)

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class FilteredViewMixin:
    filterset_class = None
    filter_fields = None
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        if self.filter_fields is None and self.filterset_class is None:
            raise ImproperlyConfigured(
                "%(cls)s não tem informações de filtragem. Defina "
                "filter_fields ou "
                "filterset_class" % {
                    'cls': self.__class__.__name__
                }
            )
            
        if self.filter_fields is not None and self.filterset_class is not None:
            raise ImproperlyConfigured(
                "%(cls)s apenas deve definir um dos seguintes: "
                "filter_fields ou "
                "filterset_class" % {
                    'cls': self.__class__.__name__
                }
            )
        
        if self.filter_fields is None:
            self.filterset = self.filterset_class(self.request.GET, request=self.request, queryset=queryset, **self.get_filterset_kwargs())
        else:
            class FilterSet(django_filters.FilterSet):
                class Meta:
                    model = self.model
                    fields = self.filter_fields
            self.filterset = FilterSet(self.request.GET, queryset=queryset)
            
        return self.filterset.qs
    
    def get_filterset_kwargs(self):
        if hasattr(self, 'filterset_kwargs'):
            return self.filterset_kwargs
        else:
            return {}

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context