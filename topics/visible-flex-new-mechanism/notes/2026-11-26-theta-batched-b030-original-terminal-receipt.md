# 分批真实角峰续接 B030：完整原日志终态收据（2026-11-26）

## 原始身份与读取边界

本收据只登记 run [45796862274](https://github.com/Rogerhu12/math-research-public/actions/runs/45796862274) 的 B030 job [139829637288](https://github.com/Rogerhu12/math-research-public/actions/runs/45796862274/job/139829637288)。在 GitHub job 已自然 completed/success 后读取完整原 stdout；没有读在途 stdout，没有重做科学计算。

- source commit：cada9c850a1a90a6709bf182bac8b8414497919b。
- 科学入口：inverse_r566_theta_peak_batched_20261126.py，SHA256 ff24fbe2e74a8caf15b78defae454eb36280c310c725a8f9d7a623a511811140。
- 原 request：request-inverse-theta-peak-batched-20261126.json，203607 B，SHA256 1cf3ff0fd598356b7e047fb12a37fa8e12e48c587b2e758ea4247f42f863f22f。
- 完整原 stdout：1131212 B，SHA256 2147aaa11311d3a8477727b886ab28589629fad96511fd3a9a7168fec0ba313c。
- THETA_PEAK_FINAL 的原 JSON：261396 B，SHA256 b28776bd2d0aa636ff0d78e1365d9784455d7f0ee668e2d4fa0e942f92905f57；与同次 FINAL_IDENTITY 一致。
- 原日志只留 Actions 与 scratch，不入 Git，也不作为 blob/artifact 保存。本文件不复制 q 或峰数组。

启动时实际公开 git pull 于 09:58:23.007280 UTC 完成，从 source 到 1f42cce3087ba23d38d469aebc03bf35f59ac49c；根 README 与课题 README blob 分别仍为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、d0432faff569c8e9af7ed4809847e12880976c11，差异为空。实际私库 pull 于 09:58:26.491066 UTC 完成，HEAD 815ee053703dabb40f8b477e7cbe441de5daf8d7，根 blob 5ba164843b1f5802184178a82d786264404873a3 未变，QUEUE 唯一且仍属本会话进行中。

## 新 scope 与已付来源

输入是 run 45790610433 的 B030 真实保留末 q，采用其全部 actual 与 pending：450 个径向节点、1536 个均匀角、1021 个额外峰反射轨道；trust=1.20135498046875。没有取此前未接受的 eta=.2708966994021432 trial。

物理参数仍 p=.85、q=.15、rounding=.15；R566 背景及 81 维有限表示不变。联合充分几何预算仍 R=1.012、Y=.3928、tau=.06072；mean E 下界 .25、det 下界 .1，几何 working margin=.001（height 除外），raw fine 接受容差 1e-8。逆设计每个 q 改变平均度量，不是固定 g 精化。

唯一已声明定位变化是把旧候选总 cap 512 改为有序 batch size 512；所有枚举候选完整处理，未完成不得接受。旧实际均匀约束、全部原峰、空间 jet、分块 AD、任意角算子及接受门保留。首次接口 parity/方向检查已在来源 run 支付，本次新检查次数为 0。

## 实际结果、几何接受与停止原因

两次 callback 均被完整 fine 网与已枚举角峰准入：

| 记录 | 已定位角峰 eta 上界观察 | raw 几何违约 | 定位候选数 |
| --- | ---: | ---: | ---: |
| 初始保留 q | .2750050277062108 | 0 | 464 |
| callback 1 | .2705909607975619 | 0 | 752 |
| callback 2 / 最后保留 q | .2651373529074538 | 0 | 693 |
| 最终同 q 独立完整扫描 | .2651373529074538 | 0 | 651 |

最后完整 fine 网为 902×3072。其均匀网 eta=.2651372774607208，attainer s=.42656249999999996、theta=1.349903093339364；任意角定位在同径向圈得到 theta=1.3497298856824302、eta=.2651373529074538。这只是当前 fine 径向圈上已枚举括号的数值定位，不是全连续二维峰覆盖证明。

终态关键几何：

| 量 | 观测值 |
| --- | ---: |
| 最大球半径 | 1.0114938678604983 |
| 最大绝对 y | .39259841884869245 |
| 最大绝对主曲率 | 16.454757882236777 |
| 曲率位置 | s=.751171875，theta=pi/2 |
| mean E 最小 / 最大 | .9961334484617511 / 3.3312840517851954 |
| det 最小 | .8535438241152891 |
| z 最小 | .02 |

球、strip、curvature-plus 的 raw slack 最小分别为 .00100001101467051、.0010261172431846877、.0008671013905829916。最后曲率 raw 门满足，但比 .001 working margin 少 .0001328986094170084；原实际约束该曲率组违约为 0，新 fine 峰未被实际约束覆盖，因此按已声明规则触发 urgent exchange。没有把 working margin 债误报成 raw 几何失格，也没有因 raw 门过而丢掉待加入曲率峰。

自然终止标签为 **unresolved_actual_peak_capacity_checkpoint**：实际还是 450 径向、1536 均匀角、1021 额外轨道；提议下一批是 **494 径向、1536 均匀角、1129 总额外轨道**，next trust 仍 1.20135498046875。1129 首次真实超过声明峰库 cap 1024，故提议未构造、未优化。径向 494 没有触及 513 cap；本次不是 512 候选 cap 或时钟终止。最后已接受 q、实际网格和未采用提议在 FINAL 中分别完整保存。

## 真实成本

科学新耗时 295.608894049 s；输入链已付 1959.1382393010003 s；累计 2254.7471333500002 s。launcher 记录子进程 09:58:33.345187–10:03:31.116888 UTC，返回码 0。

- 完成 1 个 outer、2 次完整 callback；2 次 metric 改善、0 次 restoration 改善、1 次 urgent exchange、0 次自然 OptimizeResult 返回。
- 4 个 actual value keys、2 个完整 Jacobian、12 个参数方向块；最大块值重构差 0。
- 4 次完整定位、7 个 batch、2560/2560 个候选全完成，17850 次标量定位目标评价；未完成候选与 clock partial 均 0。
- 19 个 prepared FFT states，171 个 Fourier primitive fields；125368 个非均匀点求和、11376 个严格均匀点 gather。
- oracle 的参数方向点计数 661608，point values 136744，point set preparations 17851；其实际耗时已计入科学总时钟。
- 最后 callback 的 nested FFT 观察差：metric components 1.9984014443252818e-15，relative mean E 6.434726471340396e-16，tau-curvature 3.5324276836945497e-15；这些不是连续 Fourier 尾证书。

## 范围与可接续身份

本次 batch 改动确实解除了已登记的 512 候选整批拒绝，且 eta 从 .275005 降到 .265137。下一计算可据这次真实 1129 峰需求定义更大的峰库，必须保最后 q、450 实际网格及全部 494/1129 待采用提议，不能回放上一初轮或丢峰。下一状态传输也须完整保留；仅含核心实际/提议/已付接口 provenance 的 JSON 已约 123122 B，接近常见单命令行参数容量。

当前仍是有限网几何合格的逆设计输入。连续角/径向误差、全 pair reach、固定 g 收敛、有限等距族、宏观可见形变及 README 全部门均未完成；job success 不升级这些结论。
