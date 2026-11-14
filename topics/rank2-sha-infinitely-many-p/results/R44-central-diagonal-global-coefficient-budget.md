# R44：中央 theta 整函数的完整系数预算

日期：2026-11-12。**状态：下列全权上界及准确全局预算已证明。**

固定此前构造的有理系数整函数
$$
\mathscr D(Z)=\sum_{m\ge0}e_mZ^m,\qquad
 e_m=\frac{d_m}{f^{2m+1}}\in\mathbb Q,\qquad f=34(1+i).
$$
它非多项式，复增长阶至多一。定义实际截断系数量
$$
s_p(k)=\max_{2\le m\le k}
 \left(0,-\frac{v_p(e_m)}{m-1}\right),\qquad
\mathcal B(k)=\sum_p s_p(k)\log p.
\tag{1}
$$
对每个固定 $k$，这是有限和。

**定理。** 不附加任何 Sha 或高度假设，有
$$
\boxed{\quad \mathcal B(k)=2\log k+O(1).\quad}
\tag{2}
$$
其中普通、惰性素数分别贡献 $\log k+O(1)$；固定有限例外只贡献 $O(1)$。

这一结论针对 (1) 定义的截断系数缩放预算。
它不声称 Herblot 的实际 vanishing-jet 评价映射最优算术常数至少为二。
本结果补齐该固定图像的全部有限处系数预算，说明直接用此预算不能达到
其已核的充分代数化门槛 $\alpha<1/2$。

## 1. 从固定 sigma 大小得到一个统一 Gauss 界

令 $t=-x/y$、$z=\log_E(t)$，并保留 R38 的同一个 sigma：
$$
\Sigma(t)=\sigma(\log_E(t)),\qquad
\Sigma(t)=t+O(t^5).
$$
固定一个 $p\ge7$、$p\ne17$，置
$$
c_p=\frac1{p-1}.
$$
R38 已证明，在普通处 $\Sigma\in t\mathbb Z_p[[t]]$；
在惰性处，它的准确图形大小为 $p^{-p/(p^2-1)}$。
其已证明的系数界因而在两种情形下统一给出
$$
v_p([t^r]\Sigma(t))\ge-(r-1)c_p\qquad(r\ge1).
\tag{3}
$$
这里惰性指数满足 $p/(p^2-1)<1/(p-1)$；只使用较弱的 (3)。

形式指数 $t(z)=\exp_E(z)$ 也满足同一界。
确实，不变导子 $\delta=d/\omega$ 在原点的表达为
$$
\delta=v(t)\frac d{dt},\qquad v(t)\in\mathbb Z_p[[t]],\quad v(0)=1.
$$
因此 $\delta$ 保持 $\mathbb Z_p[[t]]$，而流的系数为
$$
[z^n]t(z)=\frac{(\delta^nt)(O)}{n!}.
$$
分子整；Legendre 公式给
$$
v_p([z^n]t(z))\ge-v_p(n!)\ge-\frac{n-1}{p-1}.
\tag{4}
$$

为避免仅凭半径推断系数范数，直接检查复合。
若两个首项为变量的级数 $F,G$ 都满足第 $r$ 项赋值至少
$-(r-1)c_p$，则 $[z^n]G(z)^r$ 的每个乘积项赋值至少
$-(n-r)c_p$。再乘 $F$ 的第 $r$ 项，得到至少 $-(n-1)c_p$。
对所有 $1\le r\le n$ 求和，证明 $F\circ G$ 也满足同一界。

应用于 $\sigma(z)=\Sigma(t(z))$，令
$$
\frac{\sigma(z)}z=\sum_{j\ge0}h_jz^j,
\qquad q(z)=\frac z{\sigma(z)}=\sum_{j\ge0}q_jz^j.
$$
得到 $v_p(h_j)\ge-jc_p$。由 $h_0=q_0=1$ 及逆级数递推
$$
q_j=-\sum_{a=1}^j h_aq_{j-a},
$$
归纳即得
$$
\boxed{\quad v_p(q_j)\ge-\frac j{p-1}\qquad(j\ge0).\quad}
\tag{5}
$$
这是一条对全部权有效的统一估计。
没有把 $\sigma$ 的 Hurwitz 整性直接传给其含一个零点的倒数，
也不需要任何新的 Hurwitz 整性定理。

## 2. 真实扭点初值在全部好素数处整

设 $\mathcal S$ 为固定256点导子轨道。
每个 $S\in\mathcal S$ 满足 $[34]S=T=(0,0)$。
在本节所有 $p$ 处，$34$ 为单位，$S$ 的阶素于 $p$。
良约化下的 prime-to-$p$ torsion 约化单射，故
$x(S),y(S)$ 都整，且 division function $\Psi_{34}(S)$ 为单位：
它既不在 $O$，也不在 $[34]$ 的非零核中。

由已证明的分配公式，
$$
U_S=-\frac1{34^2}\frac{\delta\Psi_{34}}{\Psi_{34}}(S).
\tag{6}
$$
$\Psi_{34}$ 在相应仿射整模型上正则，其不变导数也正则，
所以 (6) 说明 $U_S$ 整。
这样同时处理普通与惰性处，不引入辅助整数69的例外。

固定代数微分系统为
$$
\mathcal D U=-X,\qquad \mathcal D X=2Y,\qquad
\mathcal D Y=3X^2-17,
$$
$$
C_0=1,\qquad C_{n+1}=\mathcal D C_n+UC_n.
$$
这些多项式以及每个 $\mathcal D^mC_n$ 都在
$\mathbb Z[U,X,Y]/(Y^2-X^3+17X)$ 中。
由 (6)，其在任一 $S\in\mathcal S$ 上的值、及全部轨道求和均整。

## 3. 全部中央系数的统一上界

准确中央系数公式是
$$
d_m=\frac1{m!}\sum_{j=0}^{m+1}
 \frac{q_j}{(m+1-j)!}
 \sum_{S\in\mathcal S}(\mathcal D^mC_{m+1-j})(S).
\tag{7}
$$
以下只取 $m\ge1$。
当 $j=m+1$ 时，$C_0=1$，故 $\mathcal D^mC_0=0$。
**先删去这个零项**，其余项的
$$
n=m+1-j\ge1,\qquad 0\le j\le m.
$$
利用 (5)、第 2 节的整性，以及对正整数 $r$ 的
$v_p(r!)\le(r-1)/(p-1)$，每个非零项都有
$$
\begin{aligned}
v_p\left(\frac{q_j}{m!n!}
 \sum_{S\in\mathcal S}(\mathcal D^mC_n)(S)\right)
&\ge-\frac{j+(m-1)+(n-1)}{p-1}\\
&=-\frac{2m-1}{p-1}.
\end{aligned}
$$
因为 $f$ 为单位，这给出
$$
\boxed{\quad v_p(e_m)\ge-\frac{2m-1}{p-1}\qquad(m\ge1).\quad}
\tag{8}
$$

还要核定可能出现分母的第一个范围。
若 $m\le p-2$，(7) 的实际指标 $j\le m\le p-2$；
由 (5)，$v_p(q_j)>-1$，而它是整数，故 $q_j$ 整。
同时 $m<p$、$n\le m+1<p$，两个阶乘为单位。
因此
$$
\boxed{\quad e_m\in\mathbb Z_p\qquad(1\le m\le p-2).\quad}
\tag{9}
$$
若未先删去 $C_0$ 项，就不能在边界 $j=p-1$ 上用这个严格不等式。

当某个 $m\ge2$ 有负赋值时，由 (9) 必有 $m\ge p-1$。
(8) 因而推出
$$
-\frac{v_p(e_m)}{m-1}
\le\frac2{p-1}+\frac1{(p-1)(m-1)}
\le\frac2{p-1}+\frac1{(p-1)(p-2)}.
$$
所以
$$
\boxed{
\begin{aligned}
s_p(k)&\le\frac2{p-1}+\frac1{(p-1)(p-2)},\\
s_p(k)&=0\qquad(p>k+1).
\end{aligned}}
\tag{10}
$$
第二项相对于 $2/(p-1)$ 的误差在全部素数上乘 $\log p$ 后可求和。

## 4. 普通与惰性处各有匹配的下界

由于 $\mathscr D$ 非多项式，固定一个整数 $m_0\ge1$ 使
$e_{m_0}\ne0$。剔除由它的分子、分母以及有限小素数形成的固定集合。

普通处的完整 theta 整性及对数导子模 $p$ 周期已给出
$$
v_p(e_{p-1+m_0})=-2
\quad\text{对几乎所有 }p\equiv1\pmod4.
\tag{11}
$$
具体证明见 [普通预算笔记](../notes/2026-11-12-central-diagonal-ordinary-size-budget.md)：
同一个整双级数的矩
$A_m=\Omega_p^{2m}(m!)^2d_m$
满足 $A_{m+p-1}\equiv A_m\pmod p$，且固定 $A_{m_0}$ 为单位。

惰性处则由 [中央平移笔记](../notes/2026-11-12-central-diagonal-inert-shift.md)
的实际扭点 $\mathcal D^p=-\kappa_p\partial_U$ 和两类分母相消得到
$$
p^2e_{p+1+s}\equiv\frac{\kappa_p^2}{(Nf)^2}e_s\pmod p,
\qquad0\le s\le p-3,
$$
其中 $\kappa_p\in\mathbb F_p^\times$。取 $s=m_0$，得到
$$
v_p(e_{p+1+m_0})=-2
\quad\text{对几乎所有 }p\equiv3\pmod4.
\tag{12}
$$

因此两类截断和分别至少为
$$
2\sum_{\substack{p\le k-m_0+1\\p\equiv1\ (4)}}
 \frac{\log p}{p+m_0-2}+O(1)
=\log k+O(1),
$$
$$
2\sum_{\substack{p\le k-m_0-1\\p\equiv3\ (4)}}
 \frac{\log p}{p+m_0}+O(1)
=\log k+O(1).
\tag{13}
$$
此处只是对固定模4的素数定理作分部求和；
分母与 $p$ 的固定平移之差为可求和误差。

另一方面，(10) 对每类素数分别给上界
$$
2\sum_{\substack{p\le k+1\\p\equiv a\ (4)}}
\frac{\log p}{p-1}+O(1)
=\log k+O(1),\qquad a=1,3.
\tag{14}
$$
(13)、(14) 合起来，便得到两类各自准确的 $\log k+O(1)$。

## 5. 固定例外的贡献有界

为使 (2) 真正包括全部有限处，还需说明固定的少数模型坏位不会
使 $s_p(k)$ 随 $k$ 无界。这只需各处一个正的收敛半径，不能把它
与普通位的整性混为一谈。

R38 使用的固定有理公式
$$
\log(\Sigma(t)/t)=\sum_{n\ge1}\frac1{4n}
\left(w_n-\frac12\sum_{j=1}^n\frac{w_{n-j}w_j}{4j-1}\right)t^{4n},
\quad w_n=(-1)^n\binom{2n}{n}17^n
$$
在每个固定 $p$ 处的系数负赋值仅为 $O_p(\log n)$。
所以此对数在开单位圆盘收敛；再取一个足够小的正半径，使其 Gauss 范数
小于 $p^{-1/(p-1)}$，便得到 $\Sigma(t)/t$ 的正收敛半径和非零常数项。
形式指数仍由整原点向量场给出一个正半径，故 $\sigma(z)/z$ 与它的倒数
$q(z)$ 在足够小圆盘上解析；存在固定 $c(p)$ 使
$v_p(q_j)\ge-c(p)(j+1)$。

所有扭点初值 $U_S,x(S),y(S)$ 是固定的代数数，
在这个有限集合的任一素位具有有限赋值。
多项式 $\mathcal D^mC_n$ 的普通总次数至多 $n+2m$，系数为整数；
所以当 $n\le m+1$ 时，其在这些固定初值上的赋值有一个
$-c'(p)(m+1)$ 下界。两个阶乘的负赋值也只线性增长。
由 (7) 得到 $v_p(e_m)\ge-c''(p)(m+1)$，其中 $f$ 的可能负赋值已包含。

因此每个固定例外 $p$ 的 $\sup_{k\ge2}s_p(k)$ 有限。
有限多个这类项在 (1) 中只贡献 $O(1)$，完成 (2) 的证明。

## 6. 已解决的接口与尚未解决的问题

中央整函数现在具有完整的两侧说明：

- 复侧：固定有理系数、非代数、全平面整一致化、增长阶至多一；
- 有限处：普通完整大小及半径为 $p^{-2/(p-1)}$；
  惰性处有真实中央平移和匹配的预算上下界；
- 全部截断系数缩放预算准确为 $2\log k+O(1)$。

即使假设几乎全部目标普通 $p$ 的 Sha 初级部分无限，(11) 的另一条
固定 tame 权以及 (12) 的惰性分母列都保持。
所以这套直接预算不会被中心额外零阶降到 $1/2$ 以下。

仍可研究真正评价映射的整格、其他固定函数、theta 平方根或非线性系统；
本定理没有给这些不同对象的下界。固定曲线的无穷多个初级有限结论仍未证明。

### 证明依赖

- [R38](R38-exact-inert-sigma-size-and-jet-budget.md)：同一 $\Sigma$ 的普通整性、惰性大小及固定有理对数公式。
- [固定中央 theta 对角](../notes/2026-11-12-anticyclotomic-theta-diagonal.md)：实际轨道、微分系统与含完整阶乘的 (7)。
- [普通预算](../notes/2026-11-12-central-diagonal-ordinary-size-budget.md)：全部混合矩及周期式；已核 Bannai–Kobayashi (2010) Corollary 2.17。
- [惰性中央平移](../notes/2026-11-12-central-diagonal-inert-shift.md)：真实 $U_S$、34分配及两个分母来源的严格相消。
- [中央整函数](../notes/2026-11-12-central-diagonal-entire-series.md)：固定有理下降和非多项式性。这里不另假定某个低权非零的数值猜测。
