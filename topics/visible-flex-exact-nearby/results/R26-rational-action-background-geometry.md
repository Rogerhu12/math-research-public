# R26：有理作用量背景 μ=484/89 的全域整数区间几何

2026-11-12，visible-exact-astra-f6a2。

**状态：已证明的中间结论。** 本文为 R25 的实际新背景重新证明几何，
不沿用 μ=4√2 的旧证书。计算覆盖连续小区间，余下的无限区间由解析比较覆盖。
这里没有有限幅精确等距解，也没有开平帽或非线性接尾结论。

## 1. 同一个对象和结论

取
$$
\mu=\frac{484}{89},\quad \nu=\frac{495}{89},\quad
A=\mu^2+\frac\mu4=\nu^2=\frac{245025}{7921},
\qquad Q(x)=\mu^2-A\operatorname{sech}^2x.
$$
以精确初值定义线性 ODE 和高度：
$$
h''=Qh,\qquad h(0)=1,\quad h'(0)=0,\qquad
z(x)=\int_0^x h(t)^{-2}\,dt.
\tag{1}
$$
下面的证明同时给出 $h>0$，所以积分合法。令
$$
X(x,\theta)=h(x)^{-1}e_r(\theta)+z(x)e_z.
$$
两端补点后，$X$ 为闭 $C^2$ 嵌入球面。对其外法向 $n$，有
$$
\sup|X|<\frac76,\quad D<\frac73,\quad
\max_i|\kappa_i|<4,\quad X\cdot n>\frac45,
\quad K_{\rm Gauss}<4.
\tag{2}
$$
从而
$$
\operatorname{reach}(X(S^2))>\frac14,
\qquad \frac{\operatorname{reach}(X(S^2))}{D}>\frac3{28}.
\tag{3}
$$
这是具有 R25 线性频率谱隙的**同一**径向对象。特别是改变谱参数后，
直径及厚度有独立的实际证明；没有把旧数值几何挪到新曲面。

复现：在仓库根运行

```bash
PYTHONDONTWRITEBYTECODE=1 python topics/visible-flex-exact-nearby/scripts/rational_background_interval.py
```

脚本已实跑通过。证书位于
`notes/2026-11-12-rational-background-interval-certificate.json`；
其中同时保存本脚本和整数算术依赖的 SHA256。

## 2. 有限区间计算的数学定义

取 $B=3/2$，将 $[0,B]$ 分为 600 个长度 $\Delta=1/400$ 的闭小区间。
算术采用固定分母 $S=2^{160}$ 的 dyadic 区间；端点为 Python 整数。
乘除、平方和整数平方根均向外舍入，比较全部为整数交叉相乘。
代码的 `decimal_display` 只显示结果，不参与任何判定。

指数包络采用
$$
P_{64}(t)=\sum_{j=0}^{64}\frac{t^j}{j!},\qquad
0\le e^t-P_{64}(t)
\le\frac{t^{65}/65!}{1-t/66},\qquad 0\le t\le3.
\tag{4}
$$
尾项比不超过 $t/66<1$，故 (4) 是严格包络。用
$$
\operatorname{sech}^2x=\frac{4e^{2x}}{(e^{2x}+1)^2},\quad
\tanh x=\frac{e^{2x}-1}{e^{2x}+1},\quad
Q'=2A\operatorname{sech}^2x\tanh x
$$
及 $Q$ 的递增性得到每一完整小区间的 $Q,Q'$ 包络。
与 R21 不同，本次 $\mu,A$ 都是指定有理数；没有平方根参数的近似替代。

为明确没有以数值轨道代替真解，记左端包含为 $H_i,V_i,Z_i$，
连续小区间的势包含为 $Q_i$，并记其绝对上界为 $H_c,V_c,Q_c$。
线性系统 $h'=v,v'=Qh$ 先验在有限区间存在。积分方程给
$$
M_h=\frac{H_c+\Delta V_c}{1-\Delta^2Q_c},\qquad
M_v=V_c+\Delta Q_cM_h.
\tag{5}
$$
每一步均验证分母为正。首先取
$$
H=H_i+[0,\Delta][-M_v,M_v],\quad
V=V_i+[0,\Delta][-Q_cM_h,Q_cM_h],
$$
再四次与 $H_i+[0,\Delta]V$、$V_i+[0,\Delta]Q_iH$ 求交。
各个包络始终包含真实连续解。每一步都验证 $\inf H>0$，
随后 $Z=Z_i+[0,\Delta]H^{-2}$ 包含高度。

从
$$
h'''=Q'h+Qv,\quad v''=Q'h+Qv,\quad z''=-2v/h^3
$$
得到下一左端的向外 Taylor 包含：
$$
\begin{aligned}
H_{i+1}&=H_i+\Delta V_i+\frac{\Delta^2}{2}Q(x_i)H_i
  +\frac{\Delta^3}{6}(Q_i'H+Q_iV),\\
V_{i+1}&=V_i+\Delta Q(x_i)H_i
  +\frac{\Delta^2}{2}(Q_i'H+Q_iV),\\
Z_{i+1}&=Z_i+\Delta H_i^{-2}-\Delta^2V/H^3.
\end{aligned}
\tag{6}
$$
这些余项使用完整小区间的包络。从精确初值 $(1,0,0)$ 归纳即覆盖全段。

## 3. 每个连续小区间的实际判据

令 $p=\sqrt{1+v^2}$。真实表达式为
$$
|X|^2=h^{-2}+z^2,\quad
\kappa_\theta=h/p,\quad
\kappa_s=Q(h/p)^3,\quad
K_{\rm Gauss}=Q(h/p)^4,\quad
X\cdot n=\frac{h^{-1}+zv}{p}.
\tag{7}
$$
对每个全小区间包络，脚本逐一验证
$$
|X|^2<\frac{49}{36},\quad
\kappa_\theta<4,\quad |\kappa_s|<4,\quad
K_{\rm Gauss}<4,\quad X\cdot n>\frac45.
\tag{8}
$$
下面是准确 dyadic 端点的显示值，证明输入仍是证书中的整数：

| 连续包络 | 极值端点显示 |
|---|---:|
| $|X|^2$ 上界 | 1.3251774590272325 |
| $\kappa_\theta$ 上界 | 1.0000000000000000 |
| $|\kappa_s|$ 上界 | 3.7174424512543730 |
| $X\cdot n$ 下界 | 0.8217962857197761 |
| $K_{\rm Gauss}$ 上界 | 3.3538578078096010 |
| $h$ 下界 | 0.9534005889459924 |

例如第一行的准确有理数为
$$
\frac{1936749026122305791364110484376446716127266821251}
{1461501637330902918203684832716283019655932542976}
<\frac{49}{36}.
$$
最后一步还用整数比较支付
$$
h(B)>20,\quad \frac{h'(B)}{h(B)}>\frac92,\quad
\frac{81}{100}<z(B)<\frac9{10},\quad Q(B)>22,
\quad \mu^2<30.
\tag{9}
$$
因此 (8) 是整个有限区间的严格结论，(9) 是下一节的精确输入。

## 4. 无限尾不依赖数值外推

对 $x\ge B$，$22<Q(x)<\mu^2<30$。由 (9) 和 $h''=Qh$，
$h,h'$ 保持正。令 $w=h'/h$，则 $w'=Q-w^2$。
在 $w=9/2$ 上，右端严格大于 $22-81/4=7/4$；
首次交叉论证给
$$
w>\frac92,\qquad h(x)>20e^{(9/2)(x-B)}.
\tag{10}
$$
故
$$
z_\infty-z(B)<\int_0^\infty\frac{e^{-9t}}{400}\,dt
=\frac1{3600},\qquad z_\infty<\frac{91}{100}.
\tag{11}
$$
尾部 $a=1/h<1/20$，于是
$$
|X|^2<\frac1{400}+\left(\frac{91}{100}\right)^2<\frac{49}{36}.
$$
将 (7) 改写为
$$
\kappa_\theta=\frac1{\sqrt{a^2+w^2}},\quad
\kappa_s=\frac Q{(a^2+w^2)^{3/2}},\quad
K_{\rm Gauss}=\frac Q{(a^2+w^2)^2},
$$
得到
$$
\kappa_\theta<\frac29<4,\quad
|\kappa_s|<30\left(\frac29\right)^3=\frac{240}{729}<4,\quad
K_{\rm Gauss}<30\left(\frac29\right)^4=\frac{480}{6561}<4.
$$
而
$$
X\cdot n=\frac{a^2+zw}{\sqrt{a^2+w^2}}
>\frac{81/100}{\sqrt{1+(1/90)^2}}
>\frac{81}{101}>\frac45.
\tag{12}
$$
脚本也将这几个有理不等式独立列为 `tail_tests`，全部通过。
偶性覆盖负半轴。

## 5. 两极、嵌入和全局 reach

由 $Q$ 偶和初值唯一性，$h$ 偶，$z$ 奇。全实轴 $h>0$ 已由前两节支付。
从 $w(0)=0$ 和 $Q<\mu^2$，首次交叉得 $w<\mu$。
又 $Q\to\mu^2$，对任意 $0<c<\mu$，充分远处有 $Q>c^2$，
Riccati 比较给 $\liminf w\ge c$；令 $c\uparrow\mu$ 得 $w\to\mu$。

尾部经线长度有限，因为
$$
\frac{\sqrt{1+h'^2}}{h^2}=a\sqrt{a^2+w^2}
$$
由 (10) 可积。上端以 $a=1/h$ 为平面极径，则
$$
z_a=-1/h',\quad z_a/a=-1/w\to-1/\mu,
\quad z_{aa}=-Q/w^3\to-1/\mu.
$$
这恰使旋转图的两个 Hessian 特征值连续趋于 $-1/\mu$，
故补点为正则 $C^2$ 图。下端同理。内部 $z'>0$，
每个内部高度仅一个圆，故闭面嵌入。

由 (8)、(12) 得 (2)，包括两极的连续极限。最后解释 (3) 的全局部分。
对任意 $|t|<\min(4/5,1/4)=1/4$，$X_t=X+tn$ 的微分可逆，
且 $X_t\cdot n>4/5-|t|>0$。径向投影 $X_t/|X_t|$ 是紧连通曲面
到 $S^2$ 的局部微分同胚，故为覆盖；因 $S^2$ 单连通，该覆盖为一层。
因此每个偏移面都是径向图。固定方向 $u$，写其半径为 $r_t(u)$，
内积微分给
$$
\partial_t r_t(u)=\frac1{u\cdot n}>0.
$$
不同偏移面严格嵌套，整个法向管单射。最近点的位移垂直切平面，
故该管内最近点唯一。严格的曲率/支撑余量在紧曲面上取到，
给 reach 严格大于 $1/4$。又 $D\le2\sup|X|<7/3$，遂得 (3)。

## 6. 使用范围

R25 的唯一第四模及线性增长谱隙与本文几何现在属于同一背景。
这只允许对该背景及其明确误差预算作下一步分析。固定开帽、
真实全尾的非线性接合、目标有限幅种子的全频零解以及 held 比例
仍须为同一新对象完成，不能由本证书或背景无穷小场推出。
