import requests
import json
import base64
import sys
url = 'https://rtic.com.br'
ua = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print('Uso:  ' + sys.argv[0] + ' image\n')
    print('Ex:   ' + sys.argv[0] + ' /home/user/a.png')
    exit(0)

imagePath = sys.argv[1]
    
sess = requests.session()
sess.headers.update(ua)
# pegando tokens
token = sess.request('GET', url)

# pegando sala vazia
salas = json.loads(sess.request('GET', url + '/lista_sala.php?x=1&l=1').text)
salas_zero = list(filter(lambda x: x['q'] == 0, salas[0]['o']))
sala_id = str(salas_zero[int(len(salas_zero)/2)]['i'])

# entrando na sala
sess.request('POST', url + '/autenticar.php', data={
    'login': 'upper',
    'sala': sala_id,
    'idioma': 1,
    'acesso': 1
})
print('entrou aqui ' + url+'/0' + sala_id)

# upload da imagem
imgData = open(imagePath, 'rb')
imgData = base64.encodebytes(imgData.read())
i = sess.request('POST', url + '/room/salvar_img.php', data={
    'n': 1,
    'seq': 1,
    'palavra': 1,
    'dados': ',' + imgData.decode()
})
try:
    path = i.text[i.text.find('..')+2:]
    print(url + path)
except Exception:
    print('error: ' + i.text)
