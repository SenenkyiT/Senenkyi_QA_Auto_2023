import pytest
from os import path 

# item exists and stored in specified directory
@pytest.mark.path
def test_item_exists():
    assert path.exists("/Users/pc-user/folder1/SenenkyiT_public_ssh_key.txt")

# item is a file with specified extension (text document)
@pytest.mark.path
def test_item_is_file():    
    assert path.isfile("/Users/pc-user/folder1/SenenkyiT_public_ssh_key.txt")

# item is a file with specified extension (picture)
@pytest.mark.path
def test_item_is_file2():    
    assert path.isfile("/Users/pc-user/Work/Other_stuff/Selection_420.png")