from src.checksum import modulo11_checksum


def test_good():
    assert modulo11_checksum("0-8044-2957-X")
    assert modulo11_checksum("080442957X")


def test_bad():
    assert not modulo11_checksum("2-266-11156-3")
    assert not modulo11_checksum("2-266-11156-8")
    assert not modulo11_checksum("2266111568")
