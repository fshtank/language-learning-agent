import json

file_path = '/clean-word-lists.ipynb'
with open(file_path, 'r') as f:
    nb = json.load(f)

# The cell that defines 'language' and 'total_words' is the second cell (index 1)
# We want to insert the DataFrame cell right after it (index 2)
new_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "pd.DataFrame({\n",
        "    \"language\": language,\n",
        "    \"total_words\": total_words\n",
        "})"
    ]
}

# Insert at index 2
nb['cells'].insert(2, new_cell)

with open(file_path, 'w') as f:
    json.dump(nb, f, indent=1)
