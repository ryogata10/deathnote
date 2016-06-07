#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

def death_note():
	name = input('名前をご記入ください。')
	start = datetime.datetime.now()

	cause_of_death = input('人間界単位で40秒以内に死因をご記入ください。')
	cause_limit = datetime.datetime.now()

	time = cause_limit - start
	time = time.total_seconds()
	print(time)

	if cause_of_death == "":
	    cause_of_death = "心臓麻痺"

	if time < 40:
		cause_of_death = "心臓麻痺"

	death_time = cause_limit.strftime("%Y/%m/%d %H:%M:%S")
	death_time = str(death_time)

	text_one = name + "さんは"
	text_two = cause_of_death + "のため"
	text_three = death_time + "に亡くなりました"
	text = (text_one + text_two + text_three)
	return text

if __name__ == '__main__':
	print(death_note())
