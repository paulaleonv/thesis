# thesis

## instructions

open iterm2 and go to the thesis folder

```bash
cd github/thesis
```
a folder with git, is a repository. it works as a normal folder.

git is a version control system, perfect for coding.

you have your repo both on your computer, and in github.

## further configuration of github

create a gitignore, to ignore .DS_Store, and env/

it is already done on my machine.

```bash
touch .gitignore
```


## installation of python

first install a virtualenv, this is done once, i already did it on my machine

```bash
virtualenv env
```

to activate the virtualenv, this

```bash
source env/bin/activate
```

after you run it, on the terminal, each line now starts with (env)

to quit the environment, run this

```bash
deactivate
```

## workflow

after doing cd, and being on the folder, work on your thesis, save changes.

when you are ready to save these changes on the repo, we have to do a commit.

we will use three commands on the terminal:

1. stage the commit, we tell the repo to include all the files that changed to the commit. the parameter -A means "all".

```bash
git add -A
```

2. do the actual commit. replace comment with a meaningful comment on what you changed.

```bash
git commit -m "comment"
```
now your repo has a new commit, but your github has no idea. the next command uploads your commmit to the cloud.

```bash
git push
```

when you want to run python scripts, first activate your environment

```bash
source env/bin/activate
```

run your python scripts, and then to stop working, deactivate the environment

```bash
deactivate
```
