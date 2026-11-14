# 最终 M15 真联解后的尾导出与 $2\cdot10^{-9}$ 验证：只读最小流程

作者：/root/tail_theory，2026-11-09。**状态：交接可执行计划，未对 M15 生成几何 manifest、未新调用 root/flow/导出或转包。** 目前成功的 $s=1/4$ 只是有限尾 warm；它不满足本计划的最终输入门。目标数值 $2\cdot10^{-9}$ 是待验证门，不是已取得结论。prefix 连续区间和 whole 预算的对应计划由 independent_geometry 维护。

## 1. 唯一可进入最终导出的输入

使用最终完整 M15 prefix CP 及它的 tail_seam.tail_record 所指向的**最后真实 audit 响应**。须同时满足原 prefix solver_success、actual_nonlinear_tail、真实 tail converged、原残差容差及文件 hash 绑定。不是初始 padded-cut 响应，不是 affine predictor，不是迭代 recovery，也不是单独 $s=1$ 尾响应。$s=1$ audited DN 成功后仍必须完成原真实 prefix 外层。

最后建议冻结 N512 的真实联解；若先在 N256 完成外层，再对原 N512 方程重新校正，不能只把导出器的角节点改为 512 来称为 N512 求解成功。M15、spacing3、同一 frozen flat17/weighted 背景、cut/cuff、有限 calibration 表和精确 alpha 定义保持；q 是嵌入未知量，其微小求解变化不被偷换成修改物理度量。

完整输入清单还应绑定：源 CP、原 prefix PP、source/worker/core/RK 哈希、原 native parts/steps/depth、原角 N、原 solveTolerance、源 metric/fullD 及真实 seam。样本源 metric 已明显超过 $2\cdot10^{-9}$ 时，不应先花费完整区间后台去期待包装把真实误差消掉；先继续原源方程的频率/求解校正。

## 2. 三类误差必须分开记

| 层 | 本题实际对象 | 合法加密与证据 | 不能替代它的操作 |
|---|---|---|---|
| 源 Galerkin/角求积 | 给定 M、N 的原 nonlinear prefix+tail 方程 | 真联解 M12→M14→M15；N256→N512 必须真校正；保存实际 PP/XYZ metric | 只提高导出角 N，或把未解 affine metric 当作 true joint |
| 原生径向 RK/打靶 | 给定 parts、steps 的所有 stage 与深端边界 | 同 M/N/g 重求一个更细径向 CP，并真实完成外层；比较原残差、切口和源/实际图 | 固定 CP 后把 exporter 的 flow-steps 加大 |
| 实际 XYZ 表示 | 保存的 Fourier/积分 Fr 系数、精确半径增量、实际 collar | 同一 CP 的导出网格/保留 Fourier 阶比较；对每张图直接连续验证 | 把二阶 fullTensor 当 metric，或将源两 jet 当保存多项式的导数 |

现有 exporter 的每次跨内重新积分沿其表示节点进行。因此两档固定 CP 的导出比较同时含表示插值与**局部重采样 RK 路径**变化，不是严格“同一精确源函数的纯插值”实验；但它们仍是两张明确定义的有限图。每档单列 stage 端 Fr/Frr forcing 和分布校正。

当前 M8 native32/64/128 已提供同 $g$ 原生径向对照；最终候选若还需排除新的径向限制，最直接的一档是保持 M15/N512/p8/depth12，steps32→64 后重新真联解。不要同时升 M、N、parts、steps 再把改善只归于某一个轴。已有充分验证后不机械重复所有旧格点。

## 3. 可直接复用的明确表示

冻结基线是 scripts/db6f-tail-critical-increment-export.mjs，SHA
89307bf2ca1b191c9a6850227d597325ec3c1923e2b8067a20bea58991f82175。
它从 CP 读取 M，检查 spacing/source 参数和 rawNode[D] 与细分 stage 数一致。没有 M12 专属数组维数；最终 M15 的 staged CP 可按同一格式消费。

先保留已有审过的表示：

- height 普通余弦频率 $0,3,\ldots,45$；
- planar 为 $m\equiv1\pmod3$ 的 signed modes，初档 $|m|\le192$；
- 每个物理跨上的 $F_r$ 为匹配两端 $F_r,F_{rr}$ 及物理中点 $F_r$ 的四次多项式；$F$ 由其精确积分定义，是分段五次、共享两 jet 的 $C^2$ 图；
- 一段的长度来自独立局部径向积分保存的正二进增量 $\ell_i$，再用精确有理 $\beta=(r_{\rm out}-r_{\rm in})/\sum\ell_i$ 归一。真正半径是精确增量和，不能回到两个相近 display r 相减；
- 背景是已经认证的同一解析旋转背景；mean 扰动从内端零 gauge 精确逐跨累加，display 的背景高度不是度量导数的定义。

M15/degree192 时 $C=128+16=144$，stride=$3+4C=579$。现有每片最多 1000 行的原始 f64 大小约 4.632 MB，仍在单文件 5 MB 限制内；最终依旧检查实际压缩字节并保存 gzip/hash。不能为更高 Fourier 阶继续盲用 1000 行分片。

### 3.1 角 N 与 Fourier 阶的耦合

原 exporter 的 angular-nodes 同时传给 moment/RK engine 和 Fourier 提取。它不是仅用于显示的采样参数。固定 CP 直接 N512→1024 会改变局部 root 方程及重新积分，不能叫纯 XYZ 角插值。

若只需检查平面保留阶，可在**固定 N512、固定 CP 和同径向计划**下比较 degree192→252；两者都满足 $N\ge2K+4$。后一档有 184 系数/stride739，1000 行原始体积约 5.912 MB，需要另审过的分片行数选择（例如最多 750 行），不能等最后写盘超过限制才认作成功。degree384/N1024 更不是当前最小默认方案。

common-cut-v2 会自动取完整柱模并检查无遗漏。degree192 对应柱模数至少 64；degree252 至少 84。不能将保留更高 planar mode 的尾接到旧的固定 64 模 common-cut 图。

## 4. 必须补入的 raw0/segment7 恢复起点

原 89307 exporter 只有内部 integrationBreakpoints 的 critical 层，**尚未包含后来发现的端点恢复层**。所以最终流程需要一个另存的新 exporter：只在网格提案部分加入已试过的 endpoint 规则，保留其它表示/积分/审计公式，先独审其小差分、计划及实际新数据不变量。不能宣称这个新完整版本已经实现或独审。

已有数值定位如下，详见 tail-restoration-endpoint-layer 与 boundary-height-grid-m12-fine：

| 坐标 | 已定位位置 |
|---|---:|
| 物理恢复起点半径 | 约 $.5277876988744847$ |
| 旧最坏物理点 | 约 $.5277881139390467$ |
| 原 raw profile 坐标 | 约 $.005821671659$ |
| rawCell/rawSegment | 0 / 7 |
| M12 p4 的 stage | 7，raw profile 区间 $[0,1/4]$ |
| M15 p8 的对应 stage | 15，raw profile 区间 $[0,1/8]$ |

实现应按 rawCell=0、rawSegment=7、rawLeft=0 识别，不能硬编码旧 stage7 或用近似物理半径当解析断点。

保留 0、1、均匀节点、全部原源分段点和已有内部 critical 节点。对该起点，沿当前 stage 坐标从 $|\kappa_r|<.5$ 的端点向内找首次达到背景绝对经向曲率 3 的尺度 $\lambda$，加入

$$
x_k=\lambda\,\operatorname{expm1}(k\rho),\qquad 0<x_k<1.
$$

这是**只决定节点的启发式提案**，不是区间证明。冻结背景在旧 p4 stage 中给 $\lambda\simeq.0403566090759$；同一个物理尺度在 p8 stage 中约为 $.0807132181518$。最终应从同源 profile 重算并记录，不把这些近似数当定义常数。

旧单 stage 试验中，端点 $\rho=.025$、.0125 分别使高度二阶样本差降到 $3.74\cdot10^{-8}$、$7.12\cdot10^{-9}$，一阶差已在数 $10^{-15}$。这些是 M12、单角度、固定 CP 的诊断，不能给新 M15 整图直接贴同一数值。

### 4.1 最小初始网格建议

对预期的 M15 p8/steps32，使用 export depth8、内段基本 steps32（每 raw profile 合计 256 个普通跨，和 M12 p4/64 同量级）。raw0 先用基本 steps64、内部 critical ratio .05，恢复端点 ratio .025。只有实际表示/区间失败盒需要更细时，再把 raw0 基本步数提高到128、内部 ratio .025、恢复 endpoint ratio .0125；内段保持原档。

显式保存 flow-steps，不让它由脚本默认值漂移。初档可保持 native steps32 的最大步长约束；新增表示节点仍会令实际某些积分步更短，报告必须如实记录。单 stage 旧诊断的 flow-steps256 是另一实验强度，不能默认为最终 exporter 已经用了它。

一阶误差在极短物理跨上会以 $\varepsilon_1/\ell$ 放大到二阶。源平面 $rr$ 仍由有限差分给出：先保留已比较的差分步长 $5\cdot10^{-5}$，不要盲目变小；跨含绝对值的 critical 点不享有光滑情形的统一四阶误差。该问题可由最终保存系数的曲率证书直接把关，不能把 fullTensor 降到机器精度设为本题新的完成门。

## 5. 每张新图的基本核查与实际 R6

每次完整导出后首先核：finished、输入 CP 和所有 source hash、每片 hash/尺寸/有限性、分片共享行逐字节相同、所有精确增量为正、$\beta\sum\ell_i=r_{\rm out}-r_{\rm in}$、内外锚和完整 C3 模式。这些是新数据不变量，旧 M12 的通过不能代替。

实际图的 R6 必须使用本次 exporter 自带的 -collar.json，或直接由本 manifest 内端保存的值/一/二阶系数定义。原 db6f-tail-collar-exact-check.py 可对该端迹包作精确 Fraction 账本；stream 后台也直接包含该同图 collar。另行从 CP 重新提取、带不同 Fourier 截断的 source collar packet 不能不核系数就替代实际导出图的 collar。

depth8 是初始选择。已有同 $g$ N8 极小缺陷说明其有前景，不证明 M15 的新端迹。若实际 R6 超过工作预算，再用同 CP 的更深端口（如10）生成图并重做新图证书；这只改变数值表示/截断，不改固定无限背景。不能据更深闭合缺陷变小来遮盖外区实际 metric 的源误差。

新图随后调用已审 db6f-tail-first-bounds-stream.py，批大小128；它完整覆盖有限跨及自己的 collar，给 $V_h,V_z$、水平 Jacobian 和横截面简单性。此处只是尾块嵌入性，与 prefix/cap 的全局分离、直径、三阶矩仍必须由新闭预算处理。

若要作两档同 CP 的实际 $C^2$ 比较，复用 db6f-prefix-tail-c2-stream-v2.py 并明确 batch；其 Fraction 公共物理分割和 signed mode 补零已审。范围只是共同外区扰动，不能把比较结果自动扩成两 collar、闭图高度 gauge 或无限 Cauchy 定理。

## 6. 同 $g$ 背景可复用，实际图的 metric/κ 不可复用

最短路径是从旧 M8 的**源背景包**直接转到新 manifest，避免再构造全部 primitive：

| 用途 | 旧 M8 包 |
|---|---|
| 保留适当 $w_r$ 紧度、为新图求曲率 | audit-tail-tight-final-packet.json，原5237盒 |
| 更紧 $w$、为新图求低 metric | audit-tail-lowmetric-final-packet.json，原6211盒 |

二者都绑定 tail-int2-flat17-m8-q10-n8-s32-manifest.json（SHA da0795deed1303dac7a38b68ea168ffd2883d8a84559df77c10ed3e91498e1da）。转移的是固定背景函数在物理 $r$ 上的**值包**，不是旧 V 或旧曲率；因此可以换 M、网格和实际 CP，但必须保留同一目标背景定义。

六个源绑定是 checkpoint、calibrations、alpha、cell_zero_A、inner_A、outer_B，全部须重新核文件 hash。这里 checkpoint 是建立已审背景定义的旧 M8 源参数记录，其 hash 应原样保留；不能为了“看起来是 M15”而改写为新求解 CP。新实际 map 另由 finite_tail_manifest_sha256 绑定。

转移按 exact-sum 半径、Fraction 交区间及非二进边界薄片 hull；未知物理字段仍拒绝，不能用 display r 查询代替。独立全36 profile primitive、紧 alpha 和旧包解析包含性已有审查，可直接作为同 $g$ 的证明输入；新转包的数据完整分区、文件hash和端点仍须实际复核。

### 6.1 已确认的 metadata 兼容性缺口

原 db6f-root-transfer-background.py 尚不识别新 M15 记录里的四键：iterationCheckpointFile、sharedEngines、trialDiagnosticFile、trialStatePrefix。它们只影响 I/O 或 engine 分配，已分别审过，但不能悄悄绕过 fail-closed 参数门。

拟另存显式新 transfer 入口，增加这四键及类型门，记录真实新 script/base/policy hash，并重新核全部六个背景文件。新增未知键即使值为 null 也不能因字典 get 默认 None 而漏过。

冻结 closed-budget-v2 还会重新导入旧 NUMERICAL_KEYS 并检查旧 transfer 源 SHA。因此需要一份**配套独审的新 closed-budget 身份适配**；不能仅在新转包报告中伪留旧 script SHA。root 已授权这对小适配：tail_theory 负责新 transfer，independent_geometry 负责新 budget consumer；数学转包与几何预算公式保持不变。当前未运行真正转包，quarter CP 只可用于可读参数门检查，不得制造伪几何 manifest。

## 7. 实际连续尾 metric 与曲率的最小运行顺序

先为同一个新 manifest 转两份背景包。用已审 db6f-audit-tail-stream.py 加曲率包计算**新图自己的**完整 actual $\kappa$，包括 collar；不能沿用 M12 的 8.462559。旧 proof $K_{\rm bg}\le6$ 可继续用，旧实际 V 曲率不可。

再用 db6f-audit-tail-metric-only.py 加低 metric 包，求新图全域 metric。该脚本不求曲率，报告必须继续明确 curvature_evaluated=false；其界只能和**同一新 manifest 自己的**独立曲率证书合成。

先沿用 radial1 和已审默认 Fourier/Bernstein 方法，查看实际逐行最坏盒。包装未过 $2\cdot10^{-9}$ 时，要区分：

- 源或保存图的实际 metric 本身超过门限：回源问题，不修改背景包去遮盖；
- 背景 $w$ 包太宽：看实际新图 $Z_r,Z_\theta$ 的敏感度，仅修必要盒；
- 径向/角区间扩展太松：细分验证盒，不改变实际图；
- 节点/角保留不足：形成另一张新 map，再重新绑定全部证书。

旧 M12 中 raw2/raw3 修包后的实际区间值已足够小，raw4 某选区边缘仍可给约 $1.13\cdot10^{-9}$ 的保守界。这是潜在预算占用，不是新 M15 的误差下界。到 $2\cdot10^{-9}$ 门时可能只需 raw4 或少量 raw0 的局部背景精化；不要预先重跑整个 primitive 或要求每个 $w_r$ 工作余项都很小。

新完整输出用 db6f-audit-complete-metric-report.py 检查每行与 exact partition、同一 manifest、metric 与 κ 包共同的六源身份，并由未参与计算者独立重跑原后台。metadata checker 不能代替这次真正的区间重算。

## 8. 接到完整闭图的最后门

需要新 prefix 的 exact bridge root/metric transfer，以及与新 tail 完整共享 cut 两 jet 的 common-cut-v2 图；再重做该图的 geometry、metric、moment 和 closed budget。共同 cut 的柱模由实际尾模式自动扩展。旧 root-common-cut 或旧 prefix 证书绑定旧 manifest，不能移植其数值。

固定帽/相位作用、R10 全法向管、R16 矩非全等及 R17 结构公式是可复用的证明；新 map 的 support、$D$、held、非零矩与曲率等数值假设都必须重新付。全时性由同一解析旋转/材料相位作用给出，前提是新系数严格保持规定对称与 collar 端迹；不靠只检查几个 t 的网格。

用新 whole-metric-reach 汇总同图的 prefix/caps/tail 证书，然后**另行明确检查**其全局 metric 上界是否不超过 $1/500000000$。仅脚本原 $10^{-6}$ 检查通过不是 $2\cdot10^{-9}$ 结论。最终同 $g$ 收敛记录应把 M8/M12 真正实际下降、最终 M15 与必要原生 RK/表示加密并列，不隐去 M14 的非单调失败。

最后从同一冻结闭图重建若干 t 网格，核闭有向流形/PL 嵌入/固定帽及文件大小；同一套新冻结输入与脚本交给未参与计算者端到端重跑。数值近似与严格无限非线性尾存在的差距仍明确报告。本计划本身不支付 README G5 或最终完成。
