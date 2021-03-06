from __future__ import (absolute_import, division, print_function)
from qtpy.QtWidgets import (QFileDialog)
import os

from addie.utilities.file_handler import FileHandler
from addie.step3_handler.preview_ascii_window import PreviewAsciiWindow


class Step3GuiHandler(object):

    def __init__(self, parent=None):
        self.parent_no_ui = parent
        self.parent = parent.ui
        self.current_folder = parent.current_folder

    def browse_file(self):
        _current_folder = self.current_folder
        _ascii_file = QFileDialog.getOpenFileName(parent=self.parent_no_ui,
                                                  caption='Select file to display',
                                                  directory=self.current_folder)
        if not _ascii_file:
            return
        if isinstance(_ascii_file, tuple):
            _ascii_file = _ascii_file[0]
        _ascii_file = str(_ascii_file)
        o_file_handler = FileHandler(filename=_ascii_file)
        o_file_handler.retrieve_contain()
        text_contain = o_file_handler.file_contain

        o_preview = PreviewAsciiWindow(parent=self.parent_no_ui, text=text_contain, filename=_ascii_file)
        o_preview.show()
