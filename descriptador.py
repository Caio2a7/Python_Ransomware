import os
import pyaes


def decriptador(diretorio_alvo):
    key = b"testeransomwares"
    for files in os.listdir(diretorio):
        os.chdir(diretorio)
        with open(files, 'rb') as rb:
            dados = rb.read()
            aes = pyaes.AESModeOfOperationCTR(key)
            decriptografar = aes.decrypt(dados)
            novo_arquivo = os.path.basename(files).replace('.ransomwaretroll', '(descriptografado).txt')
        os.remove(files)
        with open(novo_arquivo, 'wb') as wb:
            wb.write(decriptografar)
            wb.close()
            rb.close()



diretorio = 'D:\Python_Estudos\Cibersegurança\Criptografia\Teste Malware'
decriptador(diretorio)
