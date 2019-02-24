# wordsum
Program to solve Word Sum problems such as ROCK + ROLL = MUSIC

  ROCK
 +ROLL
 =====
 MUSIC

For instance given the following letter 2 digit associations

{'C': 2, 'I': 7, 'K': 8, 'M': 1, 'L': 4, 'O': 3, 'S': 6, 'R': 5, 'U': 0}

The above turns into

  5328
 +5344
 =====
 10672
 
The rules are that each letter has to be one of 10 digits, 0-9, and no two letters can be the same digit. 

The Python program is very simple. It simply iterates through every permutation and tests which permutations
work with the words provided. 

I run the program on a Linux box so the command line would be 

python wordsum.py rock roll music

You must have at least 3 words but you can have as many as you like.

Enjoy!
