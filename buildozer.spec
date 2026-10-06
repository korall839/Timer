[app]
title = Timer
package.name = timer
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,VIBRAT

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 26b

# (bool) Use davax instead of dx
android.skip_apk_rescale = False

[buildozer]
log_level = 2
warn_on_root = 1

# Фиксируем стабильную ветку сборщика, чтобы избежать FileNotFoundError
p4a.branch = master
