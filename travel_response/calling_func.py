# from nbconvert import execute_notebook
from pathlib import Path
from nbclient import NotebookClient
import nbformat

root_dir = Path.cwd()
# print(root_dir)
graph_notebook = root_dir / 'graph.ipynb'
print(graph_notebook)

with open(graph_notebook) as f:
    gnb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

client = NotebookClient(gnb)
print(client)
# client.execute()

