def PredictWinner(arr: list[int], p1: int, p2: int, flag: bool):
    if len(arr) == 0:
        if p1>p2:
            return True
        #print("Player 1:", p1, "| Player 2:", p2)
        return False

    if len(arr) == 1:
        if flag:
            p2 += arr[0]
        else:
            p1 += arr[0]
        if p1>p2:
            return True
        return False

    # Copy the list so recursion doesn't modify the original
    new_arr = arr[:]

    # Player 1's turn
    if not flag:
        if new_arr[0] > new_arr[-1]:
            p1 += new_arr[0]
            new_arr.pop(0)
        else:
            p1 += new_arr[-1]
            new_arr.pop()
    else:  # Player 2's turn
        if new_arr[0] > new_arr[-1]:
            p2 += new_arr[0]
            new_arr.pop(0)
        else:
            p2 += new_arr[-1]
            new_arr.pop()

    # Alternate the turn
    PredictWinner(new_arr, p1, p2, not flag)


arr = [1,5,233,7]
flag = False
if len(arr)%2 ==0:
    flag = True
p1=0
p2=0
print(PredictWinner(arr,p1,p2,flag))
print(p1>p2)