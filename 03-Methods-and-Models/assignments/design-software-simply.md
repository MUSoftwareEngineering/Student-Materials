# Model and Modify Simple Software
1. Fork this simple piece of [software from here](https://github.com/angrynarwhal/lottery), into your own GitHub repository. You will notice it is a simple program for estimating lottery numbers based on their a priori occurrence. 
_From the "README.md": "The lottery is in the opinion of this developer, a game for people who are bad at math. That doesn't mean it can't be a little fun to question the randomness of a process involving physical ping pong balls getting flopped around an airflow machine, right?"_
2. Create a python3.x virtual environment by using the `python3 -m venv <path to venv>` command. 
3. Activate your virtual environment using `source <path to venv>/bin/activate`
4. Run `megamillions-from-apriori.py` : It is supposed to be executable, so if your python environment is activated, it should just run. Sometimes I have to use `./megamillions-from-apriori.py` in order to get it to run. 
You should see output like this: 
```bash
Number 31: Probability = 2.019048
Number 10: Probability = 1.971429
Number 20: Probability = 1.971429
Number 14: Probability = 1.961905
```
for every historical number. 
5. Observe how the README.md file explains how it works at the bottom, paying special attention to the fact that balls 57-75 have only existed for a portion of the time the Megamillions lottery has existed. 
6. Examine the historical source files to understand when numbers 57-75 started getting used. They are in .csv, .xlsx, and .numbers format. All the data is the same. 
7. Using whatever means are comfortable for you, which can include pseudocode, a pencil sketch, or an online tools, design a change to `megamillions-from-apriori.py` that would normalize the historical averages to account for the more recent introduction of balls 57-75. **add this design and any related information to a directory you create in your fork, named by creating some kind of random letter sequence derived from your pawprint**. 
- Add the directory, for me it could be `kstg4` for example. 
- **Add a file with your design in whatever format you created it in to this directory** 
8. Make a copy of `megamillions-from-apriori.py` in your `kstg4` or other (other, please) new directory derived from your pawprint. 
9. Recognize you will have to modify the path to the source data in the program copy. 
10. Using pseudocode, or actual python, modify the program to implement your revised design from step 7. 
11. **create a pull request** for your changes back to the original repository. 
12. **submit a link to your modified fork** in the Canvas assignment. 