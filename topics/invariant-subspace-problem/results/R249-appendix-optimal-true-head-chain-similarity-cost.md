# R249附录：真实有限头单链相似的条件数主指数最优

日期：2026-11-13（UTC+8）。作者：boundary。状态：已证明，中间结论。

本文处理两个实际有限头 $T_m=T_N|_{\mathcal F_m}$、$T_Y|_{\mathcal F_m}$。证明 [R249](R249-balanced-true-head-jordan-similarity-and-exact-carry-margin.md) 的条件数主指数 $35/6$ 不能通过更换任意非零 Jordan 链权再降低。结论不限制其他能量投影，也不排除利用真实核向量得到比环境条件数更好的估计。

## 1. 结论与真实有限头

设 $m\ge2$、$d=2^m$、$s=2^{m-1}$。令 $B_m$ 为真实边界后移在前 $d$ 个物理坐标上的压缩：
$$
B_m e_n=\alpha_{v_2(n)}e_{n-1}\quad(1\le n<d),\qquad B_m e_0=0.
$$
记 $W_n=\prod_{\ell=1}^n\alpha_{v_2(\ell)}$、$d_j=W_{2^j}$、$\Lambda_j=-\log d_j$。准确权为
$$
-\log\alpha_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\qquad \alpha_0=e^{-20},
$$
$$
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j.
\tag{1.1}
$$
两个真实有限头分别等于 $f_m(B_m)$，其中所有表达在模 $z^d$ 意义下使用：
$$
f_{N,m}(z)=\sum_{j<m}\frac{a_jz^{2^j}}{d_j},
\qquad
f_{Y,m}(z)=\sum_{j<m}\frac{a_jz^{2^j}}{d_j+z^{2^j}},
\qquad a_j=(j+1)^{-2}.
\tag{1.2}
$$
二者的线性项均为 $\beta z$，$\beta=e^{20}$，因此均为单个长度 $d$ 的幂零 Jordan 块。

**定理。** 设 $J_\gamma$ 是任意非零加权后移链，
$$
J_\gamma e_0=0,\qquad J_\gamma e_n=\gamma_ne_{n-1},
\qquad \gamma_n\ne0\quad(1\le n<d).
$$
若任意可逆矩阵 $S$ 满足 $T_m=SJ_\gamma S^{-1}$，则
$$
\boxed{
\|S\|\,\|S^{-1}\|
\ge
\frac{s(s-1)}{4(2s-1)m^2}\,
\frac{\alpha_0}{\alpha_{m-1}}.
}
\tag{1.3}
$$
特别，对两个模型分别取所有链权及所有相似矩阵的下确界，有
$$
\boxed{
\lim_{m\to\infty}
\frac{1}{16^m}
\inf_{S,\gamma:\ T_m=SJ_\gamma S^{-1}}
\log\bigl(\|S\|\,\|S^{-1}\|\bigr)
=\frac{35}{6}.
}
\tag{1.4}
$$
下界允许链权任意依赖 $m$、大小极端不均或复数；上界由 R249 的明确实矩阵和常权链给出。这里未规定目标链范数。

## 2. 所有头链次数算子的精确形式

令 $Q_d=\operatorname{diag}(0,1,\ldots,d-1)$。对任意上述链，
$$
[Q_d,J_\gamma]=-J_\gamma.
$$
故 $A=SQ_dS^{-1}$ 满足
$$
[A,T_m]=-T_m,\qquad
\|A\|\le(d-1)\|S\|\,\|S^{-1}\|.
\tag{2.1}
$$
其中 $[X,Y]=XY-YX$。

写 $f=f_m$。因 $f(0)=0$、$f'(0)=\beta\ne0$，定义形式多项式
$$
\phi(z)=\frac{f(z)}{z f'(z)}\pmod {z^d},
\qquad \phi(0)=1.
\tag{2.2}
$$
分母 $f'(z)$ 的常数项非零，故这一式完全是有限代数运算。由 $[Q_d,B_m]=-B_m$，
$$
[Q_d\phi(B_m),f(B_m)]
=-B_m f'(B_m)\phi(B_m)=-f(B_m).
$$
因此 $A-Q_d\phi(B_m)$ 与 $T_m$ 交换。

有限形式逆把 $B_m$ 表成 $T_m$ 的多项式。于是 $T_m$ 与 $B_m$ 的交换子代数相同。$B_m$ 的所有链权非零，属于单个长度 $d$ 的幂零链；其交换子恰为次数小于 $d$ 的多项式。由此存在 $p(z)=\sum_{k<d}p_kz^k$ 使
$$
\boxed{A=Q_d\phi(B_m)+p(B_m).}
\tag{2.3}
$$
这不是仅为 R249 的一组特定换元矩阵求公式，而是涵盖全部目标链和相似矩阵。

若 $\phi(z)=\sum_{k<d}\phi_kz^k$，(2.3) 在第 $k$ 条上对角线给
$$
A_{r,r+k}=(r\phi_k+p_k)\frac{W_{r+k}}{W_r}.
\tag{2.4}
$$

## 3. 两个完全相同的真实权积消掉自由多项式

取 $k=s-1$。对 $1\le t<s$，$v_2(s+t)=v_2(t)$，所以
$$
\frac{W_{2s-1}}{W_s}=W_{s-1}.
$$
在 (2.4) 中分别取 $r=0$、$r=s$，得到
$$
A_{0,s-1}=p_kW_{s-1},\qquad
A_{s,2s-1}=(s\phi_k+p_k)W_{s-1}.
$$
两个矩阵条目都在 $d\times d$ 头内，且二者之差准确等于
$$
A_{s,2s-1}-A_{0,s-1}=s\phi_{s-1}W_{s-1}.
$$
每个条目的绝对值至多 $\|A\|$，故
$$
\boxed{\|A\|\ge\frac{s}{2}|\phi_{s-1}|W_{s-1}.}
\tag{3.1}
$$
因此不论如何加入与 $T_m$ 交换的自由多项式，都不能同时消掉这两个条目。

## 4. 最高位贡献与低头误差的准确分离

除去最高位 $j=m-1$，令 $f_<(z)$ 是 (1.2) 中 $j<m-1$ 的同一个真实符号，并置
$$
g(z)=\beta^{-1}f(z),\qquad
g_<(z)=\beta^{-1}f_<(z),\qquad
A_s=a_{m-1}e^{\Lambda_{m-1}-20}.
$$
两个模型统一满足
$$
g(z)=g_<(z)+A_s z^s+O(z^{s+1}),\qquad
g_<(z)=z+O(z^2).
\tag{4.1}
$$
对 $Y$ 模型，最高位的下一项次数是 $2s=d$，因此不会影响所需系数；低位 Cayley 分母仍全部保留在 $g_<$ 中。

定义
$$
\phi_<(z)=\frac{g_<(z)}{z g_<'(z)}.
$$
在 (4.1) 中写 $g_<=zu$、$u(0)=1$，直接展开
$$
\frac{u+A_s z^{s-1}}
 {u+zu'+sA_s z^{s-1}}
$$
到次数 $s-1$，得到准确恒等式
$$
\boxed{
\phi_{s-1}=(\phi_<)_{s-1}-(s-1)A_s.
}
\tag{4.2}
$$
下节只需把全部低头系数的合贡献付清。

## 5. 低头圆盘界与全部 $m\ge2$ 的主项支配

先取 $m\ge3$，故 $s\ge4$。令
$$
L_<=100\,\frac{(s/2)^4}{s/2-1}
=\frac{25}{2}\frac{s^4}{s-2},
\qquad \rho_<=e^{-L_<}.
$$
写
$$
\widetilde g_<(z)=\rho_<^{-1}g_<(\rho_<z)
=z+\sum_{n\ge2}c_nz^n.
$$
对两个模型，全部 $n\ge2$ 均有 $|c_n|\le1$。为避免误用仅模 $z^s$ 的旧系数结论，说明如下。

对 $i\ge1$、$i<m-1$，
$$
\frac{\Lambda_i}{2^i-1}\le L_<.
$$
这是 $\Lambda_i\le100\,16^i$ 与 $16^i/(2^i-1)$ 随 $i$ 增大所得。若 $2^i\mid n$，则 $n\ge2^i$，从而
$$
\frac{n}{2^i}\Lambda_i\le L_<(n-1).
$$
$i=0$ 的项有 $20n\le40(n-1)\le L_<(n-1)$。因此 $N$ 的单项系数或 $Y$ 的准确几何级数系数，在乘上 $e^{-20}a_i$ 后绝对值之和不超过
$$
e^{-20}\sum_{i<m-1}a_i\,e^{L_<(n-1)}
<e^{L_<(n-1)}.
$$
这证明所述全系数界，也保证缩放低头函数在 $|z|<1$ 全纯。

在 $|z|=1/4$，有
$$
|\widetilde g_<(z)/z|\le\frac43,
\qquad
|\widetilde g_<'(z)-1|
\le\sum_{n\ge2}n\,4^{-(n-1)}
=\frac79.
$$
故
$$
\left|\frac{\widetilde g_<(z)}
 {z\widetilde g_<'(z)}\right|\le6.
$$
Cauchy 系数界及缩放关系给
$$
\boxed{
|(\phi_<)_{s-1}|
\le6\,4^{s-1}e^{L_<(s-1)}.
}
\tag{5.1}
$$

由准确 $\Lambda_{m-1}$ 和 $s\ge4$，
$$
\begin{aligned}
\Lambda_{m-1}-L_<(s-1)
&\ge100s^4-105s^3-25s^4\\
&\ge\frac{195}{4}s^4.
\end{aligned}
$$
另一方面，$m\le s$、$\log4<3/2$、$\log12<3$ 给
$$
20+\log12+(s-1)\log4+2\log m-\log(s-1)
\le10s.
$$
由于 $(195/4)s^4>10s$，(5.1) 严格小于
$$
\frac12(s-1)m^{-2}e^{\Lambda_{m-1}-20}
=\frac12(s-1)A_s.
$$

剩余 $m=2$、$s=2$ 可直接检查。$N$ 的低头为 $g_<(z)=z$，所以 $(\phi_<)_1=0$；$Y$ 的低头为 $g_<(z)=z/(1+e^{20}z)$，所以 $\phi_<(z)=1+e^{20}z$。又 $\Lambda_1=1110$，故 $A_s=e^{1090}/4$，仍有 $|(\phi_<)_1|\le A_s/2$。

综上，全部 $m\ge2$、两个真实模型都满足
$$
\boxed{
|\phi_{s-1}|\ge\frac12(s-1)A_s
=\frac{s-1}{2m^2}\frac{\alpha_0}{d_{m-1}}.
}
\tag{5.2}
$$

## 6. 相似下界与最优主指数

将 (5.2) 代入 (3.1)，并用 $d_{m-1}=W_s=\alpha_{m-1}W_{s-1}$，得到
$$
\|A\|\ge
\frac{s(s-1)}{4m^2}\frac{\alpha_0}{\alpha_{m-1}}.
$$
再用 (2.1)，即为 (1.3)。

准确地，取 $d=2^m$，
$$
-\log\alpha_{m-1}
=\frac{35}{6}d^4-\frac{45}{4}d^3+150d-\frac{850}{3}.
$$
因此 (1.3) 给任何允许相似的统一下界
$$
\begin{aligned}
\log\bigl(\|S\|\|S^{-1}\|\bigr)
\ge{}&
\frac{35}{6}d^4-\frac{45}{4}d^3+150d-\frac{850}{3}-20\\
&+\log\frac{s(s-1)}{4(2s-1)m^2}.
\end{aligned}
\tag{6.1}
$$
R249 已构造一个常权链相似满足
$$
\log\bigl(\|S_m\|\|S_m^{-1}\|\bigr)
\le\frac{35}{6}d^4+O(d^3+md).
$$
上下界除以 $d^4=16^m$ 后夹逼，得到 (1.4)。

## 7. 对当前能量接口的含义

R249 的平衡矩阵已在所有非零单链权中达到最优的条件数主指数。仅通过再次缩放列、换成非恒定链权或加入与头算子交换的多项式，不可能把这一主指数降为 $o(16^m)$。

本结论没有证明移动能量中的真实核尾必须支付这个最坏环境条件数。它不排除核向量专属的头分布估计、不同正能量截断、非单链模型或其他无需环境相似范数的证明。特别，它既不证明 $N=M$，也不构造非零 $M\ominus\overline{BM}$。

