# !/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) <2019>  <Tamás Zolnai>  <zolnaitamas2000@gmail.com>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
# Add the local path to the main script and external scripts so we can import them.
sys.path = [".."] + \
    [os.path.join("..", "externals", "psychopy_mock")] + sys.path

import unittest
import asrt
import psychopy_gui_mock as pgm


class showBasicSettingsDialogTest(unittest.TestCase):

    def testDefault(self):
        gui_mock = pgm.PsychoPyGuiMock()
        exp_settings = asrt.ExperimentSettings("", "")
        numgroups = exp_settings.show_basic_settings_dialog()
        self.assertEqual(numgroups, 2)
        self.assertEqual(exp_settings.numsessions, 2)

        list_of_texts = gui_mock.getListOfTexts()
        self.assertEqual(len(list_of_texts), 3)
        self.assertEqual(
            list_of_texts[0], "Még nincsenek beállítások mentve ehhez a kísérlethez...")
        self.assertEqual(
            list_of_texts[1], "A logfile optimalizálása érdekében kérjük add meg, hányféle csoporttal tervezed az adatfelvételt.")
        self.assertEqual(
            list_of_texts[2], "Hány ülés (session) lesz a kísérletben?")

        list_of_fields = gui_mock.getListOfFields()
        self.assertEqual(len(list_of_fields), 2)
        self.assertEqual(
            list_of_fields[0].label, "Kiserleti + Kontrollcsoportok szama osszesen")
        self.assertEqual(list_of_fields[0].initial, 2)
        self.assertEqual(list_of_fields[1].label, "Ulesek szama")
        self.assertEqual(list_of_fields[1].initial, 2)

    def testCustomValues(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.addFieldValues([3, 3])

        exp_settings = asrt.ExperimentSettings("", "")
        numgroups = exp_settings.show_basic_settings_dialog()
        self.assertEqual(numgroups, 3)
        self.assertEqual(exp_settings.numsessions, 3)

    def testCancel(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.setReturnValue(False)

        exp_settings = asrt.ExperimentSettings("", "")
        with self.assertRaises(SystemExit):
            exp_settings.show_basic_settings_dialog()


if __name__ == "__main__":
    unittest.main()  # run all tests
