# Assignment 0 - Python/Git/Jupyter/Gradescope

This assignment is designed to help you get comfortable with your local python environment and Git, introduce you to jupyter notebooks and provide a refresher on the python language. After following this you will proceed with learning about jupyter notebooks in the `notebook.ipynb` (where you will make your first graded submission!). Let's get started!

If you have not setup your Python environment, STOP and complete the environment setup at https://github.gatech.edu/omscs6601/env_setup. Then return here.

### Table of Contents
- [Get repository](#repo)
- [Packages](#pkg)
- [Jupyter](#jupyter)
- [Summary](#summary)

<a name="repo"/></a>
## Setup a local repository
Georgia Tech uses github and you have the ability to build a repository to store your assignments at (https://github.gatech.edu/gatech_id) </br>
[Georgia Techs Github](https://github.gatech.edu/)</br>
[Help on GitHub](https://docs.github.com/en/get-started/quickstart)</br>

First things first, let's pull this repository to your local machine:

```
git clone https://github.gatech.edu/omscs6601/assignment_0.git
```

NOTE: For the rest of your assignments you will be assigned a private repository for each assignment. Beginning with assignment 1 you must upload
your completed assignment to that repository. You may still use a gatech repository as outlined in this assignment, however it does not 
satisfy the requirement for storing your completed assignments in the private assigned assignment repository. 

<a name="fork-instructions"/></a>
## Instructions to create a private forked repository for assignments

The assignments you will be working on throughout this semester will potentially require multiple revisions. A good way to track these revisions is by using your own private repo to backup your assignments at various stages of completion. Please remember that your assignment repository should be private and only accessible to yourself so that you do not accidentally violate the OSI policy.<br>

You can use the following steps to create a private repository for assignment 0. Please replace the A0 url with the future assignments' URL to repeat this for the future assignments.<br>

* Login to github.gatech.edu and create a private repo named : YOUR_REPO. Double check that the repo is private, otherwise you may violate the OSI policy

* Get the class repo<br> ``git clone --bare https://github.gatech.edu/omscs6601/assignment_0.git``

* Mirror this to your private repo <br>
```
cd assignment_0.git
git push --mirror https://github.gatech.edu/your_gatech_id/YOUR_REPO
```

* You can now delete the ``assignment_0.git`` directory cloned two steps ago if you wish.

* Now clone your private repo on your local system<br> ``git clone https://github.gatech.edu/your_gatech_id/YOUR_REPO``

* Next <br>
```
cd YOUR_REPO
git remote add upstream https://github.gatech.edu/omscs6601/assignment_0.git
```
You check if the remote branch has been added using ``git remote -v``

* Now you can use it like this <br>
```
git pull upstream master # the original repo 
git push origin master # your repo 
```
If you do not specify the remote, it will default to the origin (your repo)

* If you are scared of pushing to upstream you can disable pushing to upstream using<br> ``git remote set-url --push upstream PUSH_DISABLED``

> **Note:** If you are on Windows, students in the past have commonly reported an error during package installation that resembles the error in this [Github post](https://github.com/pytorch/pytorch/issues/34798). To fix this issue, head over to the [PyTorch site](https://pytorch.org) and follow the instructions to install torch manually in `ai_env`. If this does not work, you may also instead try running `conda install -c ankurankan pgmpy=0.1.10`. After trying one of the previous suggestions and getting a successful install, try `pip install -r requirements.txt` again.


<a name="pkg"/></a>
## Packages

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

We will be using multiple python packages throughout this class. Here are some of them:

* **jupyter** - interactive notebook (you will learn more about them soon)
* **numpy** - a package for scientific computing (multi-dimensional array manipulation)
* **matplotlib** - a plotting library
* **networkx** - a package for manipulating networks/graphs
* **pandas** - a package for data analysis
* **pgmpy** - library for probabilistic graphical models 

You can see the complete list of packages and required versions in [./requirements.txt](./requirements.txt).

We can install all these packages using command ``pip install -r requirements.txt``. Please navigate to the `assignment_0/` directory, activate your environment (`conda activate ai_env`), then run:

```
pip install -r requirements.txt
```

Once installed, you can run `pip freeze` to see the list of all of the packages installed in your `ai_env` environment.

> **Note:** If you are on Windows, students in the past have commonly reported an error during package installation that resembles the error in this [Github post](https://github.com/pytorch/pytorch/issues/34798). To fix this issue, head over to the [PyTorch site](https://pytorch.org) and follow the instructions to install torch manually in `ai_env`. If this does not work, you may also instead try running `conda install -c ankurankan pgmpy=0.1.10`. After trying one of the previous suggestions and getting a successful install, try `pip install -r requirements.txt` again.


<a name="jupyter"/></a>
## Jupyter

![Jupyter Logo](https://jupyter.org/assets/nav_logo.svg)

Now that you have set up the environment it's time to learn more about the jupyter notebooks. 

We have already installed jupyter. To open it up you can run:

```
jupyter notebook
```

It will start a python kernel which you can access via [https://localhost:8888](https://localhost:8888/) in your browser. For the rest of the assignment proceed to `notebook.ipynb`.

<a name="summary"/></a>
## Summary

You have now installed conda package and environment manager, created a python environment and installed all the necessary packages.

Please always remember to run:
```
conda activate ai_env
```
to activate your environment before you start working on your assignments.
