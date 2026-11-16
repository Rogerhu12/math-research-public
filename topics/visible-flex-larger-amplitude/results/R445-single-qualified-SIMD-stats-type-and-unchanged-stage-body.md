# R445 — 实际199的唯一 BatchStats 类型限定与原完整程序保留

作者：ChatGPT /root，2026-11-16。只有源码文本、原编译错误及字节身份工作；没有本地import、AST、compile、fixture或科学求值。

## 1. 实际问题与最小改动

[R424实际199](R424-actual199-persistent128-acceptance-SIMD-type-compile-block-and-partial-audit.md)从公开run43775312697/source51a38839的两份原必要结果完整读到：persistent128首alpha1已按原停止判据接受，但stage可执行文件未生成。原stage.cpp:44的 `BatchStats` 查找歧义导致编译退出1；原完整3462 B错误文本SHA256为 `e3e62b675de0e6ff10fb5354c5248ad9baf1635ecda3d43fe28555b9532cf2d7`。这不是original64非线性拒绝、native读回协议70或已运行的SIMD性能结果。

原文件 `geometry_20261115_native_simd_digit_operator_stage128.cpp` 为12670 B / `b6537c6ce86754a6a2a75eb928e543a7083fa2311eb70a4764066f2a70dda91a`。新文件独立命名：

`computations/geometry_20261116_native_simd_stats_qualified_stage128.cpp`

身份 12691 B / `eca87efc267d692e401d2ed49904d3d8e73cc16cad12eb3ae24042328f81025e`，Git blob `16559cb793d00206a616ab982334ac9b8da695f3`。

唯一实际源文本替换为：

```diff
-    BatchStats literal_stats;const auto literal_started=Clock::now();
+    simd_digit_trace128::BatchStats literal_stats;const auto literal_started=Clock::now();
```

旧文本只出现一次；逆替换后整份文件逐字等于原12670 B源。其余代码、注释、include、全体常量及控制流没有改动，旧文件保留不覆盖。新名字是独立来源，不将新的字节身份写回旧文件名。

## 2. 为什么限定为这个类型

原stage文件已经显式声明全局 `using BatchStats=simd_digit_trace128::BatchStats;`，并有 `using namespace simd_digit_trace128;`。该命名空间又通过其原依赖引入共享统计类型。实际编译器在不限定的 `literal_stats` 声明处报告歧义；因此仅有原alias并没有解决本次真实查找冲突。

所需对象由原 `LiteralBases(p,literal_stats)` 及其 `identity(...,literal_stats)` 消费；SIMD实现的这两个入口使用其自己的 `simd_digit_trace128::BatchStats`。原stage其他位置的 `std::vector<simd_digit_trace128::BatchStats>` 和总统计对象也已采用该完整限定类型。本次用同一明确类型消除这一个名字查找歧义，不改构造函数、继承关系、统计字段、字面基构造或其累加逻辑。

这是一项源码语义选择，**不声称旧歧义程序曾成功运行，也不能称新旧可执行文件运行字词相同**：旧程序此次没有stage可执行文件。只有后继公开Actions实际编译/执行能说明修复是否足以推进完整链，不能由此处文本工作补写成功。

## 3. 原数学与执行范围不变

原SIMD header、digit kernels、预组装算子及[R423三处column_environment限定](R423-qualified-column-environment-calls-and-unchanged-numerical-program.md)仍分别保原源身份。R423的三调用限定已在199实际编译路径生效；新限定不撤销、改写或重做那三处数学调用，也不把新204称为“仅三调用限定”的旧199产品。

除这个类型拼写外，stage原所有范围仍逐字保留：

- 实际同一个packet、persistent128 state及原577×224布局，576个stage、每stage224列的请求合同。
- 原各stage全部atomic RK、完整root trace/两mean/记录系数和列推进；仅完成全部请求列与原atomic步后写该stage payload。
- 原SIMD精确dyadic点积、一次RN113、实际指数跨度及全指数整数fallback；无新增精度阈值、固定limb近似、秩筛选或截断。
- 原4-thread动态stage调度、原deadline/resource stop、参考列仅原显式诊断、未完成stage与完整实际进度记录。
- 原complete-requested-range判据、原summary/error/partial语义、全部错误地址与不凭计数补科学完成的规则。

R402/R405/R414关于重关联、nominal-factor、C-based radial和不冒准确ODE/IEEE导数的范围声明继续适用。此次仅类型限定不把这些条件结论升级为实际导数证书或连续闭面证书。

## 4. 必须接入后继真正完整链

后继204由root独立编排，必须把实际launcher的STAGE指向新basename/SHA，保留原199所有89个来源并明确追加本新源与新launcher/helper/bridge/reader。实际复制/编译命令必须消费这个新文件；仅在request加一个pin而仍编译原stage不算修复。

新launcher应明确保留R423原三调用变换及其身份核；在本轮新增的必要scope字段中分别记录“三调用限定保留”和“新一处stats类型限定”，不能继续把新组合说成仅三调用改动。readout必须绑定实际request204，不重复192/196曾出现的硬190编号问题。所有变化以完整文本diff审核，实际编译只能放在公开Actions原科学流程中进行，不加独立fixture或前置科学门。

原预算和完整责任保持：从真实91输入再生当前原64/H/R273及128 owner/replay，再尝试完整576×224 stage、112 boundary、338×112 endpoint、独立完整audit；原19200总/6000 owner/1200 replay/8000 stage/600 boundary/600 endpoint/1800 audit，cleanup120、原各component overhead及330/350分钟job/step计划不放宽。四component不能用199已删partial audit或旧SHA拼成完成；native/fullDN仍要本轮完整真实返回。

## 5. 当前结论与未付

已完成的只有这一处明确类型限定及整文件逆替换字节核。尚无204run，也无实际新编译、SIMD完整576stage、112/338或完整独立audit结论。R424旧失败与560/576、7305/7488 query、6771 advance的partial范围仍属于旧run；新结果不能回填旧run。

继续建立并实际执行204完整链，终态必要结果保留为R446，由正式run绑定后唯一负责人读取。只有当前原全部门真实支付后才讨论非线性native或fullDN接受；README要求的完整闭面同g、度量、held、reach、含反射刚性及全部精化仍独立未付。
