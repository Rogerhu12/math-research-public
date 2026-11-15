# R232：原八包圆在例外偶端芽上的完整第四 ruling 严格障碍

日期：2026-11-15。本文消费一次已经完成的公开实际，不重复运行任何旧目标。结论限于 R193 冻结八包圆及下述例外 germ；它不是所有三矩圆、所有端芽或一般几何的刚性结论。

来源：[R231 完整 mixed 主层](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、[R229 同锚能量边界式](R229-p2-energy-boundary-identity-for-exceptional-germs.md)、[R227 可实现例外端芽](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)、[R183 重叠八包圆](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)。实际来源是 [run 43699241372](https://github.com/Rogerhu12/math-research-public/actions/runs/43699241372) 的 [energy job 132766507913](https://github.com/Rogerhu12/math-research-public/actions/runs/43699241372/job/132766507913)；源码提交为 ee9e2098c62392ddb709e7db26467bc225642d54。

## 1. 结论与准确端芽

对 R193 的冻结实 profile 圆及共同正归一化后的圆，本次准确计算给

$$
\boxed{L_c<0,\qquad L_s>0.}
\tag{1}
$$

在固定区间 $I=[\ell,r]$ 上取

$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=k_e(1-2\varepsilon\sigma^2),\qquad
\omega=\frac{k_e}{h},
\quad
h_e>0,\quad\varepsilon>0,\quad k_e\ne0,
\tag{2}
$$

并要求物理正支

$$
x>0,\qquad x+\frac{k_e}{h_e}>0\quad(x\in I).
\tag{3}
$$

这是 R227 的 $C=0,b=0$ 例外族。对于同一八包形状的每个正宽度，只要其支撑能在该固定 $I$ 中实现，(1) 就严格排除整个第四 ruling 对所有相位恒零。这个排除保留真实二、三阶传入 histories，并适用于全部允许的二阶、三阶 homogeneous gauge；不是把中心输入设为零后只排除一个特殊恢复。

它并不排除其他 profile 圆，也不覆盖 $b\ne0$ 或任意改动后的 germ。

## 2. 两个实际能量为何构成完整必要门

设 $J$ 是同一个正右积分，定义

$$
E_0(u,v)=\frac14\int_I\bigl(x^2u''v''+2u'v'\bigr)\,dx,
$$

$$
8G_0(u,v)=4xuv-2x^2(uv'+u'v)+2x^3u'v'
+x^2J(x^2u''v''+2u'v').
\tag{4}
$$

令

$$
A_f=G_0(f,f),\qquad A_g=G_0(g,g),\qquad A_{fg}=G_0(f,g).
$$

三矩条件使 $A_g-A_f,A_{fg}$ 紧支撑；$A_f,A_g$ 本身一般带有共同非零 $x^2$ 左尾。本次计算完整保留这些尾。两个目标正是

$$
L_c=E_0(A_f,A_g-A_f),\qquad
L_s=E_0(A_f,A_{fg}).
\tag{5}
$$

R231 的完整 R56 推导已经付清局部恢复、变化 profile 链式项和所有三阶 history。若
$\phi_\theta=\cos\theta f+\sin\theta g$，中心化后的真实 ruling 满足

$$
\frac{\widehat{\mathscr K}_\theta}{h\beta^2}
\longrightarrow
C_\theta=\sin^2\theta\,L_c+\sin(2\theta)\,L_s,
\qquad
\beta=\int_0^\sigma hk\,d\tau
\sim-k_e\sigma h.
\tag{6}
$$

实际 ruling 与该中心式的偶部差只落在

$$
\mathcal W_e
=\operatorname{span}\left\{
h,\ \sigma^2,\
\frac{1+4\varepsilon^2k_e^2\sigma^4}{h}
\right\}.
\tag{7}
$$

(7) 每个函数除以 $h\beta^2$ 均趋零。因此 germ 中的完整 ruling 恒零必迫 $C_\theta=0$ 对所有相位成立，等价于 $L_c=L_s=0$。这是 R231 的解析局部身份检验，不把实际闭路径延长到无限长。

(1) 已违反该必要条件；例如 $\theta=\pi/2$ 就有 $C_\theta=L_c<0$。虽然 R229 的 pure 四次主层准确为零，两个 mixed 能量并不随之消失。

## 3. 原输入、尾项和本次实际的范围

输入使用原冻结 helper，不重新选择包幅或左补矩参数：

$$
\rho(t)=51480t^7(1-t)^7,\qquad
\eta(t)=65536t^8(1-t)^8,\qquad
S(t)=\int_0^t\rho.
$$

$S$ 在两端分别延为 0、1；$\eta$ 零延拓。单包主部分为
$f=S(x-8)-S(x-12)$、
$g=S(x-10)-S(x-14)$。
三个左补丁在 1、3、5，ordinary complex square 系数仍为
$7A/B,-16A/B,9A/B$，其中
$A=\int_0^1(\rho')^2$、$B=\int_0^1(\eta'')^2$。
八包平移为 $20j$，实幅度满足
$\alpha_j^3=(-1)^j\binom7j$，$0\le j\le7$。

新源码只调用这份冻结 profile 构造并计算 (5)，没有重算 R193 的 $c_0,c_2,c_4,c_6$，没有重编 forcing、W 或几何。

每包完整保留 14 个单位区间，包括零输入空隙和非零常平台。公开源码在返回 complete 之前逐包准确检查：

- $A_f,A_g$ 的相同非零左二次尾，以及 $A_{fg}$ 的零左尾；
- 真右锚处三个场的 0、1、2 阶 jet 为零；
- 所有相邻区间三个原场的两阶 jet 匹配。

它没有将 $A_f,A_g$ 假定为紧槽。跨包共同尾只通过 R231(29) 的准确边界身份

$$
E_0(x^2,Z)=0
\quad\text{当 }Z\text{ 在两 collar 上为零}
\tag{8}
$$

消去；同一包内部所有左补丁、主导数段、常平台和间隙之间的尾仍在积分中。

## 4. 严格符号证书与实际状态

job 日志的第 684 行报告 13 项新增人工全部通过；开发阶段没有调用真实冻结 profile 构造，也没有 profile 积分。第 685 行报告实际 complete、two_energies_complete=true，error/reason 均为 null。

第 686 行打印了两个完整准确代数表达式。以固定正根基

$$
(1,\sqrt[3]7,\sqrt[3]{21},\sqrt[3]{35})
\tag{9}
$$

表示时，$L_c$ 的四个有理系数全部严格负，$L_s$ 的四个有理系数全部严格正。因此仅这四槽同号事实就已经证明 (1)，无需浮点容差或一般代数数非零推断。

两个原表达式的 SHA-256 为：

| 表达式 | SHA-256 |
|---|---|
| $L_c$ | 11af7b2ca34775d54d456ffbfdf23fd3212f3c9339caf92b20fbf49b0c2eca69 |
| $L_s$ | f3fd0b4c16e49f3e1868a99063a49ea3f15045235f6b94d149d59e2fad8517bd |

第 687 行还独立给出了严格有理区间，所用立方根区间精度为 16 bits：

$$
-\frac{805193206163366005339583863834011623311691350731}
{17914642656639029248}
\le L_c\le
-\frac{522544375210039313010204037773262368705951139299}
{11626290619461230464}<0,
\tag{10}
$$

$$
0<
\frac{3999547320151031278576497529953975}
{111528035328256}
\le L_s\le
\frac{127988441122201092566337989994484275}
{3568897130504192}.
\tag{11}
$$

这里 16 bits 是区间精度，不是声称执行了 16 次细化。以上值直接来自已完成 stdout，本文未重新计算。

实际计时为 0.2728170979999973 秒，峰值 RSS 为 23.23828125 MiB；开发计时为 0.019330973999998946 秒。新科学步骤与最终 publisher 均 success，没有预算退出、实现失败或代数符号未决。程序的“两能量均零，只支付此领先门”分支本次为 false。

## 5. 全允许宽度与严格 $C^\infty$ 转移

正宽度缩放使用同一全局坐标规则，不另移中心或重选包形。R231 的准确齐次式为

$$
L_c(\lambda)=\lambda L_c(1),\qquad
L_s(\lambda)=\lambda L_s(1).
\tag{12}
$$

共同正归一化只再乘同一个正四次幂。因此 (1) 对所有 $\lambda>0$ 保持；实际几何排除限于支撑 $[\lambda,155\lambda]$ 可置于所选物理正支 $I$ 的宽度，不宣任意预定 $I$ 都可容任意宽度。

本次输入是分段 $C^7$。在固定支撑的足够小 $C^4$ 邻域中，两能量连续且仍具有上述严格符号。按 R183/R193 的有限三矩修复先取一份 $C^\infty$ 单包近似，准确恢复三矩，再使用相同八平移及幅度。修复后的形状仍满足 (1)。随后对这一固定光滑形状应用 (12)，得到同一全允许正宽度结论。这里不主张未证明的普遍 $C^2$ 稳定性，也不借近似代替准确三矩。

## 6. 来源与保存边界

科研 driver：
literature_exceptional_port_two_energy_gate.py，
16867 B，
SHA-256 e1b9f37b8ce5af296a8120bd790f852b813c8aef5c3befee74ec195f643c0745。

冻结 helper：
literature_derivative_packet_full_width_gate.py，
29108 B，
SHA-256 adc5b987861633efcf56c1df5a4de4a076055d64444f05c8302025e654de6795。

[实际 receipt](../notes/actions-43699241372-1-exceptional_port_two_energy_gate/receipt.json) 为 49167 B，
SHA-256 66ecf0b4aef049bbed21de70a0ce0c5e22e650f37b033ff00c605dcf838b8d5c。它绑定：

| 临时输出 | 字节数 | SHA-256 |
|---|---:|---|
| exceptional-port-two-energy-development.json | 3059 | fd9a6f3abe65b008b2beefa223038182d38e58f07d334f74b72135215dc3ff8c |
| exceptional-port-two-energy.json | 9524 | 675a8bc4c0e6770b2becf536079e222e1806b3ff7e883103ed607215cb09c476 |
| pre-research-pull.json | 253 | 7a1e259741e79ad6362aa105c2acbccbb8405c910bb9e48db69ad308c26e7d45 |

日志确认 09:26:38 的真实研究前 git pull，源码仍为 ee9e2098c62392ddb709e7db26467bc225642d54，两份 README 未变。receipt 还记录发布前的真实 pull 与相同源码身份。

依根 README15，只保存源码、参数、run、输出 hash 与本篇人类数学结论；没有保存或重新发布机器报告、证书、Release asset。本文实际结论由已读原 stdout 的准确系数和区间取得，不把 metadata hash 本身当数学证明，也没有补造未打印的机器字段。

本篇支付的是原八包例外端芽的一个严格否定门。其他合法三矩圆可能同时满足两能量为零；即使如此也只消掉 (6) 的主层，完整次层和全部 ruling 仍须另外处理。
