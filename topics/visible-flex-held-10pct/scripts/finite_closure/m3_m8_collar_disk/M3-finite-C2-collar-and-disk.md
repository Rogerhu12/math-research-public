# 固定 m3 M8 状态的有限 C² 尾、圆领与平盘

会话：Astra-visible-held10 / literature_mechanisms。日期：2026-11-18 UTC。

## 已完成的对象与范围

已把实际接受的固定度量 M8 状态转换为一个明确的有限 C² 尾，并用精确五次 Hermite 圆领接到半径约 .05 的平盘。尾端不再是“最后一层很小，所以忽略”的定义。圆领和盘的完整 Cartesian 二阶接合是定义上的等式。

输入为 `m3_smallcut_fast45_q02_fixed_m8_breaks/seed_tail_0004.json.gz`，SHA256
`12754098ba6cffc0abb5f0c327c7a376cac826ea8ab820b793ec5ad9b958c4f2`；相配的 prefix checkpoint SHA256 为
`2efcc8e2f3edd765760266e9d1b83f0ee2cba1bc0b2fdb04e8b5427d645525a5`。
实际核心振幅为 (q=0.020001225073149356)，冻结的前缀参数为 (delta=0.06105607686781097)。本稿没有重解 BVP。

结果分成三种证据，不能混用：

1. 有限尾、圆领、盘有明确的 C² 函数定义；整个 capped tail 仍有一个外边界。
2. 圆领与盘的下列界由完整区间背景估计及精确有理运算得到，覆盖每一点：(X\cdot n>0.8)、(|X|<0.817)、圆领 (|\kappa_i|<8.002)、相对度量误差 (<1.36\times10^{-29})。盘完全平坦。
3. 外侧有限尾当前只有采样审核，最大相对度量误差 (3.59745\times10^{-8})、最大曲率 (8.04068)。这些数不是它的连续认证。共同前缀二阶接缝、前缀镜像中心、全闭面嵌入与 reach 仍须另行完成。

因此本稿没有给出整个闭球面的完成结论，也没有把有限远端 Robin 状态提升成精确无限非线性解。

## 1. 固定旋转背景及可复用性

物理背景取原 `closing_weighted_tail.mjs` / `closing_recalibrated_tail.mjs`，主要参数是

| 参数 | 固定值 |
|---|---:|
| 外切半径、斜率、径向宽度 | .3、.08、.25 |
| curvatureBound、orientation、protectCell | 8、+1、160 |
| delta0、R、指数 a、etaPower、etaRatioAtN0 | .006、64、11/4、3/2、.05 |
| prefixR / prefixReturnStart / prefixEnd | 2 / 8 / 15 |
| slopeCap、capTransition、capMode | .02、2、cut-preserving |
| cell 0 两脉冲 cap / valley cap | .4、.02 / .1 |
| cell 0 五级正 weight | 1、.5、3、.05、1 |
| 最初六个 valleyControls | 3.125、2.8125、4.0625、5、5.25、4.0625 |

其余 valleyControls 为零，其余 weights 为 1，不启用 flatOuterThroughCell 或 rejoin。具体 binary64 字面值由源码和 `physical_background.json` 冻结。有限校准常数是原 512-step 校准算法生成的固定 binary 值；本次验证得到它们全部在 ([1.01545,1.49512])。不随模数、振幅、相位或网格变化重新设计这些物理参数。

角模数不出现在旋转背景公式内，所以相同物理参数的 m4 可复用本节高度与曲率界。它不能复用 m3 的非旋转尾数组或非线性状态。

令 (a=r_{\rm cuff})，这里 binary 值为 (0.04999999999999999>1/25)。设

\[
\delta_n=d_0 2^{-n},\quad c_n=c_0 2^{-n/2},\quad
\eta_n=d_0c_0 2^{-3n/2},\quad
Y_0=6d_0+\frac{6d_0c_0}{1-2^{-3/2}}.
\]

原径向坐标满足 (r_o=a\exp(y/\sqrt{12}))，原外切点为 (a\exp(Y_0/\sqrt{12}))。九段 cell 的五个原始 log plateau 为

\[
\log\delta_n,\quad \log R_n,\quad
2\log\delta_n-\log\alpha_n,\quad 0,\quad
\log\delta_n+\tfrac{11}{4}\log2.
\]

四个过渡及两端 ports 长度为 (c_n\delta_n)，三个 plateau 长度为 (delta_n)。所有相邻 levels 用 (S(t)=10t^3-15t^4+6t^5) 插值。原 slope 由上述 profile、固定 epsilon 和 (r_o^{-7}) 给出；再施原源码的 cap 和有限 valley edits。定义 (w>0,E=1+w^2)。在每段参数 (x\in[0,1]) 上，精确重分配采用

\[
A=(1-\chi)j_0(r_o)_x+
\chi\frac{|w_x|}{8E^{3/2}},\qquad
B=\chi\frac{(r_o)_x}{E}\,W(x),\qquad
r_x=A+\lambda B.
\]

这里 (lambda) 是唯一的全局径向归一化常数，区别于 cell 校准根 (alpha_n)。所有实际参数 (r_x>0) 的证明见下文。使用真实积分定义

\[
\lambda=\frac{r_{\rm cut}-r_{160}-\int A}{\int B},\qquad
h(r)=\int_a^r w(t)\,dt.
\]

这是同一物理公式的精确定义；浮点工厂的积分值是其数值求值。不得把保存的 height 采样插值另行当作固定背景。

### 1.1 完整区间积分

`certify_background_integrals_v2.py` 在前 16 个九段 cells 上，每段用 64 个 dyadic 区间做完整值域包围，使用 60 位十进制 `mpmath.iv` 算术。它不是“两个 quadrature 结果之差”估计。(S'ge0)、七次 cap smoothstep 导数非负，以及 cap primitive 导数在 ([0,1]) 的事实用于端点值域；所有分支取包含性的 hull。

后续 cells 的粗界为

\[
W_n\le256\,2^{-7n/4},\qquad
H_n\le17+\frac75n.
\]

其中 (W_n) 控制 slope，(H_n) 控制四个 log jump。对 (n\ge16)，(R_n=64)、valley edits 为零、weights 为 1，恒定 cap 不增加 slope 或总变差。由 (2^{-7/4}<3/10)，尾部总变差有上界

\[
\operatorname{TV}_{\ge N}(w)
\le W_N\left[\frac{4H_N+1}{1-3/10}
+\frac{(28/5)(3/10)}{(1-3/10)^2}\right].
\]

若 (Y_N) 为原背景剩余 log 长度，令 (R_N^*=a\operatorname{expm1}(Y_N/\sqrt{12}))。那么未积分余项满足

\[
\int A\le\operatorname{TV}_{\ge N}(w)/8+R_N^*,\quad
\int B\le R_N^*,\quad
\int wA\le W_N\int A,\quad
\int wB\le W_N\int B.
\]

保护端的旧径向项也被 (R_N^*) 包含。用于 (int A,int B) 的实际有限重分配止于 n=159；把更深几何级数余项也加进上界是保守包围。

所有最终界向外舍入到 binary64，再作为精确 Fraction 保存。实际输出为

| 量 | 下界 | 上界 |
|---|---:|---:|
| (int A) | .12222662833886434 | .18892943570190635 |
| (int B) | .0006004970051405607 | .0006010704987725043 |
| (int wA) | .015205622590274836 | .024607320504153162 |
| (int wB) | .000019893820016693905 | .00002001032022849188 |
| (lambda) | 101.6029973569006 | 212.7793653712348 |
| 完整 (h(r_{\rm cut})) | .017226894332849643 | .028865103743246846 |
| cell 0 内半径 (r_1) | .1104690124031478 | .16000536548986485 |

特别是 (lambda>100) 已由积分包围支付，并非工厂浮点 `alpha>0` 断言。原 naive Horner 区间实现曾给出过宽的 (int A) 上界 .560879，没通过这个充分门；该记录保留为区间算法失败，不是几何失败。v2 只使用已知单调性收紧值域，没有改变物理背景。

### 1.2 全旋转背景曲率不超过 8

对所有普通 finite pieces，(chi=1)，因此

\[
|\kappa_r|=\frac{|w_x|}{r_xE^{3/2}}\le8.
\]

正 (lambda B) 保证在 (w_x=0) 处仍 (r_x>0)。对 (1\le n\le159)，原 cap 给 (w\le1/49)，所以

\[
|\kappa_\theta|=\frac{w}{r\sqrt E}<\frac{25}{49}<8.
\]

对于未修改的无限深源，只使用已公开适用性审计所记录的原深校准根 (alpha_n\in[1/2,2])、(n\ge80)；这是 R28 / 后续 R46 的背景根范围，不是其非线性满射命题。本稿没有重新证明那个根定理。它的参数条件 (d_0\in[1/200,1/160])、(c_0\in[1/25,1/16])、(R=64) 均被当前字面参数满足。

在 (n\ge160)，由 (|S'|_\infty=15/8)、(\sqrt{12}<7/2)，

\[
|w_r|\le
\frac{(7/2)(15/8)W_nH_n}{a\eta_n}+\frac{7W_n}{a}.
\]

在 n=160 使用 (a>1/25)、(eta_{160}\ge2^{-240}/5000)，右边为精确有理数，小于 .046030，也小于 (1/20)。后续第一项按 (2^{-1/4}H_{n+1}/H_n<1) 下降，第二项更快下降；两项均趋零。保护端 cell 159 的 first port 未激活 cap，原 (w_r=-7w/r_o) 极小；(chi\in[0,1]) 的凸组合径向公式于是也保持 (|\kappa_r|\le8)。这同时证明 (w,w_r\to0)，在正半径 (a) 处能 C² 接平盘。

cell 0 的特殊 caps 需单独支付。除最后两段外，(w\le.41) 直接由 cap 得到。倒数第二段令 (t=S(x))。原 log slope 有上界 (7/5-3t)，cap 后 log slope不超过 (-19/5)，因此 cut-preserving blend 满足

\[
\log w\le -\frac{19}{5}+\frac{26}{5}t-3t^2
\le-\frac{116}{75}<-\frac32,
\]

故该段 (w<1/4)。最后 port 的原 (w<.1)。这些 elementary bounds 及全部相关 literal 参数由 `check_background_analytic_gates.py` 的 11 项区间检查另行验证。

因此整个 cell 0 有 (w\le.41)，并由 (r\ge r_1>.110469) 得 (|\kappa_\theta|<8)。最后 port 是唯一外端混合径向区：(t=S(x))、(chi=1-t)、(j_0>1+4t)、(E<1.01)，weights 为 1。于是

\[
\frac{r_x}{(r_o)_x}
\ge t+4t^2+\frac{10000}{101}(1-t)\ge5.
\]

而该 port 的 (w_r) 源项需要的倍数至多 (7(.1)/(8(.04))=35/16<5)。故其子午曲率也不超过 8。剩余点均已被普通 (chi=1) 估计覆盖。

有限 joins 的 (w,w_r) 连续；即使 (|w_x|) 造成辅助径向速度的 cusp，(r_x>0) 且 (w_r=w_x/r_x) 连续，所需图 (h) 仍为 C²。综上，整个固定旋转背景 (|\kappa_i|\le8)。后文圆领预算保守输入 (B=8.001)，没有继承旧题的 6.001。

## 2. 实际有限 C² 尾的定义

原 exporter `db6f-tail-increment-export-v2.mjs` 用同一个状态的完整 mean height 和非均值数据重建 Cartesian jets；M8 数据以 256 个角节点投影到 73 个有限 Fourier 系数。平面复分量保留 (m\equiv1\pmod3)，高度保留 (\cos(3k\theta))。不能只提取非均值高度 H 代替这个完整 map。

径向每个区间用端点的一阶、二阶数据和物理中点一阶数据定义一个 quartic 一阶导数；位置是它从最深端开始的精确积分。相邻区间共享字面相同的一阶与二阶端点。保存的 position 列仅是这个积分的数值显示，不独立定义 map。实际共 4638 个唯一径向节点，有限 map 因而严格 C²。

`prepare_finite_tail.py` 仅把原 exporter 的 `assumedBackgroundCurvature:6.001` 改成 8.001；数值方程、径向锚点和插值规则不改。记录包含原、执行源码 SHA、实际 argv 和输出 hash。

该表示的外端半径为

\[
c=0.29999999999999993,
\]

比名义 rCut 小一个 ulp。当前尾度量采样仍在源 profile 对应半径执行，源半径与精确累计半径最大显示差为 (1.44329\times10^{-14})；这项不是已经支付的连续整尾误差。

## 3. 全二阶圆领与盘

令 (b=0.050562797778496996)、(a=0.04999999999999999)、(L=b-a=0.0005627977784970067)。同一完整刚体规范下，设 (A_j=\partial_r^jV(b,\theta))，(j=0,1,2)。定义 (t=(r-a)/L) 和

\[
p_0=10t^3-15t^4+6t^5,\quad
p_1=-4t^3+7t^4-3t^5,\quad
p_2=\tfrac12t^3-t^4+\tfrac12t^5,
\]

\[
V(r,\theta)=p_0A_0+Lp_1A_1+L^2p_2A_2
\quad(a\le r\le b),\qquad V=0\quad(r\le a).
\]

在 b 的 value、r、rr jets 完整等于外侧有限 map，在 a 三者严格为零。对角变量求导又给出所有混合二阶接口。背景 (h,h',h'') 在 a 也为零，所以这是完整 Cartesian C² 接合。

以有限 Fourier 加权绝对系数和控制 (|\cdot|_{C^2_\theta})，实际 Fraction 求和得到

\[
K=\frac{\|A_0\|_{2,\theta}}{L^2}
+\frac{\|A_1\|_{2,\theta}}{L}
+\|A_2\|_{2,\theta}
<5.346180\times10^{-27}.
\]

这里 (L\le a, LB\le1)。原已审通用 Hermite 估计（公共旧题 R15 §3）给

\[
\eta_1=\tfrac94LK,quad \eta_2=15K,
\qquad e_g\le2\eta_1+\eta_1^2,
\qquad |\kappa_i|\le\frac{B+\eta_2}{(1-\eta_1)^2}.
\]

实际 (e_g=1.353968187600509\times10^{-29}) 上界，曲率表达式严格小于 8.002。不能把其浮点显示值 8.001 误写成严格的 8.001 上界。

### 3.1 单一 mean gauge 与平盘高度

上侧采用整个 z 分量反射：

\[
X=(r e^{i\theta}+V_{xy},\ Z_{\rm cap}-h(r)-V_z).
\]

固定 M8 prefix 的切口 mean 为 (z_c=0.7859258290315051)。沿有限 C² 导数定义积分所得精确 mean (ar V_z(c)) 为一个有理数，其显示值是 (2.0209324610528992\times10^{-6})。定义

\[
Z_{\rm cap}=z_c+\bar V_z(c)+h(c).
\]

这是一个单一刚体竖向平移；没有在深节点反复重置 mean。名义 cut 与 c 之间的 h 差以 (.41(r_{\rm cut}-c)) 支付。完整区间于是给

\[
0.8031547442968158\le Z_{\rm cap}\le0.8147929537072129.
\]

在 (r\le a) 用 Cartesian 图 (X(x,y)=(x,y,Z_{\rm cap}))。轴点属于平盘内部，普通 Cartesian 坐标消除了极坐标假奇点。无限背景振荡积累的位置是正半径 cuff，不是极点。

### 3.2 支撑、尺寸及嵌入

设 (V_0=L^2K,V_1=2LK)。由上述 Hermite 多项式直接有

\[
|V|,|V_\theta|\le V_0,\quad |V_r|\le V_1.
\]

圆领完全位于 cell 0 内端以内（(b<r_1)），故 (w\le1/49)。令

\[
J_-=1-V_1-V_0/a-V_1V_0/a,\quad
J_+=1+V_1+V_0/a+V_1V_0/a,
\]

\[
N_h=(1/49+V_1)(1+V_0/a)+(V_0/a)(1+V_1).
\]

则对向上法向 (N=X_r\times X_\theta)，有 (N_z/r\ge J_->0)、(|N_{xy}|/r\le N_h)，且精确比较 (J_+^2+N_h^2<(1001/1000)^2)。另外

\[
z\ge Z_{\rm cap,lo}-L/49-V_0=:z_-,\qquad
|X_{xy}|\le b+V_0=:r_+.
\]

因此

\[
X\cdot n\ge\frac{z_-J_--r_+N_h}{1001/1000}
>0.8013100547>0.8.
\]

圆领与盘都有

\[
|X|^2\le r_+^2+(Z_{\rm cap,hi}+V_0)^2
<0.817^2,
\quad r_+<0.050563.
\]

盘的支撑恰为 (Z_{\rm cap}>.80315)。整个盘加圆领的平面投影为恒等映射加 (V_{xy})，其 Cartesian 导数算子范数不超过 (V_1+V_0/a<1)；在半径 b 的凸盘上积分此 Lipschitz 界，得到投影单射。因此这一 capped patch 自身嵌入。此论证不排除它与外侧非旋转尾或其他曲面片的交叉。

## 4. 可查询实现、复现与尚欠的全局步骤

`finite_closed_tail.py` 提供 `FiniteClosedTail.coefficients`、`perturbation_jets`、`upper_jets` 以及普通 Cartesian pole 图 `upper_disk_xy`。背景 h,w,w_r 必须来自本稿固定精确积分公式；不允许以一个未审插值代替它。

本包只保存源、物理参数、输入/输出 hash、命令和标量记录。原 70 文件 source manifest 缺少四个 collar/integrated exporter 文件；本包的 74 文件闭包已明确补齐，不依赖运行目录里偶然残留的源。所有 Fourier、checkpoint、径向流和生成数据只在 scratch 重算。

还需完成：固定 M8 prefix 自身 C² 表示与解析 core 接合；同一刚体规范下其外口与这里的有限尾字面共享完整二阶数据；付清这个修正的度量和曲率代价；连续审核外侧有限尾；然后才可合并上下两半、固定帽、全相位嵌入与 reach。M16 同物理 g 的细层正在另一个任务中求解；它尚未被本稿当作收敛证据。

出处与精确文件定位见 `R114-closure-scope.md` 和 `source_ledger.json`。新的背景区间积分、analytic gates、圆领标量界分别由 `background_interval_result.json`、`background_analytic_gates.json`、`collar_disk_scalar_result.json` 记录。
