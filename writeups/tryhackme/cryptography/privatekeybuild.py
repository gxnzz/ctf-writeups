from Crypto.PublicKey import RSA

p = int(input(Enter P:))
q = int(input(Enter Q:))
e = 65537 #standard RSA exponent

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

key = RSA.construct((n, e, d, p, q))
print(key.export_key().decode())
