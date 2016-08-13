# coding=UTF-8
import os
import getpass 
login_digitado=str
login_digitado2=str
confirmacao_senha=str
Vlogin=False
Vsenha=False
Vlogin2=False
Vsenha2=False
#teste

#procedimento criar tela de login. obs: só predefini usuario e senha porque o sistema de cadastro ainda não está funcionando, fiz isso apenas para simular um login na apresentação.
def salva(nome, login, senha):
    db = open('db.txt','a')
    db.write(nome+'\n')
    db.write(login+'\n')
    db.writelines(senha+'\n')
    db.close()

def tela_login(login=str, senha=str, Vlogin=bool, Vsenha=bool):
    print("")
    print("======================================================")
    print("======================================================")
    print("============= INSIRA SEU LOGIN E SENHA: ==============")
    print("======================================================")
    print("======================================================")
    #captura o nome de usuario digitado
    cont=0
    x=0
    dataset = open('db.txt','r')
    login_digitado = input("Digite seu nome de usuario: ")
    senha_digitada = getpass.getpass("Digite sua senha: ")
    for line in dataset:
        login=line
        senha=line
        if(login_digitado+"\n"==login):
            Vlogin=True
            print ("achado login")
            x=cont
        
        
        
       
        if(senha_digitada+"\n"==senha)and(cont==x+1)and (cont%2==0):
            Vsenha=True
            print("achado senha")
        cont=cont+1
        
    #captura a senha digitada
        
    
        


    #verfica se o login e a senha digitada corresposnde aos dados cadastrados
    if (Vlogin == True) and (Vsenha == True):
        #se a condição for verdadeira mostra a tela de opções
        os.system('clear')
        print("Jogador "+login_digitado+" logado com sucesso!")
        
    else:
        os.system('clear')
        erro_login()
    dataset.close()


def tela_login2(login2=str, senha2=str, Vlogin2=bool, Vsenha2=bool):
    print("")
    print("======================================================")
    print("======================================================")
    print("============= INSIRA SEU LOGIN E SENHA: ==============")
    print("======================================================")
    print("======================================================")
    #captura o nome de usuario digitado
    cont2=0
    y=0
    dataset = open('db.txt','r')
    login_digitado2 = input("Digite seu nome de usuario: ")
    senha_digitada2 = getpass.getpass("Digite sua senha: ")
    for line in dataset:
        login2=line
        senha2=line
        if(login_digitado2+"\n"==login2):
            Vlogin2=True
            print ("achado login")

           
        
        
       
        if(senha_digitada2+"\n"==senha2):
            Vsenha2=True
            print("achado senha")
        cont2=cont2+1
       
        
    #captura a senha digitada
        
    
        


    #verfica se o login e a senha digitada corresposnde aos dados cadastrados
    if (Vlogin2 == True) and (Vsenha2 == True):
        print("Jogador " +login_digitado2+" logado com sucesso!")
        print("")
        tela_jogo()

        
        
    else:
        #se a condição for falsa mostra a tela de erro de login
        
        erro_login2()

    dataset.close()

#procedimento para criar tela de cadastro
def tela_cadastro():
    print("======================================================")
    print("======================================================")
    print("============ Insira seus dados cadastrais: ===========")
    print("======================================================")
    print("======================================================")
    #captura o nome digitado pela pessoa
    nome=input("Digite seu nome e tecle enter: ")
    #captura o login digitado pela pessoa
    login=input("Digite seu login e tecle enter: ")
    #captura a senha digitada pela pessoa
    senha=getpass.getpass("Digite sua senha e tecle enter: ")
    confirmacao_senha=getpass.getpass("Repita sua senha e tecle enter: ")
    #exibe a mensagem que o cadastro foi efetuado com sucesso
    if(confirmacao_senha==senha):
       print("Cadastrado com sucesso! Faça login para acessar    as\n opções do jogo.")
       print("")
       salva(nome, login, senha)
       tela_login()
       
    else:
        while (confirmacao_senha!=senha):
          print("As senhas não correspondem, digite novamente sua senha!")
          senha=getpass.getpass("Digite sua senha e tecle enter: ")
          confirmacao_senha=getpass.getpass("Repita sua senha e tecle enter: ")
    print("Cadastrado com sucesso! Faça login para acessar    as\n opções do jogo.")
  
    salva(nome, login, senha)
    tela_login()


#procedimento para criar tela de erro de login
def erro_login():
    print("Usurio ou senha invalidos!")
    resposta=input("Para digitar novamente digite 1 e tecle enter, para cadastra novo usuario digite 2 e tecle enter: ")
    #verifica se o usuario quer repetir a tentativa de login ou ir pra tela de cadastro
    if(resposta=="1"):
        os.system('clear')
        tela_login()
    if(resposta=="2"):
        os.system('clear')
        tela_cadastro()
def erro_login2():
    print("Usurio ou senha invalidos!")
    resposta=input("Para digitar novamente digite 1 e tecle enter, para cadastra novo usuario digite 2 e tecle enter: ")
    #verifica se o usuario quer repetir a tentativa de login ou ir pra tela de cadastro
    if(resposta=="1"):
        os.system('clear')
        tela_login2()
    if(resposta=="2"):
        os.system('clear')
        tela_cadastro()

#procedimento para criar tela de voltar, sair ou jogar
def tela_voltar_sair():
    #captura a opção de qual tela mostrar ao usuario
    resposta = input("Para voltar a tela de opções digite 1 e tecle enter,\n para jogar digite 2 e tecle enter, 3 para sair: ")
    #verifica qual tela foi selecionada pelo usuario
    if (resposta == "1"):
        os.system('clear')
        tela_opcoes()
    if (resposta == "2"):
        os.system('clear')
        tela_jogo()
    if (resposta == "3"):
        os.system('clear')
        tela_sair()

#procedimento para criar tela de saída
def tela_sair():
    #captura a resposta do usuario em relação a mostra ou não a tela de saida
    pergunta=input("Tem certeza que deseja sair do jogo? sim/nao: ")
    #verificar se a opção foi por mostra a tela de saida
    if((pergunta=="sim") or (pergunta=="s")):
        os.system('clear')
        print("======================================================")
        print("======================================================")
        print("=========== Obrigado por jogar. Até logo ;) ==========")
        print("======================================================")
        print("======================================================")
    if((pergunta=="nao") or (pergunta=="não") or (pergunta=="n")):
        os.system('clear')
        tela_opcoes() 

#procedimento para criar tela de opções do jogo
def tela_opcoes():
    print("")
    print("======================================================")
    print("======================================================")
    print("============= BEM VINDO AO JOGO DA CERCA =============")
    print("============ ESCOLHA UMA DAS OPÇÕES ABAIXO ===========")
    print("======================================================")
    print("======================================================")
    print("")
    print("Para iniciar o jogo, digite o numero 1 e tecle enter.")
    print("Para ver as instruções, digite o numero 2 e tecle enter.")
    print("Para ver o ranking, digite o numero 3 e tecle enter.")
    print("Para sair, digite o numero 4 e tecle enter.")
    print("")
    #mostra a tela corresponde a opção digitda pelo usuario

    print((mostra_tela()))

#procedimento para criar tela de indtruções do jogo
def tela_instrucoes():
    print("======================================================")
    print("======================================================")
    print("================= INSTRUÇÕES DO JOGO: ================")
    print("======================================================")
    print("======================================================")
    print("")
    print("Para cada jogada a ser execultada é necessario informar\n as coordenadas (linha e coluna) dos dois pontos    que\n deseja interligar. Ex: ligar o ponto 1,1 no ponto 1,2,\n sendo que o primeiro número faz referencia a linha,  e\n o segundo a coluna. ")
    #exibe a tela que da ao usuario a opção de voltar a tela de oções, ir para o jogo ou sair do jogo
    print("")
    tela_voltar_sair()

#procedimento para criar tela do jogo


            #se a resposta for negativa volta a ler as jogadas

#procedimento para criar a tela de ranking
def tela_ranking():
    print("1º Colocado: Matheus Alves com 20 vitórias.")
    print("2º Colocado: Neymar com 18 vitórias.")
    print("3º Colocado: Messi com 14 vitórias.")
    print("4º Colocado: Pelé com 12 vitórias.")
    print("5º Colocado: Maradona com 10 vitórias.")
    # exibe a tela que da ao usuario a opção de voltar a tela de oções, ir para o jogo ou sair do jogo
    print("")
    tela_voltar_sair()

#função que verifica qual tela o usuario quer ver e retorna a tela solicitada
def mostra_tela():
    #captura o numero correspondente a escolha de tela do usuario
    escolha=input("Digite o número correspondente a sua escolha: ")

    if(escolha=="1"):
        #chama a tela do jogo
        os.system('clear')
        tela_pergunta()
    if(escolha=="2"):
        #chama a tela de instruções
        os.system('clear')
        tela_instrucoes()
    if(escolha=="3"):
        #chama a tela do ranking
        os.system('clear')
        tela_ranking()
    if(escolha=="4"):
        #chama a tela de saida
        os.system("clear")
        tela_sair()
    #retorna para a função qual tela foi escolhida
    return escolha


#procedimento para criar a tela do jogo
    
def tela_jogo():
    print("    C    1         2        3        4")
    print("")
    print("L")
    print("")
    print("1        O---------O        O        O")
    print("         |         |")
    print("         |    M    |")
    print("         |         |")
    print("2        O---------O        O        O")
    print("")
    print("")
    print("")
    print("3        O         O        O        O")
    print("")
    print("")
    print("")
    print("4        O         O        O        O")
    print("")
    print("Digite 0 (zero) e tecle enter a qualquer momento\n para voltar a tela inicial.")
    #define um valor para a jogada
   
    #repete a leitura da jogada de cada jogar enquanto a jogada for diferente no numero 0
    while(True):
        jogada1 = int(eval(input("Vez do jogador "+str(login_digitado)+" :")))
        if (jogada1 == 0) :
            # se a jogada for 0, pergunta se o usuario realmente deseja abandonar a partida
            confirmacao = input("Tem certeza que deseja abandonar a partida? sim/nao: ")
            #se a resposta for positiva, mostra a tela de opções
            if ((confirmacao == "sim") or (confirmacao=="s")):
                os.system('clear')
                tela_opcoes()

        jogada2 = int(eval(input("Vez do jogador "+str(login_digitado2)+ " :")))
        if (jogada2==0):
            # se a jogada for 0, pergunta se o usuario realmente deseja abandonar a partida
            confirmacao = input("Tem certeza que deseja abandonar a partida? sim/nao: ")
            #se a resposta for positiva, mostra a tela de opções
            if ((confirmacao == "sim") or (confirmacao=="n")):
                os.system('clear')
                tela_opcoes()


def tela_pergunta():
    login1=input("Jogador 1 já possui cadastro no jogo? Digite 'sim' e tecle enter\n caso tenha, ou digite 'não' e tecle enter para criar\n novo cadastro: ")
    if((login1=="sim") or (login1=="s")):
     #mostra a tela de login
         os.system('clear')
         tela_login()
    if((login1=="nao") or (login1=="não") or (login1=="n")):
        #mostra a tela de cadastro
        os.system('clear')
        tela_cadastro()
    
    print("")

    login2=input("Jogador 2 já possui cadastro no jogo? Digite 'sim' e tecle enter\n caso tenha, ou digite 'não' e tecle enter para criar\n novo cadastro: ")
    if((login2=="sim") or (login2=="s")):
     #mostra a tela de login
         os.system('clear')
         tela_login2()
    if((login2=="nao") or (login2=="não") or (login1=="n")):
        #mostra a tela de cadastro
        os.system('clear')
        tela_cadastro()

    print("")

    
#mostra a tela de opções no inicio do jogo
tela_opcoes()






