#import Stemmer
import json
import os
import nltk
from nltk.stem import PorterStemmer 
from nltk.stem import SnowballStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
#from nltk.stem import 	WordNetLemmatizer

#stemmer = Stemmer.Stemmer('spanish')


# Manejo de Archivos

Web_Scrap = open('scrapydoo.json')              #Abrir archivo JSON
Web_Scrap_data = json.loads(Web_Scrap.read())   #Crea un diccionario en base al JSON
Web_Scrap.close()                               #Cerrar archivo JSON'''


ignoreList= ["", ".", ";", "+", "-", "(", ")", ":" , "[", "]", "-", "<", ">", "_", "'", "?", "!","{", "}", "^", "+", "#", "$", "%", "&", "/", "*", '"', "«", "»"
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
             "el", 'de', "la", "las", "los", "para", "con", "a", "como" "por", "sin", "tras", "del"]
words = []

file = open("/home/ronaldo/Escritorio/BasesdeDatos2/Proyecto3/TextFiles/wordStemmingList.txt", "w")   #Crea el archivo txt donde se guardarán los valores

for data in Web_Scrap_data:#Limpieza de texto 
    #file2 = open("/home/ronaldo/Escritorio/BasesdeDatos2/Proyecto3/TextFiles/" + data["Title"][0] + ".txt", "w")   #Crea el archivo txt donde se guardarán los valores de cada página por separado                                            
    for textdata in data:
        for word in data[textdata]:    
            if word not in ignoreList : #data[textdata]
                token = (word_tokenize(word))                               #Hace un split, funciona igual que el método "split()" de python base
                if textdata != "Image-src-text":
                    words = [word for word in token if word.isalpha()]      #Elimina signos de puntuación
                    
                stopWords_eng = stopwords.words('english')                  #Define palabras vacías (En Inglés)
                words = [w for w in words if not w in stopWords_eng]        #Elimina palabras vacías''' 

                stopWords_esp = stopwords.words('spanish')                  #Define palabras vacías (En Español)
                words = [w for w in words if not w in stopWords_esp]        #Elimina palabras vacías
        
                '''porter = SnowballStemmer('english')
                stemmed = [porter.stem(word) for word in words]'''

                porter = SnowballStemmer('spanish')                         #Stemming de palabras, saca la raíz de la palabra
                stemmedWords = [porter.stem(word) for word in words]        #Nota: El Stemming no parece funcionar muy bien, probablemente se tenga que quitar o cambiar
                

                #wordnet_lemmatizer = WordNetLemmatizer()
                









                for word in stemmedWords:
                    #print("Lemma for {} is {}".format(word, wordnet_lemmatizer.lemmatize(word))) 
                    print("Escribiendo: " + textdata + ": " + word)
                    file.write(textdata + ": " + word + os.linesep) 
                    #file2.write(textdata + ": " + word + os.linesep) 
    

    #file.write("===========================\n")
    #file2.close() 

file.close()
#file2.close()