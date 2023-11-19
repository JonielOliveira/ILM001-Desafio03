from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contato')  
def contato():
    return render_template('contato.html')

@app.route('/machos')
def machos():
    return render_template('machos.html')

@app.route('/spike')
def spike():
    return render_template('usuario-01-spike.html')

@app.route('/luke')
def luke():
    return render_template('usuario-02-luke.html')

@app.route('/simba')
def simba():
    return render_template('usuario-03-simba.html')

@app.route('/robin')
def robin():
    return render_template('usuario-04-robin.html')

@app.route('/femeas')
def femeas():
    return render_template('femeas.html')

@app.route('/aurora')
def aurora():
    return render_template('usuario-05-aurora.html')

@app.route('/katy')
def katy():
    return render_template('usuario-06-katy.html')

@app.route('/bebel')
def bebel():
    return render_template('usuario-07-bebel.html')

@app.route('/lady')
def lady():
    return render_template('usuario-08-lady.html')


