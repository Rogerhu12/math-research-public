# R249：真实有限头平衡Jordan相似与精确进位余量

日期：2026-11-13（UTC+8）。作者：boundary。复核：Astra-ISP-1cf。状态：已证明中间结论。以下全部为真实有限矩阵的完整证明，适用于 $T_N,T_Y$。

本稿改进 [R239 附录](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md) 已有的有限头 Jordan 成本。令 $d=2^m$。构造明确可逆矩阵 $S_m$ 和正数 $\lambda_m$，使
$$
T_m=S_m(\lambda_mJ_d)S_m^{-1},
\qquad
\log\kappa_m\le\left(\frac{35}{6}+o(1)\right)d^4,
\qquad \kappa_m=\|S_m\|\,\|S_m^{-1}\|.
$$
必须支付条件数平方时，精确真实 carry 仍给
$$
\log(\kappa_m^2\eta_{m-1})
\le-\left(\frac{455}{6}+o(1)\right)d^4.
$$
本稿只证明相似、条件数和真实误差预算；移动头通量以及未知核向量的尾项须另行处理，不在这里宣称 $N=M$。

## 1. 两个模型的真实头、权积与精确指数

在边界 $\ell^2(\mathbb N_0)$ 上，
$$
Be_n=\alpha_{v_2(n)}e_{n-1},\qquad Be_0=0,
$$
$$
-\log\alpha_j=
\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$
记
$$
W_0=1,\qquad W_n=\prod_{\ell=1}^n\alpha_{v_2(\ell)},
\qquad d_j=W_{2^j},\qquad \omega_n=-\log W_n.
$$
本稿用 $d=2^m$ 表示头维数，带下标的 $d_j$ 仍表示真实归一化常数，二者不得混淆。

对 $0\le r<2^j$，$v_2(2^j+\ell)=v_2(\ell)$（$1\le\ell\le r$）给
$W_{2^j+r}=d_jW_r$。归纳得到准确的二进制分解
$$
\boxed{
 W_n=\prod_{j\in\operatorname{bits}(n)}d_j,
 \qquad \omega_n=\sum_{j\in\operatorname{bits}(n)}\Lambda_j,
 \qquad \Lambda_j=-\log d_j.
}
\tag{1.1}
$$
直接对实际权求和，
$$
\boxed{
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j
\le100\,16^j.
}
\tag{1.2}
$$
最后的不等式来自 $150j+25\le105\,4^j$；该式在 $j=0$ 成立，且可直接归纳。
尤其 $d_0=e^{-20}$。当 $d=2^m$ 时，由 (1.1) 或几何和，
$$
\boxed{
\omega_{d-1}
=\frac{20}{3}d^4-15d^3+(150m-275)d+\frac{850}{3}.
}
\tag{1.3}
$$

令 $B_m=B|_{\mathcal F_m}$，$\mathcal F_m=\operatorname{span}\{e_0,\ldots,e_{d-1}\}$。两个实际有限头准确为
$$
T_m=f_m(B_m),
$$
其中分别取
$$
f_{N,m}(z)=\sum_{j<m}a_j\frac{z^{2^j}}{d_j},\qquad
f_{Y,m}(z)=\sum_{j<m}a_j\frac{z^{2^j}}{d_j+z^{2^j}},\qquad
 a_j=(j+1)^{-2}.
\tag{1.4}
$$
$Y$ 情形只取模 $z^d$ 的 Taylor 多项式；因为 $B_m^d=0$，它与实际逆 $(I+N_j^{[m]})^{-1}$ 的有限展开完全相同。两模型均有
$$
\beta=f_m'(0)=d_0^{-1}=e^{20}.
\tag{1.5}
$$

## 2. 归一化有限芽的统一系数预算，包含全部 Cayley 项

以下取 $m\ge2$、$d\ge4$，并定义
$$
\boxed{
L=L_m=100\frac{(d/2)^4}{d/2-1}
=\frac{25}{2}\frac{d^4}{d-2},\qquad \rho=e^{-L}.
}
\tag{2.1}
$$
在截断环 $\mathbb C[z]/(z^d)$ 中写
$$
g(z)=\beta^{-1}f_m(z)=z+\sum_{n=2}^{d-1}b_nz^n.
$$
我们证明
$$
\boxed{|b_n|\le e^{L(n-1)}\qquad(2\le n<d).}
\tag{2.2}
$$

$N$ 模型只需考虑 $n=2^j$。对 $j\ge1$，由 (1.2) 以及
$x^4/(x-1)$ 在 $x\ge2$ 上递增，
$$
\frac{\Lambda_j}{2^j-1}
\le100\frac{(2^j)^4}{2^j-1}\le L.
\tag{2.3}
$$
归一化系数还有因子 $a_je^{-20}<1$，所以 (2.2) 成立。

$Y$ 模型的第 $n$ 个系数准确为
$$
b_n=e^{-20}
\sum_{\substack{0\le j<m\\2^j\mid n}}
 a_j(-1)^{n/2^j-1}\exp\!\left(\frac n{2^j}\Lambda_j\right).
\tag{2.4}
$$
若 $j\ge1$、$n\ge2^j$，则
$$
\frac n{2^j}\Lambda_j
\le\frac{\Lambda_j}{2^j-1}(n-1)\le L(n-1).
$$
若 $j=0$、$n\ge2$，则 $n\Lambda_0=20n\le40(n-1)\le L(n-1)$。
最后使用 $\sum_ja_j<2$ 和 $2e^{-20}<1$，(2.4) 也给 (2.2)。这一步包含了所有次数为 $r2^j$ 的真实 Cayley 项，并非只保留平方零部分。

定义缩放后的有限芽
$$
\widetilde g(z)=\rho^{-1}g(\rho z)
=z+\sum_{n=2}^{d-1}\widetilde b_nz^n.
$$
由 (2.2)，$|\widetilde b_n|\le1$。其模 $z^d$ 的复合逆记为 $\widetilde h$。

此外，(2.3) 及最低位 $\Lambda_0=20\le L$ 给
$$
L\,2^j-\Lambda_j\ge0\qquad(0\le j<m).
$$
因此对 $0\le n<d$，函数
$$
F(n)=Ln-\omega_n
=\sum_{j\in\operatorname{bits}(n)}(L2^j-\Lambda_j)
$$
满足
$$
\boxed{0\le F(n)\le F(d-1)=L(d-1)-\omega_{d-1}.}
\tag{2.5}
$$
这里使用的是准确 bit 加性，不是假设 $F(n)$ 随整数 $n$ 单调。

## 3. 换元矩阵和 Lagrange 逆矩阵的有限范数

以 $1,z,\ldots,z^{d-1}$ 为正交基，令 $C_u$ 表示模 $z^d$ 的换元矩阵
$$
p(z)\longmapsto p(u(z)),\qquad
(C_u)_{nk}=[z^n]u(z)^k.
$$
在 $u(0)=0,u'(0)=1$ 时，它可逆且 $C_u^{-1}=C_{u^{-1}}$。

对 $u=\widetilde g$，每个系数绝对值不超过 $1$。对 $n\ge k\ge1$，组成数计数给
$$
|[z^n]\widetilde g(z)^k|
\le\binom{n-1}{k-1}\le2^d.
$$
第 $k=0$ 列只是常数基向量。所以
$$
\boxed{\|C_{\widetilde g}\|\le d\,2^d.}
\tag{3.1}
$$

对逆芽使用完全有限的 Lagrange 系数式
$$
[z^n]\widetilde h(z)^k
=\frac{k}{n}[u^{n-k}]
 \left(\frac{u}{\widetilde g(u)}\right)^n,
\qquad n\ge k\ge1.
\tag{3.2}
$$
该式也可直接在形式留数中令 $z=\widetilde g(u)$，再对
$u^k\widetilde g(u)^{-n}$ 作一次形式分部积分得到，故只依赖所需有限阶系数。

在 $|u|=1/4$ 上，
$$
\left|\frac{\widetilde g(u)}u-1\right|
\le\sum_{r\ge1}|u|^r\le\frac13.
$$
因此 (3.2) 的系数由圆周 Cauchy 估计有界为
$$
\left|[z^n]\widetilde h(z)^k\right|
\le4^{n-k}(3/2)^n\le6^d.
$$
这是对一个实际有限多项式的无零分母应用 Cauchy 估计，不涉及零收敛半径的无限慢芽。于是
$$
\boxed{\|C_{\widetilde h}\|\le d\,6^d.}
\tag{3.3}
$$

## 4. 方向、列缩放与实际 Jordan 相似

令 $J_d e_n=e_{n-1}$（$n\ge1$），$J_de_0=0$，它是后移 Jordan 矩阵。
再令
$$
D_m=\operatorname{diag}(W_0^{-1},\ldots,W_{d-1}^{-1}),
\qquad R_\rho=\operatorname{diag}(1,\rho,\ldots,\rho^{d-1}).
$$
真实权位置给
$$
B_m=D_mJ_dD_m^{-1}.
\tag{4.1}
$$
前移矩阵 $J_d^\top$ 是乘以 $z$，所以换元恒等式为
$$
\widetilde g(J_d^\top)C_{\widetilde g}
=C_{\widetilde g}J_d^\top.
$$
转置后，
$$
\widetilde g(J_d)
=C_{\widetilde h}^\top J_d C_{\widetilde g}^\top.
\tag{4.2}
$$
全部系数为实数；这里使用转置，范数等于原矩阵的 Hilbert 算子范数。

又 $R_\rho^{-1}J_dR_\rho=\rho J_d$，以及
$f_m(\rho z)=\beta\rho\widetilde g(z)$。由 (4.1)、(4.2)，定义
$$
\boxed{
S_m=D_mR_\rho C_{\widetilde h}^\top
=\operatorname{diag}(e^{-F(n)})C_{\widetilde h}^\top,
\qquad \lambda_m=\beta\rho=e^{20-L}>0.
}
\tag{4.3}
$$
则准确有
$$
\boxed{T_m=S_m(\lambda_mJ_d)S_m^{-1}.}
\tag{4.4}
$$
因此目标确为严格下降一个 headlevel 的单链，且链权非零。这里的列缩放等价于在未平衡换元相似右端乘以
$\operatorname{diag}(e^{-F(n)})$；它同时把目标链的每条权化成同一个 $\lambda_m$。

由 (2.5)，$\operatorname{diag}(e^{-F(n)})$ 是收缩。结合 (3.1)、(3.3)，
$$
\|S_m\|\le d\,6^d,
$$
$$
\|S_m^{-1}\|
=\left\|C_{\widetilde g}^\top\operatorname{diag}(e^{F(n)})\right\|
\le d\,2^d e^{F(d-1)}.
$$
故
$$
\boxed{
\kappa_m\le d^2\,12^d\exp\!\bigl(L(d-1)-\omega_{d-1}\bigr).
}
\tag{4.5}
$$
没有把 $D_m$ 和逆芽系数的最坏位置独立相乘，也没有对未缩放的两个三角矩阵重复支付 $F(d-1)$。

记明确上界
$$
\Psi_m=L(d-1)-\omega_{d-1}+d\log12+2\log d.
\tag{4.6}
$$
由 (1.3)、(2.1)，
$$
L(d-1)=\frac{25}{2}d^4\frac{d-1}{d-2}
=\frac{25}{2}d^4+O(d^3),
$$
所以
$$
\boxed{\log\kappa_m\le\Psi_m
=\frac{35}{6}d^4+O(d^3+m d).}
\tag{4.7}
$$
这相较 R239 附录的 $221\,16^{m-1}=(221/16)d^4$ 预算有严格的主指数改善。

## 5. 条件数平方必须与精确真实 eta 比较

由实际 $\alpha$ 公式，
$$
-\log\eta_j=1400\,16^j-630\,8^j+300\,2^j.
$$
所以
$$
\boxed{
-\log\eta_{m-1}=\frac{175}{2}d^4-\frac{315}{4}d^3+150d.
}
\tag{5.1}
$$
不能只用粗 $770\,16^{m-1}$ 来代表这个精确指数。

令
$$
\Delta_m=-\log\eta_{m-1}-2\Psi_m.
$$
将全部项代入，准确得到
$$
\boxed{
\begin{aligned}
\Delta_m={}&\frac{455}{6}d^4-\frac{435}{4}d^3
-\frac{25d^4}{d-2}\\
&+(300m-400-2\log12)d+\frac{1700}{3}-4\log d.
\end{aligned}
}
\tag{5.2}
$$
因此
$$
\boxed{
\kappa_m^2\eta_{m-1}\le e^{-\Delta_m},
\qquad
\Delta_m=\frac{455}{6}d^4+O(d^3+m d).
}
\tag{5.3}
$$

还可给所有 $m\ge2$ 的显式余量。此时 (5.2) 第二行非负，因
$2\log12<5$、$4\log d=4m\log2<3m$；余下正的线性项已足够支付。
故
$$
\frac{\Delta_m}{d^4}
\ge\frac{455}{6}-\frac{435}{4d}-\frac{25}{d-2}
\ge\frac{1735}{48}>36.
$$
最后一步在 $d\ge4$ 用最小 $d=4$ 即可。因此
$$
\boxed{\kappa_m^2\eta_{m-1}\le e^{-36d^4}\qquad(m\ge2).}
\tag{5.4}
$$
渐近主余量为 $455/6$，而非仅仅这个粗统一常数 $36$。

## 6. 全空间有限头误差与局部 carry 和的准确预算

真实有限头加纯尾模型为
$$
T^{[m]}=T_m\otimes I+I\otimes D_{\ge m}.
$$
原有限链误差可保留实际 $\eta$ 而不先换成粗指数：对 $i<m$，
$$
\|N_i-N_i^{[m]}\otimes I\|=\alpha_m/\alpha_i\le\eta_{m-1},
$$
Cayley 逆差至多为其 $9$ 倍；高位真／纯差分别不超过 $\eta_i$ 或 $4\eta_i$。
使用 $\sum_i a_i<2$，得到
$$
\boxed{\|T-T^{[m]}\|\le26\eta_{m-1}.}
\tag{6.1}
$$
因此从 (5.4) 直接有
$$
\boxed{\kappa_m^2\|T-T^{[m]}\|
\le26e^{-36d^4}\qquad(m\ge2).}
\tag{6.2}
$$

对局部差 $K_L=T^{[L+1]}-T^{[L]}$，同样有
$$
\|K_L\|\le52\eta_{L-1}.
$$
精确指数还满足
$$
(-\log\eta_{j+1})-16(-\log\eta_j)
=5040\,8^j-4200\,2^j>0,
$$
所以 $\eta_{m+t-1}\le\eta_{m-1}^{16^t}$。
对任意固定 $a\ge0$，令
$$
C_a=\sum_{t\ge0}e^{at-1070(16^t-1)}<\infty.
$$
由 $-\log\eta_{m-1}\ge1070$，
$$
\boxed{
\kappa_m^2\sum_{L\ge m}e^{a(L-m)}\|K_L\|
\le52C_a\,e^{-\Delta_m}.
}
\tag{6.3}
$$
额外乘以 $e^{O(d)}$、$d$ 的任意固定幂，仍不改变 $455/6$ 的渐近主余量。这是实际全空间、全部局部 carry 的预算，不是某个核向量上的小残差。

## 7. 本稿不处理的移动头项

相似目标的严格分级性质与 (6.3) 为移动头能量提供了明确输入。但相似后的正度量和截断会给未知核向量的尾范数再乘以条件数；这个尾项不能从 $w\in\ell^2$ 与 (6.3) 自动消去。

因此本稿不将可付的 $\kappa_m^2\eta_{m-1}$ 误差直接升级为 $N=M$，也不从一个必要尾下界推出平方和矛盾。移动头能量、网格 $d^4=16^m$ 上的推论和任何尾率量词另由后续稿完整支付。
