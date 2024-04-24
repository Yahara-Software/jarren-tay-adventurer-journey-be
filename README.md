# Adventurer Journey - Back End
Please complete the story below and create a program to solve the problem. Commit any work back to the remote no later than 48 hours before the next interview.

*Please use whatever languages, references and tooling you would like to complete the story.*

## Story Instructions
You are an adventurer standing in the center of a map facing North, and you’re trying to weave through the terrain to your final destination. You have the directions to your destination indicating the number of steps and the direction to travel.

Adventurer Path & Instructions - [./Adventurer Path.md](./Adventurer%20Path.md)

Given the Path Instructions above, programmatically parse the instructions and determine what is the Euclidean (straight line) distance from your starting point to the destination in steps?

**Tech Notes:**
- Use whatever languages, references and tooling you would like.
- Provide any needed instructions to run program.
- Do not round to the nearest step.
- After program executes the answer should be returned.

## Instructions for Program Execution
You must have Python 3.10 or higher to run the program. You can find links to install at [https://www.python.org/downloads/.](https://www.python.org/downloads/) It shouldn't need additional libraries to be installed.

You can use the program in two ways. Both ways will print the Euclidian distance to the command line, or an error message.
- Calling just challenge.py will read the directions from Adventurer Path.md assuming both files are in the same directory.
```
python3 challenge.py
```
- Calling challenge.py with -s or --string allows you to manually specify the directions as an argument
```
python3 challenge.py -s <distance string, no quotations>
```
- Calling challenge.py with -h shows help text.
