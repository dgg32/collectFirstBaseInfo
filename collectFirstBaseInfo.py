#collect firstBaseInfo

#usage: python collectFirstBaseInfo.py 'Result/OutputFq/' '/home/huangsixing/where_you_collect_the_output'

import sys
import shutil
from pathlib import Path
import os

outputfq_path = sys.argv[1]
collect_path = sys.argv[2]

p = Path(outputfq_path)

for f in p.glob('**/firstBaseInfo.csv'):
    fields = str(f).split("/")
    slide = fields[-3]
    lane = fields[-2]
    name = fields[-1]

    shutil.copy2(f, os.path.join(collect_path, f"{slide}_{lane}_{name}"))