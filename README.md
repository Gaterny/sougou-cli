####基于python 的命令行下中英文翻译工具，使用搜狗翻译api
pip 安装
```
$ pip install sougou-cli
```
源码安装
```
$ git clone https://github.com/Gaterny/sougou-cli.git
$ cd sougou-cli
$ pip install -r requirements.txt
$ python setup.py install
```
使用
```
$ sg -h
usage: sg [-h] [-v] [word [word ...]]

the usage of Sougou-Dict command line

positional arguments:
  word           word or phrase you want to translate

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show current version

```
查询单词
```
$ sg beautiful

基本释义:
        >>> beautiful: 美丽的 <<<
```    
查询句子
```
$ sg where there is a will, there is a way!

基本释义:
        >>> where there is a will, there is a way!: 有志者事竟成！ <<<

```
中文翻译
```
$ sg 我不爱吃鸡排饭
基本释义:
        >>> 我不爱吃鸡排饭: I don't like chicken steak <<<

```