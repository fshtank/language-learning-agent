import json

file_path = '/clean-word-lists.ipynb'
with open(file_path, 'r') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell.get('source', [])
        if isinstance(source, list):
            for i in range(len(source)):
                line = source[i]
                if '"type": ["Raw"] * 21,' in line:
                    source[i] = line.replace('"type": ["Raw"] * 21,', '"type": ["Raw"] * len(language_raw),')
                elif '"type": ["Clean"] * 21,' in line:
                    source[i] = line.replace('"type": ["Clean"] * 21,', '"type": ["Clean"] * len(language_clean),')
                elif 'language_clean += [path.split("/")[1]]' in line:
                    source[i] = line.replace('language_clean += [path.split("/")[1]]', 'language_clean += [os.path.basename(path)]')

with open(file_path, 'w') as f:
    json.dump(nb, f, indent=1)
