# 完整 1977 格帽的四分域源：实际 12 门通过

公开 Actions [43626024582](https://github.com/Rogerhu12/math-research-public/actions/runs/43626024582)
于 2026-11-14 18:46 UTC 真正完成两端恢复及完整汇总。
finish 数学 child returncode 为 0，12 门全部通过，实际数学时间
6.851227657 秒，wrapper 记录该 child 用时 10.000693076 秒。
这不是仅通过 eligibility 或保存一个待运行提案。

## 实际覆盖与原件复用

原完整任务 [43623547711](https://github.com/Rogerhu12/math-research-public/actions/runs/43623547711)
的六个中间区间均已实际成功。其原生 native 和 artifact process 按准确 SHA
交叉消费；两个失败端点的成功 prefix 也保留。

| 来源 | 本次新增 | 原成功域复用 |
|---|---:|---:|
| 入口原父格 $[0,256)$ | 1023 | 原首格 1 |
| 末端原父格 $[1792,1977)$ | 100 | 原前缀 640 |
| 原六个中间区间 | 0 | 6080 |
| 最初 16 父格的四切 pilot | 0 | 64 |

本次只补了 1123 个缺失域。finish 核验完整笛卡尔集合
$(i,4,j)$，$0\le i<1977$、$0\le j<4$，共 7908 个域，逐一且无重复；
原 64 pilot 行的 canonical row SHA 不变，全部旧成功域未重算。
当前 7844 个非 pilot 域包含旧完成行与本次补齐行，不能误称本次新增 7844。

入口恢复只在原首 Hermite 多项式已有定义的
$[9/10,\operatorname{binary64}(0.9)]$ 极短带内放宽入口 guard。
原节点、矩阵、导数与 trial 未改。末 100 格的 NaturalGraft 读取合法参数半宽
$10^{-9}$ 的包络，其中包含固定物理 $\eta_0$；它不是零宽 target，也不把结论
扩大到整个参数盒。其余原 640 行不变。

## 同一方向上的完整物理帽误差

输入仍是准确 repaired M32 centre 与同一 $w_0$，保原 257 态、97 正交 even
输入槽、真实 even mean、完整 Fourier 余项、六条外部费用与全部 14 个
Green 增益。每父格只在完整八通道表示间选择，随后按全区平方和与原反馈
resolvent 计算；没有跨模型独立挑选有限项与余项。

实际输出的严格上界为：

| 完整合法表示 | 物理帽误差上界 |
|---|---:|
| 原 1977 格有向完整基线 | $2.418183101946\times10^{-6}$ |
| 仅原 16 父格精化的 pilot | $1.508953388222\times10^{-6}$ |
| 全部 7908 四分域直接合成 | $4.198795604199\times10^{-8}$ |
| 逐父格完整八通道选择后合成 | **$3.601796223643\times10^{-8}$** |

最后一行是实际选中的 `new_complete_coupled_selection`。
这些都是合法上界，不是实际误差的下界或近似等式。

配套的 14 条物理费用中，主要三项为
$f_B<1.225126672546\times10^{-8}$、
$f_C<1.411489725436\times10^{-8}$、
$d_B<8.882554820868\times10^{-9}$。
还保留
$r_C<2.384646419969\times10^{-10}$、
$d_C<1.785523679406\times10^{-10}$、
$f_{C0}<3.475910690813\times10^{-10}$。
原 $e_L,e_D,e_0,e_{B0},r_B,j_B,j_C,f_{B0}$ 也逐项在 native 与小 summary
中保存；它们没有因较小主项被删除。

## 完整证据身份

所有路径以下列 topic 目录为相对根：
`topics/visible-flex-exact-nearby/`。

汇总目录：

`notes/complete_quarter_cap_inlet_recovery_ci/run-43626024582-1-complete-quarter-cap-inlet-recovery-finish/`

| 文件 | SHA256 |
|---|---|
| `native/complete1977-fixed-eta-quarter-cap-sources.json.gz`，1,493,163 字节 | `770106a925812df4fc380785ca3e715b2a30a649a355fb888e0dcbe0e6a65298` |
| 仓库 `process.json` | `2a7903ef56e245315937cd5ebc8d8467b86dbf7c445c1ef4924fcd476037e9d1` |
| `evidence/complete-quarter-cap-finish-summary.json`，8,711 字节 | `36c44dff71b6ac4e577ab690cd4c25874deb0f101a289d0c1a3488db1eea2ef0` |

上表 process 是仓库快照。下游读取原 artifact process 时必须使用其真实
快照身份，不能把这个 SHA 当作 artifact SHA。

入口 native 为
`02cfd7c9945180adcdb208f0e6101b3c9da37c0deca8b012160c89ea7148ccb8`，
5,707,777 字节，按原字节分成 3 片。入口 5 门通过，新增 1023 域，
实际数学时间 1346.30361305 秒。
末端 native 为
`0a4ef5ee7924839bcc53ccf04fe85d8011c865b25a10eba59a66553331a14563`，
4,122,070 字节。末端 5 门通过，新增 100 域，实际数学时间
86.757986343 秒。

本次科学源 SHA 为
`222b9a3dbfe842fbf8823d79584174cab5a350652db8a35cded0a610c45f6793`，
worker 为
`cdaebcd03696c86249dc2cb0798a39fb4e4fabef92259af7ec3fcbe63c12a9e2`，
164 项输入 manifest 为
`b141f6d9be92cb86fc06b49933bfb005eb0de383eef5dd8bd91a6c347d8b1263`。
原 plan native
`406e3e5331720a3f87f2b5f53c2e7d2988bea25b7537d650157ed97278e3073a`
原样消费，不重算计划或原格。

finish 的 5 次真实 pull/README 检查均记录空差异，最后读至提交
`d006d04987a0f948568757fb0c61dd03534553b8`；
入口运行的 7 次检查也均为空差异，最后读至
`c216015a7fb876431b66a9ce63111b2799cc5b73`。
两份规则按已读提交
`ee26c0a65a2e63c15f2ccfba6714181584416542` 执行。

## 已授范围与后继

本结论授予同一已知 $w_0$ 的完整物理帽源误差及其匹配的 14 条费用。
它没有单独授予 Hessian 修补后的 moving 误差、真正 cut 97 行、
有限 193 态响应目标或完整无限 BVP 逆。

已部署的 cached-quarter Hessian v2 已由本次实际 success 触发，运行
[43628443697](https://github.com/Rogerhu12/math-research-public/actions/runs/43628443697)；
其后由独立消费者保全部 mean、已知 high、剩余 $Z-w_0$ 的原完整误差算子，
再消费既成 6391 片 Green。后继运行中的候选数值不属于本条已证结论。
