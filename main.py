import random
import string
from doc_palabras import lista_palabras
import vidas_representación_grafica




#el programa escoge una palabra al azar de nuestro archivo doc_palabras
def palabra_azar_ordenador(palabras):
        return random.choice(palabras)  

def ahorcado (palabras):
  # https://www.delftstack.com/es/howto/python/python-alphabet-list/  - abcdario
  #   
  palabra = palabra_azar_ordenador(palabras)
  letras_palabra = set(palabra)
  letras_abcdario = set(string.ascii_lowercase)
  letras_adivinar = letras_palabra  #investigar que poner

  vidas = 7
  while len(letras_adivinar) > 0 and  vidas > 0:
    print (f'TUS VIDAS SON[{vidas}]')
    letra_ronda = input('Escoge una letra:')
    print(f'LETRAS ESCOGIDAS:{letra_ronda}')
    if letra_ronda in  letras_abcdario: #En caso de que el usuario introduzca caracteres distintos al abc

      if palabra.find(letra_ronda):  # https://www.delftstack.com/es/howto/python/position-of-character-in-string/
        posicion = palabra.find(letra_ronda)
        letra_nv = palabra[posicion]   #saca la letra
        letras_adivinar.remove(letras_palabra)

        # letras_adivinar == '_'

      else:
        print('Esta letra no se encuentra en la palabra')
        vidas -= 1
        print(vidas_representación_grafica.repre_vida[vidas]) #cada vida perdida muestra representación

    else:
      print('No se encuentra dentro del abcedario.Intentelo de nuevo')


    if vidas == 0:
      print(f'''
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
                                   ______
                                .-"      "-.
                               /            \
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
                                  \'-=======-'/
                                  _|   .=.   |_
                                 ((|  ((1))  |))
                                  \|   /|\   |/
                                   \__ '`' __/
                                     _`) (`_
                                   _/_______\_
                                  /___________\

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
    ahorcado()
   

