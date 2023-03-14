

def process_data(data_list):
    row_count = len(data)
    col_count = len(data[0])
    new_data_list = []
    for y in range(col_count):
        new_row = []
        for x in range(row_count):
            new_data = data_list[x][y]
            new_row.append(new_data)
        new_data_list.append(new_row)
    return new_data_list
    
    

if __name__ == '__main__':
    data = [
     ['1a', '1b', '1c', '1d', '1e'],
     ['2a', '2b', '2c', '2d', '2e'],
     ['3a', '3b', '3c', '3d', '3e'],
    ]
    
    print(f"Original Data - {data}")
    print(f"Columns To Rows - {process_data(data)}")
    print()
    
    data = [
     ['1a', '1b', '1c'],
     ['2a', '2b', '2c'],
     ['3a', '3b', '3c'],
     ['4a', '4b', '4c'],
     ['5a', '5b', '5c']
    ]
    
    print(f"Original Data - {data}")
    print(f"Columns To Rows - {process_data(data)}")
