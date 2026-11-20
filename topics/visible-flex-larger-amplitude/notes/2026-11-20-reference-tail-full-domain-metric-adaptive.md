# R674 连续 relative Gram 的全原域自适应调度

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

**状态：已有严格逐胞核的完整调度源码；没有新的科学执行，没有全域度量通过声明。**
本条只增加逐胞调度、同场结果消费、检查点与瓶颈汇总。
原 [R657](../results/R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md) 与
[R674](../results/R674-reference-tail-continuous-profile-and-same-angle-remainders.md) 的数学核保持原字节。

## 1. 已有能力与真正新增部分

实际核读后确认：`exact_reference_tail_relative_gram_interval.py` 的 CLI 已支持 `--cells all`。
不应把已有能力说成缺少全域调用。
它目前按一个固定 Q/r/n 配置依次计算所选原胞，提供完整的单胞连续上界和真实误差下界。
新入口解决的是多层自适应、逐胞持久记录、已付结果复用，以及实际超标和包围尚宽的分流。

新源为
`scripts/resume_20261120/exact_reference_tail_metric_adaptive.py`，
SHA256：

`5d04728c4fe4059948e07feb63d1281846bde37300dc57ac34589466d2172759`。

它只调用以下已刊源的 `make_reader(...)` 与 `reader.certify(cell)`：

| 层 | 源 | SHA256 |
|---|---|---|
| 完整单胞 tight Gram | `exact_reference_tail_relative_gram_interval.py` | `fd4cd58045e16a969c8c1be48468ab4c1a7be929ef9b95e2a9a24ca546176b2d` |
| 新 reference-tail 连续 profile | `exact_reference_tail_interval.py` | `f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225` |
| 原 R657 分子与完整角覆盖 | `fullclosed_relative_gram_interval.py` | `5bbf821f45fec3a8ecd29ebd64dce8058bb302f7d53416b50158cca743065a13` |

没有新的标量缓存、没有替换 f122 first 源、没有删去 Fourier 高模、没有改变 q/core/H 或目标 g，也没有导入旧候选的数值证书。
每层都按原 factory 构造相应 reader；初始化成本实际记载，不能称零成本。
本地仅完成语法编译和源码接口阅读，没有运行入口、读取新科学场或制造 fixture。

## 2. 每次返回付出的准确域

对于当前实际 $J$ 个准确节点，原胞为 $C_i=[s_i,s_{i+1}]$，$i=0,\ldots,J-2$。
当前 J=923 时就是全部922胞；R676 精化后使用实际新 J，不硬编码922。

一个 `certify(i)` 返回覆盖 $C_i$ 的所有真实物理 pieces：原标量分段、eta 两端和 chi 断点按 frozen 核分开，所有准确符号端点仍为 $\alpha S+\beta$。
所选径向细分数应用于这些完整 pieces，不把一组点值冒成整胞。
角向保持当前 q/core 的全部有限模式、完整解析 lift 和严格闭角余项。
原节点/中点 a 锚或新 a/I 锚的实际误差、真实目标 a 的费用及物理 f/z 标量费用，全部仍由 fd4 原核支付。

外层不把某一个最坏 piece 的通过扩展成该胞通过，更不从所选胞扩展成全域。
它接受的最小科学单元始终是一份已经返回的完整原胞记录。
每个记录还要求当前实际 a、rho 的正性已付，否则该调用是未付，不产生一个可用的数值0。

## 3. `actual_supremum_lower` 的证据语义

真实相对 Gram 矩阵写为

$$G_{\rm rel}(s,\phi)=\begin{pmatrix}e&m\\m&g\end{pmatrix}.$$

对实对称二阶矩阵，准确有

$$\|G_{\rm rel}\|_{\rm op}
=\frac{|e+g|+\sqrt{(e-g)^2+4m^2}}2.\tag{1}$$

fd4 的 upper 路线先付整段 Bernstein 凸包和闭角覆盖，再用式(1)的向外区间上端。
其 lower 路线与此不同：在准确径向子片端点和准确 Fourier 角点，直接取分子 jet 的0阶值，重新应用 `actual_entries`。
真实目标 a 误差和新物理标量误差仍然保留，然后用式(1)的区间下端。
因此对该点 $x$，计算所得 $l_x$ 满足

$$l_x\le\|G_{\rm rel}(x)\|_{\rm op}
\le\sup_{C_i\times S^1}\|G_{\rm rel}\|_{\rm op}.$$

对这些准确点的严格下界取最大，仍是整胞真实 supremum 的下界。
这不是平均误差，不是某个上界公式的区间下端，也不依赖普通浮点采样作为证明。
因此当该下界严格超过 $10^{-6}$ 时，**这一个准确候选**的该胞真实超标；继续收紧它的证书不能修复场本身。
这不证明同一模型无解，不阻止求解器改变自由系数后产生新候选。

外层不直接使用 fd4 内以 binary64 `1e-6` 比较生成的布尔值，而将已返回端点视为准确 binary 有理数，与准确 $1/1000000$ 比较，避免阈值边缘的舍入混淆。

## 4. 单胞多次覆盖和全域合成

记第 j 次完整覆盖给

$$L_{i,j}\le E_i:=\sup_{C_i\times S^1}\|G_{\rm rel}\|_{\rm op}\le U_{i,j}.$$

不论不同覆盖采用何种 Q、径向细分、Taylor degree 或 oracle panels，输入为同一场时都可以取

$$L_i=\max_jL_{i,j},\qquad U_i=\min_jU_{i,j}.$$

上下界可以来自不同的完整调用；它们各自的原始报告 SHA、配置和见证位置分别保留。
不假设增加分辨率后浮点区间上界单调，实际仅取已经证明的有效界。
若出现互相矛盾的已返回界 $L_i>U_i$，该胞保留为 `inconsistent_returned_bounds`，不会继续宣称目标已付。

只有每一个原胞都有有效完整上界，才定义

$$U_{\rm all}=\max_{0\le i<J-1}U_i.$$

缺任何一胞时 `complete_relative_gram_operator_upper=null`、`complete_scope=false`。
可以继续报告已经覆盖部分的最大上界与严格下界，但不能补零、不能漏掉失败或未返回的胞。
局部真实下界超过阈值本身足以否定当前候选的全域目标；这类否定证据不需要其余胞返回，但也不会被写成“完整全域覆盖”。

## 5. 自适应顺序

第一层对所有尚无完整返回的原胞做 coarse cover，包括之前已有某个局部真实超标点的情形。
已经通过显式 `--seed-report` 提供且身份完全匹配的已付整胞不重复计算。
之后逐胞分为：

| 状态 | 准确条件 | 调度行为 |
|---|---|---|
| `requested_bound_paid` | $U_i\le\varepsilon$ | 本目标无需再算该胞 |
| `current_candidate_proved_above_target` | $L_i>\varepsilon$ | 保留实际瓶颈，不浪费证书精化预算 |
| `enclosure_unresolved` | $L_i\le\varepsilon<U_i$ | 进入下一声明层 |
| `unpaid_no_return` | 无有效完整返回 | 保留缺口；后续配置可再尝试 |
| `inconsistent_returned_bounds` | 已返回界冲突 | 保留问题，不给证明标签 |

外层不自动重复同一胞、同一 Q/r/n/panels 配置的 failed/unreturned 调用。
下次显式请求可以提供新的配置；更粗且参数逐项不高于某次已付配置的调用也跳过。这只是调度选择，不是声称其上界一定更差。
如果所有候选配置用完仍未付，结果如实保留，不强迫生成通过标签。

默认 `--levels auto` 取最小满足 $Q_0\ge2048$ 且 $Q_0\ge9M$ 的二次幂，然后执行

| 层 | Q | 每 joint piece 径向份数 | 标量 degree |
|---|---:|---:|---:|
| 0 | $Q_0$ | 1 | 5 |
| 1 | $2Q_0$ | 2 | 5 |
| 2 | $4Q_0$ | 4 | 6 |
| 3 | $8Q_0$ | 8 | 7 |
| 4 | $16Q_0$ | 16 | 8 |

每层 panels 默认128。以 M=160 为例，Q 从2048开始；表内只是 **尚未执行的默认计划**，不预言这些层能达标或能在某个时长内结束。
每个实例仍由 frozen 核检查实际有限带宽折扣为正。自动 Q 规则与该折扣相容：$m=4M$，其理论折扣 $1-m^2\pi^2/(2Q^2)$ 在 $Q\ge9M$ 时为正。

degree 会增加，是因为旧 R657 某些段的 Taylor 锚余项按完整 piece 形成；仅对同一 A 的 Bernstein 多项式进一步径向限制不会自动减小原余项。
新 tail 则按 fd4 的实际子片重新形成共同 jet。两条路径继续使用各自已证明的费用规则。

## 6. 检查点、已返报告和未返回状态

主报告记录完整输入路径/SHA、canonical model、J/M、原核 SHA、精确目标与全部配置。
每个调用开始前先写 `running` 和拟写 raw 路径；实际返回后，将完整 cell row 单独原子写入 runner 工作目录，再登记实际 SHA、耗时和返回状态。
主报告只保存摘要、诊断及 raw 引用。

`--seed-report` 可重复提供已有 fd4 报告，只消费其已经实际返回的 `records/covered_cells`，即使其整体仍是 partial。必须同 actual bundle/node/scalar/model，source 必须是原 fd4；旧候选不能移用。

`--resume` 消费本入口同源、同准确场的旧检查点。每个已返回 raw 文件都按实际 SHA 重新读入，重新形成 min/max 汇总，不信任旧摘要里的通过标签。
原来仍为 `running` 的 setup/cell 记为 `unreturned`，不猜测结果、不填0，也不假设耗时为0。此前其它胞或同胞旧层已经实际付出的有效界保留。
因此一个后续未返层并不会抹掉先前完整覆盖；反过来也不能给此前未覆盖的胞补上一份证明。

可选预算仅用于停止接纳新的 reader/cell 调用：当前已启动调用等待自然返回，然后写检查点。
它不发送 SIGINT，不留下后台科学进程；若 Actions 硬上限截断，最后的 `running` 记录如实留下未返回责任。
作业边界不是课题完成，下一次请求继续消费同场 raw 或从新实际候选继续。

## 7. 瓶颈输出的含义

主报告输出三张小表，默认各16胞：最高严格上界、最高实际 supremum 下界、最大未决间隙。
每项保留上界配置、真实下界配置、piece/radial-subcell/angle-index，以及能从原 row 准确恢复的物理符号端点和角点。
上界地址对应闭角段，其中心为 $2\pi j/Q$、半宽 $\pi/Q$；下界地址对应准确端点和准确角点。

同时保留：

- 三个 relative Gram 分量的绝对上界与 a/rho 下界；
- 真实目标 a 的余项费用；
- 新 f/z 物理标量的三个 relative-matrix 费用；
- 原核已有角补偿与分子系数宽度诊断。

若物理标量分量费用分别为 $d_e,d_m,d_g$，附加的准确保守算子费用显示为

$$\max(d_e,d_g)+d_m.$$

这只是该误差矩阵的行和预算。
`nonlinear_angular_fourth_order_padding_upper` 与 `numerator_coefficient_interval_width_upper` 仍是未除目标度量分母的分子诊断；不把它们与 relative Gram 范数直接相加，也不把预算上界说成实际误差的原因分解。
真正证明当前候选超标的依据仍是第3节的严格点值下界。

## 8. 两帽、镜像与全部相位

完整原胞并集覆盖上活动环带。水平镜像保持相对 Gram 算子范数，故同界覆盖下片。
R248 的材料角共轭平移是同一活动 g 的等距变换，环境旋转保持内积；全角上界因此覆盖全部相位，而非仅几个 t 采样。

未标记平帽对其平坦共同度量准确等距，误差为0。
如果另按 R661 加固定 marker 图，帽上采用这些固定图自身共同诱导度量，误差同样为0；活动 g 不变。不声称非零图仍然等距于旧平盘度量。
标记后的嵌入、reach、正 Euclidean 商距离仍由独立同场几何消费者支付，本入口不替代它。

`metric_certified` 与 `all_t_metric_certified` 只在全部原胞上界都存在且 $U_{\rm all}\le1/1000000$ 时为 true。
如果 `--target` 指定其它精确正阈值，`requested_target_certified` 单独比较它，README 标签仍固定比较 $1/1000000$，不放宽完成标准。

## 9. 完整公开 Actions CLI

首次全域调度，所有 raw 只留 runner：

```bash
python REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_metric_adaptive.py \
  --repo REPO \
  --bundle RUNWORK/tail-current/final.npz \
  --node-report RUNWORK/fullclosed_solver/data/fullclosed-hold-warm.json \
  --scalar-input RUNWORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz \
  --reference-carrier RUNWORK/tail-current/reference-tail-carrier.npz \
  --levels auto --panels 128 --target 1/1000000 \
  --bottlenecks 16 --budget-seconds 0 \
  --records-directory RUNWORK/tail-current/metric-cell-returns \
  --out RUNWORK/tail-current/metric-adaptive.json
```

`--reference-carrier` 可省略；提供时沿用 f122 原来的同 canonical bundle/载体身份检查。
没有这个 raw 文件时不伪造路径或复制旧载体。

已有同场 selected 报告时追加：

```bash
  --seed-report RUNWORK/tail-current/tight-selected-cells.json
```

自然检查点后的继续请求使用新的输出路径，并保留旧输入文件：

```bash
python REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_metric_adaptive.py \
  --repo REPO --bundle RUNWORK/tail-current/final.npz \
  --node-report RUNWORK/fullclosed_solver/data/fullclosed-hold-warm.json \
  --scalar-input RUNWORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz \
  --resume RUNWORK/tail-current/metric-adaptive.json \
  --levels 2048:1:5:128,4096:2:5:128,8192:4:6:128,16384:8:7:128,32768:16:8:256 \
  --target 1/1000000 --bottlenecks 16 --budget-seconds 0 \
  --records-directory RUNWORK/tail-current/metric-cell-returns-next \
  --out RUNWORK/tail-current/metric-adaptive-next.json
```

这是参数格式示例，不是假称最后一层已运行或 panels=256 已有结果。
新源、原 frozen 源和完整参数从已刊 checkout 取得；不下载历史 raw 或复制旧证书数值。
执行后的公开材料应包含实际 run、输入/输出 SHA、实际返回层和小瓶颈表，完整逐胞 row/检查点仍仅 runner 保存。

## 10. 尚未完成的目标

本调度只精化 **同一个准确场的误差包围**。
它不是求解器，不构成网格、频率和 t 加密下的解序列，也不证明存在精确解。
`fixed_metric_refinement_certified`、`mesh_frequency_refinement_convergence_claimed`、`topic_completion_certified` 始终为 false；几何标签同样为 false。
如果真实下界超标，主研究应继续求解新的同 g 场；如果仅上界未付，则依据已返回的实际费用和位置决定后续配置。
本条没有任何实际全域上界、下界、耗时或通过率可报告。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
