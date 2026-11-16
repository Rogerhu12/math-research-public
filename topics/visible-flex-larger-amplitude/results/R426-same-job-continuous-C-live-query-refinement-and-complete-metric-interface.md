# R426：同一 C 现场闭查询精化与完整相对 metric 接口

作者：OpenAI / ChatGPT exact_refinement agent  
日期：2026-11-16  
状态：独立源码及条件包含论证；尚未执行、导入、AST、编译或科学计算；没有实际新场、精化结果或通过结论。

## 426.1 当前缺口与本次范围

[R418](R418-current-C-complete-closed-relative-metric-source-interface.md) 已给出真正 R416 当前场的完整闭面相对算子 metric 消费者。它从同一实际 C 的 result、input-binding、query-plan、query-results 取得完整查询包围。空间 cell 继续细分时，这些原查询盒不自动变窄；单靠更多空间格不能保证消除这项依赖宽度。

本次给出可以在同一公开 Actions job 内直接调用的两个新源。它们保同一冻结十参数场、原准确目标、原 C、原全部深根族、原所有支撑/片/均值/物质角/切端、完整双活动片和两帽。新增行为只有：原尾部 cell 尚未获证时，用该 cell 的准确闭径向区间调用原 f12f **QueryCover**；把新完整包围与原完整粗包围求交，再用原四个 R251 Loewner 条件检查同一 cell。

这不是新的 native、FD、RMS、BC 或全 DN 接受条件；也不把新的分辨率目标变成 metric 证明前门。缺少新增原件、预算不足或精化未付时，原已经完整的粗包围仍有效。原 C 的运行、数值 shadow、所有参数及根选择不被替换。

## 426.2 冻结文件与真实来源

| 文件 | 字节 | SHA256 |
|---|---:|---|
| [同现场 provider](../computations/geometry_20261115_same_job_C_live_query_provider.py) | 31603 | `07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9` |
| [独立完整 metric 入口](../computations/geometry_20261115_current_C_ten_live_query_complete_metric.py) | 55040 | `77be1d98c7401c4d0962adae7b824fd22c66b3a0127885b080859edc0f4a7892` |
| 原 R418 metric 基线 | 49975 | `28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590` |
| 原 f12f 完整连续 C | 89307 | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |

独立入口的直接闭包保持原 R418 六源全部同字节：

| 角色 | basename | SHA256 |
|---|---|---|
| R416 准确场 | geometry_20261115_current_C_accurate_cut_patch.py | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| 完整十族 prefix | geometry_20261115_continuous_ten_frozen450_prefix_metric.py | `011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84` |
| 原四 Loewner 条件及闭分格 | geometry_20261115_shared_field_relative_metric.py | `a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17` |
| 原连续 C | geometry_20261115_stored_continuous_E_cover_v3.py | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| 原 cuff 图册 | geometry_20261115_current_C_original_cuff_target_atlas.py | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| 原完整两帽 | geometry_20261115_current_C_ten450_fixed_cap_balls.py | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |

另加本 provider 和原 R418 源身份，共八个直接被核源文件；入口自身另记完整身份。原 R418 文件只作算法来源核字节，不重新执行其入口；原 C 内部定义源、原 R416/450、图册及帽的递归绑定继续由各原加载器实际检查。不能把这八项误说成全部递归源码仅八件。

新 schema 分别为：

- `R426-same-job-original-C-live-closed-query-provider-v1`；
- `R426-current-C-accurate-ten-complete-closed-relative-metric-live-queries-v1`。

原 R418/f12f 文件、schema、运行实例均不改。

## 426.3 实际输入必须是什么

入口接受 R418 原完整 CLI：当前真实 450/准确场目录与 SHA、checkpoint/proof 目录、真实 cuff atlas 与 SHA、原 C result 与 SHA、eta、空间分格和计算预算。它先完整执行原 R418 的四件 C 对象绑定，包括当前目标内的实际 C 身份、160 条原 shallow rows、原 frozen warp alpha、物理参数、原定义源码、root-existence/完整有限头/拼接条件、全部查询顺序及闭端点。

新 provider 只消费同一 job 的现场数据。原 result 的 run_id/source_commit 必须与当前 GITHUB_RUN_ID/GITHUB_SHA 相同；C 目录须在本 job RUNNER_TEMP 内。这里没有实现另一次运行的语义转移，也不把上一运行的摘要或 SHA 当原件。

除四个原元数据对象，还实际读取以下两个已有文件：

1. `large-arrays/source-piece-index.json`：核完整字节/SHA、1440 原片的 n159..0/j0..8 顺序、准确分支身份和原 cap/weight/flat/cut 参数。
2. `large-arrays/complete-source-radial-panels.jsonl`：流式核完整字节/SHA/行数；每个原片完整闭参数分区从 0 到 1；全部共享累计径向端点原记录一致；保每片的原 E、E_r、E_rr、左右累计半径及 primitive 行来源。

没有从 hash 恢复已删原件，没有重新生成一份“等价”原 result，没有重选 shallow 参数或深根。已核原完整 source index 只是公式身份；旧完整字段包围仍按原 f12f 已发表生产合同消费，不冒独立重算了它们的区间数值。

这两个新增 payload 尚未读取时，状态明确记为 source unstarted。新增这两件 retained source payload 的缺失、读取或校验失败只使新增精化未付，并保原粗界；原 R418 的真实场与四件 C 元数据绑定仍按原错误处理，不能借这项回退绕开。输出 I/O、外部信号等未完成事务仍留下真实错误/未付范围。它们不是增加旧 scientific acceptance 的门。

## 426.4 同一数学对象与逆像覆盖命题

令 $\Omega$ 是原 C 定义允许的全部准确深根序列；160 条 shallow 表、原 lambda、完整 cap/flat/cut 表及物理参数固定。对每个 $\omega\in\Omega$，记该族的同一原单调径向函数与目标为

$$
r_\omega(x),\qquad E_\omega(r)=1+w_\omega(r)^2.
$$

原 source panel $P=[x_0,x_1]$ 保存的是对每个允许成员都成立的包围

$$
r_\omega(x_0)\in R_0(P),\qquad
r_\omega(x_1)\in R_1(P),\qquad
E_\omega(r_\omega(x))\in B_E(P)\quad(x\in P).
$$

其中可能的整个径向像包含于
$[\inf R_0(P),\sup R_1(P)]$。新查询 $I=[a,b]$ 只有在原共同自然域内才可取得完整 domain flag：$a\ge r_{\rm cuff}$ 且 $b\le\inf R_{\rm out}$。不把自然端点上界当共同域下界，也不把三个 cut 点盒延拓到非平凡径向区间。

**命题 426.A。** 若保留每个可能与 $I$ 相交的原 source panel，连同原完整解析深尾；分裂时每次用同一准确径向积分给两个完整子片，预算停止时保留尚未细化的完整父片，则最终所有被保留 $B_E$ 的 hull 同时包含所有 $\omega\in\Omega$ 与所有 $r\in I$ 的 $E_\omega(r)$。

证明如下。任取同一个允许成员及 $r\in I$。原完整源分区覆盖整个共同自然径向域，故该点落在完整深尾或某个有限 source panel 的真实像中。因为已存径向端点包围包含该成员的真实端点，这个 panel 不会被“径向像与查询不相交”的严格区间判断误删。若 panel 被二分，其真参数点至少落在一个闭子片；两个子片共享中点且都保端点，边界点不会遗漏。若停止细化，完整父片仍保其全部真参数点。有限或预算截断后的保留集合因此仍覆盖所取点；hull 包围成立。该论证对任意允许成员相同，不需选择一个成员或把各盒中点当同一成员。

本实现没有新写积分或逆像选择器。实际调用原：

- `ContinuousHead(p, rows, lam, binding)`：从相同准确输入重建原公式；
- `ContinuousHead.deep_cover()`：再次按原解析式包住全部深根族，不数值选择任何根；
- `SixPrimitiveIntegrator.integrate()`：六个原 primitive、原 R306 完整 cap 端点捷径和原解析/实区间回退均保；
- `QueryCover.run()`：原完整 domain 条件、所有可能逆像、闭端点、细分及粗父片保留逻辑均保。

分裂中点半径按原公式

$$
R_m\supset R_0+\int_{x_0}^{m}(f_0+\lambda f_1)\,dx
$$

形成，并与原单调端点范围相交。积分是该准确定义的原六 primitive，而非旧数值轨迹的差分。原 source 的累计半径盒和全头总和不重算；重新求中点积分不会把其父端点不确定性凭空消掉。

源码明确只把原 result 已付的 full-head/全部根条件作为这些原包围的前提；工作精度目标、query-depth、panel 数或耗时不是命题的数学前提。

## 426.5 新旧包围相交与缓存

若原完整查询对同一 $I$ 给 $B_{\rm old}$，新增完整查询给 $B_{\rm new}$，则

$$
E_\omega(I)\subseteq B_{\rm old}\cap B_{\rm new}
\quad\text{对每个 }\omega\in\Omega.
$$

实现还保原解析事实 $E\ge1$ 的交。若两个声称包住同一对象的区间相交为空，记录真实计算错误，不能挑其中一个假装完成。

缓存键是准确有理端点 $(a,b)$，不是其浮点近似、空间 cell 编号或 angle。相同径向区间可被不同 angle、反射侧和实际片共享，因为目标 C 的径向变量和全根族没有改变。缓存不会改变 field 的值或消去其均值、物质角与反射。另一径向区间不会直接冒用此包围；只有实际完成的查询闭区间联合完整覆盖一个请求区间时，才可取这些真实界的 hull。区间交只使已有证明更强，联合覆盖的 hull 可能更宽但仍有效。

每个新查询的完整原结果先写临时 requests ledger，再提交缓存条目。若被捕获的异常发生于该事务中，本次 complete/work_resolution 标志显式撤销，不能把已算出但记录未完成的局部结果冒作已提交新界；旧粗界照常保留。原 QueryCover 正常返回的完整粗界，即使 work_resolution_complete=false，仍可提交使用，不经过这个异常撤销分支。实际完整/分辨率统计由已提交 cache 条目形成。外部中断未提交的查询保其完整闭径向地址、原 metric cell 和最后实际 primitive panel 地址；不会凭已经做了部分内层计算就当该查询完成。中断在 cache 提交后、地址退休前发生时，读回单列“已提交但尚未退休”，不会错误降为原科学失败。

## 426.6 如何接回原完整 metric

新入口在数学上复制 R418 的原检查正文。原 prefix 的准确公共 u 十族目标、完整 native/collar 切片、R416 cut patch、全 six-jet、原 material $\Phi$、两 reflected sheets 和两完整帽的同图 metric 身份均不改。其余处理顺序是：

1. 以当前可用的完整 C 界执行一次原 cell 检查。
2. 原 prefix cell 或已经获证的 cell 直接保原结果。
3. 未获证的 radial cell 请求该 cell 的准确闭径向查询。
4. 若新完整查询实际返回，以同一原 field 和原四个 Loewner 条件再检查该 cell；若只命中此前已用的缓存，不重复同一 field 评价。
5. 未获证 cell 仍按原四分闭 DFS、原 depth/visited/绝对时间上限处理；缺完整目标前提仍明确未付。

原 root_plan 在任何新查询前生成并冻结，原 query cut 分割不被运行中缓存改写。新增查询不是向已付 root universe 追加或删除片，也不把原首层未付区域偷换为更小目标域。

R251 的四条件仍是唯一这一级的算子证明判据。由于 field 与 target 可能依赖同一 $\omega$，独立区间乘积只会包住更大的组合集合；对这个较大集合成立的原 Loewner 条件当然包含真实对角配对。这里没有把独立中点误认为真实同一成员，也没有反过来从区间过宽推出任何点的反例。

源码没有变更原 genuine450/native/FD/BC/RMS/完整112入口的任何接受阈值；缺少真实原场时仍不能运行成一份证书。metric true 也不自动支付 reach、held、全任务或 IEEE 执行误差。

## 426.7 新 CLI 与同 job 插槽

原 R418 CLI 全部保留。只换入口 basename，并增加以下十一项显式工作参数；没有隐藏精度或自动改 root-definition：

| CLI | 原 f12f 参数/用途 |
|---|---|
| --c-query-precision-bits | 新查询的 interval precision_bits |
| --c-query-integral-absolute-bits | 原 integral_absolute_bits |
| --c-query-integral-relative-bits | 原 integral_relative_bits |
| --c-query-analytic-guard-bits | 原 analytic_guard_bits |
| --c-query-integral-evaluation-limit | 原 Acb evaluation limit |
| --c-query-value-width-bits | 原单逆像片 E 宽度工作目标 |
| --c-query-integral-max-depth | 原积分 max_depth |
| --c-query-inverse-max-depth | 原 query_depth |
| --c-query-max-panels | 全部新增查询累计 primitive panel 上限 |
| --c-query-max-nodes | 全部新增查询累计 inverse-cover node 上限 |
| --c-query-budget-seconds | 全部新增查询累计活动时间上限 |

范围与原 C 相同：精度 128..8192；两积分位数及 value-width 位数为 1..precision；guard0..64；积分 depth0..80；逆像 depth0..60；所有计数和时间为正。它们只规定已授权计算投入，不是额外 scientific acceptance。当前没有选某个实际新父场或给未来运行预填这些值。

可执行命令结构为：

```bash
python -u computations/geometry_20261115_current_C_ten_live_query_complete_metric.py \
  --computations "$COMPUTATIONS" \
  --directory "$ACTUAL_ACCURATE_FIELD" --result-sha256 "$ACTUAL_FIELD_RESULT_SHA" \
  --checkpoint-directory "$ACTUAL_CHECKPOINT_DIRECTORY" --proof-directory "$PROOFS" \
  --cuff-atlas "$ACTUAL_CUFF_ATLAS" --cuff-atlas-sha256 "$ACTUAL_CUFF_SHA" \
  --continuous-e-result "$OWN_NAMESPACE/continuous-E/result.json" \
  --continuous-e-result-sha256 "$ACTUAL_C_RESULT_SHA" \
  --eta "$REQUESTED_ETA" \
  --interval-bits "$METRIC_BITS" --sqrt-bits "$SQRT_BITS" \
  --initial-angular-depth "$INITIAL_Q_DEPTH" --max-depth "$METRIC_DEPTH" \
  --max-visited-cells "$METRIC_CELLS" --budget-seconds "$METRIC_TOTAL_SECONDS" \
  --c-query-precision-bits "$C_QUERY_BITS" \
  --c-query-integral-absolute-bits "$C_ABSOLUTE_BITS" \
  --c-query-integral-relative-bits "$C_RELATIVE_BITS" \
  --c-query-analytic-guard-bits "$C_ANALYTIC_GUARD" \
  --c-query-integral-evaluation-limit "$C_EVALUATION_LIMIT" \
  --c-query-value-width-bits "$C_VALUE_WIDTH_BITS" \
  --c-query-integral-max-depth "$C_INTEGRAL_DEPTH" \
  --c-query-inverse-max-depth "$C_INVERSE_DEPTH" \
  --c-query-max-panels "$C_NEW_PANELS" --c-query-max-nodes "$C_NEW_NODES" \
  --c-query-budget-seconds "$C_ACTIVE_SECONDS" \
  --out "$OWN_NAMESPACE/complete-metric-live-C"
```

变量必须来自真实当前 job 的输入/输出 receipt 与明确参数，不是可空填的假路径。原 field、C、图册与 checkpoint 加载和源码核对均真正执行。入口导入原定义模块只是运行实现的必需部分；在本交付阶段没有执行该命令。

当前 postsolve 生命周期已有合适位置：原193类 job 的 C 目录为 own namespace/continuous-E；原 driver finally 只关闭 worker，原最终 cleanup 才删 namespace。因而在真实450/准确场/图册已经产生、owner静止后，可在最终清理前用本入口替代固定盒 metric role。无需令旧 native worker继续活跃，也无需重算 C 全头。R429 当前固定-R418 接线不被本稿暗改；未来具体请求必须显式 pin 两新源、给齐十一参数并记录 role/marker 的改变。

## 426.8 时钟、precision 与受控停止

整个 metric 绝对 deadline 仍从原 run(args) 开始，包含源码/场加载、源账本读取和新增查询。provider 另累计自己实际活跃的时间；普通空间 metric 工作不消耗这项子预算，但仍消耗总 metric 预算。源片读取、原积分 panel、原 query node 与 Acb callback 都沿原检查接口使用同一个绝对 deadline。

原 QueryCover 若在细化中耗尽工作预算，会以其原逻辑保全部未细分父片，因此可得到“完整粗界=true、分辨率完成=false”。这种完整粗界可照常用于原 Loewner 条件。provider 的预算耗尽后，不再启动新的精化，但并不撤销旧粗界。深尾不是有限 panel 被删掉的后缀：始终保原全根解析包围。

这仍是 cooperative time checks，不是硬异步时间保证；关闭日志和必要读回也需要实际剩余墙钟。外层 Actions owner 必须保原独占组/静止/读回/条件 cleanup 合同，不可假定最后一个查询必在预定毫秒返回。

每次查询先保存实际 flint global precision，再设其显式 query precision，finally 恢复保存值。原 field 的更高有效精度不会被查询泄漏覆盖。公开入口是单进程顺序调用；本接口不允许同一个 provider 的嵌套调用，也不宣称可并发共享全局 flint context。

## 426.9 原始证据与必要读回

完整可重算记录只在新输出的 large-arrays/live-C-queries 下：

- 原实际 input-binding；
- requests：每次真实闭查询 begin/return/未付范围；
- six-primitive-panels：原六分量全记录；
- closed-inverse-cover：所有实际保留的原逆像片；
- unpaid-query-scope：全部粗父片/停止责任；
- 原 metric 完整 cell ledger、root_plan 与 coverage-and-pending。

最终 result/summary 保新 provider/原 C/原场完整身份，真正原 source payload 的完整字节、SHA、行数和读取后缀；实际查询数、提交数、完整界数、分辨率完成数、缓存数、活动子预算和总预算；最后原 primitive 地址、当前未提交闭查询、原 metric 的 pending cell 地址与未访 root rank 后缀。原查询结果与新查询结果不混为同一原行。

原 terminal 未获证 cell 全部仍在临时完整 cell ledger；必要 stdout 保覆盖/计数/当前 pending 范围及文件身份，不搬运全部六 jet、全部大包围或原 C 大账本。只有一个必要 JSON，最大 90000 B，marker 为：

- BEGIN_R426_CURRENT_C_LIVE_QUERY_CLOSED_METRIC_SUMMARY；
- END_R426_CURRENT_C_LIVE_QUERY_CLOSED_METRIC_SUMMARY。

超限明确 return70、必要正文未发，不分包、不编码科学树、不把 hash 冒完整读回。输出 journal close 失败独立记 execution_error，不能把丢失输出说成完整。只有全部已请求读回成功且 owner 真静止后，外层既有 lifecycle 才能删原 C/source payload 和新输出；本入口自己不删输入或原 raw。

## 426.10 能改善什么，仍不能承诺什么

具体新增能力是按真实 cell 区间缩小可能逆像，并复用原严格积分缩小这些逆像片的 E 包围。它不重新校准或重新累计1440原片，因此原累计半径盒的宽度可能成为限制；全深根族的真实不确定性也不会因选择一个中点而消失。完整 coarse bound存在不等于存在足够小的相对误差余量。

此外，原 R323/十族 prefix 的语义 cut叶、R416 patch 的准确系数盒、原场 Hermite/Fourier的六 jet包围以及实际 field到目标的真实差距均未由本 provider单独缩窄。若这些量主导，继续 query细分可能无效；记录真实未付，不能把缺少成功推成无解、点态反例或普遍误差下界。

这一交付已给实际可运行的同 job入口与完整来源/资源/清理接口。它没有提供实际450、数值 envelope、新 metric结果或任何未来成功承诺。完整 diff、SHA 与本地源只作可重得的临时源码交接；科学执行及实际来源选择仍在公开 Actions。
