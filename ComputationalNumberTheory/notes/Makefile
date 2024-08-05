TEX_PATH=lualatex
TEX_PARAMS=-interaction=nonstopmode -file-line-error
TEX=$(TEX_PATH) $(TEX_PARAMS)

PACKAGE_NAME=notes

SRC_FOLDER=./src
BUILD_FOLDER=./build

all: clean build

clean:
	rm -rf $(BUILD_FOLDER)

build: clean
	mkdir $(BUILD_FOLDER) && \
	cd $(BUILD_FOLDER) && \
	cp -r ../$(SRC_FOLDER)/* . && \
	$(TEX) $(PACKAGE_NAME).tex && \
	cd .. && \
	cp $(BUILD_FOLDER)/$(PACKAGE_NAME).pdf .
	echo "🥳 PDF successfully built! 🥳"

# lets not think about that
.phony: all clean build

