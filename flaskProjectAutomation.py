"""
======================================================================================================================
Author:                         {root@lonedevwolf}
Language:                       Python
Modules:                        os, sys
Description:                    Automating a Python Flask Project Creation
======================================================================================================================
[!]:

"""
import os
import sys


def createFlaskProject(projectName):
    # Create project directory
    os.makedirs(projectName, exist_ok=True)

    # Create Virtual Environment
    os.system(f"python -m venv {os.path.join(projectName)}")

    # Create main application file
    appFileContent = """from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def helloWorld():
        return "Hello World"
        
    
    if __name__ == __main__":
        app.run(debug =True)
    """
    with open(os.path.join(projectName, 'app.py'), 'w') as appFile:
        appFile.write(appFileContent)

    # Create requirement file
    requirementContent = "Flask\n"
    with open(os.path.join(projectName, 'requirement.txt'), 'w') as reqFile:
        reqFile.write(requirementContent)

    # Create Run Script
    runScriptContent = f"""#!/bin/bash source{os.path.join(projectName, 'venv', 'bin', 'activate')}
    pip install -r {os.path.join(projectName, 'requirement.txt')}
    python {os.path.join(projectName, 'app.py')}
    """

    with open(os.path.join(projectName, 'run.sh'), 'w') as runFile:
        runFile.write(runScriptContent)

    # Create the run script executable
    os.chmod(os.path.join(projectName, 'run.sh'), 0o0755)
    print(f"Flask project '{projectName}' created successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python createFlaskProject.py <projectName>")
    else:
        projectName = sys.argv[1]
        createFlaskProject(projectName)