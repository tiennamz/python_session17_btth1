raw_logs = []
processed_logs = []

'''
Chức năng 1: Nhập và làm sạch dữ liệu

Yêu cầu người dùng nhập vào một đoạn log thô (có thể chứa ký tự rác như !, @, #, $).

Hệ thống gọi một hàm chuyên biệt để làm sạch:

- Sử dụng str.maketrans() và str.translate() để loại bỏ toàn bộ các ký tự đặc biệt (!@#$).
- Sử dụng split(';') (giả sử người dùng nhập nhiều log cách nhau dấu chấm phẩy) để tách chuỗi thành một danh sách (List).
- Lưu danh sách đã làm sạch vào biến toàn cục raw_logs.

'''
def handle_input_value(records):
    table = str.maketrans("", "", "@!#$")
    print("--- NẠP DỮ LIỆU LOG ---")
    data = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ").strip().translate(table)
    list_data = data.split(";")
    for index, value in enumerate(list_data):
        list_data[index] = value.strip()
        if list_data[index] == '':
            list_data.pop(index)
    if list_data[-1] == '':
        list_data.remove('')
    records.extend(list_data)
    print(f"Đã làm sạch và lưu {len(list_data)} dòng log vào hệ thống.")
    print(records)

'''
Chức năng 2: Lọc Log cảnh báo (List Comprehension) 

Hệ thống gọi một hàm để duyệt qua raw_logs.

Yêu cầu bắt buộc: Dùng List Comprehension để tạo ra một danh sách mới chỉ chứa những dòng log có chứa từ khóa "ERROR" hoặc "CRITICAL" (không phân biệt hoa thường).
Lưu kết quả vào biến processed_logs và in ra màn hình.

'''
def find_error(log_list, records):
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return
    search_list = [error for error in records if "ERROR" in error.upper() or "CRITICAL" in error.upper()]
    log_list.extend(search_list)
    if not log_list:
        print("Không có cảnh báo nguy hiểm nào")
        return
    print("--- LỌC CẢNH BÁO ---")
    print(f"Tìm thấy {len(log_list)} cảnh báo nguy hiểm:")
    print(log_list)


'''
Chức năng 3: Mã hóa địa chỉ IP 

Yêu cầu che giấu 2 dải số cuối của địa chỉ IP trong các log nguy hiểm để bảo mật thông tin trước khi xuất báo cáo. Hệ thống gọi một hàm để xử lý processed_logs:

- Duyệt qua từng chuỗi log. Sử dụng split() để tách các từ, tìm chuỗi có định dạng IP (chứa dấu chấm).
- Sử dụng replace() hoặc cắt chuỗi kết hợp join() để biến 192.168.1.1 thành 192.168.*.*.
- Bắt buộc Return danh sách log đã mã hóa và in ra.
'''
def processed_logs(records):
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return
    # 1. 192.168.1.1 Failed login
    for index, error in enumerate(records):
        records[index] = records[index].split(" ")
        for i,value in enumerate(records[index]):
            if value.count(".") == 3:
                records[index][i] = records[index][i].split(".")
                records[index][i][2] = "*"
                records[index][i][3] = "*"
                records[index][i] = ".".join(records[index][i])
        records[index] = " ".join(records[index])

    print(records)

def main():
    while True:
        choice = input("""
============= SECURITY LOG ANALYZER =============
1. Nhập và làm sạch dữ liệu Log thô
2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
3. Mã hóa địa chỉ IP (Masking)
4. Đóng hệ thống
=================================================
Chọn chức năng (1-4): """) 
        
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Vui lòng nhập số nguyên từ 1-4")
            continue
        
        match choice:
            case 1:
                handle_input_value(raw_logs)
                
            case 2:
                find_error(processed_logs, raw_logs)
                
            case 3:
                processed_logs(raw_logs)
            case 4:
                print("Thoát chương trình.")
                break
        
            case _:
                print("Lỗi cú pháp")
main()            