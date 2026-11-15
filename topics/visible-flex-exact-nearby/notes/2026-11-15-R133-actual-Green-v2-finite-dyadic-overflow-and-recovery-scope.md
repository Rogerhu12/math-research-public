# R133：Green v2 的真实有限数到 binary64 溢出与恢复范围

2026-11-15，visible-exact-astra-0df9。

**实际失败已定位，不是成功证书。**
[公开 run43681612825/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43681612825)
的首个完整分组在07:05:03失败，数学子进程 exit1，完整 groups 为0。
原三流 source 为
f33345d1ab2500fd3811692311ce931606e389cf3c8ef508925d225748565190。
本篇只记录原日志、原小过程和源代码能证明的事实，没有新数学求值。

## 1. 真实过程和零数学日志恢复

原 process.json 为39023B，SHA256
0b2e08152feee47b47666e2bc03a1b3e535e2389891e26a0674014d3a2fef4ba，
Git blob bfeeff63769914cc02512ff55d47653cfacecec4。
父进程测得数学 child 墙钟5100.021125664秒；
原科学摘要内部计时5097.398970254秒，两者不是同一个字段。

[零数学日志收据 run43689244062/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43689244062)
实际成功。它仅临时读取原 job132713247491 的完整文本日志，
核原 run/attempt/source/process 身份，发布必要 traceback 和原 bytes/SHA。
未运行矩阵、Gram、target、FFT 或原证书；未上传 data artifact。

| 原件 | 字节 | SHA256 |
| --- | ---: | --- |
| 原失败 job132713247491 日志 | 70333 | 69181f59587aec5db8d0d135f4ede675a7b7610c2b3bfd0470228951981e7750 |
| 零数学 receipt job132736157221 日志 | 41089 | d0242150633f848f3651c755629e2811c74bdb690217978b63989a8a9ee85a30 |
| 原 finally 完整状态计数摘要 | 7499 | 770a61fa89902954178cf1a2bb9a347312232545e434685f9e332a2ce149b8db |

最后一件为同原 process 目录的 actual-conclusion-summary.json，
Git blob f48dca43aee2476220bacbe74cce65e19c2df254。
它的8个身份门通过，完整数学目标各字段仍未得到最终值。
不将原 process 中 null 的计数字段改写成计算成功的0。

## 2. 实际调用链与可严格作出的判断

原 traceback 精确为：

~~~text
fourfold_codazzi_ephemeral_parallel_matrix_Green_Poisson_v2.py:315
    merge_group -> p.weighted_add(..., sym(Hjump*gain**2))
fourfold_codazzi_complete97_right_Poisson_Grams.py:72
    matrix.base.exact_upper_float(size.sqrt().upper())
fourfold_codazzi_same_F_triangular_source_Gram_pilot.py:65
    if not np.isfinite(chosen):
        raise ArithmeticError('nonfinite exact dyadic slack')
~~~

原 Poisson source 为26206B，SHA256
312398be818621e156c08366f74c2850c61dcc283a44a30d7bb510a1cd51fca0；
原 triangular source 为33579B，SHA256
2173281e0558cbbabf3a21d506ae3cf9b0253a9406aa2d9d15b8681e8faeaf44。
两件完整原 source 不改变。

weighted_add 的准确顺序为：取 norm(component).upper()；
zero 时返回；非finite或negative时抛出另一条明确错误；
然后才调用 exact_upper_float。后者取上端，将它转成 Python
float，并在 np.isfinite(chosen) 失败时抛出本次实际消息。

所以这次触发的是已通过有限/非负门的大小在 binary64 转换处溢出。
它不是此前的 Arb nonfinite-norm 分支，也不是 README/formatter/
metadata 发布失败。当前日志没有保存该 component 的数值大小，
不能仅凭 stack 宣称误差放大完全来自哪一个乘积项。

原 chosen_product 将选点误差按
norm(D_i)*error + rounding 累加为 scalar；
原 sandwich 再使用
norm(J)*(2*norm(E)*error+error^2) 的完整 scalar slack。
这给一个值得修复的宽放位置，但 stack 本身没有证明它是唯一原因。
仅让编码接受更大指数，并不证明得到的 Green/Poisson 界有用。

## 3. 真正完整文件计数，不能以刷新进度替代

finally 对全部完整 state 文件逐件计数并核有序收据：

| 临时阶段 | 完整文件数 | 有序实际收据 SHA256 |
| --- | ---: | --- |
| future | 4226 | 2dcc5217c6d3ebad9594f6db6effff61f21a066a19366e2aefbdab986609251f |
| past | 1800 | b6a84164447535498ce4065bbf171e2a34f2954ca5f9889a0c9e64295618ee75 |
| product | 4331 | c94fdfb1461c4469842bf6ee3f52e911f5ad9a7e6e15a0aa616ecba171abeafd |
| canonical ports | 5970 | 29a66ef939c4095a04cb71ec4acd4b3e293647679ba35e6064699fbfa9263a8a |
| complete groups | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

future 中1886件来自原成功前缀，仅逐字恢复；本次新2340件。
旧16格刷新进度的4224/1792/4320是更早检查点，不是最终完整文件数。

这些本次新产物仅留 runner 临时目录，已按现行根规15不保存为
repo/Release/新artifact。故不能在后继 run 中宣称可以恢复这些数组。
用户已经要求没推上去的结果按 HANDOFF 重做；下一 run 如需重新得到
2340个新 future、1800个 past、4331个 product 和5970个新 canonical
port，必须把这些未保存的重复工作明确列在 manifest 和实际报告中。

原已有1886/320bit前缀、完整same-F 5970、7908、source/output Grams、
targets和旧证书则仍只从 immutable 公共历史或原artifact恢复，
不重新计算。修复不改变它们的原 source/runtime/process 身份。

## 4. 修复所须保持的实际合同

后继实现继续保持原完整矩阵、两普通源、两carrier sign、
true97 even mean、原1e−30 inverse gate、signed input/output Grams、
真实 Vcutex 和同一个 C，以及全部原 scalar/height/flux 端口。

允许重新证明 product-error 的方向敏感 Loewner 递推，并用任意指数
的确切二进制表示，避免通过 binary64 丢掉已有限的 Arb 上界。
新的交叉项、选点 rounding、输入/输出 Gram 方位和正权 Young
都须完整支付；不以截断误差项、置零、逐entry最小值或删mean使计算通过。
先在公共 Actions 的真实完整入口作预检查，再跑长三流。

本篇未授任何修复后数值门。完整 groups、三个HY、全部whole合法合成、
全无限反馈及真正参数 Schur 仍是后续实际任务。

日志收据的真pull为07:17:03.651294和07:17:05.353018 UTC，
均至e9a7712fb431397cd172960692c17631f5056325；
根/本课题README的实际diff均为空。
