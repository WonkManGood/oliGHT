'''
...
'''

class lightArray():
    '''
    Matrix-like wrapper for neopixel compatable lights on a ESP12F.
    
    oLIGHT: Neopixel wrapper for a DIY matrix on ESP boards.\n
    Copyright (C) 2025 WonkManBad (Ezra J.)
    '''
    
    ...
    def __init__(self, pin, led_count) -> None:
        from machine import Pin
        from neopixel import NeoPixel
        from time import sleep

        self.pin = Pin(pin, Pin.OUT)
        self.led_count = led_count
        self.neopixel = NeoPixel(self.pin, self.led_count, 3, 1)
        
        self.toggle_pin = Pin(0, Pin.IN, Pin.PULL_UP)
        
        '''
        lights:
        [ ] [3]  [7]  [11] [15] [19]
        [0] [4]  [8]  [12] [16] [20]
        [1] [5]  [9]  [13] [17] [21]
        [2] [6]  [10] [14] [18] [22]
        '''
        
        self.category = {
            'rows': {
                'h': {
                    1: [3, 7, 11, 15, 19],
                    2: [0, 4, 8, 12, 16, 20],
                    3: [1, 5, 9, 13, 17, 21],
                    4: [2, 6, 10, 14, 18, 22],
                },
                'v': {
                    1: [0, 1, 2],
                    2: [3, 4, 5, 6],
                    3: [7, 8, 9, 10],
                    4: [11, 12, 13, 14],
                    5: [15, 16, 17, 18],
                    6: [19, 20, 21, 22]
                    },
                45: {
                    1: [3, 0],
                    2: [7, 4, 1],
                    3: [11, 8, 5, 2],
                    4: [15, 12, 9, 6],
                    5: [19, 16, 13, 10],
                    6: [20, 17, 14],
                    7: [21, 18],
                    8: 22
                    },
                -45: {
                    1: 2,  # left as is
                    2: [1, 6],
                    3: [0, 5, 10],
                    4: [4, 9, 14],
                    5: [3, 8, 13, 18],
                    6: [7, 12, 17, 22],
                    7: [11, 16, 21],
                    8: [15, 20],
                    9: 19
                }
    }
}
        
        ...
        def blink():
            _timing = 0.05
            _brightness = 1
            
            self.neopixel.fill([_brightness, _brightness, _brightness])
            self.neopixel.write()
            sleep(_timing)
            self.neopixel.fill([0, 0, 0])
            self.neopixel.write()
            sleep(_timing)
        
        blink()
        blink()
    
    class LightsInterupt(Exception):
        ...

    def _write(self):
        return self.neopixel.write()

    def interuptCheck(self):
        if self.toggle_pin.value() == 0:
            raise self.LightsInterupt
    
    def clearAll(self):
        self.neopixel.fill([0, 0, 0])
        self._write()
    
    def setAll(self, value: list):
        self.neopixel.fill(value)
        self._write()
    
    def clear(self, pos: int | list):
        if pos is int:
            self.neopixel[pos] = [1, 1, 1]
            self._write()
        if pos is list:
            for i in list:
                self.neopixel[i] = [0,0,0]
            self._write()
    
    def set(self, pos: int | list | None, value: list | None, *data: dict):
        if pos is not None and value is not None:
            if type(pos) == list:  # noqa: E721
                for i in pos:
                    self.neopixel[i] = value
            else:
                self.neopixel[pos] = value

        if pos is None and value is None and data:
            _pos = []
            _value = []
            for i in data:
                _pos.append(i.keys())
                _value.append(i.values())
            leng = len(_pos)
            for i in range(leng):
                self.neopixel[_pos[i]] = _value[i]

        self._write()
            


    @staticmethod
    def randomHexValue() -> int:
        from random import getrandbits
        return getrandbits(8)