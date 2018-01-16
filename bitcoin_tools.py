# 输入难度位计算出目标值、难度值
def compute_target_diff():
    # 难度值为1的目标值：
    maxcurrenttargettarget = 0x00000000FFFF0000000000000000000000000000000000000000000000000000

    nbits = input("输入难度位：")
    nbits = int(nbits, 16)
    print("难度位十进制：", nbits)
    power = (nbits // (16 ** 6) - 3) * 8
    base = nbits % (16 ** 6)
    currenttarget = base * (2 ** power)
    print("目标值十进制:", currenttarget)
    currenttarget_hex = hex(currenttarget)
    print("目标值十六进制:%s  左侧省略%d个0 " % (currenttarget_hex, 64 - len(currenttarget_hex)))
    print("难度值：", maxcurrenttargettarget / currenttarget)
    exit(0)
