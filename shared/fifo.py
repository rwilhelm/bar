import os
import errno

FIFO = 'fifo'

def mkfifo():
    try:
        os.mkfifo(FIFO)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise

    print("Opening FIFO...")
    with open(FIFO) as fifo:
        print("FIFO opened")
        while True:
            data = fifo.read()
            if not data:
                print("Writer closed")
                break
            print('Read: "{0}"'.format(data))
