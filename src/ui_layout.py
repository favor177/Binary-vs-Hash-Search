# -*- coding: utf-8 -*-
"""
界面布局模块

作者：赵森森（@yuhuyuyuqun）
分支：feature/yuhuyuyuqun-ui
职责：只负责「把窗口搭出来、把控件摆好、把按钮回调接上」。
      不画格子、不写算法——画布交给 render.py，数据交给 algo_*.py。
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

# ---- 配色（与设计文档 3.2 节一致，改之前先同步文档）----
BG = "#F1F4F9"
CARD = "#FFFFFF"
BLUE = "#2563EB"
TEAL = "#0D9488"
AMBER = "#F59E0B"
TEXT = "#1F2937"
MUTED = "#6B7280"


def build_layout(root: tk.Tk) -> dict:
    """搭建主窗口，返回各个关键控件。

    返回字典的键必须保持下面这些名字，render.py 和 main.py 依赖它们。

    返回：
        {
            "canvas_binary": tk.Canvas,   # 左侧画布
            "canvas_hash":   tk.Canvas,   # 右侧画布
            "log_text":      tk.Text,     # 底部日志
            "btn_step":      ttk.Button,
            "btn_auto":      ttk.Button,
            "btn_reset":     ttk.Button,
            "entry_size":    ttk.Entry,
            "entry_target":  ttk.Entry,
        }
    """
    root.title("二分查找 vs 哈希查找 · 可视化演示")
    root.geometry("1280x880")
    root.configure(bg=BG)

    # ---- 主题：换掉默认的 Windows 灰色按钮 ----
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(".", background=BG, foreground=TEXT,
                    font=("Microsoft YaHei", 10))
    style.configure("TButton", padding=(14, 8), relief="flat", borderwidth=0)
    style.configure("Accent.TButton", background=BLUE, foreground="white")
    style.map("Accent.TButton",
              background=[("active", "#1D4ED8"), ("pressed", "#1E40AF")])

    # ---- 顶部控制区 ----
    top = tk.Frame(root, bg=CARD, height=64)
    top.pack(side="top", fill="x", padx=20, pady=(16, 8))
    top.pack_propagate(False)

    tk.Label(top, text="数组容量", bg=CARD, fg=MUTED).pack(side="left", padx=(16, 6))
    entry_size = ttk.Entry(top, width=6)
    entry_size.insert(0, "10")
    entry_size.pack(side="left")

    tk.Label(top, text="目标值", bg=CARD, fg=MUTED).pack(side="left", padx=(18, 6))
    entry_target = ttk.Entry(top, width=6)
    entry_target.insert(0, "40")
    entry_target.pack(side="left")

    # TODO 1：照着上面，再加一个「哈希表容量」输入框（默认 11）

    btn_step = ttk.Button(top, text="单步执行", style="Accent.TButton")
    btn_auto = ttk.Button(top, text="自动播放")
    btn_reset = ttk.Button(top, text="载入 / 重置")
    btn_step.pack(side="right", padx=(0, 16))
    btn_auto.pack(side="right", padx=6)
    btn_reset.pack(side="right")

    # ---- 中间：左右两个画布 ----
    middle = tk.Frame(root, bg=BG)
    middle.pack(side="top", fill="both", expand=True, padx=20)

    left = tk.Frame(middle, bg=CARD)
    left.pack(side="left", fill="both", expand=True, padx=(0, 10))
    tk.Label(left, text="二分查找", bg=CARD, fg=TEXT,
             font=("Microsoft YaHei", 14, "bold")).pack(anchor="w", padx=16, pady=10)
    canvas_binary = tk.Canvas(left, bg=CARD, highlightthickness=0)
    canvas_binary.pack(fill="both", expand=True, padx=10, pady=(0, 12))

    right = tk.Frame(middle, bg=CARD)
    right.pack(side="right", fill="both", expand=True, padx=(10, 0))
    tk.Label(right, text="哈希查找", bg=CARD, fg=TEXT,
             font=("Microsoft YaHei", 14, "bold")).pack(anchor="w", padx=16, pady=10)
    canvas_hash = tk.Canvas(right, bg=CARD, highlightthickness=0)
    canvas_hash.pack(fill="both", expand=True, padx=10, pady=(0, 12))

    # ---- 底部日志 ----
    bottom = tk.Frame(root, bg=CARD)
    bottom.pack(side="bottom", fill="x", padx=20, pady=(8, 16))
    tk.Label(bottom, text="执行日志", bg=CARD, fg=TEXT,
             font=("Microsoft YaHei", 12, "bold")).pack(anchor="w", padx=16, pady=(10, 4))
    log_text = tk.Text(bottom, height=6, bg="#FAFBFC", relief="flat",
                       font=("Consolas", 10), fg=TEXT)
    log_text.pack(fill="x", padx=16, pady=(0, 12))

    # TODO 2：接上按钮回调（回调函数由 main.py 提供，先留空壳）
    #   btn_step.configure(command=on_step)
    #   btn_auto.configure(command=on_auto)
    #   btn_reset.configure(command=on_reset)

    # TODO 3：窗口缩放时画布不跟着变，需要绑定 <Configure> 事件重绘

    return {
        "canvas_binary": canvas_binary,
        "canvas_hash": canvas_hash,
        "log_text": log_text,
        "btn_step": btn_step,
        "btn_auto": btn_auto,
        "btn_reset": btn_reset,
        "entry_size": entry_size,
        "entry_target": entry_target,
    }


# ---- 自测：直接 python ui_layout.py 能弹出一个空窗口 ----
if __name__ == "__main__":
    root = tk.Tk()
    widgets = build_layout(root)
    widgets["log_text"].insert("end", "界面骨架已加载。\n")
    root.mainloop()