import virtualbox
from time import sleep

genymotion_vm_name = "Samsung Galaxy S4 - 4.3 - API 18 - 1080x1920"

vbox = virtualbox.VirtualBox()
genymotion_vm = vbox.find_machine(genymotion_vm_name)
genymotion_session = genymotion_vm.create_session()


attack = (50, 200)
army = (50, 170)
left = (100, 105)
find_match = (300, 170)

# coordinates, build time, house space
Barbarian = {'name': 'Barbarian', 'coordinates': (280, 120), 'time': 20, 'space':1}
Archer = {'name': 'Archer', 'coordinates': (450, 110), 'time': 25, 'space':1}
Giant = {'name': 'Giant', 'coordinates': (600, 110), 'time': 2*60, 'space':5}

# quantity and capacity train of barracks
barracks = {'quantity': 2, 'capacity': 30}

# slot in find match
slot1 = (150, 200)
slot2 = (250, 200)
slot3 = (320, 200)
slot4 = (420, 200)
slot5 = (520, 200)
slot6 = (600, 200)
slot7 = (700, 200)


def click((x,y)):
    genymotion_session.console.mouse.put_mouse_event_absolute(x, y, 0, 0, 0)
    genymotion_session.console.mouse.put_mouse_event_absolute(x, y, 0, 0, 1)
    genymotion_session.console.mouse.put_mouse_event_absolute(x, y, 0, 0, 0)


def keep_alive(wait_time):
    while wait_time > 0:
        print wait_time / 60
        click((360,223))
        sleep(60)
        wait_time -= 60


def buy_army(name, quantity):
    for j in xrange(quantity):
        click(name['coordinates'])
        sleep(0.1)


def buy_armys(*armys):
    # (name, quantity)
    for i in armys:
        click(army)
        sleep(0.2)
        spaces = i[0]['space'] * i[1]
        if spaces <= barracks['capacity']:
            for j in xrange(barracks['quantity']):
                click(left)
                sleep(0.2)
                buy_army(i[0], i[1])
            print 'Training {} {}'.format(i[1], i[0]['name'])
            click(attack)
            keep_alive(i[0]['time'] * i[1])
        else:
            allow = barracks['capacity'] / i[0]['space']
            while spaces > barracks['capacity']:
                buy_armys((i[0], allow))
                spaces -= allow
            buy_armys((i[0], spaces / i[0]['space']))
            keep_alive(i[0]['time'] * (spaces / i[0]['space']))


def deploy_troops():
    pass


def train(*armys):
    buy_armys(*armys)
    print 'Trained'
    print 'Safe time:'
    keep_alive(120*60)
   

if __name__ == '__main__':
    while True:
        train((Giant, 3), (Archer, 8))
        # click(attack)
        # sleep(0.2)
        # click(find_match)
        # sleep(5)
        # deploy_troops()
