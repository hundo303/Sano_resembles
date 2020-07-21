import sano
import comparison
import pprint

target_year = 2019

sano_list = sano.sano_list(target_year)
point_list = comparison.comparison(sano_list, target_year - 1)

pprint.pprint(point_list)
