# 同一背景的低 metric 供应包完成记录

状态：**已审方法生成的完整局部供应包；新候选全域 metric 仍由独立后端另报。** 本文不是课题收尾；README 的固定度量精确解近似门仍由真实频率/求解序列推进。

作者：`/root/tail_theory`，2026-11-09。

## 1. 固定对象与选择依据

所有新包都供应同一个已冻结旋转背景，使用同一有限 160-cell 校准表、同一精确积分定义的 $\alpha$ 以及同一个 depth4 primitive。depth4 的 36 个 profile 及全部叶已由 `independent_geometry` 独立重放，前 18 个与旧 depth2 表逐值相同。物理网格基准仍为已认证 M8/int2 manifest；后续只用已审精确物理半径转移工具换到新图网格。

必要范围来自 `db6f-audit-background-refinement-plan-m8.json` 的 $2\cdot10^{-10}$ 供应误差分配。该分配是工作预算，不是实际残差下界。未据此重跑无关的全部背景。

## 2. raw2/raw3

- raw2 的 `[2898,3477)` 共 579 个原 span，生成 736 盒。四个 cap 分支宽 hull 由已审单点 Lipschitz 包替换，分割与全部 $w_r$ 系数逐字不变；其余两盒虽未满足原统一 $10^{-6}$ 工作宽度，独立实际高度敏感度预算确认足够，无需继续细分。
- raw3 的必要范围为 `[2319,2401)` 和 `[2548,2898)`，分别生成 83 和 423 盒。第二段两行用相同单点方法收紧后，全宽都不超过 $6.826\cdot10^{-6}$，达到该段 $10^{-5}$ 工作阈值。
- 这些计算均实际退出 0。point-Lipschitz 全文/实现/完整 736 行及 raw3 应用均已独立重放。

正式输入分别为 `db6f-tail-background-lowmetric-raw2-point.json`、`db6f-tail-background-lowmetric-raw3a.json` 和 `db6f-tail-background-lowmetric-raw3b-point.json`。

独立后端已经将它们转至第一档 M12 critical 图，并在相关完整区域的 7,393 盒上得到 raw2 metric 上界 $1.755\cdot10^{-11}$、raw3 上界 $3.806\cdot10^{-10}$。选区首跨所含未修 raw4 带来约 $1.132\cdot10^{-9}$ 的总界；它不属于新 raw2/raw3 包的失败。正式报告为 `db6f-audit-metric-r23-m12-critical.json`。

## 3. raw0：两个严格求值改进

工作中识别了两种独立的证书过宽来源，均在新文件中修正，旧冻结供应器保留不改。

第一种是 cap 分支交界。cap 对数中支与两外支的差分别有 $t^5$ 和 $(1-t)^5$ 因子，因此源 $w(x)$ 跨界仍是 $C^4$。逐点分支 Jet hull 包住四阶导数，允许使用四阶 Taylor 余项；不能把同样结论套到含 $|w_x|$ 的 $A$。root 已全文审查并独立重跑真正跨 cap 的三盒 pilot。

第二种是近似反解跨过大量很小的 primitive 叶。原供应器合法退回全盒单调界，但会丢掉径向相关性。新方法令 $\rho=R(X(\tau))-r_l-\tau\Delta r$，用

$$
\|\rho\|_\infty\le
\max(|\rho(0)|,|\rho(1)|)+\tfrac12\|\rho'\|_\infty,
\qquad
\rho'=(A+\alpha B)(X)X'-\Delta r.
$$

它只用 $A,B$ 的值域和 Bezier 导数范围，不要求它们高阶可微。root 已全文/代码差审，并独立重放全部 86 盒的正式 raw0 pilot，数组逐字节同，工作未达数为零。

对应完整证明是 `db6f-tail-cap-c4-taylor.md` 与 `db6f-tail-background-first-derivative-phase.md`，最终生产器为 `db6f-tail-background-packet-phase.py`，SHA256 `97b8cd525586851c1e726e101db0f586518d260898fcaa6842c363ca050bc807`。

## 4. 全部 162 个必要 raw0 原 span 已生成

`db6f-tail-background-ranges.py` 按已有预算文件顺序执行 13 段，共覆盖 162 个原 span，不改变待证有限图。工作全宽设为 $4\cdot10^{-9}$，小于独立预算给出的约 $9.112\cdot10^{-9}$ 充分宽度。整个序列实际退出 0，生成 1,106 盒，运行约 625 秒，最大子进程 RSS 94.3 MB。

账本 `db6f-tail-background-lowmetric-raw0-phase.json` 已 `finished=true`，逐段保存输出文件、hash、退出码与全部设置。原第一轮仅 span 4407 的 $u\in[0,1/1024]$ 一盒未达工作宽，其实际供应预算也超线。按独立后端建议，只对 4407 整个原 span 把最大验证深度从 10 增到 14，得到 `db6f-tail-background-lowmetric-raw0-fix4407.json`：33 盒、工作未达为零、最大全宽 $3.905\cdot10^{-9}$，实际退出 0。

最终组合规则明确：先依账本覆盖 13 个完整原 span 区间，再用 fix4407 的完整 `[4407,4408)` 覆盖该原 span。不能拼接半个未完成 span。其它输出不改；旧的宽盒与失败记录全部保留。

## 5. 后续认证范围

新 $w$ 包用于 actual metric-only 后端。第一档 M12 critical 的同一 manifest 已由完整独立后端给出实际曲率上界 $8.4625591$，覆盖 29,023 盒及 R6 collar；这个旧曲率证书可以与新 metric 证书合取，因为图和真实背景没有改变。无须因新的 $w_r$ 工作范围较宽而放弃已通过的同图曲率结论。

13 段与局部修包正在交由 `independent_geometry` 完整覆盖、精确换网格和实际全域 metric 验证。工作宽度本身不代替这一验证。本文也不支付源 Galerkin/ODE 误差、真实无限尾存在或 README 的全部完成门。
