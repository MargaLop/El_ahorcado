import random
# import string
from doc_palabras import lista_palabras
import vidas_representación_grafica




#el programa escoge una palabra al azar de nuestro archivo doc_palabras
def palabra_azar_ordenador(palabras):
        return random.choice(palabras)  

def ahorcado (palabras):
      
  palabra = palabra_azar_ordenador(palabras)

  vidas = 6
  while  vidas > 0:
    letra_ronda = input('Una letra:')
    print(f'LETRAS ESCOGIDAS:{letra_ronda}')


    if palabra.find(letra_ronda):  # https://www.delftstack.com/es/howto/python/position-of-character-in-string/
      pass
    else:
      print('Esta letra no se encuentra en la palabra')
      vidas -= 1



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
   
 #asci dibujos

