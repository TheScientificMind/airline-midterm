# APCSP Airline Midterm
## Intro

In this APCSP midterm project, we will be working in a group to develop an airline ticketing and booking system. When finished, our program is going to allow people to purchase tickets, allow gate agents to check in passengers, and produce actionable reports, including graphs, allowing managers to see actionable reports about what is going on in the network. While most of this project will rely on using information that we already know, this project will also require us to do some of our own research. We will be required to learn how to use two external python libraries, one to produce graphs, and one to send email.

## Front-End

The front-end layer of the program should allow users to book airline tickets based on a number of parameters. Primarily, users must be able to specify a pair of airport codes, and a date to fly. Users should also have the option to automatically book a return flight on a subsequent date. This display should also show the flight’s times and prices. When a user has selected a ticket to book, a booking entry must be created, storing their name, phone number, and email address. Once a ticket has been booked, the user must be emailed to notify them about their booking. This email must include information about the flight, and a confirmation code that can later be used to validate the booking. An additional interface must also be created to check in customers at the airport. This interface must be set to a specific gate at start time, and then must accept a confirmation code. The console should then display the ticket holder’s name, and validate the ticket (correct airport, correct date, not already used). Once validated, the ticket should be marked as checked in.

## Back-End

The system must additionally perform data validation on the back end. Chiefly, the system must ensure that the number of tickets sold does not exceed the number of seats available for each flight. Additionally, we should configure the system to track the number of frequent flier miles that each customer has. If a new customer uses the system, a new customer frequent flier account should be generated with his email. we will be provided with a new database, and two tables. One table will show all available flights, and the second table will show how many people each aircraft can carry. Beyond this, we will have to design and implement the rest of the database on our own.

## Report generation and information

Finally, we must construct a program to generate reports on the status of the network. These reports should include a graphical and written component. To generate the graphical component, we will be using the matplotlib library, which will allow we to produce a wide variety of graphs easily though python (please note that we will have to save the figures to a png to view them). Written reports should be written to a file on the disk. we should build the following reports:

1. Day-to-day bookings and revenue – This report should produce a line graph with two lines, one representing the number of bookings per day, and the other representing the amount of
revenue generated on a day to day basis. The written report for this section should have rows
for each day, with the required information.

2. Most popular destinations – This should be a bar graph showing the most popular cities that
were booked by customers. It should show at least the 5 most popular routings. There should
also be a written list version of the report.

## Requirements

Beyond the above functional requirements, there are a few other things that our program must
include. Our programs must include at least one of the following: if statement, loop, object/class, list, function. Most of these should be satisfied automatically as we go along, but be sure that we include them. We must additionally store all of our code in a shared GitHub repository. Additionally, please try to make our program pretty and user-friendly. Observe how the SQL command like interface makes things a bit pretty when printing text. we don’t need to go this far, but make an effort. Our program should also automatically return to the main screen after the completion of a transaction unless specifically told to quit. This assignment does not have a point value because midterms are graded differently. The final thing that we need to keep in mind is the importance of code quality and keeping things neat. This is going to be a larger project, likely spanning multiple files, and we should be keeping things neat. Separate distinct blocks of code into functions with arguments and returns; use objects when appropriate; comment everything; don’t be afraid to use multiple files; avoid unneeded global vars. Enzo will be grading more harshly in this  regard, because this is designed to simulate the AP final project. AP graders will not be happy with code that they can’t understand.