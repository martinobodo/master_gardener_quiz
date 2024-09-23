** Master Gardener Quiz 

Overview 

Master Gardener Quiz is an interactive game created to challenge users with questions from a variety of categories. 
Featuring a lively and engaging interface, it appeals to trivia lovers of all ages who want to test their knowledge in a fun and exciting way.
Whether you're looking to expand your general knowledge or simply pass the time, Master Gardener Quiz offers a smooth and enjoyable experience.

source: Martin Obodo 

UX

The design process for Master Gardener Quiz centered around crafting an intuitive and user-friendly interface. 
The game is straightforward to navigate, with clear instructions and a clean layout that emphasizes smooth user interaction. 
The visual elements are both enjoyable and practical, keeping users engaged throughout their quiz experience

Features Existing Features Dynamic Question Display

Every quiz session offers a fresh set of randomly generated questions, guaranteeing a distinct experience each time. 
Users can choose how many questions they'd like to answer, 
allowing the quiz to be tailored for both brief and extended sessions.

Real-time Feedback


Users get instant feedback after each question, indicating whether their answer was correct. 
This feature helps keep them engaged and informed about their progress during the quiz.

Score Tracking

The quiz monitors the user's score and shows it after each question, as well as the final score at the end of the session. 
This feature introduces a competitive aspect to the game, motivating users to enhance their performance.

Future Features 

Introduce a high scores system that allows users to compare their scores with others. 
This feature will create a competitive atmosphere and encourage players to return for more.

Introduce a timer for each question to add a level of complexity to the game

Tools & Technologies Used used for version control. (git add, git commit, git push) used for secure online code storage. 
used for hosting the deployed back-end site. used as the back-end programming language. used as my local IDE for development. 
Data Model Flowchart A flowchart was created to map out the logic of the quiz game before coding began. 
This helped in visualizing the user journey and ensuring a friendly user experience.

Classes & Functions The program is structured using functions to handle various parts of the quiz game:

run_quiz() Controls the main flow of the quiz, including question selection and score tracking. 
display_welcome_message() Displays the welcome message and instructions for the quiz. 
get_quiz_length() Prompts the user to select the number of questions for the quiz. 
play_again() Asks the user if they want to play again after completing the quiz. 

Testing [!NOTE] For all testing, please refer to the TESTING.md file.

Deployment Master Gardener Quiz game is deployed on Heroku. Below are the steps taken to deploy the project:

Heroku Deployment Create a New App on the Heroku dashboard. 

Add Buildpacks: Python first, then Node.js. 
Configure Config Vars such as PORT and any secret keys. 
Ensure the following files are present: requirements.txt 
Procfile runtime.txt Push the project to Heroku using Git. 
Local Deployment To run the project locally:

Clone the repository: git clone https://github.com/***Master_Gardener_Quiz.git 

Install dependencies: pip3 install -r requirements.txt Run the app locally and test the features. 

Credits Content Source Location Notes Dev Tutorial https://dev.to/dev_neil_a/python-how-to-adding-color-and-styles-to-terminal-text-3699
StackOverflow various Helped troubleshoot code issues during development Media Source Location Type Notes 
Pexels hero image image Favicon and hero image Unsplash quiz images image Quiz background images 

Acknowledgements Special thanks to my Code Institute mentor for guidance and feedback throughout this project. 

Thanks to the Code Institute Slack community for support and troubleshooting help.