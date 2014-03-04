CCC Göttingen Blog
============================================================

:date: 2014-03-04 20:10
:author: Marcel Hellkamp <marc@gsites.de>
:slug: CCC-Goettingen-Blog
:category: meta
:tags: blog, help

Der CCC-Göttingen hat jetzt (testhalber) einen Blog. 

Technische Details
------------------
Dieser Blog wird mit `Pelican <http://blog.getpelican.com/>`_ aus `ReStructuredText <http://de.wikipedia.org/wiki/ReStructuredText>`_ oder `Markdown <http://de.wikipedia.org/wiki/Markdown>`_ Dateien generiert, die in einem `git <http://git-scm.com/>`_ Repository liegen. Eigentlich ganz einfach.

Artikel Schreiben
-----------------

.. code-highlight: bash

Abhängigkeiten installieren::

    apt-get install make git python python-virtualenv
    pacman -Sy make git python2 python2-virtualenv

Reporotory clonen::

    git clone https://github.com/cccgoe/blog.git
    cd blog

Einen Atrikel schreiben::

    make new
    # ... Es öffnet sich ein $EDITOR

Vorschau generieren::

    make preview

Artikel abschicken::

    git add blog-src/*.rst
    got commit -a && git push

