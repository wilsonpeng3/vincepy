__author__ = 'yangqi'
# -*- coding: utf-8 -*-

import math
import random

_number_of_team = 4

def get_namelist():
	return  ['ivan','sam','peter','flyher','andy','jack','sunwell','ramble','Fedor','ivy','leo','rocky','jason','stephen','lynn','cloudy','vince','bob']

def print_namelist(index_of_team,name_list):
	print 'Team:'+ str(index_of_team)
	for name in name_list:
		print name,
	print ''

def get_random():
	name_list = get_namelist()
	
	number_of_people = int(
	    math.ceil(
	        len(name_list)/float(_number_of_team)
	    )
	)

	for i in range(_number_of_team):
		if len(name_list) < number_of_people:
			number_of_people = len(name_list)

		temp_name_list = random.sample(name_list,number_of_people)
		print_namelist(i+1,temp_name_list)

		for name in temp_name_list:
			name_list.remove(name)



get_random()