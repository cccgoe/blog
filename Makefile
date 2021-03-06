.PHONY: clean new rebase

build: venv
	. venv/bin/activate; pelican -vs blog-conf.py\
	  -o blog-htdocs/ blog-src/

preview: venv
	. venv/bin/activate; PREVIEW=yes pelican -vs blog-conf.py\
	  -o blog-htdocs/ blog-src/
	python -m webbrowser blog-htdocs/index.html

deploy: rebase build
	rsync -r --delete blog-htdocs/ cccgoe.de:/data/ccc/htdocs/blog/

rebase:
	git rebase

clean:
	rm -rfv blog-htdocs/

new:
	bash make_post.sh

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python2 -m virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate
