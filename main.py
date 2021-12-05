import qrcode
import matplotlib

imagem_qrcode = qrcode.make("https://www.youtube.com/watch?v=AQwQODq9SWE")
imagem_qrcode.save("nova.png")
