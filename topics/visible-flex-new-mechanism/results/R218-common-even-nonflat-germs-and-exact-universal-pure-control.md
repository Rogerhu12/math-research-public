# R218：共同偶非平端口、原成本空间与精确全 pure 校正

日期：2026-11-15。作者及推导责任：tail_cost；root 阅读后登记。**完整纸面存在证明；没有新的研究计算。**

依据 [R70 真实矩阵桥](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R71 完整第三词](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R72 frame 桥](R72-same-state-zero-second-third-arbitrary-frame-bridge.md)、[R83 真实历史传递](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R89 正仿射协变](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R109 完整局部成本](R109-local-density-of-the-complete-fourth-quotient.md)、[R129 水平 IBP](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130 原真实空间](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R212 全 P 截面](R212-C1-sections-for-complete-real-pure-cost-control.md)、[R214 结构词及自由扰动](R214-nowhere-constant-closed-hook-with-exact-universal-pure-zero.md)和 [R216 平点 ruling 门](R216-fourth-ruling-obstruction-at-a-single-flat-state-point.md)。

R216 说明只去掉开常段仍不能绕过常状态的第四 ruling 门：一个四阶平点已经足够。本稿支付一个具体新接口——所有有限拼接口可统一采用偶的非平 germ，保持真实低阶词、全部桥基准、全 pure 函数与空间闭合。

本文只保证列明的全部拼接口不再是四阶平点，不宣称几何内部再无其他四阶平点，也不宣称通过了完整第四 ruling。

## 1. 端口与结论

固定 scalar 端值 $g=(h_*,k_*,\omega_*)$，$h_*>0$。令 $\varepsilon\ge0$ 是新的、仅用于设计端口的参数，不是等距变形的 Taylor 参数。规定端口在真实 s 距离 $\sigma$ 中具有共同 germ

$$
\boxed{
h(\sigma)=h_*\exp(\varepsilon\sigma^2),\qquad
k(\sigma)=k_*,\qquad
\omega(\sigma)=\omega_*.
}
\tag{1}
$$

对路径左端取 $\sigma=s-s_-$，右端取 $\sigma=s-s_+$。式 (1) 是某个正长度端邻域上的准确函数身份，不只是到有限阶匹配的多项式。

当 $\varepsilon>0$ 时，端点满足

$$
h_s=k_s=\omega_s=0,\qquad
h_{ss}=2\varepsilon h_*>0,
\tag{2}
$$

且全部奇阶 scalar jets 为零。特别它不满足 R216 的四阶平点前提。两侧采用同一 (1)，就得到一个光滑的偶形拼接口。

仍用原有限真实空间 $U$、响应空间 R 及整个 pure 空间 $P=\pi U$，不重新定义它们。

**定理 A。** 对每个指定 $p\in P$，存在 $\varepsilon_0>0$，使所有足够小的固定 $\varepsilon\in(0,\varepsilon_0)$ 都有一条实际有限光滑控制路径 $D_\varepsilon(p)$，满足

$$
M=T=0,\qquad F_{\rm end}=F_{\rm start},\qquad
\pi V_{D_\varepsilon(p)}=p.
\tag{3}
$$

它的首末采用 (1)。构造所用有限词的每个已标记拼接口——包括原语内部原先合并记录的有限拼接口——也采用相同 $\varepsilon$、相应状态值的 (1)。所有真实整数复制数固定。p 在一个邻域内可以同时作为 $C^1$ 参数；选择适当自由扰动后，每个指定 p 还可实现为无开常状态段的路径。

**定理 B。** 存在采用这些偶非平拼接口的有限光滑闭合周期浸入带，使

$$
\boxed{
M=0,\quad T=\kappa\mathfrak H\ne0,\quad
F_{\rm end}=F_{\rm start},\quad
\alpha_{\rm end}=\alpha_{\rm start},\quad
\pi V=0.
}
\tag{4}
$$

它可以没有开常状态段。所有构造中的原拼接口满足 (2)。这里的 $\kappa$ 固定非零，新增端口与校正成本全部由真实恢复计入。

这两个定理不授同 g 有限等距族、mixed period、完整 ruling、嵌入或 reach。它们也不把“已标记拼口均非平”提升为“全域没有四阶平点”。

## 2. 端速度为零已经支付原 IBP 边界

R129 使用

$$
u=h_s,\quad w=k_s,\quad a=h_{ss},\quad b=k_{ss}.
$$

其导数权一的端势为

$$
P_1=p_1(S)u+p_2(S)w.
\tag{5}
$$

导数权三端势分成

$$
P_{3,a}=B_h a+B_k b,
$$

$$
B_h=\beta_{hh}(S)u+\beta_{hk}(S)w,\qquad
B_k=\beta_{kh}(S)u+\beta_{kk}(S)w,
\tag{6}
$$

以及对 $(u,w)$ 齐次三次的

$$
P_{3,v}=\frac13(u\bar C_h+w\bar C_k).
\tag{7}
$$

所以只要端点 $u=w=0$，就准确有

$$
\boxed{P_1=P_{3,a}=P_{3,v}=0.}
\tag{8}
$$

这里 a、b 可以非零。式 (8) 直接来自完整公式；没有按导数权猜测省略某个加速度端项。

同样，R109/R129 的局部第三势

$$
N=N_0+N_2,\qquad N_2=P_{\rm acc}
$$

中，$N_2$ 是速度二次势。故 (2) 使端点 $N_2=0$；权零 $N_0$ 仍完整保留，不作零化假设。

对任意整条 M0 路径，R109 已给

$$
[V_B]_R=\left[\int_B(v-\mathcal B_mN)\,ds\right]_R.
\tag{9}
$$

其中真正的初势修正是 $\mathcal B_{M_B}(N(0))$，由完整 $M_B=0$ 消去。这个理由对 (1) 同样成立，不需要把 $N_0(0)$ 设为零，也不需要 $h_{ss}(0)=0$。

再减同一个八矩规范化 $\Gamma m$；其全积分由 M0 消去。用 (8) 对 R129 做 IBP，余下仍是 R130 的十四族状态函数值的有限维积分。由其原定理 $U=R+K$，

$$
\boxed{M_B=0,\ \text{端速度为零}\quad\Longrightarrow\quad
V_B\in U,\quad \pi V_B\in P.}
\tag{10}
$$

这里只在本稿使用的相同端口、真实完整恢复中应用 (10)。第三算子可非零，正如 R109 §6 本来不要求 T0。全 T0 的控制词当然也适用。

因此后文改端口产生的新 pure 误差始终在原 P 内；没有把新函数硬投影进 P，也没有扩大成本空间来使 IFT 方程形式上可解。

## 3. 偶 germ 的真实兼容性

### 3.1 同 k 真倒行

对长度 L 的原路径，使用 R71/R72 的同 k 真倒行：

$$
h^R(s)=h(L-s),\quad
k^R(s)=k(L-s),\quad
\omega^R(s)=\omega(L-s).
\tag{11}
$$

其 frame 和位移仍采用真实式

$$
F^R(s)=D A^T F(L-s)D,\qquad
\alpha^R(s)=D A^T(\alpha(L-s)-V),
\quad D=\operatorname{diag}(-1,1,-1),
\tag{12}
$$

其中 $F(0)=I,F(L)=A,\alpha(L)=V$。由 $D\Omega(k)D=-\Omega(k)$，(12) 满足原 frame 方程，末 frame 为 $DA^TD$。

式 (1) 在 $\sigma\mapsto-\sigma$ 下不变，所以倒行后的端口 germ 与相接端口完全一致；不能只说明端状态相同而漏掉奇导数。这里所有奇 jets 本来为零，而非事后把倒行符号删掉。

### 3.2 正 H 缩放与平移

R89 的真实正仿射作用是

$$
h\mapsto Hh,\qquad k\mapsto k,\qquad
\omega\mapsto\frac{\omega+d}{H},\qquad H>0.
\tag{13}
$$

s 参数不改变。它把 (1) 准确送到

$$
\widetilde h(\sigma)
=(Hh_*)\exp(\varepsilon\sigma^2),\quad
\widetilde k=k_*,\quad
\widetilde\omega=(\omega_*+d)/H.
\tag{14}
$$

因此同一个 $\varepsilon$ 对全部有限缩放族通用。特别比值 $h_{ss}/h=2\varepsilon$ 保持；不把各块独立指定一个互不匹配的二阶 jet。

不同状态之间的真实桥，在两端分别采用对应状态的 (1)。缩放块与桥相接处的状态值相同，故其整个 germ 相同。空间左旋转不改变 scalar germs。

### 3.3 有限重复、frame 桥及空间闭合

同一块重复时，右端与下一副本左端均为 (1)，故真实有限重复光滑。R72 的 $BB^R$ 构造仍有 frame 增量

$$
A D A^T D,
\tag{15}
$$

并由半角桥得到所需旋转；它并不要求 h 在邻域恒定。

所有中心线位移按修改后的真实 h、frame 重新确定。后面的 Klein 闭合使用四个实际左旋转

$$
I,\quad g_1,\quad g_2,\quad g_1g_2,
\qquad I+g_1+g_2+g_1g_2=0
\tag{16}
$$

作用于同一个修改后 prototype 位移。式 (16) 仍逐个 prototype 准确消位移；本稿从未要求单个新桥保持旧位移。

由 (1) 的完整 germ 匹配，frame ODE 及 $\alpha_s=h^2T$ 在每个接口均光滑，最终首尾也光滑。

## 4. 历史 composition 与倒行不新增端口误差

原 R83 传递式来自逐点向量场身份

$$
Z_2=Z_B(D)-Y_w,\qquad
Z_3=W_B(\phi,D)+2Z_B(\phi,w)-Y_u,
\tag{17}
$$

其中 w、u 是进入整块的真实 scalar histories。式 (17) 只使用恢复线性性、同一右锚及同一真实 s 初点，不要求端点附近常状态。

两块的整个 scalar germ 相接时，R56 所有局部几何项及其导数也相接。将真实 w、u 传入下一块，(17) 因此仍给同一全局光滑场；不会留下一个因为 $h_{ss}\ne0$ 产生的未记录场跳跃。

于是 R83 的完整 composition 原式逐字保持。例如

$$
A_{21}=A_1+A_2,\qquad
T_{21}(a;D)=T_1(a;D)+T_2(a;D)-A_2(a,A_1D).
\tag{18}
$$

第四式仍包括全部 $\mathcal B$ 交叉项和未知自身成本。没有将传入 histories 或其沿段导数置零。

对 M0 块，真实倒行的奇偶场身份与原端历史补正也不需要常状态邻域。由 (11)、(12) 及 (17)，

$$
\boxed{
M_{B^R}=0,\qquad T_{B^R}=-T_B,\qquad V_{B^R}=V_B.
}
\tag{19}
$$

最后一个正号仍必须保留。拼接的光滑性已由第 3 节支付；(19) 不是以形式负词代替真实路径。

因此各类结构词保持如下：

| 真实结构 | 仍准确保持的低阶量 |
|---|---|
| M0 原语 W 与其 $W^R$ 配对 | M=T0 |
| R71 的 $A(t)BA(-t)C$ 与对应倒行差词 | 完整 $T=2t[P,Q]$ |
| R72 的 M0 桥和真倒行 | M=T0，frame 由 (15) 给定 |
| 正仿射块与真实 M0 去返桥夹接 | 预定低阶算子，全部桥第三成本按 (19) 相消 |
| R83/R101 的响应词及完整偶第三消去 | M=T0 |
| 向 hook prototype 插入 M=T0 控制 | 完整 hook 的 T 不变 |

每一行均是实际有限词身份。自身第四基准仍在，不把这些块当成零成本。

## 5. 在所有原拼接口同时安装新 germ

现在回到 R214 证明中、Baire 选择之前的固定有限结构词与正则原语族。此时每条原语已有开常值端 germs。若某条原语把 $A_{\rm reg}B^N$ 整体记录为一个自由原语，仍保留其内部有限拼接口的标记；不能只修改外两端而把原内部 flat 拼口漏掉。

所有调用参数先限制在固定有限个紧邻域。辅助圈数、复制数、正反词与接口名单全部固定。每个标记接口在原族中有正长度常状态 collar；紧性与有限性给一个共同小正物理半径，使这些 collar 不相交。接口位置可以随原语参数光滑移动，但半径具有统一正下界。

在接口 e 的真实中心 $s_e$ 处记 $\sigma=s-s_e$，原状态值为 $(h_e,k_e,\omega_e)$。取偶的光滑 cutoff $\chi_e$，在较小邻域等于一、支撑在该常状态 collar 内。对 h 作准确修改

$$
h^{\rm pre}_\varepsilon(s)
=h^{\rm old}(s)
+\sum_e h_e\bigl(\exp(\varepsilon\sigma^2)-1\bigr)\chi_e(\sigma).
\tag{20}
$$

外端使用相应单侧半 collar。内部接口用同一个两侧定义，保持两侧一致。

在 $\chi_e=1$ 的核心区，原 h 等于 $h_e$，所以 (20) 正是 (1)。k 不变；修改支撑中 $k_s=0$，故预修改本身不改变真实 $\omega_s=k_s/(2h)$。对非零 $\varepsilon$，仍会改变矩阵及第四成本，后面将完整修复，不能因为 omega 不变就省略它们。

式 (20) 对原语参数和 $\varepsilon$ 光滑；在 $\varepsilon=0$ 完全恢复原族。它使用真实 s 距离，若原语内部以 $x\in[0,1]$ 记录，必须用实际长度把 $\sigma$ 换回 s，不能以一个忽略长度变化的 x 二阶 jet 代替 (2)。

具体地，设原语当前真实坐标为 $s=s_{a,\theta}(x)$，速度 $\lambda_{a,\theta}(x)=\partial_xs>0$，接口坐标为 $x_e(a,\theta)$。式 (20) 中准确使用

$$
\sigma_e(a,\theta,x)
=s_{a,\theta}(x)-s_{a,\theta}(x_e(a,\theta)).
\tag{20a}
$$

若采用统一线性归一化，这就是 $L(a,\theta)(x-x_e)$；cutoff 的半径仍是固定的物理 s 长度。于是 $D_s=\lambda^{-1}D_x$，在新 germ 内严格有 $D_sh=2\varepsilon\sigma_e h$、$D_s^2h=(2\varepsilon+4\varepsilon^2\sigma_e^2)h$。可变 L 或非恒速度不会把 $\varepsilon$ 变成 $\varepsilon/L^2$。

后面的 IFT 每次评价都使用该次实际 a、theta 对应的 (20a)，而不是把最初参数处的坐标冻结。两端物理 collar 半径在紧参数族中共同固定；其归一化 x 长度可随真实时长变化。若已有固定端 collar、仅中部改变时长的实现，同式自然退为固定端坐标情形。反向与正 H 作用不缩放 s，所以第 3 节的共同物理 germ 仍完全一致。

## 6. 每个原语的 M、omega 与 frame 先准确修复

沿用 R214 的正则原语参数。令 $a\in\mathbb R^8$ 是原 R70 的八个内部参数，$\theta$ 是有限端状态、矩阵目标和 frame 目标参数。原族对全部邻近 a 已有准确 frame 端点及 omega 末值，且 $D_aM$ 可逆。

保留一个紧支撑于非零 $k_s$ 区域的原 R214 校正函数 $\zeta$，使

$$
c_\omega=-\frac12\int\frac{k_s\zeta}{h^2}\,ds\ne0.
\tag{21}
$$

它可与上节标记 collar 分开。还允许自由 h 扰动 $\eta$；用一个随原语参数光滑的 mask，使 $\eta$ 在每个新 germ 核心邻域恒零。mask 在这些核心之外为正，故在其余任何内开区间仍保留任意紧支撑 h 扰动。式 (20) 的准确 germ 不会被之后的自由扰动破坏。

用 (20)、masked $\eta$ 及 $b\zeta$ 定义实际 h；保持原族 k，并从真实方程重新积分 omega。设

$$
G(a,b,\eta,\varepsilon,\theta)
=(M-M_*(\theta),\ \omega_{\rm end}-\omega_+(\theta)).
\tag{22}
$$

在 $\eta=\varepsilon=0$ 的原解处，仍有

$$
D_{(a,b)}G=
\begin{pmatrix}
D_aM&D_bM\\
0&c_\omega
\end{pmatrix}
\tag{23}
$$

可逆。原因是 (20) 在 $\varepsilon=0$ 连同其 a 导数均为零；原八参数族的 omega 末值仍对 a 固定。mask 的 a 导数此时乘 $\eta=0$，也不改变 (23)。

带参数 IFT 因而给真实

$$
a=a(\eta,\varepsilon,\theta),\qquad
b=b(\eta,\varepsilon,\theta),
\tag{24}
$$

使 (22) 在一个共同邻域中非线性地准确成立。正 h 和共同物理域具有统一正余量。frame 由原 k 与真实长度的族保持；h 修改不擅自改变 frame 方程。

内部接口随 (24) 移动时，(20) 的中心、状态值和 cutoff 一同移动，所以其实际 germ 仍为 (1)。同一正则族在多个词位置调用时共用这套函数，不在每次出现处独立挑一条无法匹配的桥。

这里没有控制单原语的完整 T 或第四成本。它们由第 4 节的真实词与下一节的 full-P 方程支付。

## 7. 完整词与 full-P IFT

### 7.1 任意指定 pure 目标

R214 的结构化版本给一个有限实际 full-P 坐标族 $D_0(u)$，在某个含指定 p 的开集上满足

$$
M=T=0,\qquad F_{\rm end}=F_{\rm start},\qquad
\pi V_{D_0(u)}=u.
\tag{25}
$$

构造中的所有原语都可以采用第 5–6 节的共同修改。整数复制数、原语调用格式及第三响应方向不再改变。第 4 节确保修改后的 $D_{\eta,\varepsilon}(u)$ 仍准确满足全部低阶条件。

定义

$$
\Phi_{\eta,\varepsilon}(u)=\pi V_{D_{\eta,\varepsilon}(u)}.
\tag{26}
$$

由 (10)，它的值确实在同一个 P；由真实有限恢复、ODE 依赖及 (24)，它对有限参数和充分高 $C^r$ 自由参数为 $C^1$。在原点

$$
\Phi_{0,0}(u)=u,\qquad D_u\Phi_{0,0}=I_P.
\tag{27}
$$

对整个 P 使用参数 IFT，得到

$$
u=u(p,\eta,\varepsilon),\qquad
\Phi_{\eta,\varepsilon}(u(p,\eta,\varepsilon))=p.
\tag{28}
$$

这一步同时修复 pure 商和响应两部分。不能只动 R212 最后一层响应参数而放任商坐标漂移。所有新的第四桥成本、germ 成本与原未知基准均已进入 (26)。

先在统一邻域中取一个小而严格正的 $\varepsilon$，再选 $\eta$，便得到 (3)。u 可在 p 的一个邻域内 $C^1$ 选择；不需要无限重复，也不以 $\varepsilon=0$ 的平端退化路径当最终输出。

### 7.2 闭 hook

使用 R214 的同一背景结构 $X^0_{\eta,\varepsilon}$，它由完整 R71/R72 词保持 M0、$T=\kappa\mathfrak H\ne0$，并用修改后的 prototype 位移作 Klein 闭合。

在第一 prototype 中插入上述 $D_{\eta,\varepsilon}(u)$，其在整个闭字出现四次。全部外块 M0，故真实第四加法给

$$
\Theta_{\eta,\varepsilon}(u)
=\pi V_{X^0_{\eta,\varepsilon}}
+4\pi V_{D_{\eta,\varepsilon}(u)}.
\tag{29}
$$

在原点 $\Theta_{0,0}(u)=\pi V_{X^0_{0,0}}+4u$。以
$u_0=-\pi V_{X^0_{0,0}}/4$ 为中心，

$$
D_u\Theta_{0,0}=4I_P.
$$

再次使用 full-P 参数 IFT，准确解

$$
\Theta_{\eta,\varepsilon}(u(\eta,\varepsilon))=0.
\tag{30}
$$

背景或插入块的位移都不保持旧值；完整 Klein 求和 (16) 对修改后的每个 prototype 仍准确，故空间闭合保持。frame、scalar 和全 T 由第 3–4 节保持，(30) 支付整个 universal pure，而不是有限采样或某个幂尾。

## 8. 可同时去掉开常段，但不宣称全域无四阶平点

固定上节得到的一个小正 $\varepsilon$。所有新 germ 核心区满足

$$
h_s=2\varepsilon\sigma h,\qquad
h_{ss}=(2\varepsilon+4\varepsilon^2\sigma^2)h>0.
\tag{31}
$$

因此其中没有开常状态段，中心点也由 (2) 非平。

在其他区间，重复 R214 的准确非线性约束后 Baire 论证。自由参数取有限个原语的光滑 masked h 扰动；(24)、(28) 或 (30) 已对整个邻域准确求解。对每个有限出现位置和有理内区间，仍以“h、k 在该区间都常值”为闭坏集。

若某个坏区间存在，它不能与 (31) 的核心区有内开重叠。可在坏区间内选一个 mask 严格为正的小开区间；除以这个固定正 mask 后，允许的原语自由参数仍能产生任意所需局部 bump。

在该 bump 空间上，对所有有限调用列出九约束的一阶条件，再列出全部 P 方程的一阶条件。有限个线性条件的共同核仍有非零 bump。按照 R214 的出现位置坐标 $\sigma_o$，选择其导数非零点，并利用全部参数修正的一阶变化为零，得到真实

$$
\delta h=c\,\psi\circ\sigma_o,\qquad
\delta h_s=c\,\sigma_o'\,\psi'\circ\sigma_o
$$

在某点非零。倒行的 $\sigma_o'=-1$ 不影响非零性。原语接口位置和 mask 也随参数变化，但这些变化经已施加的有限一阶条件在此方向为零，不额外产生被遗漏的项。

每个坏集因而无内点；可数 Baire 选择给一个准确满足 (28) 或 (30)、同时无开常段的光滑路径。所有 correction blocks 与 background blocks 都包含在同一有限出现列表中。

这只去掉开区间上的常状态。一个未标记的内部点仍可能满足 $h^{(j)}=k^{(j)}=0$、$1\le j\le4$；Baire 的上述证明没有排除这种零集。要证明全域没有四阶平点，需要另付受约束 jet 横截性或更强的具体构造，不能由本节直接推出。

## 9. 新端口究竟支付了什么

本稿完成的不是一个把原困难缩小到误差的近似替换。对固定小正 $\varepsilon$：

- 所有标记拼口具有准确共同偶 germ，二阶 h jet 严格非零；
- 真倒行、正 H 缩放、有限重复、不同状态桥和 frame 桥的端口完整兼容；
- 原语 M、omega 和 frame 已准确恢复；
- 完整第三算子由真实词恒等式保持；
- 新成本仍在原 U，full-P IFT 精确支付整个 pure 函数；
- 最终闭 hook 的 frame、实际位移和非零 T 保持；
- 可以进一步没有任何开常状态段。

它没有证明完整 fourth ruling 的单点 jet 条件在这些非平状态自动成立。R216 的冻结常状态公式在 (2) 这样的点不再适用；其余真实几何导数项和 gauge 响应必须按 R56 保留，不能因此直接判为可解。

R214 全平端口路线及 R216 对原八包的障碍事实均保留。本稿提供一个已经支付全部低阶与 pure 义务的新端口类别，供后续真正的 fixed-circle mixed/ruling 联合问题使用。更高阶、有限等距族和主课题的宏观嵌入标准仍未完成。

