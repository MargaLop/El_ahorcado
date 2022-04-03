from itertools import permutations
import string

#prueba find
palabra = 'perro'
letra_ronda = '3'
letras_abcdario = set(string.ascii_lowercase)
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


print('===============================================')

#en caso introducir caracteres que no se encuentren en el abcedario
vidas = 3
while vidas > 0:
    letra_usuario =input('letra:')
    if letra_usuario in  letras_abcdario:
        print('OK')
    else:
        print('no')
        vidas -= 1

print('adios')