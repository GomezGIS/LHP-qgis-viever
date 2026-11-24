from qgis.PyQt.QtWidgets import QAction, QFileDialog, QMessageBox
import xml.etree.ElementTree as ET
import os


class LHPViewerPlugin:

    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def initGui(self):

        self.action = QAction(
            "LHP XML Diagnostic Import",
            self.iface.mainWindow()
        )

        self.action.triggered.connect(self.run)

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

            tree = ET.parse(xml_file)
            root = tree.getroot()

            psk_count = len(root.findall(".//PSK"))

            log_file = os.path.join(
                os.path.dirname(xml_file),
                "lhp_import.log"
            )

            with open(
                log_file,
                "w",
                encoding="utf-8"
            ) as log:

                log.write(
                    "LHP Viewer Diagnostic 0.1a\n"
                )
                log.write(
                    f"XML: {xml_file}\n"
                )
                log.write(
                    f"PSK count: {psk_count}\n"
                )

            QMessageBox.information(
                None,
                "LHP Viewer",
                f"Nalezeno PSK: {psk_count}\n\n"
                f"Log:\n{log_file}"
            )

        except Exception as e:

            QMessageBox.critical(
                None,
                "LHP Viewer Error",
                str(e)
            )
