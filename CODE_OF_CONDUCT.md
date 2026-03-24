# Code of Conduct

> Great question! — ChatGPT, probably

The advent of AI tools has changed how we develop software. Previously, if you wanted to create great 
software, you would have to piece together information from dozens, sometimes hundreds, of internet sources,
the most famous being [Stackoverflow](https://stackoverflow.com/). Using such tools and sharing common
problems online is fundamental for modern programming, and it's hard to argue that this could be considered
plagiarism: a great deal of effort was still required to understand and adapt pieces of code for your own scenario.

AI has changed that. Tools like ChatGPT or Claude can now output senior-like code that usually works, while
abstracting away the complexity of writing code. Meanwhile, learning this complexity, and going from small to big 
problems, is a fundamental skill to be a great software developer. 

This document serves as a guideline for when and how to use AI to help your learning, ensuring that you develop a deep 
understanding of the programming language.

## Key principles

> AI tools are instruments that augment, not replace, critical thinking.

As we will also learn during the course, LLMs are probabilistic models that predict the next token with high accuracy.
But high accuracy is not perfection, and your job is to understand the strengths and weaknesses of models to know
what to trust and what _not_ to trust.

When learning, you should be the one doing the critical thinking and using AI to brainstorm solutions for the problem.

**Best practice:** Use tools with built-in learning features, like setting [Claude's Output styles to "Learning"](
https://code.claude.com/docs/en/output-styles) or [Study mode on ChatGPT](https://openai.com/index/chatgpt-study-mode/). 
They instruct the models to not give you all the answers immediately, but let you figure it out by yourself.

**Best practice**: An emerging best practice among developers is to acknowledge the parts that were assisted 
or fully generated with AI. We do it in commit messages and automated reports to ensure the reader knows what is 
AI generated and what is not.

> Students conduct each step of the coding process methodically and bear responsibility for all code they submit.

It's important to understand the principle of code responsibility, and that even when AI generates the code,
you are still responsible **for code testing and understanding what the code does**.

**Best practice**: Avoid delegating tasks from start to finish, but rather to complete small individual
steps one-by-one and progressing line-by-line, understanding how each part of the code contributes to the final result.
Ask yourself: "Does this make sense? Could it be wrong? What could break this code?"

> AI is a tool, and how you use it matters.

AI is not going away, and learning to use it is a valuable skill. The goal here is not to ban AI, but to cope with a 
world where all the easy answers might be a prompt away, yet choose to figure them out yourself. This is often easier 
said than done, so I compiled a couple of useful guidelines for the usage of AI tools:

✅ **Appropriate Uses:**

- Brainstorming and exploration.
- Specific technical questions, like syntax help and explanation of error messages.
- Repetitive tasks like boilerplate and scaffolding.
- Code review: Asking what you could have done better, after finishing the code by yourself, then applying code
  suggestions. Here, remember to add _"Be critical"_ to your prompts, as AI has the tendency to agree with you.
- Understanding library APIs.

❌ **Inappropriate Uses:**

- Submitting generated code without understanding it.
- Not properly testing AI output. You have to **make mistakes to know what output is wrong**.
- Using AI to bypass the learning goals of an assignment.
- Delegating the whole problem: "Write me a solution to this" without incremental engagement. This is, however, 
something you will do as an experienced developer, once you've learned what the solutions look like.

## What Happens If This Is Violated

> When you can only prompt, you are replaceable.

Submitting code for a graded assignment you did not write yourself is considered **plagiarism.** 
This is stated in your Academic Code of Conduct. This would result in you **failing the assignment**.

Remember that your goal here in this course is to learn. Use AI to **explore** and **verify**, not to **avoid**.

An inexperienced airplane pilot asking ChatGPT which button to press will crash. An experienced pilot using autopilot 
on cruise altitude will arrive safely. The difference is responsibility: you must understand the tool before 
delegating to it.
