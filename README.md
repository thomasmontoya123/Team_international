# Team_international
Team international challenge


The challenge is to create a program that computes some
basic statistics on a collection of small positive integers. You
can assume all values will be less than 1,000.


# First clone the repo 


# With Docker

## Requirements 
 - Docker


# Build image 
 -  Inside the repo code 
 ```
         docker build -t team_challenge .
```

- Open docker interactive session 
```
         docker run -it team_challenge bash
```

- If you want to recreate the email exmaple 
```
         python mail_example.py
```

- If you want to run the tests
```
         pytest
```

# Run local 

## Requirements 
 - python > 3.10


# Setup 
-   Create environment

    ```
        python3 -m venv venv
    ```

- Activate Environment on windows 

    ```
        path\to\venv\Scripts\activate.bat
    ```

- Activate Environment on linux 

    ```
        source /path/to/venv/bin/activate
    ```




# Run TESTS

        pytest


# Run Email example


        python3 mail_example.py