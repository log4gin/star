# STAR

## 介绍

很高兴为大家介绍这门小型编程语言，事实上这并不是我第一次尝试自己纯手动制作编程语言，龙书和虎书这类专业书籍过于复杂，导致我经常半途而废，后来在朋友的推荐下接触了 lisp 实现来一个简易的解释器后端，然后笔者发现 lisp 方言解释器和其他的编程语言解释器后端很像 ，lisp 的 s-expression不就是手写语法树了嘛。然后正式迈入了 star 的制作 …

 star 这是一门非常小的编程语言，为什么我不说他是解释语言呢？如果你看过源码就知道目前是 v1 版本，谁知道 v2 版本会不会有go 或者 rust 实现的指令集或者编译器呢。

star 的语法来源于 go 和 python 当然唯一的数据结构 table 则是借鉴了 lua ，同样 table 也是多文件编程的基础。

总之，这是一门比 lua 还小的语言，希望你玩得开心。

## 语法

### 变量声明和修改

```
_int := 0
_float := 0.1
_string := 'hi' // _string := "hi" 同样适用
_table := table(_int,_float,_string)

_int = 100 //这就是变量修改了
```

### 函数声明

```
def _fuction (arg0,arg1){
	print(arg0,arg1)
	arg0 //默认会返回最后一个值作为返回值
}
```

### 函数调用

```
_function(22,33)
```

### 循环

```
times := 10

while lt (times,100){
	print(times)
	times++
}
```

### 更多

更多的语法使用在 v1/example 里面

## 如何运行

下载 发行版本里面的 star.exe

star.exe -h

## 获取技术支持

合作开发欢迎给我发送邮件 log4gin@outlook.com。

如果有什么问题欢迎 issue 。

如果能够自己 PR ，那么是再好不过了 :)。

