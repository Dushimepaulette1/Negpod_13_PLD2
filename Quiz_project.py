#!/usr/bin/python3
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer.lower()  # Convert answer to lowercase for case insensitivity
    
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
        self.users = []  # Initialize empty list to store users
        self.admins = []  # Initialize empty list to store admins
        self.questions = {
            "ICT": [
                Question("The internet is an example of a WAN. (True/False)", "True"),
                Question("HTML stands for HyperText Markup Language. (True/False)", "True"),
                Question("RAM is a type of permanent memory. (True/False)", "False"),
                Question("Python is a type of snake. (True/False)", "True"),
                Question("A byte is 16 bits. (True/False)", "False"),
                Question("Java is a scripting language. (True/False)", "False"),
                Question("HTTP stands for HyperText Transfer Protocol. (True/False)", "True"),
                Question("GUI stands for Graphical User Interface. (True/False)", "True"),
                Question("URL stands for Uniform Resource Locator. (True/False)", "True"),
                Question("LAN stands for Local Area Network. (True/False)", "True"),
                Question("The internet is a type of LAN. (True/False)", "False"),
                Question("JSP stands for Java Server Pages. (True/False)", "True"),
                Question("CD stands for Compact Disk. (True/False)", "True"),
                Question("HTTP stands for Hypertext Transfer Protocol. (True/False)", "True"),
                Question("JPEG stands for Joint Photographic Expert Group. (True/False)", "True"),
                Question("RAM stands for Random Access Memory. (True/False)", "True")
            ],
            "Maths": [
                Question("A triangle has three sides. (True/False)", "True"),
                Question("The square root of 49 is 8. (True/False)", "False"),
                Question("Pi is approximately 3.14159. (True/False)", "True"),
                Question("5 * 5 = 30. (True/False)", "False"),
                Question("A right angle is 90 degrees. (True/False)", "True"),
                Question("The sum of the angles in a triangle is 180 degrees. (True/False)", "True"),
                Question("The number 0 is an even number. (True/False)", "True"),
                Question("The Fibonacci sequence starts with 0 and 1. (True/False)", "True"),
                Question("A prime number has exactly two factors. (True/False)", "True"),
                Question("The area of a square is calculated as s * s. (True/False)", "True"),
                Question("C stands for Compilers. (True/False)", "True"),
                Question("V stands for Virtual. (True/False)", "True"),
                Question("F stands for Fast. (True/False)", "True"),
                Question("J stands for JavaScript. (True/False)", "True"),
                Question("L stands for Language. (True/False)", "True")
            ],
            "English": [
                Question("An adjective describes a noun. (True/False)", "True"),
                Question("'They're' is a contraction of 'they are'. (True/False)", "True"),
                Question("The word 'happy' is a noun. (True/False)", "False"),
                Question("The word 'quickly' is an adverb. (True/False)", "True"),
                Question("A pronoun takes the place of a noun. (True/False)", "True"),
                Question("Shakespeare wrote 'Romeo and Juliet'. (True/False)", "True"),
                Question("A palindrome reads the same forwards and backwards. (True/False)", "True"),
                Question("English is the most spoken language in the world. (True/False)", "False"),
                Question("A comma is used to separate items in a list. (True/False)", "True"),
                Question("The past tense of 'go' is 'gone'. (True/False)", "True"),
                Question("The word 'colour' is spelled with 'or' in American English. (True/False)", "False"),
                Question("The word 'the' is a preposition. (True/False)", "False"),
                Question("The word 'time' is a noun. (True/False)", "True"),
                Question("The word 'quick' is a verb. (True/False)", "False"),
                Question("The word 'yellow' is an adverb. (True/False)", "False")
            ],
            "Science": [
                Question("Water boils at 100 degrees Celsius. (True/False)", "True"),
                Question("Humans have three lungs. (True/False)", "False"),
                Question("Plants produce oxygen. (True/False)", "True"),
                Question("The sun is a planet. (True/False)", "False"),
                Question("Sound travels faster than light. (True/False)", "False"),
                Question("The Earth orbits the Moon. (True/False)", "False"),
                Question("The human body has 206 bones. (True/False)", "True"),
                Question("Gravity is stronger on the Moon than on Earth. (True/False)", "False"),
                Question("Oxygen is the most abundant element in Earth's atmosphere. (True/False)", "True"),
                Question("Mars is known as the 'Red Planet'. (True/False)", "True"),
                Question("The Milky Way is the galaxy that contains our Solar System. (True/False)", "True"),
                Question("Water covers approximately 71% of Earth's surface. (True/False)", "True"),
                Question("A light-year measures time. (True/False)", "False"),
                Question("Astronomy is the study of stars and planets. (True/False)", "True"),
                Question("A telescope is used to observe distant objects in space. (True/False)", "True")
            ],
            "General Knowledge": [
                Question("The capital of France is Paris. (True/False)", "True"),
                Question("The Great Wall of China is visible from space. (True/False)", "False"),
                Question("There are 50 states in the USA. (True/False)", "True"),
                Question("The largest ocean on Earth is the Atlantic Ocean. (True/False)", "False"),
                Question("Mount Everest is the tallest mountain in the world. (True/False)", "True"),
                Question("The Nile River is the longest river in the world. (True/False)", "False"),
                Question("Australia is both a country and a continent. (True/False)", "True"),
                Question("Albert Einstein developed the theory of relativity. (True/False)", "True"),
                Question("The first human to walk on the Moon was Neil Armstrong. (True/False)", "True"),
                Question("Venus is the hottest planet in our solar system. (True/False)", "True"),
                Question("An apple is a fruit. (True/False)", "True"),
                Question("The sky is purple. (True/False)", "False"),
                Question("Dogs meow. (True/False)", "False"),
                Question("The world is flat. (True/False)", "False"),
                Question("The sun rises in the west. (True/False)", "False")
            ]
        }
        self.current_user = None  # Initialize current user as None

