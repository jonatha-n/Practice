#test
def solution(start, length):
    # Your code here
    
    s = length * length
    
    if length == 1:
        return start
        
    c = 0
    threshold = length
    diff = 0
    i = 0
    res = None
    while i < s:
        if c == threshold:
            while diff != 0:
                diff -= 1
                i+=1
                continue
            threshold = threshold - 1
            diff = length - threshold
            c = 0
        curr = start + i
        if curr > start + (length * (length - 1)):
            break
        c += 1
        i += 1
        if res == None:
            res = curr
        else:
            res = res^curr
    return res

x = solution(0, 1)
print(x)
print(1^2)