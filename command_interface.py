#!/usr/bin/env python3
# coding:utf8

from argparse import ArgumentParser
from mintia import Image2Markdown

parser = ArgumentParser()

parser.add_argument('directory', help='target directory path')
parser.add_argument('suffix', help='specify the target suffix with .')

arg = parser.parse_args()


if __name__ == '__main__':
	directory = arg.directory
	suffix = [arg.suffix]

	markdown = Image2Markdown(directory, suffix)
	print(markdown.create_markdown())
