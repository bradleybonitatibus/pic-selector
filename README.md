# `pic-selector`

This is a small script to help move files between directories, aimed at
simplifying the selection of pictures with some numerical suffix, a prefix,
into a "selected" directory within the folder specified.

## Example Use

Out of the following pictures in some directory (`C:\\Users\\me\\Pictures\\2024-08-04`),
I have the following pictures:
- `_DSC0001.JPG`
- `_DSC0002.JPG`
- `_DSC0003.JPG`
- `_DSC0004.JPG`
- `_DSC0005.JPG`

and I only want to select `_DSC0001.JPG`, and `_DSC0004.JPG`, my `./config.json`
would look like:
```json
{
    "input_directory": "C:\\Users\\me\\Pictures\\2024-08-04",
    "extension": ".JPG",
    "prefix": "_DSC",
    "inclusion_list": [
        "0001",
        "0005"
    ]
}
```

I would then invoke the CLI program with:

```sh
python pic_selector.py --config ./config.json
```
