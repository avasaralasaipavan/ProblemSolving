from collections import defaultdict

def removeDuplicate(s: str) -> str:
    last_occurrence = {ch: i for i, ch in enumerate(s)}
    visited = defaultdict(bool)
    stack = []

    for i, ch in enumerate(s):
        if visited[ch]:
            continue
        while stack and ch < stack[-1] and last_occurrence[stack[-1]] > i:
            removed = stack.pop()
            visited[removed] = False

        stack.append(ch)
        visited[ch] = True

    return ''.join(stack)


s = "cbacdcbc"
result = removeDuplicate(s)
print(result)  
