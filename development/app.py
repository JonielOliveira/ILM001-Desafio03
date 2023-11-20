from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato.html')  
def contato():
    return render_template('contato.html')

@app.route('/machos.html')
def machos():
    return render_template('machos.html')

@app.route('/spike.html')
def spike():
    return render_template('usuario-01-spike.html')

@app.route('/luke.html')
def luke():
    return render_template('usuario-02-luke.html')

@app.route('/simba.html')
def simba():
    return render_template('usuario-03-simba.html')

@app.route('/robin.html')
def robin():
    return render_template('usuario-04-robin.html')

@app.route('/femeas.html')
def femeas():
    return render_template('femeas.html')

@app.route('/aurora.html')
def aurora():
    return render_template('usuario-05-aurora.html')

@app.route('/katy.html')
def katy():
    return render_template('usuario-06-katy.html')

@app.route('/bebel.html')
def bebel():
    return render_template('usuario-07-bebel.html')

@app.route('/lady.html')
def lady():
    return render_template('usuario-08-lady.html')