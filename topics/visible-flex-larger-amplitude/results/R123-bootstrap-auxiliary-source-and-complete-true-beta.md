# R123：逐频辅助源收紧的真实切口消费及完整 β 接口

作者：geometry_audit（GPT-6 Astra Pro；AI-assisted）。2026-11-13。

**状态：已证明并实际执行。** 将 R121 的同对象辅助源帽接入原 R63/R82 切口
泛函，再保留 R100 的全部 transverse 差项和真实远端项。原十个工作半径的
T 内头旧账本均被准确复现，然后全部严格改善。在 $r_T=1/64$ 时，原 T 内头
非 far 界 $91.519438231535689\ldots$ 降至
$0.000015386322574161713$ 以下。完整 true-far 仍严格为正，并按整质量收费一次。

这支付的是原 R100 参数域上的**完整真实内头 β**。保留旧外侧源账本进行的
全切口复测仍失败；本文没有宣布外侧固定点、全频匹配、strong 新 g 或闭曲面完成。

## 1. 原 R74 辅助族与 R100 横轴的准确分工

沿用 [R100](R100-hybrid46-parameter-chart-and-source-transfer.md) 的同一真实
背景、同一度规、全部 46 个浅低高度及完整深尾。令

$$
\mathcal S=\{2,4,\ldots,12\},\qquad
\mathcal T=\{14,16,\ldots,92\}.
$$

六个 $\mathcal S$ 参数取原 R74 复积盒；四十个 $\mathcal T$ 参数共享原
R59 绝对轴的加权 $\ell^1$ 预算。记完整真解为 $F(\xi,d)$。
R100 的辅助中心 $C_S(\xi)$ 是 R74 二十轴辅助族的限制：前六个原参数按
$\xi$ 变化，后十四个**参数增量**为零，原全部二十个非零中心系数保留。

因此 [R121](R121-inner-aux-cell12-spectral-bootstrap.md) 在原 R74 二十轴
全域上证明的谱帽，直接控制这个 $C_S(\xi)$，但不控制额外提升 $\Lambda d$
或完整 $F(\xi,d)$ 的谱。本文没有扩大 R121 的参数域。
全部 $d$ 作用仍由 R100 的
$N(F)-N(C_S)$ 完整四块比较单独支付，见第 4 节。

减去同高度的准确线性 DN 后，真实非线性低 DN 为

$$
\boxed{
\beta(\xi,d)=\mathfrak F N(C_S)
 +\mathfrak F\{N(F)-N(C_S)\}
 +B_{\rm cut}\mathcal D(z_{\rm true}).}
\tag{123.1}
$$

这正是 R100 式 (100.29) 的真实切口读出。显式低提升 $\Lambda d$ 从线性 DN
相减中准确消去，但它在非线性源和深图中的影响仍保留。
辅助场内部已受其自身 far 提升影响；(123.1) 最后的直接 far 是完整解的
$\mathcal D(z_{\rm true})$，不能重复加辅助 far，也不能删除。

## 2. 原真实切口泛函的局部替换

令 $\Phi_m$ 是原真实齐次列，按真实 node12 cut 的
$\Phi_{Q,m}(b)=1$ 归一。R63/R110 的原 canonical 源泛函为

$$
e_{\Xi_{12},m}(b)
=\sum_{n=12}^{224}\frac{\mu_n}{\mu_{12}}
       \int_{I_n}\Phi_{Q,m}(r)F_{\Xi,n,m}(r)\,dr.
\tag{123.2}
$$

原真实 cut 转换的正上界为

$$
c_i\ge\frac{\sqrt{12}\mu_{12}}{b^4w_b^2},
\qquad c_i<6375919.466913.
\tag{123.3}
$$

代码直接读取原 R63 far completion 包中的该数，并逐项核验与 R82、R100
相同；没有用两个独立范数上界相除来伪造点态转换。

对 $\sigma=1/64$，设 $\omega_m=(1+m)e^{m\sigma}$。
R121 的源帽已经包含 canonical 权 $e^{2m}$，且正频率行包含两个 Fourier
半幅。记其第 $m$ 模二次源帽为 $Q_m$，完整 mean/inverse 的共同余项质量为
$R_*>0$。令 $\varrho_m$ 是该完整余项的实际 paired 源质量，则

$$
\varrho_m\ge0,\quad\sum_m\varrho_m\le R_*,\qquad
R_*<8.867005764\cdot10^{-61}.
\tag{123.4}
$$

在 cell 12，(123.2) 的 $\mu_{12}/\mu_{12}$ 比率恰为 1。使用 R121 已核对
的真实归一列帽 $\phi_m\ge\sup_{I_{12}}|\Phi_{Q,m}|$，得到

$$
|e^{(12)}_{\Xi_{12},m}(b)|
\le J_m(Q_m+\varrho_m),\qquad
J_m=\phi_m(3/8)^{2m}\ge\phi_m e^{-2m}.
\tag{123.5}
$$

初等不等式 $e>8/3$ 支付了最后一步；这里是真正的原参考宽度 2，未借任何外解
谱。没有多加 $\mu$ 比、$r_x$、$\sqrt2$ 或 Fourier 因子 2。

原 R82 `source_rows` 中的 $a^{\rm old}_{mn}$ 已包含正确的各胞元 $\mu_n/\mu_{12}$
和原连续条带源积分。其 R74 全域放大量仍是
$t=4225/4096$。所以其它胞元直接保持

$$
O_m=\sum_{n=13}^{224}t\,a^{\rm old}_{mn}.
\tag{123.6}
$$

本次逐项读取并保留全部 $46\times212=9752$ 个严格正项，逐项向上舍入后相加。
它不是从已舍入的总源上界中减去一个独立 cell 12 上界。

每个模式的完整辅助源新界可取

$$
A_m^{\rm new}
\le\min\!\left\{A_m^{\rm old},\
c_i\omega_m\left[O_m+
\min\{t a^{\rm old}_{m,12},\ J_m(Q_m+R_*)\}\right]\right\}.
\tag{123.7}
$$

两个分支控制同一 $N(C_S)$，因此取较小值合法。特别地，低模式上原有序材料
积分有时更紧，不能用新的全胞元源估计强制替换它。全部二十个真实中心模式
以及全部 46 个辅助模式均保持。

R121 的场谱帽仍含其它胞元和辅助 far 的公共影响；(123.6) 又是这些胞元对
**直接切口源泛函**的贡献。两者处于不同恒等式的位置，均保留。R121 的
outside budget 在本消费器中没有被设零或从场帽中删除。

## 3. 完整 mean/inverse 余项在共同质量中只付一次

对每个模式，依据 (123.7) 内层两个上界的已知大小选择一个合法分支。
若选 R121 分支，把它写成

$$
c_i\omega_m[O_m+J_mQ_m]+c_i\omega_mJ_m\varrho_m;
$$

若选原完整分支，写成 $c_i\omega_m[O_m+t a^{\rm old}_{m,12}]$，余项系数取零。
记这两个表示的固定基项、余项系数分别为 $B_m,G_m\ge0$。
对任意固定非负输出权 $h_m$，(123.4) 给

$$
\sum_m h_m\,|[\mathfrak F N(C_S)]_m|_{W_{\sigma,1}}
\le\sum_mh_m B_m+R_*\max_m(h_mG_m).
\tag{123.8}
$$

这与把 (123.7) 的逐模帽相加是两条独立合法界，可以再取较小者。
程序分别保存两者；共享余项没有被重复算成每模一整份后又声称只收费一次。

对于整个低频 $W_{\sigma,1}$ 范数，取 $h_m=1$。
对于 $W_{\tau_b,1}$，取 $h_m=e^{m(\bar\tau_b-\sigma)}$，其中
原 `head_strip` 的有理上端
$\bar\tau_b<.144435830749$ 覆盖实际 cut 宽度。
对于 T 切口预算，取原同 g 的真实边界算子和各绝对轴给出的正权 $h_m$，
仅对 $m\in\mathcal T$ 求和。对于外场范数，取原逐模边界到场算子权。
这些均未改变原输出规范。

## 4. R100 的全部横轴差费用原样保留

在 $\|d\|_v\le r_T\le1$ 上，使用 R100 已证常数

$$
K_T=\frac{273259958272}{395007},\quad\eta=4096,\quad
q(r_T)=1+\frac{K_T+\eta}{256}r_T.
\tag{123.9}
$$

R83 原全部 213 胞元聚合的四个正数记为
$P_{m,M},P_{m,C},P_{m,B},P_{m,R}$。令 $t_{\max}$ 是 R100 原已证全域常数，
则原完整差界为

$$
\begin{aligned}
D_m(r_T)\le c_i\omega_m\big[&qP_{m,M}+qP_{m,C}+q^2P_{m,B}\\
&+q\{1+qt_{\max}+(qt_{\max})^2/3\}P_{m,R}\big].
\end{aligned}
\tag{123.10}
$$

其中 $q=q(r_T)$。最后一项仍是完整 mean/inverse 差，不是有限源替代式。
没有给未知 $F-C_S$ 免费使用 canonical 宽度 2 的谱增益；它仍在原 R100
连续物理条带空间中付费。完整新 β 的值可取

$$
|\beta_m|_{W_{\sigma,1}}
\le A_m^{\rm new}+D_m(r_T)+F_{\rm true}.
\tag{123.11}
$$

原 R83 完整值帽与 R100 完整桥差提供的另一有效分支也保留并取较小值。
整质量先对非 far 项求和或用 (123.8)，再只加一次 $F_{\rm true}$；有权整质量
只加 $\max_mh_m F_{\rm true}$。

这里 $F_{\rm true}$ 是原完整 true-far 正预算，实际小于
$5.632977252\cdot10^{-2341}$。原原理已证明该预算控制参考宽度 2 的整个低频
质量，因此它也控制本次两个较小条带，转换至 $\bar\tau_b$ 时不再为 far
重复乘一个逐模指数。

## 5. 实际新 β 与内头预算

新 stable interface 对原十个 $r_T$ 和完整单位域 $r_T=1$ 都保存了全部 46 模：

- 完整非 far $W_{\sigma,1}$ 帽及包含 true-far 的完整 β；
- 完整 $W_{\bar\tau_b,1}$ 帽；
- relative physical $\bar K$ 的常规 cosine 系数帽；
- 原四块 R100 完整差的实际重权；
- 两个条带的公共质量，原场范数及原 T 切口范数的公共质量。

逐模帽与公共质量分别保存；公共质量不由重复计费的单模 far 项相加。
部分严格上界如下，显示数均在准确有理上端之上：

| $r_T$ | 原 T 内头非 far 界 | 新 T 内头完整界（含一次 far） |
| --- | ---: | ---: |
| $1/64$ | $91.519438232$ | $.000015386322575$ |
| $1/16$ | $91.519483214$ | $.000060368384061$ |
| $1/4$ | $91.519663142$ | $.000240296630008$ |
| $1$ | 本次另作单位域计算 | $.000960009613793$ |

在 $r_T=1/64$ 时，共享余项给的非 far T 界准确为

$$
1582391494762328018576617289210511087634401310668562893065\,2^{-206}.
\tag{123.12}
$$

仅将合法逐模完整帽相加的另一个界为 $.000015388173363$；(123.12) 更紧，
两者均在主包中保留。

下表给 $r_T=1/64$ 时的部分完整 β；它们是绝对值上界，不是带符号的实际数值：

| 模式 | 完整 β 的 $W_{\sigma,1}$ 上界 |
| --- | ---: |
| 2 | $2.240939106\cdot10^{-51}$ |
| 4 | $6.378273783\cdot10^{-49}$ |
| 6 | $5.575800778\cdot10^{-51}$ |
| 12 | $5.605976701\cdot10^{-63}$ |
| 14 | $1.298735637\cdot10^{-64}$ |
| 16 | $3.079801600\cdot10^{-66}$ |
| 20 | $9.672488739\cdot10^{-69}$ |
| 40 | $9.681523499\cdot10^{-70}$ |
| 92 | $2.558074041\cdot10^{-79}$ |

整个 R100 单位域同时有

$$
\|\beta_{\le92}\|_{W_{\sigma,1}}<6.456441194\cdot10^{-49},\qquad
\|\beta_{\le92}\|_{W_{\bar\tau_b,1}}<1.082728653\cdot10^{-48}.
\tag{123.13}
$$

这个整低频范数仍主要由低模式决定；本次实质消除的是原极小 T 轴归一后的
大辅助源支出。其它频率块、完整 mean 和共同 cuff 高度规范继续由 R100 原证明
保留，本文没有重新给它们定零值或增加自由平移。

## 6. Cauchy 接口及全切口复测的边界

对每个给定 $r_T$，上述值界对六个 $\xi$ 的整个复单位积盒成立。
在 $\|\xi\|_\infty\le3/4$ 上，固定 $d$ 的一、二阶算子界分别可取共同
值帽的 4 倍和 64 倍。稳定接口分别保存两个输出条带的这两项界。

横轴导数先使用同一 $\xi$ 下
$\beta(\xi,d)-\beta(\xi,0)$ 的原 R100 桥差。辅助源在这次相减中准确消去，
不用再次收取其值帽。若 $2r_T\le1$，对外圈 $\|d\|_v\le2r_T$ 的桥差帽除以
$r_T$，得到内圈 $\|d\|_v\le r_T$ 的全部方向一阶 Cauchy 界。
桥差的完整 mean/inverse 项、$d=0$ 的旧完整差和两份 true-far 均保留。
在 $r_T=1$ 的值行没有宣称这一内部横轴导数门。

本次还使用原外侧全部 46 个真实源／边界算子和原场收缩常数，完整复测了原
十个六轴 $\ell^\infty$ 加四十轴 $\ell^1$ 自映及 Schur 门。原外侧源项 T
上界仍为 $1044.119606787742\ldots$，故旧全切口充分门仍失败。新主包如实记录
`all46_projected_cut_closed = false`。这不影响本文内头 β 的改进，也不证明
真匹配不存在；新的外侧中心、真实源及导数仍需各自完成认证。

## 7. 实际执行与固定文件

实际切口入口为
[inner_aux_bootstrap_cut_consumer.py](../computations/inner_aux_bootstrap_cut_consumer.py)，
SHA256 `4121303812eba278e6f69cdfd28ef87f47427cf7546c20bc11286872512bb0d1`。
会话 **39315** 和独立 `wait4` 均正式退出 0，wall **11.923767 秒**，峰
**83936 KiB**。**10142 项 Fraction 门全部为真**，包含全部 9752 个其它源正项，
所有原对象身份以及原十个 T 内头旧总界的准确复现。

完整消费主包
[2026-11-13-inner-aux-bootstrap-cut-r1.json.gz](../notes/2026-11-13-inner-aux-bootstrap-cut-r1.json.gz)
为 1172675 字节，SHA256：

```text
33cdff5738747578aedb22412cf4fd8bd78e087d9df2fde474fbbec59ffdc475
```

稳定接口入口为
[inner_aux_bootstrap_beta_interface.py](../computations/inner_aux_bootstrap_beta_interface.py)，
SHA256 `e3ead2bff1dd57780a606770d24b134c256efc9755f0c31a11ac106a0128d25b`。
会话 **11645** 和独立 `wait4` 均正式退出 0，wall **9.081299 秒**，峰
**47500 KiB**，**80 项 Fraction 门全部为真**。它准确复现消费主包中各原半径的
全部逐模非 far 值和 T 公共质量，并另计算 $r_T=1$。

稳定接口主包
[2026-11-13-inner-aux-bootstrap-beta-interface-r1.json.gz](../notes/2026-11-13-inner-aux-bootstrap-beta-interface-r1.json.gz)
为 253556 字节，SHA256：

```text
1bd50cb4f32bb17d1238dd2487df379526246651a5ebbf1ec6fdf5809699f5ea
```

两个同前缀 `-resource.json` 保存独立终态。完整文件清单及 SHA 见
[2026-11-13-inner-aux-bootstrap-cut-manifest.json](../notes/2026-11-13-inner-aux-bootstrap-cut-manifest.json)。
全部主文件都是 fresh 输出；原 R121、R63、R74、R82、R83、R100 及其执行源均未修改。

本次未运行 ODE、Arb、Node 或新源积分。所有证明比较使用 Fraction 和定向
dyadic，显示小数不进入比较。可从本课题目录用新的输出名复现：

```bash
python computations/inner_aux_bootstrap_cut_consumer.py \
  --out notes/fresh-inner-aux-bootstrap-cut.json.gz
python computations/inner_aux_bootstrap_beta_interface.py \
  --out notes/fresh-inner-aux-bootstrap-beta-interface.json.gz
```
