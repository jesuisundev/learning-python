from contextlib import closing

class RefrigeratorRaider:
    def open(self):
        print("Open fridge")


    def take(self, food):
        print(f"finding {food}...")
        if food == 'pizza':
            raise RuntimeError("health warning")
        print(f"Taking {food}")

    
    def close(self):
        print("Close fridge door.")


def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)

raid('spam')
raid('pizza')