# R103：实际诱导度量下的准确局部曲率门

日期：2026-11-14。状态：**已证明的逐点等价条件及参数导数**。本结果只处理局部主曲率；不把它与镜像点对筛合并后冒作全曲面 reach 证书。没有评价新的研究候选，也没有运行新的几何计算。

当前 dense actual 的同参数细网格给出最大绝对主曲率约 73.10，见[实际记录](../notes/dense-mirror-minimax-first-actual-result-20261114.md)。[R66](R66-core-flat-cap-two-normal-reach-height-gate.md)已区分 README 的必要绝对 reach 门与当前较强设计值。本稿给后续实现一个不取主曲率根式、不把近似度量偷换成目标度量的准确接口。

## 1. 必须使用曲面自己的第一基本形式

设 X(s,θ) 是 C² 正则曲面片，a(s)>0 为一个已固定的正尺度。当前应用中 a 来自同一个完整目标度量

$$g=ds^2+a(s)^2d\theta^2.$$

以下推导不假定 X 已等距，也不把数值计算中的切向模长强制设为 1。定义

$$
A=X_s,\qquad T=X_\theta/a,\qquad
U=X_{ss},\qquad V=X_{s\theta}/a,\qquad W=X_{\theta\theta}/a^2.
\tag{1}
$$

在坐标基 ∂s、a⁻¹∂θ 中，真实第一基本形式为

$$
I=\begin{pmatrix}E&F\\F&G\end{pmatrix},
\qquad E=A\cdot A,\quad F=A\cdot T,\quad G=T\cdot T.
\tag{2}
$$

置

$$
w=A\times T,\qquad q=|w|>0,\qquad n=w/q.
\tag{3}
$$

拉格朗日恒等式给

$$\det I=EG-F^2=q^2>0,$$

所以 I 正定。定义未除以 q 的第二形式

$$
K=\begin{pmatrix}e&f\\f&k\end{pmatrix},
\qquad e=w\cdot U,\quad f=w\cdot V,\quad k=w\cdot W.
\tag{4}
$$

式 (4) 的 k 仅是当前曲面的 jet 分量，不是先前零矩阵路径中的 frame 参数。真实第二基本形式在同一基中恰为

$$II=K/q.\tag{5}$$

式 (1) 不需要给 V、W 加目标联络修正：第二基本形式取法向分量，坐标二阶导数中任何切向联络项都被 n 消去。这不授权在未等距时使用目标 g 的形算子。

## 2. 两个半正定矩阵等价于双侧主曲率界

给定 τ>0。真实主曲率是对称矩阵

$$S=I^{-1/2}II I^{-1/2}$$

的两个特征值。于是逐点严格等价：

$$
\max(|\kappa_1|,|\kappa_2|)\le\tau^{-1}
\quad\Longleftrightarrow\quad
I-\tau II\succeq0,\quad I+\tau II\succeq0.
\tag{6}
$$

证明只需把右侧两个矩阵分别用 I⁻¹ᐟ² 合同变换，得到单位矩阵减去、加上 τS。q 为正，因此也等价于

$$
H_\pm=qI\pm\tau K\succeq0.
\tag{7}
$$

这保留主曲率的正负两个方向。只检查高斯曲率乘积，或者只限制一个有向法曲率，都不足以给 (6)。

对于任意实对称二阶矩阵，半正定准确等价于迹和行列式同时非负。故 (7) 可以用四个光滑标量行表示：

$$
\begin{aligned}
r_\pm&=q(E+G)\pm\tau(e+k)\ge0,\\
d_\pm&=(qE\pm\tau e)(qG\pm\tau k)
       -(qF\pm\tau f)^2\ge0.
\end{aligned}
\tag{8}
$$

半正定等价式没有遗漏迹为零的边界：若两个实特征值的和为零而积非负，则两者均为零。

也可使用每个 H± 的两个对角元及行列式，共六行。它与 (8) 数学等价，浮点缩放与活跃集可能不同；实际选哪个版本，应作为新求解配置明确记录。

## 3. 完全多项式的两行版本

当希望避免平方根时，还有另一个准确等价矩阵：

$$
B=q^4I-\tau^2K\,\operatorname{adj}(I)\,K.
\tag{9}
$$

在 q>0 的正则前提下，

$$
\boxed{\ \max_i|\kappa_i|\le\tau^{-1}
\quad\Longleftrightarrow\quad B\succeq0.\ }
\tag{10}
$$

证明如下。S 对称，所有特征值的绝对值不超过 τ⁻¹，恰等价于

$$I_2-\tau^2S^2\succeq0.$$

用 I¹ᐟ² 合同变换得到

$$I-\tau^2II I^{-1}II\succeq0.$$

再由 II=K/q、I⁻¹=adj(I)/q²，乘以正数 q⁴ 即得 (9)。因此 (9) 的迹与行列式两行非负已经足够。

这里 q⁴=(EG−F²)²，而 K、I 的分量都由位置两阶 jet 的点积与叉积组成，所以 (9) 是这些 jet 的多项式。它不需要单位法向或主曲率根式。但是高次乘积可能改变数值条件，不能仅凭行数更少就宣布求解更稳。当前接口优先保留 (8) 及直接主曲率诊断，(9) 是严格备选表达。

## 4. 保持同一固定 a 的完整参数方向导数

固定 τ、a，令 δ 表示任一物理参数方向。a 不随本轮物理系数变化，因此

$$
\delta A=\delta X_s,\quad
\delta T=\delta X_\theta/a,\quad
\delta U=\delta X_{ss},\quad
\delta V=\delta X_{s\theta}/a,\quad
\delta W=\delta X_{\theta\theta}/a^2.
\tag{11}
$$

若以后另建改变 a 的设计，必须补相应商法则项；该设计不是这里的同 g 续求。

首先

$$
\begin{aligned}
\delta w&=\delta A\times T+A\times\delta T,\\
\delta q&=(w\cdot\delta w)/q,\\
\delta E&=2A\cdot\delta A,\\
\delta F&=\delta A\cdot T+A\cdot\delta T,\\
\delta G&=2T\cdot\delta T.
\end{aligned}
\tag{12}
$$

完整第二形式的导数为

$$
\begin{aligned}
\delta e&=\delta w\cdot U+w\cdot\delta U,\\
\delta f&=\delta w\cdot V+w\cdot\delta V,\\
\delta k&=\delta w\cdot W+w\cdot\delta W.
\end{aligned}
\tag{13}
$$

不能省去 (13) 中当前法向的变化。记 H± 的三个分量为 h11、h12、h22，则

$$
\delta H_\pm=(\delta q)I+q\,\delta I\pm\tau\,\delta K.
\tag{14}
$$

从而四行的完整方向导数是

$$
\begin{aligned}
\delta r_\pm&=\delta h_{11}+\delta h_{22},\\
\delta d_\pm&=h_{22}\delta h_{11}
              +h_{11}\delta h_{22}-2h_{12}\delta h_{12}.
\end{aligned}
\tag{15}
$$

对多项式版本，令 Δ=det I=q²，则

$$
\delta\Delta=G\,\delta E+E\,\delta G-2F\,\delta F,
\qquad
\delta\operatorname{adj}(I)=
\begin{pmatrix}\delta G&-\delta F\\-\delta F&\delta E\end{pmatrix}.
$$

因此

$$
\begin{aligned}
\delta B={}&2\Delta\,\delta\Delta\,I+\Delta^2\delta I\\
&-\tau^2\big[
(\delta K)\operatorname{adj}(I)K
 +K\,\delta\operatorname{adj}(I)\,K
 +K\operatorname{adj}(I)(\delta K)\big].
\end{aligned}
\tag{16}
$$

再对 B 的迹和行列式用 (15) 即可。所有参数列共用同一份当前几何；辅助 delta 不属于物理参数，因此这些曲率行对 epigraph 的辅助 delta 导数准确为零。

基础位置构造已有完整 two-jet 参数接口；将它用于本轮完整带 entry/Q 的物理族时，仍须保持所有附加列的二阶导数。当前 dense 第一阶缓存并未保留全部这些数组。新增曲率约束必须明确请求真实二阶 jet Jacobian，并按实际行/列批次控制内存；不能把已有第一阶缓存当成足够数据。

## 5. 两个不能删除的前提

### 5.1 正则性必须另查

若 A 与 T 共线，则 q=0，K=0，H± 与 B 都可以为零，所有半正定行会通过，但曲面并非浸入。这不是 (6)–(10) 的反例，而是其正则前提被删除造成的错误。

实际检查必须独立验证 q 大于声明的正下界，并保存该最小值。数值有限节点的 q 下界仍不是连续正则性证明。

### 5.2 未等距时不能换用目标度量

给一个仅用于纸面说明的局部图

$$X(s,\theta)=(s/2,\theta,s^2/(4\tau)),\qquad a=1.$$

在原点，真实 I=diag(1/4,1)、II=diag(1/(2τ),0)，主曲率为 2/τ 与 0，违反目标界。若误用目标单位矩阵计算形算子，则会读成 1/(2τ) 与 0，错误通过。

所以当前最大度量误差尚约 0.268 时，以目标 g 直接衡量第二形式尤其不能替代 (6)。即使最终近等距误差很小，若要作准确门，也应继续使用实际 I。

## 6. 与 reach 目标的准确关系

若完整闭 C² 嵌入曲面有 reach 至少 τ，则所有点必须满足 (6)。可直接从 R66 已核的法弦必要不等式取近对角极限：沿单位切向 v 的曲面曲线，

$$
X(t)-X(0)=tv+\tfrac12t^2X''(0)+o(t^2),
$$

分子为 t²+o(t²)，法向内积为 t² II(v,v)/2+o(t²)。当法曲率非零，法弦半径极限为 1/|II(v,v)|。取主方向即得必要界；零法曲率不加限制。

准确核心含直径为 2 的点对，故 README 的 reach≥0.03D 至少要求所有绝对主曲率不超过 50/3。当前设计 τ=61/1000 则对应更强的 1000/61。两者不能混作同一用户门。

反向不成立：局部曲率界没有比较远隔材料点的空间接近。即使全部点满足 (6)，仍须支付跨片点对、接缝、全时嵌入和完整法弦不等式。现有镜像必要筛只覆盖指定同参数点对；其通过也不补齐缺失的其它点对。

本稿提供后续求解所需的准确局部曲率约束与导数，没有宣称当前数值状态通过，也没有将一份静态采样推广到整条 C² 连续等距族。
