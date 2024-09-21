import csv
import datetime
import logging

# Setup logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
QUESTION_FILE = 'questions.csv'

# Class to handle the exam logic
class ExamClient:
    def __init__(self):
        self.questions = []
        self.load_questions()
        self.student_name = ''
        self.university = ''
        self.score = 0

    def load_questions(self):
        """Load questions from CSV"""
        try:
            with open(QUESTION_FILE, mode='r') as file:
                reader = csv.DictReader(file)
                self.questions = list(reader)
            logging.info('Questions loaded successfully.')
        except Exception as e:
            logging.error(f'Error loading questions: {e}')

    def start_exam(self):
        """Start the exam by asking for student details and running the quiz"""
        try:
            now = datetime.datetime.now()
            print(f"Todays date and time: {now.strftime('%d/%b/%Y %H:%M:%S')}")
            self.student_name = input("Enter student name: ")
            self.university = input("Enter university: ")
            self.take_quiz()
            self.show_result()
        except Exception as e:
            logging.error(f'Error during exam: {e}')

    def take_quiz(self):
        """Display questions and take answers from the student"""
        for question in self.questions:
            print(f"{question['num']}) {question['question']}")
            print(f"op1) {question['option1']}")
            print(f"op2) {question['option2']}")
            print(f"op3) {question['option3']}")
            print(f"op4) {question['option4']}")
            answer = input("Enter your choice (op1, op2, op3, op4): ")
            if answer == question['correctoption']:
                self.score += 1

    def show_result(self):
        """Display the result at the end of the exam"""
        total_questions = len(self.questions)
        print(f"\nStudent name: {self.student_name}")
        print(f"University: {self.university}")
        print(f"Marks scored: {self.score} correct out of {total_questions} questions")

if __name__ == '__main__':
    exam = ExamClient()
    exam.start_exam()
