# R150：已成第二提升去掉投影后的四阶段低费用接口

日期：2026-11-14。此文件是实际已成数据的续算契约。新入口只重做最终九列的低费用来源和原十七式乘回，不重做 198 个方向、旧四个方向、所选九列 $K_2$、它们的正常形或任何已成 $G$ 基。

## 1. 已付的完整商身份

输入来自 run 43619888599 的已完成阶段。虽然该运行的全流程当时在最后运输阶段达到总时限，本文使用的 selected-delta、selected-normal、selected-delta-image、primary-test 和 global-check 均已完整结束，源文件在固定输入契约中逐一以 SHA256 锁定。后续高费用原十七式乘回已经由 root 完成；本入口不复算该高费用证书。

设 $p=31$，$A$ 是保持原 6188 行来源的 primitive 整数模型，$X$ 是已经完成的 $H_0$ 模 $p^2$ 来源，$H_0=(s-2)h_0$。记

$$
r_2=(H_0T-AX)/p^2\pmod p.
$$

保存的 global315 系统顺序是 $D,R,O,\Pi,W,F,E$，其中 $D$ 是本次实际九个 $K_2$ 的第二余量，$R$ 是 $r_2$，$O$ 是旧四个第二余量的实际组合，$\Pi=P(J)(D+O)$，$W$ 是完整第一像的两列，$F$ 是按实际全局来源重新付清的系数。

从全部 $315\times9$ 坐标直接得到

$$
D+O-\Pi=0,\qquad R-D-O-WF=0.
$$

因此这九个实际组合不需要再乘 degree 189 的 $P$。runner 在使用它们前会重新检查保存数组的两个全等式，不能只凭局部 39 维相容替代。

旧四个来源只用 $S_{200},S_{201},S_{202}$。按目标 $j=2,\ldots,10$：

| $j$ | $S_{200}$ 系数 | $S_{201}$ | $S_{202}$ | $\beta_{199}$ | $\beta_{200}$ |
|---|---:|---:|---:|---:|---:|
| 2 | $14+28s$ | 20 | 13 | 18 | 30 |
| 3 | $28+18s$ | 5 | 11 | 20 | 15 |
| 4 | $4+11s$ | 3 | 19 | 16 | 29 |
| 5 | $22+10s$ | 12 | 14 | 5 | 3 |
| 6 | $1+24s$ | 14 | 6 | 30 | 11 |
| 7 | $10+27s$ | 5 | 11 | 0 | 6 |
| 8 | $29+7s$ | 30 | 4 | 21 | 0 |
| 9 | $8+4s$ | 9 | 26 | 22 | 16 |
| 10 | $18+30s$ | 9 | 26 | 25 | 19 |

表中的第一像系数是 global-check 在实际标准来源变化后重新算得的 $F$，不能换回 primary-test 的局部系数。$S_\ell$ 的系数全为零。实际所选九列的 $K_2$ 已经完整恢复，九列加权来源费用均为 85，全部来源文件原样复用。

## 2. 严格费用和最终原身份

由原权重计算，$r_2$ 费用为 86，实际新 $D$ 为 85，旧三个方向来源费用为 86，且仅 $S_{200}$ 乘一次 $s$；两列第一像来源费用为 85，系数是常数。因此

$$
\eta=r_2-D-O-WF
$$

的原右端加权费用可以取 **87**。这不是把高费用输入截断到 87；实际 mixture helper 会读取所有输入系数，并在每个分量逐项检查费用。已保存的完整 $G$ 商系数、余量和所有预基来源 trace 全部保留。

最终新求 $z$ 满足

$$
Az=\eta\pmod p.
$$

同一冻结的 source9 和原预基运输算法给出的临时来源费用上界是

$$
87+96=183.
$$

实际费用须从本次原运输数据读取，不能预先声称最终费用为 87。最终来源是

$$
Y=X+K_{2,\mathrm{new}}
  +\sum_{\nu=200,201,202}b_\nu S_{\nu,2}
  +p(f_1\widehat K_{199}+f_2\widehat K_{200})
  +p^2z\pmod {p^3}.
$$

这里每个 $S_{\nu,2}$ 都是旧任务真正恢复并全原式核过的模 $p^3$ 来源；$K_{2,\mathrm{new}}$ 也是本次已成的原来源，不能将商类符号当成来源。最后一个原生阶段会完整乘回 **17 个原方程、6188 个原行、4367 个输出分量、九个目标**，同时支付 primitive 到原方程的行缩放单位。

唯一成功结论是原 $H_0$ 目标模 29791 的完整原式身份及实际有限费用；不是特征零证书，也没有改变原目标根集。

## 3. 冻结入口和输入

新 Python 入口：

    2026-11-14-r150-second-lift-projector-free-runner-789f.py

固定输入及七个依赖的 SHA256 契约：

    2026-11-14-r150-second-lift-projector-free-input-contract-789f.json

精确 CLI：

    PYTHONDONTWRITEBYTECODE=1 python RUNNER \
      --notes-root NOTES \
      --t96-recovery T96_RECOVERY \
      --all198-recovery ALL198_RECOVERY \
      --out OUT \
      --math-seconds 120 \
      --memory-mib 512 \
      --compile-seconds 30

完整或部分恢复：

    同一命令 --resume-recovery PREVIOUS_OUT/recovery

仅输入验证及编译：

    同一命令 --prepare-only

ALL198_RECOVERY 必须直接指向含 inputs、selected-delta、selected-normal、selected-delta-image、primary-test、global-check 的恢复目录。T96_RECOVERY 指向原 T96 解压根目录；程序按文件名和精确 SHA256 查找原图、全部原正常形、H trace、forward/backward DAG。无需旧 200 大 artifact，也无需重新下载四列、H25 或第二余量 artifact，因为 all198 恢复已经保存其实际输入。

原 T96 model 和模 29791 整数模型从 NOTES 读取。总共锁定 30 个既有输入。四个原生 helper、共同 header、bitplane header、旧只负责无损格式的 Python helper 共七个依赖也逐一锁定。所有 C++ 均与已执行版本逐字相同；没有新造来源生成规则。

## 4. 单一总时钟、缓存和真正恢复

默认一次 **共享 120 秒数学时间、每进程 512 MiB**。输入哈希检查、已存 315 数组身份检查和四次各不超过 30 秒的编译在数学时钟前完成。四个新原生阶段共用一个 time.monotonic deadline，各阶段只收到当时真正剩余的秒数，不会每阶段重置到 120 秒。SIGTERM 后最多给 10 秒保存真实数组，再强制结束。

| 阶段 | 作用 | 未结束时的恢复能力 |
|---|---|---|
| image | 混合已存 NF/Q/余量；完整核 $GQ+\mathrm{rem}=\eta$，要求余量全零 | 无内部检查点；完成后有内容绑定缓存 |
| source | 从同一全图 $VQ$ 恢复九列并按真 kernel 标准化；核全部原 2195 来源身份 | 保存真实 VQ 累计数组、下一图行和阶段；周期及 SIGTERM 保存 |
| transport | 支付完整 H trace、3333 预基及 forward/backward DAG，恢复全部原 6188 行 | 无内部检查点；完成后有内容绑定缓存 |
| original | 组合五个实际来源族并完整乘回原十七式模 29791 | 保存真实原乘积数组、已完成原行、累计统计及两个真实来源前缀 |

缓存和检查点绑定输入文件内容、原生源码/headers、费用及全部系数，不绑定绝对目录。因此移到新的恢复路径仍可续，但改任何数学输入都会拒绝复用。只保存一个“下一行号”不算检查点；本入口继承的 source 和 original 两个大阶段都保存真实数组。transport 没有内部检查点，本文没有将其描述为可从任意中间 H 行继续。

编译、无损压缩和清单记录各有单独时间或定义，不混写成原生数学耗时。runner 会保留真实数学总耗时、每阶段耗时和超时退出码；共享时钟到点不会输出成功。

## 5. 成功和失败判据

主回执：

    OUT/results/projector-free-second-lift-pipeline-receipt.json

数学成功必须同时满足：

    status == "completed"
    outcome == "projector-free-full-original-mod29791-certificate"
    projectorUsed == false
    rightHandSideCostBound == 87
    fullOriginalMod29791IdentityVerified == true
    finite_budget_verified == true

原 original-product.json 还须有全部字段为 true：

    fullOriginalSeventeenEquationIdentityMod29791
    fullOriginalMacaulayIdentityMod29791
    originalRowScaleTransportVerified
    allWeightedBoundsVerified

回执保留 actualSourceCosts、maximumCoefficientDegree 和全部原17乘回统计。只有正常形身份通过时不能设置这些最终成功字段。任何异常、超时、非零原余量或未完成阶段均为 failed-or-incomplete，并返回非零进程退出码。

prepare-only 的状态专门是 prepared-no-native-mathematical-stage-executed；该状态不声称新来源或新原17乘回完成。

## 6. 全输出与落库

OUT/recovery 含四阶段的真实二进制数据、partial checkpoint、两份 recipe、完成阶段的内容绑定缓存以及每阶段 JSON。OUT/results 保存：

- 主回执、四编译日志、实际阶段日志。
- projector-free-315-identity.json，含不投 $P$ 的逐目标全315零计数和实际系数。
- 原生元数据及原始 recipe 的文本副本。
- certificate-manifest.json：每个生成二进制、partial 数组和来源前缀的原长度、原 SHA256、整体 gzip 长度与 SHA256。
- certificates 下的无损 gzip；大于 4,500,000 字节时分片，每片不超过该阈值，保存分片长度与 SHA256。
- recovery-manifest.json：全部恢复文件清单和 SHA256，包括成功和失败分支。

所有已有输入通过固定契约引用；本任务不另复制 T96 图、已有198流或已成 selected 来源。若需要后续精度，应使用此次实际完成的较低费用 $Y$，并先从它计算真实下一余量，不能把同一 $Y$ 的条件性提升等同于完整高阶核自由。
