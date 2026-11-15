# R289：actual118 八个真实32查询模型、FD与最近 MID483 障碍

类型：已执行有限计算的数值证据及原输出事实；不构成连续解、完整 BVP 或课题完成证明。
作者：ChatGPT / exact_refinement（AI-assisted）。日期：2026-11-15。
来源：[原请求与完整运行协议](../notes/2026-11-15-request118-thirty-two-midpoint471-real-pair-batches.md)、[actual110](../notes/2026-11-15-actual110-eight-real-pairs-and-midpoint471-barrier.md)。

## 1. 实际结论及范围

[Actual118 run43693006085](https://github.com/Rogerhu12/math-research-public/actions/runs/43693006085)，source `bb1d75675dc639f3f1ab74749798a5c11b2ac3a5`，compute job `132747387808`。八个新模型及各自新 warm 的 FD 全部实际完成，16个子进程退出码均为0；原51次非线性试探中8次接受、43次拒绝。最终停止原因为 `explicit_maximum_batch_count`，`maximum_batches=8`、`original_model_FD_pairs_completed=8`。没有第九批，也没有因达到最终精度而停止。

新增 MID471 后，八批最近拒绝中的该查询均为正；后四批最近拒绝只剩原 collocation MID483 失域。这支持下一次补入该真实查询的具体算法选择，不能证明所有其他域责任已解决。接受步长从前三批的 $1/8$ 缩到最后两批的 $1/256$；最终物理 collocation 最大残差仍为 `0.007107083459932941`。每批 `success=false`、`new_coupled_finite_acceptance=false`、`native_at_current_height_solved=false`、`new_full_DN_acceptance=false`。本次没有执行 native、完整 fullDN 或闭曲面验收。

本地只读取原 JSON、计数记录及核字节/SHA；未重新形成模型、矩阵作用、范数或科学比率。下面的 merit 下降、预测比、残差和 FD 均直接引用原 Actions 字段。

## 2. 真父件、查询与完整模型

初始父是可恢复的 actual98：run `43677587785`，source `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`，artifact `14147700690`，完整 ZIP `809042943` 字节，SHA256 `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`。其原31查询 warm SHA 为 `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`，status SHA 为 `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。原四数学输入、78来源、完整 ZIP 与两个选中成员的实际恢复范围见请求接口。

Actual110 的末场已经删除，未用其 SHA 伪造父场。本次从 actual98 另起轨迹；第1至7批均接本 job 上一批真实保存的 warm/status，下一批前核原字节并原样移动，没有改 producer、重序列化或复用旧 FD。未提供110首批的场数组对照，也没有把这种对照设成新门。

本次唯一新增为 MID471 的全部2048角点；旧 LEFT471 是分数 `0.17267316464601146` 的原 RMS 查询，与原 collocation midpoint 不同。32组按以下次序，每组角下标 `0..2047`，共65536行：

- LEFT20：`464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487`。
- MID12：`471,473,475,477,479,480,481,482,484,485,486,487`。MID471 为 group20。

原20个捕获区间、25个物理端点 `464..488`、完整 local8453、C4059及全部外部恢复保持；没有清零或冻结外部变量。每批实际完整模型维数236036，外部自由 core109、全局边框112；原 $A,A^T,B,B^T,g$、权重、尺度、全部仿射列和恢复保留。$lambda=270$、working512、dual200、LSMR200、原17档回溯和原接受门均未变。

## 3. 八个实际接受与 FD

各行只表示该批真实新模型自己的冻结权重 merit；不得跨行相减，把重新计算的不同权重目标冒成一个固定目标。实际 merit 不含阻尼罚项。

| 批 | 实际试探数 | 接受 $\alpha$ | 本批 $W_0$ | 接受后 $W$ | 原记录的下降 | 原四阶 FD 相对误差 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 4 | 1/8 | 43.363003729098274 | 43.33594286031892 | 0.02706086877935121 | 8.81884772255149e-10 |
| 1 | 4 | 1/8 | 43.33449126616587 | 43.31970358847642 | 0.014787677689447776 | 7.894525825628755e-10 |
| 2 | 4 | 1/8 | 43.31398352329856 | 43.29726225181123 | 0.01672127148732727 | 8.111061950955928e-10 |
| 3 | 5 | 1/16 | 43.297117414894636 | 43.28571057612342 | 0.011406838771215178 | 9.067299872698789e-10 |
| 4 | 8 | 1/128 | 43.285992742553056 | 43.284637534189145 | 0.0013552083639112311 | 8.107169474759329e-10 |
| 5 | 8 | 1/128 | 43.284724228686734 | 43.28329969228863 | 0.0014245363981046921 | 1.0858834988572664e-9 |
| 6 | 9 | 1/256 | 43.28341691250828 | 43.282741538228464 | 0.0006753742798153439 | 9.468708652938304e-10 |
| 7 | 9 | 1/256 | 43.2827939218789 | 43.28211529883264 | 0.0006786230462552112 | 8.926511510866175e-10 |

各批接受时原 `actual_to_predicted_ratio` 依次为 `1.0054807844552296, 0.5932136177355973, 0.7637266766016674, 0.967538106445899, 1.013282275508774, 1.029045314561321, 1.0144766052145893, 1.020744374681199`。这些是每批原完整模型与其实际非线性试步的读数，不是本地重新求比。

八次接受均已重新计算完整 trial RHS，节点及中点无失域；两组原 RMS 各698点、invalid_count均0。32组实际 beta 负角计数和非有限角计数均0；全部65536线性储备也均有限且严格正。原4096角 rho guard 有效，所报最小值 `0.16604058243274977`。未提前执行的 RMS 阶段仍记为未执行，不能把失败试探中的缺失字段当作0。

八个 FD 的 `implementation_check_passed`、`complete_current_warm_boundary_FD_actually_recomputed`、二阶截断收缩标志均为 true；原阈值 `5e-05`，左右边界 Jacobian offblock 最大值均0。`actual_completed_nonlinear_J_reused=true` 指该批已完成模型的 J；原 `nonlinear_DN_evaluated`、`nonlinear_native_at_current_H_solved`、`full_BVP_solved`、`full_Cartesian_closed_surface` 均为 false，不能把此实现 FD 读作当前非线性 tail/fullDN 的通过。

## 4. 最近拒绝与 MID471 的真实责任

下表列每批接受之前相邻的最后一个被拒试步。LEFT 指原左 RMS，MID 指原 collocation midpoint；负值为原输出的 $\beta^2$ 最小值。

| 批 | 最近拒绝 $\alpha$ | 原失败查询及 $\beta^2$ | 同试步 MID471 的 $\beta^2$ |
|---:|---:|---|---:|
| 0 | 1/4 | LEFT464：−0.2683514415128212 | 0.015920938113163308 |
| 1 | 1/4 | MID483：−0.025369163330261513 | 0.05905471192199563 |
| 2 | 1/4 | MID472：−0.007386907456445657；MID483：−0.008086257977948597 | 0.010529849282947867 |
| 3 | 1/8 | MID472：−0.08570553280356785 | 0.7067651216379595 |
| 4 | 1/64 | MID483：−0.011293424272345698 | 0.7258757334062336 |
| 5 | 1/64 | MID483：−0.01197360224691768 | 0.7234852619387518 |
| 6 | 1/128 | MID483：−0.0007144637703189183 | 0.723653746684376 |
| 7 | 1/128 | MID483：−0.0008413561364628563 | 0.722580170835746 |

第1至7批最近拒绝中，32个已选查询的负角计数全部0。第0批最近拒绝在已选 LEFT464 有4个负角；各批所选查询均无非有限角。原51试步都没有节点域失败或 boundary_domain_error；43次拒绝均保留实际域失败记录，而不是仅由一个缺省 `accepted=false` 推断原因。

末批 MID483 的真实站点为 `1.2367303492381132`，原左右端点 `1.2342381234882334`、`1.2392225749879933`；最坏角 `2.8440003807399785`、角下标927，共4个负角且无非有限 beta 角。原中点输入是有限的，返回分类为 `finite-original-middle-input-with-nonfinite-original-RHS`；未选入的中点域责任仍由原非线性检查实际拒绝。

这没有证明新增 MID471 对任意试步都有效。例如第7批 $\alpha=1$ 时该已选中点仍给 `−0.3006855449562016`。也没有证明 MID483 是整条路径唯一障碍：第2、3批最近拒绝有 MID472；较大试步还出现 LEFT463 等原 RMS 失域，第4批 $\alpha=1/8$ 的 LEFT463 为 `−4.290278295986819`。原完整门仍在发现线性查询之外的非线性失败。

## 5. QP精度、物理残差与停止边界

八批选中的都是 `R270-condensed-complete-H`，完整消元报告 `complete=true`，每批一次完整恢复、512次局部 H solve及对应必做残差作用，原外部109 core与完整仿射项均保留。每批最终实际全 $A,A^T,B,B^T$ 读回执行，65536原线性行均严格可行。

但局部 QP 八批都在 `maximum-working-row-budget` 停止，working上限512；末保存阶段511、200次 dual sweep，停止原因为 `maximum-dual-sweeps`。八批 `global_selector_changed_conditional_recovery=true`，`full_QP_optimality_claimed=false`。原完整模型浮点后验如下：

| 批 | 原 cross-point gap 读数 | 原完整 stationarity L2 |
|---:|---:|---:|
| 0 | 3.000998560764856e-09 | 0.003038625816318205 |
| 1 | 2.623773689907459 | 618.4471744929142 |
| 2 | 77.21167918720278 | 3355.1687321625977 |
| 3 | 47.372024928948285 | 2628.0386924985237 |
| 4 | 96.04813846345237 | 3742.12188081144 |
| 5 | 76.93705808726679 | 3349.1960122713904 |
| 6 | 121.0830934836995 | 4201.613192497169 |
| 7 | 127.48762165450324 | 4311.302490300828 |

这些是普通浮点读数，原报告明确 `posterior_is_not_a_validated_enclosure=true`，并非严格外包或最优性证书。末局部 center 梯度 L2 `8.161062766383301e-12` 也不能替代完整原 H 的 stationarity。这里没有增加一个后验通过门，更没有因有限工作集达到上限而称当前模型已最优。

初始物理 collocation 最大值 `0.00710763096028075`，末次接受后为 `0.007107083459932941`；原最坏行始终是155819、区间461，末 signed residual为 `−0.007107083459932941`。该行原冻结权重 `198.99205882032422`，读取自该批原 weight 返回，而非用 trial重新推导；其已有中点站点 `1.1420257707426757`。末完整边界最大值 `4.8077064737075215e-09`，constant collocation与左残差最大值0。小边界残差不替代仍未通过的完整物理问题。

八批上限是本次运行协议，不是数学无解、局部最小或机器误差下界。当前方向与步长同时受未选域点及有限 QP 精度范围约束，不能只凭本轮结果给出单一归因。

## 6. 原字节身份与重做入口

根唯一取得的原 compute.log 为382986字节，SHA256 `1c81a9c647e4dafefcb962ac7b49a09b74e161d9528ecd3b26cdf602ef546990`。八份原 `BEGIN_THIRTY_TWO_BATCH_SCALAR_SUMMARY` 均完整、未触发90000字节省略回退。其 SHA 口径为去掉 GitHub 时间戳后的原 JSON 文本加恰好一个 LF；不是不含 LF 的摘要，也不是解析后重编码的摘要：

| 批 | 原摘要字节数 | SHA256 |
|---:|---:|---|
| 0 | 36787 | `d8eae883fd4516d19838fbe287dc7ef1c04feda6bb08dbbfd2550e1150489a92` |
| 1 | 30720 | `c6a84a02c844eebe0594336ced7d6bb7e063b271c15f548f94a819ebe5a771e5` |
| 2 | 30728 | `61ec3c6bc2085f65857eb99ae237e6aa9e18b1c638e2e230912c13c87d2a5db6` |
| 3 | 33205 | `cc9cc4b01ab3e4b4583461f5ac9d0ea8782cde8e76ee903035b8c18d1eb0eb22` |
| 4 | 46468 | `05154d7e1c0f28d24a65b5625e4b4b148da0ac38f5ed8a00e6f0bbb4bcd48822` |
| 5 | 43345 | `dc28c9171d980b61b3cd45cce4d3521c2c786118ffcd03c0b8bba58eeccb812f` |
| 6 | 49196 | `772494bb0fc270d5b4a8d22e1752988d940ea5d429353db1297662027d078ab1` |
| 7 | 43258 | `d996ed38e592b491b95f6e31bb01fd55ff0cbdc820ca45b8c4deac2564bea7c6` |

真实末 pair：warm `5024325` 字节/SHA `46adc694ff2d989e16924c3469ba1d208630406a6e4cb5f338484bd055a540f6`；status `5391503` 字节/SHA `dd24bfeff587a9b73677fffb398ca494ccd6889bfc38361580cf197893011b3f`。末字段子集规范 JSON SHA `2e689d871ac2b60dceb84687115aef75b529db7117fffd7a6e1a44fe47873d54`，只标识原 mesh/states/rhs/field_representation/complete_scalar_profile 选择；它不是完整 warm 文档或 native数组逐词身份。

上述 raw 已由本 job 原 owned cleanup 删除，`raw_payload_uploads=Release_uploads=Git_data_publication=0`。本次只付原标量/来源读回，没有重新取得巨大数组，也不声称原 RAM-only 完整 QR 已导出。SHA不能恢复已删末场。

可重做的科学入口均在上述 source commit；完整来源75pins加独立 worker及原参数由下列两个已提交文件定义：

- `computations/public-thirty-two-model-recipe.json`：SHA `f5c0e2e67fa7855ce074a144f8b8223aedd028cd27e77f053c38f335f9342e26`。
- `computations/public-thirty-two-batch-request.json`：SHA `1a446102f3a8b6018efa5c9e4ce3a2e4c70979bf05fd2545ad8f67e9dc9056b3`。

原 worker `geometry_20261115_thirty_two_temporary_batches.py` SHA `336fc52205446977ed936035e06818abc2aebb732d1b41c8d8f2fb49eb2266b0`；其执行命令为：

```text
python -u topics/visible-flex-larger-amplitude/computations/geometry_20261115_thirty_two_temporary_batches.py
  --repo-root GITHUB_WORKSPACE
  --request topics/visible-flex-larger-amplitude/computations/public-thirty-two-batch-request.json
```

原 workflow `.github/workflows/visible-larger-public-thirty-two-batches.yml` SHA `96eeef3bf91a4ec26fc773e3c8a5cc2e020f7b029b3543140042962f79b64028`；175分钟科学step、185分钟job、批间10500秒，原科学参数及全部门见请求接口。规则 runner 在08:07:35及08:52:38 UTC实际同步，科学 checkout 未变。重跑须用真实原件/来源重新计算，不承诺跨运行浮点或工作集选择逐位相同。

## 7. 基于本轮的下一项选择

最窄且有反复原证据的扩展是保原32组并补 MID483 全部角点，再沿原完整模型与全部非线性门作有界计算。该选择必须声明新查询/捕获身份，不能把 LEFT483 或邻节点替作该中点；现有 MID472及较大试步 LEFT463 失败仍保留为可能后续限制。增加一组线性约束不保证更大非线性步长、QP最优性或完整场接受。

若要从118真正末点接续，必须重新执行原轨迹并在真实末 pair 尚在同job时消费；否则只能从仍可恢复的 actual98 另起新查询轨迹，并准确声明新起点。不能把本报告的末 SHA或字段子集摘要当作可恢复 checkpoint。该后继仍须最终支付当前非零 H 的 native、完整 fullDN、finalJ/audit、同一固定 g 的精化及全部闭面几何标准。
