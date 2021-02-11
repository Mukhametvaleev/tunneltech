# tunneltech

Создать бэкэнд-приложение на Django с подключением по gRPC API к стороннему серверу, получить данные телеметрии и отрисовать графиками 3 любых параметра в SPA на React. Данные телеметрии должны обновляться в реальном времени с заданной периодичностью (выбирается разработчиком, желательно не реже 1 раза в секунду). Библиотеки и фреймворки - любые из доступных.

## Requirements
```text
node
python~=3.8
redis
```

## Installation
```shell
./scripts/install.sh
```

## Run
```shell
python manage.py runserver
python manage.py beatserver
npm run watch
```
