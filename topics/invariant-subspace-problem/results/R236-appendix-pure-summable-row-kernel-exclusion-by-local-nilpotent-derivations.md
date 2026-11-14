# R236 附录：纯可和行的局部幂零导子与全核排除

日期：2026-11-13（UTC）。作者：normal_complex；central_review 与主会话分别全文核验。

状态：已证明的纯模型范围扩展。任意无限支撑复ℓ1纯线性行，以及至少一行无限支撑的纯二次组合，单射且值域稠密；没有实际进位迁移或普通ISP完成声明。

本文完整收录[张量工作笔记](../notes/2026-11-12-tensor-kernel-0c-agent.md)的§15。为保持原证明互引，保留§15及公式编号；下文§12–14指该笔记的历史论证。

## 15. 纯模型的单位偏导、局部幂零导子与全可和行排核

2026-11-13 新补充。作者：normal_complex；central_review 独立核验主证明。只在原 Haar plus 纯乘积表示中工作。本节不删除实际算子中的进位，也不把纯结论运输到实际 $X^2-B_0+Y$。

### 15.1 与已有结论的扣重及准确结论

[R113](R113-pure-tail-dominance-and-carry-obstructions.md) 已证明晚期相对尾范数不超过 $1/2$ 的纯线性范围，包含所列几何比率；本笔记 §12、§14 对该范围只是同步复核。§13 的算子单位图法需要另付
$\|V_j^{-1}T_{j+1}\|$，其纯二次例只处理 $0<\kappa\le2$。

以下改用两个同时成立的纯模型事实：每个固定有限头测试被充分高阶导子精确杀死；无穷多个位上的单位偏导给任意固定阶的强导子单位。所用逆的范数可以很大，因为其乘到的局部余项准确为零。没有把这些逆的费用声明为可供实际迁移的预算。

令
$$
H=L^2(\{0,1\}^{\mathbb N},\mu),\qquad
\Omega=1,\qquad
E_j=|e_1\rangle\langle e_0|_j,
$$
其中 $\mu$ 为等权乘积测度，局部参考向量为
$\Omega_+=(e_0+e_1)/\sqrt2$。所以
$$
E_j^2=0,\qquad [E_i,E_j]=0,\qquad \|E_j\|=1.
$$
系数可以任意复数，不要求按大小重排后与物理位一致。

**定理。**

1. 若 $a\in\ell^1(\mathbb C)$ 有无穷多个非零项，则
   $P_a=\sum_j a_jE_j$ 单射且值域稠密。
2. 若 $a,c\in\ell^1(\mathbb C)$，且 $c$ 有无穷多个非零项，则
   $T=4P_a^2-2P_c$ 单射且值域稠密。
3. 若 $c$ 仅有有限个非零项而 $a$ 有无穷多个非零项，第二个结论仍成立。

以上算子的全部正整数幂也单射且值域稠密。特别，§13 的
$a_j=e^{-\beta j^\alpha}$、$c_j=a_j^\kappa\mathbf1_{j>j_0}$ 在所有
$\alpha,\beta,\kappa>0$ 下满足本定理，不再要求 $\kappa\le2$ 或 $\alpha>1$。

### 15.2 有界纯尾和拟幂零，单位逆合法

每个纯提升和 $P_a$ 都由 $\ell^1$ 假设在算子范数中收敛。任取有限头，写
$$
P_a=H_m+R_m,\qquad
H_m=\sum_{j<m}a_jE_j,\qquad
R_m=\sum_{j\ge m}a_jE_j.
$$
$H_m^{m+1}=0$，且 $H_m$ 与 $R_m$ 交换。若 $|\lambda|>\|R_m\|$，则
$R_m-\lambda I$ 可逆，而
$$
P_a-\lambda I
=(R_m-\lambda I)
\left[I+(R_m-\lambda I)^{-1}H_m\right]
$$
的第二因子是恒等加一个幂零算子，故也可逆。因此
$$
\sigma(P_a)\subseteq\{|\lambda|\le\|R_m\|\}
$$
对所有 $m$ 成立。由 $\|R_m\|\to0$ 得 $\sigma(P_a)=\{0\}$。
同一论证适用于删除任意一个或有限多个位后的和。

固定一个满足 $c_j\ne0$ 的位置。写
$$
P_a=a_jE_j+P_{a,\ne j},\qquad
P_c=c_jE_j+P_{c,\ne j}.
$$
纯平方零给准确分解
$$
T=T_{\ne j}+E_jV_j,\qquad
T_{\ne j}=4P_{a,\ne j}^2-2P_{c,\ne j},\qquad
V_j=8a_jP_{a,\ne j}-2c_jI.
\tag{15.1}
$$
$V_j$ 与 $T$、$E_j$、$E_j^*$ 均交换。因为
$\sigma(8a_jP_{a,\ne j})=\{0\}$ 且 $c_j\ne0$，$V_j$ 是真实有界单位。这里使用谱可逆性，没有假设其非标量部分的范数小于 $2|c_j|$。

### 15.3 精确双导子，不交换不同位置的逆因子

记 $\delta=\operatorname{ad}_T$，即 $\delta(W)=TW-WT$。
局部矩阵计算给
$$
[E_j,[E_j,E_j^*]]=-2E_j,\qquad
[E_j,[E_j,[E_j,E_j^*]]]=0.
$$
在 (15.1) 中，$T_{\ne j}$ 与 $E_j^*$ 及 $V_j$ 交换，因此
$$
\delta^2(E_j^*)=-2E_jV_j^2,\qquad
\delta^3(E_j^*)=0.
$$
定义
$$
W_j=E_j^*V_j^{-2}.
$$
因为 $\delta(V_j^{-2})=0$，有
$$
\boxed{\delta^2(W_j)=-2E_j,\qquad \delta^3(W_j)=0.}
\tag{15.2}
$$

固定一个 $r$ 元集 $F$，按位索引递增次序取有序乘积
$$
W_F=\prod_{j\in F}^{\longrightarrow}W_j.
$$
不同 $W_j$ 不必交换。高阶 Leibniz 公式仍适用：总阶 $2r$ 中每个因子至多可分配两阶，所以只有全部分配两阶的项留下。由 (15.2)，
$$
\boxed{
\delta^{2r}(W_F)
=\frac{(2r)!}{(2!)^r}\prod_{j\in F}(-2E_j)
=(-1)^r(2r)!\,E_F,
\quad E_F=\prod_{j\in F}E_j.
}
\tag{15.3}
$$
这一步没有把 $E_i^*$ 与含其他位的 $V_j^{-2}$ 互换。

### 15.4 任意固定阶的真实强导子单位

$r$ 先任意固定。由于 $c$ 有无穷多个非零项，对每个 $N$ 可选 $N$ 个两两不交的 $r$ 元集合
$$
F_{N,1},\ldots,F_{N,N}
\subseteq\{j\ge N:c_j\ne0\}.
$$
置
$$
U_{N,r}
=\frac{(-1)^r2^r}{N(2r)!}
\sum_{\ell=1}^N W_{F_{N,\ell}}.
$$
这是每个 $N$ 上实际有界的算子；不声称它们的范数一致有界。
由 (15.3)
$$
\boxed{
\delta^{2r}(U_{N,r})
=\frac{2^r}{N}\sum_{\ell=1}^N E_{F_{N,\ell}}
=:R_{N,r}.
}
\tag{15.4}
$$
右侧范数至多 $2^r$，不含 $V_j^{-1}$ 的费用。

对一个固定有限头向量 $x$，充分大 $N$ 时所有选中位均在该头之外。局部计算为
$$
\langle E_F\Omega,\Omega\rangle=2^{-r},
\qquad
\|E_F\Omega\|^2=2^{-r}.
$$
不同 $F_{N,\ell}$ 的非真空波动正交。因此准确有
$$
\|(R_{N,r}-I)x\|^2
=\frac{2^r-1}{N}\|x\|^2.
\tag{15.5}
$$
有限头向量稠密，且 $\|R_{N,r}\|\le2^r$。故
$$
\boxed{\delta^{2r}(U_{N,r})\longrightarrow I\quad\text{强收敛}.}
\tag{15.6}
$$
$r$ 在此极限中固定；没有把 $r$ 随 $N$ 增长的情形纳入 (15.6)。

### 15.5 任何固定头测试的高阶导子准确为零

令 $D$ 为作用在前 $m$ 个物理位上的任意矩阵，张量上尾恒等。
把纯和分成头与尾：
$$
P_a=P_{a,<m}+P_{a,\ge m},\qquad
P_c=P_{c,<m}+P_{c,\ge m}.
$$
于是
$$
T=T_{\ge m}+S_m,
$$
$$
T_{\ge m}=4P_{a,\ge m}^2-2P_{c,\ge m},\qquad
S_m=4P_{a,<m}^2+8P_{a,<m}P_{a,\ge m}-2P_{c,<m}.
\tag{15.7}
$$
$T_{\ge m}$ 与 $D$、$S_m$ 都交换。$S_m$ 的每个单项至少含一个头位 $E_j$。所有这些头位平方零且交换，所以
$$
S_m^{m+1}=0.
$$
由交换导子的二项式，$\operatorname{ad}_{T_{\ge m}}D=0$ 给
$\delta^k(D)=\operatorname{ad}_{S_m}^k(D)$。再展开
$$
\operatorname{ad}_{S_m}^{2m+1}(D)
=\sum_{k=0}^{2m+1}
(-1)^k\binom{2m+1}{k}
S_m^{2m+1-k}DS_m^k.
$$
每项至少有一侧幂次不小于 $m+1$，故
$$
\boxed{\delta^{2m+1}(D)=0.}
\tag{15.8}
$$
这是准确算子等式，不是小范数估计；尾系数仍完整保留在 (15.7) 中。

### 15.6 从局部全配对排除原纯核

定义本表示内的反线性等距对合
$$
(\mathcal Cf)((b_j)_j)=\overline{f((1-b_j)_j)}.
$$
全位互补保持乘积测度，且固定 $\Omega$，所以此 $\mathcal C$ 在原 plus 表示内合法。它满足
$$
T^*=\mathcal C T\mathcal C,\qquad
B(x,y)=\langle x,\mathcal Cy\rangle,\qquad
B(Tx,y)=B(x,Ty).
$$
任意复系数均相容；没有使用一个未实现的无限相位酉。

取 $f,g\in\ker T$。对任意有界 $D,U$ 及整数 $n\ge0$，逐次把导子移过 $B$，有
$$
\boxed{
B(D\delta^n(U)f,g)
=(-1)^n B(\delta^n(D)Uf,g).
}
\tag{15.9}
$$
具体地，$B(\delta(Z)f,g)=0$ 对任意有界 $Z$ 成立；应用
$\delta(D\delta^{n-1}U)=\delta(D)\delta^{n-1}U+D\delta^nU$
并归纳即得 (15.9)。

对固定的 $m$ 头矩阵 $D$，选一个固定 $r>m$。
由 (15.8)，$\delta^{2r}(D)=0$。于是每个 $N$ 均有
$$
B(D\delta^{2r}(U_{N,r})f,g)=0.
$$
使用 (15.6) 的强极限，得到
$$
\boxed{B(Df,g)=0\quad\text{对所有有限头矩阵 }D.}
\tag{15.10}
$$

为自含地说明 (15.10) 迫核为零，反设 $0\ne f\in\ker T$，取 $g=f$。令 $\Pi_m$ 是前 $m$ 位条件期望，也就是头空间张量尾真空的投影。则 $\Pi_m\to I$ 强，且与 $\mathcal C$ 交换。选一个范数为一的头矩阵 $D_m$，把非零向量 $\Pi_m f$ 的单位化送到 $\Pi_m\mathcal Cf$ 的单位化。该局部矩阵与 $\Pi_m$ 交换，因此
$$
\begin{aligned}
B(D_mf,f)
&=\langle D_mf,\mathcal Cf\rangle\\
&=\|\Pi_mf\|\,\|\Pi_m\mathcal Cf\|
+\langle D_m(I-\Pi_m)f,(I-\Pi_m)\mathcal Cf\rangle.
\end{aligned}
$$
第二项的模至多
$\|(I-\Pi_m)f\|\,\|(I-\Pi_m)\mathcal Cf\|$，趋于零；
第一项趋于 $\|f\|^2>0$。这与 (15.10) 矛盾，故 $\ker T=0$。

由 $T^*=\mathcal C T\mathcal C$，也有 $\ker T^*=0$，即 $T$ 值域稠密。单射性与稠密值域逐次传到全部正整数幂。

### 15.7 纯线性与有限辅助支撑的补全

纯线性 $P_a$ 的证明是同一构造的特例：对每个 $a_j\ne0$，(15.1) 的偏导单位直接为 $V_j=a_jI$；(15.2)—(15.6) 全部成立。固定头拆分则用
$$
P_a=P_{a,\ge m}+P_{a,<m},\qquad P_{a,<m}^{m+1}=0.
$$
所以 (15.8)—(15.10) 同样给零核及稠密值域。这里覆盖任意有无穷非零项的复 $\ell^1$ 行，包括 R113 条件不成立的几何行或其他行；不用一个迹表示的核投影递推。

若 $c$ 有限支撑而 $a$ 有无限支撑，选一个有限头包含全部 $\operatorname{supp}c$。在该头的物理基中，$4P_a^2-2P_c$ 是有限的三角算子矩阵，每个对角块均为
$$
4P_{a,\ge m}^2.
$$
尾 $P_{a,\ge m}$ 由刚证的纯线性结论单射，其平方也单射。从三角方程的第一行起逐行消去，整个矩阵单射；反酉对称再给稠密值域。

如果 $a,c$ 都有限支撑，则 $T$ 只作用在一个有限纯头的零常数幂零代数中。非零这样的 $T$ 有非零核，故本节的无限尾条件有实际内容。

### 15.8 实际模型仍缺的步骤

本节没有支付任何原 $N_j,Q_j$ 的进位迁移。

实际模型中，固定有限物理头的幂零性质不会在原全空间上保持：
(15.8) 一般不再等于零。即使 $U_{N,r}$ 每个有界且其导子输出可逼近单位，也不能删除
$$
B((\operatorname{ad}_T^{2r}D)U_{N,r}f,g).
$$
它可能同时含真实进位、未知核和巨大逆因子的成本。

[R236 固定阶广义核附录](R236-appendix-fixed-order-double-commutators-and-generalized-kernel-isotropy.md) 已在其原实际普通 Bell 范围内付固定阶强导子单位及全局等向性；它明确没有付任意局部 $D$ 的等向性。本节新用的是纯模型精确局部幂零，所以不外推那个实际附录，也不混用两稿不同的算子范围。

因此本节关闭纯二次 $\kappa>2$ 及上述更一般纯可和范围，原实际迟首核、普通正常见证及允许误差的实际真空原像仍须继续处理。
