# actual38：两原段的四个短 J 已实算，原出口逐位保持

2026-11-14。公开 run **43619564953**，source **ceb4cd61e1a2211901dfd4c287ec28fe92309e4b**，job **132521953211**，artifact **14123093790**（`visible-mainline-nativesplitprobe-43619564953-1`）。ZIP 为 2,551,573 B，SHA256 `46780a795d4186fbb11f7f7d68159f2225ad33af31299d34030692e5bda2d018`。

## 1. 实际完成范围

已按[原同 schedule 探针接口](2026-11-14-native-same-schedule-split-probe-interface.md)完成原 stage43、58 各自的 6+6 withJac 分组：**4 个新短 J、4 个独立 no-J 半窗、全部完整中间 state**。局部 probe 用时 3.976 秒，完整 launcher 用时 28.750530708 秒。

这一次原 guard 均正常返回。原 native solve、整条尾的 J、原完整12步参考 J 重算、Newton trial、endpoint J、最终 audit 的调用数均为0。唯一协议请求在原 solve 前按计划抛出 `VISIBLE_NATIVE_SAME_SCHEDULE_SPLIT_PROBE_COMPLETE_V1`；原 worker 如实返回该 failed 字符串，随后正常退出。Python 将它登记为 `probe_completed=true`，并保持 `native_accepted=false, task_completed=false`。

实际结果身份：

| 文件 | SHA256 |
|---|---|
| `result.json` | `80a2c7ec5ad45679869b94e3b6a55e9b4504b822f6c2f972269b1b9b25f644d9` |
| `split-probe-spec.json` | `ef847ce86d834a2e5a4eb58299d12d46b5e1ff64d2d253331672aa63df935486` |
| `split-probe-summary.json` | `4a3628fda8b1e2338b7f2f03d8b348373d8314d108e014d8b2390bce610a609e` |
| `split-probe-array-manifest.json` | `15c958aeb4fcc364c20bd0b4644a9c422f12206717d78e8c9058d138d36bcd6b` |

## 2. 四个新短块的实际数组

各短 J 都是完整 224×224、401408 B，共50176个有限 binary64 条目。以下最大值来自 Actions producer 的原始统计；本地只核对应已报极值位置的 operand bits，没有重算矩阵范数或最大值。

| 原段、窗口 | 已报最大绝对条目 | 完整短 J SHA256 |
|---|---:|---|
| 43，inner k=0..5 | 1.457917049962635e21 | `cde78aec9be590b99e3541808723b1942ab113fb1a78c4817c00a338d505afdb` |
| 43，outer k=6..11，原 port 已作用 | 1.2264277478091406e14 | `d574eabaa42ca88a21e2483448d47feaa556ea8a8a3533b4349b347c015aa6ba` |
| 58，inner k=0..5 | 3.002676916799508e19 | `d8b511ee340e0726d5fcc6c91387a0ed0583f477ff401b777bd39e1afb312140` |
| 58，outer k=6..11，原 port 已作用 | 1.6260271106263415e19 | `983eaf8a7a64e14011e2ab7a09a253983221a9dce27328fbfcabc742ed64dc9b` |

原 actual28 两个长 J 的已报最大绝对条目分别为 2.5195207531999574e24 和 1.0007950021979336e29。新块的有限性与这些条目数值，尚不能决定扩展全系统的条件数、线性缺陷或 nonlinear trial 是否成功。探针没有将两个短 J 相乘回长 J。

各 withJac 短窗的原返回 guard 记录如下：

| 窗口 | minA | minD | maxRootRelative |
|---|---:|---:|---:|
| 43 inner | 0.9999999999999992 | 1 | 4.00740628163011e−16 |
| 43 outer | 0.9999999999999967 | 1 | 1.6891386768061232e−15 |
| 58 inner | 1 | 1 | 1.7379003043383196e−16 |
| 58 outer | 1 | 1 | 8.807065846442349e−17 |

独立 no-J 路径的原函数不返回 minA/minD 汇总；该路径保其真实 guard 返回和完整状态，没有补造上述统计。

## 3. 原出口、mean 和真实时序

两段的 withJac 分组最终224项旧坐标出口，均与 actual28 原完整段 `stage-out` **逐位相同**。producer 同时报告组合 `[minA,minD,meanHeight]` 三项逐位相同。完整226项中间 state 始终沿内窗传给外窗，两项 mean 积分未在中间清零。

本次独立 no-J 6+6 路径的最终224项出口与已报 meanHeight 也与 actual28 withJac 参考逐位相同。这只是该实际基点的结果。两种原字面调度仍有区别：保存的 x 位模式在原步 **5、7、10** 不同，分别来自 withJac 的 `n*(1/12)` 与 no-J 的 `k/12`。源和记录都保留了各自公式，未将这个相同出口结论扩张成两条浮点程序处处相同。

出口原始 SHA：

| 原段 | withJac、no-J 及原 actual28 出口共同 SHA256 |
|---|---|
| 43 | `90bfaafffe40aa31ab47ce2f45867d4f9f714e2e546b471f21185836497c75b9` |
| 58 | `fceed6ce39d66943d2535e714cb4c7616cdc467d944b7cc8d8ae85f7c2b75b1a` |

## 4. 只读字节与接口审计

本地仅进行文件、SHA、形状、位分类和记录对应核验，没有执行 RHS、RK、J、dot、范数、线性求解或消费者构造器。完整账见 [actual38 字节审计](2026-11-14-actual-request38-byte-identity-audit.json)。

- 实际38所列62文件、2,878,882 B全部重核 SHA；新23个 binary 数组、1,649,848 B全部重核 SHA、shape、finite 位分类及已报极值 operand bits。
- 原28全部29数组、116chunks、238,972,680 B再次流式重核。原完整 J SHA 仍是 `394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19`。
- 每段的原 input、output、guard-mean、旧 J 四份参考，均对原28对应完整字节；226项初值前224项保持旧输入，最后两项为原正零。
- 8个窗口的完整 state/tangent 文件及 hash 相符；原 portRatio 两段都为1，因此已保存 shape J 与额外 mean tangent 可逐字节核完整 tangent SHA。
- 48条实际 step 记录、288个保存的数字字记录、inner/outer索引顺序和两段同分支 schedule 全部对应。没有重新执行时序或计算新科学差值。
- 新 `oldToNew`、578段 cells、全579项显式 σ 与冻结消费者声明吻合；全部旧σ字保持，两个新增中点采用各自原 parent stage 的σ。完整原 input map、live identity 和三个 producer source SHA 均一致。

guard-mean 的加法/最小值和 J 最大值仍按 producer 实测记录引用；字节审计没有伪称重新验证其科学计算。

## 5. 已确定的后继

这份实际产物已具有[578段独立消费者](2026-11-14-native-split-equilibrated-interface.md)声明的四个完整有限短 J、完整中点和同一原输入。只读审计未发现绑定阻断，实际组装与求解仍须在公开 Actions 执行。

后继可用原574个未分组 J 与本次4个短 J 形成独立新矩阵，保原 cut/far/H、原旧节点与σ、显式新增σ，并保存新矩阵身份和完整缺陷。方向限制回旧577节点后，真正 readback 是原完整 nonlinear no-J/evaluate/trial 的全部原 guards 和接受公式。旧长 J 的线性缺陷仅保诊断，不新增为新方向的科学接受门。

本结论止于实际短块和原出口身份；本题全闭面、幅度、reach、δE 以及完成标准未由此核销。
