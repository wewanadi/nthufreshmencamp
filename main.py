from flask import Flask, request, render_template
app = Flask(
__name__, static_url_path='/',
# static_folder='/templates'
)

@app.route('/45diary')
def index():
    return render_template("45diary.html")

@app.route('/45eat')
def touch():
    return render_template("45eat.html")

@app.route('/45new')
def find():
    return render_template("45new.html")

@app.route('/find2')
def aaa():
    return render_template("123sleep2.html")


@app.route('/45zzzz')
def zzz():
    return render_template("45zzzz.html")

@app.route('/45book')
def book():
    return render_template("45book.html")

@app.route('/45system')
def phone():
    return render_template("45system.html")

@app.route('/312linethree')
def qq():
    return render_template("312linethree.html")

@app.route('/312linedragon')
def ww():
    return render_template("312linedragon.html")

@app.route('/312linebird')
def ee():
    return render_template("312linebird.html")

@app.route('/312pwd')
def ss():
    return render_template("312pwd.html")

@app.route('/45map')
def ff():
    return render_template("45map.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9109)