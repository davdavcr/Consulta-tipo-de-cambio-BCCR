from flask import request, render_template, current_app as app
from logicaNegocio import logicaNegocio

logica_negocio = logicaNegocio()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    fecha = request.form['fecha']
    try:
        tipo_cambio = logica_negocio.obtener_tipo_cambio(fecha)
        return render_template('result.html', fecha=fecha, tipo_cambio=tipo_cambio)

    except Exception as ex:
        return render_template('error.html', error=str(ex))

