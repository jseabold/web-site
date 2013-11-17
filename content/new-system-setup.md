Title: Setting up Linux on a New Laptop
Date: 2013-11-17
Tags: linux, notes-to-self
Comments: true
slug: new-system-setup
Summary: This post describes the steps I need to take to set up my working environment on a newly installed Linux OS. It includes instructions on setting up vim, git, installing common packages I need, building the numpython stack from scratch, setting up automatic backups to Amazon S3, and more.

The below may change, but I will not update the blog post. See the [source](https://github.com/jseabold/scripts/blob/master/setup.md) on github for the most up to date version.<br /><br />

I recently lost my laptop and had to start again from scratch. I have spent the last two weeks setting up my new laptop, and this is the result. May I never have to do this much drudgery again.<br /><br />

These are the steps I need to take and packages that I need to install to do my daily work right now. This includes development work in various languages, research projects, and day-to-day computing. This is as much for me as for anyone else. If you don't know what a command or package does, don't run it or install it. This list is not exhaustive, so see the link above to github for any additions or corrections.<br /><br />

This setup is for a freshly installed [Kubuntu 13.10](http://www.kubuntu.org/getkubuntu) on a [Lenovo Yoga 13 laptop](http://www.amazon.com/gp/product/B00ATANVLG/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00ATANVLG&linkCode=as2&tag=scistapro-20).

## Common Install

    sudo apt-get install chromium-browser vim-gtk git build-essential gfortran xclip curl vlc kubuntu-restricted-extras konversation subversion mercurial conky thunderbird feh ubuntuone-control-panel-qt skype

## Laptop Only

    sudo apt-get install powertop acpi

## Lenovo Yoga 13 Only 

#### Wi-Fi and Bluetooth until supported by kernel

    cd ~/scratch

    git clone git@github.com:lwfinger/rtl8723au.git
    cd rtl8723au/
    make
    sudo make install
    cd ..

    git clone git@github.com:lwfinger/rtl8723au_bt.git
    cd rtl8723au_bt/
    make
    sudo make install
    cd ~

#### Brightness Controls

Edit

    sudo gvim /etc/default/grub

Change 

    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" 

to

    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_backlight=vendor"

Run

    dpkg-reconfigure linux-image-$(uname -r)

Edit

    sudo gvim /etc/modprobe.d/blacklist.conf

Add `blacklist ideapad_laptop`

## LaTeX

This is a big install!

    sudo apt-get install texlive texlive-xetex texlive-fonts-extra lyx


## Python Setup

    sudo apt-get install python-dev python-pip

## Pip Installs

    sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev
    pip install --user lxml beautifulsoup4 html5lib
    pip install --user nose
    pip install --user sphinx
    pip install --user cython
    pip install --user virtualenv
    pip install --user coverage
    pip install --user mechanize

## Git Config

    git config --global user.email "your.email"
    git config --global user.name "your name"
    git config --global color.ui true
    git config --global alias.recent 'log -n 10 --oneline --graph'
    git config --global alias.st 'status -s'
    git config --global merge.log true
    git config --global merge.summary true
    git config --global core.editor 'gvim --nofork'

## Common Directories

    cd ~
    mkdir scratch
    mkdir src
    mkdir statsmodels
    mkdir school
    mkdir work
    mkdir virtualenvs
    mkdir -p .local/lib
    mkdir -p .local/include

## Security

#### SSH Keys

    cd ~/.ssh
    ssh-keygen -t rsa - C "email@domain.com"
    ssh-add id_rsa

#### GPG Keys

    gpg --gen-key
    gpg --armor --output .gnupg/skipperkey.asc --export

## Config Files and Scripts

    cd ~
    cd src
    git clone git@github.com:jseabold/scripts
    sudo cp ~/src/scripts/00-powersave /etc/pm/power.d/

    git clone git@github.com:jseabold/dotfiles
    ln -s ~/src/dotfiles/.bashrc ~/
    ln -s ~/src/dotfiles/.vimrc ~/
    
Add `7 10 cleanup.weekly /home/skipper/src/scripts/clean_scratch.sh` to `/etc/anacrontab`

## [Bashmarks](http://www.huyng.com/projects/bashmarks/)

Bookmark directories for the shell.

    cd ~/src/
    make install
    git clone http://www.huyng.com/projects/bashmarks/

Make sure `bashmarks.sh` is sourced in your `.bashrc` file.

## Keyboard Shortcuts

Common keyboard shortcuts I use

    ctrl+shift+i -> browser
    alt+g -> gvim
    alt+k -> konsole
    alt+m -> move window
    meta+m -> minimize window

## Vim Setup

Setup directory structure

    mkdir -p ~/.vim/autoload ~/.vim/bundle ~/.vim/ftplugin

#### [Pathogen](http://www.vim.org/scripts/script.php?script_id=2332): easy package management in vim

    curl -Sso ~/.vim/autoload/pathogen.vim \
        https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim
    cd ~/.vim/bundle

#### [sensible.vim](http://www.vim.org/scripts/script.php?script_id=4391): Defaults everyone can agree on

    git clone git://github.com/tpope/vim-sensible.git

#### [Markdown](http://www.vim.org/scripts/script.php?script_id=2882) syntax support for vim

    git clone https://github.com/hallison/vim-markdown.git

#### [LaTeX suite](http://vim-latex.sourceforge.net/) tools for vim

    git clone git://git.code.sf.net/p/vim-latex/vim-latex
    
#### [fugitive.vim](http://www.vim.org/scripts/script.php?script_id=2975): support for git in vim

    git clone https://github.com/tpope/vim-fugitive.git

#### [Command-t](https://wincent.com/products/command-t): Fast file navigation for vim

    git clone git://git.wincent.com/command-t.git
    cd command-t/ruby/command-t
    sudo apt-get install ruby-dev
    ruby extconf.rb && make
    cd ../../../

#### [snipMate](http://www.vim.org/scripts/script.php?script_id=2540): TextMate style snippets for vim

    git clone https://github.com/msanders/snipmate.vim
    echo -e "snippet ipdb\n\timport ipdb; ipdb.set_trace()" >> snipmate.vim/snippets/python.snippets
    # optional
    # cd ../
    # git clone https://github.com/scrooloose/snipmate-snippets snippets
    # delete snipmate.vim/snippets if you Install the above

Remap the trigger key, if you're going to install PyDiction below (or remap the PyDiction trigger key). Edit `after/plugin/snipMate.vim` and change the following lines

    ino <silent> <c-cr> <c-r>=TriggerSnippet()<cr>
    snor <silent> <c-cr> <esc>i<right><c-r>=TriggerSnippet()<cr>
    ino <silent> <s-c-cr> <c-r>=BackwardsSnippet()<cr>
    snor <silent> <s-c-cr> <esc>i<right><c-r>=BackwardsSnippet()<cr>

This remaps from TAB to CTRL+Return.

    cd ../bundle

#### [gnupg](http://www.vim.org/scripts/script.php?script_id=3645): plugin for editing gpg encrypted files

    git clone https://github.com/jamessan/vim-gnupg

#### [PyDiction](http://www.vim.org/scripts/script.php?script_id=850): Tab-complete Python code

    git clone https://github.com/rkulla/pydiction.git

After installing the Python modules you commonly use, update the autocomplete dictionary

    cd ~/.vim/bundle/pydiction
    python pydiction.py numpy scipy pandas statsmodels matplotlib

    cd ~

#### Custom ftplugins

Add my own custom ftplugins that are kept on github

    ln -s ~/src/dotfiles/vim/ftplugin/* ~/.vim/ftplugin/

## [Conky](http://conky.sourceforge.net/)

    cd ~/scratch/
    wget -O abite.zip http://img.dafont.com/dl/?f=a_bite
    unzip -e abite.zip
    xdg-open ABITE.ttf
    cd ~

## [Choqok](http://choqok.gnufolks.org/) KDE Microblog client

As of 1.3 Choqok still uses the Twitter 1.0 API, so you need to install from source.

    sudo apt-get install kdelibs5-dev libqjson-dev libqoauth-dev libqca2-dev cmake libindicate-qt-dev
    cd ~/src/
    wget --content-disposition http://sourceforge.net/projects/choqok/files/Choqok/choqok-1.4.tar.xz/download
    tar -xvf choqok*
    cd choqok*
    mkdir BUILD
    cd BUILD
    cmake -DCMAKE_INSTALL_PREFIX=`kde4-config --prefix` ..
    make
    sudo make install

You might need to `sudo ldconfig`.

## Python Libraries Git Sources

These are all packages I like to build from source to stay close to the bleeding edge.

    cd ~/src/
    git clone git@github.com:jseabold/ipython ipython-skipper && cd ipython-skipper && git remote add upstream git://github.com/ipython/ipython && cd ..
    git clone git@github.com:jseabold/numpy numpy-skipper && cd numpy-skipper && git remote add upstream git://github.com/numpy/numpy && cd ..
    git clone git@github.com:jseabold/scipy scipy-skipper && cd scipy-skipper && git remote add upstream git://github.com/scipy/scipy && cd ..
    git clone git@github.com:jseabold/matplotlib matplotlib-skipper && cd matplotlib-skipper && git add remote upstream git://github.com/matplotlib/matplotlib && cd ..
    git clone git@github.com:jseabold/pandas pandas-skipper && cd pandas-skipper && git remote add upstream git://github.com/pydata/pandas && cd ..
    git clone git://github.com/scikit-learn/scikit-learn/
    git clone git@github.com:jseabold/pysal pysal-skipper && cd pysal-skipper && git remote add upstream git://github.com/pysal/pysal && cd ..
    git clone git@github.com:jseabold/scikits-sparse scikits-sparse-skipper && cd scikits-sparse-skipper && git remote add upstream git://github.com/njsmith/scikits-sparse && cd ..
    git clone git@github.com:jseabold/networkx networkx-skipper && cd networkx-skipper && git remote add upstream git://github.com/networkx/networkx && cd ..
    git clone git@github.com:jseabold/gensim gensim-skipper && cd gensim-skipper && git remote add upstream git://github.com/piskvorky/gensim && cd ..
    git clone https://github.com/discoproject/disco

### [IPython](http://ipython.org/)

    sudo apt-get install libzmq-dev pandoc python-tk
    pip install --user pyzmq jinja2 tornado
    cd ~/src/ipython-skipper
    python setup.py build
    sudo python setup.py install
    cd ~
    ipython profile create
    rm ~/.config/ipython/profile_default/ipython_config.py
    ln -s ~/src/dotfiles/ipython_config.py ~/.config/ipython/profile_default/
    pip install --user ipdb
    pip install --user ipdbplugin

### [Numpy](http://www.numpy.org/)

#### [OpenBLAS](http://www.openblas.net/)

    cd src
    git clone git://github.com/xianyi/OpenBLAS
    cd OpenBLAS
    make
    make PREFIX=~/.local/ install

Add the location of these library files to the end of the following files to make them easier to find for libraries that depend on numpy

    sudo gvim /etc/ld.so.conf

#### [SuiteSparse](https://www.cise.ufl.edu/research/sparse/SuiteSparse/)

    cd src/
    wget http://www.cise.ufl.edu/research/sparse/SuiteSparse/SuiteSparse-4.2.1.tar.gz
    tar -xvf SuiteSparse-4.2.1.tar.gz

Edit SuiteSparse_config/SuiteSparse_config.mk to use the right compilers and point to BLAS and LAPACK

    # For "make install"
    INSTALL_LIB = ~/.local/lib
    INSTALL_INCLUDE = ~/.local/include

Change these lines

    BLAS = -lblas -lgfortran
    LAPACK = -llapack

to

    BLAS = -lopenblas -lgfortran -lpthread
    LAPACK = -lopenblas

Comment out

    #CHOLMOD_CONFIG = $(GPU_CONFIG)

Uncomment

    CHOLMOD_CONFIG = -DNPARTITION

Compile

    make
    make install

Build/Install NumPy

Don't rely on HOME (~) expansion in site.cfg

    cd ~/src/numpy-skipper
    echo -e "[DEFAULT]\nlibrary_dirs = /home/skipper/.local/lib\ninclude_dirs = /home/skipper/.local/include\n\n[openblas]\nlibraries = openblas\nlibrary_dirs = /home/skipper/.local/lib\ninclude_dirs = /home/skipper/.local/include\n\n[amd]\namd_libs = amd\n\n[umfpack]\numfpack_libs = umfpack" > site.cfg
    python setup.py build &> build.log
    sudo python setup.py install

### [SciPy](http://www.scipy.org/)

Dependencies (not already installed)

For UMFPACK support

    sudo apt-get install swig

    cd ~/src/scipy-skipper
    cp ~/src/numpy-skipper/site.cfg 
    python setup.py build
    sudo python setup.py install

### [Matplotlib](http://matplotlib.org/)

    pip install --user pyparsing
    pip install --user python-dateutil
    sudo apt-get install dvipng
    python setup.py build
    sudo python setup.py install

### [Pandas](http://pandas.pydata.org/)

(Optional) Dependencies

Excel Support

    pip install --user openpyxl xlrd xlwt

[Boto](http://docs.pythonboto.org/en/latest/): Amazon S3 Support. This will need to be configured with your Amazon credentials.

    pip install --user boto

[NumExpr](https://code.google.com/p/numexpr/): Fast numerical array expression evaluator for Python and NumPy

    cd ~/src/
    hg clone https://code.google.com/p/numexpr/
    cd numexpr
    python setup.py build
    sudo python setup.py install


[PyTables](http://www.pytables.org/moin) (depends on NumExpr): package for managing hierarchical datasets and designed to efficiently and easily cope with extremely large amounts of data.

    sudo apt-get install libhdf5-dev liblzo2-dev libbz2-dev
    cd ~/src/
    git clone git://github.com/PyTables/PyTables
    cd PyTables
    python setup.py build
    sudo python setup.py install

[Bottleneck](http://berkeleyanalytics.com/bottleneck/): Fast NumPy array funtions written in Cython

    cd ~/src/
    git clone git://github.com/kwgoodman/bottleneck
    cd bottleneck
    python setup.py build
    sudo python setup.py install

Build/Install pandas

    cd ~/src/pandas-skipper
    python setup.py build
    sudo python setup.py install

### [Statsmodels](http://statsmodels.sourceforge.net/): Statistics in Python

    cd ~/statsmodels
    git clone git@github.com:statsmodels/statsmodels.git
    git clone git@github.com:jseabold/statsmodels.git statsmodels-skipper && cd statsmodels-skipper && git remote add upstream git://github.com/statsmodels/statsmodels && cd ..
    pip install --user patsy
    cd statsmodels-skipper
    python setup.py build_ext --inplace
    sudo python setup.py install

### [scikit-learn](http://scikit-learn.org/stable/): machine learning in Python

    cd ~/src/scikit-learn
    python setup.py build
    sudo python setup.py install

### [starcluster](http://star.mit.edu/cluster/): cluster-computing toolkit for AMazon EC2

    cd ~/src/
    git clone git://github.com/jtriley/StarCluster.git
    cd StarCluster

Last Stable release

    git checkout 0.94.2
    sudo python setup.py install
    
[Setup your config file](http://star.mit.edu/cluster/docs/latest/quickstart.html) with SSH Keys, AWS Credentials, etc. [Setup for use with IPython](http://star.mit.edu/cluster/docs/latest/plugins/ipython.html#ipython-cluster-plugin).

## NLP / Text Processing

### [NLTK](http://nltk.org/) Natural Language Toolkit

    sudo apt-get install libyaml-dev
    pip install --user pyyaml nltk 
    cd ~/src/
    git clone https://github.com/japerk/nltk-trainer
    cd nltk-trainer
    python setup.py build
    sudo python setup.py install

### [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy): Fuzzy string matching like a boss

Fuzzy string matching library

    cd ~/src/
    pip install --user python-Levenshtein
    git clone https://github.com/seatgeek/fuzzywuzzy
    cd fuzzywuzzy 
    python setup.py build
    sudo python setup.py install

### [Snowball Stemmer](http://snowball.tartarus.org/)

    pip install --user PyStemmer

## R

Dependencies

    sudo apt-get install libreadline-dev xorg-dev

For building HTML docs

    sudo apt-get install texinfo

Build/Install R

    cd ~/src
    wget http://mirrors.nics.utk.edu/cran/src/base/R-3/R-3.0.2.tar.gz
    tar -xvf R-3*
    cd R-3*
    ./configure --with-blas="openblas" --with-lapack="-L ~/.local/lib -lopenblas" --enable-R-shlib
    make
    make check
    sudo make install

Rprofile settings.

    ln -s ~/src/dotfiles/.Rprofile ~/.Rprofile

### R Packages

Install some often used default packages

    Rscript -e "install.packages(c('car', 'systemfit', 'plyr', 'stringr', 'ggplot2', 'RColorBrewer', 'vars'))"


I like to have the source of some packages I use available to muck around in

    cd ~
    mkdir ~/src/R_packages && cd ~/src/R_packages

    wget http://cran.r-project.org/src/contrib/plm_1.3-1.tar.gz
    Rscript -e "install.packages(c('bdsmatrix','Formula'))"
    R CMD INSTALL plm_1.3-1.tar.gz
    tar -xvf plm*

    wget http://cran.r-project.org/src/contrib/textir_1.8-8.tar.gz
    Rscript -e "install.packages(c('slam'))"
    R CMD INSTALL textir_1.8-8.tar.gz
    tar -xvf textir*

### [Rpy2](http://rpy.sourceforge.net/rpy2.html)

    pip install --user rpy2

## [Gretl](http://gretl.sourceforge.net/) Gnu Regression, Econometrics, and Time-series Library

Dependencies (not yet installed above)

    sudo apt-get install gnuplot-dev libfftw3-dev libgmp-dev libmpfr-dev libcurl4-openssl-dev libgtk-3-dev libgtksourceview-3.0-dev

Optional Dependency (X-12 ARIMA)

    cd ~/src/
    mkdir x12arima && cd x12arima
    wget http://www.census.gov/ts/x12a/v03/unix/omegav03src.tar.gz
    tar -xvf omega*
    sed -i -e 's/ifort/gfortran/g' makefile.lnx
    mv makefile.lnx Makefile
    make

Build/Install Gretl

    cd ~/src/
    wget http://prdownloads.sourceforge.net/gretl/gretl-1.9.13.tar.bz2
    tar -xvf gretl*
    LAPACK_LIBS='-L/home/skipper/.local/lib -lopenblas' ./configure --with-x-12-arima --with-libR
    make
    make check
    sudo make install
    sudo ldconfig

## GIS

    cd ~/src/
    git clone git://github.com/matplotlib/basemap matplotlib-basemap
    pip install --user geopy

    sudo apt-get install libgeos-3.3.3
    pip install --user shapely

    pip install --user pyshp

    cd ~/src/
    wget http://download.osgeo.org/proj/proj-4.8.0.tar.gz
    tar -xvf proj-*
    cd proj-*
    ./configure && make
    sudo make install
    make clean && make distclean
    pip install --user pyproj

## Graph Theory / Networks

### [igraph](http://igraph.sourceforge.net/)

    cd ~/src/
    wget --content-disposition http://sourceforge.net/projects/igraph/files/C%20library/0.6.5/igraph-0.6.5.tar.gz/download
    tar -xvf igraph-*
    cd igraph
    ./configure
    make
    sudo make install
    make clean && make distclean
    
    cd ~
    pip install --user python-igraph

### [networkx](http://networkx.github.io/)

    cd ~/src/networkx-skipper
    python setup.py build
    sudo python setup.py install


## [Dropbox](https://db.tt/LLAHiF9s)

    cd ~/src/
    wget -O dropbox.tar.gz http://www.getdropbox.com/download?plat=lnx.x86_64
    tar -xvf dropbox.tar.gz
    cd .dropbox-dist

Set it up

    ./dropboxd 

## Autostart Script

    ln -s ~/src/scripts/autostart.sh ~/.kde/Autostart/

## 32-bit chroot environment

For testing development packages on 32-bit.

[https://gist.github.com/jseabold/7139282](https://gist.github.com/jseabold/7139282)

## Web Development

    sudo apt-get install nodejs npm

## Personal web-site

    cd ~/virtualenvs
    virtualenv pelican --system-site-packages
    source pelican/bin/activate
    pip install markdown
    pip install ipython==1.1

    cd ~/src/
    git clone https://github.com/getpelican/pelican
    cd pelican
    python setup.py install

    cd ~/src/
    git clone https://github.com/getpelican/pelican-plugins pelican-plugins

    cd ~
    git clone git@github.com:jseabold/web-site
    cd web-site
    mkdir themes && cd themes
    git clone https://github.com/jseabold/pelican-fresh

## Backups

### [s3fs](https://code.google.com/p/s3fs/wiki/FuseOverAmazon) FUSE-based file system backed by Amazon S3

Backuping files to Amazon S3 using s3fs. Note that this is pretty slow for use with many small files. I might consider exploring [s3curl](https://aws.amazon.com/code/128) in the future. You might also considering compressing directories to separate tarballs. I suspect that performance- and cost-wise this would be more efficient, though obviously not bandwidth-wise.

Dependencies (some already installed above)

    sudo apt-get install libfuse-dev libcurl4-openssl-dev libxml2-dev mime-support autoconf

    cd ~/src/
    svn checkout http://s3fs.googlecode.com/svn/trunk/ s3fs
    cd s3fs
    autoreconf --install
    ./configure --prefix=/usr
    make
    sudo make install
    sudo mkdir -p /mnt/backup/s3
    sudo chown skipper:skipper /mnt/backup/s3

Add your credentials to a file

    ~/.passwd-s3fs

In the form

    AccessKeyId:SecretAccessKey

Change its permissions

    chmod 600 ~/.passwd-s3fs

Create a bucket using the AWS console or your tool of choice.

Create a backup script. On KDE the `kdialog` command will send a notification to a user.

    :::bash
    #! /bin/bash

    if [[ $1 == "test" ]]; then
        mkdir ~/test_backup
        BACKUP_DIR=~/test_backup/
    else
        /usr/bin/s3fs your-bucket-name /mnt/backup/s3 -ouse_cache=/tmp
        BACKUP_DIR=/mnt/backup/s3/
    fi
    kdialog "Your S3 backup job has started" 5
    /usr/bin/rsync -avrz --delete --inplace --stats --partial --log-file=log.file --exclude-from=/path/to/exclude --files-from=/path/to/include/backup.files /home/username/ $BACKUP_DIR
    mv log.file backup.log.`date +"%Y%m%d%H%M%S"`
    if [[ $1 != "test" ]]; then
        /bin/umount /mnt/backup/s3
    fi
    kdialog "Your S3 backup job has completed" 5

Make it executable

    chmod +x ~/src/scripts/s3backup.sh

Since this is a laptop, you can add this to anacron, so that it will run the next time your machine is on according to some schedule. I added the following to `/etc/anacrontab`

    7 10 backup.weekly /home/skipper/src/scripts/s3backup.sh
