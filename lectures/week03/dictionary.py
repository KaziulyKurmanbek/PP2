ourdict={
    'mark' : 'Toyota',
    'year' : 2010,
    'cost' : '7 million'
}
print(ourdict)

ourdict['milleage'] = 808500
ourdict['mark'] = 'mers'
for key in ourdict:
    print(key, ourdict[key])