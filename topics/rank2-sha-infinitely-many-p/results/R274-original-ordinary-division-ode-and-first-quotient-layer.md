# R274 — 原普通 CM 除法对数的有限 ODE、十七根边界与真实第一商层

日期：2026-11-13。**状态：以下全局微分恒等式、原 CM 多项式的非线性方程、固定十七根处边界、第一整商层的全部系数及首权的有限有理替代均已证明。没有从单个商层单位推出原完整中央非零。**

本篇继续 R270，保留同一个普通 Frobenius $\pi$、单位根 $b_0$、原多项式 $R$、
reciprocal $R^*$ 和真正的三源 $S_A,S_B,S_H$。不改变任何来源 charge，也不删除 R266 的返回乘子。

## 1. 原连接给出的精确二阶方程

设 $p=4r+1\ge13$、$p\ne17$，并沿用
$$
v=x^{-2},\quad \Theta(v)=\vartheta(z(v)),\quad
R(U)=\frac{\sigma(\pi z)}{\sigma(z)^p},\quad
R^*(v)=v^rR(1/v),
$$
$$
\pi b_0=p,\qquad R(0)=1,\quad R\equiv1\bmod p,\quad [v^r]R=\pi.
\tag{1}
$$
定义原完整除法对数和固定算子
$$
L_p(v)=\frac{\log R(v)}p,\qquad
\mathcal D=16v(1-v)\frac{d^2}{dv^2}+(12-20v)\frac d{dv}.
\tag{2}
$$

**定理 1。** 在闭单位圆盘的原有理／解析函数中，准确有
$$
\boxed{
\mathcal D L_p
=-1+\frac{\pi^2}{p}\left(\frac{R^*}{R}\right)^2
=-1+p\,b_0^{-2}\left(\frac{R^*}{R}\right)^2.
}
\tag{3}
$$
等价的原多项式恒等式是
$$
\boxed{
16v(1-v)(RR''-(R')^2)
 +(12-20v)RR'+pR^2-\pi^2(R^*)^2=0.
}
\tag{4}
$$

**证明。** 置 $T=\log\Theta$。R270(2) 的真实 theta 连接给
$$
\mathcal DT=1.
\tag{5}
$$
亦可直接由
$$
(\log\vartheta)_{zz}=1/x,\qquad
(v_z)^2=16v^{3/2}(1-v),\qquad
v_{zz}=4v^{1/2}(3-5v)
$$
验证 (5)。

R270(15) 给
$$
L_p(v)=\frac1pT(v_\pi)-T(v),\qquad
u(\pi z)=u\,\frac{R^*}{R}.
$$
所以
$$
\partial_z^2T(v_\pi)=\pi^2/x(\pi z)
=\pi^2v^{1/2}(R^*/R)^2.
$$
除以 $v^{1/2}$，得到
$\mathcal D(T(v_\pi))=\pi^2(R^*/R)^2$。
结合 (5)，证明 (3)。将 $\mathcal D\log R=p\mathcal DL_p$ 乘 $R^2$，
便得到 (4)。$\square$

式 (3) 的右端第一修正从整体的 $p$ 一阶开始。
不能只看到 $v_\pi=\pi^4v(E/R)^4$ 就把全圆盘误差写成 $p^3$：
$E=R^*/\pi$ 的 reciprocal 高项确有 $p^{-1}$。
这与 R270 的**指定有限系数**误差不矛盾；后者另付了次数、阶乘和参考分母。

(4) 同时保留原点边界 $R(0)=1$ 与无穷边界 $[v^r]R=\pi$；
特别地
$$
12R'(0)=\pi^4-p.
\tag{6}
$$
没有引入任意的附加代数分支。

## 2. 固定十七根处的实际边界系统

仍取
$$
\beta=4-i,\qquad
K(v)=(4-i)v^4+(-12+20i)v^3+(28+10i)v^2+(-20-12i)v-i.
$$
R270 已证明唯一整除法
$$
L_p=I_p+KQ_p,\qquad \deg I_p<4,\qquad Q_p\in\mathcal O\langle v\rangle,
\tag{7}
$$
且其真实四维余式满足
$$
17pI_p=(p-\sigma_\pi)\ell_\beta+(1-p)\log_p\beta
\quad\bmod K,
\tag{8}
$$
$$
\ell_\beta=\frac14\log_p\bigl(256v^3(v-1)^2K'(v)^4\bigr).
$$
这里 $\sigma_\pi$ 是原 $\beta$ 核上 $P\mapsto[\pi]P$ 的置换；
它不是对原完整 Mellin 的变量替换。

写
$$
a(v)=16v(1-v),\qquad b(v)=12-20v,\qquad
\eta_p=-1+pb_0^{-2}(R^*/R)^2.
$$
将 (7) 代入 (3)，得到原商的完整有限阶系统
$$
\boxed{
aKQ_p''+(2aK'+bK)Q_p'
 +(aK''+bK')Q_p=\eta_p-\mathcal DI_p.
}
\tag{9}
$$
所有系数是固定多项式，唯一随 $p$ 的非线性源是已经明确保留的
$pb_0^{-2}(R^*/R)^2$。

在每个固定十七根 $\kappa$（即 $K(\kappa)=0$）处，真实解析商满足
$$
\boxed{
2a(\kappa)K'(\kappa)Q_p'(\kappa)
 +(aK''+bK')(\kappa)Q_p(\kappa)
=\eta_p(\kappa)-(\mathcal DI_p)(\kappa).
}
\tag{10}
$$
$2a(\kappa)K'(\kappa)$ 是允许素位的单位：这些四元轨道互异，
$\kappa\ne0,1$，且素位不除 $34$。
原点还必须同时满足
$$
Q_p(0)=-I_p(0)/K(0),
\tag{11}
$$
$$
12\bigl(K(0)Q_p'(0)+K'(0)Q_p(0)\bigr)
=-1+\pi^4/p-12I_p'(0).
\tag{12}
$$
(10) 不是凭空增加的四个独立中央零条件；
它是同一个实际商在固定根处的正则边界。
(9)–(12) 保留原 Frobenius 的第一商层，没有用固定挠值替换整个函数。

## 3. 第一 Frobenius 商层可以完全算出

定义固定有限有理多项式
$$
\boxed{
\ell_r(v)=\sum_{n=1}^r\lambda_nv^n,\qquad
\lambda_n=-\frac1{12n}
 \prod_{k=1}^{n-1}\frac{4k+1}{4k+3}.
}
\tag{13}
$$
所有这些分母在当前素位都是单位。
直接作用 $\mathcal D$，准确有
$$
\mathcal D\ell_r=-1-4rp\lambda_rv^r.
\tag{14}
$$

**定理 2。** 原完整 $L_p$ 满足
$$
\boxed{L_p\equiv\ell_r\pmod{p\mathcal O\langle v\rangle},\qquad
\lambda_r\equiv b_0^{-1}\pmod p.}
\tag{15}
$$
因此
$$
S_p=\frac{L_p-\ell_r}{p}\in\mathcal O\langle v\rangle
\tag{16}
$$
是**实际**第一整商，而其精确方程是
$$
\boxed{
\mathcal DS_p=
 b_0^{-2}(R^*/R)^2+4r\lambda_rv^r.
}
\tag{17}
$$

**证明。** 因 $R-1\in pv\mathcal O[v]$，有
$$
L_p\bmod p=(R-1)/p\bmod p,
$$
故它是次数至多 $r$、常数为零的多项式。
(3) 模 $p$ 给 $\mathcal DL_p=-1$。
对单项式有
$$
\mathcal D(v^n)
=4n(4n-1)v^{n-1}-4n(4n+1)v^n.
\tag{18}
$$
在次数至多 $r$、常数为零的空间中，逐项递推的前系数
$4n(4n-1)$ 全部为单位，故解唯一，恰为 (13)。
其最高系数又等于 $R_r/p=\pi/p=b_0^{-1}$，证明 (15)。
(14) 与 (3) 相减再除以 $p$，得到 (17)。$\square$

还可把 (16) 的**全部模 $p$ 系数**写出，而不是只给次数界。

**定理 3。** 模 $p$，
$$
\boxed{
S_p(v)=\sum_{m=1}^{r}s_{r+m}v^{r+m},
\qquad
s_{r+m}=
-\frac{\lambda_r\,4^m}
 {4m(4m-1)\binom{2m}{m}}.
}
\tag{19}
$$
所有 $s_{r+m}$ 都是单位。特别地
$$
\boxed{
s_{r+1}=-\frac1{6b_0},\qquad
s_{2r}=-\frac1{2b_0^2}
\quad\bmod p.
}
\tag{20}
$$

**证明。** 在模 $p^2$ 中
$$
L_p\equiv (R-1)/p-\frac p2((R-1)/p)^2.
$$
结合 (15)，可知 $S_p\bmod p$ 的次数至多 $2r$。
而 (17) 模 $p$ 是
$$
\mathcal DS_p=b_0^{-2}v^{2r}-b_0^{-1}v^r.
\tag{21}
$$
其从常数到 $v^{r-1}$ 的右端为零，(18) 逐项给
$s_1=\cdots=s_r=0$。在 $v^r$ 处给
$$
s_{r+1}=\frac{r\lambda_r}{(r+1)(4r+3)}
\equiv-\lambda_r/6.
$$
此后至 $2r-1$ 的递推是
$$
s_{n+1}=\frac{n(4n+1)}{(n+1)(4n+3)}s_n.
$$
令 $n=r+m$ 并用 $4r+1=p$，得到
$$
s_{r+m}
=-\frac{\lambda_r}{2(4m-1)}
 \prod_{j=1}^{m-1}\frac{2j}{2j+1}.
$$
恒等式
$$
\prod_{j=1}^{m-1}\frac{2j}{2j+1}
=\frac{4^m}{2m\binom{2m}{m}}
$$
给 (19)。$m\le r<p/4$，所列分母及分子均为单位。
最后比较 (21) 的 $v^{2r}$ 项：
$\mathcal D(v^{2r})$ 的同阶系数模 $p$ 为 $-2$，
故 $s_{2r}=-b_0^{-2}/2$。$\square$

这个首尾单位属于除法对数的实际第一整商。
原来源 $a_i(v)$ 从 $v$ 起，且原有限系数还乘有
$R^{n_j+1}E^{-n_j-1}\exp(-68L_p)$；
因此不能把 (20) 的末端单位直接当成第二中央权非零。
R270(26) 的聚合与非中央 carry 继续有效。

## 4. 原十七余式与商项的第一层已完全分离

令 $\operatorname{rem}_K,\operatorname{quo}_K$ 为首系数为单位的真实多项式除法。
从 (15)、(19) 得到
$$
\boxed{
\begin{aligned}
I_p&\equiv\operatorname{rem}_K(\ell_r)\pmod p,\\
Q_p&\equiv\operatorname{quo}_K(\ell_r)\pmod p,\\
I_p-\operatorname{rem}_K(\ell_r)
 &\equiv p\,\operatorname{rem}_K(S_p\bmod p)\pmod{p^2},\\
Q_p-\operatorname{quo}_K(\ell_r)
 &\equiv p\,\operatorname{quo}_K(S_p\bmod p)\pmod{p^2}.
\end{aligned}}
\tag{22}
$$
右端全部是 (13)、(19) 的有限有理多项式及固定四次除法，没有新增未知函数。

当 $r\ge4$（在当前素数范围即 $p\ge29$）时，
$\operatorname{quo}_K(\ell_r)$ 准确为 $r-4$ 次，首系数
$$
\frac{\lambda_r}{4-i}\equiv\frac1{(4-i)b_0}
$$
是单位。第一整商的多项式商准确为 $2r-4$ 次，首系数
$$
-\frac1{2(4-i)b_0^2}
$$
也是单位。这说明实际未投到十七挠值的部分本身为 primitive；
它不是因为没有算到而保留的可忽略尾项。
$p=13$ 时第一项次数小于四、商为零，但第一整商仍为二次、首系数仍为上述单位。

结合 R270 的固定挠值互反，(22) 还给明确的有限对数同余
$$
\boxed{
(p-\sigma_\pi)\ell_\beta+(1-p)\log_p\beta
\equiv
17p\,\operatorname{rem}_K(\ell_r)
+17p^2\,\operatorname{rem}_K(S_p\bmod p)
\pmod{p^3\mathcal B_p}.
}
\tag{23}
$$
该式包括平凡和全部三个非平凡四次角色。
它是从原 CM division 推得的**有限精度固定挠值公式**；
未对任何有限点公式取权导数。

## 5. 原首权下一位可进一步消去显式 Frobenius 多项式

下面给首权的一个完全有限有理表达，并解释为什么 (23) 中的 log 修正
不能独立替代原下一位。

由 R270 的真实 theta division，
$$
L_p(v)=-\log\Theta(v)+\frac1p\log\Theta(v_\pi).
$$
在次数至多 $r$ 内，$E$ 的 $p^{-1}v^r$ 项尚不能进入
$v_\pi=\pi^4v(E/R)^4$ 的相应系数。
故
$$
\boxed{
L_p(v)\equiv\ell_r(v)\pmod{(p^3,v^{r+1})}.
}
\tag{24}
$$
这里 $\ell_r$ 正是 $-\log\Theta$ 的前 $r$ 项；它们在 $\mathbb Q$ 中由 (13) 准确给出。
这比 (15) 的全圆盘同余强两阶，但只适用于所标的低次数，不能往高权免费延长。

定义有限多项式
$$
D_r(v)=\sum_{k=0}^{r}d_kv^k,\qquad
d_k=[v^k]\exp(p\ell_r(v)),
\tag{25}
$$
以及
$$
\bar E_r(v)=\frac{v^rD_r(1/v)}{d_r}.
\tag{26}
$$
因为 $d_r\equiv p\lambda_r\bmod p^2$，有 $v_p(d_r)=1$，
而 $\bar E_r(0)=1$；其 $v^r$ 系数的一个 $p$ 分母与原 $E$ 同型。

对三原源定义
$$
\boxed{
\bar B_i=
[v^r]\,
 a_i(v)\exp((p^2-68)\ell_r(v))\,\bar E_r(v)^{-p}.
}
\tag{27}
$$
则
$$
\boxed{
b_{i,p-1}\equiv\bar B_i\pmod{p^3},
\qquad i=A,B,H.
}
\tag{28}
$$
所以原完整中央零给出的第一必要条件准确化为
$$
\boxed{\bar B_A,\bar B_B,\bar B_H\in p^2\mathcal O.}
\tag{29}
$$
这里只是同一首权证书的实际有限表达；没有把它提升为完整导数的充分零条件。

**证明。** (24) 给
$$
R(v)=\exp(pL_p(v))
\equiv D_r(v)\pmod{(p^4,v^{r+1})}.
$$
于是 $d_r-\pi\in p^4\mathcal O$。
在低于 $r$ 的次数中，$E-\bar E_r\in p^3\mathcal O$；
最高 $v^r$ 项的差仅有 $p^2$，但三源的 $a_i(0)=0$，
该项根本不进入 (27) 的目标系数。
所以低次数的 $E^{-p}-\bar E_r^{-p}$ 至少为 $p^4$。
同时
$$
R^p\exp(-68L_p)
=\exp((p^2-68)L_p)
\equiv\exp((p^2-68)\ell_r)\pmod{(p^3,v^{r+1})}.
$$
R270(18) 在 $j=1$ 的第一个非中央修正属于 $p^3$；
将以上式子代入其 $B_{i,1}$，得到 (28)。
参考首权分母为单位，因此原中央零迫
$b_{i,p-1}\in p^2\mathcal O$，即 (29)。$\square$

(24) 还说明固定挠点余式和实际商在低次数中怎样相消：
虽然 (22) 的余式和商分别有真实 $p$ 一阶变化，
它们在 $L_p=I_p+KQ_p$ 的次数 $1,\ldots,r$ 中
合起来到 $p^3$ 才偏离 $\ell_r$。
只保挠值余式，会破坏原首权所需的这个精确相消。

当前可继续使用的完整系统是 (3)、(8)、(9)、(22) 和 R270(28)。
它已把第一 Frobenius 商层和固定根边界写实；
仍须从原三中央条件对更高的聚合或这些有限表达给出跨 $p$ 的非零输入。

