class Conta:
	def __init__(self):
		self._saldo = 0
		self._extrato = []
		self.limite = 500

	def verSaldo(self):
		print(F"R$ {self._saldo:.2f}")

	def depositar(self, valor):
		self._saldo = self._saldo + valor
		self._extrato.append(f"R$ {valor:.2f} foi depositado na conta.")
		print(f"Você depositou R$ {valor:.2f} na sua conta!")

	def sacar(self, valor):
		if valor > self.limite:
			raise Exception("Limite já foi excedido por hoje!")
		self._saldo = self._saldo - valor
		self.limite = self.limite - valor
		self._extrato.append(f"R$ {valor:.2f} foi sacado da conta.")
		print(f"Você sacou R$ {valor:.2f} da sua conta!")

	def verExtrato(self):
		for op in self._extrato:
			print(f"-> {op}")