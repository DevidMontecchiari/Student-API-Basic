# Student API Basic: read, understand, adapt

This small starter implements **Student** from our Student / Course / Enrolment model. Alice (1001) and Noah (1002) are fictional. All the API code to study is in **[main.py](main.py)**.

This is an independent student starter. The lecturer's larger School IS API reference also demonstrates Course, Enrolment and Python objects; it is not needed for this first activity.

## 1. Run your own copy

Repository: [Student-API-Basic](https://github.com/DevidMontecchiari/Student-API-Basic).

**In the browser:** on GitHub select **Code > Codespaces > Create codespace**. This creates your own environment, not access to the lecturer's running application. To keep and push changes to your own repository, fork the starter first and open your Codespace on that fork.

Wait for setup to finish. In a terminal at the repository root, enter only:

```sh
python run.py
```

**Cannot start it?** Follow the [quick startup checks](#quick-startup-checks).

Open **Ports > 8000 > Open in Browser**, then add `/docs` to the forwarded address. Keep the port private. Leave the terminal running; **Ctrl+C** stops it.

**On your computer:** clone this repository or choose **Code > Download ZIP**, then open that folder in VS Code. Follow [local setup](#optional-run-locally) to install the two dependencies and run the same application.

No local Python or Docker installation is needed for the browser route. Codespaces availability depends on your GitHub account.

```text
main.py                 read the data and handle three GET routes
data/students.json      fictional records (the data/ folder)
run.py                  supplied launcher, port 8000
requirements.txt        FastAPI and Uvicorn dependencies
.devcontainer/          supplied Codespaces environment setup
```

`run.py` starts **Uvicorn**, the web server, which loads the **FastAPI** application named `app` from `main.py`. Leave the supplied launcher and configuration unchanged. Start reading `main.py`.

## 2. Try the read operations

In `/docs`, expand a route, select **Try it out**, enter a value if needed, then **Execute**. Compare the status and JSON response.

| Request | Expected result |
| --- | --- |
| `GET /` | 200: welcome message and documentation path |
| `GET /students` | 200: an array containing Alice and Noah |
| `GET /students/1002` | 200: Noah's record |
| `GET /students/9999` | 404: `Student not found` |
| `GET /students/abc` | 422: the path value is not an integer |

For the last request, replace `/docs` in the browser address with `/students/abc` if the documentation interface prevents text in the integer field. A valid ID with no matching record and a value of the wrong type are different errors.

## 3. Follow one request in the code

Trace `GET /students/1002` through [main.py](main.py):

1. `@app.get("/students/{student_id}")` connects the URL pattern to `get_student`.
2. `student_id: int` tells FastAPI to validate and convert the URL value; the function receives the integer `1002`.
3. `load_students()` reads `data/students.json` into a Python list of dictionaries.
4. `for student in students` checks each record. `student["student_id"]` reads the dictionary's ID; `==` compares it with the requested ID.
5. `return student` ends the function when Noah is found. FastAPI sends the dictionary as a JSON response.
6. If no record matches, `raise HTTPException(...)` **after the loop** sends 404.

**Python refresher:** `def` defines a function; parentheses call it. Indentation groups the statements in a function, loop or `if`. `=` assigns a value while `==` compares values. `with ... as file` closes the file after its indented block. `@app.get(...)` is a decorator registering a route. The `int` annotation is a type hint that FastAPI uses for validation; ordinary Python type hints alone do not enforce types.

The JSON array becomes a Python **list**, and each JSON object becomes a **dictionary**. `json` and `pathlib` are included with Python. FastAPI and Uvicorn are the two direct dependencies in `requirements.txt`; installing them also installs libraries they depend on.

The file path is relative to `main.py`, not the terminal's working directory. Data is loaded on each request. A missing or invalid JSON file is a data/setup error, not a missing student.

## 4. Edit, read again, restore

1. In [data/students.json](data/students.json), change `Noah` to `Noah Keller`; keep ID `1002`.
2. Save and repeat `GET /students/1002`, then `GET /students`. Both should show the updated record.
3. Restore the name to `Noah`, save, and request it again.

This is a manual file edit. The API has only **GET** operations; it does not save or create records. There is no separate database or initial-data copy: `data/students.json` is the file being read.

## 5. Adapt one entity from your project

Follow **[From your models to a working API](docs/from-models-to-prototype.md)** for a step-by-step guide: select a use case, map model attributes to JSON and routes, adapt the example, check the results and plan the next operation. Keep it open beside your own models and code.

Choose an entity already described by your UML/data model and sample JSON. Identify its ID field, adapt the file and route names, and change the dictionary key used by the search. Keep the **read all / read one** pattern first. Check an existing ID, a missing ID and an invalid value.

Keep field names and value types consistent with your model. String IDs need a matching path parameter type and comparison. This activity supports the project without adding assessment requirements. The starter has no login: a student ID is a lookup, not proof of identity. Keep data fictional.

## Optional: run locally

With Python 3.12 or newer, create an environment in this folder using `python -m venv .venv`. Activate it with `.\.venv\Scripts\Activate.ps1` in Windows PowerShell or `source .venv/bin/activate` on macOS/Linux. Then:

```sh
python -m pip install -r requirements.txt
python run.py
```

Open <http://127.0.0.1:8000/docs>.

## Quick startup checks

In Codespaces, wait for environment setup to finish and use **Terminal > New Terminal** inside the Codespace. Python is supplied there; you do not need to install it on your laptop.

1. **Does Python work?** Enter `python --version`. This starter needs Python 3.12 or newer. If the command is not found locally, try `py --version` on Windows or `python3 --version` on macOS/Linux. Use the working command consistently, for example `py run.py`. If none works, [install Python](https://www.python.org/downloads/) and reopen the terminal, or use Codespaces.
2. **Are you in the correct folder?** Enter `pwd`, then `ls` (`dir` also works in PowerShell). You should see `run.py`, `main.py` and `requirements.txt`. If Python says it cannot open `run.py`, change to that folder with `cd "path/to/your/starter"`. Enter only the command, without a copied `Run:`, `$` or `PS ...>` prefix.
3. **Are dependencies installed in this Python environment?** For `No module named uvicorn` or `fastapi`, run the following in the starter folder. Locally, create and activate the environment described under [Optional: run locally](#optional-run-locally) first.

   ```sh
   python -m pip install -r requirements.txt
   python run.py
   ```

   A `(.venv)` prompt only tells you that an environment is active; it may belong to a different project. `python -c "import sys; print(sys.executable)"` shows which Python you are using.

   Use the same Python command for both lines. If PowerShell blocks environment activation, you can use `.\.venv\Scripts\python.exe` instead of `python` in both lines after creating the environment. [Python environment documentation](https://docs.python.org/3/library/venv.html).
4. **Is port 8000 already in use?** Stop your earlier application with **Ctrl+C** in its terminal, then retry. If you cannot find it, ask for help rather than stopping unrelated programs.
5. **It runs, but the page does not open?** Keep the terminal running. In Codespaces use **Ports > 8000 > Open in Browser**, then append `/docs`. Locally open <http://127.0.0.1:8000/docs>.

**PowerShell shows "Oops, something went wrong" with `PSReadLine` / `SetCursorPosition`?** This is the terminal line editor failing. Open a **Command Prompt** terminal using VS Code's terminal dropdown. From the starter folder, after creating its `.venv`, use these commands directly without activation:

```bat
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe run.py
```

For VS Code's Run button, use **Python: Select Interpreter** and choose this starter's `.venv\Scripts\python.exe`. [About PowerShell's PSReadLine editor](https://learn.microsoft.com/en-us/powershell/module/psreadline/about/about_psreadline).

Still stuck? Share the command you entered and the full error message, and say whether you are using Codespaces or your own computer.

## References

- [FastAPI: First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/): application, routes and automatic documentation.
- [FastAPI: Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/): typed URL values and validation.
- [FastAPI: Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/): `HTTPException` and 404.
- [Python: JSON](https://docs.python.org/3.14/library/json.html): JSON text and Python values.
