# 把 R227 接到当前完整闭场：诱导联络的二阶差与几何责任

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。**状态：已有定理的应用说明及最小区间消费者设计；没有新科学执行，没有新候选曲率证书，不另占 R683。**

定向检索发现 [R227 §2](../results/R227-hermite-seam-general-reference-hessian.md) 已证明所需完整曲率扰动定理。取其中的工具度量为基场的实际诱导度量，旧 Gram 误差为零、旧切向协变 Hessian 为零，即得本次所需的界。本文只说明这个准确特例怎样消费当前六 jet、哪些差可以廉价形成，以及如何与 [R662](../results/R662-complete-closed-C0-difference-and-inherited-size-amplitude.md)、[R665](../results/R665-continuous-C1-normal-cone-transfer-and-complete-immersion.md)、[R667](../results/R667-same-angle-C1-transfer-and-complete-closed-embedding.md)、[R650](../results/R650-positive-definite-flow-support-reach.md) 衔接。worker03 的实际完整 K 仍由其原任务负责；这里不填写尚未返回的 K。

## 1. 工具度量与任务固定 g 分开

在同一正则参数图上，设 $F_0,F_1$ 是 $C^2$ 场，其中 $F_0$ 已是浸入，$F_1$ 尚不预设浸入。记 $\Delta=F_1-F_0$，

$$
J_i=DF_i,\qquad G_i=J_i^TJ_i.
$$

$G_0$ 是本次比较所用的**工具度量**，不替换课题一直保持的目标 $g$，也不宣称基场对目标 $g$ 已等距。即使当前相对 Gram 很小，也不能把两者的 Christoffel 符号混用；点态小 metric 误差没有自动控制其导数。R227 §3 的反例已经说明漏掉这项费用的危险。

若在一个完整连续盒内对所有切向量 $v$ 有

$$
|D\Delta v|\le\epsilon |DF_0v|,\qquad 0\le\epsilon<1,
\tag{1}
$$

则三角不等式给

$$
(1-\epsilon)^2G_0\preceq G_1\preceq(1+\epsilon)^2G_0.
\tag{2}
$$

因此新场在该盒浸入。$F_0\in C^2$ 只要求 $G_0\in C^1$，其 Levi-Civita 联络系数连续，已足够定义连续的 $\nabla_0^2\Delta$；没有额外要求 $F_0\in C^3$。

在坐标分量上写 $B_i$ 为实际第二基本形式，取任意一致单位法向 $n_i$。准确有

$$
\nabla_0^2F_0=B_0n_0,
\qquad
B_1=(n_1\cdot n_0)B_0+n_1\cdot\nabla_0^2\Delta.
\tag{3}
$$

第二式只因从 $D^2F_1$ 减去的 $\Gamma_0DF_1$ 属于新切平面而消失。它把旧场普通二阶导中可能很大的切向重参数化部分准确消去。若

$$
|\nabla_0^2\Delta[v,v]|\le\eta\,G_0(v,v)
\tag{4}
$$

且同一盒上的基场实际欧氏主曲率绝对值至多 $K_0$，则 R227 直接给

$$
\boxed{K_1\le\frac{K_0+\eta}{(1-\epsilon)^2}.}
\tag{5}
$$

这里不需要先证明 $n_1\cdot n_0$ 为正，因为其绝对值至多 1。只控制普通 $D^2\Delta$ 而遗漏 $\Gamma_0D\Delta$，或只知道旧曲率 K 而没有基场的联络数据，都不足以消费 (5)。本文不重新认领 R227 的证明。

## 2. 完整六 jet 如何构造真实联络

使用同一个旋转正交架存储向量，但其导数必须是已含架转动的真实 Cartesian 导数。沿已刊核的名称置

$$
V=F_{0,s},\quad T=F_{0,\phi},\quad
A=F_{0,ss},\quad B=F_{0,s\phi},\quad C=F_{0,\phi\phi}.
$$

记

$$
e=V\cdot V,\quad f=V\cdot T,\quad g=T\cdot T,
\qquad w^2=eg-f^2=|T\times V|^2>0.
$$

在每一个同径向、同角连续盒内，直接用六 jet 构造

$$
G_0^{-1}=\frac1{w^2}\begin{pmatrix}g&-f\\-f&e\end{pmatrix},
\qquad
\begin{pmatrix}\Gamma^s_{ab}\\\Gamma^\phi_{ab}\end{pmatrix}
=G_0^{-1}\begin{pmatrix}V\cdot F_{0,ab}\\T\cdot F_{0,ab}\end{pmatrix},
\quad ab\in\{ss,s\phi,\phi\phi\}.
\tag{6}
$$

这是诱导连接的准确公式，不需要对已成盒的 G 作有限差分。把实际差场六 jet 记为 $dV,dT,dA,dB,dC$，先形成

$$
H_{ss}=dA-\Gamma^s_{ss}dV-\Gamma^\phi_{ss}dT,
$$
$$
H_{s\phi}=dB-\Gamma^s_{s\phi}dV-\Gamma^\phi_{s\phi}dT,
\qquad
H_{\phi\phi}=dC-\Gamma^s_{\phi\phi}dV-\Gamma^\phi_{\phi\phi}dT.
\tag{7}
$$

三者就是 $\nabla_0^2\Delta$。所有 dot、乘法、除法及尾项在**同一物理盒**内向外处理。全角最大普通 Hessian 与全角最小面积可以给保守上界，但会损失相关性；它们不能冒充同一角的实际 jet。式 (7) 中连接项会有真实抵消；先做其有符号区间表达再取范数。若盒宽仍导致过松，可细化该未付盒；不靠反复调任意数值阈值取得成功旗。

### 2.1 归一化到基场真实第一形式

为避免小 $\rho$ 区域中原参数长度的错配，使用准确参数矩阵

$$
P=\begin{pmatrix}
e^{-1/2}&-f/(\sqrt e\,w)\\
0&\sqrt e/w
\end{pmatrix},\qquad P^TG_0P=I.
\tag{8}
$$

一阶归一差的两列为

$$
d_1=\frac{dV}{\sqrt e},\qquad
d_2=\frac{e\,dT-f\,dV}{\sqrt e\,w}.
\tag{9}
$$

对 $Q_{ij}=d_i\cdot d_j$，可直接向外包围

$$
\epsilon^2=\lambda_{\max}(Q)
=\frac{Q_{11}+Q_{22}+\sqrt{(Q_{11}-Q_{22})^2+4Q_{12}^2}}2.
\tag{10}
$$

更保守的 $\epsilon\le\sqrt{|d_1|^2+|d_2|^2}$ 也有效。两式都用基场实际第一形式，而不是令 $e=1$、$f=0$、$g=a^2\rho^2$。

令 $U=P^THP$，其三个独立分量是 $\mathbb R^3$ 向量：

$$
U_{11}=H_{ss}/e,\qquad
U_{12}=(H_{s\phi}-(f/e)H_{ss})/w,
$$

$$
U_{22}=\frac e{w^2}
\left(H_{\phi\phi}-2\frac f e H_{s\phi}+\frac{f^2}{e^2}H_{ss}\right).
\tag{11}
$$

对任意单位 $z\in\mathbb R^2$，$\|zz^T\|_F=1$，所以一个完整而便宜的初版上界为

$$
\eta\le\sqrt{|U_{11}|^2+2|U_{12}|^2+|U_{22}|^2}.
\tag{12}
$$

可另对每个 Euclidean 分量的 $2\times2$ 对称矩阵取准确算子范数，再把三个范数平方和开根，并与 (12) 取小。这是同一真实张量的两个合法上界，不要求新增方向采样。若已有可靠 $n_1$ 同盒，还可包围法向投影 $n_1\cdot U$ 的算子范数，直接给 (5) 分子中较尖的法向费用；此时该费用不再宣称满足完整向量条件 (4)。最小初版不依赖这项优化。

## 3. 现有核实际提供什么、缺什么

下列是静态读码所得的准确接口范围；没有调用这些科学模块。

| 已刊源 | 当前可复用对象 | 当前缺少的对象 |
|---|---|---|
| `fullclosed_C0_difference_interval.py`，`f3b5acf1…` | 准确同节点两场 jet 差；派生 core-T 差先按实线性式重建；合并高度后的 Hermite/Bernstein 控制点；完整像 C0 界 | 无二阶协变差、无 Γ0 |
| `fullclosed_C1_support_transfer.py`，`ec21d857…` | 完整 core/解析 lift 一阶差预算；基场完整 Laurent 与全部尾项 | 无 AA/VT/EE 差，也无归一 η |
| `fullclosed_C1_support_transfer_angles.py`，`2df72750…` | 同角有符号 $V,T,dV,dT$ 盒和 R667 支撑传递，保未显式变换的全部高模 | 无第二 jet 差接口 |
| `actions_closed_curvature.py`，`8ca81fee…` | `CurvatureReader.piece_definitions(..., include_position=True)` 和 `field_blocks` 给完整 $X,V,T,AA,VT,EE$；同角低模、全部有限高模和完整解析余项 | 无 pair 差核；输出逐胞 K 不是 Γ0 数据 |
| `exact_reference_tail_interval.py`，`f1220a2e…` | `profile_controls`、`piece_definitions(mode='curvature')`、`_field_batch`、`blocks` 给非零 R671 完整五个导数向量及标量余项；`first` 给 X | 无 pair 直接 Δ-sixjet 入口；same model 不等于 same core |

R672/R674 的 $AA,VT,EE$ 已是正确 world 导数在同旋转架中的分量，消费 (6)—(11) 不再补一次架连接项。

未来实际已返 baseK 的逐胞上界可以直接用于 (5)，但报告中的 K、E、$w^2$ 摘要一般没有保全部有符号六 jet。因此 Γ0 仍须由该**实际基场**在需要的同角盒读取，或消费具有同身份/同完整盒范围的真实缓存。这是新增的连接数据，不是重跑旧 K 结论。不能从曲率很小推断普通 Hessian 或 Γ0 很小。

## 4. 差场先在共享系数中形成

### 4.1 同模型、同 core 的廉价分支

同 exact scalar、径向节点、R/S/width、$\lambda/\eta$，且所有 core 系数准确相同，则解析水平 lift 完全取消。原模型使用 $h=\chi$，R671 使用同一个准确分片 quintic $h_\lambda$，于是

$$
\Delta F=\Delta q+h\,\Delta H\,e_z.
\tag{13}
$$

在控制点先合并 $\Delta q_{Z_0}+h\Delta H$，再求其一、二径向导数和完整角导数。这一分支的水平差不需要再付独立的 a/I 或 circle 余项；共同的 k 也准确取消。基场自身的六 jet 仍必须保全部解析 lift。

### 4.2 同模型但 core 改变

用复数表示旋转架内水平向量，置

$$
z_i=e^{i\delta_i},\quad R_i=\rho_i z_i,
\quad C_i=(-\rho_i^2+i\rho_i')z_i.
$$

则差的水平 lift 六项分别为

$$
f\Delta z,\quad f'\Delta z,\quad if\Delta R,
\quad f''\Delta z,\quad if'\Delta R,\quad f\Delta C.
\tag{14}
$$

准确有

$$
\Delta z=z_0(e^{i\Delta\delta}-1),\qquad
\Delta R=\Delta\rho\,z_1+\rho_0\Delta z,
$$

$$
\Delta C=
\bigl[-(\rho_1+\rho_0)\Delta\rho+i\Delta\rho'\bigr]z_1
+(-\rho_0^2+i\rho_0')\Delta z.
\tag{15}
$$

这些公式保 core、rho、rho-prime 全链。可以先用 R665 的准确有限系数和单位圆 Lipschitz 差得到保守全尾，再按 R672 的同角 Laurent 框架收紧。若构造 $e^{i\Delta\delta}-1$ 的 Taylor 差多项式，应让零差确实给零余项；将两个大 circle 盒分别相减会丢掉共享部分。

例如已付 $|z_0-P_0|\le t_0$、$|(e^{i\Delta\delta}-1)-D|\le t_\Delta$、$|\Delta\delta|\le d$ 时，

$$
|\Delta z-P_0D|\le t_0(d+t_\Delta)+t_\Delta.
\tag{16}
$$

它只用 $|z_0|=1$ 和 $|e^{it}-1|\le|t|$；全部 Laurent 支撑及高模仍须保留或付正尾界。此处给的是可实现分解，没有新运行。

### 4.3 跨 R671 参数或表示

若 $\lambda$ 或 $\eta$ 改变，(13)—(14) 的共同 profile 取消不再成立。应为两个实际 canonical 模型分别绑定 $f_i,h_i,k_i$，先形成

$$
f_1z_1-f_0z_0=(f_1-f_0)z_1+f_0\Delta z,
$$

$$
\Delta(hH+k)=(h_1-h_0)H_1+h_0\Delta H+(k_1-k_0),
\tag{17}
$$

并保其至二阶真实径向导数。不同 $\eta$、FullHold 分片和 $\chi$ 断点取共同准确分割；不能按一方的 cell 类型省略另一方的活动 lift。原模型可作为 $f_0=\chi(R+S-s),h_0=\chi,k_0=0$ 消费，但旧 original reader 不能据此直接解释非零 R671。

若只是 $M$ 改变，可按 R678 的准确物理槽包含到共同频率列表；若径向 mesh 改变，需 R676 的准确共同限制及其已声明 carrier 舍入费用。S/R 或原目标 scalar 改变时，此最小同参数消费者不继续冒同 g；必须先有明确共同域及目标责任。byte 相同的 observation carrier 或近似相同的 H 均不能替代 canonical 模型身份。

## 5. 首 jet、支撑和 C0 的组合

R227 的法线比较直接给本次一个可供 R665 支撑式消费的角预算。由 $n_1\perp DF_1$，对旧单位切向量 $DF_0v$，

$$
|n_1\cdot DF_0v|=|n_1\cdot D\Delta v|\le\epsilon.
$$

故新旧法线夹角满足 $\sin\vartheta\le\epsilon$。沿 $F_0+t\Delta$ 的局部浸入连续选向，在 $\epsilon<1$ 时可取 $\cos\vartheta\ge\sqrt{1-\epsilon^2}$。这只是使用 R227 已付的一阶结论，不要求曲率比较先选锐角。

固定同一个 R650 矩阵 A 和中心 c。若同盒已有

$$
(A(F_0-c))\cdot n_0\ge s_0>0,\qquad
|A(F_0-c)|\le U_0,\qquad |A\Delta|\le d_A,
$$

R665 的法线锥式立即给

$$
s_1\ge s_0\sqrt{1-\epsilon^2}
-\sqrt{U_0^2-s_0^2}\,\epsilon-d_A.
\tag{18}
$$

也可直接消费已对**当前候选**付清的 R667 支撑下界，或取同域多个合法下界之大，不为形式统一重复读取。对 $A_\beta$、$0<\beta\le1$，R665 的半径上界可取 $U_0\le R_0$；通常同角局部界比把不相关全角极值拼在一起更有用。

R662 的完整像差 $d_H(S_0,S_1)\le d_0$ 给

$$
D_1\le D_0+2d_0.
\tag{19}
$$

若基场真实全闭目标的活动见证已有距离下界 $L_0$，新见证移动至多 $d_p$，则

$$
\operatorname{dist}(p_1,S_1)\ge L_0-d_0-d_p.
\tag{20}
$$

当前 core 见证的 $d_p=|\sum_m\Delta c_m|$ 可用准确 Fraction 求；same core 时为零。式 (20) 消费的是包含镜像与帽的完整目标集合，不把固定 p 的对称性从支持量对称性推来。

## 6. 帽、镜像和共同参数图的限制

曲率公式逐同参数图成立。body 的两场可以在同 $(s,\phi)$ 上比较；core 改变时，它们的材料角 $\Theta_i(\phi)$ 也改变。因而不能把这个 body 配对未经说明延成跨盘极点的全局 $C^2$ 差场。

最小完整几何消费者可以逐 body 图应用 (5)，同时按各场已刊准确 cuff 迹在 **Cartesian 圆盘图**上独立支付帽和 marker。原 affine 接口及 R671 的完整端口公式必须属于各自真实模型，C² 接缝不从胞内差界推出。R662 已明确 body 同角与 cap 同 Cartesian 的 Hausdorff 配对不必在 seam 一致；这是集合距离的合法配对，不能混成二阶差的共同图证明。

- 固定帽和 marker 若在同一 Cartesian 图中逐字相同，其 $\Delta$ 和两 jet 为零。
- 若只改变帽高 $H$，同一盘/marker 的变化是常向量 $\pm\Delta H e_z$：其一二阶差为零，曲率不变，支撑及直径仍须用新 H。
- 若 marker profile、盘半径或 chart 本身改变，须为其真实变化单独包围；不能自动拿旧 cap-K/support。
- 反射使用同一 Euclidean 正交矩阵时，诱导形式、差张量范数及绝对主曲率保持，方向符号按当前共同外向取向处理。原镜像 seam 仍须是实际两场各自的完整 C² 接缝。

若确实要在一个全闭共同 atlas 上直接比较两个场，则必须给出明确的 chart 识别及其完整两阶链式项；本文的最小接口选择 body 逐图加帽独立处理，避免把退化极坐标当正则盘图。

## 7. 从当前候选到全时间 reach 的责任清单

R227 只给浸入与局部曲率预算，**不传递全局嵌入或 reach flag**。当前新场要消费 R650，仍由同一实际候选的以下对象组合：

| 责任 | 可消费来源 |
|---|---|
| 完整闭球面、准确 C² 端口和盘图 | 当前 original/R671 的完整场定义 |
| body 浸入 | 全部连续盒的 (1)—(2)，或已有同候选完整首 jet |
| 同 A,c 的正支撑 | 当前 R667/直接首 jet，或逐盒 (18)，再合帽/marker |
| 全闭实际 K 上界 | 逐盒 (5) 的全覆盖，合独立帽/marker |
| 完整 D 上界、held 见证、grip | R662/已有同候选连续位置界及准确固定握持结构 |
| 全相位 | R248 的准确族、R650 的活动旋转交换性及固定帽/marker 输入 |
| $\delta_E>0$ | 当前候选的准确非平面与四 marker 责任，不能从 C² 接近直接继承 |

对本次已刊 p4 marker 接口，在其原假设 $\beta=1/4,H_1>1,R>9/20$、marker 高 $h=1/1000$、profile/支撑区域确实不变时，可继续用既有准确常数

$$
\overline D_{1,\rm marked}=\overline D_1+2h,\quad
\sigma_{1,\rm marked}=\min(\sigma_{1,\rm body},64/267),\quad
\overline K_{1,\rm marked}=\max(\overline K_{1,\rm body},5).
$$

同完整闭面假设下，R650 给

$$
\frac{\operatorname{reach}}D\ge
\frac{\min(\sigma_{1,\rm marked},\overline K_{1,\rm marked}^{-1})}
{\overline D_{1,\rm marked}}.
\tag{21}
$$

held 可沿已有组合器取 $\min(L_0-d_0-d_p,H_1-h)$ 为保守分子，grip 用已有准确 $9/10$；各自除同一个标记后 D 上界，与 $1/5$ 比较。reach 比较用准确 $3/100$，不新增 .98 等人为余量定义。给定候选的连续区间端点按原模型准确解读并使用 Fraction 比较。

若想先看这条传递是否有足够预算，令 $\tau=(3/100)\overline D_{1,\rm marked}$；每盒需要的充分曲率余量是

$$
\eta\le(1-\epsilon)^2/\tau-K_0.
\tag{22}
$$

右端非正只表示当前基界与这条传递式不能支付目标，不证明新真实曲率违反目标。可用更尖的同域界或直接新场 K 界；不把失败的充分条件转成求解器新的科学门。metric $10^{-6}$、固定 g 的持续精化和导出文件始终是独立责任。

## 8. 最小区间消费者设计与报告

建议一个独立 `CovariantDifferenceReader`，不改已刊核。它接受实际 base/candidate bundle、各自模型/节点/scalar 来源、已返回 base 曲率报告，以及可选同身份的首 jet/C0/support 资料。

```text
blocks(cell, shared_partition)
  -> base: X,V,T,AA,VT,EE
     delta: dX,dV,dT,dAA,dVT,dEE
     exact_domain, all_finite_modes, analytic_and_scalar_remainders

covariant_bounds(base, delta)
  -> actual G0, Gamma0, normalized first difference,
     normalized covariant second difference, epsilon_upper, eta_upper

cell(cell)
  -> all-box K1 upper, immersion scope,
     optional support/C0 transfer, unresolved boxes and their actual reason
```

优先复用 R667/R672 同角分块与 R674 profile 控制点，所有新增 pair 差先在共享系数中形成。胞、lift piece、径向子盒、角区间的并须完整覆盖所声明域；只细化未付或目标未够的盒。base 的 per-cell K 可合法用于其所有子盒，已有 base E/$w^2$ 下界也可与同基场新局部盒相交；不同 candidate 的下界不能冒作同场相交。

报告最少保留 base/candidate/模型与源 SHA、完整域范围、实际 $K_0$ 来源、各盒 $\epsilon,\eta,K_1$ 及尾项费用、body/cap/marker 各自责任。若某些 baseK 胞尚未返回，可先记已有合法子域，但未付胞不能从别处取最大值填满。只有新候选全域真实付清，才给对应全域 K/支撑结论；reach 用 (21) 另行准确组合，不复制旧 `geometryflag`。

普通数值六 jet 可以用于诊断，不能填进向外证书的同名字段。严格版本继续沿 R672/R674 已声明的 IEEE 向外模型、准确有理节点/宽度、完整 Laurent 支撑及所有 scalar 余项。本文没有实现新科学程序，没有试读胞、没有重扫旧父，也没有把未来完整 baseK 预写成已知。

## 9. 本次实际静态读取的源码身份

下列文件均在 `scripts/resume_20261120/`，仅检查源码和文件元数据，没有导入或执行科学模块。

| 文件 | SHA256 |
|---|---|
| [fullclosed_C0_difference_interval.py](../scripts/resume_20261120/fullclosed_C0_difference_interval.py) | `f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0` |
| [fullclosed_C1_support_transfer.py](../scripts/resume_20261120/fullclosed_C1_support_transfer.py) | `ec21d8575ad2d121d04beaa2b7ebc1902c0b7604c0dfaf8777610ad27f616200` |
| [fullclosed_C1_support_transfer_angles.py](../scripts/resume_20261120/fullclosed_C1_support_transfer_angles.py) | `2df727509871b604e8c359fb78484f88eb513372c8ca78eb7da8e9cd174b058b` |
| [actions_closed_curvature.py](../scripts/resume_20261120/actions_closed_curvature.py) | `8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385` |
| [exact_reference_tail_interval.py](../scripts/resume_20261120/exact_reference_tail_interval.py) | `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225` |

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
