




# (StyleLabel, Background16, Foreground16, monochrome, Background256, Foreground256)
# Monochrome can be used to define styles (bold, underline, standout) only.
# 256 color is optional.
# http://urwid.org/manual/displayattributes.html

themes = {
    'dark':[
        ('bg',     'dark blue', 'black'),
        ('header', 'white',     'dark gray'),
        ('input',  'white',     'dark blue'),

        ('logged_input',    'dark magenta',  'black'),
        ('logged_response', 'light magenta', 'black'),

        ('error',     'yellow',     'dark red'),
        ('default',   'light gray', 'black'),
        ('severity0', 'dark blue',  'black'),
        ('severity1', 'dark green', 'black'),
        ('severity2', 'dark cyan',  'black'),
        ('severity3', 'light gray', 'black'),
        ('severity4', 'light red',  'black'),
        ('severity5', 'yellow',     'dark red'),
        ('highlight', 'black',      'yellow'),
  ],

  'light':[
        ('bg',     'dark blue', 'white'),
        ('header', 'black',     'light gray'),
        ('input',  'black',     'light gray'),

        ('logged_input',    'dark magenta',  'white'),
        ('logged_response', 'light magenta', 'white'),

        ('error',     'light red',  'yellow'),
        ('default',   'black',  'white'),
        ('severity0', 'light gray', 'white'),
        ('severity1', 'dark gray',  'white'),
        ('severity2', 'dark blue',  'white'),
        ('severity3', 'black',      'white'),
        ('severity4', 'dark red',   'white'),
        ('severity5', 'light red',  'white'),
        ('highlight', 'black',      'yellow'),
  ],

}
