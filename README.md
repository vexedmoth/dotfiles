# Arch Linux setup and configuration

## PRE-BUILD 
- Configure [iwd](https://wiki.archlinux.org/title/iwd). Is a wireless daemon that works with network managers like systemd-networkd or NetworkManager
- []()
nvidia drivers propietary
alacritty
qtile
git

Right after a complete clean Arch based distro installation, we will follow this steps:

## Add user to wheel group
As root, we need to add vexedmoth user to the "wheel group" in order to grant sudo permissions. 

```zsh
usermod -aG wheel vexedmoth
```
Then open the `/etc/sudoers` file and uncomment the following line:

```bash
%wheel ALL=(ALL) ALL
```

## Enable GRUB os-prober
If we are using dual boot and the GRUB bootloader does not detect automatically other OS, then we need to install:
- [os-prober](https://archlinux.org/packages/?name=os-prober) (detect other distros using a dual boot system)
- [ntfs-3g](https://wiki.archlinux.org/title/NTFS-3G) (read NTFS files like UEFI boot file from other OS like Windows)

After that, open the `/etc/default/grub` file and uncomment the following line:

```bash
GRUB_DISABLE_OS_PROBER=false
```

## Enable Touchpad Tap
Check if [libinput](https://wiki.archlinux.org/title/libinput) is installed in our system. If not, install it.

List devices and check if touchpad is listed. 

```zsh
sudo libinput list-devices
```
If is not listed, create a config file named `30-touchpad.conf` in `/etc/X11/xorg.conf.d/` and add this lines:

```
Section "InputClass"
Identifier "touchpad"
Driver "libinput"
  MatchIsTouchpad "on"
  Option "Tapping" "on"
  Option "NaturalScrolling" "on"
  Option "ClickMethod" "clickfinger"
EndSection
```
Reboot the system. 


## Enable suspend 
By default, the system may not suspend on lid close or powerkey press button. So we need to change config in `/etc/systemd/logind.conf` and uncomment this lines:
```bash
HandlePowerKey=suspend
HandlePowerKeyLongPress=poweroff
HandleLidSwitch=suspend
HandleLidSwitchExternalPower=suspend
HandleLidSwitchDocked=suspend
LidSwitchIgnoreInhibited=yes
```
PD: The commented lines are the default setting

## Configure login manager
If we want to start the system through the terminal without a login manager, we need to uninstall these packages:
- [lightdm](https://wiki.archlinux.org/title/LightDM) (login manager by default after installation)
- [lightdm-gtk-greeter](https://archlinux.org/packages/?name=lightdm-gtk-greeter) (default GUI that prompts the user for credentials)

After that we need to paste the [xinit](https://wiki.archlinux.org/title/xinit) file `.xinitrc` from this repo in home directory `~/`. Xinit program allows to start a Xorg display server and will be executed only when there is no login manager running.

**WARNING**

1. Before reboot or poweroff the system, go to the last lines of the `.xinitrc` file (after # My config) and check which programs will be executed in the background (&). To avoid boot problems is recommended comment out those programs that we have not yet installed (when install them later remember to uncomment)

2. After reboot and logging in, we need to start our graphical environment (X) by running (type this after each booting is temporary until we set up zsh configuration later): 
```zsh
startx
```

## Add lock screen after suspend
1. Install [betterlockscreen](https://github.com/betterlockscreen/betterlockscreen) package. 
2. Paste `betterlockscreenrc` from this repo into `~/.config/`
3. Link a lock wallpaper by doing
```zsh
betterlockscreen -u ~/Wallpapers/lockscreen.png
```
4. Create a file named `betterlockscreen@service` into `/etc/systemd/system/` and add this lines:
```
[Unit]
Description=Lock X session using betterlockscreen for user %i
Before=sleep.target

[Service]
User=%i
Environment=DISPLAY=:0
ExecStart=/usr/bin/betterlockscreen -l
ExecStartPost=/usr/bin/sleep 2

[Install]
WantedBy=sleep.target
```
5. Enable that service
```zsh
sudo systemctl enable betterlockscreen@vexedmoth.service
```
6. Reboot system




## Install Paru AUR helper
Standard pacman wrapping [AUR](https://wiki.archlinux.org/title/Arch_User_Repository) helper that allows to get access to the Arch User Repository. 

```zsh
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

## GitHub ssh keys
Since we will need to clone github repositories later on, let's generate ssh keys and add them to GitHub. (I prefer this option over via https). 

[Steps](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

## Packages
Certain configs like Qtile or xinit need some packages to work correctly. For instance the volume keyboard control is configured by Qtile, and Qtile uses pamixer binary. So in this case, before paste qtile config from this repo into our new system config, or basically before doing something else, we need to install the following basic main packages:  

- [brightnessctl](https://archlinux.org/packages/community/x86_64/brightnessctl/) (control brightness)
- [pamixer](https://archlinux.org/packages/community/x86_64/pamixer/) (control volume)
- [acpi](https://wiki.archlinux.org/title/ACPI_modules) (monitoring applications like battery, fans and thermal)
- [lm_sensors](https://wiki.archlinux.org/title/lm_sensors) (provides tools and drivers for monitoring temperatures, voltage, and fans)
- [batsignal](https://github.com/electrickite/batsignal) (battery daemon notifier)
- [volumeicon](https://archlinux.org/packages/community/x86_64/volumeicon/) (volume control for the system tray)
- [cbatticon](https://github.com/valr/cbatticon) (battery control for the system tray)
- [nvidia-settings](https://wiki.archlinux.org/title/NVIDIA) (nvidia settings control)
- [scrot](https://wiki.archlinux.org/title/Screen_capture) (screenshots)
- [trash-cli](https://github.com/andreafrancia/trash-cli) (trash management)
- [udiskie](https://wiki.archlinux.org/title/udisks) (udisks2 automounter)
- [feh](https://wiki.archlinux.org/title/feh) (set wallpaper) 
- [zathura](https://wiki.archlinux.org/title/zathura) (pdf document viewer) and [zathura-pdf-poppler](https://archlinux.org/packages/?name=zathura-pdf-poppler) (dependency)
- [mpv](https://wiki.archlinux.org/title/mpv) (videoplayer)
- [geeqie](https://archlinux.org/packages/extra/x86_64/geeqie/) (image viewer)
- [xorg-xev](https://archlinux.org/packages/extra/x86_64/xorg-xev/) (print contents of X events)
- [unzip](https://archlinux.org/packages/extra/x86_64/unzip/) (extracting .zip files)
- [mlocate](https://wiki.archlinux.org/title/locate) (find files by name)
- [lxappearance](https://archlinux.org/packages/community/x86_64/lxappearance/) (GTK theme switcher)
- [bat](https://archlinux.org/packages/community/x86_64/bat/) (cat with steroids)
- [brave-bin](https://aur.archlinux.org/packages/brave-bin) (private web browser)
- [visual-studio-code-bin](https://aur.archlinux.org/packages/visual-studio-code-bin) (code editor)
- [neovim](https://wiki.archlinux.org/title/Neovim) (code editor)
- [rofi](https://wiki.archlinux.org/title/Rofi) (dmenu). **Paste `rofi` directory in `~/.config/`**
- [ranger](https://wiki.archlinux.org/title/ranger) (file manager), [ueberzug](https://archlinux.org/packages/community/x86_64/ueberzug/) (preview images for ranger) and [poppler](https://archlinux.org/packages/extra/x86_64/poppler/) (preview pdf's for ranger). **Paste `ranger` directory in `~/.config/`**
- [picom](https://wiki.archlinux.org/title/Picom) (compositor for Xorg). **Paste `picom` directory in `~/.config/`**
- [dunst](https://wiki.archlinux.org/title/Dunst) (notification daemon). **Paste `dunst` directory in `~/.config/`**
- [btop](https://archlinux.org/packages/community/x86_64/btop/) (htop with steroids). **Paste `btop` directory in `~/.config/`**
- [lsd](https://github.com/Peltoche/lsd) (ls with steroids). **Paste `lsd` directory in `~/.config/`**
- [neofetch](https://archlinux.org/packages/community/any/neofetch/) (BTW I use Arch).  **Paste `neofetch` directory in `~/.config/`**

*PD: almost all packages can be installed with pacman package manager. Few of them with paru from AUR and even manually from github*


## Add Fonts
1. Paste the `fonts` directory in `/usr/share/`. Delete the previous existing fonts directory then.
2. Refresh the font cache. This is necessary for those programs that uses fontconfig to list available fonts on the system.
```zsh
sudo fc-cache -f -v

```

## Change GTK theme
By default, the [GTK](https://wiki.archlinux.org/title/GTK) theme is Adwaita. Let's change it:

1. Download Material-Black-BlueBerry GTK theme from [here](https://www.gnome-look.org/p/1316887)
2. Unzip the .zip file
3. Move the unzipped directory into our themes directory in the system
```zsh
sudo mv Material-Black-BlueBerry /usr/share/themes
```
4. Run GTK theme switcher and change it manually with a GUI
```zsh
lxappearance
```




########################
qtile
zsh
alacritty
scripts (.local/bin)


```zsh

```



