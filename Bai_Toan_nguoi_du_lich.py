import sys

def hoan_vi(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def tinh_chi_phi(duong_di, ma_tran_chi_phi):
    tong_chi_phi = 0
    N = len(duong_di)
    for i in range(N - 1):
        tong_chi_phi += ma_tran_chi_phi[duong_di[i]][duong_di[i + 1]]
    tong_chi_phi += ma_tran_chi_phi[duong_di[N - 1]][duong_di[0]]
    return tong_chi_phi

def nhanh_va_can(cap_do, muc, ma_tran_chi_phi, chi_phi_nho_nhat, duong_di_tot_nhat):
    N = len(cap_do)
    if muc == N:
        chi_phi_hien_tai = tinh_chi_phi(cap_do, ma_tran_chi_phi)
        if chi_phi_hien_tai < chi_phi_nho_nhat[0]:
            chi_phi_nho_nhat[0] = chi_phi_hien_tai
            duong_di_tot_nhat[:] = cap_do[:]
        return

    for i in range(muc, N):
        hoan_vi(cap_do, muc, i)
        gioi_han_hien_tai = tinh_chi_phi(cap_do[:muc+1], ma_tran_chi_phi)
        if gioi_han_hien_tai < chi_phi_nho_nhat[0]:
            nhanh_va_can(cap_do, muc + 1, ma_tran_chi_phi, chi_phi_nho_nhat, duong_di_tot_nhat)
        hoan_vi(cap_do, muc, i)

if __name__ == "__main__":
    # Một ma trận chi phí mẫu lớn hơn
    ma_tran_chi_phi = [
        [0, 29, 20, 21, 16],
        [29, 0, 15, 26, 14],
        [21, 15, 0, 16, 26],
        [21, 26, 16, 0, 22],
        [16, 14, 26, 22, 0]
    ]

    N = len(ma_tran_chi_phi)
    cap_do = list(range(N))
    chi_phi_nho_nhat = [sys.maxsize]
    duong_di_tot_nhat = []

    nhanh_va_can(cap_do, 0, ma_tran_chi_phi, chi_phi_nho_nhat, duong_di_tot_nhat)

    print("Chi phí nhỏ nhất là:", chi_phi_nho_nhat[0])
    print("Đường đi tối ưu:")
    for i in range(N):
        print(f"({i + 1}, {duong_di_tot_nhat[i] + 1})", end=" ")
