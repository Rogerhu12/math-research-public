# 原 full47 短 Cartier 消费者：执行与接口

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126。

证明来源为已发表 [R1118](../results/R1118-original-short-Cartier-reading-for-CM-third-kind-values.md)。
本说明和两个消费者均未在会话内执行、编译或运行测试。
实际数学只能由本公开仓库的固定 GitHub Actions 请求启动。

## 1. 新文件

- [full_p47_short_Cartier_third_kind.py](../scripts/full_p47_short_Cartier_third_kind.py)：Sage10.6 主进程、原 graded RR、全部残数、确定性分母选择、共同73帧、Cartier 矩阵和最终原 $\alpha$。
- [full_p47_Cartier_support.py](../scripts/full_p47_Cartier_support.py)：独立纯 Python/python-flint0.9.0 子进程，实际 closed-point jet/frame 和 Gaussian free fibre 常数。
- 请求模板只说明新输入字段；它不是已经启动的请求。

主进程入口不带自选参数，准确读取
notes/full-p47-short-Cartier-third-kind-request.json，
并核环境中的 SERRE_EXPECTED_REQUEST_SHA256。
所有依赖文件都有 SHA-256 pin。实际 checkout 由旧 source_head() 与
GITHUB_SHA 比对。workflow 的 image 沿用
sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879。

## 2. 只计算新的 case

原 case 名为八个固定 ID
0、76、77、100、108、141、196、220
分别配 ZA、ZB，共16个。
模板先列12个非 0/141 case；
在途 Miller 的首4个只列为 other_active_case_ids，绝不冒称已完成。
root 发布实际请求时根据真实日志决定：
已完成的列入 already_completed_case_ids；
未完成且不再由其它任务执行的 case 才可移入本请求。

消费者拒绝 cases 与已完成或其它在途集合相交。
不会重新执行旧标签图、MW 首矩、全局高度或已认证的 $\alpha$。
固定输入允许重建并逐 hash 核对，这不是第二次认证旧结论。

## 3. 进程隔离与共享来源

主进程在导入 Sage 前先以其 Python 可执行文件启动 support 子进程。
子进程禁止 Sage，核只加载 wheel 的一份 FLINT。
只传 runner 临时目录中的整数 JSON，子进程退出后主进程才导入 Sage。
这沿用已真实修复的 FLINT ABI 隔离方式。

support 复用原 full_p47_Miller_support.py 的完整 heat 流、真实八个标记及 Reynolds 求和。
新增的支撑导数保留整个扩域；只有确为 $\mathbb F_q$ 的中心和 Gaussian 常数转为整数。
原 R1105 的 G1、短 heat 和粗切向三组 hash 都逐一核对。

Sage 重建 R1104 的原836 jet graded ring，核完整证书。
原95个 descriptor 与 all23 cusp 保留。
Gaussian 长来源只调用原 full_p47_Gaussian_CM_log.py 的
original_base() 和 torsion_eisenstein_grid()；
不调用旧 CM moment 或旧 log/Hecke 分块。

本次必须核原长 grid 的 SHA-256
627e076ae64de06332324f1bdf0a82e2888b493f4799af3b7211c6d7524d7c50，
来源为 R1093/run45947023569/job140333947037。
原物理基仍是 $P=(653,525),Q=(3860,232),i=95$，Weil root2。

## 4. RR 的实际有限检查

ResidueRR 的主要可复用接口为：

- build_cases(data,request)：完整 (1118.3) cycles，含23个 cusp 和清分母6。
- select_probes(data)：先删全部 Gaussian 支撑，再选共同73帧，返回原 $E$。
- prepare_case(case)：返回真实 $f\in V_2$、$h\in V_3(-C)$ 的系数及全部来源证书。

每例以完整闭点评价构造 $W_S$，核维数 $262-s$。
确定性选择 $f$ 的算法不靠随机试验：
按每个非零线性条件依次修正 $f\mapsto f+cb$，
只排除至多240个 $\mathbb F_q$ 值，每步保留所有先前条件。
所得 $f$ 在 $S$ 单零，避八目标与共同73帧。

colon 的所有乘法只到 $V_5$，先限制到其763个已认证 pivot 列。
当前空间始终包含 $fH^0\Omega(S)$；达到 $72+s$ 就是完整证书。
否则遍历全部 $W_S$ 基。残余零的完整重数自动包含，没有 squarefree 假设。

残数矩阵在真实闭点域逐系数展开为 $\mathbb F_q$ 方程。
其秩必须为 $s-1$、核必须为73维。
每个非 cusp 残数先核 Frobenius 下降；
23个 cusp 全用原 $47h_1/f_1$，而非省略或重新平均。

## 5. 新长展开的精确范围

每个共同 Gaussian 帧的本地参数都是实际 $B$，不是 $j$。
只求模 $B^{4513}$ 的95个原形式。
所有帧共享一个原2208点长 grid，并按 determinant-one frame 重排。
两个 Reynolds 相位完整保留。
纯虚 $\rho$ 可用第二项等于第一项的负号加速，但绝不删除该项。

每帧在同一批形式上读取：

1. 全73个 Hodge 形式乘原 $k(B)$ 的 $B^{4512}$ 系数；
2. 所有已完成 RR case 的 $k(B)h(B)/f(B)$ 的常数与 $B^{4512}$ 系数。

每个分母常数必须等于此前有限点值且非零。
95个长形式的常数必须逐项等于 support 子进程的原值。
共同73帧完成后恢复真正 Cartier 列矩阵并核
$\det(1-C)=551$。
再用正号修正 $(1-C)x=C\eta-\eta$，
最后准确除以6给原 $\alpha$。

最多四个 Sage fork worker 按帧并行。
它们只返回小的整数行；不跨进程传长级数，不保存长数组 artifact。
原旧 cusp API 的最高长度仍是836。

## 6. 完成、失败和后继

单例实际值使用 actual_third_kind_value 输出，
含自己的 $\alpha$、在全部八目标处的同一规范值、完整原除子 hash、
RR/残数证书 hash、Cartier 矩阵 hash 以及清分母6。
每个完整 row 明列 candidate_id、angle、id、coarse_parameter='j-j_CM'、
clearing_denominator=6、order_mod_q=551 和整数 alpha。
method 固定为 R1118-short-Cartier；不伪造 Miller 的 N 链终点。
这些已完整输出的 case 可被后继直接消费。

每例 RR 失败会明确记录并继续其它声明 case；
若最终只完成一部分，job 返回失败且保留已完成实际值。
73帧或 Cartier 矩阵尚未完整时，不输出任何虚构 $\alpha$。
运行时与资源仅由实际公开回执说明；本文不预言执行时间。

模板预算是数学18000秒、reserve120秒、最多四核；
短域输入有共享总预算中的1800秒上限。
root 可将实际请求收紧，但不能把未完成 case 标为完成。
不上传 artifact，不提交原矩阵、raw series 或日志分块。

这些输出随后才与 R1103 原 $K,b_y,z_Z,d_{Z,y}$ 合并；
本请求不提前宣称二次 QC 矩阵秩二或八盘唯一。
