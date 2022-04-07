import random
import string
import time
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
    # print(palabra)

    grafica_palabra = progreso_palabra(letras_adivinar, palabra)


    print(f'''
    
         .-.     .-.     .-.     .-.     .-.     .-.     .-.
    `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'

                              __________________________________________
                             /                                          \\
                            |    TUS VIDAS SON[{vidas}]                        |
                            |                                            |
             . --- .        |   'PALABRA: {' '.join(grafica_palabra)}")    
           /        \\        ___________________________________________/                          
          |  O  _  O |      /
          |  ./   \. |
          /  `-._.-'  \\
        .' /         \ `. ''')

    time.sleep(1)
    letra_ronda = input(''' 
  
                                ________________________________________
                            /                                           \\
             . --- .        |             ESCOGE UNA LETRA               |   
           /        \\        ___________________________________________/                          
          |  O  _  O |      /
          |  ./   \. |
          /  `-._.-'  \\
        .' /         \ `. 
        
    TU LETRA:'''). lower() #es necesario que sean minusculas

    print(f'''LETRAS ESCOGIDAS:{letra_ronda} ''')

    if letra_ronda in  letras_abcdario - letras_adivinar : #En caso de que el usuario introduzca caracteres distintos al abc

      letras_adivinar.add(letra_ronda)
       # https://www.delftstack.com/es/howto/python/position-of-character-in-string/       
      if palabra.find(letra_ronda) != -1: 
        letras_palabra.remove(letra_ronda)

      else:
        vidas -= 1
        print(f'''
                               _________________________________________________________
                             /                                                           \\
                            |    ESTA LETRA NO ESTA EN LA PALABRA. ME VAS A MATAR        |
                            |                                                            |
                            |    {vidas_representación_grafica.repre_vida[vidas]}                                                      
             . --- .        |                                                            |
           /  \   /  \\        __________________________________________________________/                          
          |  O  _  O |      /
          |  ./   \. |
          /  `-._.-'  \\
        .' /         \ `. 
        ''')
        time.sleep(1)

    elif letra_ronda in letras_adivinar:
      print(f'''
                                _________________________________________
                             /                                            \\
                            |   ESTA LETRA YA FUE ESCOGIDA ANTERIORMENTE  |
                            |   LAS LETRAS QUE YA ESCOGISTE SON:          |
             . --- .        |   {letras_adivinar}                          
           /  \   /  \\        ___________________________________________/                          
          |  O  _  O |      /
          |  ./   \. |
          /  `-._.-'  \\
        .' /         \ `. ''')
      time.sleep(1)

    else:

      print(f'''

                             _________________________________________
                           /                                          \\
           . --- .         |   ESTO NO ES UNA LETRAAAAAA!!!!!!!!       |                
         /  \   /  \\        __________________________________________/                          
        |  O  _  O |      /
        |  ./   \. |
        /  `-._.-'  \\
      .' /         \ `. ''')
    
      time.sleep(1)



  if vidas == 0:
      print(f'''
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'

                              ____________________
                            /                      \\
                            |    POR TU CULPA,     |
                            |   LLEGO EL DIA DE MI |
                            |        MUERTE        |
                            |    La palabra era    |
             . --- .        |    {palabra}
           /        \\        _____________________/                          
          |  ()  ()  |     /
          |     ^    |
          /   |||||  \\       
        .' /  |||||  \ `.        
    .-~.-~/           \~-.~-.      
.-~ ~    |             |    ~ ~-. 
`- .     |             |     . -'  
     ~ - |             | - ~     
         \             /             
       ___\           /___         
       ~;_  >- . . -<  _i~                       

                                  
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
        ''')
    
  else:
      print(f'''
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
                              ____________________
                            /                      \\
                            |    ¡¡ENHORABUENA!!   |
                            |    La palabra era    |
             . --- .        |    {palabra}
           /        \\        _____________________/                          
          |  O  _  O |      /
          |  ./   \. |
          /  `-._.-'  \\            .-=========-.
        .' /         \ `.          \\'-=======-'/
    .-~.-~/           \~-.~-.      _|   .=.   |_
.-~ ~    |             |    ~ ~-. ((|  ((1))  |))
`- .     |             |     . -'  \|   /|\   |/
     ~ - |             | - ~        \__ '`' __/
         \             /              _`) (`_
       ___\           /___          _/_______\_
       ~;_  >- . . -<  _i~         /___________\\             
             .-.     .-.     .-.     .-.     .-.     .-.     .-.
        `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'

      ''')
     










if __name__ == '__main__':
    nombre_usuario = input('''
                              ____________________
                            /                      \\
             . --- .        | ¿Cuál es su nombre?: |   
           /        \\        _____________________/                          
          |  O  _  O |      /
          |  ./   \. |
          /  `-._.-'  \\
        .' /         \ `.
    .-~.-~/           \~-.~-.
.-~ ~    |             |    ~ ~-.
`- .     |             |     . -'
     ~ - |             | - ~
         \             /
       ___\           /___
       ~;_  >- . . -<  _i~
       

    NOMBRE:   
    ''')


    print (f'''

     .-.     .-.     .-.     .-.     .-.     .-.     .-.
`._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'
                              ____________________
                            /                      \\
                            |      Bienvenido      |
                            |        {nombre_usuario} 
             . --- .        |      al Ahorcado     |   
           /        \\        _____________________/                          
          |  O  _  O |      /
          |  ./   \. |
          /  `-._.-'  \\
        .' /         \ `.
    .-~.-~/           \~-.~-.
.-~ ~    |             |    ~ ~-.
`- .     |             |     . -'
     ~ - |             | - ~
         \             /
       ___\           /___
       ~;_  >- . . -<  _i~
       
''')
time.sleep(1)
   
ahorcado(palabra_azar_ordenador(lista_palabras))
   

         
        






  
