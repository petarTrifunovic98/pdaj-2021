# Petar Trifunović, br. indeksa E2 4/2021

# pdaj-2021

To install all the required dependencies, run:
- "poetry lock" (might take a bit longer because of the matplotlib dependency)
- "poetry install"

Plain scripts:
- run "poetry shell"
- "cd ./plain_scripts_solutions"
- run scripts using "python script_name"
- available solutions are:
    - a sequential solution, in "sequential.py",
    - a solution using list comprehension, in "list_comprehension.py",
    - a solution using generators, in "generator.py", and
    - a solution using the multiprocessing library, in "multiprocessing_solution.py"

Web application:
- run "docker-compose up --build"
- the Dockerfile also runs "poetry lock" which might take some time
- all the routes start with "http://localhost:8000/computation"; on this, you can append:
    - "/sequential",
    - "/list_comprehension",
    - "/generator", or
    - "/multiprocessing"
- each of the routes corresponds to one of the solutions explained above