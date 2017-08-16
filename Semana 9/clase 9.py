from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/exito/<nombre>')
def exito(nombre):
    return 'Bienvenido, %s' % nombre

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['nm']
        return redirect(url_for('exito', nombre=usuario))
    else:
        usuario = request.args.get('nm')
        return redirect(url_for('exito', nombre=usuario))

if __name__ == '__main__':
    app.run()





        # from flask import Flask, redirect, url_for
# App = Flask(__name__)
#
# @App.route('/admin')
# def hola_admin():
#     return 'Xopa Admin'
#
# @App.route('/mortal/<mortal>')
# def hola_mortal(mortal):
#     return 'Larga de aqui mortal, %s' % mortal
#
# @App.route('/usuario/<nombre>')
# def hola_usuario(nombre):
#     if nombre == 'admin':
#         return redirect(url_for('hola_admin'))
#     else:
#         return redirect(url_for('hola_mortal', mortal=nombre))
#
# if __name__ == '__main__':
#     App.run(port=80)

# from flask import Flask
# App = Flask(__name__)
#
# @App.route('/')
# def hola_mundo():
#     return 'Xopa Laope!'
#
#
# @App.route('/hola/<nombre>/')
# def hola_laope(nombre):
#     return 'Hola laope,%s!' % nombre
#
#
# @App.route('/blog/<int:idEntrada>')
# def mostrar_blog(idEntrada):
#     return 'Entrada,#%d' %idEntrada
#
#
# @App.route('/itbms/<float:subtotal>')
# def calcular_itbms(subtotal):
#     return 'impuesto de,$.2f, es $%.2f' %(subtotal, subtotal*0.07)
#
# if __name__ == '__main__':
#     App.run()