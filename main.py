from flask import Flask, request, render_template
app = Flask(
__name__, static_url_path='/static',
# static_folder='/templates'
)

@app.route('/45diary')
def index():
    return render_template("45diary.html")

@app.route('/touch')
def touch():
    return render_template("45line.html")

@app.route('/find1')
def find():
    return render_template("123sleep1.html")

@app.route('/find2')
def aaa():
    return render_template("123sleep2.html")


@app.route('/45zzzz')
def zzz():
    return render_template("45zzzz.html")

@app.route('/45book')
def book():
    return render_template("45book.html")

@app.route('/312phone')
def phone():
    return render_template("312phone.html")

@app.route('/312linethree')
def qq():
    return render_template("312linethree.html")

@app.route('/312linedragon')
def ww():
    return render_template("312linedragon.html")

@app.route('/312linebird')
def ee():
    return render_template("312linebird.html")



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9109)