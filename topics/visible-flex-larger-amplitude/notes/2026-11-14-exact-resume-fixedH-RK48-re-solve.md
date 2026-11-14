# 同固定 g／完整 32H 的 RK48 真 Newton、完整 DN/J 与审计

可信度：**启发式/数值证据**。2026-11-14。原 worker 已真实退出 0，完整结果 `success=true`、`converged=true`；耗时 4114.7467434049995 秒。此条只登记已经结束的求解和比较，未把后续真实十六分点或整闭流水线算作完成。

## 同一个问题的真实 RK 精化

输入仍为原 A `2026-11-13-strong-q126-m32-tail2-actual-r1` 的完整 32 个 Dirichlet height 系数。原 RK24 收敛响应只作 warm start；RK48 重新执行原 nonlinear multiple shooting、原线搜索、完整最终 variational Jacobian、DN 读出和原有限审计，容差仍为 $2\times10^{-9}$。

与原配置相比，只改 RK/audit steps 及 warm/log/checkpoint 的 I/O 项。严格比较确认全部 H 逐项相同，物理 depth 8、M32、512 角 quadrature、8 shooting parts、576 段／577 shooting 节点、全部物理参数和源背景均相同。原 160 个校准源段与 frozen alpha 161.27721826272244 保留；source revision 为 `869436630c99aa5a68afb55bd8877c826034d117`，profile fingerprint 为 `8a87255bf9e025190a1a98ff800859f05f95a94113045a60af9391fcace51d24`。

## 实际收敛历史和终态

$$2.1789528527530774\times10^{-3}
\;\longrightarrow\;6.162478629541885\times10^{-9}
\;\longrightarrow\;1.6723555785869715\times10^{-10}.$$

两次实际接受步长都为 1。第一步尚高于原容差，因此继续了第二次真实 Newton；第二步之后仍完成最终完整 J 和审计，没有把 recovery-only 迭代包当作完成响应。

| 原 worker 最终审计量 | RK48 |
|---|---:|
| 实际 point metric | $7.994359041041177\times10^{-15}$ |
| full Darboux defect | $3.6147840431595007\times10^{-12}$ |
| normalized full defect | $1.9453290025931227\times10^{-13}$ |
| min leading | 0.8635103083329754 |
| min D | 0.9999284957696485 |
| formal curvature | 7.994260716974354 |
| max physical peak-to-valley | $5.651311493468282\times10^{-5}$ |
| holonomy | $9.480441077562133\times10^{-20}$ |

这些是原有限 worker 的点审计，不替代实际有限 Fourier/Hermite 曲面在节点之间的度量、曲率和二 jet 误差。后者由随后继续的真实内点读出和完整共同网格计算处理。

## RK24 到 RK48 的相邻级实际变化

原 RK24 的完整响应见 `2026-11-14-exact-resume-fixedH-RK24-re-solve.md`。本次比较的是两个各自真正通过原 Newton/J/audit 的响应。

| cut 量 | 最大绝对差 |
|---|---:|
| 全部 32H | 0 |
| slope | $3.5538342017457647\times10^{-13}$ |
| second | $8.292664731984756\times10^{-12}$ |
| meanSlope | $8.326672684688674\times10^{-17}$ |
| meanSecond | $2.0872192862952943\times10^{-14}$ |
| meanSlopeCorrection | $8.380967496607675\times10^{-17}$ |
| meanSecondCorrection | $2.088988907528698\times10^{-14}$ |

非均值 slope 和 second 的最大差都在第一个系数，即频率 2。全部 577×64 canonical 状态的最大绝对差为 $6.862071018076676\times10^{-6}$，在 node 10 的第一个 momentum 分量；该值不能被当作相同大小的物理位置误差。相应的原 RK12 到 RK24 canonical 差是 $1.1502295978971233\times10^{-4}$。原 RK12 到 RK48 的完整比较亦随包保存。

## 完整有限 DN Jacobian 仍有高频变化

矩阵尺寸为 98×32，原行顺序为 slope[32]、second[32]、meanSlopeCorrection、meanSecondCorrection、height[32]。slope 及 meanSlopeCorrection 使用原实际 shooting tangent 与准确 cut 链式法则；second/mean-second/height 沿用原实际 tangent graph 上的对称差分，原 difference step 为 $10^{-4}$，没有为本次比较另调参数。

| Jacobian 块 | RK24→48 最大绝对差 |
|---|---:|
| slope | 0.06710988733902923 |
| second | 1.5655088392086327 |
| meanSlopeCorrection | $5.933163682581011\times10^{-12}$ |
| meanSecondCorrection | $1.0491758586483185\times10^{-8}$ |
| height | 0 |

slope 和 second 最大差仍在频率 40 的对角元。该 slope 元从 17399.330725782973 变成 17399.263615895634；对应 second 元从 281406.930522667 变成 281405.3650138278。两个块相对旧块最大元素的差分别约 $3.857\times10^{-6}$ 与 $5.135\times10^{-6}$，不是机器精度。

相比原 RK12→24 的 slope-J 差 1.0621372059831629、second-J 差 24.777027686301153，本次两者约缩为 0.06318 倍；物理 slope 变化约缩为 0.05956 倍。这是本组三个有限步长下的实际缩小趋势，不能仅凭三层就把四阶渐近律或无限步长极限误差变成严格结论。原固定 H 处 base DN 已很稳定，也不能由此声称全部高频 J 的任意扰动响应均已机器精度稳定。

## 归档与继续范围

包 `notes/2026-11-14-exact-resume-fixedH-RK48-r1/` 保存完整 config/request/ready/response、solver result、实际 trace/stdout/stderr、两次已完成比较、工具真实退出和逐文件 SHA。新响应 SHA-256 为 `8943eb28a1913a7b9cbd390607c4dadfc6fc8eefa8604e403b798c494221dd92`；新配置 SHA-256 为 `2ffc5c2bf35caef2066e6137a78bcf8a24dd0ee008c9b8c3d8f01b0c30092ef4`。入口 `exact_20261114_fixedH_RK_refine.py` 及执行时源 SHA 在 intent/result 中。

真实退出后，`exact_20261114_RK48_cusp_pipeline_v3.py` 已自动启动从新 shooting 状态重建所有端点及真实十六分点、并在八级/十六级分别保留全部原 source 分段点的链。其后将同时输出原 prefix／固定 0.01 patch／未 patch 尾部的完整样本比较，位置、一阶、二阶差和实际整闭结果。这里没有把尚未结束的这些步骤写成完成。

原 A prefix 没有用新完整 DN/J 重解或重新接受；M40 等更高 Fourier 截断尚未由本条执行。全域原 prefix cut 平台仍为约 $4.77033\times10^{-8}$，原 prefix 容差为 $10^{-7}$，不能仅为追该不变平台而无限提高 tail RK。连续空间 reach、无限非线性尾存在性和本课题的大幅度完成门仍未由本条证明或达到。
