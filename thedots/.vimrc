set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

"Plugin 'dart-lang/dart-vim-plugin'
"Plugin 'leafgarland/typescript-vim'
"Bundle 'OmniSharp/omnisharp-vim'
"
Plugin 'VundleVim/Vundle.vim'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'majutsushi/tagbar'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'Valloric/YouCompleteMe'

call vundle#end()

syntax on
filetype plugin indent on
filetype plugin on

set path+=**
set wildmenu
set shiftwidth=4
set tabstop=4
set nocompatible
set backspace=indent,eol,start
set history=5000
set ruler
set showcmd
set incsearch
set background=dark
set showmatch
set nu
set foldmethod=indent
set expandtab
set smarttab
set tabpagemax=30

if has("vms")
    set nobackup
else
    set backup
    set undofile
endif

if has("mouse")
    set mouse=a
endif

if &t_Co > 2 || has("gui_running")
  syntax on
  set hlsearch
  set t_Co=256
endif

set undodir=~/.vim/.backup
set backupdir=~/.vim/.backup
set viminfo+=n~/.vim/viminfo

for prefix in ['i', 'n', 'v']
    for key in ['<Up>', '<Down>', '<Left>', '<Right>']
        exe prefix . "noremap " . key . " <Nop>"
    endfor
endfor

" Open the tagbar toggler
nmap <F3> :TagbarToggle<CR>
" Deletes empty lines
nmap <F4> :g/^$/d<CR>
" Removes trailing whitespaces
nmap <F5> :%s/\s\+$//e<CR>
" Add an empty space after commas
nmap <F6> :%s/,\(\S\)/, \1/g<CR>
" Remove spaces in empty strings
nmap <F7> :%s/' '/''/gc<CR>
" Add an empty space after colons
nmap <F8> :%s/:\(\S\)/: \1/gc<CR>

" Shows tabs and spaces
nmap <leader>l :set list!<CR>

if has('autocmd')
    autocmd FileType python nmap <F2> :w\|!python %<cr>
    autocmd FileType sh nmap <F2> :w\|!sh %<cr>
    autocmd FileType cpp nmap <F2> :w\|!g++ -g -c -o %< % && ./%<<cr>
    autocmd FileType cs nmap <F2> :w\|!csc ./%<cr>
    autocmd BufRead *.html nmap <F2> :w\|!brave ./%<cr>

    autocmd BufNewFile *.py 0r ~/.vim/templates/skeleton.py
    autocmd BufNewFile *.sh 0r ~/.vim/templates/skeleton.sh
    autocmd BufNewFile *.js 0r ~/.vim/templates/skeleton.js
    autocmd BufNewFile *.html 0r ~/.vim/templates/skeleton.html

    autocmd VimLeave * call delete('~/.viminfo')
endif

"UtilSnips Config
let g:UltiSnipsExpandTrigger="<c-l>"
let g:UltiSnipsJumpForwardTrigger="<c-j>"
let g:UltiSnipsJumpBackwardTrigger="<c-k>"

" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="horizontal"

"YouCompleteMe Config
let g:ycm_autoclose_preview_window_after_completion=1

"Airline Config
let g:airline_section_b = '%{strftime("%c")}'
let g:airline_section_y = 'BN: %{bufnr("%")}'
let g:airline_theme = 'simple'

" Tar files Config
" let g:loaded_tarPlugin = 1
" let g:loaded_tar = 1
