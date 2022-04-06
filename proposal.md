# Proposal

## What will (likely) be the title of your project?

World Capital Guessing Game


## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")


The user will be prompted to provide a one-word answer to the prompt: "Name the capital of xxx".
Following the Q/A, a link will be provided that will direct the user the the city's wikipedia page.


## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?


The program begins with prompting the user for a username.
If the username is new, the program will write a new save file by adding the name and a score of 0 to a text file.
Then, the program states an explanation of the rules, score system, and a statement of the users current score (0 if new, x if returning).
Next, the user will be asked to choose from one of two game modes: Global or The States. The input will stimulate an if statement.
Then, the user will be prompted to choose a difficulty: forgiving or less-forgiving. The input will stimulate an if statement.
Forgiving allows the user 3 attempts to answer the impending questions correctly, whereas less forgiving allows for only 1 attempt.

The round begins with a question, gathered by reading an random integrer selected line from the csv, which the user then answers.
The program will compare the user's input to a csv file containing the correct answers.
After the correct answer is revealed, the program will present a hyperlink to that capital's wiki page for the user to learn more.
The link pulled by reading the same csv file as the countries/states and capitals.
The user is then asked to play another round. While not "no" or rounds == 50 (states mode) or rounds == 195 (world mode), the the program repeats the aforementioned process.
After the user says no, "(username - score "points")" is printed and the score is appended to the text file of users.
The user will press enter and be returned to the beginning screen.


### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?


At minimum, I will have a text based game that does U.S. state capitals with no webbrowser interaction.


### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?


I could reasonably envision a text based game that does U.S. state capitals and world capitals with no webbrowser interaction.


### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?


The best outcome I envision is a text based game that does U.S. state capitals with webbrowser interaction.


## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?


My immediate next step is to create a csv file with the aforementioned content and start the file-reading component of my program.
I then need to design the username prompting and file writing component.
To create the most sophisticated version of my program, I will need to research and learn how to enable web functionality.
