from random import *


def goalKeepingFirst():
	pg = cg = time = 0
	while time < 90:
		i = int(input("Enter your save: "))
		if i < 0 or i > 6:
			exit(3)
			pass
		else:
			j = randrange(0, 7)
			print("Computer chooses " + str(j))
			if i == j:
				print("Computer scores a goal!")
				cg += 1
				pass
			else:
				if j == 0:
					time = time + i
					pass
				else:
					time = time + j
					pass
				print('Elapsed time is ' + str(time))
				pass
			pass
		pass
	print("Computer scores " + str(cg))
	target = cg + 1
	print("Your target is " + str(target))
	time = 0
	while time < 90 and pg < target:
		i = int(input("Enter your shot: "))
		if i < 0 or i > 6:
			exit(3)
			pass
		else:
			j = randrange(0, 7)
			print("Computer chooses " + str(j))
			if i == j:
				print("You scored a goal")
				pg += 1
				pass
			else:
				if i == 0:
					time = time + j
					pass
				else:
					time = time + i
					pass
				print("Elapsed time is " + str(time))
				pass
			pass
		pass
	decider(pg, cg)
	pass


def kickingFirst():
	pg = cg = time = 0
	while time < 90:
		i = int(input("Enter your shot: "))
		if i < 0 or i > 6:
			exit(3)
			pass
		else:
			j = randrange(0, 7)
			print("Computer chooses " + str(j))
			if i == j:
				print("You scored a goal.")
				pg += 1
				pass
			else:
				if i == 0:
					time = time + j
					pass
				else:
					time = time + i
					pass
				print("Elapsed time is " + str(time))
				pass
			pass
		pass
	print("You score " + str(pg))
	target = pg + 1
	print("Computer target is " + str(target))
	time = 0
	while time < 90 and cg < target:
		i = int(input("Enter your save: "))
		if i < 0 or i > 6:
			exit(3)
			pass
		else:
			j = randrange(0, 7)
			print("Computer chooses " + str(j))
			if i == j:
				print("Computer scored a goal")
				cg += 1
				pass
			else:
				if j == 0:
					time = time + i
					pass
				else:
					time = time + j
					pass
				print("Elapsed time is " + str(time))
				pass
			pass
		pass
	decider(pg, cg)
	pass


def decider(a, b):
	if a > b:
		print("You won.")
		pass
	elif a < b:
		print("Computer won.")
		pass
	else:
		print("Match draws.")
		pass
	input()
	exit(0)
	pass


if __name__ == '__main__':
	print("Always enter 1 for heads or 2 for tails.")
	print("Always enter 1 for kicking or 2 for goalkeeping.")
	toss = int(input("Enter the toss: "))
	if toss > 2 or toss < 1:
		exit(1)
		pass
	else:
		cToss = randrange(1, 3)
		if toss == cToss:
			print("You won the toss.")
			choose = int(input("Enter your choose: "))
			if choose > 2 or choose < 1:
				exit(2)
				pass
			else:
				if choose == 1:
					kickingFirst()
					pass
				else:
					goalKeepingFirst()
					pass
				pass
			pass
		else:
			print("You lost the toss..")
			cChoose = randrange(1, 3)
			if cChoose == 1:
				print("Computer chooses kicking")
				goalKeepingFirst()
				pass
			else:
				print("Computer chooses goalkeeping")
				kickingFirst()
				pass
			pass
		pass
	pass
