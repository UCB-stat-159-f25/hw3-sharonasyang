.PHONY: clean
.PHONY: html
.PHONY: env

env: 
    conda env update -n ligo -f environment.yml || conda env create -n ligo -f environment.yml

clean:
	rm -rf figures/* audio/* _build/*

html:
	myst build --html