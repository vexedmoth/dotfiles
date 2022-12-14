# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME=""


plugins=(
    zsh-autosuggestions
    zsh-syntax-highlighting
    web-search
    git
)

# Read and execute oh-my-zsh start script
source $ZSH/oh-my-zsh.sh

# Read and execute nvm start script to run nvm. 
source /usr/share/nvm/init-nvm.sh


################################# MY CONFIG ###################################

# Adding script binaries to PATH. All scripts inside $HOME/.local/bin will be added automatically to the PATH.
if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi


# Run X session (startx) after login in
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  exec startx
fi

# Bindkeys and aliases
bindkey '^[s' autosuggest-accept
alias fm='ranger'
alias cat='bat --style=plain --paging=never'

alias ls='exa --color=always --icons --group-directories-first'  
alias la='exa -a --color=always --icons --group-directories-first'   
alias ll='exa -l --color=always --icons --group-directories-first' 
alias lla='exa -la --color=always --icons --group-directories-first' 
alias lt='exa -aT --color=always --icons --group-directories-first'    
alias l.='exa -a | egrep "^\."'


eval "$(starship init zsh)"