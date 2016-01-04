# -*- coding: UTF-8 -*-

import qrcode

def QRCodeMake(targetString,storePath,name='qrcode.png'):

        qr = qrcode.QRCode(
                           version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=10,
                           border=4,
                           )
        qr.add_data(targetString)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(name)
        return True

