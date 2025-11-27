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
  
<p align="justify">Source code to <a href="https://www.its.ac.id/informatika/wp-content/uploads/sites/44/2023/11/Module-Handbook-Bachelor-of-Informatics-Program-ITS.pdf">Graph Theory (EF234304)</a>'s final project named Course Scheduling Optimization Using Graph Coloring. All solutions were created by <a href="https://github.com/aleahfaa">Iffa Amalia Sabrina</a>, <a href="https://github.com/bellaacp">Bella Angeline Chong Puteri</a>, <a href="https://github.com/zan4yov">Razan Widya Reswara</a>, and <a href="https://github.com/DocHudson45">Muhammad Dzaky Radithya Ryrdi</a>.</p>

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

<p>On behalf of:<p>

<p><b>Ilham Gurat Adillion, S.Kom., M.Kom.</b></p>

<hr>

## Introduction
Creating a class schedule can be difficult when multiple courses overlap in time. If two classes are held on the same day and their time ranges intersect, it causes scheduling conflicts that make it impossible for students or lecturers to attend both. Managing these conflicts manually is inefficient and error-prone, especially when there are many classes. <br>
To address this, we use Graph Theory to model the time conflicts between courses and generate a schedule that ensures no overlapping classes occur.

## Graph Theory Application
To solve the class scheduling problem is by modeling time conflicts between courses as a graph. Each class is represented as a node, and an edge connects two nodes if their schedules overlap on the same day. This forms a conflict graph that clearly shows which classes cannot be held at the same time. <br>
To generate a valid schedule, the concept of graph coloring is used. Each color represents a unique time slot, and connected nodes must have different colors. The Welsh–Powell algorithm assigns colors efficiently by starting with nodes that have the most conflicts, ensuring minimal time slots are used while avoiding overlaps.<br>
The result is a conflict-free schedule where classes sharing the same color can run simultaneously. This method automates the scheduling process, reduces human error, and optimizes time and room usage effectively. <br>
Overall, this application simplifies complex scheduling problems into a structured coloring task. It provides a systematic and efficient way to organize multiple classes, lecturers, and times without any conflicts.

## Flowchart
1. Input Data <br>
    Enter N as many as the number of subjects
2. Repeat until N
    - Request as many as N for name, day, start time, and end time
    - Save as 1 class data
3. Build Graph
    - Build relationships between classes by seeing if there is any conflict. 
    - Have Conflict? -> who is in conflict with whom:
        - If Yes → check is there overlapping time? → If yes, then these two classes cannot be concurrent, if not, then these classes can be concurrent.
        - If No → These 2 classes have no conflict and can be held simultaneously.
4. Show Each Node and its Neighbors <br>
    Displays the results of the conflict graph that has been created. The program displays each class (node) along with a list of other classes that conflict with it (its neighbors).
5. Welsh-Powell Coloring
    - Grouping classes based on time conflicts.
    - With this algorithm, each class is assigned a color (time slot). Conflicting classes cannot be at the same time, while safe classes can be at the same time.
6. Group by Color <br>
    After each class is assigned a color that indicates a time slot, the program then groups classes that have the same color.
7. Output <br>
    Print scheduling results in the form of:
      - Color or time slot for each class
      - Group classes based on the same time slot.

## Input - Output
### Input
```
Enter number of classes: 3
Class 1:
     Class name: Class A
     Day: Monday
     Start time: 8
     End time: 10
Class 2:
     Class name: Class B
     Day: Monday
     Start time: 9
     End time: 11
Class 3:
     Class name: Class C
     Day: Tuesday
     Start time: 9
     End time: 11
```
### Output
```
Adjancency List (Conflict Graph):
Class A → [‘Class B’]
Class C → []
Class Schedule Coloring Result:
Class A → Time Slot #1
Class B → Time Slot #2
Class C → Time Slot #1
No-Conflict Grouped Schedule:
Slot #1: Class A, Class C
Slot #2: Class B
```