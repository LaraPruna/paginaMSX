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
	ind=True
	juego=request.form.get("juego")
	lista=[]
	for dato in datos:
		if dato.get("categoria") not in lista:
			lista.append(dato.get("categoria"))
	categorias=[]
	for cat in lista:
		dic={}
		dic['valor']=lista.index(cat)+1
		dic['texto']=cat
		categorias.append(dic)
	if request.method=="GET":
		return render_template("buscador.html",categorias=categorias,datos=datos)
	else:
		so=request.form.get("categoria")
		for dato in datos:
			if juego in dato.get('nombre'):
				for cat in categorias:
					if dato.get("categoria")==cat.get('texto') and int(so)==cat.get('valor'):
						ind=False
		if ind:
			return render_template("buscador.html",juego=juego,datos=datos,seleccionado=int(so),categorias=categorias,error=True)
		else:
			return render_template("listajuegos.html",juego=juego,categorias=categorias,seleccionado=int(so),datos=datos)

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