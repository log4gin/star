# STAR

## 介绍

很高兴为大家介绍这门小型编程语言，事实上这并不是我第一次尝试自己纯手动制作编程语
言，龙书和虎书这类专业书籍过于复杂，导致我经常半途而废，后来在朋友的推荐下接触了
lisp 实现来一个简易的解释器后端，然后笔者发现 lisp 方言解释器和其他的编程语言解
释器后端很像 ，lisp 的 s-expression 不就是手写语法树了嘛。然后正式迈入了 star 的
制作 …

star 这是一门非常小的编程语言，为什么我不说他是解释语言呢？如果你看过源码就知道
目前是 v1 版本，谁知道 v2 版本会不会有 go 或者 rust 实现的指令集或者编译器呢。

star 的速度不会比宿主语言更快这是上限，但是会更灵活。

star 是语言无关的编程语言,源码极其短小,你可以使用任何一门你熟悉的编程语言,用几天
的时间实现你自己的编程语言。

star 的语法来源于 go 和 python 当然唯一的数据结构 table 则是借鉴了 lua ，同样
table 也是多文件编程的基础。

总之，这是一门比 lua 还小的语言，源码加上测试代码目前在 1,000 行左右，希望你玩得
开心。

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

### 函数重载

```
def eq(a,b) {
    'reload success'
}

print(( 1 == 100 ))

```

### 循环

```
times := 10

while (times < 100){
	print(times)
	times++
}
```

### 条件

```
if true {
	print('star is not lua')
}
```

### table

```
// 这是唯一的数据结构
// 可以实现 数组 字典 包
t := table(0,1,2,3,4,5,6,7)
t.name = 'star'
print(t.name)
```

### import file

```
// 导入一个文件

order := load('./stdlib/order.star')

// 使用里面的选择排序函数

choose := order.choose

print(choose(table(33,22,44,123,321,2024)))

```

### 特性

```
// 表达式必须添加一个 ()
// 以及没有优先级
// 所有的表达式最后都会被转化为函数
// 比如
a := ( 100 + 2 * 3 + 1)
// 结果是
a := 108

```

### 更多

更多的语法使用在 v1/\_example 里面

## 如何运行

下载 发行版本里面的 star.exe

### 查看帮助

```bash
star.exe -h
```

### 直接运行 star 文件

```bash
star file_path.star
```

### 编译为语法树

```bash
star -c file_path.star
```

### 运行语法树

```bash
star -v file_path.json
```

## 用途

你可以使用自己编程语言刷 leetcode ，自己 diy 自己喜欢的语法

你可以把它作为其他编程语言的缺陷的弥补，比如 golang 的错误处理不怎么样，你完全可
以把错误传给 star 处理完全后给你结果。

你甚至可以使用 star 开发插件系统，这也是我学习 lua 的原因，但是 lua 里面有太多和
其他语言不同的地方了，这也是 star 诞生的原因。

## 获取技术支持

我的联系方式是

```bash
echo dC5tZS9sb2c0Z2luIA0K | python -m base64 -d
```

如果有什么问题欢迎 issue 。

如果能够自己 PR ，那是再好不过 :)。
