# M15 真联解后升 M16 的条件式接口：全文独立静态审查

2026-11-09，审查者 `/root/tail_theory`。未参与被审接口稿、raw-lift 或 coupled 求解器的实现；先前仅给过 remesh 两半索引的窄只读核对。本次逐节审查条件、公式、命令及原源码路径，没有运行 solver、root、RK、导出器或未来候选 fixture。

**结论：v2 PASS，适用于稿中明确条件下的下一阶准备；没有证明未来 M15/M16 成功。** v1 的可选 raw-lift 命令依赖路径存在一处可复现性缺口，已由作者保留旧稿、另存 v2 修复；数学和主 coupled 命令不变。

## 1. 冻结对象与实际检查

- 被审 v2：`notes/2026-11-09-db6f-prefix-m15-to-next-mode-interface-v2.md`，SHA256 `8e14cd3142f7e09f4721e568299d76be0c5febf2fccd65edce18f470f659c769`。
- v2 来源账本：同 stem `-sources.json`，SHA256 `040c85e07ba4163fa811fa938fdd1660cc91fac04ee7eac92e1cdb9c4c38c9a5`。
- 冻结 v1：`notes/2026-11-09-db6f-prefix-m15-to-next-mode-interface.md`，SHA256 `9d9074821c88cfefab9b4762fddb0168efe0d058c120ce99fdcfffc459d3aa42`；原19源账本 SHA256 `dc7cda84e6d70706d62cb1f5c23e4dce5e1ec57d001c3fc15243203f479d2d67`。
- 独立检查器：`scripts/db6f-tail-review-next-mode-static.py`。实际工具 `exit 0`，报告 `notes/2026-11-09-db6f-tail-review-next-mode-static.json` 的 SHA256 为 `04fa7441fe8a68c4b50c92509ea6bd3ce0173cac85ee4ecfdb62a4aa9bfacbff`。

检查器只用 stdlib 的字节哈希、JSON、AST 和命令文本解析：原19源逐字节大小/SHA全同；v2共29源全部核同；原9个 closing-tail Git-blob SHA1 独立重算全同；另外绑定本次只读到的 fixed-metric/loader 等源。它没有导入数学模块、读取尚不存在的真实 baseline，或制造未来状态、配置、响应。

## 2. 真 baseline 与同 g 条件没有被初猜替代

第2节要求未来 B 是完整 M15/N512 prefix 联解，且采用它自己的 `tail_seam.tail_record`。这正确排除 affine predictor、单独 s=1 尾响应、早期 warm 和 iteration CP。与源逐项核对，原 coupled 会先保存一个 CP，再做 prefix audit 与 seam_audit；异常会被 main 捕获并写 summary。因此 CP 存在、旧 `solver_success` 标志或单独 `exit 0` 都不能代替最终完整闭合门。稿中已经要求 summary/CP/真实退出同时闭合、无 error、最终 actual outer BC、末次真 Jacobian/audit 及源绑定。

原 `curve_stable_prefix_bvp.load_checkpoint` 仅从分片载入并 concatenate，没有重新计算分片声明的 SHA。因此稿中显式要求 bytes/SHA、槽覆盖、mesh 形状另核是必要且正确的。这里只审这些未来门的规定，没有运行一份未来正例。

同 g 的依据是固定 `frozen_profile`、chart、physical port、warp reference、tail 几何/校准输入和 phase 范围，并以 `fixed=True` 构造。`closing_recalibrated_tail` 内部背景创建明确使用 `modes:1`、`quadrature:16` 和独立 `calibrationSteps`；外层 M/N 用于动量 Fourier 系统，不应误改背景校准参数。保留 support 振幅的 BVP 自由参数也不等于改变 g：固定情形的 flow 不随该参数重造度量，参数改变的是原 support 入口形状。

稿中配置是对实际成功 B 的完整 typed copy 后，只改 `modes` 和独立 I/O 路径。其效力以未来实际复制、身份检查与源字节绑定为条件；不能把本次静态 PASS 当成这些尚未发生的检查已完成。

## 3. prefix padding、自由参数与保存网格

`db6f-prefix-preserve-restart.py` 对旧 M=15、新 M=16 的槽搬移为：

| 部分 | 旧槽 | 新槽 |
|---|---|---|
| 平面均值 | 0 | 0 |
| 径向15模 | 1…15 | 1…15 |
| 切向15模 | 16…30 | 17…31 |
| 高度15模 | 31…45 | 33…47 |
| 新增三槽 | 无 | 16、32、48 初始为零 |

这些均乘原 `q0/obj.q`，所以保持相同物理 gauge。不是把旧46个槽连续复制到新49槽开头。原 `PlanarSymmetryPrefix` / fixed SupportBVP 的确具有 $3M+1$ 槽，故新槽数为49。

新参数向量长16。第0项恢复 $\log(q_{\rm actual}/q_{\rm seed})$；低模 correction 按旧、新 `pscale` 比例恢复，第15项为零。原入口修正乘局部立方截断，支撑在首段一半以内，不改末端新模为零这一初猜事实。没有丢掉 support 自由振幅。

保存网格通过旧物理 mesh、inverse chart、固定分段锚及原 `2e-13` 合并规则恢复。这个流程保留原自适应分辨率，但不意味着所有重建浮点坐标或 PPoly 端值逐位相同；稿中没有用这一恢复动作支付几何或解的误差。`--nodes 1601` 不覆盖 `--preserve-restart-mesh` 的真实恢复节点数。

## 4. tail 两半与同 shooting 网格分支

`950f-tail-warm-remesh.mjs` 的实际 copy 为

$$
\widetilde Q_j=Q_j,\quad
\widetilde\Pi_j=\Pi_j\quad(j=1,\ldots,15),\qquad
\widetilde Q_{16}=\widetilde\Pi_{16}=0.
$$

在零基数组中，旧 Pi 的偏移15搬到新偏移16；新增 Q 位15和 Pi 位31。原源码 `to[M+j]=v[oldM+j]` 正是此规则。

冻结源 `cellSegments` 恰有9个 profile；physicalDepth12、parts8 给 $12\cdot9\cdot8=864$ 个 stage，因而865个节点、13个 raw 节点。M 改变不改这些几何分段。原 `subdividePhysical` 中 `rawLeft=k/8`，`rawLeft*oldParts` 为整数，所有旧深度内节点落在 copy 分支，无需 remesh 插值 RK；没有加深尾的 appended-linear 分支。remesher 仍会构造可能插值用的旧 engine，不应把整个 worker 初始化说成无数学计算：worker 另有真实 cut root / linear-port 初始化。

copy 只保持 Q/Pi 坐标。新 Fourier 基底的非线性 momentum root 改变，故它不保证 raw slope、均值或 XYZ 图相同。稿中对此作了正确限定，没有把初猜补零当作 M16 解。

## 5. raw-lift 的物理规范和数值范围

原源给

$$
H_j=r^4Q_j,\qquad
V_j=\frac{\sqrt2\,w L_j}{\sqrt{12}\,r^3},\qquad
S_j=(3j)^2r^3Q_j+\sqrt2\,w L_j
=r^3\bigl((3j)^2Q_j+\sqrt{12}V_j\bigr).
$$

所以在同背景、同节点保留非均值 Q/V 就对应相同 H/S；稿中的 $r^4$、$r^3$、$\sqrt{12}$ 均正确，没有额外多乘 r/w 或物理频率。`initializeFromRaw` 固定非均值 L 后重求均值根，再映回全部 momentum。新增 Pi 可非零，mean slope 可变化，整个 XYZ 图未被保证保持。

raw-lift 的 node0 是 stage0 外侧输出，脚本先按 `cell.portRatio` 把 Pi 换回该 cell 的 engine 规范，转换后再除回；其他节点因选 stage i−1 的输入端而 factor=1。此与 shared-core `cutJets` 的 node0 normalization 相同。

这一转换实际调用旧 `toRaw` 根、新均值根并构造原线性图，可能失败，也有浮点转换误差；须保留它真实报告的 low-height/raw-slope/mean-slope 变化、最小 guard 和退出。稿中准确称它为可选 UNSOLVED 初猜，而不是纯元数据操作、真实 shooting、完整 raw 几何恒等证书或全域正分支证书。

## 6. v1 命令缺口及 v2 最小修复

v1 的 standalone raw-lift 命令仅设置 `VISIBLE_FLEX_SOURCE_ROOT`。但 `closing_tail_sources.mjs` 不读取这个变量，而按 adjacent → `CLOSING_TAIL_CACHE` → 旧绝对 fallback 的顺序选目录，再核九个 Git-blob。静态观察本工作树 adjacent 不存在、外层 cache env 未设，而旧 fallback 当时仍存在；因此不能将 v1 命令称为不依赖旧会话目录的独立重放入口。

作者另存 v2，显式设置同一冻结 repro 目录的 `CLOSING_TAIL_CACHE`，并保留 loader 的 adjacent 优先和九源拒绝门。我们重算九个 repro blob 全同；这没有通过改源码或绕过验证解决路径问题。若未来 adjacent 存在且字节不匹配，原 loader 拒绝是正确行为，不应偷偷退到另一源。

v1/v2差分只有标题说明、该一个环境变量、依赖说明和账本补充。普通 coupled 命令及 affine 命令逐 token 相同；ordinary shared-client 原来就给 worker 设置了该 cache。三条命令都没有在本轮运行。

## 7. 原 coupled 方程、缓存和验收仍保留

主命令全部 flags 在原 parser 中存在。空 `--warmup-scales` 后紧接 `--lagged-tail`，因此没有旧暖启动循环，但 outer 仍立即取真实 DN/J；inner affine 的输出必须再次调用真正 DN，再用原缩放 BC 判定。原 $2\times10^{-9}$、$10^{-8}$、$2\times10^{-11}$、36轮和 floor .05 未改。M16/N512 满足源的严格条件 $N>4M\cdot spacing$，即 $512>192$。

fresh shared-client 的 cache_key/cache_value 为空。后续 audit=True 总绕过 cache，因此最终 seam 是实际新响应。原 `correctInitialBoundary!==false` 给全部16模加入

$$\Delta Q_j=H_j/r_c^4-Q_{0,j}^{\rm initial}$$

的有限线性 warm 修正，然后原 nonlinear solve 判定；不是改目标方程。计划保留该缺省真值，没有继承旧零态 pilot 的 false。

实际普通 shared 八源是 client/worker/core/split、subdivision/remesh、closing weighted/recalibrated。若改用 trial wrapper，实际导入对象和八源必须如实另记。静态29源表不是将来完整执行绑定的替代品；计划已要求届时绑定所有真实输入、源、argv和退出。

## 8. affine 后备仍只定义一个辅助初猜

`LiftedAffineSlope` 对任意 $M>oldM$ 工作：真实旧响应物理高度为 H0，旧 slope 为 S0，旧 Jacobian 前15行构成低模斜率块；新增对角读原 port 的 `linearSlope[15]`。独立只读得到96项及该值 $205.94394394816572$。其单位已是物理 $dS_{16}/dH_{16}$；原 Jacobian 在 cutJets 有限差分后已除 $r_c^4$，不再乘模式或 momentum 因子。

新增交叉块置零只是 surrogate 的定义。返回的其余 Jacobian 行是未用占位，TailMixin 只消费 slope 前 M 行；audit=True 显式拒绝。输出 `actual_nonlinear_tail=False` 与 UNSOLVED 保持，因此不能据辅助 solver_success 当真联解，也不能作为要求真 baseline 的 freeze-refine 输入。

若未来真实零补模 Dirichlet 子问题受阻，用此预测自由 cut 后仍回原 coupled 是逻辑正确的备选；该路径不保证改善收敛或恢复正分支。采用 predictor 作 prefix restart 时，尾初猜仍须 T15 或实际绑定 raw-lift，最终用预测 H 真求 M16 DN。稿中未混淆这两种输入。

## 9. 最终尺寸与作用域

shared-core 的 Jacobian 行顺序为 slope M、second M、两个 mean correction、height M，共 $3M+2$ 行，列为物理 cut H 的 M列。因此 M16 是 $(3\cdot16+2)16=800$ 项；不能把705项 M15门直接套用。原 jets 为14标量加三条长度16向量；source audit为8标量；states865×32，rawStates13×32并按rawNode抽取。源码逐项吻合。

source audit actualMetric、Darboux/fullD、seam FFT/C¹ 指标均不是最终保存 XYZ 全域误差。新阶有限联解成功后，仍须新图导出、公共 C² 接缝、完整连续 metric/曲率及闭图检查；旧 M12/M15数值不能挪用。纯升模也不支付 native RK 或 N 再加密；稿中将这两类真正重求与仅 exporter 插值分开，符合本次同 g 范围。

本审查没有打开或制造未来正例，不赋予任何未来图误差、reach、精确存在或完成证书。唯一已运行的是上述纯读取静态检查器。v2已解决本轮发现的命令路径缺口，暂无其他必须修改项。
