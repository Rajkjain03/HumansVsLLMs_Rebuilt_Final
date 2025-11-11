import os, nbformat, zipfile
from nbclient import NotebookClient

base_dir = os.path.dirname(__file__)
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.ipynb'):
            nb_path = os.path.join(root, file)
            if os.path.abspath(root) == os.path.abspath(base_dir): continue
            print('Executing', nb_path)
            nb = nbformat.read(nb_path, as_version=4)
            client = NotebookClient(nb, timeout=None, kernel_name='python3', allow_errors=True)
            client.execute()
            nbformat.write(nb, nb_path)
out_zip = os.path.join(base_dir, 'HumansVsLLMs_Rebuilt_Final_Executed.zip')
with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.ipynb'):
                zf.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), base_dir))
print('Created', out_zip)
