import os
import pathlib

import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw


class ApplicationIconSetup:
    
    def root_path(self, destination_folder: str) -> str:
        root_path = r''.format(pathlib.Path(__file__).parent.absolute().parent)
        res: str = os.path.join(root_path, destination_folder)
        return res

    def setup_tabs(self, main_path: str):
        def func(tab: qtw.QWidget, tab_name: str):
            tab.setWindowIcon(qtg.QIcon('{}\\{}'.format(main_path, tab_name)))
        return func
    
    def setup_icons(self, main_path: str):
        def func(butt:qtw.QPushButton, icon_name:str):
            butt.setIcon(qtg.QIcon('{}\\{}'.format(main_path, icon_name)))
        return func
    
    def setup_pixels(self, main_path: str):
        def func(lb:qtw.QLabel, icon_name: str):
            lb.setPixmap(qtg.QPixmap('{}\\{}'.format(main_path, icon_name)))
        return func