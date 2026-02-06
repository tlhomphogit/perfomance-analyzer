from analyzer import PerfomanceAnalyser

def main():
    filename = 'student_results.csv'
    perfomance = PerfomanceAnalyser()
    perfomance.read_from_file(filename)

    print('-' * 29)
    print('STUDENTS PERFOMANCE ANALYZER')
    print('-' * 29)
    print(f'Avarage Score      : \t{perfomance.calc_avg()}')
    print(f'Highest Score      : \t{perfomance.get_highest()}')
    print(f'Lowest Score       : \t{perfomance.get_lowest()}')
    print(f'Number of Students : \t{perfomance.get_number_stud()}')
    print('-' * 39)

    print(f'{"Name":<10} {"Surname": <10} {"Results":<10} {"Status": <10}')
    print('-' * 39)
    for students in perfomance.add_status():
       print(f'{students["name"]:<10} {students["surname"]:<10} {students["score"]:<10} {students["status"]}')
    print('-' * 39)

if __name__ == '__main__':
    main()