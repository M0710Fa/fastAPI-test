# fastAPI-test

## How to Use ?
### server launch
```
docker-compose run --entrypoint "poetry install" demo-app

docker-compose build --no-cache

docker-compose up
```

### Enter MySQL
```
# api モジュールの migrate_db スクリプトを実行する
docker-compose exec demo-app poetry run python -m api.migrate_db

docker-compose exec db mysql demo
```