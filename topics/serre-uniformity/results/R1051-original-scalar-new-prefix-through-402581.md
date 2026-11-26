# R1051：原 scalar 新窗口的准确完成前缀至 402581

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

**已核实的有限公开计算。** 在
$$
200000<p\le402581,\qquad p\text{ 为素数},\qquad
p\bmod9\in\{2,5\}
$$
的全部 5372 个素数，原 $f_N$ 和副产物 $g_N$ 均非零。
这里 $p=6N+5$，继续使用原 $E:y^2=x^3-1$、$dz=dx/(2y)$、
$\sigma'(0)=1$ 和无 Gaussian 的规范。
它不是全 $p$ 的单位性定理，也不关闭 Serre 主目标、原同 $h$
筛选、核范数或实际深盘非中心零点。

## 1. 实际执行与准确边界

唯一执行为公开
[run 45869953028](https://github.com/Rogerhu12/math-research-public/actions/runs/45869953028)，
job **140082478470**，名称 original_scalar。
源提交为
[30cecd32f0dac425ed08d6aea9db1a0fb065c3b4](https://github.com/Rogerhu12/math-research-public/commit/30cecd32f0dac425ed08d6aea9db1a0fb065c3b4)。

请求的原集合是 $200000<p\le500000$、$p\bmod9\in\{2,5\}$，
共 7878 个素数。runner 在 2026-11-26 17:42:25 UTC 输出 CONTRACT，
在 18:00:25 UTC 输出 SUMMARY 和预算回执；job 全部步骤成功。
准确状态为 **budget_prefix_no_f_zero**：

| 字段 | 实际值 |
|---|---:|
| 完成数量 | 5372 |
| 首个完成素数 | 200003 |
| 最后完成素数 | 402581 |
| 完成列表恰为请求列表前缀 | true |
| 全请求区间完成 | false |
| 新 $f_N$ 零值 | 无 |
| 新 $g_N$ 零值副产物 | 无 |
| 下一个未完成素数 | 402593 |
| 重算旧完整 scalar 输入 | 无 |
| 除以 $p$ | false |
| 声称全素数单位 | false |

达到预算时，402593 尚未形成一个完成行；后继从该回执给出的
素数续算，不重新计算已完成的 5372 行。
没有新 $f_N=0$，所以“首次零值的独立原 $z$ 核准”未触发；
不能将未触发的核准写成已执行。

## 2. 消费已经证明的原算法

本次直接使用 R698/R706 已证明的
[R698_fast_scalar_window.py](../scripts/R698_fast_scalar_window.py)，
不再证明或重跑旧 $p\le200000$ 窗口。
每个新 $p$ 的完整指数递推
$$
wT'=T(H-1)
$$
均由 producer 检查；最大实际除数严格小于 $p$，
首个被排除的 $H$ 分母恰为 $p$。
consumer 对每一行都检查这两个事实及完整递推检查状态，
再记录同一原 $f_N,g_N,A_p,A_{p-3},C_p,C_{p-3}$ 与系数哈希。
没有交换 sigma 规范、有限截断或原标签。

若出现新的 $f_N=0$，请求规定使用已经存在的
[R698_verify_original_z.py](../scripts/R698_verify_original_z.py)
核原 Weierstrass 能量方程、sigma 方程与全部对应标量后停止。
本次没有遇到该分支。详细预先声明见
[方法记录](../notes/2026-11-27-original-scalar-obstruction-new-window-method.md)
在源提交中的 v1 版本。

R706 的旧 $g_N=0$ 素数 137147 完整保留；本结果没有撤销它。
本次所有素数严格超过 200000，属于一个不相交的新集合。

## 3. 来源与复核哈希

所有哈希均来自公开 stdout 的 CONTRACT、SUMMARY、OUTPUT_RECEIPT。
只保存必要回执，不提交可重算的完整行或数组。

| 对象 | SHA-256 |
|---|---|
| v1 请求 | 69115d1124c5aa08422daa6bab027b3e0b460cc1ea45f5e448f33782b35535b4 |
| 全请求素数列表 | c4ecbe6ed37926adf83c10b8b807da64deae6416ee71d56f4f7653e8808e3a4c |
| 实际完成素数列表 | fe8a7b80570207837336360f880aaa93e15ee3de45b2e318ecb2d03e1874557c |
| 全部完成行 | a344d9e303f973ac1d7a49c925519a1eb3b3f18ce7f1fd273f50ba5d525f8eee |
| runner 输出 payload | 93fe9abf1560f9a24685162e091b96c68f497c516573a7966a673c04bcdb7b78 |
| v1 consumer | f45507577c34f944f7d2d00653fe2276c175569286e102daed2be9d16447689e |
| R698 fast 算法 | 31024ef6308f251ff5c6f23650250e49cf10600de9d40f34a6419ea8387f1d9c |
| R698 原 $z$ 算法 | ef33ef0d61b4cf33c0a1fe2a23ce14b57780b5b5b49df9f609dc0e49b1014ac3 |
| v1 方法 | e93fdc0ee9b1cb29b4a2866ad38a59df2e78b89cca85e93c57c98f22e7f1fb2e |
| R706 已完成旧范围 | 87d025a882f1ff541e3cf343f012e1dff7bf463b1c4591410e2d6cdfa21378d7 |
| 根 README | 581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102 |
| 本课题 README | 6ce1403bd2d2587bb9cca70bd0095a1264b1167fe2c4b62f0652ae671e6277a5 |

依赖为 python-flint 0.9.0。payload 大小 2858480 bytes，
仅存于 runner 临时目录；没有 artifact、Release 或提交的 raw report。
公开日志保留进度和上述紧凑回执。

## 4. 预算与继续范围

预先声明总预算 1200 秒，预留 120 秒；
通常算术循环在 1080 秒停止。
SUMMARY 的实际耗时为 1080.022597918 秒，
最终预算回执为 1080.039123160 秒，
within_budget=true。workflow 的 30 分钟外限未被当作完成范围。

因此本次仅新增有限前缀结论。后继 v2 严格从 402593 开始至 500000，
原 scalar 完整输入不重复；原完整 CM 轮廓、实际最低系数和高权
范数的纸面研究同时继续。新局部 CM 核候选的 $p=47$ 诊断
与原 scalar 是不同输入，若使用则单列来源和条件，不能混入本结果。

本次数学程序只在上述公开 Actions 执行。
宿主只处理文件、日志、哈希和提交；读取 stdout 没有重新运行数学。
Serre 主目标仍 OPEN。
