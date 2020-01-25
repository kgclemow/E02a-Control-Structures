
# E02a-Control-Structures

- Open main01.py. Before running it, what do you expect this program to do?
  # I expect this program to start with a greeting and then prompt me to type the favorite color. 
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
    # The program reverted back to the original repository. 
  - What do you think the program did with what you typed in answer to the question?
    # The program converted my answer into a string. 
- Open main02.py. Before running it, describe how this is different than main01.py.
  # This program labels the function as a variable, color.
  - What do you think the color = input() will do?
      # It will store the answer of the questions (the user input) under the variable color. 
  - Run the program in the terminal and answer the question. Did the program do what you expected?
      # Yes, the program regurgatated the answer to the question as prompted by the variable, color. 
- Open main03.py. Before running it, describe how this is different than main02.py.
    # This has a condition depending on the user input which dictates how the program responds. 
  - What is happening on lines 9–12?
      # A condition is created that tells the program to respond positively if the answer is one specific answer, red, or negatively if the answer is anything else. 
  - Why are lines 10 and 12 indented?
      # The indentation shows where a block starts and stops. When the indenting returns to the original amount, the block is over. A block is just a bit of programming that is grouped as a unit. 
  - Run the program and answer the question. What happens if you don’t capitalize Red?
      # The program only counts capitalized red as correct, so it tells you "sorry, try again". 
  - What does this tell you about "color"?
      # Color is case sensitive. 
- Open main04.py. Before running it, describe how this is different than main03.py.
    # It has the variable of color representing red and Red for a positive answer. 
  - What problem is this trying to solve?
      # It is trying to make the answer not case sensitive. 
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
      # The program outputs that it is not the correct answer unless you input Red or red. 
- Open main05.py. What do you expect line 9 to do?
    # Line not will say that no matter the capitalization of the word, if the letters are r, e, d, the answer will be correct. 
  - What problem is it trying to solve?
      # It is trying to let the user answer the correct answer in whatever form they would like. 
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
      # Spaces make the word count as the wrong answer. 
 - Open main06.py. How is line 9 different than in main05.py?
    # This has .strip() added after the .lower().
   - What would you guess .strip() is doing?
      # I assume it will count as correct as long as the word red with any capitalization and spacing before or after is in the text.
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
      # Writing a sentence instead of just a word will break the logic. For example, Your favorite color is red. 
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
    # If the person types pink, there will be an answer besides wrong and a hint of "close" will be given to the user. 
   - What is happening on line 12?
      # It is giving another condition besides the singular if, representing else if. 
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
    # It creates a loop so the question is continued to be asked until the correct answer is given, ending the loop. 
   - Why are lines 10–17 indented?
      # They are a block occuring as long as the while condition is met, looping. 
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
      # The re asking of the question would not be included in the loop. 
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
      # Sorry try again is the only thing looping as th correct answer can never be given except the first time. 
 - Open main09.py. What is happening on line 13?
    # It is telling the program to keep track of the number of guesses. 
   - What is the purpose of “count”?
      # It counts the number of substrings present in order to track the guesses or inputs made. 
   - What is happening on line 22?
      # The program will tell you how many guesses you made before guessing the correct answer after you guess the correct answer. 
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
      # creates a new function call that will later return the result to the user 
  
Commit your changes and push them back to the repository.
 




When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
