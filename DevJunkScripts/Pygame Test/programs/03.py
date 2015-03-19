# Pygame_notes 03.py
# All bird sounds are copyrighted by Alberto Masi - www.scricciolo.com

import os, pygame.mixer, pygame.time

pygame.mixer.init(22050,8,1,2048)

totaltime = 0

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
f7 = 0
f8 = 0

a = os.path.join('data','Upupa.wav') # 1/8 = 220 milisecs
b = os.path.join('data','Bubo.wav')
c = os.path.join('data','Cuculus.wav')
d = os.path.join('data','Otus.wav')
e = os.path.join('data','Chersophilus.wav')
f = os.path.join('data','Parus.wav')
g = os.path.join('data','Gavia.wav')
h = os.path.join('data','Columba.wav')
i = os.path.join('data','Gavia2.wav')

aa = pygame.mixer.Sound(a)
bb = pygame.mixer.Sound(b)
cc = pygame.mixer.Sound(c)
dd = pygame.mixer.Sound(d)
ee = pygame.mixer.Sound(e)
ff = pygame.mixer.Sound(f)
gg = pygame.mixer.Sound(g)
hh = pygame.mixer.Sound(h)
ii = pygame.mixer.Sound(i)

aaa = pygame.mixer.Channel(0)
bbb = pygame.mixer.Channel(1)
ccc = pygame.mixer.Channel(2)
ddd = pygame.mixer.Channel(3)
eee = pygame.mixer.Channel(4)
fff = pygame.mixer.Channel(5)
ggg = pygame.mixer.Channel(6)
hhh = pygame.mixer.Channel(7)

clock = pygame.time.Clock()

while totaltime < 70000:

    totaltime = totaltime + clock.tick()

    if totaltime in [0,1760,3520,5280,7040,8800,10560,12320,14080,15840,\
                     17600,19360,21120,22880,24640,26400,28160,29920,31680,\
                     33440,35200,36960,38720,40480,42240,44000,45760,47520,\
                     52800,54560]:
        aaa.play(aa) # Upupa


    if totaltime in [4180,11220,18260,25300,32340,39380,46420,53460]:
        bbb.play(bb) # Bubo

    if totaltime in [7920,9680,11440,13200,14960,16720,18480,20240,22000,\
                     23760,25520,27280,29040,30800,32560,34320,36080,37840,\
                     39600,41360,43120,44880,46640,48400,53680,55440]:
        ccc.play(cc) # Cuculus

    if totaltime in [15620,17380,19140,20900,22660,24420,26180,27940,\
                     29700,31460,33220,34980,36740,38500,40260,42020,\
                     43780,45540,47300,49060,54340,56100]:
        ddd.play(dd) # Otus

    if totaltime in [21780,25300,28820,32340,35860,39380,42900,46420,49940,\
                     53460]:
        eee.play(ee) # Chersophilus

    if totaltime in [28380,30140,31900,33660,35420,37180,38940,40700,\
                     42460,44220,45980,47740,53020,54780]:
        fff.play(ff) # Parus

    if totaltime in [36300,38060,39820,41580,41580,43340,45100,46860,48620,\
                     53900,55660]:
        ggg.play(gg) # Gavia

    if totaltime in [42680,46200,53240]:
        hhh.play(hh) # Columba

    if totaltime in [57420]:
        ggg.play(ii) # Gavia2

    if totaltime == 0 and f1 == 0:
        print'Channel 1............Upupa Epops'
        f1 = 1

    if totaltime == 4180 and f2 == 0:
        print'Channel 2..............Bubo bubo'
        f2 = 1

    if totaltime == 7920 and f3 == 0:
        print'Channel 3........Cuculus canorus'
        f3 = 1

    if totaltime == 15620 and f4 == 0:
        print'Channel 4.............Otus scops'
        f4 = 1

    if totaltime == 21780 and f5 == 0:
        print'Channel 5...Chersophilus duponti'
        f5 = 1

    if totaltime == 28380 and f6 == 0:
        print'Channel 6........Parus palustris'
        f6 = 1

    if totaltime == 36300 and f7 == 0:
        print'Channel 7............Gavia immer'
        f7 = 1

    if totaltime == 42680 and f8 == 0:
        print'Channel 8..........Columba livia'
        f8 = 1

    if totaltime == 57420:
        print'Channel 7............Gavia immer'
        pygame.time.delay(3500)
        print'Channel 7............Gavia immer'
        pygame.time.delay(5000)
        print'Channel 7............Gavia immer'
