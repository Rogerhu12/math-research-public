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
