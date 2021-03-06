from flask import *
from flask_socketio import *

app = Flask(__name__)
app.debug = True
app.config.update(DEBUG = True, SECRET_KEY = 'Torres911', USERNAME='torRent', PASSWORD='puj2017')
chat = SocketIO(app)
namespace = "/senpai"


@chat.on("new-message", namespace=namespace)
def nuevo_mensaje(message):
    print("Ha llegado un nuevo mensaje {!r}".format(message))

    chat.emit("new-message", message, namespace=namespace)


@app.route('/', methods=['GET', 'POST'])
def entrarChat():
	"""
	Entrada: La informacion introducida por el usuario para iniciar sesion en los inputs

	Proceso: La organiza en dos archivos distintos un archivo para los usuarios y otro para las contraseña, 
	         el cual para acceder a la pagina principal, pasa la informacion del archivo a una lista respectivamente y 
	         compara los indices para ver si coinciden con la base de datos que ya existe

	Salida: Redirijirlo a la ventana del chat o a las otras ventanas de acceso denegado o de registro segun la situacion

	"""
	if(request.method == 'POST'):
		u = request.form['USUARIO']
		p = request.form['CONTRASEÑA']
		lista_usuarios = []
		lista_contrasenas = []

		#Funcion para separar la informacion del Username
		y = open("usuarios.txt", "r")
		user = y.readlines()
		y.close()

		tU = 0
		while(tU < len(user)):
			palabra = user[tU]
			tU += 1
			lista_usuarios = lista_usuarios + palabra.split(" ")

		for espacio in lista_usuarios:
			if('\n' in espacio):
				lista_usuarios[lista_usuarios.index(espacio)] = espacio.replace('\n', '')

		
		#Funcion para separar las contraseñas
		t = open("contrasenas.txt", "r")
		contras = t.readlines()
		t.close()

		z = 0
		while(z < len(contras)):
			palabra = contras[z]
			z += 1
			lista_contrasenas = lista_contrasenas + palabra.split(" ")

		for c in lista_contrasenas:
			if('\n' in c):
				lista_contrasenas[lista_contrasenas.index(c)] = c.replace('\n', '')

		if(u in lista_usuarios):
			if(p in lista_contrasenas):
				if(lista_usuarios.index(u) == lista_contrasenas.index(p)):
					return render_template('chat.html')
				else:
					return render_template('denegado.html')
			else:
				return render_template('denegado.html')
		else:
			return render_template('inicio.html')

	return render_template('inicio.html')

		
@app.route('/registro', methods=['GET', 'POST'])
def registros():	
	if(request.method == 'POST'):
		#Registro Usuarios Nuevos
		un = request.form['USUARIONUEVO']
		p1 = request.form['CONTRASENANUEVA']
		p2 = request.form['CONTRASENANUEVAREP']
		lista_u = []
		lista_p = []
		if(p1 == p2):
			lista_u.append(un)
			lista_p.append(p1)
			def tester():
				l = open("usuarios.txt", "r")
				test = l.readlines()
				l.close()
				a = open("usuarios.txt", "a")
				a.write("\n" + str(un))
				a.close()

				e = open("usuarios.txt", "r")
				test2 = e.readlines()
				e.close()
				b = open("contrasenas.txt", "a")
				b.write("\n" + str(p1))
				b.close()
			tester()

			return render_template('inicio.html')
		else:
			return render_template('denegado.html')
	return render_template('registro.html')


@app.route('/sobreproyecto')
def sobreproyecto():
	return render_template('sobreproyecto.html')

if __name__ == "__main__":
    chat.run(app)