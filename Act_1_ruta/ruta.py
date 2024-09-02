# mi código encuentra la ruta de menos costo, es decir,
# la ruta que sume menos puntos al ser recorrida

from heapq import heappop, heappush

# la matriz que se me ocurrió
grid = [
    [-12, 6, -8, 'B'],
    ['A', 7, 2, 1],
    [1, 2, 1, 9]
]

# las direcciones permitidas son ^, v, <, >
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start = (1, 0)  # la coord de 'A'
end = (0, 3)    # la coord de 'B'

# Function to check if the move is within the grid
def is_valid_move(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def route_shortest_path(start, end):
    queue = [(0, start, [start])]
    visited = set()
    visited.add(start)
    
    while queue:
        cost, (x, y), path = heappop(queue)
        
        if (x, y) == end:
            return path  # la ruta de menos costo qe encopntró
        
        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            
            if is_valid_move(nx, ny) and (nx, ny) not in visited:
                # se calcula el costo de llegasr a la sig celda
                next_cost = cost + (grid[nx][ny] if isinstance(grid[nx][ny], int) else 0)
                heappush(queue, (next_cost, (nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    
    return None  # si no se encuentra ruta

# encuentra la ruta de menios costo de A a B
shortest_path = route_shortest_path(start, end)

if shortest_path:
    print("ruta de menos costo:", shortest_path)
    path_values = [grid[x][y] for x, y in shortest_path]
    print("valores:", path_values)
    print("saltos:", len(shortest_path) - 1)
    subset = path_values[1:-1]
    sum = 0
    for val in subset: sum = sum + val
    print("suma de la ruta: ", sum)
else:
    print("No se encontró ruta")
