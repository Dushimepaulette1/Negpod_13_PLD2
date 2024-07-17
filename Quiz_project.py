#!/usr/bin/python3
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = (
            answer.lower()
        )  # Convert answer to lowercase for case insensitivity

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.score_history = []

    def view_progress(self):
        print("\nYour Progress:")
        for i, score in enumerate(self.score_history, 1):
            print(f"Quiz {i}: {score} points")
        if not self.score_history:
            print("No progress yet.")


class Admin(User):
    pass


class QuizApp:
    def __init__(self):
        self.users = []
        self.admins = []
        self.questions = {
            "ICT": [
                Question("The internet is an example of a WAN. (True/False)", "True"),
                Question(
                    "HTML stands for HyperText Markup Language. (True/False)", "True"
                ),
                Question("RAM is a type of permanent memory. (True/False)", "False"),
                Question("Python is a type of snake. (True/False)", "True"),
                Question("A byte is 16 bits. (True/False)", "False"),
                Question("Java is a scripting language. (True/False)", "False"),
                Question(
                    "HTTP stands for HyperText Transfer Protocol. (True/False)", "True"
                ),
                Question(
                    "GUI stands for Graphical User Interface. (True/False)", "True"
                ),
                Question(
                    "URL stands for Uniform Resource Locator. (True/False)", "True"
                ),
                Question("LAN stands for Local Area Network. (True/False)", "True"),
                Question("The internet is a type of LAN. (True/False)", "False"),
                Question("JSP stands for Java Server Pages. (True/False)", "True"),
                Question("CD stands for Compact Disk. (True/False)", "True"),
                Question(
                    "HTTP stands for Hypertext Transfer Protocol. (True/False)", "True"
                ),
                Question(
                    "JPEG stands for Joint Photographic Expert Group. (True/False)",
                    "True",
                ),
                Question("RAM stands for Random Access Memory. (True/False)", "True"),
            ],
            "Maths": [
                Question("A triangle has three sides. (True/False)", "True"),
                Question("The square root of 49 is 8. (True/False)", "False"),
                Question("Pi is approximately 3.14159. (True/False)", "True"),
                Question("5 * 5 = 30. (True/False)", "False"),
                Question("A right angle is 90 degrees. (True/False)", "True"),
                Question(
                    "The sum of the angles in a triangle is 180 degrees. (True/False)",
                    "True",
                ),
                Question("The number 0 is an even number. (True/False)", "True"),
                Question(
                    "The Fibonacci sequence starts with 0 and 1. (True/False)", "True"
                ),
                Question(
                    "A prime number has exactly two factors. (True/False)", "True"
                ),
                Question(
                    "The area of a square is calculated as s * s. (True/False)", "True"
                ),
                Question("C stands for Compilers. (True/False)", "True"),
                Question("V stands for Virtual. (True/False)", "True"),
                Question("F stands for Fast. (True/False)", "True"),
                Question("J stands for JavaScript. (True/False)", "True"),
                Question("L stands for Language. (True/False)", "True"),
            ],
            "English": [
                Question("An adjective describes a noun. (True/False)", "True"),
                Question(
                    "'They're' is a contraction of 'they are'. (True/False)", "True"
                ),
                Question("The word 'happy' is a noun. (True/False)", "False"),
                Question("The word 'quickly' is an adverb. (True/False)", "True"),
                Question("A pronoun takes the place of a noun. (True/False)", "True"),
                Question("Shakespeare wrote 'Romeo and Juliet'. (True/False)", "True"),
                Question(
                    "A palindrome reads the same forwards and backwards. (True/False)",
                    "True",
                ),
                Question(
                    "English is the most spoken language in the world. (True/False)",
                    "False",
                ),
                Question(
                    "A comma is used to separate items in a list. (True/False)", "True"
                ),
                Question("The past tense of 'go' is 'gone'. (True/False)", "True"),
                Question(
                    "The word 'colour' is spelled with 'or' in American English. (True/False)",
                    "False",
                ),
                Question("The word 'the' is a preposition. (True/False)", "False"),
                Question("The word 'time' is a noun. (True/False)", "True"),
                Question("The word 'quick' is a verb. (True/False)", "False"),
                Question("The word 'yellow' is an adverb. (True/False)", "False"),
            ],
            "Science": [
                Question("Water boils at 100 degrees Celsius. (True/False)", "True"),
                Question("Humans have three lungs. (True/False)", "False"),
                Question("Plants produce oxygen. (True/False)", "True"),
                Question("The sun is a planet. (True/False)", "False"),
                Question("Sound travels faster than light. (True/False)", "False"),
                Question("The Earth orbits the Moon. (True/False)", "False"),
                Question("The human body has 206 bones. (True/False)", "True"),
                Question(
                    "Gravity is stronger on the Moon than on Earth. (True/False)",
                    "False",
                ),
                Question(
                    "Oxygen is the most abundant element in Earth's atmosphere. (True/False)",
                    "True",
                ),
                Question("Mars is known as the 'Red Planet'. (True/False)", "True"),
                Question(
                    "The Milky Way is the galaxy that contains our Solar System. (True/False)",
                    "True",
                ),
                Question(
                    "Water covers approximately 71% of Earth's surface. (True/False)",
                    "True",
                ),
                Question("A light-year measures time. (True/False)", "False"),
                Question(
                    "Astronomy is the study of stars and planets. (True/False)", "True"
                ),
                Question(
                    "A telescope is used to observe distant objects in space. (True/False)",
                    "True",
                ),
            ],
            "General Knowledge": [
                Question("The capital of France is Paris. (True/False)", "True"),
                Question(
                    "The Great Wall of China is visible from space. (True/False)",
                    "False",
                ),
                Question("There are 50 states in the USA. (True/False)", "True"),
                Question(
                    "The largest ocean on Earth is the Atlantic Ocean. (True/False)",
                    "False",
                ),
                Question(
                    "Mount Everest is the tallest mountain in the world. (True/False)",
                    "True",
                ),
                Question(
                    "The Nile River is the longest river in the world. (True/False)",
                    "False",
                ),
                Question(
                    "Australia is both a country and a continent. (True/False)", "True"
                ),
                Question(
                    "Albert Einstein developed the theory of relativity. (True/False)",
                    "True",
                ),
                Question(
                    "The first human to walk on the Moon was Neil Armstrong. (True/False)",
                    "True",
                ),
                Question(
                    "Venus is the hottest planet in our solar system. (True/False)",
                    "True",
                ),
                Question("An apple is a fruit. (True/False)", "True"),
                Question("The sky is purple. (True/False)", "False"),
                Question("Dogs meow. (True/False)", "False"),
                Question("The world is flat. (True/False)", "False"),
                Question("The sun rises in the west. (True/False)", "False"),
            ],
        }
        self.current_user = None

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
            return
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")
            self.main_menu()

    def create_user(self):
        print("\nCREATE USER")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        self.users.append(User(username, password))
        print(f"\nUser '{username}' created successfully!")
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
        print(f"\nWelcome, {self.current_user.username}!")
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
        print(f"\nWelcome, {self.current_user.username}!")
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
            self.list_questions()
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
            print(f"\nNo questions found for {subject}. Please contact the admin.")
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

        print(f"\nQuiz completed! You scored {score} points.")
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
            print("\nQuestion added successfully!")
        else:
            print("\nInvalid subject.")

        self.admin_menu()

    def update_question(self):
        print("\nUPDATE QUESTION")
        self.list_questions()

        question_index = input("\nEnter the index of the question to update: ").strip()

        try:
            question_index = int(question_index)
            question_index -= 1  # Adjust index for zero-based indexing
            question_subjects = list(self.questions.keys())
            question_subjects.sort()

            if 0 <= question_index < len(question_subjects):
                subject = question_subjects[question_index]
                questions = self.questions[subject]

                question_number = input(
                    f"Enter the question number to update (1-{len(questions)}): "
                ).strip()
                try:
                    question_number = int(question_number)
                    question_number -= 1  # Adjust index for zero-based indexing

                    if 0 <= question_number < len(questions):
                        question = questions[question_number]
                        new_question_text = input(
                            "Enter the new question text: "
                        ).strip()
                        new_correct_answer = (
                            input("Enter the new correct answer ('True' or 'False'): ")
                            .strip()
                            .capitalize()
                        )

                        question.text = new_question_text
                        question.answer = new_correct_answer.lower()

                        print("\nQuestion updated successfully!")
                    else:
                        print("\nInvalid question number.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")
            else:
                print("\nInvalid index.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

        self.admin_menu()

    def list_questions(self):
        print("\nLIST OF QUESTIONS")
        question_subjects = list(self.questions.keys())
        question_subjects.sort()

        for i, subject in enumerate(question_subjects, 1):
            print(f"\n{i}. {subject}:")
            questions = self.questions[subject]

            for j, question in enumerate(questions, 1):
                print(f"   {j}. {question.text}")

        if not question_subjects:
            print("\nNo questions found.")

    def start(self):
        self.main_menu()


if __name__ == "__main__":
    quiz_app = QuizApp()
    quiz_app.start()
