# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: qinLess
    File: generateREADME.py
    Time: 2022/5/13 11:43
-------------------------------------------------
    Change Activity: 2022/5/13 11:43
-------------------------------------------------
    Desc: 
"""

import requests
from lxml import etree

my_headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

f = open("README.md", "w+", encoding="utf-8")


def add_info():
    info_txt = """
<h1 align="center">Hi 👋, I'm qinless</h1>

<p align="center">
<a href="https://github.com/qinLess" target="_blank">
<img src="https://github-readme-stats.vercel.app/api?username=qinLess&show_icons=true&theme=aura&count_private=true" />
</a></p>
    """
    f.write(info_txt)


def add_other_info():
    info_txt = """
## 精选仓库

<a href="https://github.com/qinLess/frida_api"><img src="https://github-readme-stats.vercel.app/api/pin/?username=qinLess&repo=frida_api&show_owner=true&&theme=aura" /></a>
<a href="https://github.com/qinLess/magical"><img src="https://github-readme-stats.vercel.app/api/pin/?username=qinLess&repo=magical&show_owner=true&&theme=aura" /></a>

## 联系我

<p align="center">
    <a href="mailto:qinless@qinless.com">
      <img alt="Email" src="https://img.shields.io/badge/Email-qinless@qinless.com-blue?style=flat-square&logo=gmail">
    </a>
</p>
    """
    f.write(info_txt)


def add_star_info():
    f.write("\n### 我的系列文章\n")
    txt = """
- [android 逆向](https://www.qinless.com/series/androidnixiang/)

- [js/小程序逆向](https://www.qinless.com/series/js-program/)

- [密码学学习记录](https://www.qinless.com/series/mimaxuexuexijilu/)

- [shield 算法分析](https://www.qinless.com/series/appshield/)

- ...
    """
    f.write(txt)


def add_blog_info():
    f.write("\n### 我的个人博客\n")

    blog_url = 'https://www.qinless.com/'
    r = requests.get(blog_url, headers=my_headers)

    if 200 == r.status_code:
        dom = etree.HTML(r.content)

        a = 0

        for i in dom.xpath('/html/body/div[2]/div/div[2]/div/div[1]/article'):
            title = i.xpath('./div/h2/a/text()')[0]
            link = i.xpath('./div/h2/a/@href')[0]

            if '找工作' in title or '郑重声明' in title:
                continue

            if a == 5:
                break

            f.write(f"- [{title}]({link})\n")

            a += 1
    else:
        f.write("Failed!\n")
    f.write("- ...\n")
    f.write(f"- [查看更多](https://www.qinless.com/)\n")


def main():
    try:

        add_info()
        f.write('\n<table align="center"><tr>\n')
        f.write('<td valign="top" width="100%">\n')
        add_blog_info()
        f.write('\n</td>\n')
        f.write('<td valign="top" width="100%">\n')
        add_star_info()
        f.write('\n</td>\n')
        f.write('</tr></table>\n')
        add_other_info()

    finally:
        f.close()


if __name__ == '__main__':
    main()
