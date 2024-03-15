def populate_table(self):
        # Ottieni la lista dei tempi unici presenti nel database
        self.db.connect()
        unique_times = set()
        notes = self.db.fetch_records("notes")
        if notes:
            for note in notes:
                unique_times.add(note[3].replace(" ", ""))  # Aggiungi il tempo alla lista dei tempi unici

        # Inserisci le righe nella tabella con l'header corrispondente al tempo
        print(unique_times)
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
                        if self.ui.tableWidget.horizontalHeaderItem(col).text().replace(" ", "") == weekday and \
                                self.ui.tableWidget.verticalHeaderItem(row_count).text().replace(" ", "") == time:
                            # Inserisci il testo della colonna "title" nella cella corrispondente
                            title = note[1]
                            print(self.ui.tableWidget.horizontalHeaderItem(col).text())
                            print(self.ui.tableWidget.verticalHeaderItem(row_count).text())
                            self.ui.tableWidget.setItem(row_count, col, QTableWidgetItem(title))
                            break
                        else:
                            print("Qualcosa non va")