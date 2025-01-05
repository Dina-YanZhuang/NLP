# Phonetic Clarity & Surprisal
## Overview
This is a small python project to testify the relation between speech information and articulatory clarity. It is said that people tend to articulate more clearly when there is more information included in the speech.  
In this project, you will find two parameters—duration and surprisal—both calculated as the average values at the word level. Duration represents the clarity of articulation for a word—the longer the duration, the clearer the word has been pronounced. On the other hand, surprisal quantifies the unexpectedness of a word in its context. A word with higher surprisal is less predictable and likely carries more informational content.  
## Files
The following data and python files are included in this project:
* Data:
  * **recorded_sentences (folder)**: It contains 10 .txt files of recorded sentences.
  * **sentences_csv (folder)**: It contains 10 recorded sentences processed by [Munich Automatic Segmentation System (MAUS)](https://clarin.phonetik.uni-muenchen.de/BASWebServices/interface/WebMAUSBasic), including the duration information for each phoneme.
  * **wiki.train.raw**: It is a raw data file used to train unigram and bigram dictionaries.
* Python:
  * **get_durations**: It aggregates the phoneme durations from the CSV files, calculates the average duration for each word, and returns a dictionary where each word is a key and its corresponding durations (in milliseconds) are the values.
  * **get_surprisals**: It returns the surprisal values for the words in the recorded sentences.
  * **main**: It aggregates functions in get_durations and get_surprisals and returns a data sheet (**Data.csv**). It takes **wiki.train.raw** and **sentences_csv** as two parameters.
  * **get_linear_model**: It uses a linear model from the Scikit-learn library, with surprisal data as the x-axis and duration as the y-axis. It returns a **LinearModel.png** image along with the model's intercept, coefficient, and R-squared value.
  * **get_histogram**: It generates a histogram with words' duration on the x-axis and their frequencies on the y-axis called **Histogram.png**.
## How to Run the Project
### 1. Clone the Repository  
First, you'll need to clone the project repository to your local machine. If you have a GitHub repository or any other Git-based platform, you can run the following command in your terminal:
```bash
Copy code
git clone <repository_url>
cd <repository_folder>
```
Replace `<repository_url>` with the URL of your repository, and `<repository_directory>` with the project folder name.
### 2. Set Up a Virtual Environment
To avoid dependency conflicts, it’s recommended to set up a virtual environment for this project. You can use `venv` to create an isolated Python environment:
```bash
python3 -m venv venv
```
After creating the virtual environment, activate it with the following command:  
* **For macOS/Linux:**
```bash
source venv/bin/activate
```
* **For Windows:**
```bash
venv\Scripts\activate
```
Your terminal should now show `(venv)` before the command prompt, indicating that the virtual environment is active.
### 3. Install Dependencies
```bash
pip install pandas numpy matplotlib scikit-learn statsmodels
```
### 4. Download the Required Data Files
Download all above-mentioned data files.
### 5. Run the Scripts
The project includes several Python scripts, which should be run in sequence to perform the analysis. Here’s how to run each of them:
#### Step 1: Generate Duration and Surprisal Data
Run the `get_durations.py`, `get_surprisals.py` and `main.py` to obtain durations and surprisals data for each word. Remember to add **wiki.train.raw** and **sentences_csv** as parameters when running `main.py`.
```bash
python3 get_durations.py
```
```bash
python3 get_surprisals.py
```
```bash
python3 main.py wiki.train.raw sentences_csv
```
#### Step 2: Train Linear Model
Run `get_linear_model.py` to perform linear regression and generate a plot for the relationship between word duration and surprisal.
```bash
python3 get_linear_model.py
```
This will output a PNG file (`LinearModel.png`) of the linear regression plot, as well as print regression statistics to the terminal.
#### Step 3: Visualize Data
Run `get_histogram.py` to generate a histogram of word durations.
```bash
python3 get_histogram.py
```
This will create a PNG file (`Histogram.png`) visualizing the frequency distribution of word durations.
### 6. Troubleshooting
If you encounter issues while setting up or running the project, here are some common solutions:  
* Missing Dependencies: Ensure all required libraries are installed with pip install -r requirements.txt or manually with pip install <library_name>.
* File Paths: Make sure all file paths referenced in the code are correct, especially the path to **wiki.train.raw** and **sentences_csv**.  
