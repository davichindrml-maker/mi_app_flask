from flask import Flask, render_template, request
import pandas as pd
import os

# Inicializar Flask
app = Flask(_name_)

# Base de datos 
dic= {
    "usuario": ["claulopez", "Jacksoooon","Phdian", "Choco_Marii", "nadiashit","berenice", "pedrinho","davidlima","Esqueyosoyasi"],
    "contraseña": ["umpalumpa","moonwenee","Mimamimi","Ingatumais","vetealv","amoamifamilia","pecj","soydaviddd","DCOPN"]
}
usuarios=pd.DataFrame(data=dic)
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
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Toma el puerto que Render le indique
    app.run(host="0.0.0.0", port=port)

