# R41：第一 chaos 与有限秩二阶 chaos 之间不存在非零全部矩消失对

日期：2026-11-12（UTC+8）。会话：Astra-ISP-e2cb8f94，子任务 `centered_literature`。

**状态：已证明的中间结论。** 一个分量允许是任意第一 Walsh chaos 向量，另一个分量允许有无限多个二阶 Walsh 系数，只要求这些二阶系数形成有限秩矩阵。证明不假定固定测试能控制任意移动函数，而是先使用有限秩将它们放进一个固定有限维空间；对可能出现的线性化退化，完整处理了有理残差不可能全部恒零的步骤。没有证明每个第一 chaos 向量都循环，也未覆盖无限秩二阶或更高有限 chaos，不解决普通 ISP，不主张文献新颖性。

依赖 R9/R12、R33 的第一 chaos 矩分离，以及[R40 的近整周期连续对卷积定理](R40-continuous-moment-convolution.md)。

## 1. 类与结论

令 $\chi_j(y)=(-1)^{b_j(y)}$，并写

$$
f=\alpha_*+\sum_{j\ge0}\alpha_j\chi_j,
\qquad\sum_j|\alpha_j|^2<\infty.
\tag{1.1}
$$

第二个向量写成

$$
g=\beta_*+\sum_{j\ge0}\beta_j\chi_j
+\sum_{0\le i<j}D_{ij}\chi_i\chi_j,
\tag{1.2}
$$

其中

$$
\sum_j|\beta_j|^2+\sum_{i<j}|D_{ij}|^2<\infty.
$$

把系数补成对称矩阵 $D_{ji}=D_{ij}$、$D_{ii}=0$，并假设这个 Hilbert–Schmidt 算子 $D$ 在 $\ell^2(\mathbb N_0)$ 上的秩有限。这里的对称是复转置对称，不要求 Hermitian。

仍令

$$
B(f,g)=\int f(y)g(-1-y)\,d\mu(y).
$$

**定理 1.1。** 若 $B(A^nf,g)=0$ 对每个 $n\ge0$ 成立，则 $f=0$ 或 $g=0$。

由于 $C$ 保持第一 chaos，并将 (1.2) 的二阶矩阵变为 $\overline D$，仍保持有限秩，所以同样排除该两类中的非零通常矩消失对 $\langle A^nf,v\rangle=0$。

这个类确实包含非柱函数、无限尾例子。若 $u,v\in\ell^2$ 支集不交，则

$$
U=\sum u_j\chi_j,\qquad V=\sum v_j\chi_j
$$

独立，$UV\in L^2$，其对称零对角系数矩阵为 $uv^t+vu^t$，秩至多二。$U,V$ 的系数尾可以任意慢。定理允许再给 $UV$ 加任意第一 chaos 向量和常数。

## 2. 高位导数落在固定有限维空间

定义第 $k$ 位的 Walsh 导数系数

$$
H_k:=\beta_k+\sum_{j\ne k}D_{kj}\chi_j.
\tag{2.1}
$$

把第 $k$ 位单独提出时，$g=g_0+\chi_kH_k$，其中 $g_0,H_k$ 都不依赖该位。由系数正交性

$$
\|H_k\|^2=|\beta_k|^2+\sum_{j\ne k}|D_{kj}|^2\le\|g\|^2.
\tag{2.2}
$$

令 $T:\ell^2\to\overline{\operatorname{span}}\{\chi_j\}$ 为等距线性映射 $Tz=\sum z_j\chi_j$。对称性给行向量 $(D_{kj})_j=D e_k$，因此

$$
H_k\in\mathcal V:=\operatorname{span}\{1\}+T(\operatorname{Ran}D),
\qquad d:=\dim\mathcal V\le1+\operatorname{rank}D<\infty.
\tag{2.3}
$$

必要时把 $\mathcal V$ 缩为所有 $H_k$ 的线性张成空间，仍是固定有限维第一 chaos 子空间。这一步是有限秩假设实际进入证明的地方；没有把任意二阶导数都当成有限维。

## 3. 全部矩消失强迫高位方程

反设 $f,g$ 都非零且全部矩消失。R11 和复对称性表明 $1$ 对 $A$、$A^*$ 都循环，所以 $f$ 或 $g$ 为非零常函数的情形会立即迫使另一个为零。以下可设二者都非常函数，因而 $d\ge1$。

固定 $r\ge0$，取充分大 $k$ 使 $2^k>r$。令 $A_k$ 为低 $k$ 位幂零截断、$Q=A_k^r$，并令 $E_k$ 为第 $k$ 位上的矩阵单位 $e_{10}$。写 $f=f_0+\alpha_k\chi_k$、$g=g_0+\chi_kH_k$，局部双线性计算给出精确恒等式

$$
\boxed{
2B(E_kQf,g)-B(Qf,g)
=B(Qf,H_k)+\alpha_kB(Q1,g)+2\alpha_kB(Q1,H_k).
}
\tag{3.1}
$$

为核实：在局部基 $(1,\chi_k)$ 中，$B(1,1)=1$、$B(\chi_k,\chi_k)=-1$、交叉项为零，而 $B(e_{10}x,y)=1/2$ 对 $x,y\in\{1,\chi_k\}$ 全部成立。把两向量展开后即得 (3.1)；$Q$ 不作用第 $k$ 位。

R12 和幂差估计给

$$
\|F_k^{\rm dyad}-E_k\|=\eta_k:=a_{k+1}/a_k,
\qquad \|A^r-Q\|\le r a_k,
$$

$$
\|F_k^{\rm dyad}A^r-E_kQ\|\le\eta_k+r a_k,
\quad F_k^{\rm dyad}=A^{2^k}/\|A^{2^k}\|.
\tag{3.2}
$$

假设中的零矩同时给 $B(A^rf,g)=0$ 和 $B(F_k^{\rm dyad}A^rf,g)=0$。在 (3.1) 中利用 (3.2)，再逐项把 $Q$ 换回 $A^r$。由于 $|\alpha_k|\le\|f\|$、$\|H_k\|\le\|g\|$，总误差不超过 $(2\eta_k+8ra_k)\|f\|\|g\|$。因此

$$
\boxed{
B(A^rf,H_k)+\alpha_kB(A^r1,g)
+2\alpha_kB(A^r1,H_k)=O_{r,f,g}(a_k).
}
\tag{3.3}
$$

这里用本权的 $\eta_k/a_k\to0$。每个 $r$ 固定后误差常数与 $k$ 无关，不声称对所有 $r$ 一致。

## 4. 有限个测试与一个精确有理曲线

对 $v\in\mathcal V$ 定义线性泛函

$$
\mathcal L_r(v)=B(A^rf,v),\qquad
\mathcal M_r(v)=B(A^r1,v),\qquad
b_r=B(A^r1,g).
\tag{4.1}
$$

R33 的矩分离适用于非零第一 chaos 向量 $f$ 和任何非零 $v\in\mathcal V$，所以

$$
\bigcap_{r\ge0}\ker(\mathcal L_r|_{\mathcal V})=\{0\}.
$$

有限维线性代数允许选 $d$ 个固定测试 $r_1,\dots,r_d$，使

$$
L:\mathcal V\longrightarrow\mathbb C^d,
\quad Lv=(\mathcal L_{r_i}(v))_{i=1}^d
$$

为同构。相应定义 $Mv=(\mathcal M_{r_i}(v))_i$、$b=(b_{r_i})_i$，并置

$$
K=L^{-1}M\in\mathcal B(\mathcal V),\qquad v_*=-L^{-1}b.
\tag{4.2}
$$

对选出的测试使用 (3.3)，得

$$
(I+2\alpha_kK)H_k=\alpha_kv_*+O_{\mathcal V}(a_k).
\tag{4.3}
$$

因为 $(\alpha_k)\in\ell^2$，有 $\alpha_k\to0$。所以充分大 $k$ 时左端矩阵可逆，其逆范数有统一界。定义近零解析有理曲线

$$
R(t)=t(I+2tK)^{-1}v_*.
\tag{4.4}
$$

则

$$
\boxed{H_k=R(\alpha_k)+O_{\mathcal V}(a_k).}
\tag{4.5}
$$

这里没有假定包含额外标量 $\alpha_k$ 的线性化在零点单射；所有退化都被保留在这个有理曲线中。

## 5. 关键步骤：剩余有理残差不可能全部恒零

对每个固定 $r\ge0$ 定义

$$
\Phi_r(t)=\mathcal L_r(R(t))+t b_r+2t\mathcal M_r(R(t)).
\tag{5.1}
$$

由 (3.3)、(4.5)，

$$
\Phi_r(\alpha_k)=O_r(a_k).
\tag{5.2}
$$

选出的 $d$ 个测试使对应 $\Phi_{r_i}$ 恒为零，但必须检查其他测试，而不能因此直接推出 $\alpha_k$ 很小。

**引理 5.1。** 至少存在一个固定 $r$ 使 $\Phi_r$ 不恒为零。

**证明。** 反设每个 $\Phi_r$ 都在零附近恒零。若 $v_*=0$，则 $R=0$，(5.1) 给所有 $b_r=0$。由于 $1$ 对 $A$ 循环，这会迫使 $g=0$，与反设矛盾。

因此 $v_*\ne0$。展开

$$
R(t)=t\sum_{j=0}^{\infty}(-2t)^jK^jv_*.
$$

在 $\Phi_r=0$ 中比较一次项，得到 $\mathcal L_r(v_*)+b_r=0$。比较更高次项则得到

$$
\mathcal L_r(K^{j+1}v_*)=\mathcal M_r(K^jv_*)
\qquad(j\ge0,\ r\ge0).
\tag{5.3}
$$

令 $\mathcal U=\operatorname{span}\{K^jv_*:j\ge0\}$。这是非零有限维 $K$-不变空间，所以存在非零 $u\in\mathcal U$ 和复数 $\lambda$ 满足 $Ku=\lambda u$。由 (5.3) 的线性性，$\mathcal L_r(Ku)=\mathcal M_r(u)$ 对所有 $r$ 成立，即

$$
B(A^r(\lambda f-1),u)=0\qquad(r\ge0).
\tag{5.4}
$$

$u\in\mathcal V$ 是非零第一 chaos 向量。$f$ 已假设非常函数，所以 $\lambda f-1$ 也非零（包括 $\lambda=0$ 的情形），并仍属于第一 chaos。式 (5.4) 与 R33 的矩分离矛盾。故某个 $\Phi_r$ 必非恒零。证毕。

## 6. 有限消失阶迫使两个向量都有连续代表

固定引理 5.1 给出的 $r$。令

$$
p_r(t)=\det(I+2tK)\,\Phi_r(t).
$$

由伴随矩阵公式，这是次数至多 $d+1$ 的非零多项式，且 $p_r(0)=0$。令其在零点的消失阶为 $\nu$，则 $1\le\nu\le d+1$。在充分小圆盘内，有 $|p_r(t)|\ge c|t|^\nu$，且行列式有界。由 (5.2)、$\alpha_k\to0$ 得

$$
|\alpha_k|^\nu=O(a_k),\qquad
|\alpha_k|=O(a_k^{1/\nu})=O(a_k^{1/(d+1)}).
\tag{6.1}
$$

又 $\|R(t)\|=O(|t|)$，所以 (4.5) 给

$$
\boxed{\|H_k\|=O(a_k^{1/(d+1)}).}
\tag{6.2}
$$

不论 $d$ 多大，指数 $1/(d+1)$ 都严格为正。因为 R9 的 $a_k\le e^{-16^k}$，(6.1) 使 $\sum|\alpha_k|<\infty$，从而 $f$ 的 Walsh 级数一致收敛，给连续代表。

对 $g$，有 $|\beta_k|\le\|H_k\|$，并且按二阶项的最大指标计数，

$$
\begin{aligned}
\sum_{0\le i<j}|D_{ij}|
&\le\sum_{j\ge1}\sqrt j
\left(\sum_{i<j}|D_{ij}|^2\right)^{1/2}\\
&\le\sum_{j\ge1}\sqrt j\,\|H_j\|<\infty.
\end{aligned}
\tag{6.3}
$$

(6.2) 同时保证一次系数绝对可和。因此 (1.2) 是连续 Walsh 函数的绝对一致收敛级数，也给 $g$ 连续代表。

这里不需要把 (6.1) 的衰减率拿去满足 R26 的某个指定插值阈值；对任意有限 $d$，绝对可和与连续性已经足够用于下一步。

## 7. 连续对卷积定理给出矛盾

§6 证明假设中的两个非零向量都有连续代表。R40 的近整周期卷积定理证明任意两个非零连续函数不可能满足 $B(A^nf,g)=0$ 对所有 $n\ge0$ 成立。与本证明的反设矛盾，定理 1.1 得证。

整个证明的闭合链条是：有限秩提供固定有限维导数空间；R33 提供有限测试的单射性；有理曲线保留退化；其全部残差若消失会产生被 R33 排除的第一 chaos 配对；一个非零残差的有限消失阶迫使绝对可和；最后 R40 排除连续对。没有用稠密性代替任何一个控制步骤。

## 8. 仍未覆盖的情形

1. 若二阶系数矩阵 $D$ 无限秩，$(H_k)$ 不再位于固定有限维空间，§4 的有限逆矩阵不存在。仅知 $\|H_k\|\to0$ 不能替代它。
2. 任意两个第一 chaos 函数的乘积，在删去对角常数后未必有有限秩系数矩阵。例如一个无限第一 chaos 函数的平方，二阶矩阵通常是有限秩矩阵减去一个无限秩对角矩阵，因此不自动属于本条。
3. 更高有限阶 chaos 的高位导数已经不在第一 chaos。R33 不能直接保证其固定有限维测试映射单射，需新的矩分离输入。
4. 一般第一 chaos 向量仍未证明循环；本条只进一步缩小其潜在轨道正交向量可处的类。
