Need 
    Python 3
    Pip 3
    libmysqlclient-dev


# how to clone 
`
git clone <repo>
`
# how to build 
```
pip install -r requirements.txt
python setup.py clean --all
python -m build
```
# how build docker
```
docker build -t <image_name>:<tag> .

```
# how to run in dev mode 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
or 
```
python -m gunicorn restWebsite.wsgi:application -b '[::]:8000'
```
# run docker 
`
docker run -d -p 80:8000  --name my_running_container  <image_name>:<tag> 
`
`
docker logs my_running_container
`
# FAQ
1. Windows error while mysql client build <br>
   Directly install binary mysqlclient
        pip install --only-binary :all: mysqlclient