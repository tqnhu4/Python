# test_hello_world_gui.py
import unittest
from unittest.mock import MagicMock
import tkinter as tk
import hello_world_gui  # file gốc

class TestHelloWorldGUI(unittest.TestCase):
    def test_say_hello_changes_label(self):
        # Tạo UI tạm để test
        root = tk.Tk()
        label = tk.Label(root, text="")
        # Mock label trong module chính
        hello_world_gui.label = label
        # Gọi hàm
        hello_world_gui.say_hello()
        # Kiểm tra kết quả
        self.assertEqual(label.cget("text"), "Hello, World!")
        root.destroy()

if __name__ == '__main__':
    unittest.main()
