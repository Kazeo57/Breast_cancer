from flask import Flask,request,render_template
from PIL import Image 
from io import BytesIO
from classification import Distinct

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/diagnostic/',methods=["GET","POST"])
def diagnostic():
    end=""
    saying=""
    if request.method=='POST':
        if 'file' not in request.files:
            print('Aucun fichier trouvé')
            return 'Aucun fichier trouvé'
        file=request.files['file']
        print(file)
        if file.filename=='':
            print('Aucun fichier sélectionné')
            return 'Aucun fichier sélectionné'
        
        #Accéder aux données binaires de l'image
        image_data=file.read()

        #Utiliser Pillow pour ouvrir l'image depuis les données binaires
        image=Image.open(BytesIO(image_data))
        image.save("static/images/1.png")
        saying=Distinct("static/images/1.png")
        print("Bla Bla bla")
        end="success"
        #return render_template("sucess.html")

    return render_template("diagnostic.html",end=end,saying=saying)

#Ctrl+Shift+R pour vider la cache du navigateur si les modifications css ne sont pas mises à jour
"""
def upload
 """
if __name__=='__main__':
    app.run(debug=True)


