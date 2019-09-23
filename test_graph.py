
from src.graph import Graph

def testGraph():
    '''
    Here we test algorithms for graphs
    We test 
     a) breadth first search
     b) depth first search
     c) minimum spanning tree using Prim's algorithm
     d) shortest distance using Dijkstra's algorithm
    
    Graph's vertices are specified as a list
    Graph's edges are represented as a dictionary
    '''

    print('Create a default graph')
    g = Graph()
    print(g.E)

    print('')
    print('Changing the default graph to the following')
    g.V = [str(i) for i in range(9)]
    g.E = {
        '0': {'1':4, '7':8},
        '1': {'0':4, '2':8, '7':11},
        '2': {'1':8, '3':7, '5':4, '8':2},
        '3': {'2':7, '4':9, '5':14},
        '4': {'3':9, '5':10},
        '5': {'2':4, '3':14, '4':10, '6':2},
        '6': {'5':2, '7':1, '8':6},
        '7': {'0':8, '1':11, '6':1, '8':7},
        '8': {'2':2, '6':6, '7':7}
    }
    print(g.E)

    strt = '0'

    print('\nBFS with starting node ' + strt)
    g.bfs(strt)

    print('\nDFS with starting node ' + strt)
    g.dfs(strt)

    print('\nPrim-MST with starting node '+ strt)
    g.prim_mst(strt)

    print('\nDijkstra with starting node ' + strt)
    g.dijkstra(strt)


if __name__ == '__main__':
    print(testGraph.__doc__)
    testGraph()
