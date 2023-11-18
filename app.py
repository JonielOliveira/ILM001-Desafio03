from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contato')  
def contato():
    return render_template('contato.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/spike')
def spike():
    return render_template('usuario-01-spike.html')



'''
app.config('MYSQL_Host') = 'localhost' # 127.0.0.1
app.config('MYSQL_USER') = 'root'
app.config('MYSQL_PASSWORD') = '1234'
app.config('MYSQL_Host') = 'contatos'

@app.route('/contato', methods=['GET','POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES(%s, %s, %s)", (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return 'sucesso'
    return render_template('contatos.html')
'''



