# 全状态 universal P1：按真实缩放权分块的公开计算接口

日期：2026-11-14。独占源码 `scripts/literature_total_P1_scaling_blocks.py`。这是针对两状态实际任务 43637269935 的具体性能修正；该任务在 480 秒时仅完成 33/72 列，尚未产生响应空间上界、匹配或分离证书。本文不把资源退出当成数学阴性，也不原样加大旧任务预算。

## 1. 新目标与有限范围

沿用 R90/R91/R94，令 $\mathcal R_*$ 为全部 reciprocal 状态对完整第三控制的两个 P1 模式响应之和。本次处理

$$b_n\stackrel{?}{\in}(\mathcal R_*)_n$$

的真实整数权块，其中 $b$ 为已经绑定的标准有理端点基准加完整常态目标。两模式仍使用同一组实系数。默认从实际原式权清单的最高候选权向下选至多三块，首轮总时间 240 秒；不构建一个混合 72 列或 252 列的目标。

物理二阶空间的同权七基为

$$r_0;\quad r_1,s_0;\quad p_0,s_1;
\quad p_1-t_1/4;\quad p_2.$$

相应权为 $-3,-2,-2,-1,-1,0,1$。真实 36 个第三基的权按 R94 逐原式核对。响应各权的原生成列数如下，内部依赖仍待准确处理。

| 权 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 | 0 | 1 | 2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 原列数 | 2 | 8 | 20 | 34 | 46 | 48 | 42 | 28 | 16 | 6 | 2 |

这些同权二阶基仅用于响应线性代数；有符号展开系数最终放进真实第三控制环，不能据此把 bulk 长度改为负。若所有目标块都给出原式成员证书，R91 的七个正完整圈 helper 提供实际 P1 构造的存在性；当前脚本不构造其具体几何路径。

## 2. 原式与来源绑定

输入仍为公开 v2 回执

`notes/actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json`，

157380 B，SHA256 `7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960`，来源提交 `26c3f2c0308d179a094d3967cfb7189db426081e`。

复用已冻结 `literature_full_phase_rational_dual.compile_original_problem`，恢复同一完整常态目标、同一彩色三线性局部式与同一真实五段端点基准；核对全部 152 个原模板 hash、36 个保留基与原始常态/基准 hash。恢复表达式不是重算 v2 的 116 条依赖、旧 C1 商搜索或失败的两个状态成员目标。旧回执已经提供被丢弃第三模板的真实原式依赖和两个非有理端点分量的支付。

所有实际用到的数学源码 byte/SHA 与这一输入回执进入新索引和每个独立块。原始有理基准仍是“原五段式减去已证明可达的原模板线性组合”，不把一个未证明等价的简化式作为新的基准。

## 3. 真实权投影与较小的响应展开

新 `ScalingGrading` 遍历原始表达式树：坐标幂加其次数，输入 $j$ 阶 jet 贡献 $-j$，真正右原函数节点加 1。逐单项分组准确重建原式。这是 R91 的真实 $S_H$ 权投影，不是由 word 代表猜测权。

标准正算子只含三个同权部分：

$$A_{1,0}=-\Phi_{r_0}/8-\Phi_{p_0}/2-\Phi_{p_2}/2.$$

因此目标第 $n$ 块直接由常态原式的第 $n$ 分量，以及每个 $A_a$ 作用于端点第三式的第 $n-a$ 分量构成。没有先展开完整混合响应再丢掉其他权。

旧接口固定 $A=A_{1,0}$；新 `full_response(ring,third,quadratic)` 接受任意上述七基。它是 R78 的准确极化，并利用

$$F-d/2=q\odot\bar q/2$$

预先消去 $q+\bar q$ 替换和重复混合项。若写 $a=A(q,q)$、$c=A(\bar q,\bar q)$，则

$$B_{-4}=
\frac{T(a;q,q)}8+\frac{T(q;q,a)}4
-\frac{A(q,T(q;q,q))}4.$$

第二模式使用同一份原式极化的十个单色第三调用。小人工 toy 将它同时与独立 literal $\mathcal K/\mathcal L$ 公式及旧固定标准 $A$ 接口比较，两个模式均准确同零。真实任务不会再执行该人工参考式。

对中间第三模板可以使用有声 word 改写来缩小替换规模，但会从原式核对差为零。负向值评价和最后正向复核都回到原始模板及原右锚。

## 4. 一个块怎样得到可用结论

每块依次完成：

1. 形成真实投影目标，并先核其余权的原式差为零。若目标的 word 表示为零，仍重新从原始基准/常态公式检查两个模式，才能记为 `target_zero_verified`。
2. 只生成满足 $a+t=n$ 的原响应列，用同一系数空间同时消元两个模式。
3. 对每条丢弃列，从原始第三模板和原始二阶算子重建依赖，两个原式模式均 fresh 同零。这才给出真实响应维数上界 $r$。
4. 若目标属于代表列 span，按原基准和原模板重新构造两个完整模式，fresh 同零才记为 `member_identity_verified`。
5. 若代表余项非零，不宣称数学阴性。对保留的全部 $r$ 列与原式权目标，使用同一实有理 polynomial profile 对、同一右锚作原始 Volterra 值评价。只有控制模秩为 $r$ 且某个 $(r+1)$ 阶增广子式非零，才记为 `nonmember_certified`。若模秩不足或有限点拟合，均记 `undecided`。

正证书的实际控制系数与两个 fresh 原式零 hash 均保存。负证书保存原式 straight-line 身份、全部分母可逆检查、选定行/列、增广矩阵、两个模行列式和真实有理 Cramer 泛函定义；不会把打印的模系数当作有理泛函系数。

默认测试 profile 仍为支撑 $[2,3]$ 上

$$f=[t(1-t)]^8,\qquad
g=f(1+2t+3t^2+5t^3),\qquad t=\xi-2,$$

查询点 $t=j/49$，$j=1,\ldots,48$；素数 2147483647。所有列、所有点和两个模式使用同一对 profile，值计算不用 word 表达式。

**这个负证书的范围与 R87 不同。** 这里评价的是算子的缩放权投影。一个块的真实非成员证明 $b\notin\mathcal R_*$，再由 R91 排除 universal 正状态恒等式；它没有证明同一固定 profile 上未投影的完整 P1 不可解。权投影在真实函数层可能需要多个缩放后的输入，不能直接套 R86 宣称一个合法三矩圆已被排除。

## 5. 每块保存、异常保留与后续接续

主参数 `--output` 是索引文件。每个完成块另写一个文件，例如

`total-P1-blocks-weight-p2.json`、`total-P1-blocks-weight-p0.json`。

每完成一块立即先保存该块完整回执，再更新索引中的长度/SHA。随后的资源退出、异常或未定块不会抹掉已完成块。当前未完成块另存部分进度，明确 `not_a_negative_mathematical_result`。

`--resume-index` 可读上一公开输出目录中的索引及独立块。恢复前检查源码集合、问题身份、每块长度/SHA/完成状态；继承块以原字节复制到新输出目录。已经完成的块不重新计算。仍要恢复同一绑定原始公式以检查问题身份和处理新的权，这一步不重跑旧块的研究计算。

默认遇到一个 `undecided` 或 `nonmember_certified` 即结束本次有界 scope；不会自动盲改素数、profile 或预算。若只完成若干正块，索引列出 `remaining_unpaid_weights`，`all_blocks_membership_verified` 保持 false。

每块默认不超过 300000 B，索引默认不超过 300000 B；总已发布文件保留 4500000 B 的硬输出上限。资源上限为 240 秒、RSS 软轮询 1024 MiB、至多三新块、60 万 coefficient nodes、20 万 profile atoms、12 万表达式项、每个 normalizer 100 万调用、消元有理数 16384 bits；模 polynomial 次数 256、每块 2000 万操作。时间和内存是已公开的轮询门，不伪称操作系统隔离或区间证书。

## 6. 命令与开发检查

本地仅执行过小人工接口检查：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_total_P1_scaling_blocks.py \
  --toy-only \
  --output topics/visible-flex-new-mechanism/notes/literature-total-P1-scaling-blocks-development-toy-20261114.json
```

首个真实任务只在本公开仓库 Actions 中执行：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_total_P1_scaling_blocks.py \
  --max-seconds 240 --max-blocks 3 \
  --output "$OUT/total-P1-blocks.json"
```

后续可在保留前次索引和块文件的前提下用 `--resume-index` 继续；也可明确指定新的权，例如 `--weights=-1,-2`。实际入口同时要求 `GITHUB_ACTIONS=true` 与 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。

人工 toy 覆盖真实权重投影/重建、微分和右原函数权、八个二阶基的权、紧凑两模式与独立公式一致、252 列分块计数，以及全秩/秩不足/零维的有理模分离界限。没有在本地调用 `compile_original_problem`、评价研究 profile、积分几何或优化候选。

无论随后是否完成全部成员块，$P_0$、完整第四 ruling、高阶与收敛，以及主课题的闭嵌入、reach 和宏观位移仍未由本接口支付。
