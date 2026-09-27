import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import random
from datetime import datetime


# ============================================================
# FILE NAMES
# ============================================================

USERS_FILE = "users.json"
QUESTIONS_FILE = "questions.json"
RESULTS_FILE = "results.json"


# ============================================================
# DEFAULT ADMIN LOGIN
# ============================================================

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


# ============================================================
# DEFAULT QUESTIONS - 30 PER TOPIC
# ============================================================

def build_default_questions():
    questions = []
    # Python: 30 questions
    questions.append({
        "question": 'Which keyword defines a function in Python?',
        "options": {'A': 'func', 'B': 'function', 'C': 'define', 'D': 'def'},
        "answer": 'D',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which data type stores True or False?',
        "options": {'A': 'String', 'B': 'Boolean', 'C': 'Integer', 'D': 'Float'},
        "answer": 'B',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which symbol starts a Python comment?',
        "options": {'A': '#', 'B': '--', 'C': '//', 'D': '/*'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which keyword creates a class?',
        "options": {'A': 'class', 'B': 'object', 'C': 'create', 'D': 'struct'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does len() return?',
        "options": {'A': 'Data type', 'B': 'Last index', 'C': 'Memory address', 'D': 'Number of items'},
        "answer": 'D',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which structure stores key-value pairs?',
        "options": {'A': 'Set', 'B': 'Dictionary', 'C': 'List', 'D': 'Tuple'},
        "answer": 'B',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which collection is ordered and mutable?',
        "options": {'A': 'Frozen set', 'B': 'Tuple', 'C': 'List', 'D': 'Set'},
        "answer": 'C',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which collection is immutable?',
        "options": {'A': 'Tuple', 'B': 'Set', 'C': 'Dictionary', 'D': 'List'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which operator performs floor division?',
        "options": {'A': '%', 'B': '**', 'C': '//', 'D': '/'},
        "answer": 'C',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which operator calculates a power?',
        "options": {'A': '^^', 'B': '**', 'C': '%%', 'D': '//'},
        "answer": 'B',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which keyword is used for exception handling?',
        "options": {'A': 'catch', 'B': 'try', 'C': 'error', 'D': 'check'},
        "answer": 'B',
        "topic": 'Python',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which block runs whether an exception occurs or not?',
        "options": {'A': 'except', 'B': 'raise', 'C': 'finally', 'D': 'else'},
        "answer": 'C',
        "topic": 'Python',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which keyword manually raises an exception?',
        "options": {'A': 'raise', 'B': 'error', 'C': 'throw', 'D': 'except'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a lambda in Python?',
        "options": {'A': 'Module', 'B': 'Loop', 'C': 'Class', 'D': 'Anonymous function'},
        "answer": 'D',
        "topic": 'Python',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which keyword imports a module?',
        "options": {'A': 'import', 'B': 'using', 'C': 'require', 'D': 'include'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which package manager commonly installs Python packages?',
        "options": {'A': 'npm', 'B': 'gem', 'C': 'maven', 'D': 'pip'},
        "answer": 'D',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does PEP 8 describe?',
        "options": {'A': 'Database rules', 'B': 'Python style guidelines', 'C': 'Web standards', 'D': 'Testing rules'},
        "answer": 'B',
        "topic": 'Python',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which function converts a value to an integer?',
        "options": {'A': 'int()', 'B': 'bool()', 'C': 'str()', 'D': 'float()'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which function converts a value to a string?',
        "options": {'A': 'char()', 'B': 'string()', 'C': 'str()', 'D': 'text()'},
        "answer": 'C',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does range(5) produce?',
        "options": {'A': '0 through 4', 'B': '0 through 5', 'C': '1 through 5', 'D': '5 only'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which keyword exits a loop immediately?',
        "options": {'A': 'exitloop', 'B': 'returnloop', 'C': 'break', 'D': 'stop'},
        "answer": 'C',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which keyword skips to the next loop iteration?',
        "options": {'A': 'passloop', 'B': 'next', 'C': 'continue', 'D': 'skip'},
        "answer": 'C',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does pass do?',
        "options": {'A': 'Stops program', 'B': 'Raises error', 'C': 'Repeats loop', 'D': 'Nothing; placeholder statement'},
        "answer": 'D',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which OOP concept hides internal implementation details?',
        "options": {'A': 'Encapsulation', 'B': 'Inheritance', 'C': 'Compilation', 'D': 'Iteration'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which OOP concept allows a class to derive from another class?',
        "options": {'A': 'Iteration', 'B': 'Parsing', 'C': 'Encapsulation', 'D': 'Inheritance'},
        "answer": 'D',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which special method initializes an object?',
        "options": {'A': '__init__()', 'B': '__newclass__()', 'C': '__create__()', 'D': '__start__()'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which function returns the type of an object?',
        "options": {'A': 'type()', 'B': 'typeof()', 'C': 'classof()', 'D': 'kind()'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which data structure contains unique unordered elements?',
        "options": {'A': 'Set', 'B': 'String', 'C': 'List', 'D': 'Tuple'},
        "answer": 'A',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does dictionary.get(key) do?',
        "options": {'A': 'Deletes a key', 'B': 'Retrieves a value for a key', 'C': 'Adds a key', 'D': 'Sorts a dictionary'},
        "answer": 'B',
        "topic": 'Python',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which statement is used to handle an exception?',
        "options": {'A': 'rescue', 'B': 'except', 'C': 'handle', 'D': 'catch'},
        "answer": 'B',
        "topic": 'Python',
        "difficulty": 'Easy'
    })
    # Artificial Intelligence: 30 questions
    questions.append({
        "question": 'What does AI stand for?',
        "options": {'A': 'Automated Internet', 'B': 'Advanced Information', 'C': 'Artificial Internet', 'D': 'Artificial Intelligence'},
        "answer": 'D',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is a branch of AI?',
        "options": {'A': 'Formatting', 'B': 'Word Processing', 'C': 'File Management', 'D': 'Machine Learning'},
        "answer": 'D',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is an intelligent agent?',
        "options": {'A': 'System that perceives and acts', 'B': 'A compiler', 'C': 'A printer', 'D': 'Only a database'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is the Turing Test used to evaluate?',
        "options": {'A': 'Machine intelligence', 'B': 'CPU speed', 'C': 'Storage size', 'D': 'Network bandwidth'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which AI field deals with human language?',
        "options": {'A': 'Networking', 'B': 'Natural Language Processing', 'C': 'Operating Systems', 'D': 'Computer Graphics'},
        "answer": 'B',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which AI field deals with images and video?',
        "options": {'A': 'Computer Vision', 'B': 'Compilers', 'C': 'Data Entry', 'D': 'Word Processing'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is an expert system?',
        "options": {'A': 'Web browser', 'B': 'Operating system', 'C': 'Rule-based knowledge system', 'D': 'Database engine'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a knowledge base?',
        "options": {'A': 'Collection of stored facts and rules', 'B': 'A graphics card', 'C': 'A compiler', 'D': 'A network cable'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which search uses a queue?',
        "options": {'A': 'Minimax', 'B': 'Depth-First Search', 'C': 'Breadth-First Search', 'D': 'Hill Climbing'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which search commonly uses a stack?',
        "options": {'A': 'Uniform Cost Search', 'B': 'Beam Search', 'C': 'Depth-First Search', 'D': 'Breadth-First Search'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is heuristic search?',
        "options": {'A': 'Database search', 'B': 'Text search', 'C': 'Search guided by estimated cost', 'D': 'Random search only'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'A* search combines path cost with what?',
        "options": {'A': 'Heuristic estimate', 'B': 'Image pixels', 'C': 'Database index', 'D': 'Random number'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is NLP?',
        "options": {'A': 'Processing human language', 'B': 'Processing hardware', 'C': 'Processing databases', 'D': 'Processing networks'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is speech recognition?',
        "options": {'A': 'Compressing data', 'B': 'Creating images', 'C': 'Converting speech to text or commands', 'D': 'Encrypting files'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is robotics?',
        "options": {'A': 'Field combining intelligent machines and control', 'B': 'Database management', 'C': 'Only web design', 'D': 'File compression'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is computer vision used for?',
        "options": {'A': 'Understanding visual data', 'B': 'Compiling code', 'C': 'Sorting files', 'D': 'Managing passwords'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is planning in AI?',
        "options": {'A': 'Creating databases', 'B': 'Formatting text', 'C': 'Selecting actions to achieve goals', 'D': 'Drawing charts'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a rational agent?',
        "options": {'A': 'Agent without sensors', 'B': 'Agent that never acts', 'C': 'Agent that chooses actions to maximize performance', 'D': 'Agent that always guesses'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a state space?',
        "options": {'A': 'Storage device', 'B': 'Network map only', 'C': 'Source code', 'D': 'Set of possible states of a problem'},
        "answer": 'D',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is minimax commonly used for?',
        "options": {'A': 'Image compression', 'B': 'Game playing', 'C': 'Database indexing', 'D': 'Speech synthesis'},
        "answer": 'B',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What does pruning in game search reduce?',
        "options": {'A': 'Image size', 'B': 'Training data', 'C': 'Database rows', 'D': 'Unnecessary branches'},
        "answer": 'D',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is fuzzy logic?',
        "options": {'A': 'Network routing', 'B': 'Logic using only true/false', 'C': 'Logic with degrees of truth', 'D': 'Database logic'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a neural network inspired by?',
        "options": {'A': 'Database tables', 'B': 'Biological neurons', 'C': 'CPU registers', 'D': 'Network cables'},
        "answer": 'B',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is an AI chatbot designed to do?',
        "options": {'A': 'Only compile code', 'B': 'Interact using natural language', 'C': 'Only store images', 'D': 'Only route packets'},
        "answer": 'B',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is recommendation in AI?',
        "options": {'A': 'Creating IP addresses', 'B': 'Formatting disks', 'C': 'Encrypting data', 'D': 'Suggesting relevant items'},
        "answer": 'D',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is knowledge representation?',
        "options": {'A': 'Representing facts and relationships for reasoning', 'B': 'Designing CPUs', 'C': 'Managing cables', 'D': 'Compressing videos'},
        "answer": 'A',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is reasoning in AI?',
        "options": {'A': 'Installing software', 'B': 'Deriving conclusions from knowledge', 'C': 'Drawing interfaces', 'D': 'Deleting data'},
        "answer": 'B',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is supervised AI learning based on?',
        "options": {'A': 'Hardware signals', 'B': 'Only random numbers', 'C': 'Labeled examples', 'D': 'No data'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is an autonomous system?',
        "options": {'A': 'A database table', 'B': 'A static webpage', 'C': 'System that can operate with limited human intervention', 'D': 'A manual calculator'},
        "answer": 'C',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is an AI model?',
        "options": {'A': 'A file extension', 'B': 'A network cable', 'C': 'A keyboard', 'D': 'Learned or programmed representation used to make predictions or decisions'},
        "answer": 'D',
        "topic": 'Artificial Intelligence',
        "difficulty": 'Easy'
    })
    # Machine Learning: 30 questions
    questions.append({
        "question": 'What is machine learning?',
        "options": {'A': 'Writing only manual rules', 'B': 'Managing hardware', 'C': 'Creating networks', 'D': 'Learning patterns from data'},
        "answer": 'D',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which learning uses labeled data?',
        "options": {'A': 'Unsupervised learning', 'B': 'Manual learning', 'C': 'Supervised learning', 'D': 'Random learning'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which learning uses unlabeled data?',
        "options": {'A': 'Unsupervised learning', 'B': 'Manual learning', 'C': 'Rule learning', 'D': 'Supervised learning'},
        "answer": 'A',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which learning uses a reward signal?',
        "options": {'A': 'Batch learning', 'B': 'Supervised learning', 'C': 'Reinforcement learning', 'D': 'Unsupervised learning'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which algorithm is used for classification?',
        "options": {'A': 'K-Means only', 'B': 'Decision Tree', 'C': 'Apriori only', 'D': 'PCA only'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which algorithm is commonly used for clustering?',
        "options": {'A': 'Naive Bayes', 'B': 'K-Means', 'C': 'Linear Regression', 'D': 'Logistic Regression'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does regression predict?',
        "options": {'A': 'Only text', 'B': 'Only categories', 'C': 'Continuous values', 'D': 'Only images'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does classification predict?',
        "options": {'A': 'Only continuous values', 'B': 'Classes or categories', 'C': 'Database keys', 'D': 'Network routes'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is overfitting?',
        "options": {'A': 'Data is deleted', 'B': 'No training occurs', 'C': 'Model learns training data too closely', 'D': 'Model is too simple'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is underfitting?',
        "options": {'A': 'Model is too simple to capture patterns', 'B': 'Model has too many layers', 'C': 'Model memorizes all data', 'D': 'Model has no features'},
        "answer": 'A',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a training set?',
        "options": {'A': 'Unused data', 'B': 'Data used only after deployment', 'C': 'Only test labels', 'D': 'Data used to learn model parameters'},
        "answer": 'D',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a test set?',
        "options": {'A': 'Data used to train weights', 'B': 'Only duplicate data', 'C': 'Only missing data', 'D': 'Data used for final evaluation'},
        "answer": 'D',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Why use a validation set?',
        "options": {'A': 'To replace training', 'B': 'To tune and compare models', 'C': 'To store passwords', 'D': 'To remove all features'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is accuracy?',
        "options": {'A': 'Mean squared error', 'B': 'Fraction of false positives only', 'C': 'Number of features', 'D': 'Fraction of correct predictions'},
        "answer": 'D',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does precision measure?',
        "options": {'A': 'Correct negatives only', 'B': 'Correct positive predictions among predicted positives', 'C': 'Training speed', 'D': 'All correct predictions'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What does recall measure?',
        "options": {'A': 'Training time', 'B': 'Model size', 'C': 'Correct positives among actual positives', 'D': 'Correct negatives among actual negatives'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is F1-score?',
        "options": {'A': 'Number of classes', 'B': 'Mean of features', 'C': 'Harmonic mean of precision and recall', 'D': 'Training loss only'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which algorithm uses nearest examples?',
        "options": {'A': 'K-Means', 'B': 'Decision Tree', 'C': 'K-Nearest Neighbors', 'D': 'PCA'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which model uses hyperplanes for classification?',
        "options": {'A': 'K-Means', 'B': 'Support Vector Machine', 'C': 'PCA', 'D': 'Apriori'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is an ensemble method?',
        "options": {'A': 'Using no validation', 'B': 'Combining multiple models', 'C': 'Removing training data', 'D': 'Using one feature'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Random Forest is based on multiple what?',
        "options": {'A': 'Clusters', 'B': 'Neural networks', 'C': 'Decision trees', 'D': 'SVMs only'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is feature scaling?',
        "options": {'A': 'Deleting features', 'B': 'Creating labels', 'C': 'Splitting classes', 'D': 'Putting features on comparable scales'},
        "answer": 'D',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which method commonly scales data to 0 to 1?',
        "options": {'A': 'Bagging', 'B': 'Min-Max scaling', 'C': 'Pruning', 'D': 'One-hot encoding'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is one-hot encoding used for?',
        "options": {'A': 'Scaling continuous values', 'B': 'Selecting a model', 'C': 'Representing categorical values numerically', 'D': 'Removing outliers'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is cross-validation?',
        "options": {'A': 'Repeated train-validation splitting', 'B': 'Training without testing', 'C': 'Deleting samples', 'D': 'Only feature scaling'},
        "answer": 'A',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a hyperparameter?',
        "options": {'A': 'A database key', 'B': 'A prediction', 'C': 'Setting chosen before/during training rather than learned as a model parameter', 'D': 'A target label'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is gradient descent used for?',
        "options": {'A': 'Encrypting data', 'B': 'Optimizing model parameters', 'C': 'Collecting labels', 'D': 'Sorting rows'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a loss function?',
        "options": {'A': 'Stores labels', 'B': 'Measures model error during training', 'C': 'Creates plots', 'D': 'Counts features'},
        "answer": 'B',
        "topic": 'Machine Learning',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is dimensionality reduction?',
        "options": {'A': 'Increasing dataset size', 'B': 'Adding labels', 'C': 'Reducing number of input features', 'D': 'Duplicating rows'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which technique reduces dimensions linearly?',
        "options": {'A': 'Random Forest', 'B': 'Naive Bayes', 'C': 'PCA', 'D': 'KNN'},
        "answer": 'C',
        "topic": 'Machine Learning',
        "difficulty": 'Medium'
    })
    # HTML: 30 questions
    questions.append({
        "question": 'What does HTML stand for?',
        "options": {'A': 'Home Tool Markup Language', 'B': 'HyperText Markup Language', 'C': 'HighText Machine Language', 'D': 'Hyperlink Text Management Language'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag creates the largest heading?',
        "options": {'A': '<h1>', 'B': '<head>', 'C': '<h6>', 'D': '<heading>'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag creates a paragraph?',
        "options": {'A': '<para>', 'B': '<p>', 'C': '<text>', 'D': '<pg>'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag creates a hyperlink?',
        "options": {'A': '<url>', 'B': '<a>', 'C': '<link>', 'D': '<href>'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which attribute specifies a link destination?',
        "options": {'A': 'targeturl', 'B': 'href', 'C': 'link', 'D': 'src'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag inserts an image?',
        "options": {'A': '<src>', 'B': '<img>', 'C': '<image>', 'D': '<pic>'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which attribute provides alternative image text?',
        "options": {'A': 'title', 'B': 'alt', 'C': 'text', 'D': 'caption'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag creates an unordered list?',
        "options": {'A': '<list>', 'B': '<ol>', 'C': '<li>', 'D': '<ul>'},
        "answer": 'D',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag creates an ordered list?',
        "options": {'A': '<order>', 'B': '<ul>', 'C': '<ol>', 'D': '<li>'},
        "answer": 'C',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag represents a list item?',
        "options": {'A': '<ulitem>', 'B': '<listitem>', 'C': '<li>', 'D': '<item>'},
        "answer": 'C',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag defines a table row?',
        "options": {'A': '<th>', 'B': '<row>', 'C': '<tr>', 'D': '<td>'},
        "answer": 'C',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag defines a table data cell?',
        "options": {'A': '<td>', 'B': '<data>', 'C': '<cell>', 'D': '<tr>'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag defines a table header cell?',
        "options": {'A': '<th>', 'B': '<theadcell>', 'C': '<trh>', 'D': '<header>'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag creates a form?',
        "options": {'A': '<form>', 'B': '<input>', 'C': '<submit>', 'D': '<field>'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which input type hides typed characters?',
        "options": {'A': 'password', 'B': 'hidden', 'C': 'secure', 'D': 'secret'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which input type selects one option from a group?',
        "options": {'A': 'selectone', 'B': 'checkbox', 'C': 'radio', 'D': 'choice'},
        "answer": 'C',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which input type allows multiple selections?',
        "options": {'A': 'checkbox', 'B': 'radio', 'C': 'select', 'D': 'multiple'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag creates a drop-down list?',
        "options": {'A': '<dropdown>', 'B': '<select>', 'C': '<optionlist>', 'D': '<listbox>'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag defines an option in a select?',
        "options": {'A': '<option>', 'B': '<choice>', 'C': '<selectitem>', 'D': '<item>'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag embeds a video?',
        "options": {'A': '<video>', 'B': '<vid>', 'C': '<media>', 'D': '<movie>'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which tag embeds audio?',
        "options": {'A': '<mp3>', 'B': '<music>', 'C': '<sound>', 'D': '<audio>'},
        "answer": 'D',
        "topic": 'HTML',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which declaration identifies an HTML5 document?',
        "options": {'A': '<!DOCTYPE html>', 'B': '<HTML5>', 'C': '<!HTML>', 'D': '<DOCTYPE5>'},
        "answer": 'A',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which semantic tag represents navigation links?',
        "options": {'A': '<links>', 'B': '<nav>', 'C': '<navigate>', 'D': '<menu>'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which semantic tag represents the main content?',
        "options": {'A': '<bodymain>', 'B': '<main>', 'C': '<content>', 'D': '<primary>'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag defines the document title shown in a browser tab?',
        "options": {'A': '<headtitle>', 'B': '<caption>', 'C': '<tab>', 'D': '<title>'},
        "answer": 'D',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag contains metadata?',
        "options": {'A': '<info>', 'B': '<meta>', 'C': '<head>', 'D': '<data>'},
        "answer": 'C',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag contains visible page content?',
        "options": {'A': '<mainpage>', 'B': '<content>', 'C': '<page>', 'D': '<body>'},
        "answer": 'D',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which attribute gives a unique identifier?',
        "options": {'A': 'key', 'B': 'id', 'C': 'nameid', 'D': 'class'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which attribute groups elements for styling?',
        "options": {'A': 'styleclass', 'B': 'class', 'C': 'css', 'D': 'group'},
        "answer": 'B',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which tag creates a line break?',
        "options": {'A': '<newline>', 'B': '<lb>', 'C': '<break>', 'D': '<br>'},
        "answer": 'D',
        "topic": 'HTML',
        "difficulty": 'Easy'
    })
    # SQL: 30 questions
    questions.append({
        "question": 'What does SQL stand for?',
        "options": {'A': 'Structured Question Language', 'B': 'Simple Query Language', 'C': 'System Query Logic', 'D': 'Structured Query Language'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which command retrieves data?',
        "options": {'A': 'READ', 'B': 'FETCH', 'C': 'GET', 'D': 'SELECT'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which clause filters rows?',
        "options": {'A': 'CHECK', 'B': 'FILTER', 'C': 'HAVING', 'D': 'WHERE'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which clause sorts results?',
        "options": {'A': 'ARRANGE', 'B': 'GROUP BY', 'C': 'ORDER BY', 'D': 'SORT'},
        "answer": 'C',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which keyword removes duplicate rows from results?',
        "options": {'A': 'UNIQUEONLY', 'B': 'NODUP', 'C': 'DIFFERENT', 'D': 'DISTINCT'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which function counts rows?',
        "options": {'A': 'NUMBER()', 'B': 'COUNT()', 'C': 'TOTAL()', 'D': 'ROWS()'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which function calculates an average?',
        "options": {'A': 'MEAN()', 'B': 'MID()', 'C': 'AVERAGE()', 'D': 'AVG()'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which function finds the largest value?',
        "options": {'A': 'LARGE()', 'B': 'MAX()', 'C': 'HIGH()', 'D': 'TOP()'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which function finds the smallest value?',
        "options": {'A': 'SMALL()', 'B': 'MIN()', 'C': 'BOTTOM()', 'D': 'LOW()'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which clause groups rows?',
        "options": {'A': 'COLLECT BY', 'B': 'CLUSTER BY', 'C': 'ORDER BY', 'D': 'GROUP BY'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which clause filters grouped results?',
        "options": {'A': 'GROUPFILTER', 'B': 'AFTER', 'C': 'HAVING', 'D': 'WHERE'},
        "answer": 'C',
        "topic": 'SQL',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which join returns matching rows from both tables?',
        "options": {'A': 'EQUAL JOIN', 'B': 'INNER JOIN', 'C': 'COMMON JOIN', 'D': 'MATCH JOIN'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which join returns all rows from the left table?',
        "options": {'A': 'RIGHT JOIN', 'B': 'LEFT JOIN', 'C': 'FULL JOIN', 'D': 'INNER JOIN'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which command adds new rows?',
        "options": {'A': 'INSERT', 'B': 'ADD ROW', 'C': 'APPEND', 'D': 'CREATE ROW'},
        "answer": 'A',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which command modifies existing rows?',
        "options": {'A': 'ALTER ROW', 'B': 'MODIFY', 'C': 'CHANGE', 'D': 'UPDATE'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which command removes rows?',
        "options": {'A': 'REMOVE', 'B': 'DELETE', 'C': 'DROP ROW', 'D': 'ERASE'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which command creates a table?',
        "options": {'A': 'BUILD TABLE', 'B': 'CREATE TABLE', 'C': 'MAKE TABLE', 'D': 'NEW TABLE'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which command changes table structure?',
        "options": {'A': 'MODIFY DATA', 'B': 'UPDATE TABLE', 'C': 'ALTER TABLE', 'D': 'CHANGE TABLE DATA'},
        "answer": 'C',
        "topic": 'SQL',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which command deletes a table?',
        "options": {'A': 'REMOVE TABLE', 'B': 'CLEAR TABLE', 'C': 'DELETE TABLE', 'D': 'DROP TABLE'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a primary key?',
        "options": {'A': 'Unique identifier for rows', 'B': 'Duplicate field', 'C': 'Optional comment', 'D': 'Foreign reference only'},
        "answer": 'A',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a foreign key?',
        "options": {'A': 'Primary password', 'B': 'Duplicate key', 'C': 'Sorting key', 'D': "Column referencing another table's key"},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which constraint prevents NULL values?',
        "options": {'A': 'NONULLS', 'B': 'REQUIRED', 'C': 'NO EMPTY', 'D': 'NOT NULL'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which constraint ensures uniqueness?',
        "options": {'A': 'DISTINCT', 'B': 'SINGLE', 'C': 'UNIQUE', 'D': 'ONLY'},
        "answer": 'C',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which command saves a transaction?',
        "options": {'A': 'SAVE', 'B': 'STORE', 'C': 'COMMIT', 'D': 'APPLY'},
        "answer": 'C',
        "topic": 'SQL',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which command undoes a transaction?',
        "options": {'A': 'REVERT', 'B': 'ROLLBACK', 'C': 'CANCELSQL', 'D': 'UNDO'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is an index used for?',
        "options": {'A': 'Storing images', 'B': 'Creating users', 'C': 'Encrypting passwords', 'D': 'Faster data retrieval'},
        "answer": 'D',
        "topic": 'SQL',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a subquery?',
        "options": {'A': 'Query nested inside another query', 'B': 'Query without SELECT', 'C': 'Deleted query', 'D': 'Backup query'},
        "answer": 'A',
        "topic": 'SQL',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which operator tests whether a value is within a range?',
        "options": {'A': 'WITHIN', 'B': 'BETWEEN', 'C': 'RANGE', 'D': 'INRANGE'},
        "answer": 'B',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which operator tests membership in a list?',
        "options": {'A': 'IN', 'B': 'LISTED', 'C': 'CONTAINS', 'D': 'MEMBER'},
        "answer": 'A',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which wildcard represents any sequence of characters in LIKE?',
        "options": {'A': '?', 'B': '*', 'C': '%', 'D': '_'},
        "answer": 'C',
        "topic": 'SQL',
        "difficulty": 'Easy'
    })
    # Data Science: 30 questions
    questions.append({
        "question": 'What is data science?',
        "options": {'A': 'Only web development', 'B': 'Only statistics', 'C': 'Field that extracts insights from data', 'D': 'Only database design'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which Python library is widely used for tabular data?',
        "options": {'A': 'Django', 'B': 'Pandas', 'C': 'Flask', 'D': 'Tkinter'},
        "answer": 'B',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which library provides arrays and numerical operations?',
        "options": {'A': 'NumPy', 'B': 'Requests', 'C': 'PyGame', 'D': 'BeautifulSoup'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which library is commonly used for plotting?',
        "options": {'A': 'TkinterSQL', 'B': 'NumPyPlotOnly', 'C': 'Matplotlib', 'D': 'PandasSQL'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is data cleaning?',
        "options": {'A': 'Fixing missing, incorrect, or inconsistent data', 'B': 'Deleting all data', 'C': 'Printing data', 'D': 'Encrypting data'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is an outlier?',
        "options": {'A': 'Observation far from typical values', 'B': 'Normal value', 'C': 'Duplicate table', 'D': 'Missing column'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is missing data?',
        "options": {'A': 'Correct value', 'B': 'Extra row', 'C': 'Expected value that is absent', 'D': 'Sorted data'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is exploratory data analysis?',
        "options": {'A': 'Writing APIs', 'B': 'Deploying software', 'C': 'Investigating data patterns and distributions', 'D': 'Encrypting files'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a histogram used for?',
        "options": {'A': 'Storing data', 'B': 'Showing distribution of numerical data', 'C': 'Displaying network packets', 'D': 'Showing source code'},
        "answer": 'B',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does a scatter plot show?',
        "options": {'A': 'Database keys', 'B': 'Text paragraphs', 'C': 'Relationship between two numerical variables', 'D': 'Only categories'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is correlation?',
        "options": {'A': 'Model accuracy only', 'B': 'Cause of every event', 'C': 'Data size', 'D': 'Measure of association between variables'},
        "answer": 'D',
        "topic": 'Data Science',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a positive correlation?',
        "options": {'A': 'One increases as other always decreases', 'B': 'No relationship', 'C': 'Both remain constant', 'D': 'Variables tend to increase together'},
        "answer": 'D',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is mean?',
        "options": {'A': 'Middle value only', 'B': 'Arithmetic average', 'C': 'Most frequent value', 'D': 'Range'},
        "answer": 'B',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is median?',
        "options": {'A': 'Middle value after ordering', 'B': 'Most frequent value', 'C': 'Largest value', 'D': 'Arithmetic average'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is mode?',
        "options": {'A': 'Average', 'B': 'Smallest value', 'C': 'Most frequent value', 'D': 'Middle value'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is standard deviation?',
        "options": {'A': 'Number of rows', 'B': 'Measure of center', 'C': 'Measure of spread around the mean', 'D': 'Model score'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is normalization?',
        "options": {'A': 'Removing labels', 'B': 'Rescaling values to a common range', 'C': 'Adding rows', 'D': 'Sorting columns'},
        "answer": 'B',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is data visualization?',
        "options": {'A': 'Graphical representation of data', 'B': 'Data encryption', 'C': 'Database backup', 'D': 'Data deletion'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a dashboard?',
        "options": {'A': 'Visual display of key metrics and charts', 'B': 'Python package', 'C': 'SQL command', 'D': 'Operating system'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is feature engineering?',
        "options": {'A': 'Deleting all features', 'B': 'Creating useful input features from raw data', 'C': 'Deploying servers', 'D': 'Writing documentation'},
        "answer": 'B',
        "topic": 'Data Science',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is sampling?',
        "options": {'A': 'Sorting data', 'B': 'Encrypting data', 'C': 'Deleting data randomly', 'D': 'Selecting a subset of data'},
        "answer": 'D',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is bias in data?',
        "options": {'A': 'Systematic distortion or imbalance', 'B': 'File size', 'C': 'Random formatting', 'D': 'Data type'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is data preprocessing?',
        "options": {'A': 'Preparing data before analysis or modeling', 'B': 'Backing up code', 'C': 'Deleting a model', 'D': 'Publishing a website'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a categorical variable?',
        "options": {'A': 'Always a continuous number', 'B': 'Variable representing categories', 'C': 'Only a timestamp', 'D': 'Only an image'},
        "answer": 'B',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a numerical variable?',
        "options": {'A': 'Boolean only', 'B': 'Text category only', 'C': 'Variable represented by numeric values', 'D': 'Image label only'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is time-series data?',
        "options": {'A': 'Observations indexed over time', 'B': 'Only categorical data', 'C': 'Only image data', 'D': 'Random unordered data'},
        "answer": 'A',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is ETL?',
        "options": {'A': 'Encode, Test, Link', 'B': 'Evaluate, Train, Learn', 'C': 'Extract, Transform, Load', 'D': 'Extract, Test, Label'},
        "answer": 'C',
        "topic": 'Data Science',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a data warehouse?',
        "options": {'A': 'Operating system', 'B': 'Programming language', 'C': 'Web server', 'D': 'Centralized store for analytical data'},
        "answer": 'D',
        "topic": 'Data Science',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a data pipeline?',
        "options": {'A': 'A single SQL query', 'B': 'Automated flow of data through processing steps', 'C': 'A chart', 'D': 'A computer cable'},
        "answer": 'B',
        "topic": 'Data Science',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is reproducibility in data science?',
        "options": {'A': 'Deleting source data', 'B': 'Ability to obtain consistent results using the same process and data', 'C': 'Changing methods every time', 'D': 'Using random methods only'},
        "answer": 'B',
        "topic": 'Data Science',
        "difficulty": 'Medium'
    })
    # Computer Networks: 30 questions
    questions.append({
        "question": 'What is a computer network?',
        "options": {'A': 'A text editor', 'B': 'A database only', 'C': 'A single CPU', 'D': 'Connected devices that communicate'},
        "answer": 'D',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does LAN stand for?',
        "options": {'A': 'Large Access Network', 'B': 'Local Access Node', 'C': 'Local Area Network', 'D': 'Linked Area Node'},
        "answer": 'C',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does WAN stand for?',
        "options": {'A': 'Web Area Node', 'B': 'Wide Access Node', 'C': 'Wireless Access Network', 'D': 'Wide Area Network'},
        "answer": 'D',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which device connects different networks?',
        "options": {'A': 'Router', 'B': 'Hub', 'C': 'Repeater', 'D': 'Switch'},
        "answer": 'A',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which device forwards frames within a LAN?',
        "options": {'A': 'Switch', 'B': 'Gateway only', 'C': 'Router', 'D': 'Modem'},
        "answer": 'A',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol translates domain names to IP addresses?',
        "options": {'A': 'FTP', 'B': 'DHCP', 'C': 'DNS', 'D': 'HTTP'},
        "answer": 'C',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol automatically assigns IP addresses?',
        "options": {'A': 'DNS', 'B': 'SMTP', 'C': 'ARP', 'D': 'DHCP'},
        "answer": 'D',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol is used for web pages?',
        "options": {'A': 'SSH', 'B': 'HTTP', 'C': 'SMTP', 'D': 'FTP'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which secure protocol is used for web pages?',
        "options": {'A': 'HTTP', 'B': 'HTTPS', 'C': 'Telnet', 'D': 'FTP'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol transfers files?',
        "options": {'A': 'DNS', 'B': 'SMTP', 'C': 'ARP', 'D': 'FTP'},
        "answer": 'D',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol is used for email sending?',
        "options": {'A': 'FTP', 'B': 'POP3', 'C': 'IMAP', 'D': 'SMTP'},
        "answer": 'D',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol is commonly used to receive email while keeping it on server?',
        "options": {'A': 'SMTP', 'B': 'IMAP', 'C': 'FTP', 'D': 'DNS'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is an IP address?',
        "options": {'A': 'Physical cable', 'B': 'Password', 'C': 'Logical address for a network interface', 'D': 'File name'},
        "answer": 'C',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a MAC address?',
        "options": {'A': 'Web URL', 'B': 'Hardware/network interface address', 'C': 'Port number', 'D': 'Subnet mask'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol maps IP addresses to MAC addresses on a LAN?',
        "options": {'A': 'DHCP', 'B': 'ARP', 'C': 'ICMP', 'D': 'DNS'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which protocol reports network errors and diagnostics?',
        "options": {'A': 'HTTP', 'B': 'FTP', 'C': 'ICMP', 'D': 'SMTP'},
        "answer": 'C',
        "topic": 'Computer Networks',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a port number?',
        "options": {'A': 'Physical cable number', 'B': 'Logical endpoint identifier for network services', 'C': 'IP version', 'D': 'MAC address'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which OSI layer handles routing?',
        "options": {'A': 'Session layer', 'B': 'Network layer', 'C': 'Physical layer', 'D': 'Transport layer'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which OSI layer handles reliable end-to-end delivery?',
        "options": {'A': 'Physical layer', 'B': 'Transport layer', 'C': 'Presentation layer', 'D': 'Network layer'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which OSI layer transmits raw bits?',
        "options": {'A': 'Session layer', 'B': 'Physical layer', 'C': 'Application layer', 'D': 'Network layer'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol is connection-oriented?',
        "options": {'A': 'ICMP', 'B': 'UDP', 'C': 'TCP', 'D': 'IP'},
        "answer": 'C',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which protocol is connectionless?',
        "options": {'A': 'SSH', 'B': 'TCP', 'C': 'FTP', 'D': 'UDP'},
        "answer": 'D',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is bandwidth?',
        "options": {'A': 'Delay only', 'B': 'Data transfer capacity', 'C': 'Packet size only', 'D': 'IP address range'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is latency?',
        "options": {'A': 'Maximum speed', 'B': 'Packet count', 'C': 'Time delay in communication', 'D': 'Cable length only'},
        "answer": 'C',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is packet switching?',
        "options": {'A': 'Sending one continuous signal only', 'B': 'Database sorting', 'C': 'File compression', 'D': 'Sending data in packets across a network'},
        "answer": 'D',
        "topic": 'Computer Networks',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a firewall?',
        "options": {'A': 'Network cable', 'B': 'System that controls network traffic', 'C': 'File system', 'D': 'Router antenna'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is topology?',
        "options": {'A': 'Protocol name', 'B': 'Arrangement of network devices and links', 'C': 'Encryption method', 'D': 'IP address type'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which topology has a central connecting device?',
        "options": {'A': 'Mesh', 'B': 'Bus', 'C': 'Star', 'D': 'Ring'},
        "answer": 'C',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which topology connects devices in a closed loop?',
        "options": {'A': 'Bus', 'B': 'Ring', 'C': 'Tree', 'D': 'Star'},
        "answer": 'B',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is network congestion?',
        "options": {'A': 'Too much traffic for available capacity', 'B': 'No network traffic', 'C': 'High storage', 'D': 'Strong encryption'},
        "answer": 'A',
        "topic": 'Computer Networks',
        "difficulty": 'Easy'
    })
    # DBMS: 30 questions
    questions.append({
        "question": 'What does DBMS stand for?',
        "options": {'A': 'Database Memory System', 'B': 'Data Backup Management Service', 'C': 'Database Management System', 'D': 'Digital Base Management System'},
        "answer": 'C',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a database?',
        "options": {'A': 'A network cable', 'B': 'Organized collection of data', 'C': 'An operating system', 'D': 'Only a program'},
        "answer": 'B',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a table?',
        "options": {'A': 'A network map', 'B': 'A programming loop', 'C': 'Rows and columns storing related data', 'D': 'Only a chart'},
        "answer": 'C',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a row?',
        "options": {'A': 'A record in a table', 'B': 'A database server', 'C': 'A constraint', 'D': 'A column name'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a column?',
        "options": {'A': 'A query result only', 'B': 'An attribute/field of a table', 'C': 'A row record', 'D': 'A complete database'},
        "answer": 'B',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a primary key?',
        "options": {'A': 'Sorting order', 'B': 'Optional description', 'C': 'Duplicate value', 'D': 'Unique identifier for each row'},
        "answer": 'D',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is normalization?',
        "options": {'A': 'Organizing data to reduce redundancy', 'B': 'Deleting tables', 'C': 'Increasing duplicates', 'D': 'Encrypting data'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is denormalization?',
        "options": {'A': 'Encrypting records', 'B': 'Deleting keys', 'C': 'Removing all redundancy', 'D': 'Adding controlled redundancy for performance or convenience'},
        "answer": 'D',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a transaction?',
        "options": {'A': 'Logical unit of database work', 'B': 'A backup file', 'C': 'A user account', 'D': 'A table column'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does ACID stand for?',
        "options": {'A': 'Accuracy, Control, Integrity, Data', 'B': 'Access, Consistency, Index, Data', 'C': 'Atomicity, Control, Isolation, Data', 'D': 'Atomicity, Consistency, Isolation, Durability'},
        "answer": 'D',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What does atomicity mean?',
        "options": {'A': 'Queries are sorted', 'B': 'Data is duplicated', 'C': 'Transactions are always fast', 'D': 'Transaction happens completely or not at all'},
        "answer": 'D',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What does consistency ensure?',
        "options": {'A': 'All data is duplicated', 'B': 'Database remains valid according to rules', 'C': 'Users cannot log in', 'D': 'Queries never fail'},
        "answer": 'B',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What does isolation address?',
        "options": {'A': 'Backup size', 'B': 'Network speed', 'C': 'Concurrent transactions not interfering incorrectly', 'D': 'Disk formatting'},
        "answer": 'C',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What does durability mean?',
        "options": {'A': 'Queries are always fast', 'B': 'Tables are normalized', 'C': 'Committed changes survive failures', 'D': 'Rows are unique'},
        "answer": 'C',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a schema?',
        "options": {'A': 'A user password', 'B': 'A query result', 'C': 'A backup only', 'D': 'Structure/design of a database'},
        "answer": 'D',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a view?',
        "options": {'A': 'Database server', 'B': 'Virtual table based on a query', 'C': 'Backup table only', 'D': 'Physical cable'},
        "answer": 'B',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a stored procedure?',
        "options": {'A': 'A password', 'B': 'A table index', 'C': 'Saved program of SQL statements', 'D': 'A view only'},
        "answer": 'C',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a trigger?',
        "options": {'A': 'Manual query', 'B': 'Action automatically executed by a database event', 'C': 'Database password', 'D': 'Table row'},
        "answer": 'B',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is an index?',
        "options": {'A': 'Structure that can speed up searches', 'B': 'A constraint only', 'C': 'A backup', 'D': 'A duplicate database'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is referential integrity?',
        "options": {'A': 'Sorting rows', 'B': 'Encrypting columns', 'C': 'Keeping foreign-key relationships valid', 'D': 'Removing indexes'},
        "answer": 'C',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is data redundancy?',
        "options": {'A': 'Unnecessary repeated data', 'B': 'Missing data', 'C': 'Encrypted data', 'D': 'Sorted data'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is concurrency control?',
        "options": {'A': 'Changing passwords', 'B': 'Formatting tables', 'C': 'Managing simultaneous database operations', 'D': 'Creating backups'},
        "answer": 'C',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a deadlock?',
        "options": {'A': 'Transactions waiting indefinitely for each other', 'B': 'Duplicate row', 'C': 'Fast query', 'D': 'Database backup'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a database administrator?',
        "options": {'A': 'Person responsible for managing databases', 'B': 'Only a programmer', 'C': 'Only a network user', 'D': 'A web designer'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is backup?',
        "options": {'A': 'Copy of data for recovery', 'B': 'Sorting records', 'C': 'Deleting data', 'D': 'Creating indexes'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is recovery?',
        "options": {'A': 'Creating a table', 'B': 'Running SELECT', 'C': 'Restoring database after failure', 'D': 'Changing a password'},
        "answer": 'C',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a candidate key?',
        "options": {'A': 'Any duplicate field', 'B': 'Index only', 'C': 'Foreign key only', 'D': 'Minimal attribute set that uniquely identifies a row'},
        "answer": 'D',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a composite key?',
        "options": {'A': 'Key made from multiple columns', 'B': 'Only foreign key', 'C': 'Key with no columns', 'D': 'Temporary password'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is an entity?',
        "options": {'A': 'A backup', 'B': 'Distinct real-world object represented in a database', 'C': 'Only a query', 'D': 'A constraint'},
        "answer": 'B',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a relationship?',
        "options": {'A': 'Association between entities', 'B': 'A password', 'C': 'A query error', 'D': 'A table backup'},
        "answer": 'A',
        "topic": 'DBMS',
        "difficulty": 'Easy'
    })
    # Cloud Computing: 30 questions
    questions.append({
        "question": 'What is cloud computing?',
        "options": {'A': 'A programming language', 'B': 'A database table', 'C': 'Only local computing', 'D': 'On-demand access to computing resources over a network'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is a cloud service model?',
        "options": {'A': 'HTTP', 'B': 'LAN', 'C': 'IaaS', 'D': 'CPU'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does IaaS provide?',
        "options": {'A': 'Only source code', 'B': 'Virtualized infrastructure', 'C': 'Only database queries', 'D': 'Complete end-user application only'},
        "answer": 'B',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does PaaS provide?',
        "options": {'A': 'Only physical cables', 'B': 'Only email', 'C': 'Platform for developing and deploying applications', 'D': 'Only end-user hardware'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What does SaaS provide?',
        "options": {'A': 'Only networking', 'B': 'Only virtual machines', 'C': 'Only storage hardware', 'D': 'Software applications over the internet'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which cloud model is dedicated to one organization?',
        "options": {'A': 'Open cloud', 'B': 'Private cloud', 'C': 'Public cloud', 'D': 'Community-free cloud'},
        "answer": 'B',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which cloud model serves many customers?',
        "options": {'A': 'Local cloud', 'B': 'Offline cloud', 'C': 'Public cloud', 'D': 'Private cloud'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a hybrid cloud?',
        "options": {'A': 'Combination of private and public cloud environments', 'B': 'Only public cloud', 'C': 'No cloud', 'D': 'Only private cloud'},
        "answer": 'A',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is elasticity?',
        "options": {'A': 'Fixed capacity', 'B': 'Data encryption only', 'C': 'Manual backup', 'D': 'Ability to scale resources with demand'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is scalability?',
        "options": {'A': 'Only security', 'B': 'Only storage', 'C': 'Only billing', 'D': 'Ability to increase or decrease capacity'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is virtualization?',
        "options": {'A': 'Writing HTML', 'B': 'Deleting servers', 'C': 'Encrypting files', 'D': 'Creating virtual computing resources'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a virtual machine?',
        "options": {'A': 'Physical router', 'B': 'Web page', 'C': 'Database table', 'D': 'Software-based emulation of a computer'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is cloud storage?',
        "options": {'A': 'Remote storage accessed through a network', 'B': 'Local RAM only', 'C': 'CPU cache', 'D': 'Keyboard memory'},
        "answer": 'A',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is multi-tenancy?',
        "options": {'A': 'Multiple customers sharing a cloud platform with logical isolation', 'B': 'One user per server only', 'C': 'Offline computing', 'D': 'No users'},
        "answer": 'A',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is pay-as-you-go pricing?',
        "options": {'A': 'Paying based on resource usage', 'B': 'No payment', 'C': 'Hardware-only payment', 'D': 'Fixed lifetime payment'},
        "answer": 'A',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is serverless computing?',
        "options": {'A': 'Only local programs', 'B': 'No servers exist', 'C': 'A physical server room', 'D': 'Running code without managing servers directly'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is an availability zone?',
        "options": {'A': 'A programming language', 'B': 'A user account', 'C': 'A database table', 'D': 'Isolated location within a cloud region'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a cloud region?',
        "options": {'A': 'A software package', 'B': 'A user group', 'C': 'Geographic area containing cloud infrastructure', 'D': 'A network protocol'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is load balancing?',
        "options": {'A': 'Encrypting data', 'B': 'Backing up files', 'C': 'Deleting requests', 'D': 'Distributing workloads across resources'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is an SLA?',
        "options": {'A': 'Server Link Address', 'B': 'Storage License Access', 'C': 'Service Level Agreement', 'D': 'System Login Application'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is cloud security?',
        "options": {'A': 'Only storage', 'B': 'Only billing', 'C': 'Protection of cloud resources and data', 'D': 'Only application design'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is IAM?',
        "options": {'A': 'Internal API Manager', 'B': 'Information Access Machine', 'C': 'Internet Application Module', 'D': 'Identity and Access Management'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a container?',
        "options": {'A': 'Physical server', 'B': 'Network cable', 'C': 'Database key', 'D': 'Lightweight isolated application environment'},
        "answer": 'D',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is Kubernetes commonly used for?',
        "options": {'A': 'Container orchestration', 'B': 'Image editing', 'C': 'SQL querying', 'D': 'Word processing'},
        "answer": 'A',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a CDN?',
        "options": {'A': 'Network that delivers content from distributed locations', 'B': 'Security password', 'C': 'Cloud database only', 'D': 'CPU scheduler'},
        "answer": 'A',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is cloud migration?',
        "options": {'A': 'Deleting cloud data', 'B': 'Creating a LAN', 'C': 'Moving workloads or data to cloud environments', 'D': 'Formatting a disk'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is disaster recovery?',
        "options": {'A': 'Creating HTML', 'B': 'Increasing screen size', 'C': 'Restoring services after a major failure', 'D': 'Sorting files'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is fault tolerance?',
        "options": {'A': 'Faster typing', 'B': 'Ability to continue operating despite failures', 'C': 'Lower screen resolution', 'D': 'No backup'},
        "answer": 'B',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a cloud API?',
        "options": {'A': 'A physical cable', 'B': 'A database row', 'C': 'Interface for interacting programmatically with cloud services', 'D': 'A user password'},
        "answer": 'C',
        "topic": 'Cloud Computing',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is object storage?',
        "options": {'A': 'Only database rows', 'B': 'Storage of data as objects with metadata', 'C': 'Only RAM', 'D': 'Only CPU cache'},
        "answer": 'B',
        "topic": 'Cloud Computing',
        "difficulty": 'Medium'
    })
    # Cyber Security: 30 questions
    questions.append({
        "question": 'What is cybersecurity?',
        "options": {'A': 'Only web design', 'B': 'Only hardware repair', 'C': 'Only programming', 'D': 'Protection of systems, networks, and data'},
        "answer": 'D',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is malware?',
        "options": {'A': 'Database software', 'B': 'Malicious software', 'C': 'Backup software', 'D': 'Office software'},
        "answer": 'B',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is phishing?',
        "options": {'A': 'Fraudulent attempt to obtain sensitive information', 'B': 'Data backup', 'C': 'Software update', 'D': 'Network speed test'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a virus?',
        "options": {'A': 'Malicious program that can replicate by attaching to files or programs', 'B': 'Firewall', 'C': 'Password manager', 'D': 'Backup'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is ransomware?',
        "options": {'A': 'Firewall', 'B': 'Malware that typically blocks access and demands payment', 'C': 'Antivirus', 'D': 'Encryption standard'},
        "answer": 'B',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a firewall?',
        "options": {'A': 'A password', 'B': 'A database', 'C': 'A virus', 'D': 'System that filters network traffic'},
        "answer": 'D',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is encryption?',
        "options": {'A': 'Deleting data', 'B': 'Sorting records', 'C': 'Transforming data to protect confidentiality', 'D': 'Compressing only'},
        "answer": 'C',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is decryption?',
        "options": {'A': 'Deleting keys', 'B': 'Backing up data', 'C': 'Converting protected data back to readable form', 'D': 'Creating malware'},
        "answer": 'C',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is authentication?',
        "options": {'A': 'Granting every permission', 'B': 'Deleting users', 'C': 'Encrypting files only', 'D': 'Verifying identity'},
        "answer": 'D',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is authorization?',
        "options": {'A': 'Determining what an authenticated user can access', 'B': 'Scanning hardware', 'C': 'Verifying identity', 'D': 'Creating a password'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is multi-factor authentication?',
        "options": {'A': 'Using one password twice', 'B': 'Using two or more authentication factors', 'C': 'No authentication', 'D': 'Sharing passwords'},
        "answer": 'B',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a strong password?',
        "options": {'A': 'Birth year only', 'B': 'Username only', 'C': 'Short common word', 'D': 'Long, unique, hard-to-guess secret'},
        "answer": 'D',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a brute-force attack?',
        "options": {'A': 'Trying many possible passwords or keys', 'B': 'Backing up data', 'C': 'Updating software', 'D': 'Sending one email'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a denial-of-service attack?',
        "options": {'A': 'Installing updates', 'B': 'Overwhelming a service to disrupt availability', 'C': 'Encrypting files', 'D': 'Stealing a password by guessing only'},
        "answer": 'B',
        "topic": 'Cyber Security',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a vulnerability?',
        "options": {'A': 'Strong password', 'B': 'Backup copy', 'C': 'Weakness that can be exploited', 'D': 'Security patch'},
        "answer": 'C',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a security patch?',
        "options": {'A': 'Update that fixes vulnerabilities or bugs', 'B': 'A password', 'C': 'A virus', 'D': 'A firewall rule only'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is social engineering?',
        "options": {'A': 'Manipulating people to reveal information or take actions', 'B': 'Updating software', 'C': 'Encrypting a disk', 'D': 'Scanning ports only'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is spyware?',
        "options": {'A': 'Compiler', 'B': 'Backup tool', 'C': 'Software that secretly monitors or collects information', 'D': 'Firewall'},
        "answer": 'C',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a botnet?',
        "options": {'A': 'Password list', 'B': 'Secure network', 'C': 'Backup server', 'D': 'Network of compromised devices controlled together'},
        "answer": 'D',
        "topic": 'Cyber Security',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a Trojan?',
        "options": {'A': 'Firewall', 'B': 'Network switch', 'C': 'Encryption key', 'D': 'Malware disguised as legitimate software'},
        "answer": 'D',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a security audit?',
        "options": {'A': 'Systematic review of security controls and practices', 'B': 'Data deletion', 'C': 'Network cabling', 'D': 'Software installation'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is confidentiality?',
        "options": {'A': 'Preventing unauthorized disclosure of information', 'B': 'Deleting data', 'C': 'Ensuring speed', 'D': 'Ensuring data is always available'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is integrity?',
        "options": {'A': 'Reducing storage', 'B': 'Keeping systems online only', 'C': 'Hiding usernames', 'D': 'Preventing unauthorized alteration of data'},
        "answer": 'D',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is availability?',
        "options": {'A': 'Ensuring authorized users can access systems when needed', 'B': 'Deleting logs', 'C': 'Changing passwords', 'D': 'Encrypting every file'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is the CIA triad?',
        "options": {'A': 'Confidentiality, Integrity, Availability', 'B': 'Control, Internet, Access', 'C': 'Code, Integrity, Access', 'D': 'Confidentiality, Internet, Authentication'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is a VPN?',
        "options": {'A': 'Encrypted or protected connection over a network', 'B': 'A password', 'C': 'A virus scanner', 'D': 'A database'},
        "answer": 'A',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a digital signature used for?',
        "options": {'A': 'Increasing storage', 'B': 'Deleting malware', 'C': 'Compressing files', 'D': 'Authenticity and integrity of digital data'},
        "answer": 'D',
        "topic": 'Cyber Security',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'What is antivirus software?',
        "options": {'A': 'A database', 'B': 'A router', 'C': 'Software that detects or blocks malicious software', 'D': 'A web browser'},
        "answer": 'C',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is a security log?',
        "options": {'A': 'A network cable', 'B': 'Password itself', 'C': 'Record of system or security events', 'D': 'A virus'},
        "answer": 'C',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Why are software updates important for security?',
        "options": {'A': 'They always increase storage', 'B': 'They remove all passwords', 'C': 'They can fix known vulnerabilities', 'D': 'They disable encryption'},
        "answer": 'C',
        "topic": 'Cyber Security',
        "difficulty": 'Easy'
    })
    # General Knowledge: 30 questions
    questions.append({
        "question": 'What is the capital of India?',
        "options": {'A': 'Hyderabad', 'B': 'New Delhi', 'C': 'Mumbai', 'D': 'Chennai'},
        "answer": 'B',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which planet is called the Red Planet?',
        "options": {'A': 'Earth', 'B': 'Venus', 'C': 'Mars', 'D': 'Jupiter'},
        "answer": 'C',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'How many continents are there?',
        "options": {'A': '7', 'B': '6', 'C': '5', 'D': '8'},
        "answer": 'A',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is the largest ocean?',
        "options": {'A': 'Pacific Ocean', 'B': 'Arctic Ocean', 'C': 'Atlantic Ocean', 'D': 'Indian Ocean'},
        "answer": 'A',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which gas is needed for human respiration?',
        "options": {'A': 'Hydrogen', 'B': 'Nitrogen', 'C': 'Carbon Dioxide', 'D': 'Oxygen'},
        "answer": 'D',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Who wrote the Indian national anthem?',
        "options": {'A': 'Subhas Chandra Bose', 'B': 'Bankim Chandra Chatterjee', 'C': 'Sarojini Naidu', 'D': 'Rabindranath Tagore'},
        "answer": 'D',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is the largest planet in the Solar System?',
        "options": {'A': 'Neptune', 'B': 'Saturn', 'C': 'Jupiter', 'D': 'Earth'},
        "answer": 'C',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is the smallest prime number?',
        "options": {'A': '0', 'B': '1', 'C': '2', 'D': '3'},
        "answer": 'C',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'How many days are in a leap year?',
        "options": {'A': '366', 'B': '367', 'C': '364', 'D': '365'},
        "answer": 'A',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which organ pumps blood through the body?',
        "options": {'A': 'Kidney', 'B': 'Liver', 'C': 'Heart', 'D': 'Lungs'},
        "answer": 'C',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is the longest river in India?',
        "options": {'A': 'Ganga', 'B': 'Yamuna', 'C': 'Narmada', 'D': 'Godavari'},
        "answer": 'A',
        "topic": 'General Knowledge',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which country is known as the Land of the Rising Sun?',
        "options": {'A': 'Japan', 'B': 'China', 'C': 'Thailand', 'D': 'Korea'},
        "answer": 'A',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is the currency of Japan?',
        "options": {'A': 'Rupee', 'B': 'Yen', 'C': 'Dollar', 'D': 'Won'},
        "answer": 'B',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is the highest mountain above sea level?',
        "options": {'A': 'Makalu', 'B': 'Kangchenjunga', 'C': 'Mount Everest', 'D': 'K2'},
        "answer": 'C',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'How many players are on a cricket team?',
        "options": {'A': '11', 'B': '12', 'C': '9', 'D': '10'},
        "answer": 'A',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which vitamin is commonly produced in skin through sunlight?',
        "options": {'A': 'Vitamin B12', 'B': 'Vitamin D', 'C': 'Vitamin C', 'D': 'Vitamin K'},
        "answer": 'B',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which metal is liquid at room temperature?',
        "options": {'A': 'Copper', 'B': 'Mercury', 'C': 'Aluminium', 'D': 'Iron'},
        "answer": 'B',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is the largest mammal?',
        "options": {'A': 'Hippopotamus', 'B': 'Giraffe', 'C': 'Elephant', 'D': 'Blue whale'},
        "answer": 'D',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which instrument measures temperature?',
        "options": {'A': 'Barometer', 'B': 'Altimeter', 'C': 'Thermometer', 'D': 'Hygrometer'},
        "answer": 'C',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which instrument measures atmospheric pressure?',
        "options": {'A': 'Ammeter', 'B': 'Thermometer', 'C': 'Barometer', 'D': 'Speedometer'},
        "answer": 'C',
        "topic": 'General Knowledge',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'How many fundamental rights are currently guaranteed in the Indian Constitution?',
        "options": {'A': 'Seven', 'B': 'Six', 'C': 'Five', 'D': 'Eight'},
        "answer": 'B',
        "topic": 'General Knowledge',
        "difficulty": 'Medium'
    })
    questions.append({
        "question": 'Which Indian city is known as the City of Pearls?',
        "options": {'A': 'Jaipur', 'B': 'Kolkata', 'C': 'Pune', 'D': 'Hyderabad'},
        "answer": 'D',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which festival is known as the festival of lights?',
        "options": {'A': 'Eid', 'B': 'Holi', 'C': 'Pongal', 'D': 'Diwali'},
        "answer": 'D',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is the national animal of India?',
        "options": {'A': 'Elephant', 'B': 'Bengal tiger', 'C': 'Lion', 'D': 'Peacock'},
        "answer": 'B',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which is the national bird of India?',
        "options": {'A': 'Sparrow', 'B': 'Parrot', 'C': 'Eagle', 'D': 'Indian peacock'},
        "answer": 'D',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which ocean lies south of India?',
        "options": {'A': 'Arctic Ocean', 'B': 'Indian Ocean', 'C': 'Pacific Ocean', 'D': 'Atlantic Ocean'},
        "answer": 'B',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'What is H2O commonly known as?',
        "options": {'A': 'Salt', 'B': 'Hydrogen', 'C': 'Water', 'D': 'Oxygen'},
        "answer": 'C',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which planet is closest to the Sun?',
        "options": {'A': 'Earth', 'B': 'Mercury', 'C': 'Venus', 'D': 'Mars'},
        "answer": 'B',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'How many hours are in a day?',
        "options": {'A': '36', 'B': '12', 'C': '48', 'D': '24'},
        "answer": 'D',
        "topic": 'General Knowledge',
        "difficulty": 'Easy'
    })
    questions.append({
        "question": 'Which language has the most native speakers in India?',
        "options": {'A': 'Tamil', 'B': 'Telugu', 'C': 'Bengali', 'D': 'Hindi'},
        "answer": 'D',
        "topic": 'General Knowledge',
        "difficulty": 'Medium'
    })
    return questions


DEFAULT_QUESTIONS = build_default_questions()


# ============================================================
# FILE FUNCTIONS
# ============================================================

def load_json(filename, default):
    """Load JSON data from file."""
    if not os.path.exists(filename):
        save_json(filename, default)
        return default

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        save_json(filename, default)
        return default


def save_json(filename, data):
    """Save data to JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def initialize_files():
    """Create required files and upgrade the question bank when needed."""
    if not os.path.exists(USERS_FILE):
        save_json(USERS_FILE, [])

    # Keep existing questions, but add the new default questions that are missing.
    # This upgrades an older questions.json without deleting admin-added questions.
    if not os.path.exists(QUESTIONS_FILE):
        save_json(QUESTIONS_FILE, DEFAULT_QUESTIONS)
    else:
        existing = load_json(QUESTIONS_FILE, [])
        existing_text = {q.get("question", "") for q in existing}
        added = 0
        for question in DEFAULT_QUESTIONS:
            if question["question"] not in existing_text:
                existing.append(question)
                existing_text.add(question["question"])
                added += 1
        if added:
            save_json(QUESTIONS_FILE, existing)

    if not os.path.exists(RESULTS_FILE):
        save_json(RESULTS_FILE, [])


# ============================================================
# MAIN APPLICATION
# ============================================================

class QuizApplication:

    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("1180x760")
        self.root.minsize(1000, 650)

        self.current_user = None

        self.quiz_questions = []
        self.current_question_index = 0
        self.selected_answer = tk.StringVar()
        self.quiz_score = 0
        self.quiz_topic = ""
        self.quiz_difficulty = ""

        initialize_files()

        self.setup_style()
        self.show_home()


    # ========================================================
    # STYLE
    # ========================================================

    def setup_style(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            font=("Arial", 28, "bold")
        )

        style.configure(
            "Heading.TLabel",
            font=("Arial", 20, "bold")
        )

        style.configure(
            "Normal.TLabel",
            font=("Arial", 12)
        )

        style.configure(
            "Action.TButton",
            font=("Arial", 12, "bold"),
            padding=10
        )

        style.configure(
            "Treeview",
            font=("Arial", 10),
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        # Modern admin styles
        style.configure(
            "Admin.TButton",
            font=("Arial", 11, "bold"),
            padding=(12, 9),
            background="#4F46E5",
            foreground="white"
        )
        style.map(
            "Admin.TButton",
            background=[("active", "#3730A3")]
        )

        style.configure(
            "Danger.TButton",
            font=("Arial", 11, "bold"),
            padding=(12, 9),
            background="#DC2626",
            foreground="white"
        )
        style.map(
            "Danger.TButton",
            background=[("active", "#B91C1C")]
        )

        style.configure(
            "Admin.Treeview",
            font=("Arial", 10),
            rowheight=34,
            background="#FFFFFF",
            fieldbackground="#FFFFFF",
            foreground="#1E293B"
        )
        style.configure(
            "Admin.Treeview.Heading",
            font=("Arial", 10, "bold"),
            background="#EEF2FF",
            foreground="#1E293B",
            padding=8
        )


    # ========================================================
    # GENERAL GUI FUNCTIONS
    # ========================================================

    def clear_window(self):
        """Remove everything from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()


    def create_header(self, title):
        """Create page heading."""
        frame = ttk.Frame(self.root)
        frame.pack(fill="x", padx=30, pady=20)

        ttk.Label(
            frame,
            text=title,
            style="Title.TLabel"
        ).pack()

        return frame


    # ========================================================
    # HOME PAGE
    # ========================================================

    def show_home(self):
        self.clear_window()

        container = ttk.Frame(self.root)
        container.pack(expand=True)

        ttk.Label(
            container,
            text="QUIZ APPLICATION",
            style="Title.TLabel"
        ).pack(pady=30)

        ttk.Label(
            container,
            text="Test your knowledge and track your performance",
            style="Normal.TLabel"
        ).pack(pady=10)

        ttk.Button(
            container,
            text="User Login",
            style="Action.TButton",
            command=self.show_user_login
        ).pack(fill="x", pady=8)

        ttk.Button(
            container,
            text="Register",
            style="Action.TButton",
            command=self.show_register
        ).pack(fill="x", pady=8)

        ttk.Button(
            container,
            text="Admin Login",
            style="Action.TButton",
            command=self.show_admin_login
        ).pack(fill="x", pady=8)

        ttk.Button(
            container,
            text="Exit",
            style="Action.TButton",
            command=self.root.destroy
        ).pack(fill="x", pady=8)


    # ========================================================
    # USER REGISTRATION
    # ========================================================

    def show_register(self):
        self.clear_window()

        self.create_header("User Registration")

        form = ttk.Frame(self.root)
        form.pack(pady=20)

        ttk.Label(
            form,
            text="Username:",
            style="Normal.TLabel"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="e")

        username_entry = ttk.Entry(form, width=35)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(
            form,
            text="Password:",
            style="Normal.TLabel"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="e")

        password_entry = ttk.Entry(form, width=35, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(
            form,
            text="Confirm Password:",
            style="Normal.TLabel"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="e")

        confirm_entry = ttk.Entry(form, width=35, show="*")
        confirm_entry.grid(row=2, column=1, padx=10, pady=10)

        def register():
            username = username_entry.get().strip()
            password = password_entry.get()
            confirm = confirm_entry.get()

            if not username or not password or not confirm:
                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )
                return

            if len(username) < 3:
                messagebox.showerror(
                    "Error",
                    "Username must contain at least 3 characters."
                )
                return

            if len(password) < 4:
                messagebox.showerror(
                    "Error",
                    "Password must contain at least 4 characters."
                )
                return

            if password != confirm:
                messagebox.showerror(
                    "Error",
                    "Passwords do not match."
                )
                return

            users = load_json(USERS_FILE, [])

            for user in users:
                if user["username"].lower() == username.lower():
                    messagebox.showerror(
                        "Error",
                        "Username already exists."
                    )
                    return

            users.append({
                "username": username,
                "password": password
            })

            save_json(USERS_FILE, users)

            messagebox.showinfo(
                "Success",
                "Registration successful!"
            )

            self.show_user_login()

        ttk.Button(
            form,
            text="Register",
            style="Action.TButton",
            command=register
        ).grid(row=3, column=0, columnspan=2, pady=20)

        ttk.Button(
            form,
            text="Back",
            command=self.show_home
        ).grid(row=4, column=0, columnspan=2, pady=5)


    # ========================================================
    # USER LOGIN
    # ========================================================

    def show_user_login(self):
        self.clear_window()

        self.create_header("User Login")

        form = ttk.Frame(self.root)
        form.pack(pady=30)

        ttk.Label(
            form,
            text="Username:",
            style="Normal.TLabel"
        ).grid(row=0, column=0, padx=10, pady=10)

        username_entry = ttk.Entry(form, width=35)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(
            form,
            text="Password:",
            style="Normal.TLabel"
        ).grid(row=1, column=0, padx=10, pady=10)

        password_entry = ttk.Entry(
            form,
            width=35,
            show="*"
        )
        password_entry.grid(row=1, column=1, padx=10, pady=10)

        def login():
            username = username_entry.get().strip()
            password = password_entry.get()

            users = load_json(USERS_FILE, [])

            for user in users:
                if (
                    user["username"] == username
                    and user["password"] == password
                ):
                    self.current_user = username
                    self.show_user_dashboard()
                    return

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

        ttk.Button(
            form,
            text="Login",
            style="Action.TButton",
            command=login
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=20
        )

        ttk.Button(
            form,
            text="Create Account",
            command=self.show_register
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=5
        )

        ttk.Button(
            form,
            text="Back",
            command=self.show_home
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=5
        )


    # ========================================================
    # USER DASHBOARD
    # ========================================================

    def show_user_dashboard(self):
        self.clear_window()

        self.create_header(
            f"Welcome, {self.current_user}"
        )

        container = ttk.Frame(self.root)
        container.pack(expand=True)

        ttk.Label(
            container,
            text="User Dashboard",
            style="Heading.TLabel"
        ).pack(pady=20)

        ttk.Button(
            container,
            text="Start Quiz",
            style="Action.TButton",
            command=self.show_quiz_setup
        ).pack(fill="x", pady=10)

        ttk.Button(
            container,
            text="My Quiz History",
            style="Action.TButton",
            command=self.show_user_history
        ).pack(fill="x", pady=10)

        ttk.Button(
            container,
            text="Logout",
            style="Action.TButton",
            command=self.logout
        ).pack(fill="x", pady=10)


    # ========================================================
    # QUIZ SETUP
    # ========================================================

    def show_quiz_setup(self):
        self.clear_window()

        self.create_header("Quiz Setup")

        questions = load_json(QUESTIONS_FILE, [])

        topics = sorted(
            list(set(q["topic"] for q in questions))
        )

        form = ttk.Frame(self.root)
        form.pack(pady=30)

        ttk.Label(
            form,
            text="Select Topic:",
            style="Normal.TLabel"
        ).grid(row=0, column=0, padx=10, pady=15)

        topic_var = tk.StringVar()

        topic_combo = ttk.Combobox(
            form,
            textvariable=topic_var,
            values=topics,
            state="readonly",
            width=30
        )
        topic_combo.grid(row=0, column=1, padx=10, pady=15)

        if topics:
            topic_combo.current(0)

        ttk.Label(
            form,
            text="Difficulty:",
            style="Normal.TLabel"
        ).grid(row=1, column=0, padx=10, pady=15)

        difficulty_var = tk.StringVar(value="All")

        difficulty_combo = ttk.Combobox(
            form,
            textvariable=difficulty_var,
            values=["All", "Easy", "Medium", "Hard"],
            state="readonly",
            width=30
        )
        difficulty_combo.grid(
            row=1,
            column=1,
            padx=10,
            pady=15
        )

        ttk.Label(
            form,
            text="Number of Questions:",
            style="Normal.TLabel"
        ).grid(row=2, column=0, padx=10, pady=15)

        number_var = tk.IntVar(value=5)

        number_spin = tk.Spinbox(
            form,
            from_=1,
            to=50,
            textvariable=number_var,
            width=10
        )
        number_spin.grid(
            row=2,
            column=1,
            padx=10,
            pady=15,
            sticky="w"
        )

        def start_quiz():
            topic = topic_var.get()
            difficulty = difficulty_var.get()

            try:
                number = int(number_var.get())
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Enter a valid number of questions."
                )
                return

            if number <= 0:
                messagebox.showerror(
                    "Error",
                    "Number of questions must be greater than 0."
                )
                return

            if difficulty == "All":
                filtered = [
                    q for q in questions
                    if q["topic"] == topic
                ]
            else:
                filtered = [
                    q for q in questions
                    if q["topic"] == topic
                    and q["difficulty"] == difficulty
                ]

            if not filtered:
                messagebox.showwarning(
                    "No Questions",
                    "No questions available for this topic "
                    "and difficulty."
                )
                return

            if number > len(filtered):
                number = len(filtered)

                messagebox.showinfo(
                    "Information",
                    f"Only {len(filtered)} questions are "
                    f"available. The quiz will contain "
                    f"{len(filtered)} questions."
                )

            self.quiz_questions = random.sample(
                filtered,
                number
            )

            self.quiz_topic = topic
            self.quiz_difficulty = difficulty
            self.current_question_index = 0
            self.quiz_score = 0

            self.show_question()

        ttk.Button(
            form,
            text="Start Quiz",
            style="Action.TButton",
            command=start_quiz
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=25
        )

        ttk.Button(
            form,
            text="Back",
            command=self.show_user_dashboard
        ).grid(
            row=4,
            column=0,
            columnspan=2
        )


    # ========================================================
    # SHOW QUESTION
    # ========================================================

    def show_question(self):
        self.clear_window()

        question = self.quiz_questions[
            self.current_question_index
        ]

        total = len(self.quiz_questions)
        current = self.current_question_index + 1

        self.create_header(
            f"Question {current} of {total}"
        )

        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill="x", padx=50)

        ttk.Label(
            top_frame,
            text=f"Topic: {self.quiz_topic}    "
                 f"Difficulty: {self.quiz_difficulty}",
            style="Normal.TLabel"
        ).pack()

        question_frame = ttk.Frame(self.root)
        question_frame.pack(
            fill="both",
            expand=True,
            padx=70,
            pady=30
        )

        ttk.Label(
            question_frame,
            text=question["question"],
            font=("Arial", 18, "bold"),
            wraplength=800,
            justify="left"
        ).pack(anchor="w", pady=20)

        self.selected_answer = tk.StringVar(value="")

        for key in ["A", "B", "C", "D"]:
            ttk.Radiobutton(
                question_frame,
                text=f"{key}. {question['options'][key]}",
                variable=self.selected_answer,
                value=key
            ).pack(
                anchor="w",
                pady=10
            )

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        def next_question():
            answer = self.selected_answer.get()

            if not answer:
                messagebox.showwarning(
                    "Select Answer",
                    "Please select an answer."
                )
                return

            if answer == question["answer"]:
                self.quiz_score += 1

            if self.current_question_index + 1 < total:
                self.current_question_index += 1
                self.show_question()
            else:
                self.finish_quiz()

        button_text = (
            "Finish Quiz"
            if current == total
            else "Next Question"
        )

        ttk.Button(
            button_frame,
            text=button_text,
            style="Action.TButton",
            command=next_question
        ).pack(side="left", padx=10)

        ttk.Button(
            button_frame,
            text="Cancel Quiz",
            command=self.cancel_quiz
        ).pack(side="left", padx=10)


    # ========================================================
    # FINISH QUIZ
    # ========================================================

    def finish_quiz(self):
        total = len(self.quiz_questions)
        correct = self.quiz_score
        wrong = total - correct

        percentage = (correct / total) * 100

        if percentage >= 80:
            performance = "Excellent"
        elif percentage >= 60:
            performance = "Good"
        elif percentage >= 40:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        results = load_json(RESULTS_FILE, [])

        result = {
            "username": self.current_user,
            "topic": self.quiz_topic,
            "difficulty": self.quiz_difficulty,
            "total_questions": total,
            "correct_answers": correct,
            "wrong_answers": wrong,
            "score": correct,
            "percentage": round(percentage, 2),
            "performance": performance,
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        results.append(result)

        save_json(RESULTS_FILE, results)

        self.show_result(
            total,
            correct,
            wrong,
            percentage,
            performance
        )


    # ========================================================
    # RESULT PAGE
    # ========================================================

    def show_result(
        self,
        total,
        correct,
        wrong,
        percentage,
        performance
    ):
        self.clear_window()

        self.create_header("Quiz Result")

        frame = ttk.Frame(self.root)
        frame.pack(expand=True)

        ttk.Label(
            frame,
            text=f"Congratulations, {self.current_user}!",
            style="Heading.TLabel"
        ).pack(pady=15)

        ttk.Label(
            frame,
            text=f"Topic: {self.quiz_topic}",
            style="Normal.TLabel"
        ).pack(pady=5)

        ttk.Label(
            frame,
            text=f"Difficulty: {self.quiz_difficulty}",
            style="Normal.TLabel"
        ).pack(pady=5)

        ttk.Label(
            frame,
            text=f"Total Questions: {total}",
            style="Normal.TLabel"
        ).pack(pady=5)

        ttk.Label(
            frame,
            text=f"Correct Answers: {correct}",
            style="Normal.TLabel"
        ).pack(pady=5)

        ttk.Label(
            frame,
            text=f"Wrong Answers: {wrong}",
            style="Normal.TLabel"
        ).pack(pady=5)

        ttk.Label(
            frame,
            text=f"Score: {correct}/{total}",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ttk.Label(
            frame,
            text=f"Percentage: {percentage:.2f}%",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ttk.Label(
            frame,
            text=f"Performance: {performance}",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        ttk.Button(
            frame,
            text="Take Another Quiz",
            style="Action.TButton",
            command=self.show_quiz_setup
        ).pack(fill="x", pady=10)

        ttk.Button(
            frame,
            text="View My History",
            style="Action.TButton",
            command=self.show_user_history
        ).pack(fill="x", pady=10)

        ttk.Button(
            frame,
            text="Dashboard",
            style="Action.TButton",
            command=self.show_user_dashboard
        ).pack(fill="x", pady=10)


    # ========================================================
    # CANCEL QUIZ
    # ========================================================

    def cancel_quiz(self):
        answer = messagebox.askyesno(
            "Cancel Quiz",
            "Are you sure you want to cancel this quiz?"
        )

        if answer:
            self.show_user_dashboard()


    # ========================================================
    # USER HISTORY
    # ========================================================

    def show_user_history(self):
        self.clear_window()

        self.create_header("My Quiz History")

        results = load_json(RESULTS_FILE, [])

        user_results = [
            r for r in results
            if r["username"] == self.current_user
        ]

        if not user_results:
            ttk.Label(
                self.root,
                text="No quiz attempts found.",
                style="Normal.TLabel"
            ).pack(pady=30)

            ttk.Button(
                self.root,
                text="Back",
                command=self.show_user_dashboard
            ).pack()

            return

        attempts = len(user_results)

        percentages = [
            r["percentage"] for r in user_results
        ]

        best = max(percentages)
        average = sum(percentages) / len(percentages)

        summary = ttk.Frame(self.root)
        summary.pack(fill="x", padx=30, pady=10)

        ttk.Label(
            summary,
            text=f"Total Attempts: {attempts}",
            style="Normal.TLabel"
        ).pack(side="left", padx=20)

        ttk.Label(
            summary,
            text=f"Best Percentage: {best:.2f}%",
            style="Normal.TLabel"
        ).pack(side="left", padx=20)

        ttk.Label(
            summary,
            text=f"Average Percentage: {average:.2f}%",
            style="Normal.TLabel"
        ).pack(side="left", padx=20)

        tree_frame = ttk.Frame(self.root)
        tree_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        columns = (
            "attempt",
            "topic",
            "difficulty",
            "score",
            "percentage",
            "performance",
            "date"
        )

        tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "attempt": "Attempt",
            "topic": "Topic",
            "difficulty": "Difficulty",
            "score": "Score",
            "percentage": "Percentage",
            "performance": "Performance",
            "date": "Date"
        }

        for column in columns:
            tree.heading(
                column,
                text=headings[column]
            )
            tree.column(
                column,
                width=120,
                anchor="center"
            )

        for index, result in enumerate(user_results, 1):
            tree.insert(
                "",
                "end",
                values=(
                    index,
                    result["topic"],
                    result["difficulty"],
                    f"{result['score']}/"
                    f"{result['total_questions']}",
                    f"{result['percentage']:.2f}%",
                    result["performance"],
                    result["date"]
                )
            )

        scrollbar = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        ttk.Button(
            self.root,
            text="Back",
            command=self.show_user_dashboard
        ).pack(pady=15)


    # ========================================================
    # ADMIN LOGIN
    # ========================================================

    def show_admin_login(self):
        self.clear_window()

        self.create_header("Admin Login")

        form = ttk.Frame(self.root)
        form.pack(pady=30)

        ttk.Label(
            form,
            text="Admin Username:",
            style="Normal.TLabel"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        username_entry = ttk.Entry(
            form,
            width=35
        )
        username_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            form,
            text="Admin Password:",
            style="Normal.TLabel"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        password_entry = ttk.Entry(
            form,
            width=35,
            show="*"
        )
        password_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            form,
            text="Default: admin / admin123"
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10
        )

        def login():
            username = username_entry.get().strip()
            password = password_entry.get()

            if (
                username == ADMIN_USERNAME
                and password == ADMIN_PASSWORD
            ):
                self.show_admin_dashboard()
            else:
                messagebox.showerror(
                    "Login Failed",
                    "Invalid admin username or password."
                )

        ttk.Button(
            form,
            text="Login",
            style="Action.TButton",
            command=login
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20
        )

        ttk.Button(
            form,
            text="Back",
            command=self.show_home
        ).grid(
            row=4,
            column=0,
            columnspan=2
        )


    # ========================================================
    # ADMIN LAYOUT / HELPERS
    # ========================================================

    def create_admin_layout(self, title, subtitle=""):
        """Create the reusable modern admin dashboard layout."""
        self.clear_window()

        # Sidebar
        sidebar = tk.Frame(
            self.root,
            bg="#111827",
            width=235
        )
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="QUIZ MASTER",
            font=("Arial", 20, "bold"),
            bg="#111827",
            fg="white"
        ).pack(pady=(28, 3))

        tk.Label(
            sidebar,
            text="ADMIN PANEL",
            font=("Arial", 9, "bold"),
            bg="#111827",
            fg="#A5B4FC"
        ).pack(pady=(0, 28))

        self._admin_nav_button(sidebar, "Dashboard", self.show_admin_dashboard)
        self._admin_nav_button(sidebar, "Users", self.admin_view_users)
        self._admin_nav_button(sidebar, "Quiz Attempts", self.admin_view_attempts)
        self._admin_nav_button(sidebar, "Performance", self.admin_user_performance)
        self._admin_nav_button(sidebar, "Question Bank", self.admin_question_bank)

        tk.Frame(sidebar, bg="#111827").pack(fill="both", expand=True)

        logout = tk.Button(
            sidebar,
            text="Logout",
            command=self.logout,
            font=("Arial", 11, "bold"),
            bg="#7F1D1D",
            fg="white",
            activebackground="#991B1B",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=10
        )
        logout.pack(fill="x", padx=18, pady=20)

        # Main content
        main = tk.Frame(self.root, bg="#F5F7FB")
        main.pack(side="right", fill="both", expand=True)

        topbar = tk.Frame(main, bg="white", height=82)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)

        tk.Label(
            topbar,
            text=title,
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#1E293B"
        ).pack(side="left", padx=28, pady=(17, 0))

        tk.Label(
            topbar,
            text="Administrator",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#64748B"
        ).pack(side="right", padx=28, pady=24)

        if subtitle:
            tk.Label(
                main,
                text=subtitle,
                font=("Arial", 10),
                bg="#F5F7FB",
                fg="#64748B",
                anchor="w"
            ).pack(fill="x", padx=28, pady=(16, 2))

        content = tk.Frame(main, bg="#F5F7FB")
        content.pack(fill="both", expand=True, padx=28, pady=(8, 25))
        return content


    def _admin_nav_button(self, parent, text, command):
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 11, "bold"),
            bg="#111827",
            fg="#E5E7EB",
            activebackground="#312E81",
            activeforeground="white",
            relief="flat",
            bd=0,
            anchor="w",
            padx=24,
            pady=12,
            cursor="hand2"
        )
        button.pack(fill="x", padx=10, pady=3)
        return button


    def _admin_card(self, parent, title, value, accent):
        card = tk.Frame(
            parent,
            bg="white",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )
        card.pack(side="left", fill="both", expand=True, padx=6)

        tk.Frame(card, bg=accent, width=5).pack(side="left", fill="y")

        body = tk.Frame(card, bg="white")
        body.pack(fill="both", expand=True, padx=14, pady=12)

        tk.Label(
            body,
            text=title,
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#64748B"
        ).pack(anchor="w")

        tk.Label(
            body,
            text=str(value),
            font=("Arial", 23, "bold"),
            bg="white",
            fg="#1E293B"
        ).pack(anchor="w", pady=(4, 0))

        return card


    def _make_admin_tree(self, parent, columns, headings, widths=None):
        frame = tk.Frame(parent, bg="white")
        frame.pack(fill="both", expand=True)

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            style="Admin.Treeview"
        )

        for i, column in enumerate(columns):
            tree.heading(column, text=headings[column])
            width = widths[i] if widths else 130
            tree.column(column, width=width, anchor="center")

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=tree.yview
        )
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        return tree


    # ========================================================
    # ADMIN DASHBOARD
    # ========================================================

    def show_admin_dashboard(self):
        content = self.create_admin_layout(
            "Admin Dashboard",
            "Monitor users, quizzes, performance and question content."
        )

        users = load_json(USERS_FILE, [])
        questions = load_json(QUESTIONS_FILE, [])
        results = load_json(RESULTS_FILE, [])

        average = (
            sum(float(r.get("percentage", 0)) for r in results) / len(results)
            if results else 0
        )

        cards = tk.Frame(content, bg="#F5F7FB")
        cards.pack(fill="x", pady=(5, 18))

        self._admin_card(cards, "Total Users", len(users), "#4F46E5")
        self._admin_card(cards, "Total Questions", len(questions), "#0891B2")
        self._admin_card(cards, "Quiz Attempts", len(results), "#16A34A")
        self._admin_card(cards, "Average Score", f"{average:.1f}%", "#F59E0B")

        lower = tk.Frame(content, bg="#F5F7FB")
        lower.pack(fill="both", expand=True)

        recent_box = tk.Frame(
            lower,
            bg="white",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )
        recent_box.pack(side="left", fill="both", expand=True, padx=(0, 8))

        tk.Label(
            recent_box,
            text="Recent Quiz Attempts",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#1E293B"
        ).pack(anchor="w", padx=18, pady=15)

        recent_tree = self._make_admin_tree(
            recent_box,
            ("username", "topic", "score", "percentage", "date"),
            {
                "username": "User",
                "topic": "Topic",
                "score": "Score",
                "percentage": "%",
                "date": "Date"
            },
            [130, 145, 85, 80, 155]
        )

        for result in list(reversed(results))[:8]:
            recent_tree.insert(
                "", "end",
                values=(
                    result.get("username", ""),
                    result.get("topic", ""),
                    f"{result.get('score', 0)}/{result.get('total_questions', 0)}",
                    f"{float(result.get('percentage', 0)):.1f}%",
                    result.get("date", "")
                )
            )

        quick_box = tk.Frame(
            lower,
            bg="white",
            width=270,
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )
        quick_box.pack(side="right", fill="y", padx=(8, 0))
        quick_box.pack_propagate(False)

        tk.Label(
            quick_box,
            text="Quick Actions",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#1E293B"
        ).pack(anchor="w", padx=18, pady=(18, 12))

        for text, command in [
            ("Manage Users", self.admin_view_users),
            ("View Attempts", self.admin_view_attempts),
            ("Check Performance", self.admin_user_performance),
            ("Manage Questions", self.admin_question_bank)
        ]:
            ttk.Button(
                quick_box,
                text=text,
                style="Admin.TButton",
                command=command
            ).pack(fill="x", padx=18, pady=6)


    # ========================================================
    # ADMIN - VIEW USERS
    # ========================================================

    def admin_view_users(self):
        content = self.create_admin_layout(
            "Registered Users",
            "Search users and view their quiz activity."
        )

        users = load_json(USERS_FILE, [])
        results = load_json(RESULTS_FILE, [])

        toolbar = tk.Frame(content, bg="#F5F7FB")
        toolbar.pack(fill="x", pady=(0, 12))

        tk.Label(
            toolbar, text="Search:", font=("Arial", 10, "bold"),
            bg="#F5F7FB", fg="#1E293B"
        ).pack(side="left", padx=(0, 8))

        search_var = tk.StringVar()
        search = ttk.Entry(toolbar, textvariable=search_var, width=35)
        search.pack(side="left")

        tree = self._make_admin_tree(
            content,
            ("username", "attempts", "best", "average", "last_quiz"),
            {
                "username": "Username",
                "attempts": "Attempts",
                "best": "Best %",
                "average": "Average %",
                "last_quiz": "Last Quiz"
            },
            [180, 110, 110, 120, 190]
        )

        def refresh(*args):
            for item in tree.get_children():
                tree.delete(item)

            query = search_var.get().strip().lower()
            for user in users:
                username = user.get("username", "")
                if query and query not in username.lower():
                    continue

                user_results = [
                    r for r in results
                    if r.get("username") == username
                ]
                percentages = [float(r.get("percentage", 0)) for r in user_results]
                attempts = len(user_results)
                best = max(percentages) if percentages else 0
                avg = sum(percentages) / attempts if attempts else 0
                last = user_results[-1].get("date", "No attempts") if user_results else "No attempts"

                tree.insert(
                    "", "end",
                    values=(username, attempts, f"{best:.1f}%", f"{avg:.1f}%", last)
                )

        search_var.trace_add("write", refresh)
        refresh()


    # ========================================================
    # ADMIN - VIEW ALL ATTEMPTS
    # ========================================================

    def admin_view_attempts(self):
        content = self.create_admin_layout(
            "Quiz Attempts",
            "Review every completed quiz attempt."
        )

        results = load_json(RESULTS_FILE, [])

        toolbar = tk.Frame(content, bg="#F5F7FB")
        toolbar.pack(fill="x", pady=(0, 12))

        tk.Label(
            toolbar, text="Search:", font=("Arial", 10, "bold"),
            bg="#F5F7FB", fg="#1E293B"
        ).pack(side="left", padx=(0, 8))

        search_var = tk.StringVar()
        ttk.Entry(toolbar, textvariable=search_var, width=35).pack(side="left")

        tree = self._make_admin_tree(
            content,
            ("username", "topic", "difficulty", "score", "percentage", "performance", "date"),
            {
                "username": "Username",
                "topic": "Topic",
                "difficulty": "Difficulty",
                "score": "Score",
                "percentage": "Percentage",
                "performance": "Performance",
                "date": "Date"
            },
            [120, 135, 100, 80, 100, 145, 175]
        )

        def refresh(*args):
            for item in tree.get_children():
                tree.delete(item)

            query = search_var.get().strip().lower()
            for result in reversed(results):
                searchable = " ".join([
                    str(result.get("username", "")),
                    str(result.get("topic", "")),
                    str(result.get("difficulty", "")),
                    str(result.get("performance", ""))
                ]).lower()
                if query and query not in searchable:
                    continue

                tree.insert(
                    "", "end",
                    values=(
                        result.get("username", ""),
                        result.get("topic", ""),
                        result.get("difficulty", ""),
                        f"{result.get('score', 0)}/{result.get('total_questions', 0)}",
                        f"{float(result.get('percentage', 0)):.1f}%",
                        result.get("performance", ""),
                        result.get("date", "")
                    )
                )

        search_var.trace_add("write", refresh)
        refresh()


    # ========================================================
    # ADMIN - USER PERFORMANCE
    # ========================================================

    def admin_user_performance(self):
        content = self.create_admin_layout(
            "User Performance",
            "Select a user to view detailed quiz performance."
        )

        users = load_json(USERS_FILE, [])
        usernames = [user.get("username", "") for user in users]

        top = tk.Frame(content, bg="#F5F7FB")
        top.pack(fill="x", pady=(0, 14))

        tk.Label(
            top, text="Select User:", font=("Arial", 10, "bold"),
            bg="#F5F7FB", fg="#1E293B"
        ).pack(side="left", padx=(0, 8))

        username_var = tk.StringVar()
        combo = ttk.Combobox(
            top, textvariable=username_var,
            values=usernames, state="readonly", width=30
        )
        combo.pack(side="left")

        summary = tk.Frame(content, bg="#F5F7FB")
        summary.pack(fill="x", pady=(0, 14))

        attempt_value = self._admin_card(summary, "Attempts", "0", "#4F46E5")
        best_value = self._admin_card(summary, "Best Score", "0%", "#16A34A")
        avg_value = self._admin_card(summary, "Average Score", "0%", "#F59E0B")

        # Get value labels inside cards by locating the second Label.
        def card_value_label(card):
            labels = [w for w in card.winfo_children() if isinstance(w, tk.Frame)]
            if labels:
                body = labels[-1]
                value_labels = [w for w in body.winfo_children() if isinstance(w, tk.Label)]
                if len(value_labels) > 1:
                    return value_labels[1]
            return None

        attempt_label = card_value_label(attempt_value)
        best_label = card_value_label(best_value)
        avg_label = card_value_label(avg_value)

        tree = self._make_admin_tree(
            content,
            ("topic", "difficulty", "score", "percentage", "performance", "date"),
            {
                "topic": "Topic",
                "difficulty": "Difficulty",
                "score": "Score",
                "percentage": "Percentage",
                "performance": "Performance",
                "date": "Date"
            },
            [150, 110, 90, 110, 160, 190]
        )

        def show_performance(event=None):
            for item in tree.get_children():
                tree.delete(item)

            username = username_var.get()
            if not username:
                return

            results = load_json(RESULTS_FILE, [])
            user_results = [r for r in results if r.get("username") == username]
            percentages = [float(r.get("percentage", 0)) for r in user_results]

            if attempt_label:
                attempt_label.config(text=str(len(user_results)))
            if best_label:
                best_label.config(text=f"{max(percentages):.1f}%" if percentages else "0%")
            if avg_label:
                avg_label.config(
                    text=f"{sum(percentages)/len(percentages):.1f}%" if percentages else "0%"
                )

            for result in reversed(user_results):
                tree.insert(
                    "", "end",
                    values=(
                        result.get("topic", ""),
                        result.get("difficulty", ""),
                        f"{result.get('score', 0)}/{result.get('total_questions', 0)}",
                        f"{float(result.get('percentage', 0)):.1f}%",
                        result.get("performance", ""),
                        result.get("date", "")
                    )
                )

        if usernames:
            combo.current(0)
            show_performance()

        combo.bind("<<ComboboxSelected>>", show_performance)


    # ========================================================
    # ADMIN - QUESTION BANK
    # ========================================================

    def admin_question_bank(self):
        content = self.create_admin_layout(
            "Question Bank",
            "Add, edit, delete and search quiz questions."
        )

        questions = load_json(QUESTIONS_FILE, [])

        toolbar = tk.Frame(content, bg="#F5F7FB")
        toolbar.pack(fill="x", pady=(0, 12))

        tk.Label(
            toolbar, text="Search:", font=("Arial", 10, "bold"),
            bg="#F5F7FB", fg="#1E293B"
        ).pack(side="left", padx=(0, 8))

        search_var = tk.StringVar()
        ttk.Entry(toolbar, textvariable=search_var, width=38).pack(side="left")

        tk.Label(
            toolbar,
            text=f"  {len(questions)} questions",
            font=("Arial", 10, "bold"),
            bg="#F5F7FB",
            fg="#64748B"
        ).pack(side="left", padx=10)

        tree = self._make_admin_tree(
            content,
            ("number", "question", "topic", "difficulty", "answer"),
            {
                "number": "No.",
                "question": "Question",
                "topic": "Topic",
                "difficulty": "Difficulty",
                "answer": "Answer"
            },
            [55, 540, 150, 110, 80]
        )

        def refresh(*args):
            for item in tree.get_children():
                tree.delete(item)

            query = search_var.get().strip().lower()
            for index, question in enumerate(questions, 1):
                searchable = " ".join([
                    str(question.get("question", "")),
                    str(question.get("topic", "")),
                    str(question.get("difficulty", ""))
                ]).lower()
                if query and query not in searchable:
                    continue

                tree.insert(
                    "", "end",
                    iid=str(index - 1),
                    values=(
                        index,
                        question.get("question", ""),
                        question.get("topic", ""),
                        question.get("difficulty", ""),
                        question.get("answer", "")
                    )
                )

        search_var.trace_add("write", refresh)
        refresh()

        button_frame = tk.Frame(content, bg="#F5F7FB")
        button_frame.pack(fill="x", pady=(14, 0))

        ttk.Button(
            button_frame,
            text="+ Add Question",
            style="Admin.TButton",
            command=lambda: self.add_question(tree)
        ).pack(side="left", padx=(0, 8))

        ttk.Button(
            button_frame,
            text="Update Question",
            style="Admin.TButton",
            command=lambda: self.update_question(tree)
        ).pack(side="left", padx=8)

        ttk.Button(
            button_frame,
            text="Delete Question",
            style="Danger.TButton",
            command=lambda: self.delete_question(tree)
        ).pack(side="left", padx=8)

    # ========================================================
    # ADD QUESTION
    # ========================================================

    def add_question(self, tree):
        self.question_editor(
            title="Add Question",
            index=None,
            tree=tree
        )


    # ========================================================
    # UPDATE QUESTION
    # ========================================================

    def update_question(self, tree):
        selection = tree.selection()

        if not selection:
            messagebox.showwarning(
                "Select Question",
                "Please select a question to update."
            )
            return

        index = int(selection[0])

        self.question_editor(
            title="Update Question",
            index=index,
            tree=tree
        )


    # ========================================================
    # QUESTION EDITOR
    # ========================================================

    def question_editor(
        self,
        title,
        index,
        tree
    ):
        questions = load_json(
            QUESTIONS_FILE,
            []
        )

        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("650x650")
        window.grab_set()

        ttk.Label(
            window,
            text=title,
            style="Heading.TLabel"
        ).pack(pady=15)

        form = ttk.Frame(window)
        form.pack(
            fill="both",
            expand=True,
            padx=30
        )

        ttk.Label(
            form,
            text="Question:"
        ).grid(
            row=0,
            column=0,
            sticky="nw",
            pady=10
        )

        question_text = tk.Text(
            form,
            height=5,
            width=60
        )
        question_text.grid(
            row=0,
            column=1,
            pady=10
        )

        option_entries = {}

        for row, key in enumerate(
            ["A", "B", "C", "D"],
            start=1
        ):
            ttk.Label(
                form,
                text=f"Option {key}:"
            ).grid(
                row=row,
                column=0,
                pady=8,
                sticky="e"
            )

            entry = ttk.Entry(
                form,
                width=55
            )
            entry.grid(
                row=row,
                column=1,
                pady=8
            )

            option_entries[key] = entry

        ttk.Label(
            form,
            text="Correct Answer:"
        ).grid(
            row=5,
            column=0,
            pady=10,
            sticky="e"
        )

        answer_var = tk.StringVar(value="A")

        answer_combo = ttk.Combobox(
            form,
            textvariable=answer_var,
            values=["A", "B", "C", "D"],
            state="readonly",
            width=10
        )

        answer_combo.grid(
            row=5,
            column=1,
            pady=10,
            sticky="w"
        )

        ttk.Label(
            form,
            text="Topic:"
        ).grid(
            row=6,
            column=0,
            pady=10,
            sticky="e"
        )

        topic_entry = ttk.Entry(
            form,
            width=55
        )

        topic_entry.grid(
            row=6,
            column=1,
            pady=10
        )

        ttk.Label(
            form,
            text="Difficulty:"
        ).grid(
            row=7,
            column=0,
            pady=10,
            sticky="e"
        )

        difficulty_var = tk.StringVar(
            value="Easy"
        )

        difficulty_combo = ttk.Combobox(
            form,
            textvariable=difficulty_var,
            values=[
                "Easy",
                "Medium",
                "Hard"
            ],
            state="readonly",
            width=15
        )

        difficulty_combo.grid(
            row=7,
            column=1,
            pady=10,
            sticky="w"
        )

        # If updating, load existing data
        if index is not None:
            question = questions[index]

            question_text.insert(
                "1.0",
                question["question"]
            )

            for key in ["A", "B", "C", "D"]:
                option_entries[key].insert(
                    0,
                    question["options"][key]
                )

            answer_var.set(
                question["answer"]
            )

            topic_entry.insert(
                0,
                question["topic"]
            )

            difficulty_var.set(
                question["difficulty"]
            )

        def save_question():
            question_value = question_text.get(
                "1.0",
                "end"
            ).strip()

            options = {}

            for key in ["A", "B", "C", "D"]:
                options[key] = option_entries[
                    key
                ].get().strip()

            answer = answer_var.get()
            topic = topic_entry.get().strip()
            difficulty = difficulty_var.get()

            if not question_value:
                messagebox.showerror(
                    "Error",
                    "Question cannot be empty.",
                    parent=window
                )
                return

            if any(
                not options[key]
                for key in ["A", "B", "C", "D"]
            ):
                messagebox.showerror(
                    "Error",
                    "All four options are required.",
                    parent=window
                )
                return

            if not topic:
                messagebox.showerror(
                    "Error",
                    "Topic cannot be empty.",
                    parent=window
                )
                return

            new_question = {
                "question": question_value,
                "options": options,
                "answer": answer,
                "topic": topic,
                "difficulty": difficulty
            }

            if index is None:
                questions.append(
                    new_question
                )
            else:
                questions[index] = new_question

            save_json(
                QUESTIONS_FILE,
                questions
            )

            messagebox.showinfo(
                "Success",
                "Question saved successfully.",
                parent=window
            )

            window.destroy()

            self.admin_question_bank()

        ttk.Button(
            window,
            text="Save Question",
            style="Action.TButton",
            command=save_question
        ).pack(pady=15)

        ttk.Button(
            window,
            text="Cancel",
            command=window.destroy
        ).pack(pady=5)


    # ========================================================
    # DELETE QUESTION
    # ========================================================

    def delete_question(self, tree):
        selection = tree.selection()

        if not selection:
            messagebox.showwarning(
                "Select Question",
                "Please select a question to delete."
            )
            return

        index = int(selection[0])

        questions = load_json(
            QUESTIONS_FILE,
            []
        )

        question = questions[index]

        confirm = messagebox.askyesno(
            "Delete Question",
            "Are you sure you want to delete this question?\n\n"
            + question["question"]
        )

        if not confirm:
            return

        questions.pop(index)

        save_json(
            QUESTIONS_FILE,
            questions
        )

        messagebox.showinfo(
            "Success",
            "Question deleted successfully."
        )

        self.admin_question_bank()


    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self):
        self.current_user = None
        self.show_home()


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()

    app = QuizApplication(root)

    root.mainloop()