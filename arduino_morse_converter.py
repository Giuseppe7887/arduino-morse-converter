from machine import Pin
from time import sleep_ms as sleep


PIN_ID = 6
INITIAL_PHRASE = """
# initial signal = 2 seconds ON + 2 seconds OFF
# short signal duration = 100 ms
# long signal duration = 600 ms
# space between signals duration = 300 ms
# space between words duration = 800 ms
digit a word or a sentence
"""
SHORT_PIN_DURATION =100 #ms
LONG_PIN_DURATION =600 #ms
SPACE_DURATION = 800 #ms
INTERSPACE_DURATION = 300 #ms


led = Pin(PIN_ID,Pin.OUT)
led.off()

corr= {
    "a":"01",
    "b":"1000",
    "c":"1010",
    "d":"100",
    "e":"0",
    "f":"0010",
    "g":"110",
    "h":"0000",
    "i":"00",
    "j":"0111",
    "k":"101",
    "l":"0100",
    "m":"11",
    "n":"10",
    "o":"111",
    "p":"0110",
    "q":"1101",
    "r":"010",
    "s":"000",
    "t":"1",
    "u":"001",
    "v":"0001",
    "w":"011",
    "x":"1001",
    "y":"1011",
    "z":"1100",
    "1":"01111",
    "2":"00111",
    "3":"00011",
    "4":"00001",
    "5":"00000",
    "6":"10000",
    "7":"11000",
    "8":"11100",
    "9":"11110",
    "0":"11111"
}


def short_pin():
    print("short")
    led.on()
    sleep(SHORT_PIN_DURATION)
    led.off()
    

def long_pin():
    print("long")
    led.on()
    sleep(LONG_PIN_DURATION)
    led.off()

def space():
    print("space")
    sleep(SPACE_DURATION)

def interspace():
    print('interspace')
    sleep(INTERSPACE_DURATION)

def start_translation_pin():
    led.on()
    sleep(2000)
    led.off()
    sleep(2000)
    print("start translation")

def Start():
    def to_morse(x):
        start_translation_pin()
        i=0
        while i < len(x):
            if str(x[i]) == " ":
                space()
            else:
                for index,bit in enumerate(corr[x[i]]):
                    if int(bit) == 1:
                        long_pin()
                    else:
                        short_pin()
                    
                    interspace()
                    
            i+=1
                
                
            
                
    phrase = input(f"{INITIAL_PHRASE}: ")

    if phrase:
        to_morse(phrase)
    else:
        print("word/sentence is required")
    
    led.off()
    
while True:Start()