import random
import os.path
FILENAME = 'data.log'

dic = {'r':'Rock', 'p':'Paper','s':'Scissors'}

class RPS():
	def __init__(self):
		self.exit_flag = False
		self.c_choice = None
		self.p_choice = None
		self.pwin = 0
		self.cwin = 0
		self.tie = 0
		self.player_history = self.data = []
		if os.path.isfile(FILENAME):
			with open(FILENAME) as input:
				print 'Loading File...\n'
				self.data = [line.strip() for line in input]
		else:
			for i in range(0, 9):
				self.data.append(random.choice(['r','p','s']))
		for i in range(0, 9):
			self.player_history.append(random.choice(['r','p','s']))
		
	def play(self):
		print '\n\n'+'_'*20 + 'NEW GAME' +'_'*20
		valid = ['r', 'p', 's']
		self.p_choice = c_choice = None
		while self.p_choice not in valid:
			self.p_choice = raw_input("Choose Rock(r), Paper(p), or Scissors(s) [Type 'e' to exit]\n")
			if self.p_choice == 'e':
				self.exit()
		self.c_choice = self.computerDecide()
		self.compare(self.p_choice, self.c_choice)
		self.update(self.p_choice)
			
	def computerDecide(self):
		size = 10
		offset = len(self.data) - size - 2
		match = False
		prob = {'r':0, 'p':0, 's':0}
		decision = None
		max_value = 0
		while((not match) or (offset > 0)):
			#print 'Offset: ' + str(offset) + '\tSize: ' + str(size)
			#print 'no match'
			guess_pattern = []
			if offset < 0:
				size -= 1
				offset = len(self.data) - size - 2
			for i in range(0+offset,size+offset):
				guess_pattern.append(self.data[i])
			if guess_pattern == self.player_history[9-size:10]:
				match = True
				#print str(guess_pattern) + ' == ' + str(self.player_history[9-size:10]) + ' Next value: ' + str(self.data[size+offset+1])
				prob[str(self.data[size+offset])] += 1
				offset -= 1
			else:
				offset -= 1
		for key,value in prob.items():
			if value > max_value:
				decision = key
				max_value = value
		return self.winning(decision)
		
	def winning(self, x):
		if x == 'r':
			return 'p'
		elif x =='p':
			return 's'
		else:
			return 'r'
	
	def compare(self, player, cpu):
		print '\nPlayer chose: ' + dic[player] + '\nComputer chose: ' + dic[cpu]
		if player == cpu:
			print "Tie Game"
			self.tie += 1
		if player == 'r':
			if cpu == 'p':
				print 'Computer Wins!'
				self.cwin += 1
			elif cpu == 's':
				print 'Player Wins!'
				self.pwin += 1
		elif player == 'p':
			if cpu == 's':
				print 'Computer Wins!'
				self.cwin += 1
			elif cpu == 'r':
				print 'Player Wins!'
				self.pwin += 1
		elif player == 's':
			if cpu == 'r':
				print 'Computer Wins!'
				self.cwin += 1
			elif cpu == 'p':
				print 'Player Wins!'
				self.pwin += 1
		print '\nPlayer Wins: ' + str(self.pwin)
		print 'Computer Wins: ' + str(self.cwin)
		print 'Number of Ties: ' + str(self.tie)	
		
	def update(self, player):
		self.data.append(player)
		del self.player_history[0]
		self.player_history.append(player)
	
	def exit(self):
		print '\n\nSaving games.\nPlease wait or data wil be lost...'
		with open(FILENAME, 'w') as output:
			for line in self.data:
				output.write(line + '\n')
			exit()
			
		

if __name__ == '__main__':
	game = RPS()

	while(not game.exit_flag):
		game.play()
