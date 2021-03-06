# -*- coding: utf-8 -*-

from geeknote.editor import Editor
import unittest


class testEditor(unittest.TestCase):

    def setUp(self):
        self.MD_TEXT = """# Header 1

## Header 2

Line 1

_Line 2_

**Line 3**

"""
        self.HTML_TEXT = "<h1>Header 1</h1><h2>Header 2</h2><p>Line 1</p><p>"\
                         "<em>Line 2</em></p><p><strong>Line 3</strong></p>"

    def test_TextToENML(self):
        self.assertEqual(Editor.textToENML(self.MD_TEXT).replace('\n', ''),
                         Editor.wrapENML(self.HTML_TEXT).replace('\n', ''))

    def test_ENMLToText(self):
        wrapped = Editor.wrapENML(self.HTML_TEXT)
        self.assertEqual(Editor.ENMLtoText(wrapped), self.MD_TEXT)

    def test_wrapENML_success(self):
        text = "test"
        result = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
<en-note>test</en-note>'''
        self.assertEqual(Editor.wrapENML(text), result)

    def test_wrapENML_without_argument_fail(self):
        self.assertRaises(TypeError, Editor.wrapENML)
