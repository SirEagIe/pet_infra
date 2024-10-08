from flask import Flask, render_template, request, abort
from PIL import Image
import psycopg2
import datetime
import random
import os


app = Flask(__name__)


@app.route('/js')
def js():
    return render_template('js.html')


@app.route('/kek')
def hello_world():
    return '<h1>ZaLuPa KoNyA</h1><img src="https://cdn-st1.rtr-vesti.ru/vh/pictures/xw/217/453/4.jpg">'


@app.route('/ivleeva_weight')
def ivleeva_weight():
    return f'<h4>Вес Ивлеевой на {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: {random.randint(30, 100)}кг</h4><br><span>(страница создана по просьбе Влада)</span>'


@app.route('/ascii', methods=['GET', 'POST'])
def ascii_art():
    if request.method == 'GET':
        return '''
        <FORM method="post" enctype="multipart/form-data">
                <input type="file" value="image" name="image"/>
                <input type="text" value="1" name="scale"/>
                <input type="submit" value="Submit"/>
        </FORM>
        '''
    if request.method == 'POST':
        image = request.files['image']
        scale = int(request.form.get('scale'))
        #grad = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
        grad = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,"^`\'.'
        img=Image.open(image.stream)
        pixelData = img.load()
        r = ''
        for i in range(0, img.size[1], scale):
            for j in range(0, img.size[0], scale):
                g=(pixelData[j,i][0]+pixelData[j,i][1]+pixelData[j,i][2])//3
                r += grad[g*(len(grad)-1)//255]
                r += grad[g*(len(grad)-1)//255]
            r += '<br>'
        return f'<div style="color:#FFF;font-family: Consolas;">{r}</div><style>body {"{background-color:#000;}"}</style>'


@app.route('/ascii_2', methods=['GET', 'POST'])
def ascii_art_2():
    if request.method == 'GET':
        return '''
        <FORM method="post" enctype="multipart/form-data">
                <input type="file" value="image" name="image"/>
                <input type="text" value="1" name="scale"/>
                <input type="text" value="0.5" name="thres"/>
                <input type="checkbox" value="1" name="inverse"/>
                <input type="submit" value="Submit"/>
        </FORM>
        '''
    if request.method == 'POST':
        d = {'00000000': ' ','10000000': '⠁','00100000': '⠂','10100000': '⠃','00001000': '⠄','10001000': '⠅','00101000': '⠆','10101000': '⠇','01000000': '⠈','11000000': '⠉','01100000': '⠊','11100000': '⠋','01001000': '⠌','11001000': '⠍','01101000': '⠎','11101000': '⠏','00010000': '⠐','10010000': '⠑','00110000': '⠒','10110000': '⠓','00011000': '⠔','10011000': '⠕','00111000': '⠖','10111000': '⠗','01010000': '⠘','11010000': '⠙','01110000': '⠚','11110000': '⠛','01011000': '⠜','11011000': '⠝','01111000': '⠞','11111000': '⠟','00000100': '⠠','10000100': '⠡','00100100': '⠢','10100100': '⠣','00001100': '⠤','10001100': '⠥','00101100': '⠦','10101100': '⠧','01000100': '⠨','11000100': '⠩','01100100': '⠪','11100100': '⠫','01001100': '⠬','11001100': '⠭','01101100': '⠮','11101100': '⠯','00010100': '⠰','10010100': '⠱','00110100': '⠲','10110100': '⠳','00011100': '⠴','10011100': '⠵','00111100': '⠶','10111100': '⠷','01010100': '⠸','11010100': '⠹','01110100': '⠺','11110100': '⠻','01011100': '⠼','11011100': '⠽','01111100': '⠾','11111100': '⠿','00000010': '⡀','10000010': '⡁','00100010': '⡂','10100010': '⡃','00001010': '⡄','10001010': '⡅','00101010': '⡆','10101010': '⡇','01000010': '⡈','11000010': '⡉','01100010': '⡊','11100010': '⡋','01001010': '⡌','11001010': '⡍','01101010': '⡎','11101010': '⡏','00010010': '⡐','10010010': '⡑','00110010': '⡒','10110010': '⡓','00011010': '⡔','10011010': '⡕','00111010': '⡖','10111010': '⡗','01010010': '⡘','11010010': '⡙','01110010': '⡚','11110010': '⡛','01011010': '⡜','11011010': '⡝','01111010': '⡞','11111010': '⡟','00000110': '⡠','10000110': '⡡','00100110': '⡢','10100110': '⡣','00001110': '⡤','10001110': '⡥','00101110': '⡦','10101110': '⡧','01000110': '⡨','11000110': '⡩','01100110': '⡪','11100110': '⡫','01001110': '⡬','11001110': '⡭','01101110': '⡮','11101110': '⡯','00010110': '⡰','10010110': '⡱','00110110': '⡲','10110110': '⡳','00011110': '⡴','10011110': '⡵','00111110': '⡶','10111110': '⡷','01010110': '⡸','11010110': '⡹','01110110': '⡺','11110110': '⡻','01011110': '⡼','11011110': '⡽','01111110': '⡾','11111110': '⡿','00000001': '⢀','10000001': '⢁','00100001': '⢂','10100001': '⢃','00001001': '⢄','10001001': '⢅','00101001': '⢆','10101001': '⢇','01000001': '⢈','11000001': '⢉','01100001': '⢊','11100001': '⢋','01001001': '⢌','11001001': '⢍','01101001': '⢎','11101001': '⢏','00010001': '⢐','10010001': '⢑','00110001': '⢒','10110001': '⢓','00011001': '⢔','10011001': '⢕','00111001': '⢖','10111001': '⢗','01010001': '⢘','11010001': '⢙','01110001': '⢚','11110001': '⢛','01011001': '⢜','11011001': '⢝','01111001': '⢞','11111001': '⢟','00000101': '⢠','10000101': '⢡','00100101': '⢢','10100101': '⢣','00001101': '⢤','10001101': '⢥','00101101': '⢦','10101101': '⢧','01000101': '⢨','11000101': '⢩','01100101': '⢪','11100101': '⢫','01001101': '⢬','11001101': '⢭','01101101': '⢮','11101101': '⢯','00010101': '⢰','10010101': '⢱','00110101': '⢲','10110101': '⢳','00011101': '⢴','10011101': '⢵','00111101': '⢶','10111101': '⢷','01010101': '⢸','11010101': '⢹','01110101': '⢺','11110101': '⢻','01011101': '⢼','11011101': '⢽','01111101': '⢾','11111101': '⢿','00000011': '⣀','10000011': '⣁','00100011': '⣂','10100011': '⣃','00001011': '⣄','10001011': '⣅','00101011': '⣆','10101011': '⣇','01000011': '⣈','11000011': '⣉','01100011': '⣊','11100011': '⣋','01001011': '⣌','11001011': '⣍','01101011': '⣎','11101011': '⣏','00010011': '⣐','10010011': '⣑','00110011': '⣒','10110011': '⣓','00011011': '⣔','10011011': '⣕','00111011': '⣖','10111011': '⣗','01010011': '⣘','11010011': '⣙','01110011': '⣚','11110011': '⣛','01011011': '⣜','11011011': '⣝','01111011': '⣞','11111011': '⣟','00000111': '⣠','10000111': '⣡','00100111': '⣢','10100111': '⣣','00001111': '⣤','10001111': '⣥','00101111': '⣦','10101111': '⣧','01000111': '⣨','11000111': '⣩','01100111': '⣪','11100111': '⣫','01001111': '⣬','11001111': '⣭','01101111': '⣮','11101111': '⣯','00010111': '⣰','10010111': '⣱','00110111': '⣲','10110111': '⣳','00011111': '⣴','10011111': '⣵','00111111': '⣶','10111111': '⣷','01010111': '⣸','11010111': '⣹','01110111': '⣺','11110111': '⣻','01011111': '⣼','11011111': '⣽','01111111': '⣾','11111111': '⣿'}
        image = request.files['image']
        scale = float(request.form.get('scale'))
        thres = float(request.form.get('thres'))
        inv = 1 if bool(request.form.get('inverse')) else -1
        img=Image.open(image.stream)
        img = img.resize((int(img.size[0] * scale), int(img.size[1] * scale)))
        pixelData = img.load()
        print(thres)
        r = ''

        for y in range(0, img.size[1] // 4 * 4, 4):
            for x in range(0, img.size[0] // 2 * 2, 2):
                p = ''
                pxl = pixelData[x, y]
                p += '1' if inv * (pxl[0] + pxl[1] + pxl[2]) // 3 > inv * 255 * thres else '0'
                pxl = pixelData[x + 1, y]
                p += '1' if inv * (pxl[0] + pxl[1] + pxl[2]) // 3 > inv * 255 * thres else '0'
                pxl = pixelData[x, y + 1]
                p += '1' if inv * (pxl[0] + pxl[1] + pxl[2]) // 3 > inv * 255 * thres else '0'
                pxl = pixelData[x + 1, y + 1]
                p += '1' if inv * (pxl[0] + pxl[1] + pxl[2]) // 3 > inv * 255 * thres else '0'
                pxl = pixelData[x, y + 2]
                p += '1' if inv * (pxl[0] + pxl[1] + pxl[2]) // 3 > inv * 255 * thres else '0'
                pxl = pixelData[x + 1, y + 2]
                p += '1' if inv * (pxl[0] + pxl[1] + pxl[2]) // 3 > inv * 255 * thres else '0'
                pxl = pixelData[x, y + 3]
                p += '1' if inv * (pxl[0] + pxl[1] + pxl[2]) // 3 > inv * 255 * thres else '0'
                pxl = pixelData[x + 1, y + 3]
                p += '1' if inv * (pxl[0] + pxl[1] + pxl[2]) // 3 > inv * 255 * thres else '0'
                r += d[p]
            r += '<br>'
        return f'<div style="white-space: pre;color:#FFF;font-family: Consolas;">{r}</div><style>body {"{background-color:#000;}"}</style>'


@app.route('/')
def test_db():
    try:
        page = request.args.get('page', default=1, type=int)
        conn = psycopg2.connect(dbname=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'], host='pg_db', port=os.environ['POSTGRES_PORT'])
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM articles ORDER BY pubdate DESC LIMIT 100 OFFSET {(page - 1) * 100}")
        articles = cur.fetchall()
        return render_template('index.html', articles=articles, page=page, request=request)
    except:
        return render_template('index.html', articles=[], page=1, request=request)


if __name__ == '__main__':
    app.run('0.0.0.0')
