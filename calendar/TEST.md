# The problem

Create a program that ask for a day and tells you if that day is working day or not.

## The conditions

* The program will asume that working days are any day between Monday and Friday.
* Non working days will be any Saturday and Sunday.

## Requeriments

* It should get string with the day.
* The day should tell the year, the month and the day.
* The day must exist. It must be a valid date.
* It will return one of the following messages:
  * "The day {date} is a working day"
  * "The day {date} is NOT a working day"
* The following formats are valid input formtas:
  * `2019, 12, 31`
  * `2019 12 31`
  * `31/12/2019`
  * `31-12-2019`

## Happy path

Test the follwing:

* The input is a valid string?
* The string is a valid day?
* Pass a Munday date and it should return True.
* Pass a Sunday date and it should return False.
* Pass a bunch of week days and it should return True.
* Pass a bunch of weekend days and it should return False.
* Pass an invalid date and it sould return an exception.
* Pass a non-existent day and it should return an exception.