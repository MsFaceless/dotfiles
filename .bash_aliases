alias modelio='/opt/modelio/modelio.sh'
alias please='sudo'
alias act='source $(pyact)'
alias update='sudo pacman -Syu'
alias yayupdate='yay -Syyuu'
#alias yayremove_dependencies='yay -Yc'
alias pacremove='sudo pacman -Rcs'
alias fbreader='FBReader'
#alias get_cmake_dependencies='cmake -hal .'

#alias envplay='cd /home/$USER/enviros/playzone/ && act'
#alias envorca='cd /home/$USER/enviros/orca_env/orca-app && act'
alias envrocket='cd /home/$USER/enviros/rocket_env/rocket && act'
#alias envzordon='cd /home/$USER/enviros/zordon_env/zordon_root && act'
#alias enveiffel='cd /home/$USER/enviros/eiffelback_env/eiffel-back && act'
#alias enveiffelfront='cd /home/$USER/enviros/eiffelfront_env/eiffel-front && act'
#alias envcalabash='cd /home/$USER/enviros/calabash_env/calabash_app && act'
#alias envservice='cd /home/$USER/enviros/services/services && act'
#alias enveve='cd /home/$USER/enviros/pyeve_env/ && act'
#alias envmsg='cd /home/$USER/enviros/message_env/messaging_service && act'

#alias envfauxbogears='cd /home/$USER/enviros/fauxbogears && act'
#alias envchikos='cd /home/$USER/enviros/kivy2_env/chikos && act'
#alias envomnipath='cd /home/$USER/enviros/omnipath_env/omnipath_app && act'
#alias envtripstar='cd /home/$USER/enviros/tripstar/tripstar_app && act'

alias goto_dev='ssh developer@dotxml.duckdns.org -p45678'
alias goto_dev_internal='ssh developer@192.168.0.20'

alias goto_qa='ssh developer@dotxml.duckdns.org -p45679'
alias goto_qa_internal='ssh qadeveloper@192.168.0.21'

alias goto_yoda='ssh developer@yoda.dotdomain'
alias goto_yoda_internal='ssh developer@192.168.0.3'

alias goto_aws_dotxml='ssh -i ~/.ssh/amazonssh.pem ubuntu@ec2-52-214-66-212.eu-west-1.compute.amazonaws.com'

alias goto_hans='ssh hans@192.168.0.86'
alias goto_dean='ssh dean@192.168.0.76'
alias goto_dotcop='ssh root@192.168.0.1'
alias goto_hans5='ssh hans@192.168.0.85'
alias goto_tjaart='ssh tjaart@192.168.0.70'
alias goto_trevor='ssh trevor@192.168.0.68'
alias goto_tafadzwa='ssh tmutero@192.168.0.91'

alias hansify='ssh -CX hans@192.168.0.86 "DISPLAY=:0 brave-nightly $1"'
alias hansify5='ssh -CX hans@192.168.0.85 "DISPLAY=:0 brave-nightly $1"'

alias tjaartify='ssh -CX tjaart@192.168.0.70 "DISPLAY=:0 google-chrome-stable $1"'
alias trevorify='ssh -CX trevor@192.168.0.69 "DISPLAY=:0 brave $1"'

alias youtubedl_video='youtube-dl -f mp4 -ciw -o "%(title)s.%(ext)s" $1'
alias dlswp='find . -iname "*.pyc" -print0 -exec rm -r {} \;'
alias surprise='DISPLAY=:0 notify-send -u critical "098FF7857C"'
