# 新材料包络场的全时相连续几何接口与尚欠证书

2026-11-27，Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：完整源码与既有定理的适用范围核查、同场消费者合同；不是新的科学返回，不是完成证书，不新增求解准入门。** 本文不重新证明 R248、R650、R661、R703/R707 或 R715，也不把旧候选的几何数值迁给新场。新的准确几何包围尚须由公开 Actions 对真实返回的同一自由点产生。本文使用的仓库读本为 `f5fd138e686b6e0c272ddf77b2e725ff3f980f23`。

## 1. 当前实际对象与有限包络的作用

新入口的材料包络记为 $\mathcal E=P_0\cup G_{05}\cup G_{07}$。它是有限的材料地址责任集合，不是第一基本形式的分量 $E=|F_s|^2$。旧载体的必要再生已经真实完成：run `45909290354/1` 的第3步重建出完整 `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`、227202 字节，旧新 cells/u/Gauss 全字相同；完整报告为 `926db461a4efce0fa40ab539b9df28143f8664cca25ec96e95ebe1d7aa83dcdf`。这支付地址字节责任，没有计算新 $F/J$ 或根，也没有支付连续几何。

当前科学物理核仍为 a62c 的完整 R711 参考中心化 normal 表示。新的包络仅改变完整有限筛查和工作不等式集合的管理，不删除自由变量、32个共同 normal 段、任何物理六jet或真实筛查。已知 $P_0$ 前缀按原规则保留；未知旧保护角色和旧192行优先次序没有被“重建”，而由已明确选用的全 $\mathcal E$ 真筛与 typed 分离政策承担。

现有活动网格与 `cap_diameter` 标量并不是两个完整 p4 图帽的数值扫描。下文沿用 R661 的明确帽配方作为闭面装配合同；图帽的真实函数、共同帽度量和接缝必须由完整装配器保留，不能仅因 report 有帽预算就声明已导出或已认证整个标记闭面。

直接阅读新的 `GeometryScreen.scan` 可确认：它读取完整当前网格、历史额外网格及全部显式永久地点，返回样本主曲率、样本半径、双符号见证距离、帽与高度标量，以及完整物理六jet检查。它的

$$
D_{\rm sample}=\max\{2,2|H_{\rm cap}|,2\max_{\mathcal E}|F|\},\qquad
0.03D_{\rm sample}\max_{\mathcal E,i}|\kappa_i|
$$

是该数值工作筛使用的直径下侧量与曲率乘积；源码另有明确 safety 常数。**这不是 $D$ 的连续上界，也不是 reach 的下界。** 样本 `min_area>0` 不证明整面浸入。`complete=True` 指这一次完整有限责任已实际读取；源码同时保持 `continuous_geometry_certified=False`、`rigorous_quadrature_or_root_errors_paid=False`。不能把这些不同含义合并。

## 2. 真正使用的 phase 公式及固定握持区

令固定材料图为 $\theta_0=\Theta_0(\phi_0)$，$\rho_0=\Theta'_0>0$。在上活动半面，先把准确的零相位场写成材料角形式

$$
\widetilde F_0(s,\theta)=F_0\bigl(s,\Theta_0^{-1}(\theta)\bigr).
$$

沿用 [R248](../results/R248-finite-C2-phase-family-and-global-reductions.md) 的圆周作用，未标记全闭面为

$$
\overline F_\alpha=R_\alpha\overline F_0\circ\psi_{-\alpha},
\qquad
\widetilde F_\alpha(s,\theta)=R_\alpha\widetilde F_0(s,\theta-\alpha).
\tag{1}
$$

上下平帽使用同一个圆周作用的 Cartesian 延拓。由于平帽的准确映射与旋转等变，式(1)使帽上的每一个材料点固定。帽上再加既定的固定 p4 图 $B$，则

$$
F_\alpha=\overline F_\alpha+B,
\qquad S_\alpha=R_\alpha A\cup C,
\tag{2}
$$

其中 $A$ 是全部活动像，$C$ 是两个固定的已标记帽。采用既定 $\alpha\in[0,\pi/2]$ 时，也可将同一范围写成 $\alpha=\pi t/2$、$t\in[0,1]$；这只是参数记号，不增加独立时间插值近似。

这里必须区别：

- 当前求解自由量 $H_{\rm cap}$ 在选定一个候选后沿全部 $\alpha$ 固定；它不等于材料握持区 $H_{\rm grip}$ 的符号。
- 固定参考 seed 的旧高度也是既定来源参数；它不应代替该候选真实的 $H_{\rm cap}$。
- 当前 core 的逆图 $\Theta_c^{-1}$ 是零相位场内部的全变量组成部分；式(1)的材料图 $\Theta_0$ 仍完全冻结。不能随相位或精化重新选图来消去误差。
- 固定帽自身采用同一张固定图的诱导度量；高度的刚性平移不改变这张帽度量。安装 p4 图不能声称保留原平帽的 Euclidean 度量。

R248 的确给出活动部分相对固定旋转对称度量的谱误差、主曲率及未标记像几何在全部 $\alpha$ 上的归约；准确 $C^2$ 场即足以给强 $C^2$ 的时间连续性，不另加 $C^3$ 门。**它不使已标记的 $S_\alpha$ 都成为 $S_0$ 的旋转。** 固定帽一般不满足 $C=R_\alpha C$，所以 marked reach 不能只凭(1)宣称相位不变。

## 3. C²闭合、角圈和物理六jet先属于哪个对象

源的拓扑仍为两个活动半面在 core 反射接合，再接两个帽的闭球面。准确的径向域、原仿射节点、R690无限平尾、参考 supports、R711中央profile和 normal 的共同分段均属于完整数学定义。活动与帽端口遵循已有 R248、R708/R711 和 R715 的两jet条件；数值载体 $\widehat S,\widehat R,\widehat s_i$ 不能无误差地取代这些准确对象。

新隐式选择还必须给出全角同一分支的 $C^2$ 关联。固定共同32段并不自动证明逐角返回的数值根属于同一连续分支。R703/R707给出的逐段交叉 Jacobian、全上游误差、角一/二jet、相邻盒的根包围包含和周期/反射接点责任仍须真实支付。不能只核最后一段，也不能以两个根盒相交代替同分支包含。

准确几何消费者必须读取 R715 的**完整物理**场。令源码 $h=1-S_5(s/S)$，当前修正切向量为 $T$，数值总积分为 $Q_ST$，原始闭合差为

$$
\Delta=\Gamma-P+Q_ST.
$$

当前 `fields_torch` 实际返回

$$
F=(1-h)P+h\Gamma+Q_sT-(1-h)Q_ST,
\quad F_s=T+h'\Delta,
\quad F_{ss}=T_s+h''\Delta,
\tag{3}
$$

以及完整

$$
F_\phi=(1-h)P_\phi+h\Gamma_\phi+Q_sT_\phi-(1-h)Q_ST_\phi,
$$
$$
F_{s\phi}=T_\phi+h'\Delta_\phi,
\qquad
F_{\phi\phi}=(1-h)P_{\phi\phi}+h\Gamma_{\phi\phi}
+Q_sT_{\phi\phi}-(1-h)Q_ST_{\phi\phi}.
\tag{4}
$$

中心化根残差则是

$$
(\Gamma-\Gamma_0)-(P-P_0)+Q_S(T-T_{\rm ref}).
\tag{5}
$$

式(5)很小不表示原始 $\Delta$ 很小，更不允许从式(3)删去 $h'\Delta$。源码已经将二者分开记录，且明确 `working_radial_Gram_error_identically_zero=False`。后继的支撑、曲率、距离、度量和导出网格必须全部使用同一套式(3)–(4)，不能混用单位 $T$ 与带 lift 的 $F$。

## 4. 同场记录的最小完整身份

每个全域证书或部分覆盖 journal 都应保留以下真实内容；这是证据之间可合并的语义，不是要求先另跑一个资格测试。

1. 实际科学 report、完整 checkpoint 和当前自由点的字节摘要；指出 initial、accepted final 或某个 rejected trial 中究竟哪一点，不能靠目录名推定。
2. 完整 outer/normal/base/reference/Q/固定标量定义及各自 canonical identity；所有实际源角色，包括 calibration、C1 helper、包络 memory/rows/geometry。若实施新的 detached-matrix政策，它也是新的实际来源，不能假用 a62c 的旧报告身份。
3. 同一个固定 $g$、固定材料图、准确 $S/R$ 与仿射节点、全部 core/rotation/$H_{\rm cap}$ 字、准确 bubble/gamma/中央profile参数、共同 normal 分割和 root-policy。
4. 工作积分/三角/归约/旋转近似规则和准确对象之间的全部费用；同一准确目标不意味着不同工作载体或不同 reduction 的字相同。
5. 覆盖记录：每个准确径向片、闭角盒、端点、core反射及帽的责任；每个部分结果的生产者和输入摘要。两个批次的报告 SHA 可以不同，但它们合并时的**数学对象和实际工作点**必须一致。
6. $D_+$、$K_+$、支撑 $\sigma_-$、握持 $L_-$ 必须来自上述同一对象。旧 e3d/b788/6077/7ebb 的相似数值不构成合并依据。

正常表达式的源身份、工作缓存策略身份与固定度量身份是不同层。R714的值/C1复用不支付区间算术，也不让新的工作候选继承旧连续证书。

## 5. 全域六jet包围的输入合同

最直接的后继接口是每个准确参数盒返回

$$
\mathcal B=(I_s,I_\phi;\ [F],[F_s],[F_\phi],
[F_{ss}],[F_{s\phi}],[F_{\phi\phi}]),
\tag{6}
$$

其中每一个区间都包围整个闭盒上的准确物理量，而不只是端点或若干 Gauss 点。它还应给出如下证据范围：

- 全部原径向胞与新增真实解析分片的并集；包括旧前缀、cut/hold、深谷替换、全部 supports、中央profile接点及无限平尾到 $s=S$ 的准确极限。不能以预算或“幅度很小”为由漏掉尾片。
- $\rho_0$ 与当前 $\rho_c$ 的全域正性、当前 core 逆图及其两角jet费用；数值 Newton 的打印残差不能直接当作真实根距离。
- 参考均值、$v,d,w,\lambda$、全部中央profile矩、完整参考节点/整胞误差。R713及准确 mean producer目前按实际 batch 绑定，`complete`只指该请求覆盖；空 `requested_nodes` 不表示 normal 的所有积分节点已付款。
- 每一段 normal 根、交叉 $3\times3$ Jacobian、全上游 $u/A$ 误差、完整一/二角jet及与实际工作根的关联；使用 R707。只需要几何时不应无故重复全部优化 J/J*，但不能省去已定义隐式场本身的角jet责任。
- 全SO3指数/小分支截断、$\omega$的完整共享quintic、工作节点/宽度/权/归约、真实积分尾、calibration与原始 lift 的全部六jet费用。R715给出相应加减与传播账；seed费用单独通过不能冒称这些费用为零。

已有 a846/1371 等区间组件的纯代数可以复用；它们严格绑定的旧 hDelta/base/checkpoint 入口不能改标签后接受新 supported-reference/centered/envelope 报告。应独立完成真实来源适配，再调用原数学部分。

`remaining_boxes=0`只能在其精确期望片集合已经全部覆盖后出现。精度目标未达而仍有完整向外包围，是有效但可能不够紧的结果；尚有片未返回，则只保真实部分进展，不能用数值常量补齐。

## 6. 同一套包围可以同时产出的几何量

在上活动面使用与准确帽外法向一致的

$$
N=F_\phi\times F_s,\qquad w=|N|>0,
\qquad n=N/w.
\tag{7}
$$

下半面按准确反射及外向约定延拓。曲率绝对值不受同时反转法向影响，但正支撑判据受影响，因此不得以“曲率反正取绝对值”为由省略朝向核。

令

$$
G=\begin{pmatrix}F_s\cdot F_s&F_s\cdot F_\phi\\
F_s\cdot F_\phi&F_\phi\cdot F_\phi\end{pmatrix},\qquad
\widetilde B=\begin{pmatrix}N\cdot F_{ss}&N\cdot F_{s\phi}\\
N\cdot F_{s\phi}&N\cdot F_{\phi\phi}\end{pmatrix}.
\tag{8}
$$

这些是已有第一/第二基本形式的同场表达。可直接由(6)向外计算：

- **浸入：** 完整 $G\succ0$，或等价地足够的 $G_{11}>0,\det G>0$。
- **曲率：** 欲验证 $|\kappa_i|\le k$，可核
  $$kwG-\widetilde B\succeq0,\qquad kwG+\widetilde B\succeq0.\tag{9}$$
  因为真实第二形式为 $\widetilde B/w$，(9)正是对全部切向 Rayleigh 商的双边界。对两个 $2\times2$ 对称矩阵，可用两条对角与行列式的向外下界；包围相关性丢失只使判据保守。这并不要求求出每盒两个浮点特征值。
- **固定正定支撑：** 对一个沿整个场固定的 $\beta>0$、轴上中心 $c$，核
  $$A_\beta=\operatorname{diag}(1,1,\beta),\quad
  A_\beta(F-c)\cdot N\ge\sigma w.\tag{10}$$
  若每盒使用不同的 $\beta$，不能把所得局部下界拼成 R650 的同一全局 $A$。选择 $\beta$ 是证明参数，可以按真实场再选一次；它不改变原 $F$ 或 $g$。
- **完整直径上界：** 若活动部分 $|F|\le R_A$，同一准确帽半径为 $R$、高度为 $H_{\rm cap}$，则使用
  $$D_+=2\max\{R_A,\sqrt{R^2+H_{\rm cap}^2}\}+2h_b,\qquad h_b=1/1000.\tag{11}$$
  这是完整 marked $F_0$ 直径的上界，不是把预算 $4.2$ 当已返结果。也可用更紧的已有同场直径消费者，但必须包括两帽和标记。
- **整像见证距离：** 同一位置盒同时核到下节 $\{p,-p\}$ 的距离。它不需要再求一遍 normal 或主曲率。

第一基本形式与曲率也可按固定 $g$ 的正交标架缩放，减少坐标病态；缩放必须保留准确 $a(s)\rho_0(\phi)$ 及所有费用，不能把数值 `a_observations` 当全域准确函数。本文不要求在实际场未接近目标前先运行昂贵连续曲率。

## 7. 首选：R650一次支付全部物理phase

[R650](../results/R650-positive-definite-flow-support-reach.md) 对完整闭 $C^2$ 球面浸入、同一 $A\succ0$ 的正支撑及完整曲率界，给出嵌入和

$$
\operatorname{reach}(S)\ge
\min\{\sigma/\lambda_{\max}(A),1/K\}.
\tag{12}
$$

这条路线不需要先从别处假设全局单射，但其完整闭拓扑、浸入、连续外法向、正支撑和曲率都必须真实成立。

对活动像，$A_\beta$ 与 $R_\alpha$ 交换，且 $c$在旋转轴上，因此(10)、曲率与浸入从同一个准确零相位活动场转到所有 $\alpha$。固定帽则始终是同一 $C$，单独付其组件界。**这正是固定帽情形的全t推理；不是 marked image 旋转恒等式。**

沿用既定 R661 四个 p4 标记，若真实 $H_{\rm cap}\ge1$、$R>1/5$，该组件已经给 $\beta=1/4,c=0$ 时

$$
K_C\le5,\qquad\sigma_C\ge64/267.
\tag{13}
$$

这只复用明确帽函数的解析结论；不借旧6077活动场的数值。令

$$
K_+=\max(K_A,5),\qquad
\sigma_-=\min(\sigma_A,64/267),\qquad
\tau_*=3D_+/100.
\tag{14}
$$

对 $A_{1/4}$，$\lambda_{\max}=1$。若真实同场返回 $\sigma_-\ge\tau_*$ 与 $K_+\tau_*\le1$，则全部 $\alpha$ 的 reach 达到 $0.03D$，其中课题的 $D=\operatorname{diam}F_0(M)\le D_+$。没有必要再用许多独立时间采样重复这一已付归约。

这也说明为什么后继 K 任务应消费真实 $D_+$，而非沿用历史 $D\approx4.10$ 或希望的 $D\le4.2$。若同场更紧的 D 上界改善，K目标随之合法改善；若 D 变坏，旧K目标即不足。

## 8. 支撑不足时：完整空间对与混合phase的接口

支撑条件是充分条件，失败不说明当前场自交或本课题无解。可继续使用 [R11](../results/R11-exact-all-phase-normal-chord-reduction.md)、[R62](../results/R62-continuous-all-phase-mixed-normal-balls.md) 及 R241/R280–R282 的完整点对覆盖。其几何分组是：

1. 活动—活动：两个点在同一物理 $\alpha$ 下共同旋转，因此回到零相位全部活动点对，仍含上下半面、core及所有近邻/远邻。
2. 固定帽—固定帽：两个点及法向均静止。
3. 活动—固定帽：只有活动端旋转，必须支付真正的混合phase责任。只检查 $\alpha=0,\pi/2$ 不够。

第三类可把两个完整空间块包围成位置/单位法向球，并在全圆上消去相位。沿 R11 记旋转端中心 $(x,z),(a,c)$、固定端中心 $(y,w),(b,e)$，$J$是水平四分之一转，$\Delta_z=w-z$，

$$
A=|x|^2+|y|^2+\Delta_z^2,\quad B=y\cdot x,\quad C=y\cdot Jx.
$$

旋转端使用 $(d_0,d_c,d_s)=(\Delta_zc-x\cdot a,y\cdot a,y\cdot Ja)$，固定端使用 $(y\cdot b+\Delta_ze,-x\cdot b,-Jx\cdot b)$。两端、两个符号的四个中心余量为

$$
M_{\nu,\varepsilon}=A-2\tau_*\varepsilon d_0
-2\sqrt{(B+\tau_*\varepsilon d_c)^2+(C+\tau_*\varepsilon d_s)^2}.
\tag{15}
$$

真实块的位置误差合计 $e_x=e_p+e_q$，该端单位法向误差为 $\eta_\nu$，并有中心弦长上界 $D_c$ 时，R62要求实际向外支付

$$
M_{\nu,\varepsilon}\ge
2D_c(e_x+\tau_*\eta_\nu)+2\tau_*e_x.
\tag{16}
$$

原球中心不必恰好单位，但真实法向必须单位。若采用 R62 的 quartic 排除双法向分支，则必须包括整个半角实线及 $\alpha=\pi$，不能以抽样代替根/符号责任。距离 $\ge2\tau_*$ 的完整块对可用既有距离门；同帽图可用已有 Hessian/凸坐标片公式。

覆盖消费者应为每一对准确材料片明确返回以下某一已证明分支：全距离门、完整双端正常弦、严格 no-double-normal、或包含接缝的局部图/曲率分支。接缝的两侧参数片不能因不同标签就被当作远离对；R282的 joint chart/cross-Gram 正是处理这类责任的既有入口。近对角局部项、帽边界、同一点的多个参数表示及全部未决片必须显式保留。

正常弦不等式在零弦处会变成 $0\le0$，故仅得到这些不等式不能偷偷证明参数场单射。若不用 R650，应由 R241等的覆盖/单射论证或真实的非局部正分离另付嵌入。这里的“全t”始终是同一个物理phase作用于同一成员的两点；不是把两个不同时刻的曲面点任意混成reach定义。

## 9. 固定握持区、完整像幅度与非轴对称见证

按当前真实 core 的全部系数定义

$$
r_0=1+\sum_{j=1}^{M}c_j,
\qquad F_0(0,0)=(r_0,0,0),
\qquad p=R_{\pi/2}F_0(0,0)=(0,r_0,0).
\tag{17}
$$

当前准确逆图在该轴上与固定图相容，故 p 是真实相位活动像上的点，不是仅一条材料点位移。沿 [R659](../results/R659-complete-image-held-amplitude-for-the-same-closed-candidate.md) 的**一般见证推理**，若同一新场的完整位置盒给

$$
\inf_{q\in A}|q-p|\ge L_A,
$$

并给固定帽距离 $L_C$，则 $L_-=\min(L_A,L_C)$ 满足

$$
\delta_{\rm hold}\ge\operatorname{dist}(p,S_0)\ge L_-.
\tag{18}
$$

四分之一角对单一 p 不闭合，所以位置消费者仍须同时读 $p,-p$ 两个符号，再用实际反射/半转对称覆盖整角。帽不能省略：一般高度扰动界给 $L_C\ge H_{\rm cap}-h_b$；对已明确的向外p4帽和 $p_z=0$ 可直接用 $L_C\ge H_{\rm cap}$。后者不需要假设整个活动面处于两帽 slab 内。

若 $R\ge9/20$，可取上下两个固定帽内半径 $9/20$ 的材料盘作为 $H_{\rm grip}$。R661标记支撑位于半径 $1/5$ 内，外缘未动的两反向点给

$$
\operatorname{diam}F_0(H_{\rm grip})\ge9/10.
\tag{19}
$$

因此该选法要支付的同场充分不等式是 $L_-\ge D_+/5$ 和 $9/10\ge D_+/5$，加上握持盘实际位于帽内。数值优化的 $4.2/.9/1.01$ 是明确工作预算；只有实际连续返回能把它们变成完成指标。

**同一套(6)位置盒确实能同时提供新场关于该相位轴的非不变见证：** 若(18)得到 $L_->0$，则 $S_{\pi/2}\ne S_0$，甚至达到题目幅度时已有更强变化。这不用另造核心对核心点云或有限相位试验。它仍不是含反射的非全等证明。

## 10. 含反射非全等：可以复用什么，不能复用什么

沿 [R238](../results/R238-planar-germ-marker-rigidity.md)，固定四个互异支撑半径、仿射独立支撑圆心的 p4 图，在**完整活动环带无平面开片**且闭嵌入的条件下，迫使任何成员间欧氏全等为恒等，包括反射。再由(18)的真实像变化，得到 $\delta_E>0$。R238的紧性论证已经把“没有达到零的刚体变换”加强为商Hausdorff距离严格正，不需重做。

R661的帽半径/分离/仿射独立/局部支撑曲率结论可按同一明确配方复用；其6077活动场的922胞有限多项式非零系数检验，**不能**迁给 a62c 的指数旋转、准确参考积分和隐式 normal 根。新的高度函数已不是该旧有限 Fourier–quintic 系数表。

同一连续六jet盒还可以给无平面开片所需的真实几何证据。例如在被完整负责的活动开片上证明第二基本形式的某一分量非零，就排除该处平面胚；或为确实适用的解析片非恒零判据提供实际非零点/四点证据。两点必须保留：

- K上界、D上界、正支撑本身都不排除平面开片。大圆帽就是反例；不能由 R650 已过顺手宣布标记唯一性。
- 仅每胞某一点的非零曲率，若没有该**新表示**的解析片及非恒零延拓责任，不覆盖该胞别处的平面开集。旧R661的多项式恒等论证不能只改文件名复用。准确帽端二阶平坦也使含端点闭盒的统一非零下界通常不可用；应保完整开片/端段解析责任，不能删除平尾。

所以适合与后继六jet消费者同时保存的是：覆盖片身份、可复用的准确第二形式区间、真实非零见证及其证明范围；是否足够支付 R238 由该完整新场的适用条件决定。本文没有预填“已无平面开片”。

[R625](../results/R625-second-volume-moment-quotient-bound-and-fixed-caps.md)的完整体积二阶矩可作为另一条既有充分路线，但其式(3)明确要求固定新增实体也半转对称。现 R661 的三个上帽、一个下帽且半径互异的图案不满足该假设，不能照抄其 $A_2+B_2$ 相位公式。若走完整矩路线，应真正支付适用的同场矩公式/误差和固定帽假设，不为省这项责任悄悄换 g 或标记。

## 11. 与共同度量及真实精化的交界

R248的材料作用对旋转对称活动度量是等距作用；因此完整准确零相位的相对谱误差上界可一次归约全部phase。固定帽的自身公共度量也不随phase变化。这消除了无意义的独立时间插值门，但并不代替整个活动面、所有准确尾、隐式根和浮点误差的支付。

后继 mesh/M/N 加密必须比较同一已冻结 g、准确参考seed、材料图、参数范围与数学选择机制。共同 normal 分段是所选场定义的一部分；改变32段或更换seed/profile是明确新输入，不能把新问题的较小残差记成旧问题已精化。工作积分加密与准确模型区分、同父测度下的误差、全部历史地点责任仍按既有规则保持。

多phase网格导出可以直接用(1)–(2)，但导出器也必须包含固定p4帽、下半面、core/cuff缝和完整真实物理场。点云或三角网的数值证据不自动成为光滑场reach或严格存在证明。

## 12. 可以紧接真实扫描的执行次序与紧凑返回

当前只等待实际包络场返回，不要求先跑未运行的plain R711场。后续可按真实剩余误差决定工作：

1. 从真实报告读取同点有限全域筛与完整来源；失败也保新地点及明确失败责任。没有 final 不虚填 final checkpoint。
2. 对有希望的真实点，独立严格来源适配参考费用、normal-chain/整胞六jet入口。一次(6)流式同时积累 D、L、支撑、浸入与曲率条件；不要为各标量重复解同一根。
3. 以实际同场 $D_+$ 决定 $\tau_*$ 和 K目标，先尝试已有固定 $A_{1/4}$ 全支撑路线。若它未给充分界，保其真实返回并转更合适的固定证明参数或完整点对路线，不把充分判据失败宣布为物理不存在。
4. 同一准确位置/第二形式盒可支付握持见证，并积累新场标记唯一性所需的真实证据；非全等的额外适用责任保持明确。

建议消费者的紧凑公开字段为：实际 report/checkpoint/model/source identities、准确cover identity、expected/covered/remaining片数、全尾是否包含、$D_+,L_-,\sigma_-,K_+$及其准确有理端点、固定 $A,c$、caps recipe、$\tau_*$、浸入/全phase适用分支、完整空间pair责任是否关闭，以及每项未付费用。所有大逐胞/逐pair原始记录保 runner 并由完整脚本/参数/run/SHA再生，不重新复制进Git。只返回期望阈值而没有实际覆盖与上界的summary不能颁发证书。

## 13. 本次完整源码读本

以下是本次核对的真实物理/筛查来源，不是未来未知候选的预填身份。路径均在 `scripts/resume_20261126/`。

| 完整文件 | 字节 | SHA256 |
|---|---:|---|
| `so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py` | 95491 | `a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd` |
| `reference_centred_c1_smooth_triangle_calibration.py` | 11893 | `3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991` |
| `so3_supported_smooth_triangle_meridian_operator.py` | 40771 | `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865` |
| `supported_smooth_triangle_meridian_reference.py` | 39728 | `0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b` |
| `so3_reference_centred_c1_material_envelope_geometry.py` | 65678 | `bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f` |
| `complete_material_envelope_memory.py` | 40091 | `c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152` |
| `complete_material_envelope_rows.py` | 13744 | `729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7` |

本次只做文字、来源和公式接口核查；没有本地 scientific import、F/J/根/区间运行，没有修改现行科学入口或分支引用，没有给尚未返回的新场授予任何连续证书。
