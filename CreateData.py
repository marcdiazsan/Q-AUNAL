from dataScrambler import DataCreator
from time import perf_counter

init_time = perf_counter()
creator = DataCreator()
creator.createData(1000, 50)
end_time = perf_counter()
print("1000 preguntas cada una con 50 comentarios en {} segundos".format(end_time-init_time))