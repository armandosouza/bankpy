contas = []

class Conta:
	def __init__(self, cpf):
		conta = {
			'saldo': 0,
			'extrato': [],
			'agencia': '0001',
			'limite': 500,
			'limiteOperacoes': 3,
			'conta': len(contas) + 1,
			'usuario': cpf
		}
		print(conta)
		contas.append(conta)


	@staticmethod
	def verificarUsuario(conta, usuario):
		for c in contas:
			if c["conta"] == conta and c["usuario"] == usuario:
				return c
		raise Exception('Conta não encontrada no sistema!')


	@staticmethod
	def verSaldo(conta):
		saldo = conta["saldo"]
		print(F"R$ {saldo:.2f}")


	@staticmethod
	def depositar(conta, valor):
		conta["saldo"] += valor
		conta["extrato"].append(f"R$ {valor:.2f} foi depositado na conta.")
		print(f"Você depositou R$ {valor:.2f} na sua conta!")


	@staticmethod
	def sacar(conta, valor):
		if valor > conta["limite"]:
			raise Exception("Limite já foi excedido por hoje!")
		elif conta["limiteOperacoes"] == 0:
			raise Exception("Limite de operações já foi excedido!")
		elif valor > conta["saldo"]:
			raise Exception("Saldo insuficiente!")
		conta["saldo"] -= valor
		conta["limite"] -= valor
		conta["limiteOperacoes"] -= 1
		conta["extrato"].append(f"R$ {valor:.2f} foi sacado da conta.")
		print(f"Você sacou R$ {valor:.2f} da sua conta!")


	@staticmethod
	def verExtrato(conta):
		for op in conta["extrato"]:
			print(f"-> {op}")