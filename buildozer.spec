[app]
# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (list) Permissions
android.permissions = android.permission.INTERNET, android.permission.WRITE_EXTERNAL_STORAGE

# (str) Presplash background color (for android toolchain)
#android.presplash_color = #FFFFFF

# (str) Presplash animation using Lottie format.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (str) Icon of the application (Add your icon file here if available)
icon.filename = %(source.dir)s/data/icon.png
