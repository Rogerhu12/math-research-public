# 完整 normal 场的闭面、物理相位与握持证据：源码端口符号核查

2026-11-27，Astra-larger-e4e2a2bf-20261126 / solver。

**状态：既有完整源码与 R248/R650/R661/R715/R716 的适用接口核查；没有新的科学执行、连续包围结果或完成证书。** 本文把完整上半面已经支付的条件准确接到下反射、两帽、固定 p4 标记、全相位支撑、reach 和握持量。它不重证既有定理，不把候选的有限筛查当连续证据，不另设求解前门。完整可执行闭面消费者由 construction 实施；本文给它可直接实例化的端口和逐项身份关系。

## 1. 核读对象和不可混用的三层身份

实际核读的完整源如下。

| 对象 | 完整 SHA256 |
|---|---|
| 原完整 base，6a803，40771 B | 6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865 |
| 当前公开解析 frame normal，3d8d，96558 B | 3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc |
| 新完整 closure-value normal，6d2b，98421 B | 6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4 |
| 准确 whole-radial/角盒源，0587，45392 B | 0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b |
| 完整准确 normal 32段及全角入口，f5ec，40268 B | f5ecc7fb67d4c34d5c52cba16ba0cee94b8fb5872f14c67123a190b32c6450c1 |
| 完整点/packet 输入，f080，26431 B | f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82 |
| 完整闭参数面矩读取器，19e4，57152 B | 19e4ab31976615b12d002a6ef26c15973859fc4268134b5fd61676206e9c11b4 |

3d8d 与 6d2b 的物理 sixjet 表达、变量布局、径向矩阵、参考、全部共同 normal 阶段未因值缓存而改变。新 6d2b 的闭合 wrapper 仍返回完整原式，所有阶段末与最终 endpoint 重读强制走原积分；其完整再生器及证明另列于 closure-value 交付清单。**这不授权把 3d8d 的实际 report 或准确费用改标签移给 6d2b。** 后继必须逐字绑定它实际采用的 outer、normal、base、reference、working policy 和真实点。

当前 0587/f5ec/f080/19e4 精确绑定 actual09 的 ff544/aee22、完整 target 7c766、参考 d449 和原 actual point。新的 run10 参考及其当前标量计算是独立真实输入；本核查没有将 run09 的1995叶、历史地址恢复的2397叶或任何未来 run10 值混作同一份费用。

本文始终区别：

1. 既有源码所定义的准确数学场及准确端口；
2. 一个完整实际点的工作场/根/积分字与误差；
3. 同一准确场的全闭面、连续域和全相位证书。

只有完整绑定和已付误差使第2层的真实候选与第1层相连；下面的条件装配才进入第3层。

## 2. 使用完整 R715 物理场，不删除 raw lift

记准确上半面为 $U(s,\phi)$，$0\le s\le S$。固定图为 $\theta=\Theta_0(\phi)$，$\rho_0=\Theta_0'>0$。令 $T$ 为包含当前全部 omega、六控制和准确参考的修正切向量，$\Gamma$ 为当前 core，$P=R e_r(\Theta_0(\phi))+H e_z$。源码使用

$$
h(s)=1-S_5(s/S),\qquad
\Delta_j=\Gamma_j-P_j+\int_0^S T_j(v,\phi)\,dv,\quad j=0,1,2.
$$

准确物理表达为

$$
U=(1-h)P+h\Gamma+\int_0^sT-(1-h)\int_0^ST,
$$

$$
U_s=T+h'\Delta_0,\qquad U_{ss}=T_s+h''\Delta_0,
$$

$$
U_\phi=(1-h)P_1+h\Gamma_1+\int_0^sT_1-(1-h)\int_0^ST_1,
$$

$$
U_{s\phi}=T_1+h'\Delta_1,\qquad
U_{\phi\phi}=(1-h)P_2+h\Gamma_2+\int_0^sT_2-(1-h)\int_0^ST_2.
$$

这正是 [R715 §6](../results/R715-reference-centred-normal-sixjets-and-error-ledger.md) 的完整方案 B，换用源码的下降 h 后的式子。0587 的 physical_cells 调用完整 physical_sixjet_boxes，同时给出三层 raw accurate closure defects；不能从中心化残差很小改写为 $\Delta_j=0$，不能用单位 $T$ 替代实际 $U_s$，不能把工作原函数的形式导数当作已付准确 sixjet。

准确参考闭合及末段准确根若另外成立，可以推导准确 $\Delta_j=0$；下面的端口核查本身不需要这种消去，因为 $h'$、$h''$ 在两端准确为零。

## 3. 直接从全变量布局实例化 core 和 cap 端口

原 J=923、角槽数482的整块 omega 数组有三条准确零行：

$$
0,\qquad 3(J-1),\qquad 3(J-1)+1.
$$

它们分别是 core 的 value，以及 cap 的 value/first radial jet。core first/second 与 cap second 仍全部自由。不能为接缝删除这些自由量。19e4 的 verify_point_layout 完整读全部1,333,370个自由变量、原 dtype/shape/字节摘要、真实末槽 H，再核这同一源码布局；它不从有限几项或错误 parent 重建当前点。

两个 Q bubble、gamma 和两个 reference-support 均严格在 $(0,S)$ 内。因而在两端的完整邻域，normal 控制修正消失，参考回到原准确标量律。该律的端口为

$$
T_{\rm ref}(0,\phi)=e_z,\quad
(T_{{\rm ref},s})_z(0,\phi)=0,
$$

$$
T_{\rm ref}(S,\phi)=-e_r(\theta),\quad
T_{{\rm ref},s}(S,\phi)=0.
$$

core 处 $\Omega=0$，但自由 $\Omega_s$ 仍贡献 $\Omega_s\times e_z$，其竖直分量准确为零。cap 处 $\Omega=\Omega_s=0$。结合完整 lift，得到以下全部端口；下标仍是固定材料 $\phi$，不是另选物理角。

| 端口 | 位置及径向/混合迹 | 角迹 |
|---|---|---|
| core $s=0$ | $U=\Gamma,\ \Gamma_z=0;\ U_s=e_z;\ (U_{ss})_z=0;\ U_{s\phi}=0$ | $U_\phi=\Gamma_\phi,\ U_{\phi\phi}=\Gamma_{\phi\phi}$，两者竖直分量为0 |
| cap $s=S$ | $U=R e_r+H e_z;\ U_s=-e_r;\ U_{ss}=0;\ U_{s\phi}=-\rho_0 e_t$ | $U_\phi=R\rho_0e_t;\ U_{\phi\phi}=R(\rho_0'e_t-\rho_0^2e_r)$ |

这使用 $h(0)=1,h(S)=0,h'(0)=h''(0)=h'(S)=h''(S)=0$，以及整份准确原函数在0与S的端值。没有将数值载体 $\widehat S,\widehat R$、工作归约或打印残差当成这些准确恒等式。新的准确输入适配仍须真核当前 scalar/source 的端点律和完整 supports，而不是只填“endpoint true”。

## 4. 完整角圈先成立，才得到闭 C² 参数球面

上半面必须先是一个确定的完整 $C^2$ 场。所需来源是全共同32段、全部准确径向片以及同一全角分支，不是几个独立角的根。

现有 f5ec/19e4 的接口可直接使用：

- complete_angle_requests 中全部 full_angle_cell 按准确 $\phi/\pi\in[0,2]$ 连续覆盖；
- 每个 job 有32个完整 stage、同一实际 source/model/point、准确根盒及收缩唯一性域；
- 相邻盒按每个 stage 的真实有向根包围包含相接；周期端还核相同准确方程的 $2\pi$ 源级周期关系；
- 每个实际 literal 角的工作选支与这条准确全圈分支关联；不能默默 wrap 或替换其字；
- complete_exact_radial_plan 从 $(0,0)$ 到 $(1,0)$，端点表示 $s=\alpha S+\beta$，全部922胞及真正解析分片都保留；
- 所有读取的 report、snapshot、point、journal、physical stream、reference 及输出字节在最终再次核验。

f5ec 的 full_same_field_angle_branch.complete_continuous_angle_branch_certified 和最后的 all_bound_input_and_output_bytes_rechecked_at_final_report 不能缺少。消费者还须从完整 journal/流重新核其覆盖和每段关系；单个 true、正的样本面积或 remaining=0 不是上述源/覆盖的替代。

全 upper 条件付清后，用有符号径向坐标 $u$ 定义

$$
F(u,\phi)=
\begin{cases}
U(u,\phi),&u\ge0,\\
J_zU(-u,\phi),&u\le0,
\end{cases}
\qquad J_z=\operatorname{diag}(1,1,-1).
$$

第3节的 $\Gamma_z=0,(U_s)_{xy}=0,(U_{ss})_z=0$ 恰是 [R248 §3.2](../results/R248-finite-C2-phase-family-and-global-reductions.md) 的全部反射条件。其角导数给剩余混合迹，没有漏付另一条反射相位。

下片各 jet 准确为 $J_zU,-J_zU_s,J_zU_\phi,J_zU_{ss},-J_zU_{s\phi},J_zU_{\phi\phi}$。上片采用 $N=U_\phi\times U_s$。因为 $\det J_z=-1$，下片在有符号 u 坐标中的同向候选法向为

$$
F_\phi\times F_u=J_zN.
$$

若实现仍以正 $s\in[0,S]$ 参数化反射下片，则它的外向候选交叉次序必须为 $F_s\times F_\phi$；19e4 已明确保存这一约定。不能保持正 s 又机械使用上片交叉次序。

## 5. 两个真实 Cartesian 帽和固定标记

cap 邻域改用 $r=R+S-s$。于是第3节给

$$
U_r=e_r,\quad U_{rr}=0,\quad
U_{r\phi}=\rho_0e_t,\quad
U_{\phi\phi}=R(\rho_0'e_t-\rho_0^2e_r).
$$

这与同一固定材料图的水平圆盘 $(r e_r(\Theta_0(\phi)),H)$ 完整两阶迹一致。cap 内部、特别是极点，应使用 Cartesian 坐标 $(x,y)$；不能把非线性 $\Theta_0$ 沿半径硬延伸为极点图。两闭盘接到上下 annulus 后是同一参数球面。

采用 [R661 §4–5](../results/R661-complete-nonplanar-activity-and-four-fixed-markers.md) 的原 p4 配方：上帽中心 $(3/20,0),(0,3/20),(-3/20,0)$，下帽中心 $(0,0)$；半径分别 $1/25,9/200,1/20,11/200$，高度 $h_b=1/1000$。沿各帽外向方向加

$$
f_i(x)=h_b(1-|x-c_i|^2/b_i^2)_+^4.
$$

只要真实 $R>1/5$，所有支撑严格在帽内，边缘的完整两 jet 与零片相接；支撑盘之间的分离沿用这组准确有理参数。上下帽写成 $(x,y,H+f_+)$ 与 $(x,y,-H-f_-)$，帽的参考度量是各固定图的自身诱导度量。H 是当前点的真实自由高度，在选定这一个场后沿 phase 固定；它不是参考初始 H0，也不改变图的梯度度量。

此段没有迁移 R661 对旧6077候选的“全部活动片无平面开片”结果。这里仅消费其真实固定帽配方和局部导数预算。

## 6. 物理 phase 的完整链式法则

全角 $\rho_0>0$ 且 $\Theta_0(\phi+2\pi)=\Theta_0(\phi)+2\pi$ 时，用真实单调 lift 定义

$$
\zeta_\alpha(\phi)=\Theta_0^{-1}\bigl(\Theta_0(\phi)-\alpha\bigr),
\qquad \alpha=\pi t/2,\quad 0\le t\le1.
$$

准确周期关联允许把它在整实线上计算后回到已证明的同一角圈；未认证的浮点 wrap 不能替代此事。活动上片为

$$
U_\alpha(s,\phi)=R_\alpha U(s,\zeta_\alpha(\phi)).
$$

一般 $\zeta_\alpha\ne\phi-\alpha$。设 $r=\rho_0(\phi)$、$q=\rho_0(\zeta_\alpha)$，则

$$
\zeta_\phi=r/q,\qquad
\zeta_{\phi\phi}=\rho_0'(\phi)/q-r^2\rho_0'(\zeta_\alpha)/q^3.
$$

全部六 jet 按下表转换，右边 U 的量都在同一个 $(s,\zeta_\alpha)$ 读取。

| jet | 准确变换 |
|---|---|
| $U_\alpha$ | $R_\alpha U$ |
| $(U_\alpha)_s$ | $R_\alpha U_s$ |
| $(U_\alpha)_\phi$ | $R_\alpha U_\phi\,\zeta_\phi$ |
| $(U_\alpha)_{ss}$ | $R_\alpha U_{ss}$ |
| $(U_\alpha)_{s\phi}$ | $R_\alpha U_{s\phi}\,\zeta_\phi$ |
| $(U_\alpha)_{\phi\phi}$ | $R_\alpha(U_{\phi\phi}\zeta_\phi^2+U_\phi\zeta_{\phi\phi})$ |

$\zeta_\phi>0$，故候选法向为 $N_\alpha=R_\alpha N\,\zeta_\phi$，单位法向为 $R_\alpha n$。下反射与绕 z 轴旋转交换。帽上使用相同 Cartesian 材料旋转与空间旋转的抵消，再加固定 p4 图，所以帽上的每个材料点逐点不动。

这正是 R248 的构造。已有 upper $C^2$ 加准确接缝给 $t\mapsto F_t$ 的强 $C^2$ 连续性；不需要新 $C^3$ 条件。marked 像为 $R_\alpha A\cup C$，一般不是整个 $S_0$ 的旋转。这里没有根据有限相位采样宣称全时间结论。

## 7. 固定 g、曲率、共同 A 的全相位归约

活动度量仍是同一个

$$
g=ds^2+a(s)^2\rho_0(\phi)^2d\phi^2.
$$

因为 $\zeta_\phi/\rho_0(\phi)=1/\rho_0(\zeta_\alpha)$，归一化列 $U_s,U_\phi/(a\rho_0)$ 在相位下只发生同一空间旋转和准确角重参数化。因此使用真实 off-diagonal 的 $2\times2$ 相对 Gram 算子误差，可以由一份完整零相位空间上界覆盖全部 t。帽自身共同度量的误差为零。主曲率的相位不变性使用 R248；不能把三个分量最大值当作谱范数。

取沿整个闭场固定的

$$
A_\beta=\operatorname{diag}(1,1,\beta),\quad \beta>0,\quad c=0,\quad
L=\max(1,\beta).
$$

A 与旋转和 $J_z$ 都交换。若完整 upper stream 给 $a_N=U_xN_x+U_yN_y$、$b_N=U_zN_z$、$w=|N|>0$，则 $(a_N+\beta b_N)/w$ 同时覆盖反射下片与所有活动 phase。不要把这里的 $a_N$ 同固定标量 a(s) 混同。每个盒另选一个 beta 不组成一个共同 A。

如果将中心改成非零轴上 $c_z$，下反射的支持项变为 $\beta(U_z+c_z)N_z$，上片则是 $\beta(U_z-c_z)N_z$；不能仍用同一 $b_N$ 下界无偿继承。当前可执行合同固定 c=0，避免引入没有付费的中心转移。

## 8. 标记帽支持界的正分子与 R650 完整闭合

原 p4 图给 $|\nabla f|\le1/20$、$|x|\le1/5$（仅在标记支撑上）、真实欧氏主曲率 $|\kappa|\le5$。令 H 的同场准确下界为 $H_-$，定义

$$
n_-=\beta H_- -1/100.
$$

**只有 $n_-\ge0$ 时**，才可利用分母上界 $801/800$ 得到

$$
\sigma_C\ge n_-/(801/800).
$$

若 $n_-<0$，这次除法不是合法下界；可以保留 $n_-$ 本身作为保守负下界，或明确该充分支撑条件尚未付。平帽补集的支持为 $\beta H$，不会比上述可行正下界更差。beta=1/4、H≥1 时这恢复已刊的 $64/267$，没有借用旧活动场数值。

若完整 upper 已付浸入、$K_A$ 和 $\sigma_A$，合成

$$
K_+=\max(K_A,5),\qquad \sigma_-=\min(\sigma_A,\sigma_C).
$$

必须先完成第4–5节闭 $C^2$ 参数球面及连续全局候选法向，才可调用 [R650](../results/R650-positive-definite-flow-support-reach.md)。它要求正支撑并直接推出嵌入及欧氏 reach；这里不预先假设外向/单射来循环证明嵌入。上帽的候选法向为 $+e_z$，R650 的单层流图结论确定嵌入后的向外选择。

完整位置包围给

$$
D_+=2\max\{R_A,\sqrt{R^2+H^2}\}+2h_b,
$$

其中 $R_A$ 是整个准确 upper 的 $|U|$ 上界，R/H 取同一实际场的准确盒。该式覆盖下片、两帽、标记及全部相位；仍只是课题 $D=\operatorname{diam}F_0(M)$ 的上界。不能用有限扫描的 diameter lower、预算4.2或旧场D代替。

令 $\tau=3D_+/100$。充分不等式是

$$
\sigma_-\ge\tau L,\qquad K_+\tau\le1.
$$

于是 R650 给全部相位 $\operatorname{reach}(S_t)\ge\tau\ge0.03D$。beta>1 的 L 不得漏掉。分量盒宽导致条件失败，只说明当前证据未给出这条充分界，不说明场不嵌入或课题无解。

## 9. 实际握持集与完整像见证

本题沿用 [原问题定义](../../visible-flexible-closed-surface/README.md)：

$
\delta_{\rm hold}=\max_{t\in[0,1]}d_H(F_t(M),F_0(M)),
$

**不做任何刚体对齐。** 只有 $\delta_{\rm E}$ 对 $\mathrm E(3)$ 取商，包括反射。下面的四个固定握持点及其稳定子是额外可复核事实，不是 $\delta_{\rm hold}$ 下界的新增前提。

若准确 $R_-\ge r_h=9/20$，可取整个上帽半径 $r_h$ 的闭材料盘作为握持集。该集包含以下四个实际固定像点：

$$
(r_h,0,H),\quad(-r_h,0,H),\quad(0,r_h,H),\quad
(3/20,0,H+h_b).
$$

前三点不在任何标记支撑内；第四点是第一标记峰顶。四点的仿射差行列式绝对值为 $2r_h^2h_b>0$。因此逐点固定整个握持集的任何欧氏等距，包括反射，都只能是恒等。该结论只使用固定握持集的实际四点，不需要先给活动片的标记唯一性或非全等结论；它也不限制任意两个像之间可能存在的、并不逐点固定握持点的刚体对齐。握持集像直径至少 $2r_h=9/10$；最终仍须验证 $9/10\ge D_+/5$。

当前 core 的全部系数给准确轴向值

$$
X=1+\sum_{j=1}^M c_j,\qquad
Y=1+\sum_{j=1}^M(-1)^j c_j.
$$

这里是当前 core 全字，不是冻结参考 core。准确单调逆图在四条轴上与 sin(2jφ)=0 相容，所以 core 包含 $(\pm X,0,0),(0,\pm Y,0)$。四分之一物理相位的像包含 $(0,\pm X,0),(\pm Y,0,0)$，无须借用整个 normal 选支的半转协变。

设完整零相位目标像（upper、lower、两平帽和所有 p4）已被水平 hull

$$
x\in[L_x,U_x],\qquad y\in[L_y,U_y]
$$

包围，则四个真实源点分别给距离下界，从而

$$
\delta_{\rm hold}\ge
\max\{0,\ X-U_y,\ X+L_y,\ Y-U_x,\ Y+L_x\}.
$$

区间实施应取各表达的安全下界；宽盒返回0是诚实未付。这一结论直接使用本题的整像 Hausdorff 定义，不需要任何刚体稳定子条件，也不是材料点位移。目标 hull 必须包含帽的整个水平盘 $[-R,R]^2$；p4只改变z不扩水平投影。上下反射不改水平投影。不能只保核心或同一材料点位移。

这是一条可以与现有 leaf 位置流同步累积的充分下界，不要求先寻找 Hausdorff 最大相位。若它不足，保留已付信息，继续同一完整场的更细目标距离包围，而不删除难片。目标是同场下界达到 $D_+/5$。

## 10. 不把 reach/握持证据冒成欧氏非全等或完整求解

本题的无对齐握持量、逐点固定握持集的刚体稳定子、以及对任意刚体对齐取商的欧氏量，是三个不同概念。R650、正握持幅度和四个固定握持点，不自动排除一个不逐点固定握持集的全等映射。

既刊 [R716](../results/R716-asymmetric-fixed-caps-and-centred-volume-moment.md) 的一般12矩/重心补偿路线保留：

- 完整零相位闭参数通量已算完，不等于它已被解释为同一嵌入闭面的有界实体矩；
- 上述实际闭面/外向证据可支付实体解释，但固定 p4 的新增体积还需实际外侧管与不交条件；
- 没有付逐段 signed-root 包含时，不用半转简式；一般中心矩保全部一阶矩和混合二阶矩；
- 未付活动面无平面开片时，不迁移 R661 旧6077的 R238 标记刚性结果。

同一固定 g 的原目标、全部变量、原32段、真实非线性求解与实际精化责任继续保留。闭面几何消费者不能把一次数值候选、有限样本或已有的条件定理登记为题目完成。

## 11. 可执行装配需要输出什么

下面是本核查对 construction 完整 producer 的实质接口，不是八个预填true的占位符。

| 实际读取/推导 | 同场来源与核验 | 尚未满足时 |
|---|---|---|
| 完整 point、model、target、参考输入 | 实际 source registry、全部字节/数组摘要；H及当前core由全点读出 | 不替换为初点或他场值 |
| 全 upper radial×circle | f5ec完整请求、各journal、32stage、最后字节重核；whole accurate sixjet和a/rho均同点 | 保真实部分覆盖，完整几何量为空 |
| C² core/cap | 第3节真实mask、准确标量律、support及完整lift；上下端全部六jet | 不把小残差或rawDelta删除当证明 |
| 闭球与法向 | 第4–5节准确反射/两Cartesian圆盘/p4；完整immersion | candidate orientation不冒外向嵌入 |
| 全phase metric/曲率/支持 | 第6–8节固定Theta0、完整准确phase，公共beta/中心、cap同预算 | 不用phase样本补齐 |
| 直径与握持 | 全leaf位置hull、准确R/H、实际4固定点/全部currentcore轴值 | 宽盒给不充分，不虚填.2D |
| reach | 闭面C²、连续法向、同beta完整支撑和曲率；tau=3D+/100 | 只保各真实条件，无总体success |
| 体积/非全等桥 | 同一已嵌入有界实体、实际outside tube/不交，或完整其他已刊路线 | 保R716 conditional，非全等未付 |

所有部分状态应区分 source-bound、covered、sufficient 和具体缺项；不能只写笼统“complete”。同一已支付的字段可以复用，完整关键身份和覆盖必须再读。新的 run10 来源适配不得将旧09 source 常量删掉后假装通用；应由独立完整新源接受实际输入，然后保存本次真正消费的 source/model/point identities。

## 12. 核查证据与范围

本次实际进行了完整小源/正式结果的文字读取和上述符号核查，没有运行原场、根、J/J*、积分、Fraction 数值算例或小型科学 fixture。没有执行后继闭面 producer，也没有声明任何尚未返回的条件通过。

原问题定义的完整4526B README 已实际读取，Git blob e2318baaa5a03c730200c26500ea2ddea7de7615、SHA256 d0119679e6c4d855f1f322fa6daa68cd2a30c795b14d0b124e6674459855fc23；没有根据旧笔记猜测握持定义。

正式引用的完整文本身份为：

| 正式条目 | SHA256 |
|---|---|
| R248 | 7b6dd9566b024484c5908366ff3f78321cd6ec28a8d0c65df1a4a680b9f9c731 |
| R650 | 35d79e32b8ca18d391576bff4f6b5427e67218a3dadc22e404de0680c2e7982f |
| R661 | b3a2eda488719544a0fc1a57cf83a306a2c3d9b6df638b823379e0c45170ddcd |
| R715 | e220528af01982c543da46f64541dc18c2a57bbb17bac4afbd7fee5db6e7e1c0 |
| R716 | 5e3ebdf00fa7fcef33e7ae7e58dcd81dadd77bde2b87f618726d1ee6af444989 |

它们的定理保持原条件和原归属；本文只把当前完整 normal / raw lift 的实际端口接到这些已有条件。新数值结果、执行成本和剩余费用只能由真正公开 Actions 返回回答。
