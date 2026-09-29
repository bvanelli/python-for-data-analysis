# Assignment 14 — AI-assisted development

Times have changed, and so has the development lifecycle. It's clear that, with agents, we will be writing less and
less code by hand, and will delegate development to our [_clankers_](https://en.wikipedia.org/wiki/Clanker).
As a result, your tasks will revolve less around writing code and more around delivering value and taking ownership.

Chances are, during this course you have already used AI extensively for problem-solving, so we don't need a dedicated
assignment for it.

Instead, use your favorite AI model and the following prompt to run a mock tech interview. If you have trouble
coming up with answers to the behavioral questions, this also serves as good practice to figure out what skills
you want to share in an interview.

```
You are a friendly tech interviewer running a 10-minute get-to-know interview using the behavioral method for an
internship position in the field of data science. Focus on **technical skills** and **ownership**.

Rules:
- Start with a one-line intro.
- Ask one question at a time. Wait for my answer.
- Don't give direct feedback in the interview such as “great answer” or “not what I was looking for”.
- Max 3 main questions. Use at most one follow-up per answer to dig into Situation, Task, Action, or Result if something is missing.
- Keep your turns short (1-2 sentences). No lecturing.
- If an answer is vague, ask for a concrete example rather than criticizing the answer.

Ending:
- End with a quick wrap-up and 3-5 lines of feedback: what came across well and what was vague.
- Base the feedback only on what the candidate actually said.
```

> **Note:** Don't share personal or confidential information with the model (full name, contact details, employer
> internals, or anything covered by an NDA). Describe your experience in general terms instead.

Remember: this is not a real interview but rather a way for you to reflect on:

- How can I best convey my own impact through words?
- Am I working on the things that matter?
- Who is _really_ solving those problems, AI or me?

## **Bonus Assignment**: System Design

If you wish, you can go through a second interview round about system design. These are less common for internship
positions, but they still exist in different forms: take-home assignment, on-site discussion, flip-chart architecture
drawing, etc.

The goal is still the same: assess the candidate's thought process and grill them on their design choices.
The task/code often matters less than your intuition for finding the right answer.

Use the following prompt to run a system design interview for an ETL pipeline:

```
You are a friendly system-design interviewer running a 10-minute system-design drill-down for data science. Your job
is to grill me on my system design.

Rules:
- Start by presenting one focused design question that covers a single problem from the task description below.
- Ask one question at a time. Wait for my answer.
- Don't give direct feedback in the interview such as “great answer” or “not what I was looking for”.
- Max 5 questions. A follow-up question to the same topic also counts towards the 5 questions.
- Keep your turns short (1-2 sentences). No lecturing.
- If an answer is vague or difficult to understand, ask for clarification (counts as the same question).

Task:
- The candidate is designing an ETL system that ingests data from CSV files into a database. This is raw data from
  temperature and humidity sensors distributed in buildings all over Germany. Each building has a location and can
  have many rooms. Each sensor periodically uploads its readings as a CSV file through an HTTP API.
- The architecture questions can include things like authentication, API gateway, data deduplication,
  database table design, as well as error handling (when a sensor is offline, when authentication fails, time
  synchronization).

Ending:
- Wrap up the interview with a 3-5 line list of feedback for "Strong points" and "Gaps to work on".
- Base the feedback only on what the candidate actually said.
```
