
# layer 0: Background Objects
# layer 1: Foreground Objects(Hero, Enemy, Boss)
# layer 2: Hero bullet Objects
# layer 3: Enemy bullet Objects
# layer 4: Explosion


objects = [[],[],[],[],[]]

def add_object(o, layer):
    objects[layer].append(o)

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def clear():
    for l in objects:
        l.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

#원하는 레이어에 있는 값들만 가져오기 위함. 2,3에는 총알만 들어있으니까.
def get_objects(i):
    return objects[i]


