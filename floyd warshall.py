v=4
inf=99999999
flag=0
def floydWarshall(graph):
    for vertex in range(v):
        graph[vertex][vertex]=0
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j]=min((int(graph[i][j])),(int(graph[i][k])+int(graph[k][j])))
    for i in range(v):
        for j in range(v):
            if graph[i][j]==99999999:
                graph[i][j]=None


    print(graph)

#گراف اماده برای تست
graph1=[[0, 5, inf, 10],
       [inf, 0, 3, inf],
       [inf, inf, 0, 1],
       [inf, inf, inf, 0]]

graph2=[[0, 3, inf, 7],
       [8, 0, 2, inf],
       [5, inf, 0, 1],
       [2, inf, inf, 0]]

graph3=[[0, 3, inf, 5],
       [2, 0, inf, 4],
       [inf, 1, 0, inf],
       [inf, inf, 2, 0]]


#read graph
def read(n):
    graph=[]
    i=0;j=0;m=0
    for i in range(n):
        graph.append([])
    for i in range(n):
        for j in range(n):
            print(f"{i},{j}:")
            graph[i].append(input())
    return graph

#اگر میخواهید مقادیر مربوط به گراف را به صورت دستی  وارد کنید باید تابع رید را به عنوان ورودی به تابع فلوید وارشال بدهید







floydWarshall(graph3)
input("press a button")

#محمد صادق نیکوفکر

