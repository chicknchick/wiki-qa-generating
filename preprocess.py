#Ask Engine
#11-411 Project, Spring 2016
#Authored by Tia Jiang | tianyinj@andrew.cmu.edu


import re

def init(file_path):
	with open(file_path) as f:
		text = f.read()
	sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
	return sentences