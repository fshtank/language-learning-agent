# Language Learning Agent
This project is based on the [JetBrains Agent AI Learning YouTube Video](https://www.youtube.com/watch?v=j4sNAwrx3kc)

It relies on [All Languages Dataset](https://github.com/eymenefealtun/all-words-in-all-languages) 

### _python packages_

```
uv add pandas
uv add ipywidgets  ## Jupyter Notebook widgets

## Language Processing ##
uv add spacy
uv add spacy-transformers
uv add wordfreq

## security
uv add python-dotenv
uv add langchain-core  ## I add all Langchain 😯 - oops
uv add langgraph   ## connect to LLM
uv add langchain-ollama
uv add langchain-openai
uv add langchain-mcp-adapters
```

### Jupyter Notebook

```
# String Processing
import csv
import os

#add Subprocesses that are needed
import subprocess

#String cleaning
from string import punctuation

# Data in a dataform 
import pandas as pd

# Data cleanup and adding additional info
import spacy
import spacy_transformers
from wordfreq import zipf_frequency


```

---


> main.py considering main.py in the project folder language-learning-agent/ , consider function def assistant lin 60 variable textual_description_of_tools.
> 1. Why does it have the tools.py methods definition for all three methods in text? and a description how to use them?

The textual_description_of_tools variable contains the method definitions and descriptions for three reasons related to Prompt Engineering and LLM Reliability:
1. Explicit Instruction (Grounding)
While the code later calls llm.bind_tools(tools), which passes the technical JSON schema of the functions to the model, many LLMs (especially smaller models like the qwen3:8b used here) perform significantly better when the tools are described in a natural or code-like format within the System Prompt.
By including the function signatures and docstrings, the developer is providing a "manual" that the agent can refer to before deciding which tool to call.
2. Constraint Enforcement
The textual descriptions include specific constraints that might be lost or ignored in a raw JSON schema. For example:
Difficulty Levels: It explicitly tells the model that difficulty_level "must be one of beginner, intermediate or advanced."
Output Formats: It describes the exact structure of the dictionary returned by translate_words, helping the model understand what to expect from the tool's output so it can plan the next step in the workflow.
3. Supporting the "Workflow" Examples
Further down in the sys_msg, the prompt provides example workflows:
Example: get_n_random_words_by_difficulty_level -> translate_words -> mcp_tools::create_deck -> mcp_tools::create_card
For the LLM to successfully map a user's request (e.g., "Get 10 easy words") to that specific sequence of tools, it needs to know exactly which tool handles "easy" (difficulty) versus "random" words. The textual descriptions provide the semantic link between the user's natural language and the specific function names.
Summary
In short, it serves as supplemental documentation. It ensures the model doesn't just know that these tools exist (via bind_tools), but understands exactly how and when to use them to achieve the desired result.