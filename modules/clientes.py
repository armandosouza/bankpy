clientes = []

class Cliente:
	def __init__(self, nome, endereco, dataNascimento, cpf):
		cpf = cpf.strip().replace('.', '').replace('-', '')
		for c in clientes:
			if c['cpf'] == cpf:
				raise Exception('Cliente já cadastrado!')
		cliente = {
			'nome': nome,
			'endereco': endereco,
			'dataNascimento': dataNascimento,
			'cpf': cpf
		}
		clientes.append(cliente)


	@staticmethod
	def verificarUsuario(cpf):
		for c in clientes:
			print(c)
			if c["cpf"] == cpf:
				return c
		raise Exception("Cliente não encontrado no sistema! Registre-se!")


	def listarClientes(self):
		for c in clientes:
			print(c)