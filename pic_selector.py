import argparse
import json
import os
import pathlib
import shutil

def make_args() -> argparse.Namespace:
    """Build argument parser for handling CLI input parameters."""
    parser = argparse.ArgumentParser("pic-selector")
    parser.add_argument(
        "--config",
        "-c",
        help="Configuration file location.",
    )
    return parser.parse_args()


def main() -> None:
    args = make_args()

    cfg_path = pathlib.Path.cwd() / pathlib.Path(args.config)
    with open(cfg_path.absolute(), mode="r", encoding="utf-8") as cfg_file:
        cfg_data = json.loads(cfg_file.read())

    input_pictures = set([
        f"{cfg_data["prefix"]}{p}{cfg_data["extension"]}"
        for p in cfg_data["inclusion_list"]
    ])
    print(input_pictures)
    picture_dir = pathlib.Path(cfg_data["input_directory"]).absolute()

    pictures = list(filter(
        lambda x: x.endswith(cfg_data["extension"]),
        os.listdir(picture_dir)
    ))
    if not (picture_dir / "selected").exists():
        os.mkdir(picture_dir / "selected")
    
    for p in pictures:
        print(p in input_pictures)
        if p in input_pictures:
            shutil.copyfile(
                (picture_dir / p).absolute(),
                (picture_dir / "selected" / p).absolute()
            )


if __name__ == "__main__":
    main()
