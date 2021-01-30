import Levenshtein as lev
import pandas as pd

def isIdDifferent(person1, person2):
	return person1['id'] != person2['id']

def isDobSimilar(person1, person2):
	isSameYear = person1['year'] == person2['year']
	isSameMonth = person1['month'] == person2['month']
	isSameDay = person1['day'] == person2['day']
	return (isSameYear and isSameMonth) or (isSameMonth and isSameDay) or (isSameDay and isSameYear)

def isNameSimilarLevenshtein(person1, person2):
	return lev.distance(person1['name'], person2['name']) < 4

df = pd.read_csv('Persons.csv', header=None)
checkFrom = 0
checkTill = 1000
df.columns = ['id', 'subId', 'name', 'countryId', 'gender', 'year', 'month', 'day', 'comment', 'rails_id', 'incorrect_wca_id_claim_count']
for i in range(checkFrom, checkTill):
	curPerson = df.loc[i]
	for j in range(i):
		prevPerson = df.loc[j]
		if (
			isIdDifferent(curPerson, prevPerson) and
			isNameSimilarLevenshtein(curPerson, prevPerson) and
			isDobSimilar(curPerson, prevPerson)
		):
			print(curPerson['id'] + ' (' + curPerson['name'] + '), ' + prevPerson['id'] + ' (' + prevPerson['name'] + ')')