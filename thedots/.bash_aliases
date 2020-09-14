alias please='sudo'
alias fbreader='FBReader'
alias yayupdate='yay -Sy'
alias act='source $(pyact)'
alias update='sudo pacman -Sy'
alias pacremove='sudo pacman -Rcs'
alias modelio='/opt/modelio/modelio.sh'

#alias update='sudo pacman -Syu'
#alias pacremove='sudo pacman -Rcs'
#alias remove_rust='rustup self uninstall'
#alias updateall='yayupdate && update && sudo snap refresh'

#alias yayremove_dependencies='yay -Yc'
#alias get_cmake_dependencies='cmake -hal .'

alias envscript='cd /home/$USER/enviros/script_env/ && act'

alias envvault='cd /home/$USER/enviros/threevault_env/threevault_hg && act'
alias envtanzanite='cd /home/$USER/enviros/tanzanite_env/tanzanite && act'

alias envrevault='cd /home/$USER/enviros/revault_env/revault && act'
alias envrocket='cd /home/$USER/enviros/rocket22env/rocket2_2 && act'
alias envrgateway='cd /home/$USER/enviros/rocket_gateway_env/rocket_gateway && act'

alias enveiffel='cd /home/$USER/enviros/eiffelfront_env/front && act'
alias enveiffelback='cd /home/$USER/enviros/calabash_eiffelcorp_backoffice/backoffice && act'

alias envtripstar='cd /home/$USER/enviros/tripstar/mastar_env/mastar && act'
alias envphos='cd /home/$USER/enviros/phosgateway_env/phosgateway && act'
alias envimali='cd /home/$USER/enviros/myimaliapigateway_env/myimaliapigateway && act'

alias envgateway='cd /home/$USER/enviros/calabash_env/calabash && act'
alias envcalaweb='cd /home/$USER/enviros/calabashweb_env/calabash_web && act'
alias envcalacampus='cd /home/$USER/enviros/calabash_campus_env/campus && act'
alias envcalamobile='cd /home/$USER/enviros/calabash_mobile_env/calabash && act'
alias envmerchant='cd /home/$USER/enviros/calabash_merchant_env/calmerchant-app && act'
alias envcalamanagement='cd /home/$USER/enviros/calabash_management_env/calabash-management && act'

#alias enveve='cd /home/$USER/enviros/pyeve_env/ && act'
#alias envrocket='cd /home/$USER/enviros/rocket_env/rocket && act'
#alias envgerrit='cd /home/$USER/enviros/camzone/forgerrit && act'
#alias envplay='cd /home/$USER/enviros/playzone/ && act'
#alias envorca='cd /home/$USER/enviros/orca_env/orca-app && act'
#alias envfauxbogears='cd /home/$USER/enviros/fauxbogears && act'
#alias envchikos='cd /home/$USER/enviros/kivy2_env/chikos && act'
#alias envservice='cd /home/$USER/enviros/services/services && act'
#alias envzordon='cd /home/$USER/enviros/zordon_env/zordon_root && act'
#alias envmsg='cd /home/$USER/enviros/message_env/messaging_service && act'
#alias envomnipath='cd /home/$USER/enviros/omnipath_env/omnipath_app && act'

alias goto_dev='ssh developer@dotxml.duckdns.org -p45678'
alias goto_dev_internal='ssh developer@192.168.0.20'

alias goto_qa='ssh developer@dotxml.duckdns.org -p45679'
alias goto_qa_johan='ssh johan@dotxml.duckdns.org -p45679'
alias goto_qa_internal='ssh qadeveloper@192.168.0.21'

alias goto_yoda='ssh developer@yoda.dotdomain'
alias goto_yoda_internal='ssh developer@192.168.0.3'

alias goto_aws_dotxml='ssh -i ~/.ssh/amazonssh.pem ubuntu@ec2-52-214-66-212.eu-west-1.compute.amazonaws.com'

alias goto_tanzanite_pythonanywhere='ssh -C devxml@ssh.pythonanywhere.com'
alias goto_eiffel_pythonanywhere='ssh -C eiffelcorpdotxml@ssh.pythonanywhere.com'

alias goto_hans='ssh hans@192.168.0.86'
alias goto_dean='ssh dean@192.168.0.76'
alias goto_dotcop='ssh root@192.168.0.1'
alias goto_hans5='ssh hans@192.168.0.85'
alias goto_tjaart='ssh tjaart@192.168.0.70'
alias goto_trevor='ssh trevor@192.168.0.68'
alias goto_tafadzwa='ssh tmutero@192.168.0.109'

alias hansify='ssh -CX hans@192.168.0.86 "DISPLAY=:0 brave-nightly $1"'
alias hansify5='ssh -CX hans@192.168.0.85 "DISPLAY=:0 brave-nightly $1"'

alias tjaartify='ssh -CX tjaart@192.168.0.70 "DISPLAY=:0 google-chrome-stable $1"'
alias trevorify='ssh -CX trevor@192.168.0.69 "DISPLAY=:0 brave $1"'

alias youvideo='youtube-dl -f mp4 -ciw -o "%(title)s.%(ext)s" $1'
alias youaudio='youtube-dl -x --audio-format mp3 -ciw -o "%(title)s.%(ext)s" $1'
alias dlswp='find . -iname "*.pyc" -print0 -exec rm -r {} \;'
alias surprise='DISPLAY=:0 notify-send -u critical "098FF7857C"'

#alias grep_sed_replace='grep -rl $1 ./ | xargs sed -i "s/$1/$2/g"'

