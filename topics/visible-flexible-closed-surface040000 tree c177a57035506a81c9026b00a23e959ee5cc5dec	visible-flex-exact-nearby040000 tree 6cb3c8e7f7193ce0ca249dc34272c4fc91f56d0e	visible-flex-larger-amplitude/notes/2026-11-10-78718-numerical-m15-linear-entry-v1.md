# 新 M15/W15/N512 真 DN 延拓联解入口 v1

作者：`/root/numerical_recovery`。状态：**源码与纯输入已冻结，待完整独立审查；没有启动新 BVP、DN 或候选计算。** 这份入口不修改 root02、旧独立 M14、旧 matched M15、旧 linear pilot 的任何源码或运行文件。

## 1. 为什么下一步是这个计算

本轮 M14 已有真有限联解，但其实际共同 prefix 对最终精确桥目标有严格轴点下界 $>7.74147506471938\times10^{-8}>2\times10^{-9}$，见本题 `2026-11-10-78718-numerical-common-axis-lower-v2.md` 及独审。只加径向节点、收紧 BVP tol、提高角求积或缩小区间上界，都不能改变这一张已定 prefix 的下界。

固定状态诊断见 `2026-11-10-78718-numerical-fixed-state-projection-analysis.md`：N512→2048的原 RHS 差在选定点上约$10^{-15}$；真正的 Fourier 速度截断贡献明显，而固定曲线的 G 不随速度投影升阶消失。旧 M15 仿射 predictor 已展示较小 sampled metric，但未经真实尾联解；旧直接 M15 和 M16 warm 大跳也未取得完整解。故选取可解释的小步 **M15/W15/N512**，用已经明确审过的 matched M15 初猜与局部真 DN warm，并将每个外部 H 跳跃交给有界真实 DN 延拓。

实际设置：M15、prefix与tail角求积512、prefix audit1024、原BVP tol$2\times10^{-9}$、BC$10^{-8}$、physical BC$2\times10^{-11}$、max_nodes8000、原6 GiB DATA每进程和Node1536 MiB。46个状态、15个自由参数；W15由原 `power2_weights(15)` 逐字算法定义，最大权2048。保持原物理 $g$、profile、warp、cut、tail背景、depth12/parts8/steps32、36轮、原root floor与线搜。

最终 CSC 容器在6599节点约391.0 MB，在2633起始节点约156.0 MB，max8000约474.0 MB；均不含LU、Jacobian批量和Node堆。它比直接跳M22的相应829.5 MB矩阵更温和，但此估算不是峰值或收敛保证。是否启动、何时与现有独立进程串并行，由root按真实可用内存和独立审查结果决定。

## 2. 精确种子与旧结论的边界

下列旧字节仅在当前checkout读入，未冒称恢复旧process。

| 输入（均在notes） | bytes | SHA-256 |
|---|---:|---|
| `2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz` | 27524 | `cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc` |
| 同stem `_coeff_00.npy.gz` | 4174602 | `afde04de0544743ee695ce539abcc91116b142ff3aaae3d3fbd88d34fb3a789f` |
| 同stem `_coeff_01.npy.gz` | 1467096 | `f988042717251970e96fdd47eb9f4dc03475c55f9772c339f81c319b2e554f2f` |
| 同stem `-preparation.json` | 50218 | `31bc073433407e02edb11ec7ea41478195b46d95de1bb73d04b864e56c40a358` |
| `2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01_tail_0001.json.gz` | 272279 | `6f4de10c22fc05cedc87994c274c3643b5390add7bfe0ca71001e02a440a7a86` |
| `2026-11-09-db6f-root-matched-cut-observed-execution-01.json` | 6034 | `1f7a7290c5c65a9f73531cd0edddf8f15b0290477be7d0b74eff9a3d5ba57334` |

旧 prefix 必须保持 `UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS`、solver_success=false、2633节点；保存的完整46维有限PP和15个参数都重新核。它来自旧已审 affine predictor的全局Z-only quintic校正，原preparation仅作为来源，不是新联解结果。其旧N512 prefix配置与原固定物理字段逐项同M14祖先。

旧首DN是**原N256的局部真成功**，residual$1.2533744091676813\times10^{-9}$、705 Jacobian、audit=false，不能算新N512成功。其旧完整matched run在第二真DN失败，虽然原root工具 `ff466f` exit0（旧主程序捕获异常），mathematical_success=false；新输入门对此硬钉。旧响应的705Jacobian不会预填新缓存。

纯PP检查中旧prefix端点与此真实首请求H的最大差实际为0.0，但新程序不把这件偶合当成普遍roundtrip等价门。若新实际请求与种子标签不同，必须先做原false/false bootstrap再真实推进；若相同，直接按原请求flags做真实bootstrap。成功完全由新实例实际响应支付。

## 3. 从已审控制 v2 到新 N512 身份的精确变更

祖先 `db6f-prefix-tail-linear-continuation-client-v2.py` SHA `6d278d78e275df2e0e66db3eb0edb592321fecc22c1c229eacd53f5869166d15`；全文审查见 `2026-11-09-db6f-tail-review-linear-dn-implementation.md`。新的 `78718-prefix-tail-linear-m15q512-v1.py` 保留 Coordinator、完整trial分组分类、缓存、预算、日志与last-good语义。

明确变化只有新schema/文件身份、运行quad=512、旧warm config和resolved parameters比较时仅容许**旧256→新512**这一已声明数值变化，及五个原I/O路径。运行ready参数仍逐值带JSON类型比较，除上述quad和I/O外任何变化都拒绝。原N256响应只由旧schema验证作初猜；新实例先真算N512。

外请求路径仍是

$$H(\tau)=H_0+\operatorname{float}(\tau)(H_1-H_0),$$

到1处直接用原 `goal.copy()`。步长初始与上限$1/8$、最低$1/1024$，最多32次物理请求（含bootstrap、失败及最终验证）、1024逻辑移动，成功不增步。只有已闭、完整分类的原数值失败可折半；其它失败终止该实例。TRACK两个false不是便宜线性响应，仍是真正原DN。最后目标必须完成调用者的真实Jacobian/audit flags；路径secant不能代目标Jacobian。

每个实际packet诚实保留原trial八源并增加本控制器第九源。selector仅把原coupled程序中shared-client导入重定向到这个新控制器；原 `solve_with_actual_tail`、`main`、BVP、BC、core自由参数和最终seam数学源码不改。没有修改旧模块的常量来冒认新M15身份。

## 4. 新完整入口与来源冻结

完整12源清单及全部实际纯证据在 `2026-11-10-78718-numerical-m15-linear-entry-v1-source-manifest.json`，6,237 B，SHA `77e402d9911b2cadf20e2b0004467f1ee8e2ad9ac113b3e13dd3eae66bb55cd8`。核心角色如下。

| 新源 | 角色 |
|---|---|
| `78718-prefix-m15-linear-inputs-v1.py` | 独立新输入门；原97/141/152闭包自验，新的UNSOLVED seed/真warm/完整当前trial依赖、W15与policy绑定 |
| `78718-prefix-prepare-m15-linear-v1.py` | 仅产生新config/policy/launch/准备报告，0候选与solver |
| `78718-prefix-tail-linear-m15q512-v1.py` | 原有界控制的明确N512派生；705目标Jac与原完整响应门 |
| `78718-prefix-flat-linear-m15q512-v1.py` | 只改实际client选择，保原coupled主数学代码 |
| `78718-prefix-spectral-m15-linear-v1.py` | M15/W15 + 原release-LU/direct-CSC；每次inner前后完整typed runtime与物理callback检查 |
| `78718-prefix-audit-m15-linear-v1.py` | 完整M15 finite出口、自己末尾packet、完整原门、root真实自然exit0 |
| `78718-audit-m15-linear-control-v1.py` | 从真实闭packet重新重放完整Coordinator日志，不再调用任何数学solver |
| `78718-prepare-m15-linear-guard-v1.py` | 沿用冻结6GiB资源wrapper及原disk guard，0启动 |
| `78718-check-m15-linear-runtime-v1.py` | 原十函数typed/source与恢复的实际小检查 |
| `78718-check-m15-linear-protocol-v1.py` | 原21类纯抽象控制协议检查，无法伪装成候选fixture |
| `78718-check-m15-linear-entry-gates-v1.py` | 188输入及实际导入30控制函数的typed/source对比和30篡改拒绝 |
| `78718-build-m15-linear-entry-v1.py` | 只写7份另名派生源，逐项替换计数、完整diff/AST账本 |

源生成真实 `dde2e9` exit0。全部差分在 `2026-11-10-78718-numerical-m15-linear-generated-sources-v1.diff`，32,192 B，SHA `c7e6fe79bbbd6861a8751f2b611ba9635033e48b14bd81326ddbb4489a12ebf4`；来源账本22,268 B，SHA `bc74421b42c62996d0dfbef51fa029a9e397304cb8e86083285abeff91e257d3`。三份新手写输入/prepare/closed-control文件完整独立列审，未伪称与旧函数AST相同。新小entry checker也独立列审。

新主driver SHA `33aaef9f6abb70c9e1eab6981d977dc16d5dfdb8740c969d773d6d2cbd9b6e81`；新final auditor SHA `fd41b9ef4c2eea648cbb1ab1c3b638e61bc41d97d99d9213ad0370c042ff147e`；新控制器SHA `3ff7fe2810f15ee7f352d49739a38d5c42bbaf8980ec78c8c66a429faa35624e`；新控制闭审SHA `010acd43f77d1388e53b4ce7b6e8593d9110e07bbc7b38c77a0c26c36dee9d40`。

## 5. 原有限出口和新增控制闭包

保留原物理RMS≤$2\times10^{-9}$、原BC、true outer、首真实目标包、最终自己实际audit包、全部17 cutJets、8 audit数、705 Jacobian、865×30 states及13×30 rawState mirror、物理PP全部46维有限系数、真实完整seam、1024prefix audit与原$64M=960$seam采样。每次真实BVP前后仍检查原十函数typed源码、原/selected/closure及恢复，不把marshal表示偶合当同一性。

延拓可在第一次inner前产生多个物理包，故首binding按**本实例实际last-good引用**定位目标包，不再错误写死`_tail_0001`。它必须是新stem、自有完整九源、精确当次H、Jac=true/audit=false的真实响应；旧种子不支付这一门。

完整finite关闭还逐个读`_tail_0001`到CP实际tail_calls，要求无缺口无额外调用；验证每包的实际config/九源/有限schema与目标标签。以已闭actual响应实现只读RecordedPort，再调用冻结Coordinator重放每个外请求。实际目标从其真正return包取出并与begin/end的digest/flags逐项核。原trial日志决定是否允许已记录的失败折半；所有events（除UTC字符串）必须完全重现，最终last-good引用也必须完全重现。它不构造WeightedTailPort、不启动Node、不进行新的DN或优化；它也不是对连续几何误差的证明。

最终仍要求固定`observer=/root`的真实工具自然exit0以及必需闭合文件。guard/live/程序自身success不能替代自然工具出口。root可以沿当前已实用的持续`tools.write_stdin`监控方式独占工具session，实际返回无session且整数exit后才调用原 `78718-record-root-tool-observation-v1.py`；Unknown handle只可记录unavailable。

## 6. 已实际执行的纯门

完整原argv、初始工具与自然末工具在 `2026-11-10-78718-numerical-m15-linear-observed-pure-executions-01.json`，没有把guard字段当工具回执。

| 真实工具 | exit | 实际范围 |
|---|---:|---|
| `587874` | 0 | 新M15输入门；旧UNSOLVED prefix与真局部warm，0写/0solver |
| `e9cc5a` | 0 | 原21类抽象控制协议；报告4,183 B，SHA `8b75c7687c7e080b8edffd9a3f97119da08f34c37e3b5f81cdff6fd957dee8f7` |
| `202b76` | 0 | 原10 live typed函数/10拒绝/恢复；报告98,318 B，SHA `6a6b8fd079c04d2d4668fcd5b4be57f2e06373ff8f5856d0262c64aa956c0293` |
| `ec266b` | 0 | 完整纯prepare；188 launch/187 policy绑定 |
| `130c00` | 0 | 188输入/30 live control函数/30逐个篡改拒绝，0 port构造；报告51,807 B，SHA `b83056e9f8e940bdd314a2db905c3a8f6d0507a0646a6fb46881ebf3e68c2692` |
| `9e5691` | 2 | 正确拒绝缺未来root出口，0候选成功报告 |
| `3cfc0d` | 0 | 原6GiB资源guard元数据，190绑定，0solver启动 |

当前launch：`2026-11-10-78718-numerical-m15-linear-01-launch.json`，124,724 B，SHA `dbccb1b7892a0cfda626bf2769270b8bd1c9d3e3ef715c7583d8e731f88fee03`；它是结构化metadata，不全文读入对话。prepare报告6,614 B，SHA `0a3a61e3393a631d14c3c5a3dc06fd69fe7357c0debdf9578028a1e6d86d3475`。guard launch55,210 B，SHA `879dc8f158b855e90b33dd0898e4676d7cb9f7a3734b61fde9f2839ef0bc4a0f`。

## 7. 独审可执行检查与未来root启动

以下路径以本题目录为cwd。独审输出请使用自己的全新stem。前两种检查均0solver。

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 scripts/78718-check-m15-linear-entry-gates-v1.py \
 --launch notes/2026-11-10-78718-numerical-m15-linear-01-launch.json \
 --out notes/NEW-INDEPENDENT-CONTROL-IDENTITY.json

/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 scripts/78718-prefix-audit-m15-linear-v1.py \
 --launch notes/2026-11-10-78718-numerical-m15-linear-01-launch.json \
 --mode final --out notes/NEW-INDEPENDENT-NEGATIVE-FINAL.json
```

**未来重计算命令，当前未执行。** 完整审查及资源可用后，由root持续持有实际工具回执；cwd为repo根。原wrapper文件名虽含m14，它只设置资源并调用传入的完整已绑定命令，不选择M或更改数学。

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
 topics/visible-flexible-closed-surface/scripts/78718-run-m14-csc-resource-6g.py \
 --launch topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01-guard-launch.json \
 --observation topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01-guard-completion.json \
 --backup-observation topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01-guard-live.json
```

成功后也只先取得新有限联解；需要自己的末tail、prefix、exact bridge/common graph、连续metric/reach/网格及真正独立完整重跑。**原整图$2\times10^{-9}$门不变**。当前root-only M14后链计划器不能直接冒充M15输入；M15成功后链将另名绑定其新finite auditor、自己CP和九源末包，原存储消费者和数学阈值仍按已审定义保留。
