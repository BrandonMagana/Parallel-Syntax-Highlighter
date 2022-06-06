import ply.lex as lex
from multiprocessing import Pool
import os
import glob
from datetime import datetime
import pathlib

N_PROCESSORS = os.cpu_count()-1
INPUT_DIRECTORIES = list(pathlib.Path('./src/input').glob('**/*.txt'))

tokens = (
    "delimiter",
    "regex_1",
    "regex_2",
    "regex_3",
    "regex_4",
    "regex_5",
    "regex_6",
    "regex_7",
    "regex_8",
    "regex_9",
    "regex_10",
    "regex_11",
    "regex_12",
)

with open("./src/regex.txt", "r") as file:
    reg_expressions = file.readlines()

t_delimiter = r'[\b    \b\t\s]'
t_regex_1 = rf"{reg_expressions[0]}"
t_regex_2 = rf"{reg_expressions[1]}"
t_regex_3 = rf"{reg_expressions[2]}"
t_regex_4 = rf"{reg_expressions[3]}"
t_regex_5 = rf"{reg_expressions[4]}"
t_regex_6 = rf"{reg_expressions[5]}"
t_regex_7 = rf"{reg_expressions[6]}"
t_regex_8 = rf"{reg_expressions[7]}"
t_regex_9 = rf"{reg_expressions[8]}"
t_regex_10 = rf"{reg_expressions[9]}"
t_regex_11 = rf"{reg_expressions[10]}"
t_regex_12 = rf"{reg_expressions[11]}"

def t_error(t):
    t.lexer.skip(1)

def analyzeFile(input):
    with open(input) as file:
        lexer = lex.lex()
        data = file.read()
        lexer.input(data)

    line = ''
    while True: 
        tok = lexer.token()
        if not tok:
            break
        
        if tok.type == 'delimiter':

            if tok.value == '\n': line += '<br>'
            if tok.value == '\t': line  += '&emsp'
            if tok.value == ' ' : line +=   "&nbsp;"

            else: 
                line += tok.value
        
        elif tok.type == 'regex_4':
            line += f'<span class={tok.type}>{tok.value}</span><br>'
        
        else:
            line += f'<span class={tok.type}>{tok.value}</span>'
    
    return line

def create_html_output_file(line, filename):
    new_line_index = 0
    with open('./src/template/index.html', 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if lines[i] == '\n':
            new_line_index = i 
            break

    lines[new_line_index] = line

    with open(f"{filename}", 'w') as file:
        file.writelines( lines )

def parallel_analisis(inputs_directories):
    pool = Pool(N_PROCESSORS)
    lines = pool.map(analyzeFile, inputs_directories)
    pool.close()
    
    for i in range(len(lines)):
        create_html_output_file(lines[i], f"./parallel_outputs/output_{i+1}.html")

def sequential_analisis(inputs_directories):
    lines = []
    
    for file in inputs_directories:
        lines.append(analyzeFile(file))

    for i in range(len(lines)):
        create_html_output_file(lines[i], f"./sequential_outputs/output_{i+1}.html")

    
def calculate_execution_time(function, inputs):
    start_time = datetime.now()
    function(inputs)
    return datetime.now() - start_time

def parallel_vs_sequential():
    print(f"Processes used: {N_PROCESSORS}")
    print(f"Analized files: {len(INPUT_DIRECTORIES)}")

    parallel_time = calculate_execution_time(parallel_analisis, INPUT_DIRECTORIES)
    sequential_time = calculate_execution_time(sequential_analisis, INPUT_DIRECTORIES)

    print(f"\nSequential time: {sequential_time}")
    print(f"Concurrent time: {parallel_time}")

    print(f"\nSpeed up: {sequential_time / parallel_time}")

if __name__ == '__main__':
    parallel_vs_sequential()
    