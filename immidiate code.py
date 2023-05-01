print("1. Assignment\n2. Arithmetic\n3. Relation\n4. Exit")

while True:
    n = int(input("\n Enter your choice: "))
    match n:
        case 1:
            three_addr_code = input("Enter the Assignment operation: ")
            temp1,temp2 = three_addr_code.split('=')
            print(f'temp={temp2}')
            print(f'{temp1}=temp')
        case 2:
            three_addr_code = input("Enter the arithmatic operation: ")
            temp1,temp2 = three_addr_code[:3],three_addr_code[3:]
            print(f'temp={temp1}')
            print(f'temp1=temp{temp2}')
        case 3:
            three_addr_code = input("Enter relational expression: ")
            addr = 100
            print(f'{addr} if {three_addr_code} goto {addr+3}')
            addr+=1
            print(f'{addr} T=0')
            addr+=1
            print(f'{addr} goto {addr+2}')
            addr+=1
            print(f'{addr} T=1')
        case 4:
            break