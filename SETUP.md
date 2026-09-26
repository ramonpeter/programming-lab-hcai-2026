# Setup

You need three things. That is all, for the whole lab.

| | What it is | What it does |
|---|---|---|
| **Python** | the interpreter | reads your code and runs it |
| **VS Code** | an editor | where you write `.py` files and notebooks, with a terminal built in |
| **Jupyter** | notebooks | code, output and text in one file (`.ipynb`); runs inside VS Code |

**Google Colab** (<https://colab.research.google.com>) runs notebooks in the browser with
nothing to install. It is the fallback if your installation does not work yet — not a
replacement: you cannot run a `.py` script from a terminal there.

---

## 1 · Install Python

Pick **one** route. If unsure, take **A**.

- **A — python.org** (recommended). Small, standard, what the rest of the world uses.
- **B — conda** — *expert mode.* conda manages separate Python environments and scientific
  packages. Worth it later, more to understand now. Fine if you already use it or want to try
  it. Instructions [below](#route-b--conda-all-systems). Do **not** install both A and B.

The sections for Windows, macOS and Linux are route **A**.

### Windows

Since Python 3.14, python.org installs Python on Windows through the
**Python install manager**. Get it from <https://www.python.org/downloads/> (or search
*"Python Install Manager"* in the Microsoft Store — it is the same thing).

1. Install it and open a **new** PowerShell window (Start → "PowerShell").
2. It runs a short configuration check the first time. **Answer yes** to its questions —
   in particular to adding its commands to your PATH. (If it did not appear:
   `py install --configure`.)
3. Install the current Python:

   ```
   py install 3.14
   ```

Check, in a **new** PowerShell window:

```
python --version
```

If you see *"Python was not found; run without arguments to install from the Microsoft
Store"*, the terminal is finding the Windows placeholder instead of your Python: close all
terminals, run `py install --configure` again and accept the PATH change, then open a new
terminal.

### macOS

macOS has a `python3` that belongs to the system tools; do not use it for the lab.

Download the **macOS 64-bit universal2 installer** for Python 3.14 from
<https://www.python.org/downloads/> and run it. At the end, double-click
*Install Certificates.command* in the folder that opens.

Check, in *Terminal* (Cmd + Space → "Terminal"):

```
python3 --version
```

With route A, the command on macOS and Linux is **`python3`**, not `python`.

### Linux

Python 3 is almost certainly installed already. Check:

```
python3 --version
```

If it is older than 3.12, or missing, install it from your package manager, e.g. on
Ubuntu/Debian:

```
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

`python3` works on every distribution. Plain `python` depends on the distribution: Fedora and
Arch have it, Ubuntu and Debian do not (unless you install `python-is-python3`). Use
`python3` and you never have to think about it.

### Route B — conda (all systems)

Install **Miniforge** (<https://github.com/conda-forge/miniforge>): conda, set up to use the
free community channel *conda-forge*. Miniconda or Anaconda work too, if you already have
one.

Then, in a terminal — on Windows the **Miniforge Prompt** (or **Anaconda Prompt**) from the
Start menu, since `conda` is not found in an ordinary PowerShell:

```
conda create -n lab python=3.13 ipykernel
conda activate lab
python --version
```

Inside an activated environment the command is **`python` on every system** — also on
macOS and Linux. Run `conda activate lab` each time you open a new terminal; the prompt
then starts with `(lab)`.

---

## 2 · Install VS Code

Download from <https://code.visualstudio.com/> and install. Then open VS Code, go to the
**Extensions** panel (the four squares on the left, or Ctrl/Cmd + Shift + X) and install:

- **Python** (by Microsoft)
- **Jupyter** (by Microsoft)

---

## 3 · First run

1. Create a folder `programming-lab`, with a folder `lab01` inside it.
2. In VS Code: *File → Open Folder…* → choose `programming-lab`.
3. Open a terminal inside VS Code: *Terminal → New Terminal*.
4. Type `python --version` (Windows) or `python3 --version` (macOS/Linux).
   With conda: `conda activate lab`, then `python --version`.
5. Open `lab01-exercises.ipynb`. Click **Select Kernel** (top right) → *Python Environments*
   → the Python you installed in step 1 (with conda: the one called `lab`).

   Route A: if VS Code asks to install **ipykernel**, say yes. If it does not offer, run in
   the terminal:

   ```
   python -m pip install ipykernel        # Windows
   python3 -m pip install ipykernel       # macOS / Linux
   ```

   Linux, if pip refuses with *"externally-managed-environment"*: create a small environment
   inside `programming-lab` and pick `.venv` as the kernel in step 5:

   ```
   python3 -m venv .venv
   .venv/bin/python -m pip install ipykernel
   ```

   With conda, `ipykernel` is already in the environment.

6. Run the first code cell (Shift + Enter). It should print `Python 3.1x.x on ...`.

Done.

---

## When it does not work

- **In session 1:** put your hand up — we solve installation problems in class. Still stuck
  after ~20 minutes: use Colab for the rest of the session and finish the setup at home.
- **No laptop in session 1?** Then this page is your homework before session 2.
- **"python is not recognized" / "command not found"** → the terminal cannot find Python.
  Close *all* terminals and VS Code, open again. Still failing: PATH (Windows, see above).
- **Notebook runs the wrong Python** → click the kernel name, top right, pick the right one.
- **Everything else**: copy the **last line** of the error message into your question.
