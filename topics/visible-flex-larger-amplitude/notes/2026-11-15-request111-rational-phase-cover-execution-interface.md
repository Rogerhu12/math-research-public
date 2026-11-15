# Request111：准确换门覆盖及明确不足预算的公开执行

2026-11-15。此请求执行 R281 新解析配置，独立于当前 native/fullDN、prefix 和小核支线，不读取旧场或旧 fixture。R281 证明登记不等待本次运行。

## 冻结文件

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| public-rational-phase-cover-request.json | 5555 | ee9d115df498362d48507a7ee89a5f6be6345619fcb1eec611e8a2feaec8ffe7 |
| visible-larger-public-rational-phase-cover.yml | 10850 | 7f5ff78090a563bf818d9584e50e394c8396aa133e499a4f3aa379773c3fe259 |

workflow 放 .github/workflows/；request 放 topics/visible-flex-larger-amplitude/computations/。唯一触发路径为该 request，concurrency group 为 visible-larger-r281-rational-phase-cover，cancel-in-progress=false。

源码闭包只有三件：

- geometry_20261115_rational_phase_cover.py：f6214d1dc66f9890e99f5d9bbbc93fa0e6524acd6ac879f0058ea023ebc17537；
- geometry_20261115_joint_phase_normal_balls.py：c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466；
- root_mixed_phase_normal_balls.py：ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6。

R281证明为 R281-exact-rational-phase-disjunction-and-finite-cover.md，SHA112d49e942c4a6728baf7f683d53dedf04a63f5efc4786c9e2b02a111cc0d6ee。新源与旧两源的算法身份均未再修改。

## 一组输入、两种明确资源预算

配方完整保存 R281 §281.6 的有理参数：

$$
p_0=(1,0,0),\quad q_0=(1/2,0,2),\quad
n_0=(-3/5,0,4/5),\quad m_0=(3/5,0,4/5),\quad \tau=6/5,
$$

四个误差半径均为零。它不是当前实际场数据，而是有完整解析恒等式的新条件配置。

两次都用 sqrt-bits=128、max-cells=16。唯一差别是最大深度：

| 执行标签 | 最大深度 | 解析预期已测单元 | 二分单元 | 终止叶 | 已付叶 | 未付叶 |
|---|---:|---:|---:|---:|---:|---:|
| complete-depth2 | 2 | 8 | 3 | 5 | 5 | 0 |
| limited-depth1 | 1 | 4 | 1 | 3 | 1 | 2 |

两次旧全圆距离、移动端、固定端和联合项都应未付，因而两次都实际执行新的两图分区。原全部法向弦条件也应未付。

完整深度二分区的解析预期为：

| 图 | 二进制路径 | 闭区间 | 支付门 |
|---|---|---|---|
| t | 空路径 | $[-1,1]$ | moving |
| u | 00 | $[-1,-1/2]$ | moving |
| u | 01 | $[-1/2,0]$ | distance |
| u | 10 | $[0,1/2]$ | distance |
| u | 11 | $[1/2,1]$ | moving |

在 u 根区间，moving 多项式端点严格正，内部却有一个不同的偶重实根0；请求显式核该根计数为1，不能以同号端点冒连续严格正性。

深度一的两个 u 叶只报告最大深度未付。源码正常返回完整未付分区，不能把它作为“几何失败”抛出。workflow 比较的是已声明的解析预算行为；完整成功和有限预算未完成都是本配方预期的真实记录。

所有表格数值仍是解析/源级预期，尚无实际运行结果或预填run/result SHA。

## 步骤、资源和权限

稀疏 checkout 两 README、request 和三源；核根README blob74c08a36f6c997d0bc1e64a7956b42276f5fa5d7、topic blob bff8aea253a9e6a7a4fac28d810ac454c5499fec。随后核完整 request SHA、三source SHA和AST，才由参数配方生成runner临时输入。

Python固定3.12.14。两次算术各有5分钟step上限，job10分钟；没有改变任何原求解预算。permissions仅contents:read，科学步骤没有传入GitHub token，源码还自行要求公开仓库环境。

报告步骤按实际输出读取：

- 全部旧全圆布尔量；
- 两次真实计数、完整小叶分区及实际选中门；
- 每个已付叶的严格端点/有限Sturm证据；
- u根区间四项原失败证据，包括内部偶重根；
- 完整临时输出的字节数和SHA；
- 真实run、attempt、source commit和Python版本；
- 所有解析预期不符项，先完整输出小诊断后才报工程执行失败。

没有新数学验收门，没有把此例结论推广至当前闭面。

## Rule15 与本地检查

workflow没有upload-artifact、Release、publisher或Git写步骤。完整可重算结果与派生输入仅在runner临时目录；公开源码、参数、真实run、输出SHA和紧凑日志/step-summary。

request111-source-only-check.json 已核 YAML、4个shell block的bash -n、2个内嵌Python AST、三源码字节身份及唯一trigger。没有本地导入数学源，没有执行多项式、Sturm、根号或任一科学案例，没有Git mutation、下载或Actions派发。
