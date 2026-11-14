# R234 第二附录：四次头幂将孔次数权阶降至任意 p>4/3

日期：2026-11-13（Asia/Taipei）。作者：boundary。状态：已证明。

本稿的“权阶”指 $e^{c(q+1)^p}$ 中的幂 $p$；新的有效范围是 $p>4/3$。

R234 的实际右逆构造保持不变，只改进其有限头幂的范数预算。由真实二进制 carry 得到四次衰减后，同一个逐层右逆满足
$\log\|R_q\|=O(((q+1)\log(q+2))^{4/3})$。
原来的全部 carry 误差及输出次数预算继续适用。结合已证高位夹置接口，形式原像和正则核的结论可从三次权降到每个 $p>4/3$，并给未知缺陷的次数尾下界。

## 1. 沿用 R234 的原算子

对两个边界慢符号
$$
T_N=\sum_{j\ge0}a_jN_j,\qquad
T_Y=\sum_{j\ge0}a_jN_j(I+N_j)^{-1},\qquad
a_j=(j+1)^{-2},
$$
仍记 $T_m=T|_{\mathcal F_m}$。R234 的逐尾次数右逆为
$$
D_{\ge m}Q_{m,s}=I,\qquad
\|Q_{m,s}\|\le
\kappa_{m,s}:=[10000(m+s+1)^2]^{s+1}.
\tag{1.1}
$$
$\mathcal Q_m$ 表示把这些 $Q_{m,s}$ 按尾孔次数拼起来的算子。它与有限头 $T_m$ 交换。

保持原来的
$$
m=m(q)=10+\lceil\log_2(q+1)\rceil,\qquad
d=d(q)=2^m,
$$
$$
R_q=
\left.\sum_{k=0}^{d-1}(-T_m)^k\mathcal Q_m^{k+1}\right|_{H_q}.
\tag{1.2}
$$
这些是原有的实际有界算子，不是重新选取的右逆。R234 已证
$$
1024(q+1)\le d<2048(q+1),
\tag{1.3}
$$
输出次数不超过
$$
r_q=q+m+d,
\tag{1.4}
$$
且对于原三次权空间 $\mathscr X_{1,3}$，
$$
\boxed{
\|(TR_q-I)v\|_{\mathscr X_{1,3}}
\le2e^{-40d(q)^4}\|v\|.
}
\tag{1.5}
$$
本稿没有改变 (1.5) 的实际误差。

## 2. 有限头全部高幂的真实四次衰减

**引理 2.1。** 设
$$
\gamma=\frac{770}{16^4}.
$$
对两种模型，
$$
\|T_m^k\|\le6^k\quad(k\ge0),
$$
并且当 $k\ge\max(2m,16)$ 时，
$$
\boxed{\|T_m^k\|\le6^k e^{-\gamma k^4}.}
\tag{2.1}
$$

证明：先对单项 $\prod_{j<m}N_j^{k_j}$ 作完整实际进位，记 $k=\sum_jk_j$，$n=\sum_jk_j2^j$。令 $c_j$ 为第 $j$ 位往上的进位次数，$r_j\in\{0,1\}$ 为最后二进制位。真实关系 $N_j^2=\eta_jN_{j+1}$ 给
$$
\prod_{j<m}N_j^{k_j}
=\left(\prod_{j\ge0}\eta_j^{c_j}\right)
\prod_{j:r_j=1}N_j.
\tag{2.2}
$$
总进位数满足
$$
C_{\rm car}:=\sum_jc_j
=k-\operatorname{popcount}(n).
$$
由于 $n\le k2^{m-1}$，
$\operatorname{popcount}(n)\le m+\lfloor\log_2k\rfloor$。
当 $k\ge2m$ 且 $k\ge16$ 时，
$$
C_{\rm car}\ge k/4.
\tag{2.3}
$$

置 $E_{\rm car}=\sum_j16^jc_j$。进位递推还给
$$
c_{j+\ell}\ge\left\lfloor c_j/2^\ell\right\rfloor.
$$
当 $c_j\ge1$，取 $\ell=\lfloor\log_2c_j\rfloor$，得
$$
E_{\rm car}\ge16^{j+\ell}\ge16^j(c_j/2)^4.
$$
因此 $c_j\le2E_{\rm car}^{1/4}2^{-j}$；求和得
$C_{\rm car}\le4E_{\rm car}^{1/4}$。与 (2.3) 合并，
$$
E_{\rm car}\ge(k/16)^4.
$$
利用 $\eta_j\le e^{-770\,16^j}$ 与 $\|N_j\|=1$，(2.2) 的范数至多 $e^{-\gamma k^4}$。

对 $T_N$，多项式系数绝对和为 $(\sum_{j<m}a_j)^k<2^k$。对 $T_Y$，全部实际逆彼此交换，每个单项的逆总次数是 $k$，所以只付 $3^k$；加上系数和至多为 $6^k$。这得到全空间有限和的界。有限头算子是这些真实算子在不变 $\mathcal F_m$ 上的限制，故同界成立。若进位已越过第 $m$ 位，有限头上的该项直接为零，不会增加误差。证毕。

在 (1.2) 中 $m\ge10$，所以高幂阈值就是 $k\ge2m$。

## 3. 对原逐层右逆的全部 $k$ 区间求和

记
$$
\ell_q=\log(q+2),\qquad t_q=(q+1)\ell_q,\qquad A=81960.
$$
先对每个 $0\le k<d$ 估计实际 $\mathcal Q_m^{k+1}$。输入尾次数至多为 $q$，每次只升一次数，所以由 (1.1)，
$$
\|\mathcal Q_m^{k+1}|_{H_{\le q}\ {\rm tail}}\|
\le\prod_{\nu=0}^k\kappa_{m,q+\nu}.
\tag{3.1}
$$
因 $m+q+d+1<2d<4096(q+1)$，
$$
\log[10000(m+q+d+1)^2]\le40\ell_q.
\tag{3.2}
$$
例如 $\log10000<14\log2$、$2\log4096=24\log2$，足以核对 (3.2)。
又 $q+k+1\le q+d\le2049(q+1)$。于是
$$
\begin{aligned}
\log\prod_{\nu=0}^k\kappa_{m,q+\nu}
&\le(k+1)(q+k+1)\log[10000(m+q+d+1)^2]\\
&\le A(k+1)t_q.
\end{aligned}
\tag{3.3}
$$
这是对全部 $k<d$ 的统一界，未在优化前遗漏靠近 $d$ 的项。

### 3.1. 高幂段 $k\ge2m$

因为 $t_q\ge\log2$，有 $k\log6\le3t_qk$。由 (2.1)、(3.3)，第 $k$ 项的对数范数至多
$$
A t_q+(A+3)t_qk-\gamma k^4.
\tag{3.4}
$$
对任意 $b\ge0$，实变量优化准确给
$$
\sup_{x\ge0}(bx-\gamma x^4)
=\frac{3}{4^{4/3}\gamma^{1/3}}\,b^{4/3}.
\tag{3.5}
$$
所以全部高幂项均不超过 $\exp(C_{\rm hi}t_q^{4/3})$，其中 $C_{\rm hi}$ 是固定常数。

### 3.2. 低幂段 $0\le k<2m$

这里不用未达到阈值的四次界，只用 $\|T_m^k\|\le6^k$。
由 $m\le11+\log_2(q+1)\le18\ell_q$，以及 $k+1\le2m$，(3.3) 给
$$
\log\|T_m^k\mathcal Q_m^{k+1}\|
\le36(A+3)t_q\ell_q.
$$
对 $x\ge1$，$\log(1+x)\le\sqrt x$，故
$\ell_q^2\le q+1$，从而 $\ell_q\le t_q^{1/3}$。因此低幂段也统一满足
$$
\log\|T_m^k\mathcal Q_m^{k+1}\|
\le36(A+3)t_q^{4/3}.
\tag{3.6}
$$

最后，项数 $d$ 的对数仅为 $O(t_q)$。所以存在一个绝对有限常数 $K$，使
$$
\boxed{\|R_q\|\le\exp(Kt_q^{4/3})
=\exp\!\left(K((q+1)\log(q+2))^{4/3}\right).}
\tag{3.7}
$$
例如可以取
$$
K=(A+12)(\log2)^{-1/3}
+36(A+3)
+\frac{3(A+3)^{4/3}}{4^{4/3}\gamma^{1/3}}.
$$
常数很宽松，但独立于 $q,m$；所有 $k$ 区间均已控制。

## 4. 右逆及形式原像的权阶降到每个 $p>4/3$

定义
$$
\mathscr X_{c,p}=
\left\{f:\sum_{q\ge0}e^{c(q+1)^p}\|\mathsf P_qf\|<\infty\right\}.
$$
先取 $4/3<p\le3$、$0<c\le1$。由
$$
((q+1)\log(q+2))^{4/3}=o((q+1)^p),
$$
(3.7) 使原来的 $R=\sum_qR_q\mathsf P_q$ 有界
$\mathscr X_{c,p}\to H_-$。另一方面，此权逐点不超过原三次权，故由 (1.5)，同一 $E=TR-I$ 满足
$$
\|E\|_{\mathscr X_{c,p}\to\mathscr X_{c,p}}
\le2e^{-40\cdot1024^4}<1/4.
$$
因此
$$
\boxed{
\mathcal G_{c,p}=R(I+E)^{-1}:\mathscr X_{c,p}\to H_-,
\qquad T\mathcal G_{c,p}=I.
}
\tag{4.1}
$$
全部这些扩张在有限输入上与原 R234 构造相同；没有改动 $R_q$ 或实际误差 $E$。

以下把已证高位夹置机制的关键条件逐一核清。令 $\mathscr X_{c,p}^+$ 的权为 $e^{c(q+2)^p}$。
$N_i\mathcal G_{c,p}E_i^*$ 在这个空间上一致有界，且
$$
T N_i\mathcal G_{c,p}E_i^*=N_iE_i^*
=I-E_i^*E_i.
$$
取弱算子聚点得有界右逆 $C_{c,p}$。对有限 $v$，
$N_i\mathcal G_{c,p}E_i^*v-J_Tv$ 最终属于
$M\cap\operatorname{Ran}B\subset N$，故
$C_{c,p}v-J_Tv\in N$。

对任意 $a>0$、$0<c<\min(a,1)$，局部 carry 分解
$T=D+\sum K_L$ 仍给
$$
T:\mathscr X_{a,p}\longrightarrow\mathscr X_{c,p}^+
\quad\text{有界}.
\tag{4.2}
$$
确实，局部 $K_L$ 最多改 $L+1$ 孔，且对某些固定 $A,C$，
$$
\sup_q\sqrt{q+L+2}\,
e^{c(q+L+3)^p-a(q+1)^p}
\le Ce^{A(L+2)^p}.
$$
其证明与三次情形相同：选 $c<c'<a$，吸收平方根后，使用
$c'(y+1)^p-ay^p$ 的有限上界；$e^{-770\,16^{L-1}}$ 再支付全部 $L$ 和。
故有限头逼近给
$$
\boxed{M\cap\mathscr X_{a,p}\subseteq N
\qquad(a>0,\ 4/3<p\le3).}
\tag{4.3}
$$

原输出次数界 $r_q+1\le4096(q+1)$ 仍成立。取
$\gamma=c/(4\cdot4096^p)$，由 (3.7) 的 $o(q^p)$ 成本得到
$\mathcal G_{c,p}:\mathscr X_{c,p}\to\mathscr X_{\gamma,p}$ 有界。
因此有限 $v$ 的原始右逆差
$\mathcal G_{c,p}v-J_Tv$ 在 $M\cap\mathscr X_{\gamma,p}$，由 (4.3) 属于 $N$。

对 $w\in W$ 的形式原像 $T^*h=w$，有限测试配对遂合法给
$$
\boxed{
h_q=(\mathcal G_{c,p}|_{H_q})^*w,\qquad
\|h_q\|\le\|\mathcal G_{c,p}\|e^{c(q+1)^p}\|w\|.
}
\tag{4.4}
$$
这仍是完整固定次数层的 Hilbert 空间结论，不是全 $h\in H_-$。

对 $p>3$，(4.3)—(4.4) 直接由任何较小的已证指数推出；无需另为更强权重声称原 $E$ 是收缩。因此最终有效范围确为任意 $p>4/3$。$c>1$ 的层上界也由一个较小正 $c$ 的结论立即推出。

## 5. 真正缺陷向量的孔次数尾下界

以下仍用 $4/3<p\le3$、$0<c\le1$，记
$G=\|\mathcal G_{c,p}\|$，并取非零 $w\in W$，先归一化为 $\|w\|=1$。
设 $q\ge1$，并令
$$
u_q=\sum_{r=0}^q\mathsf P_rw,\qquad
\tau_q=\|w-u_q\|.
$$
$u_q$ 的孔次数有限，位置仍可无限。由 (4.2)，有限整数头在这固定次数空间的逼近可经 $T$ 连续送入 $\mathscr X_{c,p}^+$，所以第 4 节的稳定右逆满足
$$
u_q-C_{c,p}Tu_q\in N.
\tag{5.1}
$$
由 $w\perp N$，
$$
\|u_q\|^2
=|\langle C_{c,p}Tu_q,w\rangle|
\le G\|Tu_q\|_{\mathscr X_{c,p}^+}.
\tag{5.2}
$$

因为 $Tw=0$，低输出次数至多 $2q$ 的部分满足
$$
\left\|\sum_{r\le2q}\mathsf P_rTu_q\right\|_{\mathscr X_{c,p}^+}
\le6\sqrt{2q+1}\,e^{c(2q+2)^p}\tau_q.
\tag{5.3}
$$
高输出中，纯 $D$ 不可能从次数至多 $q$ 到达次数大于 $2q$。
局部 $K_L$ 要到达这些输出必须 $L\ge q$，故
$$
\left\|\sum_{r>2q}\mathsf P_rTu_q\right\|_{\mathscr X_{c,p}^+}
\le\delta_{q,c,p},
$$
其中
$$
\delta_{q,c,p}
=52\sum_{L\ge q}\sqrt{q+L+2}\,
e^{-770\,16^{L-1}+c(q+L+3)^p}
\longrightarrow0.
\tag{5.4}
$$
最后的趋零可直接用 $q\le L$：这是一个被
$\sqrt{2L+2}e^{-77016^{L-1}+c(2L+3)^p}$ 控制的可和级数尾。

最终 $\|u_q\|^2\ge1/2$，且 $G\delta_{q,c,p}\le1/4$。由 (5.2)—(5.4)，
$$
\boxed{
\tau_q\ge
\frac{e^{-c(2q+2)^p}}
{24G\sqrt{2q+1}}
\quad\text{对全部充分大的 }q.
}
\tag{5.5}
$$
充分大阈值可依赖固定 $w,c,p$，右侧常数不依赖 $q$。

因为可以任取正 $c$，(5.5) 特别给
$$
\boxed{
-\log\left\|\sum_{r>q}\mathsf P_rw\right\|=o(q^p)
\qquad\text{对每个 }p>4/3
}
\tag{5.6}
$$
（单位非零 $w\in W$）。因此非零缺陷的次数尾不能以任意正
$e^{-a q^p}$ 速度衰减，$p>4/3$。这个次数方向结论不同于 R214 的最高物理位尾。

## 6. 未覆盖的端点与主缺口

本稿没有证明临界权 $e^{c q^{4/3}}$ 上的右逆，因为 (3.7) 仍含 $(\log q)^{4/3}$；也未得到任何次数无关的右逆范数或 $\sum_q\|h_q\|^2<\infty$。

式 (5.6) 仍允许一般 $\ell^2$ 向量具有更慢次数尾，故没有给 $W=0$ 的矛盾。剩余需要使用新的分层 Hilbert 方程控制跨次数能量，或确实构造非零 $W$。原不变子空间问题未在本稿完成。

依赖：R234 原 $R_q$、局部误差及输出次数；高位夹置与三次正则核饱和附录；R200 的 $M\cap\operatorname{Ran}B\subset N$。新增有限头四次 carry 界与全部 $k$ 的成本优化已在本稿独立写全。
