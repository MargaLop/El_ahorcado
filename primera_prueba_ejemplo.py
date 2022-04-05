'''
from itertools import permutations
import string
from tkinter import W

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

print('===============================================')

#minusuclas
palabra = input ('palabra:'). lower()
    
print(palabra)
'''
print('===============================================')
palabra ='oso'
letra_ronda = 's'
if palabra.find(letra_ronda):
    print('ok')
else:
    print('not')
print('===============================================')
import string

palabra = 'salon'
letras_abcdario = set(string.ascii_lowercase) #el abcedario esta en minusculas
letras_adivinadas =0
letras_adivinar = palabra - letras_adivinadas #investigar que poner

letra_ronda ='r'
vidas = 7
while len(letras_adivinar) > 0 and  vidas > 0:
  grafica_palabra = [letra if letra in letras_adivinar else '-' for letra in palabra]
  print(grafica_palabra)
  print (f'TUS VIDAS SON[{vidas}]')
  letra_ronda = input('Escoge una letra:'). lower() #es necesario que sean minusculas
  print(f'LETRAS ESCOGIDAS:{letra_ronda}')


    if letra_ronda in  letras_abcdario - letras_adivinar :

        if palabra.find(letra_ronda):  # https://www.delftstack.com/es/howto/python/position-of-character-in-string/         
          letras_adivinar.add(letra_ronda)
        else:
         print('Esta letra no se encuentra en la palabra')
         vidas -= 1

    elif letra_ronda in letras_adivinar:
      print('Esta letra ya fue escogida anteriormente')
    else:
      print('No se encuentra dentro del abcedario.Intentelo de nuevo')
