from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=10)


def icon(fg='text', bg='dark', fontsize=20, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=1
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=24,
        padding=0
    )

def powerline2(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_right
        fontsize=24,
        padding=0
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='MesloLGS NF',
            fontsize=20,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='line',
            # urgent_alert_method='text',
            # urgent_border=colors['grey'],
            this_current_screen_border=colors['light'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
    ]

def longNameParse(text): 
    for string in ["Brave", "Firefox"]: 
        if string in text:
            text = string
        else:
            text = text
    return text

#----------------------------PRIMARY WIDGETS----------------------------

primary_widgets = [

    # ------Arch LOGO------

    icon(fg="archlogo", bg="dark", text='  ', fontsize=26), 

    powerline2('dark', 'color1'),

    # ------Clock------

    widget.Clock(**base(bg='color1'), format='  %H:%M   %d/%m/%Y '),

    powerline2('color1', 'dark'),

    # ------Workspaces------

    *workspaces(),


    # ------WindowName------

    widget.WindowName(
        **base(fg='focus'), 
        fontsize=12, 
        padding=5,
        parse_text=longNameParse,
    ),


    # ------Updates------

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates} ',
        update_interval=1800,
        custom_command='checkupdates',
        padding=5,
    ),

    # ------Current Layout------

    powerline('color3', 'color4'),
    
    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.60),

    widget.CurrentLayout(**base(bg='color3'), padding=6),


    # ------Net------

    powerline('color2', 'color3'),

    icon(bg="color2", text='  '),  

    widget.Wlan(
        **base(bg='color2'),
        interface='wlan0',
        format='{essid} Q:{percent:2.0%} | ',
        disconnected_message='No WLAN signal | ',
        update_interval=5
    ),

    widget.Net(
        **base(bg='color2'),
        interface='enp4s0',
        format=' {total} ',
        update_interval=2,
    ),

    # ------CPU: Temperature-----

    powerline('color5', 'color2'),

    icon(bg="color5", text=' '), 

    widget.ThermalZone(
        **base(bg='color5'),
        fgcolor_normal="#0f101a",
        high=65,
        fgcolor_high="#c43d10",
        crit=80,
        fgcolor_crit="#f70505",
        format=' {temp}°C  ',
        update_interval=5,
    ),

    # ------CPU: Load-----

    icon(bg="color5", text=''), 

    widget.CPU(
        **base(bg='color5'),
        format=' {load_percent}%  ',
        update_interval=5,
    ),

    # ------CPU: Memory-----

    icon(bg="color5", text=''), 

    widget.Memory(
        **base(bg='color5'),
        measure_mem='M',
        format=' {MemUsed:.0f} {mm}B  ',
        update_interval=5,

    ),

    # ------Backlight------

    powerline('dark', 'color5'),
   
    icon(fg="light", bg="dark", text=' '),

    separator(),

    widget.Backlight(
        backlight_name="intel_backlight", 
        **base(fg='light', bg='dark'),
    ),

    # ------Volume------

    separator(),
    separator(),

    icon(fg="light", bg="dark", text=''),

    separator(),

    # widget.PulseVolume(
    #     update_interval=0.01, 
    #     **base(fg='light', bg='dark')
    # ),

    # ------Battery------

    separator(),
    separator(),

    widget.Battery(
        format="{char} {percent:2.0%}", 
        **base(fg='light', bg='dark'),
        update_interval=10,
        low_percentage=0.20,
        low_foreground="#f70505",
        discharge_char=' ',
        charge_char=' ',
    ),

    separator(),

    # ------Systray------

    widget.Systray(background=colors['dark'], padding=5),

    separator(),

    

]

#----------------------------SECONDARY WIDGETS----------------------------

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

#----------------------------CONFIG WIDGETS----------------------------

widget_defaults = {
    'font': 'MesloLGS NF Bold', 
    'fontsize': 12,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
