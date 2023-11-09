project('k-lang', 'c', version : '0.1.0',
                 default_options : ['c_std=c11'])

gtk = dependency('gtk4')
sqlite = dependency('sqlite3')

src = ['main.c']

executable('k-lang', sources: src, dependencies : [gtk, sqlite])
