# 真正58 joint168首尝试：固定高度行断言错误，求解尚未开始

日期：2026-11-16 18:01 UTC。**原正式科学尝试已退出；没有 OptimizeResult、候选、预测或 actual，当前仍是接受点58。** 本文从完整原研究日志和完成后只读报告记录实际失败，不将实现断言失败解释为几何不可行。

## 1. 唯一原运行和原返回

| 项目 | 实际记录 |
|---|---|
| run / attempt | [43923038659 / 1](https://github.com/Rogerhu12/math-research-public/actions/runs/43923038659) |
| source | 47942fb212bcc2f424fdf546437cd38b08c2d7e1 |
| workflow | .github/workflows/visible-true58-joint168-body-suffix.yml |
| research job | 133495072427；failure，正式step exit code2 |
| research时段 | 2026-11-16T17:53:15Z 至17:54:12Z |
| 完成后report | 133495656824；success |
| request | 91699B / 0611ff5c76d3bf25be879d7d2de01ab214f9253a8be742b5fc7764d2e6f98b96 |
| 来源 | 原395项源，正式source和request身份完整保留 |
| COMPLETE status | true58-joint168-body-suffix-raised |
| 异常 | ValueError: every original physical172 row has an actual full168 direction |
| 原失败位置 | build_joint168_body_suffix_model → _linear_rows；core源第256行 |
| 新接受 | 0；原selected_two_grid_physical_point仍为58 |

原异常在新完整172仿射图的线性约束构造中发生，早于prepare_geometry、初始联合模型值、J及SLSQP。因此没有模型几何/J或后端raw170可读取；不是遗漏一个成功返回，也不取末数组或callback作候选。原MODEL_PARTIAL按实际已完成字段保存，未填np.empty区域未哈希或输出。

## 2. 原准确H显示的两个固定物理行

已回读原[frame_height_null_coordinates.py](https://github.com/Rogerhu12/math-research-public/blob/47942fb212bcc2f424fdf546437cd38b08c2d7e1/topics/visible-flex-new-mechanism/scripts/frame_height_null_coordinates.py)，该源码SHA256为5ebfde0a3322bd119704fda517b2f15db48964fad7a3a344b1e863ec4c2f2f22，与原request一致。

ExactFiveHeightBasis先把H9×5置零，仅对行0、1、2、3、6、7、8赋值。原H第4、5行准确为0，所以physical172中第158、159行固定为永久reference的相应值；第157、162行是耦合行。完整168独立控制没有丢失，真实非零物理增量行数是170。

首版错误地对全部172个P行要求非零。这个额外实现断言不是原几何门，不由准确null-height定义支持。它导致了本次原退出；不能把它当作某个曲率/metric/盒失败。

必要窄修为去掉该错误断言，并把definition/metadata准确写成“172行保留，170个非零增量行，fixed=[158,159]”。原344条物理盒仍全留；172对norm行也全留，固定两行的四条norm约束准确为-h≤0的冗余行。因而692线性、154155非线性、154847总行和170列全部不改。原P、K/h、向内Bounds、准确RN后physical172、原strict metric/actual14可行域没有放宽或增加新控制。

本次原设计/合同在首source处关于“172行均非零”的文字也属于错误，不作为有效结论沿用。修正源与续接请求应明确该差异并保留原source、失败记录和费用；不覆盖原request以伪装首次正确。

## 3. 完整费用和真正未执行的部分

| 原最终字段 | 实际值 |
|---|---:|
| 新科学秒数 | 26.784710984000014 |
| 原祖科学秒数 | 3757.97482037 |
| 累计科学秒数 | 3784.759531354 |
| 原full值总数 | 147 |
| 新原actual grid值 / pairs | 0 / 0 |
| 模型构造 started | 1，raised |
| 新输入准备 started | 1；只进入线性图之前的准备 |
| solver sessions started | 0 |
| 新联合点值 / J / backend | 0 / 0 / 0，按原失败位置与完整组件记录 |
| paid metric bindings | 1 |
| paid first-jet bindings | 2 |
| canonical预测 | 0 |
| 原余额 | 1773.215289016秒 |
| scope_exhausted / overrun | false / 0 |
| process_seconds | 26.78479057200002 |
| 峰RSS（Linux KiB） | 907632 |
| COMPLETE前科学stdout | 240642B |

原runtime_import_seconds=1.2382295300000123；读取五份源日志的elapsed_source_input_seconds=11.035032806000004。两者都已包含在最终26.784710984000014秒内，不再次相加。

MODEL_PARTIAL仅有一个组件new_full168_linear_rows：started1、completed0、failed1、seconds0.003782735000015691；build local_elapsed_seconds0.09488910999999689，外层ledger模型事件0.09492849100001877。嵌套秒数不是额外科学账。prepare_charge_receipt为ordinal1，不能因构造失败把started debit清零。

原first-jet/fixed metric只绑定已有正文，之后新的几何未开始。原primitive、全selected/后缀值、完整J及其费用均不能据此称已经付过；summary或array SHA也不能代替未保存科学数组。

此次仅为原同一数学问题的首个实施尝试失败。必要实现修复继续原未进入的任务时，**只能从原1800秒余额1773.215289016续接**，连同首尝试26.784710984000014及全部失败counts带入完整链，不另发一份1800秒、不冒换数学问题。solver1200秒/240iter/480q/960backend以及唯一actualpair均尚未使用；新attempt的必要恢复、重新绑定、构造和导入也继续实际计费，不借旧费用称免费。

该余额约束不作为主课题停止理由；若真正原范围以后结束，仍按实际结果接open的下一个新问题。

## 4. 所有原记录与完整性

原research log：**568954B / 8f8335df21ad4e36e1c930e6aaec982f93cd158c9c386e1b86369c9d6005f851**。共7条原记录：

| tag | JSON+LF字节 | SHA256 |
|---|---:|---|
| PUBLIC_PULL | 1485 | bea02554a62d89a5a854f3cf5af66c801709771e12001850c7292427d81c76df |
| PRIVATE_PULL | 584 | ca427718897b4a86b9f791c2a9327a6268706bfdd310407ac66a1db61bbc0278 |
| REQUEST | 9226 | be875a773dc9decd0a82aa28a96ade1b167c146cc05d4dd589bd2bf146e538ba |
| INPUT | 230007 | e0cf880110f51da8a311e67f08d22a909150dc1b7a8c4896a599c04d43dc612a |
| MODEL_PARTIAL | 1297 | 87cc4e973f7aa6358291c97e798f478891cee9b3db7d63495cb603b3331bb776 |
| COMPLETE | 185677 | 35f866b1643bff0fa7d28348682ea858ac83eb6ce774b0f37b79d077bf4aab83 |
| FINAL_CLOCK | 6593 | f9c5fc51500f41376a54ea70363853781bd04e009a0d47c748b37244e95004be |

原report log：631128B / e1ce441abb23ce7b398127abeb722097acec76c6fa157df9c5e44ea34c978314；READ_ONLY_REPORT为501640B / fd230d43ce4a04663e48e2b40e69d5fec4dccfce982e5be1532ef188a1ec31ac。

只读report的原状态original-output-selected，semantic_read_is_incomplete=false；parse_errors、missing_required_current_records、missing_current_record_receipts均空，7个原记录齐备，原source/run身份匹配。两个本次生产者回执MODEL_PARTIAL与COMPLETE均对应原正文；旧祖先的tag不是缺失本次结果。observed workflow in_progress只因report自身尚在运行，不能改写已经completed/failure的research。

观察器实际1.767068387000009秒单独记录，scientific_imports、scientific_or_development_calls、scientific_recomputations均0。观察器成功只表示完整读到失败，不能表示科学问题通过。

## 5. 四次真正双仓pull和规则差异

| 所属job / 仓库 | 原开始→完成（UTC） | 实际所读commit |
|---|---|---|
| research / public | 17:53:41.472690→17:53:41.808076 | 47942fb212bcc2f424fdf546437cd38b08c2d7e1 |
| research / private | 17:53:43.900783→17:53:44.437896 | 5967eff3a3dc560781354e14564fdcb839404a28 |
| report / public | 17:54:29.742081→17:54:30.132624 | 47942fb212bcc2f424fdf546437cd38b08c2d7e1 |
| report / private | 17:54:33.016460→17:54:33.752780 | 2dc8b0fa60bc03f989904678ee3468b9ca6c9bf2 |

两public均原git pull --rebase返回0、passed=true；根/本题README diff为空，blob仍21bd547f56590b7f2dd279d0297efb289a9b2783 / d0432faff569c8e9af7ed4809847e12880976c11。private根blob5ba164843b1f5802184178a82d786264404873a3，private题README不存在；两次queue_unique_and_ongoing_for_this_session=true。没有发表私有正文。

最新真pull为17:54:30.132624 /17:54:33.752780，下一不晚于**18:54:30 /18:54:33 UTC**。这些都是原Actions中的真实Git回执；API ref更新或GET没有冒充pull/rebase。

## 6. 当前可继续状态

原全域/全时/同g/握持大振幅/非局部reach及严格存在标准仍未完成。实际接受点保持58。修复只恢复准确原H与原线性行的合法接线，继续同一尚未开始求解的问题；它不授可行性、局部驻点、任何实际下降或接受59。原full62细metric失败、full51钟停、whole34缺失数组等祖边界继续保留。
