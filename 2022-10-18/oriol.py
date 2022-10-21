from yogi import read
def bars(n:int):
    if n == 1:
        print ("*")
    else:
        bars(n-1)
        print("*"*n)
        bars(n-1)

if __name__ == "__main__":
    bars(read(int))
