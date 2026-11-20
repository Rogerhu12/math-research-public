# R678. 仅增加角频率的同度量精化：原观察目标、完整步长范数与自然终态衔接


日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**已证明：准确频率包含下的同场、同有限目标和完整母范数/增广最小商范数限制恒等式。实现仅源码准备，未执行新数值求解。**

## 范围和当前状态

本文给出一个真正只改变 $M$ 的最小入口。输入是**实际自然完成的完整 QP 报告及其 final bundle**，可以是原级报告，也可以是 R676 径向精化后实际返回的完整报告。入口支持原 polynomial lift，以及 canonical R671 的 $\lambda=0$ 和 $\lambda\ne0$ 两类。它保持同一精确 $g$、径向节点、所有模型参数、帽、$\eta$、$\lambda$ 和时间范围，把 $M$ 增为 $M'>M$，只在原 $R/T/Z$ 和 free core 槽补零，再在新完整自由空间调用一次真正 QP。默认 $M'=2M$、一个方向、最多 256 次内层推进、`qp_atol=0`。

这次准备**没有执行科学计算、没有产生新父、没有登记误差下降**。源只做 AST/编译语法检查和文件身份核对；实际 NPZ 数组读取、R671 profile 实体化、场读取及 QP 仅允许 `Rogerhu12/math-research-public` 的公开 Actions。是否安排本入口的科学预算，由正在返回的径向精化实际归因决定；本文不是新预算申请或等待用户确认的门槛。

本文不重证 [R655 的完整观察行含义](R655-node-midpoint-blind-space-and-Gauss-control.md)、[R676 的符号径向精化](R676-fixed-metric-refinement-and-complete-observation-transfer.md)、[R671 的解析尾模型](R671-exact-reference-tail-affine-lift.md)、[R660 的正谱目标](R660-positive-spectral-Gram-blocks-and-maximum-control.md) 或 [R664 的准确残差 Hessian](R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md)。这里付的是另一条具体接口：**只增加频率时，原有限观察函数及原子空间步长范数必须保持。**

## 1. 为什么不能调用 R676 的 radial-factor=1

冻结的 `refine_fixed_g_fullclosed.py` 即使取 `--radial-factor 1`，仍会重建新的六 Gauss 规则，并把完整旧规则与新规则作各一半的混合。保留旧行且权为正不等于保留每个权。那条入口适合 R676 的一般层间精化，却不能把所得 native Phi 与父 native Phi 直接相减来说明“仅增加频率”的效果。

本入口不调用其 `main`、`combine_observations`、`prepare_scalar` 或 `restrict_jets`。它仅复用已刊的通道补零函数、旧 canonical 模型验证函数和冻结依赖路径。传给新完整 driver 的 `--observations` 就是输入的原 NPZ 路径，SHA-256 也相同。因此以下全部载体逐字保留：

| 对象 | 本入口的操作 |
|---|---|
| `mesh` 及每个准确 $\alpha S+\beta$ 定义 | 不插点，不改端点，不改符号 |
| `ObservationPlan` 的 cells/u/times/三 jet 权 | 复用原文件全部数组 |
| 原 node/mid、Gauss 及此前 retained rows | 全部保留，次序不变 |
| Gauss 与 legacy 两组径向权 | 全部保留，不重新混合 |
| `a_stages`、`a_observations` 及原误差数组 | 原载体值全部保留 |
| full $N$、quarter 角值、orbit multiplicity | 保持实际父报告的 $N$ |
| 已知几何位置 | 同 cell、binary $u$、binary $\phi$；完整历史并集 |
| $M$、$R/T/Z$ 载体槽、自由变量数量 | 显式扩大，新增模补零 |
| R671 profile 的模型身份 | 新 $M$/node-report SHA 必须重新绑定 |

接口要求原 $N>4M'$ 且 $4\mid N$。默认 $160\to320$ 在实际 $N=2048$ 时满足这个条件。若再倍增不满足，入口明确拒绝把角网格扩大偷偷塞进这次单因素试验；可选较小的显式 `--modes`，或另准备有共同原角网格比较的角精化。原 carrier 的 `observation_default_full_angles` 只是默认建议，若真实已完成 driver 曾显式覆盖它，本入口以**实际报告的 $N$**为准，并分别记录两者。

## 2. 精确零嵌入与全部六 jet

设每个原径向节点的槽次序为

$$
(R_0,R_1,\ldots,R_M,\ T_1,\ldots,T_M,\ Z_0,Z_1,\ldots,Z_M).
$$

在 $M'>M$ 中，把每个已有物理槽移至同名频率槽，并把 $M<m\le M'$ 的三类系数及其径向零、一、二阶 jet 全设为零。记原自由空间到新自由空间的仿射嵌入为 $\iota$，其方向线性部分为 $E$。自由 core 系数同样延长为

$$
c'_m=c_m\quad(m\le M),\qquad c'_m=0\quad(M<m\le M').
$$

固定的前 $K$ 个 core 系数完全不动。core 的派生端口仍按准确关系

$$
T_m(0)=-\nu_m c_m,\qquad \nu_m=2m
$$

定义，不把已有 round 后的独立槽误当另一自由变量。实际源逐槽复制原 binary 数值，新增 core-$T$ 零采用 canonical unpack 的负零符号；这个符号不影响实数零。原自由系数不经过浮点加、乘或投影。已有 literal affine 接口在补零前后按冻结公式核对，canonical R671 的 `pack(..., require_affine=True)` 也不允许静默投影。

径向节点没有变化，故每个已有通道的两端共享三 jet 没有变化。quintic Hermite 唯一性立即给出同一个径向多项式；新增通道的多项式恒为零。于是对所有径向 $s$ 和角 $\phi$，而不只对观察点，

$$
q_{M'}(\iota x;s,\phi)=q_M(x;s,\phi).
$$

core 的解析量也逐项相同：

$$
\rho=1+\sum_{m=1}^{M}(1-\nu_m^2)c_m\cos(\nu_m\phi),
$$

$$
\Theta-\phi=\sum_{m=1}^{M}
\frac{1-\nu_m^2}{\nu_m}c_m\sin(\nu_m\phi).
$$

增添零项不改变 $\rho,\Theta$ 或任何导数；$e_r(\Theta)$ 始终按完整解析函数使用，没有截断其 Fourier 尾。原 lift 不变；R671 中

$$
F=q+f_\lambda e_r(\Theta)+(h_\lambda H+k_\lambda)e_z
$$

的 $f_\lambda,h_\lambda,k_\lambda$ 由同一个 $g,S,R,\lambda,\eta$ 定义，也不变。因而有准确恒等式

$$
F_{M'}(\iota x)=F_M(x),
\qquad
\partial_s^a\partial_\phi^bF_{M'}(\iota x)
=\partial_s^a\partial_\phi^bF_M(x),\quad a+b\le2.
$$

同一结论包括所有节点两侧、lift 分片边界、镜像半面和帽。这里的六 jet 转移差**准确为零**，无需像新插入非有理节点的二分限制那样支付新 jet 舍入预算。它是系数嵌入的代数结论，不是一次有限采样的“很接近”。

另一方面，浮点实现扩展数组维度后，求和或变换的运算次序可能变化。源不把“数学场相同”写成“运行时每个 residual bitwise 相同”；新完整 driver 的 initial 是实际 binary 重读，转移前后的有限 Phi 差会单独标为运算路径差异。

## 3. 原有限函数及其线性化准确包含

令原径向观察点为 $s_i$，正权为 $w_i$，quarter 角 orbit 的 multiplicity 为 $m_j$。原 relative Gram 矩阵为

$$
\mathcal E_{ij}(x)=
\begin{pmatrix}
|F_s|^2-1 & F_s\cdot F_\phi/(a_i\rho_j)\\
F_s\cdot F_\phi/(a_i\rho_j)&|F_\phi|^2/(a_i\rho_j)^2-1
\end{pmatrix}.
$$

记其两特征值为 $\lambda_{ij,+},\lambda_{ij,-}$。当前 $p=8$、$\varepsilon=.001$、$c=.05$ 固定，函数为

$$
\Phi_M(x)=\frac1{C_0}\sum_{i,j}w_i m_j
\sum_{\tau\in\{+,-\}}
\left(\frac{\lambda_{ij,\tau}(x)^2+\varepsilon^2}{c^2}\right)^4,
\qquad C_0=\Bigl(\sum_iw_i\Bigr)N.
$$

本节是原有限载体函数：$a_i$、观察位置及参考 profile 使用父 driver 的同一 literal 载体约定。其准确实数解释下的包含恒等式和普通浮点执行记录分别陈述；连续准确 $a(s)$ 的区间误差仍由原连续核负责。

本入口保全部 $s_i,a_i,w_i,\phi_j,m_j,N$，并且上一节的 $F$ 与 $\rho$ 恒等。因此

$$
\mathcal E_{M'}(\iota x)=\mathcal E_M(x),
\qquad \Phi_{M'}(\iota x)=\Phi_M(x).
$$

只要处于原合法 $\rho>0$ 域，微分得到

$$
J_{M'}(\iota x)E=J_M(x),
\qquad E^T\nabla\Phi_{M'}(\iota x)=\nabla\Phi_M(x).
$$

R664 的正残差 Hessian 也在相同残差处相同，故新拉回正规矩阵的旧子空间限制等于原矩阵。这不把 R664 的 $J^TH_{\mathcal E}J$ 误称完整 $x$-Hessian，也不把 Hessian 乘 residual 误当真实 gradient。原 driver 仍用已刊的真实 gradient、相同正块、真实 Phi 回溯和全部原几何点。

因为新的空间包含旧空间，若对完全相同的实际约束求**全局最优值**，其最优值不会变大。但这不保证一次有穷内层 QP/回溯会找到严格下降，也不推出连续度量误差随 $M$ 降低。零补时数学目标恰好相等，必须把随后实际求解的效果分开报告。

这里没有新的观察行，`new_only_observation_rows=0`。增加频率自由度不等于增加角采样点；也没有把当前有限角值集合称为连续上确界。未来若增大 $N$，应另作角网格包含与共同原 grid 的归因，不能沿用本节的逐字同一有限函数结论。

## 4. 完整 integrated/height/angular-H² 范数的旧子空间限制

这一节直接使用 [R654](R654-complete-integrated-H2-norm-and-endpoint-spectrum.md) 的完整坐标和实际冻结的 `DoubleIntegrated`、`physical_height_coordinates`、`angular_h2_coordinates` 公式；没有删除任何 $A/E/D$ 或 free core 自由度。

设原径向胞长为 $h_i>0$，节点权为 $\omega_j$。对每个通道 $\nu$，完整 inverse 中的缺陷为

$$
e_i=\frac{U_{i+1}-U_i}{h_i}-\frac{A_i+A_{i+1}}2,
\qquad
d_i=\frac{Y_{i+1}-Y_i}{h_i}-\frac{U_i+U_{i+1}}2.
$$

这些是原完整 quintic 的真实缺陷，不强制为零。令

$$
\sigma_\nu=\sqrt{1+(\nu/\nu_c)^2},\qquad \nu_c=24.
$$

当前正尺度逐通道为

$$
s_A=\frac1{\sqrt{\omega_j}\sqrt{1+\nu^2}\,\sigma_\nu},
\quad
s_E=\frac1{\sqrt{h_i}\sqrt{1+\nu^2}\,\sigma_\nu},
\quad
s_D=\frac{\sqrt{h_i}}{\sqrt{1+\nu^2}\,\sigma_\nu},
$$

$$
s_{c_\nu}=\frac1{(1+\nu^2)\sigma_\nu},
\qquad
s_H=\sqrt{\frac{7S^3}{120}}.
$$

本节的 $A,e,d,c,H$ 都是方向坐标，使用 `affine=false`；$H$ 在这里表示方向的帽高度增量。

因此，在 physical-height 逆映射后的真实 integrated 坐标中，平方母范数是所有存在的通道项之和：

$$
\sum_\nu (1+\nu^2)\sigma_\nu^2
\left(\sum_j\omega_j A_{j,\nu}^2
+\sum_i h_i e_{i,\nu}^2+\sum_i\frac{d_{i,\nu}^2}{h_i}\right)
+\sum_{\nu\text{ free core}}(1+\nu^2)^2\sigma_\nu^2c_\nu^2
+\frac{H^2}{s_H^2}.
$$

所有尺度只依赖本通道的 $\nu$ 和固定 $h_i,\omega_j,S,\nu_c$，没有 $M$ 的全局归一。保留旧通道后它们逐项相同；新增通道为零，故其贡献为零。

还须核 endpoint 投影和 physical-height 变换，不能只看这张对角表。记原 normalized endpoint 投影为 $\Pi_M$。endpoint Gram 只包含单通道二阶块，或同一个 $\nu$ 的 core-$R/T$ 四阶耦合块；不同频率之间没有 coupling。增加频率是这些块的直和。因此 normalized 坐标中的零嵌入 $E_z$ 满足

$$
\Pi_{M'}E_z=E_z\Pi_M,
\qquad L_{M'}E_z=E L_M,
$$

其中 $L$ 为完整 integrated lift。

physical-height 映射为 $A=I+v_q e_H^T$，其逆为 $I-v_q e_H^T$。$v_q$ 只在 $Z_0$ 中含原 nodal $b-\chi$；R671 中是同一个 $b-h_\lambda$。$h_\lambda$、原节点、$S$ 不变，没有新增高模，因此

$$
A_{M'}E=EA_M,
\qquad A_{M'}^{-1}E=EA_M^{-1}.
$$

由此，实际完整方向范数

$$
\|v\|_M^2=
\left\|\operatorname{DI}_M^{-1}(A_M^{-1}v;\mathrm{affine}=\mathrm{false})/s_M\right\|_2^2
$$

满足准确限制恒等式

$$
\|Ev\|_{M'}=\|v\|_M.
$$

### 4.1 冗余 coarse 列不能悄悄改变旧方向的最小范数

保持父报告实际 `coarse_low_modes` 和 requested centers。其 cutoff 不超过原 $M$；mesh 不变，实际 center indices 和每个 radial basis 不变。故 $B_{M'}=EB_M$，同一母范数下的 coarse Gram、正对角/Cholesky 白化也保持，记白化矩阵为 $R$。

当前完整增广映射是

$$
T_M(u,z)=A_ML_Mu+B_MRz.
$$

新 integrated 坐标分为旧频率块和新增频率块。endpoint 投影及 $A$ 都保这一直和，而 $B$ 没有新增块。要表示旧输出 $Ev$，新增块的输出必须为零。把任何新增坐标替换为零不会改变旧输出，且不会增大 $\|u\|^2+\|z\|^2$；反过来，任何旧表示补零即为新表示。因此

$$
\inf_{T_{M'}(u,z)=Ev}(\|u\|_2^2+\|z\|_2^2)
=\inf_{T_M(u,z)=v}(\|u\|_2^2+\|z\|_2^2).
$$

所以不只是一个选定坐标表示，**增广最小商范数本身**在旧方向上也不变。新增高模不能通过抵消来免费降低旧方向的正则代价。此结论是代数恒等式，不保证 BLAS/Cholesky 的浮点输出逐字相同；入口也不以 `largest_squared_ratio` 等新 $M$ 诊断量做额外全局再缩放。

## 5. R671 的新 M 身份重绑

原 observation carrier 本身不强制绑定 $M$，可直接逐字复用。R671 canonical definition 和 optional profile carrier 则含 $M$、mesh SHA、node-report SHA、factory/operator/scalar 来源。即使 profile 的数值数学上相同，也不能把带旧 $M$ 的 profile SHA 冒作新身份。

实际入口按以下确定顺序执行：

1. 先用冻结 `model_definition` 完整验证旧 bundle 的 canonical definition、全部 $\lambda$ 标签、mesh、原 node report、原 observation carrier、scalar 输入及 operator/factory SHA。
2. 原自由系数准确补零，生成不带旧 model JSON 的**新维度坐标 seed**。这一步已经由第 2 节付清同场含义，不能称旧模型内部的一次 `transfer_seed`。
3. 生成新的 node report，$M,n$ 和 source identity 更新；所有 $\alpha S+\beta$、准确 $S/R$ 盒、`true_a_stage_boxes` 和原 scalar 定义原样保留。这些盒对应的物理点完全没变，所以不需要新 oracle 查询，更不能复制盒到不同点。
4. 用同一原 carrier、同 $\lambda$、同 $\eta$ 两个符号端点及相同节点 indices，创建新 `TailLiftContext`。`create_pair` 和 `save_carrier` 为新 $M$/node identity 形成合法完整 canonical/profile；不使用旧 profile 的 SHA。
5. 逐项要求除 $M$ 与 node-report SHA 外的物理 definition 项相同。保存新 bundle 后，随后完整 driver 的 `keep-q` 接续已经是**同新 M 身份内部**的接续，非零 $\lambda$ 的旧 guard 正常成立。

本最小入口对 canonical $\lambda=0$ 也保留其 canonical 身份；不因它的数值场等于旧类而丢失 provenance。非零 $\lambda$ 全部支持，不作 nodal-projection、不调整 $\eta$、不重新拟合解析尾。冻结 R671 完整 driver 的原 oracle panel 参数是 128，故此入口要求其实际父也是该 panel 约定；若将来更换 carrier 计算政策，应显式提供对应新 driver，不在此处悄悄混用。

新 R671 profile 所需的同点标量仍由原 FullHold 整数 oracle 生成，但**目标** `a_observations` 一项不改，不插值、不换 $g$。原 observations 文件 SHA 在实体化结束后再核其未变。

## 6. 实际父报告、末 $\mu$ 与全部位置

复用已刊 `launch_refinement_from_full_report.py` 的完整 helper，源码 SHA 为 `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60`。先 `bound_parent_source`，再 `terminal_damping`。自然报告必须 `complete=true`，且其 `final_bundle_sha256` 等于实际输入 bundle；原 carrier SHA 同样准确匹配。R671 还绑定实际 node/scalar 输入 SHA。

若父是 manifest-only AST 派生 driver，helper 不只信注释头，而会以冻结 base 和已刊 `ExactLocationDriver` 重建预期 AST、比较实际完整 body AST。这使后续末 damping 重放确实对应已知更新规则：整方向拒绝乘 4；接受满步且 ratio 大于 .75 时除 2、下限 $10^{-8}$；其他接受不改。无 directions 用实际 `initial_damping`，不发明原报告不存在的 `final_damping`。

完整位置并集包括所有 supplied manifests、父 final curvature/radius memory、protected 点、每个 trial 新永久点、actual_geometry 位置、原 grid/arbitrary 带标签位置及 protected current representatives。只按准确 binary tuple 去重，不 round13；完整位置结构不设 100 KB 任意大小门。旧纯位置 manifest 可原样传入，此外附上完整历史并集；历史几何数值不当新候选的验收证据。

本次 radial cells/$u$、角 $\phi$ 和 $N$ 全不变，位置转移是恒等映射。只有旧记录含 stage/angle 编码时，Actions 才读取**原 carrier** 的对应 row，按原 $N$ 解析该位置。补零保持 core $\Theta$，所以在转移时其真实材料位置也相同。此后完整 solver 仍按其已刊原规则处理每一步 core 与所有历史位置，本文没有另换一个冻结物理角的求解模型。

新 driver 仍由已刊 `launch_fixed_g_refinement_qp.py`、SHA `100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622` 的相同 AST 变换产生：仅完整位置格式、去尺寸门、精确 tuple。完整方程、正目标、范数、真实回溯和原 driver 字节不改。QP 模块默认按**真实父报告**的 `source_sha256_by_role['qp']` 继承，可显式 `--qp-source`；若显式改变则计划中单独记录，不冒称它还是单一的算法变量。

## 7. 接口、返回内容与证据边界

完整已刊源为 `scripts/resume_20261120/launch_frequency_only_fullclosed.py`，40571 B，SHA256 `eea174b983d20543a154df6fdb308bb5742c7f3bde04936c960fd572de267677`。本地只允许准备；准备不 import 数值库或 field/oracle 模块，不读取 NPZ 数组。示意调用为：

```text
python launch_frequency_only_fullclosed.py
  --repo REPO --work WORK
  --parent-report ACTUAL_FULL_REPORT.json
  --bundle ACTUAL_FULL_FINAL.npz
  --carrier ACTUAL_ORIGINAL_OBSERVATIONS.npz
  --node-report ACTUAL_CURRENT_NODE_REPORT.json
  --scalar-input ORIGINAL_FULLHOLD_INPUT.json.gz
  --manifest ALL_OLD_LOCATIONS.json
  --parent-source ACTUAL_DERIVED_PARENT_DRIVER.py
  --outdir FRESH_M_ONLY_DIRECTORY
```

`--parent-source` 仅实际父为已派生 driver 时必需。可重复 `--manifest`；可显式 `--modes` 和 `--qp-source`。只有公开 Actions 中添加 `--execute` 才会读取科学数组、实体化 seed/profile 并执行 driver。默认参数为 $M'=2M$、directions=1、maxiter=256、qp_atol=0；相对容差、working-row cap、target、coarse cutoff/centers 及其余实际报告中的求解政策继承父值。准备后的同参数计划可在原目录执行；已启动实际科学尝试的目录不得覆盖。

原 $n=3M+2$，固定 $J,K$ 时自由变量数为

$$
n_{\rm free}(M)=(M-K)+(2M+1)+3(J-2)(3M+2)+1.
$$

故新增自由变量为 $(9J-15)(M'-M)$。完整 integrated 坐标数比自由变量数多 $2(3M+2)$，其增加为 $9(J-1)(M'-M)$。coarse 列数不变，residual 行数不变。源只报告这些代数维度及单项数组字节，不冒估整个进程 RSS 或实际内层速度。

实际返回的 `frequency-plan.json` 绑定全部输入、源、完整 argv、末 $\mu$、QP module、转移报告、位置并集和真正 solve 报告/终态。`frequency-transfer.json` 区分准确系数补零、canonical 重绑和未进行独立场读；实际场读取由完整 driver 的 initial 负责，不另加重复 probe。

自然返回后，源核实际 driver SHA、QP SHA、input seed SHA、final bundle SHA、$J,M',N$、全部行数和新变量数；再从已返回报告直接列出：

| 读出 | 准确含义 |
|---|---|
| parent Phi / maxGram | 真实自然父报告终态的同 grid 值 |
| zero-padded initial Phi / maxGram | 新 M 完整 driver 对准确补零场的实际 binary 重读 |
| after solve Phi / maxGram | 新 M 空间中实际回溯接受后的终态 |
| initial − parent Phi | 同场、同有限函数的浮点评价路径差；不算物理改善 |
| final − initial Phi | 真正新 M 求解对同有限函数的变化 |
| final − parent Phi | 同有限观察函数的父到终态比较；仍是普通数值 |
| 新观察行数量 | 本接口恒为 0；新增的是自由频率模 |

这些普通数值不是向外区间证书。一次真实下降最多是一个频率层的进展；所有 `frequency_convergence_demonstrated`、连续 metric/geometry 和课题完成 flag 仍为 false。本入口不把 seed 的零 padding 写成误差下降，也不把自然完成一批、一次径向细分或一次频率增加写成 README 要求的持续精化收敛。

## 8. 下一层与全部时间范围的准确边界

同 $g$ 的径向层由 R676 接，频率层由本文接；如果两者在连续几何允许的同模型中实际反复下降，再结合完整连续 relative Gram 上界，才向 README 第 4、5 条推进。每层仍须保持原 scalar、模型参数、帽/marker、准确 $\eta/\lambda$、全部观察/永久位置的适当同域归因。若更改 $\lambda$ 或 $\eta$，那是另一个模型参数试验，不能混入这条固定参数精化序列。

时间相位没有新待解的网格问题。[R248](R248-finite-C2-phase-family-and-global-reductions.md) 已给准确相位作用和全 $t$ 的度量/几何归约。在维持其同一族、固定区及参数范围时，频率补零和后续同模型候选仍使用这条准确作用；无需人为加一项独立 $t$-grid 收敛门。README 的若干 $t$ 网格导出仍须提供，它们应直接从准确族生成，不能用导出帧之间的线性插值另造一个未经证明的族。

**当前完成的是这个最小频率接口及上述包含/范数证明；没有新的科学结果和候选。**

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
