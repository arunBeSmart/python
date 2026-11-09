"""Display the current time in seven countries."""

import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


CLOCKS = (
    ("United States", "New York", "America/New_York", "#ff6b6b"),
    ("United Kingdom", "London", "Europe/London", "#4dabf7"),
    ("Japan", "Tokyo", "Asia/Tokyo", "#f06595"),
    ("India", "New Delhi", "Asia/Kolkata", "#ffd43b"),
    ("China", "Beijing", "Asia/Shanghai", "#ff922b"),
    ("Australia", "Sydney", "Australia/Sydney", "#69db7c"),
    ("Brazil", "Sao Paulo", "America/Sao_Paulo", "#b197fc"),
)


def main() -> None:
    root = tk.Tk()
    root.title("World Clock")
    root.configure(bg="#151922")
    root.minsize(780, 560)

    try:
        clocks = [
            (country, city, ZoneInfo(timezone_name), color)
            for country, city, timezone_name, color in CLOCKS
        ]
    except ZoneInfoNotFoundError:
        messagebox.showerror(
            "Time zone data unavailable",
            "Time zone data is missing. On Windows, install it with:\n\n"
            "python -m pip install tzdata",
            parent=root,
        )
        root.destroy()
        return

    heading = tk.Label(
        root,
        text="WORLD CLOCK",
        font=("Segoe UI", 22, "bold"),
        fg="#f1f3f5",
        bg="#151922",
        pady=18,
    )
    heading.pack()

    grid = tk.Frame(root, bg="#151922", padx=18, pady=8)
    grid.pack(fill="both", expand=True)
    for column in range(3):
        grid.columnconfigure(column, weight=1, uniform="clock")
    for row in range(3):
        grid.rowconfigure(row, weight=1, uniform="clock")

    time_labels: list[tuple[ZoneInfo, tk.Label]] = []
    positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1)]

    for (country, city, timezone, color), (row, column) in zip(clocks, positions):
        card = tk.Frame(grid, bg="#222836", padx=12, pady=12)
        card.grid(row=row, column=column, padx=9, pady=9, sticky="nsew")

        tk.Label(
            card,
            text=country,
            font=("Segoe UI", 14, "bold"),
            fg=color,
            bg="#222836",
        ).pack(pady=(8, 2))
        tk.Label(
            card,
            text=city,
            font=("Segoe UI", 10),
            fg="#adb5bd",
            bg="#222836",
        ).pack()

        time_label = tk.Label(
            card,
            font=("Consolas", 21, "bold"),
            fg=color,
            bg="#222836",
        )
        time_label.pack(pady=(12, 4))
        time_labels.append((timezone, time_label))

    def update_clocks() -> None:
        for timezone, label in time_labels:
            label.configure(
                text=datetime.now(timezone).strftime("%H:%M:%S\n%A, %d %B")
            )
        root.after(1000, update_clocks)

    update_clocks()
    root.mainloop()


if __name__ == "__main__":
    main()