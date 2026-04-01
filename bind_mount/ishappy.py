def isHappy(n):
    arr = set()
    while n != 1 and n not in arr:
        arr.add(n)
        total_sum = 0
        for num in str(n):
            total_sum += int(num) ** 2
        n = total_sum
    return n == 1
    pass 

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    # 반드시 아래 경로로 저장해야 컨테이너와 호스트가 공유됨
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")