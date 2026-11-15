# R787：首个42维双probe格的实际结束与可复用状态

## 1. 已证明的有限计算结论

公开run [43748801736](https://github.com/Rogerhu12/math-research-public/actions/runs/43748801736)，
job132918006043，源提交e2ac3449ac480c6f00bce197c0bd5202f8b1fda4，
在2026-11-15 19:05:49.930048 UTC结束。核心用时894.401223039秒、exit2；
其计算步骤容许失败后上传完整状态，最终verify据未完成准确关系而返回失败。

本次只消费已认证的原430位lift，不增加Dixon位、不重做原十四分支逆。
按[双probe方法](R787-original-projective-two-probe-reconstruction-method.md)
直接取原C0、C1两行，以同一整阶O的14坐标建立42维格。
全部42条LLL行已保存，84个原probe同余由实际核心核过。
42个分母均非零、互异，且均为辅助素数处单位；这些单位诊断没有充当接受条件。
实际分母最大整数坐标位长只出现8570、8571。

全部42个候选的准确拒绝记录给

$$
\operatorname{first\_nonzero\_relation\_order}=1.
$$

这里序号m对应Laurent指数m−1。因此每个候选先通过m=0、Laurent指数−1，
随后在m=1、Laurent指数0得到已保存的准确非零残差。
核心按m递增、只有完整原280个有理坐标为零才进入下一阶；
这个顺序和逐候选拒绝记录共同给上述有限结论。

**不能把false FINAL里的exact_verified_orders=0解读为没有单阶通过。**
该字段只在完整129阶成功时赋129，否则赋0；当前已读的逐候选残差才决定实际失败位置。
同理，本次没有恢复真实A/B，也没有计算β、η或高度。

m=0通过还有明确的构造原因。原已认证rational-blocks给E0 Z=0，
新候选先用B′=Z C′再除共同整数内容，故B′的常数项准确为零。
该阶方程是R0 B′0=0，R0=1且A_{−1}=0。
所以m=0不提供额外的恢复精度证据，m=1才是本次首先遇到的未预先强制等式。
这也不把m=1残差归因于某个C probe：A和未知C分别从模数中取中心代表，
残差只否定整个候选A/B。

## 2. 实际停止的含义

本次控制为maximum_nodes=42、maximum_lattices=1。
核心记录search_node_budget_reached与search_lattice_budget_reached均为true，
candidate_search_exhausted为false，时间预算未到。

准确队列已完成pair0，probe_pair_index=1、next_candidate_position=0；
保留42个processed_node_ids，不会再执行这42个候选。
原固定剩余顺序为：

| pair | 两probe（全局C后A索引） |
|---:|---|
| 1 | C0、C2（0、2） |
| 2 | C1、C2（1、2） |
| 3 | C0、A0（0、1214） |
| 4 | C1、A0（1、1214） |
| 5 | A0、A1（1214、1215） |

提高同一核心的停止预算并绑定本次真实artifact，可从该队列继续。
若改为增加probe数量等新的候选算法，必须使用真实新核心和新数学身份；
已有完整42维格基、候选分母与准确拒绝可作为旧来源读取，不能冒充新输出。
是否增加信息或继续原固定顺序，不由一次失败强行推出。

本次严格排除了这42个具体候选。
它不证明原430位精度不足，不证明真实关系不存在，
也不证明任何坐标高度或所有候选的完备性。
LLL短行只是候选来源；唯一成功出口仍为原free1186方向、
原Z展开与内容约分、完整129×280准确式和B非零。

## 3. 原计算身份和活跃输出

| 对象 | bytes | SHA-256 |
|---|---:|---|
| 核心R787_projective_two_probe_reconstruction.py | 47438 | 73bac3a27c27e8e5411a0950d6efe7575c7b6e7d60dc1ed0b7eca94de1fcb093 |
| 包装器R787_projective_two_probe_public.py | 43795 | fe276ba3aec1c2d3e1c32b42e2f54e8a9c759aef2bee4aa8045493904567f926 |
| 方法笔记 | 11850 | 17c8927190cdc66aedf644004fe25ad7e3c24f042f5f6a660758d54c05c49a05 |
| 请求R787_projective_two_probe-public-request.json | 5974 | 7421c941ffa61a552d6d1c5b1ca968639b1833c1f17058c08f63428edd99306b |
| 完整输出manifest | 28618 | 2a18a2f48509695e6f316087c09c6fa9c8fd92bcf47b26c768174b6290c95845 |
| 全部准确stage清单 | 13118 | 40c54fc03eabe994156f1006616b0b8f46c153ff71e0d491f0385531daf7ea2d |
| 当前搜索队列 | 6328 | 2cf3e41f796e90b6eb9edd5d01c93bc12a8d46638cf8572c81649eced28a4f3d |
| pair0完整42维LLL记录 | 3194201 | 3b8fbe90d539bb01609391a3ce7843e2ca75896bb2de3322840b4aef2ce452ef |
| 原1380个输入的活跃carrier | 189156436 | ad0c9493b6dc6f6ed99b37c58941000c638fcad683992e9b538a81a2123ed6e4 |

完整manifest含137项。原run的冻结IO已验证全部manifest文件、全部1380个载体成员、
以及42份闭合失败回执。每份闭合回执保实际拒绝、结果和已退役大payload的SHA/bytes；
只有闭合失败payload被移除，当前或成功候选不会这样退役。

一日artifact14176445740，
serre-global-R787-projective-two-probe-43748801736-1：
195943656 bytes，平台ZIP SHA-256
1fdcdc967431ffaac36810967bdf2a0b989fc95d9041dea2e9e5de0cce49fd4d，
到期2026-11-16 19:05:50 UTC。
实际core receipt SHA-256为
1e79ad17ac89f22ef2980c120cda9f3e44c29d4404b7c1e98b7aa700073dd2ff；
false FINAL SHA-256为
d7e0e128ea8bc9b5efc2d50ebaa6bb502b6e1ea3e4ff7b2f7bd041206b141c5d。

## 4. 只读消费者与来源边界

纯IO公开run [43750891953](https://github.com/Rogerhu12/math-research-public/actions/runs/43750891953)，
job132924366195，源40c3bb3c22f46c4a2a8b1051f4a90d9cb5864281，
AST、实际源读取与artifact上传全部success。

它执行已提交的R787_two_probe_ended_IO.py
（12194 bytes，SHA-256
ff9885d01ebb8168155bda32a4cf9b18e757477c21c80d5c3ab0375fd7b05f7b），
请求SHA-256
6bb58581a03fe39a40353425ce0c65027c494079850fd87e635e94ecd95b47cf，
workflow SHA-256
f1b0b74940f054d57c3a1bbd29c56f3a15b48559e221fe9e3a7617b3d8026434。

该消费者只取136个非carrier输出及manifest/reference，
逐项核bytes/SHA、完整tag和队列/LLL/拒绝/闭合回执的引用关系，
不重做格约化或任何关系验算。
11个HTTP Range请求实际传输6815816 bytes。
载体本次只引用原已核身份，没有重新下载；
平台ZIP摘要也明确不称为本次对195943656字节重新哈希。

小IO一日artifact14175778017：7104291 bytes，
ZIP SHA-256
69fe114133f94219f299ab2c434ed7adb2a1bb530f29672e7aabe206e828f5cb，
到期2026-11-16 19:10:20 UTC。其机器summary、LLL及残差只留活跃artifact，
不写Git或Release。仓库只保脚本、参数、真实run、摘要和本解释。

本记录不重开固定p41分类，不改变原模型或已有精确结论。
主目标与同一原规范的函数/高度输入仍开放，继续由实际保存状态推进。
