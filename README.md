# Обрезка ссылок с помощью Битли
Теперь вы можете сокращать ссылки из терминала, а так же получать количество кликов по полученной ссылке.
Для этого вам достаточно передать при запуске кода аргумент:
ссылку которую вы хотите превратить в битлинк, либо ссылку битлинка – для подсчета переходов по этой ссылке.
### Как установить
Для запуска необходим токен, получить его можно при регистрации на официальном сайте [bitly](https://app.bitly.com/).
Далее рядом с кодом вы должны создать файл `.env`, в котором будет храниться ваш токен:
```
BITLINK_TOKEN='ВАШ ТОКЕН'
```
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
Для запуска передайте аргумент в виде ссылки, заменив `url`:
```
$ python main.py url
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).