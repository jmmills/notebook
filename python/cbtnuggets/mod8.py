Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 16 2013, 23:39:35) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> tuplist = [(1,2), (3,4), (5,6)]
>>> tuplist
[(1, 2), (3, 4), (5, 6)]
>>> for (a, b) in tuplist:
	print (a, b)

	
1 2
3 4
5 6
>>> import os
>>> for k, v in os.environ.items():
	print('%s = %s' % (k,v))

	
BASHISH_OLDPATH = /opt/local/libexec/gnubin:/opt/local/libexec/perl5.16:/opt/local/bin:/opt/local/sbin:/opt/local/lib/mysql5/bin/:/usr/local/go/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/MacGPG2/bin
UPLOAD = root@logger2.ipt:/var/unifi/rsync/sounds-1.8/
SECURITYSESSIONID = 186b6
OLDPWD = /Users/jason
SHLVL = 1
SHELL = /opt/local/bin/bash
COLORFGBG = 7;0
Apple_PubSub_Socket_Render = /tmp/launch-muHJjM/Render
TERM = xterm
PERL5LIB = /Users/jason/perl5/lib/perl5:
TTY = /dev/ttys008
__CHECKFIX1436934 = 1
LS_COLORS = no=00;38;5;244:rs=0:di=00;38;5;33:ln=01;38;5;37:mh=00:pi=48;5;230;38;5;136;01:so=48;5;230;38;5;136;01:do=48;5;230;38;5;136;01:bd=48;5;230;38;5;244;01:cd=48;5;230;38;5;244;01:or=48;5;235;38;5;160:su=48;5;160;38;5;230:sg=48;5;136;38;5;230:ca=30;41:tw=48;5;64;38;5;230:ow=48;5;235;38;5;33:st=48;5;33;38;5;230:ex=01;38;5;64:*.tar=00;38;5;61:*.tgz=01;38;5;61:*.arj=01;38;5;61:*.taz=01;38;5;61:*.lzh=01;38;5;61:*.lzma=01;38;5;61:*.tlz=01;38;5;61:*.txz=01;38;5;61:*.zip=01;38;5;61:*.z=01;38;5;61:*.Z=01;38;5;61:*.dz=01;38;5;61:*.gz=01;38;5;61:*.lz=01;38;5;61:*.xz=01;38;5;61:*.bz2=01;38;5;61:*.bz=01;38;5;61:*.tbz=01;38;5;61:*.tbz2=01;38;5;61:*.tz=01;38;5;61:*.deb=01;38;5;61:*.rpm=01;38;5;61:*.jar=01;38;5;61:*.rar=01;38;5;61:*.ace=01;38;5;61:*.zoo=01;38;5;61:*.cpio=01;38;5;61:*.7z=01;38;5;61:*.rz=01;38;5;61:*.apk=01;38;5;61:*.gem=01;38;5;61:*.jpg=00;38;5;136:*.JPG=00;38;5;136:*.jpeg=00;38;5;136:*.gif=00;38;5;136:*.bmp=00;38;5;136:*.pbm=00;38;5;136:*.pgm=00;38;5;136:*.ppm=00;38;5;136:*.tga=00;38;5;136:*.xbm=00;38;5;136:*.xpm=00;38;5;136:*.tif=00;38;5;136:*.tiff=00;38;5;136:*.png=00;38;5;136:*.svg=00;38;5;136:*.svgz=00;38;5;136:*.mng=00;38;5;136:*.pcx=00;38;5;136:*.dl=00;38;5;136:*.xcf=00;38;5;136:*.xwd=00;38;5;136:*.yuv=00;38;5;136:*.cgm=00;38;5;136:*.emf=00;38;5;136:*.eps=00;38;5;136:*.CR2=00;38;5;136:*.ico=00;38;5;136:*.tex=01;38;5;245:*.rdf=01;38;5;245:*.owl=01;38;5;245:*.n3=01;38;5;245:*.ttl=01;38;5;245:*.nt=01;38;5;245:*.torrent=01;38;5;245:*.xml=01;38;5;245:*Makefile=01;38;5;245:*Rakefile=01;38;5;245:*build.xml=01;38;5;245:*rc=01;38;5;245:*1=01;38;5;245:*.nfo=01;38;5;245:*README=01;38;5;245:*README.txt=01;38;5;245:*readme.txt=01;38;5;245:*.md=01;38;5;245:*README.markdown=01;38;5;245:*.ini=01;38;5;245:*.yml=01;38;5;245:*.cfg=01;38;5;245:*.conf=01;38;5;245:*.c=01;38;5;245:*.cpp=01;38;5;245:*.cc=01;38;5;245:*.log=00;38;5;240:*.bak=00;38;5;240:*.aux=00;38;5;240:*.lof=00;38;5;240:*.lol=00;38;5;240:*.lot=00;38;5;240:*.out=00;38;5;240:*.toc=00;38;5;240:*.bbl=00;38;5;240:*.blg=00;38;5;240:*~=00;38;5;240:*#=00;38;5;240:*.part=00;38;5;240:*.incomplete=00;38;5;240:*.swp=00;38;5;240:*.tmp=00;38;5;240:*.temp=00;38;5;240:*.o=00;38;5;240:*.pyc=00;38;5;240:*.class=00;38;5;240:*.cache=00;38;5;240:*.aac=00;38;5;166:*.au=00;38;5;166:*.flac=00;38;5;166:*.mid=00;38;5;166:*.midi=00;38;5;166:*.mka=00;38;5;166:*.mp3=00;38;5;166:*.mpc=00;38;5;166:*.ogg=00;38;5;166:*.ra=00;38;5;166:*.wav=00;38;5;166:*.m4a=00;38;5;166:*.axa=00;38;5;166:*.oga=00;38;5;166:*.spx=00;38;5;166:*.xspf=00;38;5;166:*.mov=01;38;5;166:*.mpg=01;38;5;166:*.mpeg=01;38;5;166:*.m2v=01;38;5;166:*.mkv=01;38;5;166:*.ogm=01;38;5;166:*.mp4=01;38;5;166:*.m4v=01;38;5;166:*.mp4v=01;38;5;166:*.vob=01;38;5;166:*.qt=01;38;5;166:*.nuv=01;38;5;166:*.wmv=01;38;5;166:*.asf=01;38;5;166:*.rm=01;38;5;166:*.rmvb=01;38;5;166:*.flc=01;38;5;166:*.avi=01;38;5;166:*.fli=01;38;5;166:*.flv=01;38;5;166:*.gl=01;38;5;166:*.m2ts=01;38;5;166:*.divx=01;38;5;166:*.webm=01;38;5;166:*.axv=01;38;5;166:*.anx=01;38;5;166:*.ogv=01;38;5;166:*.ogx=01;38;5;166:
HOME = /Users/jason
MANPATH = /opt/local/share/man:/opt/local/share/man:
SSH_AUTH_SOCK = /tmp/launch-bqO0vT/Listeners
EDITOR = vi
LANG = en_US.UTF-8
PWD = /Users/jason/cbtnuggets/python
PERL_MB_OPT = --install_base /Users/jason/perl5
__CF_USER_TEXT_ENCODING = 0x1F5:0:0
__PYVENV_LAUNCHER__ = /Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3
_ = /usr/local/bin/idle3
DESTINATION = /var/folders/p_/n2518hrs2cd87y2ht907849c0000gn/T/iTerm 1.0.0.20131228 Update
BASHISH_CP = utf8
COM_GOOGLE_CHROME_FRAMEWORK_SERVICE_PROCESS/USERS/JASON/LIBRARY/APPLICATION_SUPPORT/GOOGLE/CHROME_SOCKET = /tmp/launch-evBOA9/ServiceProcessSocket
PERL_MM_OPT = INSTALL_BASE=/Users/jason/perl5
GOROOT = /usr/local/go
OS_NAME = Darwin
ITERM_SESSION_ID = w0t5p0
TERM_PROGRAM = iTerm.app
TMPDIR = /var/folders/p_/n2518hrs2cd87y2ht907849c0000gn/T/
DISPLAY = /tmp/launch-0P3dIZ/org.macosforge.xquartz:0
LS_OPTIONS = --color=auto
PATH = /Users/jason/bin/:/Users/jason/perl5/bin:/Users/jason/perl5/bin:/Users/jason/.bashish/launcher:/opt/local/share/bashish/lib:/opt/local/libexec/gnubin:/opt/local/libexec/perl5.16:/opt/local/bin:/opt/local/sbin:/opt/local/lib/mysql5/bin/:/usr/local/go/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/MacGPG2/bin
ITERM_PROFILE = Default
ENV = /Users/jason/.profile
USER = jason
LOGNAME = jason
PERL_LOCAL_LIB_ROOT = /Users/jason/perl5:
>>> f = open('spam.txt')
>>> for line in f:
	print(line)

	
This is the first line.

This is the second line.

This is the third line.

>>> nm = {'Key 1':'Value 1', 'Key 2':'Value 2'}
>>> nm
{'Key 2': 'Value 2', 'Key 1': 'Value 1'}
>>> for k, v in nm.items():
	print (k, v)

	
Key 2 Value 2
Key 1 Value 1
>>> i = ["abc", 123, (5,6), 4.20]
>>> query = [(5,6), 3.14]
>>> for key in query:
	if key in i:
		print(key, "was found")

		
(5, 6) was found
>>> for key in query:
	if key in i:
		print(key, "was found")
	else:
		print(key, "not found")

		
(5, 6) was found
3.14 not found
>>> for multi in range(4,7):
	for i in range(1,11):
		print (i, 'x', mult, '=', i * mult)
	print()

	
Traceback (most recent call last):
  File "<pyshell#33>", line 3, in <module>
    print (i, 'x', mult, '=', i * mult)
NameError: name 'mult' is not defined
>>> for multi in range(4,7):
	for i in range(1,11):
		print (i, 'x', multi, '=', i * mult)
	print()

	
Traceback (most recent call last):
  File "<pyshell#35>", line 3, in <module>
    print (i, 'x', multi, '=', i * mult)
NameError: name 'mult' is not defined
>>> for mult in range(4,7):
	for i in range(1,11):
		print (i, 'x', mult, '=', i * mult
		       )
	print()

	
1 x 4 = 4
2 x 4 = 8
3 x 4 = 12
4 x 4 = 16
5 x 4 = 20
6 x 4 = 24
7 x 4 = 28
8 x 4 = 32
9 x 4 = 36
10 x 4 = 40

1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50

1 x 6 = 6
2 x 6 = 12
3 x 6 = 18
4 x 6 = 24
5 x 6 = 30
6 x 6 = 36
7 x 6 = 42
8 x 6 = 48
9 x 6 = 54
10 x 6 = 60

>>> xj = 0
>>> y = 13
>>> whiel x < y:
	
SyntaxError: invalid syntax
>>> while x < y:
	print (x)
	x += 1

	
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    while x < y:
NameError: name 'x' is not defined
>>> x = 0
>>> while x < y:
	print (x)
	x += 1

	
0
1
2
3
4
5
6
7
8
9
10
11
12
>>> 
