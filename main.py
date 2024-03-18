# -*- coding: utf-8 -*-

# Importazione moduli #

# Moduli PySide6:
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QGraphicsOpacityEffect
from PySide6.QtGui import QTextCharFormat, QTextDocument
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QPropertyAnimation, QTimer, QTime
from PySide6.QtPrintSupport import QPrinter

# Moduli per gestire gli orari e i giorni:
from datetime import datetime, timedelta
import locale
import time

# Moduli threading:
#from threading import Thread

# Moduli database:
import sqlite3
from sqlite3 import Error

# Moduli layout:
from ui_main import *

# Moduli di sistema:
import sys
import userpaths
import os

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml, OxmlElement

import html2text

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.documents_path = userpaths.get_appdata()
        # Verifica se la cartella "WeekPlanner" esiste già
        if not os.path.exists(self.documents_path+"\\WeekPlanner\\"):
            os.makedirs(self.documents_path+"\\WeekPlanner\\")

    def connect(self):
        # Connessione al database
        self.conn = sqlite3.connect(self.documents_path+"\\WeekPlanner\\"+self.db_name)

    def disconnect(self):
        # Chiusura della connessione al database
        if self.conn:
            self.conn.close()
        
    def create_table(self, table_name, columns):
        # Creazione di una tabella con i nomi di colonne specificati
        if self.conn:
            cursor = self.conn.cursor()
            column_str = ', '.join(columns)
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({column_str})')
            self.conn.commit()

    def insert_record(self, table_name, values):
        # Inserisce una nuova riga nella tabella specificata
        if self.conn:
            cursor = self.conn.cursor()
            placeholder_str = ', '.join(['?' for _ in range(len(values))])
            cursor.execute(f'INSERT INTO {table_name} VALUES (NULL, {placeholder_str})', values)
            self.conn.commit()

    def fetch_records(self, table_name, order_by=None):
        # Ottiene tutte le righe dalla tabella specificata, eventualmente ordinate
        if self.conn:
            cursor = self.conn.cursor()
            if order_by:
                cursor.execute(f'SELECT * FROM {table_name} ORDER BY {order_by}')
            else:
                cursor.execute(f'SELECT * FROM {table_name}')
            return cursor.fetchall()
        
    def delete_record(self, table_name, record_id):
        # Elimina un record dalla tabella specificata dato il suo ID
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute(f'DELETE FROM {table_name} WHERE id = ?', (record_id,))
            self.conn.commit()

    
    def delete_all_records(self, table_name):
        # Elimina tutti i record dalla tabella specificata
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute(f'DELETE FROM {table_name}')
            self.conn.commit()

    def update_record(self, table_name, column_to_update, new_value, condition_column1, condition_value1, condition_column2, condition_value2):
        # Aggiorna un record nella tabella specificata
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute(f'UPDATE {table_name} SET {column_to_update} = ? WHERE {condition_column1} = ? AND {condition_column2} = ?', (new_value, condition_value1, condition_value2))
            self.conn.commit()
    
    def get_formatted_text(self, note_id):
        try:
            # Connetti al database
            self.connect()
            cursor = self.conn.cursor()
            # Esegui la query per recuperare il testo formattato dalla riga corrispondente
            cursor.execute("SELECT text FROM notes WHERE id = ?", (note_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Error as e:
            print("Errore durante il recupero del testo formattato:", e)
            return None
        finally:
            # Chiudi la connessione al database
            self.disconnect()

class AddRowDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inserisci l'orario")
        self.setStyleSheet(
            "QDialog { background-color: #E9ECEF; border-radius: 10px; }"  # Aggiungi un bordo arrotondato al dialogo
            "QLabel { color: #212529; font-size: 14px; }"  # Modifica la dimensione del carattere per i label
            "QTimeEdit { background-color: #ADB5BD; color: #212529; border-radius: 5px; padding: 4px; }"  # Aggiungi un bordo arrotondato e modifica il colore per i QTimeEdit e inserisci del padding interno
            "QTimeEdit::down-arrow { image: url(:/icons/down-arrow.png); width: 12px; height: 12px; }"  # Aggiungi lo stile per la freccia verso il basso
            "QTimeEdit::up-arrow { image: url(:/icons/up-arrow.png); width: 12px; height: 12px; }"  # Utilizza un'icona più moderna per la freccia verso l'alto
            "QTimeEdit::drop-down { subcontrol-origin: padding; subcontrol-position: center right; width: 20px; border-left-width: 0px; }"  # Posiziona il menu a discesa al centro e modifica la larghezza
        )

        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)
        
        self.time_picker_start = QtWidgets.QTimeEdit()
        self.time_picker_start.setDisplayFormat("HH:mm")
        self.time_picker_start.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.time_picker_start)
        
        separator_label = QtWidgets.QLabel("-")
        separator_label.setStyleSheet("QLabel { font-size: 18px; }")
        layout.addWidget(separator_label)
        
        self.time_picker_end = QtWidgets.QTimeEdit()
        self.time_picker_end.setDisplayFormat("HH:mm")
        self.time_picker_end.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.time_picker_end)
        
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        # Imposta il valore minimo del secondo time picker in base al valore del primo
        self.time_picker_start.timeChanged.connect(self.update_end_time_min)

    def update_end_time_min(self):
        start_time = self.time_picker_start.time()
        self.time_picker_end.setMinimumTime(start_time.addSecs(60))  # Imposta il valore minimo come il tempo selezionato più un minuto

    def get_time_interval(self):
        start_time = self.time_picker_start.time().toString("HH:mm")
        end_time = self.time_picker_end.time().toString("HH:mm")
        if start_time and end_time:
            return f"{start_time}-{end_time}"
        else:
            return ""


class MainAppScreen(QMainWindow):
    def __init__(self):
        super(MainAppScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Rende la finestra senza cornice
        self.db = Database("my_database.db")
        self.db.connect()
        self.db.create_table(
            table_name="notes", 
            columns=[
                "id INTEGER PRIMARY KEY", 
                "title TEXT NOT NULL", 
                "day DATE NOT NULL",
                "time TEXT NOT NULL",
                "weekday TEXT NOT NULL",
                "text TEXT NOT NULL"
                     ]
            )
        self.drag_position = QtCore.QPoint()  # Variabile per memorizzare la posizione del mouse durante il trascinamento
        self.setup_ui()  # Configura l'interfaccia utente e i gestori eventi del mouse
        self.show()  # Mostra la finestra
        self.current_week_start = datetime.now()
        # Imposta le dimensioni di base della finestra
        self.resize(1120, 610)

    def setup_ui(self):
        # Imposta le dimensioni della tabella in base alle dimensioni della finestra
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Collegamento delle funzioni ai bottoni
        self.ui.pushButton_7.clicked.connect(self.toggle_bold)
        self.ui.pushButton_10.clicked.connect(self.toggle_italic)
        self.ui.pushButton_11.clicked.connect(self.toggle_underline)
        self.ui.pushButton_12.clicked.connect(self.insert_unordered_list)
        self.ui.pushButton_13.clicked.connect(self.insert_ordered_list)
        self.ui.pushButton_14.clicked.connect(self.set_text_color)

        # Colleghiamo le funzioni ai bottoni
        self.ui.pushButton_4.clicked.connect(self.resize_window)
        self.ui.pushButton_2.clicked.connect(self.minimize_window)
        self.ui.pushButton_3.clicked.connect(self.close_window)

        # Collega gli eventi del mouse per il trascinamento della finestra alla barra del titolo
        self.ui.frame_2.mouseMoveEvent = self.mouseMoveEvent
        self.ui.frame_2.mousePressEvent = self.mousePressEvent

        # Imposta la larghezza minima del frame
        self.ui.frame_9.setMinimumWidth(130)
        self.ui.frame_9.setMaximumWidth(270)

        # Abilita la formattazione ricca del testo
        self.ui.textEdit.setAcceptRichText(True)

        # Bottone per aggiungere una nuova riga
        self.ui.pushButton_6.clicked.connect(self.add_row_dialog)
        
        self.ui.tableWidget.cellClicked.connect(self.clear_text_edit)

        # Colleghiamo la funzione per aggiornare il testo del QLabel all'evento cellChanged
        self.ui.tableWidget.cellChanged.connect(self.update_label_text)

        # Colleghiamo la funzione per cancellare il testo del QTextEdit all'evento cellClicked
        self.ui.tableWidget.cellClicked.connect(self.update_label_text)

        self.ui.pushButton_9.clicked.connect(self.save_notes)

        self.ui.pushButton_8.clicked.connect(self.delete_selected_cells)

        self.ui.pushButton_17.clicked.connect(self.highlight_text)

        self.ui.pushButton_16.clicked.connect(self.save_to_pdf)

        # Collega la funzione change_text_format al segnale currentIndexChanged
        self.ui.comboBox.currentIndexChanged.connect(self.change_text_format)

        # Imposta i titoli delle colonne in grassetto
        header = self.ui.tableWidget.horizontalHeader()
        font = header.font()
        font.setBold(True)
        header.setFont(font)

        # Imposta la localizzazione italiana per ottenere i nomi dei giorni della settimana in italiano
        locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')

        # Imposta gli header orizzontali della tabella con i nomi dei giorni della settimana e le relative date
        self.set_horizontal_headers()
        self.ui.pushButton_5.clicked.connect(self.update_horizontal_headers_next_week)
         # Connetti il segnale sectionDoubleClicked dell'header verticale al metodo per modificare l'orario
        self.ui.tableWidget.verticalHeader().sectionDoubleClicked.connect(self.modify_time)


        self.ui.pushButton_15.clicked.connect(self.update_horizontal_headers_previous_week)
        # Recupera i dati dal database e popola la tabella
        self.populate_table()

    def modify_time(self, row):
        # Ottieni l'indice della colonna degli orari
        orario_column_index = 0  # Assumendo che la colonna degli orari sia la prima (indice 0)

        # Ottieni l'orario corrente nella cella corrispondente
        current_time_item = self.ui.tableWidget.verticalHeaderItem(row)
        if current_time_item is not None:
            current_time = current_time_item.text()

            # Apri la finestra di dialogo per modificare l'orario
            dialog = AddRowDialog()
            dialog.setWindowTitle("Modifica Orario")
            dialog.time_picker_start.setTime(QTime.fromString(current_time.split('-')[0], 'hh:mm'))
            dialog.time_picker_end.setTime(QTime.fromString(current_time.split('-')[1], 'hh:mm'))
            if dialog.exec_():
                # Ottieni il nuovo intervallo di tempo dalla finestra di dialogo
                new_time_interval = dialog.get_time_interval()

                # Aggiorna l'orario nella cella corrispondente
                new_time_item = QtWidgets.QTableWidgetItem(new_time_interval)
                self.ui.tableWidget.setVerticalHeaderItem(row, new_time_item)

    def update_horizontal_headers_next_week(self):
        # Trova la data del Lunedì della prossima settimana
        self.current_week_start += timedelta(days=(7 - self.current_week_start.weekday()))
        
        # Formatta gli header orizzontali della tabella con i nomi dei giorni e le relative date in italiano
        giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
        for i, giorno in enumerate(giorni_settimana):
            current_day = self.current_week_start + timedelta(days=i)
            # Utilizza il metodo title() per avere le iniziali dei nomi dei giorni in maiuscolo
            header_text = giorno + " " + current_day.strftime("%d/%m")
            header_item = QTableWidgetItem()
            header_item.setText(header_text)
            self.ui.tableWidget.setHorizontalHeaderItem(i, header_item)
        
        self.populate_table()

    def update_horizontal_headers_previous_week(self):
        # Trova la data del Lunedì della settimana precedente
        self.current_week_start -= timedelta(days=(self.current_week_start.weekday() + 7))
        
        # Formatta gli header orizzontali della tabella con i nomi dei giorni e le relative date in italiano
        giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
        for i, giorno in enumerate(giorni_settimana):
            current_day = self.current_week_start + timedelta(days=i)
            # Utilizza il metodo title() per avere le iniziali dei nomi dei giorni in maiuscolo
            header_text = giorno + " " + current_day.strftime("%d/%m")
            header_item = QTableWidgetItem()
            header_item.setText(header_text)
            self.ui.tableWidget.setHorizontalHeaderItem(i, header_item)
        
        self.populate_table()

    def set_horizontal_headers(self):
        # Ottieni la data di oggi
        today = datetime.now()
        
        # Trova la data del Lunedì della settimana corrente
        start_of_week = today - timedelta(days=today.weekday())

        # Formatta gli header orizzontali della tabella con i nomi dei giorni e le relative date in italiano
        giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
        for i, giorno in enumerate(giorni_settimana):
            current_day = start_of_week + timedelta(days=i)
            # Utilizza il metodo title() per avere le iniziali dei nomi dei giorni in maiuscolo
            header_text = self.ui.tableWidget.horizontalHeaderItem(i).text() + " " + current_day.strftime("%d/%m")
            header_item = QTableWidgetItem()
            header_item.setText(header_text)
            self.ui.tableWidget.setHorizontalHeaderItem(i, header_item)

    def current_week_dates():
        # Trova la data di oggi
        today = datetime.date.today()

        # Trova il giorno della settimana (0 = Lunedì, 1 = Martedì, ..., 6 = Domenica)
        current_day_of_week = today.weekday()

        # Trova la data del Lunedì della settimana corrente
        start_of_week = today - datetime.timedelta(days=current_day_of_week)

        # Crea una lista di oggetti datetime.date per i giorni della settimana corrente
        week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]

        return week_dates
    
    def get_orario_column_index(self):
        # Ottieni il numero totale di colonne
        total_columns = self.ui.tableWidget.columnCount()

        # Cerca il testo degli header orizzontali per trovare la colonna degli orari
        for col in range(total_columns):
            header_text = self.ui.tableWidget.horizontalHeaderItem(col).text()
            if "Orario" in header_text:  # Modifica questa condizione in base al testo effettivo dell'header
                return col

        return -1  # Ritorna -1 se non viene trovata la colonna degli orari
    
    def populate_table(self):
        # Pulisci la tabella prima di popolarla nuovamente
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        horizontal_header = self.ui.tableWidget.horizontalHeader()
        header_list = [] 

        # Itera su tutti gli header orizzontali e aggiungili alla lista
        for index in range(horizontal_header.count()):
            header_text = horizontal_header.model().headerData(index, Qt.Horizontal)
            header_list.append(header_text)

        # Ottieni la lista dei tempi unici presenti nel database
        self.db.connect()
        unique_times = set()
        notes = self.db.fetch_records("notes", order_by="time")
        count = 0
        if notes:
            for note in notes:
                if note[4] in header_list:
                    count = True
                    unique_times.add(note[3].replace(" ", ""))  # Aggiungi il tempo alla lista dei tempi unici

        
        # Ordina gli orari in modo crescente
        unique_times = sorted(unique_times)
        #print(unique_times)
        # Inserisci le righe nella tabella con l'header corrispondente al tempo
        for time in unique_times:
            # Aggiungi una nuova riga
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)
            # Imposta l'header della riga con il tempo
            header_item = QTableWidgetItem(time)
            header_item.setFont(QFont("Arial", weight=QFont.Bold))
            self.ui.tableWidget.setVerticalHeaderItem(row_count, header_item)

            # Popola la riga con i dati dalla tabella "notes" per il tempo corrente
            for note in notes:
                if note[3].replace(" ", "") == time.replace(" ", ""):
                    # Trova la cella corrispondente per weekday
                    weekday = note[4].replace(" ", "")
                    for col in range(self.ui.tableWidget.columnCount()):
                        if weekday in self.ui.tableWidget.horizontalHeaderItem(col).text().replace(" ", "") and \
                                self.ui.tableWidget.verticalHeaderItem(row_count).text().replace(" ", "") == time:
                            # Inserisci il testo della colonna "title" nella cella corrispondente
                            title = note[1]
                            item = QTableWidgetItem(title)
                            item.setData(Qt.UserRole, note[0])  # Imposta l'ID del database come metadata della cella
                            self.ui.tableWidget.setItem(row_count, col, item)
                            break

        # Collega l'evento cellClicked per mostrare il testo formattato nel QTextEdit
        self.ui.tableWidget.cellClicked.connect(self.show_formatted_text)

    def save_to_pdf(self):
        # Ottieni il percorso del file PDF in cui salvare il documento
        file_path, _ = QFileDialog.getSaveFileName(self, "Salva come PDF", "", "File PDF (*.pdf)")

        if file_path:
            # Crea un documento PDF
            doc = SimpleDocTemplate(file_path, pagesize=letter)
            
            # Stile per il titolo
            styles = getSampleStyleSheet()
            title_style = styles["Title"]
            
            # Aggiungi il titolo al documento
            title = Paragraph("<b>Il mio programma settimanale</b>", title_style)
            elements = [title]
            
            # Ottieni i dati dalla tabella
            data = []
            header = []
            
            # Aggiungi gli header verticali
            for row in range(self.ui.tableWidget.rowCount()):
                row_data = []
                row_header = self.ui.tableWidget.verticalHeaderItem(row).text()
                row_data.append(row_header)
                for column in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, column)
                    if item:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                data.append(row_data)
            
            # Aggiungi l'header orizzontale
            horizontal_header = [""]  # Header per la prima cella vuota
            for column in range(self.ui.tableWidget.columnCount()):
                column_header = self.ui.tableWidget.horizontalHeaderItem(column).text()
                horizontal_header.append(column_header)
            data.insert(0, horizontal_header)

            # Aggiungi il testo del QTextEdit al documento PDF
            text = self.ui.textEdit.toPlainText()

            # Aggiungi la tabella al documento PDF
            table = Table(data)
            table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

            # Aggiungi il testo alla tabella
            data.insert(0, [''] * len(data[0]))  # Aggiungi una riga vuota all'inizio per il testo
            data.append([''] * len(data[0]))  # Aggiungi una riga vuota alla fine per il testo
            data.append(["Testo:", text])  # Aggiungi il testo alla fine

            # Costruisci la struttura del documento
            elements.append(table)

            # Usa la classe Database per ottenere le note
            db = Database("my_database.db")  # Istanza della classe Database
            db.connect()
            notes = db.fetch_records("notes")  # Supponi che "notes" sia il nome della tabella delle note

            # Aggiungi le note al documento PDF
            for note in notes:
                # Aggiungi il testo della nota
                note_text = db.get_formatted_text(note[0])  # Supponi che il primo elemento di ogni riga sia l'ID della nota
                if note_text:
                    # Converti il markup HTML in testo normale
                    plain_text = html2text.html2text(note_text)
                    # Aggiungi il testo HTML alla struttura del documento
                    note_paragraph = Paragraph(plain_text, styles["Normal"])
                    #elements.append(note_paragraph)

                # Aggiungi tutte le informazioni della nota
                note_info = f"Title: {note[1]}, Day: {note[2]}, Time: {note[3]}, Weekday: {note[4]}, Text: {plain_text}"
                note_info_paragraph = Paragraph(note_info, styles["Normal"])
                elements.append(note_info_paragraph)

            # Scrivi il documento PDF
            doc.build(elements)

            QMessageBox.information(self, "Salvataggio completato", "Il documento è stato salvato come PDF.")

    def get_table_data_with_headers(self):
        # Ottieni i dati dalla tabella
        data = []
        header = []
        
        # Aggiungi gli header verticali
        for row in range(self.ui.tableWidget.rowCount()):
            row_data = []
            row_header = self.ui.tableWidget.verticalHeaderItem(row).text()
            row_data.append(row_header)
            for column in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, column)
                if item:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data.append(row_data)
        
        # Aggiungi l'header orizzontale
        horizontal_header = [""]  # Header per la prima cella vuota
        for column in range(self.ui.tableWidget.columnCount()):
            column_header = self.ui.tableWidget.horizontalHeaderItem(column).text()
            horizontal_header.append(column_header)
        data.insert(0, horizontal_header)

        return data, horizontal_header
    
    def convert_html_to_plain_text(self, html_text):
        # Carica il testo HTML in un documento QTextDocument
        doc = QTextDocument()
        doc.setHtml(html_text)

        # Estrai il testo formattato dal documento
        plain_text = doc.toPlainText()

        return plain_text
    
    def get_formatted_text_elements(self):
        # Ottieni i testi delle note con la formattazione
        elements = []
        for row in range(self.ui.tableWidget.rowCount()):
            for column in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, column)
                if item:
                    note_id = item.data(Qt.UserRole)
                    formatted_text = self.get_formatted_text_from_database(note_id)
                    if formatted_text:
                        # Aggiungi il testo formattato come elemento Paragraph
                        styles = getSampleStyleSheet()
                        note_paragraph = Paragraph(formatted_text, styles["Normal"])
                        elements.append(note_paragraph)
        return elements
    
    def show_formatted_text(self, row, column):
        # Ottieni l'elemento selezionato
        item = self.ui.tableWidget.item(row, column)
        if item:
            # Ottieni l'ID del database dall'elemento
            note_id = item.data(Qt.UserRole)
            # Ottieni il testo formattato dalla riga corrispondente nel database
            formatted_text = self.get_formatted_text_from_database(note_id)
            # Mostra il testo formattato nel QTextEdit
            self.ui.textEdit.setHtml(formatted_text)

    def get_formatted_text_from_database(self, note_id):
        # Ottieni il testo formattato dalla riga corrispondente nel database
        formatted_text = self.db.get_formatted_text(note_id)
        if formatted_text:
            return formatted_text
        else:
            return "<b>Ancora nessuna nota</b>"

    def time_to_minutes(self, time_str):
        # Converte l'intervallo di tempo nel formato "HH:MM-HH:MM" in minuti totali
        start_time, end_time = time_str.split("-")
        start_hours, start_minutes = map(int, start_time.split(":"))
        end_hours, end_minutes = map(int, end_time.split(":"))
        total_minutes = (end_hours - start_hours) * 60 + (end_minutes - start_minutes)
        return total_minutes

    def time_range_to_minutes(self, time_range):
        # Dividi l'intervallo di tempo nei due orari di inizio e fine
        start_time, end_time = time_range.split("-")

        # Estrai le ore e i minuti dall'orario di inizio
        start_hour, start_minute = map(int, start_time.split(":"))

        # Estrai le ore e i minuti dall'orario di fine
        end_hour, end_minute = map(int, end_time.split(":"))

        # Calcola i minuti totali dall'orario di inizio all'orario di fine
        total_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)

        return total_minutes

    # Funzione per inserire una nuova nota nel database
    def insert_note(self, title, text, day, time, weekday):
        self.db.connect()
        try:
            # Controlla se esiste già una nota con lo stesso giorno, titolo, tempo e giorno della settimana
            existing_notes = self.db.fetch_records("notes")
            for note in existing_notes:
                if note[3].replace(" ", "") == time.replace(" ", "") and note[4].replace(" ", "") == weekday.replace(" ", ""):
                    # Se esiste una nota con gli stessi dettagli, aggiorna il testo invece di inserire una nuova nota
                    self.db.update_record("notes", "text", text, "time", time, "weekday", weekday)
                    self.db.update_record("notes", "title", title, "time", time, "weekday", weekday)
                    return True
            # Se non esiste una nota con gli stessi dettagli, inserisci una nuova nota
            self.db.insert_record("notes", (title, day, time, weekday, text))
            return True
        except Error as e:
            print("Errore durante l'inserimento o l'aggiornamento della nota nel database:", e)
            return False
        
    def delete_selected_cells(self):
        # Ottieni tutte le celle selezionate
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            # Conferma l'eliminazione con una finestra di dialogo
            confirm = QMessageBox.question(self, "Conferma Eliminazione", "Sei sicuro di voler eliminare queste note?",
                                            QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.db.connect()
                for item in selected_items:
                    # Ottieni l'ID del record dal metadata della cella
                    note_id = item.data(Qt.UserRole)
                    if note_id is not None:
                        # Elimina il record dal database
                        self.db.delete_record("notes", note_id)
                    else:
                        QMessageBox.warning(self, "Errore", "Impossibile trovare l'ID della nota selezionata.")
                self.db.disconnect()

                # Rimuovi le righe corrispondenti dalle intestazioni verticali della tabella
                rows_to_remove = set()
                for item in selected_items:
                    rows_to_remove.add(item.row())
                for row in sorted(rows_to_remove, reverse=True):
                    self.ui.tableWidget.removeRow(row)
        else:
            QMessageBox.warning(self, "Selezione", "Nessuna cella selezionata.")

        # Recupera i dati dal database e popola la tabella
        self.populate_table()

    def show_popup(self, message, color):
        self.popup = QMessageBox()
        self.popup.setWindowTitle("Successo")
        self.popup.setText(message)
        self.popup.setStandardButtons(QMessageBox.Ok)

        # Imposta la finestra del popup senza cornice
        self.popup.setWindowFlags(Qt.FramelessWindowHint)
        # Imposta uno stile minimalista al popup
        self.popup.setStyleSheet(f"QMessageBox {{ border: none; background-color: {color}; }}")

        # Imposta un timer per chiudere automaticamente il popup dopo 2 secondi
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.popup.close)
        self.timer.start(1000)  # 2000 millisecondi (2 secondi)

        # Visualizza il popup
        self.popup.show()


    def save_notes(self):
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                row = item.row()
                column = item.column()
                title = item.text()
                text = self.ui.textEdit.toHtml()
                current_time = datetime.now()
                day = current_time.strftime("%Y-%m-%d")
                time = self.ui.tableWidget.verticalHeaderItem(row).text()
                weekday = self.ui.tableWidget.horizontalHeaderItem(column).text()
                if self.insert_note(title, text, day, time, weekday):
                    print(f"Nota salvata con successo per la cella {row}, {column} nel database!")
                    self.show_popup("Nota salvata con successo!", "#dde5b6")
                    self.populate_table()
                else:
                    print(f"Errore durante il salvataggio della nota per la cella {row}, {column} nel database.")
                    self.show_popup("Qualcosa è andato storto", "#f38375")
        else:
            print("Nessuna nota selezionata.")
            self.show_popup("Nessuna nota selezionata", "#f38375")


    def update_label_text(self, row, column):
        # Aggiorna il testo del QLabel con il testo della cella modificata
        item = self.ui.tableWidget.item(row, column)
        if item is not None:
            # Ottieni il testo della cella
            cell_text = item.text()

            # Ottieni il titolo dell'header della riga e della colonna
            row_header_text = self.ui.tableWidget.verticalHeaderItem(row).text()
            column_header_text = self.ui.tableWidget.horizontalHeaderItem(column).text()

            # Aggiungi il testo dell'header della riga e della colonna al testo della cella
            label_text = f"{cell_text} | {column_header_text} | {row_header_text}"
            
            # Imposta il testo del QLabel
            self.ui.label_2.setText(label_text)

    def clear_text_edit(self):
        # Cancella il contenuto del QTextEdit quando viene cliccata una cella della tabella
        self.ui.textEdit.clear()

    def add_row_dialog(self):
        # Mostra la finestra di dialogo personalizzata per inserire l'intervallo di tempo della nuova riga
        dialog = AddRowDialog(self)
        if dialog.exec_():
            time_interval = dialog.get_time_interval()
            
            if time_interval:
                # Aggiunge una nuova riga con l'intervallo di tempo inserito
                row_count = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row_count)
                for col in range(self.ui.tableWidget.columnCount()):
                    item = QtWidgets.QTableWidgetItem("")
                    self.ui.tableWidget.setItem(row_count, col, item)

                header_item = QtWidgets.QTableWidgetItem(time_interval)
                header_item.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))  # Imposta il grassetto
                self.ui.tableWidget.setVerticalHeaderItem(row_count, header_item)

    def toggle_bold(self):
        # Applica o rimuove la formattazione in grassetto al testo selezionato
        font = self.ui.textEdit.currentFont()
        font.setBold(not font.bold())
        self.ui.textEdit.setCurrentFont(font)

    def toggle_italic(self):
        # Applica o rimuove la formattazione in corsivo al testo selezionato
        font = self.ui.textEdit.currentFont()
        font.setItalic(not font.italic())
        self.ui.textEdit.setCurrentFont(font)

    def toggle_underline(self):
        # Applica o rimuove la formattazione sottolineato al testo selezionato
        font = self.ui.textEdit.currentFont()
        font.setUnderline(not font.underline())
        self.ui.textEdit.setCurrentFont(font)

    def insert_unordered_list(self):
        # Inserisce una lista non ordinata nel cursore attuale del QTextEdit
        cursor = self.ui.textEdit.textCursor()
        cursor.insertHtml("<ul><li>Item 1</li><li>Item 2</li></ul>")

    def insert_ordered_list(self):
        # Inserisce una lista ordinata nel cursore attuale del QTextEdit
        cursor = self.ui.textEdit.textCursor()
        cursor.insertHtml("<ol><li>Item 1</li><li>Item 2</li></ol>")

    def set_text_color(self):
        # Imposta il colore del testo nel QTextEdit
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.textEdit.setTextColor(color)

    def highlight_text(self):
        # Ottieni il testo selezionato nel QTextEdit
        selected_text = self.ui.textEdit.textCursor().selectedText()

        # Se non c'è testo selezionato, esci dalla funzione
        if not selected_text:
            return

        # Ottieni il colore selezionato dall'utente
        color = QColorDialog.getColor()
        if color.isValid():
            # Aggiorna il colore di sfondo del bottone con il colore selezionato dall'utente
            #self.ui.pushButton_14.setStyleSheet("background-color: " + color.name())

            # Ottieni il formato di carattere corrente
            cursor = self.ui.textEdit.textCursor()
            char_format = cursor.charFormat()

            # Aggiorna il formato di carattere con il nuovo colore di sfondo
            char_format.setBackground(color)

            # Applica il nuovo formato di carattere solo alla selezione attuale
            cursor.setCharFormat(char_format)

    @QtCore.Slot()
    def change_text_format(self, index):
        # Ottieni il formato selezionato dal combobox
        format_type = self.ui.comboBox.currentText()

        # Crea un formato di carattere in base al tipo di formato selezionato
        char_format = QTextCharFormat()
        if format_type == "Titolo":
            char_format.setFontPointSize(18)
            char_format.setFontWeight(QFont.Bold)
        elif format_type == "Sottotitolo":
            char_format.setFontPointSize(12)
            char_format.setFontWeight(QFont.DemiBold)  # Grassetto leggero
        elif format_type == "Paragrafo":
            char_format.setFontPointSize(10)
        
        # Ottieni il testo selezionato nel QTextEdit
        selected_text = self.ui.textEdit.textCursor().selectedText()

        # Se c'è del testo selezionato, applica il formato a tale testo
        if selected_text:
            cursor = self.ui.textEdit.textCursor()
            cursor.setCharFormat(char_format)
        else:
            # Altrimenti, applica il formato al testo che verrà digitato successivamente
            self.ui.textEdit.setCurrentCharFormat(char_format)

    def resize_window(self):
        # Ridimensiona la finestra
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_4.setIcon(QIcon(":/icons/resize (1).png"))
        else:
            self.showMaximized()
            self.ui.pushButton_4.setIcon(QIcon(":/icons/minimize (1).png"))

    def minimize_window(self):
        # Riduce la finestra ad icona
        self.showMinimized()

    def close_window(self):
        # Chiude la finestra
        self.close()

    def mousePressEvent(self, event):
        # Gestisce l'evento di pressione del mouse
        if event.button() == Qt.LeftButton:  # Verifica se è stato premuto il pulsante sinistro del mouse
            self.drag_position = event.globalPos() - self.pos()  # Calcola la posizione relativa del mouse rispetto all'angolo superiore sinistro della finestra
            event.accept()  # Accetta l'evento di pressione del mouse

    def mouseMoveEvent(self, event):
        # Gestisce l'evento di movimento del mouse
        if event.buttons() == Qt.LeftButton:  # Verifica se il pulsante sinistro del mouse è stato premuto
            self.move(event.globalPos() - self.drag_position)  # Sposta la finestra in base al movimento del mouse rispetto alla sua posizione iniziale
            event.accept()  # Accetta l'evento di movimento del mouse

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainAppScreen()
    sys.exit(app.exec())