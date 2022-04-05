import random
import string
from doc_palabras import lista_palabras
import vidas_representación_grafica




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
    print (f'TUS VIDAS SON[{vidas}]')
    grafica_palabra = progreso_palabra(letras_adivinar, palabra)
    # print(palabra)
    print(f"Palabra: {' '.join(grafica_palabra)}")
    letra_ronda = input('Escoge una letra:'). lower() #es necesario que sean minusculas
    print(f'LETRAS ESCOGIDAS:{letra_ronda}')

    if letra_ronda in  letras_abcdario - letras_adivinar : #En caso de que el usuario introduzca caracteres distintos al abc

      letras_adivinar.add(letra_ronda)
       # https://www.delftstack.com/es/howto/python/position-of-character-in-string/       
      if palabra.find(letra_ronda) != -1: 
        letras_palabra.remove(letra_ronda)

      else:
        print('Esta letra no se encuentra en la palabra')
        vidas -= 1
        print(vidas_representación_grafica.repre_vida[vidas]) #cada vida perdida muestra representación

    elif letra_ronda in letras_adivinar:
      print('Esta letra ya fue escogida anteriormente')

    else:
      print('No se encuentra dentro del abcedario.Intentelo de nuevo')


  if vidas == 0:
      print(f'''
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
                                   ______
                                .-"      "-.
                               /            \\
                              |              |
                              |,  .-.  .-.  ,|
                              | )(__/  \__)( |
                              |/     /\     \|
                              (_     ^^     _)
                               \__|IIIIII|__/
                                | \IIIIII/ |
                                \          /
                                 `--------`
                    
                                 GAME OVER
                         La palabra era {palabra}
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
        ''')
    
  else:
      print(f'''
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
                                  .-=========-.
                                  \\'-=======-'/
                                  _|   .=.   |_
                                 ((|  ((1))  |))
                                  \|   /|\   |/
                                   \__ '`' __/
                                     _`) (`_
                                   _/_______\_
                                  /___________\\

                                ¡¡ENHORABUENA!! 
                          La palabra era {palabra}
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'

      ''')
     










if __name__ == '__main__':
    nombre_usuario = input('¿Cuál es su nombre?:')
    print (f'''
     .-.     .-.     .-.     .-.     .-.     .-.     .-.
`._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
         Bienvenido {nombre_usuario} al Ahorcado
     .-.     .-.     .-.     .-.     .-.     .-.     .-.
`._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
''')
   
ahorcado(palabra_azar_ordenador(lista_palabras))
   

         
        






  
