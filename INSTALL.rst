=========================
Installation instructions
=========================

KellerSensorTelegramBot can be installed using pip::

    $ sudo apt install git python3-pip
    $ sudo python3 -m pip install git+git://github.com/linuxluigi/kellerbot.git

This command will fetch the archive and its dependencies from the internet and
install them. 

If you've downloaded the tarball, unpack it, and execute::

    $ sudo python setup.py install

You might prefer to install it system-wide. In this case, skip the ``--user``
option and execute as superuser by prepending the command with ``sudo``.

After finishing the install enable the service for start on boot & set the telegram bot ID & telegram chat ID::

    $ sudo systemctl daemon-reload
    $ sudo systemctl edit keller.service

    [Service]
    Environment="BOT_ID=XXX"
    Environment="CHAT_ID=XXX"

    $ sudo systemctl daemon-reload
    $ sudo systemctl enable keller.service
    $ sudo systemctl status keller.service

Troubleshoot
------------

Windows users may find that these command will only works if typed from Python's
installation directory.

Some Linux distributions (e.g. Ubuntu) install Python without installing pip.
Please install it before. If you don't have root privileges, download the
get-pip.py script at https://bootstrap.pypa.io/get-pip.py and execute it as
``python get-pip.py --user``.