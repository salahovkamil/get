import RPi.GPIO as gpio
import time
from matplotlib import pyplot

gpio.setmode(gpio.BCM)
dac = [8,11,7,1,0,5,12,6]
leds = [9,10,22,27,17,4,3,2]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)
gpio.setup(leds, gpio.OUT)
comp = 14
troyka = 13
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)



def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        daccc = []
        daccc = perev(k)
        gpio.output(dac, daccc)
        time.sleep(0.01)
        compv = gpio.input(comp)
        if compv == gpio.HIGH:
            k -= 2**i
    return k

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

try:
    napr=0
    result_ismer=[]
    time_start=time.time()
    count=0

    #зарядка конденсатора, запис показаний в процессе
    print('начало зарядки конденсатора')
    gpio.output(troyka, 1)

    while napr<256*0.94:
        napr=adc()
        print(napr)
        result_ismer.append(napr)
        time.sleep(0.005)
        count+=1
        gpio.output(leds, perev(napr))

    gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
    print(result_ismer)

    #разрядка конденсатора, запис показаний в процессе
    print('начало разрядки конденсатора')
    gpio.output(troyka, 0)
    while napr>256*0.12:
        napr=adc()
        print(napr)
        result_ismer.append(napr)
        time.sleep(0.005)
        count+=1
        gpio.output(leds, perev(napr))

    time_experiment=time.time()-time_start

    #запись данных в файлы
    print('запись данных в файл')
    with open('data.txt', 'w') as f:
        for i in result_ismer:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.01289')
    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/count, 1/(time_experiment/count), 0.013))

#графики
    print('построение графиков')
    y=[i/256*3.3 for i in result_ismer]
    x=[i*time_experiment/count for i in range(len(result_ismer))]
    pyplot.plot(x, y)
    pyplot.xlabel('время')
    pyplot.ylabel('вольтаж')
    pyplot.show()

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()
