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

**1) Abhängigkeiten installieren**::

    apt-get install make git python python-virtualenv
    pacman -Sy make git python2 python2-virtualenv

**2) Repository auschecken:**

Zuerst brauchst du einen Fork des https://github.com/cccgoe/blog repositories. Alternativ kannst du auch Pusch-Rechte erfragen und direkt mit dem `cccgoe/blog` Repositrory arbeiten::

    git clone https://github.com/YOURNAME/blog.git
    cd blog

**3) Einen Atrikel schreiben**::

    make new
    # ... Es öffnet sich ein $EDITOR

**4) Vorschau generieren**::

    make preview

**5) Artikel abschicken**::

    git add blog-src/*.rst
    git commit -a && git push

Wenn du keine Pusch-Rechte für das `cccgoe/blog` Repositiory hast und mit deinem Fork arbeitest, kannst du jetzt auf GitHub einen Pull-Request erstellen.

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







