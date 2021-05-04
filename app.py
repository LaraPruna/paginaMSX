from flask import Flask, render_template, abort, request
import json, os

app = Flask(__name__)
with open("./MSX.json") as fichero:
		datos=json.load(fichero)

@app.route('/')
def inicio():
	return render_template("inicio.html")

@app.route('/juegos',methods=["GET","POST"])
def buscador():
	ind=False
	if request.method=="GET":
		return render_template("buscador.html")
	else:
		juego=request.form.get("juego")
		lista=[]
		if juego != None:
			for dato in datos:
				dic={}
				dic['nombre']=dato.get("nombre")
				dic['desarrollador']=dato.get("desarrollador")
				dic['id']=dato.get("id")
				lista.append(dic)
			return render_template("listajuegos.html",juego=juego,lista=lista,datos=datos)
		else:
			for dato in datos:
				if juego not in dato.get("nombre"):
					ind=True
			if ind:
				return render_template("listajuegos.html",juego=juego,lista=lista,datos=,error=True)
			else:
				return render_template("listajuegos.html",juego=juego,lista=lista,datos=datos)
		

@app.route('/juego/<int:identificador>')
def detalles(identificador):
	detalles={}
	ind=True
	for dato in datos:
		if identificador == dato.get("id"):
			detalles["nombre"]=dato.get("nombre")
			detalles["sistema"]=dato.get("sistema")
			detalles["distribuidor"]=dato.get("distribuidor")
			detalles["desarrollador"]=dato.get("desarrollador")
			detalles["categoria"]=dato.get("categoria")
			detalles["anno"]=dato.get("año")
			ind=False
	if ind:
		abort(404)
	return render_template("detalles.html",detalles=detalles)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=True)