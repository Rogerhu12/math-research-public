# R467 补充：原混合 j 格的全分支次数界

日期：2026-11-14。以下为 R467 的完整补充证明，不另设结果编号。仍只约束真实有限来源中的首核和原真正第二核，不给新增来源、因子或乘积赋中央零。

## 原混合来源及完整次数

取原 $0\le j\le J\le16$，既可使用原
$\mathcal W_{D,J}=\bigoplus\mathscr R^nq_n\mathcal O[t]_{\le e_{n+1}}T^j$，也可使用 R453 的计算来源
$\widetilde{\mathcal W}_{D,J}=\bigoplus\mathscr R^nq_n\mathcal O[t]_{\le e_{n+1}+6j}T_0^j$。
后者保留每个 $j$ 的全部额外 $6j$ 角次数和一次整返回成本；它不是新增的算术中央对象。

直接用原 $X=\Theta$，而不新加 Kummer 变量。实际恒等式为
$$
\mathscr R^nq_nT^j
=7^{-j}X^{17n+36j}
d^{n-C_n+j}(th_7)^{A_n+j}(t-1)^{B_n+j}V^j.
\tag{1}
$$
因为 $n-C_n+j\ge0$，每一列已经是 $t,X$ 的真实多项式，毋须清新的角分母。原 $T$ 的 $V^j$ 六次成本恰与 $T_0$ 扩格的 $6j$ 多项式成本相同。因此两个整个实际格都满足
$$
\boxed{\deg_XP\le N=17D+36J,\qquad
\deg_tP\le M=\lfloor11D/2\rfloor+4+11J.}
\tag{2}
$$
本补充使用 $N<p$。它在固定 $J$、$D\asymp\sqrt p$ 的渐近临界区成立，但不能由 $f_D<p$ 在全部范围直接替代。没有把原混合格改成 (2) 内任意多项式。

## 原 Theta 方程与分支共振

原 $Z=\log\Theta$ 满足
$$
6t(1-t)Z''+(5-8t)Z'=2/3.
$$
所以对应 R467 的方程取
$$
A=6t(1-t),\qquad B=5-8t,\qquad C=2/3,
$$
$$
\mathscr D_\Theta(X)=A(XX''-(X')^2)+BXX'-CX^2.
\tag{3}
$$
其正规对数导数的递推是
$$
v_0=2/15,\qquad (6n+5)v_n=(6n+2)v_{n-1}.
$$
在 $n=s-1$ 处仍有同一个非零首共振。对 $t=u^e$、$p\nmid e$ 的单位分支，$X'/X\in u^{1-e}k[[u]]$；R467 的整数幂平均仍落在 $k[[t]]$、保留常数右端 $2/3$，所以不存在 tame 单位解。

原 regularized 轴是 $(g/d)^{1/17}$，其次数小于 $s$ 的系数与原 $\Theta$ 完全相同。这里的十七次根由原点值一唯一确定；$17$ 为单位。没有更换固定原来源的高轴，也没有把该形式根另计为免费来源。

设不可约 $F(t,X)$ 经过 $(0,1)$，记
$a=\deg_tF,b=\deg_XF$，$c$ 是 $F(0,X)$ 在 $X=1$ 的重数。由 $b\le N<p$，R467 的 tame 分裂、Hensel 因子和判别式证明全部适用。唯一的次数改变是 (3) 的 $A,B,C$ 比 R467 各低二次：其隐式多项式 $K_F$ 满足
$$
\deg_tK_F\le3a,\qquad \deg_XK_F\le3b-1,
\qquad \deg_t\operatorname{Res}_X(F,K_F)\le a(6b-1).
$$
全部局部分支共同的判别式仍支付 $3(c-1)$ 阶，因而
$$
\boxed{\min\{\operatorname{ord}_tF(t,\Theta_{\rm reg}),s\}
\le a(6b-1)-2c+3\le a(6b-1)+1.}
\tag{4}
$$
若 $b=1$，用 $F=uX-v$ 的真实有理分支，$U=uv,W=v'u-u'v$。分子
$A(W'U-WU')+BWU-CU^2$ 的次数至多 $4a$，不再含旧 $d^2$ 的二次成本，所以更强地
$$
\boxed{b=1\quad\Longrightarrow\quad
\min\{\operatorname{ord}_tF(t,\Theta_{\rm reg}),s\}\le4a+1.}
\tag{5}
$$

## 原三块首核的全部接触因子

在 $t=0$，原混合格仍只允许 $j=0,n=0,1,2$，所以
$P(0,X)=c_0+c_1X^{17}+c_2X^{34}$。相对 Euler 是
$E=(X/17)\partial_X$，故三个真实 Gaussian 常数行仍给电荷 $0,1,2$ 的单位 Vandermonde。任何非零 $\bar P\in\ker\bar J$ 仍有 $t\mid\bar P$。

写全部实际分解
$$
\bar P=t^rQ\prod_iF_i^{\nu_i},\quad r\ge1,\quad Q(0,1)\ne0,
\quad F_i(0,1)=0.
$$
由 (2)，$\sum\nu_i a_i\le M-r$、$\sum\nu_i b_i\le N$。原第一块和 (4) 给
$$
s\le r+\sum_i\nu_i\{a_i(6b_i-1)-2c_i+3\}.
\tag{6}
$$
因此，只要所有接触因子的 $b_i\le B$，$B\ge1$，就有
$$
s\le(6B-1)M-(6B-2)r+N
\le(6B-1)M+N-6B+2,
$$
即
$$
\boxed{p\le(36B-6)M+6N-36B+11.}
\tag{7}
$$
当 $p>6M-1$ 时，纯角情形已经排除，故确有接触因子且
$$
\boxed{\max_i b_i\ge
\left\lceil\frac{p+6M-6N-11}{36(M-1)}\right\rceil.}
\tag{8}
$$
若全部接触因子对原 $\Theta$ 都是一次，用 (5) 得
$$
s\le4M-3r+N\le4M+N-3,
$$
所以
$$
\boxed{p\le24M+6N-19\le234D+480J+77.}
\tag{9}
$$
对 $J=0$ 应优先使用 R467 的原 $Y=\mathscr R$ 界，保留它已经支付的十七倍次数节省；本补充没有用较弱的 $\Theta$ 矩形覆盖掉那项改进。

最后，R449 的 $K_2^{\rm red}(M^{\rm orig})\subset\ker\bar J$ 使上述条件同样适用于原真正第二核。完整 $P_{134}/U_0$、总 charge 四十、初始十三自由行及两条十三行 carry 都按原整运输保留。对于 R453 扩格，回到旧格时仍支付其固定次数、目标行和 carry 成本。式 (7)–(9) 仍允许高径向次数的临界分支，尚未把两个原完整中央失败接入该实际像问题。
