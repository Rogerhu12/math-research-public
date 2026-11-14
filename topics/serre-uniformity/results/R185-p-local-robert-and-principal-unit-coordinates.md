# R185：同一主化元与原始 Robert 单位的实际 $43$ 进坐标

状态：**已证明**。本条固定 R171 的同一个 $776$ 位素数 $q$、同一个全局生成元 $y$ 和同一个主化元
$\alpha=1+89460y$，不增加候选素数。

本条把 R180 中原来抽象给出的 $p$ 局部平坦校正实际算出：在下文明确规范的局部基中，

$$
\boxed{\operatorname{loc}_{43}d_q=(20,29),\qquad
\operatorname{loc}_{43}d^{\rm Rob}_{43}=(24,20).}
\tag{185.1}
$$

二者的行列式为 $5\ne0$。平坦切线的正交空间恰为第二条坐标轴，因此 R180 的校正系数和校正后的局部值为

$$
\boxed{\beta_q=8,\qquad
\operatorname{loc}_{43}(d_q-8d^{\rm Rob}_{43})=(0,41).}
\tag{185.2}
$$

这里 $d_q$ 保留 R171 的 $q$ 奇异坐标 $1$，$d^{\rm Rob}_{43}$ 保留 R161 的原始投影及其 $1/(p^2-1)$ 因子。
两条类的全局嵌入、同源标记、Artin 方向和局部参数都在证明中固定。
**这些量不是 R176 的 $\Omega_2$，也不是 R180 的 $t_q/43^2$。** 本条没有计算非线性的二阶晶体迹。

数据与程序：

- [标准库核验器](../notes/verify_r185_p_local_kummer.py)；
- [有理多项式及局部证书](../notes/r185_p_local_kummer_certificate.json)。

核验器读取已发布的 R171 模型和 R171/R161 标准库算术模块，不依赖 PARI、Sage、浮点数或数值对数。

## 1. 同一个全局域及 $43$ 处的规范参数

始终取

$$
p=43,\quad K=\mathbf Q(i),\quad A:y^2=x^3-x,\quad
T=K(A[p]),\quad \mathscr F=T^{\mathbf F_p^\times},\quad
H=\mathscr F^{\langle\tau\rangle}.
$$

$\tau$ 是 R171 固定的复共轭，$H$ 的次数为 $44$、签名为 $(2,21)$；没有把 $H$ 当作全实域。
沿用 R171 的首一多项式 $P$、元素 $y$、有理多项式 $t=t(y)$、主 CM 嵌入和 $q$ 进嵌入。
特别地，$q$ 处的基点是 $y_0=-1/89460$，并且 $\alpha=1+89460y$ 的范数为 $-q$。

### 1.1 Eisenstein 方程

证书中的全部整数系数直接给出

$$
P(Y)=Y^{44}+p\sum_{j=0}^{43}c_jY^j,
\qquad
C:=-c_0=70375455224064,
\qquad C\equiv38\pmod {43}.
\tag{185.3}
$$

每个非首项系数可被 $43$ 整除，常数项不能被 $43^2$ 整除。所以 $P$ 在 $43$ 处 Eisenstein，

$$
H_{43}=\mathbf Q_{43}(y),\qquad e(H_{43}/\mathbf Q_{43})=44.
$$

由于 $-1$ 在 $\mathbf F_{43}$ 中非平方，

$$
\mathscr F_{43}=\mathbf Q_{43^2}(y)=H_{43}(i)
\tag{185.4}
$$

是全局 $\mathscr F$ 的唯一 $43$ 进完备化。其惯性群 $C_{44}=\operatorname{Gal}(\mathscr F_{43}/\mathbf Q_{43^2})$
为循环群，$\tau$ 固定 $y$ 并把 $i$ 变成 $-i$。

定义

$$
\pi=y\left(1-\sum_{j=1}^{43}\frac{c_j}{C}y^j\right)^{-1/44},
\tag{185.5}
$$

括号的 $44$ 次根取主单位中的唯一一个。$44$ 是 $43$ 进单位，故 Hensel 引理给出存在唯一性。
$P$ 为偶多项式，所以这个定义满足

$$
\pi^{44}=Cp,\qquad \pi/y\in1+y^2\mathcal O_{H_{43}},\qquad \tau\pi=\pi.
\tag{185.6}
$$

反过来令 $y=\pi u(\pi)$，则 $u\in1+\pi^2\mathbf Z_{43}[[\pi]]$ 是下式唯一的形式幂级数解：

$$
u^{44}-1+\sum_{j=1}^{43}\frac{c_j}{C}\pi^ju^j=0.
\tag{185.7}
$$

在 $u=1,\pi=0$ 处导数为 $44$。因此这里的幂级数解及核验器的 Newton 迭代都有唯一性，不是任意选取一个局部根。

### 1.2 同一个 Artin 方向

仍取 R171 的 Gaussian primary 素元

$$
\beta=-1+2i,\qquad \sigma=\operatorname{Frob}_{(\beta)},\qquad
\omega=\beta^{1-p}=(8,25)\in\mathbf F_{p^2}^{\times}.
$$

$\omega$ 的阶为 $44$。$\sigma$ 在 $A[p]$ 上作用为乘 $\beta$。
在 arithmetic reciprocity 约定下，局部单位 $\beta$ 对 $\pi^{44}=Cp$ 的作用为
$\pi\mapsto[\beta]^{-42}\pi$。全局主理想互反及 $\beta\equiv1\bmod(1+i)^3$ 给
$\sigma=\operatorname{rec}_{43}(\beta)^{-1}$，所以

$$
\sigma\pi=\zeta\pi,\qquad
\zeta=[\beta^{42}]=[\omega]^{-1}.
\tag{185.8}
$$

方括号表示在 $\mathbf Z_{43^2}$ 中的 Teichmüller 提升。
$\zeta^{43}=\zeta^{-1}$。本条没有把 $q$ 处的根标签重新排列；(185.8) 使用的正是 R171 的算术 Frobenius。

## 2. 一个真正的局部 Kummer 基

设 $W=\operatorname{ad}^0(A[p])/\mathbf F_pJ$，其中 $J=i$。
沿用 R161 的实二维写法

$$
D_z(v)=z\bar v,\qquad
F=D_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
K_0=JF=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

$\sigma D_z=D_{\omega z}$，$\tau D_z=D_{\bar z}$。
Kummer 理论和 $[\mathscr F_{43}:\mathbf Q_{43}]=88$ 与 $43$ 互素给出

$$
H^1(\mathbf Q_{43},W(1))
\simeq(\mathscr F_{43}^{\times}/\mathscr F_{43}^{\times p}\otimes W)^ {\operatorname{Gal}(\mathscr F_{43}/\mathbf Q_{43})}.
\tag{185.9}
$$

对 $a\in H_{43}^{\times}$ 定义

$$
\mathcal B([a])=\sum_{j=0}^{43}[\sigma^ja]\otimes D_{\omega^j}.
\tag{185.10}
$$

$C_{44}$ 的下标平移及 $\tau:j\mapsto-j$ 分别证明这个和不变，故它确有唯一的有理局部下降。
这里**不除以 $44$**。它与 R171 的 $q$ 奇异赋值规范完全相同。

### 2.1 Artin–Hasse 基的完整性

写

$$
E_p(X)=\exp\left(\sum_{r\ge0}\frac{X^{p^r}}{p^r}\right)\in1+X\mathbf Z_p[[X]].
$$

其整性可由形式恒等式
$E_p(X)=\prod_{(n,p)=1}(1-X^n)^{-\mu(n)/n}$ 得到。
令

$$
b_1=\mathcal B(E_p(\pi)),\qquad
b_2=\mathcal B(E_p(\pi^{45})).
\tag{185.11}
$$

**引理 185.1。** $(b_1,b_2)$ 是 $H^1(\mathbf Q_{43},W(1))$ 的一组基。

**证明。** 在主单位的 $\mathbf Z_p$ 完备化上考虑整幂等元

$$
e=\frac1{44}\sum_{j=0}^{43}(\zeta^j+\zeta^{-j})\sigma^j.
\tag{185.12}
$$

它的系数在 $\mathbf Z_p$ 中，并与 $\tau$ 交换。$H_{43}$ 不含 $\mu_p$：否则 $42$ 整除 $44$，矛盾。
故主单位群无 $p$ 挠，$p$ 进对数在其中单射。
在加法空间 $H_{43}$ 中，$e$ 的像为

$$
\mathbf Q_p\pi\oplus\mathbf Q_p\pi^{43}.
$$

主单位群的秩为 $44$；例如足够深的主单位经对数同构于一个整数格即可证明这一点。
所以 $e$ 主单位群是秩二的自由 $\mathbf Z_p$ 模。
$p\equiv-1\bmod44$，故 $E_p(\pi)$ 和 $E_p(\pi^{45})$ 的所有对数项均落在该 $e$ 空间。

这两个单位模 $p$ 独立。若一个主单位 $v$ 满足 $v_\pi(v-1)=r\ge1$，则

$$
v_\pi(v^p-1)=\min(pr,44+r)
=\begin{cases}43,&r=1,\\44+r\ge46,&r\ge2.\end{cases}
\tag{185.13}
$$

两项不会同赋值，因为 $44/(p-1)=22/21$ 不是整数。
当 $s\not\equiv0\bmod p$ 时，$E_p(\pi)^sE_p(\pi^{45})^t-1$ 的赋值为 $1$；当 $s=0,t\ne0$ 时赋值为 $45$。
这两种都不可能是 $p$ 次幂。它们因此给出整个 $e$ 主单位模 $p$ 的基。

在 (185.10) 的 $F$ 系数中，$\mathcal B(a)$ 恰等于 $22e[a]$；这是把
$\operatorname{Re}(\omega^j)=(\zeta^j+\zeta^{-j})/2$ 代入所得。
$22$ 是 $p$ 单位，所以 $\mathcal B$ 在此二维空间中单射。
R161 的局部 Euler 特征给 $\dim H^1(\mathbf Q_p,W(1))=2$，或者直接对 (185.9) 做同样的特征分解也可得到此维数。
故 (185.11) 为基。证毕。

这个证明也说明第二条基线具有内在描述：它是该等型 Kummer 空间中由 $U^{45}$ 主单位给出的唯一一维子空间。
后面对平坦线的识别不依赖于交换两个特征嵌入的记号。

## 3. 将原始 Robert 单位压到同一个 $44$ 次域

本节先给全局代数恒等式，避免以形式局部函数替换一个未经识别的全局单位。

### 3.1 规范函数的同源范数

对任意椭圆曲线 $E$ 及整数 $11$，令

$$
F_E(Q)=\frac{\Delta_E^{10}}{\psi_{11,E}(Q)}.
\tag{185.14}
$$

Scholl (1998), Theorem 1.2.1(iii) 和紧随其后的 Remarks(iv)、证明给出了规范 Kato–Siegel 函数对任意次数与 $11$ 互素的同源的范数关系。
其规范函数与 (185.14) 至多差一个对所有曲线相同的符号：两者的除数相同，零截面的规范给出 $\pm\Delta^{10}$。
当同源次数为奇数 $43$ 时，这个符号在范数比中以 $43-1$ 次方出现，因而消失。
所以对任意阶 $43$ 子群 $C'$ 及商同源 $\phi_{C'}$，精确有

$$
\prod_{U\in C'}F_E(Q+U)=F_{E/C'}(\phi_{C'}Q).
\tag{185.15}
$$

这里使用了该规范范数定理，不能仅比较除数后丢弃可能随 $C'$ 变化的常数。

若 $Q_4$ 的阶为 $4$，标准除法多项式递推给

$$
\psi_4(Q_4)=0,\quad \psi_5=-\psi_3^3,\quad
\psi_7=-\psi_3^6,\quad \psi_9=\psi_3^{10},\quad
\psi_{11}=\psi_3^{15}.
$$

因此

$$
F_E(Q_4)=\left(\frac{\Delta_E^2}{\psi_{3,E}(Q_4)^3}\right)^5.
\tag{185.16}
$$

### 3.2 明确的四挠标记

沿用 R171 的二同源

$$
\phi_2:A\longrightarrow B:y^2=x^3-11x-14,
\qquad \ker\phi_2=\langle(1,0)\rangle.
$$

它把 $P_2=(i,1-i)$ 送到 $(-1,-2i)$；此点的二倍为 $R=(-2,0)$。
在 $B$ 中把 $R$ 移到 $x=0$ 后，模型为

$$
y^2=x^3-6x^2+x,
$$

四挠点的 $x$ 坐标为 $1$。
对 $C=\langle P\rangle\subset A[p]$ 做同一个交换的 $2$–$p$ 同源方块。
在 $B/\phi_2(C)$ 中令 $R'$ 为 $R$ 的像，并令四挠点像相对 $R'$ 的 $x$ 坐标为 $r$。
这个 $r$ 在 $H$ 中，因为复共轭把该四挠点变为其负点。
写模型为

$$
y^2=x^3+A_2x^2+r^2x,\qquad w=A_2/r.
$$

R171 的同一个 Hauptmodul 为

$$
\delta=t^3=16(w^2-4).
\tag{185.17}
$$

证书给出一个有理多项式 $h=h(y)$，逐整数验证

$$
\boxed{t^3=16h^2(h^2+4),\qquad h\equiv2\pmod {\pi}.}
\tag{185.18}
$$

它的全部系数属于 $\mathbf Z_{43}$。这个恒等式可用 `nfeltissquare` 找到，但证明和最终核验只使用证书中的有理系数。
于是 $w=\pm(h^2+2)$。

正确符号为 $w=-h^2-2$。说明如下。商去 $R'$ 后的对偶二同源模型，在把 $x$ 除以 $r$ 的记号中，为

$$
y^2=x^3-2wx^2+(w^2-4)x.
\tag{185.19}
$$

$P_2$ 在 $A/C$ 的像经该同构给一个在 $\mathscr F$ 上的四挠点，其二倍的 $x$ 坐标是 $w+2$。
半点公式给其 $x$ 坐标

$$
x=z^2+2z,\qquad z^2=w+2,\qquad z\in\mathscr F.
\tag{185.20}
$$

若 $w=h^2+2$，则 $h^2+4$ 必在 $H(i)$ 中为平方。
一个 $H$ 元素在 $H(i)$ 中为平方，当且仅当它或其负数在 $H$ 中为平方。
但是 $h^2+4\equiv8\bmod\pi$，而 $8$ 在 $\mathbf F_{43}$ 中非平方；它不可能是 $H$ 中的平方。
其负数在 $H$ 的 R171 主实嵌入下为负数，也不可能是平方。
所以只剩 $w=-h^2-2$，且 $z=\pm ih$。

在 (185.19) 中代入 $w=z^2-2$、$x=z^2+2z$，直接计算得到

$$
\psi_3=32z^3(z+2)^2,\qquad
\Delta=256z^4(z-2)^2(z+2)^2,
$$

从而

$$
\frac{\Delta^2}{\psi_3^3}
=U(z):=\frac{2(z-2)^4}{z(z+2)^2}.
\tag{185.21}
$$

### 3.3 全局符号由同一个有限嵌入锁定

令

$$
v=F_A(P_2+P),\qquad
u=N_{T/\mathscr F}v
=\prod_{a\in\mathbf F_p^\times}F_A(P_2+[a]P).
\tag{185.22}
$$

标量 Cartan 元固定 $P_2$，故这个乘积正是所写的域范数。
$F_A(P_2)=2^{15}$。由 (185.15)–(185.21)，$u$ 必等于以下两个全局候选中的一个：

$$
\frac{U(ih)^5}{2^{15}},\qquad \frac{U(-ih)^5}{2^{15}}.
$$

在 R171 已固定的 $q$ 进嵌入、$y_0=-1/89460$ 和同一个实 $p$ 挠点 $P_q$ 下，核验器计算全部 $42$ 个非零标量的原始值。
它与负号候选精确相等，并与正号候选不同。因此

$$
\boxed{u=\frac{U(-ih)^5}{2^{15}}.}
\tag{185.23}
$$

这一步是在已经证明只有两个全局候选之后选择符号，不是由有限域相似数值猜测一个全局单位。
它沿用 R171 的同一 $y$ 嵌入，同时固定了 $P_2$、复共轭和 $p$ 局部计算的符号。

## 4. 有限精度为何决定全部 Kummer 坐标

本节给核验器的无限尾证明。
设 $g(X)\in1+X\mathbf Z_p[i][[X]]$。若

$$
\log g(X)=\sum_{k\ge1}a_kX^k,
$$

则从 $\log(1+V)=\sum_{n\ge1}(-1)^{n+1}V^n/n$ 立即得到

$$
v_p(a_k)\ge-\lfloor\log_pk\rfloor.
\tag{185.24}
$$

按 (185.8)、(185.12) 投影后，只留下 $k\equiv\pm1\bmod44$ 的项。
用 $\pi^{44}=Cp$ 约化，写成

$$
e\log g(\pi)=A\pi+B\pi^{43}.
$$

设 $\ell_k$ 是 $p\log g(X)$ 的系数。模 $p^2$ 足够的公式为

$$
\begin{aligned}
A&\equiv\ell_1/p+C\ell_{45}+C^2p\ell_{89}\pmod {p^2},\\
pB&\equiv\ell_{43}+Cp\ell_{87}\pmod {p^2}.
\end{aligned}
\tag{185.25}
$$

确实，第一行被省略的项有 $k=1+44j,j\ge3$，其赋值至少
$j-\lfloor\log_p(1+44j)\rfloor\ge2$。
第二行被省略的项有 $k=43+44j,j\ge2$，其赋值至少
$j+1-\lfloor\log_p(43+44j)\rfloor\ge2$。
两个不等式从最小的 $j$ 直接检查；之后可由 $43^{j-1}>44j+1$ 及相应更弱的不等式归纳。
所以这些是真正的无限尾界。

程序在 $(\mathbf Z/p^3)[i][X]/(X^{90})$ 中计算 (185.7) 的根及 $p\log g$。
$n\le89$ 时 $p/n$ 总是 $p$ 整的，故没有隐藏分母；只有 (185.25) 的 $\ell_1/p$ 损失一位精度。
先算到 $p^3$ 正好保证它模 $p^2$ 正确。

对于本条用到的两类单位，常数项可以先除掉。该常数属于未分歧基域，$e$ 会杀掉其对数，因此不影响结果。

### 4.1 实单位坐标

Artin–Hasse 对数给

$$
\begin{aligned}
\log E_p(\pi)&=\pi+\pi^{43}/p+\text{本计算中为零的尾项},\\
\log E_p(\pi^{45})&=Cp\pi+\text{本计算中为零的尾项}.
\end{aligned}
$$

例如第一行的下一项是 $\pi^{1849}/p^2=C^{42}p^{40}\pi$；第二行下一项的 $B$ 系数含 $p^{42}$。
因此 $\mathcal B(g)$ 相对 $(b_1,b_2)$ 的坐标为

$$
\left(pB\bmod p,\quad\frac{A-pB}{Cp}\bmod p\right).
\tag{185.26}
$$

分子的整性也由引理 185.1 的基结论保证；程序另外直接检查了所需同余。

### 4.2 原始 Robert 的虚部及 $1/(p^2-1)$

R161 的精确规范是

$$
\xi=\frac1{p^2-1}\sum_{a\in\mathbf F_{p^2}^{\times}}
a^{1-p}[\sigma_av],\qquad d^{\rm Rob}_p=i\xi.
\tag{185.27}
$$

把标量 $a\in\mathbf F_p^\times$ 先求和，(185.22) 给

$$
d^{\rm Rob}_p=\frac1{1848}\,\mathcal J\mathcal B(u),
\qquad \mathcal J:D_z\longmapsto D_{iz}.
\tag{185.28}
$$

这里 $u$ 一般不属于 $H$。由 $\tau v=\sigma_{-i}v$，并且 $-i$ 的投影是 $\sigma^{22}$，有

$$
\tau u=\sigma^{22}u.
$$

由于 $e$ 对数的两个指数均为奇数，$e\log u$ 必为

$$
e\log u=iA\pi+iB\pi^{43},\qquad A,B\in\mathbf Q_p.
\tag{185.29}
$$

这个复共轭同时作用于单位和系数；不能漏掉系数 $i\mapsto-i$。
相对 $E_p(i\pi),E_p(i\pi^{45})$，虚部的两个坐标是

$$
\left(-pB\bmod p,\quad\frac{A+pB}{Cp}\bmod p\right).
\tag{185.30}
$$

为把它变成 (185.11) 的坐标，注意 $\zeta=[\omega]^{-1}$，所以 $\mathcal B$ 对 $\pi$、$\pi^{43}$ 的对数像分别沿着
$F-iK_0$、$F+iK_0$；左乘 $J$ 分别乘 $i$、$-i$。
由此逐项得到

$$
\mathcal J\mathcal B(E_p(i\pi^r))=-\mathcal B(E_p(\pi^r)),
\qquad r=1,45.
\tag{185.31}
$$

最后 $-1/1848\equiv1\bmod43$。因此 (185.30) **正好**是 R161 的 $d^{\rm Rob}_p$ 在 (185.11) 中的坐标。
这一步保留了原始 Robert 倒数、标量范数、整个 Cartan 的 $1/1848$、$\mathcal J$ 和复共轭，没有把任意同一直线的生成元换成原规范生成元。

## 5. 实际输出

对 $\alpha=1+89460y$，(185.25) 给

$$
A\equiv407,\qquad pB\equiv1095\pmod {1849}.
$$

所以 (185.26) 给 $(20,29)$。
对 (185.23) 的 $u$，(185.29) 的虚部给

$$
A\equiv927,\qquad pB\equiv320\pmod {1849},
$$

实部均为 $0\bmod1849$，(185.30) 给 $(24,20)$。

核验器记录的 $p\log$ 系数如下；Robert 一列写成 $(\text{实部},\text{虚部})\bmod79507$。

| $k$ | $p\log\alpha$ | $p\log(u/u(0))$ |
|---:|---:|---:|
| $1$ | $30444$ | $(14792,73143)$ |
| $43$ | $67659$ | $(1849,29904)$ |
| $45$ | $57749$ | $(79206,53406)$ |
| $87$ | $516$ | $(58437,51729)$ |
| $89$ | $68112$ | $(47171,8428)$ |

这些单项不必逐一是纯实或纯虚；用 $\pi^{44}=Cp$ 约化并做特征投影后才得到 (185.29)。
两个实际类的行列式为

$$
20\cdot20-29\cdot24\equiv5\pmod {43},
\tag{185.32}
$$

因此它们的 $p$ 局部值线性独立。这一点本身不需要下一节的平坦线识别。

## 6. 实际有限平坦条件恰杀掉高单位线

令 $L_{\rm fl}\subset H^1(\mathbf Q_p,W)$ 为 R161/R180 的固定 cyclotomic determinant 有限平坦切线。
已证 $\dim L_{\rm fl}=1$，其生成元由 R180 的完整晶体迹参数 $t$ 规范。

**引理 185.2。** 在 (185.11) 的规范下，

$$
\boxed{L_{\rm fl}^{\perp}=\mathbf F_p b_2.}
\tag{185.33}
$$

**证明。** 限制到未分歧二次域 $\mathbf Q_{p^2}$ 后，残余 $A[p]$ 在扩系数后分成两个 CM 特征线，
惯性特征为 $\psi,\psi^p$。平坦自扩张可在权 $0,1$ 的 Fontaine–Laffaille 精确范畴中，对其子对象和商对象用这两个残余 CM 幂等元作 pullback/pushout。
所得非对角扩张仍来自有限平坦群概形。
也可以直接对整个被 $p$ 杀死的四维平坦自扩张使用 Fontaine 的分歧界，再取野惯性上的非对角分量。
二者都不需要声称扭曲成 $\left(\begin{smallmatrix}\chi&*\\0&1\end{smallmatrix}\right)$ 后仍是有限平坦群概形；这里只用 tame 扭曲不改变野惯性。

两个非对角比值为 $\psi^{1-p}$、$\psi^{p-1}$。
在 DDR (2016), §8.4 的标签下，二者通过交换两个嵌入写成 Case III 的签名 $(p-2,p)$。
于是

$$
n_0=p^2+p-2,\qquad e=p+1=44,\qquad
n'_1=\frac{e n_0}{p^2-1}=p+2=45,\qquad n'_0=1.
\tag{185.34}
$$

DDR 的式 (15)、(16) 给出如下已经证明的局部类域论事实：这两个 AH 层分别为 $1$ 和 $45$；
杀掉全部高层 $E_p([a]\pi^{45})$ 的扩张直线是低分歧直线。
其两个可能的非零斜率（上分歧 break 加 $1$）为

$$
1+\frac1{44}=\frac{45}{44},\qquad
1+\frac{45}{44}=\frac{89}{44}.
$$

DDR p.15 明确说明 Fontaine (1985), §2.1 的有限平坦分歧界使原始有限平坦扩张落入
$\operatorname{Fil}^{p/(p-1)}=\operatorname{Fil}^{43/42}$。
由于

$$
\frac{45}{44}<\frac{43}{42}<\frac{89}{44},
$$

它必须在上述低分歧直线上。该子空间是一维，$L_{\rm fl}$ 也是一维，故二者相等。

在 (185.9) 的局部 Tate 配对中，类域论的求值正是 Kummer 单位与该特征扩张的配对。
所以这个低分歧直线的正交空间为高单位线。
引理 185.1 已在本条自己的 $\pi$ 和 $\mathcal B$ 规范中把它识别成 $\mathbf F_p b_2$。
交换 DDR 的特征嵌入标签，或把其 geometric Artin 改为本文 arithmetic Artin，只改变相应求值的非零标量，不交换单位过滤层 $1$ 与 $45$。
这避免了在最后一步未经说明地互换 AH 坐标。证毕。

此处只使用 DDR 已证明的 AH/分歧计算与有限平坦上界；没有使用其一般 Conjecture 7.2，也不需要把未证明的 Serre 权重配方当作输入。

### 6.1 R180 的校正现在有确切值

取 R180 的同一个晶体迹切线 $f$，记

$$
k=\langle f,\operatorname{loc}_p d_p^{\rm Rob}\rangle_p\ne0.
$$

由 (185.33)，对 $(b_1,b_2)$ 的配对只读第一坐标，并且在 $b_1$ 上非零。
故

$$
\beta_q=
\frac{\langle f,\operatorname{loc}_p d_q\rangle_p}
{\langle f,\operatorname{loc}_p d_p^{\rm Rob}\rangle_p}
=\frac{20}{24}=8\in\mathbf F_{43}.
$$

令 $\widetilde d_q=d_q-8d_p^{\rm Rob}$，则

$$
\operatorname{loc}_p\widetilde d_q=(0,41)\ne0,
\qquad \operatorname{loc}_p\widetilde d_q\in L_{\rm fl}^{\perp}.
$$

R171 已证 $\operatorname{loc}_q d_p^{\rm Rob}=0$，所以 $\widetilde d_q$ 的 $q$ 奇异坐标仍为 $1$，有限坐标仍为 $\lambda_q=16$。
在这个单素数实例中，R180 的 $p$ 正规化局部矩阵仍是 $\widetilde C=(16)$。

## 7. 已得到的接口及尚未得到的二阶量

本条实际计算了：

1. 同一个主化元的两个 $p$ 局部 Kummer 坐标；
2. R161 精确原始 Robert 生成元的同基坐标；
3. 有限平坦正交线、实际全局 $q$–$S$–unit 校正系数 $8$，以及校正后非零局部类 $(0,41)$。

这给出后续二阶计算所需的一个确切局部分裂。它没有计算 R176 中把一个给定模 $p^2$ 全局表示抬到模 $p^3$ 时产生的非线性二上链，也没有计算其与 $d_p^{\rm Rob}$ 的局部配对。
因此既没有得到 $\Omega_2$，也没有得到 $t_q/43^2$；甚至晶体迹规范下的单独非零比例 $k$，也不能从一个平坦子空间的识别自动读出。

R171 的 Gaussian $5$ 条件已经排除这个 $q$ 来自实际椭圆曲线。
R180 已经构造的完整平坦 $\mathbf Z_{43}$ 表示与这一事实不矛盾。
本条提供的是同一真实全局类的实际局部数据，不把它改称为新的椭圆曲线候选或一致性问题的排除。

复算入口：

```bash
python3 verify_r185_p_local_kummer.py --check
```

完整证明中的无限尾界及平坦线识别是数学输入；程序精确验证有理恒等式、唯一局部根方程、原有 $q$ 的同源标记符号和全部所列整数坐标。

## 参考文献

- A. J. Scholl, **An introduction to Kato's Euler systems**, in *Galois Representations in Arithmetic Algebraic Geometry*, London Mathematical Society Lecture Note Series 254, Cambridge University Press, 1998, pp. 379–460. Theorem 1.2.1(iii)、Remarks(iv) 及其证明，印刷 pp.384–386。
  [作者全文](https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf)。这里只用规范 Kato–Siegel 函数的同源范数，不用其 Euler 系统结论。
- L. Dembélé, F. Diamond and D. P. Roberts, **Serre weights and wild ramification in two-dimensional Galois representations**, *Forum of Mathematics, Sigma* 4 (2016), e33, 49 pp., DOI 10.1017/fms.2016.27. 本文使用 p.15 的 finite-flat 分歧说明、§8.4 pp.36–37 的 Case III 以及式 (15)、(16)。
  [期刊全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/58CBCE9CC2568B368ADA26B550AD5070/S205050941600027Xa.pdf/serre_weights_and_wild_ramification_in_twodimensional_galois_representations.pdf)。
- J.-M. Fontaine, **Il n'y a pas de variété abélienne sur $\mathbf Z$**, *Inventiones Mathematicae* 81 (1985), pp.515–538, §2.1，DOI 10.1007/BF01388584。所需有限平坦分歧界的规范按 DDR p.15 的陈述使用。
- [R161](R161-strict-adjoint-selmer-line-and-tate-support-orthogonality.md)、[R163](R163-all-prime-primitive-adjoint-robert-generator.md)、[R168](R168-tate-frobenius-sunit-slopes-and-weil-squareclasses.md)、[R171](R171-principal-norm-selflocal-tate-slope.md)、[R180](R180-flat-tate-lifting-and-canonical-crystalline-trace.md)：分别提供原始单位规范、全局生成、局部有限/奇异坐标、同一个全局域与主化实例，以及平坦变形参数及其矩阵校正。
