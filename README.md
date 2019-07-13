# xrescat

`xrescat` is a simple utility which prints the value of an X resource.  It is [based on `xgetres`](https://github.com/tamirzb/xgetres) but does not add a linefeed, like `cat`.

## Example

    $ cat ~/.Xresources
    simple: 1
    *wildcard: 2
    $ xrescat simple
    1$
    $ xrescat foo.wildcard
    2$
    $

## Build & installation

First make sure you have libx11.

In order to build, simply run:

    $ make

Then in order to install, run:

    $ sudo make install

Installation location is determined by the `PREFIX` variable
(`/usr/local` by default).
