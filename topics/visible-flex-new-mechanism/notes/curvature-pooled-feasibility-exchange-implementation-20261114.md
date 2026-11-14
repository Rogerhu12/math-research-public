# 曲率交换的池内可行性恢复：同度量续求实现

日期：2026-11-14。新增两个独立脚本；原曲率计算、恢复脚本及全部冻结几何源码保持不变。当前本地执行器不可用，本文提交时新人工路径尚未执行，须由公开 Actions 的同一任务先运行人工入口。

## 1. 已保存的实际历史支持这项具体修正

原曲率 run43645177423 的完整报告经 artifact 原字节恢复。随后公开只读 run43647629532 提炼其已有历史，没有重算几何：

[完整 trial 诊断](actions-43647629532-1-curvature_trial_diagnostics/curvature-trial-diagnostics.json)，66,170 B，SHA256 为 d25d0ac3ff7bb86317c3b8929f4a5bfc22f4bc8db85e5e49eee652c5c2f20038。

它保留 61 个辅助/物理向量评价。20 次两步交换触发时，当前已经入池的行仍全部存在违反；对应违反数依次为：

$$
124,\ 111,\ 146,\ 106,\ 132,\ 140,\ 166,\ 186,\ 248,\ 198,\
216,\ 192,\ 250,\ 198,\ 222,\ 208,\ 232,\ 226,\ 198,\ 216.
$$

这不是仅有“尚未加入的行”需要补齐。最后一次触发时，池内尚有 132 条 metric-minus、58 条 metric-plus 和 26 条 curvature-plus-determinant 违反；池外只有 24 条 metric-minus 违反。原回调未区分这两种原因，始终在两个 major iteration 后结束当前 SLSQP 并重新初始化下一次调用。

曲率最低的试探约为 39.282，但 $\eta\approx1.170$，不能接受。更接近预算的物理评价 38 达到 $\kappa_{\max}\approx53.6252$、$\eta=0.26720664534367655$，超过固定预算 $0.2672$ 约 $6.65\times10^{-6}$；它通过帽高、盒、正高度、球、条带及镜像对筛，但仍有 208 条池内违反、4 条遗漏违反。没有将它重新标记为可行。

这些数据足以支持“不要在当前池仍未恢复可行时仅因遗漏行抢先重启”的算法改动；尚不能证明该改动必定降低曲率，也不能据这次失败宣称固定度量连接不存在。

## 2. 新策略只改变交换调度

库为 [frame_curvature_feasible_exchange.py](../scripts/frame_curvature_feasible_exchange.py)，实际 driver 为 [frame_curvature_feasible_exchange_audit.py](../scripts/frame_curvature_feasible_exchange_audit.py)。

几何评价、实际第一/第二基本形式、四个曲率 PSD 行、完整二阶 jet Jacobian、16 行分批方式、单一共同高度原函数及所有候选筛选，均继承已公开的上一版本。

每个回调仍评价同一完整 $160\times384$ 网格。设当前已入池索引集为 $P$，十一组原始数值容差为 $\varepsilon_g$。只有同时满足：

$$
c_j\geq-\varepsilon_{g(j)}\quad(j\in P),
$$

且原帽高/盒检查、独立正则性检查通过，才把当前池标记为 ready。这个标记不是全网可行结论。

达到原最少两个 major iteration 后：

- 若当前池不 ready，即使池外存在违反，也继续同一次 SLSQP，让它保留本次迭代状态恢复已强制的约束。
- 若当前池 ready 且池外存在违反，才触发交换。
- 若当前池 ready 且没有遗漏违反，不因交换机制中断。
- 若优化库自行返回而当前池仍不 ready，明确保存“library-return-before-enforced-pool-feasibility-restored”并停止这次阶段；不把它转换成成功，不借重新启动掩盖失败。

回调和库返回两处都用原实际组容差收集遗漏。特别是 metric 使用原 $10^{-9}$，不再用旧回调的 $10^{-5}$ 宽触发阈值。处于两者之间的遗漏仍会补入；最终完整网格筛绝不放宽。

每次回调会记录池内各组最小行、违反数、ready 原因、遗漏数以及是否继续同一次 SLSQP。这样下一实际结果能够判断修正是否确实让池内恢复，而非只得到更长的运行时间。

## 3. 从合格原态复用已学的行

本次初始物理态仍为完整合格的

**e407a21488257097f60073f7e46e19f987dc963760957040ee7254a02889beb4**。

不使用任何旧不合格 trial 作为 warm start。新增第十一输入为已经恢复的原曲率完整报告：

- 原计算 source：2f1b809c0b0abb7a26303d36940edc203815f872；
- 原报告 raw bytes：5,220,015；
- raw SHA256：5b04d6a7c85870687b979bbda87bbf8bd4d429d3b36c918d83cebde59b4dcaa0。

前十输入仍按原严格链恢复。新增 loader 检查原曲率实现、配置、完整前序输入、初态/末态、全部准确系数、同 $g$/同高度基、两套角网格物理筛，以及完整值网格定义。

它只复用原报告末次保存的 **3,866 个行索引**。检查包括索引 SHA、唯一排序、范围、十一组顺序、索引展开规则和完整网格身份。池是评价/约束调度的一部分，不加入物理场身份。新 pool 不丢弃这些已学行，后续仍按原规则单调补充。

新辅助 $\lambda$ 仍按已公开规则由两套原曲率最大值加明确余量初始化。旧 raw $\lambda$、旧失败的 metric $\delta$ 和旧阶段退出原因作为来源保留。后续若补入新行，辅助变量的显式重设仍单独记录；最终细网审计不抬高选中态的 raw $\lambda$。

## 4. 原科学门和预算保持

本次没有放宽：

- 固定度量预算 $\bar\eta=167/625$；
- 原 $g$、固定高度基、163 个物理参数及其盒；
- 帽高线性门、正高度 $10^{-4}$、球半径 $101/100$；
- 内条带 $38999/100000$、外条带 $39/100$；
- 镜像对 $\tau=61/1000$ 的必要筛和独立非退化检查；
- 最多 80 major、120 次物理评价、300 秒优化时间、20 轮的共同预算；
- 全网独立 best-physical 与辅助可行 best 的分别保存；
- 最终同一参数在 384/768 角网格上的位置二阶 jets、实际度量、主曲率、镜像、形状及 raw 辅助量审计。

初始加载、几何预构建和导数准备仍与优化计时分开，总过程时间从 main 入口计算。池内可行不替代完整网格选择；曲率及镜像点对通过也不构成完整曲面 reach 证书。

## 5. 新人工覆盖的范围

公开人工入口不重跑旧研究状态：

1. 纯数组验证：池内违反阻止交换，帽高/盒失败也阻止交换；遗漏 $5\times10^{-9}$ 必须被原 $10^{-9}$ 容差发现。
2. 两标量问题验证真实调度：最小化 $\lambda$，约束 $1-x^2\geq0$、$0.8-x\geq0$、$\lambda+x-2\geq0$。后一个空间限制先留在池外；检查同一次 SLSQP 在池内违反期间继续，池恢复后才交换，最终解到 $x=0.8$。它只是调度 toy，不是曲面。
3. 新完整 I/O 路径用小人工几何构造第十一报告，核准确池复用、同态/同度量、错误 SHA、坏索引、变网格、变物理态拒绝及失败小 JSON；evaluation-only 路径不调用研究优化器。
4. 新报告与摘要字节绑定及最终同态角精化路径被实际调用。

提交本文时这些新检查尚未运行；不能用旧人工 passed 代替本次回执。

## 6. CLI

同一个公开 Actions job 先调用：

    python scripts/frame_curvature_feasible_exchange_audit.py \
      --check-only --out "$VISIBLE_NEW_OUT/curvature-feasible-development.json"

实际调用保留上一曲率 driver 的全部十组 path/SHA 参数，再增加：

    --curvature-audit topics/visible-flex-new-mechanism/notes/actions-43646786908-1-curvature_output_recovery/curvature-epigraph-exchange-audit.json.gz
    --expected-curvature-sha256 5b04d6a7c85870687b979bbda87bbf8bd4d429d3b36c918d83cebde59b4dcaa0
    --out "$VISIBLE_NEW_OUT/curvature-feasible-exchange-audit.json"

只有新的同度量曲率阶段被调用；不重新执行原 metric 或原 curvature 优化。原报告的提炼、原失败事实与已恢复科学字节均保持。
