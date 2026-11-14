# R136：独立有限块的无次数上界循环性

日期：2026-11-12（UTC）。独占稿：critical_kernel。
状态：**以下定理与例子已证明。** 块 Jacobi/Carleman 方向由根代理提出，本稿独立核验并写全缺陷向量定义域、真实进位扰动及 gauge 闭包。允许块内部算子范数任意大，不要求总向量或其实际乘子有界。

## 1. 假设与结论

令 J_n⊂N₀ 为两两不交的非空有限物理位集合。对每个 n，令 f_n 是只依赖 J_n 的有限柱函数，并满足

$$
\int f_n\,d\mu=0,\qquad
\sigma^2:=\sum_{n\ge1}\|f_n\|_2^2<\infty.
\tag{1.1}
$$

各 f_n 两两正交，因此对任意 a_*∈C，

$$
f=a_*+\sum_{n\ge1}f_n
\tag{1.2}
$$

在 L² 中收敛，且 ∥f∥₂²=|a_*|²+σ²。

记

$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
S_j=I-2E_j,
$$

分别为实际和纯的一位乘子。对块 Walsh 展开

$$
f_n=\sum_{\varnothing\ne F\subseteq J_n}a_{n,F}\chi_F
$$

定义有限块乘子

$$
P_n=\sum_{\varnothing\ne F\subseteq J_n}a_{n,F}V_F,\qquad
P_n^0=\sum_{\varnothing\ne F\subseteq J_n}a_{n,F}S_F.
\tag{1.3}
$$

P_n 是真实𝓐中的有限解析乘子；P_n^0只作用于块 J_n。
二者作用于常函数都恰为 f_n。

额外假设真实差可和：

$$
\boxed{\sum_n\|P_n-P_n^0\|<\infty.}
\tag{1.4}
$$

**主定理。** 在 (1.1)、(1.4) 下，每个非零 f 都对 A 循环。存在一个以有限物理柱为图核心的闭乘子 X_f，满足

$$
X_f^*=CX_fC,\qquad X_f1=f,\qquad
\overline{\operatorname{Ran}X_f}=\operatorname{cyc}_A(f).
\tag{1.5}
$$

每个有界 T∈{A}' 都保持 DomX_f 并在域上交换。若 f 非常数，则对每个 λ∈C，

$$
\boxed{\ker(X_f-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(X_f-\lambda I)}=H.}
\tag{1.6}
$$

不要求 |J_n| 或 f_n 的 Walsh 次数有统一上界。也不要求
∑∥P_n^0∥、sup_n∥P_n^0∥或∑∥f_n∥₂有限。

一个可直接检查的充分条件是

$$
\boxed{
\sum_n\sum_{\varnothing\ne F\subseteq J_n}
|a_{n,F}|\,8^{|F|}
\sum_{j\in F}\eta_j<\infty.
}
\tag{1.7}
$$

§7证明 (1.7) 蕴含 (1.4)，且可将任意给定的有限块模板递归远移以实现它。

## 2. 按非参考块个数分级

给未被任何 J_n 使用的位补上零符号的单点块。这样可以不失一般性地将全部物理位分成可数个有限块。零块不改变任何算子、系数条件或结论。

在第 n 块 Hilbert 空间 H_n 中，令 Ω_n=1 为归一化参考向量，并写

$$
H_n=\mathbb C\Omega_n\oplus K_n,\qquad K_n=\Omega_n^\perp.
$$

全 Haar 空间按有限非参考块集合分解：

$$
H=\bigoplus_{S\subset\mathbb N,\ S\text{ finite}}H_S,
\qquad
H_S=\bigotimes_{n\in S}K_n,
\tag{2.1}
$$

未出现在 S 的块均放参考向量 Ω。每个 H_S 有限维。
再按非参考块数分级：

$$
\mathcal H_q=\bigoplus_{|S|=q}H_S,\qquad
H=\bigoplus_{q\ge0}\mathcal H_q.
\tag{2.2}
$$

令 𝓟 为所有有限物理柱函数。等价地，它是 (2.1) 中有限个 H_S 的代数直和。任何有限物理位集合只碰有限个有限块，反过来有限块的并也是有限物理位集合，所以这两个定义确实相同。

各纯 P_n^0 对块反线性共轭

$$
(C_nu)(b)=\overline{u(1-b)}
$$

对称。因为 Ω_n 被 C_n 固定、f_n 均值为零，

$$
P_n^0\Omega_n=f_n\in K_n,\qquad
(P_n^0)^*\Omega_n=C_nf_n\in K_n.
\tag{2.3}
$$

所以相对于 Ω_n⊕K_n，

$$
P_n^0=
\begin{pmatrix}
0&\langle\,\cdot\,,g_n\rangle\\
f_n&D_n
\end{pmatrix},
\qquad
g_n=C_nf_n,\qquad
\|g_n\|=\|f_n\|.
\tag{2.4}
$$

内积按第一变量线性理解；上右角表示对应的有界线性泛函。
D_n 是 K_n 上的任意有限矩阵，其范数不需要统一控制。

## 3. 纯初始算子与 Dirac 的三对角结构

在𝓟上定义

$$
T_0x=a_*x+\sum_nP_n^0x.
\tag{3.1}
$$

此和对每个 x∈𝓟都在 H 中收敛：若 x 只依赖有限块集 B，
则 n∈B 的项有限；对 n∉B，P_n^0x=x⊗f_n，
这些向量两两正交，平方范数之和是
∥x∥²∑_{n∉B}∥f_n∥²。相同论证用 g_n 给通常形式伴随

$$
T_0^\dagger=\overline{a_*}I+\sum_n(P_n^0)^*
=CT_0C
\quad\text{于 }\mathcal P.
\tag{3.2}
$$

因此二者可闭，并且

$$
\mathscr T_0=
\begin{pmatrix}0&T_0^\dagger\\T_0&0\end{pmatrix}
\quad\text{于 }\mathcal P\oplus\mathcal P
\tag{3.3}
$$

稠密定义且对称。

把自旋两分量加入 (2.2)，记
𝓚_q=𝓗_q⊕𝓗_q。Dirac 只连接 q−1、q、q+1 三个等级。

### 3.1 对角部分是真正的自伴直和

对固定有限 S，令

$$
D_S=a_*I+\sum_{n\in S}D_n^{(n)}.
$$

等级 q 上的对角块为

$$
\mathscr A_q
=\bigoplus_{|S|=q}
\begin{pmatrix}0&D_S^*\\D_S&0\end{pmatrix}
\tag{3.4}
$$

及其自然平方可和图定义域。每个小块是有限维自伴矩阵，
所以𝓐_q是自伴直和；有限 S 支撑的向量是其图核心。

这里允许不同 S 上的矩阵范数无界。后面的证明先将缺陷向量放入这个自然定义域，才取对角项的实部或虚部。

### 3.2 相邻等级的统一界

令 C_q(f):𝓗_q→𝓗_{q+1} 为创建一个新块并放入 f_n 的算子。
对输出集合 T，|T|=q+1，

$$
(C_q(f)x)_T=\sum_{n\in T}f_n\otimes x_{T\setminus\{n\}},
$$

按固定张量次序识别各项。Cauchy–Schwarz 给

$$
\begin{aligned}
\|C_q(f)x\|^2
&\le(q+1)\sum_{|T|=q+1}\sum_{n\in T}
\|f_n\|^2\|x_{T\setminus\{n\}}\|^2\\
&\le(q+1)\sigma^2\|x\|^2.
\end{aligned}
$$

g_n 的创建算子同样有此界。因 Dirac 的两个创建通道落在不同自旋分量，连接 q 到 q+1 的块 𝓑_q 满足

$$
\boxed{\|\mathscr B_q\|\le\sigma\sqrt{q+1}.}
\tag{3.5}
$$

删除通道恰为相邻创建通道的通常伴随。这些界只涉及
vacuum 与 excited 两个方向的范数 ∥f_n∥，与 D_n 的大小无关。

## 4. 自含块 Carleman 缺陷论证

**引理4.1。** (3.3) 本质自伴。

若 σ=0，全部 f_n=0，算子只是标量的 Dirac 块，结论直接成立。
以下设 σ>0。

取 ξ∈ker(𝓣₀*−iI)，写 ξ=(ξ_q)_{q≥0}，ξ_q∈𝓚_q。
先证明

$$
\xi_q\in\operatorname{Dom}\mathscr A_q.
\tag{4.1}
$$

对等级 q 内、有限 S 支撑的测试向量 x，伴随恒等式中相邻两项
由 (3.5) 是对 x 有界的线性泛函。因此
〈𝓐_qx,ξ_q〉也由某个 H 向量表示。
测试域是𝓐_q的图核心，所以 ξ_q∈Dom𝓐_q*=Dom𝓐_q。
并且得到真实等级方程

$$
i\xi_q
=\mathscr A_q\xi_q+
\mathscr B_{q-1}\xi_{q-1}
+\mathscr B_q^*\xi_{q+1},
\qquad \mathscr B_{-1}=0.
\tag{4.2}
$$

现在将 (4.2) 与 ξ_q 配对，q=0,…,Q 求和并取虚部。
对角项由 (4.1) 及自伴性为实数；内部相邻项成共轭对，虚部相消。
只剩边界：

$$
\sum_{q=0}^Q\|\xi_q\|^2
\le
\|\mathscr B_Q\|\,\|\xi_Q\|\,\|\xi_{Q+1}\|
\le
\sigma\sqrt{Q+1}\,\|\xi_Q\|\,\|\xi_{Q+1}\|.
\tag{4.3}
$$

如果 ξ≠0，选择 Q₀、c>0，使所有 Q≥Q₀ 的左边至少为 c。于是

$$
\|\xi_Q\|^2+\|\xi_{Q+1}\|^2
\ge\frac{2c}{\sigma\sqrt{Q+1}}.
\tag{4.4}
$$

对 Q 求和，左边至多2∥ξ∥²，右边却因
∑(Q+1)^{-1/2}=∞ 而发散，矛盾。故 ξ=0。
对 ker(𝓣₀*+iI) 取相反虚部，完全相同。

两缺陷核均零。闭对称算子 closure𝓣₀±iI 的像由图范数恒等式闭；
其正交补为上述缺陷核，故两像也稠密，因而满射。这证明本质自伴，
没有调用未验证的无限维 Jacobi 定理。

由 Dirac 图范数的分量分解，若 X₀=closure T₀，则

$$
\boxed{X_0^*=\overline{T_0^\dagger}=CX_0C.}
\tag{4.5}
$$

𝓟按定义为 X₀ 及 X₀* 的图核心。本证明不要求 T₀𝓟⊂𝓟；
事实上一次创建一般已经产生无限多个块的 ℓ² 和。

## 5. 实际有界进位差与域交换

由 (1.4)，有算子范数收敛

$$
K=\sum_n(P_n-P_n^0).
\tag{5.1}
$$

各项 C 对称，所以 K*=CKC。定义

$$
X_f=X_0+K,\qquad \operatorname{Dom}X_f=\operatorname{Dom}X_0.
\tag{5.2}
$$

有界扰动给闭性、𝓟图核心及

$$
X_f^*=X_0^*+K^*=CX_fC.
\tag{5.3}
$$

有限实际部分

$$
T_N=a_*I+\sum_{n\le N}P_n\in\mathcal A
$$

在每个 x∈𝓟上趋于 X_fx。特别 T_N1→f，所以 X_f1=f。

取任意有界 T∈{A}'。对 x,z∈𝓟，每个 T_N B 对称并与 T 交换，故

$$
B(Tx,T_Nz)=B(TT_Nx,z).
$$

取极限，再按图范数将 z 延到 DomX_f。由 (5.3) 的双线性伴随定义，
Tx∈DomX_f 且 X_fTx=TX_fx。最后用𝓟图逼近和 X_f 闭性，将 x 推广到全部域：

$$
\boxed{
T\operatorname{Dom}X_f\subseteq\operatorname{Dom}X_f,
\qquad X_fT=TX_f\text{ 于该域}.
}
\tag{5.4}
$$

有限柱 u 的实际乘子 X_u∈𝓐 满足 X_u1=u。有限部分交换给

$$
X_fu=\lim_NT_Nu=\lim_NX_uT_N1=X_uf\in\operatorname{cyc}_A(f).
$$

𝓟为图核心，故 closure RanX_f⊂cyc_A(f)。
反向由 1∈DomX_f 和 (5.4) 对 A 使用，得到
A^nf=X_fA^n1。所以

$$
\boxed{\overline{\operatorname{Ran}X_f}=\operatorname{cyc}_A(f).}
\tag{5.5}
$$

## 6. 有限块 gauge 差完成实际排核

固定 ζ^{2^m}=1。若 J_n∩[0,m)=∅，对应 P_n 中的全部 V_j 都被
γ_ζ固定，所以 P_n也被固定。由于各块不交，至多 m 个非零块与前 m 位相交。因此有限实际部分取足够大 N 后，其差稳定为

$$
\gamma_\zeta(T_N)-T_N=F_\zeta(A),
\tag{6.1}
$$

其中 F_ζ 是有限个有限柱乘子之差形成的真正有理解析芽。

U_ζ双向保持有限物理柱𝓟。先在𝓟上取极限，再分别取闭包，
由于右侧是 X_f 的有界扰动，得到

$$
\boxed{
\gamma_\zeta(X_f)=X_f+F_\zeta(A),\qquad
U_\zeta\operatorname{Dom}X_f=\operatorname{Dom}X_f.
}
\tag{6.2}
$$

R125 的闭加性 cocycle 定理适用：本稿已经逐项给出 C 自伴性、
有限柱图核心、全部有界交换子的域交换及 (6.2)。

为明确排核逻辑，若 X_f 非标量，则其 dyadic 稳定子是一个真子群。
全固定时，有限柱上 X_fu=(X_f1)u，图核心使 X_f包含于最大点乘；
A1在域以及域交换又给 w(y)f(y)=w(y)f(y−1)，遍历性迫 f常数，
于是闭算子本身为全域标量，矛盾。因此稳定子为某个有限 μ_h。

对 ζ∉μ_h，F_ζ 是非零解析芽，可写成 A^r乘𝓐单位。每个闭
A 不变空间 M 的 A^r值域稠密。对于
M=ker(X_f−λI)，(6.2)保证跨核配对两端同域，所以

$$
B(F_\zeta(A)M,U_\zeta M)=0
\quad\Longrightarrow\quad
B(M,U_\zeta M)=0.
$$

相应 L¹乘积只剩 μ_h 中的有限 Fourier 模式。总支撑全测与逐柱秩一论证给 dimM≤h，而 A 单射拟幂零，故 M=0。
C 自伴性给值域稠密，(5.5)给 f循环。

若 X_f为标量，则 f=X_f1为常数，非零情形直接由1循环处理。
因为 f_n均值为零且两两正交，f非常数等价于至少一个 f_n非零。
这证明主定理及 (1.6)。

## 7. 可检查 carry 条件与任意模板的递归远移

已有真实一位界

$$
\|V_j\|\le6,\quad\|S_j\|\le3,\quad\|V_j-S_j\|\le8\eta_j.
$$

对有限 F，按任意固定顺序作乘积望远镜展开，不需要混合因子交换：

$$
\|V_F-S_F\|
\le8\,6^{|F|-1}\sum_{j\in F}\eta_j
\le8^{|F|}\sum_{j\in F}\eta_j.
\tag{7.1}
$$

因此 (1.7) 确实蕴含 (1.4)。

给定任意一列抽象有限块模板 f_n，保持它们的有限 Walsh 系数、
维数和 L²范数不变。令

$$
H_n=\sum_{\varnothing\ne F}|a_{n,F}|\,8^{|F|}|F|<\infty.
$$

递归选择起点 m_n，使各新块排在先前块之后，并使

$$
H_n\eta_{m_n}\le2^{-n}.
\tag{7.2}
$$

η_j→0 保证可行。将模板变量放到长度为相应块维数的连续位段上；
于是 ∑_{j∈F}η_j≤|F|η_{m_n}，所以总 carry 界≤∑2^{-n}<∞。

远移不改变各块的概率分布、独立性、Walsh 次数或纯局部算子范数。
本定理因而允许任意大的有限块内部复杂度，只要求零均值块的 L²能量可和，再将位置选得足够远。

不能把这条可构造性误写成任意原位局部有限符号自动满足 (1.4)；
(1.7)仍是需逐例核验的真实条件。

## 8. 全局次数无界且实际乘子无界的连续例子

取抽象块大小 d_n=3n，并令

$$
f_n=2^{-n}\chi_{J_n}.
\tag{8.1}
$$

按 §7 递归放置块。此时 ∑∥f_n∥₂²<∞，且 ∑∥f_n∥∞<∞，
所以 f=∑f_n 是连续有界函数。它在次数 d_n→∞ 上都有非零 Walsh 系数，
不属于任何有限次数层。

纯局部矩阵 S_j=I−2E_j 的范数为 1+√2，故

$$
\|P_n^0\|
=2^{-n}(1+\sqrt2)^{3n}\longrightarrow\infty.
\tag{8.2}
$$

这迫纯模型乘子 X₀无界。确切地，在块 n 上取任意单位向量 u_n，
其余块均取参考常数，所得全向量记为 u。P_n^0u 与所有 P_m^0u（m≠n）正交，
因为后者在第m块放入零均值 f_m；因此

$$
\|T_0u\|\ge\|P_n^0u\|
$$

（这里取 a_*=0）。优化该块 u，即得 ∥T₀∥≥∥P_n^0∥。
实际 X_f=X₀+K只差有界算子，仍无界。

但主定理证明 f循环，且每个 X_f−λI都单射稠密。
这说明本定理确实超出“有界交换乘子＋局部有限支撑”的范围，
即使函数 f本身仍有连续代表。

## 9. 向量与实际乘子都无界的块尖峰例子

取抽象块大小 d_n=4n，p_n=2^{-d_n}，E_n为该块全部物理位为0的事件。
置 c_n=2^{-n}，并定义

$$
f_n=
\frac{c_n}{\sqrt{1-p_n}}
\left(p_n^{-1/2}1_{E_n}-p_n^{1/2}\right).
\tag{9.1}
$$

它均值为零、L²范数恰为 c_n，最高 Walsh 次数 d_n的系数非零。
按 §7 递归远移，使 (1.7) 成立。

f=∑f_n 属于 L²且有无界全局次数。它没有本质有界代表：
对第n块条件期望，其他独立零均值项消失，得到
E[f | J_n]=f_n，而

$$
\|f_n\|_\infty
=c_n\sqrt{\frac{1-p_n}{p_n}}
\longrightarrow\infty.
$$

若 f∈L∞，条件期望 L∞范数应被∥f∥∞一致控制，矛盾。

此例的实际乘子也无界。纯物理事件乘子为

$$
P_{1_{E_n}}^0=\prod_{j\in J_n}(I-E_j).
$$

令 φ=(1+√5)/2，单个位 I−E_j的范数恰为φ。因此

$$
\|P_n^0\|
\ge
\frac{c_np_n^{-1/2}}{\sqrt{1-p_n}}
\left(\phi^{d_n}-p_n\right)
\longrightarrow\infty.
\tag{9.2}
$$

和 §8 相同的单块测试使 X₀无界，实际有界进位差不能改变这一点。
主定理仍给 f循环及其闭乘子全部参数的单射稠密值域。

## 10. 适用范围

本稿允许任意有限块内部系数、无界块算子范数、无全局 Walsh 次数界，
以及无界 L²向量。它依赖三项精确结构：

- 块物理支撑互不相交；
- 零均值块 L²能量平方可和；
- 实际与纯块乘子的算子范数差可和。

块 Jacobi 的缺陷证明只控制跨 vacuum 的通道，内部大矩阵留在自伴对角直和中。
没有把内部大范数丢弃，也没有假设纯模型的核能连续迁移到实际模型。

任意重叠的无界次数超图、任意未控制的原位 carry 和、以及一般 L²输入仍未解决。
本稿不是完整 Hilbert ISP 的结论。
