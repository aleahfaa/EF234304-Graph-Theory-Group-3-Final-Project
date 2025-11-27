def have_conflict(class_a, class_b):
    if class_a['day'] != class_b['day']:
        return False
    start_a, end_a = class_a['start'], class_a['end']
    start_b, end_b = class_b['start'], class_b['end']
    return not (end_a <= start_b or end_b <= start_a)

def build_graph(classes):
    graph = {cls['name']: [] for cls in classes}
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            if have_conflict(classes[i], classes[j]):
                graph[classes[i]['name']].append(classes[j]['name'])
                graph[classes[j]['name']].append(classes[i]['name'])
    return graph

def welsh_powell_coloring(graph):
    sorted_nodes = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
    colors = {}
    color_num = 0
    for node in sorted_nodes:
        if node not in colors:
            color_num += 1
            colors[node] = color_num
            for other in sorted_nodes:
                if other not in colors:
                    if all(colors.get(adj) != color_num for adj in graph[other]):
                        colors[other] = color_num
    return colors

def group_by_color(colors):
    grouped = {}
    for cls, color in colors.items():
        grouped.setdefault(color, []).append(cls)
    return grouped

def main():
    n = int(input("Enter number of classes: "))
    classes = []
    for i in range(n):
        print(f"\nClass {i + 1}:")
        name = input("Class name: ").strip()
        day = input("Day (e.g., Monday, Tuesday): ").strip().capitalize()
        start = int(input("Start time (e.g., 8 for 08:00): "))
        end = int(input("End time (e.g., 10 for 10:00): "))
        classes.append({'name': name, 'day': day, 'start': start, 'end': end})
    graph = build_graph(classes)
    print("\nAdjacency List (Conflict Graph):")
    for node, adj in graph.items():
        print(f"  {node} -> {adj}")
    colors = welsh_powell_coloring(graph)
    grouped = group_by_color(colors)
    print("Class Schedule Coloring Result:")
    for node, color in colors.items():
        print(f"  {node} -> Time Slot #{color}")
    print("No-Conflict Grouped Schedule:")
    for slot, cls_list in grouped.items():
        print(f"Slot #{slot}: {', '.join(cls_list)}")

if __name__ == "__main__":
    main()