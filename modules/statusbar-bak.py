# credits: the-argus
# TODO: my own statusbar, use this to setup qtile for now.

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

spacer = [
    widgetx.Spacer,{"left":True}
]

groupbox = [
    widgetx.GroupBox,
    {
        #"active": palette[15],
        "block_highlight_text_color": palette[24],
        "disable_drag": True,
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"] + 4,
        "hide_unused": True,
        "highlight_method": "block",
        "inactive": palette[15],
        "spacing": 5,
        "margin_x":15,
        "this_current_screen_border": palette[4],
        "other_screen_border": palette[17],
        "urgent_alert_method": "line",
        "urgent_border": palette[6],
        "urgent_text": palette[7],
        "use_mouse_wheel": True,
        "right": True,
    },
]

windowname = [
    widgetx.WindowName,
    {
        "background": palette[23],
        # "center_aligned": True,
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"],
        "markup": True,
        "fmt": "{}",
        "format": "{name}",
        "max_chars": 0,
        "padding": 30,
        "scroll": True,
        "mouse_callbacks": {"Button1": lazy.spawn("rofi -show windowcd")},
        "left": True
    },
]

systray = [
    widgetx.Systray,
    {
        "background": palette[23],
        "theme_path": "/usr/share/icons/Papirus-Dark/",
        "padding": 20,
        "left": True
    },
]


logo = [
    widgetx.TextBox,
    {
        "font": fontinfo["font"],
        "background": palette[14],
        "fontsize": fontinfo["fontsize"] * 2,
        "foreground": palette[23],
        "mouse_callbacks": {"Button1": lazy.spawn(os.path.expanduser("~/.config/rofi/bin/launcher"))},
        "padding": 0,
        "text": "  ᛝ  ",
        "right": True,
    },
]

power = [
    widgetx.TextBox,
    {
        "font": fontinfo["font"],
        "background": palette[5],
        "fontsize": fontinfo["fontsize"] * 1.8,
        "foreground": palette[23],
        "mouse_callbacks": {"Button1": lazy.spawn(os.path.expanduser("~/.config/rofi/bin/powermenu"))},
        "padding": 10,
        "text": "  ",
        # "right": True
    },
]

layout = [
    widgetx.CurrentLayoutIcon,
    {
        **fontinfo,
        "background": palette[9],
        "foreground": palette[23],
        # "custom_icon_paths": "./icons",
        "scale": 0.60,
        "use_mask": True,
        "right": True
    },
]

cpu = [
    widgetx.CPU,
    {
        **fontinfo,
        "background": palette[10],
        "foreground": palette[23],
        "format": " {freq_current}GHz {load_percent}%",
        "left": True
    },
]

net = [
    widgetx.Net,
    {
        **fontinfo,
        "background": palette[3],
        "foreground": palette[23],
        "format": "{up} 李{down}",
        "interface": "enp5s0",
        "update_interval": 3,
        "left": True
    },
]

mem = [
    widgetx.Memory,
    {
        **fontinfo,
        "background": palette[4],
        "foreground": palette[23],
        "format": " {MemUsed:.2f}/{MemTotal:.2f}{mm}",
        "measure_mem": "G",
        "update_interval": 1.0,
        "left": True
    },
]

mpris = [
    widgetx.Mpris2,
    {
        **fontinfo,
        "foreground": palette[23],
        "background": palette[7],
        "max_chars": 300,
        "paused_text": " {track}",
        "playing_text": " {track}",
        "left": True,
        "name":"spotify",
        "width": 200
    },
]


datetime = [
    widgetx.Clock,
    {
        "font": fontinfo["font"],
        "fontsize": fontinfo["fontsize"] + 2,
        "background": palette[6],
        "foreground": palette[24],
        "format": "%B %d, %H:%M:%S",
        "left": True
    },
]


def widgetlist(primary=False):
    widgets =  [
        logo,
        groupbox,
        layout,
        # spacer,
        windowname,
        spacer,
        mpris,
        cpu,
        net,
        mem,
        systray,
        datetime,
        power
    ]
    if not(primary):
        widgets.remove(systray)
        widgets.remove(mem)
        widgets.remove(mpris)
        widgets.remove(net)
        widgets.remove(cpu)
        # widgets.remove(spacer)
        # widgets.remove(spacer)

    return widgets


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


def my_bar(primary=False, h=34):
    return bar.Bar(
        [*style(widgetlist(primary),primary)],
        h,
        foreground=palette[14],
        background=palette[23],
        # background='#00000009',
        margin=[
            borderline["margin"],
            borderline["margin"],
            borderline["border_width"],
            borderline["margin"],
        ],
        opacity=1
    )


widget_defaults = dict(
    **fontinfo,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=my_bar(primary=True)),
    Screen(bottom=my_bar(primary=False, h=50)),
    Screen(bottom=my_bar(primary=False, h=50)),
    Screen(bottom=my_bar(primary=False, h=50))
]
