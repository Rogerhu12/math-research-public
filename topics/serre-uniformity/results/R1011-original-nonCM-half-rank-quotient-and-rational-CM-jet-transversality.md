# R1011：原曲线的非 CM 半秩实际商与有理 CM jet 的解析横截性

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 在 R1010 的范围内，从同一个原 CM 点差构造原曲线上的实际有理商，其 Mordell–Weil 秩恰为维数的一半。证明保留三次环类角色、全部同源重数与内扭曲，并给出原有理 CM 点处的真实线性 Chabauty 函数。

本篇不声称该函数的首项是 p 进单位，也不给原候选所在圆盘的统一零数。这里获得的是实际商、准确秩及非零首项；积分格、首项赋值和完整余项仍须继续证明。

## 1. 对象与结论

沿用 [R1010](R1010-original-CM-divisor-nontorsion-in-nonCM-part.md)：
\[
X_d=\operatorname{Norm}(X_{\rm ns}^+(p)\times_j\mathbf P^1_b),
\qquad j=6912db^3(1-db^3),
\]
\[
K=\mathbf Q(\zeta_3),\quad \alpha=\sqrt[3]4>0,\quad
F_{\rm cub}=\mathbf Q(\alpha),\quad L=K(\alpha),
\qquad \operatorname{Gal}(L/\mathbf Q)\simeq S_3.
\]
写
\[
\iota:X_1\longrightarrow X_4,\quad u=b/\alpha,\qquad
\delta:b\longmapsto\zeta_3b,\qquad N=1+\delta+\delta^2.
\]
这里 \(N\) 是有理自同态；\(\iota\) 定义在 \(F_{\rm cub}\)，不冒称有理同构。

取 R616 的同一 \(\mu_6\)-稳定 CM 项链，以及
\[
c_0:b=0,\qquad c_1:b=1,\qquad
D_0=(3-N)[c_1-c_0]\in J_1(\mathbf Q),\quad J_1=J_{X_1}.
\tag{1011.1}
\]
本文范围是
\[
p\ge10^{18},\ p\equiv5\pmod6,
\quad\text{或}\quad
p\ge431,\ p\equiv11\pmod{12}.
\tag{1011.2}
\]

**定理 1011.1。** 存在实际的满射
\[
q_C:J_1\twoheadrightarrow C
\]
和全实数域 \(F_0=\operatorname{End}_{\mathbf Q}^0(C)\)，使 \(C/\mathbf Q\) 简单且来源于非 CM canonical Hecke 部分，并满足
\[
q_CN=0,\qquad
\beta=q_C(D_0)\ \text{非挠},
\]
\[
\boxed{\quad
\dim C=2f,\qquad
\operatorname{rank}C(\mathbf Q)=f,\qquad
C(\mathbf Q)\otimes\mathbf Q=F_0\beta,
\quad f=[F_0:\mathbf Q].
\quad}
\tag{1011.3}
\]
实际同态通过清除一个非零整数同源分母取得；上述结论不依赖这个尺度。

对任一有限素数 \(\ell\)，令
\[
\mathcal L_\ell=(F_0\otimes\mathbf Q_\ell)\log_\ell\beta
 \subset\operatorname{Lie}(C)(\mathbf Q_\ell).
\]
则
\[
\boxed{\quad
\dim_{\mathbf Q_\ell}\mathcal L_\ell=f,\qquad
\mathcal L_\ell\cap\operatorname{Lie}(C)(\mathbf Q)=\{0\}.
\quad}
\tag{1011.4}
\]
这里也允许 \(\ell=p\) 及坏约化；对数通过乘整数进入形式邻域后定义。

原 \(c_1\) 处 \(t=b-1\) 是有理参数。写真实映射的形式对数
\[
\log_\ell q_C[x-c_1]=\sum_{n\ge m}u_nt^n,\qquad
u_n\in\operatorname{Lie}(C)(\mathbf Q),\quad u_m\ne0.
\tag{1011.5}
\]
则存在 \(\lambda\in\operatorname{Ann}(\mathcal L_\ell)\)，使
\[
\lambda(u_m)\ne0,\qquad
\lambda\log_\ell q_C[x-c_1]
 =\lambda(u_m)t^m+O(t^{m+1}).
\tag{1011.6}
\]
这个函数在定义它的邻域内的全部有理点上为零，且其消失阶准确为 \(m\)。

## 2. 同一个 CM 点及 Nekovář 定理的实际输入

由 R1010，可选非 CM canonical 简单 Hecke 因子
\[
q_\pi:J_4\longrightarrow A_\pi,\qquad q_\pi N=0,
\qquad q_\pi\iota_*D_0\ \text{非挠}.
\tag{1011.7}
\]
新部分是 \(N\) 的零部，并且 \(N\) 与 Hecke 作用相容，所以可以在新部分选择实际 Hecke 商映射。若有重数，只选择对给定点非零的一个映射；这里不把重数默认为一。

canonical 水平含中心，故相关权二自守表示 \(\pi\) 的中央角色平凡。记
\[
F=\operatorname{End}_{\mathbf Q}^0(A_\pi),\qquad
d=[F:\mathbf Q]=\dim A_\pi.
\]
这是全实 GL2 型系数域。可在有理同源类中换模型使端环为 \(\mathcal O_F\)，再清同态分母；不改变下文秩与非挠性。

[R616 §2](R616-original-CM-point-difference-and-explicit-height-basis.md) 已准确计算
\[
c=\iota(c_1):\ v=1,\quad u=1/\alpha,\qquad
K(c)=L.
\]
令 \(c_{0,4}=\iota(c_0)\)；它是有理点。对
\[
P=q_\pi[c-c_{0,4}]\in A_\pi(F_{\rm cub})
\tag{1011.8}
\]
及 \(\sigma\in\operatorname{Gal}(L/K)\) 的生成元，有
\[
\sigma c=\delta_{\kappa(\sigma)^{-1}}c,
\quad \kappa(\sigma)=\sigma(\alpha)/\alpha,
\]
\[
q_\pi\iota_*D_0=(2-\sigma-\sigma^2)P.
\tag{1011.9}
\]
复共轭 \(s\) 固定 \(P\)，并满足 \(s\sigma s^{-1}=\sigma^{-1}\)。

在 \(F'=F(\zeta_3)\) 上令
\[
e_\kappa=\sum_{i=0}^2\kappa(\sigma)^{-i}\sigma^i,
\qquad
e_{\kappa^{-1}}=\sum_{i=0}^2\kappa(\sigma)^i\sigma^i.
\]
注意这两个未除以三的平均满足
\[
e_\kappa+e_{\kappa^{-1}}=2-\sigma-\sigma^2.
\]
由 (1011.9) 至少一个投影非挠；复共轭只作用点而固定系数 \(F'\)，将两投影交换，故二者均非挠。

应用 Nekovář 的 Theorem 3.2，准确数据如下：

| 定理输入 | 本文实际数据 |
|---|---|
| 全实底域、四元数代数 | \(\mathbf Q,\ M_2(\mathbf Q)\) |
| 开紧水平 | 原 canonical \(H_6\times N_{\rm ns}(p)\) 及外处最大紧群 |
| 简单商 | 上述实际 \(A_\pi\)，系数域 \(F\) |
| CM 域和 CM 点 | \(K=\mathbf Q(\zeta_3)\)，同一个 \(c=(v=1,u=1/\alpha)\) |
| 点域及角色 | \(K(c)=L,\ \kappa,\kappa^{-1}\) |
| 非 CM 假设 | \(\pi\) 非 CM，满足该定理的条件 \((\star)\) |
| 非挠输入 | 刚得到的 \(e_\kappa P,e_{\kappa^{-1}}P\) |

若该文使用有理 Hodge 除子作基点，与 \(c_{0,4}\) 的差为有理常数，非平凡角色平均将它消去。这正是 R616 (616.12)，没有删除未知的非有理常数。

该定理适用于任意上述开紧群；不额外要求这里的水平平方自由，也不须先假设 Rankin 导数非零。它给
\[
\dim_{F'}\bigl((A_\pi(L)\otimes_{\mathbf Z}\mathbf Q)\otimes_FF'\bigr)^{(\kappa)}
 =
\dim_{F'}\bigl((A_\pi(L)\otimes_{\mathbf Z}\mathbf Q)\otimes_FF'\bigr)^{(\kappa^{-1})}=1.
\tag{1011.10}
\]
记 \(M=A_\pi(L)\otimes_{\mathbf Z}\mathbf Q\)，这是 \(F[S_3]\)-模。其三阶子群非平凡部分恰为一份二阶标准表示：
\[
M_{\rm new}\simeq\operatorname{Std}_F.
\tag{1011.11}
\]
平凡和符号表示都限制为三阶子群的平凡表示，不在此部中。式 (1011.10) 排除了额外标准表示重数。

## 3. 三次限制标量的 trace-zero 部分准确为半秩

构造真正有理阿贝尔簇
\[
B=\ker\!\left(
 \operatorname{Tr}:\operatorname{Res}_{F_{\rm cub}/\mathbf Q}(A_\pi)
 \longrightarrow A_\pi
 \right)^0.
\tag{1011.12}
\]
它的维数为 \(2d\)，且 \(F\) 在 \(\mathbf Q\) 上作用。

有理点张量 \(\mathbf Q\) 后，有限分量群及有限上同调障碍均消失；因此
\[
B(\mathbf Q)\otimes\mathbf Q
 \simeq
 \ker\!\left(A_\pi(F_{\rm cub})\otimes\mathbf Q
     \xrightarrow{\operatorname{Tr}} A_\pi(\mathbf Q)\otimes\mathbf Q\right).
\]
在 \(M^s\) 上，该 trace 是 \(1+\sigma+\sigma^2\)。标准表示的 \(s\)-不变部为一维，平凡表示的 trace 为三，符号表示没有 \(s\)-不变向量。由 (1011.11) 得
\[
\boxed{\quad
\dim B=2d,\qquad
\operatorname{rank}B(\mathbf Q)=d,\qquad
\dim_F(B(\mathbf Q)\otimes\mathbf Q)=1.
\quad}
\tag{1011.13}
\]
这一步直接计算实际三次限制标量的秩，不将 \(\pi\) 与 \(\pi\otimes\chi_{-3}\) 作为已知互异的有理因子来计数。

## 4. 全部同源重数和内扭曲的处理

须证明从 \(B\) 取出的简单商仍有准确半秩；仅用 (1011.13) 的总秩不足以逐因子推出此结论。

取辅助 Tate 素数 \(r\)。在每个 \(F\hookrightarrow\overline{\mathbf Q}_r\) 嵌入上，\(A_\pi\) 的二维表示记为 \(V_\pi\)。限制标量的置换表示分解为 \(\mathbf1\oplus\operatorname{Std}\)，所以 \(B\) 的对应四维表示为
\[
W_\pi=V_\pi\otimes\operatorname{Std}_{L/\mathbf Q}
 \simeq
 \operatorname{Ind}_{G_K}^{G_{\mathbf Q}}
     \bigl(V_\pi|_{G_K}\otimes\kappa\bigr).
\tag{1011.14}
\]
\(\pi\) 非 CM，故 \(V_\pi|_{G_K}\) 绝对不可约。也可直接使用 Nekovář Proposition 6.2.1 中非 CM 与限制表示绝对不可约的等价关系。

两个 \(G_K\) 共轭组成部分的行列式分别为
\[
\chi_{\rm cyc}\kappa^2,\qquad
\chi_{\rm cyc}\kappa^{-2}.
\]
二者不同，因为 \(\kappa\) 阶为三。因此这两个不可约表示不等价，指数二诱导 (1011.14) 绝对不可约。

由 Schur 引理及 Faltings 的 Tate 同态定理，
\[
\operatorname{Cent}_{\operatorname{End}_{\mathbf Q}^0(B)}(F)=F.
\tag{1011.15}
\]
这里先按 \(F\)-作用分解 Tate 模再取中央化子；不同系数嵌入之间可能的内扭曲不会被漏计，也不会被错当作 \(F\)-线性自同态。

所有中心幂等元都属于 (1011.15) 的域 \(F\)，故 \(B\) 在 \(\mathbf Q\) 上同源于一个简单簇的幂：
\[
B\sim_{\mathbf Q}C^m.
\]
记
\[
D=\operatorname{End}_{\mathbf Q}^0(C),\quad
F_0=Z(D),\quad [D:F_0]=n^2,\quad [F_0:\mathbf Q]=f.
\]
由 (1011.15)，\(F_0\subset F\)，且 \(F\) 是中央单代数 \(M_m(D)\) 的极大交换子域。因此
\[
d=mnf.
\tag{1011.16}
\]

非零 \(D\)-模 \(C(\mathbf Q)\otimes\mathbf Q\) 在除环 \(D\) 上自由，设其秩为整数 \(t\ge1\)。一方面
\[
\operatorname{rank}B(\mathbf Q)=mtn^2f;
\]
另一方面由 (1011.13)、(1011.16) 等于 \(d=mnf\)。于是
\[
tn=1,\qquad t=n=1.
\]
故
\[
D=F_0\subset F,\qquad
\operatorname{rank}C(\mathbf Q)=f,\qquad
\dim C=\frac{2d}{m}=2f.
\tag{1011.17}
\]
\(F_0\) 是全实域。这还排除了会使简单因子秩计算失真的非平凡 Schur 指数；没有忽略潜在的 quaternionic 内扭曲。

## 5. 商确实来自原 \(J_1\)，且原 \(D_0\) 在商中非挠

在 \(F_{\rm cub}\) 上，\(q_\pi\iota_*:J_1\to A_\pi\) 是实际同态。通过限制标量的伴随性质，得到 \(\mathbf Q\)-同态
\[
\Psi:J_1\longrightarrow
 \operatorname{Res}_{F_{\rm cub}/\mathbf Q}(A_\pi).
\]
它的三个几何分量是 \(\iota_*\) 的三个共轭再接 \(q_\pi\)。其 trace 为
\[
q_\pi(1+\delta+\delta^2)\iota_*
 =q_\pi N\iota_*=0.
\]
因 \(J_1\) 连通，\(\Psi\) 的像包含在 \(B\) 的单位分量中；并且 \(\Psi N=0\)。

\(\Psi(D_0)\) 的一个几何分量是 (1011.7) 的非挠点，故 \(\Psi(D_0)\) 非挠。又 \(\operatorname{im}\Psi\) 是 \(B\sim C^m\) 的阿贝尔子簇，故它同源于 \(C\) 的一个非零幂。取对这个点非零的简单商投影，清除同源分母，得到实际有理满射
\[
q_C:J_1\twoheadrightarrow C,\qquad q_CN=0,
\]
且 \(\beta=q_C(D_0)\) 非挠。由 (1011.17)，\(C(\mathbf Q)\otimes\mathbf Q\) 在 \(F_0\) 上一维，因此恰等于 \(F_0\beta\)。定理 (1011.3) 成立。

这也说明所选 \(C\) 确实来源于原曲线的非 CM 部分。有限扩张 \(L\) 后，(1011.14) 回到非 CM 的 \(V_\pi\) 组成部分；它不变成由一维角色组成的 CM 表示。

## 6. 原有理 CM jet 与实际 Mordell–Weil 对数空间的横截性

### 6.1 非挠有理点的几何稠密性

\(\langle\beta\rangle\) 的 Zariski 闭包是定义在 \(\mathbf Q\) 上的代数子群。因 \(\beta\) 非挠，其单位分量正维；由 \(C/\mathbf Q\) 简单，该单位分量为 \(C\)。故
\[
\overline{\langle\beta\rangle}^{\,\rm Zar}=C.
\tag{1011.18}
\]
同样对 \(\beta\) 的任意非零整数倍成立。特别地，任何包含这种倍数的真 \(\overline{\mathbf Q}\)-代数子群都不可能存在。

对任意 \(\ell\)，\(C(\mathbf Q_\ell)\) 紧；形式对数在有限指数开子群上定义且局部单射，所以用乘整数延拓后，其核为挠群。因此 \(\log_\ell\beta\ne0\)，不要求好约化。

### 6.2 对数空间的维数

Fuchs–Pham Theorem 2.2 的精确版本给出：若一个非零代数点对数落入定义在 \(\overline{\mathbf Q}\) 上的线性子空间，则存在包含该点的正维代数子群，其 Lie 代数包含在该子空间中。这里需要“包含该点”，而不仅是存在某个不相干的正维子群。

按 \(\tau:F_0\hookrightarrow\overline{\mathbf Q}\) 分解
\[
\operatorname{Lie}(C)_{\overline{\mathbf Q}}
 =\bigoplus_\tau V_\tau,\qquad \dim_{\overline{\mathbf Q}}V_\tau=2.
\]
固定 \(\overline{\mathbf Q}\hookrightarrow\mathbf C_\ell\)。若 \(\log_\ell\beta\) 的任一 \(\tau\) 分量为零，它便落入删去该 \(V_\tau\) 的真代数线性子空间。当 \(f=1\) 时这直接违反对数非零；否则上述定理与 (1011.18) 矛盾。

所以每个 \(\tau\) 分量非零，特别是在 \(F_0\otimes\mathbf Q_\ell\) 的每个局部域因子中都非零。乘法映射
\[
F_0\otimes\mathbf Q_\ell\longrightarrow
\operatorname{Lie}(C)(\mathbf Q_\ell),\qquad
a\longmapsto a\log_\ell\beta
\]
因此单射，给出 \(\dim\mathcal L_\ell=f\)。

### 6.3 没有非零有理 Lie 向量

假设 \(0\ne u\in\operatorname{Lie}(C)(\mathbf Q)\cap\mathcal L_\ell\)，写
\[
u=a\log_\ell\beta,\qquad a\in F_0\otimes\mathbf Q_\ell.
\]
\(\operatorname{Lie}(C)(\mathbf Q)\) 是二维 \(F_0\)-向量空间。选 \(F_0\)-基后，\(u\) 的两个坐标至少一个是 \(F_0^\times\)，故它在每个局部域因子中的向量均非零。这迫使 \(a\) 在每个局部因子中非零，即 \(a\) 可逆。因此
\[
\log_\ell\beta\in(F_0u)\otimes\mathbf Q_\ell.
\]
但 \(F_0u\) 是定义在 \(\mathbf Q\) 上的 \(f\) 维真子空间，严格小于 \(\dim C=2f\)。再次用包含点版本的解析子群定理，与 (1011.18) 矛盾。由此证明 (1011.4)。

### 6.4 原参数和实际消失函数

R616 已证明指定 \(c_1\) 处粗 \(j\)-映射在特征零一次，且 \(b=1\ne0\)，故 \(t=b-1\) 是有理局部参数。映射
\[
x\longmapsto q_C[x-c_1]
\]
在 \(c_1\) 取零值，且不恒定：否则其诱导的 Jacobian 同态 \(q_C\) 为零，与满射矛盾。

阿贝尔簇在特征零的形式对数由有理群律唯一确定，故 (1011.5) 的全部系数都是有理 Lie 向量，且存在有限的首个 \(m\)。由 (1011.4)，\(u_m\notin\mathcal L_\ell\)；有限维线性代数给出 (1011.6) 所需的 \(\lambda\)。

若 \(x\in X_1(\mathbf Q)\) 落在这个解析邻域中，则
\[
q_C[x-c_1]\in C(\mathbf Q),\qquad
\log_\ell q_C[x-c_1]\in\mathcal L_\ell,
\]
所以 (1011.6) 的函数在 \(x\) 上为零。其首项准确非零，从而在一个可能依赖 \(p,C,\lambda\) 的充分小邻域内，仅 \(c_1\) 是零点。这里没有把这个未知大小的邻域认作原候选所在的统一圆盘。

## 7. 精确边界及接续任务

1. 本文只处理原 \(X_1\) 及同一个 \(c_0,c_1,D_0\)。变化 \(X_d\) 的点域、实际秩和局部格不能由本篇照搬。
2. (1011.6) 是特征零非消失。不能据此写 \(\lambda(u_m)\in\mathbf Z_p^\times\)，也没有统一控制将 \(\lambda\) 化为本原整向量所需的尺度。
3. R434 的固定一维 CM 整首项结论不自动适用于本篇的非 CM 商。这里实际消失函数的系数涉及 \(\log_p\beta\) 与原 Abel jet 的相对位置，必须证明相应首项相对于完整尾项的赋值界。
4. 相同的局部 Weil–Deligne 型不固定 potentially crystalline 表示的 Hodge filtration，故不能将 R374/R390 的 CM 形式通道移给本篇非 CM 因子；必须计算实际两列对数与 jet。
5. 坏素 \(p\) 处的原模型、参数半径、同源分母、Mordell–Weil 格与非 \(p\) 条件全部保留；半秩不代替这些局部计算。
6. R1007/R1008 的全部有理自对应高度障碍仍有效。本文的线性商路线不撤销它们，也不删除原 \(\eta_h\) 高度问题。
7. 即使随后完成原圆盘排点，仍须处理 R1003/O0 的全局覆盖：完整惯性、非整 \(j\)、变化 CM 域、非平凡 \(\sigma\) 及其它真实小除法域支路。

## 8. 原始来源和审核

- Jan Nekovář, *The Euler system method for CM points on Shimura curves*, in **L-functions and Galois representations**, LMS Lecture Note Series 320, Cambridge University Press (2007), pp. 471–547；使用 §3.1、Theorem 3.2、§3.4 以及 Proposition 6.2.1。已实读原文的开紧群、实际 CM 点、角色和非 CM 条件：[原文 PDF](https://citeseerx.ist.psu.edu/document?doi=bb4d35a23c1b2ec8d55e67466e32933f4690ee37&repid=rep1&type=pdf)；[出版页](https://www.cambridge.org/core/books/abs/lfunctions-and-galois-representations/euler-system-method-for-cm-points-on-shimura-curves/238DD71B774BD86BE904D7A81371E64C)。
- Gerd Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, **Invent. Math. 73** (1983), 349–366；使用导言 b) 的 Tate 同态定理：[原文 PDF](https://math.uchicago.edu/~drinfeld/Deligne%27s_conjecture_Manin_conf/Faltings_argument/Faltings.pdf)，[DOI](https://doi.org/10.1007/BF01388432)。相关勘误 **Invent. Math. 75** (1984), 381；本篇不使用原高度公式。
- Clemens Fuchs and Duc Hiep Pham, *The p-adic analytic subgroup theorem revisited*, **p-Adic Numbers, Ultrametric Analysis and Applications 7** (2015), 143–156，Theorem 2.2，特别是结论中代数子群包含指定点：[原文](https://arxiv.org/html/1502.00768v1)，[DOI](https://doi.org/10.1134/S2070046615020065)。
- 原几何、点域和基点归一化：[R616](R616-original-CM-point-difference-and-explicit-height-basis.md) §§1–2；原非 CM 非挠输入：[R1010](R1010-original-CM-divisor-nontorsion-in-nonCM-part.md)。没有使用相反扭向的秩零断言。
- global_route 与 root 独立纸面审核三次标准表示、内扭曲/Schur 指数、实际商下降及两次解析子群定理。root 补核每个 \(\ell\)-进系数域因子的非零性与 \(\dim\mathcal L_\ell=f\)。本篇无新数学程序执行，无旧窗口重算。


## 后继：原饱和 CM Lie 商的首层单位

[R1026](R1026-original-single-remainder-and-integral-CM-annihilating-log-direction.md)
在充分大的 \(p\equiv11\bmod12\) 行，给原 \(P=(p-1)D_0\)
在真实整 \(\delta\)-方向和原 Lie 格定义的饱和 CM 商中的第
\(m\) 层本原性。它尚不保证本篇任意选定具体 \(C\) 模型的
Néron differential 饱和；同源尺度与原 \(c_1\) jet 的相对比较
仍是实际待证接口。


## 后继：实际整MW消去测试

[R1035](R1035-original-lowest-type-integral-Lie-comparison-by-two-PD-thickenings.md)已支付原最低型的实际Lie整搬运；[R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md)进一步核本篇条件非挠块的split中心及原J真实重数，构造由完整原log定义的整MW消去泛函。它可能为零或非本原，原CM配对K_p仍待单位证明；不据此宣称本篇任意商模型的Néron格饱和。
