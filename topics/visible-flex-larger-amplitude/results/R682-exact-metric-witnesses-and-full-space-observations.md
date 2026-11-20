# R682. 严格度量下界见证到永久观察：位置、目标版本与全自由导数接口

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / geometry_path。

**已证明：严格点下界的正确地址消费、准确位置身份与新增正权必换离散目标的界限，以及完整点残差的全自由 Jv/VJP 和 R664 拼接因子。当前没有新的数值见证或适配器执行。**

本说明只读已刊源码并作纸面推导，没有运行科学计算、读取一个尚未返回的候选数值、创建 fixture、改动既有源或 Git 索引。它不预设当前 Actions 候选在哪一胞失败，也不宣称已把新点接入求解。待实际 complete-cell 返回后，可直接依下述接口消费真实位置。

**结论：** fd4 的 `actual_supremum_lower` 可以给出一个严格超标的具体物理点；原 raw 足以无损恢复该点的位置，但不含带符号特征值或特征向量。保持旧正权谱泛函和旧归一化时，新点只能作为独立诊断/约束使用。给它新增正目标权必然需要新的离散目标版本；同一个固定 $g$、同一个物理场空间不意味着两个离散泛函相同。

## 1. 本次实际对照的接口

以下 SHA256 均由源码字节读取，未 import 科学模块。

| 源 | SHA256 |
|---|---|
| `exact_reference_tail_metric_adaptive.py` | `5d04728c4fe4059948e07feb63d1281846bde37300dc57ac34589466d2172759` |
| `exact_reference_tail_relative_gram_interval.py` | `fd4cd58045e16a969c8c1be48468ab4c1a7be929ef9b95e2a9a24ca546176b2d` |
| `exact_reference_tail_interval.py` | `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225` |
| `fullclosed_relative_gram_interval.py` | `5bbf821f45fec3a8ecd29ebd64dce8058bb302f7d53416b50158cca743065a13` |
| `gauss_observed_closed_gram.py` | `26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d` |
| `exact_reference_tail_lift.py` | `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216` |
| `positive_spectral_gram_weights.py` | `e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91` |
| `positive_spectral_gram_hessian.py` | `29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4` |
| `fullclosed_gauss_exact_tail_inequality_qp.py` | `b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8` |
| `fullclosed_point_cotangent_memory.py` | `029f581c74082e36fd37663192a0bb42a20ef595c324c1d4e1e8f85e1657c26e` |

基本度量与谱目标分别沿用 [R657](R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md)、[R660](R660-positive-spectral-Gram-blocks-and-maximum-control.md)、[R664](R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md)。新参考尾沿用 [R671](R671-exact-reference-tail-affine-lift.md)、[R674](R674-reference-tail-continuous-profile-and-same-angle-remainders.md)。本说明没有重证 [R655](R655-node-midpoint-blind-space-and-Gauss-control.md) 的欠观察核，也没有重做 [R676](R676-fixed-metric-refinement-and-complete-observation-transfer.md) 的精化转移。

## 2. 严格 lower 究竟证明了什么

写实际相对 Gram 矩阵为

$$
E(s,\phi)=\begin{pmatrix}e&m\\m&g\end{pmatrix},\qquad
e=|F_s|^2-1,\quad m=\frac{F_s\cdot F_\phi}{a\rho},\quad
g=\frac{|F_\phi|^2}{a^2\rho^2}-1.
$$

fd4 `certify(cell)` 的闭角弧上界与真实点下界是两条不同计算。真实点分支取一个已分片的径向 Bernstein **端控制点**（`endpoint=0` 或 `-1`），再取准确 Fourier 网格角；端控制点此时就是对应端点值，不是任意内部控制点。它仍经过 `actual_entries`，包含目标 $a$ 与新 $f,z$ 的全部已声明标量误差，角向取值也使用向外算术。因此得到包含该**同一真实点**三项 $(e,m,g)$ 的区间。

对任一实对称二阶矩阵，

$$
\|E\|_{\rm op}=\frac{|e+g|+\sqrt{(e-g)^2+4m^2}}2.
$$

`norm_interval(actual)[0]` 是这个点值范数的区间下端。取有限点中最大的下端 $L$ 后，有

$$
\sup_{(s,\phi)\in\text{该胞}}\|E(s,\phi)\|_{\rm op}
\ \geq\ \|E(p_*)\|_{\rm op}\ \geq\ L.
$$

若 $L>1/1000000$，则当前被绑定候选确实在 $p_*$ 超标。此推断不要求该胞上界很紧；也不来自平均值、上界公式的下端或 `worst` 上界弧位置。fd4 在新 lift 不活动的胞调用原 R657 `certify`，其 endpoint 下界语义相同。

原 raw 的 `actual_lower_witness` 只有 `piece, radial_subcell, endpoint, angle_grid_index`。它**没有**保存 $(e,m,g)$ 点区间、符号、特征向量。由一个范数下界无法无损反推这些量；它们只能在需要时于该准确位置对当前场重新读取。增加完整三项 Gram 残差本身并不需要一个特征向量。

必须消费 adaptive 的 `lower_source` 与 `lower_configuration`。它们可能不同于提供最小上界的 `upper_source`/配置。未返回胞和仅有 `worst` 上界地址的胞不能伪装成严格超标点。比较阈值时用 JSON 还原后的 binary64 值对应的准确 Fraction，或已保存的 `lower_exact`；不要把打印十进制字符串当作另一个未经向外证明的更大下界。

## 3. 无损位置不是一对浮点数

原节点是 $s_i=\alpha_iS+\beta_i$。对 fd4 活动胞，`scalar_pieces` 已逐 subpiece 保存准确符号左右端；对于旧公式胞，由该 piece 的符号端点和准确分数 `sub/r` 恢复。角点为

$$
\phi_* =\frac{2j}{Q}\pi,\qquad 0\leq j\leq Q/4.
$$

adaptive 源现成的 `address(row,spec,'lower')` 已完成这个**纯元数据**步骤，输出 `exact_witness_s=[alpha,beta]` 与 `angle_center_pi_coefficient_exact`。不需要重写一份计算器或重新支付整个胞。

永久位置的主身份应保存

$$
(\text{原 scalar 定义身份},\ \alpha_*,\beta_*,\ \phi_*/\pi),
$$

所有分数约成标准形式。cell、piece、sub、端点、发现层 $Q,r$ 是定位与来源信息，不能替代物理位置。跨候选发现同一点时合并来源；发现候选的 bundle SHA 归 provenance，不应使同一个物理位置变成两条重复权重。未经准确等同性证明，不把两个靠近的 float 位置合并。

一般有

$$
u_* =\frac{(\alpha_*-\alpha_i)S+(\beta_*-\beta_i)}
{(\alpha_{i+1}-\alpha_i)S+(\beta_{i+1}-\beta_i)}.
$$

这个 $u_*$ 未必是有理数；不能总写成某个固定二进制 `float u`。冻结 factory 的 `_point_definition` 会把 `Fraction(float(u))` 作为准确插值参数，所以把一个近似 $u_*$ 传给原 `point_adapter` 会选择一个可能略有差别的物理点。`phi=float(pi*r)` 同样只是角的载体。

最小新观察适配器应接受符号 $(\alpha_*,\beta_*,\phi_*/\pi)$，从**同一** FullHold 和准确节点定义取得 $a$、$h/f/k$ 以及所需导数，再建立该点的 Hermite/角系数数值载体。记录准确位置、载体及其包围误差；普通求解中的载体读数仍标为数值量，不能把它冒作原区间点值。准确位置规格不变，最终连续验证仍对该规格下的真实场负责。这不改变 $g$，也不以插值旧 $a$ 数组代替原 oracle。

新 point adapter 可将这些已绑定的 Hermite 权、六个可微 lift 列、三个固定 offset 列交给单点 view。不要绕回只接受 float $u$ 的旧 `pullback_at` 重新查询一个略异位置。旧 canonical bundle、旧观察 carrier 与所有旧位置原样保留；额外点由单独 manifest 绑定，不重写旧 carrier 身份。

## 4. 为什么不直接给 ObservationPlan 追加一行

现 `ObservationPlan` 只有径向 `cells/u/times/weights`；每个 stage 共用整个固定角网格。`ObservationMixin.residual` 的形状是 $(P,N,3)$，原节点/中点前缀必须逐字保留，Gauss 权和旧 Simpson 权分别保留，`mixed_stage_weights(t)` 为

$$
w_s=t\,w_s^{\rm Simpson}+(1-t)\,w_s^{\rm Gauss}>0.
$$

追加一个 stage 会读一整圈角，而不只是发现的角点；新的 $2j\pi/Q$ 也未必在原 $N=2048$ 网格上。若 $Q$ 是 $N$ 的倍数，仍需 $jN/Q$ 为整数才重合。换 $N$、四舍五入到邻角、给旧 Gauss 数组偷偷添质量，都不是无损的单点接线。

因此最小扩展是**独立稀疏点块**，保留旧 tensor operator 不动：旧块仍为 $(P,N,3)$，新块为 $(L,3)$。已精确落在旧观察点上的见证只链接该旧行并增加永久检查身份，不重复加权。新块明确没有隐含的角 orbit 权。

若选择将其完整对称 orbit 计入目标，$\phi=0,\pi/2$ 的代表倍数为 2，其余四分之一内点为 4；也可直接声明一个已包含 orbit 的总质量 $\omega_\ell$。两种约定只选一种。镜像和相位不应额外重复乘权；原谱目标就是活动上片的完整角 orbit 约定。

## 5. 保持原谱目标的精确边界

设 $p=2k$、$c>0$、$\epsilon>0$ 固定，

$$
\ell(E)=\operatorname{tr}\left(\frac{E^2+\epsilon^2I}{c^2}\right)^k,
\quad C_0=\left(\sum_sw_s\right)N_{\rm full},
\quad \Phi_0(x)=\frac1{C_0}\sum_{s,j}w_sm_j\ell(E_{sj}(x)).
$$

这正是当前 `statistics` 与 full-Phi driver 的离散泛函。$a$、原 core/material 链、新尾表示、旧 $w_s,m_j,p,\epsilon,c,C_0$ 均不因发现见证而改变。

### 5.1 原泛函完全不变：额外点是诊断或约束

独立读取永久集合上的 $E(p_\ell,x)$，可作为报告和真实线搜的额外检查；若需要参与方向，可另加明确的度量不等式。它们在目标中的新增权是零，因此不能称为“给原目标增加了正权残差”。原有每一条目标行仍保持正权。

约束 $\|E(p_\ell,x)\|_{\rm op}\leq\tau$ 等价于

$$
-\tau I\preceq E(p_\ell,x)\preceq\tau I.
$$

在当前点选单位向量 $v$ 与 $\sigma\in\{-1,1\}$，线性化切面为

$$
\sigma v^TDE(p_\ell,x)[d]v
\leq\tau-\sigma v^TE(p_\ell,x)v.
$$

基点两支特征向量给出有用切面，但一组有限固定向量不能保证新场的全部谱约束。每次真实 trial 必须重读完整三项和两个特征值，永久保存的是位置，不能永久只检查最初那支符号/向量。重根时不硬套唯一特征向量导数；固定 Rayleigh 方向仍定义合法切面。

**现有求解器限制：** 当前 full-QP 明记 `phase_I_restoration_implemented=False`，要求 $d=0$ 对线性不等式可行。若严格下界已经大于 $10^{-6}$，不能直接加该上限后复用零初值 feasible-CG。可保持 $\Phi_0,C_0$，先使用明确的当前可行算法上限并作不增检查；它不等于达到 README 的 $10^{-6}$。若要强制下降到一个当前不可行上限，必须有独立登记的恢复/松弛阶段或可行非零初值，不能把负 bound 改成零。这里不预设哪一种数值策略会成功。

### 5.2 给新点正质量：新的目标版本

取固定 $\omega_\ell>0$，它已包含需要的 orbit 倍数，$W=\sum_\ell\omega_\ell$。保留旧分子权和旧 $C_0$ 时，实际目标为

$$
\Phi_+(x)=\Phi_0(x)+\frac1{C_0}\sum_\ell\omega_\ell\ell(E(p_\ell,x)).
$$

因为 $\epsilon>0$，每个 $\ell(E)>0$，所以只要 $W>0$，就有 $\Phi_+(x)>\Phi_0(x)$，不能把新增后数值与旧值直接相减并称为下降。此时总归一质量是 $1+W/C_0$，不能仍声称正权和为 1。零残差常数也由 $2(\epsilon^2/c^2)^k$ 变成其 $1+W/C_0$ 倍。

若改为单位总质量，则另一个明确目标是

$$
\Phi_{\rm av}(x)=\frac{C_0\Phi_0(x)+\sum_\ell\omega_\ell\ell(E(p_\ell,x))}{C_0+W}.
$$

它改了归一化及旧行的归一系数。重新分配旧正权、将新点称为更好的求积，也不能无证明地宣称有限泛函完全相同；当前场含完整非多项式 lift，未有这些任意点对该谱损失精确求积的恒等式。若只是一个已存在点的重复副本，分裂其原权能保持总泛函，但直接复用原行更简单，也不应额外添质量。

严格下界只证明一个点的值，不给这个点一个自然的正测度质量。不能用发现它的区间盒宽或 norm 下界自动冒充已证积分权。$\omega_\ell$ 是需明确记录的优化参数，至少在一个方向及整条回溯中固定。新增位置/质量后开始新 objective epoch，在**同一个实际父场**重读 $\Phi_0$ 与新 $\Phi$，随后只比较同一版本的父/子值。保留旧 $J_w$、旧 max、见证集合 max、以及新目标值各自的名字。

## 6. 可直接接全自由空间的三项点残差

本节给新单点适配器的完整数学接口；既有全变量、core 链、端口与物理高度坐标映射不变。记

$$
V=F_s,\qquad d=F_\phi,\qquad W=\frac d{a\rho},\qquad
r=(|V|^2-1,\ V\cdot W,\ |W|^2-1).
$$

位置固定；$a,h/f/k$ 由同一个固定 scalar/表示给出。原 core 坐标的链仍须更新，不能冻结在发现时的 $\rho$。按原记号 $\nu_m=2m$、$q_m=1-\nu_m^2$，

$$
\delta\rho=\sum_mq_m\cos(\nu_m\phi)\,\delta c_m,
\qquad
\delta\theta=\sum_m\frac{q_m}{\nu_m}\sin(\nu_m\phi)\,\delta c_m.
$$

由完整节点方向经该点 Hermite 权得到 $\delta Y,\delta U$。新尾 $k$ 是固定 offset，故

$$
\delta V=\operatorname{synth}(\delta U)+f_s\delta\theta e_t+h_s\delta H e_z,
$$
$$
\delta d=\operatorname{angular}(\delta Y)
+f(\delta\rho e_t-\rho\delta\theta e_r),
\qquad
\delta W=\frac{\delta d}{a\rho}-W\frac{\delta\rho}{\rho}.
$$

于是完整 Jv 是

$$
\delta r=(2V\cdot\delta V,\ W\cdot\delta V+V\cdot\delta W,\ 2W\cdot\delta W).
$$

对 raw 三项余向量 $z=(z_e,z_m,z_g)$，物理一阶余向量及直接分母链为

$$
g_V=2z_eV+z_mW,\qquad
g_d=\frac{z_mV+2z_gW}{a\rho},
$$
$$
g_\rho^{\rm direct}=-\frac{z_m(V\cdot W)+2z_g|W|^2}{\rho}.
$$

将 `Fs=g_V,Fphi=g_d`、其他四个 six-jet 余向量为零交给同新 $h/f/k$ **单点 view** 的现成 `pullback`，已经包含物理场对 core 的 lift 链和所有节点/H 链。然后只额外加

$$
(g_c)_m\mathrel{+}=g_\rho^{\rm direct}q_m\cos(\nu_m\phi)
$$

到原允许的自由 core 槽。不能漏掉这个直接 $a\rho$ 分母项，也不能在物理 pullback 外再重复其已有 lift 对 $\rho$ 的链。固定前三个 core 系数仍不是自由槽。此即对原完整 free vector 的精确有限载体转置，不需要丢列或把百万维向量改为一个低模空间。

一个带符号 Rayleigh 残差是

$$
q_{\sigma,v}=\sigma\frac{v^TEv}{v^Tv};
\quad
z=\frac\sigma{v^Tv}(v_1^2,2v_1v_2,v_2^2).
$$

这个 $z$ 直接进入上述 VJP。若只需数值方向，当前实际矩阵的数值特征向量即可，并标为数值量；若要一个严格带符号见证，用一个准确有理非零 $v$ 收缩真实点矩阵区间，单独验证其下界。不能把原范数 lower 自动变成这个新 Rayleigh lower。

## 7. 新正权谱块接 R664 的精确因子

若决定采用第 5.2 节的新目标，单点矩阵用已有 `HessianBlocks(raw,parameters)`。这里 $T(r)=\begin{pmatrix}r_1&r_2\\r_2&r_3\end{pmatrix}$ 是 raw 三项到对称矩阵的嵌入，$T^*(B)=(B_{11},2B_{12},B_{22})$；它与下面的完整物理方向映射 $T_{\rm free}$ 分开。令 $B_\ell^TB_\ell=L_\ell$，$g_{0,\ell}=T^*h(E_\ell)$；其中 $h(t)=t((t^2+\epsilon^2)/c^2)^{k-1}$。新目标分母记为 $C_*$，明确等于 $C_0$ 或 $C_0+W$。

对完整方向映射 $T_{\rm free}$，附加模型块为

$$
A_\ell=\sqrt{\frac{k\omega_\ell}{c^2C_*}}\,B_\ell J_\ell T_{\rm free},
\qquad
v_\ell=\sqrt{\frac{k\omega_\ell}{c^2C_*}}\,B_\ell^{-T}g_{0,\ell}.
$$

将它们与原完整模型块纵向拼接；若 $C_*$ 改变，原块也相应改用新分母。三项交叉 Frobenius 因子已在 R664 的 raw 块中，不再乘一次 $\sqrt2$。新块的 orbit 质量也只出现一次。真实梯度为

$$
\nabla\Phi=\frac{2k}{c^2C_*}
\left(\sum_{s,j}w_sm_jJ_{sj}^Tg_{0,sj}
+\sum_\ell\omega_\ell J_\ell^Tg_{0,\ell}\right).
$$

虚拟 RHS 不是 $B r$，其平方范数不是新 $\Phi$。仍为 residual-Hessian pullback，不是对自由变量的完整 Hessian，也不是 $p>2$ 的 MM 上界。真正回溯必须读取当前 epoch 的完整谱损失，原全部几何位置的筛选另行保留。改变数据块归一化后，原 $\mu$ 对物理 H² 范数的相对强度也应据实记录，不能默认数值相同就代表同一正则强度。

## 8. 最小接口及永久记录约定

本次不另造重复 `address()` 的导出入口。实际返回后，新小消费者可按以下三个层分开实现：

```text
collect_returned_witnesses(checkpoint, raw_files, previous_manifest)
    -> exact MetricPointSpec list + discovery provenance

materialize_metric_points(specs, same_field_context, same_scalar_oracle)
    -> fixed point carriers + raw_residual(x), jvp(x,d), vjp(x,z)

attach_metric_point_layer(base_problem, points, objective_policy)
    -> diagnostics/constraints OR an explicitly new spectral objective epoch
```

`MetricPointSpec` 至少包含以下字段；没有实际值的字段应为 null，不造占位峰值：

```text
point_id: canonical scalar identity + reduced (alpha,beta,phi/pi)
s_affine_exact: [alpha,beta]
phi_pi_exact: rational string
discovery:
    bundle/node/model/scalar/source identities
    raw report path + SHA, complete-cell return and configuration
    actual_supremum_lower_exact, original piece/sub/endpoint/j
signed_direction: null unless actually read and separately labelled
carrier:
    original-cell address, symbolic u numerator/denominator
    numerical point/Hermite/angular/profile carriers and error provenance
role: metric_point
```

`objective_policy` 必须选定一种：

1. `diagnostic_or_constraint`：原 $\Phi_0,C_0$ 与原行权 SHA 完全不变；记录额外 numerical metric screen/恢复策略，不称新增正权目标。
2. `additive_same_C0`：给出全部正质量、总 $W$、新 epoch，目标为 $\Phi_+$。
3. `renormalized_union`：给出全部正质量、$C_*=C_0+W$、新 epoch，目标为 $\Phi_{\rm av}$。

已有位置和权从旧 manifest 保留，新的准确不同位置 append；同位置的新来源只合并 provenance，不重复增加质量。不得在一个方向的回溯中改变点集或权。新的 scalar/M/mesh/模型观察载体只按既有身份与准确物理位置重绑定规则处理，旧严格 lower 只属于发现它的旧 bundle，不可复制为新父的数值结论。

每次跨 objective epoch，在同父至少记录 `old_phi_at_parent`、`new_phi_at_parent`；接受子步记录同版本 `new_phi_at_child`，同时继续记录 `old_phi_at_child`、旧全观察 max 与永久新点 max。新的 `objective_id` 应绑定参数、旧权数组/归一化、追加位置与质量、点读取源、scalar/representation 身份。单独保存 field 身份；目标变化不应冒成物理场变化，物理场变化也不能只叫目标版本变化。

## 9. 实际输入的消费顺序与未付范围

已有 adaptive 原始返回就足以定位严格超标点；不需等全部 922 胞结束才可导出**已返回**点。现在没有为本说明假定一个具体失败胞。应先消费真实返回，确认是 $L>1/1000000$ 而非仅 $U>1/1000000$，并确认是旧观察已包含的点、额外径向点还是额外角点，再写最小实际接线入口和明确目标策略。不能在没有真实返回时给当前求解器盲加权或预排科学预算。

度量点 manifest 与已有 curvature/radius 的永久几何记忆是不同集合，不能把 metric 点塞进曲率 manifest 就声称它参与了谱残差。反之，新增 metric 行也不替代已有 reach 必要筛选。

有限点目标下降、所有新增点通过，都不支付完整连续 $10^{-6}$。完整原活动域仍须每个原胞/真实 scalar piece 全覆盖，帽与镜像依原准确接口处理。平帽使用平面度量；若加入固定 marker 图，帽上使用各相位共同的图诱导度量，不能把它称为旧平面 $g$ 未变。最终全域/全相位 metric 结论仍只由相应同场完整上界给出。本说明不支付新的 metric、embedding、reach、精化收敛或课题完成结论。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。

## 10. 准确点适配的最小实现边界

这是对现有源的进一步静态定位，没有新增科学执行。无需改写冻结的 FullHold、ObservationPlan 或 canonical factory。现有代码没有名为 `scalar_exact_point` 的公开函数，但已有 `full.affine_time(alpha,beta)` 与 `full.at_box(sbox)`：后者返回同一点的 `a` 盒和相对 cut 的高度增量，cut 前该高度量为 `None`。新尾活动区已由原 factory 限制在 cut 后；`ctx._angle_curvature(sbox)` 可直接消费该准确时间盒。禁止先转 float-u 再调用 `reference_at/lift_at/pullback_at`，因为那会重新定义点。

最小独立适配器只需承担以下五项明确责任：

| 接口 | 准确输入与输出 | 不变条件 |
|---|---|---|
| `locate_symbolic_point` | $(\alpha,\beta)$、原 cell hint → cell、准确宽度和 $u$ 分子/分母/盒 | 不用浮点近邻、clamp 或猜测代替符号位置 |
| `scalar_exact_point` | 同 FullHold 点 → $a$ 及 $h,h',h'',f,f',f'',k,k',k''$ 九列、载体误差 | 九列独立于当前自由 $H$；原 scalar 不换 |
| `hermite_point_tables` | 同一符号点 → 三阶输出乘六个端 jet 的权表 | 原 shared quintic 不重新拟合；旧观察权不改 |
| `angle_point_tables` | 准确 $\phi/\pi$ → 全部角基底载体、误差与身份 | 不强制投到旧角 grid，不丢准确相位 |
| `RaggedMetricPoints` | 固定点表 → `residual/jvp/vjp` | 每次当前 core/$\rho$/转角/$H$ 重读；不隐含赋目标质量 |

构造位置时先在符号系数上相减，再求盒：

$$
h_i=(\alpha_{i+1}-\alpha_i)S+\beta_{i+1}-\beta_i,
\qquad u=\frac{(\alpha-\alpha_i)S+\beta-\beta_i}{h_i}.
$$

这保留共同 $S$ 的消去，不先将两个宽时间盒相减。准确节点使用相应端 jet 恒等权。若现有 $S$ 盒仍不能判定不同表达式的先后，位置归属未付，不能改用浮点猜测。

需要补的小 scalar helper 是同一个 quintic cutoff 的准确点 jet：分别使用原 $\chi$ 的 $[S-\mathrm{width},S]$ 和原 $\eta$ 两个符号端点，直接包围其零/一/二阶导数，再按R671组合九列。它不需要新的积分定义。尤其不能拿 f122 为某个父 $H$ 形成的 $z=Hh+k$ 表当固定新点表；那会冻结原本允许变化的高度方向。实际当前值仍须组成

$$V=\operatorname{synth}(U)+f'e_r+(h'H+k')e_z.$$

已刊单点 `pullback` 从 view 的 `observation_cells`、`observation_weights`、`lift_scalar` 取径向表，故可构造直接持有这些预制表的 view，调用 `pullback(view,prepared,0,0,cotangent)`，不经 `pullback_at` 重查。六jet及角导数使用原 rotating-phi 正交分量约定，角导数包含基底旋转，不混用Cartesian余向量。

旧 `pullback` 会从 `view.phi` 重新作 NumPy sin/cos。因此最小直接复用必须让 fields/Jv 使用相同载体算术，同时保准确 $\pi r$ 身份和误差。若选择整数trig盒的中点或轴上准确零作载体，应另加小的 `pullback_from_tables` 消费同一 co/si；不能用两份不同角表后仍声称Jv/VJP配对。

物理 pullback 外还须准确加一次第6节的直接 $a\rho$ 分母链。多个点可将局部贡献累加到一个完整 jet/core/H 缓冲，最后调用一次原 `_free_adjoint`；无须为每点保存一条百万维余向量。全部core、节点三jet、H及固定端口政策保持。以上仅定位可复用与必新增的函数边界，未写或运行一个假定失败位置的新适配器；外层目标/约束策略仍按第5节真实选择。

