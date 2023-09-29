from conta import Conta

conta = Conta()
try:
	conta.depositar(250)
	conta.sacar(125.75)
	conta.verSaldo()
	conta.depositar(135.50)
	conta.sacar(187.44)
	conta.verExtrato()
	conta.depositar(135.50)
	conta.sacar(187.44)
except Exception as e:
	print(e)