import platform
#from random_password_generator_lite import random_password as rand
#from pipe import *
import os
from sys import exit as e
from os import system as s
passwords = []
platform=platform.system().lower()
if platform=='windows':
	pass
try:
	print('Target: ', end='')
	target = input()
	target = target.strip()
	cont = target.split('.') if '.' in target else ['']
	if len(target)==0:
		target='passwords.txt'
	else:
		if cont[-1] != ('txt' or 'lst'):
			target=target+'.txt'
		del cont
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
	d = 0
	file = None
	splitter = '-' * 60
	while True:
		if file is None:
			print(splitter)
			print('File: ', end='')
			files = input()
			files=files.split('+')
			for file in files:
				if len(files)>1:	
					print('File:', file)
				recovery = file
				file = file.strip('.txt').replace('/', '\\')
				for_target = file.split('\\')[-1]
				# target1 = target.strip('.txt').split('\\')[-1]+'__'
				target1 = target.strip('.txt')+'__'
				# print(target1)
				filename_k = target1 + for_target + '_k.txt'
				# print(filename_k)
				filename_percent = target1 + for_target + '_percent.txt'
				# print(filename_percent)
				filename_a = target1 + for_target + '_a.txt'
				# print(filename_a)
				filename_n = target1 + for_target + '_n.txt'
				# print(filename_n)
				if len(file) == 0:
					e()
				file+='.txt'
				recovery+='.txt' if '.txt' not in recovery else ''
				try:
					with open(filename_k, 'r') as f:
						k = f.read()
				except FileNotFoundError:
					k = None
				k = 1 if k is None else (int(k) if k != '' else 1)
				try:
					with open(filename_percent, 'r') as f:
						percents = f.read()
						content = percents.split('\n')
						percent1 = content[0]
						percent = content[1]
				except FileNotFoundError:
					percent1 = percent = None
				percent1 = 0 if percent1 is None else (float(percent1) if percent1 != '' else 0)
				percent = 0 if percent is None else (float(percent) if percent != '' else 0)
				try:
					with open(filename_a, 'r') as f:
						a = f.read()
				except FileNotFoundError:
					a = None
				a = 1 if a is None else (int(a) if a != '' else 0)
				try:
					with open(filename_n, 'r') as f:
						n = f.read()
				except FileNotFoundError:
					n = None
				n = 1 if n is None else (int(n) if n != '' else 0)
				try:
					with open(file, 'r', encoding = 'utf-8') as f1:
						content = f1.read()
						content = content.split('\n')
						percent0 = len(content)
						content = content[k-1:]
				except FileNotFoundError:
					with open(recovery, 'r', encoding = 'utf-8') as f1:
						content = f1.read()
						content = content.split('\n')
						percent0 = len(content)
						content = content[k-1:]
				#print(percent0)
				for password in content:
					percent = round(k/percent0*100, 2)
					if percent>100.0:
						print('Complete 100.0%', end = '')
					else:
						string='Complete '+str(percent)+'%'
						string1=string.strip('%').split('.')
						if int(string1[-1])<10:
						    string+=' '
						print(string, end = ' ')
					k += 1
					f = open(target, 'a', encoding = 'utf-8')
					if password not in passwords:
						passwords.append(password)
						f.write(password + '\n')
						string = password+' added '
						a += 1
						f.close()
						with open(filename_a, 'w') as f_a:
							f_a.write(str(a))
						with open(filename_a, 'r') as f_a:
							a=int(f_a.read())
					else:
						string = password+' not added '
						n += 1
					with open(filename_n, 'w') as f_n:
						f_n.write(str(n))
					while len(string) < 40:
						string = ' '+ string
					print(string, end = '\r')
					#del content[0]
					#print(string, 'Owes:', len(content), end='\r')
					with open(filename_k, 'w') as f2:
						f2.write(str(k))
					with open(filename_percent, 'w') as f3:
						f3.write(str(percent1)+'\n'+str(percent))
				print('\nAdded:', a,'\tNot added:', n)
				print(splitter)
				os.remove(filename_percent)
				os.remove(filename_k)
				if os.path.exists(filename_a):
					os.remove(filename_a)
				if os.path.exists(filename_n):
					os.remove(filename_n)
				if os.path.exists('__pycache__'):
					os.remove('__pycache__')
						