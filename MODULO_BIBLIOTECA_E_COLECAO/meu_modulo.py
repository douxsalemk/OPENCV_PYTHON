# funcao para somar dois numeros inteiros

def somar (numa , numb):
    numa= float(numa)
    numb= float(numb)
    return numa + numb
#------------------------------------------------------------------------------

#classe para somar 2 num int utilisando o método somar.


class Somadois:
    
    def __init__(self, numa, numb):
        self.__numa = numa
        self.__numb = numb

    def somar (self):
        numa = float(self.__numa)
        numb = float(self.__numb)
        return numa + numb


#------------------------------------------------------------------------------

if __name__ == "__main__":
    #Recebendo dados do usúario

    try:
        vara = input('\ninsere o primeiro número ==> ' )
        varb = input('insere o segundo número ==>  ' ) 
    except:
        print("Verifique que inseriu os dados da forma correta")



    #somando
    try:
        print('\nUtilizando a função "somar" ')
        print(f'\na soma de "{vara}" e "{varb}" é: {somar(vara, varb)} \n')


        #instanciando o objeto somadois
        somando = Somadois(vara, varb)
        print("=============================================================")
        print('\nUtilizando o metodo "somar" da classe "somadois" ')
        print(f'\na soma de "{vara}" e "{varb}" é: {somando.somar()} \n')
    except:
        print("Desculpa! não consigo somar valor nao numerico")
