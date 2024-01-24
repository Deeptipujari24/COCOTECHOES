import networkx as nx

language_data = [
    (1, ['hindi', 'english', 'gujarati']),
    (2, ['hindi', 'odia']),
    (3, ['tamil', 'english']),
    (4, ['odia', 'spanish']),
    (5, ['gujarati', 'tamil']),
    (6, ['tamil', 'odia']),
    (7, ['telugu', 'english']),
    (8, ['telugu', 'hindi']),
    (9, ['marathi', 'hindi']),
    (10, ['english', 'spanish']),
]

graph = nx.Graph()

for person, languages in language_data:
    graph.add_edges_from([(person, other) for other, other_languages in language_data if set(languages) & set(other_languages)])

def find_all_translation_paths(person1, person2):
    try:
        paths = nx.all_shortest_paths(graph, source=person1, target=person2)
        return [path[1:] for path in paths]  # Exclude the starting person as they don't need translation with themselves
    except nx.NetworkXNoPath:
        return None  # No path exists, indicating no common language
        
# Example: Person 1 talking to Person 4
person1 = 1
person2 = 4
translation_paths = find_all_translation_paths(person1, person2)

if translation_paths is not None:
    print(f"To translate the conversation between Person {person1} and Person {person2}, involve the following people in each path:")
    for path in translation_paths:
        print(", ".join([f"Person {person}" for person in path]))
else:
    print(f"There is no common language between Person {person1} and Person {person2}. Translation not possible.")

