"""

This script is a wrapper to allow imglib2-imglyb code that uses Java's AWT
to run properly on OS X.  It starts the Cocoa event loop before Java and
keeps Cocoa happy  See https://github.com/kivy/pyjnius/issues/151 for more.

In particular, this wrapper allows one to run the code from imglyb-examples.

Tested in Python 3 only!  Not sure if you'd need to change anything for Python 2
beyond the print statements.

usage: python OSXAWTwrapper.py [module name | script path] [module or script parameters]

"""

import objc
from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper

import imagej

usage = "usage: python OSXAWTwrapper.py [module name | script path] [module or script parameters]"


class AppDelegate (NSObject):
    def init(self):
        self = objc.super(AppDelegate, self).init()
        if self is None:
            return None
        return self

    def runjava_(self, arg):
        ij = imagej.init('/Applications/Fiji.app', headless=False)
        ij.ui().showUI("swing")

    def applicationDidFinishLaunching_(self, aNotification):
        self.performSelectorInBackground_withObject_("runjava:", 0)


def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    # this is necessary to have keyboard events sent to the UI;
    #   basically this call makes the script act like an OS X application,
    #   with Dock icon and everything
    NSApp.setActivationPolicy_(NSApplicationActivationPolicyRegular)
    AppHelper.runEventLoop()

if __name__ == '__main__' : 
    main()

