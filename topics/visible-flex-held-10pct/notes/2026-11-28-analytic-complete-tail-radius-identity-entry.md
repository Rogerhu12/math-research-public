# 完整 unscaled 尾场的半径图恒等核验入口

独立入口 [`verify_complete_tail_radius_identity.py`](../scripts/resume_20261128/analytic/verify_complete_tail_radius_identity.py)，SHA `4c775e4333d789d5481531316d02e02a974212997eb6c14b2d9f99f7f7281116`。它只核验同一实际完整尾场的保存半径与物理切口半径相等是否使 near-cut 半径重参数恰为恒等；不继承旧尾场的 metric、曲率、嵌入或整个闭曲面结论。

## 两种诚实输入来源

`verify` 子命令需要 `--geometry-bundle --source-run --constants --normalization-certificate --outdir`；真正耦合场还必须给 `--coupling-summary`。

无 coupling summary 时，使用原 `accepted_original` 门，H 定义来自实际接受原设计源的 `raw_return.candidate_H`。有 coupling summary 时，独立调用 `actual_cartesian_coupled_prefix.accepted_coupled`，H 定义仅来自其 full-height binding 的最终 physical `candidate_H`。后者与 raw candidate 即使只差舍入，也不替换使用；实际 bundle 必须绑定同一个最终 physical-endpoint packet。输出用不同 `source_kind` 区分这两种来源，不改动原 actual-tail flags，不把耦合场冒名放行给 `accepted_original`。

两种分支都要求原 `seam_certify_tail_geometry_v2.validate_inputs` 通过、字面 factor = 1、`factor_exact_binary = "1"`、unscaled role/verified 标记一致，并重新核 reference、request、checkpoint 的完整 H 与该源定义逐位相同。仅把另一份已缩放 H 命名为 reference 不能通过这些绑定。

完整 bundle 必须包含所有 finite stages。入口使用真正的 `ActualFiniteTailV2`，重新核所有 stage 的完整平面／高度谱、字面公共二阶 jets、未重置的累计 mean，并将重新生成的 canonical index 与绑定原 index 比较。没有构造大 prefix geometry，没有执行原 BVP 或 native solver。

## 半径等式及结论范围

从 stage 0 的真正外端节点取得字面 binary `radiusJS`，记为精确有理数 c；将其与物理参数的字面 binary rCut 记为的精确有理数 Rc 比较。同时核 actual cap.c、canonical cut index、原 port 与同一 R58 constants 里的相应值。

只有 c = Rc 时，才依据已绑定并审核过的 `ActualCutTarget.perturbation_radius` 实表达式得到

\[
\delta=c-R_c=0,\qquad r(R)=R,\qquad r'(R)=1,\qquad r''(R)=0
\]

在整个声明域上成立。脚本对该 live 半径方法的少量数值调用只是附加诊断，恒等结论来自字面有理等式和方法公式，不来自抽样。为防源定义悄然改变，核验当前 cap constructor、cut target constructor 和半径方法的已审 AST 源 SHA；改变这些定义需显式新审查。

若 c ≠ Rc，输出 `validated_complete_bundle_has_nonidentity_radius_chart` 并返回 code 2，明确标记仍需单独重参数传递；不会把一个小差当作 0。半径相等本身不支付该实际尾场的连续 metric/curvature、prefix attachment 或 embedding。不存在完整真实 bundle 时，正向门尚未实际执行。

## 已执行的真实半幅负向门

当前仅用真正已接受的 D/M24 半幅 packet `tail-mild-modes-20261128-d/m24/tail_0001.json.gz` 做负向检查，packet SHA 为 `1cb9a3ae6a0aa943fa8f305e0ce52b7028650210244e942df2794aa0b970b306`。原有限 residual 为 3.1311279019737547e−10，参考 H 为 `tail-adaptive-fullheight-20261128-a/height-reference.json` 的 `candidate_H`，实际请求为原 numpy 算术 H_j·.5^j。

`negative-warm-check` 实际正常退出 0：原 `bind_height(.5)` 绑定得到 warm 身份后，被新 unscaled 门明确拒绝；对同一真实 packet 直接调用原 `bind_height(1)` 也因请求 H 不同而拒绝。没有制造正向 packet/bundle，没有改 reference 或复写接受标记。峰 RSS 32524 KiB，用时 .08159895999961009 秒。

完整负向记录见[相邻 JSON](2026-11-28-analytic-radius-identity-negative-warm.json)，SHA `ed8564c03736711f62135b8838329f146aedacbc135bbfc233de94ab53762186`。源码整体可执行，负向入口真实验证；完整 bundle 的正向半径恒等结论仍待真实 factor-one bundle 到位后执行。
