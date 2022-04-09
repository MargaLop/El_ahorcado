import random
import string
import time
from doc_palabras import lista_palabras
import vidas_representación_grafica
import dibujos_pinguino as dp


#el programa escoge una palabra al azar de nuestro archivo doc_palabras
def palabra_azar_ordenador(palabras):
        return random.choice(palabras)  

def progreso_palabra(letras_adivinadas,palabra):
  resultado = []
  for letra in palabra:
    if letra in letras_adivinadas:
      resultado.append(letra)
    else:
      resultado.append('-')
  
  return resultado


def ahorcado (palabra):
  # https://www.delftstack.com/es/howto/python/python-alphabet-list/  - abcdario

  letras_palabra = set(palabra)
  letras_abcdario = set(string.ascii_lowercase) #el abcedario esta en minusculas
  letras_adivinar = set()   #investigar que poner
  

  vidas = 7

  while len(letras_palabra) > 0 and  vidas > 0:
    print(palabra)

    grafica_palabra = progreso_palabra(letras_adivinar, palabra)
    print(dp.vidas_palabra(vidas,grafica_palabra))
    time.sleep(1)
    letra_ronda = input(dp.letra_usuario()). lower() #es necesario que sean minusculas
    print(f'''LETRAS ESCOGIDAS:{letra_ronda} ''')


    if letra_ronda in  letras_abcdario - letras_adivinar : #En caso de que el usuario introduzca caracteres distintos al abc

      letras_adivinar.add(letra_ronda)
       # https://www.delftstack.com/es/howto/python/position-of-character-in-string/       
      if palabra.find(letra_ronda) != -1: 
        letras_palabra.remove(letra_ronda)

      else:
        vidas -= 1
        print(dp.letra_incorrecta(vidas_representación_grafica.repre_vida[vidas]))
        time.sleep(1)

    elif letra_ronda in letras_adivinar:
      print(dp.ya_escogida(letras_adivinar))
      time.sleep(1)

    else:
      print(dp.no_letra())
      time.sleep(1)

  if vidas == 0:
    print(dp.ganar_perder(palabra,False))
  
  else:
    print(dp.ganar_perder(palabra,True))
    
  

if __name__ == '__main__':
  nombre_usuario = input(dp.nombre_usuario()).upper()
  print(dp.bienvenido(nombre_usuario))
  time.sleep(1)
   
ahorcado(palabra_azar_ordenador(lista_palabras))
