# -*- coding: utf-8 -*-

from resumable.files import ResumableFile
from sougenius.utils.templatetags.useful_tags import normalize_ascii

class ChunkedFile(ResumableFile):

    @property
    def filename(self):
        file_name = super(ChunkedFile, self).filename

        return normalize_ascii(file_name)
