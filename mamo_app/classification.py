def Distinct(img_path):
    import tensorflow as tf
    from tensorflow.lite.python.interpreter import Interpreter
    #from tensorflow.lite.python.tflite_convert import from_saved_model
    from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
    from PIL import Image
    import numpy as np
    import os
    from random import choice


    #print(tf.version)
    # Charger le modèle TensorFlow Lite
    model_path = os.path.join(os.getcwd(),"mamo_app\\breast.tflite")
    #part_path=model_path.split("\\")
    #model_path="/".join(part_path)
    #print("---------------"+model_path+"---------------------")
    if os.path.exists(model_path):
        print("Le fichier existe")
    else:
        print("Le fichier n'existe pas.")

    interpreter = Interpreter(model_path)
    interpreter.allocate_tensors()

    # Charger l'image à tester
    #img_path = "/static/images/1.png"

    # Redimensionner l'image à une taille fixe (224x224)
    img = Image.open(img_path)
    img = img.resize((640,640))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    #conversion de l'image condé en unit8 en float32
    #img_array=tf.convert_to_tensor(img_array,dtype=tf.float32)
    img_array = preprocess_input(img_array)


    # Faire une prédiction
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])
    formule=[["Félicitation,vous n'avez rien","Dieu soit loué,le test est négatif","Vous êtes à l'abri de tout danger","Vous avez une mammographie normale"],
             ["Vous n'êtes encore qu'au début,toutes les chances sont encore de votre côté",
              "le mal n'a pas encore atteint un stade sévère","Votre mammographie montre que vous êtes à un niveau bénigne",
             "Vous êtes à un niveau bénigne,une masse est présente dans votre sein,mais les chances qu'elle deviennet une tumeur maligne ne sont pas nulles.Nous allons vous garder en observation afin de suivre l'évolution de celle-ci."],
             ["J'ai le regret de vous annoncer que vous avez une tumeur maligne,qui pourrait bien s'aggraver encore et impacter négativement votre santé.","Vous avez une tumeur malign","Votre mamographie montre des masses qui se sont développés à un stade significatif,j'ai le regret de vous anoncer que vous êtes atteint du cancer du sein"]]
    # Afficher la classe prédite
    list_proba=predictions[0]
    #print(list_proba)
    #print("max",max(list_proba))
    saying=""
    if max(list_proba)<0.50:
        saying=choice(formule[0])
    else:
        predicted_class = np.argmax(predictions)
        #print(predicted_class)
        #classes=['benign','malignant']
        #pred=classes[predicted_class]
        if predicted_class==0:
            saying=choice(formule[1])
        else:
            saying=choice(formule[2])

        return saying
        #print( predictions)

Distinct("static/images/1.png")
