alias act='source $(pyact)'
alias update='sudo pacman -Syu'
alias pacremove='sudo pacman -Rcs'

alias get_cmake_dependencies='cmake -hal .'

#alias envlearn='cd /home/$USER/enviros/tglearnenv/officeadmin && act'
alias envtripstar='cd /home/$USER/enviros/tripstar/tripstar_app && act'
alias envplay='cd /home/$USER/enviros/playzone/ && act'
alias envzordon='cd /home/$USER/enviros/zordon_env/zordon_root && act'
alias envmodules='envzordon && cd zordon_app/lib/service_utils'
alias envvanilla='cd /home/$USER/enviros/vanilla_env/vanilla_app/vanilla-app && act'
alias envsecurity='cd /home/$USER/enviros/security_env/security_app && act'
alias envrocket='cd /home/$USER/enviros/rocket_env/rocket_app && act'
alias envcalabash='cd /home/$USER/enviros/calabash_env/calabash_app && act'
alias envomnipath='cd /home/$USER/enviros/omnipath_env/omnipath_app && act'
alias envvault='cd /home/$USER/enviros/vault_service_env/vault_service && act'
alias envutils='cd /home/$USER/enviros/utils_service_env/utils_service && act'
alias envmsg='cd /home/$USER/enviros/message_service_env/message_service && act'

alias goto_devserver_internal='ssh developer@development.dotdomain'
alias goto_devserver='ssh developer@dotxml.duckdns.org -p45678'
alias goto_yoda='ssh developer@yoda.dotdomain'
alias goto_dotcop='ssh root@192.168.0.1'
alias goto_hans='ssh hans@192.168.0.85'
alias goto_tjaart='ssh tjaart@192.168.0.70'
alias goto_trevor='ssh trevor@192.168.0.110'

alias hansify='ssh -CX hans@192.168.0.85 "DISPLAY=:0 brave-beta $1"'
alias tjaartify='ssh -CX tjaart@192.168.0.70 "DISPLAY=:0 google-chrome-stable $1"'

#alias encamilla='cd /home/$USER/enviros/camilla/code && act'
#alias encodeshare='cd /home/$USER/enviros/jist_codeshare/codeshare && act'
#alias endocstore='cd /home/$USER/enviros/jistdocstore/jistdocstore && act'
#alias enoldstore='cd /home/$USER/enviros/jistdocstore_old/'
#alias enframework='cd /home/$USER/enviros/jist_framework/hansframework && act'
#alias enplt='cd /home/$USER/enviros/jistdocstore/jistdocstore && act && cd ../camilladocstore/camilladocstore/public/ipython_notebooks/'

#alias alify='ssh -CX alistair "DISPLAY=:0 chromium-browser $1"'

#alias offproxy='sudo mv /etc/apt/apt.conf.d/01proxy /etc/apt/apt.conf.d/01proxy.bk && ll /etc/apt/apt.conf.d/01proxy.bk && update'
#alias onproxy='sudo mv /etc/apt/apt.conf.d/01proxy.bk /etc/apt/apt.conf.d/01proxy && ll /etc/apt/apt.conf.d/01proxy && update'

function dlswp () {
    deltargets=('*.pyc' '__pycache__' '*.i')
    for target in ${deltargets[*]};
    do
        find . -iname $target -print0 -exec rm -r {} \; > /dev/null 2>&1
    done
}

function surprise () {
    DISPLAY=:0 notify-send -u critical "098FF7857C"
}
