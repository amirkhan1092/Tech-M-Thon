from kivy.garden.mapview import MapView
from kivy.app import App
from kivy.uix.label import Label

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        return mapview
        # return Label(text='hello Python')

MapViewApp().run()


