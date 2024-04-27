# Define maximum values 
N_MAX = 500
M_MAX = 65535

def init():
    global N, currency, value, F, M
    N = int(input("Nhập số lượng loại tiền: "))
    currency = [None] * (N_MAX + 1)  # Mảng lưu trữ tên các loại tiền
    value = [0] * (N_MAX + 1)      # Mảng lưu trữ mệnh giá của các loại tiền
    F = [[M_MAX + 1 for j in range(M_MAX + 1)] for i in range(N_MAX + 1)]  # Mảng 2 chiều lưu trữ số lượng tối thiểu tờ tiền cần thiết
    M = int(input("Nhập số lượng tiền muốn thanh toán: "))

    # Khởi tạo hàng đầu tiên và cột đầu tiên của F
    for i in range(M_MAX + 1):
        F[0][i] = M + 1
    for i in range(N_MAX + 1):
        F[i][0] = 0

    # Đọc tên và mệnh giá các loại tiền
    for i in range(1, N + 1):
        currency[i] = input(f"Loại tiền thứ {i} là: ")
        value[i] = int(currency[i])  # Giả sử mệnh giá là một số nguyên

def optimize():
    for i in range(1, N + 1):
        for j in range(1, M_MAX + 1):
            F[i][j] = F[i - 1][j]  # Tối thiểu sử dụng loại tiền trước
            if j >= value[i] and F[i][j] > 1 + F[i][j - value[i]]:
                # Cập nhật tối thiểu nếu sử dụng loại tiền hiện tại giảm số tờ tiền
                F[i][j] = 1 + F[i][j - value[i]]

def result():
    # Kiểm tra xem có thể thanh toán số tiền hay không
    if F[N][M] == M_MAX + 1:
        print("Không thể thanh toán với các loại tiền này!")
    else:
        # Tính toán và hiển thị số lượng tối thiểu tờ tiền cần thiết
        min_coins = F[N][M]
        print(f"Số lượng ít nhất của các loại tiền cần dùng là: {min_coins}")

if __name__ == "__main__":
  init()
  optimize()
  result()
