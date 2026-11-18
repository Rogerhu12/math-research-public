# 原 native CLI 的四进程分段执行：完整数值字节身份

**范围：执行方式与有限批输出身份。** 本条只将已经完成过的一份
2304 段完整变分批分给四个进程，各进程调用同一个已编译原 CLI。
没有改变 C++、精度、点根、RK、任何浮点表达式、输入状态或容差，
没有新增 H、DN 解或物理候选。正在运行的 35038 仍使用其原来源。

## 原运算如何保留

新增 [parallel_native_batch.py](../scripts/resume_n4_tail/native_extended/parallel_native_batch.py)
只解释二进制协议的整数尺寸和字节边界，数学数据原样复制。
原完整输入的 SHA 为

bd9b1121152881c0ece0d4e28de2a9c660cca3b53fe32f14d3a58439c46abb1e。

每个原 stage 的输入状态、冻结系数、RK 网格与切分保持为同一字节串。
共同数字配置、三角表和原门也逐字复制。第 $k$ 个子进程处理
$k,k+4,k+8,\ldots$；这分散了沿径向不同点根工作量。只有子批段数及
不参与数学的 opaque identity token 改变，输出后恢复父批原 token
和全局段次序。

原 CLI 对每个 stage 独立调用原 vf_run_stage；该调用以该段输入
构造自己的运行器，输出原状态、完整变分与根诊断。分段不改变单段
内部的求和、点根迭代或表达式顺序，也不在 Python 中重新计算或
重编码浮点数据。

原 CLI 二进制始终为

1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94，

原生产 C++ 始终为

e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf。

代码按原全局段序选择第一个 domain failure，保留此前完整输出及该
原错误；工程退出不被当成数值接受。本次实际批全部成功，因此本次
执行的完整字节验证覆盖成功路径；没有声称另外实测了各类损坏输入
或失败分支。无效协议在包装层按工程错误拒绝。

## 唯一完整执行

计划为 n4_work/native-parallel-equivalence-v1/plan.json，SHA
0bcf040ae92c8dec850ed5786bde31648b0e7f6282af519c2e4468b1d8b027fe。
四进程入口的实际 session 为 95657，启动块 3285e2，终态块 9e9b57；
包装层与四个原 CLI 子进程全部实际退出 0。

| 项目 | 实际范围或读数 |
|---|---:|
| 完整原 stage | 2304 |
| 原 $M$ / spacing / 角求积 | 20 / 4 / 512 |
| RK 步总数（既存输入） | 36891，27段含额外 cusp 切分 |
| 全部状态标量 | 96768 |
| 全部原 native Jacobian 标量 | 3870720 |
| 根计数与几何诊断标量 | 16128 |
| 原串行进程 wall time | 392.136659724 秒 |
| 本次并行包装层 wall time，含拆分合并 | 104.92322919600701 秒 |
| 本次两项 wall time 之比 | 3.7373674326344815 |

这两个时间来自不同的实际执行负载，最后一行是单次观察，不是普遍
加速保证。每段 kernel_seconds 也按本次真实计时保存，没有复制旧时间。

## 完整数值身份的只读核对

[compare_parallel_native_batch.py](../scripts/resume_n4_tail/native_extended/compare_parallel_native_batch.py)
实际 5b4f38、exit0，只读取完成的二进制文件与来源，没有调用任何
数学运算器。它核对：

1. 全部 2304 原 stage 输入字节和共同数字配置逐字相同。
2. 输出头、父 token、全局段号、原 status 全同。
3. 全部 state、Jacobian、根调用/更新/fallback 计数以及 minA、minD、
   根残差、literal Jacobian pivot 的字节全同，连同符号零保留。
4. **只排除每个成功段末尾的 8 字节 kernel_seconds**；没有排除任何
   数学输出或条件检查。数值 wire 摘要保存在执行记录中。

完整数据和四个子批留在 scratch；发布件只有源、来源、命令、哈希
与紧凑计数。实际输出、全部子进程记录及先前串行批来源均由
[native_parallel_equivalence.json](../scripts/resume_n4_tail/native_parallel_equivalence.json)
绑定。

## 后续接入与数学边界

该独立包装层接受原 INPUT、OUTPUT 两个参数；额外计划可以通过
明确的 --plan 参数或 VISIBLE_FLEX_PARALLEL_NATIVE_PLAN 指定。
计划分开绑定包装层、原 CLI 和原构建来源。后续 owned manifest
也必须分清这些身份，不把包装层的 SHA 当成 C++ 二进制身份。
每次使用新的输出路径；失败文件保留，成功子批可按明确计划清理，
父批完整输出与元数据仍保留。

本条没有为原固定态降低残差：相同输入与全部相同数值输出仍对应
既存 $1.5211857880292614\times10^{-8}$ 的原残差，超过 $2\times10^{-9}$。
这里只证明这一次有效完整输入的数值身份并说明独立 stage 执行的
保序机制；真实 DN、全 H、前缀联立、闭合和比例仍继续由原程序检验。
