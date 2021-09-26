clean:
	rm -rf *.pyc dist sentenceLabel.egg-info __pycache__ build

upload:
	python setup.py upload

pyrcc:
	pyrcc5 -o resources.py resources.qrc