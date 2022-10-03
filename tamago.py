import time, os, sys
#animação sono
def sono():
	x = 1
	while x < 5:
		os.system('cls')
		x = x + 1
		print("z")
		time.sleep(1)
		os.system('cls')
		print("zZ")
		time.sleep(1)
		os.system('cls')
		print("zzZ")
		time.sleep(1)
		os.system('cls')

def sprite():
	print("       . ")
	print("     _ \ \   .")
	print("    | \|   \|  \ ")
	print("    | /      \  |")
	print("    /          \|")
	print("  /    |. |     |")
	print(" |    _______ _   |")
	print(" \. /          \ ./")
	print("   '-__________-' ")

class Tamago:
	def __init__(self, nome='Tamago', fome=False, energia=100):
		self.nome = nome
		self.fome = fome
		self.energia = energia

	def status(self):
		sprite()
		print("Tamago: {} ~ Fome: {} ~ Energia: {}".format(self.nome, self.fome, self.energia,))
		if self.energia == 0:
			print("Você morreu")

	def decidir_atividade(self):	
		if self.energia >= 55:
			resp = input('Brincar com Tamago: ')
			if resp == 's':
				self.ativ()
			elif resp == 'n':
				self.energia = self.energia
				print("{} vai descansar".format(self.nome))
				self.descansar()
		else:
			print("Sem energia")
	
	#atividades fisicas
	def descansar(self):
		self.energia = self.energia + 50
		self.status()
		sono()
		print("{} descansou.".format(self.nome))
		print(self.energia)
	def ativ(self):
		self.energia = self.energia - 35
		self.fome = True
		#self.status()	
	def alimentar(self):	
		self.fome = self.fome
		self.fome = False
		self.energia = self.energia + 25
		

	def interagir(self):
		self.status()
		inte = input("Como deseja interagir?\n1 ~ brincar\n2 ~ descansar\n3 ~ alimentar\n")
		if inte == '1':
			os.system('cls')
			self.decidir_atividade()
		elif inte == '2':
			os.system('cls')
			self.descansar()
		elif inte == '3':
			os.system('cls')
			self.alimentar()
			

Nee = Tamago('Nee')
while True:
	Nee.interagir()

