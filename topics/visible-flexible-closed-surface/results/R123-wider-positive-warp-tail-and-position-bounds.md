# R123：保持固定 cuff 的尾部扩宽、精确端口与真实路径几何界

2026-11-12，Astra-visible-flex-fd2d / constructive_geometry。

**状态：已证明，条件构造及条件几何结论。** 从一个正精确径向归一化的固定 source 出发，cut 向外移动有完整的显式参数公式，保持正径向速度和 C² 平 cuff，并使旋转背景的两种主曲率逐 source 点不增。真实非轴对称尾若满足同 g 与固定 cuff，则其球包、板宽及 held 球排除由路径长度直接控制。没有证明新非线性尾或活动核心存在，没有将背景曲率代替实际曲率，也没有证明实际尾或完整闭核的 reach。

## 1. 固定数据及结论的准确范围

采用本题 `closing_weighted_tail.mjs` / `closing_recalibrated_tail.mjs` 的正向 source，固定：

- cuff 半径 $r_f=8/25$、source 的所有 δn/cn、有限校准常数及无限深校准根；
- wCut=$w_c=1/10$、K=7、protectCell=160；
- 全部 cap/valley 控制、positive free-warp weights、cut-preserving 规则；
- 未改无限深 source 及其在 cuff 的 C² 平连接。

浅层数据为 `notes/2026-11-12-fd2d-ellipse-cuff032-cut04-config.json`。
无限深校准括号为 R15 §2.2 已使用的 $\alpha_n\in[1/2,2]$（$n\ge80$）；它只依赖 δn、cn、R=64、指数 11/4，和当前操作无关。
source 身份与参数缩放证明见 `notes/2026-11-09-closing-deep-background-n160.md`、
`notes/2026-11-09-closing-deep-radius-family.md`；其中上游 R28 的 Git blob 为
`cf9881e3ae2c2797a61213ab099dbec239be5f0d`。

令原 cut 为 $R_0=2/5$。本结果的一个明确前提是：原目标由其真实积分定义的归一化 $\lambda_0$ 为正。这里用 λ 表示全局 warp 常数，以免和 source 的逐 cell 校准根 αn 混淆。有限 quadrature 给出的 $\lambda_0\simeq7.71714$ 不是本结果对该前提的区间证明。

把 cut 改为 $R\ge R_0$，同时把物理径向宽度改为 $R-r_f$。保持上述全部 source 数据不变。以下证明给出新归一化和完整轴对称目标尾；这是一族不同的物理度量 $g_R$。旧 cut 的线性或非线性 DN 均不能未经重算直接使用。

## 2. 只需改变一个明确的径向项

将有限受保护 source 从深端到外端按顺序连接，用 ξ 表示共同的单调参数。可直接选旧 source 的物理半径作 ξ；不能把相邻局部 x 的未缩放导数直接视为同一 ξ 导数。旧 source 径向函数记 $r_o(\xi)$，它与 R 无关，且 $r_{o,\xi}>0$。
cap 后的 slope $w(\xi)>0$、其导数、$E=1+w^2$、保护函数 χ 和正权重 ω 都与 R 无关。

程序在有限部分的物理径向速度为

$$r_{R,\xi}=A_R'(\xi)+\lambda(R)B'(\xi), \tag{1}$$

其中

$$A_R'=r_{o,\xi}j_R(1-\chi)+\chi\frac{|w_\xi|}{K E^{3/2}},
\qquad B'=\omega\chi\frac{r_{o,\xi}}E. \tag{2}$$

除 cell 0 的最后 flat source port 外，$j_R=1$。该外 port 上令 $S=S_5(x)$，则准确地

$$\chi=1-S,\qquad
j_R=1+\left(\frac R{r_{o,c}}-1\right)S,$$

其中 $r_{o,c}$ 是固定 source 的最外半径。于是唯一的 R 导数为

$$\partial_R A_R'=D'(\xi)
=\frac{r_{o,\xi}}{r_{o,c}}S^2\quad\text{（最外 port）},\qquad
D'=0\quad\text{（其余部分）}. \tag{3}$$

以最深受保护点为积分起点，定义

$$A_R(\xi)=\int A_R',\quad B(\xi)=\int B',\quad D(\xi)=\int D'.$$

在外端以无自变量的 $A_R,B,d$ 表示总量。显然 $B>0$，且

$$0<d=\frac1{r_{o,c}}\int_{outer\ port}r_{o,\xi}S^2d\xi
<\frac{r_{o,c}-r_{o,start}}{r_{o,c}}<1. \tag{4}$$

这里仅用 $0\le S\le1$、非退化 source port 与 $r_{o,start}>0$，没有使用 quadrature 的符号判断。

设受保护深端半径为固定 $r_d$。目标 cut 条件为

$$r_d+A_R+\lambda(R)B=R.$$

由 $A_R=A_{R_0}+(R-R_0)d$ 得到准确公式

$$\boxed{\lambda(R)=\lambda_0+\frac{(R-R_0)(1-d)}B.} \tag{5}$$

所以每个 $R\ge R_0$ 均有 $\lambda(R)\ge\lambda_0>0$；归一化解唯一。
在 χ>0 处，(1) 的 free term 严格为正；χ=0 的端点由 $r_{o,\xi}j_R>0$ 保证。因此整个有限尾的径向速度严格为正。

## 3. 点态径向、曲率、长度与高度的精确单调性

在任意固定 source 点，

$$\boxed{\partial_R r_R(\xi)
=D(\xi)+(1-d)\frac{B(\xi)}B\in[0,1].} \tag{6}$$

其 ξ 导数也非负：

$$\partial_R r_{R,\xi}=D'+\frac{1-d}B B'\ge0. \tag{7}$$

因此增大 R 既不减小任一点的物理半径，也不减小径向速度。深端两式为零，cut 处 (6) 等于 1。

旋转背景的两种主曲率绝对值是

$$|\kappa_{mer,R}|=\frac{|w_\xi|}{r_{R,\xi}E^{3/2}},\qquad
|\kappa_{circ,R}|=\frac w{r_R\sqrt E}.$$

分子和 E 不变，分母不减，所以这两种背景曲率逐 source 点不增。这个命题也覆盖 $w_\xi=0$ 的 cusp，那里第一式为零。它不涉及尚未求出的非轴对称曲面的实际第二基本形式。

### 3.1 C² 接合与端口

有限 join 上 w、wξ 与 (1) 连续，且径向速度为正，故物理高度图的
$h'=\pm w$、$h''=\pm w_\xi/r_{R,\xi}$ 连续。辅助 $r_R(\xi)$ 本身无须在绝对值 cusp 处具有三阶或二阶导数。
最深保护端 χ=0，(3) 也为零，因此原深 source 的位置和径向速度保持；其 w、wr 趋零的无限 C² 平 cuff 证明原样有效。

在外端 S=1、χ=0，(1) 为
$r_{R,\xi}=r_{o,\xi}R/r_{o,c}$。
最后 source port 的 $w_\xi=-7wr_{o,\xi}/r_o$，所以新 cut 准确满足

$$r=R,\qquad w=w_c,\qquad w_r=-7w_c/R. \tag{8}$$

上半核由中央向 cuff 行进时，背景弧长坐标 s 的两 jet 为

$$\boxed{a=R,\qquad a'=-\frac1{\sqrt{1+w_c^2}},\qquad
a''=\frac{7w_c^2}{R(1+w_c^2)^2}.} \tag{9}$$

相应 $z'=w_c/\sqrt{1+w_c^2}$。因此扩宽保留 cut 的一阶倾角，同时按 $1/R$ 准确改变二阶径向 jet；前缀必须匹配新 (9)，不能继续把旧 $a''$ 当作目标。

### 3.2 长度和高度是 R 的仿射函数

设从 cuff 到 cut 的目标经线长为 $L(R)$，背景高度差的绝对值为 $V(R)$。未改深段贡献固定，有限段为

$$L(R)=L_{deep}+\int\sqrt E\{A_R'+\lambda(R)B'\}d\xi,$$

$$V(R)=V_{deep}+\int w\{A_R'+\lambda(R)B'\}d\xi.$$

由 (3)、(5)，两者均为 R 的仿射函数，且

$$L'(R)=\int\sqrt E\left(D'+\frac{1-d}B B'\right)d\xi,$$

$$V'(R)=\int w\left(D'+\frac{1-d}B B'\right)d\xi. \tag{10}$$

括号是非负权，积分恰为 $d+(1-d)=1$。若整个 source 有 $w\le W$，则

$$\boxed{1\le L'(R)\le\sqrt{1+W^2},\qquad 0<V'(R)\le W.} \tag{11}$$

因此可准确增加尾部材料长度，背景新增高度至多为 $W(R-R_0)$。这里只控制背景高度差；对于非线性尾，不能由 (11) 宣称实际高度单调或 $|z|\le Z$。

## 4. 当前参数的严格粗量与实际有限新端口

`notes/2026-11-12-fd2d-geometry-tail-length-necessary-bound.md` §3 已对本 source 完整证明

$$0<w< W:=.100122,$$

包含 cut-preserving 两段及全部无限未改深 source。该上界不含物理 cut R，所以本节整个扩宽族都适用。
也可直接用 $L(R)<(R-r_f)\sqrt{1+W^2}$。准确分数平方比较给

| cut R | 径向宽度 | 严格 L 上界 | 相对 R0 的背景新增高度上界 |
|---:|---:|---:|---:|
| .4 | .08 | .0804 | 0 |
| .45 | .13 | .13065 | .0050061 |
| .50 | .18 | .1809 | .0100122 |

这些严格粗数也容纳 source assembler 的 binary64 endpoint 差异；将各显示径宽加 $10^{-16}$ 后，平方不等式仍严格成立。

新配置和有限线性端口已另名保存，原 .4 输入未动：

- `notes/2026-11-12-fd2d-wider-tail-cut045-config.json`，SHA256 `7189d35b2489b76f1072ae021cbc801d5b17b0a4f19eacb9bc7cb29ddded2ca9`；
- `notes/2026-11-12-fd2d-wider-tail-cut050-config.json`，SHA256 `39a0d34e5f37f097bffb9c6c1cd21a4634bf8aedf6701f933062bed345e90d33`；
- 两个 `...wider-tail-cut{045,050}-linear-port-01.json` 由实际 `fd2d-gc-linear-tail-batch.mjs` 分别运行，48 cells、每段256步、模式 2/4/6/8；均自然 exit0。

| R | 有限 λ | 有限 L | 有限 V | 有限 D2 |
|---:|---:|---:|---:|---:|
| .45 | 20.59206829226054 | .13006949604313445 | .0023393603215910294 | 8.943319656154925 |
| .50 | 33.46699667014308 | .1800829334150301 | .0027663431030757273 | 7.8144486356260145 |

这张表仅是有限 quadrature / 线性 transfer 的实际结果，不能当作区间证书或真实非线性 DN。解析结论 (5)–(11) 不依赖这些末位数。特别是 D2 已改变，证实不能沿用旧 cut 的线性方向；任何新固定 g 的非线性 branch 都需匹配其自己的端口。

## 5. 实际尾的球包、板宽及 held 球排除

本节假设确实给出了某条实际 C¹ tail 图 F，其 cuff 是逐材料固定的半径 $r_f=.32$ 圆，平面高度为 Z，并且

$$.9\le Z\le1.378642<1.379.$$

假设其实际拉回度量满足 $F^*e\le(1+\epsilon)g_R$，其中 $0\le\epsilon\le10^{-6}$；准确等距为 ε=0。令 $R\le.5$。
每条固定材料角的 cuff→尾点路径长至多 $\sqrt{1+\epsilon}L(R)$，所以第 4 节给

$$\operatorname{dist}(F(s,u),F_{cuff}(u))
<.1809\sqrt{1+10^{-6}}<.181. \tag{12}$$

这由真实路径长度得到，不要求实际路径沿着背景旋转经线，不要求尾高度单调，也不要求先有任何曲率或 reach 界。

### 5.1 水平板与球包

cuff 圆的水平半径为 .32，故 (12) 立即给整个真实尾

$$\sqrt{x^2+y^2}<.501<.85. \tag{13}$$

因此它在任何空间相位均满足 R121 初始活动板的要求。又因

$$.32^2+1.379^2<1.416^2,$$

有

$$\boxed{|F(s,u)|<1.416+.181=1.597<2.25.} \tag{14}$$

这是实际尾的球包，而非背景高度估算。它不蕴含 $|z|\le Z$；如某个帽嫁接假设另需高度排序，仍须单独支付。

### 5.2 真实中央见证点的 held 保护

取 R121 §7 的实际中央见证点 $p=(0,A_q,0)$，$A_q\ge1.28$。它到整个 cuff 圆的距离为

$$\sqrt{(A_q-.32)^2+Z^2}
\ge\sqrt{.96^2+.9^2}>1.315.$$

由 (12) 的三角不等式，

$$\boxed{\operatorname{dist}(p,F(tail))>1.315-.181=1.134>.9.} \tag{15}$$

相同证明对反射下尾成立。若活动相位图通过空间旋转和材料角平移产生，cuff 圆集合、路径长度与上述包围条件均不变，故 (13)–(15) 自动覆盖整个相位区间。
中央 witness 必须确为实际曲面上的点，Aq 必须来自实际中央核；本节没有从支撑参数或背景自动推定这个事实。

## 6. 对完整强目标的作用和未付项

R121 的固定帽只消费 cuff 半径、实际 Z、原活动闭核的几何条件及标记窗；把 cut 在内部从 .4 改成 .45 或 .50 不改变这些固定帽本身。
当真实新尾满足同 g 与固定 cuff 后，(13)–(15) 已支付其板、球和 held 保护，无需再用全尾位置采样代替这些解析结论。

仍须实际解决并证明：新 g 的非线性前缀/尾端口与两 jet 接合、完整 prefix 的相应位置条件、可能需要的 $|z|\le Z$、真实局部曲率、原平盘闭核的全局 reach，以及最终全时闭族与同 g 加密。背景曲率的单调性和真实路径几何都不代付这些问题。
当前主线 p148 的 cut=.4 继续原 BVP；本结果提供另名、可消费的扩宽设计自由度，不将一阶 cut gain 的大幅外推视为非线性不存在结论。证毕。
