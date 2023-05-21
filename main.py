from flask import Flask, render_template, url_for, request

app = Flask(__name__)  # указываем имя нашего приложения
# __name__ указывает имя текущего файла, но можно указать и __main__
# будет там искать шаблоны и тд

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")  # с помощью декоратора указываем url
# @app.route("/index") #если по разным url должен выполняться один обработчик, пишем их подряд
def index():  # по которому будет отработывать обрабочик
    print(url_for('index'))  # получим url обработчика "/"
    return render_template('index.html', title="Про Flask", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О сайте", menu=menu)


@app.route("/profile/<username>")  # динамечкое создание url
def profile(username):
    return f"Пользователь: {username}"


# надо явно указать, что можем принимать данные методом POST: methods=["POST"]

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
    return render_template('contact.html', title="Обратная связь", menu=menu)


if __name__ == '__main__':  # это прописывается для запуска именно на локальном устройстве
    app.run(debug=True)  # запускаем локальный веб сервер. debug=True - в браузере будем видеть все ошибки
    # по оканчании разработки надо поставить False
