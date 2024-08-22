# `RanTool`: A `PsychoPy` script to measure the ability to produce random series

This is a _python_ based script to conduct simple experiments on human-generated randomness. It allows gathering basic demographic data like sex, age, faculty, and dominant hand. First, it displays two instructions and afterward a red square which dictates the tempo of random series generation. It allows gathering responses from only two keys ('period' and 'slash') but an easy modification might change it. It writes all the data to a `CSV` format file. During the process of generating randomness, the script enables displaying the history of already produced elements. Therefore, it allows running experiments in which in one condition participants see last generated elements and in the second condition they do not see them.

The main script `ranTool.py` reads information about the condition from `conditions.csv` file which might be created with the use of `make_conditions.py` _python_ script. By 
default `make_conditions.py` creates a list of 50 visible history and 50 invisible history conditions.

The project was supported by the funds from the Polish National Science Center (project no. 2019/35/N/HS6/04318).

## Main Dependencies

* python3.7 ([anaconda distribution](https://www.anaconda.com/download/) is preferred)
* other _python_ dependencies are specified in `requirenments.txt`
* [Latin modern family of fonts](http://www.gust.org.pl/projects/e-foundry/latin-modern)
* [TexLive 2019](https://www.tug.org/texlive/)
* [ImageMagick 7.0.9-14 or higher](https://imagemagick.org/index.php)

## Setup

1. Clone the repo: [git@github.com:MikoBie/ranTool.git](git@github.com:MikoBie/ranTool.git)
2. Set up the proper virtual environment with python3.6
3. Install all the dependencies from `requirenments.txt`
4. Install other dependencies: Latin modern family of fonts, TexLive 2019, and ImageMagick

The fourth step is only necessary if you want to edit instructions. The default instructions are stored in `png` files together with the `tex` source codes. However, it is better to install the Latin modern family of fonts, regardless, because otherwise visible history and ending note will have a different family of fonts than instructions.

## Limitations

The scrip was tested on MacBook 13-inch Early 2015. On other machines, it might require adjusting stimulus positioning cause PsychoPy acts weirdly with Retina displays.

