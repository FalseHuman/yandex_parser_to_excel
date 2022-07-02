# Парсер Яндекс.Маркет

## Установка зависимостей и запуск бота
```bash
$ cd yandex_parser_to_excel
$ pip install -r ./requirements.txt
token = 'YOU_TOKEN' # Необходимо добавить свой токен полученный у BotFather
$ python bot.py
```
### Для работы парсера нужен установленный браузер Google Chrome и Chromedriver, так же измените настройки на свои:
[Ссылка на Chromedriver](https://chromedriver.storage.googleapis.com/index.html)
```bash
options.add_argument(f"user-data-dir=YOUR_PATH_PROFILE_CHROME") # Путь до профиля можно найти введя в адресную строку Chrome - chrome://version/
driver = webdriver.Chrome(executable_path='YOUR_PATH_CHROMEDRIVER', chrome_options=options) # путь до chromedriver
```
## ❗❗❗Ремарка по поводу профиля Chrome ❗❗❗
Прежде чем запустить парсер необходимо залогиниться в Яндексе, это необходимо для того, чтобы обходить капчу. Если не хотите использовать дефолтный профиль Chrome, то необходимо указать путь до профиля, в котором так же необходимо пройти авторизацию в Яндексе.

[Папка с примерами](https://github.com/FalseHuman/yandex_parser_to_excel/tree/master/sample_files)
Связаться со мной в [Telegram](https://t.me/FalseHuman)
