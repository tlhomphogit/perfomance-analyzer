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
                
    def __str__(self):
        return f'{self.student_data}'
    
    def __repr__(self):
        pass

def main():
    filename = 'student_results.csv'
    perfomance = PerfomanceAnalyser()
    perfomance.read_from_file(filename)
    print(perfomance)

if __name__ == '__main__':
    main()