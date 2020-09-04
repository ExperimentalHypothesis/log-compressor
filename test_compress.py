import pytest, os
from compress import compress_to_gzip

def test_compress():
    """ 
    Make a testlog folder with couple of subfolders and files.
    Check there are files with .txt and no .gz extension.
    Run the function.
    Check there are files with .gz and no .txt extension.
    """

    try:
        os.mkdir("testlog")
        os.mkdir("testlog/service_one")
        os.mkdir("testlog/service_two")
        with open("testlog/service_one/test_log1.txt", 'w') as file:
            file.write("first test...")
        with open("testlog/service_two/test_log2.txt", 'w') as file:
            file.write("second test..")
        with open("testlog/log.txt", 'w') as file:
            file.write("another test...")
    except:
        pass

    for pth, dirs, folders in os.walk("log"):
        for file in folders:
            assert os.path.isfile(os.path.join(pth, file))
            assert file.endswith(".txt") == True
            assert file.endswith(".gz") == False

    compress_to_gzip("testlog")

    for pth, dirs, folders in os.walk("testlog"):
        for file in folders:
            assert os.path.isfile(os.path.join(pth, file))
            assert file.endswith(".txt") == False
            assert file.endswith(".gz") == True   


    
