# -*-coding:utf-8-*-
"""
@author:Mark
@file: rsa_decode.py 
@time: 2018/05/25
"""
from base64 import b64decode

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.PublicKey import RSA as rsa
from Crypto.Util import asn1

pub_key_str = u"""
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD
p0KiaMwXijkcqxE1MpcB/tdNNjb7UHu9R7pcH4jn1t71ga6DQ
kg8/I/UVqbOA9kDtObP21VCppiwsJy1eFrTviLRrsuFNgdwJD
4GfbEqxyO5viZWH+YkMDPRGEN6McbFTks8wFpb67oNgpoSIvB
GOFx1rU33iO/Rj22GXS64tnQIDAQAB
"""
priv_key_str = u"""
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAOnQqJozBeKORyrETUylwH+1002NvtQe71HulwfiOfW3vWBroNCSDz8j9RWps4D2QO05s/bVUKmmLCwnLV4WtO+ItGuy4U2B3AkPgZ9sSrHI7m+JlYf5iQwM9EYQ3oxxsVOSzzAWlvrug2CmhIi8EY4XHWtTfeI79GPbYZdLri2dAgMBAAECgYEAzSqmN6CcAl+8fP+BoMc1Mhs3ji7aC0IV1/wXFPjiyQVwrIHku//eVxZTQa4GcBwlfsQKcYZe4G6LBjdebNhZ7MTPS/PjlhdXFoWb1/jiXZC1eB1k2w8z9fiS+kfaaY9eC8iH8QDaq2Z/w01IUEZoSRXjLB+vGMpP11DcS18aRNUCQQD3ru/mWz+Iwi+S0FQh+inULBiC6eLR/CISDPVdK9UIR8DULaLLxX+p/VOOfojGqre5xvtkgzN6ZCRKY0u9O4AXAkEA8aqC1y/27WIr3/HLsJ7XmZOCcqiG58fdvXwRMhqDaKYCBiOLzUd+PrxcqFxD+fCb1XIrvVaNpcKdoFFNvq/8awJAZ6iLNnlR6cZ7apJN47py7x1VVNTV3NQM3kkWF1xU2BZPmX1P+MA7YcVnxucmDx87rUCdzb8rODnZBljwRc41GQJBAIOnZ6ZBbB1AiTR0Lopmzn/M+5jpNK1alfNffqK0DPjaz2l2vfe0RhN5XGUf9qxYJx0uGKQKXhp6npKzGE6U40cCQDfIe3xjBNjLds72D8SBoe0GB5LZeAVISQ5G9yveSl/5uySWQkOpsrb9tQRvsmK4PI2turk7muWNTOQeSj+tleg=
"""


def rsa_long_encrypt(pub_key_str, msg):
    msg = msg.encode('utf-8')
    length = len(msg)
    default_length = 117
    # 公钥加密
    pubobj = PKCS1_v1_5.new(RSA.importKey(b64decode(pub_key_str)))
    # 长度不用分段
    if length < default_length:
        return "".join(pubobj.encrypt(msg))
    # 需要分段
    offset = 0
    res = []
    while length - offset > 0:
        if length - offset > default_length:
            res.append(pubobj.encrypt(msg[offset:offset + default_length]))
        else:
            res.append(pubobj.encrypt(msg[offset:]))
        offset += default_length
    return "".join(res)


def rsa_long_decrypt(priv_key_str, msg):
    # msg = msg.encode('utf-8')
    length = len(msg)
    default_length = 256
    # 私钥解密
    priobj = PKCS1_v1_5.new(RSA.importKey(b64decode(priv_key_str)))
    # 长度不用分段
    if length < default_length:
        return "".join(priobj.decrypt(msg, 'xyz'))
    # 需要分段
    offset = 0
    res = []
    while length - offset > 0:
        if length - offset > default_length:
            res.append(
                priobj.decrypt(msg[offset:offset + default_length], 'xyz'))
        else:
            res.append(priobj.decrypt(msg[offset:], 'xyz'))
        offset += default_length
    return "".join(res)


# 明文
msg = "H134" * 1000

e = rsa_long_encrypt(pub_key_str, msg)
d = rsa_long_decrypt(priv_key_str, e)
print "加密后是：%s ;   解密后是：%s  " % (e, d)
