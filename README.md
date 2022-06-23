# bb-microservice
Baber booking BE with microservice

## permiss for all file
```
sudo chown -R $USER:[$USER] . 
Example: sudo chown -R $USER:ductai26998 . 
```
## github
### Add submodule
- In baber_booking_microservice run: 
```git submodule add```
## Docker
### Add a project in submodule
```docker-compose run [container_name] django-admin startproject api [submodule_name]```
Example: docker-compose run bb_service django-admin startproject api bb_service

### Add an app in project
Create a folder=app_name then:
```django-admin startapp [app_name] path```
Example: docker-compose exec bb_account django-admin startapp gallery bb_account/gallery

## After alter model:
```
docker-compose exec bb_service python3 ./bb_service/manage.py makemigrations api
docker-compose exec bb_service python3 ./bb_service/manage.py migrate
```
