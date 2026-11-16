# R860 — 原共同奇来源的 Frobenius 交叉项与完整平衡伙伴

日期：2026-11-16。**状态：已证明。** 本文证明原三差矩阵的完整乘法/热相容式，并把第一次平衡伙伴的二挠边界与剩余全纯来源全部写明。它不证明四个原中央值共同非消失；该问题仍在 open.md。

固定原 $p=6s-1>211$、单位 $b$、$y^2=x^3+b$ 及 $D_zx=2y$。
全部输入取自[原共同 C24 来源及三维差矩阵](../notes/2026-11-16-original-common-odd-degree24-and-three-row-pairing.md)：
$$
E_j=-b^j\sigma^{24}x^{8-3j}y,\quad j=0,1,2,\qquad
c_*=(1,-4/7,16/7)^t,\qquad C_{24}=\sum_jc_{*,j}E_j.
$$
四个伙伴 $J_\nu=\sigma^{n_\nu}S_\nu$ 是该来源的完整式(5)–(6)，
$n_S,n_T,n_U,n_V=10,48,112,42$，原 $A_\nu=C_{24}J_\nu$。
该来源式(16)定义原三差矩阵
$M_{\nu j}=\mathfrak B(E_jJ_\nu)-\mathfrak B(E_jJ_S)$，
$\nu=T,U,V$，且四个原中央首条件等价于其式(18)
$\mathfrak B_S=0,\ M_pc_*=0$。

为便于沿原来源追踪，本文保留续式号(37)–(58)；
对式(5)、(6)、(11)、(16)、(18)的引用均指上述来源注。
所用原 whole 整性及固定 Hasse 提升见
[R856](R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)，
完整热乘法见 [R855](R855-original-full-heat-connection-and-canonical-divided-jet.md)。
以下为代数恒等式证明，没有数学数值运行或素数扫描。

## 1. 同一三列的 Frobenius 乘法缺陷及完整热兼容

本节计算第(16)式的实际横向范围，不将原 CM 点上的一个零条件
自动延伸到参数方向。
记
$$
a=g_2/12,\quad H=\operatorname{Ha}_p,\quad C=LH,\quad
\mathcal R_p=(LC+aH)/p,
$$
并保持 R856 对这些特征零多项式的固定提升。
在物理变量的微分代数上先定义以下有理算子
$$
P_m=D_z^p-HD_z-mCz,\qquad
\mathscr D_m=P_m/p,\qquad
Q_m=L-\frac{D_z^2}{2m}-\frac{ma}{2}z^2.
\tag{37}
$$
$\mathscr D_m$ 在原 whole degree $m$ 整格上的整性是 R856 的 whole 定理；
这里不声称它在任意 Hurwitz 格上整。其固定值不能以更换 $H,C$ 的提升改变。直接计算 commutator 得到特征零恒等式
$$
\boxed{
[Q_m,\mathscr D_m]
=m\left\{
azD_z^{p-1}+\frac{p-1}{2}aD_z^{p-2}
-\mathcal R_pz
\right\}.
}
\tag{38}
$$
其中 $-CD_z$ 与 $+CD_z$ 正好相消，而
$LC+aH=p\mathcal R_p$ 产生最后一项。它不能在反复横向微分前冻结。

对两个物理输入，定义整多项式
$$
\mathfrak C_p(\xi_1,\xi_2)
=\frac{(\xi_1+\xi_2)^p-\xi_1^p-\xi_2^p}{p}
=\sum_{k=1}^{p-1}\frac1p\binom pk\xi_1^k\xi_2^{p-k}.
\tag{39}
$$
令 $\mu$ 表示 $z_1=z_2=z$ 的准确对角限制，$M=m+n$。
则有下列形式乘法恒等式；其三项除 $p$ 读数的整性在两输入分别属于
原 whole degree $m,n$ 格时由 R856 保证：
$$
\boxed{
\mathscr D_M(FG)
=(\mathscr D_mF)G+F(\mathscr D_nG)
+\mu\mathfrak C_p(D_1,D_2)(F\otimes G).
}
\tag{40}
$$
因此对(11)和(6)，
$$
\boxed{
M_{\nu j}=
\left.D_z\mu\mathfrak C_p(D_1,D_2)(E_j\otimes J_\nu)\right|_{z=0}
-\left.D_z\mu\mathfrak C_p(D_1,D_2)(E_j\otimes J_S)\right|_{z=0}
\pmod p.
}
\tag{41}
$$
这不是新行；它和(16)逐项相等。
准确的两个高端贡献因 $j_1(J_\nu)=j_1(J_S)=1$ 相消；
各自剩余的 $j_p(E_j)$ 又被 $p$ 整除。
不能给不同 degree 的 $J_\nu-J_S$ 配一个未定义的单一热算子；
以下热兼容对两项分别进行。

在双输入上用
$$
Q_{m,n}=L-\frac{D_1^2}{2m}-\frac{D_2^2}{2n}
-\frac a2(mz_1^2+nz_2^2),\qquad
K_{m,n}=\frac{(nD_1-mD_2)^2}{2mnM}.
$$
有准确的两个运输式
$$
Q_M\mu=\mu Q_{m,n}+\mu K_{m,n},\qquad
P_M\mu=\mu(P_m^{(1)}+P_n^{(2)})+p\mu\mathfrak C_p(D_1,D_2).
\tag{42}
$$
第一个式子的 $K_{m,n}$ 正是 R855 的完整平衡伙伴，
不是可删的零项。
而
$$
[K_{m,n},P_m^{(1)}+P_n^{(2)}]=0
\tag{43}
$$
在特征零中严格成立：$nD_1-mD_2$ 与
$mz_1+nz_2$ 交换，也与其它显示项交换。

若 $\partial_i$ 表示对多项式变量 $\xi_i$ 求导，
则还有完整式
$$
\boxed{
[Q_{m,n},\mathfrak C_p(D_1,D_2)]
=a\left\{
mz_1(\partial_1\mathfrak C_p)(D)
+nz_2(\partial_2\mathfrak C_p)(D)
+\frac{m(\partial_1^2\mathfrak C_p)(D)
      +n(\partial_2^2\mathfrak C_p)(D)}2
\right\}.
}
\tag{44}
$$
例如
$\partial_1\mathfrak C_p=(\xi_1+\xi_2)^{p-1}-\xi_1^{p-1}$，
其第二导数为
$(p-1)((\xi_1+\xi_2)^{p-2}-\xi_1^{p-2})$；
所有系数均整。

将(38)分别代入(42)，借(43)，恰回到(44)。
尤其其 $\mathcal R_p$ 项在对角上为
$$
-M\mathcal R_pz+m\mathcal R_pz+n\mathcal R_pz=0.
\tag{45}
$$
所以已付的 $\mathcal R_p/g_2^2$ 单位没有直接留下为
三差矩阵的一个常数 forcing。反过来，(44)的 $a$ 项
也不能因 $a(P)=0$ 被永久删掉，因为 $La(P)=-2b$ 是单位。
这精确标出本乘法缺陷的实际横向项。

## 2. 首次平衡伙伴的完整来源及非零二挠边界

现在不再只计算环境算子，而将(42)实际作用于每个 $E_j,J_\nu$。
写
$$
E_j=\sigma^{24}R_j,\quad R_j=-b^jx^{8-3j}y,\qquad
J_\nu=\sigma^{n_\nu}S_\nu,
$$
其中 $S_\nu$ 是(6)的完整多项式。
在原 CM 纤维用 $D=2y\partial_x+3x^2\partial_y$，定义
$$
\boxed{
K_{\nu j}^{\rm pol}
=\frac{n_\nu(D^2R_j)S_\nu}{48M_\nu}
+\frac{12R_j(D^2S_\nu)}{n_\nu M_\nu}
-\frac{(DR_j)(DS_\nu)}{M_\nu}
-\frac{xR_jS_\nu}{2},\qquad M_\nu=24+n_\nu.
}
\tag{46}
$$
则
$$
\boxed{
\mu K_{24,n_\nu}(E_j\otimes J_\nu)
=\sigma^{M_\nu}K_{\nu j}^{\rm pol}.
}
\tag{47}
$$
(46)是(6)和(11)的有限显式多项式算式，保全部 $H_8$ 等因子，
不是另选一个来源。它为型四，唯一函数极阶至多 $M_\nu-4$。

取任一非零二挠点 $Q=(e,0)$，$e^3=-b$。
所有原 $R_jS_\nu$ 都有因子 $y^2$，但(46)在这里只有中间项留下：
$$
K_{\nu j}^{\rm pol}(Q)
=-\frac{(DR_j)(Q)(DS_\nu)(Q)}{M_\nu}.
\tag{48}
$$
准确的导数值为
$$
(DR_j)(Q)=-3b^je^{10-3j},
$$
$$
\begin{array}{c|c}
\nu&(DS_\nu)(Q)\\ \hline
S&3^3be^2\\
T&-3^{11}b^8\\
U&3^{28}b^{18}e^2/13\\
V&3^{11}b^7 .
\end{array}
\tag{49}
$$
这些数直接从(5)–(6)得到。例如在 $X=-b$，
$A_2=-3^3b^2$、$F_4=G_4=3^6b^4$、
$H_8=3^{12}b^8$，所以 $U$ 的整乘积为 $-3^{27}b^{18}$；
并没有用有限点拟合决定该来源。

定义四个完整参考截面和常数
$$
\begin{array}{c|c|c}
\nu&\Xi_\nu&k_\nu\\ \hline
S&\sigma^{34}&3^4b^5/34\\
T&x\sigma^{72}&3^{12}b^{11}/72\\
U&\sigma^{136}&3^{29}b^{22}/(13\cdot136)\\
V&x\sigma^{66}&-3^{12}b^{10}/66 .
\end{array}
\tag{50}
$$
由 $e^3=-b$，(48)–(49)给
$$
\boxed{
\left.\sigma^{M_\nu}K_{\nu j}^{\rm pol}\right|_{E[2]\setminus\{O\}}
=k_\nu(-1)^j\left.\Xi_\nu\right|_{E[2]\setminus\{O\}}.
}
\tag{51}
$$
这是同一局部 theta frame 中的完整值式。
所有 $k_\nu$ 在本题单位域为单位，$\Xi_\nu$ 在这些点无零。
因此三列的这个实际边界商秩恰为一，其行是
$$
(1,-1,1).
\tag{52}
$$
指定原向量给
$$
(1,-1,1)c_*=\frac{27}{7}\ne0.
\tag{53}
$$
特别四个原首次伙伴都确实离开
$\langle E_0J_\nu,E_1J_\nu,E_2J_\nu\rangle$：
后者的每个元素在所有非零二挠点至少二阶为零，
而(51)–(53)的原伙伴在那里非零。
这是一条实际闭合检验，不只是环境维数比较。

## 3. 必须保留的伙伴仍有一个完整 whole 表达

上述漏出不要求引入未指定的函数。
写 $\Xi_\nu=\sigma^{M_\nu}x^{r_\nu}$，
其中 $r_S=r_U=0,r_T=r_V=1$。
因(51)在 $x^3=-b$ 的三个根逐个成立，定义
$$
\boxed{
L_{\nu j}
=\sigma^{M_\nu-8}
\frac{K_{\nu j}^{\rm pol}-k_\nu(-1)^jx^{r_\nu}}{X+b}.
}
\tag{54}
$$
分子被 $X+b$ **作为多项式**整除；
它的系数和全部来源由(46)、(50)固定。
最高函数极阶至多 $M_\nu-10$，故
$$
L_{\nu j}\in\mathscr V_{M_\nu-8}^{(2)},\qquad
\operatorname{ord}_O L_{\nu j}\ge2.
\tag{55}
$$
完整伙伴分解准确为
$$
\boxed{
\mu K_{24,n_\nu}(E_j\otimes J_\nu)
=k_\nu(-1)^j\Xi_\nu+\frac{\sigma(2z)^2}{4}L_{\nu j}.
}
\tag{56}
$$
这里 $\sigma(2z)^2/4=y^2\sigma^8$，因此(56)直接由(54)成立，
包含全部有限零、极和原半特征。

令 $L_{\nu,*}=\sum_jc_{*,j}L_{\nu j}$。
原 $C_{24}=z^5+\cdots$ 与 $J_\nu=z+\cdots$ 给
$$
\boxed{
L_{\nu,*}(z)=
\frac{5(n_\nu-12)}{12M_\nu}z^2+O(z^8).
}
\tag{57}
$$
因为(47)的首项是
$[20n_\nu^2-10\cdot24n_\nu]z^4/
(2\cdot24n_\nu M_\nu)$，而(50)的参考截面在更高阶才出现。
四个首系数依次为
$$
-\frac5{204},\quad\frac5{24},\quad
\frac{125}{408},\quad\frac{25}{132},
$$
所以这些也是实际非零的 whole 伙伴，不能只保(51)的有限值后删去它们。

例如 R856 的同一 whole 定理还准确给
$$
j_{p+3}(L_{\nu,*})
\equiv3(M_\nu-8)c_p\,j_2(L_{\nu,*})\ne0\pmod p.
\tag{58}
$$
(58)只固定这个实际伴随的一个高 jet；
它并不对 $L_{\nu,*}$ 添加任何中央零，
也不把其非零换成原(18)的不相容。

所以当前原三维行的完整热接口由(38)–(45)及(46)–(58)共同组成。
三维乘法子空间在第一次平衡操作已经有准确的非零边界，
其余 whole 伙伴又被(54)完整固定。
若要继续横向消元，必须带上这些来源及其真实二挠变换；
不能在原 $M_p$ 的三列上冻结一个没有该边界的闭合矩阵。

