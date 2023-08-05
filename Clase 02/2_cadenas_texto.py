print("Hola mundo")

cadenamultiple = """
Por favor ingresa una frase este
programa cuenta el numero de palabras
que tiene una frase
"""

print(cadenamultiple)

text = input ("Ingresa la frase : ")

# pyton es maravilloso y versatil

#print(len(text)) 

count_text = len (text)

#"remplaza texto o caracter por otro dentro del texto "

text_replace = text.replace(" ","")
count_text_replace =len(text_replace)
        
print(count_text)
print(count_text_replace)
# print(len(text_replace))

espace = count_text - count_text_replace
print(f"La frase que ingresaste tiene {espace+1} palabras")
