from qgis.PyQt.QtWidgets import (
    QAction,
    QFileDialog,
    QMessageBox
)

from core.xml_parser import XMLParser


class LHPViewerPlugin:

    def __init__(self, iface):

        self.iface = iface
        self.action = None

    def initGui(self):

        self.action = QAction(
            "LHP XML Diagnostic",
            self.iface.mainWindow()
        )

        self.action.triggered.connect(
            self.run
        )

        self.iface.addPluginToMenu(
            "LHP Viewer",
            self.action
        )

    def unload(self):

        if self.action:

            self.iface.removePluginMenu(
                "LHP Viewer",
                self.action
            )

    def run(self):

        xml_file, _ = QFileDialog.getOpenFileName(
            None,
            "Vyber XML",
            "",
            "XML (*.xml)"
        )

        if not xml_file:
            return

        try:

            parser = XMLParser(xml_file)

            psk_count = parser.count_psk()

            QMessageBox.information(
                None,
                "LHP Viewer",
                f"Nalezeno PSK: {psk_count}"
            )

        except Exception as e:

            QMessageBox.critical(
                None,
                "LHP Error",
                str(e)
            )
