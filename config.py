# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
colorN = "#32CD32"
colorF = "#006400"
colorBarra = "#17202a"
fontDefault = "nerd fonts ubuntu mono"
# modified icon size a your like
iconSize = 18 
# color background 
color_bg = "#00c2f7"
terminal = "alacritty"
sizeicon = 33
color1 = "#a9cce3"
color2 = "#7fb3d5"
color3 = "#5499c7"
color4 = "#3498db"
color5 = "#2e86c1"
dispositive_net = "wlan0"

def fc_separator():
    return widget.Sep(
        padding = 5,
        linewidth = 0,
        #background = "",
    )

def fc_rectangulo(color1,color2):    
    return widget.TextBox(
        text = "",
        fontsize = sizeicon,
        foreground = color1,
        padding = 0,
        #padding = 0,
        background = color2,
    )


    #function write text in icons
def fc_icono(icono, color_group):
    return widget.TextBox(
        text = icono,
        foreground = "#ffffff",
        background =color_group,
        # fontsize = 0,
    )

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    #screenshots screen
    Key([mod], "s", lazy.spawn("scrot"), desc="screenshot"),

    #screenshots screen select
    Key([mod, "shift"], "s", lazy.spawn("scrot -s"), desc="screenshot windows select"),
    
    #nautilus
    Key([mod], "e", lazy.spawn("nautilus"), desc="File nautilus"),

    # volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="- volumen"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="+ volumen"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="mute volumen"),

    #brightness of the screen
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="+ brightness of the screen"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="- brightness of the screen"),
    
    # start Rofi -show drun
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Start menu"),
    
    # start visual studio code
    Key([mod], "v", lazy.spawn("code"), desc="Visual Studio Code"),
    # controlers sound alsa-utils
#     keys= [
#     #...
#     # Sound
#     Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
#     Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
#     Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute"))
#    ]
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in 
    [
        # nerd fonts your like icons copy in www.nerdfonts.com 
        # but first download and install ubuntu mono font 
        # https://aur.archlinux.org/packages/nerd-fonts-ubuntu-mono/
        "","","","","","漣",
    ]
]

for i, group in enumerate(groups):
    numeroEscritorio = str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], numeroEscritorio, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], numeroEscritorio, lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(
        #border_normal = colorN,
        border_focus = colorF, 
        border_width=2,
        #margin = 2,
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
      layout.Matrix(
          #border_normal = colorN,
          border_focus = colorF,
          margin = 3,
          border_width = 2,  
      ),
      layout.MonadTall(
          single_border_width = 0,
          border_width = 2,
          #border_normal = colorN,
          border_focus = colorF,
          single_margin = 0,
          margin = 3,
      ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=fontDefault,
    fontsize=15,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                
                widget.GroupBox(
                    fontsize = iconSize,
                    borderwidth = -1,
                    highlight_method='block',
                    update_interval = 0.5,
                    urgent_border = color5,
                    this_current_screen_border = color5,
                    padding = 10,                     
                ),
                
                fc_separator(),
                widget.TextBox(
                    text = "",
                ),
                
                widget.Prompt(),
                widget.WindowName(),
                
                #fc_rectangulo(color_bg,0),
                fc_rectangulo(color_bg , colorBarra),
                fc_icono("",color_bg),
                widget.ThermalSensor(
                    background = color_bg,
                    fontsize = sizeicon - 20,
                    threshold = 50,
                    tag_sensor = "Core 0",
                    fmt = '{}'
                ),
                fc_rectangulo(color5,color_bg),
                fc_icono("龍",color5),
                widget.Net(
                    fontsize = sizeicon - 20,
                    background = color5,
                    format = '{down} {up}',
                    interface = dispositive_net,
                    use_bits = 'true',
                ),
                fc_rectangulo(color3, color5),
                fc_icono("",color3),
                widget.Memory(
                    background = color3,
                    padding = 4,
                    fontsize = sizeicon - 20,
                ),
                fc_rectangulo(color2, color3),
                fc_icono("",color2),
                widget.Clock(
                    format = '%d / %m / %Y - %I:%M %p',
                    #format='%Y/%m/%d - %I:%M %p',
                    background = color2,
                    fontsize = sizeicon - 20,
                ),
                
                #widget.QuickExit(),
                fc_rectangulo("#154360", color2),
                widget.CurrentLayoutIcon(
                    background = "#154360",
                    scale = 0.5,
                ),
                widget.CurrentLayout(
                    background = "#154360",
                ),
                #fc_rectangulo(colorBarra,),
                fc_rectangulo( color5, "#154360"),
                fc_icono("",color5),
                widget.PulseVolume(
                    background = color5,
                    limit_max_volume = True,
                    fontsize = sizeicon - 23,
                    volume_down_command = True,
                    volume_up_command = True,
                ),
                fc_rectangulo(color3,color5),
                widget.BatteryIcon(
                    background = color3,
                    mouse_callbacks = {},
                  
                    
                ),
                widget.Battery(
                    background = color3,
                    fontsize = sizeicon - 20,
                    format = '{char} {percent:2.0%}',
                    charge_char='',
                    discharge_char='',
                    fmt = '{}',
                ),
                fc_rectangulo(colorBarra,color3),
                widget.Systray(
                    icon_size = 20,
                ),
                fc_separator(),
            ],
            24,
            background = colorBarra,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

inicio = [
    "feh --bg-fill /home/adder/Pictures/ArchLinux.jpg",
    "picom &"
    "nm-applet &"
]

for item in inicio:
    os.system(item)