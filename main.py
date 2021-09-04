from flask import Flask, request, render_template
app = Flask(
__name__, static_url_path='/static/',
# static_folder='/path/to/static/folder'
)

@app.route('/312phone')
def index():
    return render_template("312phone.html")

@app.route('/touch')
def touch():
    return render_template("45system.html")

@app.route('/find1')
def find():
    return render_template("123sleep1.html")

@app.route('/find2')
def aaa():
    return render_template("123sleep2.html")


@app.route('/45zzzz')
def zzz():
    return render_template("45zzzz2.html")

    


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9109)