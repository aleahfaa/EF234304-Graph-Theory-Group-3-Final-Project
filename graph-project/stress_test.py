import random
import importlib.util
import sys
import os
import time

sys.path.append(os.getcwd())
import schedule_fp

def import_dsatur():
    spec = importlib.util.spec_from_file_location("dsatur_fp", "dsatur-fp.py")
    dsatur_module = importlib.util.module_from_spec(spec)
    sys.modules["dsatur_fp"] = dsatur_module
    spec.loader.exec_module(dsatur_module)
    return dsatur_module

dsatur_fp = import_dsatur()

def run_stress_test(num_trials=100000):
    print("="*60)
    print("      ROBUSTNESS & STRESS TESTING: GRAPH COLORING       ")
    print("="*60)
    print(f"Target: {num_trials} Random Course Combinations")
    print(f"Goal:   Find valid input where DSatur is more efficient than Welsh-Powell")
    print("-" * 60)

    files = ['schedule_odd.csv', 'schedule_even.csv']
    all_classes = []
    for f in files:
        if os.path.exists(f):
            all_classes.extend(schedule_fp.read_csv(f))
    
    print(f"Dataset Loaded: {len(all_classes)} Total Courses across Odd & Even Semesters")
    print("Starting Exhaustive Search Strategy...\n")

    start_time = time.perf_counter()
    inconsistencies = 0
    consistent_count = 0
    

    semesters = list(set(c['semester'] for c in all_classes))
    
    for i in range(1, num_trials + 1):
        # 1. Randomly pick a semester
        target_sem = random.choice(semesters)
        candidates = [c for c in all_classes if c['semester'] == target_sem]
        
        # 2. Randomly sample courses (size 5 to max)
        if len(candidates) < 5: continue
        k = random.randint(5, len(candidates))
        selected_indices = random.sample(range(len(candidates)), k)
        selected = [candidates[x] for x in selected_indices]
        
        # 3. Build Graph
        graph = schedule_fp.build_graph(selected)
        
        colors_wp = schedule_fp.welsh_powell_coloring(graph)
        chromatic_wp = len(set(colors_wp.values())) if colors_wp else 0
        
        colors_ds = dsatur_fp.dsatur_coloring(graph)
        chromatic_ds = len(set(colors_ds.values())) if colors_ds else 0
        
        if chromatic_wp != chromatic_ds:
            inconsistencies += 1
            print(f"[!] DIFFERENCE FOUND at Trial {i}")
            break
        else:
            consistent_count += 1
            
        if i % 10000 == 0:
            print(f"[{i}/{num_trials}] Trials Completed... (100% Consistent so far)")

    end_time = time.perf_counter()
    duration = end_time - start_time

    print("\n" + "="*60)
    print("                 STRESS TEST RESULTS                  ")
    print("="*60)
    print(f"Total Combinations Tested : {consistent_count}")
    print(f"Inconsistencies Found     : {inconsistencies}")
    print(f"Consistency Rate          : {(consistent_count/num_trials)*100:.2f}%")
    print(f"Execution Time            : {duration:.2f} seconds")
    print("-" * 60)
    
    if inconsistencies == 0:
        print("CONCLUSION: 100% Consistency in Chromatic Number.")
        print("Welsh-Powell performs equally efficiently to DSatur")
        print("for this dataset structure (Interval Graph behavior).")
    else:
        print("CONCLUSION: Differences were found.")
        
    print("="*60)

if __name__ == "__main__":
    run_stress_test(100000)
