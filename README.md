# Parallel Syntax highlighter 
Parallel Syntax Highlighter is a Python script that tokenizes a given .txt file and creates an HTML file for visualizing the different tokens located in the text. The script uses PLY library and multiprocessing module to analyze the files in parallel, resulting in a significant speedup when processing multiple files.

## Usage
The script requires Python 3 and the PLY library to be installed. To use the script:
1. Clone the repository to your local machine.
2. Navigate to the repository folder.
3. Place the .txt files you want to analyze in the src/input directory.
4. Run the script using the command python main.py.
5. The analyzed HTML files will be stored in the parallel_outputs and sequential_outputs directories.

## Token Types
The script tokenizes the text using the following types:
- delimiter: white space, tabulation or a new line.
- regex_1 to regex_12: Regular expressions defined in ./src/regex.txt file.


## Multiprocessing
The script uses the multiprocessing module to analyze files in parallel. The number of processes used is determined by the available CPUs minus one.

## Performance Comparison
The script includes a performance comparison between sequential and parallel execution. The script analyzes the files sequentially and in parallel and calculates the execution time for both methods. It also shows the speedup achieved by parallel execution.
