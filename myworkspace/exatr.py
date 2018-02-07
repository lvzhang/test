# f = open('xiaoxiao.txt','a',encoding='utf-8')
# print(type(f))
# f.write('我喜欢你你喜欢我吗')
# f.write('\n')
# f.write('你还想我吗')
# f.write('\n')
# f.write('我已经忘记了你')
# f.write('\n')
# print('我在执行一次')

# f = open('xiaoxiao.txt','r',encoding='utf-8')
# # content = f.read()
# # print(content)
#
# text = f.read(1024)
# print(text)
# f.close()

# f = open('xiaoxiao.txt','r',encoding='utf-8')
# content = f.readlines()#读完 放入list里面
#
# print(content)
#
# # text = f.read(1024)
# # print(text)
# f.close()
# f   = open('xiaoxiao.txt','r',encoding='utf-8' )
# for line in f:
#     print(line[2])

# with open('xiaoxiao.txt','r',encoding='utf-8') as  f:
#     content = f.readlines();
#     i= 0
#     print(content[2])
#     for line in content:
#         i = i+1
#         print(i,line)

def make():
    print(2222)

    make()
