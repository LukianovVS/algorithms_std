# -*- coding: utf-8 -*-
"""
breadth-first search - алгоритм поиска в ширину

Created on Tue Mar  8 18:50:52 2022

@author: lvs
"""

# import fifo queue
from collections import deque


def bfs(graph: dict, start_key: str, check: str):
    '''
    поиск в ширину по графу. Здесь проверятся только факт наличия пути 
    из start_key в check (путь не сохраняется)
    
    graph - словарь/граф, по которому проводится поиск
    start_key - тартовая позиция 
    check - то что ищем
    '''
    # fifo очередь, ожидающая проверку 
    search_queue = deque()
    # начинаем проверку с себя
    search_queue.append(start_key)
    # проверенные элементы. Храним для избежания коллизий 
    # (зацикленность при обратной связи)
    searched = []
    
    
    while search_queue:
        # первый из очереди
        word = search_queue.popleft()
        if not word in searched:
            print(f'-> {word}', end = '')
            if word == check:
                print(f'\n{check} found')
                print('----------------')
                return True
            else:
                # все пути из этой точки добавляем в очередь (список может быть пустым) 
                search_queue += graph[word]
                searched.append(word)
    print(f'\n{check} not found')
    print('----------------')
    return False




if __name__ == '__main__':
    # граф поиска
    graph = {}
    graph['London'] = ['Edinburgh', 'Manchester', 'Music City']
    graph['Edinburgh'] = ['London', 'Birmingham']
    graph['Manchester'] = ['London', 'Birmingham', 'Music City', 'Glasgow']
    graph['Music City'] = ['Birmingham', 'Bristol']
    graph['Glasgow'] = ['Music City', 'Bristol']
    graph['Bristol'] = ['Oxford', 'Cambridge']
    graph['Cambridge'] = ['Cardiff', 'Liverpool']
    # "тупик"
    graph['Birmingham'] = []
    graph['Oxford'] = []
    graph['Liverpool'] = []
    graph['Cardiff'] = []
    # info
    print(graph.keys())
    print(len(graph))
    print('-----------------------')
    
    # поиск
    
    bfs(graph, 'London', 'Liverpool')    
    bfs(graph, 'London', 'Liverpol')    
    bfs(graph, 'Liverpool', 'Liverpool') 
    bfs(graph, 'London', 'Glasgow') 