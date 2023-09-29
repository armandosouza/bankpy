from modules.conta import Conta
from modules.clientes import Cliente
from sys import exit
from os import system

menu = """
[1] - Criar usuário
[2] - Criar conta bancária
[3] - Acessar BankPy
[4] - Sair
"""

while True:
	print(menu)
	option = input("Digite sua opção: ")
	if option == '1':
		nome = input("Digite seu nome: ")
		logradouro = input("Digite o logradouro do seu endereço: ")
		numero = input("Digite o número da sua residência: ")
		bairro = input("Digite o bairro: ")
		cidade = input("Digite a cidade: ")
		siglaEstado = input("Digite a sigla do estado: ")
		endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{siglaEstado}"
		cpf = input("Digite seu CPF: ")
		dataNascimento = input("Digite sua data de nascimento (dd/mm/yyyy): ")
		try:
			cliente = Cliente(nome, endereco, dataNascimento, cpf)
		except Exception as e:
			print(e)
	elif option == '2':
		try:
			cpf = input("Digte seu CPF: ").strip().replace('-', '').replace('.', '')
			Cliente.verificarUsuario(cpf)
			conta = Conta(cpf)
		except Exception as e:
			print(e)
	elif option == '3':
		system('cls')
		try:
			numeroConta = int(input("Digite o número da sua conta: "))
			cpf = input("Digite o seu CPF: ").strip().replace(".", "").replace("-", "")
			conta = Conta.verificarUsuario(numeroConta, cpf)

			while True:
				menuPrincipal = """
					[1] - Ver saldo
					[2] - Sacar
					[3] - Depositar
					[4] - Ver extrato
					[5] - Sair
				"""
				print(menuPrincipal)
				option = input("Digite sua opção: ")
				if option == "1":
					Conta.verSaldo(conta)
				elif option == "2":
					saque = float(input("Digite o valor para saque: R$ "))
					Conta.sacar(conta, saque)
				elif option == "3":
					deposito = float(input("Digite o valor para depositar: R$ "))
					Conta.depositar(conta, deposito)
				elif option == "4":
					Conta.verExtrato(conta)
				elif option == "5": 
					break
		except Exception as e:
			print(e)
	elif option == '4':
		exit(1)