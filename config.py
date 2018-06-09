# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL
})

# Emacs-like keybindings in non-Emacs applications
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt", "konsole", "gnome-terminal"), {
    # Cursor
    K("C-n"): with_mark(K("left")),
    K("C-y"): with_mark(K("right")),
    K("C-r"): with_mark(K("up")),
    K("C-l"): with_mark(K("down")),
    K("C-j"): with_mark(K("backspace")),
    # Forward/Backward word
    K("M-x"): with_mark(K("C-left")),
    K("M-u"): with_mark(K("C-right")),
    # Beginning/End of line
    K("C-a"): with_mark(K("home")),
    K("C-d"): with_mark(K("end")),
    # Page up/down
    K("C-f"): with_mark(K("page_up")),
    K("C-h"): with_mark(K("page_down")),

    K("C-k"): with_mark(K("C-l")),
    # # Beginning/End of file
    # K("M-Shift-comma"): with_mark(K("C-home")),
    # K("M-Shift-dot"): with_mark(K("C-end")),
    # # Newline
    # K("C-m"): K("enter"),
    # K("C-j"): K("enter"),
    # K("C-o"): [K("enter"), K("left")],
    # # Copy
    # K("C-w"): [K("C-x"), set_mark(False)],
    # K("M-w"): [K("C-c"), set_mark(False)],
    # K("C-y"): [K("C-v"), set_mark(False)],
    # # Delete
    # K("C-d"): [K("delete"), set_mark(False)],
    # K("M-d"): [K("C-delete"), set_mark(False)],
    # # Kill line
    # K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # # Undo
    # K("C-slash"): [K("C-z"), set_mark(False)],
    # K("C-Shift-ro"): K("C-z"),
    # # Mark
    # K("C-space"): set_mark(True),
    # K("C-M-space"): with_or_set_mark(K("C-right")),
    # # Search
    # K("C-s"): K("F3"),
    # K("C-r"): K("Shift-F3"),
    # K("M-Shift-key_5"): K("C-h"),
    # # Cancel
    # K("C-g"): [K("esc"), set_mark(False)],
    # # Escape
    # K("C-q"): escape_next_key,
    # # C-x YYY
    # K("C-x"): {
    #     # C-x h (select all)
    #     K("h"): [K("C-home"), K("C-a"), set_mark(True)],
    #     # C-x C-f (open)
    #     K("C-f"): K("C-o"),
    #     # C-x C-s (save)
    #     K("C-s"): K("C-s"),
    #     # C-x k (kill tab)
    #     K("k"): K("C-f4"),
    #     # C-x C-c (exit)
    #     K("C-c"): K("C-q"),
    #     # cancel
    #     K("C-g"): pass_through_key,
    #     # C-x u (undo)
    #     K("u"): [K("C-z"), set_mark(False)],
    # }
}, "Emacs-like keys")
