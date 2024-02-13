import qrcode

img = qrcode.make('https://zeydan.net')
img.save('SimpleURL.png')