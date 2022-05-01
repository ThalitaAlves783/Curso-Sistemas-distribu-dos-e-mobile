from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
app = Flask(__name__)
#############################################################
# RETORNANDO JSON
@app.route("/")
def index():
 return jsonify({"mensagem":"Hello Json!"})
#############################################################
# UTILIZANDO METALINGUAGEM JINJA
@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome=None):
    return render_template('hello.html', name=nome)
#############################################################
# PASSAGEM DE PARÂMETRO - NÚMERO INTEIRO
@app.route('/show/<int:id>')
def show(id):
    return 'Valor recebido id = %d' %id
#############################################################
# VERIFICANDO O METODO (VERBO HTTP) UTILIZADO
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Login via POST'
    else:
        return '''
                <html>
                    <body>
                        <form method="post">
                            <p><input type=text name=username>
                            <p><input type=submit value=Login>
                        </form>
                    </body>
                </html>
                '''
#############################################################
# Pagina nao encontrada - erro 404
@app.errorhandler(404)
def page_not_found(error):
     return render_template('error.html'), 404
#############################################################
if __name__ == '__main__':
 app.run()