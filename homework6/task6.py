import sys
import os
import json
import yaml
import subprocess

list1 = ['version', 'name', 'python executable location', 'pip location', 'PYTHONPATH', 'installed packages','site packages']
list2 = [sys.version[:5], os.popen('pyenv version-name').read().strip(), sys.executable,
         os.popen("which pip").read().strip(), sys.exec_prefix,os.popen("pip freeze").read().strip().split('\n'),
         subprocess.getoutput("python -m site --user-site")]
dictionary = dict(zip(list1, list2))
json = json.dumps(dictionary, indent=4, sort_keys=True)
with open('data.json', 'w') as outfile:
    outfile.write(json)
    outfile.close()
with open('data.yaml', 'w') as outfile:
    outfile.write(yaml.dump(dictionary, allow_unicode=True))
    outfile.close()


