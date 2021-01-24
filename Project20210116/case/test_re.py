import requests
import re
r = requests.session()
url = "http://news.baidu.com/"
reposon_text = r.get(url)
# r.headers.update(token)
aa = re.findall('d="tip-float" class="(.+?)"',reposon_text.text)
# bb = re.findall('meta http-equiv=Content-Type (.+?)="') # content
print(aa[0])

print(reposon_text.text)


if "mod-headline-tip" in reposon_text.text:
    print("测试通过")
else:
    print("测试失败")
