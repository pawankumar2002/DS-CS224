import pandas as pd
import json

india_states = json.load(open('states_india.geojson', 'r'))

print(india_states['features'][0])
