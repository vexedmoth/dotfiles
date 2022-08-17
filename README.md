# Arch Linux setup and configuration

################################## archinstall

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



## Other basic setup
To enable other basic functions like turn the volume/brightness up or down, check battery, configure graphics... we need to install the packages below:

- brightnessctl
- pamixer
- acpi
- lm_sensors
- scrot
- nvidia-settings
- 



## Install Paru AUR helper
Standard pacman wrapping [AUR](https://wiki.archlinux.org/title/Arch_User_Repository) helper that allows to get access to the Arch User Repository. 

```zsh
sudo pacman -S git
sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
```

## 


########################
picom
feh
xinit
uninstall lightdm
ssh keys github
fuentes
rofi
vscode
brightnessctl, pamixer, acpi, xev, scrot, 

```zsh

```



