import time, os, pyfiglet
#animação sono
def sono():
	x = 0
	while x < 5:
		os.system('cls')
		f = open('sprite_sleep/sprite_sleep.txt','r')
		text = f.read()
		print(text)
		time.sleep(0.3)
		os.system('cls')
		f.close()
		f = open('sprite_sleep/sprite_sleep - 2.txt','r')
		text = f.read()
		print(text)
		time.sleep(0.3)
		os.system('cls')
		f.close()
		x = x + 1

def sprite():
	f = open('sprite_base/sprite_base.txt','r+')
	sprite_base = f.read()
	print(sprite_base)
	f.close()

def sprite_eat():
	x=0
	while x < 1:
		f = open('sprite_eat/sprite_eat.txt', 'r')
		sprite_eat = f.read()
		print(sprite_eat)
		time.sleep(0.7)
		f.close()
		os.system('cls')
		f = open('sprite_eat/sprite_eat - 2.txt', 'r')
		sprite_eat = f.read()
		print(sprite_eat)
		time.sleep(0.7)
		f.close()
		os.system('cls')
		f = open('sprite_eat/sprite_eat - 3.txt', 'r')
		sprite_eat = f.read()
		print(sprite_eat)
		time.sleep(0.7)
		f.close()
		os.system('cls')
		f = open('sprite_eat/sprite_eat - 4.txt', 'r')
		sprite_eat = f.read()
		print(sprite_eat)
		time.sleep(0.7)
		f.close()
		os.system('cls')
		f = open('sprite_eat/sprite_eat - 5.txt', 'r')
		sprite_eat = f.read()
		print(sprite_eat)
		time.sleep(0.7)
		f.close()
		os.system('cls')
		x = x + 1
	f = open('sprite_eat/sprite_eat - 6.txt', 'r')
	sprite_eat = f.read()
	print(sprite_eat)
	time.sleep(1.2)
	f.close()
	os.system('cls')
	
def sprite_brincar():
	x=0
	while x < 4:
		f = open('sprite_brincar/sprite_brincar.txt', 'r+')
		text = f.read()
		print(text)
		time.sleep(0.3)
		os.system('cls')
		f.close()
		f = open('sprite_brincar/sprite_brincar - 2.txt', 'r+')
		text = f.read()
		print(text)
		time.sleep(0.3)
		os.system('cls')
		f.close()
		f = open('sprite_brincar/sprite_brincar - 3.txt', 'r+')
		text = f.read()
		print(text)
		time.sleep(0.3)
		os.system('cls')
		f.close()
		x = x + 1

class Tamago:
	def __init__(self, nome='Tamago', fome=True, energia=70, life=True):
		self.nome = nome
		self.fome = fome
		self.energia = energia
		self.life = life

	def status(self):
		sprite()
		if self.fome == True:
			statusfome = "Com fome"
		if self.fome == False:
			statusfome = "Sem fome"
			#terminar aqui oh
		print("Tamago: {} ~ Fome: {} ~ Energia: {}".format(self.nome, statusfome, self.energia,))

	def decidir_atividade(self):	
		if self.energia >= 55:
			self.ativ()
		else:
			print("Sem energia")
			respcan = input("Brincar com tamago mesmo assim? ")
			if respcan == 's' and self.fome == True:
				x = 0
				while x < 2:
					x = x + 1
					self.life = False
					break
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
		sprite_brincar()
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
			
	def decisao(self):
		if self.life == True:
			self.interagir()
		elif self.life == False:
			print(pyfiglet.figlet_format("You  Die"))
			resp = input("Gostaria de reiniciar? ")
			if resp == 's':
				os.system('cls')
				self.life = True
				self.energia = 70
				self.fome = True
				self.interagir()
			else:
				os.system('cls')
				exit()
			
Nee = Tamago('Nee')
while True:
	Nee.decisao()