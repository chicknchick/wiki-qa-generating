#Ask Engine
#11-411 Project, Spring 2016
#Authored by Tia Jiang | tianyinj@andrew.cmu.edu

import sys
import ask_sys
import preprocess

def main(argv):

	file_path = argv[1]
	num_questions = argv[2]

	extract_sentences = preprocess.init(file_path)

	questions = ask_sys.init(extract_sentences)

	for question in questions:
		print(question)



if __name__ == '__main__':
	main(sys.argv)