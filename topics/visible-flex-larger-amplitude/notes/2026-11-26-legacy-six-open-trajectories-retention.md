# 六份旧独立开放轨道的完整留存与第十九次普通移出

2026-11-26。原留存记录由 geometry 在 scratch 准备；其准备过程没有删除仓库文件或写 ref。
root 随后独立核原字节、完整来源、全部非轨道字段/参数及当前脚本依赖，
本条已普通移出下列六份可再生轨道，实际应用记录见第7节。
遵照根 README 第 8、10、15 条以及既有前十八次 raw 留存记录：
只移出可由完整原源和全部参数再生的轨道输出，
不改写历史，不移出源码、模型参数、证明或当前输入。

## 1. 明确的六项建议移出清单

本次已逐字核对六份现有文件与固定公开提交
ca7a460703a86324926b4ab69144428a578a1f47 相同。
全部路径均相对于本课题目录。

| 原路径 | 字节 | SHA256 |
|---|---:|---|
| notes/alternative-hermite-k045-v04-s065-m96.json | 408868 | 4129371ee0d8a1117b14280139063fbec522b1f618637f3729cf43b09ec4dde3 |
| notes/alternative-hermite-k045-v035-s065-m96.json | 408718 | 55016cf545e88d49958e6e2ffe3b36f1cc577b27088125be446e8ff2f582351e |
| notes/alternative-fast-m96-v04-s05.json | 397932 | e34d578cbe36bc71c1a273aaaae6cc732c62927125f7711086bab23e6d2fff05 |
| notes/alternative-fast-m96-v035-s045.json | 397820 | 71185a4d494c7e9dcc807f00f15cff43c96c00d5492dfc8e3e412fc5748555aa |
| notes/alternative-fast-A041-m96-v035-s045.json | 397291 | f924ce876cf00447e299624ff3f56d4f71f5e834485b195209d365bc73f0c8e7 |
| notes/alternative-fast-m64-v045-s06.json | 265587 | f618367980036799b6f45a9e7c99d318947181672e820fdbf02fe7a5ee9b4acc |

原 raw 共 2,276,216 B。
这些文件的已核结构都明确含生成的 rows、coefficient_states、
final_coefficients；并非按扩展名把未知 JSON 认定为 raw。

[独立紧凑留存记录](../computations/resume-20261126-legacy-six-open-trajectory-retention.json)
保存各文件全部其他原顶层字段、完整 config、全部原源码 SHA、
原首末完整 row、轨道状态数和末系数个数、完整再生 argv、
固定恢复提交及 blob SHA。
不把完整系数轨道换名为“参数”再次入库。

准备时观测到的 HEAD 为
a4e081b9509fd211644ea227ba87403ca7ea1275，
课题当时受跟踪文件为 199,607,565 B；
这是该时点的文件元数据，不冒称并行提交后的最终容量。
root 普通应用前后仍按实际树计数。
紧凑 JSON 为 44,280 B，加本说明后净释放超过 2.2 MB。

## 2. 完整原生成源码及参数全部保留

三件源码均继续留在原路径，逐字 SHA 与原报告记录匹配：

| 源码 | 字节 | SHA256 |
|---|---:|---|
| computations/alternative-controlled-profile.py | 7561 | 0af61a3bfccf093bfe6c255f864c658c37119b890f362d5d2e16429d2969e430 |
| computations/alternative-outward-probe.py | 7708 | cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb |
| computations/alternative-fast-profile.py | 5644 | d6e0515c179a1e96ff2507e4fb5c8e3974ca170a0821af7e0441c7564cc0cc76 |

两份 Hermite 均为原解析 core 出发的独立计算，
A=.38、M96、N1536、S=.65、k0=.45，
速度分别 .4 与 .35。
四份 fast 同样各从源码内完整解析 core 出发，
全部 A/M/N/v/S/power/rtol/maxstep/steps 等原字段
都保留在 JSON 中。
六份都没有外部初轨道输入、restart 或被删祖先依赖。

每项重建 argv 是从已保存完整 config 和逐字未改的原源默认值
明确构造的可执行命令；
原报告未保存原始 shell argv 字符串，因而不冒称恢复了那条逐字命令。
科学参数不靠文件名推断。
NumPy/SciPy 和单线程 BLAS 设置由原源保留；
旧 Python/NumPy/SciPy 版本、OS 退出码和 Actions run 号未记录，
仍保持 null，不虚构。

未来如需重算，只能在本公开仓库 Actions 的隔离 scratch 中执行，
输出 raw 留在 runner。
计时字段和浮点库版本不同可能改变逐字输出 SHA；
需要准确原字节时应使用下一节的固定历史恢复，
不能把新输出的近似值当原文件。

## 3. 固定原字节恢复

六份都已用固定 commit 的 Git blob 读取并与现存完整原字节相等比较。
固定历史提交不需要改写，仍可按原路径恢复。
例如：

~~~sh
git show ca7a460703a86324926b4ab69144428a578a1f47:topics/visible-flex-larger-amplitude/notes/alternative-fast-m96-v035-s045.json > /tmp/alternative-fast-m96-v035-s045-original.json
~~~

先核第一节所列 SHA256，再把历史消费者的输入路径显式指向 scratch。
完整六个恢复命令的参数数组和各 blob SHA 在紧凑 JSON 内。
准备时另在 geometry 的 retention-originals-m96-six scratch 目录
保留了六份逐字副本；
它们没有通过 connector 上传，也不提交到 Git、Release 或 artifact。

## 4. 已有结论与失败范围不变

下表所有数值只从旧 JSON 标量字段复制，没有科学复算。

| 旧轨道 | 原 reached / target | 原样本最大度量误差 | 原状态 |
|---|---|---|---|
| Hermite M96、v=.4 | .65 / .65 | 8.272225127115007e-10 | success |
| Hermite M96、v=.35 | .65 / .65 | 1.7125412199447965e-11 | success |
| fast M96、v=.4 | .5 / .5 | 3.815489553193885e-7 | success |
| fast M96、v=.35 | .45 / .45 | 4.7719383999833553e-11 | success |
| fast A=.41、M96、v=.35 | .45 / .45 | 1.6505043998193969e-9 | success |
| fast M64、v=.45 | .57 / .6 | .0001297447614596603 | 原真实 domain 失败 |

最后一份的原完整状态为
FloatingPointError('domain at s=0.5775, margin=-3.53068173612')。
其实际保存最后径向点是 .57，
不能把报错尝试点 .5775 或目标 .6 当成已到达场。
全部旧 status、calls、seconds、样本曲率/裕量和其他标量
都在紧凑记录中原样保留。
清理没有把该失败隐藏为 success，也没有重新运行失败步。

这六份都是有边界开放前缀的数值轨道。
样本误差、样本曲率或记录的 success 均不等于
闭曲面、全域 reach、20% 握持幅度、严格存在或完成的固定参数精化。
各 profile 的参数不同也不构成同一个固定度量的加密链。
原 notes 中的数学正文和数值解释继续保留。

## 5. 依赖范围的实际检查

针对六个完整 basename 的定向文本搜索，
当前本课题 scripts/ 与 computations/ 中没有命中；
因此本次没有发现当前完整 R690/mean/Haar/deep/SO3、
固定矩 Q、R696 求解、准备脚本或活动参数引用这些原输出。
当前 reference、完整载体、准确模型参数和待跑 source/argv 均不在清单中。

完整本课题 notes 搜索仍找到七个历史消费者记录，
没有删除或改写它们：

- geometric-core-screen-fast035-m96.json；
- alternative-turn-fast035-flat005-m96.json；
- alternative-flat-fast035-m96-turn-budget.json；
- alternative-flat-fast035-m96-width01.json；
- alternative-flat-fast035-m96-width015.json；
- alternative-flat-fast035-m96-width02.json；
- alternative-flat-hermite045-040-065-m96-width01.json。

每个被移出文件究竟对应哪些历史引用，
已逐项保存在紧凑 JSON 中。
旧消费者若要重读完整系数，必须先按固定 commit 恢复至 scratch；
本次不声称所有旧消费者已“无引用”或自动重跑成功。

本次 sparse 工作树中未检出的其他课题或 workflow 内容，
没有冒称全部扫描过。
检查对象明确是本课题当前源和参数及其历史 notes；
原大文件的可重算性还由完整源码、config、无外部初输入
及固定历史逐字核验共同建立。

## 6. 操作边界

本准备只做 JSON 字段复制、长度/字节/SHA、
源码文本/AST 与精确文件名依赖检查。
没有运行轨道、解 ODE、计算新的极值或生成科学证书。
容量记录不新增数学结论。
原证明、源码、参数、运行边界和失败结论均保留。
root 已以普通新提交移出清单中的六条路径并保留本记录，
不改写已有提交，不强推。

## 7. root实际应用登记

2026-11-26 15:28:56 UTC，root在完整基提交 `97d24ef0fc5b4f3ad6fb738f97e9b9cc6e60c153` 上执行第十九次普通移出，操作前整课题受跟踪大小为 199761233 B。六份原raw共2,276,216 B，逐一再次核完整SHA、原非轨道所有字段/config、首末紧凑row、三件全源SHA、固定ca7历史逐字相等、scratch原副本与当前scripts/computations精确路径无引用；没有科学复算。

最终完整留存JSON为 44978 B、SHA256 `a5426b8856f7ad6137d1a32adacd1816607b8bdfd64dd9afd8fd2a2117f8c5dd`，其root_application区分原准备与实际移出。不把未记录的版本/run/OS退出码补成已知，也不改变M64失败状态。六份历史原字节可由固定提交恢复；本条只普通新commit移出当前树，未改历史。所有当前R690、deep、SO3、moment-Q、角向及缓存续算输入保留。最终发布整树大小由正常推送守卫实际重计，后续活动记录增长不回填成此操作前数值。
