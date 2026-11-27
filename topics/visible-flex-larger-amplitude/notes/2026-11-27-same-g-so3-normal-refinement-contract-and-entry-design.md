# 当前 SO3 normal 表示的同度量精化：准确包含、真实接口与转移设计

日期：2026-11-27。会话：Astra-larger-e4e2a2bf-20261126 / geometry。

**状态：源阅读与完整条件论证；尚未实现或执行新的 SO3 精化求解器。** 本文完整读取 R676、R678、R679、R691 后，只处理现有 SO3/normal/R715 表示新增的责任。没有重算旧候选，没有本机标量、场、根或矩阵计算，也没有把下一层的输入、数值或证书预填为已返回。下列运行合同是完整新入口的设计，不能把本文当作已可运行的 fine driver。

## 1. 已有结论直接复用到哪里

[R676](../results/R676-fixed-metric-refinement-and-complete-observation-transfer.md) 已证明共享二阶 jet 的 quintic 准确限制、符号节点二分、保留旧观察与永久位置以及共同父有限函数的比较。其单个标量多项式的 Hermite 公式可用于任何一个旋转系数；其针对旧 $R/T/Z$ 向量场的通道排布、物理连接项和直接六 jet 误差消费者不能直接当作 SO3 算子。

[R678](../results/R678-frequency-only-refinement-and-identical-parent-functional.md) 已区分纯频率包含与改变观察规则。SO3 也应先保全部旧观察和权，单独增加自由频率，但它的新旋转通道和隐式闭合链必须另核。

[R679](../results/R679-dyadic-angular-refinement-and-common-grid-attribution.md) 的正权偶奇分解是一般有限和恒等式。能在 quarter 上使用它，还须引用当前 SO3 场自己的反射与同分支条件，不能只因旧 carrier 只有 quarter 就默认准确整圈归约成立。

[R691](../results/R691-frozen-physical-mean-endjet-and-material-Haar.md) §5.2 的原则仍适用：当前候选的 $M/J/N$ 改变不能移动已经冻结的参考对象。这里实际求解目标是原固定 R690 的
$$
g=ds^2+a_{\mathrm{deep}}(s)^2d\theta_0^2,
$$
不是 finite-physical 或 Haar 目标；不应借精化重新平均一个新的 $g$。R691 不给当前 SO3 表示的精确解存在结论。

当前源另使用 R703 的固定有限 normal 选支、R707 的完整根/角 jet/参数费用、R711 的固定平滑三角 seed、R714 的相同前向字下一阶图复用、R715 的完整数值 raw-lift。它们不能被旧 quintic 转移记录替代。

## 2. 必须分离的四个对象

令固定参考对象为 $\mathcal R_*$，它包含：

- 原准确 $S,R,a_{\mathrm{deep}}$ 及全 scalar 定义；
- 原固定材料图 $\theta_0(\phi)=\Theta_{c_*}(\phi)$，其完整 core $c_*$；
- 冻结 seed $T_*(s,\phi)$ 的准确 R709/R711 定义、原 core/H、支撑与端层、profile 参数；
- 其真实原参考文件、模型、源和工作求积/均值根约定。

这份对象保留自己的 $M_*,J_*$。新增当前试验空间的 $M,J$ 不改它，也不把当前 core 或 H 重新选作参考。

当前自由量为
$$
x=(c_{K+1},\ldots,c_M;\ \omega\text{ 的完整自由节点三 jet};\ H),
\qquad K=3.
$$
当前 $\omega$ 用新试验网格表示；当前 core 逆图仍解
$$
\Theta_c(\psi)=\theta_0(\phi).
$$
左边使用当前 $M$，右边使用冻结 $M_*$。因而同一个 literal $\phi$ 在整个精化序列中代表同一个材料角 $\theta_0$，即使当前 core 后来改变。这比旧 q 表示中的共同 $\phi$ 比较更直接，但不重解释已经按政策收入的历史地址。

还要分离：

1. **场的经线积分工作规则**：全积分及 partial 规则决定当前普通浮点场读数，不是 $g$ 的数学定义。
2. **观察规则**：径向观察、正权、目标 $a_i$ 载体与 full $N$ 决定当前有限 loss。
3. **normal 辅助分段**：$\tau_0=0<\cdots<\tau_m=1$，目前完整 $m=32$。它是选择隐式控制分支的数学输入，不是物理 $t$，也不是径向 mesh。
4. **参考求值工作规则**：seed 自己的 split 积分、均值根、profile 求积及实际缓存，不能误称 outer 积分规则或精确参考费用。

最小精化保持 $\tau$、两 bubble、gamma、十八个准确 binary Q 参数、六控制的单位及选支约定。改变这些东西可作为独立新表示继续研究，却不能记作此固定表示的单因素 mesh/M/N 精化。

## 3. 实际源里的确定接口障碍

以下是直接源码阅读所得，不是数值失败归因。

| 完整源/方法 | 当前约束 | 新入口的处理 |
|---|---|---|
| `so3_axisymmetric_reference.py`，4e65577…，`AxisymmetricReferenceContext.from_files` | 原参考固定 $M_*=160,J_*=923$、7377 个观察；验证完整原文件身份 | 保留这个冻结参考验证器，不把 fine 节点或新维度伪装成旧原参考 |
| 同源 `create_problem` | 明确只接受 $N=2048$ | 新观察上下文独立建立；原参考上下文保持不变 |
| `so3_supported_smooth_triangle_meridian_operator.py`，6a80361…，构造器 | 当前 $M,J$ 直接取自原参考，`parent_core` 与 `freq` 共用 | 独立 `reference_context/reference_freq/reference_core` 与 `current_layout/current_freq` |
| 同源 `_angular_nodes` | SO3 三个世界轴频率槽 | 用第4节准确排布，不用旧 R676 `pad_modes` |
| a62c245… normal 的 `_chart` | 当前 `freq` 与冻结 `parent_core` 相乘 | 明确只用冻结参考频率；当前 `_core_and_cap` 的逆图用当前频率 |
| 3e478bbe… calibration | baseline 是当前 base.initial 且与原 parent_core 全数组相等 | 新 source 明确验证原参考初点在新布局中的准确嵌入；保原 seed 与原 baseline 身份，另记新布局 point SHA |
| 307ebae… literal-Q binder | definition 含实际 base 与 initial-full-point 身份 | 独立精化 binder 重绑来源/布局；十八字、准确支撑和数学 Q 保持，不能冒旧 definition SHA |
| c79c7f7… material memory | 固定原 $J/P/N$、mesh 与原 context.core；没有固定当前自由 $M$ | **M-only 可直接继续用这套完整旧 E**，只要冻结 context 与全部原地址仍实际相同；radial/N 才需要独立完整迁移消费者 |
| geometry/driver/reader/可选性能 helper | 完整 source/schema、模型、norm、实际布局守卫 | 为新模型生成完整独立源并逐角色绑定；不改已排旧源，不放宽旧消费者来偷收新场 |

当前标准 SO3 合成是直接 sin/cos 矩阵乘法，不是旧 q 的 FFT/DCT。因此 R678 的 $N>4M$ 不是此新算子的数学定义域条件。可明确选择 $160\to320$、保持 $N=2048$ 作为一个具体首实验，但不把该选择当作一般 SO3 别名已消或新前门。$\exp(\omega\times)$ 及隐式 core/normal 链本来就不具有旧有限角带宽。

## 4. SO3 的准确频率嵌入

当前世界轴旋转为
$$
\begin{aligned}
\omega_x(s,\phi)&=\sum_{j=0}^{M}X_j(s)\sin((2j+1)\phi),\\
\omega_y(s,\phi)&=\sum_{j=0}^{M}Y_j(s)\cos((2j+1)\phi),\\
\omega_z(s,\phi)&=\sum_{j=1}^{M}Z_j(s)\sin(2j\phi).
\end{aligned}
$$
共 $n=3M+2$ 个通道，但实际分段长度是 $(M+1,M+1,M)$。R676 的旧 q 分段是 $(M+1,M,M+1)$，两者不能互换。

对 $M'>M$，每个节点和三 jet 槽分别作：
$$
\begin{aligned}
[0,M+1)&\longrightarrow[0,M+1),\\
[M+1,2M+2)&\longrightarrow[M'+1,M'+M+2),\\
[2M+2,3M+2)&\longrightarrow[2M'+2,2M'+M+2).
\end{aligned}
$$
其余新通道为准确零。当前 core 的前 $M$ 项逐字复制，新增项为零；固定前三项与 H 不动。所有旧自由字只复制，不重新拟合或投影。

全部旧系数函数及其 s/phi 导数准确不变，因此 $\omega$ 和 $\exp(\omega\times)T_*$ 不变。$\Theta_c,\rho_c$ 及当前 core 逆图也准确不变，因为只加零项。原固定参考图根本不改。

完整径向自由槽数是 $3J-3$：只固定 core 的旋转值，以及 cap 的旋转值和一阶径向 jet。故
$$
d(M,J)=(M-3)+(3J-3)(3M+2)+1,
$$
纯 M 增量为 $(9J-8)(M'-M)$。不能照抄 R678 原 q 自由维数。这里没有去掉旋转 gauge、没有删除任何原自由量，也没有把六隐式控制改为额外独立 outer 变量。

## 5. 同场包含还必须经过全部 normal 链

设准确闭合函数使用 R715 的中心化形式
$$
f(x,u,\phi)=S^{-1}\left[
(\Gamma_c-\Gamma_*)-(P_H-P_*)+
\int_0^S\{\exp(Bu)\exp(\omega\times)T_*-T_*\}\,ds
\right].
$$
$B(s,\phi)$ 只依固定准确 S、固定十八字 Q、固定材料图、固定 bubble/gamma。令 $E$ 为第4节方向嵌入，$\iota$ 为状态嵌入，则对**所有**六控制 u，
$$
f_{M'}(\iota x,u,\phi)=f_M(x,u,\phi).
$$
这不是只在所选根处的等式。

R703 的第 i 段是
$$
A_{i-1}=f_u(x,u_{i-1},\phi),\qquad
u_i=u_{i-1}+A_{i-1}^{T}\eta_i,\qquad
f(x,u_i,\phi)=(1-\tau_i)f(x,0,\phi).
$$
从 $u_0=0$ 逐段归纳：若沿用同一个准确已选根，则旧 $A,\eta,u$ 全部也是新空间的根，完整物理场相等。若各段交叉 Jacobian $f_u(u_i)A_{i-1}^T$ 在所选解处可逆，普通参数 IFT 给其局部唯一延拓；于是可将新分支定义为旧分支的兼容延拓，在该邻域有
$$
F_{M'}(\iota x)=F_M(x),\qquad
J_{M'}(\iota x)E=J_M(x).
$$
按 R703 完整微分，此等式包含所有上游 frame、core/H、角一二 jet；没有把 $A(y,u_{i-1})$ 的导数冻结。其普通坐标转置满足 $E^T(D F_{M'})^T=(D F_M)^T$。若星号表示带内积的伴随，则准确写成 $E^{\dagger}J_{M'}^*=J_M^*$，其中 $E^{\dagger}$ 为相应方向范数的伴随；须采用同一观察内积，并使用第6节的等距嵌入或与它对应的归一化坐标，不能把任意重标坐标的转置直接混用。

**条件范围。** 仅有“同一 Newton 零初值与容差”不能证明两个普通浮点求解选中同一个准确根，更不能证明全角统一分支或反射接点 C²。实际新初场必须重读；R707 的局部根包围、上游同支和全角拼接责任继续保留。这里不要求把这些未付条件先证完才允许完整新求解；失败要如实报告，不能继承父 flag。

当前源的 checkpoint 只存 outer core/omega/H 和完整模型，不保存全角准确分支证书。因此不能把一个新 checkpoint 路径自动叫作同一全角已认证物理场。对于准确原参考初点，R714 已给出的零链是可用的特例；不能把此特例迁给任意实际非零末点，或强置工作残差为零。

上述结论是新模型包含旧模型的**同分支条件恒等式**。它不证明任何旧/新有限空间中存在精确等距根，也不证明固定 normal 选择覆盖所有可能闭合场。

## 6. M-only 的有限函数、范数与算法参数

最小首入口保原 carrier 文件、所有观察 cell/u、目标 a 载体、正权、full N、角字、orbit、经线积分 mesh/Q、参考工作规则和所有永久地址。其准确实数解释下，若第5节同分支成立，原 native relative Gram/loss 在嵌入上相同。谱 p/epsilon/scale 和观测混合权必须取实际父报告，不把 R676 文中的旧 p8 默认移给当前 p4。

普通浮点数组维度、trig 求和、core 逆图和隐式 AD 的运算路径可能改变。因此分别报告：

1. 实际父末点的原报告值；
2. 新完整 driver 对补零初点的真实重读；
3. 新完整空间求解后的真实末点。

第2项减第1项是同数学输入的评价/选支路径差；真正当前新表示上的求解归因是第3项减第2项。不能把补零本身叫作改进。

现 SO3 的两个母范数都逐旋转频率分离，角尺度为固定 $\sigma_\nu$，free-core 权由本频率 $1-\nu^2$ 给出，H 权不变。M-only 径向 mesh 和节点权不变，因此 jet-sum 与 integral 两种范数在嵌入的旧方向上均准确相同。此处使用源中真实 SO3 范数，不冒 R678 旧 DI/height 范数。

新 norm 记录的数组形状和完整身份当然不同；不能要求新 SHA 等于旧 SHA，也不能绕过原 restart 守卫。新入口明确登记范数限制恒等式与新实际 factor/norm ID。终末 $\mu$ 可在这个同单位合同下从实际父恢复，不按新自由变量数量缩放它。若另改 norm/坐标/算法，作为额外显式输入记录。

原 C 的数值行和旧维度矩阵不复制为新 C。全部原位置/分支/符号/伙伴语义保留，在实际新父重新求完整 point VJP，再过当前完整坐标转置。新频率方向必须进入所有原残差和约束；不能只在少数新增模式求校正。当前 coarse/preconditioner 的严格源守卫也应独立接新布局，不能把旧列贴上新标签。

## 7. 径向精化：可复用标量 Hermite，不能复用旧六 jet 结论

保持同一个准确 S，当前节点为 $s_i=\alpha_iS+\beta_i$。准确二分并在中点取原 $\omega$ 的值、一阶和二阶 jet，直接应用 R676-A 每一标量通道的唯一性，理想新 $\omega$ 准确等于旧 $\omega$。core/H、参考对象、Q/gamma、normal 分段均不动，第5节的条件包含随之成立。

保存 binary64 新中点 jet 时，R676 的中点公式和向外算术可复用；但要：

- 用 SO3 的三段世界轴频率打包，不执行旧 core-T 派生槽覆盖；
- 保旧节点字与结构零槽，新的准确符号节点另有 carrier；
- 对每个新增三 jet 保存实际载体减理想限制的向外盒，零通道保持准确零；
- 只把这些盒称作 $\Delta\omega$ 及其所需导数差，不叫作完整 $\Delta F$ 盒。

世界轴基本身不随 phi 旋转，所以其导数只乘相应 odd/even 频率，不使用 R676(676.11) 的旧 $e_r/e_\theta$ connection。由 Bernstein 控制值可取得全域 $\Delta\omega,\Delta\omega_s,\Delta\omega_\phi,\Delta\omega_{\phi\phi}$ 等盒。再用 R694/R707 的完整 SO3 微分界，把它们传到未校正经线、准确 normal 链、闭合控制和全部物理六 jet。最终仍含 R715 raw defect lift、所有积分/浮点/参考误差，不能直接把 quintic 误差上界当成 reach 可继承的差界。

integral SO3 范数在理想同函数限制下准确相同，因为原积分逐胞可加；六点 Gauss 对指定 polynomial norm 的准确代数解释照 R699 使用。实际 hhat/权/factor/solve 的舍入费用仍分列。jet-sum 重新分配节点质量后通常不保持该限制等式，R698 已指出它不统一控制径向精化下的 H²；不得把同一个 $\mu$ 字自动解释为完全相同的新惩罚。可明确选择 integral 作为统一数学范数，或保 jet-sum 并如实登记其改变。没有理由先制造额外 fixture 才能使用已经完整实现的范数分支。

## 8. fine 点必须使用准确仿射查询，固定 seed 不重造

旧 provider 0d09 的公开 `evaluate(cells,local,phi)` 把 cell/u 解释在**原参考节点**上。新的 trial cell 不能直接传给它。即使二分，新点转回旧胞的局部数 $(j+u)/2$ 也未必能由一个 binary64 准确表示；不能把舍入后的旧 u 当作准确同点。

完整新 provider adapter 应保原 seed 对象/均值计划/冻结 core/H，新增明确接口：

```text
evaluate_affine(exact_pairs, phi_words)
evaluate_on_layout(current_nodes, cells, literal_local_u, phi_words)
```

其中 `evaluate_on_layout` 先以 Fraction 构造每个准确
$$
(\alpha,\beta)=(1-u)(\alpha_L,\beta_L)+u(\alpha_R,\beta_R),
$$
再交 `evaluate_affine`。已有原地址可命中旧 scalar cache；新增点使用同一 WholeAxisymmetricLaw 的准确仿射查询。区间跨 prefix/analytic/Hold/deep 或支撑边界时按完整准确分片/hull，不按工作 mesh 的 region 标签裁掉真实可能性。

同角的 v/d/w/lambda 及其两角 jet 仍来自**原冻结均值方程与原规则**。不因 fine mesh/M 变了就重新定义平均、用当前 H/core 造 seed，或令参考的 $M_*$ 跟随当前 M。原 seed definition 作为数学对象完整保存；新 evaluator source 与新查询缓存另有身份。若将来提高参考求积精度，这是同准确参考的工作求值细化，需另列其载体误差，不成为换 g 的借口。

场的 outer 积分可选择在 fine mesh 上保同 Q，从而细化全/partial 求积。它改变工作闭合方程与 raw-lift 值，不能宣称转移 initial 的全部数值逐字等于旧场。R715 calibration 必须在这次实际完整规则上，用固定原参考初点的嵌入重新生成；不得抄旧 delta_ref，也不得删它。若为了分清误差来源暂保旧积分 partition，必须把 trial mesh 与积分 mesh 显式分离，并仍有真正后续积分细化；不能把粗积分读数冒连续定义。

## 9. 完整观察、历史和有限 envelope 的迁移

径向二分的准确位置映射继续用 R676(676.15)：$u\le1/2$ 取左子胞，$u>1/2$ 取右子胞；以 Fraction 核新旧准确 $s$ 一致，再核新 local carrier 准确可表示。literal phi 原字保留。此处 phi 是固定材料图地址，不应再通过当前 $\Theta_c$ 重新变换。

新观察必须完整保所有父行，并让每行在实际 loss 权下严格为正；新增 node/mid/Gauss 只追加。可复用 R676 的正权混合思想，但混合系数取明确新政策，完整保存父实际权与映射，不能谎称 native fine Phi 是原有限函数。新增 a 点查询同一准确 scalar，旧 common-parent 读数保父 a 字与父权。

历史不止显式三元组。必须包含：

- 原完整 P0，曲率/半径/protected 角色；
- 旧/current material envelope 的完整隐式 G；
- 每个已实际发生报告的新增点、全部 trial 和 SOC typed rows；
- principal branch/sign、正负握持符号、actual D partner、first-discovery 来源；
- 当前 policy 把整个 E 潜在 protected 的责任，不伪造未知旧晋升顺序。

M-only 的 J/P/N/phi/原 context 不变，c79 的上述完整 E 可保持原字消费。radial/N 精化则构造独立完整 `RefinedMaterialEnvelope`：先在各父自己的 carrier/N 下解码 tagged grid，按准确地址迁移，再并入 fine G。旧 G 的所有点继续真筛，不以新 grid 很接近来删点。当前新增 typed 值必须在 fine 当前场重读，原几何数值、旧 C 或旧有限通过 flag 不迁移。

新 envelope 中 partner 若只给旧 grid 索引，也先在其所属父规则恢复完整 cell/u/phi；不能只迁主曲率点而丢 D partner。只合并数值完全相同的地址，不按 round13 或最近网格归并。raw 大数组留 runner，公开完整 producer/参数/来源/run/SHA 和紧凑读数。

## 10. N-only 与共同父函数

在真正固定物理场及同分支下，R679 的 $\Phi_{2N}=(\Phi_N+\Phi_N^{odd})/2$ 和样点最大值集合关系原样适用。固定 $\theta_0$ 后，旧 literal phi 保留同一材料角；倍增公式实际偶列字也要读取核对，不凭标签填 true。

新 complete observer 可以保原4e参考上下文，仅独立设置当前 full N/phi/orbit。不能调用只接受2048的原 `create_problem` 后伪造其来源记录。反射/quarter 的准确范围由当前 seed、omega 奇偶和 normal 同分支共同承担，必要时完整全角读者仍是合法选择；这不是旧 carrier 自动证明的性质。

N-only 不改变当前自由布局和数学母范数，但会请求新角的参考均值根、normal 根和几何读数。旧完整参考文件仍为同一固定对象；新工作批必须有自己的真实来源。C1/矩阵缓存仅按实际新角/图/字键命中，不继承另一个 N 的错误缓存。

共同归因采用同一个新算子/同一实际 buffer 读 transfer seed 与 final，分别列旧 even、new odd 和 all。径向精化同理列 complete-parent 与 native-fine。不得用不同网格/不同工作积分的 parent native 与 final native 直接相减宣布求解下降。

固定 t 族继续按 R248 和当前同场合同准确生成。normal 的 tau 精化或 N 的半步角都不是物理 t 网格精化；不另造时间离散求解门，也不省 README 要求的若干 t 网格导出。

## 11. 建议实现的最小完整源包

**首先做 M-only，随后接 radial/N。** 它避免在第一次新布局中同时改参考查询、积分规则和观察权，且不是以冻结输入为新的执行前门。选择真实已返回的完整 parent；没有实际 parent final 就不填候选 SHA。

拟定接口如下，文件名是设计名，尚未生成：

| 新完整源 | 真正职责 |
|---|---|
| `so3_fixed_reference_refinement_layout.py` | 全 source/model/父报告绑定；current M/J 与 frozen M0/J0 分离；SO3 三频道注入；完整当前 point 与原 baseline 嵌入记录 |
| `so3_refined_fixed_seed_meridian_operator.py` | 新 base 完整布局；旧数学旋转/全 free/core/H 保留；固定图与当前逆图各用其正确频率；完整 norm |
| `so3_refined_reference_centred_normal_operator.py` | 全32段及角6m/9m/外 J/J*保留；准确同 seed/Q/gamma；新 calibration 与 baseline-layout 身份；六 jet raw-lift不删 |
| `so3_refined_reference_binding.py` | 精确旧参考/Q/input→新布局来源重绑；不改变十八字或 seed definition；正常 restart 仅收同新完整模型 |
| `so3_refined_geometry.py` | 新严格 source guard，全原 scan/192-prefix/幅度/typed/全E；原 matrix 不搬维度 |
| 完整 driver/launcher/pure-reader | 用当前真实算法全体，保历史与 actual terminal μ；分别记录 transfer initial、native final/common-parent、失败实际状态 |
| radial-only 后继 adapter/transfer/observer/envelope | 第7–9节全部准确节点/载体/历史责任；不通过改旧4e或c79标签实现 |

对已有 C1、detached/adjacent 矩阵性能层：可在新 source 下严格重派生相同数学方法的 guards；如果尚无相应 helper，先使用完整原 AD 也是同一科学方法。不得为复用性能层省掉新变量或上游 frame 导数。是否更快只由真实 Actions 返回说明。

M-only 的 transfer-only 输出应至少有：原 report/final/source/bundle 真绑定、全部旧输入与固定参考 ID、新 M/布局/point、精确频道映射、原 core/H 字保留证据、结构零槽、旧/新数学范数说明、全 history 来源及新完整 source/argv。它不能输出 `continuous_same_field_certified=true`，也不能把 coordinate seed 在缺少新 full model 的情况下冒成合法 final checkpoint。

## 12. 仍未支付及真正下一步

没有任何一条空间包含定理能保证该固定 g/固定 seed/固定 normal 选择中存在精确等距 flex。R691 的必要兼容性也没有变成充分性；R700 的范数控制明确固定 M，随 M 增大要重新支付其频率常数。不能用新空间变大代替实际连续最大误差趋零。

本次已完成的是：四篇指定旧结论的完整阅读、当前源的确定接口审查、SO3 通道和维数、同分支 normal 包含证明、范数限制范围、准确新点/工作积分/calibration/typed E 的完整迁移设计。没有新增科学候选、精化读数或收益宣称。

下一实际实现应从当时真实可用的 complete parent 选择 M-only 的完整新入口，保原工作规则与全部历史，随后按实际结果做同 g 的 radial/N 层。无论一层接受还是拒绝，都保真实新点并继续完整目标；本设计不是停止条件，也不放宽 README。


## 13. root登记与实施边界

root于2026-11-27完整读取本文后登记。原始22745-byte设计的SHA256为`1d9e4aba17da7f82663bc61bd5c851f9e3909a8bbbda6e1a14e36c8d49b9dde3`；本版只补§5转置/内积作用域及本节，不改变条件包含结论。该结论针对当前SO3/完整normal表示，既不重复R676旧R/T/Z布局，也不把R678旧FFT带宽条件搬成新前门。

当前完整M-only源的实际实施已开始：保持原4e/0d09冻结参考上下文，另设current M320的布局/core逆图/三旋转通道；normal仍完整32段和全部角/参数导数。完整driver/launcher/typed转移/pure reader尚在完成，未有新的M320实际科学返回。本文“未实现入口”的状态指设计锁定时点；不能拿实施中的文件或源审查充当已准入、已求解或已完成精化的记录。

08相邻frame完整粗空间入口已由提交`291adcd2b2f4de1dac4c7118dbce69b471dc5813`实际推送，Actions `45929088658/1`启动。未来fine层选择当时真实可用的完整parent，绑定全部终态/变量/输入/历史，并在新source中重读完整初场；不预填一个尚未返回的08末点，不把独立原参考起跑冒成粗末点转移。

当前每个具体科学任务继续运行；本条件论证及接口设计不是README完成证书，也不是暂停研究或要求用户另行批准的理由。
