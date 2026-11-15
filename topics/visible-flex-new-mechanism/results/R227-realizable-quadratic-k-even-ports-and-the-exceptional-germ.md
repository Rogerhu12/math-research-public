# R227：可实现的二次 k 共同偶端芽与指数增长分支的例外

日期：2026-11-15。**完整纸面存在证明；没有运行新的研究符号、profile 或几何计算。**

来源：[R70 真实矩阵桥](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R73 点态八矩](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R83 完整历史传递](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R129 水平分部积分](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R214 正则原语](R214-nowhere-constant-closed-hook-with-exact-universal-pure-zero.md)、[R218 共同偶端芽](R218-common-even-nonflat-germs-and-exact-universal-pure-control.md)、[R220 受约束 Morse 几何](R220-constrained-Morse-geometry-with-exact-universal-pure-control.md)、[R222 全 pure 与八通量控制](R222-simultaneous-real-pure-and-eight-flux-control.md)、[R223 保全有限观测的 Morse 路径](R223-Morse-closed-hooks-with-exact-pure-and-eight-flux-constraints.md)、[R224 偶端芽 ruling 障碍](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)。

本稿给出一种真正可以安装到上述有限词的新端芽。它保留全部端速度为零、真实倒行、原成本空间和完整第三算子结构，并允许所有已付 finite pure/flux 目标保持准确。改变 k 所产生的 frame 变化由一项明确的三维参数修正支付，不能沿用 R218 中“k 不变，所以 frame 不变”的理由。

本稿**不证明新端芽的完整 ruling 可解**。R224 的一般偶部商仍存在；这里准确改变的是这个商中的三矩子空间和 canonical 目标。特别，原常状态的二次 s 项在新子空间中被准确包含，不能再单独充当排除证据。新的 quartic 条件仍须按完整 R56 检验。

## 1. 单一共同端芽与直接真倒行的兼容限制

先区分一项架构限制与具体端芽选择。

设一条实际块 B 的首末都采用同一个完整 scalar germ。沿用 R71/R72 的同 k 真倒行：

$$
h^R(s)=h(L-s),\qquad
k^R(s)=k(L-s),\qquad
\omega^R(s)=\omega(L-s).
\tag{1}
$$

在 $B B^R$ 的中间接口，右侧的第 j 阶 scalar 导数等于左侧导数的 $(-1)^j$ 倍。因此这个直接拼接为光滑，要求该端口全部奇阶 jets 为零。若再允许同一配对块直接重复，其首端也有同样要求。

对这里使用的“同一完整 germ 可重复，且可直接接其真倒行”的结构，最方便的准确条件是共同 germ 本身为偶函数。若 germ 只是假定光滑，零奇阶 jets 并不单独迫它在开邻域内为偶；本稿选取解析偶 germ，从而同时保证函数级匹配与全部 jets 匹配。

这一观察不排除有多个端口类型、另加连接器的非偶构造。它只说明：不能把原词里的共同偶 germ 直接换成有非零奇 jet 的同一 germ，却继续无改动使用原重复和真倒行身份。新增端口类型必须另付匹配与连接成本。

对任意全偶的 h、k、omega，R73 的点态 $M_{\rm raw}$ 仍为偶函数；R221 的局部二阶 gauge 项仍为奇函数，累计矩阵仍为“中心常数加奇函数”。所以 R224 的一般结论

$$
\operatorname{Ev} B_\theta(w)\in
\mathcal W_e,\qquad
\mathcal W_e=\operatorname{span}\{w_0,w_1,w_2\}
\tag{2}
$$

继续成立。本文没有消灭这个偶部 quotient。

## 2. 一个准确的二次 k 端芽

给定端值

$$
S_e=(h_e,k_e,\omega_e),\qquad h_e>0,\quad k_e\ne0,
$$

令 $\varepsilon>0$ 为小的端芽设计参数，$\sigma=s-s_e$ 为真实物理 s 距离，并记

$$
t=\sigma^2,\qquad b_e=\omega_e-\frac{k_e}{h_e}.
$$

规定端口核心邻域中的准确函数为

$$
\boxed{
\begin{aligned}
h(\sigma)&=h_e e^{\varepsilon\sigma^2},\\
k(\sigma)&=k_e(1-2\varepsilon\sigma^2),\\
\omega(\sigma)&=b_e+\frac{k_e}{h_e}e^{-\varepsilon\sigma^2}.
\end{aligned}}
\tag{3}
$$

所有三式均对 $\varepsilon=0$ 光滑延拓为原常状态，不含 $1/\varepsilon$ 奇性。直接微分给

$$
\omega_s=-\frac{2\varepsilon k_e\sigma}{h_e}
e^{-\varepsilon\sigma^2}
=\frac{-4\varepsilon k_e\sigma}{2h}
=\frac{k_s}{2h}.
\tag{4}
$$

所以它是原水平几何方程的准确解，不能把 omega 当作独立指定函数。

在端口中心，

$$
\begin{gathered}
(h,k,\omega)(0)=(h_e,k_e,\omega_e),\\
h_s(0)=k_s(0)=\omega_s(0)=0,\\
h_{ss}(0)=2\varepsilon h_e>0,\qquad
k_{ss}(0)=-4\varepsilon k_e\ne0,\qquad
\omega_{ss}(0)=-\frac{2\varepsilon k_e}{h_e}.
\end{gathered}
\tag{5}
$$

全部奇阶 jets 为零。h 在中心是非退化极小值；在整个核心区

$$
h_{ss}=(2\varepsilon+4\varepsilon^2\sigma^2)h>0.
\tag{6}
$$

最简单的共同端值是 $(h_e,k_e,\omega_e)=(1,1,1)$：

$$
h=e^{\varepsilon\sigma^2},\qquad
k=1-2\varepsilon\sigma^2,\qquad
\omega=e^{-\varepsilon\sigma^2}.
\tag{7}
$$

不要求每个辅助接口都取这一个状态；不同接口可以取相应的非零 $k_e$，并共用同一个 $\varepsilon$。

### 2.1 三矩子空间的准确改变

R73/R221 的状态量和三矩权为

$$
d=h\omega-k,\qquad
w_0=\frac{1+d^2}{4h},\quad
w_1=\frac d2,\quad
w_2=\frac h4.
$$

置 $a=2\varepsilon k_e\ne0$。由 (3) 得

$$
d=b_eh+at.
\tag{8}
$$

于是

$$
w_1-2b_ew_2=\frac a2t,
\qquad
w_0-b_ew_1+b_e^2w_2
=\frac{1+a^2t^2}{4h}.
\tag{9}
$$

从而

$$
\boxed{
\mathcal W_e=
\operatorname{span}
\left\{h,\ t,\ \frac{1+a^2t^2}{h}\right\}.
}
\tag{10}
$$

这三个解析函数在任何端口开邻域中线性独立。若其某常系数组合为零，解析性先把恒等式延到 $t\ge0$；依次用指数增长的 h、线性 t、指数衰减的最后一项分离系数，即得全零。这里只检验三个显式解析函数，不把实际闭路径向无穷延长。

特别，

$$
\boxed{
\sigma^2=\frac{1}{\varepsilon k_e}
(w_1-2b_ew_2)\in\mathcal W_e.
}
\tag{11}
$$

在每个固定正 $\varepsilon$，这是准确身份。它不是令 $\varepsilon\to0$ 后用发散系数作近似；系数虽随 $\varepsilon$ 变大，对已选定的正 $\varepsilon$ 仍是有限实数。式 (7) 更有 $w_1=\varepsilon\sigma^2$。

因此“冻结常状态的非零 $\sigma^2$ 系数”本身不再排除 (3)。但是 (11) 绝不蕴含完整 $\operatorname{Ev}K_\theta^0\in\mathcal W_e$；新的目标还可能含有商中非零部分。

### 2.2 为什么这是一般候选族中的特定例外

若仍取 $h=h_e e^{\varepsilon t}$，要求

$$
d=b_eh+at
$$

并保持相同中心值及水平方程，则解为

$$
\begin{aligned}
k&=\frac{a}{2\varepsilon}-at+
\left(k_e-\frac{a}{2\varepsilon}\right)e^{2\varepsilon t},\\
\omega&=b_e+\frac{a}{2\varepsilon h_e}e^{-\varepsilon t}
+\frac{k_e-a/(2\varepsilon)}{h_e}e^{\varepsilon t}.
\end{aligned}
\tag{12}
$$

这里的指数 k 项系数是

$$
C=k_e-\frac{a}{2\varepsilon}.
$$

式 (3) 正是 $C=0$，即 $a=2\varepsilon k_e$ 的子族。不能因为一般 (12) 也满足 (9)，就说所有 $C\ne0$ 分支都逃过 R224 型的更高增长障碍。该分支的 canonical 目标也改变，必须另作完整分析。

若中心 $k_e=0$ 被预先固定，$C=0$ 又要求 $a=0$，就退回常 k 的原端芽。本稿的新接口明确使用 $k_e\ne0$。它不承诺在保留一个既定零 k 端值时实现 (11)。

## 3. 倒行、正仿射作用与原成本空间

### 3.1 真倒行和有限复制

式 (3) 全偶，故 (1) 保持整个 germ。采用原真实 frame/位移公式

$$
F^R(s)=D A^TF(L-s)D,\qquad
\alpha^R(s)=D A^T(\alpha(L-s)-V),
\quad D=\operatorname{diag}(-1,1,-1),
\tag{13}
$$

其中 $F(0)=I,F(L)=A$，可直接拼接原配对词。k 不随倒行另加负号。

同状态的重复块、M0 桥和其倒行、R72 半角 frame 桥、R71/R101 的完整结构词均采用相匹配的 (3)。全部导数一致，所以 R56 局部恢复项也匹配。真实 W2/W3 初值仍逐块传递；没有在接口置零。

对 M0 块，原关系

$$
M_{B^R}=0,\qquad T_{B^R}=-T_B,\qquad V_{B^R}=V_B
\tag{14}
$$

仍成立。第四成本的正号没有改变；新端芽不提供成本的形式负元。

### 3.2 正 H 与 omega 平移

R89 的真实作用

$$
h\mapsto Hh,\qquad
k\mapsto k,\qquad
\omega\mapsto\frac{\omega+c}{H},\qquad H>0
\tag{15}
$$

不改变 s。它把 (3) 准确送到相同 $\varepsilon$ 的同类端芽，其参数为

$$
\widetilde h_e=Hh_e,\quad
\widetilde k_e=k_e,\quad
\widetilde\omega_e=\frac{\omega_e+c}{H},\quad
\widetilde b_e=\frac{b_e+c}{H}.
\tag{16}
$$

所以 $C=0$ 子族对既有正仿射控制作用封闭。不同状态桥的两端分别使用各自 (3)，不要求整条桥保持这一局部公式。

### 3.3 端势与 U 归属

R129 的全部相关端势具有如下准确结构：

$$
P_1=p_1(S)h_s+p_2(S)k_s,
$$

$$
P_{3,a}=(\beta_{hh}h_s+\beta_{hk}k_s)h_{ss}
+(\beta_{kh}h_s+\beta_{kk}k_s)k_{ss},
$$

以及速度三次的 $P_{3,v}$。R109 的 $N_2$ 是速度二次。

故 (5) 给

$$
P_1=P_{3,a}=P_{3,v}=N_2=0
\tag{17}
$$

在所有外端及拼口中心成立，虽 $k_{ss}\ne0$。$N_0$ 仍保留；其初势项由整块 $M=0$ 的 $\mathcal B_MN_0$ 消去，而不是假设 $N_0=0$。

因此 R218 §2 的原式证明原样适用：相同端口、完整 M0 的真实块，其第四成本仍在原来已经证明的有限空间 U 内，

$$
V_B\in U,\qquad \pi V_B\in P=\pi U.
\tag{18}
$$

第三算子可非零。没有因为改变 k 的二阶 jet 而重新定义 U，或用新的函数坐标扩大原成本空间。

## 4. 把端芽安装到真实正则原语：先 frame，再九个约束

### 4.1 有限准备与准确物理坐标

从 R214/R223 已使用的一个有限正则原语库出发。各调用参数限制在固定紧小盒；整数圈数和词的复制次数固定。保存全部需要共同匹配的接口及其原常值 collars。

端口状态是设计数据。可先选它们的 $k_e\ne0$；R70 的任意 scalar/frame 端点能力允许这个选择，其辅助正负圆本来在 $k=\pm1$ 的小邻域。若从含零 k 端值的某个已选有限库出发，可以把对应的共同端值作为外参数作一致的小非零改变，并在后面的完整有限约束中恢复目标。这里改变的是设计几何，不声称保持原度量不变。

本命题的准确前提是：待安装的有限标记端口均已取非零 k，并在所用紧参数盒内与零有正距离。它不需要 k 在整条路径上处处非零，也不禁止不同正负端口之间经过 k=0。

令 $a\in\mathbb R^8$ 为 R70 的矩阵正则参数，$\theta$ 收集端状态、矩阵目标和其他有限调用参数。另把**指定末 frame** $F\in SO(3)$ 暂时当作独立外参数。原 R70 族对每个邻近 $(a,F,\theta)$ 都准确具有末 frame F、指定 omega 端值，且 $D_aM$ 可逆。

把接口中心记为真实 $s_e(a,F,\theta)$。在其常 collar 内取固定物理半径的偶 cutoff $\chi_e$，核心区为一。原 h、k 的预修改为

$$
\begin{aligned}
h^{\rm pre}_\varepsilon
&=h^{\rm old}
+\sum_e h_e(e^{\varepsilon\sigma_e^2}-1)\chi_e,\\
k^{\rm pre}_\varepsilon
&=k^{\rm old}
-\sum_e2\varepsilon k_e\sigma_e^2\chi_e,
\qquad \sigma_e=s-s_e.
\end{aligned}
\tag{19}
$$

外端取对应单侧 collar，内部接口使用同一个两侧公式。每次评价都用该次参数的真实物理 s 坐标、真实时长和接口位置；不能冻结最初归一化坐标后忽略时长变化。

式 (19) 在核心区准确给 (3) 的 h、k，在 $\varepsilon=0$ 连同参数导数恢复原族。

### 4.2 三维 frame 修正

改变 k 会改变真实 frame。记预修改后、按真实时长积分原 frame ODE 得到的末 frame 为

$$
\mathfrak F(a,F,\varepsilon,\theta).
$$

有

$$
\mathfrak F(a,F,0,\theta)=F.
\tag{20}
$$

设所需末 frame 为 $F_*(\theta)$。在其附近取 SO(3) 坐标，解

$$
\log\!\bigl(F_*(\theta)^{-1}
\mathfrak F(a,F,\varepsilon,\theta)\bigr)=0.
\tag{21}
$$

在 $\varepsilon=0,F=F_*(\theta)$，对 F 的导数为三维恒等。有限维 IFT 给唯一邻近的

$$
F=\widehat F(a,\varepsilon,\theta),\qquad
\widehat F(a,0,\theta)=F_*(\theta).
\tag{22}
$$

先用 (22) 代回 (19)，末 frame 从此对全部邻近 a 精确。特别

$$
D_a\widehat F(a,0,\theta)=0.
\tag{23}
$$

这不是新添一条“零成本 frame 桥”，也不把 k 修改的成本忽略。它调整原正则桥族的一个指定端数据；全部修改后的实际几何参与后面的矩阵和成本计算。

frame 方程只读 k 和真实时长。因此下面只改变 h 的自由扰动与 omega 修正参数不影响 (21)。这使三维 frame 方程可先解，再保留原来的九约束结构。

### 4.3 完整 M 与 omega 末值的九维修正

保留 R214 的函数 $\zeta$，支撑在一个 $k_s\ne0$ 的内部区域，满足原点处

$$
c_\omega=-\frac12\int\frac{k_s\zeta}{h^2}\,ds\ne0.
\tag{24}
$$

该区域与新端芽核心分离。另取自由光滑 h 扰动 $\eta$，用 mask 使其在所有保护核心为零。令

$$
\widehat h=h^{\rm pre}_\varepsilon+\eta+z\zeta,
\qquad
\widehat k=k^{\rm pre}_\varepsilon,
\tag{25}
$$

其中预修改已代入 (22)。omega 沿真实方程从指定首值积分：

$$
\widehat\omega(s)
=\omega_-+\int_{s_-}^s
\frac{\widehat k_s}{2\widehat h}\,d\tau.
\tag{26}
$$

对整条原语解

$$
\mathcal G(a,z,\eta,\varepsilon,\theta)
=\bigl(M-M_*(\theta),\
\widehat\omega(s_+)-\omega_+(\theta)\bigr)=0.
\tag{27}
$$

在原点 $\eta=\varepsilon=z=0$，(19)、(22)、(23) 给

$$
D_{(a,z)}\mathcal G=
\begin{pmatrix}
D_aM&D_zM\\
0&c_\omega
\end{pmatrix},
\tag{28}
$$

仍可逆。矩阵 M 使用 (26) 的真实 omega 和 R73 完整点态密度，不在改 h/k 后保留旧历史。

在充分高的有限 $C^r$ 参数空间上应用 IFT，得到

$$
a=a(\eta,\varepsilon,\theta),\qquad
z=z(\eta,\varepsilon,\theta),
\tag{29}
$$

使 frame、完整八矩、omega 末值全部准确满足。有限参数紧性给统一小正 $\varepsilon$，并保正 h 和原物理支的正余量。限制到光滑 masked $\eta$，每条路径仍为 $C^\infty$。

### 4.4 内部 omega germ 不需要漏加的约束

在任一保护核心，h、k 已准确为 (3) 的前两式，所以 (26) 必具有

$$
\widehat\omega(\sigma)
=\widehat b_e+\frac{k_e}{h_e}e^{-\varepsilon\sigma^2}.
\tag{30}
$$

其中心值给 $\widehat b_e=\widehat\omega(s_e)-k_e/h_e$。原语内部的这一中心值允许随真实前方积分改变；它不需要逐内口重置为旧值。内部两侧是同一个真实解，故其整个 omega germ 匹配。

外端 omega 中心值由首条件和 (27) 固定，所以相邻原语之间则具有规定的同一 (3)。这解释了为何 (28) 只有一个 omega 末值约束，而没有把每个内部端口都误当成可独立重置的 omega。

## 5. 完整第三结构、有限观测与空间闭合

第 4 节没有控制单个原语的完整 T。与 R214/R218 一样，使用同一已修正原语族的共享副本组成 R71 的对称词。各副本保持指定 M、frame、端口；原未知第三量由真实 composition 恒等式准确消去，故

$$
T_{\mathcal L(t)}=2t[P,Q]
\tag{31}
$$

仍是完整三槽身份。R101/R102 的响应词同样保其低阶结构与全部偶基准。不得把 (31) 换成只对角相等，或把共享族在不同位置独立选择。

若原有限库还带有 R212/R223 的准确有限坐标截面，记所控制的观测为

$$
\mathcal E(V)=(\pi V,\mathcal F_8(V)).
$$

原点处有限成本映射具有已付的满秩导数。第 4 节对所有原语进行共同修改后：

- 全部低阶结构仍由 (31) 及原词保持；
- 由 (18)，完整新成本仍在同一个 U；
- 成本、有限观测和所有已求参数对 $\eta,\varepsilon$ 为 $C^1$；
- 在 $\eta=\varepsilon=0$，恢复原满秩坐标族。

因此同一个有限维参数 IFT 保持所选的全部 $\mathcal E$ 目标。它计算完整修改后成本，包含新 germ、frame 修正、九维补偿和全部原未知基准；并未先把这些误差投影掉。若只需全 pure，取对应原 full-P 截面即可。

上述应用只使用 R223 已具有完整三槽结构保持族的有限库。它不由 R208 的 diagonal 覆盖推出任意 mixed 第三算子都可自由扰动，也不把 R225 的一般 period 商控制自动升级为 Morse 结论。

闭 hook 的位置仍按修改后实际 prototype 位移作 Klein 求和。相同控制在四个左旋转副本中出现，完整 M0 第四加法仍给原来的因子四。位移不要求逐原语保持旧值；四个实际向量之和准确为零。

在保护核心，(6) 已保证 h Morse。其余区域保留任意 masked h bump，R223 的有限积分密度与两 jet 分离证明仍适用；先施加 (21)、(27) 及全部有限观测约束的一阶零变化，再作原受约束横截选择。frame 方程不含自由 h，故不新增点值型限制。可由此在同一准确约束流形中取得全域 h Morse。

共同物理区间的次序也不改变：先固定有限库和紧参数包络，再选 I/profile 圆；或者从一个已有严格物理余量的固定 I 出发，把上述全部修改限制得足够小。后续始终使用同一 I、同一右锚及同一个圆。改变几何一般会改变目标度量；本稿不称沿这一设计修改保持原 g。

## 6. 新 ruling 问题的准确位置

对 (3)，R224 消去中心传入 W2/W3 后得到的 canonical 偶部仍必须满足

$$
\operatorname{Ev}K_\theta^0
\in\operatorname{span}
\left\{h,\sigma^2,
\frac{1+4\varepsilon^2k_e^2\sigma^4}{h}\right\}.
\tag{32}
$$

第三 homogeneous gauge、二阶 gauge 的偶部和相应平方项仍仅改变右侧三矩部分。这个必要条件未被本文支付。

新的主二次算子也不等于 R224 标准 $k=\omega=0$ 端芽的 T。为明确剩余对象，可只从 R73 的六个点态系数手工提取一个精确的最高指数层。令

$$
q=x+b_e,\qquad
J_{b_e}(f,g)=\int_x^r
\bigl((\eta+b_e)^2f''g''+2f'g'\bigr)\,d\eta.
$$

当以三个显式端芽函数在正 $\sigma$ 上作解析比较时，

$$
r_s=hk\,G_{b_e}+\text{不含正 h 幂的多项式增长项及衰减项},
\tag{33}
$$

其中

$$
\boxed{
8G_{b_e}(f,g)=
4qfg-2q^2(fg'+f'g)+2q^3f'g'
+q^2J_{b_e}(f,g).
}
\tag{34}
$$

验证 (33) 不需要第四 forcing 编译：在 R73 (4)–(6) 代入
$z=q+k_e/h$、$e=hq+2\varepsilon k_e\sigma^2$，
其唯一正 h 层分别为

$$
\begin{aligned}
A_0&=hk\,q/2+\text{低层},\\
A_1/2&=-hk\,q^2/4+\text{低层},\\
A_2&=hk\,q^3/4+\text{低层},\\
(B_0,B_1,B_2)
&=\frac{hkq^2}{8}(b_e^2,2b_e,1)+\text{低层}.
\end{aligned}
\tag{35}
$$

$h_s/h=2\varepsilon\sigma$、$k$ 及 $k_s$ 都是多项式，故 R73 的导数项没有另一个遗漏的正 h 层。若 $b_e=0$，按同一八坐标约定，

$$
G_0=-\frac12\Phi_{p_2}.
\tag{36}
$$

式 (33)–(36) 只定位新的二阶输入层，**没有据此省掉第四层的局部恢复或链式项**。记

$$
E_{b_e}(u,v)=\frac14\int_I
\bigl((x+b_e)^2u''v''+2u'v'\bigr)\,dx.
$$

例如将来若要以

$$
E_{b_e}(G_{b_e}(q_0,q_0),G_{b_e}(q_0,q_0))
+2E_{b_e}(q_0,G_{b_e}(q_0,G_{b_e}(q_0,q_0)))
\tag{37}
$$

给出符号障碍，必须先从完整 R56 证明其确为保留全部历史后的领先 quartic 系数，再判断该固定圆上的值。R193/R224 的 $T$ 系数 $c_6>0$ 不能把 (37) 自动代换为正数。

## 7. 本稿完成的接口

现在已有准确的有限真实构造，允许在非零 k 端值处同时保持：

1. 真实水平方程与同一个解析偶 germ；
2. 非零的 $h_{ss},k_{ss}$，但端速度仍为零；
3. 同 k 真倒行、正 H/omega 平移、有限重复及整个 scalar 匹配；
4. 原 U 中的完整成本归属，保留 $N_0$ 和所有传入 histories；
5. 由三维 frame IFT 加九维矩阵/omega IFT 支付的真实端点约束；
6. 原结构库的完整第三算子、已付 pure/八通量目标及 Klein 空间闭合；
7. 在 R223 的相同结构前提下，全域 Morse h。

它没有证明任一固定圆的完整 mixed period 或 ruling 已属于可解像。其具体新价值是：标准常 k 指数端芽不是原真实构造的唯一可用端口；(3) 是保持既有精确控制结构的一个真正替代物，而它剩下的 ruling 输入已准确改为 (32)–(37)。
