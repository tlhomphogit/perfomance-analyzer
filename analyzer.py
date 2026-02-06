import os
import csv

class PerfomanceAnalyser():
    def __init__(self):
        self.student_data = []

    def read_from_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f'Error! The file {filename} was not found.')

        with open(filename, mode='r') as file:
            student_results = csv.DictReader(file)
        
            for row in student_results:
                row['score'] = int(row['score'])
                self.student_data.append(row)

    
    def calc_avg(self):
        self.scores = [s['score'] for s in self.student_data]
        return round(sum(self.scores) / len(self.scores), 2)
    
    def get_lowest(self):
        return min(self.scores)

    def get_highest(self):
        return max(self.scores)
    
    def add_status(self):
        self.student_data = [
            {'name': s['name'], 
            'surname': s['surname'],
            'score': s['score'], 
            'status': 'pass' if s['score'] >= 50 else 'fail'} for s in self.student_data
        ]
        return self.student_data


    def get_number_stud(self):
        return len(self.student_data)
        