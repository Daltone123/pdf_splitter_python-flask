import qrcode
import qrcode.image.svg

koy = qrcode.image.svg.SvgPathImage

svg_img = qrcode.make('https://koy.network/', image_factory=koy)
svg_img.save('KOY1.svg')