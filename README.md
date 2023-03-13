## Ah 

Este software emplea el micrófono de la laptop para reconocer cuando se pronuncia la palabra “Macri" y luego reproduce el sonido de un felino maullando, cambiando la imagen en la ventana de un gato en estado de tranquilidad al de uno alterado.

![Ah... pero](https://i.postimg.cc/JzChbB3C/Captura-de-pantalla-2023-01-26-09-17-06.png)

La idea es poner en evidencia la intención de construir a un enemigo para aglutinar en él la causa de todos los males y transformalo en una situación graciosa.
Además se incorpora un contador para dejar constancia de la cantidad de veces que se ha realizado dicha acción.
--------------------------------------------------------------------------------


## requisitos:

Este programa utiliza SpeechRecognition con Google Speech Recognition por lo que necesita estar conectado a Internet para que funcione el reconocimiento de voz, así mismo se recomienda ejecutarlo en una laptop y no en una PC de escritorio ya que las primeras traen incorporado un micrófono que es necesario para que el programa pueda reconocer el audio. 
Gracias Google Speech Recognition este programa se puede correr en computadoras medianamente antiguas y / o de bajos recursos

* Conexión a Internet: si
* Micrófono activado y configurado: si

--------------------------------------------------------------------------------

## Efectividad: 
El reconocimiento de la palabra clave no va a ser del 100% ya que depende de factores como: 
* la calidad del micrófono, 
* el alcance del mismo, 
* el ruido ambiente, 
* la pronunciación del emisor, 
* etc. 

Así mismo, la primera vez que se ejecuta el programa, puede que tarde un tiempo mayor a lo habitual en realizar el reconocimiento.

## informacón técnica:

Este script fue realizado en el lenguaje de programación python3

## dependencias:
    • sys
    • threading
    • time
    • tkinter 
    • queue
    • random
    • speech_recognition  
    • playsound
     
para agregar las dependencias utilise:

    pip install -r requirements.txt

* playsound==1.2.2 para windows

## garantía:

No se ofrece ningún tipo de garantía

## licencia:

Este programa se publica bajo la licencia de software libre GPLv3 (https://www.gnu.org/licenses/gpl-3.0.txt)
