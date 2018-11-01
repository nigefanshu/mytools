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
    print(
        "目标值十六进制:%s 现在%d位数 左侧省略%d个0 " % (currenttarget_hex, len(currenttarget_hex) - 2, 66 - len(currenttarget_hex)))
    print("难度值：%.20f" % (maxcurrenttargettarget / currenttarget))


def testblockheader():
    blockheader = input("blockheader: ")
    blockheader = int(blockheader, 16)
    print("难度值: ", 0x00000000FFFF0000000000000000000000000000000000000000000000000000 / blockheader)


def expected_time_block():
    diff = input("难度：")
    power = input("算力(MH/s)：")
    time = 10 * int(diff) * 7.185 / int(power)
    print(time, "mins")
