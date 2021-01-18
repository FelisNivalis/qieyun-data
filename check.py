from QieyunEncoder import from描述
import re

pattern = re.compile(r'[\x00-\x7F]')

def contains_ascii(s: str):
	'''
	Check if a string contains at least one ASCII character.
	'''
	return bool(pattern.match(s))

with open('data.csv') as f:
	next(f) # skip header
	for line in f:
		描述, 反切, 字頭, 解釋 = line.rstrip('\n').split(',')
		from描述(描述) # function from描述 will perform checks on 描述
		assert len(反切) in (2, 0), 'The length of 反切 should be 2, otherwise it should be an empty string'
		assert len(字頭) == 1, 'The length of 字頭 should be 1'
		assert not contains_ascii(解釋), '解釋 should not contain any ASCII characters'
