import time

def parse(fname):
    with open(fname, "r") as file:
        return file.readlines()

def run(day, part, func):
    print("AoC Day{:02d} Part{:02d} Start".format(day, part))
    start = time.time()
    func()
    end = time.time()
    dt = end - start
    print("AoC Day{:02d} Part{:02d} End Elapsed Time {:.3f}s".format(day, part, dt))
