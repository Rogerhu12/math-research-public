# R128：第一chaos在不变子空间内的域与预解正则化

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。

状态：完整证明。前半审计根代理 R125 所用的闭乘子构造，明确通常伴随、反线性对称、有限柱图核和 gauge 定义域。后半证明新的限制结论：对任意复 $\ell^2$ 第一阶系数，每个闭 $A$-不变子空间上的乘子定义域稠密，并给出保持该子空间的共同正则化；非负系数的限制值域稠密，非负且不在 $\ell^1$ 的系数更给出全部复数处的有界预解式及限制满射。

一般复系数的限制值域稠密性没有被四个正分量的论证自动解决。

## 1. 记号与纯模型的准确符号

设

$$
f=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a\in\ell^2.
$$

记 $\mathcal D=\bigcup_{p\ge0}H_{\le p}$，$\mathcal D_c$ 为全部有限柱向量。令反线性等距共轭

$$
(Cu)(y)=\overline{u(-1-y)}.
$$

在 Walsh 基上，$C$ 对系数作共轭并把 $\chi_S$ 乘以 $(-1)^{|S|}$。取物理单个位上的 $E_j=e_{10}$。在参考基 $1,\chi_j$ 中，

$$
V_j^0=I-2E_j
=\begin{pmatrix}0&-1\\1&2\end{pmatrix}
=c_j-a_j^{\rm ann}+2n_j.
\tag{1.1}
$$

最后三个符号分别表示产生、消灭和占据算子；为避免与数值系数 $a_j$ 混淆，下文把其加权和记为

$$
\mathsf C(a),\qquad\mathsf A(a),\qquad\mathsf D(a).
$$

因此纯乘子是

$$
S_0=a_*I+\mathsf C(a)-\mathsf A(a)+2\mathsf D(a)
\quad\text{于 }\mathcal D.
\tag{1.2}
$$

这里 $\mathsf A(a)$ 与 $\mathsf C(a)$ 都对数值系数线性，而非把共轭藏进记号。其形式通常伴随为

$$
S_0^\dagger
=\overline{a_*}I+\mathsf A(\bar a)-\mathsf C(\bar a)
+2\mathsf D(\bar a)
=CS_0C.
\tag{1.3}
$$

这核对了产生、消灭项的相反符号。

在 $H_{\le p}$ 上，直接按无交叠系数的 Cauchy–Schwarz 估计、其伴随以及占据对角式，有

$$
\|\mathsf C(a)u\|\le\sqrt{p+1}\|a\|_2\|u\|,
\quad
\|\mathsf A(a)u\|\le\sqrt p\|a\|_2\|u\|,
\quad
\|\mathsf D(a)u\|\le\sqrt p\|a\|_2\|u\|.
$$

所以存在固定 $K$，使 $S_0,S_0^\dagger$ 都把 $H_{\le p}$ 送入 $H_{\le p+1}$，且

$$
\|S_0u\|,\ \|S_0^\dagger u\|
\le K\sqrt{p+1}\|u\|.
\tag{1.4}
$$

这些不等式也保证有限数值系数截断在每个固定有限次数层上以算子范数收敛。

## 2. Dirac 块的自含本质自伴证明

在 $\mathcal D\oplus\mathcal D$ 上定义对称算子

$$
\mathscr K=
\begin{pmatrix}0&S_0^\dagger\\S_0&0\end{pmatrix}.
$$

若 $u$ 的两个分量都在 $H_{\le p}$，反复使用 (1.4) 得

$$
\|\mathscr K^nu\|
\le K^n\sqrt{\frac{(p+n)!}{p!}}\|u\|.
\tag{2.1}
$$

故对任意实数 $t$，级数

$$
U(t)u=\sum_{n\ge0}\frac{(it)^n}{n!}\mathscr K^nu
$$

及其一次导数在有界 $t$ 段上范数一致收敛。有限部分属于 $\operatorname{Dom}\mathscr K$，其算子像也收敛，所以

$$
U(t)u\in\operatorname{Dom}\overline{\mathscr K},
\qquad
\frac d{dt}U(t)u=i\overline{\mathscr K}U(t)u.
$$

闭对称算子 $\overline{\mathscr K}$ 使范数导数为零，因此 $\|U(t)u\|=\|u\|$。

若 $w\in\ker(\mathscr K^*-iI)$，采用内积对第一变量线性的约定，逐项配对给

$$
\langle U(t)u,w\rangle=e^t\langle u,w\rangle.
$$

左边对全部 $t$ 的模长不超过 $\|u\|\|w\|$。令 $t\to+\infty$，得 $\langle u,w\rangle=0$；稠密性推出 $w=0$。对 $\ker(\mathscr K^*+iI)$，令 $t\to-\infty$ 同样成立。

两缺陷核为零。又

$$
\|(\overline{\mathscr K}\pm iI)x\|^2
=\|\overline{\mathscr K}x\|^2+\|x\|^2,
$$

所以这两个像闭，且由缺陷核为零而稠密，因此均为全空间。这推出 $\overline{\mathscr K}$ 自伴。

块图范数分别为 $S_0,S_0^\dagger$ 的图范数直和，所以若 $X_0=\overline{S_0}$，就有

$$
\overline{S_0^\dagger}=X_0^*=CX_0C.
\tag{2.2}
$$

此外，$\mathcal D_c$ 是两者的图核：对 $u\in H_{\le p}$，有限位条件期望仍在 $H_{\le p}$，在 $L^2$ 中趋于 $u$，(1.4) 同时保证算子像趋于相应极限。再用 $\mathcal D$ 本来就是闭包图核即可。

## 3. 实际进位是有界反线性对称扰动

实际算子为

$$
N_j=A^{2^j}/d_j,\quad
Y_j=N_j(I+N_j)^{-1},\quad
V_j=I-2Y_j.
$$

由真实一位关系 $N_j=E_j+\eta_jE_j^*N_{j+1}$ 以及 $N_j^2=\eta_jN_{j+1}$，有

$$
\|V_j-V_j^0\|\le C_0\eta_j,
\qquad \eta\in\ell^2.
$$

因此

$$
E_a=\sum_ja_j(V_j-V_j^0)
$$

按算子范数绝对收敛，且 $\|E_a\|\le C_0\|a\|_2\|\eta\|_2$。每项均满足通常伴随等于 $C$ 共轭，故 $E_a^*=CE_aC$。

定义

$$
X_a=X_0+E_a,\qquad\operatorname{Dom}X_a=\operatorname{Dom}X_0.
\tag{3.1}
$$

它闭，有限柱为图核，并且

$$
\boxed{X_a^*=CX_aC.}
\tag{3.2}
$$

有限部分

$$
X_{a,N}=a_*I+\sum_{j<N}a_jV_j\in\mathcal A
$$

及其通常伴随在每个有限柱向量上分别收敛到 $X_a$、$X_a^*$。由于 $V_j1=V_j^01=\chi_j$，还有 $X_a1=f$。

## 4. 与全部有界交换子的定义域交换

这里可得到比只与 $A$ 交换更强的性质。

**引理 4.1。** 对每个 $T\in\{A\}'$，

$$
T\operatorname{Dom}X_a\subseteq\operatorname{Dom}X_a,
\qquad X_aTu=TX_au.
\tag{4.1}
$$

**证明。** 先取有限柱 $u,v$。有限部分 $X_{a,N}$ 与 $T$ 交换，所以

$$
\begin{aligned}
\langle TX_au,v\rangle
&=\lim_N\langle X_{a,N}Tu,v\rangle\\
&=\lim_N\langle Tu,X_{a,N}^*v\rangle
=\langle Tu,X_a^*v\rangle.
\end{aligned}
$$

有限柱是 $X_a^*$ 的图核，所以 $Tu\in\operatorname{Dom}X_a^{**}=\operatorname{Dom}X_a$，并有 $X_aTu=TX_au$。再对任意 $u\in\operatorname{Dom}X_a$ 用有限柱图逼近及 $X_a$ 的闭性推广。证毕。

这一步不能被“$A$ 保持有限 chaos”替代：一般 $A^n1$ 并不属于有限 chaos。

每个有限柱 $u$ 可写成 $R(A)1$，其中 $R$ 是在零点解析的有理芽。由引理 4.1，$X_au=R(A)f$。有限柱图核遂给

$$
\boxed{\overline{\operatorname{Ran}X_a}
=\overline{\operatorname{span}\{A^nf:n\ge0\}}.}
\tag{4.2}
$$

反向包含使用 $1\in\operatorname{Dom}X_a$ 及 (4.1)，故每个 $A^n1$ 在定义域内、像为 $A^nf$；它不需要声称这些向量是有限柱。

## 5. dyadic gauge 共轭的闭图相等

设 $\zeta^{2^m}=1$，$U_\zeta$ 是乘以特征 $y\mapsto\zeta^y$ 的酉算子。它把有限柱双向映为有限柱。对 $N\ge m$，

$$
U_\zeta X_{a,N}U_\zeta^*-X_{a,N}
=D_\zeta(A),
$$

其中 $D_\zeta$ 是有限有理解析芽，只涉及 $j<m$。在有限柱上取极限，再分别取双方闭包，得到

$$
\boxed{U_\zeta X_aU_\zeta^*=X_a+D_\zeta(A),}
\qquad U_\zeta\operatorname{Dom}X_a=\operatorname{Dom}X_a.
\tag{5.1}
$$

这里有限柱是共轭算子的图核，因为 $U_\zeta$ 在有限柱上双向不变；它也是有界扰动 $X_a+D_\zeta(A)$ 的图核。因此 (5.1) 是闭算子及定义域的相等，不只是共同核心上的形式公式。

当根代理的 R125 在核 $M=\ker X_a$ 上使用跨核配对时，(5.1) 保证两端向量都在所需定义域；(3.2) 及 $D_\zeta(A)$ 的反线性对称则保证相应 $B$-对称合法。

## 6. 非负系数给极大增生算子

本节把常数项取为零，并设 $b_j\ge0$、$b\in\ell^2$。记对应闭乘子为 $X_b$。

由于 $\|N_j\|\le1$，其 Cayley 变换

$$
V_j=(I-N_j)(I+N_j)^{-1}
$$

是增生的。具体地，对 $v=(I+N_j)^{-1}u$，

$$
\operatorname{Re}\langle V_ju,u\rangle
=\|v\|^2-\|N_jv\|^2\ge0.
\tag{6.1}
$$

有限部分 $\sum_{j<N}b_jV_j$ 增生；在有限柱上取极限，再用图核，知 $X_b$ 增生。由 $X_b^*=CX_bC$，$X_b^*$ 也增生。

对任意 $t>0$，

$$
\|(I+tX_b)u\|\ge\|u\|.
$$

故该算子的像闭；其像的正交补是 $\ker(I+tX_b^*)$，增生性使此核为零。因此它满射，并有收缩预解式

$$
\boxed{R_b(t)=(I+tX_b)^{-1},\qquad\|R_b(t)\|\le1.}
\tag{6.2}
$$

同理，当 $\operatorname{Re}z>0$ 时，$X_b+zI$ 可逆且逆范数不超过 $(\operatorname{Re}z)^{-1}$。这就是本稿所需的极大增生性质，不要求调用半群存在定理。

由 (4.1)，$R_b(t)\in\{A\}'$。在 $u\in\operatorname{Dom}X_b$ 上，

$$
R_b(t)u-u=-tR_b(t)X_bu\longrightarrow0
\quad(t\downarrow0).
$$

收缩性及定义域稠密性遂给 $R_b(t)\to I$ 强收敛。

### 6.1 非负闭乘子的单射性可以独立证明

若 $b\ne0$，则 $X_b$ 单射，继而由 (3.2) 值域稠密。以下证明不依赖 R125 的一般复系数核定理。

相对于物理第 $j$ 位，真实块形式为

$$
N_j=\begin{pmatrix}0&\eta_jN_{j+1}\\I&0\end{pmatrix}.
$$

写 $v=(v_0,v_1)$，则 (6.1) 的右端为

$$
\|v_1\|^2-\eta_j^2\|N_{j+1}v_1\|^2
\ge(1-\eta_j^2)\|v_1\|^2.
\tag{6.3}
$$

因此耗散型为零当且仅当 $v_1=0$，也即 $u=(I+N_j)v=(v_0,v_0)$ 不依赖第 $j$ 位；此时 $V_ju=\chi_ju$。

若 $X_bu=0$，注意 $X_b-b_jV_j$ 是删去第 $j$ 个非负系数后的闭增生乘子，定义域与 $X_b$ 相同。因此对每个 $b_j>0$，(6.1) 的耗散型必须为零。于是 $u$ 独立于全部这些位。

向量 $\chi_ju$（$b_j>0$）两两正交，故

$$
\sum_{j<N}b_jV_ju=\sum_{j<N}b_j\chi_ju
\longrightarrow \sum_jb_j\chi_ju,
\qquad
\left\|\sum_jb_j\chi_ju\right\|=\|b\|_2\|u\|.
$$

对有限柱伴随图核配对，有限部分的这个强极限必等于 $X_bu$。所以 $u=0$。

## 7. 任意复系数在每个不变子空间内有稠密定义域

使用 R88：$\{A\}'$ 是多项式的强算子闭包。因此每个闭 $A$-不变子空间 $M$ 都被全部有界交换子保持。

把任意复系数写为

$$
a=b_1-b_2+i b_3-i b_4,\qquad b_\nu\ge0,\quad b_\nu\in\ell^2,
$$

其中取实部、虚部的正负部分。令 $\lambda=(1,-1,i,-i)$，并约定零分量的预解式为 $I$。由引理 4.1，所有 $R_{b_\nu}(t)$ 两两交换，而且每个都保持每个 $X_{b_\mu}$ 的定义域并与之域交换。

定义

$$
R(t)=\prod_{\nu=1}^4R_{b_\nu}(t).
\tag{7.1}
$$

它是收缩、有界交换子，$R(t)\to I$ 强收敛，且

$$
\operatorname{Ran}R(t)
\subseteq\bigcap_{\nu=1}^4\operatorname{Dom}X_{b_\nu}.
$$

该共同定义域包含于 $\operatorname{Dom}X_a$，且在那里

$$
X_a=a_*I+\sum_{\nu=1}^4\lambda_\nu X_{b_\nu}.
\tag{7.2}
$$

证明 (7.2) 时不要仅说“闭包可以与有限和交换”。对共同定义域内的 $u$ 和有限柱 $v$，按通常伴随配对，右端与 $v$ 的内积恰为 $\langle u,X_a^*v\rangle$。有限柱是 $X_a^*$ 的图核，遂得 $u\in\operatorname{Dom}X_a$ 及等式。

由 (6.2)，有准确有界恒等式

$$
\boxed{
X_aR(t)
=a_*R(t)+\frac1t\sum_{\nu=1}^4
\lambda_\nu(I-R_{b_\nu}(t))
\prod_{\mu\ne\nu}R_{b_\mu}(t).
}
\tag{7.3}
$$

右端属于 $\{A\}'$，因而保持 $M$。于是

$$
R(t)M\subseteq
\{u\in M\cap\operatorname{Dom}X_a:X_au\in M\}.
$$

强收敛 $R(t)\to I$ 证明右端在 $M$ 中稠密。

实际上，对任意 $u\in\operatorname{Dom}X_a\cap M$，引理 4.1 给

$$
X_aR(t)u=R(t)X_au\longrightarrow X_au.
$$

由于每个左端属于闭空间 $M$，自动有 $X_au\in M$。所以限制部分恰为

$$
X_{a,M}:\operatorname{Dom}X_a\cap M\longrightarrow M,
$$

它闭、稠密定义。共同正分量定义域与 $M$ 的交是其图核，因为 $R(t)u$ 对每个 $u$ 给出图逼近。

这解决了有限部分 $X_{a,N}$ 不一致有界所造成的域障碍；并未断言这些有限部分在任意 $M$ 上直接强收敛。

## 8. 非负系数的限制值域稠密

设 $0\ne b\ge0$。由 §6.1，$\operatorname{Ran}X_b$ 在全 $H$ 稠密。对 $x=X_bu$，

$$
R_b(t)x=t^{-1}(I-R_b(t))u\longrightarrow0
\quad(t\to\infty).
$$

收缩性将此强极限延拓到全 $H$，即 $R_b(t)\to0$ 强收敛。另一方面，对 $x\in M$，

$$
(I-R_b(t))x=tX_bR_b(t)x
\in\operatorname{Ran}X_{b,M}.
$$

因此

$$
\boxed{\overline{\operatorname{Ran}X_{b,M}}=M.}
\tag{8.1}
$$

更一般地，若一个同类闭乘子经乘固定复相位后增生，且全空间上单射，则相同预解式论证适用。不能仅从四个非负部分分别有稠密值域，推断其任意复线性组合也有这个性质。

## 9. 非负、非绝对可和系数的空谱与限制满射

进一步设

$$
b_j\ge0,\qquad b\in\ell^2,\qquad\sum_jb_j=\infty.
\tag{9.1}
$$

**命题 9.1。** $X_b$ 的预解集是整个 $\mathbb C$。对每个闭 $A$-不变 $M$ 及任意 $\lambda\in\mathbb C$，

$$
X_{b,M}-\lambda I:
\operatorname{Dom}X_b\cap M\longrightarrow M
$$

双射，且逆为全空间有界预解式在 $M$ 上的限制。

**证明。** 固定 $\lambda$。取 $m$，使

$$
\beta_m=\sum_{j<m}b_j>\operatorname{Re}\lambda.
$$

有限头写成

$$
H_m=\sum_{j<m}b_jV_j=\beta_mI+K_m,
\quad K_m=-2\sum_{j<m}b_jY_j.
$$

$K_m\in\mathcal A$，常数特征为零，故拟幂零。尾闭乘子

$$
T_m=X_b-H_m
$$

对应非负 $\ell^2$ 尾系数，因而极大增生；它的定义域与 $X_b$ 相同。于是

$$
R=(T_m+(\beta_m-\lambda)I)^{-1}
$$

有界并属于 $\{A\}'$。引理 4.1 及其预解式形式保证 $R$ 与 $K_m$ 交换。由

$$
\|(K_mR)^n\|^{1/n}
\le\|K_m^n\|^{1/n}\|R\|\longrightarrow0,
$$

$I+K_mR$ 有界可逆。真实域等式为

$$
X_b-\lambda I
=(I+K_mR)(T_m+(\beta_m-\lambda)I).
$$

故

$$
\boxed{(X_b-\lambda I)^{-1}=R(I+K_mR)^{-1}\in\{A\}'.}
\tag{9.2}
$$

此逆保持 $M$，其值落入 $\operatorname{Dom}X_b\cap M$，从而限制算子也双射。证毕。

因此，对同一射线上的非 $\ell^1$ 系数 $a_j=e^{i\theta}b_j$，任意常数项 $a_*$ 都给 $X_a=a_*I+e^{i\theta}X_b$ 的空谱及上述限制满射性质。

当 $b\in\ell^1$ 时，不能使用 (9.1) 的头常数趋无穷步骤；特别是减去全部头常数所得的临界有界乘子，不能从本节自动获得标准闭理想或全部限制值域稠密。

## 10. 与 R125 的直接推论及剩余边界

根代理 R125 的一般复 $\ell^2$ 核证明，结合本稿 (3.2)、(4.2)，给每个非零第一 chaos 向量循环。因此对固定 $0\ne g\in H$，此前 R104 的空间准确加强为

$$
Z_g^{(1)}=\{0\}.
$$

也因此，每个真闭 $A$-不变子空间 $M\ne H$ 都有

$$
M\cap H_{\le1}=\{0\}.
$$

这两条使用 R125 的全复系数循环结论；本稿的定义域正则化、非负系数单射性及 §§8–9 不依赖该一般核结论。

尚未解决的是：任意复 $\ell^2$ 系数的非零闭乘子，在任意闭 $A$-不变 $M$ 上是否总有稠密值域。全 $H$ 上的 $C$-自伴性不能直接传到任意 $M$，因为 $C$ 未必保持 $M$；四分量正则化只解决定义域、图核及像保持，不越过这个缺口。
