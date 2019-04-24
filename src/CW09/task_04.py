names = ['sergey', 'nikita']
print([(lambda name: f'Hello {name}')(name) for name in names])
print(( lambda names : [f'Hello {name}' for name in names])(names))

