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

.. code-highlight: sh

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
    git commit -a && git push

Artikel mit Bildern oder Dateien
--------------------------------

Alle Dateien im ``blog-src`` Ordner werden auch veröffentlicht. Man kann sie aus den Dokumenten heraus mit dem
``{filename}`` Macro referenzieren.

* **Absolute Pfade:** ``{filename}/path/to/file`` (relativ zum ``blog-src`` Ordner)
* **Relative Pfade:** ``{filename}path/to/file`` (relativ zum aktuellen Dokument)

Beiträge mit sehr vielen Dateien sollten in ein eigenes Verzeichnis unterhalb von ``blog-src`` gepackt werden. Die ``*.rst`` Datei wird trotzdem gefunden. Das macht es einfacher, mit relativen Pfaden zu arbeiten und das haupt-verzeichnis nicht voll zu müllen. Der Verzeichnis-Name ist dabei egal.

Permanente Links
----------------

Das wichtigste Attribut eines Beitrages ist der **slug**. Dieser String definiert die permanente URL des Beitrages (und sollte nur Zeichen enthalten, die in URLs vorkommen dürfen). Der Dateiname oder der Pfad zum Artikel ist dabei völlig egal.







