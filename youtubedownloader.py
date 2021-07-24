import gi
import subprocess
import urllib.request
from validator_collection import validators, checkers
import re
import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class youtube(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="youtube downloader simple")
        self.set_size_request(800, 500)
        grid = Gtk.Grid()
        self.add(grid)

        entrybox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        grid.add(entrybox)
        self.entry = Gtk.Entry()
        self.entry.set_width_chars(50)
        self.entry.set_size_request(120, 50)
        self.entry.set_margin_left(20)
        self.entry.set_text("paste link ...")
        entrybox.pack_start(self.entry, True, True, 10 )


        buttondownload = Gtk.Button.new_with_label("dowload")
        buttondownload.connect("clicked", self.download)
        buttondownload.set_margin_top(380)
        buttondownload.set_margin_left(200)
        buttondownload.set_size_request(170, 50)
        grid.attach(buttondownload, 1, 2, 1, 2)



        buttoncancel = Gtk.Button.new_with_label("cancel")
        buttoncancel.connect("clicked", self.cancel)
        buttoncancel.set_margin_top(380)
        buttoncancel.set_margin_right(220)
        buttoncancel.set_size_request(170, 50)
        grid.attach(buttoncancel, 1, 2, 1, 2)




    def download(self, button):
        print("ok")
        link = self.entry.get_text()

        response = checkers.is_url(link)

        if(response):

            reg = re.search("youtube*.com", link)
            if reg:
               print(urllib.request.getproxies())	
               system_proxies = urllib.request.getproxies()
	       	      	     
               proxy = system_proxies['https']
               
               subprocess.call(["/home/mrrabbit/.local/bin/youtube-dlc", "--proxy", proxy , link])


            else:
                response = requests.get(link)
                if(response):
                    content = response.content
                    splitlink = link.split('/')
                    leng = len(splitlink) - 1
                    namelink = splitlink[leng]
                    if(namelink != ""):
                        open(namelink, 'wb').write(content)
                    else:
                        namelink = "FILE"
                        open(namelink, 'wb').write(content)
        else:
            win = Gtk.Window()
            win.set_size_request(500, 300)

            errorbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            win.add(errorbox)
            label = Gtk.Label()
            label.set_text("please insert a valid url...!!!")
            label.set_justify(Gtk.Justification.LEFT)
            errorbox.pack_start(label, True, True, 0)
            win.connect("destroy", Gtk.main_quit)
            win.show_all()
            Gtk.main()


    def cancel(self, button):
        self.destroy()



window = youtube()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
