# 第20次容量维护准备：六份旧 M64/M48 独立开放轨道

2026-11-26，Astra-larger-e4e2a2bf-20261126 / solver。

**状态：root已于2026-11-26 17:12:35 UTC实际普通移出下列六份当前raw。** 准备代理只在scratch工作；root逐字核对完整留存后应用，未改历史或执行科学计算。实际应用详情见§7。

按根 README 第 8、15 条及前十九次容量维护的同一边界，
只考虑已识别为生成轨道的数组输出；完整源码、参数、历史身份与原失败结论全部保留。
不是按扩展名删除未知 JSON。

## 1. 固定候选及逐字身份

六份当前字节已逐一与固定公开提交
`1d284f875eb4290b2e99805f08c7ed74ee234f6a`
的相同路径比较，全部逐字相同。
以下路径相对于本课题目录。

| 原路径 | 字节 | SHA256 |
|---|---:|---|
| `notes/alternative-hermite-k045-v04-s065-m64.json` | 290416 | `39b326ad89baee2380216a44f71ec5d3f4d6f5d6a4d9888081fc1db45c7ce931` |
| `notes/alternative-hermite-k045-v035-s065-m64.json` | 290390 | `f2093e89beeed01ae2c4f7292153a0cc216edc96b7f0ed438aa5e54e8f62adcc` |
| `notes/alternative-hermite-k045-v03-s065-m64.json` | 290313 | `f48663f4699242c648dd9ce5f957f4d549caae99c8e1e050e18c2c1d569a9f33` |
| `notes/alternative-fast-m64-v04-s05.json` | 279561 | `1a00ae000c29a1c14ca41248ddc838fae8cd5a38b9cd4d477b51ef2447907b23` |
| `notes/alternative-fast-m64-v035-s045.json` | 279439 | `4c878e1d2ae79a43ac9fa9bb90f413630ce6ad07d035ceeabd89b3a1e9c60aa8` |
| `notes/alternative-fast-m48-v05-s0667.json` | 183341 | `4f95fe9edbd11a5191f4fa43c2f720bf26ecd04da74c55fc67554c45de71c90f` |

候选原 raw 共 **1,613,460 B**。
上述固定提交的整课题受跟踪大小为 **198,875,141 B**；
这只是准备时固定树的元数据，不冒称并行新提交后的最终容量。
root 应在真正应用时按最新树重新计数。

[完整紧凑留存 JSON](../computations/resume-20261126-legacy-six-open-m64-retention.json)
为每项保留全部原顶层非轨道字段、完整 config、完整首末 row、
生成数组的元素数量、准确 blob 与恢复提交、全部再生 argv、
当前源/参数及历史 notes 的精确路径搜索结果。
五份 M64 各有 41 个完整系数状态及 194 个末系数；
M48 失败轨道只有 34 个状态及 146 个末系数。
这些完整系数数组不换名为“参数”重新提交。

`alternative-hermite-k045-v025-s065-m64.json` 不在本清单。
旧 double-boost 留存链仍明确依赖该祖先，本次没有必要扩大这条恢复责任。

## 2. 三件完整原生成器与全部独立输入

三件源码当前与固定历史逐字相等，且 SHA 与原报告执行源字段准确匹配：

| 完整源码 | 字节 | SHA256 |
|---|---:|---|
| `computations/alternative-controlled-profile.py` | 7561 | `0af61a3bfccf093bfe6c255f864c658c37119b890f362d5d2e16429d2969e430` |
| `computations/alternative-outward-probe.py` | 7708 | `cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb` |
| `computations/alternative-fast-profile.py` | 5644 | `d6e0515c179a1e96ff2507e4fb5c8e3974ca170a0821af7e0441c7564cc0cc76` |

三份 Hermite 都从完整原解析 core 独立出发：
`A=.38, M=64, N=1024, S=.65, k0=.45`，
速度分别 `.4/.35/.3`，其余 `rtol=1e-11, maxstep=.00025, steps=40`。
没有 `--input`、continued law、restart 或外部祖先数组。
完整原源中的初值、Hermite law、DOP853 与
`atol=rtol*.01`、`max_step=min(maxstep,(right-last)/2)` 全部保留。

三份 fast 同样从完整解析 core 独立出发。
M64 两份分别采用 `(v,S)=(.4,.5)`、`(.35,.45)`，
`A=.38, N=1024, power=1, rtol=1e-11, maxstep=.00025, steps=40`。
M48 采用 `v=.5, S=.6666666666666666, N=768, power=1,
rtol=1e-10, maxstep=.0004, steps=40`。
三份都没有 `end_s` 或 `coast_at` 覆盖，
原 FastProbe 以完整 FastOutwardLeg 和 `s_end=S` 定义目标。
源内 `amax`、初始加速度、coast 默认值的生成规则与原 config 字面值均保在 JSON 中。

每项完整 argv 由保存的 config 和逐字相同的原源码明确构造，
不是凭文件名推断参数，也不冒称原报告保存过逐字 shell 命令。
浮点参数用可往返原 binary64 的十进制字面串传递。
三源依赖 NumPy/SciPy，原单线程 BLAS 设置仍在源内。
旧 Python、NumPy、SciPy 版本、OS 退出码和 Actions run 号均未记录，
本次保留 null，不以报告 `status=success` 编造进程退出码或 Actions 编号。

## 3. 准确原字节恢复和完整再生

六项均可用第1节同一个固定 commit 的原路径恢复。
例如：

~~~sh
git show 1d284f875eb4290b2e99805f08c7ed74ee234f6a:topics/visible-flex-larger-amplitude/notes/alternative-fast-m48-v05-s0667.json > /tmp/alternative-fast-m48-v05-s0667-original.json
~~~

先核第1节准确 SHA256，再把历史消费者的输入路径显式指向 scratch。
全部六项的 `git show` 参数、各 blob SHA 和恢复目标都在紧凑 JSON 中。
准备期间还将逐字原件复制到 solver 的 `retention20/originals/` scratch 目录，
只作本地字节留存，未传 connector、提交 Git、Release 或 artifact。

如需科学再生，只能在本公开仓库 Actions 的隔离 scratch 中执行。
例如 M64 Hermite `.35` 的完整有效参数命令为：

~~~sh
python topics/visible-flex-larger-amplitude/computations/alternative-controlled-profile.py \
  --A 0.38 --M 64 --N 1024 --v 0.35 --S 0.65 --k0 0.45 \
  --rtol 1e-11 --maxstep 0.00025 --steps 40 \
  --out /tmp/alternative-hermite-k045-v035-s065-m64-recomputed.json
~~~

M48 fast 原失败分支的完整有效参数命令为：

~~~sh
python topics/visible-flex-larger-amplitude/computations/alternative-fast-profile.py \
  --A 0.38 --M 48 --N 768 --v 0.5 --S 0.6666666666666666 --power 1 \
  --rtol 1e-10 --maxstep 0.0004 --steps 40 \
  --out /tmp/alternative-fast-m48-v05-s0667-recomputed.json
~~~

其余四份全部 argv 在 JSON 中逐项保留。
重算计时、库版本和浮点轨道可能改变输出字节；
需要原准确 SHA 时用固定历史恢复，不能把近似重算结果冒充原字节。
新 raw 仍只留 Actions runner。

## 4. 原结果及失败边界完整保留

下表只抄录原 JSON 标量，没有重跑轨道或计算新科学量。

| 旧轨道 | 原 reached / target | 原样本最大度量误差 | 原状态 |
|---|---|---:|---|
| Hermite M64，`v=.4` | `.65 / .65` | `1.2399691973197235e-7` | success |
| Hermite M64，`v=.35` | `.65 / .65` | `2.3092725509599177e-9` | success |
| Hermite M64，`v=.3` | `.65 / .65` | `1.0478506951017152e-11` | success |
| fast M64，`v=.4` | `.5 / .5` | `7.68717663701679e-6` | success |
| fast M64，`v=.35` | `.45 / .45` | `2.004603871785804e-8` | success |
| fast M48，`v=.5` | `.55 / .6666666666666666` | `0.00021536291086099446` | 原 domain 失败 |

最后一项原完整状态是
`FloatingPointError('domain at s=0.5648, margin=-0.513286840939')`。
实际保存末点是 `.55`，不能把报错尝试点 `.5648` 或目标值当成已到达场。
该失败、calls、seconds、原样本曲率与裕量以及全部其他非轨道字段原样留存。
其失败不推数学不存在；清理也不把它隐藏为 success。

六份全是有边界的开放前缀。
样本小误差、样本曲率或报告 success 不给出闭曲面、全域 reach、
20% 整像握持幅度、严格存在或同固定参数的完成精化。
不同 profile 之间也不冒同固定度量的精化链。
原 [几何筛查说明](geometric-prefix-phase-screen-summary.md)
及其他旧数学/数值说明、原消费者记录全部保持。

## 5. 实际依赖核查范围

对六个完整 basename，当前本课题 `scripts/`、`computations/` 精确文本搜索均无命中。
因此未发现当前已刊求解源或完整计算参数直接引用这六条路径。
这是限定范围的实际搜索，不冒称对所有其他课题、动态构造路径或未检出 workflow 作了全仓证明。

历史 notes 中仍有以下消费者：

- `geometric-core-screen-hermite045-v035-s065-m64.json`；
- `geometric-core-screen-hermite045-v03-s065-m64.json`；
- `geometric-alternative-fast040-width015.json`；
- `alternative-flat-fast035-m64-width02.json`；
- `alternative-flat-fast035-m64-width03.json`；
- `geometric-alternative-fast035-width020.json`。

每项与哪份候选对应已在 JSON 逐条保留。
这些旧引用本身没有删除或改写；
未来消费者如需原完整轨道，必须先按固定历史恢复并显式接入 scratch 文件。
不能把删除后的旧 raw 链接称为当前路径仍然存在，
也不声称那些旧消费者已自动重跑成功。

## 6. 本次已做和待 root 应用的边界

本准备仅做字节/长度/SHA 与 Git blob 相等检查、
完整 JSON 非数组字段复制、原源 AST 解析和精确文件名搜索。
没有导入原科学模块，没有解 ODE、计算新极值、重跑旧结论或生成证书。
紧凑 JSON 的 `root_application` 现为 null、`current_files_removed=false`，
准确反映尚未应用；root 应在普通移出时另记实际提交前后容量与核对状态。
任何已推历史保持，不强推。

## 7. root实际应用

2026-11-26 17:12:35 UTC：root完整读本文及六项紧凑字段/全部argv，逐一核原字节、固定1d284历史、scratch原件、三完整source和原所有非轨道字段/首末row/数组计数相等；精确basename重搜当前scripts/computations均无引用。真实普通移出6项共1,613,460B；保v=.25祖先、全部原源/配置/旧失败和消费者，未重做任何科学计算或改历史。准备段的“尚未应用”描述属于原准备时点；正式JSON现current_files_removed=true及root_application记录此次实际应用。应用前当前题字节为198911408；应用后当前树容量见正式JSON，推送后以实际Git树为准。
