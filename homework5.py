my_list = ['apple ', 'chery ', 'coconut ', 'purple ', 'orange ']
print(my_list)
print('First element: ' + my_list[0])
print('Last element: ' + my_list[4])
print('sublist: ', my_list[2:5])
my_list[2] = 'carrot'
print(my_list)

my_dict = {'table' :'стол', 'chair' : 'стул', 'sofa' : 'диван'}
print('Dictionary: ',  my_dict)
print('Translation: ', my_dict.get('sofa'))
my_dict = {'table' :'стол', 'chair' : 'стул', 'sofa' : 'диван', 'lamp' : 'свет'}
print('Modified dictionary: ', my_dict)