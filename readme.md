# Uso del programa. 

## Abrir una terminal

1.- Una vez abierta la termianl usa el comando: docker-compose up.

* Esto hara que se levante nuestro servidor en docker

2.- Una vez inicializado el docker podremos acceder desde un navegador al localhost:5000

3.- En el navegaro con la ruta anteriormente dada podremos acceder al programa y tendremos que subir un archivo .mp3

4.- Una vez subido el archivo .mp3 podremos ve un mensaje que indica que su fragmento el archivo correctamente

5.- En el mismo navegador podremos acceder a los diferentes fragmentos usando la siguiten liga localhost:5000/fragment/0, para solicitar las diferente partes del audio podemos cambiar el numero que aparece al final de la liga hasta un total de 9 

6.- En caso de querer acceder al audio recontruido usaremos la liga de localhost:5000/ensamblar/ esta nos redigira a el audio ya reconstruido.