# R64. 已登记 M24 真桥端点的直接半径原函数界

**已证明。** 日期：2026-11-26。此处只收紧 R60 原图在真实 cut 的唯一半径原函数值，
以及已经定义的目标半径 Hermite 修补界；不改原图、目标 $g$ 或 mean1168，
不重跑桥整场证书，不构造 full-H 尾。

## 1. 直接结论

令 $A=a_*(s_c)$ 为 R60 同一字面相位在末段解析延拓后的真实原函数，
$R_c=\operatorname{binary}(.3)$。已完成精确有理多项式积分及 Taylor 余项外包：

$$
2.2575781682669222\cdot10^{-17}
\le A-R_c\le
2.2575781682669225\cdot10^{-17}.
$$

原函数的精确有理包围宽度小于
$1.1149388319468693\cdot10^{-42}$；上面显示的十进制端点另经 binary64
向外取整，故显示区间较宽。特别地，$A-R_c$ 为正，不能把它直接改成零。

对已指定的真实尾 cut $w=\operatorname{binary}(.08)$、
$w_R=-7w/R_c$、$E=1+w^2$，目标弧长半径两阶为

$$
\widehat a_s=-E^{-1/2},\qquad
\widehat a_{ss}=-ww_R/E^2.
$$

在同一末端，目标减实际的差满足：

| 阶数 | 向外下界 | 向外上界 |
| --- | ---: | ---: |
| 0 | $-2.2575781682669225\cdot10^{-17}$ | $-2.2575781682669222\cdot10^{-17}$ |
| 1 | $-3.8393935033519557\cdot10^{-17}$ | $-3.839393503351955\cdot10^{-17}$ |
| 2 | $-2.307938832091436\cdot10^{-15}$ | $-2.3079388320914355\cdot10^{-15}$ |

因此原已定义、末端长度 $1/1000$ 的同一个目标半径 Hermite 修补满足

$$
\bigl(\|\widehat a-a_*\|_\infty,\,
\|\widehat a_s-a_{*,s}\|_\infty,\,
\|\widehat a_{ss}-a_{*,ss}\|_\infty\bigr)
\le
(2.259125465362424\cdot10^{-17},\,
1.1295627326812119\cdot10^{-13},\,
4.5198097675145096\cdot10^{-10}).
$$

R60 的同一实际图转移到这个已经登记的目标 $g$ 后，
全桥连续相对度量上界收紧为

$$
9.300000001511123\cdot10^{-7}.
$$

这是旧上界的收紧，不是新场、重新冻结的目标或 fixed-$g$ 收敛结论。
该半径误差已经远低于目前度量预算，后续应处理真实 full-H 与 Cartesian
接缝，不再追加这项精度。

## 2. 输入和唯一原函数的定义

输入是已入库小记录
[2026-11-20-short-bridge-gl64-jet-execution.json](../notes/2026-11-20-short-bridge-gl64-jet-execution.json)，
SHA-256 为
`3e2c62be58d9f5dfaa2f19b26e2745f2e424c9115b350e9a33785e44e4c214d2`。
它绑定原 M24 run
`c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a`。
以下每个小数均按对应 binary64 常数精确解释：

| 量 | 字面值 |
| --- | --- |
| $p$ | 1.5069323382251065 |
| $\epsilon$ | 0.015965997142447508 |
| $L_1$ | 0.565099626834415 |
| $L_2$ | 0.34832173342948536 |
| $L_3$ | 0.017270909669753535 |
| $s_b$ | 0.49457743382696573 |
| $s_c$ | 1.4252697037606197 |

精确跨度为

$$
s_c-s_b=\frac{4191465360069805}{4503599627370496}.
$$

定义 $u=(s_c-s_b-L_1-L_2)/L_3$。它略大于 $1$，
脚本使用解析末段而非 upper clipping。按 R60 原函数定义，

$$
A=1-L_1\int_0^1\sin[p(3t^2-2t^3)]\,dt
-L_2\sin p
-L_3\int_0^u\sin(p-\epsilon t^2)\,dt.
$$

第一段相位位于 $[0,p]$，末段相位位于 $[p-\epsilon u^2,p]\subset[0,p]$。
以 40 阶 Taylor 多项式代入并精确积分。由于正弦第 40 阶系数为零，
多项式最高非零次为 39，但 Lagrange 余项仍为
$p^{41}/41!$。原函数总误差半径不超过

$$
(L_1+L_2+L_3u)\frac{p^{41}}{41!}
=(s_c-s_b)\frac{p^{41}}{41!}.
$$

端点导数直接使用同一解析相位
$\phi_c=p-\epsilon u^2$：

$$
a_{*,s}=-\sin\phi_c,\qquad
a_{*,ss}=\frac{2\epsilon u}{L_3}\cos\phi_c.
$$

这两项也以有理 Taylor 余项外包；$\sqrt E$ 通过整数平方根得到严格有理上下界。
没有调用非验证的 libm 求积，也未读取旧场数组。

## 3. 已定义修补和同一目标度量的转移

令 $d_j=\widehat a^{(j)}(s_c)-a_*^{(j)}(s_c)$、$\ell=1/1000$、
$v=(s_c-s)/\ell$。原修补是

$$
e(s)=\sum_{j=0}^2(-\ell)^j d_jH_j(v),
$$

$$
\begin{aligned}
H_0(v)&=1-10v^3+15v^4-6v^5,\\
H_1(v)&=v-6v^3+8v^4-3v^5,\\
H_2(v)&=\tfrac12v^2-\tfrac32v^3+\tfrac32v^4-\tfrac12v^5.
\end{aligned}
$$

每个基函数在 $v=0$ 给出指定的单一 0/1/2 阶 jet，在 $v=1$ 的三阶以下
jet 全为零。脚本以精确有理 Bernstein 系数给出每个导数的上界，
再乘以这次收紧的 $|d_j|$ 界。未选择 $A$ 的区间中点，未改变 $d_j$ 所定义的真修补。

R60 已付 $a_*>.299$。若 $e_0\ge\|e\|_\infty$，
则 $\widehat a>.299-e_0$，置 $\eta=e_0/(.299-e_0)$。
两个目标正交框架之间的径向缩放为 $1$，角向缩放为 $a_*/\widehat a$，
故原相对度量上界 $\varepsilon=9.3\cdot10^{-7}$ 转移为

$$
(1+\eta)^2\varepsilon+2\eta+\eta^2.
$$

脚本只重新组合这个标量界；原桥非均值/均值、曲率、支撑、前缀、
深帽和 cell 7 证书均未重跑。

## 4. 重建及执行绑定

首次源码及临时大输出随环境重置丢失，故按已保留推导重建源文件，
并实际复现一次最终版本以绑定新源 SHA；没有把旧源哈希充当新源码哈希。
源码：
[seam_bridge_endpoint_primitive.py](../scripts/resume_20261126/seam_bridge_endpoint_primitive.py)。
小执行记录：
[2026-11-26-seam-direct-cut-primitive-execution.json](../notes/2026-11-26-seam-direct-cut-primitive-execution.json)。

~~~bash
python topics/visible-flex-held-10pct/scripts/resume_20261126/seam_bridge_endpoint_primitive.py \
  --record topics/visible-flex-held-10pct/notes/2026-11-20-short-bridge-gl64-jet-execution.json \
  --out /tmp/held10-seam-rebuilt/recorded-m24-cut-primitive-rebuilt.json
~~~

最终源 SHA-256 为
`ac9c07f3022f3b271a873acad100dc779f421d44fe1397ccd75612597ac8b7a1`；
实际 exit 0，约 0.067 秒。完整有理输出 60076 bytes，
SHA-256 为
`fc8537759a415980b92935d6dbf79608376f27e18f1947e3c74ea5cb4a80a1c5`。
可重生成的大有理输出只留 scratch；仓库仅保存源、结论和小绑定记录。
没有新增非线性求解、core evaluation、尾连接或 full-H 完成声称。
