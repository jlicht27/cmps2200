# Recitation Test

This is a test lab to make sure we can get the labs to work using github classroom.

1. Accept the github classroom assignment invitation sent via Canvas.
  - be sure to login to github with the ID you gave in the survey
2. Point your browser to your github repository that was created for this assignment (e.g., for **me** this is <https://github.com/tulane-cmps2200/test-lab-amaus>)
  - You will see the starter repository for this "lab". Each lab will have a README with the lab instructions/questions to answer and the starter source code for the lab.
3. [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) the lab to your computer.
4. Implement the `sum_of_squares` function in `main.py`.
  - Confirm that the provided test function `test_one` passes.
5. Add a new test function called `test_two` that gives some other test case and confirm it passes.
6. [Add, commit, and push](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-using-the-command-line/adding-a-file-to-a-repository-using-the-command-line) your completed lab back up to GitHub. 
  - You will need to issue `git add` for all files that you have modified. For this test lab, that should only be `main.py`, but for regular labs, they will also include the README (and possibly other files as well).
  - For example, on the command line, in the same directory as your cloned lab:
```
$ git add main.py
$ git commit -m "Implement Sum of Squares"
$ git push origin main
```
