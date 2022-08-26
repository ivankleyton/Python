#Aluno: Edésio Rafael Cunha Pereira    #2016003787
#Aluno: Ivan Kleyton Campelo Ferreira  #2016011484
#Aluno: Mario Henrique Silva de Souza  #2016011519

questao=int(input("Informe uma questão a ser executada: "))
#31-Faça um algoritmo que leia dois números A e B e imprima o maior deles.
if questao==31:
    A=int(input("Digite um número:"))            
    B=int(input("Digite um segundo número:"))         
    if(A>B):
        print("O maior número é:", A)
    else:
        print("O maior número é:", B)

#33-Faça um algoritmo para calcular a média final de um aluno baseada em 3 provas com pesos 2, 3 e 5 respectivamente
elif questao==33:
    n1=float(input("Digite a primeira nota: "))
    n2=float(input("Digite a segunda nota: "))
    n3=float(input("Digite a terceira nota: "))
    x1=n1*2
    x2=n2*3
    x3=n3*5
    media=(x1+x2+x3)/10
    print("Sua média é", media)

#35 Faça um algoritmo referente a um vestibular
elif questao==35:
#A O nome e as notas em cada prova do candidato 
    nome_candidato=(input("Digite o nome do candidato: "))
    nota_pt=float(input("Digite sua nota em Português: "))
    nota_mtm=float(input("Digite sua nota em Matemática: "))
    nota_cg=float(input("Digite sua nota em Conhecimentos Gerais: "))
    print("O nome do candidato é:", nome_candidato)
    print("Nota de português",nota_pt)
    print("Nota de matemática",nota_mtm)
    print("Nota de conhecimentos gerais",nota_cg)

#B A média do candidato
    media=(nota_pt+nota_mtm+nota_cg)/3
    print("Sua média no vestibular foi", media)

#C Imprimir se o candidato foi aprovado ou não levando em consideração média maior que 7 e nenhuma nota abaixo de 5.
    if(( ((nota_pt+nota_mtm+nota_cg)/3)>7) and nota_pt>5 and nota_mtm>5 and nota_cg>5):
        print("Parabéns,",nome_candidato,"você foi aprovado!")
    else:
        print("Você não foi aprovado!")

#37  Escreva um algoritmo que determine o número de dias que uma pessoa já viveu. Considere que um mês tenha 30 dias. 
elif questao==37:
    x1=float(input("Digite o mês em que nasceu(MM): "))
    x2=float(input("Digite o ano em que nasceu(AAAA): "))
    x3=float(input("Digite o ano em que estamos(AAAA): "))
    n1=(12-x1)*(30)
    n2=(x3-x2)*(30)*12
    dias_de_vida=(n1+n2)
    print("O total de dias vividos foi: ",dias_de_vida)

#39 a, escreva um algoritmo quemostre o número mínimo de notas que o caixa deve fornecer como troco. Mostre
#também: o valor da compra, o valor do troco e a quantidade de cada tipo de nota do troco.
elif questao==39:
    valor=int(input("Digite o valor a ser sacado: "))
    x=valor//100
    valor=valor%100
    y=valor//10
    z=valor%10
    print("O numero de notas de 100 vai ser",x,"\nO numero de notas de 10 vai ser",y,"\nO número de notas de 1 vai ser",z)
    
#41 Faça um algoritmo que determine o salário total de um vendedor. Sendo que a revendedora paga aos seus funcionários
#vendedores dois salários mínimos fixos, mais uma comissão fixa de R$ 50,00 por carro
#vendido e mais 5% do valor das vendas
elif questao==41:
    salario_minimo=880
    cv=int(input("Digite a quantidade de carros vendidos: "))
    va=float(input("Digite o valor arrecadado no mês: "))
    print("Seu salário será R$",salario_minimo*2+cv*50+(va/20))

#43) Uma empresa irá dar um aumento de salário aos seus funcionários de acordo
#com a categoria de cada empregado. O aumento seguirá a seguinte regra:
#• Funcionários das categorias A, C, F, e H ganharão 10% de aumento sobre o salário;
#• Funcionários das categorias B, D, E, I, J e T ganharão 15% de aumento sobre o salário;
#• Funcionários das categorias K e R ganharão 25% de aumento sobre o salário;
#• Funcionários das categorias L, M, N, O, P, Q e S ganharão 35% de aumento sobre o salário;
#• Funcionários das categorias U, V, X, Y, W e Z ganharão 50% de aumento sobre o salário.
#Faça um algoritmo que escreva nome, categoria e salário reajustado de cada empregado.

elif questao==43:
    nome=input("Digite seu nome: ")
    categoria=input("Digite sua categoria: ")
    x=int(input("Digite seu salário: "))
    y=int(input("Digite o número referente a sua categoria:\n1-A\n2-C\n3-F\n4-H\n5-B\n6-D\n7-I\n8-J\n9-T\n10-K\n11-R\n12-L\n13-M\n14-N\n15-O\n16-P\n17-Q\n18-S\n19-U\n20-V\n21-X\n22-Y\n23-W\n24-Z\nDigite aqui: "))
    print("O nome do funcionário é",nome)
    print("Sua categoria é",categoria)
    if y==1 or y==2 or y==3 or y==4:
        print("Seu novo salário será",x+(x*10/100))
    elif y==5 or y==6 or y==7 or y==8 or y==9:
        print("Seu novo salário será",x+(x*15/100))
    elif y==10 or y==11:
        print("Seu novo salário será",x+(x*25/100))
    elif y==12 or y==13 or y==14 or y==15 or y==16 or y==17 or y==18:
        print("Seu novo salário será",x+(x*35/100))
    elif y==19 or y==20 or y==21 or y==22 or y==23 or y==24:
        print("Seu novo salário será",x+(x*50/100))



#45 . Escreva um algoritmo que, para uma conta bancária, leia o seu número, o saldo,
#o tipo de operação a ser realizada (depósito ou retirada) e o valor da operação.
#Após, determine e mostre o novo saldo. Se o novo saldo ficar negativo, deve ser
#mostrada, também, a mensagem “conta estourada”. 
elif questao==45:
    numero_conta=int(input("Digite o número da sua conta: "))
    print("O número da sua conta é",numero_conta)
    saldo=100
    print("Seu saldo é",saldo)
    x=int(input("Qual operação deseja executar?\n1-Depósito\n2-Retirada\nDigite aqui:"))
    if x==1:
        deposito=float(input("Quanto deseja depositar? "))
        print("Seu novo saldo é",saldo+deposito)
    if x==2:
        retirada=float(input("Quanto deseja retirar? "))
        print("Seu novo saldo é",saldo-retirada)



#47 Construir um algoritmo que tome como entradas três valores distintos e os
#apresente (imprima) em ordem crescente (menor para o maior). 
elif questao==47:
    v1=float(input("Digite o primeira valor: "))
    v2=float(input("Digite o segunda valor: "))
    v3=float(input("Digite o terceiro valor: "))
    if(v1>v2 and v2>v3):
       print("A sequencia de números é:",v3,v2,"e",v1)
    elif(v2>v1 and v1>v3):
       print("A sequencia de números é:",v3,v1,"e",v2)
    elif(v2>v1 and v1>v3):
       print("A sequencia de números é:",v3,v1,"e",v2)
    elif(v1>v3 and v3>v2):
       print("A sequencia de números é:",v2,v3,"e",v1)
    elif(v3>v2 and v2>v1):
       print("A sequencia de números é:",v1,v2,"e",v3)

#49  Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos
#lados de um triângulo, e se forem, verificar se é um triângulo equilátero, isóscele
#ou escaleno. Se eles não formarem um triângulo, escrever uma mensagem
elif questao==49:
    x1=int(input("Digite o valor x do triangulo:"))
    y1=int(input("Digite o valor y do triangulo:"))
    z1=int(input("Digite o valor z do triangulo:"))
    if(x1+y1>z1 and x1+z1>y1 and y1+z1>x1):
        print("Os valores digitados formam um triangulo")
    if (x1==y1 and x1==z1):
        print ("O triangulo formado é equilatero")
    if (x1==y1 or x1==z1 or y1==z1):
        print (" O triangulo formado é isóscele")
    if  (x1!=y1 and x1!=z1):
        print ("O triangulo formado é escaleno")


#51 Faça um algoritmo que leia dois números e mostre qual o maior dos dois. 
elif questao==51:
    n1=int(input("Digite um numero: "))
    n2=int(input("Digite outro numero: "))
    if(n1>n2):
        print("O maior numero é:", n1)
    elif(n2>n1):
        print("O maior numero é:", n2)

#53 Faça um algoritmo que leia três números e mostre-os em ordem decrescente.
elif questao==53:
    n1=int(input("digite o primeiro numero: "))
    n2=int(input("digite o segundo numero: "))
    n3=int(input("digite o terceiro numero: "))
    if(n1>n2 and n2>n3):
        print("A ordem decrescente é",n1,n2,n3)
    elif(n2>n1 and n1>n3):
        print("A ordem descrescente é",n2,n1,n3)
    elif(n3>n1 and n1>n2):
        print("A ordem decrescente é",n3,n1,n2)
    elif(n2>n3 and n3>n1):
        print  ("A ordem decrescente é",n2,n3,n1)
    elif(n3>n2 and n2>n1):
        print  ("A ordem decrescente é",n3,n2,n1)

#55  Calcule a média aritmética das três notas de um aluno e mostre, além do valor da
#média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 7; a
#mensagem “em prova final” caso a média seja menor que 7 e maior ou igual a 4;
#e "reprovado", caso contrário. 
elif questao==55:
    n1=float(input("Digite a primeira nota: "))
    n2=float(input("Digite a segunda nota: "))
    n3=float(input("Digite a terceira nota: "))
    media=(n1+n2+n3)/3
    if(media>=7):
       print("Aprovado")
    elif(media>=4<=7):
       print("Em prova final")
    else:
        print("Reprovado")
    print("Sua média final foi", media)

#57  Elaborar um algoritmo que lê dois valores a e b e os escreve com a mensagem: “São múltiplos” ou “Não são múltiplos”. 
elif questao==57:
    a=int(input("Digite um numero a: "))
    b=int(input("Digite um numero b: "))
    x=(a%b)
    if(x==0):
        print ("Os números são multiplos")
    if(x!=0):
        print("Os números não são múltiplos")
#59  Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo. 
elif questao==59:
    n1=int(input("Digite um numero "))
    n2=(n1%2)
    if (n2==0):
        print(n1,"é par")
    else:
        print(n1,"é par.")
    if(n1>0):
        print(n1,"é positivo.")
    else:
        print(n1,"é negativo.")

#61 . Um usuário deseja um algoritmo pelo qual possa escolher que tipo de média
#deseja calcular a partir de três notas. Faça um algoritmo que leia as notas, a
#opção escolhida pelo usuário e calcule a média:
#1- aritmética
#2- ponderada (pesos 3, 3, 4) 
elif questao==61:
    n1 = float(input("Digite primeira nota:"))
    n2 = float(input("Digite segunda nota:"))
    n3 = float(input("Digite a terceira nota:"))
    x1 = (n1+n2+n3)/3
    y1 = (n1*3+n2*3+n3*4)/10
    a=int(input("Digite 1 para media aritmética, 2 para média ponderada:"))
    if(a==1):
          print("Sua média é: " +str(x1))
    if(a==2):
          print("Sua média é: " +str(y1))

#63  Um vendedor necessita de um algoritmo que calcule o preço total devido por um
#cliente. O algoritmo deve receber o código de um produto e a quantidade
#comprada e calcular o preço total
elif questao==63:
    codigo=int(input("Digite o código do produto:\n1001      5,32\n1324      6,45\n6548      2,37\n0987      5,32\n7623      6,45\nDigite aqui: "))
    quantidade=int(input("Digite a quantidade: "))
    if codigo==1001:
        print("O valor devido é",5.32*quantidade)
    if codigo==1324:
        print("O valor devido é",6.45*quantidade)
    if codigo==6548:
        print("O valor devido é",2.37*quantidade)
    if codigo==987:
        print("O valor devido é",5.32*quantidade)
    if codigo==7623:
        print("O valor devido é",6.45*quantidade)


#65 Crie um algoritmo em que o aluno digita duas notas bimestrais e informa se o
#aluno foi aprovado ou não. Nota: Considere aprovado se a nota for maior que 5.0. 
elif questao==65:
    nota_1=float(input("Digite a primeira nota: "))
    nota_2=float(input("Digite a segunda nota: "))
    media=(nota_1+nota_2)/2
    if ((media)>5):
       print("O aluno foi aprovado")
    else:
       print("O aluno foi reprovado")

#67 Não compilada :(
elif questao==67:
    x1=float(input("Digite o salario do funcionario: "))
    if(x1>=1500 and x1<1750):
        print("O aumento será de"(x1+(x1*12/100)))
    if(x1>1750 and x1<2000):
        print("O aumento será de"(x1+(x1*10/100)))
    if(x1>=2000 and x1<3000):
        print("O aumento será de"(x1+(x1*7/100)))
    if(x1>=3000):
        print("O aumento será de"(x1+(x1*5/100)))

#69
elif questao==69:
    print("Questão não resolvida")
    
#71 Crie um algoritmo que peça o nome, a altura e o peso de duas pessoas e
#apresente o nome da mais pesada e o nome da mais alta. 
elif questao==71:
    nome_1=input("Digite um nome:")
    peso_1=float(input("Digite peso da primeira pessoa: "))
    altura_1=float(input("Digite a altura da primeira pessoa em CM: "))
    nome_2=input("Digite o nome da segunda pessoa: ")
    peso_2=int(input("Digite um peso: "))
    altura_2=float(input("Digite altura da segunda pessoa: "))
    if(peso_1>peso_2):
        print("A pessoa mais pesada é a",nome_1)
    elif(peso_2>peso_1):
        print("A pessoa mais pesada é",nome_2)
    if(altura_1>altura_2):
        print("A pessoa mais pesada é",nome_1)
    elif(altura_2>altura_1):
        print("A pessoa mais alta é",nome_2)

#73 Faça um programa, utilizando estrutura de condição, que receba um número real,
#digitado pelo usuário e mostre o menu para selecionar o tipo de cálculo que deve ser realizado
elif questao==73:
    N1=int(input("Digite um número: "))
    print("Deseja que faça qual operação com o número?")
    n2=int(input("Escolha a operação a ser realizada\n101-Raiz Quadrada\n102-A metade\n103-10% do número\n104-O Dobro\nDigite aqui:"))
    if(n2==101):
        print("A raiz quadrada do número", N1,"é", (N1**(1/2)))
    if(n2==102):
        print("A metade do número", N1,"é", (N1/2))
    if (n2==103):
        print("O valor equivalente a 10% do", N1,"é", (N1/10))
    if (n2==104):
        print("O dobro do numéro", N1,"é", (N1*2))

#75 . Faça um programa que receba o valor da venda, escolha a condição de
#pagamento no menu e mostre o total da venda final conforme condições a seguir:
#Venda a Vista - desconto de 10%
#Venda a Prazo 30 dias - desconto de 5%
#Venda a Prazo 60 dias - mesmo preço
#Venda a Prazo 90 dias - acréscimo de 5%
#Venda com cartão de débito - desconto de 8%
#Venda com cartão de crédito - desconto de 7%
elif questao==75:
    n1=int(input("Digite o valor da venda: "))
    print("Como será realizado o pagamento?")
    n2=int(input("Escolha a forma de pagamento\n 1-À vista\n 2-Com 30 dias de prazo\n 3-60 dias de prazo\n 4-90 dias de prazo\n 5-No cartão de débito\n 6-No cartão de crédito\nDigite aqui:"))
    if (n2==1):
        print("O valor da sua compra é", (n1-(n1/10)))
    
    elif(n2==2):	
        print("O valor da sua compra é", (n1-(n1/20)))
    elif(n2==3):
        print("O valor da sua compra é", (n1))
    elif(n2==4):
        print("O valor da sua compra é", (n1+(n1/20)))
          
    elif(n2==5):
        print("O valor da sua compra é", (n1-(n1/100)*8))
    elif(n2==6):
        print("O valor da sua compra é", (n1-(n1/100)*7))

#77
elif questao==77:
    print("Questão não resolvida")

#79 . Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e
#mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo,
#Divorciado, Desquitado). Mostre uma mensagem de erro, se necessário
elif questao==79:
    print("Digite o numero correspondente a primeira letra do seu estado civil")
    x=int(input("1 para S\n2 para C\n3 para V\n4 para D\nDigite aqui:"))
    if (x==1):
        print("Você é Solteiro")
    if (x==2):
        print("Você é casado")
    if (x==3):
        print("Você é viuvo")
    if (x==4):
        print ("Você é divorciado/desquitado")

#81 . Crie um algoritmo para ler uma letra do alfabeto e mostrar uma mensagem: se é vogal ou consoante. 

elif questao==81:
    letra = input("Digite uma letra:")
    vogal="a"
    vogal_2="e"
    vogal_3="i"
    vogal_4="o"
    vogal_5="u"
    consoante="b"
    consoante_2="c"
    consoante_3="d"
    consoante_4="f"
    consoante_5="g"
    consoante_6="h"
    consoante_7="j"
    consoante_8="l"
    consoante_9="m"
    consoante_10="n"
    consoante_11="p"
    consoante_12="q"
    consoante_13="r"
    consoante_14="s"
    consoante_15="t"
    consoante_16="u"
    consoante_17="v"
    consoante_18="x"
    consoante_19="w"
    consoante_20="y"
    consoante_21="z"
    if (letra==vogal):
        print("É vogal")
    if (letra==vogal_2):
        print("É vogal")
    if (letra==vogal_3):
        print("É vogal")
    if (letra==vogal_4):
        print("É vogal")
    if (letra==vogal_5):
        print("É vogal")
    if (letra==consoante):
         print("É consoante")
    if (letra==consoante_2):
         print("É consoante")
    if (letra==consoante_3):
         print("É consoante")
    if (letra==consoante_4):
         print("É consoante")
    if (letra==consoante_5):
         print("É consoante")
    if (letra==consoante_6):
         print("É consoante")
    if (letra==consoante_7):
         print("É consoante")
    if (letra==consoante_8):
         print("É consoante")
    if (letra==consoante_9):
         print("É consoante")
    if (letra==consoante_10):
         print("É consoante")
    if (letra==consoante_11):
         print("É consoante")
    if (letra==consoante_12):
         print("É consoante")
    if (letra==consoante_13):
         print("É consoante")
    if (letra==consoante_14):
         print("É consoante")
    if (letra==consoante_15):
         print("É consoante")
    if (letra==consoante_16):
         print("É consoante")
    if (letra==consoante_17):
         print("É consoante")
    if (letra==consoante_18):
         print("É consoante")
    if (letra==consoante_19):
         print("É consoante")
    if (letra==consoante_20):
         print("É consoante")
    if (letra==consoante_21):
         print("É consoante")

#83
elif questao==83:
    print("Questão não resolvida")

#85 Faça um algoritmo para o jogo “pedra-papel-tesoura”. O jogo deve imprimir
#vitória, empate ou derrota conforme a opção que o jogador escolher e a opção
#que for sorteada aleatoriamente pelo computador. Obs.: pedra ganha de tesoura;
#que ganha de papel; que ganha de pedra.
elif questao==85:
    from random import randint
    x1=int(input("Digite o numero correspondente a sua escolha, 1-Papel,2-Pedra, 3- Tesoura:"))
    x2=randint(1,3)
    if(x2==1):
        print ("Seu adversario escolheu Papel")
    if (x2==2):
        print ("Seu adversario escolheu pedra")
    if(x2==3):
        print("Seu adversario escolheu tesoura")
    if(x1==1 and x2==1):
        print ("empate")
    if(x1==2 and x2==2):
        print ("empate")
    if(x1==3 and x2==3):
        print ("empate")
    if(x1==1 and x2==2):
        print ("Você venceu, papel enrola pedra")
    if(x1==1 and x2==3):
        print ("Você perdeu, Tesoura corta papel")
    if(x1==2 and x2==1):
        print ("Você perdeu, Papel enrola pedra")
    if(x1==2 and x2==3):
        print ("Você ganhou, pedra amassa tesoura")
    if(x1==3 and x2==1):
        print ("Você ganhou, tesoura corta papel")
    if(x1==3 and x2==2):
        print ("Você perdeu, pedra esmaga tesoura")

#87  Crie um algoritmo que solicita ao usuário para digitar um número e mostra-o por
#extenso. Este número deve variar entre 1 e 10. Se o usuário introduzir um
#número que não está neste intervalo, mostre: "Número inválido"
elif questao==87:
    x=int(input("Digite um numero entre 1 e 10:"))
    if (x==1):
        print("Um")
    elif (x==2):
        print("Dois")
    elif (x==3):
        print("Três")
    elif (x==4):
        print("Quatro")
    elif (x==5):
        print ("Cinco")
    elif (x==6):
        print ("Seis")
    elif (x==7):
        print ("Sete")
    elif (x==8):
        print ("Oito")
    elif (x==9):
        print("Nove")
    elif (x==10):
        print ("Dez")
    else:
        print("Número inválido")

else:
    print("Questão inválida")
