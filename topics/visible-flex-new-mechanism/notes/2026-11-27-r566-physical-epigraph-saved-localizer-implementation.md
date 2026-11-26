# B030：完成真实未闭合角峰队列，并修复辅助 epigraph 回退

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

**状态：纯源码与下一次公开 Actions 输入，尚无本 scope 的科学结果。**
这不是固定度量证书、连续角峰界、reach 证书或 README 完成结论。
源终态数值见 [原始终态收据](2026-11-27-r566-backend-preserving-original-terminal.md)。

## 实际来源与改变的理由

唯一源 run 为
[45883086225](https://github.com/Rogerhu12/math-research-public/actions/runs/45883086225)，
job `140126984773`，触发提交
`7923e588c07cd47852dfdf4604db5bc8246ce92d`。
原 stdout 为 21,831,112 B，SHA-256
`86b6cfc91026975192da40e960b356680c09f3da5c227a37941ce013f59f4916`；
原 FINAL JSON 为 529,571 B，SHA-256
`7f71616f8fe94fd1c58889a4e64d66b8253dd6ffef35c75549ffbf70760ae406`。

真实保留的 81q 为
`bb921f60d02a3624552d79ebc623e3eb3306b174d981a3ca794a57b44d8edaa4`：
605 个径向点、1355 个实际峰 orbit、463 条工作行、1536 点均匀 FFT；
通过的 fine 为 1212×3072，另有全部 1292 个已完成角峰定位，
实际 $\eta=0.24394558845134018$。
真实 trust 与尚未改变的 next trust 都是 `0.3003387451171875`。
源段已完成 19 次实际 metric 接受和 48 个完整 Jacobian，不重新运行。

源原日志提供了具体瓶颈：按 raw q 去重后，48/48 次 working 失败
只有 `metric_plus/metric_minus` 违反，所有物理 working 组都通过；
12/12 次完整 coarse 拒绝也只有 metric epigraph 违反。
这是针对已经支付的原 `fun` 向量的分组解析，没有额外科学求值。
因此新段允许对**同一个物理 q 的独立候选副本**抬升辅助变量 e，
随后仍要求真实 $\eta$ 严格下降；抬升 e 本身不是进展。

## 原未完成候选必须先完成

源末次半步候选
`bc9b991faee4beb81b91cbdc834aae6dbdcb1be951d803386f787c97430df097`
尚未接受。它已经完成原 working、2,151,130 条完整 coarse、
1212×3072 完整 fine 及 nested FFT 比较，但角峰队列的 1353 个
candidate 一个也未处理。原 fine 的 $\eta=0.2430865314325668$
不能替代未完成的全部角峰门。

新段先在原 q、原 fine 数组、原 FFT3072、原 oracle identity
`5a3bd2d05c0fad31786fc416eb5fdb2299671a2f9461b00d3fe9bad3e22002a1`
上逐一处理原保存队列，不重新枚举，不跳过 bracket。
原 partial JSON 为 305,148 B，SHA-256
`7ff97bef28f0039ddd6c05ec21cb739debc59cc2b32fd5d6f22c7b00f5573915`；
fine 径向数组 binary64 SHA-256 为
`29db161be6a30bbe07ce8e28c30160fe1982aacf1d8ec4a79262364140afc2d1`。
helper 验证每个原径向索引、角索引、中心/边界分类及 bracket 端点。
目标仍是原 four-orbit 值，`bounded` 定位、`xatol=1e-10`、
`maxiter=50`、低于原 sampled 值时回到原中心值，全部照原实现。

重建该 q 的 FFT/primitive 是跨进程继续所需的新工作，计入同一个
`OracleLedger`。已支付的 coarse/fine/nested 报告仅因 q 与完整
原 scope 精确相同而复用，不把它们记作新扫描，也不重新执行。
源固定物理 box 逐坐标验证。原 pending 的径向点
`0.47812499999999997` 尚不在原 605 点 coarse 中，故先完成
上述原 scope，才采用 pending 物理库；不偷换局部化网格。

若 1353 个 bracket 仍未全闭合，保存剩余队列且不接受。
若全部闭合，也仍需原工作几何 margin、真实物理几何、
nested 容差、epigraph 包含全部观测最大值及真实 $\eta$ 严格下降。
这个候选若最终接受，其身份是“补全原未完成候选”，
不标成新 SLSQP raw 点，更不假称原 BFGS 数组已经恢复。

## 辅助抬升的数学理由与执行门

原 `constraint_groups` 的两个 metric 行是

$$
e-\frac{\sqrt{\mathfrak e^2+4\mathfrak f^2+10^{-24}}
                  +\mathfrak e}{2},\qquad
e-\frac{\sqrt{\mathfrak e^2+4\mathfrak f^2+10^{-24}}
                  -\mathfrak e}{2}.
$$

固定 q 后，仅把 e 增加 $d\ge0$，每条 metric 行恰好增加 d，
全部物理行与 q 的 box 不变。因此源未完成候选在较小 e
已通过的完整 coarse/working 行，可在相同 q 的较大 e 直接继承。
原 queue 的 metric 候选阈值为
$e-\max(0.002,0.01\max(0,e))$，它随 e 单调增加；
较小旧 e 已保留的全部候选也是较大新 e 所需集合的超集。

正常新候选不只靠这条代数性质省略原门。工作行、完整 coarse
或完整 fine 后产生抬升时，都调用原 `WorkingRows.fun`；
coarse/fine 抬升后也重新调用原 `candidate_rows`。
所有这些新求值、FFT、定位与完整 Jacobian 均记账。
抬升余量为所需非负增量加 `32*eps*max(1,abs(e),increment)`；
原 SLSQP 数组不会原位修改。

执行顺序保持：固定当前 trust box 内的物理 q；全部工作行；
全部 coarse 均匀行和实际 peak orbit；完整 fine；nested 比较；
全部观测 bracket；原 margin 与真实几何门；真实 $\eta$ 严格下降。
geometry restoration 阶段不采用此 e 抬升。
保留球、条带、正高度、mean-E/det 下限、两个曲率组、mirror 必要条件，
也保留原完整物理参数与优化参考度量设计。

抬升前找到的新 coarse 工作 witness 和 fine/实际角峰证据不会消失：
全部实际物理新点仍进入 pending；最坏有据工作行进入下一轮 matrix。
真正发生库交换仍重启 backend。没有库/phase 变化时，同一 SLSQP
调用继续持有自己的 raw 点及 BFGS 历史；独立物理 best 不写回它们。

## 完整细网与费用继承

纯坐标解析确认，上一终态的 1172 点 fine 是此次 1212 点 fine 的
精确子集；按旧源码恢复的此次 fine 与原 partial 数组逐项相同。
新实现永久取旧 fine、每次新增 fine 和全部当前 coarse 的精确并集，
避免后来插入 coarse 点改变中点时遗失旧 fine 点。
checkpoint 分别输出当前完整 fine 库与保留 q 真正通过的 fine 库，
旧 q 不因库增大而自动取得新网格资格。

working 容量从 512 增至 1024，因为源已有 463 行并有新证据。
这不删除任何物理行。原径向容量 1025、peak orbit 容量 2048、
每批 512 个 bracket、块方向 16、全部 tolerance 与 trust 范围保留。
每段科学上限 2400 秒、收尾预留 30 秒、job 上限 50 分钟；
时限只形成可继续的真实 checkpoint，不表示课题完成。

源科学链已知下界为 `9988.810808117` 秒，较早三个外部截断区间
仍是未知费用，不被编造成零。新段记录独立的新费用，保留全来源链。
原完整 FINAL 中的 q、实际库、工作证据与未完成 bracket 是后继必要输入；
不提交原 stdout、全扫描数组、网格输出、artifact 或缓存。

## 发布文件

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `scripts/r566_saved_brackets_and_epigraph_20261127.py` | 7137 | `5ba4aaa134135ce871a76d0aafe2c6161789e41fac20dc1ef26aecb9bf2000e5` |
| `scripts/r566_physical_epigraph_and_saved_resume_20261127.py` | 53193 | `f5aa6c45a9d56b2f55eb12e33ae4223d5bbf737c7edcfe5a27f5ad0cea7d0911` |
| `computations/request-r566-physical-epigraph-20261127.json` | 687391 | `84d8f1be89f5acbc1760fd1fd9a6f8ee0f2da64498cb737c9e6a6f8fe8b21d2c` |
| `.github/workflows/visible-r566-physical-epigraph-20261127.yml` | 4756 | `9cd1f8921b62d872958fa6fe28c3d7f756a2cc72c553f472fb1afdcb793285ec` |

lane 为 `rounded-core-B030-physical-epigraph`。
stdin 592,563 B，SHA-256
`3d6764d22cfad7d020240fb3f54407715bda413d45f3ba6fba11325646c92706`。
26 个源码/前驱 request/workflow 绑定均匹配；本地只做文本、AST、JSON、
hash 和原日志/坐标解析，没有导入或运行科学模块。

公开 workflow 先真实 pull 双仓并核对 README 与本会话 QUEUE 认领，
删除认证环境后才执行新科学。所有新数值结论等待实际 Actions 原终态。
