# Run10：同一实际完整场的闭面多时刻网格与真实离散精化输入

## 1. 交付范围与实际状态

本次给出四份完整运行源码、三份完整源码再生器，以及两个各含科学计算和纯读取的完整参数方案。它们重建 run10 的原完整算子 $q$，选择一个真实完整自由点，在该点上生成整个闭面的多个物理时刻网格。整个流程不调用外层优化器，不截掉自由变量、normal stages 或原物理提升项。

此时没有执行本入口，没有实际网格、精化差值或预览结果。源码身份和参数不是计算结果。live scalar progress 即使带有非初始 point SHA，也没有给出那一点的全部控制词和可重复的场值，不能作为点输入。本文件没有给未来 report、final、snapshot 或输出填写 SHA。

本入口 complete 仅表示所声明的工作场、有限网格和离散时间读数确实计算并完整保存。它不把有限样本升级成连续 $C^2$、嵌入、reach、$\delta_{\rm hold}$、$\delta_E$ 或等距误差证书。normal/root/六jet、Gram/曲率/支撑、闭面装配与 R716 的准确费用继续承担各自原有责任；不能由 mesh complete 跳过。

本次“同一问题”只在 run10 内部、同一个完整 target 和当前点上成立。固定 chart 的字与某个旧 run 相同，不让本入口继承旧 run 的目标身份、选支、末点或证书。

## 2. 完整实际来源与两种合法点输入

| 对象 | 完整 SHA256 |
|---|---|
| 原完整 driver c3dc，75 个 source roles | `c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1` |
| 原完整 pure reader 2efa | `2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e` |
| 原 launcher 22069 | `22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604` |
| 完整 normal、raw lift 与闭合复用 6d2 | `6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4` |
| 完整 meridian base 6a803 | `6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865` |
| 当前实际 reference model | `081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5` |
| 当前独立固定 target | `e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049` |
| 实际完整 input-binding 文件，430908 B | `4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf` |
| 原固定 chart 全字 | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` |

实际六文件和公开来源由既有完整 run10 binding 再读；原 report 与 launcher command 的 source commit、GitHub run id、workflow trigger 必须一致，原 run id 是 `45972294636`。实际输入返回见 [run10 小分卷](2026-11-27-public-actions-45972294636-1-part-001.md)。不复制这些大 raw 本体到 Git。

当前表示保持 $M=160$、$J=923$、原工作 $N=2048$ 和全部 32 个固定 normal stages。当前 core 的全部原自由系数、三组旋转场的全部自由共享 quintic jets、自由高度 $H$ 都从实际完整点取得，不能用 frozen base.initial() 替代。

两种点来源严格分开：

1. **真实 final。** 原 report 必须 complete；读取它自己声明的 final_bundle，完整 SHA 相等。完整十三个 NPZ members 必须齐；保存的 model/base/scalar/root policy、mesh、固定原 core、全部 current core/omega/H、积分阶与 full angles 全核。原 `q.load_checkpoint` 返回后，重新解包的 core/omega/H 逐字等原数组，点摘要还必须等原 final_geometry 的 current point。
2. **真实 immutable packet。** 只能从捕获 report 的实际 snapshot 索引选择。不指定某身份时取实际具有完整 required-angle roots 的最后一项；指定时必须唯一存在。完整点数组由原 31f validator 按整文件和 descriptor 核验。cache point 不自动是 accepted outer point，此分支明记没有由 snapshot 推断接受或 final 完成。

两个方案没有 initial fallback，也不消费 live progress 的摘要。缺输入是实际输入失败，保原错误，不称数学场失败。

原 report 连读两次，只有整字节相同才保存新的 immutable copy。以后原 report 可以继续推进；本消费者只读该捕获字节，不拼接后来的数值。完整输入文件 inventory 进入新 binding，完成时及纯读取时再次核整路径/大小/SHA。

## 3. 原 main 中的完整 $q$ 构造

原 driver 没有 build_problem。本次 `_build_complete_original` 保留原 main 从 `preparation, reference_binding = actual_reference(args, paths)` 到完整 `RotationH2Coordinates` 构造的连续 **8919 字节**，SHA：

`612f000bcf42f37c13cecb03f6c380e894176a13a69474c49043c19295ce1d92`。

原 driver 整体 SHA、该连续段以及新 input 中同段在运行时核对。全部 75 roles 先验证；原 reference、seed、mean、meridian、normal、calibration、J3、frame、C1、stage、adjacent、closure、moment binder、geometry、QP、history 和 envelope 模块全部保留。新 main 只另加 input、mesh arithmetic 和三个完整原 entry 文件，合计 80 roles。

实际 launcher command 是完整参数来源；调用原 driver.parse_args 解析全部实际 argv，核 report/outdir/command 对应。ready 还保存已刊原参数的全部 149 个 argv 元素。构造时仅将新 cache/progress 输出目录换到独立 fresh 目录。构造后整 model/canonical、coordinate norm、working evaluation、reference model、target、完整 public input binding 必须等于实际 report。

原 22069 launcher 在启动 Python 前设置 OPENBLAS、OMP、MKL threads 为 1。新 main 在导入 NumPy/SciPy/Torch 前原样设置，同时禁止写 bytecode；input 核这些值。原 Torch threads/interop、积分阶、inverse/core、seed、root policy 和库版本仍按实际 command/report 核对。新的 fixed-chart inverse 参数只取材点，不改变 $q$ 的 core inverse 或 normal budgets。

本次不改原求解器源，不删除物理后缀，不在原 normal/J/J* 中接一个简化 mesh 算子。

## 4. 已记录根、固定 seed 与 calibration 的恢复

同点调用原 `_select_point` 后，要求 root cache 为空且全点摘要相等。每个已存在 packet 先经原完整 validator，恢复全部实际 `Z`、`zero`、32 stage records、eta/frame/controls/J3、实际角阶与矩阵阶；原 adjacent `_root_protection` 在恢复对象上的摘要必须相等。没有算过的二阶 jet 不补作已算零，原来没有的 J6/J9 仍为 None。恢复本身不调用科学。

fixed seed 使用同 seed model 的完整 radial-plan arrays/description、12 个均值候选 jet 与 literal phi words，逐 NPZ/descriptor 核验。重复候选角不任选一份。reference calibration 另核它的 frozen baseline point、Gamma/P/delta/phi 和同 field model，恢复原 cache tuple。当前 H 不拿来重建 fixed seed 或 baseline。

若真实 final 没有同点 snapshot，明确记录未恢复旧根，再按原完整算法评价新角；若有，则恢复真实既有词。新取材角仍需原完整 field/root 真正返回。cache 恢复不支付跨角关联或连续唯一性。

原 packet 保存的完整 integration carrier 若存在，重建后的 mesh、Gauss、grid phi 和 integration query 全数组必须字同。记录缺失则不声称字同，不能从 whole NPZ 摘要猜子数组。

## 5. 当前 2218 叶 scalar 与新的同-target 节点

当前 run10 preparation 的实际 scalar table 是 **2218 叶**。2397 叶只属于旧 carrier 历史再生，不能替换当前场。

input 保留已刊 `complete_dyadic_radial_observations.py` 中 `counted_tail_class` 与 `_restore_actual_scalar` 两个完整函数主体。父全文 SHA 是：

`2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74`。

其准确核仍原 e091；按真实 live-leaf count 复现原 priority/sequence 划分，所有 exact per-leaf operations 不变。结果 metadata 除 elapsed_seconds 外必须与当前 preparation 整体相等，包括实际宽度、全尾域与 requested accuracy 状态。叶数相等不等于误差目标达到。

每个新 $(cell,u)$ 使用原 point_definition 产生准确地址，affine pair 顺序为

$$s=\lambda S+\eta.$$

$u$ 用真实 binary64 字的准确有理值，再组合准确两端节点。$a(s)$ 用原完整 target_a_box 重读包围，保工作中点及误差，不插值旧 observation 列来冒同一 target。

全部 922 个原 cell 及其 dyadic 子分点保留，最后 cap 点保留。即使 rounded global s 字重合也不删 cell。有限差商取原 positive cell width 除显式整数；它不是准确宽度证书。a 的包围宽度尚未加入工作 Gram norm，输出显式保此责任。

## 6. 固定材料 chart 下的真实物理 phase

采用 [R248](../results/R248-finite-C2-phase-family-and-global-reductions.md) 的完整公式

$$
\alpha=\pi t/2,\qquad
\zeta=\Theta_0^{-1}(\Theta_0(\phi)-\alpha),\qquad
F_t(s,\phi)=R_\alpha U(s,\zeta).
$$

$\Theta_0$ 是固定参考 chart，不是当前自由 core chart。不能写成 $U(s,\phi-\alpha)$，也不能只转旧 phi 顶点再沿同编号缝到固定帽。

先用完整原 `q._chart`，对均匀 physical-material $\theta=\Theta_0(\phi)$ full-circle 表取工作 inverse。保全部 phi.hex、正 rho0、迭代数与残差。默认最多 64 次，工作阈值 $2\cdot10^{-12}$；每个实际 field block 再用原同 block chart 核 rho 字及 inverse residual。这不是区间 inverse 证书。

令 $G(s,\theta)=U(s,\Theta_0^{-1}(\theta))$，则

$$G_t(s,\theta)=R_\alpha G(s,\theta-\alpha).$$

当 full angles 为 $n$ 且 $nt/4$ 是整数时，在同一完整 theta 表上按准确整数索引移位，再计算工作旋转矩阵。准确的是有理索引关系；三角函数、inverse 和 working root 没被声称准确。参数不满足索引合同即明确拒绝，不静默插值另一场。

默认导出 $t=0,1/4,1/2,3/4,1$；时间比较用完整 $[0,1]$ 的 4、8、16 段。mesh full angles 为 512、1024、2048；原 $q$.N 始终 2048。粗 mesh 取材数不是求解空间缩小。

finest 在全部 3689 个径向点与全部 2048 个全圈角上一次读完整原 field，角块保持原 8。没有由 quarter symmetry 推 full circle。另在 literal $\phi=2\pi$ 对全部径向点重读六jet，与 phi=0 真实值比较；记录六项 seam 差与 chart residual，不能据小差宣布 continuous branch glue。

转换为固定物理材料坐标的六jet 时：

$$
G_\theta=U_\phi/\rho_0,\qquad
G_{s\theta}=U_{s\phi}/\rho_0,\qquad
G_{\theta\theta}=U_{\phi\phi}/\rho_0^2-\rho_0'U_\phi/\rho_0^3.
$$

F/Fs/Fss 与这三项保存为完整 float64 arrays。全程调用原 6d2 fields_torch(curvature=True)，完整 h/hp/hpp 和实际 raw Delta 保留。unit tangent 不能冒最终 Fs，centered root residual 不能代 raw physical defect。

## 7. 下反射、Cartesian p4 帽与接缝舍入

signed 参数 $u\in[-S,S]$ 的下片为

$$F_t(u,\phi)=J_zR_\alpha U(-u,\zeta),\qquad J_z=\operatorname{diag}(1,1,-1).$$

belt 顶点从 lower cuff 经 core 到 upper cuff，core 只保一圈共享索引。面次序对应 $F_\theta\times F_u$；若下片仍用正 s，则对应 $F_s\times F_\theta$。这只是 candidate orientation，外向由闭面/R650 费用装配证明。

帽不随 t 转动，始终为

$$
z_+=H+f_1+f_2+f_3,\qquad z_-=-H-f_4,\qquad
f_i=\frac1{1000}(1-|(x,y)-c_i|^2/b_i^2)_+^4.
$$

$H$ 是当前实际全点的末字，在每个 t 固定。标记完整采用 [R661](../results/R661-complete-nonplanar-activity-and-four-fixed-markers.md)：

| 帽 | 中心 | 半径 |
|---|---|---|
| upper 1 | $(3/20,0)$ | $1/25$ |
| upper 2 | $(0,3/20)$ | $9/200$ |
| upper 3 | $(-3/20,0)$ | $1/20$ |
| lower 4 | $(0,0)$ | $11/200$ |

源码包含完整图值、gradient 和 Hessian。outer cap rings 直接共享 belt cuff 索引，upper 帽为 +z 绕序，lower 反向。marker 中心与帽坐标都保持 Cartesian，不跟着 active phase 旋转。

原准确源端口给 cuff $(R\cos\theta,R\sin\theta,\pm H)$ 与 core 的 z=0。输出闭 polygonal mesh 时，这些边界采用源公式的工作字，并记录 raw working F 到边界字的实际最大投影差。原六jet files 不改写。这个显式 mesh 舍入既不能隐藏，也不能由强制共享索引倒推 working field 有准确 $C^2$ ports。

程序记录全部已采样 core parity 与 cap 六jet port 差；R 的工作 carrier、chart 和场的准确误差仍未支付。对于上片 R 个 radial rows、N 角、K 个含 0/R 的 cap radii，组合拓扑为

$$
V=(2R-1)N+2\{1+(K-2)N\},\qquad T=2V-4.
$$

逐块核实际写出 counts、indices 和精确 PLY bytes。组合 Euler characteristic=2 不能排除空间自交、退化片或连续嵌入失败。

## 8. 同一 target 的真实空间离散比较

| 层 | 每原 cell 子分数 | 全圈角数 | cap 基础环数 |
|---|---:|---:|---:|
| 0 | 1 | 512 | 16 |
| 1 | 2 | 1024 | 32 |
| 2 | 4 | 2048 | 64 |

所有粗 radial/angular words 都从同一 finest 表选取；没有重算一套近似 chart 冒同节点。帽除基础环外还加全部 marker 中心/支撑径向位置及可用 grip 半径；粗环实际字必须在细环中。全 cell/full-circle 不做预算截断。

相邻两层在全部较细节点，比较真实细读数与完整粗三角片。每矩形用固定对角线两三角片的 $(s,\theta)$ barycentric map。保原 raw working position 差、实际导出 port-rounded position 差、这些节点的实际 projection、原 Fs/Ftheta 对导出粗 PL 导数的差，以及两类有限 relative metric operator norms。

active 的同一 target 是 $\operatorname{diag}(1,a^2)$。记

$$
E=\begin{pmatrix}
|F_s|^2-1&F_s\cdot F_\theta/a\\
F_s\cdot F_\theta/a&|F_\theta|^2/a^2-1
\end{pmatrix};
\quad
\|E\|_2=\frac{|\operatorname{tr}E|+\sqrt{(E_{11}-E_{22})^2+4E_{12}^2}}2.
$$

程序确实算实对称 $2\times2$ 谱范数，不把三分量 max 换名 operator norm。a 来自同一准确 scalar 新地址的工作中点；其包围误差未加入这项工作读数。

两 marked caps 逐实际三角片在 Cartesian centroid 比较 PL graph metric 与完整 p4 graph metric，用 $g^{-1/2}(g_h-g)g^{-1/2}$ 的谱范数。若有退化片，全帽最大字段为 None，另记仅非退化片的最大值，不删坏片后称全帽通过。全部细 cap nodes 还比较完整中心 fan 与其他粗片的实际 position 差。

这些是明确的有限读数，不是网格间处处上界，也不是一串非线性求解已经收敛的证据。working field、准确 target、polygonal interpolation 和序列化责任分别保留。

## 9. t 精化比较的对象与误差意义

对 4→8、8→16，每个细 t 都在整个 finest 上片节点上按真实 R248 phase 求值。下反射保持相同欧氏范数；两固定 Cartesian 帽的时间插值误差为零。

比较的是该 phase 图和相邻粗帧的线性插值。记录每个细 t 的 position、radial derivative、physical-angular derivative 差；raw working position 与 port-rounded position 分开，所有测试 t 的实际 port projection 也单列。

线性插值是另一张映射，未宣称它仍等距。有限细 t 也不是整个 $[0,1]$ 的误差上界。材料点位移不冒无对齐 Hausdorff $\delta_{\rm hold}$，不做刚体拟合来代 $\delta_E$。

原 R248/R650/R716 连续证明不在这里重写。实际闭面/all-phase 装配由完整 `run10_complete_closed_phase_grip_evidence.py`（f7a10d7d…）及准确费用承担。本入口不等待一个 proof metadata=true 才能读场，也不因导出 mesh 替证明填 true。

## 10. 同一真实点的 M320 频率精化输入

同一点另输出原 `q.save` 生成的新同模型完整十三成员检查点，完整 old/current core/omega，以及 $M=160\to320$ 的准确零扩张输入。新序列化文件不能冒原 final whole SHA。

| 旧旋转槽半开区间 | 新起点 |
|---|---:|
| `[0,161)` | 0 |
| `[161,322)` | 321 |
| `[322,482)` | 642 |

原 word 逐字保留，新增系数为 literal positive zero。全部原共享 quintic jets 与 H 保留，reference chart 仍是原 160 参数；不能用 current core 的扩张覆盖 fixed reference。准确有限 Fourier 函数不变，但浮点评价次序、根支、模型、norm、damping 不自动相等。

输出明确 `actual_new_frequency_field_evaluated=False`。它提供完整点/model/target/reference/history/report/snapshot 和所有输入，供后继完整 source-specific 的 run10 频率族核验；不把其他 run 的 refined source 改标签接入。后继须真绑定 e711 target、完整新布局/初值/typed history，再读全场、原及新正行、metric 与 geometry，报告实际同问题差值。这里不据零扩张输入宣称频率收敛要求完成。

## 11. 全部 raw、预览与纯读取

六jet arrays、point/root packets、固定参考、完整读数、科学网格和预览只留 runner。Git 保留完整生成器/参数、实际 run/whole hashes 和紧凑标量；不上传 raw 到 Git、Release 或 artifact。

每个声明 t 导出全部三层 float64 scientific PLY。另每个 t 输出一个独立完整闭面预览：默认 96 个实际 radial rows、128 个全圈角、32 个 cap 基础环，含上下片、共享 core/cuffs 和全部 p4 caps，坐标 float32。写前按格式精确算 bytes，必须严格小于 5000000，再核实际 bytes。预览仅显示完整形状，不冒包含全部原 radial cells 的科学 refinement grid。

六份完整工作数组主体是 $6\cdot3\cdot8RA$ bytes，默认 $R=3689,A=2048$；每科学 PLY 主体是 $24V+13T$ bytes 加实际 header。多层多 t 可占数 GB，不能拆进小 Git 文件。这里是格式体量，不声称当前 runner 磁盘/时限已测得足够，也不改原优化预算。

纯读取器只走 stdlib，核全部 80 source roles、原 report、immutable inventory、完整点与 target、六份 NPY header/shape/dtype/whole bytes、所有 PLY counts/bytes 和 frequency input。它不建 q、不算 F/J/root/chart/mesh，不重算一个数值指标。缺报告真实失败，partial 保 partial，不补零。

新 recorder 仍为原 31f，但 caller 是新 mesh main 与真实 80-role registry，不冒 c3dc。只接受 c3dc/2efa 的旧准确费用 binder 不会自动接受这个新 caller。以后消费 mesh 新 packet 需要完整显式来源适配；不能因公式相同修改旧 guard。

## 12. 完整源码、参数与实际源核验

四个完整运行文件：

| 文件 | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| `run10_same_field_mesh_input.py` | 59302 | `74320688c14852461b195a41ef9093a66f6b7fa8f9e9f73dfa9a6d89d5734aed` | `b5f76a45887807e6fa178bfad9c0d3989748b3b4` |
| `run10_complete_phase_mesh_arithmetic.py` | 39424 | `34c437b2e1e099dc5d675bdf345caf50cbab9b619e0d9bdb7e46fa32d5579c58` | `fcc24aff138c3013b3566f9ed9b06b2ef02d127f` |
| `run10_complete_same_field_phase_meshes.py` | 38603 | `905ee29d2f15b1c2f9d861c37ee1b6e5ad13941f8ba38415492c34d0a9fa85c2` | `d1c5d035d09b2c740f0a57b177ba7b557697a9a1` |
| `read_run10_same_field_phase_mesh_report.py` | 18184 | `680600ddb54c2fd8dbe861de16ec46705ec04bec250293e44e5ecbe68223c5ac` | `9a46d62047c15d5040095e431483bebab65c0a97` |

三份 stdlib 再生器包含输出源码的完整 literal bodies，不是补丁骨架。input 再生器另核 8919-byte 原构造段和 scalar 两主体；entry 再生器核完整原 75 roles 与新 80 roles。它们不导入数值模块，不执行科学；它们不是新的科学前门。

| 再生器 | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| `reproduce_run10_same_field_mesh_input.py` | 65560 | `3bccd8ad9bcf64ce0181ee43ca24128c73b5f8ec5119f0ed25e03846bb492a42` | `f8119331f9acfa520831d76454c74c9af9a3cfc9` |
| `reproduce_run10_phase_mesh_arithmetic.py` | 43743 | `a955aeabc0fc4b70017339cb443f40b57f577fd91e4fe16cce96972e7f63898b` | `57757b2fb370091b219ca213d7eccb1f5b73675b` |
| `reproduce_run10_complete_phase_mesh_entry.py` | 63650 | `44d377c84bbb53fc930e36da1f12c73c8ce2e163d89f21ea3418deaeca81622e` | `3431c34b1dd3c3b182e3dc5e2921c7f1632a8daa` |

两个 ready 都保全部原 149 argv、75 source hashes、完整 mesh 参数和真实 scalar selectors。各两 steps：完整科学消费者，随后完整 pure reader。controller parent 用实际 reference bundle，避免一个未来 final 阻止真实错误报告；真正点来源由科学入口严格核。

| 参数文件 | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| `run10-complete-same-field-phase-mesh-final-ready.json` | 36220 | `0cf45a65dee71b08a0a5f53e202aac0382984b6da7193b910023ab642a00a8ae` | `0ef28c52958ed6bf15b7ecb9611ce71a936e13b8` |
| `run10-complete-same-field-phase-mesh-packet-ready.json` | 36367 | `23ef79d18fd9dffcc9d028a869d474abf1a71258216f7d720ceb30481576f136` | `fd6b1c0f9f29092d906f24e8b4dcf12c182c77a0` |

final 与 packet 是两种明确参数选择，不能在同一次调用因 final 缺失偷偷切换。输出分别为 `{work}/run10-same-field-phase-mesh-final-v1` 和 `{work}/run10-same-field-phase-mesh-packet-v1`，必须 fresh。没有写队列或触发执行，future point/output hashes 未填。live progress 只读标量，不调用科学，也不使进度点成为合法输入。

已实际完成完整源码阅读、SHA/字节计数、8919-byte constructor 比较、当前 scalar 两完整主体比较，以及 literal-body 在 JavaScript 中解码后逐字还原四源。函数分隔空行不属于 scalar 主体。几何协作者定点核根恢复、reference calibration、构造与实际点接口，结论只覆盖该范围，没有扩大成全包通过。

当前 executor 不可用；未实际 Python AST/compile，也没有本地 F/J/root、chart、Fraction 数值例或 mesh 实验。首次 public Actions 返回须看完整实际来源、状态和误差。此交付使真实 same-field multi-t mesh 与 refinement 输入可执行，不登记新的存在性、全域误差或速度结论。
