def read_next(*args):
    for seq in args:
        yield from seq
        