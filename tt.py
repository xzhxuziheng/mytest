# 生成指定大小文件
def gen_file(path, size):
    file = open(path, 'w')
    file.seek(1024*1024*size)
    file.write('\x00')
    file.close()


if __name__ == '__main__':
    gen_file('./test.bmp', 2.99)
