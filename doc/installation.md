# Déploiement serveur pythonanywhere
Voir la documentation DjangoGirls

# Sur poste dev

##init git
~~~
git init
~~~

## config git

~~~
 git config --global user.name hugo.roussaffa
 git config --global user.email hugoroussaffa@gmail.com
~~~

## commit des modifs git
~~~
git add -A .
git commit -m "init"
~~~

## publier sur le nouveau repo

~~~
git remote add origin https://github.com/geodatup/QuOrEL.git
git push origin master
~~~

# sur prod

## clone de la source
~~~
git clone https://github.com/geodatup/QuOrEL.git
~~~

suite à des modification de la source faire un pull

~~~
git pull https://github.com/geodatup/QuOrEL.git master
~~~

## Créer un env virtuel 

~~~
cd quorelcms
virtualenv --python=python3.4 myvenv
source myvenv/bin/activate
~~~

## installer django et les dépendances

~~~
pip install -r requierment
~~~

###et aussi mysql

```
export DJANGO_SETTINGS_MODULE=quorelcms.settings.local
```


# Migration des données du projets
Necéssite de créer un autre projet cms à coté puis de lancer 
python manage.py migrate 
dans le projet quorelcms
(sinon ça ne marche pas... la table n'existe pas dit il...)


## deplacer les fichiers media

##coté dev créer un dump

## Load du dump sur la prod

```
python manage.py loaddata data_final.json
```

#puis collecter les fichiers static
```
python manage.py collectstatic
```



# creer le super utilisateur
```
python manage.py createsuperuser
```


#Commande GIT 
###DEPUIS POSTE DEV
```
git add -A .
git commit -m "auto comment"
git push origin master
```


###clone Git (1er déployement)
```
git clone https://github.com/geodatup/QuOrEL.git


virtualenv --python=python3.4 myvenv
source myvenv/bin/activate


pip install Django==1.9 whitenoise
pip install django-leaflet
pip install django-geojson
pip install django-import-export
pip install mysqlclient
```

# create database
```
mysql 
pwsd : **

python manage.py collectstatic
```






###DEPUIS POSTE QUALIF - Pythonanywhere (myvenv)
```
cd /QuOrEl

git pull

python manage.py migrate

```




## troubleshooting 

~~~
django.db.migrations.state.InvalidBasesError: Cannot resolve bases for [<ModelState: 'djangocms_column.MultiColumns'>, <ModelState: 'djangocms_column.Column'>, <ModelState: 'djangocms_text_ckeditor.Text'>, <ModelState: 'djangocms_style.Style'>]
This can happen if you are inheriting models from an app with migrations (e.g. contrib.auth)
 in an app with no migrations; see https://docs.djangoproject.com/en/1.8/topics/migrations/#dependencies for more
~~~
~~~
disable all of the cms apps within INSTALLED_APPS in settings.py
run manage.py migrate
enable 'cms',
    'menus',
    'sekizai',
    'treebeard',
run manage.py migrate again
enable all of apps in INSTALLED_APPS
run manage.py migrate again
~~~

~~~
_mysql_exceptions.OperationalError: (1252, 'All parts of a SPATIAL index must be NOT NULL')
~~~

