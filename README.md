**ECON 484: Machine Learning for Applied Economics (Spring 2026)**

This repository contains the course materials, lecture notes, and projects for ECON 484. In this course, we do not just learn about algorithms. We focus on the Machine Learning (ML) Process as a tool for making real-world decisions.

**Course Philosophy:** "Beyond Model Training." Most courses focus only on training models. In ECON 484, we focus on the entire lifecycle: cleaning messy data, making honest assumptions, and defending our results.

**Note on Syllabus and Slides:** The lecture slides and the syllabus may not match perfectly. This is intentional. The course is dynamic and changes based on current technology and student needs. This repository is the most up-to-date source for the course flow.
Course Structure

The course follows a step-by-step journey through the ML Lifecycle:
1. Strategy and Data Preparation

    Focus: How to represent data correctly.

    Topics: Data collection, cleaning, and managing bias.

    Goal: Understanding that high-quality data is more important than a complex algorithm.

2. Technical Operations

    Focus: How to manage your code like a professional.

    Topics: Version control (Git), using IDEs (PyCharm), and visualizing data with Mosaic or Scatter plots.

    Goal: Making your experiments reproducible and organized.

3. The Discipline of Discovery

    Focus: Scientific honesty.

    Topics: Experiment Ledgers (Lab Notebooks) and Hypothesis Testing.

    Goal: Learning to record every failure and success to find the best solution.

4. Model Decay / Cold Start

    Focus: Lifecycle Management & Reliability.

    Topics: Concept Drift (the world changes), Data Drift (the input changes), and the "Boiling Frog" problem. Introduction to Cold Start problems in new environments. 

    Goal: Understanding that models are living systems that "expire," and learning how to diagnose when a model is no longer safe to use.

5. Decision Defense / Model Ethics

    Focus: Professional Accountability.

    Topics: Model Interpretation, Business Metric alignment, Bias detection, and the "Manager’s Questions." 

    Goal: Translating mathematical output into defensible business strategies. Moving from "It works" to "It is safe."


Additional topics will be added over time. 

**Applied Projects and Code Examples**

The course repo includes Python projects to demonstrate. Each folder contains a project and a specific explanation of the code.
1. Data Visualization

    Focus: Pre-modeling Sanity Checks.

    Topics: Mosaic plots, Scatter plots, and Box plots for analyzing feature relationships.

    Goal: Learning to "see" the data distribution to catch errors before the model does.

2. Experiment Ledgers

    Focus: Immutable Record Keeping.

    Topics: Linking Git commits to Excel results, Hypothesis logging, and parameter tracking. 

    Goal: Creating a "paper trail" that proves exactly how a result was achieved.

3. Simulated Decay 

    Focus: Stress Testing & Fragility.

    Topics:  Injecting noise, simulating sensor failure, and observing the collapse of model performance. 

    Goal: Experiencing the "Garbage In, Garbage Out" reality firsthand in a controlled environment.

4. Drift Monitoring

    Focus: Operational Safety.

    Topics: Statistical tests for distribution shifts and automated threshold alerts.

    Goal: Building an automated "watchdog" system to detect when a model needs retraining.

You can browse the repo, but descriptions will be added over time. 

**Homework Assignments** 

There will be four homework assignments which have to be submitted individually. 
- **HW Assignment 1** (Core Python & Github) - Download and execute the given code (simple estimation), create and save plots. Write a very simple reports and upload on Github. 
- **HW Assignment 2** (Work with Ledger) - Run a very simple clustering model using a ledger. Experiment with Silhouette scores. Write a simple report and upload all on Github. 
- **HW Assignment 3** (Model Fragility aka Garbage In, Garbage Out) - Train an estimation algorithm based on sensor inputs. Run on test data. Modify the test data to simulate problems (noise, sensor errors, etc). Run again on the modified test data. Write a comparison report and upload all on Github. 
- **HW Assignment 4** (Observability) - Develop a monitoring solution that creates a warning message once the decay becomes serious. The solution uses the experiment ledger output as its input. As this is a student homework the monitoring solution is not expected to be real time. 

These assignment deserve a short discussion:
- Assignment 1 focuses on "Infrastructure". Can the students set up the environment? Can they use Git? This removes the "I couldn't get Python to work" excuses early.
- Assignment 2 focuses on "Traceability". By using Clustering here, we bypass the complexity of Train/Test splits and target variables. Students only have "Inputs" and "Results" (e.g., Inertia/Silhouette). This forces them to focus purely on the mechanics of the Ledger without getting bogged down in validation logic.
- Assignment 3 focuses on "Fragility". The idea here is to simulate decay and learn from it.
- Assignment 4 focuses on "Observability". This is the logical response to the prior assignment: "My model broke (HW3), so now I need a system to watch it (HW4)."

**Scientific Integrity & Unique Results**

To ensure every student engages with the material individually and experiences the "messiness" of real data, we enforce strict reproducibility rules: 
- **Unique Seeds**: You must use your Student ID as the random seed in your code (instead of the default 42). This ensures your train/test splits are unique to you.
- **Assigned Datasets**: You may be assigned specific subsets of data. This means your errors and your results will be unique, making copying impossible.
- **Use of LLMs**: Students are allowed and encouraged to use LLMs (ie. ChatGPT, Gemini, Claude). But they are also required to commit their "Prompt History" as a markdown file. If no such file is committed to their repo, then they are assumed to have claimed no AI use.  

**Tools and Guidelines**
- **GitHub**: All assignments and projects must be uploaded here. Mastering version control is required.
- **IDE**: I recommend using JetBrains PyCharm (Student License is free). You can also use VS Code.
- **AI Policy**: You are encouraged to use LLMs (like ChatGPT or Gemini) for writing code. However, you are the "Lead Architect." You must understand and explain every line of code the AI generates.

**Note for Students: The "Decision Defense"**

In the final project, we do not only look at your "Accuracy Score." You must defend your decisions. You need to explain:
- Why did you choose this data?
- What did you learn from your failures?
- Is your model safe for a real business decision?
