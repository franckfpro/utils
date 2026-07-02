Crée et applique les migrations de la base de données :
```Bash
uv run python manage.py makemigrations tasks
uv run python manage.py migrate
```

(Optionnel) Crée quelques tags via le shell pour tester le champ ManyToMany :
```Bash
uv run python manage.py shell -c "from tasks.models import Tag; Tag.objects.create(name='Projet'); Tag.objects.create(name='Personnel')"
```


Lance le serveur de développement :
```Bash
uv run python manage.py runserver
```
