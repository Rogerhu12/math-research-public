# 原闭点 Tate 全迹实现的独立标量对照成功

日期：2026-11-16。此记录核验 [R883 附录G](../results/R883-original-relative-six-shadow-and-complete-boundary.md)
算法在原两个固定好素数上的实际实现。它没有输入原四个交除子，
所以不声称原 shadow 非零或任何原映射已获证书。

## 成功运行

- [run 43862778281](https://github.com/Rogerhu12/math-research-public/actions/runs/43862778281)，job 133283559262，完整成功。
- source：`84fd72748e36a2cbfd42201c623d0b86eb780303`。
- producer：[check-original-shadow-tate-trace.py](../scripts/check-original-shadow-tate-trace.py)。
- helper：[original_shadow_tate_trace_tools.py](../scripts/original_shadow_tate_trace_tools.py)。
- 同底群及原consumer：[original_shadow_relative_six_tools.py](../scripts/original_shadow_relative_six_tools.py)。
- 完整 RESULT SHA256：`ac1fd52fb71cff75eab47fb500aa6bc553e7766f4642648e92525656fb18e7bc`。
- 全部逐点对照记录 SHA256：`6e2590873e882a5ff01ccde042c069649dd376a49bdf0eba851f152b1ed367b2`。
- 三份源码 SHA256 按上述顺序：
  `06a93873b008d4c7a894e120ced8e43188d5ce162b7033737b55c1f8e9b7e5d5`、
  `46a97715ca2f5da1c884b67b5583a358a5a41d78a4728fb575ee66114ba9d5f9`、
  `98a5f572427f7ed1e7af10a77540ed328f20598a583b99be2ba0d79b8a21adeb`。

使用已固定的 Sage 10.6 镜像
`sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb`，
公开 Actions 中只读挂载、无网运行。数学程序实际用时1.138秒，
不含镜像拉取和启动时间。
根/题 README blob 仍为
`21bd547f56590b7f2dd279d0297efb289a9b2783`、
`965ab236bbd6753acb812b45fcc36ae9b6f83b3c`。

## 核验的实际边界

每个输入 \(P\in E(\mathbf F_{r^{2d}})\) 都由同一真实常数嵌入比较
\[
 \text{两个约化Tate读数恢复的点}
 =\left[\frac{1-(-r)^d}{\ell}\right]P
 =[6]\operatorname{Tr}_dP.
\]
两侧独立执行，比较的是完整椭圆点。没有先把 \(d\) 或未迹点约掉。

| \(r,\ell\) | \(d\) | 与完整标量比较的点数 | 非零全迹数 | 特别覆盖 |
|---|---:|---:|---:|---|
| \(29,5\) | 1 | 25 | 24 | 全部底域5挠点，含 \(O,-U,-2U\) |
| \(29,5\) | 2 | 15 | 13 | 原嵌入上的一般扩域点 |
| \(29,5\) | 5 | 22 | 19 | 两个独立25挠点及其实际组合 |
| \(41,7\) | 1 | 49 | 48 | 全部底域7挠点，含 \(O,-U,-2U\) |
| \(41,7\) | 2 | 15 | 14 | 原嵌入上的一般扩域点 |
| \(41,7\) | 7 | 22 | 19 | 两个独立49挠点及其实际组合 |

此外在 \(d=\ell\) 时，分别把两个原底域基点送入扩域并实际核验全迹为零。
同一度数下真正 \(\ell^2\) 挠点的全迹却非零，因而测试覆盖了
“扩域上底域配对限制退化”与“原完整迹仍非零”的区别。
每个扩域配对都使用完整 \((r^{2d}-1)/\ell\) 指数。

实际底域配对矩阵分别为
\[
 M_{29}=\begin{pmatrix}0&2\\3&0\end{pmatrix}\pmod5,\qquad
 M_{41}=\begin{pmatrix}0&2\\5&0\end{pmatrix}\pmod7.
\]
它们由原基和同一 Miller 规范现场校准；不预设软件的 Weil 方向。
\(U/2U\) 的第二选择在两组运行中均实际使用。
这次核验后不再增加同类可选点测试；原算法的一般性由附录G完整证明，
后续进入真实原除子计算。

## 已修复的实际接口故障

首run43861463682/job133279080828及随后修点数循环的
run43861552312/job133279604099，在进入配对之前同样失败：
`E.points()` 经PARI转换时，有限域变量名
`omega` 与其内置符号冲突。
失败不是一个数学零值或配对不相等。

当前原consumer在两个固定小底域逐个枚举所有 \(x\)，保每个平方根的
正负两点及 \(O\)，再核完整 \((r+1)^2\) 点数和原 \(\ell^2\) 挠点表。
这消除了对PARI变量名的依赖，且成功运行核验的是此同一实现。
生产 consumer 已提供 tate、scalar 和逐贡献闭点 compare 三种模式；
真实双map PASS 门、全部几何交重、剩余次数、Artin读数和两点判据不变。
