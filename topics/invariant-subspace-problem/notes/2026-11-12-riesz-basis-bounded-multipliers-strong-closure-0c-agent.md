# R88 草稿：全次数 Riesz 基、有界乘法的双向判据与完整交换子的强闭包

日期：2026-11-12（UTC）。独占稿：critical_kernel；全次数排序合成的起点由 l2_moments 提出。

**状态：以下定理均已证明。** 本稿证明实际归一化幂产生一个整个 Hilbert 空间上的 Riesz 基，精确刻画哪些向量给出有界轨道乘法，并证明完整交换子代数等于多项式的强、弱算子闭包。证明还给出有界序列的明确逼近方式。它不把任意 L² 向量都当成有界乘法向量，不把线性乘法对应当成代数同构，也不证明所有非零交换子单射。

内部依赖为 [R9](../results/R9-radial-odometer-and-nilpotent-approximants.md)、[R12](../results/R12-normalized-powers-and-compact-commutant.md) 的实际归一化幂与位模型，[R11](../results/R11-cyclic-cylinder-core-for-odometer.md) 的常函数循环性，[R31](../results/R31-generated-uhf-algebra.md) 的具体 UHF 代数，[R32](../results/R32-gauge-action-and-formal-coefficients.md) 的常数特征及单点谱。与 [R84](../results/R84-l2-high-bit-synthesis-finite-chaos.md) 的区别是本稿允许合成系数遍历全部 Walsh 次数，而不是固定一个次数；其代价由实际误差的超快衰减承担。

## 1. 记号与定理

令 H=L²(Z₂,μ)，χ_j=(-1)^{b_j}，χ_J=∏_{j∈J}χ_j。有限集合 J 的 χ_J 构成正交归一基；常函数 1 的范数为一。记

$$
N_j=\frac{A^{2^j}}{d_j},\qquad d_j=\|A^{2^j}\|,\qquad E_j=e_{10}
$$

分别为实际归一化幂和作用于第 j 位的独立 nilpotent。已有精确关系

$$
\|N_j\|=1,\qquad
N_j=E_j+\eta_j E_j^*N_{j+1},\qquad
\|N_j-E_j\|=\eta_j,
\tag{1.1}
$$

$$
\eta_j\le e^{-770\,16^j}.
\tag{1.2}
$$

定义

$$
U_j=I-2N_j,\qquad V_j=I-2E_j.
\tag{1.3}
$$

实际 U_j 彼此交换；独立 V_j 彼此交换。混合的 U_j、V_k 不被假定交换。它们满足

$$
\|U_j\|,\|V_j\|\le3,\quad
\|U_j-V_j\|\le2\eta_j,\quad
V_J1=\chi_J,\quad V_j^2=2V_j-I.
\tag{1.4}
$$

记

$$
\mathcal U=C^*(I,A),\quad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\quad
\mathscr E=\{E_j:j\ge0\}',\quad
\mathscr C=\{A\}'.
\tag{1.5}
$$

所有交换子均指 B(H) 中的有界算子。置

$$
\rho=2\sum_{j\ge0}\eta_j10^{j/2}.
\tag{1.6}
$$

因为 16^j-1≥15j，

$$
\rho\le
\frac{2e^{-770}}{1-\sqrt{10}\,e^{-11550}}
<3e^{-770}<1.
\tag{1.7}
$$

**主定理。**

1. 由 Wχ_J=U_J1 定义的映射延为 H 上可逆的有界算子，并且

   $$
   W,W^{-1}\in\mathcal U,\qquad \|W-I\|\le\rho.
   \tag{1.8}
   $$

2. 对给定 f∈H，存在 P_f∈𝓔、P_f1=f，当且仅当存在 X_f∈𝓒、X_f1=f。两者分别唯一。对应 Φ(P_f)=X_f 是有界线性双射，满足

   $$
   \|X_f\|\le\frac{1+\rho}{1-\rho}\|P_f\|,
   \qquad
   \|P_f\|\le(1+\rho)^2\|X_f\|.
   \tag{1.9}
   $$

3. 若 f_m 是 f 的低 m 位条件期望，则对任意 X_f∈𝓒，有限柱乘子 X_{f_m}∈𝓐 且

   $$
   X_{f_m}\xrightarrow{\rm SOT}X_f,\qquad
   \sup_m\|X_{f_m}\|
   \le \frac{(1+\rho)^3}{1-\rho}\|X_f\|.
   \tag{1.10}
   $$

   特别地

   $$
   \boxed{
   \mathscr C=
   \overline{\mathcal A}^{\rm SOT}
   =\overline{\mathcal A}^{\rm WOT}
   =\overline{\mathbb C[I,A]}^{\rm SOT}
   =\overline{\mathbb C[I,A]}^{\rm WOT}.}
   \tag{1.11}
   $$

4. 有界乘法向量的准确判据为

   $$
   \boxed{
   f\text{ 给出有界 }X_f
   \iff
   \sup_m\left\|
   \sum_{K\subset[0,m)}
   \widehat f(K)V_K
   \right\|<\infty.}
   \tag{1.12}
   $$

   右端范数可以只在低 m 位的有限维空间计算，其上确界恰为 ∥P_f∥。

以下逐项证明，并给出第一 chaos 的充要条件和一个不满足 Walsh 系数 ℓ¹ 条件的二次例子。

## 2. 全次数合成：误差位之前有限，之后正交

对 j≥0、K⊂[0,j)，在低 j+1 位空间中定义秩一算子

$$
Q_{j,K}^{\rm head}
=|1_{[0,j]}\rangle\langle\chi_{K\cup\{j\}}|.
$$

将其张量上尾恒等，记为 Q_{j,K}。它是有限局部矩阵，因而属于 𝓤，且范数为一。对有限 Walsh 多项式 h=∑_J c_Jχ_J，

$$
Q_{j,K}h
=\sum_{L\subset(j,\infty)}
c_{K\cup\{j\}\cup L}\chi_L.
\tag{2.1}
$$

注意右端仍保留全部高位函数，只把低 j+1 位换成常函数。对固定 j，不同 K 的输入正交，所以

$$
\sum_{K\subset[0,j)}\|Q_{j,K}h\|^2\le\|h\|^2.
\tag{2.2}
$$

按位次序展开有限乘积，无需混合因子交换：

$$
U_J-V_J=
\sum_{j\in J}U_{J\cap[0,j)}
(U_j-V_j)V_{J\cap(j,\infty)}.
\tag{2.3}
$$

将 (2.3) 作用于 1，并对 c_J 求和，由 V_L1=χ_L 得

$$
(W-I)h=\sum_{j\ge0}D_jh,
\qquad
D_j=\sum_{K\subset[0,j)}
U_K(U_j-V_j)Q_{j,K}.
\tag{2.4}
$$

这里每个 D_j 的 K 和是有限和。由 Cauchy–Schwarz，

$$
\begin{aligned}
\|D_jh\|
&\le2\eta_j
\sum_{K\subset[0,j)}3^{|K|}\|Q_{j,K}h\|\\
&\le2\eta_j
\left(\sum_{K\subset[0,j)}9^{|K|}\right)^{1/2}\|h\|\\
&=2\eta_j10^{j/2}\|h\|.
\end{aligned}
\tag{2.5}
$$

因此 (2.4) 按算子范数收敛，并给 ∥W-I∥≤ρ<1。Neumann 逆保证 W 可逆。每个 D_j 都属于 𝓤，所以 W∈𝓤，逆闭性给 W⁻¹∈𝓤。也可直接用在 𝓤 内收敛的 Neumann 级数。

特别地，对任意有限标量族 c_J，

$$
(1-\rho)\left(\sum_J|c_J|^2\right)^{1/2}
\le
\left\|\sum_Jc_JU_J1\right\|
\le
(1+\rho)\left(\sum_J|c_J|^2\right)^{1/2}.
\tag{2.6}
$$

其闭线性张成是整个 H。这证明 Riesz 基结论。

另一个后面必需的代数事实是：若 n=∑_{j∈J}2^j，则

$$
U_J=\prod_{j\in J}
\left(I-\frac{2A^{2^j}}{d_j}\right)
$$

是次数恰为 n、最高系数非零的多项式。故按 n=0,1,2,… 排序，这些多项式与普通幂 1,z,z²,… 的有限段之间是可逆三角变换。因此它们的代数线性张成恰为所有多项式，而不只是具有相同的闭包。

## 3. 独立模型的有界乘法及唯一性

给定 f∈H，先在有限 Walsh 多项式上定义

$$
P_f^0\chi_J=V_Jf.
\tag{3.1}
$$

如果它有有界延拓 P_f，则该延拓与每个 V_j、E_j 交换。确切地说，V_j 在 Walsh 基上的作用由

$$
V_j\chi_J=
\begin{cases}
\chi_{J\cup\{j\}},&j\notin J,\\
2\chi_J-\chi_{J\setminus\{j\}},&j\in J
\end{cases}
\tag{3.2}
$$

给出，而 V_j²=2V_j-I 保证在该稠密定义域上 P_f^0V_j=V_jP_f^0。连续延拓便给交换性。

反过来，任意 P∈𝓔 若 P1=f，则

$$
P\chi_J=PV_J1=V_Jf.
$$

故 P 必为上述延拓，并由 Walsh 基的完备性唯一。

实际模型同样有唯一性：若 X∈𝓒 且 X1=f，则

$$
Xp(A)1=p(A)f.
\tag{3.3}
$$

因为 1 对 A 循环，(3.3) 唯一决定有界 X。存在性则需要下两节的范数控制，不能从循环性单独推出。

## 4. 从独立乘法到实际乘法

设 P=P_f∈𝓔。在有限 Walsh 多项式上定义 Y_fχ_J=U_Jf。依 (2.3) 展开，由 V_Lf=Pχ_L 得

$$
(Y_f-P)h
=
\sum_{j\ge0}\sum_{K\subset[0,j)}
U_K(U_j-V_j)P Q_{j,K}h.
\tag{4.1}
$$

固定 j 后与 (2.5) 同样使用 Cauchy–Schwarz，得到

$$
\|Y_f-P\|\le\rho\|P\|.
\tag{4.2}
$$

所以 Y_f 有有界延拓，∥Y_f∥≤(1+ρ)∥P∥。定义

$$
X_f=Y_fW^{-1}.
\tag{4.3}
$$

对每个有限 J 有 X_fU_J1=U_Jf。由 §2 的三角多项式事实，因而对所有多项式 p 有 (3.3)。在稠密的多项式轨道上比较 X_fA 和 AX_f，得 X_f∈𝓒。同时 X_f1=f。

(4.2) 及 ∥W⁻¹∥≤(1-ρ)⁻¹ 给

$$
\|X_f\|\le\frac{1+\rho}{1-\rho}\|P\|.
\tag{4.4}
$$

还可定量比较同一 H 上的两个算子。由

$$
X_f-P=(Y_f-PW)W^{-1}
$$

得到

$$
\boxed{\|X_f-P\|\le\frac{2\rho}{1-\rho}\|P\|.}
\tag{4.5}
$$

若 P∈𝓤，则 (4.1) 的每个项都在 𝓤，按范数收敛后 Y_f∈𝓤，故 X_f∈𝓤。

## 5. 反向乘法：完整交换子不能逃过有限头判据

设 X∈𝓒，f=X1。现在 Y_f=XW 是有界算子，且 Y_fχ_J=U_Jf。

使用另一方向的排序 telescoping：

$$
U_J-V_J=
\sum_{j\in J}V_{J\cap[0,j)}
(U_j-V_j)U_{J\cap(j,\infty)}.
\tag{5.1}
$$

对后段 L⊂(j,∞)，因 X 与 U_L 交换，

$$
U_Lf=XU_L1=XW\chi_L.
\tag{5.2}
$$

因此在有限 Walsh 多项式上

$$
Y_f-P_f^0
=
\sum_{j\ge0}\sum_{K\subset[0,j)}
V_K(U_j-V_j)XWQ_{j,K}.
\tag{5.3}
$$

固定 j 后用 ∥V_K∥≤3^{|K|} 和 (2.2)，得到右端按范数收敛，并且

$$
\|Y_f-P_f^0\|\le\rho\|X\|\|W\|.
\tag{5.4}
$$

故 P_f^0 有有界延拓 P_f∈𝓔，且

$$
\boxed{\|P_f\|\le(1+\rho)^2\|X\|.}
\tag{5.5}
$$

同样，

$$
\|P_f-X\|
\le\|P_f-XW\|+\|X(W-I)\|
\le\rho(2+\rho)\|X\|.
\tag{5.6}
$$

如果 X∈𝓤，(5.3) 的每个项也属于 𝓤，所以 P_f∈𝓤。

由两边唯一性，§4 和本节互逆，给出主定理的有界线性双射 Φ。它保持向量值 Φ(P)1=P1；同时

$$
P\in\mathscr E\cap\mathcal U
\iff
\Phi(P)\in\mathscr C\cap\mathcal U.
\tag{5.7}
$$

该双射不是代数同构，见 §8 的明确例子。

## 6. 有限柱的精确实际乘子

本节给出有限柱乘子的直接公式，避免从抽象有界性错判它们位于 UHF 代数外。

令 e_0^{(m)} 为低 m 位全部为零的示性函数，其尾因子为常函数 1。设 N=2^m，记 e_n^{(m)} 为低 m 位等于 n 的示性函数。在 n<N 时，真实加权平移从输入低位 0 走到 n 不产生越过第 m 位的进位，故精确有

$$
A^ne_0^{(m)}=W_ne_n^{(m)},\qquad W_n=\|A^n\|.
\tag{6.1}
$$

二进位乘积恒等式 W_n=∏_{j:b_j(n)=1}d_j 给

$$
Z_m:=\prod_{j<m}(I+N_j)
=\sum_{n=0}^{N-1}\frac{A^n}{W_n},
\qquad
Z_me_0^{(m)}=1.
\tag{6.2}
$$

每个 N_j 拟幂零，故 I+N_j 及 Z_m 在 𝓐 中可逆。

若 f 是低 m 位柱函数，f(n) 表示它在该剩余类的值，定义

$$
p_f(z)=\sum_{n=0}^{N-1}\frac{f(n)}{W_n}z^n.
\tag{6.3}
$$

由 (6.1) 有 p_f(A)e_0^{(m)}=f，故

$$
\boxed{X_f=p_f(A)Z_m^{-1}\in\mathcal A.}
\tag{6.4}
$$

这也证明有限柱乘子无需 §4 才能存在。若 f≠0，则 p_f 非零；写 p_f(z)=z^r u(z)、u(0)≠0，得到 X_f=A^r 乘以 𝓐 中可逆元。因为 A 单射且值域稠密，X_f 也单射且值域稠密，恢复有限柱循环性。

特别地，令

$$
R_j=(I-N_j)(I+N_j)^{-1}.
\tag{6.5}
$$

对有限 K，把 (6.2) 中相应位的正号换成负号，得到

$$
\boxed{X_{\chi_K}=R_K:=\prod_{j\in K}R_j,\qquad R_K1=\chi_K.}
\tag{6.6}
$$

也有

$$
X_{b_j}=N_j(I+N_j)^{-1},
\qquad b_j=(1-\chi_j)/2.
\tag{6.7}
$$

这些全是 𝓐 中的实际有理函数。

## 7. 有限头压缩、有界强逼近和 UHF 部分

先在独立侧工作。把 H=H_{<m}⊗H_{≥m}，令 J_m:H_{<m}→H 为 h↦h⊗1 的等距嵌入。对 P∈𝓔 定义

$$
\widehat P_m=J_m^*PJ_m,\qquad P_m=\widehat P_m\otimes I_{≥m}.
\tag{7.1}
$$

这是有限矩阵张量尾恒等，因而 P_m∈𝓤，且

$$
\|P_m\|\le\|P\|.
\tag{7.2}
$$

它与低位 E_j 交换，高位交换性来自尾恒等，故 P_m∈𝓔。若 f=P1，则

$$
P_m1=f_m:=\mathbb E[f\mid b_0,\ldots,b_{m-1}].
\tag{7.3}
$$

低位的常向量在有限纯代数下循环，有限 Walsh 基给出唯一性，因此

$$
P_m=\sum_{K\subset[0,m)}\widehat f(K)V_K.
\tag{7.4}
$$

对固定有限 J，当 m>max J 时，

$$
P_m\chi_J=V_J f_m\longrightarrow V_Jf=P\chi_J.
\tag{7.5}
$$

(7.2) 及 Walsh 基稠密性给 P_m→P 强收敛。因而

$$
\|P\|=\sup_m\|P_m\|.
\tag{7.6}
$$

这里没有把整个 H 上投到有限柱的有限秩正交投影当作 UHF 元素；真正使用的 UHF 元素是 (7.1) 的有限矩阵提升。

现在设 X∈𝓒，取其对应 P，记 X_m=Φ(P_m)。由 (6.4)，X_m=X_{f_m}∈𝓐。由 (4.4)、(5.5)，

$$
\sup_m\|X_m\|
\le\frac{1+\rho}{1-\rho}\|P\|
\le\frac{(1+\rho)^3}{1-\rho}\|X\|.
\tag{7.7}
$$

在多项式轨道上，

$$
X_m p(A)1=p(A)f_m\longrightarrow p(A)f=Xp(A)1.
\tag{7.8}
$$

这一次输入稠密性有统一算子范数 (7.7) 配合，故可合法延拓到全 H，得到 X_m→X 强收敛。

𝓒 是弱算子闭的，并包含 𝓐。因此 (7.8) 证明 (1.11) 前两个闭包等式。再对每个 X_m 选一个 A 的多项式，令范数误差小于 1/m，得到仍一致有界的多项式序列强趋 X；从而其余等式也成立。

还有范数级对应。若 P∈𝓔∩𝓤，则 (7.1) 的压缩提升对局部矩阵最终恒等，并在 𝓤 上为压缩映射，所以由局部矩阵的范数稠密性有 P_m→P 于范数。Φ 有界，故 X_m→X 于范数，得到 X∈𝓐。反向由 X∈𝓐⊂𝓤 和 (5.3) 得 P∈𝓤。因此

$$
\boxed{\Phi(\mathscr E\cap\mathcal U)=\mathcal A.}
\tag{7.9}
$$

这也重新得到 𝓒∩𝓤=𝓐，与 R38 一致，但完整交换子的 SOT/WOT 等式是新增结论。

最后，所有 X∈𝓒 都由 A 的多项式强逼近，故它与每个 Y∈𝓒 交换。因此 𝓒 是交换代数，且

$$
\{A\}''=\{A\}'.
\tag{7.10}
$$

这是非自伴算子代数的陈述；不把它称作由 A 生成的 von Neumann 代数。

## 8. 对应不是代数同构；有界性不是任意向量的自动性质

取 P=E_0∈𝓔，f=E_01=b_0。由 (6.7)，

$$
\Phi(E_0)=N_0(I+N_0)^{-1}.
\tag{8.1}
$$

E_0²=0，但右端是单射算子，其平方也单射且非零。因此

$$
\Phi(E_0^2)\ne\Phi(E_0)^2.
\tag{8.2}
$$

也就是说，一个在算子范数上极小的线性变形可以改变零因子结构；(4.5) 不能用于转移核或谱。

对任意 f∈H，若 (1.12) 右端有限，则 (7.4) 中的 P_m 一致有界，且对固定 χ_J 有 P_mχ_J→V_Jf；稠密性给有界延拓 P_f。反向已经由 (7.1)–(7.6) 证明。因此 (1.12) 是充要条件，而不是仅一个充分条件。

它也给实际乘子的双边范数比较：

$$
\frac{1}{(1+\rho)^2}\sup_m\|P_m\|
\le\|X_f\|
\le\frac{1+\rho}{1-\rho}\sup_m\|P_m\|.
\tag{8.3}
$$

下一节展示即使次数仅为一，也确有 L² 向量不满足该判据。

## 9. 第一 chaos：有界乘法当且仅当系数绝对可和

设

$$
f=a_*+\sum_{j\ge0}a_j\chi_j,\qquad (a_j)\in\ell^2.
\tag{9.1}
$$

其有限头纯乘子为

$$
P_m=
\left(a_*+\sum_{j<m}a_j\right)I
-2\sum_{j<m}a_jE_j.
\tag{9.2}
$$

每个二阶 nilpotent E_j 的数值域恰为半径 1/2 的闭圆盘：若单位向量为 (α,β)，则其数值为 α\overline β，模可取 [0,1/2]，辐角任意。对不同位选择独立单位向量，再取张量积，(9.2) 的数值域包含以 a_*+∑_{j<m}a_j 为中心、半径 ∑_{j<m}|a_j| 的整个圆盘。因此

$$
\|P_m\|\ge\sum_{j<m}|a_j|.
\tag{9.3}
$$

若存在有界实际乘子，(8.3) 强制这些和一致有界，即 (a_j)∈ℓ¹。

反之，若 (a_j)∈ℓ¹，则 a_*I+∑a_jV_j 按范数收敛，给 P_f∈𝓔∩𝓤。因此 X_f∈𝓐。由 (6.6) 及线性连续性，

$$
\begin{aligned}
X_f
&=a_*I+\sum_ja_jR_j\\
&=\left(a_*+\sum_ja_j\right)I
-2\sum_ja_jN_j(I+N_j)^{-1}.
\end{aligned}
\tag{9.4}
$$

两级数都按算子范数收敛。故

$$
\boxed{
f\in H_{\le1}\text{ 给出有界实际乘法}
\iff (a_j)\in\ell^1.}
\tag{9.5}
$$

ℓ¹ 情形下 f 有连续代表，且

$$
f(0)=a_*+\sum_ja_j.
\tag{9.6}
$$

R32 的常数特征作用于 (9.4) 恰给这个值。因此

$$
f(0)\ne0
\Longrightarrow X_f\text{ 在 }\mathcal A\text{ 中可逆}
\Longrightarrow f\text{ 对 }A\text{ 循环}.
\tag{9.7}
$$

最后一步因为 X_f 与 A 交换，且 X_f 将稠密轨道 span{Aⁿ1} 送到 span{Aⁿf}，可逆性保证后者也稠密。

若 f(0)=0，(9.4) 只给一个 𝓐 中的拟幂零算子；本稿不证明任意此类算子单射。特别地，系数非增重排超快并不等于系数按原来的位索引具有规则衰减。

一个更一般的充分类是

$$
\sum_{K\text{ finite}}3^{|K|}|\widehat f(K)|<\infty.
\tag{9.8}
$$

此时纯级数 ∑_K f̂(K)V_K 按范数收敛于 𝓔∩𝓤，实际级数

$$
X_f=\sum_K\widehat f(K)R_K\in\mathcal A
\tag{9.9}
$$

也按范数收敛。可直接用 ∥Φ(V_K)∥≤(1+ρ)(1-ρ)⁻¹3^{|K|} 保证后一收敛。连续向量的值 f(0)=∑_K f̂(K) 是 X_f 的常数特征；非零时同样可逆、循环。

## 10. 全矩消失的实际核解释

使用 R24 的对称双线性形式

$$
B(f,g)=\langle f,Cg\rangle,\qquad
(Cg)(y)=\overline{g(-1-y)}.
$$

A 为 C 对称。实际上每个 X∈𝓒 也为 C 对称。证明只需在稠密多项式轨道上检验：

$$
\begin{aligned}
B(Xp(A)1,q(A)1)
&=B(X1,p(A)q(A)1)\\
&=B(p(A)q(A)1,X1)\\
&=B(p(A)1,Xq(A)1).
\end{aligned}
\tag{10.1}
$$

第一、三步使用 A 的对称性和 X 的交换性；中间一步使用 B 对称。由有界性推广到所有向量。

因此若 f=X_f1 为有界乘法向量，则

$$
B(A^nf,g)=B(A^n1,X_fg).
\tag{10.2}
$$

由于 1 对 A 循环，右端对所有 n 为零当且仅当 X_fg=0。也就是说

$$
\boxed{
B(A^nf,g)=0\ (\forall n\ge0)
\iff X_fg=0.}
\tag{10.3}
$$

这将第一 chaos 的 ℓ¹ 剩余情形准确化为 (9.4) 的实际核问题；它没有以形式除法代替实际算子，也没有自动排除常数特征为零的核。

## 11. 超出 Walsh ℓ¹ 的明确二次有界乘法与循环向量

本节构造一个次数恰为二、Walsh 系数不绝对可和的连续 f，使 X_f∈𝓐。加上常数 1 后得到循环向量。这表明 (9.8) 在高于一次时不是必要条件。

### 11.1 有限 Hadamard 块

取 n=2^r，令 H_n 为 Sylvester Hadamard 矩阵，首行首列均为 1，且

$$
H_nH_n^*=nI.
$$

令 𝟙 为 n 维常向量，定义

$$
P_n=I-\frac1n\mathbf1\mathbf1^*,
\qquad
A_n=P_nH_nP_n.
\tag{11.1}
$$

于是 A_n 每行、每列的和均为零，并且

$$
\|A_n\|\le\sqrt n,\qquad
\|A_n\|_{\rm F}\le n.
\tag{11.2}
$$

以下行列索引从 0 开始。因为 H_n𝟙=n e_0，

$$
A_n=H_n-\mathbf1e_0^*-e_0\mathbf1^*
+\frac1n\mathbf1\mathbf1^*.
\tag{11.3}
$$

因此对 i,j≥1，(A_n)_{ij}=(H_n)_{ij}+1/n，从而

$$
\sum_{i,j}|(A_n)_{ij}|
\ge(n-1)^2(1-1/n).
\tag{11.4}
$$

取两组互不相交的 n 个位，分别记其 Walsh 字符 χ_i、χ'_j。对标量 α 定义有限二次柱

$$
f_{n,\alpha}
=\alpha\sum_{i,j}(A_n)_{ij}\chi_i\chi'_j.
\tag{11.5}
$$

由于行列和均零，展开 V_iV'_j 后的常数及一次项全部精确消失，故其纯乘子为

$$
P_{f_{n,\alpha}}
=4\alpha\sum_{i,j}(A_n)_{ij}E_iE'_j.
\tag{11.6}
$$

置 G_i=∑_j(A_n)_{ij}E'_j。行列算子 Cauchy–Schwarz 给

$$
\left\|\sum_iE_iG_i\right\|
\le
\left\|\sum_iE_iE_i^*\right\|^{1/2}
\left\|\sum_iG_i^*G_i\right\|^{1/2}.
\tag{11.7}
$$

第一因子至多 √n。又由 A_n* A_n≤nI，

$$
\sum_iG_i^*G_i
\le n\sum_j(E'_j)^*E'_j
\le n^2I.
\tag{11.8}
$$

所以

$$
\boxed{\|P_{f_{n,\alpha}}\|\le4|\alpha|n^{3/2}.}
\tag{11.9}
$$

同时，

$$
\|f_{n,\alpha}\|_\infty
\le|\alpha|n^{3/2},\qquad
\|f_{n,\alpha}\|_2
=|\alpha|\|A_n\|_{\rm F}
\le|\alpha|n.
\tag{11.10}
$$

第一式来自两个符号向量的欧氏范数均为 √n 及 (11.2)，第二式来自不同 χ_iχ'_j 正交。

### 11.2 无穷个互不相交的块

对 m≥1 取

$$
n_m=2^{4m},\qquad
\alpha_m=2^{-m}n_m^{-3/2},
\tag{11.11}
$$

并让所有块使用彼此不交的位。令 f_m=f_{n_m,\alpha_m}，定义

$$
f=\sum_{m\ge1}f_m.
\tag{11.12}
$$

由 (11.10)，∑∥f_m∥∞≤∑2⁻ᵐ<∞，故 f 是连续函数，且纯 Walsh 次数为二。各块之间正交，特别地也在 L² 中收敛。跨全部第一组、第二组位的二次系数矩阵包含无穷个不交的非零对角块，因此具有无限秩。

另一方面，由 (11.4)，

$$
\sum_K|\widehat f(K)|
\ge\sum_{m\ge1}
\alpha_m(n_m-1)^2(1-1/n_m)
=+\infty,
\tag{11.13}
$$

因为其第 m 项与 2⁻ᵐ√n_m=2ᵐ 同阶。所有系数支撑大小都是二，所以 (9.8) 也发散。

但是由 (11.9)，

$$
\sum_m\|P_{f_m}\|\le4\sum_m2^{-m}<\infty.
\tag{11.14}
$$

每项是纯有限局部矩阵；故 P_f=∑P_{f_m}∈𝓔∩𝓤，并由 (7.9)

$$
X_f=\sum_m X_{f_m}\in\mathcal A
\tag{11.15}
$$

按范数收敛。每块 f_m(0)=0，因为 A_n 的所有元素和为零；其有限柱乘子常数特征也为零。因此 X_f 的常数特征为零。

于是 X_{1+f}=I+X_f 的常数特征等于一。由 R32，它在 𝓐 中可逆，故

$$
\boxed{
1+f\text{ 对实际 }A\text{ 循环，}
\quad 1+f\in H_{\le2}\cap C(\mathbb Z_2),
\quad
\sum_K|\widehat f(K)|=\infty.}
\tag{11.16}
$$

这是一个直接构造的无限秩二次类实例；其证明只使用上面的有限块算子估计，不需要任何一般多项式延拓定理。

## 12. 对当前未解问题的准确意义

本稿已经闭合此前 R38 明确保留的强闭包问题：完整有界交换子恰为 A 多项式的 SOT/WOT 闭包，而且每个交换子都由其向量 X1 的有限头条件期望产生的有界乘子序列逼近。

本稿同时将“给定 f 的轨道乘法是否有界”转为精确有限矩阵判据 (1.12)。第一 chaos 的答案完全是 ℓ¹ 条件；二次情形已有超出系数 ℓ¹ 的明确类。一般有限次数的完整向量空间刻画可另作进一步研究。

但是 Φ 只线性双向有界，不保持乘法或零因子。独立模型中的大量 nilpotent 与核不能通过 Φ 自动转成实际模型的核。反方向也不能仅由 ∥Φ(P)-P∥ 很小推出实际 X_f 单射。

特别地，尚未从 (1.12) 证明所有非零有界乘子都单射；也没有证明任意 L² 向量都属于有界乘法类。没有构造非零真闭普通不变子空间，也没有证明所有非零向量循环。本稿是完整交换子结构及具体向量类的新结论，不是完整 Hilbert 不变子空间问题的解答。

