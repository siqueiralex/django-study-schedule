# Here if the command is dump, app or test, the script will capture ARG parameter
ifneq ($(filter $(MAKECMDGOALS), dump app test module),) 
	ARG := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
	$(eval $(ARG):;@:)
endif



#### SÓ RODAR NA MÁQUINA LOCAL #####
#### REMOVER DEPOIS QUE AS MIGRACOES PASSAREM A SER COMMITADAS #####

db_down:
	docker-compose -f ./postgres/docker-compose.yaml down --volumes

db_stop:
	docker-compose -f ./postgres/docker-compose.yaml stop db

db_destroy: db_stop db_down
	docker volume rm dstudy_pg_data --force

db_up:
	docker-compose -f ./postgres/docker-compose.yaml --env-file ./postgres/.env up -d

sleep:
	sleep 1

setup_new_db: db_destroy db_up sleep stop destroy build start migrations migrate superuser
	@echo "Local deploy set up!!"

#######################################################################################


build:
	docker-compose --env-file ./.env up --build -d

destroy: stop
	docker-compose down --rmi local 

start:
	docker-compose start
	
stop:
	docker-compose stop 

restart: stop start
	@echo "Restarted containers!"

migrations:
	docker-compose exec django django-admin makemigrations 

migrate:
	docker-compose exec django django-admin migrate

superuser:
	docker-compose exec django django-admin createsuperuser --no-input

logs: start
	docker-compose logs -f django

populate_base:
	docker-compose exec django django-admin populate -f ./fixtures/base

populate_fake:
	docker-compose exec django django-admin populate -f ./fixtures/fake
	
app: 
	@docker-compose exec django django-admin startapp $(ARG) \
	&& sudo mv ../$(ARG) ../django-study-schedule/apps \
	&& sudo mkdir ../django-study-schedule/apps/$(ARG)/templates \
	&& sudo mkdir ../django-study-schedule/apps/$(ARG)/templates/$(ARG) \
	&& sudo chown -R $(USER): ../django-study-schedule/apps/$(ARG)

shell: 
	docker-compose exec django django-admin shell_plus

show_urls: 
	docker-compose exec django django-admin show_urls	

test:
	docker-compose exec django django-admin test $(ARG) 

network:
	docker network create --driver=bridge dstudy_backend

remove_migrations:
	docker-compose exec -T django django-admin shell < ../scripts/remove_migrations.py
