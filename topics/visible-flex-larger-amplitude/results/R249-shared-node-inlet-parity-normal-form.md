# R249：共享节点 Hermite 入口奇偶规范形及同一度量下的修补代价

日期：2026-11-14。状态：**完整条件定理与可复用构造**；此文不是一次新的 full-DN 数值接受，也不声称尚未读出的新大核闭面已通过度量、曲率、reach 或幅度门。

相关结果：[R248](R248-finite-C2-phase-family-and-global-reductions.md) 给出反射拼接的三项精确奇偶条件及物理相位族的归约。本结果把其中的入口条件落实为一个有限、局部、可精确描述的构造，并给出必须另付的几何代价。实现为 [`geometry_20261114_inlet_parity_normal_form.py`](../computations/geometry_20261114_inlet_parity_normal_form.py)。

## 1. 输入对象与精确有限场的含义

取物理径向节点

\[
0=s_0<s_1<\cdots<s_J=L,
\]

以及各节点的完整状态值、一阶和二阶径向 jet

\[
Y_j,V_j,A_j\in\mathbb R^{3M+2}.
\]

状态顺序固定为

\[
(r_0,\ldots,r_M,\ t_1,\ldots,t_M,\ z_0,\ldots,z_M).
\]

所有这些保存的 binary64 数在本节定义中均解释为精确有理数。每个相邻节点区间上的状态函数是匹配两端这三阶 jet 的**唯一实系数五次 Hermite 多项式**；相邻区间共享同一份节点 jet。记其整体为 \(P(s)\)。因此 \(P\in C^2([0,L])\)，无需假设这些数据精确满足原 Frenet 方程。

由状态构造完整空间函数的线性算子为

\[
\begin{aligned}
R_v(\phi)&=\sum_{m=0}^{M}r_m\cos(2m\phi),\\
T_v(\phi)&=\sum_{m=1}^{M}t_m\sin(2m\phi),\\
Z_v(\phi)&=\sum_{m=0}^{M}z_m\cos(2m\phi),\\
\mathcal W_\phi(v)&=
\bigl(R_v\cos\phi-T_v\sin\phi,
      R_v\sin\phi+T_v\cos\phi,Z_v\bigr).
\end{aligned}
\]

材料角沿用同一个完整核心 \(c_1,\ldots,c_M\)：

\[
\theta=\Phi(\phi)
=\phi+\sum_{m=1}^M\frac{(1-4m^2)c_m}{2m}\sin(2m\phi),
\qquad
\rho(\phi)=\Phi'(\phi)
=1+\sum_{m=1}^M(1-4m^2)c_m\cos(2m\phi).
\]

假设已有一个真实的全角正下界 \(\rho\ge\rho_*>0\)。于是 \(\Phi\) 是圆上的光滑微分同胚。定义

\[
U(s,\theta)=\mathcal W_{\Phi^{-1}(\theta)}(P(s)).
\]

其径向正则性为 \(C^2\)，角向解析。源码沿用原 SavedPrefix 的完整核心及 R237 下界，没有删高模，也没有改变材料角。

**表示约定。** 上述共享节点实多项式是本文的精确有限场。实现用 longdouble 重建系数、用浮点计算三角函数和材料角逆，是这个定义的数值读出。一个分别舍入过系数且在节点强行返回保存值的可执行函数，不能仅因端点样值相等就被宣称字面上 \(C^2\)。实现明确分别保存 `exact_reflection_inlet_C2_in_this_normal_form` 与 `literal_rounded_polynomial_C2_identity_certified=False`。本文的有理恒等式和连续差界针对前述精确规范形；浮点求值误差仍单独说明。

## 2. 三块共享节点投影

只修改第零节点如下三个互不混淆的分量块：

\[
\begin{array}{c|c}
\text{节点 jet}&\text{修改}\hline
Y_0&z_0,\ldots,z_M\ \text{全部设为 }0\\
V_0&r_0,\ldots,r_M,t_1,\ldots,t_M\ \text{全部设为 }0\\
A_0&z_0,\ldots,z_M\ \text{全部设为 }0.
\end{array}
\]

其他第零节点分量与所有 \(j\ge1\) 的三阶节点 jet 完全不变。用这些新的共享数据定义唯一 Hermite 场 \(\widetilde P\)，并相应定义 \(\widetilde U\)。

令 \(h=s_1\)，三个状态变化为 \(d_0,d_1,d_2\)。则在 \(0\le s\le h\)，置 \(t=s/h\)，有

\[
\widetilde P-P
=H_0(t)d_0+hH_1(t)d_1+h^2H_2(t)d_2, \tag{1}
\]

其中

\[
\begin{aligned}
H_0(t)&=1-10t^3+15t^4-6t^5,\\
H_1(t)&=t-6t^3+8t^4-3t^5,\\
H_2(t)&=(t^2-3t^3+3t^4-t^5)/2.
\end{aligned}
\]

对 \(s\ge h\)，变化为零。

### 命题 2.1：局部性与共享 \(C^2\) 性

\(\widetilde P\in C^2([0,L])\)，修补只支撑在第一物理单元 \([0,h]\)。在 \(h\) 处，变化的零、一、二阶径向 jet 都严格为零。因此 \(\widetilde U-U\) 的这些径向 jet 及其任意阶角向导数也在 \(h\) 处为零。

**证明。** 直接代入可得

\[
H_k^{(i)}(0)=\delta_{ik},\qquad
H_k^{(i)}(1)=0\quad(0\le i,k\le2).
\]

式 (1) 中的 \(h^k\) 恰好把单位区间导数还原为所需物理 jet \(d_k\)。左右六项条件唯一确定次数至多五的多项式，故式 (1) 正是新旧 Hermite 多项式之差。在其他区间两端数据未改，唯一性使整个多项式未改。材料角与 \(s\) 无关，\(\mathcal W\) 对状态线性且角向解析，因此上述零恒等式可任意角向微分。证毕。

实现使用精确 `Fraction` 从实际三个变化向量重建式 (1)，逐状态分量核对左右六个端点 jet；当状态维数为 \(n=3M+2\) 时核对 \(6n\) 条有理恒等式。它还检查所有其他节点数据相等、重建的其他数值区间系数逐项相等。这两个检查各有自己的含义，后者不能代替前者的实多项式论证。

## 3. 精确反射入口

取 \(J=\operatorname{diag}(1,1,-1)\)，在有符号坐标 \(u\) 上拼接

\[
F(u,\theta)=
\begin{cases}
\widetilde U(u,\theta),&u\ge0,\\
J\widetilde U(-u,\theta),&u\le0.
\end{cases} \tag{2}
\]

### 定理 3.1：式 (2) 的入口是 \(C^2\)

对每个材料角，严格有

\[
\widetilde U_z(0,\theta)=0,\qquad
(\widetilde U_s)_{xy}(0,\theta)=0,\qquad
(\widetilde U_{ss})_z(0,\theta)=0. \tag{3}
\]

式 (2) 因而在整个入口圆上为 \(C^2\)。若 \(\widetilde U\) 在入口是浸入，则此反射延拓在该圆附近也是浸入。

**证明。** 第一个投影令完整高度 Fourier 函数恒为零，第二个令完整水平一阶径向向量恒为零，第三个令完整垂直二阶径向函数恒为零；从 \(\phi\) 换到同一 \(\theta\) 不改变恒等为零的事实，故 (3) 成立。

式 (2) 左右的函数值分别为 \(J\widetilde U\) 与 \(\widetilde U\)，一阶径向导数为 \(-J\widetilde U_s\) 与 \(\widetilde U_s\)，二阶为 \(J\widetilde U_{ss}\) 与 \(\widetilde U_{ss}\)。对应相等正是 (3)。对恒等式再作一或二次角向求导给出所有总阶数不超过二的其他匹配条件，包括混合导数。各侧本来具有连续二阶导数，故拼接为 \(C^2\)。浸入性是连续一阶微分的开条件，得最后一句。证毕。

当前闭组装对整个 prefix 只作一次平面 proper SE(2) 配准，形式为

\[
(x,y,z)\longmapsto\bigl(((x,y)-b)Q,z\bigr),\quad Q\in SO(2).
\]

它不改变任何高度，并与 \(J\) 交换。因此 (3) 在这一次配准后仍成立，反射平面仍是 **\(z=0\)**。尾部为了匹配 prefix 切口材料均值而加的绝对高度常数只作用在尾/帽构造上，不是对整个 prefix 再作一次高度平移。

若另一构造确实统一把全部 prefix 平移至反射平面 \(z=h_c\)，第一条件必须相应改为 \(U_z=h_c\)，并以该平面为中心反射；不能继续套用式 (2) 而遗漏这个变化。本实现没有执行这种另一次平移。

此定理只付清入口。尾节点、collar、外切口、固定帽的自身 \(C^2\) 定义仍按各自构造支付，不能用本定理代替。相位族的全 \(t\) 连续性在这些其余条件齐备后可直接使用 R248；这里不增加 \(C^3\) 假设。

## 4. 哪些实际输入严格保留

由于 \(s_J\ge h\)，命题 2.1 给出：

1. 实际末端的完整状态及零、一、二阶物理径向 jet 完全保留，连同任意角向导数，故切口的九 jet 未变。
2. 完整核心 \(c\)、材料角 \(\Phi\)、完整固定标量函数 \(a(s;p_*)\) 与全部三个冻结设计参数均不变；v4 的空 active 参数向量也不会被填成三个伪参数。
3. 切口完整材料均值
   \[
   \overline Z=z_0+\frac12\sum_{m=1}^M z_m(1-4m^2)c_m
   \]
   及它的前两阶径向导数不变。完整 \(z_0\) 始终只出现一次。
4. 原 actual-tail 的输入 \(H\)、响应与配置哈希、所有非线性 DN 审计数据仍为同一份。这里没有产生新尾解，也没有重解原 DN 系统。
5. 用切口整函数拟合的一次 proper SE(2) 的输入未变。外切口全角 Hermite 修补、尾部绝对高度配准、帽高所用的切口数据也未变。

这些保留项**不**表示修补后的 prefix 仍是原离散 BVP 的解。唯一被接受的 checkpoint 仍是原始输入文件；源码不编辑其 `success/status`，不输出一个伪造的新 accepted checkpoint。输出明确标记它是从该输入定义的后处理有限场。新首单元的度量、曲率以及必要的全局几何检查须针对它自身完成。

## 5. 连续九 jet 的显式修补预算

### 5.1 单位区间 Bernstein 界

三个 \(H_k\) 的五次 Bernstein 控制系数分别为

\[
(1,1,1,0,0,0),\quad
(0,1/5,2/5,0,0,0),\quad
(0,0,1/20,0,0,0).
\]

Bernstein 基非负且和为一，因此多项式的绝对值不超过控制系数绝对值最大值。一次导数的控制系数是原系数的五倍一阶差，二次导数是二十倍二阶差。故对 \(0\le t\le1\)，有

\[
|H_k^{(i)}(t)|\le B_{ik},\qquad
B=\begin{pmatrix}
1&2/5&1/20\\
5&2&1/4\\
20&12&2
\end{pmatrix}. \tag{4}
\]

### 5.2 完整旋转坐标的角向界

对状态 \(v\) 定义

\[
L_j(v)=\sum_{m=0}^M(2m+1)^j|r_m|
       +\sum_{m=1}^M(2m+1)^j|t_m|
       +\sum_{m=0}^M(2m)^j|z_m|,
\quad j=0,1,2, \tag{5}
\]

其中 \(0^0=1\)。那么

\[
\sup_\phi|\partial_\phi^j\mathcal W_\phi(v)|\le L_j(v). \tag{6}
\]

**证明。** 每个水平径向或切向模与旋转框架相乘后分成频率 \(2m+1\) 与 \(1-2m\) 的两个复指数项，各系数绝对值为原模的一半。第 \(j\) 阶导数的两项模长之和不超过 \((2m+1)^j\) 倍原模绝对值。高度频率为 \(2m\)。逐项应用三角不等式即可。特别是不能把水平模的频率误写成只有 \(2m\)，遗漏转动坐标框架的一阶贡献。证毕。

由 (1)、(4)、(6)，对 \(i,j\in\{0,1,2\}\) 得到

\[
b_{ij}:=\sum_{k=0}^2h^{k-i}B_{ik}L_j(d_k),
\qquad
\sup_{s,\phi}|\partial_s^i\partial_\phi^j(\widetilde U-U)|\le b_{ij}. \tag{7}
\]

式中暂以 \(\phi\) 表示未拉回的空间函数。此界覆盖整个首单元；其他单元差为零。

### 5.3 同一个材料角的拉回

另记

\[
R_1=\sum_{m=1}^M2m(4m^2-1)|c_m|,
\quad |\rho_\phi|\le R_1.
\]

材料逆满足

\[
\phi_\theta=\rho^{-1},\qquad
\phi_{\theta\theta}=-\rho_\phi\rho^{-3},\qquad
\phi_s=0.
\]

故所需的九个材料 jet 差分别满足

\[
e_{i0}=b_{i0},\qquad
e_{i1}=b_{i1}/\rho_*,\qquad
e_{i2}=b_{i2}/\rho_*^2+b_{i1}R_1/\rho_*^3. \tag{8}
\]

这些界在统一 SE(2)、空间反射及 R248 的相位搬移下保持不变。实现从实际 binary64 变化向量、节点宽度和完整核心用有理数计算 (7)、(8)，同时保存精确字符串与向上舍入的便读小数。其 `continuous_bounds_for` 明确限定为两个共享节点实 Hermite 规范形之差，不把三角函数或逆角求值误差默认为零。

## 6. 同一固定度量的 operator 误差代价

固定参考度量为

\[
g_0=ds^2+a(s)^2d\theta^2,\quad a(s)\ge a_*>0.
\]

令旧场归一化切向矩阵 \(T=(U_s,U_\theta/a)\)，新场为 \(\widetilde T=T+E\)。用 (8) 设

\[
\epsilon^2=e_{10}^2+(e_{01}/a_*)^2.
\]

则 \(\|E\|_{\rm op}\le\|E\|_F\le\epsilon\)。如果旧场在整个首单元已有

\[
\|T^TT-I\|_{\rm op}\le\eta,
\]

则 \(\|T\|_{\rm op}\le\sqrt{1+\eta}\)，并且

\[
\boxed{\quad
\|\widetilde T^T\widetilde T-I\|_{\rm op}
\le\eta+2\sqrt{1+\eta}\,\epsilon+\epsilon^2.
\quad} \tag{9}
\]

**证明。** 展开 Gram 差为
\(T^TT-I+T^TE+E^TT+E^TE\)，对四项分别取算子范数，即得 (9)。这没有更换 \(a\) 或 \(g_0\)。证毕。

若 \(\eta<1\) 且 \(\epsilon<\sqrt{1-\eta}\)，还得到

\[
\sigma_{\min}(\widetilde T)
\ge\sqrt{1-\eta}-\epsilon>0, \tag{10}
\]

从而首单元浸入性也有定量保证。对整条 prefix，其余区间的旧误差不变，只需与新首单元界取最大值。

这里的 \(\eta\) 是真实的归一化 Gram **operator** 界，不能直接用三个分量的最大值代替。数值读出直接计算

\[
\frac{|e+d|+\sqrt{(e-d)^2+4f^2}}2,
\quad
(e,f,d)=\bigl(|U_s|^2-1,\langle U_s,U_\theta\rangle/a,|U_\theta|^2/a^2-1\bigr).
\]

旧场的有限样点最大值本身不建立 (9) 的连续前提。源码的可选 `--old-metric-bound` 只计算带有外部前提标记的条件上界；不把它设置成一个额外的强制完成门。正常数值通路同时输出相同网格上的修补前后真实 operator 与分量误差，明确仍是样点。

### 首单元 \(a_*\) 的一个小型精确来源

当前完整标量的第一个物理单元若位于原保存标量前缀内、且在全部控制支撑左端之前，则所有设计 bump 在该单元上恒为零。对原标量源区间长度 \(H\)，左右精确二阶 jet 为 \((a,a',a'')\)、\((b,b',b'')\)，其五次 Bernstein 控制系数是

\[
a,\quad a+Ha'/5,\quad a+2Ha'/5+H^2a''/20,
\quad b-2Hb'/5+H^2b''/20,\quad b-Hb'/5,\quad b.
\]

取所有与第一物理单元相交的原源区间的这些数的最小值，就得到合法下界，即使物理单元只占某个源区间的一部分也成立。第一个源节点的 jet 必须按原 `exact_original_jet` 公式重算，不能误用被该公式替换掉的打印值。实现正是如此；若前提不符或凸包下界不正，它只报告该自动界不可用，不重拟合标量函数。

## 7. 曲率代价的条件上界与实际读出

本节给出可组合的连续不等式，并不把数值抽样自动提升为这些前提。设旧场在首单元还满足真实主曲率绝对值上界 \(K\)，以及完整归一化二阶空间 jet 的界

\[
\left(|U_{ss}|^2+2|U_{s\theta}/a|^2+|U_{\theta\theta}/a^2|^2\right)^{1/2}\le H_*.
\]

令

\[
\begin{aligned}
x&=e_{10},&y&=e_{01}/a_*,\\
\gamma&=\sqrt{1+\eta}(x+y)+xy,&
\nu&=\min\{2,2\gamma/(1-\eta)\},\\
\Delta_H&=\sqrt{e_{20}^2+2(e_{11}/a_*)^2+(e_{02}/a_*^2)^2},&
\ell&=\sqrt{1-\eta}-\epsilon.
\end{aligned}
\]

若 \(\eta<1\) 且 \(\ell>0\)，则

\[
\boxed{\quad
\widetilde K\le
\frac{(1+\eta)K+\Delta_H+\nu H_*}{\ell^2}.
\quad} \tag{11}
\]

**证明。** 旧归一化切向两列的叉积模长至少为 \(1-\eta\)。新旧叉积之差是两项一次变化与一项二次变化之和，故其模长不超过 \(\gamma\)。对非零向量，单位方向之差至多为两倍向量差除以旧模长，也至多为二，故新旧单位法向差不超过 \(\nu\)。

令 \(G=T^TT\)，\(B\) 为在同一归一化坐标基中的第二基本形式矩阵。旧主曲率界意味着
\(\|G^{-1/2}BG^{-1/2}\|_{\rm op}\le K\)，所以
\(\|B\|_{\rm op}\le(1+\eta)K\)。新旧第二基本形式之差由新法向作用于二阶 jet 变化，加上法向变化作用于旧二阶 jet 构成；矩阵 Frobenius 范数至多 \(\Delta_H+\nu H_*\)。因此新第二基本形式的算子范数至多为 (11) 分子。由 (10)，新 Gram 最小特征值至少为 \(\ell^2\)，再次归一化即得 (11)。证毕。

该式可能保守；不要求为了使用本构造而人为建立一个新的全区间机器证书。实际公开 Actions 消费者会从修补前后的**同一个六 jet 定义**计算首单元的实际 Gram 与主曲率，并继续输出全 prefix/闭面所需数值读出。若后续使用连续封套，则其来源与假设须像 R241 一样列明。

从 (7) 可见，位置残差的二阶代价带 \(h^{-2}\)，一阶残差的二阶代价带 \(h^{-1}\)。因此“小的入口残差”并不自动保证“小的曲率变化”；细化时也不能只看原 boundary tolerance 而忽略单元宽度。另一方面，课题的同一度量精化标准并没有要求所有六 jet 的相邻差都达到机器精度；本结果不额外添加这样的门。必须实际核对课题所要求的同一 \(g\) 下度量误差改善，以及用于 reach 的有余量曲率和空间几何。

## 8. 计算接口、出处与当前边界

`normalize_inlet(saved)` 接受当前完整 SavedPrefix API，保留 `saved.rec` 原样，另保存 `saved.original_quintic`，替换有限读出的 `quintic/sol`，并在

```
saved.definition["inlet_normalization"]
```

中固定记录源 SHA、原输入 SHA、原/新三份共享节点数组哈希、实际支撑 \([0,h]\)、精确修补恒等式及连续九 jet 差界。`read_saved(checkpoint, normalize=True)` 严格按 v3/v4 的真实 schema 选择原 reader；设 `normalize=False` 得到原字段，不能拿它生成的网格悄悄配给规范化后的覆盖器。

三个公开 Actions 入口分别是：

- `audit`：同一实际 checkpoint 的首单元前后 operator、分量误差、主曲率、奇偶残差和六 jet 差，加有理 Hermite 代价；
- `readout`：复用原完整材料角读出，但构造器明确换成上述规范形；
- `closed`：复用同一实际尾响应、完整切口九 jet 与原闭组装，同时把规范形身份写入 plan/assembly。

先完成原 full-DN 求解，再对同一真实成功输出运行这些接口即可；无需为了入口规范化重新求一次 DN 解。所有新度量/曲率/空间覆盖结果必须绑定同一个规范形身份与同一新网格。

本文完成的是一个可执行有限场定义及其精确入口定理、连续代价公式。写本文时没有在本地启动新 Frenet/BVP/尾/几何数值计算，也没有把尚未返回的公开 Actions 结果预填成成功。反射入口之外的完整闭面嵌入、固定帽识别、真实整面 Hausdorff 幅度、所有相位 reach 和实际同一度量精化，仍必须由相应实际数据与既有定理分别支付。
