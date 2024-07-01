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
                start = int(match.group(1))
                end = int(match.group(2))
                weight = float(match.group(3))
                edges.append((start, end, weight))
            else:
                print(f"Invalid input line: {line}")
    return edges

#最長経路を求める
def find_longest_path(edges):
    graph = defaultdict(list)
    #始点をキーにする
    for start, end, weight in edges:
        graph[start].append((end, weight))
    
    #深さ優先探索
    def dfs(node, visited, path, current_distance, longest_path_info):
        visited.add(node)
        path.append(node)
        
        #最長経路の更新
        if current_distance > longest_path_info['max_distance']:
            longest_path_info['max_distance'] = current_distance
            longest_path_info['path'] = list(path)
        
        #未到達の隣接点ごとに再帰呼び出し
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, path, current_distance + weight, longest_path_info)
        
        #前のノードに戻る
        visited.remove(node)
        path.pop()

    longest_path_info = {'path': [], 'max_distance': 0}
    
    for node in graph:
        dfs(node, set(), [], 0, longest_path_info)
    
    return longest_path_info['path']

def main():
    input_data = sys.stdin.read().splitlines()
    edges = parse_input(input_data)
    #エラー処理
    if not edges:
        print("No valid edges found.")
        return
    longest_path = find_longest_path(edges)
    if longest_path:
        for node in longest_path:
            print(node)
    #エラー処理
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
