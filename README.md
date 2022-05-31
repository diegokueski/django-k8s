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

## Connect to Postgres BD
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=XvxtXjM7GN
export HOST=127.0.0.1
export POSTGRES_PORT=5432

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
docker build -t soydiegomen/django_hello_app:v2  .
docker push soydiegomen/django_hello_app:latest

## Kubernetes
kubectl apply -f k8s/namespace.yml
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml

+Porforwarding para consultar el servicio 
kubectl port-forward service/django-app  8080:8080 -n django-app
http://localhost:8080/

## Install Postgresql
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/postgresql

+Obtener el pass de postgres
kubectl describe secret  my-release-postgresql
export POSTGRES_PASSWORD=43qzNLy1f0

+Hacer el tunnel para conectarme a la BD
kubectl port-forward --namespace django-app svc/postgres-service-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432
-----
+Conectarme a la BD utilizando un conteiner con un cliente de postgresql
kubectl get all -o wide  
kubectl run postgres-postgresql-client --rm --tty -i --restart='Never' --namespace django-app --image docker.io/bitnami/postgresql:11.9.0-debian-10-r48 --env="PGPASSWORD=$POSTGRES_PASSWORD" --command -- psql --host postgres-service-postgresql -U postgres -d postgres -p 5432
+Hacer un query
SELECT * FROM phonebook ORDER BY lastname;

## Secrets to base64
echo -n "postgres" | base64
echo -n "XvxtXjM7GN" | base64

+ Create BD secrets in cluster
kubectl apply -f k8s/postgres/secrets.yml

+Referencias: 
https://itnext.io/basic-postgres-database-in-kubernetes-23c7834d91ef
https://bitnami.com/stack/postgresql/helm

