import os

def find_files(suffix, path):
  

    if path is None:
        return []
    if not is_directory(path):
        return []

    directories = []

    
    
    if path and suffix:
        directories.append(path)
    else:
        directories = None

    files = []

    while directories:

        folder = os.path.join(directories.pop(0))



        folder_content = os.listdir(folder)
        for content in folder_content:
            
            if is_file(folder + content, suffix):
                files.append(content)
            elif is_directory(folder + content):
                directories.append(folder + content)
    return files

def is_file(new_path, suffix):
    return new_path.endswith(suffix)

def is_directory(directory):
    return os.path.isdir(directory)


        
# tets
def test_find_all_files_with_c_suffix():
    
    result = find_files('.c', 'testdir')

    expected_result = ['t1.c', 'a.c', 'a.c', 'b.c']

    if len(result)==4 and result == expected_result: 
        result = "Pass"
    else:
        result = "Fail"
        
    print("test_find_all_files_with_c_suffix {}".format(result))
    #['t1.c', 'a.c', 'a.c', 'b.c']

def test_find_all_files_with_h_suffix():
    
    result = find_files('.h', 'testdir')

    expected_result = ['t1.h', 'a.h', 'a.h', 'b.h']

    if len(result)==4 and result == expected_result: 
        result = "Pass"
    else:
        result = "Fail"
        
    print("test_find_all_files_with_h_suffix {}".format(result))
    
def test_find_all_files_with_h_suffix_insubdir():
    
    result = find_files('.h', 'testdir/subdir1')

    expected_result = ['a.h']

    if len(result)==1 and result == expected_result: 
        result = "Pass"
    else:
        result = "Fail"
        
    print("test_find_all_files_with_h_suffix_insubdir {}".format(result))

def test_find_files_with_none_dir():
    
    result = find_files('.h', None)

    expected_result = []

    if len(result)==0 and result == expected_result: 
        result = "Pass"
    else:
        result = "Fail"
        
    print("test_find_files_with_none_dir {}".format(result))
    
def test_find_files_with_none_suffix():
    
    result = find_files(None, 'testdir')

    expected_result = []

    if len(result)==0 and result == expected_result: 
        result = "Pass"
    else:
        result = "Fail"
        
    print("test_find_files_with_none_suffix {}".format(result))

def test_find_files_where_the_directory_path_should_be_path_of_a_file():
    
    result = find_files('.c', 'testdir/t1.c')

    expected_result = []

    if len(result)==0 and result == expected_result: 
        result = "Pass"
    else:
        result = "Fail"
        
    print("test_find_files_where_the_directory_path_should_be_path_of_a_file {}".format(result))

test_find_all_files_with_c_suffix()
# ['t1.c', 'a.c', 'a.c', 'b.c']
test_find_all_files_with_h_suffix()
#  ['t1.h', 'a.h', 'a.h', 'b.h']
test_find_all_files_with_h_suffix_insubdir()
# ['a.h']
test_find_files_with_none_dir()
# []
test_find_files_with_none_suffix()
# []
test_find_files_where_the_directory_path_should_be_path_of_a_file()
# []