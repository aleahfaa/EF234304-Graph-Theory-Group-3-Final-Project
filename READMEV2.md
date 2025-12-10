<div align="center">
    <h1>Graph Theory - EF234304 (2025)</h1>
</div>

<p align="center">
  <b>Institut Teknologi Sepuluh Nopember</b><br>
  Sepuluh Nopember Institute of Technology
</p>

<p align="center">
  <img src="assets/Badge_ITS.png" width="50%">
</p>
  
<p align="justify">Source code to <a href="https://www.its.ac.id/informatika/wp-content/uploads/sites/44/2023/11/Module-Handbook-Bachelor-of-Informatics-Program-ITS.pdf">Graph Theory (EF234304)</a>'s final project named <b>Course Scheduling Optimization Using Graph Coloring</b>. All solutions were created by <a href="https://github.com/aleahfaa">Iffa Amalia Sabrina</a>, <a href="https://github.com/bellaacp">Bella Angeline Chong Puteri</a>, <a href="https://github.com/zan4yov">Razan Widya Reswara</a>, and <a href="https://github.com/DocHudson45">Muhammad Dzaky Radithya Ryrdi</a>.</p>

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NetworkX](https://img.shields.io/badge/NetworkX-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

</div>

<br>

<div align="center">
  <table>
    <thead>
      <tr>
        <th align="center">NRP</th>
        <th align="center">Name</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td align="justify">5025221077</td>
        <td align="justify">Iffa Amalia Sabrina</td>
      </tr>
      <tr>
        <td align="justify">5025231073</td>
        <td align="justify">Bella Angeline Chong Puteri</td>
      </tr>
      <tr>
        <td align="justify">5025241004</td>
        <td align="justify">Razan Widya Reswara</td>
      </tr>
      <tr>
        <td align="justify">5025241010</td>
        <td align="justify">Muhammad Dzaky Radithya Ryrdi</td>
      </tr>
    </tbody>
  </table>
</div>

<p align="center">On behalf of: <b>Ilham Gurat Adillion, S.Kom., M.Kom.</b></p>

<hr>

## Table of Contents
- [Introduction](#introduction)
- [New Features](#new-features)
  - [Graph Visualization](#graph-visualization)
  - [Performance Benchmarking](#performance-benchmarking)
  - [Robustness & Stress Testing](#robustness--stress-testing)
- [Prerequisites & Installation](#prerequisites--installation)
- [How to Run](#how-to-run)
- [Graph Theory Application](#graph-theory-application)
- [Theoretical Insight](#theoretical-insight)
- [Flowchart](#flowchart)
- [Input-Output](#input---output)

## Introduction
Creating a class schedule can be difficult when multiple courses overlap in time. To address this, we use Graph Theory to model the time conflicts between courses and generate a schedule that ensures no overlapping classes occur using **Welsh-Powell** and **DSatur** algorithms.

## New Features
### Graph Visualization
Both scheduling scripts (`schedule_fp.py` and `dsatur-fp.py`) now include a built-in visualization feature using **NetworkX** and **Matplotlib**. After generating the schedule, a popup window displays the conflict graph with nodes colored according to their assigned time slots.

### Performance Benchmarking
A new script `compare_algorithms.py` provides a side-by-side comparison of Welsh-Powell and DSatur.
- **Metrics**: Execution time (ms) and Chromatic Number (number of time slots).
- **Goal**: To analyze which algorithm is faster and more efficient for a given set of courses.

### Robustness & Stress Testing
A stress test script `stress_test.py` performs an **Exhaustive Search** strategy by simulating over 100,000 random course combinations to rigorously test algorithm consistency and stability.

## Prerequisites & Installation
Ensure you have Python installed. You also need the following libraries:

```bash
pip install -r graph-project/requirements.txt
```
*Dependencies: `networkx`, `matplotlib`, `pandas` (optional if using pure csv lib)*

## How to Run
Navigate to the project directory:
```bash
cd graph-project
```

### 1. Run Scheduling & Visualization
```bash
# Welsh-Powell Algorithm
python schedule_fp.py

# DSatur Algorithm
python dsatur-fp.py
```

### 2. Run Performance Benchmark
To see a comparative analysis (Time Complexity vs Efficiency):
```bash
python compare_algorithms.py
```

### 3. Run Stress Test
To run the exhaustive robustness test (>100k trials):
```bash
python stress_test.py
```

## Graph Theory Application
To solve the class scheduling problem is by modeling time conflicts between courses as a graph. Each class is represented as a node, and an edge connects two nodes if their schedules overlap. The algorithms assign colors (time slots) such that no connected nodes share the same color.

## Theoretical Insight
**Why do Welsh-Powell and DSatur often produce the same results here?**
University schedules typically behave like **Interval Graphs** (linear time blocks). For Interval Graphs, simple greedy algorithms like **Welsh-Powell** are mathematically capable of finding near-optimal solutions. DSatur's advanced heuristics, while powerful for general graphs, are often "overkill" for this specific dataset structure, resulting in identical efficiency but with slightly higher computational overhead.

## Input - Output
### Input Example
```
Enter your semester: 2
Select courses (example: 1, 3, 5): 1, 2, 3, 4, 5
```

### Output Example (Benchmark)
```
--- PERFORMANCE ANALYSIS RESULT ---
Dataset: Semester 2
Total Classes (N): 16
----------------------------------------
1. Welsh-Powell:
   - Time: 0.0539 ms
   - Chromatic Number (Slots): 4

2. DSatur:
   - Time: 0.1248 ms
   - Chromatic Number (Slots): 4
----------------------------------------
Conclusion:
- Speed: Welsh-Powell is faster by 0.0709 ms.
- Efficiency: Both algorithms used the same number of slots.
```
