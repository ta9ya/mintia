#!/usr/bin/env python3
# coding:utf8


import re

from pathlib import Path
from typing import List, Dict, Tuple


class Image2Markdown:

    def __init__(self, _target_dir: str, _suffixes: List[str]) -> None:

        assert len(_target_dir) > 0, 'target_dir is empty'
        self.target_dir = Path(_target_dir)

        assert len(_suffixes) > 0, 'suffix is empty'
        self.target_suffixes = _suffixes

        self.__created_markdowns: List[Path] = list()

    def create_markdown(self) -> List[str]:
        '''
        :param self
        :return: created markdown file names
        '''

        # get dirpath
        p_list = self.target_dir
        dirpathes = [p for p in p_list.iterdir() if p.is_dir()]

        assert len(dirpathes) > 0, 'directory is not found'

        # create filelist by a directory
        for dirpath in dirpathes:

            input_texts = [d.name for d in dirpath.glob('*') if re.search('|'.join(self.target_suffixes), str(d))]
            input_texts = ['![]({})'.format(dirpath.name + '/' + t) for t in input_texts]

            # create markdown
            markdown_file = self.__create_markdown(dirpath, input_texts)

            # store filename to class member
            self.__created_markdowns.append(markdown_file)

        # print created file names
        markdown_filenames = [c.name for c in self.__created_markdowns]
        print('created files: \n{}'.format('\n'.join(markdown_filenames)))

        return markdown_filenames

    @staticmethod
    def __create_markdown(dirpath: Path, input_texts: List[str]) -> Path:

        markdown_path = dirpath.parent / (dirpath.name + '.md')

        with markdown_path.open(mode='w') as f:
            f.write('\n\n'.join(input_texts))

        return markdown_path


if __name__ == "__main__":
    path = '/Users/denso/work/ai-agent-report/deliverables/19-1Q'

    markdown = Image2Markdown(path, _suffixes=['.png', '.pdf'])
    markdown.create_markdown()
