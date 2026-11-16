# R601 — 实际 R580/R596 同对象 C0 与 world C1 组合接口

作者：ChatGPT /root（AI），2026-11-16。可信度：完整作者源码与条件证明；尚无实际执行。

## 1. 交付与固定父源

源码：computations/geometry_20261116_actual_analytic_saved_RHS_C1_defect.py  
源码 bytes：23113  
源码 SHA-256：12450be1cbdd289b69f74535d98fa42586506709244ed066b338c98cd494490d  
schema：R601-actual-analytic-projection-saved-RHS-world-C1-defect-v1

完整证明：[R601 同一实际残差与完整解析投影的 world 角导数界](../results/R601-actual-analytic-projection-and-saved-RHS-world-C1-defect.md)。

| 实际对象 | 必须实际加载的源 | 完整 SHA-256 |
|---|---|---|
| R580 BoundAnalyticProjection | geometry_20261116_same_evaluation_analytic_angle_projection.py | 0abe4629415a0e9219a50cf248f30bdceb9819b4338189b811101bdadf3d543f |
| R596 BoundSavedRHSDefect | geometry_20261116_actual_saved_RHS_reference_defect.py | 8a242686845844df64d248b7b9fd47096ff2c7a8c2044346c85fc9b7425afb3f |

调用者继续完整登记原 R575/R553/R521、R596 已核四个原 flow 来源、真实 checkpoint、原同次 cubic capsule 和 deadline。R601 不复制这些数组、不另导入原求解器、不另选择 C 根或初猜。class owner 的真实 module/source/file/class identity 会在构造时核验；同名不同字节不接受。

## 2. 只绑定真实对象

~~~python
observer = module.bind_loaded_continuous_RHS_C1_defect(
    actual_R580_observer, actual_R596_observer)
binding = observer.describe()
~~~

两个参数必须是固定源定义的实际对象，且：

- actual_R580.reference is actual_R596.projection，即同一个实际 R575；
- tubes、field、current、api 都是同一个对象；
- M、N、3M+2 layout、sqrt_bits 和已保存在对象中的原 budget callback 相同；
- R596 的有限参考实际 sigma=+1；
- 原 R580、R596 的完整 describe 身份绑定。

没有 h、C、eta、A_lower、rho_lower 或 anchor 参数，也不接收调用者编制的 summary。所有新界从这两个真实对象在本次结束点返回的原数据中取得。

这里的固定正支是原准确 finite FFT 参考的分支，不声明识别了 native DtN worker。反射和坐标转换按完整证明中的实际分支合同另付。

## 3. 原 cell 路径全部保留

原 caller 继续在原同一次 R553 记录上运行 R580.inspect，并在原 DFS 退休点运行 R580.commit_original_retirement。R596 的实际 cell/完整 N 点有限参考及原 retirement 亦保持。R601 不拥有 cell、split、closed root queue 或任何新 ledger。

本组件只接管两件的原 finish 位置。不能在原 R580.summary 已经完成以后再调用本组件，否则会把它的全局解析界重新算一遍。实际新 view 必须按完整 literal plan 将该结束位置替换，并保原别的消费者顺序。

原 R575 的独立诊断仍是原 caller 的责任；R601 不要求它的 B2 可用或通过。它也不要求 R596 的 literal cubic 或每个mesh节点形成摘要成功作为 Q 全域缺陷的新门。

## 4. 唯一实际结束调用

~~~python
combined = observer.summary(
    original_coverage=coverage,
    complete_cell_ledger=cell_ledger,
    original_error=error,
    original_stop=stop,
    close_errors=close_errors)

analytic_summary = combined["actual_R580_summary"]
saved_rhs_summary = combined["actual_R596_summary"]
~~~

上面两个赋值是引用本次真实返回的完整原对象；不是分别再调用一遍原 summary。

summary 内部顺序为：

1. actual R580.summary 使用原 coverage/ledger/error/stop/close_errors；
2. actual R596.summary 使用同一参数，不传 optional actual_projection_summary；
3. 原全域标志与完整退休计数均已付时，形成新的 C1 和组合；
4. 完整保留两份原 summary 的所有字段，加入组合是否已付、当前错误和未完成操作。

原 R596 不接另一个 R575 composition 参数，所以本组件并未同时形成两套不同 projection gap。R580 已有四个完整 power/sum enclosures 直接用于导数尾，不重算 Taylor/exponential/power sum，不增全 N 网格。源码新工作只是明确有限个准确有理组合及一次原 R521 sqrt。

## 5. 当前 complete 的严格含义

complete_prefix_physical_RHS_C0_and_world_C1_bound 只在当前完整组合返回时为 true。它要求：

- completed_all_DFS_work=true、完整原 ledger 非空；
- 当前原 error/stop/close_errors 为空；
- R580 actual complete analytic projection、整个 R553 cover、全解析终叶及退休责任完成；
- R596 actual complete finite quintic residual、完整原 closed DFS 及退休责任完成；
- 两者 observed/committed/split/terminal 逐项等于同一实际对象计数；
- 所有完整来源、grid、layout、正 gap、原真实 extrema 一致。

原 R596 summary 的 ledger 字段是 complete_cell_ledger，R580 为 complete_original_cell_ledger；源码分别核真实字段，不根据另一个 schema 猜同名键。原 coverage 对象不被替换成只有 completed=true 的手制字典。

若这些前提未付，complete_prefix_bound 为 null。原两份 summary 保它们自己已付/未付的全部范围，partial maxima 不升级成全域常数。某个可选诊断没有global bound，不作为原场或 BVP 的数学拒绝。

## 6. 新完整结果中的主要字段

| 字段 | 准确意义 |
|---|---|
| actual_eta_Q_upper | 原 R596 全系数、全闭单元 finite 残差界 |
| complete_coefficient_C0_norm_upper | 原 R596 已向外形成的完整合成常数 |
| complete_coefficient_world_C1_component_weights | M(M+2)、(M+1)^2、M(M+1) |
| complete_coefficient_world_C1_norm_upper | 三条完整权平方和平方根的原有理上端点 |
| actual_projection_world_C0_upper | 原 R580 已形成的完整 C0 projection defect |
| complete_rotating_derivative_tail_upper | 所有无限 Fourier 尾的加权导数界 |
| complete_all_retained_alias_derivative_upper | 原全部 alias_upper_used 乘2M后的向外上界 |
| complete_world_projection_derivative_upper | 上两项及原C0连接项之和 |
| complete_prefix_unprojected_physical_RHS_defect_upper | 同一准确 prefix r=X_s-V_+ 的world C0界 |
| complete_prefix_unprojected_physical_RHS_world_phi_derivative_upper | 同一r的物理角world导数界 |

角单位始终是物理 phi 弧度；径向始终是原numeric prefix s。q 或共同材料坐标的真实链式因子不在本组件中被默认为1。原rho/BC锚/径向积分没有新数值输出。

两件原 summary identities、完整源binding、当前ledger和field dimensions一起保留。identity只用于定位完整对象，不替代两份原summary或大ledger的真实内容。

## 7. 向外算术与原预算

原 R580 形成的独立 gap_lo>0 必须保留，即使其 r_hi=1。不能用1-r_hi并误报division/domain失败，也不能向下截断正数。新的 weighted tail 使用全部非负项，随后每次 relative_dyadic_bounds 只取上端点；系数常数用已绑定的 R521 sqrt。

work 在每个新运算阶段先记录真实 operation/position，再调用已有原预算回调。未新设deadline、reserve、进程或重试策略。RuntimeError及MemoryError不被普通错误处理吞掉；原 ResourceStop 沿原调用栈传播。

普通的算术/来源结构错误记录完整 type/message/traceback和实际unfinished operation；不造一个零上界。原两份summary中的错误与当前formation_error分开保。

## 8. 原停止后的恢复

若第一次结束在原全局解析界或新C1形成中收到原 ResourceStop，原 caller 必须先记录这次真实 stop/error，再调用相同 summary 参数的恢复路径。

第二次调用只有 original_error、original_stop 或 close_errors 实际非空时才允许。此时原 R580 既有完整条件为false，只做元数据；R596亦只形成其原元数据摘要，R601不重试任何界。actual_unfinished_operation保第一次真实进展，两份原summary保原未访责任。

若此前已经有完成组合、随后出现原错误，previous_completed_composition_not_current_after_a_stop会明确把它标作历史值；当前complete仍false。不能拿历史成功掩盖本次error，也不能对第一次超预算再开一个较长clock。

## 9. 必要读回与来源级联

后继 actual caller 必须独立登记本源的完整 bytes/SHA，并让同一次实际 R575 的 R580/R596对象进入本库。新source basename与完整 literal replacement/count/生成identity按真实祖先另刊，不原名覆写运行中的源码。

两个原summary全体保留，包括未识别键、原formation/unpaid、same-call cubic来源、所有计数和scope。它们可能使实际整份necessary超过90000；原wholebody/70仍严格执行，不拆包、不提高cap、不把某个旧overflow当fixture，也不允许只返回成功字段。源码本身不实施任何关系编码或quiet/cleanup判断。

本组件没有CLI、workflow、dispatch或文件写出。大数组和cell ledger仍在原Actions临时生命周期；Git交付仅本作者源码/证明/接口。

## 10. 不曾执行与未付责任

本组件目前未执行，没有本地科学算术/import/AST/compile/test/fixture，也没有增加独立科学前门。完整证明给条件包含关系，不说明已在某个实际field取得E0/E1。

后继仍须真实支付：A*rho全域正分母、原BC/cuff锚、完整径向路径；tail/collar/cut-patch/帽各自的准确参考；native worker自身分支与形成差；完整闭场relative metric、reach/held/反射距离和同一g的实际精化。既有R514/R519/R459可独立继续，本C1路线不升格为README的强制前置门。
