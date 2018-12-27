import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
searchd = {'type':'content','q':'python'}
response = requests.get("http://www.zhihu.com/search",params = searchd,headers = headers)
print(response.text)