# Hello django app in k8s

## Local requirements
- python 3.9.10

## Local setup

### Intall libraries
python3 -m venv .venv  
source .venv/bin/activate   
pip install -r requirements.txt 
django-admin startproject django_project .  

### Run migrations
python3 manage.py runserver
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser (admin/admin)

## Create requirements.txt
pip freeze > requirements.txt

## Connect to Postgres BD
export POSTGRES_USER=postgres  
export POSTGRES_PASSWORD=l2wLCwcw0q  
export POSTGRES_HOST=127.0.0.1  
export POSTGRES_PORT=5432  

---

## Docker

##· Create image
docker build -t django_hello_app:latest  .

### Run container
docker run -p 8000:8000 django_hello_app:latest  

### Run container using local postgresql
docker run -p 8000:8000 -e POSTGRES_HOST=127.0.0.1 -e POSTGRES_PORT=5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=XvxtXjM7GN --entrypoint /bin/bash -it soydiegomen/django_hello_app:v2

### Crear tag 
docker image tag django_hello_app:latest soydiegomen/django_hello_app:latest
docker images

---

## Docker Hub

### Login
docker login

### Logout
docker logout

## Push a docker hub
docker build -t soydiegomen/django_hello_app:v2  .  
docker push soydiegomen/django_hello_app:latest

---

## Kubernetes
kubectl apply -f k8s/namespace.yml
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml

### Porforwarding para consultar el servicio
kubectl port-forward service/django-app  8080:8080 -n django-app
http://localhost:8080/

## Install Postgresql
+ Reference:  https://github.com/bitnami/charts/tree/master/bitnami/postgresql   
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install django-app bitnami/postgresql -n django-app

### Get postgresql pass
kubectl describe secret  my-release-postgresql
export POSTGRES_PASSWORD=43qzNLy1f0

## Setup tunnel to connect to postgres
kubectl port-forward --namespace django-app svc/django-app-postgresql 5432:5432

## Test postgres connection
kubectl get all -o wide  
kubectl run postgres-postgresql-client --rm --tty -i --restart='Never' --namespace django-app --image docker.io/bitnami/postgresql:11.9.0-debian-10-r48 --env="PGPASSWORD=$POSTGRES_PASSWORD" --command -- psql --host postgres-service-postgresql -U postgres -d postgres -p 5432

### Secrets to base64
echo -n "postgres" | base64
echo -n $POSTGRES_PASSWORD | base64

### Create BD secrets in cluster
kubectl apply -f k8s/postgres/secrets.yml

## Delete postgres service (Helm Chart)
helm delete postgres-service -n django-app
---

## Referencias: 
https://itnext.io/basic-postgres-database-in-kubernetes-23c7834d91ef
https://bitnami.com/stack/postgresql/helm

## Create tunnel to test de django app
kubectl port-forward service/django-app  8080:8080 -n django-app
http://localhost:8080/