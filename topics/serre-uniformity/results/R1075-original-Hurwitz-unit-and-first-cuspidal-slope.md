# R1075：原 Hurwitz 系数的 theta 恒等式与第一 cuspidal 斜率单位

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o1_theta / o2_high_coefficient / root。

**已证明。**

本文接 [R1071 §16](R1071-original-p-local-cuspidal-label-polynomials.md) 的原 sigma/Hurwitz 归一，证明其中尚未支付的 $G_{p-5}$ 单位性。全节是纸面恒等式证明，不执行新窗口。设 $p\ge41$ 为素数，原参考椭圆曲线与微分写为
$$
E_{a,b}:y^2=x^3+ax+b,\qquad \omega=\frac{dx}{2y},
$$
并要求判别式非零。用不同符号 $a,b$ 区分曲线系数与 Bernoulli 数。原 Hurwitz 系数始终由
$$
x(z_{\rm add})=z_{\rm add}^{-2}
 +\sum_{\substack{d\ge4\\d\ {\rm even}}}(d-1)G_dz_{\rm add}^{d-2},
 \qquad dz_{\rm add}=\omega
\tag{1075.1}
$$
确定。

结论为：在任一超奇异参考上，令
$$
\beta_{\rm Car}=\frac{E_{p+1}(E,\omega)}{12}.
$$
则 $\beta_{\rm Car}\ne0$，并且
$$
\boxed{\quad
G_{p-5}^{\,p}=-\frac{24}{7}\,b\,
                 \beta_{\rm Car}^{\,p-6}.
\quad}
\tag{1075.2}
$$
所以 $G_{p-5}\ne0$ 当且仅当 $b\ne0$，即当且仅当 $j(E)\ne1728$。这不是把不同权的模形式在超奇异点直接认同，而是下面完整同权恒等式的特化。

特别地，若 $p\equiv5\pmod6$ 且原 $j=0$ 参考为
$y^2=x^3+b$、$b\in\mathbb F_p^\times$，则
$$
\beta_{\rm Car}
 =\binom{(p-1)/2}{(p-2)/3}b^{(p+1)/6}\in\mathbb F_p^\times,
\qquad
\boxed{\quad G_{p-5}=-\frac{24b}{7\beta_{\rm Car}^{\,5}}\in\mathbb F_p^\times.\quad}
\tag{1075.3}
$$
这里 $\beta_{\rm Car}$ 不替代 R1071 §16 的节点单位 $\beta_0$，二者各保原定义。

## 1. 保全部 Frobenius 项的同权 Eisenstein 恒等式

用 coefficient-one 的 Hecke 归一
$$
\mathcal E_d(q)
 =-\frac{B_d}{2d}+\sum_{n\ge1}\sigma_{d-1}(n)q^n.
$$
不要将它与 constant-one 的 $E_d$ 混用。令
$H=E_{p-1}$、$J=E_{p+1}$，约化到特征 $p$。标准同权环中的 Serre 导数为
$$
\partial_w f=q\frac{df}{dq}-\frac w{12}E_2f.
$$
由 $H(q)=1$、$J(q)=E_2(q)$，定义真正模形式算子
$$
\mathcal T_w f=H\,\partial_w f+\frac w{12}Jf
 \in M_{w+p+1}(\mathbb F_p).
\tag{1075.4}
$$
其 $q$ 展开正是 $q\,df/dq$。每次迭代都使用实际新权
$w_i=6+i(p+1)$。

在 $p\nmid n$ 时，逐个除数换元给
$$
n^{p-6}\sigma_5(n)=\sigma_{p-6}(n)\pmod p.
$$
在 $n=p^r n_0$、$r\ge1$、$p\nmid n_0$ 时，左端为零，而
$$
\sigma_{p-6}(n)-\sigma_{p-6}(n/p)=0\pmod p.
$$
常数项也在 $\mathcal E_{p-5}-\mathcal E_{p-5}^p$ 中抵消。因此完整 $q$ 身份为
$$
\boxed{\quad
\mathcal T^{p-6}\mathcal E_6
 =H^{p-5}\mathcal E_{p-5}-\mathcal E_{p-5}^{\,p}.
\quad}
\tag{1075.5}
$$
两边的实际权都是 $p(p-5)$；右侧的 Frobenius 项尤其不能删去。

所有使用的 Eisenstein 级数均 $p$ 整：$6,p-5$ 都小于 $p-1$，且非零，von Staudt--Clausen 排除了其 Bernoulli 常数的 $p$ 分母。固定权的 $q$ 原理可自足地按标准基验证：$E_4,E_6,\Delta$ 的适当固定权单项式可取为 $\Delta^rE_4^{a_r}E_6^{b_r}$，其中 $b_r\in\{0,1\}$；其首 $q$ 次数为互异的 $r$，首系数均为 $1$。因此同权 $q$ 恒等式在 $\mathbb F_p[E_4,E_6]$ 中成立，进而可在原带微分的椭圆参考上求值。

## 2. 超奇异特化与原 Hurwitz 阶乘

在 $H(E,\omega)=0$ 处，(1075.4) 每一步直接成为
$$
(\mathcal T_{w_i}f)(E,\omega)
 =w_i\beta_{\rm Car}f(E,\omega).
$$
此处是在每个实际模形式值上连续应用；导数项一直带 $H$，没有任何除 $H$ 操作。因
$$
\prod_{i=0}^{p-7}w_i
 =\prod_{r=6}^{p-1}r=-\frac1{5!}\pmod p,
$$
(1075.5) 给出
$$
\mathcal E_{p-5}^{\,p}
 =\frac{\beta_{\rm Car}^{p-6}}{120}\mathcal E_6.
\tag{1075.6}
$$

在原微分/Tate 标架中，(1075.1) 的 lattice-sum 系数满足
$$
G_d=\frac{2}{(d-1)!}\mathcal E_d.
\tag{1075.7}
$$
这一式可由 Tate 原点的 Weierstrass 展开直接核：常数为
$-B_d/d!$，正 $q$ 系数为 $2\sigma_{d-1}(n)/(d-1)!$。
特别地，
$$
E_4=-48a,\qquad E_6=+864b,\qquad
G_6=-\frac b{35}.
\tag{1075.8}
$$
这里原 Tate 微分下 $c_6=-E_6$；若误用 $E_6=c_6$ 会反转本节符号。

由 Wilson，
$$
(p-6)!=\frac1{120}\pmod p.
$$
将 (1075.7) 代入 (1075.6)，保留左侧实际 $p$ 次方，得到
$$
G_{p-5}^{\,p}
 =120\,\beta_{\rm Car}^{p-6}G_6
 =-\frac{24}{7}b\,\beta_{\rm Car}^{p-6},
$$
即 (1075.2)。这一步只使用小于 $p$ 的阶乘，全部为单位。

## 3. $\beta_{\rm Car}$ 的实际 Cartier 归一及单位性

记 $m=(p-1)/2$、$f(X)=X^3+aX+b$。Hasse 多项式及实际相对 Cartier 系数为
$$
H=[X^{p-1}]f(X)^m,\qquad
\beta_{\rm Car}=[X^{p-2}]f(X)^m,
\qquad
C_{\rm rel}(x\omega)=\beta_{\rm Car}\omega'.
\tag{1075.9}
$$
第二式确与 $E_{p+1}/12$ 相同，以下给出不省标架的多项式验证。写
$P=f^{m-1}=\sum c_jX^j$。从
$[X^{p-1}](f^m)'=0$ 及 $[X^{p-1}](X^2f^m)'=0$ 得
$$
3c_{p-3}+ac_{p-1}=0,\qquad
c_{p-5}=-3ac_{p-3}-4bc_{p-2}.
$$
故
$$
\begin{aligned}
[X^{p-2}]f^m
 &=c_{p-5}+ac_{p-3}+bc_{p-2}\\
 &=\frac23a^2c_{p-1}-3bc_{p-2}\\
 &=6b\,\frac{\partial H}{\partial a}
       -\frac43a^2\,\frac{\partial H}{\partial b}.
\end{aligned}
$$
由 (1075.8) 与
$\partial E_4=-E_6/3$、$\partial E_6=-E_4^2/2$，
末式就是 $\partial H$。又 $12\partial H=E_{p+1}$，遂得 (1075.9) 中的确切归一。

为支付全部超奇异点的非零性，可在带完整 level-2 标记及非零微分的参数上使用
$$
P_m(\lambda)=\sum_{i=0}^{m}\binom mi^2\lambda^i.
$$
它是 Legendre Hasse 多项式的一单位倍，且
$P_m(0)=1$、$P_m(1)=\binom{p-1}m\ne0$。它满足
$$
\lambda(1-\lambda)P_m''
 +(1-2\lambda)P_m'-\frac14P_m=0.
$$
若在 $\lambda\ne0,1$ 有重根，取其最小重数 $2\le r\le m<p$，微分方程最低项的系数
$\lambda(1-\lambda)r(r-1)$ 为单位，矛盾。因此原 Hasse 截面的所有超奇异零都简单。完整 level-2 标记在 $p>2$ 的光滑模叠上为 étale；同时保留非零微分消去 $\{\pm1\}$ 稳定子，故不丢 $j=0,1728$ 的真实细参数。

在光滑 Weierstrass 模叠上，Serre 向量场
$(-E_6/3,-E_4^2/2)$ 与缩放向量场 $(4E_4,6E_6)$ 的行列式为
$2(E_4^3-E_6^2)=3456\Delta\ne0$。Hasse 截面在其零点的缩放导数为零，且其细模参数零简单，故 $\partial H\ne0$，即 $\beta_{\rm Car}\ne0$。

在本节原 $j=0$ 行还可完全绕过上述一般简单零论证：令 $p=6k-1$、$a=0$，则 (1075.9) 直接给
$$
\beta_{\rm Car}
 =\binom{3k-1}{2k-1}b^k.
$$
分子、分母所有阶乘都小于 $p$，$b\ne0$，所以它是单位。在 $\mathbb F_p$ 参考上，
$\beta_{\rm Car}^{p-6}=\beta_{\rm Car}^{-5}$ 且 $G_{p-5}^p=G_{p-5}$，得 (1075.3)。对于运输到扩域的不同标架，先保 (1075.2) 的 Frobenius，不擅删扭曲。

## 4. 原 cuspidal 斜率与准确完成范围

消费 R1071 §16 已证的原 sigma/division-polynomial 身份
$A_{p-5}=\kappa_\chi G_{p-5}$。原 $\chi=\omega^{p-3}$ 属于 forced 模块，其未除圆单位基的完整局部多项式斜率
$$
-\frac{\beta_0^{p(p-5)}\lambda^3\kappa_\chi G_{p-5}}3
$$
在每个 $p\equiv5\bmod6$、$p\ge41$ 都是单位；这一局部断言不要求 Bernoulli-good。
对实际 Bernoulli-good 的
$\chi=\omega^{p-3}$，原 $j=0$ 粗盘坐标 $T_{\rm coarse}=t^3$ 满足
$$
\begin{aligned}
c_{\chi,s}(T_{\rm coarse})-c_{\chi,s}(0)
 &=\frac{\beta_0^{p(p-5)}\lambda^3G_{p-5}}{6b_\chi}\,
     T_{\rm coarse}\\
 &=-\frac{4b\,\beta_0^{p(p-5)}\lambda^3}
          {7b_\chi\beta_{\rm Car}^{5}}\,
     T_{\rm coarse}.
\end{aligned}
\tag{1075.10}
$$
这里采用原 $\mathbb F_p$ 参考；$b_\chi$ 中原 Weil/Teichmüller 相位及
$\beta_0,\lambda$ 都保 R1071 §16 的实际定义。所有右侧因子为单位。故此**实际 label 的整粗盘约化为非零斜率的仿射函数**；并非仅证明某个抽象同权源非零。一般超奇异参考的相应 fine 三次最高系数也在 $j\ne1728$ 时非零，但这不把三次多项式称为注入。

本节完成原 $G_{p-5}$ 与此原 $j=0$ 斜率的单位性，不声称每个所需素数的 $\chi$ 均 Bernoulli-good，不将其替换为原 $f_N/e$、O2 bare 高坐标、primitive/Legendre 同标签或全部圆盘目标。原 $f_N/e$ 单位及主目标继续 OPEN。已认证 $p=47$ 的 $G_{42}=17$、$A_{42}=31$ 与原斜率记录由 R1072 消费；本证明不新增或重跑窗口。

## 5. 输入来源与范围

- Ahlgren--Raum--Richter, *Theta Cycles of Modular Forms Modulo $p^2$*, [arXiv:2604.06049v1](https://arxiv.org/pdf/2604.06049), §1.1 (1.7)--(1.8) 的 theta/Serre 导数归一，§1.3 (1.14) 的 $12\partial E_{p-1}=E_{p+1}\pmod p$。这里只使用这些标准模 $p$ 输入，未调用该文模 $p^2$ filtration 结论。
- R1071 §16 的原 sigma、原 elliptic logarithm/eigenparameter、$A_{p-5}$ 与全部节点/Weil 尺度。
- 上述完整 divisor-sum 身份、同权 $q$ 原理、Wilson 及实际 Cartier 系数给出本节其余证明；未以一个低 Hasse 单位代替未比较的指定源。


o1_theta 给出原 theta/q 恒等式及完整 Hurwitz/Cartier 归一；o2 与 root 独核全部权、Frobenius 项、Wilson 常数和原斜率。root 已亲读所引 (1.7)–(1.8)、(1.14)，并逐项核 Legendre 简单零及一般 Cartier 多项式身份。本结果未运行数学程序。
