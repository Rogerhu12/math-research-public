# 完整 m=8 pure 右尾 R8 投影：消费器设计

日期：2026-11-14。代码文件：scripts/literature_full_m8_tail_response_projection.py。本文是新公开 Actions 运算的设计说明；在实际报告 completion=complete 之前，不声明新秩、依赖、剩余障碍或完整尾可解。

## 1. 真正新增的目标

R110 已给一个真实方向 K=B_t1(tau_p1,t1) 的完整 pure −4 输出；R111 用其四个平移，只支付 m=8 的 D25 多项式。那四个自由度已经用于 c⁷、c⁵、c³、c，其他 r 次数与它们耦合，不能据此宣称整个 pure 尾周期已清除。

新的有限目标是下列完整线性投影：

$$
\mathcal R_8=\operatorname{span}\{\mathcal B_P(T):P\in E_8,\ T\in W\}
\longrightarrow\mathbb Q[c,r],\qquad
K\longmapsto K_{-4}[(c-\xi)^8](c-r).
$$

E₈ 使用全部八个真实无迹矩阵算子，不再限制到旧正 bulk 的七维空间；W 使用已证明完整的 36 个真实外槽第三模板。运算保留全部 c/r 单项式和全部右原函数，不选一个有限数值节点集合。

总共有 8×36=288 个原列。R110 的 (外方向 t₁，第三原列 12) 已有完整八项，因此逐字节消费它的原报告，新的实际仅评价其余 287 列。旧 P1 目标、旧权零字符、旧 15 点查询、旧第四 forcing、旧 116 条第三依赖均不重算。

## 2. 必须消费已公开 W 原式，不重新编译

literature_local_fourth_quotient.py 的公开实际将在 N 势降维及长 weight 分块之前保存 W-only portable export。该文件含原始 profile atom DAG、W0…W35 的完整表达式及其 original_root_sha256；不是只保存 hashes。

消费器必填：

- --templates：公开 gzip 原式文件；
- --source-report：对应公开生产者报告；
- --source-report-sha256：所读报告的准确 SHA-256；
- --source-run、--source-commit：相同生产者运行与源码提交。

生产者报告必须匹配 schema、run、source commit 与当前冻结生产者源码。packed/raw 字节数和 SHA 从报告的 portable_W_expression_export 绑定；若消费旧的完整 W+local export，则采用 portable_original_expression_export。消费器只使用 W 根，不将 local density 结果当作本次输入。

W-only schema 为 visible-flex-R109-local-fourth-quotient-static-v1-original-expressions，content_scope=W-only，恰含 36 个 W 根。共同 decode_expressions 逐根重算原 SHA。随后与公开 v2 receipt 43633746055 的全部 36 原模板 SHA、retained indices 和 receipt 身份逐一比较。

若生产者在导出 W 之后因后续研究预算退出，已完成的 W 导出仍可消费；不要求后续局部第四目标完成。但生产者报告必须确实保存匹配的完整导出记录。没有这份公开导出就不运行实际消费，也不退回重编 W 的路径。

### 已公开紧凑报告的伴随 receipt

run 43645177423/source 2f1b809c0b0abb7a26303d36940edc203815f872 的局部生产者已完整导出 W，但其主报告因摘要长度门缩成 completion=output_limit，并未保留 github_run_id/github_sha。消费器不能跳过来源检查，也不修改该原报告。

此时必须额外传 --publication-receipt 指向同目录公开 receipt.json。消费器严格核其中 repository、lane、run_id、source_commit；核 source_files 中原生产者的 bytes/SHA；核 outputs 中主报告的全部 bytes/raw_bytes/SHA，以及 W 导出的 packed/raw bytes/SHA。只有原主报告两个来源字段都缺失时，才使用这份已核终端发布记录中的来源；原字段存在而不匹配仍拒绝。

本次主报告为 3982 bytes，SHA-256 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a。W-only packed 7377 bytes，SHA-256 45cbdc8f38a4b5561924badaf9cd68a93a7fa71c6264d95489034703af4ee44a；raw 31750 bytes，SHA-256 615d848611aaf787bc3ae790b4b1f81fe91338301bcb57afdfd111758cf533bf。所有身份来自真实公开 receipt，生产者本身不修改。

R110 输入为 notes/actions-43643100132-1-c7_transverse_tail_probe/c7-transverse-tail-probe.json：2179 bytes，SHA-256 c6c2c4c886dc5f115569ab4dd36176530efcf80ed12bb83b3d19223a7a279746；完整八项数组 SHA-256 e37a582bd52a0a7028e2794cd0d6084f050dc4a65b5905d949c00e9dcecdf850。原 t₁/tau_p1,t1 列不再评价。

## 3. 准确右锚与完整相位比例

复用已发布 literature_c7_transverse_tail_probe.py 的 Fraction 双变量算术，不更改该文件。它取 x=c−r、Dξ=−Dr、J=∫₀ʳ。

原 colored DAG 的 int_right 实际表示 I=∫c^ξ，因此消费时准确取 I=−J。新读取器直接递归原 atom DAG，不进行 word 归约或删除原函数常数；保留 exterior a 与 inner b,c 的真实顺序，不以一个新对称假设给输入排序。

对每个原外方向 P 和原第三模板 τ，准确使用

$$
K_{\rm pure}
=2\tau(P(q,q);q,q)
+4\tau(q;q,P(q,q))
-4P(q,\tau(q;q,q)).
$$

pure −4 输出为该完整式的 1/16，来源是
φθ=(e⁻ⁱθq+eⁱθq̄)/2 的第四齐次相位展开。不存在另一个为结果调节的归一。

## 4. 权分块、完整多项式秩及证书

八个第二参数的真实缩放权为
(−1,0,1,−3,−2,−2,−1,0)。
W36 使用原已证 THIRD_WEIGHTS；组合响应权 w 为两者之和。

对于四次 m=8 输入，每一非零单项式必须满足

$$
a+b=32+w\qquad(c^a r^b).
$$

实际逐列验证这项结构，否则整个运算不发布数学结论。不同 w 的单项式支撑互不相交，因此完整投影秩是各 weight 块的准确秩之和。

每块用 Fraction 的完整列消元，不取模、不采样、不作浮点阈值判断。证书保存：

- 全部 288 原列的准确多项式、原 W SHA、外方向与 weight；
- 独立原列序号、真实主元单项式和归一前主元值；
- 每一丢列在独立原列上的准确有理系数；
- 在完整已评价多项式上重新相减为零的检查；
- 所有出现的 c/r 单项式行和完整数据 SHA。

因此所得秩和依赖在这个准确有限尾投影中同时有上下界。投影中的零列或依赖不自动是 universal R8 的真实全函数关系；报告明确不宣称完整 R8 维数。

## 5. R104/R106 四块的准确投影

对一个 pure 尾单项式 cᵃrᵇ，反射倒行四块的作用为

$$
2\{V(c,r)+V(-c,-r)\}
=2(1+(-1)^{a+b})\,c^ar^b.
$$

所以偶总次数乘四，奇总次数为零。对 homogeneous 32+w 列，恰是偶 w 保留、奇 w 消失。报告同时给完整 R8 右尾投影和这一四块后投影的准确秩、支撑与独立列。

这只是已付反射公式在完整尾多项式上的有限线性投影，不替代固定全带右锚的 ruling；也没有让真实单块 V 自动变成 −V。原基准块的成本仍须处于可调投影内并实际支付，才能升级为某个完整尾周期控制。

## 6. 新人工入口与实际入口

--toy-only 只检查新接口：

1. 人工 colored 多项式/原函数 DAG 的原 SHA roundtrip；
2. int_right 与双变量 J 的负号；
3. 外槽及内槽顺序没有被错误交换；
4. 人工有限多项式的准确秩、完整有理依赖；
5. 混合总次数的四块投影；
6. 人工伴随发布记录的正确来源接受，以及主报告 hash 错误时明确拒绝。

人工输入次数至多三，不加载实际 W36、不调用 m=8 目标、不编译真实 forcing、不积分参考几何。当前容器不可用，本地未运行这套新检查；必须在公开 Actions 先作 py_compile 和 --toy-only，并如实保存其实际结果。

实际入口有 GITHUB_ACTIONS=true 与 GITHUB_REPOSITORY=Rogerhu12/math-research-public 的双门。需要上述完整公开输入。默认完整计算 240 秒，RSS 1 GiB，poly/linear 各 10⁷ 次操作，最多 5000 项中间多项式、总次数 80、有理位长 8192。所有报告保留 completion；超限不能把部分列秩冒完整投影结论。

## 7. 输出及边界

主报告保存来源、原列计数、新/复用列数、每个 weight 的准确秩、四块投影秩及全证书身份。完整证书为 gzip JSON，raw≤32MB、packed≤4.8MB，保存全部原列和全部投影依赖，不截断为预览。

本次只刻画一个完整指定尾代数中的真实第四方向投影。它不评价任何基准几何的真实第四成本，不支付混合 −2 模式，不清除第三/第四 ruling，不给合法全局 C∞ 三矩圆、不求有限等距族或闭嵌入材料面。若投影留下非零余项，也只能作为下一项具体范围门，不能仅凭未付的代表式宣称完整非成员。
