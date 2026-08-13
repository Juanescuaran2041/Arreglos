import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import methods

# ═══════════════════════════════════════════════════════════════════════════
# COLORES Y CONSTANTES
# ═══════════════════════════════════════════════════════════════════════════

BG          = "#1e1e2e"
PANEL       = "#2a2a3e"
ACCENT      = "#7c3aed"
ACCENT2     = "#06b6d4"
TEXT        = "#e2e8f0"
TEXT_DIM    = "#94a3b8"
CELL_BG     = "#313149"
CELL_BORDER = "#4f4f7a"
CELL_HL     = "#7c3aed"
DANGER      = "#ef4444"

CELL_W = 60
CELL_H = 50


# App ArrayVisualizer

class ArrayVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Array Visualizer - 1D & 2D")
        self.geometry("1400x800")
        self.configure(bg=BG)
        self.resizable(True, True)
        
        # Arrays vacíos inicialmente
        self.arr1d = []
        self.arr2d = []
        self.selected_1d = None
        self.selected_2d = None
        
        # Rastrear si fueron creados
        self.created_1d = False
        self.created_2d = False
        
        # Botones de crear (para deshabilitar después)
        self.btn_create_1d = None
        self.btn_create_2d = None
        
        self._build_ui()
    
    def _build_ui(self):
        """Construye la interfaz principal"""
        # ─── HEADER ────────────────────────────────────────────────────────
        header = tk.Frame(self, bg=ACCENT, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text="⬡  ARRAY VISUALIZER", bg=ACCENT, fg="white",
                 font=("Segoe UI", 18, "bold")).pack(side="left", padx=20, pady=15)
        
        # ─── MAIN FRAME ────────────────────────────────────────────────────
        main_frame = tk.Frame(self, bg=BG)
        main_frame.pack(fill="both", expand=True, padx=16, pady=16)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # Panel 1D
        self._build_1d_panel(main_frame)
        
        # Panel 2D
        self._build_2d_panel(main_frame)
    
    # Array 1d
    
    def _build_1d_panel(self, parent):
        """Panel para visualizar y manipular array 1D"""
        outer, inner = self._create_card(parent, "[ ]  ARRAY 1D", ACCENT)
        outer.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        
        # ─── Botón crear ───────────────────────────────────────────────────
        self.btn_create_1d = tk.Button(inner, text="CREAR ARRAY 1D", command=self._create_1d,
                              bg=ACCENT, fg="white", relief="flat",
                              font=("Segoe UI", 10, "bold"), padx=16, pady=8, cursor="hand2")
        self.btn_create_1d.pack(pady=(12, 12), padx=12, fill="x")
        
        # ─── Canvas visualización ──────────────────────────────────────────
        self.canvas_1d = tk.Canvas(inner, bg=PANEL, highlightthickness=0, height=120)
        self.canvas_1d.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self.canvas_1d.bind("<Button-1>", self._click_cell_1d)
        
        # ─── Info ──────────────────────────────────────────────────────────
        self.info_1d = tk.Label(inner, text="Click en 'CREAR ARRAY 1D' para empezar",
                               bg=PANEL, fg=TEXT_DIM, font=("Segoe UI", 9, "italic"))
        self.info_1d.pack(fill="x", padx=12, pady=(0, 8))
        
        # ─── Botones de métodos ────────────────────────────────────────────
        self.methods_frame_1d = tk.Frame(inner, bg=PANEL)
        self.methods_frame_1d.pack(fill="x", padx=12, pady=(0, 12))
        self._build_1d_methods()
    
    def _build_1d_methods(self):
        """Construye botones para métodos 1D"""
        # Limpiar frame anterior
        for widget in self.methods_frame_1d.winfo_children():
            widget.destroy()
        
        if not self.created_1d:
            return
        
        # Frame con grid para botones
        self.methods_frame_1d.columnconfigure(0, weight=1)
        self.methods_frame_1d.columnconfigure(1, weight=1)
        self.methods_frame_1d.columnconfigure(2, weight=1)
        
        tk.Label(self.methods_frame_1d, text="Métodos:", bg=PANEL, fg=TEXT,
                font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(4, 4))
        
        btn_frame = tk.Frame(self.methods_frame_1d, bg=PANEL)
        btn_frame.pack(fill="x")
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        btn_frame.columnconfigure(2, weight=1)
        
        tk.Button(btn_frame, text="🔍 get_second", command=self._exec_1d_get_second,
                 bg=ACCENT2, fg="white", relief="flat", font=("Segoe UI", 8),
                 pady=4).grid(row=0, column=0, padx=2, sticky="ew")
        
        tk.Button(btn_frame, text="🔎 search_value", command=self._exec_1d_search,
                 bg=ACCENT2, fg="white", relief="flat", font=("Segoe UI", 8),
                 pady=4).grid(row=0, column=1, padx=2, sticky="ew")
        
        tk.Button(btn_frame, text="🔄 sort", command=self._exec_1d_sort,
                 bg=ACCENT2, fg="white", relief="flat", font=("Segoe UI", 8),
                 pady=4).grid(row=0, column=2, padx=2, sticky="ew")
    
    def _exec_1d_get_second(self):
        """Ejecuta get_second_element"""
        try:
            result = methods.get_second_element(self.arr1d)
            self.info_1d.config(text=f"get_second_element() → {result}")
        except Exception as e:
            self.info_1d.config(text=f"Error: {str(e)}", fg=DANGER)
    
    def _exec_1d_search(self):
        """Ejecuta search_value_1d"""
        val = simpledialog.askinteger("Buscar", "Ingresa el valor a buscar:")
        if val is not None:
            try:
                result = methods.search_value_1d(self.arr1d, val)
                self.info_1d.config(text=f"search_value_1d({val}) → {result}")
            except Exception as e:
                self.info_1d.config(text=f"Error: {str(e)}", fg=DANGER)
    
    def _exec_1d_sort(self):
        """Ejecuta sort_1d"""
        try:
            result = methods.sort_1d(self.arr1d)
            self.info_1d.config(text=f"sort_1d() → {result}")
        except Exception as e:
            self.info_1d.config(text=f"Error: {str(e)}", fg=DANGER)
    
    def _create_1d(self):
        """Dialogo para crear array 1D"""
        dialog = tk.Toplevel(self)
        dialog.title("Crear Array 1D")
        dialog.geometry("320x280")
        dialog.configure(bg=PANEL)
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()
        
        # Tamaño
        tk.Label(dialog, text="Tamaño del array:", bg=PANEL, fg=TEXT,
                font=("Segoe UI", 10)).pack(pady=(12, 4))
        size_var = tk.IntVar(value=5)
        tk.Spinbox(dialog, from_=1, to=20, textvariable=size_var,
                  bg="#252538", fg=TEXT, font=("Segoe UI", 10),
                  relief="flat", width=10).pack(pady=(0, 12))
        
        # Valores
        tk.Label(dialog, text="Ingresa los valores (uno por línea):", bg=PANEL, fg=TEXT,
                font=("Segoe UI", 9)).pack(pady=(8, 4))
        
        text_widget = tk.Text(dialog, bg="#252538", fg=TEXT, font=("Segoe UI", 9),
                             height=8, relief="flat", insertbackground=TEXT, width=35)
        text_widget.pack(padx=12, pady=4, fill="both", expand=True)
        
        def create():
            size = size_var.get()
            values = text_widget.get("1.0", tk.END).strip().split('\n')
            
            # Crear array con los valores
            self.arr1d = []
            for i in range(size):
                if i < len(values) and values[i].strip():
                    try:
                        self.arr1d.append(int(values[i].strip()))
                    except:
                        self.arr1d.append(values[i].strip())
                else:
                    self.arr1d.append(None)
            
            self.selected_1d = None
            self._draw_1d()
            self.info_1d.config(text=f"✓ Array 1D creado con {size} elementos")
            self.created_1d = True
            self.btn_create_1d.config(state="disabled", text="✓ Array Creado")
            dialog.destroy()
        
        tk.Button(dialog, text="Crear", command=create, bg=ACCENT, fg="white",
                 relief="flat", font=("Segoe UI", 10, "bold"), pady=6).pack(pady=12, padx=12, fill="x")
    
    def _draw_1d(self):
        """Dibuja el array 1D"""
        self.canvas_1d.delete("all")
        
        if not self.arr1d:
            self.canvas_1d.create_text(300, 50, text="Array vacío",
                                      fill=TEXT_DIM, font=("Consolas", 12))
            return
        
        n = len(self.arr1d)
        spacing = 6
        pad_x = 16
        pad_y = 16
        
        total_w = n * (CELL_W + spacing) - spacing
        self.canvas_1d.update_idletasks()
        canvas_w = self.canvas_1d.winfo_width()
        
        if canvas_w <= 1:
            canvas_w = 300
        
        start_x = max(pad_x, (canvas_w - total_w) // 2)
        
        for i, val in enumerate(self.arr1d):
            x0 = start_x + i * (CELL_W + spacing)
            y0 = pad_y
            x1 = x0 + CELL_W
            y1 = y0 + CELL_H
            
            is_sel = (i == self.selected_1d)
            border = CELL_HL if is_sel else CELL_BORDER
            fill = "#4b2d8c" if is_sel else CELL_BG
            
            # Sombra
            self.canvas_1d.create_rectangle(x0+2, y0+2, x1+2, y1+2, fill="#111122", outline="")
            
            # Celda
            self.canvas_1d.create_rectangle(x0, y0, x1, y1, fill=fill, outline=border,
                                          width=2, tags=f"cell_{i}")
            
            # Valor
            display = str(val) if val is not None else "∅"
            self.canvas_1d.create_text((x0+x1)//2, (y0+y1)//2, text=display,
                                      fill=TEXT, font=("Consolas", 11, "bold"), tags=f"cell_{i}")
            
            # Índice
            self.canvas_1d.create_text((x0+x1)//2, y1+12, text=f"[{i}]",
                                      fill=ACCENT2, font=("Segoe UI", 8))
    
    def _click_cell_1d(self, event):
        """Selecciona una celda 1D"""
        tags = self.canvas_1d.find_closest(event.x, event.y)
        for tag in self.canvas_1d.gettags(tags[0] if tags else -1):
            if tag.startswith("cell_"):
                idx = int(tag.split("_")[1])
                self.selected_1d = idx
                self._draw_1d()
                val = self.arr1d[idx]
                self.info_1d.config(text=f"✓ Seleccionado: arr[{idx}] = {val}")
                return
    
    # ═══════════════════════════════════════════════════════════════════════
    # PANEL ARRAY 2D
    # ═══════════════════════════════════════════════════════════════════════
    
    def _build_2d_panel(self, parent):
        """Panel para visualizar y manipular array 2D"""
        outer, inner = self._create_card(parent, "[ ][ ]  ARRAY 2D", ACCENT2)
        outer.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        
        # ─── Botón crear ───────────────────────────────────────────────────
        self.btn_create_2d = tk.Button(inner, text="CREAR ARRAY 2D", command=self._create_2d,
                              bg=ACCENT2, fg="white", relief="flat",
                              font=("Segoe UI", 10, "bold"), padx=16, pady=8, cursor="hand2")
        self.btn_create_2d.pack(pady=(12, 12), padx=12, fill="x")
        
        # ─── Canvas con scroll ─────────────────────────────────────────────
        scroll_frame = tk.Frame(inner, bg=PANEL)
        scroll_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        
        self.canvas_2d = tk.Canvas(scroll_frame, bg=PANEL, highlightthickness=0, height=120)
        h_scroll = ttk.Scrollbar(scroll_frame, orient="horizontal", command=self.canvas_2d.xview)
        v_scroll = ttk.Scrollbar(scroll_frame, orient="vertical", command=self.canvas_2d.yview)
        
        self.canvas_2d.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)
        
        self.canvas_2d.grid(row=0, column=0, sticky="nsew")
        h_scroll.grid(row=1, column=0, sticky="ew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        
        scroll_frame.rowconfigure(0, weight=1)
        scroll_frame.columnconfigure(0, weight=1)
        
        self.canvas_2d.bind("<Button-1>", self._click_cell_2d)
        
        # ─── Info ──────────────────────────────────────────────────────────
        self.info_2d = tk.Label(inner, text="Click en 'CREAR ARRAY 2D' para empezar",
                               bg=PANEL, fg=TEXT_DIM, font=("Segoe UI", 9, "italic"))
        self.info_2d.pack(fill="x", padx=12, pady=(0, 8))
        
        # ─── Botones de métodos ────────────────────────────────────────────
        self.methods_frame_2d = tk.Frame(inner, bg=PANEL)
        self.methods_frame_2d.pack(fill="x", padx=12, pady=(0, 12))
        self._build_2d_methods()
    
    def _create_2d(self):
        """Dialogo para crear array 2D"""
        dialog = tk.Toplevel(self)
        dialog.title("Crear Array 2D")
        dialog.geometry("340x380")
        dialog.configure(bg=PANEL)
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()
        
        # Filas y columnas
        tk.Label(dialog, text="Filas:", bg=PANEL, fg=TEXT, font=("Segoe UI", 10)).pack(pady=(12, 4))
        rows_var = tk.IntVar(value=3)
        tk.Spinbox(dialog, from_=1, to=10, textvariable=rows_var,
                  bg="#252538", fg=TEXT, font=("Segoe UI", 10),
                  relief="flat", width=10).pack(pady=(0, 12))
        
        tk.Label(dialog, text="Columnas:", bg=PANEL, fg=TEXT, font=("Segoe UI", 10)).pack(pady=(4, 4))
        cols_var = tk.IntVar(value=4)
        tk.Spinbox(dialog, from_=1, to=10, textvariable=cols_var,
                  bg="#252538", fg=TEXT, font=("Segoe UI", 10),
                  relief="flat", width=10).pack(pady=(0, 12))
        
        # Valores
        tk.Label(dialog, text="Valores (separados por comas o saltos de línea):", bg=PANEL,
                fg=TEXT, font=("Segoe UI", 9)).pack(pady=(8, 4))
        
        text_widget = tk.Text(dialog, bg="#252538", fg=TEXT, font=("Segoe UI", 9),
                             height=10, relief="flat", insertbackground=TEXT, width=40)
        text_widget.pack(padx=12, pady=4, fill="both", expand=True)
        
        def create():
            rows = rows_var.get()
            cols = cols_var.get()
            values_text = text_widget.get("1.0", tk.END).strip()
            
            # Crear matriz vacía
            self.arr2d = [[None for _ in range(cols)] for _ in range(rows)]
            
            # Llenar con valores si existen
            if values_text:
                values = values_text.replace('\n', ',').split(',')
                idx = 0
                for r in range(rows):
                    for c in range(cols):
                        if idx < len(values) and values[idx].strip():
                            try:
                                self.arr2d[r][c] = int(values[idx].strip())
                            except:
                                self.arr2d[r][c] = values[idx].strip()
                        idx += 1
            
            self.selected_2d = None
            self._draw_2d()
            self.info_2d.config(text=f"✓ Array 2D creado: {rows}×{cols}")
            self.created_2d = True
            self.btn_create_2d.config(state="disabled", text="✓ Array Creado")
            self._build_2d_methods()
            dialog.destroy()
        
        tk.Button(dialog, text="Crear", command=create, bg=ACCENT2, fg="white",
                 relief="flat", font=("Segoe UI", 10, "bold"), pady=6).pack(pady=12, padx=12, fill="x")
    
    def _draw_2d(self):
        """Dibuja el array 2D"""
        self.canvas_2d.delete("all")
        
        if not self.arr2d:
            self.canvas_2d.create_text(300, 50, text="Array vacío",
                                      fill=TEXT_DIM, font=("Consolas", 12))
            return
        
        rows = len(self.arr2d)
        cols = len(self.arr2d[0]) if rows > 0 else 0
        spacing = 6
        pad_x = 20
        pad_y = 20
        
        for r in range(rows):
            for c in range(cols):
                x0 = pad_x + c * (CELL_W + spacing)
                y0 = pad_y + r * (CELL_H + spacing)
                x1 = x0 + CELL_W
                y1 = y0 + CELL_H
                
                is_sel = (self.selected_2d == (r, c))
                border = CELL_HL if is_sel else CELL_BORDER
                fill = "#4b2d8c" if is_sel else CELL_BG
                
                # Sombra
                self.canvas_2d.create_rectangle(x0+2, y0+2, x1+2, y1+2, fill="#111122", outline="")
                
                # Celda
                self.canvas_2d.create_rectangle(x0, y0, x1, y1, fill=fill, outline=border,
                                              width=2, tags=f"cell_{r}_{c}")
                
                # Valor
                val = self.arr2d[r][c]
                display = str(val) if val is not None else "∅"
                self.canvas_2d.create_text((x0+x1)//2, (y0+y1)//2, text=display,
                                          fill=TEXT, font=("Consolas", 10, "bold"), tags=f"cell_{r}_{c}")
        
        # Etiquetas
        for c in range(cols):
            x0 = pad_x + c * (CELL_W + spacing)
            self.canvas_2d.create_text(x0 + CELL_W//2, pad_y - 12, text=f"C{c}",
                                      fill=ACCENT2, font=("Segoe UI", 8))
        
        for r in range(rows):
            y0 = pad_y + r * (CELL_H + spacing)
            self.canvas_2d.create_text(pad_x - 16, y0 + CELL_H//2, text=f"F{r}",
                                      fill=ACCENT, font=("Segoe UI", 8))
        
        # Scroll region
        total_w = pad_x + cols * (CELL_W + spacing) + 20
        total_h = pad_y + rows * (CELL_H + spacing) + 20
        self.canvas_2d.configure(scrollregion=(0, 0, total_w, total_h))
    
    def _click_cell_2d(self, event):
        """Selecciona una celda 2D"""
        x = self.canvas_2d.canvasx(event.x)
        y = self.canvas_2d.canvasy(event.y)
        items = self.canvas_2d.find_closest(x, y)
        
        for tag in self.canvas_2d.gettags(items[0] if items else -1):
            if tag.startswith("cell_"):
                parts = tag.split("_")
                r, c = int(parts[1]), int(parts[2])
                self.selected_2d = (r, c)
                self._draw_2d()
                val = self.arr2d[r][c]
                self.info_2d.config(text=f"✓ Seleccionado: arr[{r}][{c}] = {val}")
                return
    
    
    def _create_card(self, parent, title: str, color: str) -> tuple:
        """Crea un panel con encabezado, retorna (outer, inner)"""
        outer = tk.Frame(parent, bg=BG)
        
        header = tk.Frame(outer, bg=color, height=40)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text=title, bg=color, fg="white",
                font=("Segoe UI", 12, "bold")).pack(side="left", padx=14, pady=8)
        
        inner = tk.Frame(outer, bg=PANEL)
        inner.pack(fill="both", expand=True)
        
        return outer, inner


#Initializer

if __name__ == "__main__":
    app = ArrayVisualizer()
    app.mainloop()
