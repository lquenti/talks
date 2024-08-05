TARGET=main
TEX_SOURCES=$(TARGET).tex *.tex
CMD_OPTIONS=-shell-escape

all: fast

fast: $(TEX_SOURCES)
	pdflatex $(CMD_OPTIONS) $(TARGET)
	pdflatex $(CMD_OPTIONS) $(TARGET)
	pdflatex $(CMD_OPTIONS) $(TARGET)

biber: clean
	pdflatex $(CMD_OPTIONS) $(TARGET)
	biber $(TARGET)
	pdflatex $(CMD_OPTIONS) $(TARGET)
	pdflatex $(CMD_OPTIONS) $(TARGET)

index:
	pdflatex $(CMD_OPTIONS) $(TARGET)
	makeindex $(TARGET)
	pdflatex $(CMD_OPTIONS) $(TARGET)
	pdflatex $(CMD_OPTIONS) $(TARGET)

clean:
	rm -f *.log *.toc *.lof *.lot *.out *.pdf *.aux *.bbl *.blg *.idx *.ilg *.ind *.lol *.bcf *.run.xml *.nav *.snm
	rm -rf _minted-main

.PHONY: biber index

