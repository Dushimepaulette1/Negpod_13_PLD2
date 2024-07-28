#!/usr/bin/python3
import json
import os


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = (
            answer.lower()
        )  # Convert answer to lowercase for case insensitivity

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer

    def to_dict(self):
        return {"text": self.text, "answer": self.answer}

    @staticmethod
    def from_dict(data):
        return Question(data["text"], data["answer"])


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.score_history = []

    def view_progress(self):
        print("\nYour Progress:")
        for i, score in enumerate(self.score_history, 1):
            print("Quiz {}: {} points".format(i, score))
        if not self.score_history:
            print("No progress yet.")

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "score_history": self.score_history,
        }

    @staticmethod
    def from_dict(data):
        user = User(data["username"], data["password"])
        user.score_history = data.get("score_history", [])
        return user


class Admin(User):
    pass


class QuizApp:
    def __init__(self):
        self.users = []
        self.admins = []
        self.questions = self.load_questions()
        self.current_user = None
        self.load_users()

    def load_users(self):
        if os.path.exists("credentials.json"):
            with open("credentials.json", "r") as file:
                try:
                    users_data = json.load(file)
                    self.users = [User.from_dict(user) for user in users_data]
                except json.JSONDecodeError:
                    self.users = []

    def save_users(self):
        with open("credentials.json", "w") as file:
            json.dump([user.to_dict() for user in self.users], file)

    def load_questions(self):
        if os.path.exists("quizzes.json"):
            with open("quizzes.json", "r") as file:
                try:
                    data = json.load(file)
                    return {
                        subject: [Question.from_dict(q) for q in questions]
                        for subject, questions in data.items()
                    }
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_questions(self):
        with open("quizzes.json", "w") as file:
            json.dump(
                {
                    subject: [q.to_dict() for q in questions]
                    for subject, questions in self.questions.items()
                },
                file,
            )

    def load_progress(self):
        if os.path.exists("progress.json"):
            with open("progress.json", "r") as file:
                try:
                    data = json.load(file)
                    for user_data in data:
                        for user in self.users:
                            if user.username == user_data["username"]:
                                user.score_history = user_data.get("score_history", [])
                except json.JSONDecodeError:
                    pass

    def save_progress(self):
        with open("progress.json", "w") as file:
            json.dump([user.to_dict() for user in self.users], file)

    def main_menu(self):
        print("\n******************************************")
        print("*                                        *")
        print("*        WELCOME TO THE MENU DRIVEN      *")
        print("*               QUIZ PROGRAM             *")
        print("*                                        *")
        print("******************************************")
        print("\nMAIN MENU:")
        print("1. Create User")
        print("2. Login")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            self.create_user()
        elif choice == "2":
            self.login()
        elif choice == "3":
            self.admin_login()
        elif choice == "4":
            print("\nThank you for using the Quiz Program!")
            self.save_users()
            self.save_questions()
            self.save_progress()
            return
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")
            self.main_menu()

    def create_user(self):
        print("\nCREATE USER")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        self.users.append(User(username, password))
        self.save_users()
        print("\nUser '{}' created successfully!".format(username))
        self.main_menu()

    def login(self):
        print("\nLOGIN")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                self.user_menu()
                return

        print("\nInvalid username or password. Please try again.")
        self.main_menu()

    def admin_login(self):
        print("\nADMIN LOGIN")
        password = input("Enter admin password: ").strip()
        if password == "adminpass":
            self.current_user = Admin("admin", password)
            self.admin_menu()
        else:
            print("\nIncorrect admin password. Please try again.")
            self.main_menu()

    def user_menu(self):
        print("\nWelcome, {}!".format(self.current_user.username))
        print("\nUSER MENU:")
        print("1. Take Quiz")
        print("2. View Progress")
        print("3. Logout")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            self.take_quiz()
        elif choice == "2":
            self.current_user.view_progress()
            self.user_menu()
        elif choice == "3":
            self.current_user = None
            print("\nLogged out successfully.")
            self.main_menu()
        else:
            print("\nInvalid choice. Please enter a number from 1 to 3.")
            self.user_menu()

    def admin_menu(self):
        print("\nWelcome, {}!".format(self.current_user.username))
        print("\nADMIN MENU:")
        print("1. Add Question")
        print("2. Update Question")
        print("3. Delete Question")
        print("4. List All Questions")
        print("5. Logout")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            self.add_question()
        elif choice == "2":
            self.update_question()
        elif choice == "3":
            self.delete_question()
        elif choice == "4":
            self.list_all_questions()
        elif choice == "5":
            self.current_user = None
            print("\nLogged out successfully.")
            self.main_menu()
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")
            self.admin_menu()

    def take_quiz(self):
        print("\nTAKE QUIZ")
        print("Choose a subject:")
        print("1. ICT")
        print("2. Maths")
        print("3. English")
        print("4. Science")
        print("5. General Knowledge")

        subject_choice = input("\nEnter your choice (1-5): ").strip()

        subjects = ["ICT", "Maths", "English", "Science", "General Knowledge"]
        subject = subjects[int(subject_choice) - 1]

        questions = self.questions.get(subject, [])

        if not questions:
            print(
                "\nNo questions found for {}. Please contact the admin.".format(subject)
            )
            self.user_menu()

        score = 0

        for question in questions:
            print("\n" + "-" * 50)
            print(question.text)
            user_answer = input("Enter 'True' or 'False': ").strip().capitalize()

            if question.check_answer(user_answer):
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        if score > 0:
            self.current_user.score_history.append(score)
            self.save_progress()

        print("\nQuiz completed! You scored {} points.".format(score))
        self.user_menu()

    def add_question(self):
        print("\nADD QUESTION")
        print("Choose a subject to add a question to:")
        print("1. ICT")
        print("2. Maths")
        print("3. English")
        print("4. Science")
        print("5. General Knowledge")

        subject_choice = input("\nEnter your choice (1-5): ").strip()

        subjects = ["ICT", "Maths", "English", "Science", "General Knowledge"]
        subject = subjects[int(subject_choice) - 1]

        question_text = input("Enter the question text: ").strip()
        correct_answer = (
            input("Enter the correct answer ('True' or 'False'): ").strip().capitalize()
        )

        if subject in self.questions:
            self.questions[subject].append(Question(question_text, correct_answer))
            self.save_questions()
            print("\nQuestion added successfully!")
        else:
            print("\nInvalid subject.")

        self.admin_menu()

    def update_question(self):
        print("\nUPDATE QUESTION")
        self.list_questions()

        question_index = input("\nEnter the index of the question to update: ").strip()

        try:
            question_index = int(question_index) - 1
            if question_index < 0:
                raise ValueError

            subjects = ["ICT", "Maths", "English", "Science", "General Knowledge"]
            subject = input("Enter the subject of the question: ").strip()

            if subject not in subjects:
                print("\nInvalid subject.")
                self.admin_menu()

            if subject in self.questions:
                if 0 <= question_index < len(self.questions[subject]):
                    question = self.questions[subject][question_index]
                    print("Current question: {}".format(question.text))
                    new_text = input("Enter new question text: ").strip()
                    new_answer = (
                        input("Enter new answer ('True' or 'False'): ")
                        .strip()
                        .capitalize()
                    )

                    question.text = new_text
                    question.answer = new_answer

                    self.save_questions()
                    print("\nQuestion updated successfully!")
                else:
                    print("\nInvalid question index.")
            else:
                print("\nSubject not found.")

            self.admin_menu()

        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            self.update_question()

    def delete_question(self):
        print("\nDELETE QUESTION")
        self.list_questions()

        question_index = input("\nEnter the index of the question to delete: ").strip()

        try:
            question_index = int(question_index) - 1
            if question_index < 0:
                raise ValueError

            subjects = ["ICT", "Maths", "English", "Science", "General Knowledge"]
            subject = input("Enter the subject of the question: ").strip()

            if subject not in subjects:
                print("\nInvalid subject.")
                self.admin_menu()

            if subject in self.questions:
                if 0 <= question_index < len(self.questions[subject]):
                    self.questions[subject].pop(question_index)
                    self.save_questions()
                    print("\nQuestion deleted successfully!")
                else:
                    print("\nInvalid question index.")
            else:
                print("\nSubject not found.")

            self.admin_menu()

        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            self.delete_question()

    def list_questions(self):
        print("\nLIST ALL QUESTIONS")
        for subject, questions in self.questions.items():
            print("\nSubject: {}".format(subject))
            for i, question in enumerate(questions, 1):
                print("{}. {} (Answer: {})".format(i, question.text, question.answer))

    def list_all_questions(self):
        print("\nLIST ALL QUESTIONS")
        for subject, questions in self.questions.items():
            print("\nSubject: {}".format(subject))
            for i, question in enumerate(questions, 1):
                print("{}. {} (Answer: {})".format(i, question.text, question.answer))

        self.admin_menu()


if __name__ == "__main__":
    app = QuizApp()
    app.main_menu()
