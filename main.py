import sano_2019
import comparison
import pprint

sano_list = sano_2019.sano_list('2019')
point_list = comparison.comparison(sano_list, '2018')

pprint.pprint(point_list)
