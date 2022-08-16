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
docker-compose exec db mysql demo
```