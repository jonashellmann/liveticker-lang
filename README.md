# Liveticker

Inspired by [Rockstar](https://codewithrockstar.com/), Liveticker is a super-simple programming language to write code
that looks like a football (soccer) liveticker.
The source code is translated to Python code and then gets executed with Python.

## Installation

To run a program written in Liveticker you need to have Python 3 installed. No additional Python packages are needed
so far.
Then you just clone this repository and run the following command in your console:
`python /path/to/repo/liveticker.py --file /path/to/file.live`

## Usage

- Variable names can contain spaces.
- Every dot in the text is ignored as well as upper and lower case letters. Every letter gets converted into lowercase.
- A variable for a number gets initialized by the number on the jersey: `Christiano Ronaldo has the number 7` ->
  `christiano_ronaldo = 7`.
- To initialize a number variable with zero, one can tell that he does not play: `Lionel Messi is not on the pitch` ->
  `lionel_messi = 0`. Everything after "is not on the pitch" can be anything you want it to be.
- A number is incremented by scoring a goal: `Didier Drogba scores a goal` -> `didier_drogba += 1`.
- Subtract a variable from another: `a gets as many goals denied by the VAR b` -> `a -= b`. The part between "gets as
  many goals denied" and the second "as" is not considered.
- For comparisons there are currently the following operations:
  - `a is better than b` -> `a > b`
  - `a is better than or as good as b` -> `a >= b`
  - `a is worse than b` -> `a < b`
  - `a is worse than or as good as b` -> `a <= b`
  - `a scores no goal` -> `a == 0`
- To connect two comparisons you can use `and`.
- To create a while-loop, write `while` in front of a comparison: `While A is better than b` -> `while a > b:`.
  - A sentence with "new kickoff" in it continues the loop to the next iteration: `The ball crossed the goal line, new
    kickoff.` -> `continue`. Everything else in this line is not important.
- An if-statement is achieved by putting `if` in front of a comparison: `If A is better than b` -> `if a > b:`.
- A new function is introduced by writing the function name, then "plays with" and then specifying how many arguments
  the function has: `Werder Bremen plays with 3 defenders today.` -> `def werder_bremen(the_first, the_second)`.
  Up to nine parameters are possible. Everything after the number is not considered.
  - To access an argument inside a function, use "the first", "the second", ...
  - A variable is returned if it gets the ball: `Robert Lewandowski gets the ball` -> `return robert_lewandowski`
- A block of code (if, while, function) is ended by a line in which the word "referee" is in.
- Call to a method: `Germany including (Lukas Podolski,Michael Ballack)` -> `germany(lukas_podolski, michael_ballack)`
- If there is a "says" in a line, everything after it (in quotes) is printed to the console: `Someone says "Hello"` ->
  `print("Hello")`. It doesn't matter who says something.
- To print a variable, "calls for" is used: `The trainer calls for Mo Salah` -> `print(mo_salah)`.

### Examples

There are a few examples on how this programming language works in the `examples` folder.

## License

This project is under the [MIT License](https://github.com/jonashellmann/liveticker-lang/blob/main/LICENSE).