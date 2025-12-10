import csv

# ==========================
#     PARSE TIME UTILITIES
# ==========================

def parse_time(time_str):
    time_str = time_str.strip()
    time_str = time_str.replace(".", ":")
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


def parse_range(range_str):
    range_str = range_str.replace(" ", "")
    range_str = range_str.replace(".", ":")
    start, end = range_str.split("-")
    return parse_time(start), parse_time(end)


# ==========================
#     CONFLICT CHECK
# ==========================

def have_conflict(a, b):
    if a['day'] != b['day']:
        return False
    return not (a['end'] <= b['start'] or b['end'] <= a['start'])


def build_graph(classes):
    graph = {cls['name']: [] for cls in classes}
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            if have_conflict(classes[i], classes[j]):
                graph[classes[i]['name']].append(classes[j]['name'])
                graph[classes[j]['name']].append(classes[i]['name'])
    return graph


# ==========================
#     DSATUR ALGORITHM
# ==========================

def dsatur_coloring(graph):
    colors = {}
    saturation = {node: 0 for node in graph}
    degrees = {node: len(graph[node]) for node in graph}

    # Node pertama → degree tertinggi
    current = max(graph, key=lambda n: degrees[n])

    while len(colors) < len(graph):

        used_colors = {colors.get(nei) for nei in graph[current] if nei in colors}
        color = 1
        while color in used_colors:
            color += 1

        colors[current] = color

        # Update saturation tetangga
        for nei in graph[current]:
            if nei not in colors:
                neighbor_colors = {colors.get(n) for n in graph[nei] if n in colors}
                saturation[nei] = len(neighbor_colors)

        # Pilih node berikutnya
        uncolored = [n for n in graph if n not in colors]
        if not uncolored:
            break

        current = max(uncolored, key=lambda n: (saturation[n], degrees[n]))

    return colors


# ==========================
#     GROUP BY COLOR
# ==========================

def group_by_color(colors):
    grouped = {}
    for name, c in colors.items():
        grouped.setdefault(c, []).append(name)
    return grouped


# ==========================
#    NORMALIZE CSV HEADERS
# ==========================

def normalize_headers(reader):
    normalized = []
    for h in reader.fieldnames:
        h = (h or "").strip().lower().replace(" ", "_").replace("\ufeff", "")
        normalized.append(h)
    reader.fieldnames = normalized
    return reader


# ==========================
#      READ CSV FILE
# ==========================

def read_csv(filename):
    classes = []
    with open(filename, newline='', encoding='utf-8-sig') as raw:
        sample = raw.read(4096)
        raw.seek(0)
        dialect = csv.Sniffer().sniff(sample)

        reader = csv.DictReader(raw, dialect=dialect)
        reader = normalize_headers(reader)

        for row in reader:
            time_raw = row['time'].strip()
            start, end = parse_range(time_raw)

            classes.append({
                'name': row['course_name'].strip(),
                'day': row['day'].strip().capitalize(),
                'start': start,
                'end': end,
                'display_time': time_raw,
                'semester': row['semester'].strip()
            })

    return classes


# ==========================
#            MAIN
# ==========================

def main():
    semester = input("Enter your semester: ").strip()

    if semester.isdigit() and int(semester) % 2 == 0:
        filename = "schedule_even.csv"
    else:
        filename = "schedule_odd.csv"

    all_classes = read_csv(filename)
    available = [c for c in all_classes if c['semester'] == semester]

    if not available:
        print("No courses found for this semester.")
        return

    print("\nAvailable Courses:")
    for i, cls in enumerate(available, 1):
        print(f"[{i}] {cls['name']} ({cls['day']} {cls['display_time']})")

    choice = input("\nSelect courses (example: 1,3,5): ")
    indexes = [int(x.strip()) - 1 for x in choice.split(",")]
    selected = [available[i] for i in indexes]

    graph = build_graph(selected)

    print("\nAdjacency List (Conflict Graph):")
    for node, adj in graph.items():
        print(f"{node} → {adj}")

    colors = dsatur_coloring(graph)

    print("\nClass Schedule Coloring Result (DSATUR):")
    for node, color in colors.items():
        print(f"{node} → Time Slot #{color}")

    grouped = group_by_color(colors)

    print("\nNo-Conflict Grouped Schedule:")
    for slot, cls_list in grouped.items():
        print(f"Slot #{slot}: {', '.join(cls_list)}")


if __name__ == "__main__":
    main()
