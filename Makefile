html_files := $(shell ls slides/*.html)
lessons.json: jsonify.py $(html_files)
	python jsonify.py slides/*.html > lessons.json

