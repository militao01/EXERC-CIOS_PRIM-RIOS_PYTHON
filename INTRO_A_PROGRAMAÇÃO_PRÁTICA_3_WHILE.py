### Completar o menu implementando subtração e multiplicação ###
def soma (numero1, numero2):
    return numero1 + numero2
def subtracao (numero1, numero2):
    return numero1 - numero2
def multiplicacao (numero1, numero2):
    return numero1 * numero2
def divisão (numero1, numero2):
    return numero1/numero2

opcao = 0              

while opcao != 4:      
    print("\n========== MENU ==========")   
    print("1 - Somar")                      
    print("2 - Subtrair")                   
    print("3 - Multiplicar")                
    print("4 - Sair \n")                    

    opcao = int(input("Escolha uma opção(1 a 4): "))  
    if opcao == 1:                         
        print("Você escolheu somar.")      
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: "))  
        s = soma(numero1, numero2)            
        input("Pressione Enter para continuar...") 
        print(f"A soma dos seus números é {s}")

    elif opcao == 2:                        
        print("Você escolheu subtrair.") 
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: "))    
        sub = subtracao(numero1,numero2)
        input("Pressione Enter para continuar...") 
        print(f"A subtração dos seus números é {sub}")
    elif opcao == 3:                        
        print("Você escolheu multiplicar.") 
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: ")) 
        m = multiplicacao(numero1, numero2)
        input("Pressione Enter para continuar...")
        print(f"A multiplicação dos seus números é {m}")

    elif opcao == 4:                        
        print("Saindo...")    
    else:                                   
        print("Opção inválida!")
        