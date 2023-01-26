## Ah 

Este programa utiliza el micrófono de la laptop para reconocer cuando se pronuncia la palabra “macri" y luego reproduce el sonido de un felino maullando, cambiando la imagen en la ventana de un gato en estado de tranquilidad al de uno alterado.

![Ah... pero](https://i.postimg.cc/JzChbB3C/Captura-de-pantalla-2023-01-26-09-17-06.png)

La idea es poner en evidencia esta clara y burda intención de construir a un enemigo para aglutinar en él la causa de todos los males que aquejan a la sociedad. Transformándolo en una situación graciosa.
Además de incorporar un contador con el fin de acentuar la cantidad de veces que se ha intentado realizar dicha acción.
--------------------------------------------------------------------------------

## requisitos:

Este programa utiliza SpeechRecognition con Google Speech Recognition por lo que necesita estar conectado a Internet para que funcione el reconocimiento de voz, así mismo se recomienda ejecutarlo en una laptop y no en una PC de escritorio ya que las primeras traen incorporado un micrófono que es necesario para que el programa pueda reconocer el audio. 
Gracias Google Speech Recognition este programa se puede correr en computadoras medianamente antiguas y / o de bajos recursos

* Conexión a Internet: si
* Micrófono activado y configurado: si

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
    • pyaudio
     
para agregar las dependencias utilise:

    pip install -r requirements.txt

## garantía:

No se ofrece ningún tipo de garantía

## licencia:

Este programa se publica bajo la licencia de software libre GPLv3 (https://www.gnu.org/licenses/gpl-3.0.txt)
