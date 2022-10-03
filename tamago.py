import time, os, sys
#animação sono
def sono():
	x = 0
	while x < 5:
		f = open('sprite_sleep.txt','r')
		text = f.read()
		print(text)
		f.close()
		time.sleep(0.5)
		os.system('cls')
		f = open('sprite_sleep - 2.txt','r')
		text = f.read()
		print(text)
		f.close()
		time.sleep(0.5)
		os.system('cls')
		x = x + 1

def sprite():
	f = open('sprite_base.txt','r+')
	sprite_base = f.read()
	print(sprite_base)
	f.close()

def sprite_eat():
	x=0
	while x < 2:
		f = open('sprite_eat.txt', 'r')
		sprite_eat = f.read()
		print(sprite_eat)
		time.sleep(0.7)
		f.close()
		os.system('cls')
		f = open('sprite_eat - 2.txt', 'r')
		sprite_eat = f.read()
		print(sprite_eat)
		time.sleep(0.7)
		f.close()
		os.system('cls')
		x = x + 1
	

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
		if self.energia < 80:
			self.energia = self.energia + 20
			self.status()
			sono()
			print("{} descansou.".format(self.nome))
			print(self.energia)
		else:
			print("\nJá está descansado!")

	def ativ(self):
		self.energia = self.energia - 35
		self.fome = True
		#self.status()	
	def alimentar(self):
		if self.fome == True:	
			self.fome = self.fome
			self.fome = False
			self.energia = self.energia + 25
			sprite_eat()
		else:
			print("\nSem fome")
		

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

