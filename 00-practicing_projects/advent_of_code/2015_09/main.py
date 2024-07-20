from typing import Any, TypedDict

Edge = TypedDict("Edge", {"vertex": str, "distance": float})

Vertex = TypedDict("Vertex", {"vertex": str, "edges": list[Edge]})

class Graph():
    _graph: list[Vertex] = []

    def __init__(self, locations_pair: list[str]):
        self._init_graph(locations_pair)

    def get_graph(self):
        return self._graph

    def _get_vertex(self, vertex: str) -> Vertex | None:
        for v in self._graph:
            if v["vertex"] == vertex:
                return v
        return None

    def _add_edge_or_create_vertex(
            self,
            vertex: Vertex | None,
            origin: str,
            destination: str,
            distance: str
    ) -> None:
            if vertex:
                vertex["edges"].append(
                        {"vertex": destination, "distance": float(distance)}
                )
            else:
                self._graph.append({
                    "vertex": origin,
                    "edges": [{"vertex": destination, "distance": float(distance)}]
                })
        

    def _init_graph(self, locations_pair: list[str]) -> None:
        for location_pair in locations_pair:
            [origin, to_and_distance] = location_pair.split(" to ")
            [to, distance] = to_and_distance.split(" = ")
            origin_vertex = self._get_vertex(origin)
            self._add_edge_or_create_vertex(origin_vertex, origin, to, distance)
            destination_vertex = self._get_vertex(to)
            self._add_edge_or_create_vertex(destination_vertex, to, origin, distance)

    def shortest_path_through_all_vertices(self) -> float:
        seen: list[str] = []
        curr = self._graph[0]
        total_dist: float = 0.0
        while len(seen) < len(self._graph):
            seen.append(curr["vertex"])
            closest_vertex: Edge = {"vertex": "", "distance": float('inf')}

            for edge in curr["edges"]:
                if edge["vertex"] not in seen:
                    if edge["distance"] < closest_vertex["distance"]:
                        closest_vertex = edge

            for v in self._graph:
                if v["vertex"] == closest_vertex["vertex"]:
                    print(f"{curr['vertex']} - {closest_vertex['distance']} -> {closest_vertex['vertex']}")
                    total_dist += closest_vertex['distance']
                    curr = v
                    break

        return total_dist

if __name__ == "__main__":
    with open("input.txt") as f:
        input_lines = [l.strip() for l in f.readlines()]
        graph = Graph(input_lines)
        total_dist = graph.shortest_path_through_all_vertices()
        print(f'total distance = {total_dist}')
        print()
        for v in graph.get_graph():
            print(v)
            print()
