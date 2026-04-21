# HW Assignment 1: Infrastructure, Environment, and The Discipline of Discovery

## Overview
This assignment marks your transition from a consumer of information to a practitioner in the Data Lab. In the professional world, Machine Learning (ML) is not just about writing an algorithm; it is about managing a complex lifecycle of tools, data, and documentation. 

This task is intentionally simple in its mathematical scope but intensive in its technical requirements. You will set up your professional infrastructure, establish a reproducible environment, and practice the "Discipline of Discovery"—recording your experiments systematically so that your results can be defended and reproduced by others.

---

## Step 0: Infrastructure & Environment Setup
You must establish your professional presence and local development environment before writing any code.

### 1. Platform Memberships (GitHub & Kaggle)
* **Account Creation:** Create accounts on [GitHub](https://github.com) and [Kaggle](https://kaggle.com).
* **Professional Identity:** Choose a "sensemaking" username (e.g., `firstname-lastname`). These handles will follow you throughout your professional life. Avoid casual or cryptic pseudonyms so your instructor and future employers can identify your work easily.
* **Account Longevity:** Add a secondary backup email to your security settings. These accounts will remain valuable assets long after you graduate.

### 2. Python Environment (The IDE)
* **JetBrains Toolbox:** Download and install the [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/). This is the standard way to manage professional development tools.
* **PyCharm Professional:** Use the Toolbox to install **PyCharm Professional**. 
* **Licensing:** Create a JetBrains account using your university email address to claim your free Professional Student License. This version includes essential data science features that are necessary for this course.

---

## Your Tasks

### 1. Research and "AI-Assisted Discovery"
Navigate to the [Avocado Prices Dataset](https://www.kaggle.com/datasets/neuromusic/avocado-prices) on Kaggle. 
* Explore the **"Code"** tab to see how other users have handled this data. 
* Choose a solution that looks clear and use an AI tool (like Gemini) to explain it. Ask the AI: *"How is this code structured? What libraries are used and what does each do?"*
* You are the **Lead Architect**. You may use AI to explore, but you must understand every line of code you eventually implement.

### 2. Execution & Commenting
Write a Python script to perform the following:
* **Load:** Import the dataset using the `pandas` library.
* **Experiment:** Perform at least **five (5) experiments**. Each experiment involves selecting a specific combination of a City (Region) and a Type (Organic or Conventional).
* **Visualize:** For each experiment, generate a line plot showing price fluctuations over time.
* **Code Documentation:** Comment your code thoroughly. For a beginner, there is no such thing as "too many comments." Explain what each block of code is doing in plain language. Over-commenting is encouraged.

### 3. The Experiment Ledger (CSV)
Maintain a separate file named `ledger.csv`. This acts as your Lab Notebook. It must contain 5 rows (one for each experiment) with these columns:
* `Experiment_ID`: A unique ID (e.g., EXP-001).
* `Region`: The chosen city.
* `Type`: Organic or Conventional.
* `Avg_Price`: The mean price for that specific subset.
* `Plot_Filename`: The name of the saved plot (e.g., `plot-EXP-001.png`).

### 4. AI Prompt History (Markdown)
You are required to submit your AI prompts as a Markdown (`.md`) file named `prompts.md`. 
* If you have never created a Markdown file, ask your AI: *"Convert my prompt history for this assignment into a clean Markdown format for GitHub."* * This file provides transparency into how you used AI to solve problems, explain code, or fix errors.

### 5. Technical Report
Write a report (saved as `REPORT.md`) that includes:
* **User Profiles:** Links to your GitHub and Kaggle profiles.
* **Problem Statement:** A brief description of the Avocado dataset and your tasks.
* **Technical Structure:** An explanation of your code structure (e.g., functions, pandas dataframe objects).
* **Visual Evidence:** Embed at least one generated plot and a screenshot of your working environment (PyCharm IDE showing your code).
* **Self-Assessment:** A conclusion on what you learned and how the AI helped or hindered your learning.

### 6. Kaggle Submission (Visibility)
Upload your finalized code and the ledger to Kaggle as a "New Notebook" attached to the Avocado Prices dataset.
* **Why:** This builds your public portfolio. Future employers often look at Kaggle activity to assess a candidate's technical communication and consistency.

---

## Submission Checklist
1. [ ] **GitHub Repository:** A private repository named `ECON484-HW1`.
2. [ ] **Code:** Your commented `.py` or `.ipynb` file.
3. [ ] **The Ledger:** `ledger.csv` with 5 experiment records.
4. [ ] **Plots:** Five image files named according to the Ledger.
5. [ ] **Prompt History:** `prompts.md` documenting your AI usage.
6. [ ] **Report:** `REPORT.md` with profile links, plot, and IDE screenshot.
7. [ ] **Kaggle Link:** Your public Kaggle notebook link included in the report.

---

## Pro-Tips for Success

### The Importance of Atomic Commits
Do not wait until the end to upload to GitHub. Use **Atomic Commits**: upload your work every time you complete a small task (e.g., "Added pandas import" or "First plot generated"). This protects your work and provides a clear audit trail of your progress.

### IDE Integration
PyCharm is designed to help you. If you copy a code snippet and see red underlines, hover over them. PyCharm will suggest a fix (like "Install package"). Use these built-in tools to manage your library dependencies.

### Optimizing AI Prompts
When asking an AI for help, the more context you provide, the better the answer. Use a prompt like:
> *"I am a student using **PyCharm Professional** for ECON 484. I am working on the **Avocado Prices** dataset and I need to filter for 'Boston' and 'Organic'. Here is my code so far... can you help me fix this error?"*
