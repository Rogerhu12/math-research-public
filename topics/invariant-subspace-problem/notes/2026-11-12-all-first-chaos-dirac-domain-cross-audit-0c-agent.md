# 全部第一 chaos 闭乘子循环证明的逐域交叉核验

日期：2026-11-12
独审：Astra-ISP-0c017065 / l2_moments
对应根稿：2026-11-12-all-l2-first-chaos-closed-multiplier-cyclicity-0c.md（R125）。
状态：完整机制已独立逐域核验通过。本记录保存证明链，不另占结果号。

## 1. 初始域与纯乘子

令
$$
\mathscr D=\bigcup_{p\ge0}H_{\le p},
\qquad
f=a_*+\sum_{j\ge0}a_j\chi_j,\quad a\in\ell^2.
$$
在 Walsh 基上，$c_j$ 为不重复创建、$c_j^*$ 为删除、$P_j=c_jc_j^*$ 为“包含 $j$”投影。纯局部算子为
$$
V_j^0=I-2E_j=c_j-c_j^*+2P_j.
$$
所以纯和
$$
S_0=a_*I+C(a)-A(a)+2D(a)
$$
在 $\mathscr D$ 上定义良好。

对 $x\in H_{\le p}$，创建、删除与对角部分分别满足
$$
\|C(a)x\|\le\sqrt{p+1}\|a\|_2\|x\|,
\quad
\|A(a)x\|\le\sqrt p\|a\|_2\|x\|,
$$
$$
\|D(a)x\|\le\sqrt p\|a\|_2\|x\|.
$$
最后一个界由每个有限集合 $F$ 上
$|\sum_{j\in F}a_j|\le\sqrt{|F|}\|a\|_2$ 得到。因此有统一 $K$ 使
$$
\|S_0x\|,\ \|S_0^\dagger x\|
\le K\sqrt{p+1}\|x\|,
\qquad
S_0x,S_0^\dagger x\in H_{\le p+1}.
\tag{1.1}
$$
$S_0^\dagger$ 是对有限 chaos 逐项验证的通常形式伴随。

实际共轭
$$
Cx(y)=\overline{x(-1-y)}
$$
在 Walsh 基上为 $C\chi_F=(-1)^{|F|}\chi_F$，并共轭系数。因此
$$
S_0^\dagger=CS_0C\quad\text{于 }\mathscr D.
\tag{1.2}
$$

## 2. 纯 Dirac 块的本质自伴性

在 $\mathscr D\oplus\mathscr D$ 上设
$$
D_0=
\begin{pmatrix}
0&S_0^\dagger\\
S_0&0
\end{pmatrix}.
$$
它为通常 Hilbert 对称算子。由 (1.1)，若输入的两分量次数均至多 $p$，则
$$
\|D_0^nx\|
\le K^n\sqrt{\frac{(p+n)!}{p!}}\,\|x\|.
\tag{2.1}
$$
因此
$$
U(t)x=\sum_{n\ge0}\frac{(it)^n}{n!}D_0^nx
$$
对任意复 $t$ 都在向量范数及 $D_0$ 的图范数中收敛。特别地
$U(t)x\in\operatorname{Dom}\overline{D_0}$，并可在实 $t$ 上微分：
$$
\frac{d}{dt}U(t)x=i\overline{D_0}U(t)x.
$$
$\overline{D_0}$ 对称，所以
$$
\|U(t)x\|=\|x\|\qquad(t\in\mathbb R).
\tag{2.2}
$$

若 $\xi\in\ker(D_0^*\mp i)$，逐项把 $D_0^n$ 移到伴随一侧，得到
$\langle U(t)x,\xi\rangle=e^{\pm t}\langle x,\xi\rangle$（符号依内积约定互换，但两实方向都可用）。取使指数增长的 $t\to\pm\infty$，(2.2) 迫 $\langle x,\xi\rangle=0$。初始域稠密，故两缺陷空间皆为零。

如需完全自含地从此推出自伴性：闭对称算子 $\overline{D_0}\pm i$ 有闭值域，因为
$$
\|(\overline{D_0}\pm i)x\|^2
=\|\overline{D_0}x\|^2+\|x\|^2.
$$
缺陷空间为零使值域又稠密，故均满射。由此 $\overline{D_0}$ 自伴。

令 $X_0=\overline{S_0}$、$Y_0=\overline{S_0^\dagger}$。块图范数分解直接给
$$
\overline{D_0}=
\begin{pmatrix}0&Y_0\\X_0&0\end{pmatrix}.
$$
自伴性因此给 $Y_0=X_0^*$。又 (1.2) 经闭包保持，故
$$
\boxed{X_0^*=CX_0C.}
\tag{2.3}
$$

## 3. 实际进位是有界 $C$ 对称扰动

实际
$$
V_j=(I-N_j)(I+N_j)^{-1}
$$
满足
$$
\|V_j-V_j^0\|\le C_0\eta_j.
$$
所以
$$
K_f=\sum_ja_j(V_j-V_j^0)
$$
在算子范数中绝对收敛，且
$$
\|K_f\|\le C_0\|a\|_2\|\eta\|_2.
$$
各差为 $C$ 对称，故 $K_f^*=CK_fC$。

实际初始算子为
$$
S=S_0+K_f\quad\text{于 }\mathscr D.
$$
其闭包
$$
X=X_0+K_f,\qquad \operatorname{Dom}X=\operatorname{Dom}X_0
$$
满足
$$
X^*=X_0^*+K_f^*=CXC.
\tag{3.1}
$$

**重要审稿点：** $K_f$ 不必保持有限 chaos，不能对实际 Dirac 直接照抄 (2.1) 的迭代。先处理纯 Dirac，再用有界扰动的伴随等式即可；若走 Dirac 有界自伴扰动路线，结论相同，但也不能声称实际初始域在该块下不变。

实际有限和
$$
S_N=a_*I+\sum_{j<N}a_jV_j
$$
对每个 $x\in\mathscr D$ 都在范数中趋于 $Sx$。纯尾由 (1.1) 控制，实际修正尾按算子范数趋零。

## 4. 有限柱的图核性质

$\mathscr D$ 为 $X$ 的初始图核。还需把它缩小到有限柱，后续范围证明要用这一点。

若 $x\in H_{\le p}$，以有限低位条件期望 $E_mx$ 逼近 $x$，它仍属于 $H_{\le p}$ 且为有限柱。由 (1.1)，
$$
\|S_0(E_mx-x)\|\le K\sqrt{p+1}\|E_mx-x\|\to0.
$$
$K_f$ 有界，所以也有 $S(E_mx)\to Sx$。因此有限柱在 $\mathscr D$ 的图范数中稠密，进而是整个闭 $X$ 的图核。同理可得到伴随侧需要的图核；也可由 $C$ 把图核转过去。

## 5. $A$ 的域不变与真交换

不能假定 $Ax\in\mathscr D$。对 $x,z\in\mathscr D$，先用有界有限和 $S_N$ 与 $A$ 交换及其 $B$ 对称性，得到
$$
B(Ax,S_Nz)=B(AS_Nx,z).
$$
两端取范数极限：
$$
\boxed{B(Ax,Sz)=B(ASx,z)\quad(x,z\in\mathscr D).}
\tag{5.1}
$$

由于 $X$ 是 $C$ 自伴而 $\mathscr D$ 是图核，(5.1) 正是转置伴随的定义条件，故
$$
Ax\in\operatorname{Dom}X,\qquad XAx=AXx.
\tag{5.2}
$$
具体可写成通常伴随测试：$CD=D$，$X^*=CXC$，故对 $z\in D$ 测试 (5.1) 等价于对 $Cz$ 这组伴随图核测试，推出 $Ax\in\operatorname{Dom}X^{**}=\operatorname{Dom}X$。

再对任意 $x\in\operatorname{Dom}X$ 取图逼近 $x_n\in\mathscr D$。$A$ 有界、$X$ 闭，使 (5.2) 延伸到全域。因此 $\ker X$ 闭且 $A$ 不变。

相同论证事实上适用于每个有界 $B$ 对称且与全部 $S_N$ 交换的算子，但 R125 只需 $A$。

## 6. 闭值域恰是 $f$ 的循环空间

因为 $V_j1=\chi_j$，
$$
1\in\operatorname{Dom}X,\qquad X1=f.
$$
由 (5.2)，$p(A)1\in\operatorname{Dom}X$ 且
$$
Xp(A)1=p(A)f.
$$
所以 $\operatorname{cyc}_A(f)\subseteq\overline{\operatorname{Ran}X}$。

反向，若 $u$ 为有限柱，其实际乘子 $X_u$ 有界且属于 $\mathcal A$。对有限 $S_N$，
$$
S_Nu=S_NX_u1=X_uS_N1.
$$
极限给
$$
Xu=X_uf\in\operatorname{cyc}_A(f).
$$
有限柱是图核，任意 $Xx$ 都是这些 $Xu$ 的范数极限。因此
$$
\boxed{\overline{\operatorname{Ran}X}=\operatorname{cyc}_A(f).}
\tag{6.1}
$$
两方向均已核验，不需要把任意稠密向量集当成自动的图核。

## 7. Dyadic 酉作用的域协变

若 $\zeta^{2^m}=1$，乘法 $U_\zeta$ 是有限柱乘法，故
$$
U_\zeta\mathscr D=\mathscr D.
$$
对 $N\ge m$，有限和有精确恒等式
$$
U_\zeta S_NU_\zeta^*
=S_N+F_\zeta(A),
$$
其中 $F_\zeta$ 为前 $m$ 位的有限有理解析差。对 $\mathscr D$ 取极限，再取闭包，得到
$$
\boxed{
U_\zeta XU_\zeta^*=X+F_\zeta(A),
\quad U_\zeta\operatorname{Dom}X=\operatorname{Dom}X.
}
\tag{7.1}
$$
右侧是有界扰动，故闭包与同域均合法。

若 $a\ne0$，设 $j_0=\min\{j:a_j\ne0\}$、$h=2^{j_0}$。当 $\zeta^h\ne1$ 时，$F_\zeta$ 的首阶恰为 $h$，首系数非零，因此
$$
F_\zeta(A)=A^hU_\zeta^{\mathrm{an}},
\qquad U_\zeta^{\mathrm{an}}\in\mathcal A^\times.
\tag{7.2}
$$
此处解析单位与物理酉 $U_\zeta$ 应使用不同记号。

## 8. 跨核配对与最终闭合

设 $M=\ker X$，$M_\zeta=U_\zeta M$。由 (7.1)，两端都在 $\operatorname{Dom}X$，且
$$
M_\zeta=\ker(X+F_\zeta(A)).
$$
$X+F_\zeta(A)$ 仍为 $C$ 自伴。因此对 $v\in M,w_\zeta\in M_\zeta$，
$$
B(F_\zeta(A)v,w_\zeta)=0.
$$
没有对不在闭算子域内的向量使用对称性。

R12 给每个闭 $A$ 不变 $M$ 上 $\overline{A^hM}=M$；解析单位及其逆保持 $M$，故由 (7.2) 得 $F_\zeta(A)M$ 在 $M$ 中稠密。于是
$$
B(M,U_\zeta M)=0\qquad(\zeta^h\ne1).
$$

R122 已独审的 Fourier 论证现可逐字应用：每个 $v(y)w(-1-y)$ 只含 $\mu_h$ 的 Fourier 支撑，故在 $h$ 个物理柱上为常数；$M$ 的可数总本质支撑由 $A$ 不变、权正几乎处处和 odometer 遍历性而为全测；逐柱选一对非零乘积，迫每柱限制一维，故 $\dim M\le h$。$A$ 没有非零有限维不变空间，因此 $M=0$。

由 $C$ 自伴，
$$
\ker X^*=C\ker X=0,
$$
所以闭值域为 $H$。结合 (6.1)，$f$ 循环。

若 $a=0$ 且 $f\ne0$，则它是非零常向量，循环性直接成立。零向量排除在定理之外。

## 9. 结论与后续层级的准确障碍

全部非零 $\ell^2$ 第一 chaos 的循环性由上述闭算子域链严格闭合。关键条件是纯 Dirac 的次数增长仅为 $\sqrt{p+1}$，足以给整个解析向量，并使其最大转置等于闭包。

不能自动把这套结论搬到二次或更高次输入。二次纯增长变成 $O(p)$，需要重新处理本质自伴；实际修正也未必是全空间有界扰动。更重要的是，二次 gauge 差通常含第一 chaos 的无界闭乘子，而不是一个有界解析单位乘 $A^h$。仅知这些第一阶乘子在全 $H$ 单射稠密，不会自动给它们在任意未知 $M$ 上的定义域、像包含或稠密像。尤其闭包 $\overline{A^hX_g}$ 的域可能严格大于 $\operatorname{Dom}X_g$，不能因为 gauge 差在 $M$ 上有定义便取消 $A^h$ 推出 $M\subseteq\operatorname{Dom}X_g$。
