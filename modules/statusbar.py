from libqtile import bar, qtile, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from modules.groups import borderline

from qtile_extras import widget as widgetx
from qtile_extras.widget.decorations import PowerLineDecoration

import os

from modules.themes import palette

fontinfo = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=7,
)

rofi = "rofi -no-lazy-grab -show drun -modi drun"

def colorstr(color,symbol,params):
    return f"<span size='large' foreground='{color}'>{symbol}</span> <span rise='1pt'>{params}</span>"

sl = [
    widgetx.Spacer,
    {
        "left":True,
        "background": palette[25],
        "foreground": palette[11],
    }
]

sr = [
    widgetx.Spacer,
    {
        "right":True,
        "background": palette[25],
        "foreground": palette[11],
    }
]

groupbox = [
    widgetx.GroupBox,
    {
        "background": palette[21],
        "active": palette[14],
        "block_highlight_text_color": palette[20],
        "this_current_screen_border": palette[3],
        "this_screen_border":palette[8],
        "highlight_color":palette[21],
        "other_screen_border": palette[11],
        "other_current_screen_border":palette[9],
        "disable_drag": True,
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"],
        "hide_unused": True,
        "highlight_method": "block",
        "inactive": palette[15],
        "use_mouse_wheel": True,
        "borderwidth":10,
        # "fontshadow": palette[25],
        "right": True,
    },
]

windowname = [
    widgetx.WindowName,
    {
        "background": palette[24],
        "foreground": palette[14],
        # "center_aligned": True,
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"],
        "width": 300,
        "fmt": "{}",
        "format": "  {name}",
        "empty_group_string": "",
        "max_chars": 0,
        "padding": 10,
        # "max_chars": 200,
        "scroll": True,
        "mouse_callbacks": {"Button1": lazy.spawn("rofi -show windowcd")},
        "right": True
    },
]

systray = [
    widgetx.Systray,
    {
        "background": palette[20],
        "foreground": palette[3],
        # "theme_path": "/usr/share/icons/Papirus-Dark",
        "padding": 15,
        "icon_size":15,
        # "use_mask": True,
        "left": True
    },
]


logo = [
    widgetx.TextBox,
    {
        "font": fontinfo["font"],
        "background": palette[20],
        "fontsize": fontinfo["fontsize"] * 1.5,
        "foreground": palette[3],
        "mouse_callbacks": {"Button1": lazy.spawn(os.path.expanduser("~/.config/rofi/bin/launcher"))},
        "padding": 20,
        "text": "",
        "fontshadow": palette[23],
        "right": True,
    },
]

dash = [
    widgetx.TextBox,
    {
        "font": fontinfo["font"],
        "background": palette[20],
        "fontsize": fontinfo["fontsize"] * 1.5,
        "foreground": palette[3],
        "mouse_callbacks": {"Button1": lazy.spawn(os.path.expanduser("~/.config/qtile/Scripts/player"))},
        "padding": 20,
        "text": "",
        "fontshadow": palette[23],
        "right": True,
    },
]

power = [
    widgetx.TextBox,
    {
        "font": fontinfo["font"],
        "background": palette[19],
        "fontsize": fontinfo["fontsize"]*1.5,
        "foreground": palette[5],
        "fontshadow": palette[23],
        "mouse_callbacks": {"Button1": lazy.spawn(os.path.expanduser("~/.config/rofi/bin/powermenu"))},
        "padding": 10,
        "text": " ",
        # "right": True
    },
]

layout = [
    widgetx.CurrentLayout,
    {
        **fontinfo,
        "background": palette[22],
        "foreground": palette[14],
        # "scale": 0.60,
        # "use_mask": True,
        "right": True
    },
]

windowcount = [
    widgetx.WindowCount,{
        "text_format":'缾 {num}',
        "background":palette[23],
        "foreground":palette[14],
        "show_zero":True,
        "right": True
    },
]

openwin = [
    widgetx.TaskList,{
        "background": palette[23],
        "foreground": palette[14],
        "highlight_method":"block",
        "border": palette[21],
        "fontsize": fontinfo["fontsize"]-4,
        # "margin_y": 0,
        # "padding_y": 0,
        # "max_title_width": 150,
        "markup": True,
        "theme_path":"/usr/share/icons/ePapirus-Dark",
        "icon_size":fontinfo["fontsize"]+3,
        "theme_mode": "preferred",
        # "markup_floating":"<span>{}</span>",
        "markup_focused":"<b>{}</b>",
        "markup_maximized":"<span>{}</span>",
        "markup_minimized":"<s>{}</s>",
        "markup_normal":"<span>{}</span>",
        "right": True
    }
]

volume = [
    widgetx.ALSAWidget,{
        "mode": "both",
        "background":palette[21],
        "bar_colour_high":palette[7],
        "bar_colour_loud":palette[4],
        "bar_colour_normal":palette[8],
        "bar_colour_mute":palette[21],
        "bar_width": 100,
        "update_interval": 0.1 ,
        "margin_y": 5,
        "foreground":palette[14],
        # "scroll":True,
        "text_format": '{volume}%',
        "font":fontinfo["font"],
        "fontsize":fontinfo["fontsize"],
        "emoji":True,
        "theme_path":"/usr/share/icons/Papirus-Dark",
        "volume_app": "pavucontrol",
        "right": True
    },
]

checkupdates = [
    widgetx.CheckUpdates,{
        "background":palette[24],
        "foreground":palette[14],
        "colour_no_updates":palette[14],
        "colour_have_updates":palette[14],
        "markup":True,
        "display_format": colorstr(palette[5],"","{updates}"),
        "no_update_string": colorstr(palette[9],"","0"),
        "distro": "Arch_yay",
        "left": True
    },
]

cpu = [
    widgetx.CPU,
    {
        **fontinfo,
        "background": palette[21],
        "foreground": palette[14],
        "format": colorstr(palette[6],"","{freq_current}GHz {load_percent}%"),
        "markup": True,
        "left": True
    },
]

net = [
    widgetx.Net,
    {
        **fontinfo,
        "background": palette[23],
        "foreground": palette[14],
        "format": colorstr(palette[7],"","{up} 李 {down}"),
        "interface": "enp5s0",
        "update_interval": 3,
        "left": True
    },
]

mem = [
    widgetx.Memory,
    {
        **fontinfo,
        "background": palette[22],
        "foreground": palette[14],
        "format": colorstr(palette[8], "", '{MemUsed:.2f}|{MemTotal:.2f}{mm}'),
        "measure_mem": "G",
        "update_interval": 1.0,
        "left": True
    },
]

mpris = [
    widgetx.Mpris2,
    {
        **fontinfo,
        "foreground": palette[14],
        "background": palette[22],
        "markup": True,
        "fmt": colorstr(palette[8], "懶","  {}"),
        "left": True,
        "width": 250,
        "display_metadata": ['xesam:title','xesam:artist'],
        "scroll": True,
        "mouse_callbacks": {"Button1": lazy.spawn(os.path.expanduser("~/.config/qtile/Scripts/player"))},
    },
]


datetime = [
    widgetx.Clock,
    {
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"],
        "background": palette[20],
        "foreground": palette[14],
        "markup": True,
        "format": colorstr(palette[11], "", '<b><span rise="1pt"> %a %d/%m/%Y</span></b>  '),
        "mouse_callbacks": {"Button1": lazy.spawn(os.path.expanduser("~/.config/qtile/Scripts/calendar"))},
        # "left": True
    },
]

clock = [
    widgetx.Clock,
    {
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"],
        "background": palette[25],
        "foreground": palette[14],
        "format": '<b>%I:%M %p</b>',
        # "right": True
    },
]

vpn = [
    widgetx.Image,
    {
        "background": palette[20],
        "filename": "/home/stavox/.config/qtile/icons/nord.svg",
        "mouse_callbacks": {"Button1": lazy.spawn(os.path.expanduser("~/.config/qtile/Scripts/nord"))},
        "margin": 5,
        "scale": True,
        "right": True,
    },
]


def widgetlist(primary=False, top=True):
    widgets =  [
        logo,
        groupbox,
        layout,
        windowcount,
        # openwin,
        windowname,
        sl,
        clock,
        sl,
        mpris,
        systray,
        power
    ]

    b_widgets =  [
        vpn,
        sr,
        sl,
        checkupdates,
        net,
        mem,
        cpu,
        datetime
    ]
    if not(primary):
        widgets.remove(systray)
    if (top):
        return widgets
    else:
        return b_widgets


def style(widgetlist, primary=False):
    styled = widgetlist[:]

    for index, wid in enumerate(widgetlist):

        plr = dict(
            decorations=[
                PowerLineDecoration(path="arrow_right")
            ]
        )

        pll = dict(
            decorations=[
                PowerLineDecoration(path="arrow_left")
            ]
        )
        if not(primary):
            styled[index][1].update([("fontsize",fontinfo["fontsize"] + 10)])
        
        if widgetlist[index][1].get("right"):
            styled[index][1].update(pll)
        elif widgetlist[index][1].get("left"):
            styled[index][1].update(plr)

    return [w[0](**w[1]) for w in styled]


def my_bar(primary=False, h=34, pos=True):
    if(pos):
        margin = [15,15,0,15]
    else:
        margin = [0,15,15,15]

    return bar.Bar(
        [*style(widgetlist(primary, pos),primary)],
        h,
        foreground=palette[14],
        background=palette[23],
        #background='#00000009',
        margin=margin,
        opacity=1
    )


widget_defaults = dict(
    **fontinfo,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=my_bar(primary=True,pos=True),
        bottom=my_bar(primary=True, pos=False)
    ),
    Screen(top=my_bar(primary=False)),
    Screen(top=my_bar(primary=False)),
    Screen(top=my_bar(primary=False))
]
