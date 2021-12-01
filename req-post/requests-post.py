"""
post方法
    某些网站需要提交表单信息才会返回数据的请求
    例如，登录、注册

"""
import requests

# 请求的地址
url = "https://passport.17k.com/ck/user/login"
# 请求头
hd = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"
}

# 表单的数据
data = {
    "loginName":"13168837959",
    "password":"a343105980"
}


res = requests.post(url, headers=hd,  data=data)
# print(res)
# 响应头
set_cookie = res.headers['Set-Cookie']
split_res_list = set_cookie.split(';')  # 根据set_cookie里的token值，进行提取
cookie = ''
for i in split_res_list:
    if 'accessToken' in i:
        cookie = i.split(',')[-1].strip()
print(cookie)


# 书架的接口链接
books_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
# 请求头中，添加cookie身份令牌
hd2 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29",
    "cookie":cookie
}
res_books = requests.get(books_url, headers=hd2)
# 处理编码
res_books.encoding = 'utf-8'
print( res_books.status_code)
books_data = res_books.json()
data_list = books_data['data']
for i in data_list:
    bookName = i['bookName']
    print(bookName)