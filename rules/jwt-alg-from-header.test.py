def verify_bad(header, signing_input, signature):
    # ruleid: jwt-alg-from-header
    if header["alg"] == "RS256":
        rsa_verify(signing_input, signature)
    elif header["alg"] == "HS256":
        hmac_verify(signing_input, signature)
    else:
        raise ValueError


def verify_bad_get(header, signing_input, signature):
    # ruleid: jwt-alg-from-header
    if header.get("alg") == "RS256":
        rsa_verify(signing_input, signature)
    elif header.get("alg") == "HS256":
        hmac_verify(signing_input, signature)


def verify_ok(header, signing_input, signature):
    # ok: jwt-alg-from-header
    if header.get("alg") != "RS256":
        raise ValueError
    rsa_verify(signing_input, signature)
