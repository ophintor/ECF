# ECF

A couple of utilities to keep track of your ECF grading (for chess players in the UK)

** calc_rating.py **

This is a small python program intended to calculate/estimate your current ECF grading up to date.

The python programs needs to read a file called games.txt that will live in the same folder and that will hold the information of all your past games, one game per line. The format is as follows:

<Date (dd/mm/yyyy)> <result(1/0/0.5)> <opponent rating/UNG> <opponent name>

Example:

17/09/2015 1 81B  Smith, John
13/10/2015 0 UNG  White, John
15/12/2015 0 81A  Williams, Peter
28/01/2016 0 117B Smith, John
23/02/2016 1 52F  White, Peter
25/02/2016 0 137A Smith, John
01/03/2016 0 64B  White, Peter
15/03/2016 1 77B  Smith, John
12/04/2016 1 108C Smith, John
03/05/2016 1 103B Johnson, Thomas
10/06/2016 0 114A Harris, John
11/06/2016 0 122A Johnson, Mary
12/06/2016 0 105A Wallman, Mary
12/06/2016 0 UNG  Johnson, John
06/09/2016 1 109C White, Peter
13/09/2016 0.5 113D Johnson, John
15/09/2016 0 UNG Brown, Peter
20/09/2016 0 82 Johnson, Mary


** ecf.py **

Converter between ECF -> ELO.

Just run it with no parameters and enter your ECF rating. Or run it alternatively with your ECF rating as your one parameter.
