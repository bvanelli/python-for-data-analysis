import streamlit as st
import reveal_slides as rs


st.set_page_config(
    page_title="CES Python Programming - Fundamentals (2,5 ECTS)", page_icon="🐍", initial_sidebar_state="collapsed"
)


def fragment(i: int) -> str:
    return f'<!-- .element: class="fragment" data-fragment-index="{i}" -->'


slides_intro = f"""
### **CES Python Programming - Fundamentals (2,5 ECTS)**

[github.com/bvanelli/python-for-data-analysis](https://github.com/bvanelli/python-for-data-analysis/)

---
### 🎯What do we want to learn?

* Fundamentals of Python and its data types
* Python programming logic, conditional, loops, functions, and Python objects
* Data analysis packages Numpy and Pandas
* Plotting packages like Matplotlib
* Basic Statistics
* Time series data
* Modules and classes
* Git and GitHub
* Clean coding
* AI-assisted programming
"""
i_title = 0
i_agenda = 1
i_last = i_agenda

slides_tutor = f"""
---
# 📚 **The tutor**
--
### Brunno Vanelli

- Graduated in Control and automation engineering
- 6 years of experience in Python development
- Working at plus10 with data acquisition and real-time transformation for our cloud services
- Ample experience in design of data pipelines with PostgresSQL databases for data analytics
- Open-source enthusiast on my free time
- 🏃 I also like running {fragment(0)}
"""

slides_why = f"""
---
# 🐍 **Why learn Python?**

Source: [State of Python 2025](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/) and
[Developer Ecosystem Survey 2024](https://www.jetbrains.com/lp/devecosystem-2024/),
both done by Jetbrains
--
Data science is now over half of all Python: 

"This year, **51%** of all surveyed Python developers are involved in data exploration and processing"
--
In 2024, **57%** of developers have used Python for Programming, scripting, and markup, being the second most used 
language overall. 

As a comparison, this number was **37%** in 2017. 

Part of the reason for the adoption is: ease of use, speed of implementation, wide ecosystem, and extensive documentation.
--
(if you are wondering how vast the ecosystem is, I created these slides using Python.)
"""

slides_classes = f"""
---
# 🎒 **Classes**
--

### Material

- Full material available on my Github [bvanelli/python-for-data-analysis/](https://github.com/bvanelli/python-for-data-analysis/)
- Announcements are made on the [Ilias page](https://elearning.hs-albsig.de/ilias.php?baseClass=ilrepositorygui&ref_id=507956)
- You can also write questions directly on the dedicated Teams channel (link on the Ilias page) 
or via email (brunno.vanelli@hs-albsig.de)

--
### Classes

Weekly on Wednesday - from 14:00 to 15:30

- Each of the double classes are divided equally into lecture and practical session
    - The lecture will introduce the day’s topic.
    - The practical part will exercise what has been learned during the lecture
    - An optional assignment will accompany each class to dive deeper into the material
- Each lesson will have optional reading material from the textbook and online resources
- All material is delivered via Jupyter notebooks, which are often used for data exploration tasks

--
### Hybrid class format

- Classes will be done in person once a month - it will be communicated beforehand
- For all the other classes, you can find the invitation for the online class on the Ilias page

--
### Learning goals

- The classes will contain real-world datasets: the goal is to develop the skills to manipulate and extract useful 
information from the data as if they were real-world datasets.
- The final assignment also will be aligned with the goals above. The final assignment description and datasets will be
delivered until the Winter break in December.
- The goal of the assignments is to exercises the commands, but also to **understand what to use and when**.
"""

slides_philosophy = f"""
---
# 🤔 **Course philosophy**

--
**You learn Python by doing, just like anything else**. With a few exceptions, you're not going to break your computer by
trying new commands. So try it and see what happens. Print output of commands. Print values of variables. Kick
the thing until it works.
--
Resist the urge to get frustrated and blame the computer when your code doesn't run. Computers are deterministic
machines; **it's almost always your fault**. But that's OK! Your computer will give you error messages that describe what
went wrong. Read them and try to understand them.
--
When you don't know how to do something, **google it**. You'll be amazed by the solutions you'll find to do thing x if
you google "python thing x". StackOverflow will often have high-quality answers to your problem.
--
Resist the urge of using AI tools to do all the job or answer all your questions: doing so will often prevent you
from learning from your mistakes. Remember that _"the master has failed more times than the beginner has tried"_.
There will be a class where you will learn how to use AI tools to help you in your programming.
--
Remember Zed's sage wisdom:

* Practice every day.
* Don't overdo it. Slow and steady wins the race.
* It's alright to be totally lost at first.
* When you get stuck, get more information.
* Try to solve it yourself first.
"""

slides_feedback = f"""
---
# 🧐 **Feedback**
--
Each one of you is invited to fill in the feedback form at the Ilias page. That is a basic evaluation of your 
**existing knowledge in programming languages**.
--
At any given time, there is also a Google form to give feedback on the class available at the README of the Github 
repository. You can use the form to give feedback of your perception of the lecture.

You may also provide this feedback **multiple times** during the semester.
"""

slides_thanks = f"""
---
# 🙏 **Thank you**

## 🙋 **Any questions?**

(now we can start) {fragment(0)}

<img style="height: 100%" src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjQxaHk0cnE0NGlrdzN1MXJvcXhxbmc0ZXFsbnVidGZmanN2MnpneSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LDBuYzAwu8L4I/giphy.gif"> {fragment(0)}
"""
ih_thanks = i_last + 1

slides_markdown = (
    slides_intro
    + slides_tutor
    + slides_why
    + slides_classes
    + slides_philosophy
    + slides_feedback
    + slides_thanks
)


# change this while developing to start in the appropriate place
indexh = 0
indexv = 0
indexf = 0


def app():
    with st.sidebar:
        st.subheader("Slides component parameters")
        theme_default = "dracula"
        theme_options = [
            "black",
            "black-contrast",
            "blood",
            "dracula",
            "moon",
            "white",
            "white-contrast",
            "league",
            "beige",
            "sky",
            "night",
            "serif",
            "simple",
            "solarized",
        ]
        theme = st.selectbox(
            "Theme", theme_options, index=theme_options.index(theme_default)
        )

        transition = st.selectbox(
            "Transition", ["slide", "convex", "concave", "zoom", "none"]
        )

        # height = st.number_input("Height", value=500)
        height = 500
        # content_height = st.number_input("Content Height", value=900)
        content_height = 900
        # content_width = st.number_input("Content Width", value=900)
        content_width = 900
        # scale_range = st.slider("Scale Range", min_value=0.0, max_value=5.0, value=[0.1, 3.0], step=0.1)
        scale_range = [0.1, 3.0]
        # margin = st.slider("Margin", min_value=0.0, max_value=0.8, value=0.1, step=0.05)
        margin = 0.1
        # plugins = st.multiselect("Plugins", ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
        plugins = ["highlight", "katex"]

    currState = rs.slides(
        slides_markdown,
        height=height,
        theme=theme,
        config={
            "transition": transition,
            "width": content_width,
            "height": content_height,
            "minScale": scale_range[0],
            "center": True,
            "maxScale": scale_range[1],
            "margin": margin,
            "plugins": plugins,
        },
        initial_state={
            "indexh": indexh,
            "indexv": indexv,
            "indexf": indexf,
        },
        markdown_props={"data-separator-vertical": "^--$"},
        key="foo",  # what is this about?
    )

    if currState["indexh"] == i_title:
        # todo add link (also to reveal?)
        st.markdown(
            "Slides made with [streamlit-reveal-slides](https://github.com/bouzidanas/streamlit-reveal-slides).  \n"
            "See sidebar for changing `theme` and `transition`."
        )
        st.markdown("Press `F` for full screen, `Esc` to exit full screen.")


if __name__ == "__main__":
    app()