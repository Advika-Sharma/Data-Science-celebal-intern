#steps tp follow 
✅ 1. Understand the Need for Virtual Environments
You should be able to explain:

Why virtual environments are necessary (e.g., avoiding package version conflicts across different Python projects).

How they help isolate project dependencies.

✅ 2. Create and Use Virtual Environments (venv)
Be comfortable with:

Running: python -m venv myenv

Activating the environment:

On Windows: myenv\Scripts\activate

On Mac/Linux: source myenv/bin/activate

Deactivating it: deactivate

Understanding how activating changes your python path and environment.

✅ 3. Manage Packages with pip
Practice commands like:

Installing:
python -m pip install <package>
e.g., python -m pip install numpy

Installing a specific version:
python -m pip install requests==2.6.0

Upgrading:
python -m pip install --upgrade requests

Uninstalling:
python -m pip uninstall requests

Listing installed packages:
python -m pip list
or python -m pip freeze

Creating and using requirements.txt for reproducible environments:

Export: python -m pip freeze > requirements.txt

Install: python -m pip install -r requirements.txt







#cmd 
Microsoft Windows [Version 10.0.26100.4202]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Advika Sharma>python -m venv myenv

C:\Users\Advika Sharma>myenv\Scripts\activate

(myenv) C:\Users\Advika Sharma>deactivate
C:\Users\Advika Sharma>python -m pip install numpy
Defaulting to user installation because normal site-packages is not writeable
Collecting numpy
  Downloading numpy-2.3.0-cp313-cp313-win_amd64.whl.metadata (60 kB)
Downloading numpy-2.3.0-cp313-cp313-win_amd64.whl (12.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.7/12.7 MB 3.9 MB/s eta 0:00:00
Installing collected packages: numpy
  WARNING: The scripts f2py.exe and numpy-config.exe are installed in 'C:\Users\Advika Sharma\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed numpy-2.3.0

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip

C:\Users\Advika Sharma>python -m pip install requests==2.6.0
Defaulting to user installation because normal site-packages is not writeable
Collecting requests==2.6.0
  Downloading requests-2.6.0-py2.py3-none-any.whl.metadata (31 kB)
Downloading requests-2.6.0-py2.py3-none-any.whl (469 kB)
Installing collected packages: requests
Successfully installed requests-2.6.0

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip

C:\Users\Advika Sharma>python -m pip install --upgrade requests
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: requests in c:\users\advika sharma\appdata\roaming\python\python313\site-packages (2.6.0)
Collecting requests
  Downloading requests-2.32.4-py3-none-any.whl.metadata (4.9 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.4.2-cp313-cp313-win_amd64.whl.metadata (36 kB)
Collecting idna<4,>=2.5 (from requests)
  Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Downloading urllib3-2.4.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests)
  Downloading certifi-2025.4.26-py3-none-any.whl.metadata (2.5 kB)
Downloading requests-2.32.4-py3-none-any.whl (64 kB)
Downloading certifi-2025.4.26-py3-none-any.whl (159 kB)
Downloading charset_normalizer-3.4.2-cp313-cp313-win_amd64.whl (105 kB)
Downloading idna-3.10-py3-none-any.whl (70 kB)
Downloading urllib3-2.4.0-py3-none-any.whl (128 kB)
Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests
  WARNING: The script normalizer.exe is installed in 'C:\Users\Advika Sharma\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Attempting uninstall: requests
    Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed certifi-2025.4.26 charset_normalizer-3.4.2 idna-3.10 requests-2.32.4 urllib3-2.4.0

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip

C:\Users\Advika Sharma>python -m pip uninstall requests
Found existing installation: requests 2.32.4
Uninstalling requests-2.32.4:
  Would remove:
    c:\users\advika sharma\appdata\roaming\python\python313\site-packages\requests-2.32.4.dist-info\*
    c:\users\advika sharma\appdata\roaming\python\python313\site-packages\requests\*
Proceed (Y/n)? Y
  Successfully uninstalled requests-2.32.4

C:\Users\Advika Sharma>python -m pip list
Package            Version
------------------ ---------
certifi            2025.4.26
charset-normalizer 3.4.2
idna               3.10
numpy              2.3.0
pip                25.0.1
urllib3            2.4.0

C:\Users\Advika Sharma>python -m pip freeze > requirements.txt

C:\Users\Advika Sharma>python -m pip install -r requirements.txt
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: certifi==2025.4.26 in c:\users\advika sharma\appdata\roaming\python\python313\site-packages (from -r requirements.txt (line 1)) (2025.4.26)
Requirement already satisfied: charset-normalizer==3.4.2 in c:\users\advika sharma\appdata\roaming\python\python313\site-packages (from -r requirements.txt (line 2)) (3.4.2)
Requirement already satisfied: idna==3.10 in c:\users\advika sharma\appdata\roaming\python\python313\site-packages (from -r requirements.txt (line 3)) (3.10)
Requirement already satisfied: numpy==2.3.0 in c:\users\advika sharma\appdata\roaming\python\python313\site-packages (from -r requirements.txt (line 4)) (2.3.0)
Requirement already satisfied: urllib3==2.4.0 in c:\users\advika sharma\appdata\roaming\python\python313\site-packages (from -r requirements.txt (line 5)) (2.4.0)

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip
