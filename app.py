# proyecto flask 
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html" , title="inicio")

@app.route('/usuario/<nombre>')  
def usuario(nombre):
    return f"hola,{nombre}¡ "

@app.route('/acerca')    
def acerca():
    return render_template("about.html" , title="acerca de")

@app.route('/contactos')    
def about():
     return "n000s" 
if __name__=='__main__':
    app.run(debug=True)
