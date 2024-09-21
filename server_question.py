import csv
import os
import logging

# Setup logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
QUESTION_FILE = 'questions.csv'

# Class to manage the question bank
class QuestionMaster:
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """Load questions from CSV file into a nested data structure"""
        try:
            if os.path.exists(QUESTION_FILE):
                with open(QUESTION_FILE, mode='r') as file:
                    reader = csv.DictReader(file)
                    self.questions = list(reader)
            logging.info('Questions loaded successfully.')
        except Exception as e:
            logging.error(f'Error loading questions: {e}')
        
    def save_questions(self):
        """Save questions back to CSV file"""
        try:
            with open(QUESTION_FILE, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['num', 'question', 'option1', 'option2', 'option3', 'option4', 'correctoption'])
                writer.writeheader()
                writer.writerows(self.questions)
            logging.info('Questions saved successfully.')
        except Exception as e:
            logging.error(f'Error saving questions: {e}')
    
    def add_question(self):
        """Add a new question to the data structure"""
        try:
            num = len(self.questions) + 1
            question = input("Enter the question: ")
            option1 = input("Enter option 1: ")
            option2 = input("Enter option 2: ")
            option3 = input("Enter option 3: ")
            option4 = input("Enter option 4: ")
            correctoption = input("Enter the correct option (op1, op2, op3, or op4): ")
            self.questions.append({
                'num': num, 'question': question, 'option1': option1,
                'option2': option2, 'option3': option3, 'option4': option4, 'correctoption': correctoption
            })
            self.save_questions()
            logging.info('Question added successfully.')
        except Exception as e:
            logging.error(f'Error adding question: {e}')
    
    def search_question(self):
        """Search for a question by question number"""
        try:
            num = input("Enter question number to search: ")
            question = next((q for q in self.questions if q['num'] == num), None)
            if question:
                print(question)
            else:
                logging.info(f'Question number {num} not found.')
        except Exception as e:
            logging.error(f'Error searching for question: {e}')
    
    def delete_question(self):
        """Delete a question by number"""
        try:
            num = input("Enter question number to delete: ")
            self.questions = [q for q in self.questions if q['num'] != num]
            self.save_questions()
            logging.info(f'Question number {num} deleted successfully.')
        except Exception as e:
            logging.error(f'Error deleting question: {e}')
    
    def modify_question(self):
        """Modify an existing question by number"""
        try:
            num = input("Enter question number to modify: ")
            question = next((q for q in self.questions if q['num'] == num), None)
            if question:
                question['question'] = input("Enter new question text: ")
                question['option1'] = input("Enter option 1: ")
                question['option2'] = input("Enter option 2: ")
                question['option3'] = input("Enter option 3: ")
                question['option4'] = input("Enter option 4: ")
                question['correctoption'] = input("Enter the correct option (op1, op2, op3, or op4): ")
                self.save_questions()
                logging.info(f'Question number {num} modified successfully.')
            else:
                logging.info(f'Question number {num} not found.')
        except Exception as e:
            logging.error(f'Error modifying question: {e}')
    
    def display_all_questions(self):
        """Display all the questions"""
        if self.questions:
            for question in self.questions:
                print(question)
        else:
            logging.info('No questions available.')

def menu():
    """Menu for question master operations"""
    qm = QuestionMaster()
    while True:
        print("\n1) Add a question")
        print("2) Search for a Question")
        print("3) Delete a Question")
        print("4) Modify a Question")
        print("5) Display all Questions")
        print("6) Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            qm.add_question()
        elif choice == '2':
            qm.search_question()
        elif choice == '3':
            qm.delete_question()
        elif choice == '4':
            qm.modify_question()
        elif choice == '5':
            qm.display_all_questions()
        elif choice == '6':
            break
        else:
            logging.warning('Invalid choice!')

if __name__ == '__main__':
    menu()
