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

## Table of Contents
- [Introduction](#introduction)
- [Graph Theory Application](#graph-theory-application)
- [Flowchart](#flowchart)
- [Input-Output](#input---output)
  - [Input](#input)
  - [Welsh-Powell Output](#welsh-powell-output)
  - [DSatur Output](#dsatur-output)
- [Analysis and Comparison](#analysis-and-comparison)
  - [Differences](#differences)


## Introduction
Creating a class schedule can be difficult when multiple courses overlap in time. If two classes are held on the same day and their time ranges intersect, it causes scheduling conflicts that make it impossible for students or lecturers to attend both. Managing these conflicts manually is inefficient and error-prone, especially when there are many classes. <br>
To address this, we use Graph Theory to model the time conflicts between courses and generate a schedule that ensures no overlapping classes occur.

## Graph Theory Application
To solve the class scheduling problem is by modeling time conflicts between courses as a graph. Each class is represented as a node, and an edge connects two nodes if their schedules overlap on the same day. This forms a conflict graph that clearly shows which classes cannot be held at the same time. <br>
To generate a valid schedule, the concept of graph coloring is used. Each color represents a unique time slot, and connected nodes must have different colors. The Welsh–Powell algorithm and DSatur algorithm assign colors efficiently by starting with nodes that have the most conflicts, ensuring minimal time slots are used while avoiding overlaps.<br>
The result is a conflict-free schedule where classes sharing the same color can run simultaneously. This method automates the scheduling process, reduces human error, and optimizes time and room usage effectively. <br>
Overall, this application simplifies complex scheduling problems into a structured coloring task. It provides a systematic and efficient way to organize multiple classes, lecturers, and times without any conflicts.

## Flowchart
1. Input Data <br>
    - Input semester
    - Choose available course
    - Check if the semester is even or odd
2. Read CSV file
    - Normalize headers
    - Parse class times
    - Build class records
    - Filter class by semester
3. Build Graph
    - Build relationships between classes by seeing if there is any conflict. 
    - Have Conflict? -> who is in conflict with whom:
        - If Yes → check is there overlapping time? → If yes, then these classes cannot be concurrent, if not, then these classes can be concurrent.
        - If No → These classes have no conflict and can be held simultaneously.
4. Show Each Node and its Neighbors <br>
    Displays the results of the conflict graph that has been created. The program displays each class (node) along with a list of other classes that conflict with it (its neighbors).
5. Coloring Algorithm: Welsh-Powell Algorithm and DSatur Algorithm <br>
      - Grouping classes based on time conflicts.
      - With this algorithm, each class is assigned a color (time slot). Conflicting classes cannot be at the same time, while safe classes can be at the same time.
6. Group by Color <br>
    After each class is assigned a color that indicates a time slot, the program then groups classes that have the same color.
7. Output <br>
    Print scheduling results in the form of:
      - Adjacency List (Conflict Graph)
      - Class Schedule Coloring Result
      - No-Conflict Grouped Schedule

## Input - Output
### Input
```
Enter your semester: 2
Available Courses:
// List of available courses
Select courses (example: 1, 3, 5): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
```
### Welsh-Powell Output
```
Adjacency List (Conflict Graph):
Kalkulus 2 - IUP → ['Komputasi Numerik - A']
Komputasi Numerik - A → ['Kalkulus 2 - IUP']
Pemrograman Berorientasi Objek - RPL (M) → ['Sistem Operasi - A', 'Struktur Data - A', 'Struktur Data - IUP']
Sistem Operasi - A → ['Pemrograman Berorientasi Objek - RPL (M)', 'Struktur Data - A', 'Struktur Data - IUP']
Struktur Data - A → ['Pemrograman Berorientasi Objek - RPL (M)', 'Sistem Operasi - A', 'Struktur Data - IUP']
Struktur Data - IUP → ['Pemrograman Berorientasi Objek - RPL (M)', 'Sistem Operasi - A', 'Struktur Data - A']
Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M) → ['Sistem Operasi - B', 'Teori Graf - RKA (N)']
Sistem Operasi - B → ['Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M)', 'Teori Graf - RKA (N)']
Teori Graf - RKA (N) → ['Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M)', 'Sistem Operasi - B']
Organisasi Komputer - A → ['Struktur Data - B']
Struktur Data - B → ['Organisasi Komputer - A']
Komputasi Numerik - B → ['Komputasi Numerik - IUP', 'Konsep Kecerdasan Artifisial - RKA (N)']
Komputasi Numerik - IUP → ['Komputasi Numerik - B', 'Konsep Kecerdasan Artifisial - RKA (N)']
Konsep Kecerdasan Artifisial - RKA (N) → ['Komputasi Numerik - B', 'Komputasi Numerik - IUP']
Metodologi Penelitian - A → ['Struktur Data - RPL (M)']
Struktur Data - RPL (M) → ['Metodologi Penelitian - A']

Class Schedule Coloring Result:
Pemrograman Berorientasi Objek - RPL (M) → Time Slot #1
Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M) → Time Slot #1
Komputasi Numerik - B → Time Slot #1
Kalkulus 2 - IUP → Time Slot #1
Organisasi Komputer - A → Time Slot #1
Metodologi Penelitian - A → Time Slot #1
Sistem Operasi - A → Time Slot #2
Sistem Operasi - B → Time Slot #2
Komputasi Numerik - IUP → Time Slot #2
Komputasi Numerik - A → Time Slot #2
Struktur Data - B → Time Slot #2
Struktur Data - RPL (M) → Time Slot #2
Struktur Data - A → Time Slot #3
Teori Graf - RKA (N) → Time Slot #3
Konsep Kecerdasan Artifisial - RKA (N) → Time Slot #3
Struktur Data - IUP → Time Slot #4

No-Conflict Grouped Schedule:
Slot #1: Pemrograman Berorientasi Objek - RPL (M), Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M), Komputasi Numerik - B, Kalkulus 2 - IUP, Organisasi Komputer - A, Metodologi Penelitian - A
Slot #2: Sistem Operasi - A, Sistem Operasi - B, Komputasi Numerik - IUP, Komputasi Numerik - A, Struktur Data - B, Struktur Data - RPL (M)
Slot #3: Struktur Data - A, Teori Graf - RKA (N), Konsep Kecerdasan Artifisial - RKA (N)
Slot #4: Struktur Data - IUP
```
### DSatur Output
```
Adjacency List (Conflict Graph):
Kalkulus 2 - IUP → ['Komputasi Numerik - A']
Komputasi Numerik - A → ['Kalkulus 2 - IUP']
Pemrograman Berorientasi Objek - RPL (M) → ['Sistem Operasi - A', 'Struktur Data - A', 'Struktur Data - IUP']
Sistem Operasi - A → ['Pemrograman Berorientasi Objek - RPL (M)', 'Struktur Data - A', 'Struktur Data - IUP']
Struktur Data - A → ['Pemrograman Berorientasi Objek - RPL (M)', 'Sistem Operasi - A', 'Struktur Data - IUP']
Struktur Data - IUP → ['Pemrograman Berorientasi Objek - RPL (M)', 'Sistem Operasi - A', 'Struktur Data - A']
Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M) → ['Sistem Operasi - B', 'Teori Graf - RKA (N)']
Sistem Operasi - B → ['Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M)', 'Teori Graf - RKA (N)']
Teori Graf - RKA (N) → ['Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M)', 'Sistem Operasi - B']
Organisasi Komputer - A → ['Struktur Data - B']
Struktur Data - B → ['Organisasi Komputer - A']
Komputasi Numerik - B → ['Komputasi Numerik - IUP', 'Konsep Kecerdasan Artifisial - RKA (N)']
Komputasi Numerik - IUP → ['Komputasi Numerik - B', 'Konsep Kecerdasan Artifisial - RKA (N)']
Konsep Kecerdasan Artifisial - RKA (N) → ['Komputasi Numerik - B', 'Komputasi Numerik - IUP']
Metodologi Penelitian - A → ['Struktur Data - RPL (M)']
Struktur Data - RPL (M) → ['Metodologi Penelitian - A']

Class Schedule Coloring Result (DSATUR):
Pemrograman Berorientasi Objek - RPL (M) → Time Slot #1
Sistem Operasi - A → Time Slot #2
Struktur Data - A → Time Slot #3
Struktur Data - IUP → Time Slot #4
Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M) → Time Slot #1
Sistem Operasi - B → Time Slot #2
Teori Graf - RKA (N) → Time Slot #3
Komputasi Numerik - B → Time Slot #1
Komputasi Numerik - IUP → Time Slot #2
Konsep Kecerdasan Artifisial - RKA (N) → Time Slot #3
Kalkulus 2 - IUP → Time Slot #1
Komputasi Numerik - A → Time Slot #2
Organisasi Komputer - A → Time Slot #1
Struktur Data - B → Time Slot #2
Metodologi Penelitian - A → Time Slot #1
Struktur Data - RPL (M) → Time Slot #2

No-Conflict Grouped Schedule:
Slot #1: Pemrograman Berorientasi Objek - RPL (M), Pengantar Teknologi Elektro dan Informatika Cerdas - RPL (M), Komputasi Numerik - B, Kalkulus 2 - IUP, Organisasi Komputer - A, Metodologi Penelitian - A
Slot #2: Sistem Operasi - A, Sistem Operasi - B, Komputasi Numerik - IUP, Komputasi Numerik - A, Struktur Data - B, Struktur Data - RPL (M)
Slot #3: Struktur Data - A, Teori Graf - RKA (N), Konsep Kecerdasan Artifisial - RKA (N)
Slot #4: Struktur Data - IUP
```

## Analysis and Comparison
### Differences
<div align="center">
  <table>
    <thead>
      <tr>
        <th align="center">Welsh-Powell Coloring</th>
        <th align="center">DSatur Coloring</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td align="justify">1. Sort the nodes from highest degree to the lowest degree <br> 2. Color the node from the highest degree <br> 3. Repeat the second steps until all of the nodes are colored</td>
        <td align="justify">1. Pick the node with highest saturation degree <br> 2. If there are more than one nodes with highest saturation degree, pick the highest-degree node <br> 3. Recalculate saturation after every coloring <br> 4. Repeat from the first step until all of the nodes are colored</td>
      </tr>
    </tbody>
  </table>
</div>