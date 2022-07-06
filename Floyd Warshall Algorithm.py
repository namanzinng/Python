nI = 4
INF = 999

def floyd_wa(G):
    dist = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(nI):
        for i in range(nI):
            for j in range(nI):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    display(dist)


def display(dist):
    for i in range(nI):
        for j in range(nI):
            if(dist[i][j] == INF):
                print("INF", end=" ")
            else:
                print(dist[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_wa(G)
