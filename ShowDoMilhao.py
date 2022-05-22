import random

# Perguntas:
e1p1 = ["=> Qual o valor de a<->b sabendo que a=1 e b=0?", "1) 1", "2) 1 e 0", "3) 0", "4) 0 e 1", "5) 0 e 0"]
e1p2 = ["=> Qual o comando para apresentar uma frase no output na linguagem Python?", "1) printf()", "2) input()", "3) int(input())", "4) print()", "5) read()"]
e1p3 = ["=> Qual biblioteca é utilizada para operações de raiz quadrada e potência na linguagem C?", "1) string.h", "2) stdio.h", "3) sqrt.h", "4) math.h", "5) operations.h"]
e1p4 = ["=> Em lógica, sabendo que a->b = 0, qual o valor de a e b, respectivamente?","1) 0 e 1","2) 1 e 1","3) 0 e 0","4) 1 e 0","5) Não é possível determinar."]
e1p5 = ["=> Qual o comando para iniciar uma matriz na linguagem C?","1) variavel[vetor]+[vetor]","2) matriz[10]*[10]","3) variavel[10][10]","4) matriz[vet]","5) matriz[10*10]"]

e2p1 = ["=> Como se chama um dos métodos de ordenação de valores no vetor em algoritmos?","1) Ordenação Física","2) Bubble Sort","3) Vector Sorting","4) Ordenação em String","5) Validação Ordenada"]
e2p2 = ["=> Em lógica, um argumento é falho quando?","1) O valor do argumento é 0. ","2) O valor do argumento é 1 e da conclusão é 0.","3) O valor do argumento é 1.","4) O valor do argumento é 0 e da conclusão é 1.","5) O argumento é falho quando não há respostas."]
e2p3 = ["=> Qual o método para transformar um valor em hexadecimal para binário?","1) Transformação em 4 bits.","2) Transformação em 3 bits.","3) Polinômio.","4) Divisão.","5) Não há como transformar um valor hexadecimal para binário."]
e2p4 = ["=> Qual a função utilizada pela biblioteca string.h para comparar valores de duas strings?","1) strlen","2) strcat","3) strupr","4) strcpy","5) strcmp"]
e2p5 = ["=> Em lógica, como testar se há implicância entre argumentos e conclusão através de condicional?","1) Se os resultados forem falsos.","2) Se os resultados forem contradição.","3) Se os resultados forem tautologia.","4) Se os resultados forem contingência.","5) Se os resultados forem indeterminação."]

e3p1 = ["=> Qual a conclusão de a->c, b->a ?","1) a<->c","2) b->c","3) c<->b","4) c->a’","5) b’->a’"]
e3p2 = ["=> Ao multiplicar uma matriz de tamanho 124x86 e outra matriz de tamanho 86x1500, qual o tamanho da matriz resultante?","1) 124x1500","2) 124x86","3) 86x86","4) 86x1500","5) Não há como realizar a multiplicação destas matrizes."]
e3p3 = ["=> Qual o comando para concatenar duas strings na biblioteca string.h?","1) string.h","2) concstr","3) strconc","4) strcnc","5) strcat"]
e3p4 = ["=> O que a função ijust realiza na linguagem Python?","1) Retorna um string justificado à direita em um campo de tamanho largura.","2) Retorna um string centrado em um campo de tamanho largura.","3) Retorna o número de ocorrências de item.","4) Retorna um string justificado à esquerda em um campo de tamanho largura.","5) Retorna o índice mais à esquerda onde o substring item é encontrado."]
e3p5 = ["=> Qual a linguagem de programação mais usada atualmente no mundo?","1) Javascript.","2) Java.","3) C++.","4) Python.","5) C#."]

pfinal = ["=> Qual foi a primeira linguagem de programação de alto nível a ser criada?","1) FORTRAN","2) PLANKALKÜL","3) PASCAL","4) ALGOL","5) COBOL"]

# Cores Prompt:
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"

# Função de Universitarios:
qtduniv = 3
def univ(respdaperg):
    global uni1
    global uni2
    global uni3
    global qtduniv
    if respdaperg>3:
        uni1 = random.randint(respdaperg, 5)
        uni2 = random.randint(respdaperg, 5)
        uni3 = random.randint(respdaperg, 4)
    elif respdaperg<3:
        uni1 = random.randint(2, respdaperg)
        uni2 = random.randint(1, respdaperg)
        uni3 = random.randint(1, respdaperg)
    else:
        uni1 = random.randint(2, 4)
        uni2 = random.randint(2, 3)
        uni3 = random.randint(2, 4)

    print("O universitário número 1 indicou a resposta número:", uni1)
    print("O universitário número 2 indicou a resposta número:", uni2)
    print("O universitário número 3 indicou a resposta número:", uni3)

    qtduniv-=1

    if qtduniv > 0:
        print(BLUE + "\nVocê pode usar a ajuda dos universitários mais", qtduniv, "vezes.\n")
    else:
        print(RED + "\nVocê não poderá mais utilizar a ajuda dos universitários!\n")

#Função Plateia:
qtdplateia = 3
def plateia(respdaperg):
    global qtdplateia

    if respdaperg > 3:
        qtdde1 = random.randint(1, 3)
        qtdde2 = random.randint(1, 3)
        qtdde3 = random.randint(1, 4)
        qtdde4 = random.randint(5, 10)
        qtdde5 = random.randint(5, 10)
        tot = qtdde1+qtdde2+qtdde3+qtdde4+qtdde5
    elif respdaperg < 3:
        qtdde1 = random.randint(5, 10)
        qtdde2 = random.randint(5, 10)
        qtdde3 = random.randint(1, 4)
        qtdde4 = random.randint(1, 3)
        qtdde5 = random.randint(1, 3)
        tot = qtdde1+qtdde2+qtdde3+qtdde4+qtdde5
    else:
        qtdde1 = random.randint(1, 2)
        qtdde2 = random.randint(5, 7)
        qtdde3 = random.randint(5, 12)
        qtdde4 = random.randint(5, 7)
        qtdde5 = random.randint(1, 2)
        tot = qtdde1+qtdde2+qtdde3+qtdde4+qtdde5

    if tot < 30:
        qtdnsei = 30 - tot
    else:
        qtdnsei = 0

    print("Quantidade de placas número 1:", qtdde1)
    print("Quantidade de placas número 2:", qtdde2)
    print("Quantidade de placas número 3:", qtdde3)
    print("Quantidade de placas número 4:", qtdde4)
    print("Quantidade de placas número 5:", qtdde5)
    print("Quantidade de pessoas que não souberam:", qtdnsei)

    qtdplateia-=1

    if qtdplateia > 0:
        print(BLUE + "\nVocê pode usar a ajuda da plateia mais", qtdplateia, "vezes.\n")
    else:
        print(RED + "\nVocê não poderá mais utilizar a ajuda da plateia!\n")

# Função das Cartas:
qtdcartas = 3
def cartas(respdaperg):
    global qtdcartas
    global acertoucarta

    premiada = random.randint(1, 4)

    carta = int(input("Escolha uma das quatro cartas, digitando o número dela: 1, 2, 3 ou 4.\n"))
    while carta < 1 and carta > 4:
        carta = int(input("Digite novamente o valor da carta."))

    if carta == premiada:
        print(GREEN + "Você tirou Ás, sendo assim, a alternativa correta é a:", respdaperg)
    else:
        print(RED + "Você tirou Reis. Mais sorte na próxima vez!")

    qtdcartas-=1

    if qtdcartas > 0:
        print(BLUE + "\nVocê pode usar a ajuda das cartas mais", qtdcartas, "vezes.\n")
    else:
        print(RED + "\nVocê não poderá mais usar a ajuda das cartas!\n")

# Função Pular:
qtdpular = 1
def pular(respdaperg):
    global qtdpular
    print("Você decidiu pular! A resposta correta é:" + GREEN, respdaperg)
    qtdpular-=1

# Função Ajudas:
def querajuda(respcerta):
    # Universitarios:
    if qtduniv > 0:
        usaruniv = int(input(BLUE + "Gostaria de perguntar aos universitários? Digite: 1 - Sim, 2 - Não.\n"))
        while usaruniv != 1 and usaruniv != 2:
            usaruniv = int(input("Digite novamente o valor!\n"))
        if usaruniv == 1:
            univ(respcerta)
    # Plateia:
    if qtdplateia > 0:
        usarplateia = int(input(BLUE + "Gostaria de perguntar à plateia? Digite: 1 - Sim, 2 - Não.\n"))
        while usarplateia != 1 and usarplateia != 2:
            usarplateia = int(input("Digite novamente o valor!\n"))
        if usarplateia == 1:
            plateia(respcerta)
    # Cartas:
    if qtdcartas > 0:
        usarcartas = int(input(BLUE + "Gostaria de utilizar a ajuda das cartas? Digite: 1 - Sim, 2 - Não.\n"))
        while usarcartas != 1 and usarcartas != 2:
            usarcartas = int(input("Digite novamente o valor!\n"))
        if usarcartas == 1:
            cartas(respcerta)
    # Pular:
    if qtdpular > 0:
        usarpular = int(input(BLUE + "Gostaria de pular esta pergunta? Digite: 1 - Sim, 2 - Não.\n"))
        while usarpular != 1 and usarpular != 2:
            usarpular = int(input("Digite novamente o valor!\n"))
        if usarpular == 1:
            pular(respcerta)
            print(RED + "\nVocê não poderá mais pular perguntas!")

#Função do Prêmio:
vpremio = 0
def premio():
    global vpremio
    print(YELLOW + "\nVocê acertou! Seu prêmio acumulado é de:", vpremio,"reais.\n")

#Define perdeu = 0, chegou no final sem errar ou parar.
perdeu = 0

Jogando = True
while Jogando == True:
        print(CYAN + "Bem-vindo ao Jogo do Milhão, nesta semana, o tema é PROGRAMAÇÃO!")
        print("A cada pergunta você poderá parar, levando todo seu prêmio acumulado, mas caso deseje continuar e errar, perderá metade do seu prêmio.\n")
        print(BLUE + "Você pode pedir ajuda aos universitários, 3 universitários dirão qual resposta eles escolheriam.")
        print("Você pode pedir ajuda à plateia, a plateia irá levantar uma placa referente à resposta que eles escolheriam.")
        print("Você pode utilizar a ajuda das cartas, onde serão aprensetadas 4 cartas, caso acerte qual é a carta Às, será aprensetada a resposta correta.")
        print("As três ajudas poderão ser utilizadas 3 vezes durante o jogo, mas não estarão disponíveis na pergunta de 1 milhão!")
        print(YELLOW + "Caso esteja sem saída, poderá utilizar a opção PULAR, mas utilize-a com cautela, pois esta só pode ser utilizada uma única vez!\n")
        print(CYAN + "Começa agora a primeira etapa contendo 5 perguntas!\n")

        # >>>> e1p1
        for i in range(0,6,1):
            print(GREEN + e1p1[i])

        # Quer ajuda?
        respcerta = 3
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE + "\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 3:
            perdeu = 3
            print(CYAN + "A resposta correta era:", e1p1[respcerta])
            break
        else:
            vpremio+=1000
            premio()

        # >>>> e1p2
        print(GREEN + e1p2[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break

        for i in range(1,6,1):
            print(GREEN + e1p2[i])

        # Quer ajuda?
        respcerta = 4
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 4:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e1p2[respcerta])
            break
        else:
            vpremio+=1000
            premio()

        # >>>> e1p3
        print(GREEN + e1p3[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e1p3[i])

        # Quer ajuda?
        respcerta = 4
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 4:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e1p3[respcerta])
            break
        else:
            vpremio+=1000
            premio()

        # >>>> e1p4
        print(GREEN + e1p4[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e1p4[i])

        # Quer ajuda?
        respcerta = 4
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 4:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e1p4[respcerta])
            break
        else:
            vpremio+=1000
            premio()

        # >>>> e1p5
        print(GREEN + e1p5[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e1p5[i])

        # Quer ajuda?
        respcerta = 3
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 3:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e1p5[respcerta])
            break
        else:
            vpremio+=1000
            premio()

        print(CYAN + "Começa agora a segunda etapa contendo 5 perguntas!")

        # >>>> e2p1
        print(GREEN + e2p1[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e2p1[i])

        # Quer ajuda?
        respcerta = 2
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 2:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e2p1[respcerta])
            break
        else:
            vpremio=10000
            premio()

        # >>>> e2p2
        print(GREEN + e2p2[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e2p2[i])

        # Quer ajuda?
        respcerta = 2
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 2:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e2p2[respcerta])
            break
        else:
            vpremio+=10000
            premio()

        # >>>> e2p3
        print(GREEN + e2p3[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e2p3[i])

        # Quer ajuda?
        respcerta = 1
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 1:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e2p3[respcerta])
            break
        else:
            vpremio+=10000
            premio()

        # >>>> e2p4
        print(GREEN + e2p4[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e2p4[i])

        # Quer ajuda?
        respcerta = 5
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 5:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e2p4[respcerta])
            break
        else:
            vpremio+=10000
            premio()

        # >>>> e2p5
        print(GREEN + e2p5[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e2p5[i])

        # Quer ajuda?
        respcerta = 3
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 3:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e2p5[respcerta])
            break
        else:
            vpremio+=10000
            premio()

        print(CYAN + "Começa agora a terceira etapa contendo 5 perguntas!")

        # >>>> e3p1
        print(GREEN + e3p1[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e3p1[i])

        # Quer ajuda?
        respcerta = 2
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 2:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e3p1[respcerta])
            break
        else:
            vpremio=100000
            premio()

        # >>>> e3p2
        print(GREEN + e3p2[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e3p2[i])

        # Quer ajuda?
        respcerta = 1
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 1:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e3p2[respcerta])
            break
        else:
            vpremio+=100000
            premio()

        # >>>> e3p3
        print(GREEN + e3p3[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e3p3[i])

        # Quer ajuda?
        respcerta = 5
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 5:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e3p3[respcerta])
            break
        else:
            vpremio+=100000
            premio()

        # >>>> e3p4
        print(GREEN + e3p4[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e3p4[i])

        # Quer ajuda?
        respcerta = 4
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)
        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 4:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e3p4[respcerta])
            break
        else:
            vpremio+=100000
            premio()

        # >>>> e3p5
        print(GREEN + e3p5[0])
        # Deseja continuar?
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + e3p5[i])

        # Quer ajuda?
        respcerta = 1
        if qtdcartas > 0 or qtduniv > 0 or qtdplateia > 0 or qtdpular > 0:
            usarajudas = int(input(BLUE + "\nGostaria de utilizar alguma ajuda? Digite: 1- Sim. 2 - Não.\n"))
            while usarajudas != 1 and usarajudas != 2:
                usarajudas = int(input("Digite novamente o valor!\n"))
            if usarajudas == 1:
                querajuda(respcerta)

        # Resposta:
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 1:
            perdeu = 1
            vpremio = vpremio / 2
            print(CYAN + "A resposta correta era:", e3p5[respcerta])
            break
        else:
            vpremio+=100000
            premio()

        # Pergunta Final
        print(CYAN + "Você chegou à última pergunta, a pergunta no valor de um milhão de reais!")
        print(CYAN + "Se parar agora, leva o seu premio de 500 mil reais, porém, se errar, perderá tudo!\n")
        print(GREEN + pfinal[0])
        continuar = int(input(RED + "\nDeseja continuar ou parar? Digite: 1 - Continuar. 2 - Parar.\n"))
        while continuar != 1 and continuar != 2:
            continuar = int(input("Digite novamente: 1 - Continuar. 2 - Parar.\n"))
        if continuar == 2:
            perdeu = 2
            break
        for i in range(1,6,1):
            print(GREEN + pfinal[i])
        # Resposta:
        respcerta = 2
        resp = int(input(BLUE +"\nDigite o valor de sua resposta!\n"))
        while (resp < 1 or resp >5):
            resp = int(input("Digite novamente o valor!\n"))
        if resp != 2:
            perdeu = 4
            vpremio = 0
            print(CYAN + "A resposta correta era:", pfinal[respcerta])
            break
        else:
            break

#Verifica valor de perdeu:
# Perdeu = 1, Parou = 2, Perdeu na 1ª pergunta = 3, Perdeu na ultima pergunta = 4
if perdeu == 1:
    print(RED + "\nVocê perdeu, mas seu prêmio foi de:", int(vpremio),"reais!")
elif perdeu == 2:
    print(CYAN + "\nParabéns por chegar até aqui! Seu prêmio foi de:", int(vpremio),"reais!")
elif perdeu == 3:
    print(RED + "\nVocê perdeu, mais sorte na próxima vez!")
elif perdeu == 4:
    print(RED + "\nVocê perdeu TUDO! Mais sorte na próxima vez.")
else:
    print(CYAN + "\nPARABÉNS!!! Você é um milionário!")
    print(YELLOW + "        '._==_==_=_.'     ")
    print("        .-\\:      /-.    ")
    print("       | (|:.     |) |    ")
    print("        '-|:.     |-'     ")
    print("          \\::.    /      ")
    print("           '::. .'        ")
    print("             ) (          ")
    print("           _.' '._        ")
    print("          '-------'       ")
