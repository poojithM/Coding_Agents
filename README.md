# Code Execution and Analysis System

This system uses the `crewai` library to set up an automated environment for executing and analyzing Python code. It is designed to identify and correct errors in code snippets, provide detailed error analyses, and rewrite the corrected code with explanations.

## System Components

### Agents
- **Code Execution Agent**: This agent is responsible for running the Python code until it executes without errors. It is equipped with tools to interpret code and read files, aiming to find and fix errors in the code.

- **Code Reporting Analyst**: After the code execution agent corrects the code, this agent takes over to write the error-free code into a new Python file. It includes explanations of the errors as comments, ensuring clarity and understanding.

### Tools
- **CodeInterpreterTool**: Assists the Code Execution Agent by interpreting the provided code, looking for syntactic and runtime errors.

- **FileWriterTool**: Used by the Code Reporting Analyst to write the corrected code and explanations into a new file.

- **FileReadTool**: Allows the Code Execution Agent to read from the specified file, aiding in the error detection and correction process.

### Tasks
- **Task 1**: Involves the Code Execution Agent, which reads and attempts to execute the code, identifies errors, and provides corrected code along with explanations.

- **Task 2**: The Code Reporting Analyst writes the corrected code and documents the errors in comments, aiming for clear and informative annotations.

### Process
The process is defined as sequential, meaning Task 1 must complete before Task 2 begins. This ensures that the code is corrected before any reporting or documentation is done.

### Crew
A crew consisting of both agents carries out the tasks in the specified order. The process is controlled and verbose output is enabled for detailed tracing.

## Usage

To run this system, ensure you have the necessary environment variables set (e.g., `OPENAI_API_KEY`), and the `crewai`, `langchain_openai`, and `dotenv` libraries installed.

Once configured, execute the script to initiate the crew, which will process the tasks sequentially and output the results.

## Dependencies
Ensure you have the following dependencies installed:
- `crewai`: This library is essential for setting up the agents and tasks.
- `langchain_openai`: Provides integration with OpenAI's models.
- `python-dotenv`: For loading environment variables from a `.env` file.

## Configuration
- Make sure to set up your `.env` file with your `OPENAI_API_KEY`.

## Results
The results of the script will print the output from the Crew, showing whether the code was processed successfully and any errors were corrected and documented.

