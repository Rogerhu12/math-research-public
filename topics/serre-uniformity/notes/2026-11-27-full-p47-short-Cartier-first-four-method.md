# 首四例的独立短 Cartier 请求

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126。

## 1. 准确的新范围

本请求只读取尚未向本消费者提供完整值的
0-ZA、0-ZB、141-ZA、141-ZB 四例。
[R1121](../results/R1121-certified-original-twelve-short-Cartier-values.md)
的十二个已完成 case 一律排除，不重新计算其第三类形式或数值。

原 Miller run45973334832/job140418866621 仍在执行。
请求如实记录同一四例正由不同算法计算，并明确记录已经观察到的完成值为空；
这不声称尚未公开的内部计算没有进度。
如果该原任务后来完成，只消费那一次已有回执，不补跑 Miller。

2026-11-27 重新全文读取两 README：没有“在途未出值不得用另一算法读取”的禁令。
根规矩2、6、12要求继续必要工作，且根已明确授权这个新输入。
v1 的 other_active_case_ids 是当时十二例的调度范围，不被篡改。
本次新增独立 v2 请求、入口和 workflow；所有成功 v1 文件、请求与哈希保持原样。

## 2. 入口与没有改动的数学引擎

新入口为
scripts/full_p47_short_Cartier_first_four.py，
读取
notes/full-p47-short-Cartier-first-four-request.json。
read_request() 明确要求 v2 ID、四例固定顺序、十二例完整成功回执、
原 Miller 并行来源以及全部依赖 SHA-256。

它复用原 full_p47_short_Cartier_third_kind.py 的 ResidueRR、
prepare_case、共同 Gaussian frame_worker 和原 support.worker。
只为新的 scope 构造 FourRR 子类：其 build_cases 逐字沿用原清分母 cycle 公式，
但只允许两个中心与两个角。没有动态字符串修改源码，也不重写任何 v1 guard。

父进程先启动同一新入口的 --field-worker 分支，
该分支先验证 v2 请求，再直接调用未改动的 support.worker。
它不调用 v1 的命令行请求读取器；因此不需要篡改执行 ID、请求字节或预期 SHA。
纯 FLINT 子进程完成后，父进程才导入 Sage。
全部原闭点 jet、三种 stabilizer、cusp 留数和粗参数保持 R1118 的规范。

新入口在 fork worker 中调用原 frame_worker。
每个共同帧只同时计算这四个新分子；
没有调用原十二例的 prepare_case，也没有生成其新的 alpha。

## 3. 共同 C/E/grid 是必要输入

四个新的 $h/f$ 仍需要同一73个真实局部图的 $B^{4512}$ 系数，
所以必须在 runner 中重新生成原长 grid 与 probe 上的形式。
这只是新读取所需的共同输入，不把它写成第二次认证旧结论。

在输出任何新 $\alpha$ 前，程序强制比较：

- 原 Gaussian grid：627e076ae64de06332324f1bdf0a82e2888b493f4799af3b7211c6d7524d7c50；
- 原 $E$：8c5073af02da9d9731f7cbff7ab5fa1e061e590fe965355c9a2e79ff463795bb，行列式3058；
- 原73个 determinant-one frame hash 与95值 hash；
- Cartier 列矩阵：21fc43c13f58e974adb58804e3480f80d3268104546e31e40ca5370806bbb58f；
- Cartier 行矩阵：deda5ed6dbe8122f243c46bb60245cf8facc00b6040a8f34958c9ca4241d855d；
- $\det(1-C)=551$ 与原 KS 常数809。

含 meromorphic case 值的 all73_frame_values_sha256 会随这次新 case 改变，
所以不能误拿它与十二例的旧 hash 比较。
原 $C,E,$ frame 和 grid 本身则必须逐 hash 相同。

## 4. 原归一及失败范围

新 row 与 QC v2 接口完全一致：
candidate_id、angle、id、coarse_parameter='j-j_CM'、
clearing_denominator=6、order_mod_q=551、alpha，
method='R1118-short-Cartier'。
正号修正仍是 $(1-C)^{-1}(C\rho-\rho)$，最后准确除以6。
不写不存在的 Miller 链终点，不把其它 $D_y$ 的 all_eight 表列改称本例值。

每个新的 RR case 完整保留支撑、残数和分母证书。
只有共同73帧全部完成且旧输入身份通过后，才输出已完成 case。
任何失败都保留此前真实完成行，并以失败状态退出。

预算为3600秒、reserve120秒、最多四核；
独立域输入上限1800秒，包含在总预算内。
不保存 raw 矩阵、长级数或 artifact。
旧四例 Miller 的在途工作不因本 workflow 被重新触发。

本方法和源码只作纸面审查，未在会话内执行、编译或运行数学测试。
