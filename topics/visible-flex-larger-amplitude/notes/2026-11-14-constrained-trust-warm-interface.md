# 完整约束坐标下的阻尼初猜及原 fullDN 接续

日期：2026-11-14。request17 / `coupling112trust` 的执行说明。**目前仅源码及公开 Actions 接线就绪，没有预报下降、BVP 接受或闭曲面。**

## 1. 精确保留的有限问题

使用原 accepted96、原 699 点完整 M112/N2048 初猜、真正 T112 零高度完整 J 和原配置，四输入 SHA 均硬绑定。原文件不改写，不插值失败的 966 或 1073 点结果。

新坐标包含后 698 个节点的全部 338 维物理状态、109 个自由 core 和全部三个 scalar controls，共 $338\times698+112=236036$ 个未知量。入口物理状态由原完整 core 精确构造，第一项 r0=1、所有 z 为零、$r_m=c_m$、$t_m=-2mc_m$，前三 core 固定；全部节点复制同一个 core 和 p。因此原常数 ODE 行及左边界成为恒等式。所有 physical collocation 与全部 112 条 Rphi 仍保留，零点与原完整有限问题对应。入口浮点规范化的实际最大改变量单独记录。

完整物理、core、p 方向在局部 L/R、入口链式项和完整右边界中传播。正向与转置运算保留所有这些项，不构造正规方程或截掉高模。原全增广块作用、伴随恒等式以及直接 complex 原 collocation 的 global core/p 方向用于检查新实现的具体风险；这些不替代科学验收。

## 2. 本次改变的是求解方向和匹配的下降判据

每个模型固定残差权重 Wr：物理行为原 collocation 除以 $h(1+|f_{mid}|)$，右边界权重为 $10^{-6}/10^{-11}$。变量方向尺度对 r/t 取 $(1+2m)^2$，z 取 $1+(2m)^2$，core 还包含入口 $t_m=-2mc_m$ 的额外频率代价，controls 按其实际 0/1/2 scalar jets 的采样最大值缩放。这些是优化权重，不是连续 C² 证书。

显式矩形算子 $[A;\lambda I]$ 采用 LSMR 和精确列范数的对角预条件；$\lambda>0$。没有通过正规方程求解。算法实际记录原加权残差的方向导数、未含阻尼罚项的预测下降、真实下降及二者比值。

每个试探重新调用原完整 RHS，重建真正非线性 Hermite midpoint，再求 midpoint RHS 和当前 Rphi。保原 uniform-phi rho guard；预期逆图域失败只拒绝该试探，其他程序错误如实失败。保存前再查原两个 RMS/Lobatto 查询。真实 merit 必须下降超过数值噪声且实际/预测比至少 .1；这是已明确改变的优化算法，不冒原 17 次 Newton 接受式。

每一个这样的结果仍保存为 `success=false`、`new_coupled_finite_acceptance=false` 的 warm，包含全部原 mesh、states、rhs、新完整 scalar spec、输入源 SHA、真实 H 及 p。三模型/80 LSMR 步/至多五阻尼尝试/1200 秒只限制这一初猜尝试，不是研究任务停止条件；保存的 warm 可继续重启。

## 3. 原真实尾部与接受程序的边界

warm 和其导数核验阶段把已完成真正 T112 零 H 的全 J 显式保持仿射。warm 的当前 H 可以非零；报告同时保存当前 H 与零锚，不声称当前 H 已进行 native 非线性求解。

新 `constrained_trust_response.py` 对实际新 warm 重做原三步 centered FD、两个 Richardson 值和原 `5e-5` 检验，包含非零高度试探以核两个 core 链式项。报告重新绑定实际 warm 和所有当前源码，没有修改旧报告的 SHA 来假装通过。

这之后才调用原 `physical_test_full_dn.py`。它对 warm 的真实 H 调用原 native TailClient；任何非零 H 都不能命中 exact-zero 首请求缓存。原完整 outer true-tail、全带 LU、17 次 Newton、RMS `1e-6`、BC `1e-11`、冻结物理检查及最终 fresh audit 全保。只有这一原程序实际接受，才自动进入已有完整 readout、自己的尾、闭合及 R249 规范形流程。

## 4. 首次实际调用

`constrained_trust_warm.py`：

- accepted：原 `public-actions-43580643038-1-free3/stage-00/actual.json.gz`。
- prepared：原 `public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz`。
- tail-anchor：原 `public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz`。
- tail-config：同一 prepare112 的 `T112-config.json`。
- 参数：`--iterations 3 --lsmr-iterations 80 --damping 1 --damping-attempts 5 --line-search-steps 17 --budget-seconds 1200 --jac-workers 2 --angles 4096`。

workflow 从真实 `driver-status.json` 的 latest_warm_file 选择并重新核 SHA，只有确有优化进展才传入新 response。response 使用同 accepted、anchor、config 和 `--angles 4096`。随后原 fullDN 的 warm/response 路径指向这两个真实新产物，其他数学源、维数和原门不变。

| 新源 | SHA256 |
|---|---|
| constrained_collocation | `70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8` |
| constrained_trust_warm | `5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2` |
| constrained_trust_response | `7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78` |

本地只做源码、AST/编译及 YAML 静态检查；全部数学求值在公开仓库自身 Actions。artifact 和 publisher 始终保留真实结果及失败。publisher 的非快进同步去掉旧 30 次截断，按用户指令立即 pull/rebase 再普通 push，直到成功；其他 Git 错误或 README 新差异保留原件并明确报告，不强推。

