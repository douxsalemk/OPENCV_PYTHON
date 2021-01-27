
import meu_modulo as mod

#Recebendo dados do usúario
try:
    vara = input('\ninsere o primeiro número ==> ' )
    varb = input('insere o segundo número ==>  ' )
except:
    print("Verifique que inseriu os dados da forma correta")



#somando
try:
    print('\nUtilizando a função "somar" ')
    print(f'\na soma de "{vara}" e "{varb}" é: {mod.somar(vara, varb)} \n')



    #instanciando o objeto somadois
    somando = mod.Somadois(vara, varb)
    print(somando.somar())

    print('\nUtilizando o metodo "somar" da classe "somadois" ')
    print(f'\na soma de "{vara}" e "{varb}" é: {somando.somar()} \n')
except:
    print("Desculpa! não consigo somar valor nao numerico")