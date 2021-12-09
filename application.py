from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tareas = [{"id":1, "materia":"fisica", "descripcion":"Hacer modelo unificado", "avance":90, "fecha":"24/12/2021"}]
@app.route("/tareas")
def index():
    return render_template("tareas.html", tareas = tareas)

@app.route("/tarea/<int:id>")
def detalle(id):
    for tarea in tareas:
        if tarea['id'] == id:
            return render_template("tarea.html", tarea = tarea)
    return render_template("error.html", mensaje = f"La tarea con el id {id} no existe.")

@app.route("/crear", methods = ["GET", "POST"])
def crear():
    if request.method == "GET":
        return render_template("crear.html")
    else:
        materia = request.form["materia"]
        descripcion = request.form['descripcion']
        avance = float(request.form['avance'])
        fecha = request.form['fecha']
        id = obtenerIdSiguiente()
        nuevaTarea = {"materia":materia, "descripcion":descripcion, "avance":avance, "id":id, "fecha":fecha}
        tareas.append(nuevaTarea)
        return redirect("/tareas")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    # Se busca la tarea que se desea cambiar
    tareaAModif = None
    for tarea in tareas:
        if tarea['id'] == id:
            tareaAModif = tarea
            break
    if tareaAModif is not None:
        if request.method == "GET":
            return render_template("update.html", tarea = tareaAModif)
        else:
            for tarea in tareas:
                if tarea['id'] == id:
                    tarea['materia'] = request.form['materia']
                    tarea['descripcion'] = request.form['descripcion']
                    tarea['avance'] = request.form['avance']
                    tarea['fecha'] = request.form['fecha']
                    break
            return redirect('/tareas')
    else:
        return render_template("error.html", mensaje = "La tarea a modificar no existe")

def obtenerIdSiguiente():
    #crear una variable que guarde
    # el máximo id visto

    #iterar sobre las tareas
    #guardar el id máximo en la variable
    idMax = -1
    for tarea in tareas:
        if tarea["id"] > idMax:
            idMax = tarea["id"]
    return idMax + 1