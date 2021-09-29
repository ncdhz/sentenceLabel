clean:
	rm -rf *.pyc dist sentenceLabel.egg-info __pycache__ build ./*/__pycache__

upload:
	python setup.py upload

pyrcc:
	pyrcc5 -o sentenceLabelLib/resources.py resources.qrc

sdocs:
	docsify serve ./docs