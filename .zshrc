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
export ZSH_DISABLE_COMPFIX=true
source $ZSH/oh-my-zsh.sh

# Read and execute nvm start script to run nvm. 
source /usr/share/nvm/init-nvm.sh

# Adding CUDA binaries to PATH
export CUDA_PATH=/opt/cuda
export PATH=$PATH:/opt/cuda/bin:/opt/cuda/nsight_compute:/opt/cuda/nsight_systems/bin
export NVCC_CCBIN='/usr/bin/g++-13'


# Anaconda3
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/vexedmoth/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/vexedmoth/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/vexedmoth/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/vexedmoth/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


################################# MY CONFIG ###################################

# Adding script binaries to PATH. All scripts inside $HOME/.local/bin will be added automatically to the PATH.
if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi


# Run Hyprland after login in
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  exec Hyprland &> /dev/null
fi

# Bindkeys and aliases
bindkey '^[s' autosuggest-accept
alias fm='ranger'
alias cat='bat --style=plain --paging=never'

alias l='exa -lahg --color=always --icons --group-directories-first'
alias ls='exa -g --color=always --icons --group-directories-first'  
alias la='exa -a --color=always --icons --group-directories-first'   
alias ll='exa -lg --color=always --icons --group-directories-first' 
alias lla='exa -lag --color=always --icons --group-directories-first' 
alias l.='exa -a | egrep "^\."'


eval "$(starship init zsh)"


