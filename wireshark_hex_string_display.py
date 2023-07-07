from urllib.parse import unquote


def hex2visible_str(hex_str):
    """将16进制字符串转化为可视化字符串"""
    hex_list = []
    ret_hex = ''
    while len(hex_str):
        hex_list.append(hex_str[0:2])
        hex_str = hex_str[2:]
    for i in hex_list:
        if ('a' in i[1] or 'b' in i[1] or 'c' in i[1] or 'd' in i[1] or 'e' in i[1] or 'f' in i[1]) and\
                i[0] not in 'abcdef':
            if i[0].isdigit():
                if 2 <= int(i[0]) <= 7:
                    if int(i[0]) == 7 and i[1] == 'f':
                        ret_hex += '.'
                    else:
                        ret_hex += unquote('%'+i)
                else:
                    ret_hex += '.'
            else:
                ret_hex += '.'
        else:
            if i[0].isdigit():
                if 0x20 <= int(int(i[0])*16+int(i[1])) <= 0x7e:
                    # print(unquote('%'+i))
                    ret_hex += unquote('%'+i)
                else:
                    ret_hex += '.'
            else:
                ret_hex += '.'
    return ret_hex


if __name__ == '__main__':
    hex_string = "504f5354202f6d6d746c732f303030303465653020485454502f312e310d0a4163636570743a202a2f2a0d0a43616368652d436f6e74726f6c3a206e6f2d63616368650d0a436f6e6e656374696f6e3a20636c6f73650d0a436f6e74656e742d4c656e6774683a203436390d0a436f6e74656e742d547970653a206170706c69636174696f6e2f6f637465742d73747265616d0d0a486f73743a2065787473686f72742e77656978696e2e71712e636f6d0d0a557067726164653a206d6d746c730d0a557365722d4167656e743a204d6963726f4d657373656e67657220436c69656e740d0a582d4f6e6c696e652d486f73743a2065787473686f72742e77656978696e2e71712e636f6d0d0a0d0a19f10400a10000009d0104f10100a8111084f1b70d588d9ae34d7e79b2c0d2997f78b8364be5b8e2f08ae5156ece896256f4490000006f010000006a000f01000000630100093a80000000000048000cca765c99e511090ecec8597f0048d670bf4e217402bdf6a3636ad8caef0e5ba0a966c9f8fae13ee25a6ca68f0fed1f3eaa989d34b850af6d69f209d44f97a1149c0cb07d9d10328049505c0371909e844b36034519b219f10400243658566d4c28660b719792835c27368edc7dad468f84e9e194f987a4f4ab2dc54eed5cd417f10400e592d0f27f2dc12ac89be062d79a4c2c23069064c5158959dc20a50dc440394148dd7fcd0e130a746e9b7b621e36cc2d1bbfbb501f9d5469d3130f326671adbed395e49f67c443bb69cfc1b1e6d8bb1abd49d63c1f9abfb925834d4daaf49142f6c1789fe2605ba05099c3c400ee9926952c4f8d5c5e3e71da4efc2bf0bc5c0df09fe6700e2adad11c95685e7364821ce2a507e3e29bfa2b5d764428604f65e16afdd6f54f5fa4afb434f2ba98e719c9d4a7cf17bc26b1c5c8226a6474a1712d648bd5301cc3f4304d00aeededc4e09640b73a982d49ce79971b19de26bd80f6cb832edc91fc15f1040017b6a1de6b2513db2403d9bb5ea89fc2616fb14178eb4733"
    print(hex2visible_str(hex_string))