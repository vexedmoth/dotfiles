
# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod1"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows 
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "space", lazy.layout.next()),

    # Shuffle windows
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),

    # Normalize windows
    ([mod], "n", lazy.layout.normalize()),

    # Maximize focus window
    ([mod], "period", lazy.window.toggle_fullscreen()),
    
    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Toggle Stack mode
    ([mod], "Return", lazy.layout.toggle_split()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Qtile restart and shutdown
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),

    # ------------ App Configs ------------

    # Rofi
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # Terminal
    ([mod], "i", lazy.spawn("alacritty")),

    # Screenshot
    ([], "Print", lazy.spawn("scrot /home/vexedmoth/Screenshots/%b%d::%H%M%S.png")),

    # Spotify
    ([], "Delete", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),
    ([], "Prior", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),
    ([], "Next", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),



    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioRaiseVolume", lazy.spawn("changevolume up")),
    ([], "XF86AudioLowerVolume", lazy.spawn("changevolume down")),
    ([], "XF86AudioMute", lazy.spawn("changevolume mute")),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("changebrightness up")),
    ([], "XF86MonBrightnessDown", lazy.spawn("changebrightness down")),
]]
