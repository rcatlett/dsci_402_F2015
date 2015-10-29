def build_graph(items, link_f, directional=False):
	#link_f(A, B) -> true if A and B are connected, otherwise False
	graph = {}
	for i in range(0, len(items) - 1):
		if not(graph.has_key(i)):
			graph[items[i]] = []
		for j in range(i+1, len(items)):
			if not(graph.has_key(j)):
				graph[items[j]] = []
			graph[items[i]].append(items[j])
			graph[items[j]].append(items[i])
	return graph
