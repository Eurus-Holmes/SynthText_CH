# SynthText_CH

> *Modify from [SynthText_Chinese_py3](https://github.com/yanhaiming56/SynthText_Chinese_py3) to generate chinese character.*

## Setup the env

```
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

The `data` directory is just the same as [here](https://github.com/yanhaiming56/SynthText_Chinese_py3/tree/master/data), including:

  - **dset.h5**: This is a sample h5 file which contains a set of 5 images along with their depth and segmentation information. Note, this is just given as an example; you are encouraged to add more images (along with their depth and segmentation information) to this database for your own use.
  - **data/fonts**: three sample fonts (add more fonts to this folder and then update `fonts/fontlist.txt` with their paths).
  - **data/newsgroup**: Text-source (from the News Group dataset). This can be subsituted with any text file by `newsgroup.py` or your code. Look inside `text_utils.py` to see how the text inside this file is used by the renderer.
  - **data/models/colors_new.cp**: Color-model (foreground/background text color model), learnt from the IIIT-5K word dataset.
  - **data/models**: Other cPickle files (`char_freq.cp`: frequency of each character in the text dataset; `font_px2pt.cp`: conversion from pt to px for various fonts: If you add a new font, make sure that the corresponding model is present in this file, if not you can add it by adapting `invert_font_size.py`).


The `dataset` directory, you need to put these files into this folder.

  - **dset.h5**: You need to genetate the "dset.h5" file by yourself. You must download these files:
The 8,000 background images used in the paper, along with their segmentation and depth masks, 
have been uploaded here: `http://www.robots.ox.ac.uk/~vgg/data/scenetext/preproc/` + `filename`, where, `filename` can be:

    - **imnames.cp [180K]**: names of filtered files, i.e., those files which do not contain text
    - **bg_img.tar.gz [8.9G]**: compressed image files (more than 8000, so only use the filtered ones in imnames.cp)
    - **depth.h5 [15G]**: depth maps
    - **seg.h5 [6.9G]**: segmentation maps

    After that, you also have to unzip the "bg_img.tar.gz" to this folder. You only run:

```
python gen_dset.py
```

The "gen_dset.py" file can generate 800k images infomation. If you want to generate more images infomation, You can modify the value of `i` or `j`. Then you just copy the generated file `dset.h5` to the folder `data`.


At last, you only run:

```
python gen.py
```

If You want to visualize these synthtext images,you can run:
```
python gen.py --viz
```

This script will generate random scene-text image samples and store them in an h5 file in `results/SynthText_800000.h5`. If the `--viz` option is specified, the generated output will be visualized as the script is being run; omit the `--viz` option to turn-off the visualizations. If you want to visualize the results stored in `results/SynthText_800000.h5` later, run:

```
python visualize_results.py
```


> Note: I do not own the copyright to these images. More detail content,you can consult the https://github.com/ankush-me/SynthText.


## Update

  - To generate `org_img`, run `draw_org_img.py`
  - To generate `render_img` & `label_txt`, run `draw_wordBB.py`
  - To facilitate subsequent data preprocessing, run `rename.py` or `rename2.py`.


