def knapsack(weights, values, capacity):
  """
  Giải bài toán ba lô bằng quy hoạch động.

  Args:
    weights: Danh sách trọng lượng của các đồ vật.
    values: Danh sách giá trị của các đồ vật.
    capacity: Sức chứa tối đa của ba lô.

  Returns:
    Giá trị tối đa có thể đạt được và danh sách các đồ vật được chọn.
  """
  n = len(weights)  # Số lượng đồ vật
  dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]  # Khởi tạo bảng dp

  # Khởi tạo bảng dp: giá trị tối ưu cho trường hợp không chọn đồ vật nào
  for j in range(capacity + 1):
    dp[0][j] = 0

  # Duyệt qua các đồ vật từ 1 đến n
  for i in range(1, n + 1):
    for j in range(capacity + 1):
      # Trường hợp 1: Không chọn đồ vật thứ i
      dp[i][j] = dp[i - 1][j]  # Giá trị tối ưu bằng giá trị tối ưu khi không chọn i

      # Trường hợp 2: Chọn đồ vật thứ i
      if weights[i - 1] <= j:  # Kiểm tra xem có thể chọn i hay không
        dp[i][j] = max(
            dp[i - 1][j],  # Giá trị tối ưu khi không chọn i
            dp[i - 1][j - weights[i - 1]] + values[i - 1]  # Giá trị tối ưu khi chọn i
        )

  # Truy vết để lấy danh sách các đồ vật được chọn
  selected_items = []
  current_weight = capacity
  for i in range(n, 0, -1):
    if dp[i][current_weight] != dp[i - 1][current_weight]:
      selected_items.append(i - 1)  # Thêm i vào danh sách
      current_weight -= weights[i - 1]  # Cập nhật trọng lượng còn lại

  # Giá trị tối ưu và danh sách các đồ vật được chọn
  return dp[n][capacity], selected_items

# Ví dụ
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 10

# Giải bài toán
max_value, selected_items = knapsack(weights, values, capacity)

# Hiển thị kết quả
print("Giá trị tối đa:", max_value)
print("Danh sách các đồ vật được chọn:", selected_items)
