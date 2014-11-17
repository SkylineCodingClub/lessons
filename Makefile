html_files := $(shell ls slides/*.html)
lessons: jsonify.py $(html_files)
	python jsonify.py slides/*.html

