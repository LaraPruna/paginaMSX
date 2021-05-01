from flask import Flask, render_template, abort, request
import json, os

app = Flask(__name__)
with open("./MSX.json") as fichero:
		datos=json.load(fichero)

@app.route('/')
def inicio():
	return render_template("inicio.html")

@app.route('/juegos')
def buscador():
	return render_template("buscador.html")	

@app.route('/listajuegos', methods=["POST"])
def listajuegos():
	juego=request.form.get("juego")
	if juego != None:
		lista=[]
		for dato in datos:
			dic={}
			dic['nombre']=dato.get("nombre")
			dic['desarrollador']=dato.get("desarrollador")
			dic['id']=dato.get("id")
			lista.append(dic)
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