# Web-Crawling-And-Information-Extraction

NAME : SOMOSHREE DATTA
ROLL NUMBER: 20CS60R05
SUBJECT: CL-II ASSIGNMENT 8
COMMAND TO RUN THE PROGRAM: make

CODE FILES: task1.py (CONTAINS THE CODE TO TAKE THE INPUTS AND DISPLAY THE OUTPUTS TO THE USER. ALSO CALLS THE SECOND CODE FILE FOR PARSING THE INPUT)
task2.py (CONTAINS THE GRAMMAR AND THE TOKENS FOR PARSING AN HTML FILE)

ASSUMPTIONS AND FLOW OF PROGRAM:

1. THE GENRE NAME TO BE ENTERED BY THE USER MUST EXACTLY MATCH THE GENRE NAME THAT GETS DISPLAYED ON THE CONSOLE.

2. THE MOVIE NAME TO BE ENTERED BY THE USER MUST EXACTLY MATCH THE MOVIE NAME THAT IS SHOWN ON THE LIST OF MOVIES DISPLAYED IN THE CONSOLE (DON'T CONSIDER THE NUMBER OF THE MOVIE INTO THE MOVIE NAME).

3. ENTER 'E' (WITHOUT INVERTED COMMAS) TO EXIT OUT OF THE PROGRAM.

4. INITIAL CRAWLING TAKES TIME AS IT SAVES THE WEBPAGES OF ALL THE 10 GENRES. THEREAFTER, CRAWLING DOESN'T REQUIRE ANY TIME AS IT USES THESE SAVED WEBPAGES TO ANSWER THE QUERIES OF THE USER.

5. AFTER CRAWLING ALL THE WEBPAGES, A MENU CONSISTING OF THE 10 GENRES ARE DISPLAYED TO THE USER. ONCE THE USER ENTERS ONE OF THE GENRE NAMES AS INPUT, ALL THE 100 MOVIES CORRESPONDING TO THAT GENRE GETS DISPLAYED ONTO THE CONSOLE.

6. NOW THE USER IS PROMPTED TO ENTER A MOVIE NAME FROM THE LIST OF MOVIES THAT ARE DISPLAYED IN ORDER TO QUERY DETAILS ABOUT THE MOVIE NAME.  THE CORRESPONDING HTML FILE OF THE MOVIE IS PARSED.

7. NEXT, THE USER IS PROMPTED TO ENTER THE FIELD NAME THAT IT WISHES TO QUERY FROM THE LIST OF THE FIELD NAMES THAT ARE DISPLAYED ON THE CONSOLE. THE FIELD NAME ENTERED SHOULD MATCH IN A CASE-INSENSITIVE WAY WITH THE FIELD NAME THAT IS DISPLAYED ON CONSOLE, I.E. UPPER CASE OR LOWER CASE LETTERS DON'T MATTER. JUST THE NAME SHOULD BE IDENTICAL AS THE ONE THAT IS SHOWN ON SCREEN.

8. FINALLY THE CORRESPONDING VALUE FOR THE FIELD NAME IS DISPLAYED ONTO THE CONSOLE. ALSO, A FILE NAMED AS 'result_log.txt' GETS FORMED IN THE SAME FOLDER AS THE CODE FILES WHERE ALL THE LOGS OF THE QUERIES ARE STORED.

