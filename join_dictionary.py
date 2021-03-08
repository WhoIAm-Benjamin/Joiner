from sys import exit as e
from os import remove as r
from os import system as s
passwords = []
try:
	print('Target: ', end='')
	target = input()
	if len(target) == 0:
		s('cls')
		target = 'passwords'
		print('Target:', target)
	target = target.strip()
	if '.txt' not in target:
		target+='.txt'
	with open(target, 'r', encoding = 'utf-8') as f:
		content = f.read()
		content = content.split('\n')
		for i in content:
			passwords.append(i)
except FileNotFoundError:
	pass
finally:
	a = 0
	n = 0
	l = 0
	while True:
		print('--------------------------------------')
		print('File: ', end = '')
		file = input()
		if len(file) == 0:
			e()
		if 'txt' not in file:
			file += '.txt'
		try:
			with open(file+'k.txt', 'r') as f:
				k = f.read()
		except FileNotFoundError:
			k = None
		if k is None:
			k = 1
		else:
			if k != '':
				k = int(k)
			else:
				k = 1
		try:
			with open(file+'percent.txt', 'r') as f:
				percents = f.read()
				content = percents.split('\n')
				percent1 = content[0]
				percent = content[1]
		except FileNotFoundError:
			percent1 = None
			percent = None
		if percent1 is None:
			percent1 = 0
		else:
			if percent1 != '':
				percent1 = float(percent1)
			else:
				percent1 = 0
		if percent is None:
			percent = 0
		else:
			if percent != '':
				percent = float(percent)
			else:
				percent = 0
		try:
			with open(file+'a.txt', 'r') as f:
				a = f.read()
		except FileNotFoundError:
			a = None
		if a is None:
			a = 1
		else:
			if a != '':
				a = int(a)
			else:
				a = 0
		try:
			with open(file+'n.txt', 'r') as f:
				n = f.read()
		except FileNotFoundError:
			n = None
		if n is None:
			n = 1
		else:
			if n != '':
				n = int(n)
			else:
				n = 0
		with open(file, 'r', encoding = 'utf-8') as f1:
			content = f1.read()
			content = content.split('\n')
			percent0 = len(content) / 100
			print(percent0)
			content = content[k-1:]
			for password in content:
				k += 1
				if k/10 > (percent1 / 10):
					percent1 += percent0 / 10
					percent += 0.1
					percent = round(percent, 1)
				if percent == '100.1':
					print('Complete 100.0%', end = '')
				elif percent == '100.0' and k < len(content):
					print('Complete 99.9%', end = '')
				else:
					print('Complete '+str(percent)+'%', end = '')
				f = open(target, 'a', encoding = 'utf-8')
				if password not in passwords:
					passwords.append(password)
					f.write(password + '\n')
					string = password+' added'
					while len(string) < 40:
						string = ' '+ string
					print(string, end = '\r')
					a += 1
					f.close()
				else:
					string = password+' not added'
					while len(string) < 40:
						string = ' '+ string
					print(string, end = '\r')
					n += 1
				with open(file+'k.txt', 'w') as f2:
					f2.write(str(k))
				with open(file+'percent.txt', 'w') as f3:
					f3.write(str(percent1)+'\n'+str(percent))
				with open(file+'a.txt', 'w') as f_a:
					f_a.write(str(a))
				with open(file+'n.txt', 'w') as f_n:
					f_n.write(str(n))
			print('\nAdded:', a,'\tNot added:', n)
			r(file+'percent.txt')
			r(file+'k.txt')
			r(file+'a.txt')
			r(file+'n.txt')
			file=None
				