# B030：55be 真后继与 43015466 剩余 1906 原括号的实际续接

2026-11-28；会话 `Astra-new-mechanism-8cdb3418-20261128`。

本范围消费已经自然完成的 run `46123017949` / job `140911408687`，终态见同日 `r566-6482-to-55be-natural-terminal` note。入口 `scripts/r566_native_55be_partial1906_20261128.py`；只恢复必要真实状态与原 partial 工作队列，不重演旧科学扫描。

## 1. 原样保留的真实状态

保留 q=`55be941cbf3ff39b259713a5ecf264bddbc7ce934b2e7ac7436713d58396df63`，η=`0.1932424342521748`、原 g 精确 binary64 0、phase=metric，实际 trust=`0.45050811767578125`、retained working extra=`0.1932424442521748`。

原完整库为 904 coarse / 1810 fine、2020 物理峰、601 working 行、uniform=1536；真正已接受的独立 fine 资格是 **1786×3072**。两列表 **2 physical / 8 working pending** 暂不应用，先完成候选在原库上的资格。原 H 82 维、packed LDL 3403 项、23 个 pending 非零乘子、原固定乘子梯度/J/QP 锚与 metric 语义全部恢复。没有声称恢复未保存的完整 Jacobian 或 native 工作数组。

所有源费用保留：新近 2370.609989817 秒、4 metric+1 restoration、15 完整 J/1290 块、全部祖先费用与原截断未知量；不能把源 partial 的已付目标计算算成零。历史 309b8 的已闭 4465 / 未执行 8635 仍留在原绑定输入，继续不执行、不删除、不宣称已闭。

## 2. 仅续真实 1906 队列

候选 q=`43015466eb4f1818628178bf8f900cba2304fcd74753bab5759f214ff188dd23` 是原 **half-backtrack**。原 working、physical box、全部 coarse、1810×3072 fine 和 nested 比较已经完成；其 fine η=`0.19294084341286163`、g=0，尚有改善可能。现有部分没有充分拒绝证据，不能套用旧 known-violation fail-fast。

原定位共 2810 个候选，904 已闭，1906 尚未处理。原完整 PARTIAL 字面 JSON 是 580912 B / `fb72d7582afccc1843210d7fbc4adbb2104b73cb8bfed6b7f8c8a166c89b37af`；其中 904 已闭峰的 canonical hash 为 `5aa58a88ad8b37a8be143ad96f2c1f32df233586677463175e727c9e2825d820`，1906 队列 hash 为 `4b9352eb53d41f3c8a9f766d89a1d57e64d870943c0aab1cfe38fbee2246160d`。

请求只新增必要的 904 峰记录和 partial 元数据；q/fine/remaining 与完整 FINAL 共用。同一 canonical 重建逐字得到上述完整原 PARTIAL，防止前缀和剩余队列错配。通过冻结 `r566_saved_partial_queue_20261127.py` 在同 q、同 oracle identity、同 1810/3072 网、同原四轨道目标上消费仅剩 1906；不重新枚举候选、不重做 904 个已闭括号、不重跑 coarse/fine/nested。必要 oracle/FFT 重建是本次真实费用，不能冒称旧数组已在内存。

中断发生在一个未闭候选内部，该候选内部未保存的优化器响应不被伪造；其原 8072 次总目标求值与 32.787831607 秒完整留在源账本。后继若再被时钟截断，则新已闭前缀、原剩余队列、实际 q、两 pending、H 与全部费用仍完整保存。

## 3. 结算真实原 metric 接受，不预先接受

复用已发布 `r566_partial391_physical_resume_20261127.py` 的 metric partial 结算规则，并保留当前 exact-g 语义。合并全部已付与新完成峰后，重新依据真实 maximum 判断几何、η 与完整资格；原 working、physical box、coarse、fine、nested 条件全部保留。

如果实际 η 需要更高的辅助 epigraph，只改变独立 e，并记录抬升：同 q 的原 metric 行为 `e−field`，在已付较小 e 合格即意味着在较大 e 合格；几何行、物理盒与目标 η 本身不变。这条准确单调性允许复用已经支付的原行，不需要重扫原完整网，也不把 epigraph 抬升算成实际 η 改善。

全部原/新违反坐标继续加入 physical/working pending，即使抬升 e 后已被覆盖也不丢掉其交换证据。真正接受仍要求完整定位闭合、原几何与 margin 合格、nested 合格、metric epigraph 覆盖实际峰、η 严格小于保留 η−1e-12。只有此时才以候选替换 55be，并将其实际 1810 fine 资格登记为新的已接受资格。

若候选最终不合格或没有严格改善，保留 55be。任何情况下，剩余队列未闭都不接受，也不捏造候选的完整科学终态。

## 4. 原 source outer 的真实 trust 后决策

源 outer12 完成时已经是同一 55be、4 metric+1 restoration；outer13 进入后的接受计数仍相同，所以其此前确实 0 次接受。新范围先结算此次半步候选，才完成这个原 outer 的后决策。

用原尺度 `.5/.2/.15/.1` 与原 backend seed 计算**实际新接受位移**。若确实接受且该位移达到 `.9×actual_trust`，才按原规则提到 `min(maximum_trust,1.5×actual_trust)`；否则保留实际 trust。source 没有自然 native 返回，且已有原 pending 交换；不能假造一个自然返回、空 pending 的失败来缩 trust。

这项后决策与“恢复旧 native 运行栈”不同。未打印的 native 工作数组始终不可用；完成原 callback 的物理判断后，按实际 pending 交换进入新的原 backend，使用被声明为启发初始化的真实 H/pending。行函数或 phase 改变时仍由旧 helper 按原语义 reset；不因新 session 名称而 reset。

## 5. 接下来的原完整求解

从 `for outer in range(args.outer)` 起，完整正常 loop、callback、working 回溯、所有物理/coarse/fine/localizer/nested/margin 门、完整 J 构造、native 历史策略与 retirement 与已发布 6482 driver 的 AST 完全相同。新增内容只处理这份真实 source、已付前缀复用及被中断 callback 的实际后决策。

原 2400 秒预算、30 秒 final reserve、全部原物理及 solver 参数保持，公开 Actions 运行；本地只解析已完成日志、构造/检查源码和请求，不执行科学计算。原日志、轨迹、完整 J、native 工作区和可重算大表不入库，必要续接状态进入压缩请求。

这不是新固定度量等距族或连续 reach 证书。B030 仍是静态设计搜索，原 README 完成标准不变；候选结算后继续下一个真实 outer，不在阶段结果上停下。
