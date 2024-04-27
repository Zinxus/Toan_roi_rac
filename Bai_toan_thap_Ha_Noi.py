def hanoi(n, source, dest, aux):
    if n == 1:
        print(f"Di chuyển đĩa {n} từ {source} sang {dest}")
        return
    else:
        hanoi(n - 1, source, aux, dest)
        print(f"Di chuyển đĩa {n} từ {source} sang {dest}")
        hanoi(n - 1, aux, dest, source)

def hanoi_dp(n):
    # Tạo bảng lưu trữ kết quả
    dp = [[0 for _ in range(3)] for _ in range(n + 1)]

    # Khởi tạo giá trị ban đầu
    for i in range(1, n + 1):
        dp[i][0] = i  # Di chuyển 1 đĩa từ A sang C cần i bước
        dp[i][1] = i * 2 - 1  # Di chuyển 1 đĩa từ A sang B cần 2i - 1 bước

    # Tính toán số bước tối thiểu cho các trường hợp còn lại
    for i in range(2, n + 1):
        for j in range(1, 3):
            if j == 0:
                dp[i][j] = dp[i - 1][2] + 1  # Di chuyển i đĩa từ B sang C
            elif j == 1:
                dp[i][j] = dp[i - 1][0] + dp[i - 1][2] + 1  # Di chuyển i đĩa từ A sang B
            else:
                dp[i][j] = dp[i - 1][1] + 1  # Di chuyển i đĩa từ B sang A

    # Trả về số bước tối thiểu cho n đĩa
    return dp[n][1]

# Ví dụ sử dụng
n = 64
print(f"Số bước tối thiểu để di chuyển {n} đĩa bằng quy hoạch động:", hanoi_dp(n))