from lightArray import lightArray
from time import sleep
from random import getrandbits


# ... Main Function

pin = 5
length = 27
lights = lightArray(pin, length)
sleep(1)

# ... Global Variable and Color Zone yippeeeee!!!11!!
class COLORS:
    def __init__(self):
        ...

    RED = [20, 0, 0]
    GREEN = [0, 20, 0]
    BLUE = [0, 0, 20]
    PORPLE = [3, 0, 4]
    YELLOW = [15, 15, 0]
    WHITE = [15, 15, 15]
    ORANGE = [20, 6, 0]

    MAX = [255, 255, 255]
    MIN = [1, 1, 1]
    TEST = [5, 0, 0]
    
    @staticmethod
    def babySafeIt(color: list) -> list:
        print('Baby Safing the color. . .')
        _color = []
        for c in color:
            c = c * 0.25
            round(c)
            _color.append(int(c))
        return _color
    
    pos = 0
    @classmethod
    def randomColor(cls):
        
        _colors = [
            getattr(cls, name)
            for name in dir(cls)
            if not callable(getattr(cls, name)) and not name.startswith("__")
        ]
        for i in _colors:
            if i == COLORS.MAX or i == COLORS.TEST or i == COLORS.MIN:
                _colors.remove(i)
        while True:
            if COLORS.pos <= (len(_colors) - 1):
                COLORS.pos = COLORS.pos + 1
            if COLORS.pos >= (len(_colors) - 1):
                COLORS.pos = 0
            if getrandbits(1):
                return _colors[COLORS.pos]

FILL = True
COLOR = ...
GLOBAL_SPEED = 0.1

_on = [] 

rows = 'rows'
v = 'v'
h = 'h'

...
class lightFunctions():
    def __init__(self) -> None:
        ...
    
    @staticmethod
    def randomFadeInFadeOut(c):
        print('randomFadeInFadeOut')

        r = getrandbits(4)
        for i in range(1, 20):
            lights.set(r, c)
            sleep(0.05)
        for i in range(20, 1, -1):
            lights.set(r, c)
            sleep(0.05)
        lights.clearAll()
        sleep(0.5)
    
    @staticmethod
    def rollRight(c, fill=False):
        print('rollRight')
        
        for i in range(1, 7):
            i = int(i)
            lights.set(lights.category['rows']['v'][i], c)
            sleep(GLOBAL_SPEED)
            if not fill:
                lights.clearAll()
        lights.clearAll()
    
    @staticmethod
    def rollLeft(c, fill=False):
        print('rollLeft')

        for i in range(6, 0, -1):
            i = int(i)
            lights.set(lights.category['rows']['v'][i], c)
            sleep(GLOBAL_SPEED)
            if not fill:
                lights.clearAll()
        lights.clearAll()


    @staticmethod
    def rollUp(c, fill=False):
        print('rollUp')
        
        for i in range(4, 0, -1):
            i = int(i)
            lights.set(lights.category['rows']['h'][i], c)
            sleep(GLOBAL_SPEED*1.2)
            if not fill:
                lights.clearAll()
        lights.clearAll()

    @staticmethod
    def rollDown(c, fill=False):
        print('rollDown')

        lights.interuptCheck()
        for i in range(1, 5):
            i = int(i)
            lights.set(lights.category['rows']['h'][i], c)
            sleep(GLOBAL_SPEED*1.2)
            if not fill:
                lights.clearAll()
        lights.clearAll()
    
    @staticmethod
    def rollDiaTopLeft(c, fill=False):
        print('rollDiaTopLeft')
        for i in range(1, 9):
            lights.set(lights.category['rows'][45][i], c)
            sleep(GLOBAL_SPEED)
            if not fill:
                lights.clearAll()
        lights.clearAll()
    
    @staticmethod
    def rollDiaBotRight(c, fill=False):
        print('rollDiaBotRight')
        
        for i in range(8, 0, -1):
            lights.set(lights.category['rows'][45][i], c)
            sleep(GLOBAL_SPEED)
            if not fill:
                lights.clearAll()
        lights.clearAll()    
    
    @staticmethod
    def rollDiaBotLeft(c, fill=False):
        print('rollDiaBotLeft')
        for i in range(1, 10):
            lights.set(lights.category['rows'][-45][i], c)
            sleep(GLOBAL_SPEED)
            if not fill:
                lights.clearAll()
        lights.clearAll()
    
    @staticmethod
    def rollDiaTopRight(c, fill=False):
        print('rollDiaTopRight')
        for i in range(9, 0, -1):
            lights.set(lights.category['rows'][-45][i], c)
            sleep(GLOBAL_SPEED)
            if not fill:
                lights.clearAll()
        lights.clearAll()

    @staticmethod
    def _random(): # MPY is so weird with their rand module.
        a, b = getrandbits(3), getrandbits(4)
        if not a and b:
            a = a + 1
        r = a + b
        return r
    
    @staticmethod
    def rollAllClockwise(c, fill=False):
        _fill = fill
        print('rollAllClockwise')
        lightFunctions.rollDiaBotLeft(c, fill=_fill)
        lightFunctions.rollRight(c, fill=_fill)
        lightFunctions.rollDiaTopLeft(c, fill=_fill)
        lightFunctions.rollDown(c, fill=_fill)
        lightFunctions.rollDiaTopRight(c, fill=_fill)
        lightFunctions.rollLeft(c, fill=_fill)
        lightFunctions.rollDiaBotRight(c, fill=_fill)
        lightFunctions.rollUp(c, fill=_fill)

    @staticmethod
    def rollAllRandomly(c, fill=False, randomlyFill=False): # MPY is so weird with their rand module.
        print('rollAllRandomly')
        #r = lightFunctions._random()
        r = getrandbits(3)
        _fill = fill
        if randomlyFill:
            _ = getrandbits(1)
            if _:
                _fill = True
        
        if r == 0: return lightFunctions.rollDown(c, fill=_fill)
        if r == 1: return lightFunctions.rollUp(c, fill=_fill)
        if r == 2: return lightFunctions.rollRight(c, fill=_fill)
        if r == 3: return lightFunctions.rollLeft(c, fill=_fill)
        if r == 4: return lightFunctions.rollDiaBotLeft(c, fill=_fill)
        if r == 5: return lightFunctions.rollDiaBotRight(c, fill=_fill)
        if r == 6: return lightFunctions.rollDiaTopLeft(c, fill=_fill)
        if r == 7: return lightFunctions.rollDiaTopRight(c, fill=_fill)
    
    _on = []
    @staticmethod
    def randomStaticSingle(c, fill=False):
        on = lightFunctions._on
        print(f'\rrandomStaticSingle: {on}', end='')
        r = lightFunctions._random()
        
        on.sort()
        if r not in on:
            if not fill:
                lights.clearAll()
            on.append(r)
            lights.set(r, c)
            sleep(GLOBAL_SPEED * 1.50)
        if on == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]:
            print('')
            lights.clearAll()
            lightFunctions._on = []
    
    @staticmethod
    def corcle(c, fill = False):
        for i in range(0, 4):
            if not fill:
                lights.clearAll()
            lights.set(lights.category[rows][h][1][i], c)
            
            sleep(GLOBAL_SPEED)
        for i in range(0, 3):
            if not fill:
                lights.clearAll()
            lights.set(lights.category['rows']['v'][6][i], c)
            sleep(GLOBAL_SPEED)
        for i in range(5, 0, -1):
            if not fill:
                lights.clearAll()
            lights.set(lights.category[rows][h][4][i], c)
            sleep(GLOBAL_SPEED)
        for i in range(2, 0, -1):
            if not fill:
                lights.clearAll()
            lights.set(lights.category[rows][v][1][i], c)
            sleep(GLOBAL_SPEED)
        for i in range(0, 5):
            if not fill:
                lights.clearAll()
            lights.set(lights.category[rows][h][2][i], c)
            sleep(GLOBAL_SPEED)
        for i in range(2, 2):
            if not fill:
                lights.clearAll()
            lights.set(lights.category[rows][v][5][i], c)
            sleep(GLOBAL_SPEED)
        for i in range(4, 0, -1):
            if not fill:
                lights.clearAll()
            lights.set(lights.category[rows][h][3][i], c)
            sleep(GLOBAL_SPEED)

        if not fill:
            lights.clearAll()
            lights.set(4, COLOR) # Keep concurency with the circle so it just kinda loopdeloops
            sleep(GLOBAL_SPEED)

        lights.clearAll()
    

    ...
    @classmethod
    def allFunctions(cls):
        return [
            getattr(cls, name)
            for name in dir(cls)
            if callable(getattr(cls, name)) and not name.startswith("__")
        ]

testing = 0
while True:
    try:
        '''
        lights:
        [ ] [3]  [7]  [11] [15] [19]
        [0] [4]  [8]  [12] [16] [20]
        [1] [5]  [9]  [13] [17] [21]
        [2] [6]  [10] [14] [18] [22]
        '''
        ...
        while True:
                if testing: ...
                else:
                    try:
                        lightFunctions.randomStaticSingle(COLORS.babySafeIt(COLORS.randomColor()), FILL)
                    except lights.LightsInterupt:
                        on = []
                        sleep(0.5)
                        break
        
    except KeyboardInterrupt as e:
        raise e
    finally:
        lights.clearAll()
