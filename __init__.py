def classFactory(iface):
    from .plugin import LHPViewerPlugin
    return LHPViewerPlugin(iface)
