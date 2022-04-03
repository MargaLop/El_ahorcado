from itertools import permutations
import string

#prueba find
palabra = 'perro'
letra_ronda = 'r'
if palabra.find(letra_ronda):  # https://www.delftstack.com/es/howto/python/position-of-character-in-string/
  posicion = palabra.find(letra_ronda)
  letra_nv = palabra[posicion]
  print(posicion) #funciona pero solo muestra la primera
  print(letra_nv)

  print('===============================================')

  #pruebas set
  lestras_palabra = set(palabra)
  letras_abcdario = set(string.ascii_lowercase)
  letras_adivinar = ''


  print (lestras_palabra)
  print(letras_abcdario)

  print('===============================================')

else:
    print('esta letra no se encuentra')

