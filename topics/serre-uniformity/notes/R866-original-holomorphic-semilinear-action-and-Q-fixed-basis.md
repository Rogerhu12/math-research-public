# R866：原全纯微分的真实半线性作用与 Q 固定基

日期：2026-11-16。状态：有限准确执行证明。实际输入必须是 R864 成功输出的完整 127 维 $K$ 基；在该输入产生及本消费者公开完成前，本文不预填新的矩阵、选行、特征维数或固定基数值。

本文接 [R864](R864-original-holomorphic-differentials-from-cusp-evaluation.md)、[R853 实际结果](../results/R853-certified-original-three-V1-conjugates-and-semilinear-generators.md)、[R853 原执行规范](R853-original-three-V1-conjugates-method.md)、[R802](../results/R802-original-semilinear-parity-and-degree-seven-relations.md) 与 [R860](R860-original-adjugate-semilinear-descent-and-rational-differential.md)。本次只作用于原全纯微分空间，不构造整个函数域或 272 维正规整基的半线性矩阵。

## 1. 这里的共轭确实同时作用于系数和原曲线

固定原
$$
K=\mathbb Q(s),\quad s=1+2\zeta,\quad s^2=-3,
\qquad \xi=\zeta_{41}.
\tag{866.1}
$$
R802 区分的系数作用是 $c_0(s)=-s$、$c_0(\xi)=\xi$；它不是 $\xi\mapsto\xi^{-1}$。原模型的扭曲再引入 $T^{41}$，在同一参考 cusp 上给 $q_Y\mapsto-q_Y$。原 weight 2 automorphy 因子为 1，故原截面的准确展开满足
$$
[q_Y^n]\varepsilon(c_YF)=(-1)^n c_0([q_Y^n]\varepsilon(F)).
\tag{866.2}
$$
此外 $c_Y\tau=\tau$ 且 $c_Y\nu=\nu$，其中 $\nu=82\tau\,dq_Y/q_Y$ 是同一原微分。后者也可直接由 $d(-q_Y)/(-q_Y)=dq_Y/q_Y$ 验证。

R853 所读的每个原 $V_1$ 截面 $e_i$ 都有 129 项已成展开，其字段 `integer_qY_xi_coefficients` 是每项 40 个**整数**，原 $e_i=82^2T_{(1,i)}$ 本身已经包含整尺度 $6724=82^2$，不是还需除回或再乘的数值。故这些具体系数属于 $\mathbb Q(\xi)$，逐项被 $c_0$ 固定。只对这些原有理坐标列，(866.2) 才能简化为行符号作用；对之后任意 $K$ 系数列，仍须保留 $s\mapsto-s$。

令 $A\in\mathbb Z^{560\times146}$ 是 R853 已使用的完整原矩阵：
$$
A_{40n+r,i}=[q_Y^n\xi^r]e_i,
\quad 0\le n\le13,\quad0\le r<40.
\tag{866.3}
$$
R853/R837 已认证它的 146 个原选行 $I$ 给非零子式。14 项完整展开在原 $V_1$ 上单射；此单射及选行证书直接复用。本次不重新生成旧 Fourier 行，不将 560 行换成 280 个 compressed real 坐标。

## 2. 一个 127 阶有理块决定全部原半线性作用

令 $B\in\mathbb Q^{146\times127}$ 是 R864 的 `original_V1_coefficients` 按列组成的矩阵。其列定义原截面 $F_j=\sum_i B_{ij}e_i$，以及完整 $K$ 基
$$
\omega_j=82F_j\,dq_Y/q_Y.
\tag{866.4}
$$
这里 $F_j$ 是 weight 2 截面，绝非 (866.1) 的 $s$。R864 已把 $\sigma=e_1+e_{73}$ 的第 73 项转换一次；本篇直接读 $B$，不再次加该项。

构造唯一的新前缀矩阵
$$
H=AB\in\mathbb Q^{560\times127}.
\tag{866.5}
$$
它的条目就是原 $F_j$ 的展开，等价地是 $\omega_j/(82\,dq_Y/q_Y)$ 的展开。$e_i$ 相对原 $T_{(1,i)}$ 的 $82^2$ 已在已存整数中，形成 $H$ 时不再乘或除该尺度。若需要微分的 Fourier 系数，准确乘 $82H$；作用矩阵和选行逆始终使用未另缩放的 $H$。R864 全纯性也迫 $H$ 的头 40 行准确为零；这是可以逐项输出的真实接缝。

因 $A_I$ 可逆、$B$ 秩 127，$H_I$ 秩 127。按固定次序从**原已成的 146 行 $I$ 内**选出 127 行 $J$，得到
$$
Q=H_J\in\operatorname{GL}_{127}(\mathbb Q).
\tag{866.6}
$$
这只是一个新的小子式选择，不需要原 $146\times146$ 逆或任何 $K(z)$ Krylov 逆。新程序保存实际 $J,Q,Q^{-1}$ 并核两个准确乘积。

令 $S\in\operatorname{GL}_{560}(\mathbb Q)$ 的第 $40n+r$ 对角元为 $(-1)^n$，$S_J$ 为其选行限制。定义
$$
\boxed{\quad C=Q^{-1}S_JQ.\quad}
\tag{866.7}
$$
完整终验必须为
$$
HC=SH
\tag{866.8}
$$
的全部 $560\times127$ 个原坐标等式。仅在 $J$ 上相等不足以替代终验。

**定理866.1。** 若 (866.6)–(866.8) 的准确证书成立，则对任意 $x\in K^{127}$，原算术半线性作用在基 (866.4) 中恰为
$$
c_Y\left(\sum_jx_j\omega_j\right)
=\sum_i(C\bar x)_i\omega_i,
\qquad \bar s=-s.
\tag{866.9}
$$
而且 $C$ 的元素在 $\mathbb Q$ 中，$C^2=1$。

**证明。** 全纯空间被原 $c_Y$ 保持，所以 $c_Y\omega_j$ 在 (866.4) 中有唯一 $K$ 坐标列。(866.2) 对有理矩阵 $B$ 及整数矩阵 $A$ 给其完整前缀 $SH$；(866.8) 和单射说明该唯一坐标就是 $C$。对于一般 $K$ 列，系数共轭给 $C\bar x$。最后 (866.7) 直接给 $C^2=Q^{-1}S_J^2Q=1$，程序也逐项保存准确乘回。$\square$

没有从“原 normal 坐标有理”推断微分是 $\mathbb Q$ 定义；(866.8) 是原曲线扭曲在这个真实空间上的明确证书。

## 3. 同一个逆立即给完整 Q 固定基

对第 $k$ 个选行 $J_k=40n_k+r_k$，令
$$
\epsilon_k=(-1)^{n_k},\qquad
t_k=\begin{cases}1,&\epsilon_k=1,\\s^{-1}=-s/3,&\epsilon_k=-1.\end{cases}
\tag{866.10}
$$
定义 $T=\operatorname{diag}(t_k)$ 和
$$
P=Q^{-1}T\in\operatorname{GL}_{127}(K),\qquad
\eta_k=\sum_jP_{jk}\omega_j.
\tag{866.11}
$$
这不需要另一个线性系统。由 $\epsilon_k\overline{t_k}=t_k$，
$$
C\bar P=P.
\tag{866.12}
$$
故每个 $\eta_k$ 被原 $c_Y$ 固定；程序以原 $K$ 基 $(1,s)$ 输出准确两分量，并核 (866.12) 以及全部 560 行的展开等式
$$
S\,\overline{HP}=HP.
\tag{866.13}
$$

**定理866.2。** (866.11) 是 $H^0(Y/\mathbb Q,\Omega_Y^1)$ 的完整 127 元 $\mathbb Q$ 基。

**证明。** $P$ 可逆，故这些向量是原全纯空间的 $K$ 基。(866.12) 证明它们固定。任意固定向量唯一写成 $\sum a_k\eta_k$，施加原共轭后由 $K$ 线性独立性得到 $a_k=\bar a_k$，即 $a_k\in\mathbb Q$。这同时证明生成和独立，不需要只引用抽象下降存在性。$\square$

输出还给 $BP$ 的原 146 个 $V_1$ 系数。若消费者确需 normal 表达，原 $V_1$ 列 $u$ 的唯一转换为
$$
u_0+u_1z+\sum_{i=2}^{145}u_i\beta_{i-1}-u_1\beta_{72}.
\tag{866.14}
$$
这里的负号是 $e_1/\tau=z-\beta_{72}$；不能再次使用 R864 从铅笔坐标到原 $V_1$ 的正加号。

## 4. 与真实 Hecke 消费者共享同一块

$H$ 的头 40 行为零，因此删除它们就是 R865 所需 $q_Y^1,\ldots,q_Y^{13}$ 的完整 520 行矩阵。若 R866 先完成，R865 可直接引用实际 $H,J,Q^{-1}$，把行号减去 40；禁止把未完成的约定当成已有 source。反之，若同原 basis/tag 的准确 $127$ 阶块先在 R865 完成，R866 应从其真实来源读取，不重复相同选择与逆运算。

这种复用要求原 R864 基的逐字身份、原 146 条 R786 行及同一个尺度完全相同。它不依赖某个 Hecke 算子已经计算，也不把这块新小逆说成完整正规环乘法表。

## 5. 实际消费者与有限源闭包

新源码为 `R866_original_holomorphic_descent.py`，数学 RESULT 为 `R866-original-holomorphic-semilinear-descent`，成功 FINAL 为 `p41-original-holomorphic-semilinear-descent-certificate.json`。CLI 为 `--config <expanded-job.json> --out <directory> --budget-minutes <minutes>`。

来源分两条：

- R864 的真实成功 manifest/metadata/certificate、kernel、basis、原 evaluation/source audit 及准确 stage 引用；源未出时保持 `null` 和 `producer_inputs_pending=true`。
- 已成功 R853 的原 9 个小 source，及其一日 169 成员 carrier 中的原 R786146条、同一 R837 146 行子式和其完整元数据。载体先逐成员 bytes/SHA 全核，随后按实际读取闭包保留；不从已过期的最初 R786/R837 artifact 猜取数据。R853 的三个原共轭只读引用，不重算。

全部新数学只在公开 Actions。必须保存可共享的 `R866-original-holomorphic-Fourier-matrix.json.gz` 与 `R866-holomorphic-selected-exact-inverse.json.gz`，包括完整行次序、尺度、实际 $J$、原矩阵及两逆乘回。作用矩阵、固定基、原 $V_1$/normal 运输和完整逐行检查按块原子保存；恢复只读同 source/tag 已成阶段。新成功出口要求全部 (866.8)、(866.12)、(866.13) 和原基变换回代，不以估计秩或一个局部子块代替。

本篇没有得到第三类连接、指定补空间、Hecke 活跃投影、原周期、高度或非 $p$ 项。它提供这些消费者所需的真实 $\mathbb Q$ 全纯基，保留原曲线和原 $c_Y$，不改变它们的规范。
