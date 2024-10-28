Запуск docker-compose для postgres:

```bash
docker-compose up -d
```

После того как контейнер запущен, вы можете подключиться к базе данных с помощью следующей команды:

```bash
psql -h localhost -p 5433 -U admin -d railway_db
```
