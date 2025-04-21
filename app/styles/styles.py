def apply_modern_style(widget):
    """Aplica um tema moderno e consistente para todos os widgets"""
    widget.setStyleSheet("""
        /* Estilos base */
        QWidget {
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 13px;
        }
        
        /* Estilo para botões */
        QPushButton {
            background-color: #4a6fa5;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 500;
            min-width: 100px;
            transition: background-color 0.3s ease;
        }
        
        QPushButton:hover {
            background-color: #5a8fd8;
        }
        
        QPushButton:pressed {
            background-color: #3a5a80;
        }
        
        QPushButton:disabled {
            background-color: #cccccc;
            color: #666666;
        }
        
        /* Estilo para campos de entrada */
        QLineEdit, QDateEdit, QTextEdit {
            background-color: #ffffff;
            border: 1px solid #d1d1d1;
            padding: 10px 15px;
            border-radius: 6px;
            selection-background-color: #4a6fa5;
            selection-color: white;
        }
        
        QLineEdit:focus, QDateEdit:focus, QTextEdit:focus {
            border: 1px solid #4a6fa5;
            box-shadow: 0 0 0 2px rgba(74, 111, 165, 0.2);
        }
        
        /* Estilo para labels */
        QLabel {
            color: #333333;
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 5px;
        }
        
        /* Estilo para tabelas */
        QTableWidget {
            background-color: #ffffff;
            border: 1px solid #d1d1d1;
            border-radius: 6px;
            gridline-color: #eaeaea;
            font-size: 13px;
        }
        
        QTableWidget::item {
            padding: 8px 12px;
            border-bottom: 1px solid #eaeaea;
        }
        
        QTableWidget::item:selected {
            background-color: #4a6fa5;
            color: white;
        }
        
        QHeaderView::section {
            background-color: #4a6fa5;
            color: white;
            padding: 10px;
            font-weight: 500;
            border: none;
        }
        
        QHeaderView::section:checked {
            background-color: #3a5a80;
        }
        
        /* Barra de rolagem */
        QScrollBar:vertical {
            border: none;
            background: #f5f5f5;
            width: 10px;
            margin: 0px 0px 0px 0px;
        }
        
        QScrollBar::handle:vertical {
            background: #c1c1c1;
            min-height: 20px;
            border-radius: 5px;
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }
        
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
    """)


# Versões individuais para cada widget (opcional)
def apply_button_style(button):
    button.setStyleSheet("""
        QPushButton {
            background-color: #4a6fa5;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: 500;
            min-width: 100px;
            transition: background-color 0.3s ease;
        }
        QPushButton:hover {
            background-color: #5a8fd8;
        }
        QPushButton:pressed {
            background-color: #3a5a80;
        }
        QPushButton:disabled {
            background-color: #cccccc;
            color: #666666;
        }
    """)

def apply_input_style(input_widget):
    input_widget.setStyleSheet("""
        QLineEdit {
            background-color: #ffffff;
            border: 1px solid #d1d1d1;
            padding: 10px 15px;
            border-radius: 6px;
            color: #333333;  /* Texto escuro para contraste */
            selection-background-color: #4a6fa5;
            selection-color: white;
        }
    """)

def apply_date_edit_style(date_edit):
    date_edit.setStyleSheet("""
        QDateEdit {
            background-color: #ffffff;
            border: 1px solid #d1d1d1;
            padding: 10px 15px;
            border-radius: 6px;
        }
        QDateEdit:focus {
            border: 1px solid #4a6fa5;
            box-shadow: 0 0 0 2px rgba(74, 111, 165, 0.2);
        }
        QDateEdit::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
            border-left-width: 1px;
            border-left-color: #d1d1d1;
            border-left-style: solid;
            border-top-right-radius: 6px;
            border-bottom-right-radius: 6px;
        }
    """)

def apply_label_style(label):
    label.setStyleSheet("""
        QLabel {
            color: #333333;
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 5px;
        }
        QLabel[important="true"] {
            color: #d32f2f;
            font-weight: 600;
        }
    """)

def apply_table_style(table):
    table.setStyleSheet("""
        QTableWidget {
            background-color: #ffffff;
            border: 1px solid #d1d1d1;
            border-radius: 6px;
            gridline-color: #eaeaea;
        }
        QTableWidget::item {
            color: #333333;  /* Texto escuro */
            padding: 8px 12px;
            border-bottom: 1px solid #eaeaea;
        }
        QTableWidget::item:selected {
            background-color: #4a6fa5;
            color: white;  /* Texto branco quando selecionado */
        }
        QHeaderView::section {
            background-color: #4a6fa5;
            color: white;
            padding: 10px;
            border: none;
        }
    """)

def apply_text_edit_style(text_edit):
    text_edit.setStyleSheet("""
        QTextEdit {
            background-color: #ffffff;
            border: 1px solid #d1d1d1;
            padding: 10px;
            border-radius: 6px;
            color: #333333;  /* Texto escuro */
        }
        QTextEdit:focus {
            border: 1px solid #4a6fa5;
        }
    """)