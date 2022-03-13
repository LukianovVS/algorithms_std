# -*- coding: utf-8 -*-
"""
Алгоритм Дейкстры
    + Работает со взвешенными графами 
    + ему НЕ страшны циклы (т.к. каждый узел обрабатывается 1 раз)
    + алгоритм относительно простой
    - не работает с отрицательными весами (т.к. каждый узел обрабатывается 1 раз, 
           а отрицательный путь - всё ломает)

Смог придумать костыль, для работы с отрицательными весами. Этот костыль с точки 
зрения кода - не оптимален,он, скорее, помог мне убедиться что я правильно все понял. 


Created on Sun Mar 13 21:36:33 2022

@author: lvs
"""

# моя самопроизвольна адаптация алгоритма для работы с отрицательными весами. 
# Т.е. - если отрцательный вес уменьшил стоимость, то надо все обработать с самого начала
# на простом примере прокатило - но, возмоно всё не так просто, надо думать...
FLAG_CHECK_NEGATIVE_WEIGHT = False


inf = float('inf')

def get_lowest_cost_node(costs, procesed):
    ''' поиск нового узла с минимальной стоимостью'''
    cost_min = inf
    node_min = None
    
    for node in costs.keys():
        if node in procesed:
            continue
        if costs[node] < cost_min:
            cost_min = costs[node]
            node_min = node
    
    return node_min
            
    

def search(graph:dict, costs:dict, parents:dict):
    procesed = [] # список обработанных узлов
        
    while True:
        # В цикле обрабатываются все узылы.
        # каждый узел обрабатывается 1 раз 
        # новый узел - самый дешевый узел (это важно!!!)
        node = get_lowest_cost_node(costs, procesed)        
        if not node:
            break
        print(node)
        # проверяем, возможно из этого узла жо соседа путь короче, чем был известен
        for n in graph[node].keys():
            cost_new = costs[node] + graph[node][n]
            if cost_new < costs[n]:
                parents[n] = node
                costs[n] = cost_new
                # мой костыль для отрицательного веса
                if FLAG_CHECK_NEGATIVE_WEIGHT:
                    if graph[node][n] < 0:
                        procesed = []
                
        procesed.append(node)
        


if __name__ == '__main__':
#     задаем граф
    # graph
    graph = {}
    graph['beg'] = {}
    graph['A']   = {}
    graph['B']   = {}
    graph['C']   = {}
    graph['D']   = {}
    graph['E']   = {}
    graph['F']   = {}
    graph['G']   = {}
    graph['H']   = {}
    graph['I']   = {}
    graph['end']   = {}
    
    graph['beg']['A'] = 5
    graph['beg']['B'] = 1
    
    graph['A']['D'] = 11
    graph['A']['E'] = 3
    
    graph['B']['C'] = 2
    graph['B']['E'] = 29
    
    # C -empty
    
    graph['D']['F'] = 4
    graph['D']['G'] = 9
    
    if FLAG_CHECK_NEGATIVE_WEIGHT:
        graph['D']['E'] = -16
    
    
    graph['E']['H'] = 5
    graph['E']['I'] = 3
    
    graph['F']['end'] = 12
    
    graph['G']['end'] = 4
    
    graph['H']['G'] = 2
    
    graph['I']['H'] = 1
    graph['I']['end'] = 9
    
#   "стоимость"
    costs = {}
#   родитель
    parents = {}
    for k in graph.keys():
        if k == 'beg':
            continue
        costs[k] = inf
        parents[k] = None
#   Начльная точка для стоимости и родителя    
    for k in graph['beg'].keys():    
        costs[k] = graph['beg'][k]
        parents[k] = 'beg'
    
#   поиск    
    search(graph, costs, parents)
#   вывод результата
    print('------------------------')
    print(costs)
    print(parents)    
    print('------------------------')
    
    print(f'cost = {costs["end"]}')
    parent = 'end'
    way = ''
    while parent != 'beg':
        parent_next = parents[parent]
        s = f' -> {parent}'
        if parent_next == 'beg':
            s += f' ({costs[parent]})'
        else:
            s += f' (+{costs[parent] - costs[parents[parent]]} = {costs[parent]})'
            
        way =  s + way
        
        parent = parent_next
    way = 'beg' + way
    print(way)
    
    