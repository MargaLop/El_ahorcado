import random
import string
from doc_palabras import lista_palabras





def palabra_azar_ordenador(palabras):
        return random.choice(palabras)  #el programa escoge una palabra al azar de nuestro archivo doc_palabras


def ahorcado (palabras):
      
    palabra = palabra_azar_ordenador(palabras)

    vidas = 7
    while  vidas > 0:

    




















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
   
 #asci dibujos

'''
   +---+
   |   |
       |
       |
       |
       |
 =========

   +---+
   |   |
   O   |
       |
       |
       |
 =========

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========


  +---+

   |   |

   O   |

  /|\  |

  / \  |

       |
========='''