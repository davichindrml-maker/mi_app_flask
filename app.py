from flask import Flask, render_template, request
import pandas as pd

# Inicializar Flask
app = Flask(__name__)

# Base de datos 
usuarios = pd.read_csv("C:/Users/davic/Mensajes/Usuarios.csv",index_col=0)
@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        user = request.form['usuario']
        password = request.form['contraseña']
        
        # Verificamos si existe el usuario y contraseña
        validacion = usuarios[
            (usuarios['usuario'] == user) & 
            (usuarios['contraseña'] == password)
        ]
        
        if not validacion.empty:
            mensaje = f"✅ Bienvenido, {user.title()}!"
        else:
            mensaje = "❌ Usuario o contraseña incorrectos"
    
    return render_template('login.html', mensaje=mensaje)

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
