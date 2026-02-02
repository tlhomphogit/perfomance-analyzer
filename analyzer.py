class PerfomanceAnalyser():
    def __init__(self):
        pass

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            student_results = file.read()
