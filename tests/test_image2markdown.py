#!/usr/bin/env python3
# coding:utf8


from pathlib import Path
from image2markdown import Image2Markdown


def test_create_markdown():
    TESTS = []

    target_dir = 'test_markdown/'
    suffix = ['.png']

    im = Image2Markdown(target_dir, suffix)
    markdown_filenames = im.create_markdown()

    target_path = Path(target_dir)

    assert markdown_filenames == [t.name for t in target_path.glob('*') if t.suffix == '.md']
