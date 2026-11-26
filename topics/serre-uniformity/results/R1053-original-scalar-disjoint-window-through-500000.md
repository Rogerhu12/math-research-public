# R1053：原 scalar 不相交新窗口完整完成至 500000

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

**公开有限计算已完整核实。** 在
$$
200000<p\le500000,\qquad p\text{ 为素数},\qquad
p\bmod9\in\{2,5\}
$$
的全部 **7878** 个素数，原 $f_N$ 与 $g_N$ 均非零。
它由 R1051 已完成的 5372 行和本次严格不相交的 2506 行组成。
没有重算旧 $p\le200000$ 窗口或 R1051 的完整行。
本结论只覆盖这个有限集合，不证明全素数单位性或 Serre 一致性。

## 1. 本次实际续段

公开 [run 45874715945](https://github.com/Rogerhu12/math-research-public/actions/runs/45874715945)，
job **140098765505**（original_scalar），全部步骤成功。
源提交为
[7e47699cd195f7fd70eca38a2f9f1011a636a090](https://github.com/Rogerhu12/math-research-public/commit/7e47699cd195f7fd70eca38a2f9f1011a636a090)。
execution_id 是 scalar-obstruction-20261127-v2。

它严格从前次真实回执的 resume_lower=402593 开始，
上界仍为 500000。producer 同时强制已完成截止 402581，
所以不能把旧完整 scalar 行重新纳入。

| 项目 | 真实回执 |
|---|---:|
| 请求数量 | 2506 |
| 完成数量 | 2506 |
| 首个完成素数 | 402593 |
| 最后完成素数 | 499979 |
| 完成列表恰为请求列表前缀 | true |
| 整个请求区间完成 | true |
| 状态 | complete_no_f_zero |
| 新 $f_N$ 零值 | 无 |
| 新 $g_N$ 零值副产物 | 无 |
| resume_lower | null |
| 原 $z$ 零值复核 | 未触发 |
| 重算旧完整 scalar 行 | 无 |
| 除以 $p$ | false |

原模型、sigma 规范及算法完全沿 R1051：
$E:y^2=x^3-1$，$dz=dx/(2y)$，$\sigma'(0)=1$，无 Gaussian。
每个新行都核完整指数递推、最大除数 $<p$、
首个排除的 $H$ 分母为 $p$，并记录原系数和输入哈希。
没有新的 $f_N=0$，故独立原 $z$ 零值核准没有触发；
不能声称它在本次另跑了 2506 次。

## 2. 与前缀合并的依据

[R1051](R1051-original-scalar-new-prefix-through-402581.md) 的请求集合
原本就是本篇全部新区间；其真实完成列表是从 200003 至 402581
的准确前缀，完成 5372 行，并给下一输入 402593。
本次 consumer 接受这个确切续点，且回执确认自己的完整请求全部完成。
因此两段没有重叠、没有漏掉中间的合格素数，
数量为 $5372+2506=7878$，与原完整请求数量一致。

两段的 $f_N,g_N$ 零值列表都为空，所以得到标题中的完整有限结论。
R706 旧窗口的唯一 $g_N=0$ 素数 137147 保持原结论；
它未被本次重新计算，也不与本篇新区间结论冲突。

## 3. 本次必要回执和来源 pins

| 对象 | SHA-256 |
|---|---|
| v2 请求 | a1e4af4b4808d47588b3f748b5ab61a9b4cb51cc786c27ac090bf7df6b1c7abd |
| 请求列表＝完成列表 | e7256110dcc5bc493c4fcfb6bff6fcd6783a6bd99ab20f65dd739d5275272a10 |
| 全部完成行 | 7f5bf714ce7422381d5197544f7b164b528daa93a7f73475c5ab5cdb98d55953 |
| runner payload | c5d9d1964d9ac220ff7a2354c85d9788ba4f1df3c5f6bf60d8635e7b08603102 |
| v2 consumer | a99fe1212176daa4b0a9da5a7874ceb7ee1234bade567523e764d043ee5de312 |
| v2 方法 | d2d0644bcad18b2285a290ae506c4d6e6790f46ca2de22c15d0c04dc3307ed4c |
| R698 fast 算法 | 31024ef6308f251ff5c6f23650250e49cf10600de9d40f34a6419ea8387f1d9c |
| R698 原 $z$ 算法 | ef33ef0d61b4cf33c0a1fe2a23ce14b57780b5b5b49df9f609dc0e49b1014ac3 |
| 根 README | 581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102 |
| 本课题 README | 6ce1403bd2d2587bb9cca70bd0095a1264b1167fe2c4b62f0652ae671e6277a5 |

依赖为 python-flint 0.9.0。
源提交中的 [consumer](../scripts/original_scalar_obstruction_new_window.py)、
[请求](../notes/original-scalar-obstruction-new-window-request.json) 与
[方法](../notes/2026-11-27-original-scalar-obstruction-new-window-method.md)
保留精确输入。复核本次版本须使用上方的源提交和哈希，
不能默认以后 main 上的同名文件仍为同一版本。

payload 1337545 bytes，只保留于 runner scratch。
没有 artifact、Release 或提交的可重算完整行。
同一个 job 中另有一次新 $p=47$ CM 核候选诊断，
它不属于这里的原 scalar 素数列表，结论另行登记；
没有计算 $p=47$ 的旧 $f_N,g_N$。

## 4. 实际预算和后继

总预算 1200 秒，预留 120 秒；本次未用满算术预算。
SUMMARY 耗时 895.286468547 秒，
最终 BUDGET_RECEIPT 为 **895.294074836 秒**，
within_budget=true。
这包括同一 job 中的新局部候选诊断。

至 500000 的声明新区间已经完成，没有待续前缀。
不再自动重开这个窗口；后继研究原全称单位性、真实完整 CM
消去值和 O0 全局覆盖。有限非零值不能替代这些证明。

全部数学程序只在上述公开 Actions 执行。
宿主仅处理文本、日志、哈希及提交，没有运行数学。
Serre 主目标仍 OPEN。
