# R715 的完整参考中心化 R711 normal 入口

## 1. 本次实际交付和未执行范围

本次给出六个完整独立执行源、两个完整纯源码再生器、同一组十份历史输入的两步参数，以及精确源码身份表。它直接采用已刊 R711 的完整十二段平滑三角参考、原 R690 准确标量目标和原完整自由点布局，并实现 R715 的参考中心化闭合方程与完整六 jet 数值校准。这里没有执行科学计算，也没有填入尚未返回的场、报告、模型或连续证书身份。

原未运行的 plain R711 normal 参数只作为本次参数与完整代码的来源；它不构成必须先运行的科学前驱。新中心化入口可以直接成为下一条完整 R711 方向。真正已经发生、或在本入口准入前实际执行的同目标报告仍须进入永久地点历史；不能以换表示、换源码身份或等待结果为由删除这些责任。

本说明实现已刊的 [R715](../results/R715-reference-centred-normal-sixjets-and-error-ledger.md)，不另登记重复数学结果。准确参考的存在、角向分支和误差责任分别沿用 R708/R709、R711/R712、R713、R703/R707；这里只说明新的完整源怎样实现其已明确的条件与数值差额。

## 2. 完整文件及身份

下列执行源部署于 `scripts/resume_20261126/`。每份均为可完整核读的文件，小于 100000 字节；不是省略主体的 patch。

| 完整文件 | 字节 | SHA256 |
|---|---:|---|
| `reference_centred_smooth_triangle_calibration.py` | 11884 | `a8e849068b12ffe2876c07ec2518947890c9f09614da2a9882b53e268e3ba873` |
| `so3_reference_centred_smooth_triangle_normal_lift_operator.py` | 94557 | `b2597012ec8ee063fabbb49a758b592d10f607de55ded3becaa8b62b6a50118d` |
| `so3_reference_centred_smooth_triangle_normal_lift_geometry.py` | 57809 | `6536a71b9db5858d258ecdf71ada39611772f4ff28fe857887fef142386376cf` |
| `fullclosed_reference_centred_smooth_triangle_normal_lift_so3_qp.py` | 68816 | `92233b4ffb0aaff1644e0c4bc9e7357a8eae37bd68e6d02ef0c6e0dcfbb31b81` |
| `launch_reference_centred_smooth_triangle_normal_lift_so3_actions.py` | 17523 | `68a6979d35fe7a953975c5a191928668765ddde7b4018fc7a8dee353138475dc` |
| `read_reference_centred_smooth_triangle_normal_lift_so3_report.py` | 67732 | `7fc213c108245cb2c555d573a52961fd07f1b941d85411e8e6e8d8c22f20a5bb` |

两个纯源码再生器也是完整文件：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `derive_reference_centred_smooth_triangle_normal.py` | 12379 | `3d12c0fcfba4e9477bb989f55917e3cd3d5d720338b297854e97800299a20040` |
| `derive_reference_centred_smooth_triangle_entry.py` | 41051 | `f05ff8ff07939fe62cb3deff333744861f9b2240008e0e19c5ef6e9dd18cba1c` |

参数文件 `computations/reference-centred-smooth-triangle-normal-full-history-run05-ready.json` 为 31298 字节，SHA256 为 `db99d87e07974848ac61b6b93bb294cb1fbeb28faf7187edc8f072ce6d8b8934`。它完整保留原参数的科学 argv，仅更换新的 entry 路径、独立输出目录与步骤身份；所有新增 summary 都指向标量或允许未读的 null。

纯文本再生器另在临时目录生成 `reference-centred-source-lock-table.json`，记录原五份主体、helper、再生器、派生结果与 AST 比较范围；这份可再生成的输出不入仓库或 Release。其实际输出为 4064 字节、SHA256 `14074d69c92be5e452365f83f861807532c55a6dc06982f424085e62c56973c8`；本节完整表与参数保留所需源身份。源码完成与静态核对均不代替真实运行后才生成的报告及候选身份。

## 3. 复用的准确目标、参考与完整参数

本入口原样使用以下已刊完整源：R711 mean `f8487dfe…`、参考 provider `0d09ca45…`、完整 base `6a80361a…` 和十二键字面 Q 输入 binder `307ebae3…`。其完整 SHA 都在 driver 的 27 角色源码注册表与两步参数中。原十八个 Q 字面字和历史 `05dc…` 定义只作为显式固定参数来源；本次仍通过原 R711 十二键 binder 重新绑定真实 reference、完整固定 seed、原初点及准确标量定义，不宣称它是当前场的准确矩逆。

准确标量仍由实际 reference/preparation/carrier/node/scalar 五份输入决定。当前全部自由 core 系数、全部共享 quintic 的三轴 omega 自由量、末槽自由 H、原 norm 和全部正权 Gram 行保留。原参考的 core 与 H 只用于冻结参考函数和数值中心；不冻结当前自由变量，也不把参考均值的逆当成 normal 控制的逆。

科学参数与原完整 R711 ready 相同：全角数 2048，quarter 计算载体及原轨道权重，922 个径向胞、全部 legacy/Gauss 观测；角块 8、工作积分阶 8、seed 端层分段正权阶 8、中央十二段各阶 16、边层总长比 `1/16`、中央 delta `1/128`。六个 normal 控制、每段三个隐式增量、共同 32 段准确分割均不改变。每个角和每个当前自由点使用同一分割。

首参数为一条最多 16 advances 的 metric 方向，至多四条各 64 advances 的完整 Phase I restoration；两初始 damping 均显式 `.01`。保留 p=4、epsilon=.001、scale=.05、legacy fraction=.5、完整原 192 工作集和追加幅度约束、reach ratio=.03 与 .992 工作安全系数、marked D=4.2、L=.9、Hfloor=1.01。数值目标 `1e-9` 沿原 ready，是求解入口参数，不冒题目原 solver floor 或完成标准。

## 4. 固定数值中心的来源闭包

新 helper 在构造时只冻结真实 `base.initial()`：原完整 core、全部 omega=0、原 H 的准确 binary64 字。它检查该点与 provider 定义、base 完整模型、源码、固定图和 H 相符。原初点数组是只读副本，记录包含 dtype、shape 和全部字节的摘要；当前自由点变化不能重选基线。

参考 meridian 的积分节点从同一 `base._parent_tensor(integration_query,phi,'integration')` 路径取得。参考端点三 jet 则经本次新 normal 自身的完整 Torch `_core_and_cap` 方法在冻结原初点求出，避免把 provider 的另一归约路径冒充本次端点工作字。固定角块使用完整 literal `phi.hex()` 列表作为缓存键；它不按近似角度合并地点。

helper 不硬编码自身未知调用者的未来全文 SHA，因而没有循环固定点。它严格核对调用者两方法的实际源码文件 SHA、明确的 endpoint schema、调用者全局注册的 helper SHA，以及同一对象和 base。normal 建模完成后，再一次性将 helper 绑定至该完整模型的 canonical identity。driver 同时硬 pin 两份完整文件，geometry 和 pure reader再核相同定义及原初点。后继若改变 endpoint schema，必须独立派生对应 helper 并更新完整来源链，不能放宽这一守卫。

每个实际参考角批的原始三 jet 校准差额记录为

$$
\delta_{\rm ref}^{(j)}=P_0^{(j)}-\Gamma_0^{(j)}-Q_ST_{\rm ref}^{(j)},\qquad j=0,1,2.
$$

这些值没有被强置为零。其完整数组只在 runner 的原参考缓存目录中保存，文件与各数组摘要、角列表摘要、字节数及三个实际最大范数进入报告。纯 reader只保来源摘要和标量归因；公开 controller summary不搬运这些数组。

## 5. 每个 normal 方程及全部上游导数

新 `_closure_jets` 使用

$$
E^{(j)}=(\Gamma_x^{(j)}-\Gamma_0^{(j)})-(P_x^{(j)}-P_0^{(j)})
 +Q_S\big(T(x,u)^{(j)}-T_{\rm ref}^{(j)}\big).
$$

参考在每个积分节点先减，再按原完整 cell 权重和 `torch.cumsum` 归约。`reference`、`reference_core`、`reference_cap` 三组数据完整进入 detach/subset 路径，不能只在完整批上中心化，却在单角 Newton 或 jet 升级时遗漏。

`_normal_frame_jets`、完整每段根、所有跨段前态和 frame、零控制 target、角一阶与二阶隐式矩阵、缓存升级、最终 implicit surrogate、jvp/vjp/point_vjp 均保留原完整方法。即使原初点的某些 forward 字面差为零，也不删除段、不强制控制或角 jet 为零、不跳过真正已声明的 stage 和残差检查。其外参数导数仍须读取 current core/H/omega、每个上游 normal frame 和原零控制 target。

实际 AST 比较确认 normal 原 49 个方法中 41 个相同；改变的八个仅为构造身份、当前点追踪、data detach/subset、closure、meridian data、physical fields 和 metadata。新增一个 `_reference_data` 委托方法。准确模型和工作表达的差别明确在新 schema，不借旧 source 身份换公式。

## 6. 物理六 jet 的完整工作 lift

记原 query 的 $h=1-S_5(s/S)$。本次每个角阶 $j$ 都按原实际积分规则读取当前已旋转、已 normal 修正的 $T^{(j)}$，置

$$
D^{(j)}=\Gamma_x^{(j)}-P_x^{(j)}+Q_ST^{(j)}.
$$

随后物理角 jet 为

$$
F^{(j)}=(1-h)P_x^{(j)}+h\Gamma_x^{(j)}+Q_sT^{(j)}-(1-h)Q_ST^{(j)}.
$$

完整径向和混合 jet 为

$$
F_s=T+h'D^{(0)},\qquad
F_{ss}=T_s+h''D^{(0)},\qquad
F_{s\phi}=T_\phi+h'D^{(1)}.
$$

这里所有当前 $D^{(j)}$ 都保持在 active graph 中。不能 detach 当前闭合差额，不能只在 $F$ 加一个常量而遗漏 $F_s,F_{ss},F_{s\phi}$，也不能只改根而让旧单位 $T$ 冒实际 $F_s$。这些六 jet 随后进入原完整 Gram、world curvature cotangent、全部幅度和 reach 筛及完整参数 pullback。

在准确参考闭合及准确最终 normal 根条件下，R715 已证明它与准确单位径向场相同。工作计算中原始校准差和根残差仍分开，`radial_Gram_error_identically_zero` 与 `radial_metric_error_identically_zero` 均为 false，`radial_Gram_uses_complete_hprime_Delta` 为 true。准确条件性径向恒等字段另列，不能用它跳过实际 E 行。

直接 raw-lift 公式和把 $\delta_{\rm ref}-E$ 代入的差分公式只在准确线性归约下恒等；不同括号归约的浮点费用仍沿 R715 明示。源码选择直接完整 current raw-lift 工作公式，不宣称两种机器表达逐位相同。

## 7. 完整几何、QP 和失败读取

新 geometry 仅独立更改构造守卫和来源/校准绑定；原 24 个扫描、幅度、地点、行组装及 pullback 方法 AST 相同。原完整 e783 选择器、原 192 prefix、双见证符号、真实 reach product、全部永久地点以及全部自由 core 的 witness 导数保持。

driver 原 11 个顶层函数 AST 相同；只有 main 增加新完整源加载、构造参数及报告字段。自嵌套 `def save_report()` 到 EOF 的完整字节后缀与原 fd95 相同，SHA256 为 `9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee`。这包括真正 initial/full read、失败报告、完整 Phase I、QP、所有实际 line trials、地址积累、实际接受和最终读取。没有用本次中心化说明替代原科学循环。

新的 current-point snapshot 保留原 34 个 normal 字段，并加 `current_reference_calibration`。新增记录包含冻结参考点摘要、当前完整点摘要、raw 和 centered 各三阶最大范数、完整 lift 和非单位工作径向范围。原初根、provider、field 或 geometry 失败时，尚未读到的值保留 null；reader不从 latest 或其他点回填。

pure reader分别核完整模型、source roles、固定准确标量、原初点、seed、字面 Q、normal 分割、当前点 snapshot 和 helper metadata。它检查参考批文件/数组身份及记录之间的一致性，不重算数组或把这些来源核当准确积分证书。数值根失败仍只是当前完整数值输入和算法的失败，不推出整个控制族或本课题不存在。

pure step 的准入 parent 仍是已存在的原 `reference.npz`，不是尚未返回的 `final.npz`；因此真实 initial failure 也能被完整读取。`--verify-final-bundle` 只在实际报告 `complete=true` 时核返回 final 文件，其余失败语义由原 reader 主体保留。

## 8. 十份实际历史与两步准入

两步 ready 保留原顺序的十份完整输入：

1. `axisymmetric-R690-reference-v2-first/locations.json`；
2. `axisymmetric-so3-complete-v2-first/report.json`；
3. `axisymmetric-so3-prior-separation-SOC-first/report.json`；
4. `angular-unit-complete-first/report.json`；
5. `axisymmetric-so3-integral-norm-first/report.json`；
6. `axisymmetric-so3-integral-norm-second/report.json`；
7. `zero-closure-added-gamma-KKT-explicit-H-first/report.json`；
8. `zero-closure-fixed-normal-lift-first/report.json`；
9. `zero-closure-fixed-normal-lift-explicit-H-first/report.json`；
10. `supported-unit-fixed-normal-lift-first/report.json`。

第十份是实际在跑的五段 supported seed 场。未返回不等于没有地点责任，准入前须有其实际完整报告。未运行的 plain R711 场没有新增历史地点，不增加虚构依赖，也无需为本入口另跑该场。若 direct SOC 或其他同目标分支实际先执行，root按真实顺序把该报告追加；不能在本文件提前填未知身份。

新的输出目录是 `{work}/reference-centred-smooth-triangle-normal-lift-first`，纯读取输出是 `{work}/postprocess/reference-centred-smooth-triangle-normal-lift-first-readout.json`。仅清理该目录的 `rows-*` 临时矩阵缓存；保留完整 reference/calibration raw 缓存供同场诊断，不让 controller 展开巨大的全参考缓存 cleanup 文件清单。

全部 summary selector 都是原报告已有的标量叶子或新增 raw/centered 范数标量，缺失保持 null。未知实际模型、候选、first/geometry 和准确费用仍为空，不以源码完成冒运行成功。

## 9. 完整源码再生与实际静态核查

已实际执行的本地工作仅为文本派生、stdlib AST/compile、重复键和尾空白检查、源码摘要和 argv 解析，不导入科学模块，不运行 F/J、根、积分或数值 fixture。

27 角色完整 driver source pins 已逐文件字节核对；本次新六源与原已刊依赖相符。两份 parse 函数的 AST 在纯 stdlib namespace 中分别接受同一条完整 ready argv，共 150 个 argv 字、10 个 manifest、32 个 normal stages；driver/launcher参数差仅原有 `install-torch/print-command` 两个 wrapper flag。所有 scientific 参数与原 ready除输出目录外逐字相同。

在已刊同一 scripts 目录拥有 helper 和两个再生器后，可在仓库外暂存目录运行：

```bash
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/derive_reference_centred_smooth_triangle_entry.py \
  --repo /absolute/path/to/repository \
  --out-dir /absolute/path/outside-repository/r715-regenerated
```

它严格读取并核对完整原 66e/ef46/fd95/8dc8/3914 五源、完整 helper、完整 normal 再生器和原 ready `7d967cdb…`，生成全部六源、新两步 ready及完整源身份表。component-directory默认本再生器所在目录；科学模块不被 import。新 helper 是完整独立源输入，不靠调用者缺失片段拼出。纯派生再生器本身不运行任何科学断言或追加完成门。

## 10. 后继费用与本次结果边界

已有 R713 费用 consumer 只绑定原 R711 driver/reader；不能把本次新报告改标签喂入旧 consumer。后续若有值得认证的实际候选，需要独立完整派生严格绑定本次 source/model 的 fee adapter，并将准确 mean、实际 profile lambda/d/w、outer node/cumsum、core inverse、normal 根和校准 lift 的全部费用支付到同场六 jet。当前源码不把这些未付费用设为零。

原参考准确闭合、全角分支、角向对称和接缝的数学条件继续保留。R715 的 lift在准确误差为零时恢复原结构；实际 core/cap/quarter 数值误差、全部 physical-t、E3/held、embedding/reach、原固定问题的径向/角向/求值精化以及有意义的 solver floor仍是该题的实际责任。完整 source 准备完成没有替代任何一个实际科学返回。

construction 的 R714 C1缓存作为另一个独立后继源码包接入。当前这六源未使用该缓存，不预填其命中数、速度或科学改善。后继缓存必须保全部 stage 与全部上游一次参数导数，并完整更新 schema/helper/driver/reader 来源闭包。

根另全文核过两完整纯文本再生器、新 helper 与 normal 差异、全部 driver/geometry/reader/launcher 派生改动及全参数；实际仅在临时目录做纯文本再生，六完整执行源与 ready 逐字等于上述交付，27 角色文件 SHA 全同。没有导入科学模块或执行 F/J、根、积分。再生输出表保留上述摘要，未转存生成数据。
