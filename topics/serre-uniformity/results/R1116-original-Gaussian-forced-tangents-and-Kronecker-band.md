# R1116：原 Gaussian forced 切向的完整 Kronecker 反对角来源

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

**已证明的范围。** 本篇把 R1071 原 Gaussian 全 forced 标签在 CM 中心的
coarse 一阶系数，逐个且保尺度地接到同一个原 Kronecker 核的有限反对角。
这使“所有这些切向同时为零”成为一个明确的奇偶半段缺失条件。
同时给出该同次项的真实 Fay norm 方程，完整保留全部较低同次项乘积。
本文没有证明这个缺失条件不可能，也不将一个边界单位替代指定半段非零。

## 1. 原模型、指数和有限核

保持 R1082、R1114 的原模型与微分：
$$
E_a:y^2=x^3+ax,\qquad
a\in\mathbf F_p^\times,\qquad
p=4k+3\ge41,\qquad \omega=dx/(2y).
\tag{1116.1}
$$
先在原 Gaussian CM lift 的 additive 参数 $t$ 中取
$\sigma'(0)=1$、$\zeta=\sigma'/\sigma$。原 eigenparameter $T$
与 $t$ 的精度按 R1071 §11、R1079 保留，不重新选 period。
记
$$
D=d/\omega,\qquad D\Psi=\delta\in\mathbf F_p^\times,\qquad
\beta_{\rm Car}=-\delta.
$$
原 R1082 已付 $D^{p-2}x=\Psi$ 及原短 carry
$$
\Psi(T)=Z(T)^p+\delta T+O(T^{p^2}),
\qquad
Z(T)=T^{-1}-\sum_{\substack{4\le d<p\\d\text{ 偶}}}G_dT^{d-1}.
\tag{1116.2}
$$
Gaussian 不允许的权项为零；不把整个含 $p$ 分母的 zeta series
直接约化。

定义真正的有限核源
$$
\mathscr K(t,u)=\frac{\sigma(t+u)}{\sigma(t)\sigma(u)}.
\tag{1116.3}
$$
它关于两个变量对称。除 $t^{-1}+u^{-1}$ 外，其形式展开在
$(t,u)=(0,0)$ 正规；两个坐标轴上的留数均为一。
Gaussian 规范 $\sigma(it)=i\sigma(t)$ 给
$$
\mathscr K(t,u)=t^{-1}+u^{-1}+\sum_{h\ge1}P_h(t,u),
\qquad \deg P_h=4h-1,
\tag{1116.4}
$$
其中 $P_h$ 为对称齐次多项式。本篇所需的最高项是 $P_k$，
总次数 $4k-1=p-4$。只需 $\sigma$ 至 $4k+1=p-2$ 次，
所有这些系数 $p$ 整；没有读取第一个不整高尾。

写
$$
P_k(t,u)=\sum_{s=0}^{4k-1}c_s\,t^{4k-1-s}u^s.
\tag{1116.5}
$$
则
$$
c_s=c_{4k-1-s},\qquad
c_0=c_{4k-1}=-G_{p-3}\ne0.
\tag{1116.6}
$$
最后的单位是 R1082 的
$G_{p-3}=2a/(5\delta^3)$。它目前只支付边界，不支付其它 $c_s$。

## 2. 带原 sigma 分母的 Appell 多项式

令
$$
\mathcal A(t,u)=
e^{-\zeta(t)u}\frac{\sigma(t+u)}{\sigma(t)\sigma(u)}.
$$
对每个 $r\ge0$，定义
$$
\mathcal C_r(X;x,y,a)
=r![u^{r-1}]\bigl(e^{Xu}\mathcal A(t,u)\bigr),
\qquad x=x(t),\quad y=y(t).
\tag{1116.7}
$$
$e^{-\zeta(t)u}$ 恰消去 $t$ 平移的准周期，
所以每个系数是原椭圆曲线上的椭圆函数。
它只在 $O$ 有极点，因而可按 $1,x^i,yx^i$ 写成多项式。
权为 $r$，且关于 $X$ 是首一 $r$ 次多项式。直接有
$$
\partial_X\mathcal C_r=r\mathcal C_{r-1},\qquad
\mathcal C_r(\zeta(t);x(t),y(t),a)=r![u^{r-1}]\mathscr K(t,u).
\tag{1116.8}
$$
这里 $\mathcal C_0=1$。前四项是
$$
\begin{aligned}
\mathcal C_1&=X,\\
\mathcal C_2&=X^2-x,\\
\mathcal C_3&=X^3-3xX-2y,\\
\mathcal C_4&=X^4-6xX^2-8yX-3x^2-\frac{12a}{5}.
\end{aligned}
\tag{1116.9}
$$
尤其
$$
\mathcal C_4(\zeta)=\frac{\sigma^{(4)}}{\sigma}-\frac{2a}{5}.
\tag{1116.10}
$$
这一个常数来自 $1/\sigma(u)$，不能只用
$\sigma^{(4)}/\sigma$ 代替完整原核。

本篇只用 $r\le2k-2=(p-7)/2$。
(1116.7) 的所有阶乘及所需 $G_d$ 均在 $d<p-1$ 的安全范围，
所以这些有限多项式可约化到特征 $p$。

## 3. 原有界 primitive 的统一恒等式，包括常数

对 $1\le r\le2k-2$，准确有
$$
\boxed{\quad
D^{p-r-1}x=
\frac{\mathcal C_r(\Psi;x^p,y^p,a^p)}
     {r!\delta^{r-1}}.
\quad}
\tag{1116.11}
$$
这里每个 $p$ 次方都属于原同一曲线；不是换一个 Frobenius 标架。

先证明导数与极界。右端记 $F_r$。
(1116.8) 及 $D(x^p)=D(y^p)=0$ 给
$D F_r=F_{r-1}$；$F_1=\Psi$ 是已付原身份。

在 $O$，用 (1116.2) 展开 Appell 多项式。有限负次部分准确为
$$
\mathcal C_r(\Psi;x^p,y^p,a^p)
=
\sum_{\nu=0}^r\binom r\nu(\delta T)^\nu
 \mathcal C_{r-\nu}(Z;x,y,a)^p
+\text{正次误差}.
\tag{1116.12}
$$
对 $s\ge2$，$\mathcal C_s(\zeta(t))$ 在 $t=0$ 正规：
这由 $\mathscr K(t,u)=t^{-1}+\zeta(u)+O(t)$ 直接给出。
只有 $s=1$ 的项有 $t^{-1}$，故 (1116.12) 唯一最高负次来自
$\nu=r-1$，极阶为 $p+1-r$。所示 $\Psi$ 的误差乘其它因子后，
最低次数至少
$$
p^2-p(r-1)=p(p-r+1)>0.
\tag{1116.13}
$$
所以 $F_r$ 只在 $O$ 有极，且极阶至多 $p+1-r$。

归纳已知上一阶时，
$F_r-D^{p-r-1}x$ 的 $D$ 导数为零。它是一个 $p$ 次幂函数，
且只可能在 $O$ 有低于 $2p$ 的极；
非恒定椭圆函数的最小极阶为二，因此该差只能是常数。
奇数 $r$ 时两边均为奇函数，这个常数为零。

还须付款偶数 $r$ 的常数，不能靠导数相同删除。
对 $4\le r\le2k-2$ 偶数，R1075 的同权证明给一般反射式
$$
G_{p+1-r}^{\,p}
=(r-1)!\,\beta_{\rm Car}^{\,p-r}G_r.
\tag{1116.14}
$$
为使本篇量词自足，这一步的完整来源为
$$
\mathcal T^{p-r}\mathcal E_r
 =H^{p+1-r}\mathcal E_{p+1-r}
  -\mathcal E_{p+1-r}^{\,p}.
$$
逐个除数换元及 $p$ 倍指标的 Frobenius 项，和 R1075 §1 完全相同；
两边实际权均为 $p(p+1-r)$。在 $H=0$ 处，
$\prod_{a=r}^{p-1}a=-1/(r-1)!$；
再用 $G_d=2\mathcal E_d/(d-1)!$ 和
$(p-r)!=(r-1)!^{-1}$，即得 (1116.14)。
所有 Eisenstein 常数和阶乘均 $p$ 整，所读权小于 $p-1$。

原 $\mathbf F_p$ 参考中 $G_r,\delta$ 都被 Frobenius 固定，
$\beta_{\rm Car}=-\delta$，故
$$
\frac{G_{p+1-r}}{(r-1)!}=-\delta^{1-r}G_r.
\tag{1116.15}
$$
左边是 $D^{p-r-1}x$ 的常数项：Wilson 给
$(p-r-1)!(p-r)=1/(r-1)!$。
右边恰是 $F_r$ 的常数项，因为
$\mathcal C_r(\zeta)(0)=-r!G_r$。
$r=2$ 时两个常数都为零：前者用 Gaussian
$G_{p-1}=0$，后者由 $\mathcal C_2(\zeta)=\zeta^2-x$ 的零常数。
因此 (1116.11) 包括全部常数，证明完成。

## 4. 实际高 Hurwitz 系数的有限反对角

对原 forced 指标
$$
1\le j\le k-1,\qquad r=2j,\qquad
R=p-1-r,\qquad \chi_j=\omega^R,
$$
令
$$
d_j=(p+1)R-2(p-1)
=p(p-r-2)-r+1.
\tag{1116.16}
$$
它正是 R1071 的 fine $i=2$ 项，并非任意选的同权指数。

将 (1116.11) 的 $T^{p(p-r-3)}$ 系数逐边读取。
左边的下降阶乘与原 $x$ 系数准确给
$$
(d_j-1)(d_j-2)_{p-r-1}G_{d_j}
=\frac{G_{d_j}}{(r-1)!}.
$$
右边 (1116.12) 中只有 $\nu=0$ 的项能贡献这个 $p$ 倍指数：
其余项的次数为 $\nu\bmod p$，而 $1\le\nu\le r<p$。
(1116.13) 比所读次数高 $4p$，所以整个短 carry 的误差不能回流。
得到
$$
\boxed{\quad
G_{d_j}=
\frac{[T^{p-r-3}]\mathcal C_r(Z;x,y,a)}
     {r\delta^{r-1}}
=\frac{(r-1)!}{\delta^{r-1}}\,c_{r-1}.
\quad}
\tag{1116.17}
$$
系数在 $\mathbf F_p$ 上，才在此去掉其实际 $p$ 次方。

这里 $\mathcal C_r$ 的单项式权为 $r$；
要读 $T^{p-r-3}$，各 $Z,x,y$ 输入只需到总权 $p-3$。
所以用到的 zeta/Hurwitz 系数全部在 $d<p$ 的安全范围。
同一原 $t(T)=T+O(T^{p^2})$ 也不会改变所读的 $G_{d_j}$：
其 $x$ 变化从 $T^{p^2-3}$ 起，而
$d_j-2<p^2-3$。对有限不变导数的误差同样高于所读次数。
没有约化一条未经支付的完整 logarithm 或 zeta series。

$j=1$ 时，(1116.17) 是 R1082 的原
$G_{p^2-4p-1}=\mathcal H_p/(2\delta)$。
$j=2$ 时，它读
$$
G_{p^2-6p-3}
=\frac1{4\delta^3}
 [T^{p-7}]\left(\zeta^4-6x\zeta^2-8y\zeta-3x^2\right).
\tag{1116.18}
$$
此处可以不写 (1116.9) 的常数，只因为 $p-7>0$；
不能据此回到 §3 删除 primitive 的常数。

## 5. 原 coarse 首项、regularizer 与 good mask

R1071 §5 中 fine $i=2$ 项为
$$
-(p+1)\beta_0^{d_j}\lambda^2 A_{d_j}
                  \frac{d_j-1}{2}.
$$
当前 $\mathbf F_p$ Gaussian reference 的原 division identity，
在 $d_j<p^2-1$ 的安全精度给
$$
A_{d_j}=-(c^{d_j}-c^2)G_{d_j}
       =\kappa_{\chi_j}G_{d_j}.
\tag{1116.19}
$$
因为 $d_j\equiv-2r\bmod p-1$，而
$\kappa_{\chi_j}=c^2-c^{-2r}$。
原 $c$、full-level basis 和 Weil root 都保持 R1071 的同一选择。

$\mu_4$ 使完整 fine polynomial 为偶函数。
写原 coarse 坐标 $z=t_*^2$。若角色 $\chi_j$ Bernoulli-good，
除以同一圆单位系数 $b_{\chi_j}$ 后，准确得到
$$
\boxed{\quad
[z]\bigl(c_{\chi_j,s}(z)-c_{\chi_j,s}(0)\bigr)
=
-\frac{r!}{4b_{\chi_j}\delta^{r-1}}\,
       \beta_0^{d_j}\lambda^2\,c_{r-1}.
\quad}
\tag{1116.20}
$$
因此该实际首项非零当且仅当指定 $c_{r-1}$ 非零。
在 R1071 §12 已付 $\beta_0=1,\lambda=-1$ 的 branch，
外部两因子的乘积为一；$b_{\chi_j}$ 仍保真实 Weil 相位。

未除圆单位时的原 local-log 首项则为
$$
\frac{r!\kappa_{\chi_j}}{2\delta^{r-1}}\,
       \beta_0^{d_j}\lambda^2\,c_{r-1}.
\tag{1116.21}
$$
它不要求该角色 good。反过来，不能因为 (1116.21) 有定义，
就对一个不 good 的角色除以可能为零的 $b_{\chi_j}$。

所以原全部 forced-good 首项同时为零，准确等价于
$$
c_{2j-1}=0
\quad\text{对所有 }1\le j\le k-1
 \text{ 且 }p\nmid B_{p-1-2j}.
\tag{1116.22}
$$
不能删除这个 mask。若另有全部 forced 的首项为零
（例如全部这些角色 good 并满足 (1116.22)），则得到完整条件
$$
c_1=c_3=\cdots=c_{2k-3}=0,\qquad
c_{2k+2}=c_{2k+4}=\cdots=c_{4k-2}=0.
\tag{1116.23}
$$
第二行由原核对称性给出。它是一个具体的奇偶半段缺失，
不是任意重选基后的零模式。

## 6. 真实 Fay norm 与完整较低乘积

本规范的准确加法式是
$$
\boxed{\qquad
\mathscr K(t,u)\mathscr K(t,-u)=x(t)-x(u).
\qquad}
\tag{1116.24}
$$
符号由首项
$(t^{-1}+u^{-1})(t^{-1}-u^{-1})=t^{-2}-u^{-2}$
固定。可直接用原 sigma 加法式证明；
在同一椭圆函数上的 divisor 和此首项也唯一确定该式。
不能改为相反的 $x(u)-x(t)$。

把 $P_k$ 按 $u$ 的奇偶拆为 $P_k^{\rm ev}+P_k^{\rm odd}$。
取 (1116.24) 的总次数 $4k-2=p-5$，完整得到
$$
\begin{aligned}
\frac{2P_k^{\rm ev}(t,u)}t
-\frac{2P_k^{\rm odd}(t,u)}u
&+\sum_{h=1}^{k-1}
       P_h(t,u)P_{k-h}(t,-u)\\
&=(4k-1)G_{p-3}
       \left(t^{4k-2}-u^{4k-2}\right).
\end{aligned}
\tag{1116.25}
$$
左边两个商均为多项式：齐次次数为奇数，$u$ 偶项必含 $t$，
$u$ 奇项必含 $u$。求和包含全部较低齐次项，没有假设它们抵消。

右侧的 $G_{p-3}$ 是原单位；但它并不单独排除
(1116.22) 或 (1116.23)。
后继若用二同源、其它 Fay 式或有限 theta pairing，
必须同时结算 (1116.25) 的完整较低乘积。
R1114 的
$5\mathcal H_p+(8a^2/45)\mathcal K_p=16G_{p-3}$
仍是同一原 Gaussian 上的已付旁约束；
本篇没有把 $\mathcal K_p$ 偷换成某个 $c_{2j-1}$。

本篇只完成实际统一来源、全部 primitive 常数、
反对角/首项尺度和真实缺失条件。未证明任一指定高系数单位，
未证明 full forced-good 向量必非零，未将 center 首项非零自动提升为
整个 coarse 标签注入。原 bare $r=2,8$、$f_N/e$、
短 $\eta_k,\nu_k$ 也没有因此关闭。无数学程序执行。

来源：R1071 §§5–6、11–16 的原 source/Weil/regularizer；
R1075 的完整同权 theta 证明（本篇 §3 明列其所需一般偶权版本）；
R1079 的原短 $\Psi$ carry；R1082 的 Gaussian 标架、$\delta$ 与
$G_{p-3}$；R1114 的同一原二挠及 $1+i$ 归一。


## 7. 完整实际 V 的同一反对角：全部低角色也保原尺度

本节扩大第3–5节的可读范围，不修改前文对 forced 来源的证明。
仍固定 $p=4k+3\ge41$ 及同一个原 Gaussian frame。

### 7.1 原 Appell primitive 的全短范围

准确的有限身份其实在整个范围
$$
\boxed{\quad
D^{p-r-1}x=
\frac{\mathcal C_r(\Psi;x^p,y^p,a^p)}
 {r!\delta^{r-1}},
\qquad 1\le r\le p-3,
\quad}
\tag{1116.26}
$$
成立。为避免只作形式外推，逐项核对扩大后的边界。

首先 $\mathcal C_r$ 只需 $\sigma(u)$ 至 $u^{r+1}$，
而 $r+1\le p-2$；所需阶乘与 Hurwitz 权均严格低于 $p-1$。
所以原 Appell 定义仍 $p$ 整。
在原 $T=0$ 展开，只有
$\mathcal C_1(Z)$ 有负次；其余 $\mathcal C_s(Z)$，$s\ge2$，
都正规到本次所需精度。
(1116.12) 的唯一最高负项仍是 $\nu=r-1$，
故右端极阶至多 $p+1-r<2p$。
截断 zeta 与原 $\Psi$ 两种误差的最低次数仍至少
$p(p-r+1)>0$。这里没有让大 $r$ 的 Laurent 极点吞掉误差。

原 $D F_r=F_{r-1}$ 递推从 $F_1=\Psi$ 开始，因而两个原 primitive
之差是一个 $p$ 次幂函数，且只在 $O$ 有严格低于 $2p$ 的极。
椭圆曲线非恒定函数的最小极阶为二，所以差为常数。
奇 $r$ 由奇性定零。
偶 $4\le r\le p-3$ 时，纯 G 反射 (1116.14) 仍合法：
两侧权 $r,p+1-r$ 均在 $[4,p-3]$，全部 Eisenstein 常数和阶乘 $p$ 整。
故左右常数仍准确为
$$
\frac{G_{p+1-r}}{(r-1)!}
 =-\delta^{1-r}G_r.
$$
$r=2$ 仍由 Gaussian $G_{p-1}=0$ 及 $\mathcal C_2$ 零常数支付。
这给出 (1116.26) 的全部常数，不以导数相同略去它们。

### 7.2 任一实际偶角色的 i=2 源

令
$$
2\le R\le p-3,\quad R\text{ 偶},\qquad
r=p-1-R,\qquad
d_R=(p+1)R-2(p-1)=p(R-2)+R+2.
\tag{1116.27}
$$
$r$ 为偶数且 $2\le r\le p-3$，$d_R\ge4$。
R1071 的真实 profile 对任何实际 $V_{\omega^R}\ne0$ 均适用；
其 $i=2$ 系数合法，二项式为
$(d_R-1)/2\equiv(R+1)/2\ne0$。
本节不使用一个不在 $V$ 中的 ambient 角色作标签。

取 (1116.26) 的 $T^{p(R-2)}$ 系数。
左侧是 $D^R x$，原 Hurwitz 系数乘子为
$$
(d_R-1)(d_R-2)_R\equiv(R+1)!
 =\frac1{(r-1)!}\pmod p.
$$
右侧只有 (1116.12) 的 $\nu=0$ 能给这个 $p$ 倍指数。
原 $\Psi$ 误差最低次 $p(R+2)$ 与目标 $p(R-2)$ 恰相差 $4p$。

原 additive $t$ 和 eigen-$T$ 也没有额外混合：
$t(T)=T+O(T^{p^2})$，$x$ 的误差从 $T^{p^2-3}$ 开始；
对 $D^R x$，所涉导数或参数误差最早在 $T^{p^2-R-3}$。
它与目标之差为
$$
p^2-R-3-p(R-2)
=4p+(p+1)(p-3-R)\ge4p.
$$
同时 $d_R-2<p^2-3$。
所以扩大范围仍没有读取第一个未付的高尾。

得到同一个原反对角的准确公式
$$
\boxed{\quad
G_{d_R}
 =\frac{(r-1)!}{\delta^{r-1}}\,c_{r-1}
 =\frac{(r-1)!}{\delta^{r-1}}\,c_{R-2}.
\quad}
\tag{1116.28}
$$
最后一步只是原 $P_k$ 的对称性，因为
$(r-1)+(R-2)=p-4$。
输入的有限总权始终是 $p-3$，并没有随 $r$ 增大而读取不整 Hurwitz 项。

### 7.3 全部实际 good 首项及 R=2 的原尺度复核

若该实际角色 Bernoulli-good，仍用同一个原 $b_{\omega^R}$，
以及 R1071 的 $\beta_0,\lambda$。
原 division identity 是
$$
A_{d_R}=\kappa_{\omega^R}G_{d_R},
$$
因为 $d_R\equiv2R\pmod{p-1}$。
$\kappa_{\omega^R}$ 对全部实际 $V$ 非零，已由 R1070 §10 支付。
在 Gaussian coarse 参数 $z=t_*^2$ 上，准确有
$$
\boxed{\quad
[z]\bigl(c_{\omega^R,s}(z)-c_{\omega^R,s}(0)\bigr)
 =-\frac{r!}{4b_{\omega^R}\delta^{r-1}}\,
   \beta_0^{d_R}\lambda^2 c_{r-1}.
\quad}
\tag{1116.29}
$$
这是完整多项式的一阶系数；一般 $R$ 的更高 coarse 项仍保留，
不把所有角色的 profile 误称为 affine。
$R=2$ 与第一 forced $R=p-3$ 是已付 degree 界中的特殊 affine 情形。

特别 $R=2$ 时，$r=p-3$、$d_R=4$。
由 Wilson
$$
(p-4)!=1/6,\qquad (p-3)!=-1/2,
$$
以及 $\delta\in\mathbf F_p^\times$、$c_{p-4}=-G_{p-3}$，
(1116.28) 给
$$
G_4=-\frac{\delta^3}{6}G_{p-3}=-\frac a{15}.
$$
(1116.29) 因而严格成为
$$
-\frac{\delta^3G_{p-3}}{8b_{\omega^2}}\,
 \beta_0^4\lambda^2
=-\frac{a\,\beta_0^4\lambda^2}{20b_{\omega^2}},
\tag{1116.30}
$$
与 R1127 的实际 affine unit 逐因子相同。
这里没有重算一个有限素数或把边界单位换成别的同权源。

### 7.4 原全 good mask 及高低配对的确切位置

令
$$
\mathcal G_p=
\{\,R:\ 2\le R\le p-3,\ R\text{ 偶},\
       V_{\omega^R}\ne0,\ p\nmid B_R\,\}.
$$
全部实际 good 标签在 Gaussian 中心的一阶同时为零，准确等价于
$$
c_{p-R-2}=c_{R-2}=0
\qquad(R\in\mathcal G_p).
\tag{1116.31}
$$
这是同一个 $P_k$ 的一组指定系数条件，
没有把 bad 角色的全局像擅自设为零。

R1128 的互不相交高低配对在此有具体位置。
对奇数 $j$、$1\le j\le k-1$，令
$$
R_{\rm hi}=p-1-2j,\qquad R_{\rm lo}=j+1.
$$
前者是原 forced 角色；后者小于 $(p-1)/2$。
其原出现判据是
$$
V_{\omega^{R_{\rm lo}}}\ne0
 \quad\Longleftrightarrow\quad p\mid B_{R_{\rm hi}}.
$$
所以在假设 (1116.31) 下：

- 若 $p\nmid B_{R_{\rm hi}}$，必有原奇下标
  $c_{2j-1}=0$。
- 若 $p\mid B_{R_{\rm hi}}$ 而 $p\nmid B_{j+1}$，
  必有原偶下标 $c_{j-1}=0$。
- 若这两个 Bernoulli 都 bad，本配对没有提供可除圆单位的约束；
  两者均不能被省略。

R1128 已严格下界这些实际 good 角色的总数；
本节把它们的 Gaussian 首项全部定位到原完整核。
但不同系数位置及其原来源得到确认，不等于这些指定值已证非零。
二同源分布和 (1116.25) 的全部低乘积仍在；
本节没有排除 (1116.31)，也没有把原 bare、primitive/Legendre 或
$\eta_k,\nu_k$ 换成这个 mask。

本附节仅为纸面全范围延拓及原尺度核对；无数学程序执行。

root 已独立纸核 §7 全短 primitive 的常数、两种参数误差的至少4p间隔、实际全部角色的 regularizer、R=2 与 R1127 的逐因子一致及双支 good mask。旧 §§1–6 逐字保留。


## 8. 原 Gaussian 完整 profile 的有限 Kronecker gauge

本节读取整个 centered profile，而不只上一节的 coarse 首项。
仍保原 $\mathbf F_p$ Gaussian reference、$\delta$、$\beta_0$、
$\lambda$ 和实际 Weil/circular-unit 系数 $b_{\omega^R}$。
下文的两个核变量记为 $T,U$；它们是第1节同一个 additive
formal parameter 的两份，不是新的 deformation 坐标。
原 fine deformation 变量另记为 $t_*$，coarse 变量为 $z=t_*^2$。

### 8.1 每一个合法非零 fine 项都来自有限低 band

固定实际 $V_{\omega^R}\ne0$，$R$ 为偶数、$2\le R\le p-3$。
R1071 §15 的 Lucas 消去与 Gaussian $\mu_4$ 共同说明：
全部可能非零的非 constant 项恰在
$$
i=2h,\qquad 2\le i\le\min(R,p-R-1).
$$
这是一个允许范围，未声称范围内所有系数非零。置
$$
r=p+1-R-i,\qquad
d=(p+1)R-i(p-1)=p(R-i)+R+i.
\tag{1116.32}
$$
则 $r$ 为偶数，$2\le r\le p-3$；$R-i\ge0$，
$r-1=p-R-i\ge1$，所有阶乘指标均小于 $p$。

使用 (1116.26)，取 $D^{R+i-2}x$ 的
$T^{p(R-i)}$ 系数。左侧原 Hurwitz 乘子准确为
$$
(d-1)(d-2)_{R+i-2}
\equiv(R+i-1)!=\frac1{(r-1)!}\pmod p.
$$
最后等号用 $R+i-1$ 为奇数及 Wilson，
并非在可能含 $p$ 的下降阶乘上作约分。

右侧 (1116.12) 仍只有 $\nu=0$ 项能给一个 $p$ 倍指数。
原 $\Psi$ 误差最低次为 $p(R+i)$，
比目标高 $2pi\ge4p$。
原参数或导数误差最早在 $T^{p^2-R-i-1}$，
与目标的差是
$$
p^2-R-i-1-p(R-i)=p^2-1-d\ge4p.
$$
这里用 $R\le p-3$、$i\ge2$，故
$d\le p^2-4p-1$。
因此这些读取均由已付原短 carry 支持。

由 (1116.8) 得完整高系数身份
$$
\boxed{\quad
G_d=\frac{(r-1)!}{\delta^{r-1}}\,
       [T^{R-i}U^{r-1}]\mathscr K(T,U).
\quad}
\tag{1116.33}
$$
所读核的总次数为 $p-2i=4(k+1-h)-1$，
恰是原 $P_{k+1-h}$。
所需 Hurwitz 总权 $p+1-2i\le p-3$，
没有读取未知的总次数 $p$ 的下一 band。
系数均在当前 $\mathbf F_p$ reference 上，
所以此处去掉实际 $p$ 次方合法。

### 8.2 全部原 factorial、regularizer 和相位

R1071 (1071.20)、(1071.25) 中，
原 $i$ 次系数为
$$
-\frac{m(p+1)}{\kappa_{\omega^R}b_{\omega^R}}\,
 \beta_0^d\lambda^i A_d
 \frac{\binom{d-1}{i-1}}i.
$$
在这里 $d\equiv2R\bmod p-1$，
同一个原 division identity 给 $A_d=\kappa_{\omega^R}G_d$。
实际 $\kappa_{\omega^R}$ 为单位；不引入其它 smoothing constant。
又
$$
-m(p+1)=\frac12,\qquad
\frac1i\binom{d-1}{i-1}
 =\frac{(R+i-1)!}{i!\,R!}\quad\text{in }\mathbf F_p.
$$
与 (1116.33) 的 factorial 正好全部抵消，得到
$$
\boxed{\quad
[t_*^i]\bigl(c_{\omega^R,s}(t_*)-c_{\omega^R,s}(0)\bigr)
 =
 \frac{\beta_0^d\lambda^i}
      {2b_{\omega^R}R!\,i!\,\delta^{r-1}}\,
 [T^{R-i}U^{p-R-i}]\mathscr K(T,U).
\quad}
\tag{1116.34}
$$
用核的对称性可以交换两个显示指数。
本式对原 good 角色使用 $b_{\omega^R}^{-1}$；
并未对一个 bad 角色作不存在的 global-unit 坐标归一。

令
$$
w=\delta\lambda\beta_0^{\,1-p}t_*,
\qquad
N_R=\frac{(\beta_0^{p+1})^R\delta^{R-1}}
           {2b_{\omega^R}R!}.
\tag{1116.35}
$$
所有量都来自同一原 full-level/Weil 标记。
这里不假设 $\beta_0$ 或 $\lambda$ 属于 $\mathbf F_p$，
也不把 $\beta_0^{p+1}$ 私自改为一。
只对已固定的 $\delta\in\mathbf F_p^\times$ 用
$\delta^{p-1}=1$：
$$
\beta_0^d\lambda^i\delta^{1-r}
=(\beta_0^{p+1})^R\delta^{R-1}
       (\delta\lambda\beta_0^{1-p})^i.
$$
因此 (1116.35) 保留了完整原尺度。

### 8.3 有限 exponential 的准确意义及唯一 principal 角色

定义同一个有限核
$$
\mathscr K_{\le p-4}(T,U)
 =T^{-1}+U^{-1}+\sum_{j=1}^kP_j(T,U).
$$
以下的 $e^{wTU}$ 只需指数 $i\le(p+1)/2<p$，
即读有限和 $\sum_{i=0}^{p-1}(wTU)^i/i!$；
没有在特征 $p$ 中使用无限 exponential 的未定义分母。

令 $\mathscr M_w(T,U)$ 是
$(e^{wTU}-1)\mathscr K_{\le p-4}(T,U)$
的总次数 $p$ 部分。其完整表达为
$$
\begin{aligned}
\mathscr M_w(T,U)
={}&\sum_{h=1}^{k}
 \frac{w^{2h}(TU)^{2h}}{(2h)!}\,P_{k+1-h}(T,U)\\
&+\frac{w^{2k+2}(TU)^{2k+2}}{(2k+2)!}
       (T^{-1}+U^{-1}).
\end{aligned}
\tag{1116.36}
$$
这是真正的对称齐次多项式，次数为 $p$，且为 $w^2$ 的多项式。
第一行保留全部原低 band；第二行保留两个 principal terms。

对偶数 $R$ 读取 $[T^{p-R}U^R]$ 时，
第二行仅能落在
$$
R=2k+2=(p+1)/2=m+1.
$$
R1070 (1070.40) 已按原 Stickelberger 格证明
$V_{\omega^{m+1}}=0$：
其原 Jacobi 和 valuation 为 $+1$，
而 $B_{2,\omega^{-2}}$ valuation 为 $-1$，
二者乘积 $S_{\omega^{-(m+1)}}$ 是单位。
所以这次 principal 项消失由真实角色缺席支付，
不是形式地忽略极部，也不是因为该角色不在某个 chosen mask 中。

### 8.4 整个原 centered profile 的单一核公式

合并 (1116.34)–(1116.36)，对每个实际 good 角色准确有
$$
\boxed{\quad
c_{\omega^R,s}(t_*)-c_{\omega^R,s}(0)
 =N_R[T^{p-R}U^R]\mathscr M_w(T,U)
 =N_R[T^{p-R}U^R]
       (e^{wTU}-1)\mathscr K(T,U).
\quad}
\tag{1116.37}
$$
最后一个写法总是按 §8.3 的有限读取解释。
因 $e^{wTU}-1$ 无 constant term，
第一个未付的总次数 $p$ 的 $\mathscr K$ band 从未被使用。
更高 band 也不能回流。
对 $i=2$，本式逐因子恢复 (1116.29)；
对 $R=2$，恢复 R1127 的原 affine unit。

这是完整原 profile，不是任意同权替代源。
其右边只含 $w^2$，因而与原 $z=t_*^2$ coarse descent 相容。
R1071 的两条 Gaussian twist line 仍按同一
$\beta_0,\lambda,b_{\omega^R}$ 一起运输；
没有只保一个固定 fine line 的平方像。

### 8.5 同一 sigma 的形式 gauge 与完整 Fay 约束

在 characteristic zero 中置
$$
\sigma_w(t)=e^{wt^2/2}\sigma(t).
$$
直接有
$$
\frac{\sigma_w(T+U)}{\sigma_w(T)\sigma_w(U)}
 =e^{wTU}\mathscr K(T,U)=:\mathscr K_w(T,U).
\tag{1116.38}
$$
所以 (1116.37) 是同一个原 sigma 的形式 gauge 差。
这只说明所读取函数的精确身份；
不声称原非恒定椭圆 deformation family 与固定曲线全局同构。
约化时仍只取 §8.3 的安全有限部分。

同一 gauge 满足
$$
\mathscr K_w(T,U)\mathscr K_w(T,-U)=x(T)-x(U),
\qquad
\partial_w\mathscr K_w=TU\,\mathscr K_w.
\tag{1116.39}
$$
第一式中的两个 exponential 准确抵消，符号仍由
$T^{-2}-U^{-2}$ 定准。

也可保留原 norm-two note 的全部相位。
为免与 (1116.35) 的 source 单位 $\lambda$ 混淆，
这里把 $1+i$ 另记为 $\alpha$，$\bar\alpha=1-i$。
令 $\mathscr K_{Q,w}=e^{wTU}\mathscr K_Q$，$Q=(0,0)$。
原线性及乘法分布逐项乘上 exponential 后成为
$$
\begin{aligned}
\alpha\,\mathscr K_w(\alpha T,U)
 &=\mathscr K_{iw}(T,\bar\alpha U)
   +\mathscr K_{Q,iw}(T,\bar\alpha U),\\
\alpha\sqrt{x(U)}\,\mathscr K_w(\alpha T,\alpha U)
 &=\mathscr K_{iw}(T,U)\mathscr K_{Q,iw}(T,U).
\end{aligned}
\tag{1116.40}
$$
这里 $i\bar\alpha=\alpha$、$\alpha^2=2i$ 支付两个指数；
$\mathscr K_Q$ 仍包含原
$e^{-\zeta(Q)U}$ 和全部 square-root lower convolutions。
先在 characteristic zero 比较，再对 centered finite part 约化。
没有从乘法分布删去低 band 的乘积。

### 8.6 精确后继问题

(1116.37) 将所有实际 good 坐标放到一个固定核的有限 gauge 中。
特别两个原 coarse 参数具有相同完整 good 标签，
等价于该同一 $\mathscr M_w-\mathscr M_{w'}$
在实际 $\mathcal G_p$ 指定位置的系数全为零；
相差 sign 的 fine 参数本来代表同一 coarse 参数，必须先识别。

目前没有证明这些指定系数不能同时消失，
也未从 (1116.39)–(1116.40) 中删除全部较低乘积。
R1128 的角色维数下界仍只给实际可用位置的数量。
本节不把 complete profile、coarse 首项、原 bare、$f_N/e$
或短 $\eta_k,\nu_k$ 互相替换。
全文无数学程序执行。

root 已全文独核 §8，回读 R1071 原 (1071.20)/(1071.25)/§15 及 R1070 (1070.40)：全部合法 i、Wilson/δ/circular-unit 因子、真实非Fp source相位、唯一principal缺席、有限exp和二同源w→iw均一致。无数学程序执行。


## 9. 原完整 gauge 的 Ramanujan 迭代与有限共纤维式

本节继续 (1116.37) 的同一个原核与全部 source 单位。
它把两个实际参数的完整读数之差化为一个有界单变量系数，
并明确第一个 $p$ 次迭代的真实边界。
以下没有从某两个点的取值相等，推断其横向导数相等；
也没有删除 actual-good mask。

### 9.1 真正的三变量 Ramanujan 向量场

先在一般短模型 $y^2=x^3+ax+b$ 上保留独立 gauge 变量 $w$。
R1129 已从原 sigma 热式证明
$$
\partial\mathscr K
 =\left(\partial_T\partial_U-\frac a3TU\right)\mathscr K,
\qquad
\partial=6b\,\partial_a-\frac{4a^2}{3}\,\partial_b.
$$
对 $\mathscr K_w=e^{wTU}\mathscr K$，逐项共轭给
$$
\partial\mathscr K_w
=\left[
 \partial_T\partial_U
 -w(T\partial_T+U\partial_U+1)
 +(w^2-a/3)TU
 \right]\mathscr K_w.
\tag{1116.41}
$$
这里 $w$ 在 $\partial$ 下保持不变；它与下面完整三变量向量场的
第三个分量不可混淆。

固定偶数 $v\ge4$，定义
$$
f_n^{v,w}
 =[T^{v+n-1}U^n]\mathscr K_w,\qquad n\ge0.
$$
因 $v\ge4$，principal 项不改变 $f_0^{v,w}=-G_v$。
又有
$$
\partial_w f_n^{v,w}=f_{n-1}^{v,w},\qquad f_{-1}^{v,w}=0.
$$
从 (1116.41) 读取系数，完整得到
$$
(v+n)(n+1)f_{n+1}^{v,w}
=\partial f_n^{v,w}
 +(v+2n)w f_n^{v,w}
 +(a/3-w^2)\partial_w f_n^{v,w}.
\tag{1116.42}
$$
给 $a,b,w$ 分别赋权 $4,6,2$，则 $f_n^{v,w}$ 权为 $v+2n$。
因此 (1116.42) 的右端准确是
$$
\Theta f_n^{v,w},\qquad
\boxed{\quad
\Theta=(4wa+6b)\partial_a
 +(6wb-4a^2/3)\partial_b
 +(w^2+a/3)\partial_w.
\quad}
\tag{1116.43}
$$
归纳得到
$$
\boxed{\qquad
f_n^{v,w}=-\frac{\Theta^nG_v}{n!(v)_n}.
\qquad}
\tag{1116.44}
$$
这是原完整核的身份，不是只比较一个最高项。
其中 $(v)_n=v(v+1)\cdots(v+n-1)$。

对实际 $R\in\mathcal G_p$，采用 R1129 (1129.12) 的
$$
(v,s)=
\begin{cases}
(p+1-2R,R),&R<(p-1)/2,\\
(2R-p+1,p-R),&R>(p+1)/2.
\end{cases}
$$
于是 $v=p+1-2s$、$4\le v\le p-3$、$s<p$，
且 $(v)_s$ 最大因子为 $p-s<p$。
所以 (1116.44) 对 $0\le n\le s$ 的全部分母是 $p$-单位。
输入 $G_v$ 是 R1129 已付的 $p$ 整非零权多项式。

这还说明该指定 interior coefficient $f_s^{v,w}$ 本身 $p$ 整，
尽管本篇仍不约化整条未截断的最高核 band。
当读取 centered difference 时，(1116.37) 已保证只用权至 $p-3$
的低 band；下文再次逐项检查这个精度。

### 9.2 只至 p−1 阶的精确 Möbius 时间变换

固定 $(a,b)$，令
$$
(a_0(u),b_0(u),w_0(u))
$$
是 (1116.43) 从 $(a,b,0)$ 出发的有限 Taylor 解。
在特征 $p$ 中，这句话只指模 $u^p$ 的 jet：
其 $u^n$ 系数为 $\Theta^n(a,b,w)|_{w=0}/n!$，$n<p$。
不使用 $1/p!$，也不假设这个有限解已延拓成整条加法群作用。

初始 gauge 改为 $\eta$ 时，准确的有限变换为
$$
\begin{aligned}
a_\eta(t)
 &=(1-\eta t)^{-4}
      a_0\!\left(\frac{t}{1-\eta t}\right),\\
b_\eta(t)
 &=(1-\eta t)^{-6}
      b_0\!\left(\frac{t}{1-\eta t}\right),\\
w_\eta(t)
 &=\frac{\eta}{1-\eta t}
  +(1-\eta t)^{-2}
      w_0\!\left(\frac{t}{1-\eta t}\right)
 \pmod {t^p}.
\end{aligned}
\tag{1116.45}
$$
证明可先在特征零直接代入三个微分方程：
变换后初值为 $(a,b,\eta)$，
且 $d(t/(1-\eta t))/dt=(1-\eta t)^{-2}$。
逐系数唯一性只需除以 $1,\ldots,p-1$，
故原式的每个所用 jet 都可准确约化，得到 (1116.45)。

对权 $v$ 的原 $G_v$，置
$$
\mathcal E_v(u)=G_v(a_0(u),b_0(u)).
$$
同权性给
$$
G_v(a_\eta(t),b_\eta(t))
 =(1-\eta t)^{-v}
       \mathcal E_v\!\left(\frac{t}{1-\eta t}\right)
 \pmod {t^p}.
$$
用实际换元 $t=u/(1+\eta u)$ 取 $t^s$ 系数：
$$
[t^s]G_v(a_\eta(t),b_\eta(t))
 =[u^s](1+\eta u)^{v+s-1}\mathcal E_v(u).
$$
当 $v=p+1-2s$ 时，$v+s-1=p-s$。
因 $s<p$，$(1+\eta u)^p=1+\eta^pu^p$ 的第二项不参与读取，
所以准确得到
$$
\boxed{\quad
f_s^{v,\eta}(a,b)
=-\frac1{(v)_s}
 [u^s](1+\eta u)^{-s}\mathcal E_v(u).
\quad}
\tag{1116.46}
$$
这里 $(1+\eta u)^{-s}$ 只展开到 $u^s$；
所有负二项式系数都在本范围内有定义。

### 9.3 两个原参数的完整共同纤维条件

现在回到原 Gaussian $b=0$。
令
$$
\kappa_*=\delta\lambda\beta_0^{1-p},\qquad
w=\kappa_*t_*,\qquad w'=\kappa_*t_*',
$$
并保持 (1116.35) 的原 $N_R$。
核对称性及 (1116.37)、(1116.46) 给出
$$
\boxed{\quad
\Pi_R(t_*^2)-\Pi_R(t_*'^2)
=-\frac{N_R}{(v)_s}
 [u^s]\left\{(1+wu)^{-s}-(1+w'u)^{-s}\right\}
      \mathcal E_v(u).
\quad}
\tag{1116.47}
$$
同一条 Gaussian twist line 上的两个 coarse 参数共纤维，
准确等价于 (1116.47) 对全部 $R\in\mathcal G_p$ 为零。
对另一 twist line 应按原 source 一起运输，
不能私自固定 $\beta_0,\lambda$ 或合并两个不同的 Weil frame。

本次系数的安全范围还可以直接从有限流看清。
从 $(a,0,0)$ 出发，$a_0(u)$ 是偶 jet，
$b_0(u),w_0(u)$ 是奇 jet；
由 $G_v$ 同权性，$\mathcal E_v(u)$ 只含与 $s$ 同 parity 的次数。
所以 (1116.47) 中只有偶次 $i\ge2$ 的 gauge 差参与。
它恰为完整有限和
$$
-\frac{N_R}{(v)_s}
 \sum_{\substack{2\le i\le s\\i\ {\rm even}}}
 (-1)^i\binom{s+i-1}{i}
 (w^i-w'^i)\,[u^{s-i}]\mathcal E_v(u).
\tag{1116.48}
$$
当 $s$ 为奇数，上限自动变为 $s-1$。
最大输入是 $[u^{s-2}]\mathcal E_v$，
其权为 $v+2(s-2)=p-3$。
因而 (1116.47) 没有偷偷恢复被 centered difference 删除的高 band，
也没有读取 $G_v$ 流的第 $p$ 阶。

(1116.48) 保留了所有 $i$；不能由两个参数的这个单一线性组合为零，
反推每个 $[u^{s-i}]\mathcal E_v$ 为零。
特别，R1129 的非恒定性判据不能直接应用到某一个共纤维点对。
相差 sign 的 $w,w'$ 本来就是同一个 coarse 参数，须先识别。

### 9.4 原 Hasse first integral 与非零 p 次边界

记原规范的权多项式
$$
H=E_{p-1}(a,b),\qquad B=\frac{E_{p+1}(a,b)}{12},
\qquad C=B-wH,
$$
并记加权 Euler 向量场
$$
E=4a\partial_a+6b\partial_b+2w\partial_w.
$$
模 $p$ 的原 Serre 恒等式为
$$
\partial H=B,\qquad \partial B=\frac a3H.
$$
因 $H,B$ 的权分别同余 $-1,1$，代入 (1116.43) 立即得到
$$
\boxed{\qquad
\Theta H=C,\qquad \Theta C=0,\qquad \Theta^2H=0.
\qquad}
\tag{1116.49}
$$
在 supersingular Gaussian 点，$H=0$、$B=\beta_{\rm Car}=-\delta$
是单位。因此上一节从该点出发的有限流准确满足
$H(a_0(u),b_0(u))=B(a,0)u\bmod u^p$。

完整 restricted-power 恒等式是
$$
\boxed{\qquad
\Theta^p=H^2\Theta+HC\,E+C^2\partial_w.
\qquad}
\tag{1116.50}
$$
这正是 Bianchini，
[On the Ramanujan Vector Field modulo p,
arXiv:2602.20109v1](https://arxiv.org/abs/2602.20109)，
Theorem 1 / (22) 的原规范换元：
$$
e_2=12w,\qquad e_4=-48a,\qquad e_6=864b.
$$
该文的 $-12\partial_{e_2}$ 是 $-\partial_w$，
其 $(\widetilde B-e_2\widetilde A)/12$ 恰为这里的 $C$。
三个分量也可直接核为
$$
\begin{aligned}
\Theta^p a&=4HBa+6H^2b,\\
\Theta^p b&=6HBb-\frac43a^2H^2,\\
\Theta^p w&=B^2+\frac a3H^2.
\end{aligned}
$$
root 与 o2 已亲读该主要来源并独立核对全部换元。

特别在 $H=0$ 上，
$$
\Theta^p|_{H=0}=B^2\partial_w=\delta^2\partial_w.
\tag{1116.51}
$$
这是第 $p$ 次迭代的真实非零方向；不是 $\Theta^p=0$。
$\Theta$ 自身横截 $H=0$，所以不能先把 $\Theta$ 限制成
supersingular 直线上的向量场再随意迭代。
同样不能对 (1116.47) 的某个点对等式作未付的横向微分。

本附节完成的是原完整 profile 的真实 Ramanujan 来源、
安全有限时间变换与共同纤维的准确有界系数式。
尚未证明 actual-good mask 上 (1116.47) 无不同 coarse 解。
原较低 Fay / norm-two 乘积、bad 角色和各 source 相位仍全部保留。
全文无数学程序执行。

root 已全文独立纸核 §9 的热式共轭、Euler 第三分量、有限时间换元、全部 source 与 parity/最高安全权；o1 另行全文独核 (41)–(48)，并核 (49)–(51) 的代数换元。旧 §§1–8 逐字保留。无数学程序执行。
