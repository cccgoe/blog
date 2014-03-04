.PHONY: clean new

build: venv
	. venv/bin/activate; pelican -vs blog-conf.py -o blog-htdocs/ blog-src/

preview: build
	python -m webbrowser blog-htdocs/index.html

deploy: build
	rsync -r blog-htdocs/ cccgoe.de:/data/ccc/htdocs/blog/


clean:
	rm -rfv blog-htdocs/

new:
	bash make_post.sh

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python2 -m virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate
