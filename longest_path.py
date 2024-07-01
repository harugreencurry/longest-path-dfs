import sys
import re
from collections import defaultdict, deque

#データ抽出
def parse_input(input_data):
    edges = []
    for line in input_data:
        line = line.strip()
        if line:
            #ホワイトスペースの処理
            match = re.match(r"(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)", line)
            if match:
                #それぞれのデータの型変換
                start = int(match.group(1))
                end = int(match.group(2))
                weight = float(match.group(3))
                edges.append((start, end, weight))
    return edges


#最長経路の作成
def find_longest_path(edges):
    #グラフ(dict)の作成
    #始点をキー、値を終点と辺重みのタプルとする
    graph = defaultdict(list)
    for start, end, weight in edges:
        graph[start].append((end, weight))
    
    
    #深さ優先探索
    def dfs(node, visited, path, current_distance):
        nonlocal longest_path, max_distance#関数の外にあるのでnonlocal
        visited.add(node)
        path.append(node)
        
        #最長経路、距離の更新
        if current_distance > max_distance:
            max_distance = current_distance
            longest_path = list(path)
            
        
        for neighbor, weight in graph[node]:
            #未到達の隣接点ごとに再帰呼び出し
            if neighbor not in visited:
                dfs(neighbor, visited, path, current_distance + weight)
        
        #前のノードに戻る
        visited.remove(node)
        path.pop()

    longest_path = []
    max_distance = 0
    
    #各点を始点にする
    for node in graph:
        dfs(node, set(), [], 0)
    
    return longest_path

def main():
    input_data = sys.stdin.read().splitlines()
    edges = parse_input(input_data)
    longest_path = find_longest_path(edges)
    for node in longest_path:
        print(node)

if __name__ == "__main__":
    main()
