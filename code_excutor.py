from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import CodeInterpreterTool, FileWriterTool, FileReadTool

from langchain_openai import OpenAI
import os

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo', temperature = 0.5, api_key = os.getenv("OPENAI_API_KEY"))

code_interpreter = CodeInterpreterTool()
file_writer = FileWriterTool()
file_read = FileReadTool({"code": "code_sample.py"})

Agent1 = Agent(
    role = "Code Execution Agent",
    goal = """Run the code file till it didnt getting any erros and provide the explanation 
                of error""",
    backstory = """You are master at executing the code and finding the errors and rewrite the correct code""",
    tools = [code_interpreter, file_read],
    LLM = llm,
    verbose = True,
    allow_delegation = False
)

Agent2 = Agent(
    role = "Code Reporting Analyst",
    goal = """From the provided corrected code and summary write the corrected code 
              and explanation of errors in comments  in a python file""",
    backstory = """You are master at understanding the code and error""",
    tools = [file_writer],
    LLM = llm,
    verbose = True,
    allow_delegation = False
    
)

Task1 = Task(
    description = """First understand and read the code file {code} Find the errors and provide the errorless 
                    code and explanation of errors""",
    expected_output = """Errorless code with explanation of errros in the code""",
    agent = Agent1
)

Task2 = Task(
    description = """Write the error less code in new python file with explanation of errors
                     in comments """,
    expected_output = """errorless correct code with explanation of errors in comments
                        in a python file""",
    agent = Agent2
)

crew = Crew(
    agents = [Agent1, Agent2],
    tasks = [Task1, Task2],
    verbose = True,
    process = Process.sequential,
)


result = crew.kickoff()
print(result)