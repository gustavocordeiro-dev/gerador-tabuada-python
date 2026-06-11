while True:
    while True:
        try:
            numero = int(input("\nDeseja obter a tabuada de qual número? : "))
            break
        except ValueError:
            print("Digite apenas números aqui!")
        
    
    print(f"\n--- Tabuada do {numero} ---\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
    
    sair = input("Deseja sair? (S/N) : ").title().strip()
    
    if sair == "S" :
        print("Obrigado, finalizando o programa.")
        break
    elif sair == "N" :
        continue
    else:
        print("Digite uma opção válida, o programa continuará ...")