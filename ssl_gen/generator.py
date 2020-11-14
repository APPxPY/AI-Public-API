from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from os.path import exists, join

from env import *

class SSLGenerator:
    
    @classmethod
    def generate_cert(cls):
        if not exists(join(CERT_DIR, CERT_FILE)) or not exists(join(CERT_DIR, KEY_FILE)):
            
            k = crypto.PKey()
            k.generate_key(crypto.TYPE_RSA, 1024)

            cert = crypto.X509()
            cert.get_subject().C = COUNTRY
            cert.get_subject().ST = STATE
            cert.get_subject().L = CITY
            cert.get_subject().O = ORGANIZATION_NAME
            cert.get_subject().OU = ORGANIZATION_UNIT_NAME
            cert.get_subject().CN = HOST
            cert.set_serial_number(1000)
            cert.gmtime_adj_notBefore(0)
            cert.gmtime_adj_notAfter(10*365*24*60*60)
            cert.set_issuer(cert.get_subject())
            cert.set_pubkey(k)
            cert.sign(k, 'sha256')
            open(join(CERT_DIR, CERT_FILE), "wb").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
            open(join(CERT_DIR, KEY_FILE), "wb").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

        return True