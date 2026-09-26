# Workshop: Programming Lab — Human-Centered Artificial Intelligence

**Università degli Studi di Milano — A.Y. 2026/2027**

| | |
|---|---|
| **Course** | Workshop: Programming Lab |
| **Programme** | Human-Centered Artificial Intelligence (LM-55 R) |
| **Credits** | 3 ECTS — 36 hours (9 sessions × 4 h) |
| **Language** | English |
| **Period** | First semester |
| **Instructors** | [Ramon Winterhalder](https://www.rpwinterhalder.com) (sessions 1–3), tbc (sessions 4–9) |
| **Official page** | [myAriel](https://myariel.unimi.it/user/index.php?id=14344) · [unimi.it course page](https://www.unimi.it/en/education/degree-programme-courses/2027/workshop-programming-lab) |

---

## Where the material is

**myAriel** is the official page for the whole lab: announcements and material for all nine
sessions.

**This repository** holds the complete material for **sessions 1–3**: slides, exercise
notebooks and solutions. No login needed.

> **No access to Ariel yet, because your enrolment has not gone through?**
> Use this page for the first three sessions. Click **Watch → Custom → Releases** (top right)
> if you want a notification whenever new material appears.

| What | Where |
|---|---|
| Installing Python and VS Code | [`SETUP.md`](SETUP.md) |
| Session 1: slides, exercise notebook, files | [`lab01/`](lab01/) |
| Solutions | `labNN/solutions/` |

### Release policy

| Item | Published |
|---|---|
| Exercise notebook | before the session |
| Slides | at the start of the session |
| Solutions | after the session, once we have discussed them |

---

## Course description

A hands-on introduction to programming in Python. Most of every session is spent at the
keyboard: a short introduction, then exercises, then the solutions discussed together. It covers
variables and data types, conditions and loops, strings, lists, tuples, sets and dictionaries,
functions, working with files, and a first look at libraries, with an emphasis on writing
readable code and testing and fixing it.

**Prerequisites:** basic computer skills. Familiarity with basic programming concepts is
useful, not required.

Every exercise has a level: 🟢 **core** (everyone), 🟡 **stretch**, 🔴 **challenge**
(if you have programmed before). Finish the core exercises first.

---

## Schedule

| # | Date | Topics |
|---|---|---|
| 01 | 28.09 | Setup, running Python three ways (prompt, script, notebook), the terminal, first programs, reading error messages |
| 02 | 05.10 | Variables, values, types and operators; input from the user |
| 03 | 12.10 | Conditions, logical operators, handling errors with `try` / `except` |
| 04–09 | from 19.10 | Loops and lists, strings, tuples, sets, dictionaries, functions, files, libraries |

Sessions 1–3 build one small program step by step: a rule-based study assistant.

---

## Getting set up

Follow [`SETUP.md`](SETUP.md). Session 1 starts with it, so if something does not work yet,
bring your laptop anyway.

### Getting the material

Use the green **Code → Download ZIP** button, or, if you already use git:

```bash
git clone https://github.com/ramonpeter/programming-lab-hcai-2026.git
cd programming-lab-hcai-2026
git pull            # run this before each session to get the new material
```

---

## Assessment

Pass / fail (*superato / non superato*).

- **Standard route:** a final practical test. Nothing needs to be handed in during the term.
- **Project route**, for students who can already program: an individual project, presented
  in about 10 minutes, with questions on your code. Evidence of prior experience: a passed
  programming exam, or a GitHub repository with code you wrote. Decide by **session 3
  (12.10)**. Details to follow.

---

## Questions

Open an [issue](../../issues) if you spot a mistake in the material or have a question that
others would benefit from. For anything personal, write an email.

---

## License

Course material (slides, exercises, texts): [CC BY-NC-SA 4.0](LICENSE).
Code and notebooks: [MIT](LICENSE).
