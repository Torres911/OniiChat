from flask import *
from flask_socketio import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def login():
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

		f = open("usuarios.txt", "r")
		texto = f.readlines()
		f.close()

		temp = 0
		while(temp < len(texto)):
			frase = texto[temp]
			temp += 1
			lista_usuarios = lista_usuarios + frase.split(" ")

		for item in lista_usuarios:
			if('\n' in item):
				lista_usuarios[lista_usuarios.index(item)] = item.replace('\n', '')

		f2 = open("contrasenas.txt", "r")
		texto2 = f2.readlines()
		f2.close()

		temp2 = 0
		while(temp2 < len(texto2)):
			frase2 = texto2[temp2]
			temp2 += 1
			lista_contrasenas = lista_contrasenas + frase2.split(" ")

		for item2 in lista_contrasenas:
			if('\n' in item2):
				lista_contrasenas[lista_contrasenas.index(item2)] = item2.replace('\n', '')

		if(u in lista_usuarios):
			if(p in lista_contrasenas):
				if(lista_usuarios.index(n) == lista_contrasenas.index(c)):
					return render_template('mainpage.html')
				else:
					return render_template('denegado.html')
			else:
				return render_template('denegado.html')
		else:
			return render_template('register.html')
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def registrarse():
	"""
	Esta funcion agrega los datos de inicio de sesión a la lista de datos.
	"""
	if(request.method == 'POST'):
		un = request.form['USUARIONUEVO']
		p1 = request.form['CONTRASEÑANUEVA']
		p2 = request.form['CONTRASEÑANUEVAREP']
		lista_usuarios = []
		lista_contrasenas = []
		if(p1 == p2):
			lista_usuarios.append(un)
			lista_contrasenas.append(p1)
			def archivos():
				a = open("usuarios.txt","r")
				texto = a.readlines()
				a.close()
				a = open("usuarios.txt", "a")
				a.write("\n" + str(un))
				a.close()

				b = open("contrasenas.txt","r")
				texto2 = b.readlines()
				b.close()
				b = open("contrasenas.txt", "a")
				b.write("\n" + str(p1))
				b.close()

			archivos()
			return render_template('home.html')
		else:
			return render_template('denegado.html')
	return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)