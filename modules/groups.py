from libqtile import bar, layout, widget
from libqtile.command import lazy
from libqtile.config import DropDown, EzClick, EzKey, Group, Match, ScratchPad
from modules.keymaps import keys

import os

from modules.themes import palette

groups = [
    Group("1", label="",screen_affinity=0,layout="columns",init=True),
    Group("2", label="",screen_affinity=1,layout="verticaltile",init=True),
    Group("3", label="",screen_affinity=2,layout="verticaltile",init=True),
    Group("4", label="六",screen_affinity=0,layout="columns",init=True),
    Group("5", label="八",screen_affinity=0,layout="verticaltile",init=True),
    Group("6", label="九",screen_affinity=1,layout="verticaltile",init=True),
    # Group("7", label="六",screen_affinity=1,layout="monadtall",init=True),
    # Group("8", label="八",screen_affinity=2,layout="monadtall",init=True),
    # Group("9", label="九",screen_affinity=2,layout="monadtall",init=True),
    #Group("0", label="",screen_affinity=0,layout="plasma",init=True,persist=True),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            EzKey("M-%s" % i.name, lazy.group[i.name].toscreen()),
            # mod1 + shift + letter of group => move focused window to group
            EzKey("M-S-%s" % i.name, lazy.window.togroup(i.name)),
        ]
    )

borderline = dict(
    border_focus=palette[3],
    border_normal=palette[23],
    border_width=2,
    margin=15,
)


layouts = [
    layout.Tile(**borderline,expand=True,master_length=1,),
    layout.VerticalTile(**borderline),
    layout.Columns(**borderline,insert_position=1,num_columns=2),
]

# Automatically float application pop-ups
floating_layout = layout.Floating(
    **borderline,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_type="utility"),
        Match(wm_type="notification"),
        Match(wm_type="toolbar"),
        Match(wm_type="splash"),
        Match(wm_type="dialog"),
        Match(wm_class="file_progress"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(title="branchdialog"),  # gitk
        Match(wm_class="pinentry"),  # GPG key password entry
        Match(title="Picture-in-Picture"),  # FireFox
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="sun-awt-X11-XWindowPeer"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="python3.10"),
        Match(title="Android Emulator"),
    ],
)

# Scratchpads
# TODO: protonmail -> float on title recognition + scratchpad launch?
next_maximum = {
    "x": 0.02,
    "y": 0.02,
    "width": 0.95,
    "height": 0.95,
    "opacity": 0.95,
    "on_focus_lost_hide": False,
    "warp_pointer": True,
}

groups.append(
    ScratchPad(
        "SPD",
        [
            DropDown(
                "Alacritty",
                "alacritty",
                x= 0.003,
                y= 0.692,
                width= 0.993,
                height= 0.3,
                opacity= 0.95,
                on_focus_lost_hide= False,
                warp_pointer= True,
            ),
            DropDown(
                "WhatsApp",
                "whatsdesk",
                x= 0.3,
                y= 0.2,
                width= 0.4,
                height= 0.6,
                opacity= 0.95,
                on_focus_lost_hide= False,
                warp_pointer= True,
            ),
            DropDown(
                "Pamac",
                "pamac-manager",
                match=Match(wm_class="pamac-manager"),
                x= 0.20,
                y= 0.02,
                width= 0.6,
                height= 0.95,
                opacity= 0.95,
                on_focus_lost_hide= False,
                warp_pointer= True
            ),
            DropDown(
                "Nemo",
                "nemo",
                match=Match(wm_class="nemo"),
                **next_maximum,
            ),
            DropDown(
                "Spotify", 
                "spotify",
                x= 0.25,
                y= 0.02,
                width= 0.55,
                height= 0.95,
                opacity= 0.95,
                on_focus_lost_hide= False,
                warp_pointer= True
            ),
            DropDown(
                "Transmission",
                "transmission-gtk",
                x= 0.3,
                y= 0.2,
                width= 0.4,
                height= 0.6,
                opacity= 0.95,
                on_focus_lost_hide= False,
                warp_pointer= True,
            ),
            DropDown(
                "Volume Control",
                "pavucontrol",
                x= 0.3,
                y= 0.2,
                width= 0.4,
                height= 0.6,
                opacity= 0.95,
                on_focus_lost_hide= False,
                warp_pointer= True,
            ),
            DropDown(
                "Nitrogen",
                "nitrogen",
                x= 0.3,
                y= 0.2,
                width= 0.4,
                height= 0.6,
                opacity= 0.95,
                on_focus_lost_hide= False,
                warp_pointer= True,
            ),
        ],
        True
    )
)

keys.extend(
    [
        EzKey("M-A-t", lazy.group["SPD"].dropdown_toggle("Alacritty")),
        EzKey("M-A-w", lazy.group["SPD"].dropdown_toggle("WhatsApp")),
        EzKey("M-A-a", lazy.group["SPD"].dropdown_toggle("Pamac")),
        EzKey("M-A-e", lazy.group["SPD"].dropdown_toggle("Nemo")),
        EzKey("M-A-s", lazy.group["SPD"].dropdown_toggle("Spotify")),
        EzKey("M-A-d", lazy.group["SPD"].dropdown_toggle("Transmission"),),
        EzKey("M-A-v", lazy.group["SPD"].dropdown_toggle("Volume Control")),
        EzKey("M-A-n", lazy.group["SPD"].dropdown_toggle("Nitrogen")),
        EzKey("M-A-h", lazy.group["SPD"].hide_all()),
    ]
)