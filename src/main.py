import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.orm import create_table, insert_data

create_table()
insert_data()