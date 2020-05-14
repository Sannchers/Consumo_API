import requests  #importar pacote request
def main():
    print("#################")
    print("##CONSULTA CEP###")
    print("#################")

    cep_input = input ("Digite seu cep para consulta: ") # Entrada de dados
    if len(cep_input) != 8:      #retorna a quantidade de elementos contidos numa lista,
        print("Quantidade de digitos inválida")
        exit()
    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input)) #A função requests. get() obtém um recurso qualquer através de uma URL passada como argumento
    address_data = request.json()  #variável recebe resultado da requisição
    if "erro" not in address_data: #Se no dicionário não tem o atributo erro vai imprimir o resultado da solicitação
        print(">>>CEP ENCONTRADO<<<")
        print("CEP:{}".format(address_data["cep"]))
        print("Logradouro:{}".format(address_data["logradouro"]))
        print("Complemento:{}".format(address_data["complemento"]))
        print("Bairro:{}".format(address_data["bairro"]))
        print("Cidade:{}".format(address_data["localidade"]))
        print("Estado:{}".format(address_data["uf"]))
    else:
        print('{}:"Cep inválido.'.format(cep_input))  #se tem erro vai mostrar cep inválido

    option = int(input('Deseja realizar mais consultas?\n1. Sim\n2. sair\n')) #nova variável com a opção de prosseguir ou não
    if option == 1:
        main()
    else:
        print("Sessão encerrada!")
if __name__ == "__main__":
    main()







