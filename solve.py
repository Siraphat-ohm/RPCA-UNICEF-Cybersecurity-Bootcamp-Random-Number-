import pwn
from randcrack import RandCrack

# initRc: Initialize the RandCrack 
def initRc(io):
    rc = RandCrack()
    for _ in range( 312 ):
        io.recvline()
        current = io.recvline().decode().split(':')[1]
        rc.submit(int(current))

        io.sendline( b'0' )

        io.recvline()
        next_int = io.recvline().decode().split(':')[1]
        rc.submit(int(next_int))
    return rc

def solve(io, rc):
    for _ in range( 10 ):
        io.recvline()
        io.recvline().decode().split(':')[1]

        rc.predict_randrange(0, 4294967295)
        # we sent a next_int for guessing
        next_int = rc.predict_randrange(0, 4294967295)
        io.sendline( str(next_int).encode() )

        line = io.recvline().decode().strip()
        print(line)
        io.recvline()

    line = io.recvline().decode().strip()
    print(line)

def main():
    io = pwn.remote('103.13.31.236', 10006)
    rc = initRc(io)
    solve(io, rc)
    io.close()

if __name__ == '__main__':
    main()