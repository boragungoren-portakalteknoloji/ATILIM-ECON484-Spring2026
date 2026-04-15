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

    Focus: --

    Topics: -- 

    Goal: --

5. Decision Defense / Model Ethics

    Focus: --

    Topics: -- 

    Goal: --


Additional topics will be added over time. 

**Applied Projects and Code Examples**

The course repo includes Python projects to demonstrate. Each folder contains a project and a specific explanation of the code.
1. Data Visualization

    Focus: --

    Topics: -- 

    Goal: --

2. Experiment Ledgers

    Focus: --

    Topics: -- 

    Goal: --

3. Simulated Decay 

    Focus: --

    Topics: -- 

    Goal: --

4. Drift Monitoring

    Focus: --

    Topics: -- 

    Goal: --

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

As these assignments are individual and highly digitized we take some precautions against cheating. For individual execution; students have to:
- Use their **student ID as seed** in their homeworks rather than the default "42" in sample code
- Use **assigned datasets** so that the issues they face may be different



**Tools and Guidelines**
- GitHub: All assignments and projects must be uploaded here. Mastering version control is required.
- IDE: I recommend using JetBrains PyCharm (Student License is free). You can also use VS Code.
- AI Policy: You are encouraged to use LLMs (like ChatGPT or Gemini) for writing code. However, you are the "Lead Architect." You must understand and explain every line of code the AI generates.

**Note for Students: The "Decision Defense"**

In the final project, we do not only look at your "Accuracy Score." You must defend your decisions. You need to explain:
- Why did you choose this data?
- What did you learn from your failures?
- Is your model safe for a real business decision?
