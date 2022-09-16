import random
class Cuestionador:

    def __init__(self):
    
        self.questions= [
            "¿que es el almicantarat?",
            "¿donde se encuentra el zenit?",
            "¿cuántos órdemes ecisten en la taxonimia de suelos?"
        ]
        self.answers=  [
            "circulo imaginario en esfera celeste",
            "90 grados respecto al horizonte",
            "12"
        ]

    def jugar (self):
        #genrar un numero aleatorio entre 0 y n-1, siendo n el tamaño de la lista de preguntas 
        n=len(self.questions)
        number= random.randint(0, n-1)
        print(self.questions[number])
        #Solicitar la respuesta al usuario
        respuesta= input ("¿cual es tu respuesta?")
        #Verificar si la respuesta es correcta

        if respuesta == self.answers[number]:
            print("eres genial")
        else:
            print ("perdio")