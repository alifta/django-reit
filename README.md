**Save list of packages**

```shell
python -m pip freeze > requirements.txt
```

**Reset Django Project**

1. Remove database migrations

```shell
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

2. Drop current database or delete `db.sqlite3`

**Local mail server**
To run a local mail server and testing forgot password functionality, run the following in terminal to start
a SMTP server at http://localhost:1025. It won't send any emails to actual email address but show them in terminal.

```shell
python -m smtpd -n -c DebuggingServer localhost:1025
```
