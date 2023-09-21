**Reset Django Project**

1. Remove database migrations

```shell
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

2. Drop current database or delete `db.sqlite3`

3. Clear migration history

```shell
python manage.py migrate --fake core zero
```
