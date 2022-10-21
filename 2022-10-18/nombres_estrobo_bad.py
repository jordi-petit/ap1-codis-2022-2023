import yogi

# codi poc modular, falta documentacio
def strobogrammatic(n: int) -> bool:
    num = str(n)  # canvi de tipus il.legal
    if not ("2" in num or "3" in num or "4" in num or "5" in num or "7" in num):
        for i in range(len(num) // 2):
            first = num[i]
            last  = num[-(i+1)]
            if first != last or (first == last and first == "6" or last == "9" \
                (first == "6" and last == "9") or (last == "6" and first == "9"):
                return False
        return True
    else:
        return False


def main():
    senars = 0
    n = yogi.scan(int)
    while n is not None:
        if strobogrammatic(n):
            senars += 1
            print(f"{n} si es estrobogramatic")
        else:
            print(f"{n} no es estrobogramatic")
        n = yogi.scan(int)

    print(f"estrobogramatics senars: {senars}")

if __name__ == "__main__":
    main()