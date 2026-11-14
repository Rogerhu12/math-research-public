# R141：相邻有限胞块的高阶Carleman循环判据

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。

状态：下述定理及连通高次数例均已完整证明。它允许 Walsh 次数和逐位参与数都无界，也允许局部纯乘子的范数趋于无穷。核心条件只控制改变胞块占据状态的矩阵块；保持固定占据集合的内部矩阵留在自伴直和中，不作统一范数估计。

本条不把一般局部有限支撑自动判为循环。局部有限性保证可作相邻胞块分解；还须检验下文的跨状态界与真实进位条件。

## 1. 假设与主定理

把全部物理位分成非空有限集合

$$
\mathbb N_0=\bigsqcup_{n\ge1}J_n.
$$

不要求 $|J_n|$ 有统一上界，也不要求它们是连续区间。记

$$
H_n=L^2(\{0,1\}^{J_n}),\qquad
\Omega_n=1,\qquad
P_n^{\rm vac}=|\Omega_n\rangle\langle\Omega_n|,
\quad Q_n^{\rm occ}=I-P_n^{\rm vac}.
$$

以下称第 $n$ 个胞块非真空为“占据”。每个 $H_n$ 有限维，且
$H_n=\mathbb C\Omega_n\oplus K_n$，$K_n=\Omega_n^\perp$。

对每个 $n$，取一个只依赖 $J_n\cup J_{n+1}$ 的有限柱函数 $f_n$，满足

$$
\int f_n\,d\mu=0,\qquad
\sigma^2:=\sum_{n\ge1}\|f_n\|_2^2<\infty.
\tag{1.1}
$$

允许某些 $f_n=0$。写其有限 Walsh 展开为

$$
f_n=\sum_{\varnothing\ne F\subseteq J_n\cup J_{n+1}}a_{n,F}\chi_F.
$$

定义纯与实际有限乘子

$$
L_n^0=\sum_Fa_{n,F}S_F,\qquad
L_n=\sum_Fa_{n,F}V_F,
\quad S_j=I-2E_j,\quad
V_j=(I-N_j)(I+N_j)^{-1}.
\tag{1.2}
$$

这里 $E_j=e_{10}$ 是物理一位的 raising 矩阵单位，$S_F=\prod_{j\in F}S_j$、
$V_F=\prod_{j\in F}V_j$。纯算子 $L_n^0$ 只作用于两个胞块，实际 $L_n\in\mathcal A$ 则保留真实进位。两者均把 $1$ 送到 $f_n$，且各自满足 $C$ 对称。

对两胞块的状态 $s=(s_1,s_2)\in\{00,10,01,11\}$，记

$$
\Pi_{n,s}=R_{n,s_1}R_{n+1,s_2},
\qquad R_{j,0}=P_j^{\rm vac},\quad R_{j,1}=Q_j^{\rm occ}.
$$

假定存在有限 $M$，使

$$
\boxed{
\|\Pi_{n,t}L_n^0\Pi_{n,s}\|\le M
\quad(n\ge1,\ s,t\in\{10,01,11\},\ s\ne t).
}
\tag{1.3}
$$

不要求任何对角状态块 $\Pi_{n,s}L_n^0\Pi_{n,s}$ 的范数一致有界。
最后假定真实差可和：

$$
\boxed{\sum_{n\ge1}\|L_n-L_n^0\|<\infty.}
\tag{1.4}
$$

**主定理。** $f=a_*+\sum_nf_n$ 在 $H$ 中收敛。若 $f\ne0$，则 $f$ 对实际 $A$ 循环。存在以有限物理柱为图核心的闭算子 $X_f$，满足

$$
X_f1=f,\qquad X_f^*=CX_fC,\qquad
\overline{\operatorname{Ran}X_f}=\operatorname{cyc}_A(f).
\tag{1.5}
$$

每个有界交换子保持其定义域并与之域交换。若 $f$ 非常数，则对每个 $\lambda\in\mathbb C$，

$$
\ker(X_f-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(X_f-\lambda I)}=H,
\qquad f-\lambda\text{ 循环}.
\tag{1.6}
$$

不要求 $X_f$ 有界，也不声称一般有限 Walsh 次数空间都包含于其定义域。本文使用的图核心是有限物理柱。

## 2. 初始纯算子与有限占据集合

相同奇偶性的相邻胞块对 $J_n\cup J_{n+1}$ 两两不交。其 $f_n$ 均值为零，故每个奇偶类内正交。由 (1.1)，两个子级数均在 $H$ 中收敛，因而 $\sum_nf_n$ 收敛，且

$$
\left\|\sum_nf_n\right\|_2\le\sqrt2\,\sigma.
\tag{2.1}
$$

按有限占据集合分解全空间：

$$
H=\bigoplus_{S\Subset\mathbb N}H_S,
\qquad H_S=\bigotimes_{j\in S}K_j,
\qquad \mathcal H_q=\bigoplus_{|S|=q}H_S.
\tag{2.2}
$$

每个 $H_S$ 有限维。有限物理柱空间 $\mathcal P$ 正是这些 $H_S$ 的有限代数直和：有限物理位只碰有限个胞块，有限胞块的并也只含有限物理位。

在 $\mathcal P$ 上定义

$$
T_0x=a_*x+\sum_{n\ge1}L_n^0x.
\tag{2.3}
$$

若 $x$ 只依赖有限胞块集合 $B$，与 $B$ 相交的相邻对只有有限多个。其他项作用为外张量 $x\otimes f_n$；分别在奇偶类中，它们两两正交并受 (1.1) 控制。所以 (2.3) 对每个 $x\in\mathcal P$ 收敛。

每个 $L_n^0$ 对块反射共轭 $C$ 对称，且 $C1=1$，故

$$
(L_n^0)^*1=Cf_n,\qquad\|Cf_n\|_2=\|f_n\|_2,
\qquad\langle (L_n^0)^*1,1\rangle=0.
$$

同一论证定义了通常形式伴随

$$
T_0^\dagger=CT_0C\quad\text{于 }\mathcal P.
$$

二者满足通常伴随配对，故都可闭。其 Dirac 块

$$
\mathscr T_0=
\begin{pmatrix}0&T_0^\dagger\\T_0&0\end{pmatrix}
\quad\text{于 }\mathcal P\oplus\mathcal P
\tag{2.4}
$$

稠密定义且对称。

## 3. 无界内部矩阵形成真正的自伴对角直和

将每个 $L_n^0$ 分成三类矩阵块：

1. 相同状态 $s\to s$；
2. $00\leftrightarrow s$，$s\ne00$；
3. 非零且不同的状态 $s\to t$。

第一类保持整个占据集合 $S$。特别地，

$$
\Pi_{n,00}L_n^0\Pi_{n,00}
=\langle f_n,1\rangle\Pi_{n,00}=0.
\tag{3.1}
$$

因此固定有限 $S$ 后，第一类只涉及满足 $\{n,n+1\}\cap S\ne\varnothing$ 的相邻对；其个数至多 $2|S|$。它在有限维 $H_S$ 上给出一个有限矩阵 $D_S$，并加上单个常数项 $a_*I$。没有来自远处 $00$ 状态的无限标量背景。

Dirac 的相应对角部分为

$$
\mathscr D_S=
\begin{pmatrix}0&D_S^*\\D_S&0\end{pmatrix}.
$$

对固定 $q$ 取自然自伴直和

$$
\mathscr D_q=\bigoplus_{|S|=q}\mathscr D_S,
\quad
\operatorname{Dom}\mathscr D_q
=\left\{(x_S):\sum_{|S|=q}\|\mathscr D_Sx_S\|^2<\infty\right\}.
\tag{3.2}
$$

每个小块有限维且自伴，所以 (3.2) 自伴，有限 $S$ 支撑是其图核心。允许 $\|D_S\|$ 随 $S$ 任意增长。

剩余第二、三类组成 Dirac 的 $\mathscr W$ 部分。下面只估计 $\mathscr W$，不把整个 $\mathscr D_q$ 误作有界等级块。

## 4. 真空通道：奇偶不交对给平方根等级界

令

$$
F_n=(I-\Pi_{n,00})L_n^0\Pi_{n,00}.
$$

这是把两胞块真空送到 $f_n$ 的秩一局部创建通道；其范数是 $\|f_n\|_2$。
反向通道由 $(L_n^0)^*1=Cf_n$ 描述，具有相同范数。

对固定奇偶类，视每个不交相邻对为一个较大块。按非真空大块数分级，通常无重复创建估计给

$$
\|\text{创建}:\text{等级 }r\to r+1\|
\le\sqrt{r+1}
\left(\sum_{n\text{ 属于该类}}\|f_n\|_2^2\right)^{1/2}.
\tag{4.1}
$$

证明是对输出的 $r+1$ 个可能新加入块作 Cauchy–Schwarz，再对输入块集合求和。局部向量的内部维数不影响此界。删除取伴随，得 $\sqrt r$ 的同型界。

若原胞块占据数恰为 $q$，则每个奇偶分组内的非真空大块数至多 $q$。因此 (4.1) 对整个 $\mathcal H_q$ 成立。对两个奇偶类求和，并对 Dirac 两个自旋分量使用相同估计，第二类的总贡献满足安全界

$$
\|\mathscr W^{\rm vac}x\|
\le4\sigma\sqrt{q+1}\,\|x\|,
\qquad x\in\mathcal H_q\oplus\mathcal H_q.
\tag{4.2}
$$

创建可增加一个或两个胞块占据数，删除相反；所以这部分只连接 $q$ 与 $q\pm1,q\pm2$。

奇偶分组只在本节用于估计真空通道。没有把两个分组的无界内部算子相加后直接宣称其闭包自伴。

## 5. 非零状态转移：块 Schur 界为线性等级增长

考虑 $s,t\in\{10,01,11\}$、$s\ne t$ 的局部压缩。它只把占据集合

$$
S\longmapsto
S'=\bigl(S\setminus\{n,n+1\}\bigr)\cup t
$$

改变在两个胞块内，且输入、输出的局部状态都非零。因此
$|S'|-|S|\in\{-1,0,1\}$。

固定输入 $|S|=q$，可作用的相邻对至多 $2q$ 个；每对只有另外两个非零目标状态，所以至多 $4q$ 个带重数的转移。固定输出 $|S'|=r$，反向同理至多 $4r$ 个来源。每个局部矩阵块的范数由 (1.3) 不超过 $M$，外部张量恒等不改变范数。

所用 Hilbert 块 Schur 不等式如下：若块矩阵 $B_{ST}$ 满足

$$
\sup_S\sum_T\|B_{ST}\|\le R,\qquad
\sup_T\sum_S\|B_{ST}\|\le C,
$$

则 $\|B\|\le\sqrt{RC}$。这是先对每一行用带权 Cauchy–Schwarz，得到

$$
\left\|\sum_TB_{ST}x_T\right\|^2
\le\left(\sum_T\|B_{ST}\|\right)
\left(\sum_T\|B_{ST}\|\|x_T\|^2\right),
$$

再对 $S$ 求和。多条局部转移落入同一个块时，先以范数三角界合并；上述带重数计数仍有效。

因此从 $q$ 到 $r$ 的第三类块满足

$$
\|\mathscr W^{\rm nz}_{r,q}\|
\le4M\sqrt{qr}
\quad(|r-q|\le1),
\tag{5.1}
$$

Dirac 两个自旋分量具有相同界；通常伴随只交换 $s,t$，不改变 (1.3)。
对三个可能等级求和，可取安全界

$$
\|\mathscr W^{\rm nz}x\|
\le12M(q+1)\|x\|.
\tag{5.2}
$$

结合 (4.2)，置 $K=4\sigma+12M$，得到

$$
\boxed{
\|\mathscr Wx\|\le K(q+1)\|x\|,
\qquad
\mathscr W_{r,q}=0\quad(|r-q|>2).
}
\tag{5.3}
$$

有限部分在每个等级上强收敛并给这些有界块：第三类对有限 $S$ 支撑只有有限项；第二类由奇偶类的平方可和尾收敛。统一范数界将强收敛从稠密的有限 $S$ 支撑推广到完整等级；这里没有要求第三类的尾算子范数趋于零。各互逆等级块互为通常伴随，源于初始 Dirac 的对称性。

## 6. 两级分组后的块 Carleman 证明

将相邻两个等级合并，记

$$
\mathscr K_m=(\mathcal H_{2m}\oplus\mathcal H_{2m})
\oplus(\mathcal H_{2m+1}\oplus\mathcal H_{2m+1}),
\qquad m\ge0.
$$

由 (5.3)，Dirac 在这些大等级上只连接 $m-1,m,m+1$。
大等级的对角算子是

$$
\mathscr A_m=(\mathscr D_{2m}\oplus\mathscr D_{2m+1})
+1_{\mathscr K_m}\mathscr W1_{\mathscr K_m}.
\tag{6.1}
$$

第二项是有界对称算子，范数不超过 $4K(m+1)$；所以 $\mathscr A_m$ 自伴，定义域为前一自伴直和的定义域，有限 $S$ 支撑仍是图核心。
相邻大等级的块 $\mathscr B_m:\mathscr K_m\to\mathscr K_{m+1}$ 也满足

$$
\|\mathscr B_m\|\le4K(m+1).
\tag{6.2}
$$

这些界可直接对两个输入小等级分别使用 (5.3) 再用 Cauchy–Schwarz 得到；常数取了余量。

若 $K=0$，只剩 (3.2) 的自伴直和，结论直接成立。设 $K>0$，取
$\xi\in\ker(\mathscr T_0^*-iI)$，写 $\xi=(\xi_m)$。
先用第 $m$ 大等级中有限 $S$ 支撑的测试向量。相邻项由 (6.2) 对测试向量有界，因此伴随恒等式使
$\langle\mathscr A_mx,\xi_m\rangle$ 由一个 Hilbert 向量表示。
测试域是 $\mathscr A_m$ 的图核心，故

$$
\xi_m\in\operatorname{Dom}\mathscr A_m^*
=\operatorname{Dom}\mathscr A_m,
$$

并得到真实等级方程

$$
i\xi_m=\mathscr A_m\xi_m+
\mathscr B_{m-1}\xi_{m-1}+\mathscr B_m^*\xi_{m+1}.
\tag{6.3}
$$

对 $m=0,\ldots,N$ 配对 $\xi_m$ 后求和取虚部。对角项现在已合法地为实数，内部相邻项成共轭对相消，只剩边界：

$$
\sum_{m=0}^N\|\xi_m\|^2
\le4K(N+1)\|\xi_N\|\|\xi_{N+1}\|.
\tag{6.4}
$$

若 $\xi\ne0$，左边从某处起至少为 $c>0$，所以

$$
\|\xi_N\|^2+\|\xi_{N+1}\|^2
\ge\frac{c}{2K(N+1)}.
$$

对 $N$ 求和与 $\xi\in H\oplus H$ 矛盾。另一缺陷符号取相反虚部，论证相同。两缺陷核为零；闭对称算子的 $\pm i$ 值域由图范数恒等式闭，再由缺陷核零而稠密，故满射。因此 $\mathscr T_0$ 本质自伴。

Dirac 图范数分解成两个分量，令 $X_0=\overline{T_0}$，得到

$$
\boxed{X_0^*=\overline{T_0^\dagger}=CX_0C.}
\tag{6.5}
$$

$\mathcal P$ 按定义是两者的图核心。本证明没有要求 $T_0\mathcal P\subseteq\mathcal P$，也没有要求无界内部对角被占据数控制。

## 7. 加入实际进位、真实域交换及闭加性 gauge

由 (1.4)，

$$
K_f=\sum_n(L_n-L_n^0)
$$

按算子范数绝对收敛。每项 $C$ 对称，所以 $K_f^*=CK_fC$。定义

$$
X_f=X_0+K_f,\qquad\operatorname{Dom}X_f=\operatorname{Dom}X_0.
$$

它闭，$\mathcal P$ 仍为图核心，且 $X_f^*=CX_fC$。有限实际部分

$$
T_N=a_*I+\sum_{n\le N}L_n\in\mathcal A
$$

在 $\mathcal P$ 上趋于 $X_f$，伴随同样收敛；特别 $X_f1=f$。

对任意 $D\in\{A\}'$，有限部分交换与 $B$ 对称给

$$
B(Dx,T_Nz)=B(DT_Nx,z)\qquad(x,z\in\mathcal P).
$$

取极限，再用 $\mathcal P$ 的伴随图核心及 $C$ 自伴性，得到
$Dx\in\operatorname{Dom}X_f$、$X_fDx=DX_fx$。对一般域向量用图逼近及闭性推广。这给全部有界交换子的真实域交换。

若 $u$ 是有限柱，其实际有界乘子 $X_u\in\mathcal A$ 满足 $X_u1=u$。于是
$X_fu=X_uf\in\operatorname{cyc}_A(f)$。图核心给
$\overline{\operatorname{Ran}X_f}\subseteq\operatorname{cyc}_A(f)$；反向由
$X_fA^n1=A^nf$ 给出。这证明 (1.5) 的值域恒等式。

固定 $\zeta^{2^m}=1$。前 $m$ 个物理位只碰有限个胞块，每个胞块只邻接两个局部对。因此只有有限个 $L_n$ 的 gauge 发生变化；充分大有限部分的差稳定为一个真正有理解析芽 $F_\zeta(A)$。$U_\zeta$ 双向保持有限物理柱，故在该共同图核心上取极限再取闭包，得到

$$
U_\zeta X_fU_\zeta^*=X_f+F_\zeta(A)
\tag{7.1}
$$

以及完整定义域相等。

R125 §9 的闭加性 cocycle 定理现在逐项适用：有限柱图核心、$C$ 自伴、全部有界交换子的域交换及 (7.1) 都已证明。非标量时，每个 $X_f-\lambda I$ 的核为零且像稠密；(1.5) 给 $f-\lambda$ 循环。若 $X_f$ 是标量，则 $f=X_f1$ 是常数，非零情形直接由 $1$ 循环处理。主定理得证。

## 8. 一般局部有限超图如何进入本判据

设 $\mathcal F$ 为非空有限物理位集的族，对每个固定物理位 $j$，包含 $j$ 的 $F\in\mathcal F$ 只有有限多个；不要求这个数或 $|F|$ 有统一上界。

可构造递增有限集合 $K_n$，使 $\bigcup_nK_n=\mathbb N_0$，且

$$
F\cap K_n\ne\varnothing\quad\Longrightarrow\quad F\subseteq K_{n+1}.
\tag{8.1}
$$

具体取 $K_0=\varnothing$；从 $K_n$ 出发，加入所有与它相交的 $F$ 的顶点，并加入最小的尚未包含的物理位。局部有限性使这一步加入的集合有限；新增最小缺位保证严格增长并最终覆盖全部物理位。置
$J_n=K_n\setminus K_{n-1}$。

若 $F$ 最早碰到第 $n$ 个胞块，则 $F\cap K_{n-1}=\varnothing$，而 (8.1) 给

$$
F\subseteq J_n\cup J_{n+1}.
\tag{8.2}
$$

把每个 Walsh 项分给其最早胞块，可写成本文的 $f_n$。每个 $f_n$ 只有有限项；不同 $n$ 使用不同 Walsh 集合。因此若原系数平方可和，

$$
\sum_n\|f_n\|_2^2=\sum_{F\in\mathcal F}|a_F|^2<\infty.
$$

所以对一般局部有限支撑，(1.1) 及相邻结构是自动可建立的。新增要核验的条件准确为跨非零状态界 (1.3) 和实际差可和 (1.4)。本条不声称两者也自动成立。

一个充分的显式进位条件是

$$
\sum_n\sum_{\varnothing\ne F\subseteq J_n\cup J_{n+1}}
|a_{n,F}|\,8^{|F|}\sum_{j\in F}\eta_j<\infty.
\tag{8.3}
$$

因为 $\|V_j\|\le6$、$\|S_j\|\le3$、$\|V_j-S_j\|\le8\eta_j$，有限乘积望远镜式给
$\|V_F-S_F\|\le8^{|F|}\sum_{j\in F}\eta_j$。下面的例子使用更好的 raising 乘积估计，不必承担这个指数次数因子。

## 9. 连通、次数与参与数都无界的具体例子

取连续胞块 $J_n$，长度

$$
k_n=\left\lceil2\log_2(n+1)\right\rceil,\qquad
m_n=2^{-k_n}.
$$

它们按自然次序分割物理位。于是

$$
\frac1{2(n+1)^2}<m_n\le\frac1{(n+1)^2}.
\tag{9.1}
$$

### 9.1 物理 raising 算子与实际乘子必须区分

定义

$$
E_{J_n}=\prod_{j\in J_n}E_j.
$$

它是物理张量矩阵单位 $|\boldsymbol1\rangle\langle\boldsymbol0|$，不是事件乘法算子；其范数是 $1$。只在作用于参考向量时，

$$
E_{J_n}\Omega_n=1_{\{\text{该胞块全部位为1}\}}=:e_n,
\qquad \|e_n\|_2=\sqrt{m_n},\quad
\langle e_n,\Omega_n\rangle=m_n.
\tag{9.2}
$$

对局部反射共轭，$E_{J_n}^*=C_nE_{J_n}C_n$。取

$$
L_n^0=n\bigl(E_{J_n}E_{J_{n+1}}-m_nm_{n+1}I\bigr).
\tag{9.3}
$$

这是有限 $S_j$ 多项式，因为 $E_j=(I-S_j)/2$；它 $C$ 对称。对应向量

$$
f_n=n(e_ne_{n+1}-m_nm_{n+1})
\tag{9.4}
$$

均值恰为零，且

$$
\|f_n\|_2^2
=n^2\bigl(m_nm_{n+1}-m_n^2m_{n+1}^2\bigr)
\le\frac{n^2}{(n+1)^2(n+2)^2}
\le\frac1{(n+2)^2}.
\tag{9.5}
$$

因此 (1.1) 成立。

### 9.2 跨状态界为1，内部范数仍可增长

相对于 $\Omega_n\oplus K_n$，写

$$
E_{J_n}=\begin{pmatrix}m_n&g_n^*\\v_n&D_n\end{pmatrix}.
$$

这里

$$
\|v_n\|=\|g_n\|=\sqrt{m_n-m_n^2}\le\sqrt{m_n},
\qquad\|D_n\|\le1.
\tag{9.6}
$$

两个非零且不同的占据状态之间的转移，必在至少一个胞块上使用 $v_j$ 或 $g_j^*$：例如 $10\to11$ 的范数至多 $n\|D_n\|\|v_{n+1}\|$，$10\to01$ 的范数至多 $n\|g_n\|\|v_{n+1}\|$。其余四种同理。减去的标量只作用于相同状态。因此每个这样的块都满足

$$
\|\Pi_{n,t}L_n^0\Pi_{n,s}\|
\le n\max(\sqrt{m_n},\sqrt{m_{n+1}})
\le\frac{n}{n+1}<1.
\tag{9.7}
$$

可取 $M=1$。

相反，$D_n=Q_n^{\rm occ}E_{J_n}Q_n^{\rm occ}$ 的范数实际为 $1-m_n$：它是两个长度 $\sqrt{1-m_n}$ 的投影物理基向量所成的秩一算子。所以 $11\to11$ 内部块的范数至少

$$
n(1-m_n)(1-m_{n+1})-nm_nm_{n+1}\longrightarrow\infty.
\tag{9.8}
$$

这正是本定理允许而不放入跨等级估计的无界内部部分。

### 9.3 真实进位差可和

实际 raising 对应物是

$$
Y_j=N_j(I+N_j)^{-1}=(I-V_j)/2,
\qquad Y_J=\prod_{j\in J}Y_j.
$$

它不是 $E_J$，但

$$
\|Y_j-E_j\|\le4\eta_j,
\qquad\|Y_j\|\le1+4\eta_j.
$$

令 $H_\eta=\sum_j\eta_j<\infty$。对任意有限位集 $J$，乘积望远镜式给

$$
\|Y_J-E_J\|
\le4e^{4H_\eta}\sum_{j\in J}\eta_j.
\tag{9.9}
$$

混合纯、实际因子无需交换；每个剩余乘积的范数均由
$\prod_j(1+4\eta_j)\le e^{4H_\eta}$ 控制。

令

$$
L_n=n\bigl(Y_{J_n}Y_{J_{n+1}}-m_nm_{n+1}I\bigr)\in\mathcal A.
$$

这是 (9.3) 对应的真实有限 Walsh 乘子。不同位的真实乘子在未使用位的向量上精确点乘，故 $Y_{J_n}Y_{J_{n+1}}1=e_ne_{n+1}$，所以 $L_n1=f_n$。

由 (9.9)，

$$
\sum_n\|L_n-L_n^0\|
\le4e^{4H_\eta}\sum_n n\sum_{j\in J_n\cup J_{n+1}}\eta_j
\le8e^{4H_\eta}\sum_{j\ge0}(j+1)\eta_j<\infty.
\tag{9.10}
$$

最后一步用每个物理位只属于一个胞块、只被两个相邻对计数，以及自然排列时 $j\in J_n$ 蕴含 $n\le j+1$。本题超快 $\eta_j$ 保证右侧收敛。

所以全部主定理假设成立，得到

$$
\boxed{
f=\sum_{n\ge1}n(e_ne_{n+1}-m_nm_{n+1})
\quad\text{对实际 }A\text{ 循环}.
}
\tag{9.11}
$$

### 9.4 这确实是无界、连通而无全局次数界的范围

因
$c_*:=\sum_n nm_nm_{n+1}<\infty$，非负随机级数

$$
G(y)=\sum_n n e_n(y)e_{n+1}(y)
$$

在 $L^1$ 中收敛且几乎处处有限。由已证的 $L^2$ 收敛，其与 (9.11) 的关系为 $f=G-c_*$。对每个 $n$，事件 $e_ne_{n+1}=1$ 有正测度，并在其上 $G\ge n$。所以 $f$ 没有本质有界代表。

其实际闭乘子也无界。取非负归一化有限柱

$$
x_n=(m_nm_{n+1})^{-1/2}
1_{\{J_n\cup J_{n+1}\text{ 全部位为0}\}}.
$$

有 $\|x_n\|=1$，而 $E_{J_n}E_{J_{n+1}}x_n$ 的范数为1。
所有物理 raising 乘积均保持函数正锥，故未中心化的纯部分作用于 $x_n$ 后是非负函数，且范数至少为其第 $n$ 项的范数 $n$。这些部分的 $H$ 收敛由 §2 加上 $c_*<\infty$ 保证。因此

$$
\|T_0x_n\|\ge n-c_*\longrightarrow\infty.
$$

实际差有界，故 $X_f$ 也无界。也不存在另一个有界交换子 $B$ 满足 $B1=f$：否则对每个有限柱 $u=X_u1$，有
$Bu=X_uf=X_fu$；有限柱是 $X_f$ 的图核心，会迫 $X_f=B$ 为全域有界算子，矛盾。

在 Walsh 展开中，每个 (9.4) 含 $J_n\cup J_{n+1}$ 的全部非空子集，系数为
$n2^{-k_n-k_{n+1}}(-1)^{|F|}$。重叠单项式的符号相同，不发生取消。因此支撑逐位局部有限，但逐位参与数无统一上界，最大次数 $k_n+k_{n+1}$ 也趋于无穷。

每个相邻胞块之间都存在跨胞块的非零 Walsh 集合，所以支撑连接了整条无限胞块链。它不能放进一族两两不交的有限物理块中，否则一个块必须沿链包含全部胞块。这区别于 R136 的独立有限块范围；同时它不满足 R137 的固定次数及统一参与数假设，也没有 R123 所需的有界实际乘子。

## 10. 已证明范围与剩余缺口

本稿证明了一个实际可检查的局部有限高阶判据：固定占据集合上的内部矩阵可任意大，真空出入具有平方可和强度，非零状态之间的转移具有统一有限强度，实际 carry 差可和。缺陷证明在取对角虚部之前先把缺陷向量放入真正的自伴对角域，未以形式矩阵替代定义域论证。

一般局部有限 Walsh 支撑总能按 §8 相邻化，但不保证 (1.3)。如果这些跨状态块也任意增长，本文的块 Schur 与谐级数 Carleman 控制便不足；没有由这种不足反推真实核非零或不变子空间存在。

依赖：R125 §9 的闭加性 cocycle 定理；R136 的独立块缺陷论证作为出发点；本文 §§2–6 重证了新的相邻重叠情形。真实局部恒等式及 $C$ 对称沿用 R9/R13/R24，有限柱乘子与循环向量沿用 R11。
