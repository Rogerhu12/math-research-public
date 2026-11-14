# R61. canonical 除 p 热行與固定 Miller 范数

日期：2026-11-12。**状态：各行、类型、范数与精度比较已证明；跨素数非零未证明。**

## 1. 实际整数提升上的 canonical 行

在 $E_0:y^2=x^3-x$ 上置 $V=x^{-2}$、$F_k=\theta^{17}V^k$，
$0\le k\le4$。这些函数的 Hurwitz 系数全为整数。
固定惰性 $p\ge7$、$d=p+1$，在中心为零的整格
$I=\bigoplus_{k=1}^4\mathbb ZF_k$ 上，
$$
\mathcal B_p(F)=F^{(d)}(0)/p\pmod p
\tag{1}
$$
是良定的 $I/pI$ 上的泛函，且
$$
[z^d]F\equiv-\mathcal B_p(F)\pmod p.
\tag{2}
$$
良定性来自整个整格上的 $p\mid F^{(d)}(0)$，不是任意选一个模形式提升。
若 $\Xi_k=(\Theta^{17}v^k)'/F(v)$，则
$$
\mathcal B_p(F_k)=-4[v^{(p-3)/4}]\Xi_k\pmod p.
\tag{3}
$$
根端复跑[独立整数流脚本](../scripts/check-canonical-divided-heat-row.py)，
$p=7,11$ 的四行分别为 $(4,6,0,0)$、$(10,8,10,0)$。
实际目标向量为 $(1,3/5,-1/5,1/5)$。

同次数比较截面
$$
C_{17}=\frac{\theta((4-i)z)-\theta((4+i)z)}{-40i}
       =F_1-\frac75F_2+\frac35F_3-\frac15F_4
$$
的完整导数等于固定代数数的非零 $p$ 进对数，然而其十七处类型是 trivial，
实际目标为 quartic 类型。实际 $\mathcal B_7$ 在这两个类型上都非零，
故不能把它作为单一角色的等变行来应用 Schur 引理。

同次数有理参考 $f_0=\theta((4-i)z)$ 下，四个 $F_k/f_0$ 的
holomorphic 剩余行准确为
$$
(3+12i,-9-2i,-17,-5-54i)/1088.
$$
有理向量的纯 $d\log$ 子空间因此恰为
$$
a_2=6a_1-27a_4,\qquad a_3=-3a_1+14a_4.
\tag{4}
$$
实际向量在这个二维子空间中；已知非零的 $C_{17}$ 方向不在其中。
全部有限商代数与类型计算见
[canonical 行全文](../notes/2026-11-12-canonical-divided-heat-row-and-cm-type.md)。

## 2. 短周期素数的固定单位与真实 theta 范数

令 $R=A_1/f_0$，其十六个简单极点为 $P=T+S$、
$0\ne S\in E_0[4-i]$，留数为 $\rho_P$。
R59 的准确纯对数式使用固定 Miller 函数
$$
R\omega=\sum_P\rho_Pd\log g_P/17,\qquad
\operatorname{div}g_P=17(P)-17(T),\quad g_P(O)=1.
$$
对 $p\equiv35,67\pmod{68}$，写 $[p]P=s_pP$、$s_p=\pm1$。
固定 $b=69$、$v_P=\Psi_b(P)/\Psi_b(T)$，Weil 互反及 sigma 交换式给
$$
\prod_{Q\in E[p]}g_P(Z+Q)=C_{p,P}g_{s_pP}([p]Z),
\qquad C_{p,P}^{b^2-1}=v_P^{17(p^2-1)}.
\tag{5}
$$
所有 $v_P$ 是这些素数处的单位。但 $v_{iP}=v_P$、$\rho_{iP}=i\rho_P$，
所以真实加权对数 $\sum\rho_P\log_pv_P$ 准确为零。
保留全 jet 的交换式同样不增加独立的非 Wieferich 条件：
$b^n-b^2$ 已是对应固定对数 jet 的因子。

对 (5) 求对数导数得到完整有理式
$$
\sum_{Q\in E[p]}R(Z+Q)=s_ppR([p]Z).
\tag{6}
$$
以代数 Mumford 平移并将每个因子正规到常数项一，真实 theta 切向范数为
$$
\prod_{Q\in E[p]}\mathcal T_Q(f_0+\tau A_1)
 =f_0(pz)+\tau s_ppA_1(pz),\qquad \tau^2=0.
\tag{7}
$$
这里不能在惰性 theta Taylor 级数中直接代入 $p$ 挠点；代数平移的
代数性由 Bannai–Kobayashi 2010 Theorem 2.9 给出，原文范围已核。
只有 $1+\tau R(t)$ 是整个开正式盘内的实际整单位，其局部范数为
$1+\tau s_ppR(t)$。这一固定本征方向不能单独给非零整的范数相容逆系统。

(7) 的临界系数为 $s_pp^{p+2}\beta_{p+1}$。例如 $p=67$，
[两种独立系数算法](../scripts/check-inert-theta-prime-diagonal.py) 均由根端给
$\beta_{68}=57\bmod67$，故该系数赋值准确为 $69$。
保留高斜率正规化是比较目标除 $p$ 行的必要条件。
完整证明、固定单位和全 jet 公式见
[短周期 Miller 与 theta 切向范数](../notes/2026-11-12-short-cycle-miller-and-theta-tangent-norm.md)。

## 3. 保持的待证条件

实际首层非零仍是 $\mathcal B_p(A_1)\ne0$；更深条件仍是 R54 的
$J_{A,p}'(0)\ne0$。上述固定单位与范数没有证明其无穷次非零。
完整半权热族在 Legendre 参数上不满足有限阶代数系数线性微分方程，
证明见[半权单值性](../notes/2026-11-12-half-weight-heat-scalar-monodromy.md)；
这不排除指定素数对角另有需证明的有限 Frobenius/Bockstein 比较。
