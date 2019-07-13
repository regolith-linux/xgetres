VERSION ?= 1.0

CPPFLAGS := -DVERSION=\"$(VERSION)\" $(CPPFLAGS)
CFLAGS ?= -O2 -Wall -Werror
LDFLAGS := -lX11 $(LDFLAGS)

PREFIX ?= $(DESTDIR)
BINDIR ?= $(PREFIX)/usr/bin
MANDIR ?= $(PREFIX)/usr/share/man/man1

all: xrescat

xrescat: xrescat.c
	$(CC) $(CPPFLAGS) $(CFLAGS) $? -o $@ $(LDFLAGS)

install: xrescat
	mkdir -p $(BINDIR)
	install -D $< $(BINDIR)
	mkdir -p $(MANDIR)
	install -Dm 644 xrescat.1 $(MANDIR)/xrescat.1

clean:
	rm -f xrescat

.PHONY: all install clean
