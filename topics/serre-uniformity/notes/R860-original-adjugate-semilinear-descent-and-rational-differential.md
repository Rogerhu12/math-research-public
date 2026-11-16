# R860：原函数域的有界余子式下降与同一有理微分

日期：2026-11-16。状态：**以下是已成原来源上的准确纸面定理及有限执行入口。尚未展开新的二元余子式、幂基坐标、RR 核、连接或 period。**

本文接 [R853 的实际三个共轭](../results/R853-certified-original-three-V1-conjugates-and-semilinear-generators.md) 与 [FM 的有限 RR 矩阵](2026-11-16-original-Y-finite-RR-matrices-and-source-leaves.md)。不重求 R853 三个已成右端，也不把 R806 的辅助有理坐标形式误当原曲线的实下降。新增的是：两个次数至多 272 的二元余子式直接给原剩余生成元的准确函数分式；同一个分式转换适用于实际 normal 向量；原导子及其对偶微分已经被真正的算术共轭固定。

## 1. 全部对象保持原来源

令 $K=\mathbf Q(s)$，$s^2=-3$。在原 $Y_K$ 的 $\tau\ne0$ 图上，保持 R805/R806 的原正规整基

$$
R_\tau=\bigoplus_{i=0}^{271}K[z]\beta_i,
\qquad \epsilon=(0,1^{144},2^{127}),
\qquad \beta_0=1,
\tag{860.1}
$$

以及原整数规范

$$
\tau=e_0,\qquad \sigma=e_1+e_{73},\qquad
w_0=e_2,\qquad z=\sigma/\tau,\qquad w=w_0/\tau.
\tag{860.2}
$$

原 $e_i$ 的尺度为 $82^2$。normal 基中的 $\beta_1=e_2/\tau=w$、$\beta_{72}=e_{73}/\tau$；后者记为 $r$。原 127 个二次补基及其次序不改。

R806 已准确完成 $W(z)=M_w\in M_{272}(\mathbf Q[z])$，列为输入、行为输出，并证明

$$
\deg_z W_{ba}\le1+\epsilon_a-\epsilon_b,
\qquad K(Y)=K(z)[w],\qquad [K(Y):K(z)]=272.
\tag{860.3}
$$

负次数上界表示该项为零。其所有 272 列已经原 820 行准确乘回，不能重新构造旧 S3 块或重求同一 272 列。

R853 的实际输出是

$$
c_Y(\tau)=\tau,\qquad c_Y(\sigma)=e_1-e_{73},
\qquad c_Y(w_0)=w_0,
\tag{860.4}
$$
$$
c_Y(s)=-s,\qquad c_Y(z)=z-2r,\qquad c_Y(w)=w.
\tag{860.5}
$$

这里只剩将一个已知 normal 向量 $r=\beta_{72}$ 写成指定 $K(z)[w]$ 中的实际函数分式；没有三个尚需求的共轭。

## 2. 两个有界余子式

引入独立变量 $T$，定义

$$
A(z,T)=TI_{272}-W(z),\qquad
\chi(z,T)=\det A(z,T),\qquad C(z,T)=\operatorname{adj}A(z,T).
\tag{860.6}
$$

这里 $\chi$ 由原 $W$ 定义，不声称已有一个另行展开的 characteristic-polynomial 文件。令

$$
D(z,T)=C_{00}(z,T),\qquad N(z,T)=C_{0,72}(z,T).
\tag{860.7}
$$

**定理 860.1。** 在原函数域中有

$$
\boxed{\quad r=\frac{N(z,w)}{D(z,w)},\qquad D(z,w)\ne0.\quad}
\tag{860.8}
$$

两个多项式均在 $\mathbf Q[z,T]$，满足

$$
\deg_{z,T}D\le271,\quad \deg_TD=271,
\quad [T^{271}]D=1,
\tag{860.9}
$$
$$
\deg_{z,T}N\le272,\qquad \deg_TN\le270.
\tag{860.10}
$$

其中 $N$ 是删除 $A$ 的 **第 72 行、第 0 列** 后的行列式，符号为 $(-1)^{72}=1$；不是删第 0 行、第 72 列。$D$ 删第 0 行、第 0 列。全部索引从 0 起。

证明。写 $F=K(z)$、$E=F(w)$。由 (860.3)，$W$ 是次数 272 的域扩张中原始元 $w$ 的乘法矩阵。因此 $\chi$ 是 $w$ 在 $F$ 上的首一最小多项式；其次数为 272，并因特征零而可分。在 $E$ 中，$A(z,w)$ 的秩为 271。

原函数行向量 $\boldsymbol\beta=(\beta_0,\ldots,\beta_{271})$ 满足

$$
\boldsymbol\beta W=w\boldsymbol\beta,
\qquad \boldsymbol\beta A(z,w)=0.
\tag{860.11}
$$

伴随恒等式 $CA=\chi I$ 表明 $C(z,w)$ 的第 0 行属于这一维左核。$D$ 是一个 $271\times271$ 主子式，关于 $T$ 的首项严格为 $T^{271}$，故 $D$ 非零且 $\deg_TD<\deg_T\chi$。最小多项式不可约给 $D(z,w)\ne0$。由于 $\beta_0=1$，该行的比例因子只能是 $D(z,w)$，于是

$$
C_{0j}(z,w)=D(z,w)\beta_j\qquad(0\le j\le271).
\tag{860.12}
$$

这给 (860.8)，没有使用一个未执行的 Krylov 逆。

最后，对 $A$ 的任何非零条目赋予总次数上界 $1+\epsilon_a-\epsilon_b$。任一删除第 $j$ 行、第 $i$ 列的行列式项，其上界相加为

$$
271+\sum_{a\ne i}\epsilon_a-\sum_{b\ne j}\epsilon_b
=271+\epsilon_j-\epsilon_i.
\tag{860.13}
$$

故 $\deg_{z,T}C_{ij}\le271+\epsilon_j-\epsilon_i$。对于 $i=0,j=72$ 得 272；非对角余子式不能使用 271 个对角 $T$，所以 $\deg_TN\le270$。证毕。

这一定理给的是一个有界二元多项式**分式**，并不主张 $r\in K[z,w]$。原 $K[z,w]$ 也不因此成为整闭环。$D(z,w)$ 是函数域中的非零元素，不必在整张图上为单位，也不必在某个指定点非零。

## 3. 一条实际 normal 右端的通用入口

对任意实际给定的 normal 多项式向量 $v(z)=(v_i(z))$，令

$$
f=\sum_i v_i(z)\beta_i,
\qquad B_v(z,T)=e_0^t C(z,T)v(z).
\tag{860.14}
$$

由 (860.12) 立即得到

$$
\boxed{\quad f=\frac{B_v(z,w)}{D(z,w)}.\quad}
\tag{860.15}
$$

如果 $\deg_zv_i\le m-\epsilon_i$，则 $\deg_{z,T}B_v\le271+m$，且 $\deg_TB_v\le271$。一个实际多项式向量只需一个标量的 bordered determinant：

$$
B_v(z,T)=-\det
\begin{pmatrix}A(z,T)&v(z)\\e_0^t&0\end{pmatrix}.
\tag{860.16}
$$

对于有理向量 $v=p/d$，保留其真实共同分母 $d(z)\ne0$，得到 $f=B_p(z,w)/(d(z)D(z,w))$；不删任何比例或未知单位。对于原 L 系数，直接沿 $K\to L$ 基变换，原 $b,s$、Galois 相位及常数保持。

因此，FM/R849 中实际需求的 normal 右端可以逐个用 (860.15) 送入同一函数域。首个消费者只需要 $v=e_{72}$，所以不先形成完整 272 个 $C_{0j}$ 或完整乘法表。若将来消费者实际需要一批 $v$，共同的 $A,D$ 保持一个源，按需新增 $B_v$。

### 3.1 回到原 normal 环及有限余模

令 $\mathcal D=D(z,W)$，$\mathcal N_v=B_v(z,W)$。由 $D(z,w)\ne0$，$\mathcal D$ 是 $F$ 上可逆的乘法矩阵。于是

$$
\mathcal D M_f=\mathcal N_v,
\qquad \mathcal D v_f=\mathcal N_v e_0.
\tag{860.17}
$$

这给真正的按需域求值和回代接口。若只要 $f$ 的一个乘法右端，就只解那一个 $\mathcal D$ 右端；若某有限 RR 步确需完整生成矩阵，再处理该步实际的右端。不能把 $\mathcal D$ 在某个坏纤维的奇异性误判为原函数不存在。

清分母之后，membership 仍在原正规环 (860.1) 的完整生成矩阵中判断，沿 FM.6、FM.12、FM.14 的有限余模/有限核规则执行。不把 $D$ 的零点排除出图，也不把一个不消去分母的平面幂环 membership 替代原正规环 membership。本式提供有限原源；尚未执行的生成矩阵或饱和不会因写出分式就变成已成。

### 3.2 原函数的真正共轭

设 $\overline{F}$ 表示只对常数字段施加 $s\mapsto-s$ 的系数共轭。将 (860.8) 代入 (860.5)，对指定函数分式 $F(z,w)$ 有

$$
\boxed{\quad c_Y(F)=
\overline{F}\left(z-2\frac{N(z,w)}{D(z,w)},w\right).\quad}
\tag{860.18}
$$

这是真正的原 $Y$ 算术下降，包含几何 twist。由 R853 原作用两次为恒等，$c_Y(r)=-r$，故 (860.18) 是对合。它不来自“$W$ 的条目在 $\mathbf Q[z]$ 中”这一事实，更不允许略去 $z$ 的替换。

原 $\tau$ 已固定，因此 $U_\tau$ 在真实共轭下稳定；原 $U_\sigma$ 不必单独稳定。共轭先在同一函数域中按 (860.18) 执行，再按完整原两图理想检查正则性或 membership。此处没有假定原 $z$ 是 $\mathbf Q$ 有理函数，也没有偷换成另一个无基点铅笔。

## 4. 原导子及其对偶微分已经下降

保持 R813 的原尺度

$$
D_0=\frac{q_Y}{82}\frac d{dq_Y},\qquad
\delta=\tau^{-1}D_0,\qquad g=\delta z,\qquad h=\delta w.
\tag{860.19}
$$

**定理 860.2。** 原函数域上有

$$
c_Y\delta=\delta c_Y.
\tag{860.20}
$$

令 $\nu=dz/g$ 为 FM/YP 使用的同一个原有理微分，则

$$
\boxed{\quad c_Y(\nu)=\nu,\qquad
c_Y(f\nu)=c_Y(f)\nu.\quad}
\tag{860.21}
$$

证明。R802.11 在同一个参考 cusp 的准确 Laurent 展开给

$$
\varepsilon(c_YF)(q_Y)=c_0(\varepsilon(F))(-q_Y).
\tag{860.22}
$$

$D_0$ 在第 $n$ 项乘准确有理数 $n/82$，与右端常数共轭及 $(-1)^n$ 均交换。此处对权 0 函数施加 $D_0$ 后得到权 2 对象，R802 对原偶权截面的作用仍无额外 automorphy 标量。因此

$$
c_Y(D_0F)=D_0(c_YF).
\tag{860.23}
$$

R853 给 $c_Y\tau=\tau$；除以同一个原 $\tau$ 得 (860.20)。Laurent 展开的单射性将此式提升为原全球函数域等式。

于是 $c_Yg=\delta(c_Yz)$。在微分域中 $dF=(\delta F)\nu$，故

$$
c_Y\nu=\frac{d(c_Yz)}{c_Yg}
=\frac{\delta(c_Yz)}{c_Yg}\nu=\nu.
\tag{860.24}
$$

也可以在同一个原 Tate 帧直接看见 $\nu=82\tau\,dq_Y/q_Y$，而 $dq_Y/q_Y$ 在 $q_Y\mapsto-q_Y$ 下保持。此论证保留原 $82$ 与 $\tau$ 的尺度，不改任何补空间或高度规范。证毕。

特别地，

$$
c_Yh=h,\qquad c_Yg=g-2\delta r,
\tag{860.25}
$$

FM.27 中原先保留的比值 $\delta(c_Yz)/c_Yg$ 在这个实际来源下严格等于 1。这是从 R853 真输出及原 R802/R813 作用得到的新简化，不再要求为微分下降计算一个新的完整 $c_Yg$ normal 矩阵或一般 $\Gamma$。

对余子式分式本身仍可用原已成 $g,h$ 做准确链式微分：

$$
\delta r=
\frac{(gN_z+hN_T)D-N(gD_z+hD_T)}{D^2}\Big|_{T=w}.
\tag{860.26}
$$

偏导作用于两个真实源多项式；需要时可用行列式的逐行导数恒等式形成有限 DAG，不须猜新的连接。在 $D$ 造成的可去奇点，按原 normal 环/局部函数解释，不单独对分母球取逆。

## 5. 有限 RR 与原连接的实际消费边界

FM 中一个完整 RR 核一旦实际得到，其每个源向量都可由 (860.15) 转成有界函数分式，再由 (860.18) 得真实共轭。对定义于 $\mathbf Q$ 的指定可逆层，先按原两图 membership 确定同一空间，再用该真实半线性作用取固定部分。对一次微分只需对其系数作同一作用，$\nu$ 不再附带未知比较因子。

这可以服务 YP 中实际 $a_j$、$\alpha_0$ 的 RR 输入；它不替代那些尚未得到的完整生成矩阵、RR 核向量、所选 $a_j$ 的点值和首项。保原 $\beta,\eta$、$P_0,P_1$、$t=a^3$、theta 二挠、非 $p$ 项、原 splitting 与原 Hecke 行。原 period、高度以及指定 $T_p$ 非零均未由本篇得到。

## 6. 最小执行源与可续状态

首 scope 只构造上述两个余子式的准确原源 DAG、真正共轭替换及同一微分的下降接口。输入为：

1. R806 成功 certificate、原 normal polynomial-multiplier index、实际 34 个准确坐标组、accepted candidate/definition、原 cyclic witness、stage manifest 与 metadata。旧组的分子/逐列分母和原 S3 行映射原样消费，$82^6$ 只用于核来源，不再次乘入已成系数。
2. R805 实际 graded-free-basis 及其原 certificate/metadata，核 $\beta_{72}=e_{73}/\tau$、全部 $\epsilon$ 和原基身份。规格引用不代文件字节。
3. R853 实际三个共轭的准确坐标、function-field DAG、certificate、source audit、stage manifest 与 metadata，逐 SHA 绑定 R805/R806 的同一原来源。
4. 本篇及 R802/R805/R806/R813/R853/FM 的固定证明身份。

R806 已成源码没有另行完成的 $\chi$ 或特征零 Krylov 矩阵可直接消费；本入口不会把一个仅列为规格的文件当作已取源。完整已成 W34 的实际字节已有独立 IO 缓存，后继应直接续载。

核心保存完整原 W 的系数引用、矩阵约定、删行/删列、两个度数界和真实非零分母证明依赖。若保留未展开 determinant 节点，成功字段只称 `exact_original_semilinear_fraction_DAG_constructed`，并明确 `expanded_bivariate_cofactors_computed=false`、`expanded_power_basis_coordinates_computed=false`、`actual_RR_kernel_computed=false`。任何后继实际展开应在同一源身份上增加新阶段；不能将旧表达式构造的成功冒称新算术已完成。

所有新数学仅在本公开仓库 Actions；本篇没有运行新矩阵、域运算或微分求值。

### 原来源链接与关键身份

- [R802](../results/R802-original-semilinear-parity-and-degree-seven-relations.md)，SHA256 `2e8a3b19685d6f607d4f1b000c98e34a98370aa54a98ffeeb2c59e892ba393ca`。
- [R805](../results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)，原证明 SHA256 `b48d9f8dd5d8d1a89aa2574ab7f9ee014b83ca21baf41694252b9c53993571e8`。
- [R806 实际结果](../results/R806-certified-original-primitive-multiplication.md)，SHA256 `d4d6dc9391ea7a5f663fe53a5ae55095a43934cfe31c3a153abfaaa72b139fcc`；原 W index 为 10847B / `63b38d14dbeb4b504619db65f56c151146885173b8cef253dfba3bebc76cd2dd`。
- [R813 实际结果](../results/R813-certified-original-Wronskian-normal-vectors.md)，SHA256 `a2f41569eb7c5017989623b45148e483d9f176a796d3aa423fa9e71d9e9b7738`。
- [R853 实际结果](../results/R853-certified-original-three-V1-conjugates-and-semilinear-generators.md)，SHA256 `f9635345f5f1ab4a3911fc34d8a5f303b73205486faef1ab3b06fe79f8087333`；原准确三列 stage 为 10604B / `4b397fcb470302666fcc6b3cb33366fd0d110b36956f064f59c45130b15db616`。
- [FM](2026-11-16-original-Y-finite-RR-matrices-and-source-leaves.md)，SHA256 `a5d65aa4a841c77eb7d29ccf98e96b01e60691ffdf1d763115487889a1695fbe`。
