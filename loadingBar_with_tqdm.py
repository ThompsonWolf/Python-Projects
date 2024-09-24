"""
======================================================================================================================
Author:                         {root@lonedevwolf}
Language:                       Python
Modules:
Description:
======================================================================================================================
[!]:

"""
from tqdm import tqdm
import time

for i in tqdm(range(100), desc="Loading...", ascii=False, ncols=100):
    time.sleep(0.1)
    print("Complete")
