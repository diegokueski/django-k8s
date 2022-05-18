#Utiliza python 3.9.10

python3 -m venv .venv  
source .venv/bin/activate   
echo  django >> requirements.txt
pip install -r requirements.txt 
django-admin startproject django_project .
python3 manage.py runserver
python3 manage.py makemigrations
python3 manage.py migrate
pip freeze > requirements.txt
python manage.py createsuperuser (admin/admin)

## Docker

+Crear imagen
docker build -t django_hello_app:latest  .

+Ejecutar el contenedor
docker run -p 8000:8000 django_hello_app:latest

+Crear tag
docker image tag django_hello_app:latest soydiegomen/django_hello_app:latest
docker images

+Iniciar sesión en docker
docker login

+Logout
docker logout

+Push a docker hub 
docker push soydiegomen/django_hello_app:latest

## Kubernetes
kubectl apply -f k8s/namespace.yml
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml

+Porforwarding para consultar el servicio 
kubectl port-forward service/django-app  8080:8080 -n django-app
http://localhost:8080/