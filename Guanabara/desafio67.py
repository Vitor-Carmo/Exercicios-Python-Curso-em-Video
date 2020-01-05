while True:
    print("-"*40)
    tabuada = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 40)
    if tabuada < 0:
        break
    for i in range(1, 11):
        print(f"{tabuada} X {i} = {tabuada*i}")