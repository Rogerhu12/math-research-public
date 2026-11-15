# R281 到实际闭场链：准确边界与两帽连续有理球

2026-11-15，geometry，AI-assisted。**源码分析与独立生产器接口；没有执行新科学计算，也没有实际接受闭场。** 本文不增加 native、BVP、metric、reach 或 held 的接受门，不重复 R280/R281 的相位证明。

## 1. 当前实际入口不是 mixed-pair 相位消费者

以下已读源码已逐项用公开提交 `763f5d841ac86548aca689fd0154ce31875b5dd9` 的 Git tree blob OID 核对，全部与本地已读原字节及下列 SHA256 一致。此次只读 tree metadata，未取科学 payload。旧源全部保持不变。

|实际层|入口及源 SHA256|实际职责|
|---|---|---|
|闭场编排|`geometry_20261114_full_dn_closed_followup.py`，`54079bcdd1d8ddc2b9321d940b9b43f3448f3a5cab11444df649bf16d2365634`|`build` 消费自己的真实 full-DN/尾输入；`measure` 把显式同场 envelope 传给原 cover，再独立运行 held。|
|共享 B 加载|`geometry_20261114_shared_background_continuous_cover.py`，`fc5bbb6762cf589a8ab6096c066bdd1bbad17c516954a43c4a40496445e9a5fb`|通过 `load_shared_bundle` 绑定新几何；没有改变原空间门。|
|完整场中心/法向|`geometry_20261114_full_state_continuous_cover.py`，`c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6`|用完整 SavedPrefix、材料角、实际尾、原 mean/SE2 重读中心与法向。连续误差预算仍是输入。|
|实际 R241 budget|`geometry_20261114_continuous_cover_budget_v3.py`，`3362fc35c09b98a8feb10706f2b126c9bc45e7d45a4294c928b4b72e59d2c7a1`|对**去掉固定 marker 的静态闭面**验证空间块，再用 R24 支付 marker 扰动。|
|整像位置包|`geometry_20261114_held_hausdorff_cover.py`，`3ba8a0d02266d2b057862c0741dc0a6f65c1276514adab8e403852d69a55809c`|保存全部活动位置块和两个完整固定帽的 disk/height 包围，供真正整像 held 下界。|

v3 的 `main` 先计算 `target_tau=.03*marked_D_upper`，再从 R24 的 height/gradient/Hessian/support-separation 预算计算 `base_tau`。随后其全部 spatial pairs 都是 **static base** 的点对，最后报告 `entire_phase_circle_reduced_to_static_base=True`。这两个 tau 有不同职责，不能把其中一个替成另一个，或为了让 R281 通过而改变它们。

旧门包括 complete active self-cell 的短路径、静态距离、平帽径向排除、两端原 normal-cone、失败 prefix 对的完整 angular children；每个已付门保留。`numerical_cover_budget_passed` 仍要求旧 uncovered=0、curvature gate、marker gate、sample-containment 全部成立。源码明确 `continuous_reach_interval_certificate=False`。

因此，**把一个未付静态对的左端送去绕轴旋转不是合法 fallback**：那会换成另一组几何点对。R281 处理的是正确的 moving/fixed 连续球，而非给所有未付静态对增加一个相位参数。

## 2. 现有输出的精确缺口

`write_position_cover` 导出 `finite-closed-active-position-cover-v1`。其 NPZ 只有 `centers`、`enclosures`、`source_vertex_indices`；另有共同 axis、全部活动覆盖声明、完整两帽的平面 disk 与 marker-height 包围、同场 bundle SHA。

|R281/完整 mixed 责任所需|当前实际已给|当前确切未给|
|---|---|---|
|同一几何身份|plan/assembly/shared-B/mean/SE2/原 target metric 绑定|没有实际 accepted full-native/full-DN 场，不能用失败状态补造。|
|活动位置球|全部活动中心、数值 enclosure、来源索引|其连续有效性及求值/舍入上界没有由当前源码导出为严格证书。|
|活动单位法向球|运行时有中心 normal 和 projector-cone 数值|位置包不保存 normal、正常量球 radius 或完整选向依据；projector 的 sine 不能不加说明地改标 Euclidean normal radius。|
|固定 marked-cap 球|整帽 disk 与高度上界|没有分块的实际 bumped-cap 位置/单位法向球。静态 cover 中使用的是 unmarked 平帽。|
|完整待付 pair 责任|总计数与全活动 position cover|`worst` 受 `witness_limit` 截短，单失败父对只列至多 4 个失败 child。它不是完整 mixed pair 清单。|
|固定轴与配准|canonical cap frame 的轴 `(0,0)`，唯一原 SE2 被 shared loader 保留|不可对不同坐标系的球重新拟合；未来 pair 包必须继续绑定同一个 frame。|

旧精确有理入口 `root_bottleneck_distance_cover.py`（`6efed6468e5e1cc07150d3add8c7dfa86e20a166ac4b199686bb5c1953c78788`）也不是漏接的实际闭场 exporter：它检查**外部给定** rational pair 条件，且对 `motion='rotating-fixed'` 的 normal-ball 行明确要求另外的全相位界。它不构造连续球、完整空间 cover 或实际场。

现阶段不能诚实生成“R281 已接实际 R241 全面验证”的结果，也不宜再造一个重复的独立 cases-JSON wrapper。最小有用推进是先补一个真实缺失的球生产边界。

## 3. 选择补齐的真实有限表达式：原固定两帽

新增独立入口：

`computations/geometry_20261115_fixed_cap_rational_balls.py`

它只消费已经真实生成的共享 B `plan` 和 `assembly`，二者 SHA 均由 CLI 显式提供。没有演示默认参数、没有假 accepted field、没有新场构造、没有新 mesh，没有 BVP/RHS/J/ODE 调用。当前没有给它任何 actual 输入，也没有运行它。

实际继承链是

`SharedBackgroundAssembly` → `LargeCoreAssembly` → `RefinedAssembly.cap`。

两帽的有限实定义是：令 $\varepsilon=+1$ 表示上帽、$\varepsilon=-1$ 表示下帽，原 cuff 为 $r_c>0$，原 absolute cap-height 为任意有限实数 $H$，则

$$
X_\varepsilon(x,y)=\bigl(x,y,\varepsilon[H+b_\varepsilon(x,y)]\bigr),
\qquad x^2+y^2\le r_c^2,
$$

$$
b_\varepsilon(x)=\sum_{j\text{ on this cap}}
A_j\left(1-\frac{|x-c_j|^2}{R_j^2}\right)_+^4.
$$

这里每个 $A_j,R_j,c_j,H,r_c$ 都取原 JSON 解码后的实际 binary64 值，随后作为精确有理数；整数原值按整数处理。**不**把浮点 JSON 的打印十进制重新解释成另一精确十进制场。

新入口绑定原 `shared_background_geometry` 全字典、原 fixed-cap 定义 SHA、原 cap-height、原唯一 SE2 标识，并固定在原 canonical cap frame。没有新坐标拟合、平移、旋转、缩放，也不修改原 $g$、共享 B、marker 支撑、帽高度或上下反射。

原 `RefinedAssembly.cap`、其 `LargeCoreAssembly`/`SharedBackgroundAssembly` 继承及 cap-height 形成没有不可缺的 $H>0$ 前提。位置球对常量竖直平移不敏感，法向只依赖梯度，因此本入口保留任意有限原 $H$，包括零或负值；只要求原 $r_c>0$。旧 held writer 对两帽分离的正高度要求仍在自己的调用范围，不能作为本局部球生产器的新门。两帽是否分离、全曲面是否嵌入仍由原完整几何责任判断。

### 3.1 原 graph 导数与独立 kappa 字段

原 `cap` 位置使用 `row.height` 和 `row.radius`；它的精确图梯度系数是

$$\kappa_j^{\rm graph}=8A_j/R_j^2.$$

原 `cap_normals` 用另行保存的 `row.kappa`。理想设计公式使两者对应，但各自经过 binary64 形成后，源码没有给出两者作为精确实数恒等的保证。这里**不声称实际已有差值**，因为没有为本生产器读取任何新实际场。

新生产器从原 graph 参数精确求导，并将 `stored_kappa_equals_graph_derivative` 及精确差作为诊断，不以它们建立新的接受门，也不改原 renderer。这样新的 normal ball 绑定的是原有限图的数学法向，不是未经付误差的浮点 normal 样本。

## 4. 连续球公式及其证明

以下是已有 R14/R21 标记公式的直接包围实现，不新增 reach/曲率/全场定理。

### 4.1 单 bump 的全域导数界

对 $b=A(1-u)^4_+$、$u=|x-c|^2/R^2$，在 $0\le u\le1$ 有

$$
\nabla b=-\frac{8A}{R^2}(x-c)(1-u)^3.
$$

Hessian 的切向、径向特征值分别为

$$
-\frac{8A}{R^2}(1-u)^3,
\qquad -\frac{8A}{R^2}(1-u)^2(1-7u).
$$

前者绝对值不超过 $8|A|/R^2$。令 $f(u)=(1-u)^2(1-7u)$，则

$$f'(u)=-3(1-u)(3-7u).$$

端点值为 $1,0$，唯一内部极值 $u=3/7$ 给 $-32/49$，故 $|f|\le1$。支撑边界外函数为零，跨支撑边界至少 $C^2$，以上全域 Hessian 界仍成立。再从中心零梯度沿半径积分，得

$$\|D^2b\|\le8|A|/R^2,\qquad |\nabla b|\le8|A|/R.$$

令闭 rectangle $Q$ 的 center 为 $z$、half-diagonal 为 $\rho$。只计入支撑圆与该 rectangle 可能相交的 marker；对严格不交者用准确的 rectangle-to-center squared distance 排除。以非严格相交为保留条件，因此切触支撑的情况没有漏掉。

令

$$G_Q=\sum_{j\cap Q\ne\varnothing}8|A_j|/R_j,\qquad
K_Q=\sum_{j\cap Q\ne\varnothing}8|A_j|/R_j^2.$$

不要求 supports 不交；三角不等式允许重叠。rectangle 凸，故对任意 $x\in Q$，

$$|b(x)-b(z)|\le G_Q|x-z|,\qquad
|\nabla b(x)-\nabla b(z)|\le K_Q|x-z|.$$

### 4.2 位置球

取精确 graph center $q_0=X_\varepsilon(z)$。它不必在 $Q\cap\{|x|\le r_c\}$ 内；包围球的中心没有该要求。对帽域内全部 $x\in Q$，

$$|X_\varepsilon(x)-q_0|\le \rho\sqrt{1+G_Q^2}.$$

源码用原 R62 `sqrt_upper` 返回已证明向上 dyadic 平方根，形成有理上界

$$e_Q=\rho^+\sqrt{1+G_Q^2}^{\,+}.$$

没有用 grid 采样、中心误差猜测或经验外扩。这里包围的是精确有限图，非浮点 renderer 的逐值舍入误差。

### 4.3 法向球及上下帽

分别选择上帽向上、下帽向下的连续法向，写

$$w_\varepsilon(x)=(-\nabla b_\varepsilon(x),\varepsilon),\qquad
N_\varepsilon(x)=\frac{w_\varepsilon(x)}{\sqrt{1+|\nabla b_\varepsilon(x)|^2}}.$$

下帽 $X_-(x,y)=(x,y,-H-b_-(x,y))$ 的向下法向正是上述式子；不会把上帽反射只用于位置而遗漏法向方向。

映射 $v\mapsto(-v,\varepsilon)/\sqrt{1+|v|^2}$ 的微分算子范数不超过 1，因此

$$|N_\varepsilon(x)-N_\varepsilon(z)|\le K_Q\rho.$$

令 $w=w_\varepsilon(z)$、$s=|w|^2\ge1$，取原有理上根 $L^+\ge\sqrt s$，输出有理中心 $m_0=w/L^+$。它不必恰为单位向量，这与 R62/R281 的输入合同相同。因为 $\sqrt s\ge s/L^+$，

$$
\left|\frac{w}{\sqrt s}-\frac{w}{L^+}\right|
=1-\frac{\sqrt s}{L^+}
\le 1-\frac{s}{(L^+)^2}=:\delta_0.
$$

于是完整单位法向球半径为

$$\eta_Q=K_Q\rho^++\delta_0.$$

`fixed_normal_centre` 与 `fixed_normal_radius` 正好可作为 R281 的固定端输入。不能把 `K_Q*rho` 单独当作总误差而忘记中心归一化误差。

### 4.4 全 disk 覆盖和收敛

从 $[-r_c,r_c]^2$ 作原点坐标中的闭 quadtree 划分。只在一个闭 rectangle 到原点的准确最小平方距离**严格大于** $r_c^2$ 时剔除；等号保留。其余叶代表 rectangle 与原闭 disk 的交集，重叠边界有意重复覆盖。每个 split 包含全部四个闭子框，因此不存在角度接缝、极点漏项或被截掉的失败叶。

完整输出保留所有 retained cap cells 和所有严格 outside 省略记录。两帽分别生成，不能将一个帽的 normal center 重标为另一个帽。

固定有限个 marker 的 $G_Q,K_Q$ 有共同有限上界，$\rho\to0$。源码取 `effective_sqrt_bits=base_bits+depth`，归一化上根误差也趋于零；因 $s\ge1$，$\delta_0\to0$。所以位置球及 normal 球半径均随 refinement 收敛到零。这是有效连续球生产条件，不是凭 $C^2$ 名称声称存在某个无法计算的 modulus。

`max_cells` 只限制显式完整 grid 的资源预算。若不容纳所请求的两帽 grid，入口以资源错误退出，不产生“几何失败”判断。

## 5. CLI、依赖与输出

未来真实调用模板为：

```sh
python computations/geometry_20261115_fixed_cap_rational_balls.py \
  --plan ACTUAL_SHARED_SURFACE_PLAN \
  --plan-sha256 ACTUAL_PLAN_SHA \
  --assembly ACTUAL_SHARED_SURFACE_ASSEMBLY \
  --assembly-sha256 ACTUAL_ASSEMBLY_SHA \
  --source-directory computations \
  --depth EXPLICIT_DYADIC_DEPTH \
  --sqrt-bits 128 \
  --max-cells 1000000 \
  --out "$RUNNER_TEMP/fixed-cap-rational-balls.json"
```

所有 `ACTUAL_*` 待实际输出生成后传入，不预填未来 SHA。`require_actions` 同时核 `GITHUB_ACTIONS=true` 与 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。没有本地示例执行或新 fixture/workflow。

四个源码依赖只读原件 SHA：原 R62 exact sqrt kernel；`exact_20261114_refined_tail_adapter.py` 的实际帽定义；`geometry_20261114_large_core_closed_assembly.py` 与 `geometry_20261114_shared_background_closed_assembly.py` 的继承和不改帽合同。**只有 R62 的标准库数学 kernel 被 import**；不构造 SavedPrefix、TailClient、LargeCoreAssembly 或 SharedBackgroundAssembly。

结果 schema 为 `same-shared-field-two-fixed-cap-rational-balls-v1`。每个 cap-cell 导出：

- 完整 closed box、quadtree path、upper/lower、fixed-motion 标记；
- `fixed_position`、`fixed_position_radius`；
- `fixed_normal_centre`、`fixed_normal_radius`；
- 所有 touching marker 索引、$G_Q,K_Q,\rho^+$、精确中心梯度、normal numerator、归一化误差及精度参数；
- 原 plan/assembly/完整几何/marker 原数值位身份，未用 nominal kappa 替图导数的说明。

完整结果只作 Actions 临时数据，不上传 raw、不入 Git/Release。标准输出仅实际输出 size/SHA、真实输入 SHA、cell 数和范围标志。代码/参数/run/SHA/紧凑结论按第15条保存。

## 6. 对真正 R281 adapter 的最小后续合同

固定端字段齐后，仍须从**同一实际有限场**取得正确的活动位置/normal 球和完整空间块责任。可按以下准确边界接入，不能跳过其中几何含义：

1. 保留整个旧静态-base/R24 路线及其既有判断；该路线已经付的原对不重新审。
2. 只有明确 `motion='rotating-fixed'`、且两端均为连续球的实际 mixed pair，才交 R281。固定端可直接引用本生产器 cell，活动端必须给自己的正确证据和原坐标 frame。
3. 使用同一原目标 $\tau$ 和整面 $D$ 责任；不将 R24 `base_tau` 混作 marked target，不降低曲率或整像门。
4. R281 的已有 whole-circle distance/两端/joint OR 与两图 fallback 全保留。只给一个 pair 全相位结论，不自动构成完整空间 cover。
5. 新路线还必须覆盖 active-active、fixed-fixed、自块、共同 cuff/接缝附近的 local path 责任。marked-cap 自块不能无依据沿用“unmarked flat cap”标签；可使用已有图 Hessian/法向弦论证的准确范围。
6. 完整 mixed 列表不能从 `worst` 截短样本恢复。将来应在实际完整 block 枚举的原边界流式转交每个仍需负责的 pair，保持全部旧 path/spatial/curvature/同 $g$/held 合同。

目前缺的是实际场及活动侧正确球/完整 mixed 枚举，不是再加一层审核。这个生产器只消去已能由现有确切有限表达式解决的固定帽数据缺口。它没有声称当前 closed chain 已经得到全 $t$ reach、全域 metric、整像 held、$\delta_E$ 或 fixed-$g$ 精化结论。
