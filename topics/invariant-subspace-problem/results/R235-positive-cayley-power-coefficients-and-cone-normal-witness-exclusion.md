# R235：实际慢 Cayley 和的正幂系数与保正锥正常见证排除

日期：2026-11-12（UTC）。作者：Astra-ISP-0c017065。

**状态：以下结论完整证明。** 本文在原 Haar 表示中工作。将“Hilbert 自伴正”与“保持函数非负锥”始终分开：后者是新增假设，一般正有限秩密度并不满足它。结论不排除任意正常正湮灭态，不证明普通 ISP。

## 1. 模型、两种正性与结论

令 $H=L^2(\mathbb Z_2,\mu)$，$\mu$ 为 Haar 概率测度，
$$
Af(y)=w(y)f(y-1),\qquad w(y)\ge0,
$$
其中本题实际权只在 $0$ 处为零。使用已证明的归一化幂
$$
N_j=A^{2^j}/d_j,\qquad d_j>0,\qquad
N_j^2=\eta_jN_{j+1},\qquad
0<\eta_j\le e^{-770\,16^j},\qquad \|N_j\|=1.
\tag{1.1}
$$
这些是 [R9](../results/R9-radial-odometer-and-nilpotent-approximants.md) 的真实幂恒等式；本文保留全部 carry，绝不令 $N_j^2=0$。

记 $H_+$ 为实值非负函数锥。写 $L\ge_{\mathrm{lat}}0$，意为有界算子 $L$ 把 $H_+$ 映入 $H_+$；写 $L\ge_{\mathrm{lat}}K$，意为 $L-K\ge_{\mathrm{lat}}0$。这与自伴 Loewner 正序不同。

置
$$
a_j=(j+1)^{-2},\qquad
S_N=\sum_{j\ge0}a_jN_j,\qquad
S_Y=\sum_{j\ge0}a_jN_j(I+N_j)^{-1},
\qquad \delta=8e^{-770}<\tfrac12.
\tag{1.2}
$$

**定理1.1。** 以下全部成立。

1. $S_Y$ 有算子范数绝对收敛的 $A$ 幂展开
   $$S_Y=\sum_{n\ge1}c_nA^n,$$
   每个 $c_n$ 都严格为正，且
   $$S_Y\ge_{\mathrm{lat}}(1-\delta)S_N\ge_{\mathrm{lat}}0,
   \qquad S_N,S_Y\ge_{\mathrm{lat}}d_0^{-1}A.$$
2. 若迹类算子 $\rho$ 保持 $H_+$ 且 $t=\operatorname{Tr}\rho>0$，则
   $$\boxed{\operatorname{Tr}(\rho S_N)>0,
   \qquad\operatorname{Tr}(\rho S_Y)>0.}$$
   不要求 $\rho$ 自伴；若另有 $\rho\ge0$（Hilbert 正）且非零，则当然 $t>0$。
3. 因而同时 Hilbert 正、保持函数正锥的非零正常密度，不能湮灭 $S_N\mathcal A$ 或 $S_Y\mathcal A$，其中 $\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$。事实上仅检验单位元 $I\in\mathcal A$ 就已矛盾。

这一结论不要求任何 Walsh 次数指数矩、最高位矩、有限秩或函数的额外可积性。

## 2. Cayley 和的真实幂系数

由 (1.1)，对 $\ell\ge0$ 有
$$
\|N_j^{2\ell}\|\le\eta_j^\ell,\qquad
\|N_j^{2\ell+1}\|\le\eta_j^\ell.
\tag{2.1}
$$
第一式在 $\ell=0$ 也成立。故
$$
\sum_{k\ge1}\|N_j^k\|
\le1+\frac{2\eta_j}{1-\eta_j}
=\frac{1+\eta_j}{1-\eta_j}<2.
\tag{2.2}
$$
这直接证明真 Neumann 展开
$$N_j(I+N_j)^{-1}=\sum_{k\ge1}(-1)^{k-1}N_j^k$$
在算子范数绝对收敛。因为 $\sum_j a_j\le2$，双级数
$$
\sum_j\sum_{k\ge1}
 a_j(-1)^{k-1}\frac{A^{k2^j}}{d_j^k}
\tag{2.3}
$$
绝对范数可和，允许按 $A$ 的指数重排。

给定 $n\ge1$，唯一写成 $n=2^j m$，其中 $m$ 为正奇数。只有 $k\le j$ 的第 $k$ 个 dyadic 行贡献该指数。在最高行 $j$，Neumann 符号为正；在所有更低行 $k<j$，指数 $n/2^k$ 为偶数，符号为负。因此准确系数为
$$
\boxed{
c_{2^jm}=d_j^{-m}
\left[a_j-\sum_{k=0}^{j-1}a_k
 \left(\frac{d_j}{d_k^{2^{j-k}}}\right)^m\right].}
\tag{2.4}
$$
$j=0$ 时空和为零，故每个奇数指数的系数恰为 $d_0^{-m}>0$。

由 (1.1) 与非零 $A^{2^{k+1}}$，有
$$d_{k+1}/d_k^2=\eta_k.$$
递推给出对 $k<j$ 的准确等式
$$
r_{k,j}:=\frac{d_j}{d_k^{2^{j-k}}}
=\prod_{i=k}^{j-1}\eta_i^{2^{j-1-i}}
\le\eta_{j-1}<1.
\tag{2.5}
$$
因此对所有正奇数 $m$，
$$
\sum_{k<j}a_kr_{k,j}^m
\le2\eta_{j-1}.
\tag{2.6}
$$
对 $j\ge1$，$(j+1)^2\le4\,16^{j-1}$，并且 $x e^{-770x}$ 在 $x\ge1$ 上递减，所以
$$
\frac{2\eta_{j-1}}{a_j}
\le2(j+1)^2e^{-77016^{j-1}}
\le8e^{-770}=\delta.
\tag{2.7}
$$
把 (2.6)—(2.7) 代回 (2.4)，得到
$$
 c_{2^jm}\ge(1-\delta)a_jd_j^{-m}>0
 \quad(j\ge1),
\qquad c_m=d_0^{-m}>0\quad(j=0).
\tag{2.8}
$$

此外，从 (2.3) 的绝对可和性得
$$\sum_{n\ge1}|c_n|\|A^n\|<\infty.$$
每个 $A^n$ 都保持 $H_+$。在 dyadic 指数 $2^j$ 上使用 (2.8)，在其余指数上使用 $c_n>0$，即可逐项减去 $(1-\delta)S_N$。非负锥在 $H$ 中闭，故有界保锥算子的集合在算子范数下闭，最后得到
$$S_Y\ge_{\mathrm{lat}}(1-\delta)S_N.$$
$n=1$ 的系数恰为 $d_0^{-1}$，其余系数非负，故 $S_Y\ge_{\mathrm{lat}}d_0^{-1}A$；$S_N$ 的同一下界直接来自 $j=0$ 项。定理第一项证毕。

这不是宣称每个单独的 $N_j(I+N_j)^{-1}$ 保锥。式 (2.4) 使用整个慢和的各行相消，随后才得到总和的正系数。

## 3. 保锥迹类算子的迹非负

**引理3.1。** 若 $R$ 为保持 $H_+$ 的迹类算子，则 $\operatorname{Tr}R\ge0$，且该迹为实数。

证明。令 $P_m$ 为到前 $m$ 位有限柱空间的正交条件期望。它是保锥的有限秩正交投影，且 $P_m\to I$ 强。该空间有由归一化柱集示性函数组成的正交基 $\{e_{m,r}\}_{r<2^m}$，全部基函数非负。因此
$$
\operatorname{Tr}(P_mRP_m)
=\sum_{r<2^m}\langle Re_{m,r},e_{m,r}\rangle\ge0.
\tag{3.1}
$$
每项都为实数。对迹类 $R$，
$$\|P_mRP_m-R\|_1\longrightarrow0.$$
这可先对有限秩 $R$ 用强收敛证明，再由 $\|P_m\|\le1$ 和有限秩在迹范数中的稠密性推广。于是 (3.1) 的迹趋向 $\operatorname{Tr}R$，引理得证。

**推论3.2。** 若 $\rho$ 是保锥迹类，$L\ge_{\mathrm{lat}}K$，则
$$\operatorname{Tr}(\rho L)\ge\operatorname{Tr}(\rho K).$$
因为 $\rho(L-K)$ 仍为保锥迹类，可直接用引理。这里不假设 $L,K$ 自伴，也不使用不适用的 Loewner 迹比较。

## 4. Haar 正常性给出的严格正迹

为付清所用的弱极限，回忆实际纯位近似
$$N_j=E_j+R_j,\qquad \|R_j\|\le\eta_j\to0,$$
其中 Haar 参考向量为 $\Omega_+=(e_0+e_1)/\sqrt2$，$E_j=e_{10}^{(j)}$。若 $f,g$ 都只依赖前 $m$ 位，则对 $j\ge m$，
$$\langle E_jf,g\rangle=\tfrac12\langle f,g\rangle.$$
有限柱在 $H$ 稠密，且 $\|N_j\|=1$，所以
$$N_j\longrightarrow\tfrac12 I\quad\text{WOT}.
\tag{4.1}
$$
这与 [R12](../results/R12-normalized-powers-and-compact-commutant.md) 的归一化幂极限一致。对任意迹类 $\rho$，先以有限秩逼近再使用范数统一界，(4.1) 给
$$\operatorname{Tr}(\rho N_j)\longrightarrow\tfrac12\operatorname{Tr}\rho.
\tag{4.2}
$$
这里使用的是原 Haar 表示中的正常性，不能把该步骤移到 R210–R211 的奇异状态。

现在设 $\rho$ 保锥且 $t=\operatorname{Tr}\rho>0$。引理3.1给
$$\operatorname{Tr}(\rho N_j)\ge0\quad\text{对所有 }j.$$
由 (4.2)，存在 $J=J_\rho$，使所有 $j\ge J$ 均满足
$$\operatorname{Tr}(\rho N_j)\ge t/4.$$
范数绝对收敛允许逐项取迹，于是
$$
\operatorname{Tr}(\rho S_N)
=\sum_ja_j\operatorname{Tr}(\rho N_j)
\ge\frac t4\sum_{j\ge J}\frac1{(j+1)^2}
\ge\frac{t}{4(J+1)}>0.
\tag{4.3}
$$
再用第2节的格序比较和推论3.2，
$$
\boxed{
\operatorname{Tr}(\rho S_Y)
\ge(1-\delta)\operatorname{Tr}(\rho S_N)
\ge\frac{(1-\delta)t}{4(J+1)}>0.}
\tag{4.4}
$$
$J_\rho$ 不提供跨所有正常态的统一速率；本文只需每个固定正常密度的确切极限。

对于任意非负可和系数列 $a$，只要正系数出现于无穷多个位，同一论证直接给 $\operatorname{Tr}(\rho\sum a_jN_j)>0$。Cayley 总和则须另检查 (2.4) 的支配条件；本文仅声称已明确验证的 $a_j=(j+1)^{-2}$ 情形。

## 5. 有限放大零子商与具体密度类

若 $f\ge0$，则秩一算子 $f\otimes f:x\mapsto\langle x,f\rangle f$ 同时 Hilbert 正且保锥。任意有限和，或满足 $\sum_\nu\|f_\nu\|^2<\infty$ 的可数和
$$\rho=\sum_\nu f_\nu\otimes f_\nu,\qquad f_\nu\ge0,$$
均具有相同两种正性。各 $f_\nu$ 允许任意慢的位尾与次数尾；逐向量乘任意常数相位不改变 $\rho$。

更一般，定理直接适用于所有同时具有这两种正性的迹类算子，不要求预先给出非负向量的秩一分解。

在有限放大中，设 $M,N\subset H^{(d)}$ 为闭 $A^{(d)}$ 不变旗，$N\subset M$；令 $Q=M\ominus N$ 为商的正交实现，且 $S_Q=0$，其中 $S=S_N$ 或 $S_Y$。若 $q=(q_1,\ldots,q_d)\in Q$，则
$$\rho_q=\sum_{i=1}^dq_i\otimes q_i\ge0,\qquad
\operatorname{Tr}(\rho_qS)=\langle S^{(d)}q,q\rangle=0.$$
若 $q\ne0$ 且 $\rho_q$ 保锥，(4.3)—(4.4) 矛盾。因此
$$
\boxed{q\in Q,\quad \rho_q\ge_{\mathrm{lat}}0\ \Longrightarrow\ q=0.}
\tag{5.1}
$$
特别，各分量在乘以常数相位后均非负的非零向量不可能在这样的 $Q$ 中。此处不假设 $P_Q$ 保锥、不假设 $C$ 保持 $Q$，也不通过未经证明的投影正则性改变向量。

## 6. 与次数指数矩路线独立的明确例子

令 $F_k$ 为两两不交的有限位集合，且 $|F_k|=k$，例如
$$F_k=\{k(k-1)/2,\ldots,k(k+1)/2-1\},\qquad k\ge1.$$
取
$$f=1+\sum_{k\ge1}\frac{1}{4k^2}\chi_{F_k}.$$
由于 $\sum k^{-2}\le2$，该级数一致收敛，且 $f\ge1/2$。因此 $f$ 有界、非负且非零，$\rho=f\otimes f$ 同时具有两种正性。

然而对任意 $r>1$，Walsh 次数指数矩为
$$\|r^{\mathcal N}f\|^2
=1+\sum_{k\ge1}\frac{r^{2k}}{16k^4}=\infty.$$
故这一密度不满足 [R230](../results/R230-normal-positive-chaos-factorization-and-annihilator-exclusion.md) 的任何次数指数矩假设，却被本文定理排除为慢符号湮灭见证。

另一方面，一般 Hilbert 正秩一密度并不保函数正锥。若 $f=\mathbf1_E-\mathbf1_F$，其中 $E,F$ 为不交正测度集合，则对非负输入 $\mathbf1_E$，$(f\otimes f)\mathbf1_E$ 在 $F$ 上为负。C 实化、有限秩或正常性本身均不消除这个差别。

因此本结果提供一个无尾矩假设的正常见证可排类，但没有把任意正有限秩见证放入该类。一般原 Haar 正常见证、两个实际边界的 $N=M$、原候选算子的普通不变格及普通 Hilbert ISP 仍未解决。
