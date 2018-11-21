from datetime import date
import time
from datetime import datetime, timedelta
now = datetime. now()
i=0
code = []
marca = []
modelo = []
ano = []
valorD = []
estatus = []
dias = []
codigo = 0
hoje = date.today()
alugados = 0
reservados = 0

while i==0 :
    #primeiro menu
    print('==============================SEJA BEM VINDO !!!==============================')
    print("DATA ATUAL: " ,hoje)

    print('Quatidade de veiculos cadastrados: ',codigo)
    print('Quatidade de veiculos alugados: ',alugados)
    print('Quatidade de veiculos reservados: ',reservados)
    dia = now.day
    
    print('dia: ',dia)
    def  menu():

        print('1-Consultar veículos')
        print('2-Adiconar veículos')
        print('3-Alugar/reservar veículos')
        print('4-Devolver/liberar veículos')
        print('5-Excluir veículos')
        print('6-Avançar data atual')
        print('7-Sair')

        opcao = (int)( input('Escolha a opção desejada:'))
        
        return opcao
    resposta = menu()

    #função 2
    if resposta == 2:

        codigo = codigo+1
        code.append(codigo)
        status = 'disponivel'
        estatus.append(status)

        d = (input('Marca do carro: '))
        marca.append(d)

        e = (input('Modelo do carro: '))
        modelo.append(e)

        f = (input('Ano do carro: '))
        ano.append(f)

        g = (input('valor da diaria: '))
        valorD.append(g)
        
    if resposta == 1:#funcção 1
        print('Deseja uma opção mais detalhada ? Digite 100 e aperte enter: ')
        print('Codigo:',code,'modelo:',modelo, 'estatus:',estatus)
        
    if resposta == 100:
            print('marca:',marca,'ano:',ano, 'valor da diaria',valorD)
            
    if resposta == 3:#função 3
        (input('Qual o seu nome: '))
        alRes =(input('Voce deseja alugar ou reservar, alugar digite 1 reservar digite 2:'))
        if  alRes == '1':
            data = (int)(input('Por quanto dias você deseja alugar o carro ? Máximo de 30 dias: '))
            carro =(int)(input('Digite o codigo do veiculo que deseja alugar: '))
            dias.append(data)
            if data <= 30:            
                if data in dias:
                     if carro in code:#parte de reserva
                            carro = carro-1
                            if estatus[carro] == 'disponivel':
                                estatus[carro] = 'alugado'
                                print('veículo alugado')
                            else:
                                print('veiculo não pode ser alugado, tente outro por favor')
                
            alugados = alugados+1
        if  alRes == '2':
            data = (int)(input('Por quanto dias você deseja reservar o carro ? Máximo de 30 dias: '))
            carro =(int)(input('Digite o codigo do veiculo que deseja reservar: '))
            dias.append(data)
            if data <= 30:            
                if data in dias:
                     if carro in code:#parte de reserva
                            carro = carro-1
                            if estatus[carro] == 'disponivel':
                                estatus[carro] = 'reservado'
                                print('veículo reservado')
                            else:
                                print('veiculo não pode ser reservado, tente outro por favor')
            reservados = reservados+1
                            
    if resposta == 6:#passagem de  o tempo
        futuro=date.fromordinal(hoje.toordinal()+1)
        hoje=futuro
        
    if resposta == 5:
            remove =(int)(input('Digite o codigo do veiculo que deseja excluir : '))
            if remove in code:#parte de remover veículo
                            remove = remove-1
                            if estatus[remove] == 'disponivel':
                                del estatus[remove]
                                del code[remove]
                                del marca[remove]
                                del modelo[remove]
                                del ano[remove]
                                del valorD[remove]
                                codigo = codigo - 1
                                print('veículo removido do sistema! ')
                                
                        
    #if resposta == 4:
        
        
            
    if resposta == 7:
        break
    
        
        
