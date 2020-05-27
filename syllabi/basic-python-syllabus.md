# Python basics

## Motivation

I want to be fluent in carrying out basic Python data tasks and want to understand the key concepts (e.g. APIs, philosophies) that underlie the tools I
use for this purpose.

In particular, I want to build fluency in:

- Writing Pythonic code
- Pandas
- Data visualisation in Matplotlib, Seaborn, and Altair
- Object oriented programming
- Functional programming
- Testing

I then want to move on to causal analysis and, after that, machine learning:

- Basic statistics in Python
- Causal analysis in Python
- Scikit-learn


## Goal

Explore mdb data for PhD in best-practice fashion and master basic Pandas operations such that I do to the data whatever I want without having to google much and without producing errors.


## Timeline

The goal is to get through the end of the Pandas syllabus below by the end of February, and then move on to further topics in March. In mid Feb, I'll start reflecting on progress so far and start develop the new curriculum.


## Learning approach

To explore and get familiar with the data I use for my PhD I'll try explore everything in the syllabus directly in the notebook I use for working with this data.


## Timeline update 22 March 2020

I'm still working on becoming fluent in Pandas. The delay is partially because there were days when I focused on the PhD
exclusively, and the past week I was unable to work due to the coronavirus. I want to finish the Pandas basics by the end of March, and then move on to machine learning (in case I keep pursuing the machine-learned time-preference idea).


## Syllabus

Python basics and writing Pythonic code (w6 and w7)
- [Stanford CS41](https://stanfordpython.com) (lectures up to Python and the Web and all extra readings)
- [CS41 idiomatic Python](https://drive.google.com/file/d/0B-eHIhYpHrGDNGZCYUN6SVB1OGc/view)

IPython (w8)
- [BIDS bootcamp: IPython notebook use](https://www.youtube.com/watch?v=HrylK8I1ALs&index=3&list=PLKW2Azk23ZtSeBcvJi0JnL7PapedOvwz9)
- [IPython tips and tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
- IPython-Notebook-Shortcuts (on disk)
- Scientific workflow (BIDS part 12)

Numpy (w9)
- Numpy in pythonfordataanalysis (pfda)

Week 10
- PFDA Chap. 5, getting started with Pandas
- PFDA Chap. 6, importing data
- PFDA Chap. 7, data cleaning and preparation
- PFDA Chap. 8, data wrangling
- PFDA Chap. 10, data aggregation and group operations
- PFDA Chap. 11, time series
- [Dplyr/pandas vignette comparison](https://nbviewer.jupyter.org/gist/TomAugspurger/6e052140eaa5fdb6e8c0)

Week 11
- PFDA Chap. 10, data aggregation and group operations
- PFDA Chap. 12, advanced pandas
- PFDA Chap. 13, intro to modeling libraries
- PFDA Chap. 14, data analysis examples
- PFDA App. A, advanced numpy
- PFDA App. B, more iPython
- [Pandas videos](https://github.com/justmarkham/pandas-videos): watch tricks, changes, more tricks, best practice

Week 12
- PFDA Chap. 14, data analysis examples
- PFDA App. A, advanced numpy
- PFDA App. B, more iPython
- [Pandas videos](https://github.com/justmarkham/pandas-videos): watch tricks, changes, more tricks, best practice

Week 13
- PFDA Chap. 14, data analysis examples
- PFDA App. A, advanced numpy
- PFDA App. B, more iPython
- PFDA Chap. 9, data visualisation
- PFDA reread key sections
- [Pandas videos](https://github.com/justmarkham/pandas-videos): answer each question on my own before checking in pythonfordatascience and video (use this to review concepts)
- [Modern Pandas](https://tomaugspurger.github.io/modern-1-intro)

Week 14
- Relax and patch and plan next learning cycle


Week 14
- For machine learning, use jvdp data science handbook
- Key libraries intro
- Statsmodels
- Scipy
- Scikit-learn

Week 15
- Easter holiday in Sicily




Software engineering basics (version control, unit testing)

Code style revision and in depth python understanding
- fluent-python (on disk) chapter 1
- [Python tricks](https://github.com/sahands/python-by-example/blob/master/python-by-example.rst)
- [Nate Batchelder: loop like a native](https://www.youtube.com/watch?time_continue=14&v=EnSu9hHGq5o)
- [Jeff Knupp: Python's execution mode](https://www.jeffknupp.com/blog/2013/02/14/drastically-improve-your-python-understanding-pythons-execution-model/)
- Jeff Knupp's idiomatic python

# Further topics:
- Replicate jvdp posts
- Tidy Tuesday
- Data visualisation
- Object oriented programming
- Functional programming
Testing
- pytest unit test runner for ipython nbs
- And then causal analysis, stats, and machine learning.


## Log

Week 13:
- PFDA Chap. 14, data analysis examples (first three and extra work)

Week 12:
- Coronavirus moving and re-adjustment

Week 11:
- PFDA Chap. 10, data aggregation and group operations
- PFDA Chap. 12, advanced pandas
- PFDA Chap. 13, intro to modeling libraries

Week 10:
- PFDA Chap. 5, getting started with Pandas
- PFDA Chap. 6, importing data
- PFDA Chap. 7, data cleaning and preparation
- PFDA Chap. 8, data wrangling
- PFDA Chap. 11, time series
- [Dplyr/pandas vignette comparison](https://nbviewer.jupyter.org/gist/TomAugspurger/6e052140eaa5fdb6e8c0)

Week 9
- First tidy Tuesday challenge (I spend an hour with the data myself and then compare my approach to David Robinson's, and then learn how to do what like best about his approach in Python).
- Reading numpy chapter in pfda

Week 8:
- [BIDS bootcamp: IPython notebook use](https://www.youtube.com/watch?v=HrylK8I1ALs&index=3&list=PLKW2Azk23ZtSeBcvJi0JnL7PapedOvwz9)
- [IPython tips and tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

Week 7:
- [Stanford CS41](https://stanfordpython.com) (lectures up to Python and the Web, and all extra readings)
- [CS41 idiomatic Python](https://drive.google.com/file/d/0B-eHIhYpHrGDNGZCYUN6SVB1OGc/view)

Week 6:
- Completed CS41 up to functional programming (incl. lab sessions)
- Decided to move working through composingprogrammes.com to a separate project.




# Workflow

Create environment

conda create -n python=3.7 matplotlib pandas scikit-learn seaborn


Set up project folder



