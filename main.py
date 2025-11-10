from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

def validar_nota(valor, minimo=10, maximo=70):
    try:
        n = float(valor)
    except (ValueError, TypeError):
        return None
    if n < minimo or n > maximo:
        return None
    return n


def validar_asistencia(valor, minimo=0, maximo=100):
    try:
        a = float(valor)
    except (ValueError, TypeError):
        return None
    if a < minimo or a > maximo:
        return None
    return a


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    errores = []

    if request.method == 'POST':
        n1 = validar_nota(request.form.get('nota1'))
        n2 = validar_nota(request.form.get('nota2'))
        n3 = validar_nota(request.form.get('nota3'))
        asistencia = validar_asistencia(request.form.get('asistencia'))


        if n1 is None:
            errores.append("Nota 1 inválida. Debe ser número entre 10 y 70.")
        if n2 is None:
            errores.append("Nota 2 inválida. Debe ser número entre 10 y 70.")
        if n3 is None:
            errores.append("Nota 3 inválida. Debe ser número entre 10 y 70.")
        if asistencia is None:
            errores.append("Asistencia inválida. Debe ser número entre 0 y 100.")

        if not errores:
            promedio = (n1 + n2 + n3) / 3.0
            estado = "APROBADO" if (promedio >= 40 and asistencia >= 75) else "REPROBADO"
            resultado = {
                "nota1": n1,
                "nota2": n2,
                "nota3": n3,
                "promedio": round(promedio, 2),
                "asistencia": round(asistencia, 2),
                "estado": estado,
                "criterio": "Promedio >= 40 y asistencia >= 75%"
            }

    return render_template('ejercicio1.html', resultado=resultado, errores=errores)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    errores = []

    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()


        if not nombre1 or not nombre2 or not nombre3:
            errores.append("Debe ingresar los tres nombres.")
        elif len({nombre1.lower(), nombre2.lower(), nombre3.lower()}) < 3:
            errores.append("Los nombres deben ser diferentes.")

        if not errores:
            nombres = [nombre1, nombre2, nombre3]
            nombre_mas_largo = max(nombres, key=len)
            longitud = len(nombre_mas_largo)

            resultado = {
                "nombre_mas_largo": nombre_mas_largo,
                "longitud": longitud,
                "todos": nombres
            }

    return render_template('ejercicio2.html', resultado=resultado, errores=errores)

if __name__ == '__main__':
    app.run(debug=True)