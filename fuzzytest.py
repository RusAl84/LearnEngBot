from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.WRatio('Плохое начало ведет к плохому концу', 'Плохое начало не к доброму концу')
print(a)
a = fuzz.WRatio('Плохое начало ведет к плохому концу', 'Плохое начало ведет не к доброму концу')
print(a)