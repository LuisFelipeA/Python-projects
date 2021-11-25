#O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Mercadinho BigBom
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0

qtd_compra = [] #quantidade de compras feitas

while(True):
    
    qtd_compra.append(1)
    print(f"Compra {len(qtd_compra)}")

    preco_produto = 1 #representa o valor de cada produto
    total_compra = 0 #representa o total da compra
    np = 1 #número do produto
    pagamento = 0 #valor pago pelo cliente
    troco = 0 #troco do cliente

    while(preco_produto != 0):
        preco_produto = float(input(f"Informe o preço do produto {np}: R$"))
        total_compra = total_compra + preco_produto
        np = np+1
    
    print(f"Total da compra: R${total_compra:.2f}")
    pagamento = float(input("Pagamento: R$"))

    while(pagamento < total_compra):
        print("Pagamento inválido, faça novamente!")
        pagamento = float(input("Pagamento: R$"))

    troco = pagamento - total_compra

    print(f"Troco: R${troco:.2f}")

    print("Luis Felipe Adriani")
    print("RA: 1922432")