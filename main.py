from flask import Flask, render_template, url_for

app = Flask(__name__)#указываем имя нашего приложения
#__name__ указывает имя текущего файла, но можно указать и __main__
#будет там искать шаблоны и тд

menu = ["Установка", "Первое приложение", "Обратная связь"]

@app.route("/")# с помощью декоратора указываем url
#@app.route("/index") #если по разным url должен выполняться один обработчик, пишем их подряд
def index():#по которому будет отработывать обрабочик
    print(url_for('index'))# получим url обработчика "/"
    return render_template('index.html', title="Про Flask", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О сайте", menu=menu)


@app.route("/profile/<username>")#динамечкое создание url
def profile(username):
    return f"Пользователь: {username}"


if __name__ == '__main__':# это прописывается для запуска именно на локальном устройстве
    app.run(debug=True)# запускаем локальный веб сервер. debug=True - в браузере будем видеть все ошибки
    #по оканчании разработки надо поставить False
