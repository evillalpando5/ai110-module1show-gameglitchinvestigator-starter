# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The first time I ran the game I did not open the developer debug info I just played one round of the game. I noticed there were different difficulty levels and was a bit confused on how that would work since its a guessing game. After exploring I realized the difficulty level is tied to the number of guesses. The UI was very nice and easy to understand it felt intuitive. Some features worked like the hint toggle button while others like the press enter to apply was not. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first bug I noticed was the provided hints were leading me in the wrong direction. I was adjusting my guess according to them but never got the correct answer so I looked in the developer debug info to find it was providing incorrect hints.
The second bug I noticed was the little message in the guess text bar that says press enter to apply. I hit enter multiples but it did not work I had to press submit guess manually. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-------|-------------------|-----------------|------------------------|-------------------------|
| 70    | Hint Go Higher    | Hint go Lower   |          none          | app.py, check_guess     |
|new game| restart neew game| attempts left changed but unable to submit guess| none | app.py, st.session_state.secret |
| difficulty easy   | secret in range 1-20| secrect 43 |  none                  |  app.py, st.session_state.secret    |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
For this project I used claude code in vs code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

An AI suggestion that was correct was the code to fix the hint message. Claude suggested not passing the secret as as a string because it produces errors when being compared to an integer. I was able to verify that this code was correct because before any fix I understood what the issue which was the unnecessary string conversion when the attempt was even. Additionally after making the changes I had claude generate tests for the fix and made sure the original tests as well as the new tests passed successfully. 

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

One AI suggestion I did not accept was an error I made in prompting it that I caught when checking the changes claude was proposing. Claude did not challenge my thinking it followed my instruction blindly even though I was going against the game logic. I mentioned I wanted to test the correct hints were showing up when the user guessed too low and it should guess low. This is in incorrect. Claude mentioned something about swapping the messages and that raised a red flag and that is when I realized I prompted Claude incorrectly. I repromted it and I verified it worked by running the test on both a guess that was two high and a guess that was too low.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was really fixed but creating tests that targeted the specific fix as well as making sure that the original tests continued to also pass. Claude genreated the tests and I reviewed them to make sure they made sense and covered the scenerio I was interested in. I made sure that the bug was fix and that it did not break anything else in the process. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I ran manually was choosing guesses purposefully after viewing the secret to test whether all the items were working was they should. It helped me point out other errors in the code besides the hint message. The first run was not being saved to the guess history and the attempts remaining started off incorrectly on the normal difficulty level. 

- Did AI help you design or understand any tests? How?
AI did help design tests for the bugs. I was able to understand the tests on my own. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns automatically reruns the code on every single interaction. In order to save values across the reruns you use session state which preserves the values until you make a change to the browser like refreshing it or closing and reopening it.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One strategy from this project that I will reuse in future labs and projects is the flow of making changes. I will understand the issue first, make changes, and then test these changes worked and did not affect any other part of my project. Specifically reviewing changes before approving them. You can have claude auto edit your files but I think that's when things can get complicated.

- What is one thing you would do differently next time you work with AI on a coding task?

Text time I work with AI on a coding task I will start a new chat for each fix. I forgot to in this scenario but it is helpful to be able to trace your steps and keeps everything organized.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project changed the way I view AI generated code because now I understand that you still have control over the changes by reviewing them first. AI code is a tool to help you speed up the process but reviewing the changes and ensuing they work is a vital step in the process as well.