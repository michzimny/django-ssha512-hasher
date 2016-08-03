from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_noop as _
from django.contrib.auth.hashers import BasePasswordHasher
import base64
import hashlib


class SSHA512PasswordHasher(BasePasswordHasher):
    algorithm = "ssha512"

    def salt(self):
        return get_random_string(8)

    def encode(self, password, salt):
        salt = str(salt)
        base64_encoded = base64.encodestring(hashlib.sha512(password + salt).digest() + salt).replace('\n', '')
        return 'ssha512${SSHA512}' + base64_encoded

    def verify(self, password, encoded):
        password = str(password)
        encoded = str(encoded)
        algorithm, data = encoded.split('$', 2)
        assert algorithm == self.algorithm
        assert data.startswith('{SSHA512}')
        base64_decoded = base64.decodestring(data[9:])
        assert len(base64_decoded) == 72
        hashed_password_plus_salt = base64_decoded[:64]
        salt = base64_decoded[64:]
        return hashlib.sha512(password + salt).digest() == hashed_password_plus_salt

    def safe_summary(self, encoded):
        algorithm, data = encoded.split('$', 2)
        assert algorithm == self.algorithm
        return OrderedDict([
            (_('algorithm'), algorithm),
        ])

