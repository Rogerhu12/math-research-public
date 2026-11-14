# 真 A 的固定度量尾部加密：恢复后的实际入口

作者：exact_closure，GPT-6 Astra Pro，AI 辅助。2026-11-14。

本文记录一个实际数值实验，不登记新的无限维存在性结论。课题完成标准仍要求整闭面的大幅度、全时刻 reach 和固定问题的网格/频率/时间加密。

## 1. 幸存对象与应纠正的深度

原接受 A 的主件是
`notes/2026-11-13-strong-q126-m32-tail2-actual-r1.json.gz`，
SHA256 `917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf`。
其实际尾响应为同前缀 `-tail-response_0003.json.gz`，SHA256
`018d19c6ca8c27acc5cc1dde6d396ee783e34ae25e5b525158c5bb37086520d9`。

本次直接读原配置得到：

| 项目 | 原接受 A 的实际值 |
| --- | ---: |
| Fourier 余弦/正弦模数 | 32（物理偶频 2 至 64） |
| 非线性物理深度 | 8 |
| 每个原段 shooting 分段 | 8 |
| 每个 cell 的原段数 | 9 |
| 非线性 stage / node 数 | 576 / 577 |
| 每个 stage 的 RK4 步数 | 12 |
| 角求积节点 | 512 |
| 线性 far / 步数 | 48 / 2048 |
| 原有限 Newton 容差 | $2\times10^{-9}$ |

不能把旧 q003/R26/R145 线上 `depth=12` 的证书移给 A：那是另一条对象链。A 的实际 worker 使用 `tail_frozen_geometry.mjs` 的 **stored** 工厂；它保留原 160 个浅头和原辅助 far 图，不使用 `closure_frozen_endpoint_worker.mjs` 的有理深尾替换。若要以后接入 $n\ge160$ 的 $65/64$ 深定义，需另外说明同一对象与接合关系。

幸存 A 尾原 audit 是

$$
\text{metric}_{\rm finite}=5.55152887355675\times10^{-15},\qquad
\text{fullD}=3.6135721861390253\times10^{-12}.
$$

这只是原有限样本 audit，但已经远低于原完整前缀/均值读数约 $6.73\times10^{-8}$。因此实际幅度、闭面几何和前缀仍是主线；不能用大量小尾预算工作代替真实增幅。

## 2. 本次只增加有限非线性深度

新脚本
`computations/exact_20261114_fixedH_tail_depth.py`
从原配置直接复制，仅把非线性深度从8改为12，并更新日志/检查点输出路径。全部32个物理 cut 高度 $H_m$、stored 工厂、角频率、求积、原 RK 步数、线性 far/步数及 Newton 容差保持。

worker
`computations/exact_20261114_stored_depth_worker.mjs`
复用原 `tail_frozen_worker.mjs`，只把深度增加时的初猜入口交给已有
`closure_depth_warm_remesh.mjs`。其深度 remesh 实际得到865节点：旧577节点逐位保留，新增288节点按原线性图补成**初猜**。之后仍执行原完整非线性 residual/Jacobian、线搜索和显式请求的有限 audit；初猜不是新解。

原通用 worker 还会在请求入口执行一次比例为1的 `geometricAmplitudeWarm`。本次实际日志保留其重新计算 mean 后的微小浮点变化：非恒定径向高度 Fourier $\ell^1$ 差小于 $6.63\times10^{-19}$、动量相对差小于 $8.48\times10^{-14}$。所以“逐位保留”严格指深度 remesh 的输出，不指经过该通用初猜转换后的每个二进制数。最终结果仍由原真实方程判定。

新旧 stored 工厂的两组全160头历史指纹实际相同。工厂名为 `physicalParameters` 的对象也携带 `depth` 和 I/O 字段；比较时仅排除这一次明确变更的深度与 I/O，其余全部字段保持。不能因为该对象名字含 physical 就把纯离散字段的变化误判为换度量。

## 3. 可复现命令

先用现有 `prepare-source-dependencies.py` 在固定修订
`869436630c99aa5a68afb55bd8877c826034d117`
恢复 `source-dependencies.json` 列出的91个小依赖。令 `SOURCE_TOPIC` 指向其中的 `topics/visible-flexible-closed-surface`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python computations/exact_20261114_fixedH_tail_depth.py \
  --topic /absolute/path/to/topics/visible-flex-larger-amplitude \
  --source-topic "$SOURCE_TOPIC" \
  --out-dir /fresh/path/A-depth12 \
  --depth 12 --node-heap-mib 384

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python computations/exact_20261114_compare_depth.py \
  --topic /absolute/path/to/topics/visible-flex-larger-amplitude \
  --new-dir /fresh/path/A-depth12 \
  --out /fresh/path/A-depth12-comparison.json
```

控制器保存实际 stdout 返回的 ready、完整响应、所有阶段/迭代日志与真实子进程退出码。比较器从完整原 flow 身份中读取 node8 的真实线性 far graph，比较两次实际解在同物理 cut 的高度、坡度、二阶及完整 mean 修正，并读更深解在旧 node8 边界的非零 Robin 缺陷。

首次 `r1` 在进入科学计算前因未显式设置 `CLOSING_TAIL_CACHE` 被原源加载器拒绝；实际退出1，0.5388秒。修复只是在控制器中把它指向已核的相邻源码目录。`r2` 已在 2026-11-14 05:15 UTC 完成真实求解及原完整 audit，实际子进程退出0，墙钟1643.73秒。终态全件保存于
`notes/2026-11-14-exact-resume-fixed-H-depth12-r2/`；其中 `response.json.gz` 含完整865节点终态，`ready.json.gz` 记录原度量/初猜身份，`result.json` 记录实际退出，`comparison.json` 是两个已成功有限解的比较。`iteration.json.gz` 是同一次运行的恢复检查点，不是另一次独立解。

## 4. 已完成的同 H、同 g 深度比较

旧、新有限残差分别为 $9.4590080\times10^{-10}$ 和
$8.3617779\times10^{-11}$，都通过原 $2\times10^{-9}$ 容差。新运行一次全 Newton 步把初猜残差 $3.72621\times10^{-3}$ 降到终值；其后完整 Jacobian 再评估与原全尾 audit 均完成。

| 实际比较量 | depth8 | depth12 / 差值 |
| --- | ---: | ---: |
| shooting nodes | 577 | 865 |
| 全有限 audit metric | $5.5515288736\times10^{-15}$ | $5.5515288760\times10^{-15}$ |
| 全有限 audit fullD | $3.6135721861\times10^{-12}$ | $3.6135695938\times10^{-12}$ |
| 最小 leading | 0.8635125234879344 | 0.8635125234879352 |
| 最小 D | 0.9999285137949182 | 0.9999285137949182 |
| 最大 formal curvature | 7.994254693544281 | 7.998111913734926 |
| cut 全32模高度最大差 | — | 0 |
| cut 全32模坡度最大差 | — | $5.4210108624\times10^{-20}$ |
| cut 全32模二阶最大差 | — | $1.0842021725\times10^{-19}$ |
| cut 完整 meanSlope / meanSecond 差 | — | 0 / 0 |
| cut meanSecondCorrection 差 | — | $3.3881317891\times10^{-21}$ |

这里比较的是相同物理 cut 的 mean **一、二 jet**，没有把两种不同内端锚点的整体均值高度直接相减。旧577个 canonical 节点的最大坐标差为 $1.02055\times10^{-11}$，逐节点按旧节点最大分量归一化后的最大差为 $9.74578\times10^{-9}$。这些内部浮点变化与 cut 的变化不是同一种范数。

更深解在原 node8 上对**原实际 far graph**的 Robin 缺陷
$\|\Pi-B_8Q\|_\infty=1.9756723083\times10^{-24}$，约为原 node8 最大分量的 $1.01908\times10^{-8}$；旧有限解因施加该边界而为 $2.13821\times10^{-50}$。新解无需在原内端继续满足旧 Robin 条件。

因此，这个固定 A、固定完整 $H$ 上，将物理深度从8延长到12，cut D-N 响应的差已经处于当前双精度舍入尺度。当前先增大前缀可见幅度有直接数值依据；不能由这一个点外推到未来更大幅度的 $H$。新候选接受后仍应在自己的固定 $H$ 上比较。

## 5. 这项计算能回答什么

它量化同一个 stored 度量、同一个完整 $H$ 下，原有限线性 far 边界从node8移至node12时的实际 D-N 变化。node8 原完整32模的最大 canonical 幅度出现在主模：

$$
Q_2=-5.8420293213562315\times10^{-18},\qquad
\Pi_2=1.9386758366505556\times10^{-16}.
$$

这里的 $\Pi$ 是原非线性 connection 动量，不偷换为真实线性 canonical $\Xi$；这些值也不是物理空间位移下界。

两个有限深度的成功与接近，不单独证明无限尾存在，也不证明全部深度序列收敛。它不消除角频率/径向误差、不自动重新满足前缀 BVP 边界，不处理永久固定 collar 的缺陷，更不替代 $\delta_{\rm hold}/D\ge0.2$ 和全闭面 reach。若只靠增加层数压低一个未接到精确解的固定缺陷，仍不满足课题README；本次实验仅是固定问题收敛链的一项具体输入。
