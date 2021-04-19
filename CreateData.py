from dataScrambler import DataCreator
from time import perf_counter

init_time = perf_counter()
creator = DataCreator()
creator.createData(2500000, 4)
end_time = perf_counter()
