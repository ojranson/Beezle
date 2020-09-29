import json
import collections

with open('res/ships/cruiser.json') as json_file:
  data = json.load(json_file)

  results = []
  result_string = ''
  count = 0
  for ship_name, ship_info in data.items():
    count += 1
    if count == 1:
      old_value = ship_info['TechLevel']
    else:
      if old_value != ship_info['TechLevel']:
        results.append(result_string)
        old_value = ship_info['TechLevel']
        result_string = ''

      result_string += '\n{}'.format(ship_name)

      for key in ship_info:
        if ship_info[key] != None:
          result_string += '\n  {}: {}'.format(key, ship_info[key])
      result_string += '\n'


  
  print(results[1])
  #print(result_string)

