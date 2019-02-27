# Erika3004

## Encoding

The Erika3004 Typewriter uses a proprietary encoding NOT compatible with ASCII, Unicode, etc.  
Therefore, software is needed to convert the RAW encoding (or DDR ASCII (GDR ASCII) as we call it ;) ) 
into something more useful (by modern standands) like ASCII.

A table of all available characters and their hexadecimal value can be found in this 
manual( [Erika-IF2014_AnwenderHandbuch](Erika-IF2014_AnwenderHandbuch.pdf) ) as Appendix E on page 10.    
It also has a list of the most used controll characters on page 11 (Appendix F).  
A complete list can be found [here](http://hc-ddr.hucki.net/wiki/doku.php/z9001/erweiterungen/s3004).  

We implemented the conversion in python using a json-file which contains all characters and their hexadecimal values.  
Find it in the `erika` directory (that name was chosen because python module names are based on directory names). 
  
The implementation for Arduino uses hard-coded arrays instead.  
Find it in the `arduino` directory. 

## Hardware

Description of the Erica connector:  
![Erika Connector](http://hc-ddr.hucki.net/wiki/lib/exe/fetch.php/z9001/erweiterungen/s3004_anschluss.jpg?cache=)

More information can be found here (German):  
[http://hc-ddr.hucki.net/wiki/doku.php/z9001/erweiterungen/s3004](http://hc-ddr.hucki.net/wiki/doku.php/z9001/erweiterungen/s3004)

A schematic of our Arduino based interface can be found [on EasyEDA](https://easyeda.com/sirexeclp/erikaarduinointerface).
![Schematic](docs/Schematic_ErikaArduinoInterface.png)

## Software

### Arduino Sketch

Located in `arduino` directory.

The arduino sketch should be compilable for any Arduino that has at least one hardware 
[UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter) (hardware serial).  
TODO: Test on Mini, Nano

The arduino will communicate with your PC using the default hardware serial, which is usually connected to a 
USB-to-serial converter.  
It will use a software serial to communicate with the Erika3004.  
More information about SoftwareSerial can be found on the 
[Arduino-Website](https://www.arduino.cc/en/Reference/SoftwareSerial).
In `erika.ino`, you can set the following constants:

> Remember: Serial connections are connected with cross-over. This means RX on the Arduino connects to TX on the Erika and vice versa.

|Name|Description|Default Value|Comment|
|----|-----------|-------------|-------|
|PC_BAUD| Baudrate used to communicate with the pc|9600|You can change this to fit your needs.|
|RTS_PIN| Pin that is connected to the ready to send pin of the Erika.|3|You can change this to any available digital input pin on your arduino.|
|ERIKA_RX| Recieve pin of the SoftwareSerial to communicate with Erika.|10|Check the limitations section on the  [Arduino-Website](https://www.arduino.cc/en/Reference/SoftwareSerial), to find out which pins can be used by SoftwareSerial.|
|ERIKA_TX| Transmit pin of the SoftwareSerial to communicate with Erika.|11|Check the limitations section on the  [Arduino-Website](https://www.arduino.cc/en/Reference/SoftwareSerial), to find out which pins can be used by SoftwareSerial.|
|ERIKA_BAUD| Baudrate used by the Erika3004.|1200|DON'T CHANGE THIS! The Erika3004 will only work with 1200 Baud!|

Translation from ASCII to DDR-ASCII is done using arrays defined in `ddr2ascii.h` and `ascii2ddr.h`.  

Let's build a secret chat system using 2 of these. :)


## Installation 

### Install python3
```
sudo apt-get install python3
```

### Install pip package manager for python
```
sudo apt-get install python3-pip
```

### Install necessary packages
```
pip3 install -r requirements.txt
```


## ASCII art

### Create ASCII art for printout

* install Imagemagick's convert tool
```
sudo apt install imagemagick 
```
* install jp2a
```
sudo apt install jp2a
```
* convert png files on the command line like this: 
  * leave one dimension unspecified to keep teh original ratio
```
convert ubuntu-logo32.png jpg:- | jp2a - --width=80 --height=80
```

### Print ASCII art programmatically 

TODO 

* Rendering strategies:
  * LineByLine
    * render the given image line by line 
  * Interlaced 
    * render the given image, every even line first (starting count at 0), every odd line later
  * PerpendicularSpiralOutward (TODO)
    * render the given image, spiralling outward from the middle while going parallel to X or Y axis all the time
  * PerpendicularSpiralInward (TODO)
    * render the given image, spiralling inward to the middle while going parallel to X or Y axis all the time
  * RandomDotFill (TODO)
    * render the given image, printing one random letter at a time
  * NaturalSpiralOutward (TODO)
    * render the given image, starting from the middle, following as close a natural spiral as possible
  * NaturalSpiralInward (TODO)
    * render the given image, towards the middle, following as close a natural spiral as possible


## Testing

### Run unit tests

For now, call this in bash: 
```
./run_unittests.sh
```


### Run integration tests

For now, call this in bash: 
```
./run_integrationtests.sh
```
