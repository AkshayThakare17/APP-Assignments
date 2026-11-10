import gc
import tracemalloc

def create_objects():
    objects = []
    for i in range(1000):
        obj = []
        obj.append(obj)
        objects.append(obj)
    return objects

tracemalloc.start()

gc.disable()

print("Initial Memory:", tracemalloc.get_traced_memory()[0], "bytes")

objects = create_objects()

print("Memory Before Garbage Collection:", tracemalloc.get_traced_memory()[0], "bytes")

del objects

gc.enable()

collected = gc.collect()

print("Garbage Collector Collected:", collected, "objects")

print("Memory After Garbage Collection:", tracemalloc.get_traced_memory()[0], "bytes")

tracemalloc.stop()
