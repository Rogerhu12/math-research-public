# R142 / ASP：全 155 母格缺陷六球已成，保留真实失败并接同算子有符号回路

2026-11-27，visible-exact-astra-fb31ed6-20261127 / positive_inverse。

**实际结论。** [公开 run 45880363964/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45880363964)
已完成原比较算子的全部 155 母格、1,424 细格和 root97/outer96 共 193 个输出点。
六个完整缺陷球、完整源积分和及其读回后的 false 充分门已经原子保存。
本次承接原 76 个母格，只新算剩余 79 个母格的 1,348 细格；没有重新评价已接受源目标。
因而此前准备的 DP 并行源片续接对这个目标已无剩余域，**不得再启动**。

进程后来在 `core.read_spec` 的 `current file containment` 末尾检查失败；
真实 `actual_returncode=1`、`complete=false`、`proved=false` 和执行的
`scientific_complete=false` 全部保留。该失败不是预算届满、timeout 或取消，
也不是六球未完成。下文只消费保存事实，未改写失败状态。

## ASP.1　完整输入及真实执行身份

| 完整公开对象 | 字节数 | SHA256 |
| --- | ---: | --- |
| [actual-scientific-conclusion.json](../notes/low193_streamed_defect_ci/run-45880363964-1/actual-scientific-conclusion.json) | 65,855 | `a674a43c5d24e24a59499cb93b5f4c21e3786c8e97f126fca86de210f93468de` |
| [execution.json](../notes/low193_streamed_defect_ci/run-45880363964-1/execution.json) | 64,093 | `2254670ad25736632f4706039d308029c5cd5b6ed7e443d21a3bb4e0125347a3` |
| [本次固定 manifest](../notes/2026-11-27-low193-streamed-defect-after-45802396138-inputs.json) | 见该 whole 文件 | `f10490f5c4e4e7c6dc71d3dca78dad20354a37675a6b67e24d22606974134714` |

触发提交为 `0f3608fad5b825cb30a309ecf520765a9e5cb740`，实际科学 checkout 为
`9d775288a99a687f888d2a392ee900de59cc159f`。唯一子进程从
2026-11-26 19:01:42.781442 UTC 运行到 23:55:32.653130 UTC，墙钟
17,629.871663895003 秒，`child_timeout=false`。执行保存了 13 次实际 pull /
README 检查的链；保留的首条及最新三条 whole receipt 均记录两个 README 无差异。

输入是同一 WVC hybrid 中心：全族固定 η、原修复低系数、真径向长度、全部 mean、
真实 root97/outer96 混合边界和同一个正权 S。完整模型链仍为
`33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79`；
原 153 中心片、155 比较片、1,424 细格和 1,425 图表节点均保留。
本结论未把这一 hybrid 替换成新 compact mean-exact 中心或完整真实 DF。

## ASP.2　六个完整保存球及实际 false 门

下表是对 whole `certificate.defect` 中十进制整数球 upper 作精确有理比较得到的
便于阅读的上舍入数；完整中点、半径和指数仍以 ASP.1 所链原 JSON 为准。
这里的数值是相应计算上界的包围，不能反读为真实算子范数的下界。

| whole 字段 | 严格上界 |
| --- | ---: |
| `body_HS2_upper` | 4108.506944 |
| `root97_HS2_upper` | 96.073293 |
| `outer96_HS2_upper` | 1.662764 |
| `body_norm_upper` | 64.097637 |
| `atoms193_norm_upper` | 9.886155 |
| `complete_norm_upper` | 64.855555 |

原 body Neumann 门准确读取保存后的 `body_norm_upper`，其值约
64.097636021621827；含 193 点项的总上界约 64.855554884299896 是不同的量。
原门是 false，而 `strict_gate_uses_saved_decimal_upper=true`。
没有将较大的充分上界当作奇异性证明，也没有用一个合成 upper 减去另一个 upper
来造出有利的余量。

完整源积分前缀的 `complete_parent_count=155`、
`complete_refined_cell_count=complete_model_cell_count=1424`、
`whole_output_atom_count=193`，唯一角色为 `true_coefficient_defect`。
其契约仍为 `GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles`；
`all_real_radial_outputs_in_each_source_slice`、
`both_same_cell_signed_triangles_retained` 和 `whole_saved_prefix_readback_used`
均为 true。原 76 母格覆盖 76 细格，余 79 母格覆盖 1,348 细格，二者并成完整域。

## ASP.3　后处理失败不撤销已经原子保存的数学目标

原固定 owner 的 `finish_defect` 先把六球写入候选，完整读回并逐球验证包含性，
然后用已保存 body upper 判门。它把下列四者放进同一个再次验证的候选，再作原子提交：

1. 六个原完整球和使用 whole saved decimal upper 的标志；
2. false Neumann 门及不推出奇异性的声明；
3. `completed_targets=[complete_streamed_parent_true_hybrid_low_coefficient_defect]`；
4. `current_target=null`、`new_targets_completed=1`。

真实 actual 同时保存了这些事实、155/1424/193 完整源域和第 22 个门
`complete_declared_directed_certificate_branch_saved`。失败栈位于随后的
`for spec in manifest["files"]: core.read_spec(root, spec)`。因此准入这些原球不依赖
猜测内存、未公开 cursor、纯 counter 或不存在的完成标记。

这一准入也不会把程序失败升级成成功。后继保留整个 actual 和 execution，使用
既有 `completed_parent_defect` 对 `streamed_whole_six_ball_false_branch` 的明确分支。
原 `sources={}`、`whole_interval_transversality=null`，four-source/whole-point/CFB、
正族真实逆、finite-ρ 桥、原七端口和任一原 RHS 均未因此完成。

## ASP.4　直接后继是同一 body 空间上的新有符号量

[R149](R149-signed-Green-loop-and-symmetric-part-coercivity.md) 已证明，对同一个
\(\mathcal K=S\bar G\Delta S^{-1}\) 及同一个实
\(L^2(dr;\mathbb R^{193})\)，

\[
\left\|\frac{\mathcal K+\mathcal K^*}{2}\right\|_{\rm HS}^2
=\frac{\|\mathcal K\|_{\rm HS}^2+
\operatorname{Re}\operatorname{tr}(\mathcal K^2)}{2}.
\tag{ASP.1}
\]

因此旧 `body_HS2_upper` 可原样作第一项的完整 upper，真正尚缺的是第二项的
完整 signed ball。原 193 点输出已通过真实 Green 的边界进入该 body 核，但不把
点测量额外拼进取伴随的 Hilbert 空间。两 mean、原坐标归一、S、ordinary dr、
全点边界和原 varying defect 均不改。

后继目标唯一为 `complete_same_weighted_body_signed_trace_and_symmetric_part`。
它先保存/读回 signed trace，再形成并保存/读回新的对称部上界；只有该上界严格
小于 1 时，才按原 R149 定理消费 coercive resolvent。旧 ε 和原 false 门始终保留。
这一新目标即使失败也不证明奇异。原四源、点和高频反馈仍须各自继续完成。

具体 metadata 生成器为 [make_low193_signed_loop_manifest.py](../scripts/make_low193_signed_loop_manifest.py)，
传入 ASP.1 三个完整前驱路径。它导入的仅是 owner 的纯 metadata 准入函数，
本地科学评价数为 0。原 Green 的私有可重算数组未公开；后继按同一确定定义仅作
必要输入物化，不重新登记旧 Green、六球、QR/SVD 或任何旧成功范数目标。

新的 workflow sparse checkout 显式列出全部 manifest 当前输入路径，使每半小时
的 mandatory pull 仍保留完整文件；旧入口只列 worker/manifest，曾依赖范围外临时
物化。此处消除一个确定的后继文件保留风险，不把没有逐文件定位的旧末尾异常
伪装成已证明的特定缺失路径。旧 PS owner/math 和旧执行记录不因该操作改写。
新 signed-loop owner 的首次数学预算由 16,800 秒增为 19,500 秒，仍在其既定
20,100 秒 child timeout 和 350 分钟 workflow 范围内；此为首次新目标的执行预算，
未修改积分公式、全域完整度或任一原科学输入。

**scope。** 本篇完成的是已真实保存缺陷六球的数学归档及唯一合法新目标接线；
没有宣称 R149 的新门已成，也没有宣称本课题 README 的完成标准已达成。
