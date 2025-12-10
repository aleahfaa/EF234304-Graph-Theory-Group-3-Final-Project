import time
import importlib.util
import sys
import os

sys.path.append(os.getcwd())


import schedule_fp

def import_dsatur():
    spec = importlib.util.spec_from_file_location("dsatur_fp", "dsatur-fp.py")
    dsatur_module = importlib.util.module_from_spec(spec)
    sys.modules["dsatur_fp"] = dsatur_module
    spec.loader.exec_module(dsatur_module)
    return dsatur_module

dsatur_fp = import_dsatur()

def measure_performance(algorithm_func, graph, *args):
    start_time = time.perf_counter()
    colors = algorithm_func(graph, *args)
    end_time = time.perf_counter()
    duration_ms = (end_time - start_time) * 1000
    chromatic_number = len(set(colors.values())) if colors else 0
    return duration_ms, chromatic_number, colors

def main():
    print("--- COURSE SCHEDULING ALGORITHM BENCHMARK ---\n")
    
    semester = input("Enter your semester: ").strip()

    if semester.isdigit() and int(semester) % 2 == 0:
        filename = "schedule_even.csv"
    else:
        filename = "schedule_odd.csv"

    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    all_classes = schedule_fp.read_csv(filename)
    available = [c for c in all_classes if c['semester'] == semester]

    if not available:
        print("No courses found for this semester.")
        return

    print("\nAvailable Courses:")
    for i, cls in enumerate(available, 1):
        print(f"[{i}] {cls['name']} ({cls['day']} {cls['display_time']})")

    choice = input("\nSelect courses (example: 1,3,5): ")
    try:
        indexes = [int(x.strip()) - 1 for x in choice.split(",")]
        selected = [available[i] for i in indexes]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    # 1. Build Graph
    graph = schedule_fp.build_graph(selected)
    print(f"\nGraph built successfully with {len(graph)} nodes.\n")

    # 2. Benchmark Welsh-Powell
    print("Running Welsh-Powell...")
    wp_time, wp_chromatic, wp_colors = measure_performance(schedule_fp.welsh_powell_coloring, graph)

    # 3. Benchmark DSatur
    print("Running DSatur...")
    ds_time, ds_chromatic, ds_colors = measure_performance(dsatur_fp.dsatur_coloring, graph)

    print("\n" + "="*40)
    print("--- PERFORMANCE ANALYSIS RESULT ---")
    print("="*40)
    print(f"Dataset: Semester {semester}")
    print(f"Total Classes (N): {len(selected)}")
    print("-" * 40)
    
    print("1. Welsh-Powell:")
    print(f"   - Time: {wp_time:.4f} ms")
    print(f"   - Chromatic Number (Slots): {wp_chromatic}")
    
    print("\n2. DSatur:")
    print(f"   - Time: {ds_time:.4f} ms")
    print(f"   - Chromatic Number (Slots): {ds_chromatic}")
    
    print("-" * 40)
    time_diff = abs(wp_time - ds_time)
    faster = "Welsh-Powell" if wp_time < ds_time else "DSatur"
    
    slot_diff = abs(wp_chromatic - ds_chromatic)
    more_efficient = "Equal"
    if wp_chromatic < ds_chromatic:
        more_efficient = "Welsh-Powell"
    elif ds_chromatic < wp_chromatic:
        more_efficient = "DSatur"

    print(f"Conclusion:")
    print(f"- Speed: {faster} is faster by {time_diff:.4f} ms.")
    if more_efficient == "Equal":
        print(f"- Efficiency: Both algorithms used the same number of slots.")
    else:
        print(f"- Efficiency: {more_efficient} is more efficient by {slot_diff} slots.")
    
    print("="*40)

if __name__ == "__main__":
    main()
