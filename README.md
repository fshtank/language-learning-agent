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