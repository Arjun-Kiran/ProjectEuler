
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# NOT SOLVED 

import sys,os,math,re

def parseDate(sDate):
	tDate = sDate.split('/');

	month = int(tDate[0]);
	day = int(tDate[1]);
	year = int(tDate[2]);

	return day,month,year;

def parseDay(sDate):
	tDate = parseDate(sDate)

	return tDate[0];

def parseMonth(sDate):
	tDate = parseDate(sDate)

	return tDate[1];

def parseYear(sDate):
	tDate = parseDate(sDate)
	return tDate[2];


def isLeapYear(nYear):

	if((nYear % 4) == 0 and (nYear % 100) != 0):
		result = True;
	elif((nYear % 400) == 0):
		result = True;
	else:
		result = False;

	return result;

def isThirtyDayMonth(nMonth):
	result = False;
	if(nMonth == 4 or nMonth == 6 or nMonth == 9 or nMonth == 11):
		result = True;

	return result;

def isThirtyOneDayMonth(nMonth):
	result = False;

	if(nMonth != 2 ):
		result = True;
	elif(isThirtyDayMonth(nMonth) != False):
		result = True;
	else:
		result = False;

	return result;

def numDaysInMonth(nMonth):
	if(isThirtyDayMonth(nMonth)):
		nDay = 30;
	elif(isThirtyOneDayMonth(nMonth)):
		nDay = 31;
	else:
		nDay = 28;

	return nDay;

def sumOfFullMonthsInDays(nStartMonth,nEndMonth):
	sum = 0;
	for i in xrange(nStartMonth,nEndMonth+1):
		sum += numDaysInMonth(i);

	return sum;

def daysLeftInAMonth(sDate):
	nDay = parseDay(sDate);
	nMonth = parseMonth(sDate);

	daysLeft = numDaysInMonth(nMonth) - nDay;
	return daysLeft;

def diffYear(sStartDate,sEndDate):
	pass;

def diffDays(sStartDate, sEndDate):
	nStartMonth = parseMonth(sStartDate);
	nEndMonth = parseMonth(sEndDate);
	nEndDay = parseDay(sEndDate);

	totalDiffDays = daysLeftInAMonth(sStartDate) + sumOfFullMonthsInDays(nStartMonth+1,nEndMonth-1) + nEndDay + 1;

	return totalDiffDays


print diffDays('1/1/2001','3/3/2001')








