# R239 附录：全尾保持 D 核的 D3 原像及相容链的方差下界

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；AI 辅助：GPT-6 Astra Pro。root 已全文核验前缀共原始源、重叠常数及全尾对偶。
状态：下述全尾最小原像与相容链的下界已证明。它不把所造局部源认作某个实际 $w\in M$ 的残量，也不推出无权核内饱和失败。

## 1. 对象及所补的范围

令 $m\ge5$、$q\ge8$，并记
$$
a_j=(j+1)^{-2},\qquad
D=\sum_{j\ge m}a_jE_j,\qquad
D_3=\sum_{j\ge m}a_j^3E_j,\qquad J=m+2q.
$$
将前缀 $I=[m,J)$ 分成 $q$ 个相邻二位块，远尾为 $[J,\infty)$。
固定孔层的全尾满射及真正最小右逆已由
[R271 全尾双行稿](R271-appendix-full-tail-two-row-fixed-layer-range-and-contractive-known-images.md)
证明。本文只补充一般全尾右逆必须支付的一个下界。

沿用
[R271 远尾双行稿](R271-appendix-far-tail-two-row-hodge-inverse-and-optimal-joint-vacuum-jets.md)
的记号
$$
S_{2r}(J)=\sum_{j\ge J}a_j^{2r},\qquad
\mu=\frac{S_4(J)}{S_2(J)},\qquad
V_J=S_6(J)-\frac{S_4(J)^2}{S_2(J)}.
\tag{1.1}
$$
这里 $V_J>0$，并且
$$
V_J=\left(\frac{16}{539}+O(J^{-1})\right)J^{-11}.
\tag{1.2}
$$
下文的源属于完整 $D_m$ 的真实核，原像也允许使用整个 $[m,\infty)$，并非被限制为在远尾真空上创建。

## 2. 固定一个 D-原始源

对每个二位块 $(j,j+1)$，$j=m,m+2,\ldots,J-2$，令
$$
h_j=\frac{a_{j+1}|10\rangle-a_j|01\rangle}
{\sqrt{a_j^2+a_{j+1}^2}}.
$$
则 $(a_jE_j+a_{j+1}E_{j+1})h_j=0$。定义
$$
h_{m,q}=\bigotimes_{j=m,m+2,\ldots,J-2}h_j
\ \otimes\Omega_J.
\tag{2.1}
$$
因此
$$
\|h_{m,q}\|=1,\qquad
h_{m,q}\in\ker D\cap\mathcal H_q^{(m)}.
\tag{2.2}
$$

为得到保持 $D$-核时的准确远尾方差，使用同一完整算子
$$
C=D_3-\mu D=\sum_{j\ge m}c_jE_j,\qquad
c_j=a_j(a_j^2-\mu).
\tag{2.3}
$$
积分比较给
$$
\mu\le\frac{3(J+1)^3}{7J^7},\qquad
\mu J^4\le\frac37(1+1/J)^3<\frac12
\quad(J\ge21).
\tag{2.4}
$$
本稿的 $m\ge5,q\ge8$ 确保 $J\ge21$。
对 $j<J$，$a_j^2\ge J^{-4}$，所以 $c_j>0$。

每个二位块取单位共原始向量
$$
g_j=\frac{c_j|10\rangle-c_{j+1}|01\rangle}
{\sqrt{c_j^2+c_{j+1}^2}},
\qquad
g_{m,q}=\bigotimes_jg_j\otimes\Omega_J.
\tag{2.5}
$$
直接计算
$$
(c_jE_j^*+c_{j+1}E_{j+1}^*)g_j=0,
\qquad C_I^*g_{m,q}=0.
\tag{2.6}
$$
此处共原始使用 $C=D_3-\mu D$，而不是 $D$ 或未减去均值的 $D_3$。

## 3. 两个真实前缀向量的重叠趋于一

记
$$
\rho_{m,q}=\langle h_{m,q},g_{m,q}\rangle
=\prod_j
\frac{a_{j+1}c_j+a_jc_{j+1}}
{\sqrt{a_j^2+a_{j+1}^2}\sqrt{c_j^2+c_{j+1}^2}}.
\tag{3.1}
$$
各因子均正。对一个块令
$$
u=\log(a_j/a_{j+1}),\qquad v=\log(c_j/c_{j+1}).
$$
由 $a_j=(j+1)^{-2}$，
$$
0\le u\le\frac2{j+1}.
$$
再考虑 $c(x)=x^{-6}-\mu x^{-2}$。在 $j+1\le x\le j+2\le J$ 上，
$\mu x^4\le1/2$，故
$$
-\frac{d}{dx}\log c(x)
=\frac{6+4\mu x^4/(1-\mu x^4)}x\le\frac{10}x.
$$
所以
$$
0\le v\le\frac{10}{j+1}.
\tag{3.2}
$$
(3.1) 的单块因子准确等于
$$
\frac{\cosh((u-v)/2)}{\sqrt{\cosh u\cosh v}}.
$$
使用 $\log\cosh x\le x^2/2$，得到
$$
\log\rho_j\ge-\frac{u^2+v^2}{4}
\ge-\frac{26}{(j+1)^2}.
$$
而相邻块起点的和满足
$$
\sum_{\ell\ge0}\frac1{(m+1+2\ell)^2}
\le\frac1{(m+1)^2}+\frac1{2(m+1)}
\le\frac{2}{3(m+1)}.
$$
因此可统一取
$$
\boxed{e^{-20/(m+1)}\le\rho_{m,q}\le1.}
\tag{3.3}
$$
尤其在原全整数头 $m=m(q)\to\infty$ 下，$\rho_{m,q}=1-o(1)$，不需对 $q$ 另加与源有关的假设。

## 4. 允许整个尾空间，仍须支付同一方差

设 $t\ge1$，且
$$
v\in\mathcal H_{q+t}^{(m)},\qquad Dv=0,\qquad D_3^tv=h_{m,q}.
\tag{4.1}
$$
因为 $D,D_3$ 交换，(4.1) 给
$$
C^tv=(D_3-\mu D)^tv=D_3^tv=h_{m,q}.
\tag{4.2}
$$
由 (2.6) 和不交物理位的交换关系，
$$
(C^*)^tg_{m,q}
=\left(\bigotimes_jg_j\right)\otimes(C_J^*)^t\Omega_J.
\tag{4.3}
$$
远尾 $c_j$ 可有两种符号，这不影响正交有限子集展开：
$$
\|(C_J^*)^t\Omega_J\|^2
=(t!)^2 e_t((c_j^2)_{j\ge J})
\le t!\left(\sum_{j\ge J}c_j^2\right)^t
=t!V_J^t.
\tag{4.4}
$$
最后一步使用 (1.1) 中的最小方差选择 $\mu=S_4/S_2$。

配对 (4.2)，得到
$$
\rho_{m,q}
=|\langle v,(C^*)^tg_{m,q}\rangle|
\le\|v\|\sqrt{t!V_J^t}.
$$
所以
$$
\boxed{\|v\|\ge
\frac{\rho_{m,q}}{\sqrt{t!}\,V_J^{t/2}}
\ge\frac{e^{-20/(m+1)}}{\sqrt{t!}\,V_J^{t/2}}.}
\tag{4.5}
$$
这是对全部满足 (4.1) 的全尾原像成立的下界；
证明中没有假定 $v$ 在前缀上保持张量形式，没有把它限制在远尾创建空间内。
事实上这段配对也没有使用 $v$ 的固定孔层条件；对任意 $v\in\ker D$ 且 $D_3^t v=h_{m,q}$，同一下界仍成立，因为所有算子有界且 (4.2)--(4.4) 原样适用。

特别，对真正最小右逆，
$$
\boxed{
\|R^{(3),\min}_{m,q}h_{m,q}\|
\ge\rho_{m,q}V_J^{-1/2},
\qquad
\|R^{(3),\min}_{m,q}\|\ge\rho_{m,q}V_J^{-1/2}.
}
\tag{4.6}
$$
沿 $m(q)$，
$$
\|R^{(3),\min}_{m(q),q}\|
\ge(1-o(1))\frac{\sqrt{539}}4
\bigl(m(q)+2q\bigr)^{11/2}.
\tag{4.7}
$$

## 5. 同一源的全部相容链

若
$$
v_0=h_{m,q},\qquad
Dv_t=0,\qquad D_3v_t=v_{t-1},
\qquad v_t\in\mathcal H_{q+t}^{(m)}
\quad(1\le t\le\nu),
$$
则 $D_3^tv_t=h_{m,q}$，每一层都适用 (4.5)。不同层正交，因此
$$
\boxed{
\sum_{t=1}^{\nu}\|v_t\|^2
\ge\rho_{m,q}^2\sum_{t=1}^{\nu}\frac1{t!V_J^t}.
}
\tag{5.1}
$$
固定孔层满射逐次应用保证此类有限链确实存在；(5.1) 是所有这样的链共同满足的最小能量下界。

若 $\nu\le2d=O((\log q)^{1/3})$ 且 $m=m(q)$，由 (1.2)、(3.3) 可将 (4.5) 统一写为
$$
\|v_t\|\ge(1-o(1))
\frac{(\sqrt{539}/4)^t J^{11t/2}}{\sqrt{t!}},
\qquad 1\le t\le\nu.
\tag{5.2}
$$
这里一致误差只需 $\nu/J\to0$，当前窗口满足。

## 6. 对已知像收缩与实际源的含义

R271 全尾稿证明
$$
R^{(3),\min}_{m,q}D_3f
=P_{(\ker D)\ominus(\ker D\cap\ker D_3)}f
$$
（在相应固定输入层上），因此它对已知像是收缩。这与 (4.6) 不冲突：
若 $D_3f=h_{m,q}$、$Df=0$，那么 $f$ 本身已经必须支付 (4.5) 的一次成本。

本稿的源虽然是完整 $D_m$ 的真实一阶核向量，但没有证明它来自实际 $M$ 的低输出投影或最优联合旗通量。
因此 (4.7) 不能用来反驳实际源上的更好预算；它指出一般逆范数无法代替真正已知像的范数控制。
当前仍需把真实 $w\in M\ominus N$ 的测试域、最优链和已知像的收缩联系起来。
