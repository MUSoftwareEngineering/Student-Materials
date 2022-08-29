# Software Engineering Exercise 1: Collaborative Development With GIT

## Fun w/ GIT
The general exercise goal here is familiarity with GIT. Just as with any other new technology you are exposed to; the more you use it, the easier
it becomes to use. A secondary goal is to help you develop your problem solving skills through research on the Internet and use of tutorials and
manuals.

Read this entire document before you begin as it will help prevent many issues that will inevitably come up

## This assignment has 2 components that you must accomplish
1.  In your github account create a repository and make sure you know how to pull, push, and make changes.
2.  You will be editing a repository that includes all of the students
    in this class and you will all be working together to create a
    story.

### First part
-   In your account create a new repo
-   In this repo, you will need to clone it so that you can edit it (in whatever software you prefer, though command line will work if you chose to use that)
-   Create a branch
-   In this branch create a file and write something in it
-   Now merge this branch with the master branch in your repository.
-   Take a screenshot of the commit (repo page -\> commits -\> your commit) which you will submit with the files from the second part
-   Now onto the repo you will all be part of....

### Second part
Remember, there are many students that will be contributing to this repository and there should be \~120 branches pushed up to me when this is all said and done.

#### STEP 1 
-   View the repository website. Determine the manner in which you should clone the repository and any necessary step.
-   **<https://github.com/musoftwareengineering/GitMagic>**
-   **WARNING: Downloading a ZIP or TGZ ?   Nope... this means you\'re doing it wrong!**

#### STEP 2
 -   Test that what you pulled down actually compiles\... or do you get to fix someone else's errors?
```
make 
gcc -c story.c
gcc -c sentences/bpbkt7.c
gcc   story.o bpbkt7.o   -o story
make test
```
- You should see this output: 
```
Once upon a time

The end. 
```
- **Make sure you read the story so you can make it better!!!!**
- Consult the great and powerful Google. **Branch** the *master* into a new branch that is the name of your University Pawprint

#### Review the following files that are part of the code:
1.  source code in story.c
2.  Makefile
3.  sentences/bpbkt7.c
4.  sentences/\_HEADERS.h

**Add at least two non-consecutive sentences to the story by completing the following steps:**
1.  create a file in the sentences folder named after your pawprint, it
    - should include at least two different function to calls that each
    - have a single **printf** of a sentence.
    - For example, see the** sentences/bpbkt7.c**
2.  Edit the sentences/\_HEADERS.h file as expected
3.  Edit the story.c file call your sentence in the appropriate spot... **after the previous person's sentence and before the end.**
4.  Modify the Makefile to:
    - Compile your source file into an object file
    - Link your object file into the program
5.  Build, run, confirm

#### STEP 3
1. When you first begin to register activity into the repository, it may ask you who you are: 
***Please tell me who you are.*** 
2. **Run**
``` 
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```
3. to set your account's default identity.
```
Omit --global to set the identity only in this repository.


fatal: unable to auto-detect email address (got 'sgoggins@goggins.(none)')
```
4. Apply common sense to interpret this message
    - Example, I did the following ... you should substitute you:
``` 
    git config --global user.email "gogginss@missouri.edu"
    git config --global user.name "Sean Goggins"
```
5. Consult the great and powerful Google and **pull down an update of
master**
    - Result conflicts? Then fix them
    - Does is build OK?
    - Merge your branch into master
    - Does is build OK?
        - YES: Commit and Push
        - NO: Resolve issues, Commit and Push *master*
6. Switch to your branch and Push

#### STEP 4
-   Do your happy dance

#### STEP 5
1. Document your completion of the exercise
-   Switch to your branch and produce a GIT log using:
```
git log --stat > branch_*pawprint*.log
```
2. Switch to the master branch and produce another log using:
```
    git log --stat > master_*pawprint*.log**
```
3. Zip the two files along with the screenshot from the first part **together**
4. Submit to canvas before due date

 

=============

## Example GIT WORKFLOW
-   `git status`
    - (Are you on your branch?)
-   Make changes
    -   `git add .` (NOTICE the '.') This is shorthand for `git add --all`. It adds all the files that
        - aren't staged, which is NOT ALWAYS the right way to go. But,
        - often it is.
-   `git commit -m "Type your detailed commit message here"`
-   `git push`
-   (Switch back to master: `git checkout master`)
-   `git merge your_branch_name_here`
-   `git push`
-   Notes:
    -   When you hop on for the first time every day to work, checkout
        - the master, pull down any changes with `git pull`. Switch
        - back to your branch and type `git merge master`. Proceed with step 1!
    -   Address any conflicts. You\'ve just merged the master into your branch. Then start with step 1


## Special Instructions for Windows Users
For Windows, you need to be able to compile C for the GitMagic exercise. **Please note that we have limited knowledge of the Windows operating system, and are able to provide more clear assistance with literally every other operating system.**

An apparently simple option is to use this [online C compiler]( https://www.tutorialspoint.com/compile_c_online.php), as recommended by fly_s.y (Shen Yang) in the Slack GitMagic channel. There are screenshots and a hint in the Slack discussion. I was unable to get this to work for me, however.

Otherwise, one compiler you may want to use is [MinGW](http://www.mingw.org/), a native Windows port of the GNU Compiler Collection (GCC).

You can download MinGW here: https://sourceforge.net/projects/mingw/files/
and the install instructions are here: http://www.mingw.org/wiki/Getting_Started .
If you run into problems or have a question, post in the Slack channel for GitMagic.

After installing MinGW, to compile and run:
- Open the cmd window as an administrator (type cmd in the search box, right click on the program icon and choose "Run as administrator").
- Navigate to the GitMagic directory by typing:
  - cd "C:\{Your_path_here}\GitMagic"
- To compile, instead of "make", type: 
    - MinGW32-make
- To run the program and output it to the story text file, type one of the following:
  - story > the_story.txt
  - story.exe > the_story.txt
