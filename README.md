
 Quiz Application

Welcome to the Quiz Application! This is a simple console-based quiz program that allows users to take quizzes on various subjects, track their progress, and for admins to manage quiz questions.

## Features

- User Management: Create and login users.
- Admin Management: Admin login to manage questions.
- Quiz Taking: Users can take quizzes in different subjects.
- Progress Tracking: Users can view their quiz score history.

## Subjects Available

1. ICT
2. Maths
3. English
4. Science
5. General Knowledge

## Classes and Their Responsibilities

### Question

Represents a single quiz question.

- Attributes:
  - text: The text of the question.
  - answer: The correct answer to the question.
- Methods:
  - check_answer(user_answer): Checks if the user's answer is correct.

### User

Represents a user of the quiz application.

- Attributes:
  - username: The username of the user.
  - password: The password of the user.
  - score_history: A list to track the user's quiz scores.
- Methods:
  - view_progress(): Prints the user's quiz score history.

### Admin (inherits from User)

Represents an admin user with permissions to manage quiz questions.

### QuizApp

Main application class to handle user interactions and quiz logic.

- Attributes:
  - users: A list to store user objects.
  - admins: A list to store admin objects.
  - questions: A dictionary to store questions categorized by subjects.
  - current_user: The currently logged-in user.
- Methods:
  - main_menu(): Displays the main menu and handles user choices.
  - create_user(): Creates a new user.
  - login(): Logs in an existing user.
  - admin_login(): Logs in an admin user.
  - user_menu(): Displays the user menu and handles user choices.
  - admin_menu(): Displays the admin menu and handles admin choices.
  - take_quiz(): Allows the current user to take a quiz.
  - add_question(): Adds a new question to a subject.
  - update_question(): Updates an existing question.
  - delete_question(): Deletes a question from a subject.
  - list_questions(): Lists all questions categorized by subjects.
  - start(): Starts the quiz application by displaying the main menu.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/quiz-application.git
   ```
2. Navigate to the project directory:
   ```
   cd quiz-application
   ```

### Usage

1. Run the quiz application:
   ```
   python quiz_app.py
   ```
2. Follow the on-screen instructions to create users, take quizzes, and manage quiz questions.

### Admin Features

- Add Question: Add new questions to any subject.
- Update Question: Update existing questions.
- Delete Question: Remove questions from any subject.
- List All Questions: View all questions categorized by subjects.

## Acknowledgements

- Inspired by various quiz applications and educational tools.
- Thank you to all contributors who are paulette,blair,josue,cynthia, allan and brave
- Thank you for all who will and use our project and do the quizes
  
Enjoy the Quiz Application and happy learning!
