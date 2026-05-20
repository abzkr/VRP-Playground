# Vehicle Routing Problem - Algorithm Development Portfolio

## Requirements
Python 3 (Only internal modules used - matplotlib, itertools, time etc)

## Project Strcture
src/ -> algorithm implementation source code
Output Screenshots/ -> Screenshots of algorithm outputs (5 test cases with varying data for each algorithm)

## How to Run

### Algorithms:
python src/greedy_solution.py
python src/ai_solution.py
python src/optimised_solution.py

In each file, datasets.py can be imported and the datasets can be used
with all algorithms for individual testing.

### Benchmarking:
pip install matplotlib   (main dependency)
python /src/benchmark.py

## Datasets
5 datasets of varying sizes (7, 9, 10, 12, 15 nodes) are included in datasets.py

## Output
Each algorithm prints routes and total distance to the terminal.
benchmark.py generates three comparison graphs as well as numerical outputs of time/distance benchmarks.