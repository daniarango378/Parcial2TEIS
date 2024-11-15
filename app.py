from flask import Flask, render_template

app = Flask(__name__)

# Función para calcular el factorial
def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

# Ruta principal para la aplicación
@app.route('/<int:numero>')
def factorial(numero):
    resultado = calcular_factorial(numero)
    return render_template('result.html', numero=numero, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
