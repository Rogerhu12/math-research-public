# R142 supplement: durable parent source integrals for exact-moment continuation

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

本篇给尚未完成的原 low193 moment 目标一个可真正续接的积分次序。原 comparison Green、真实系数、五种源角色、155 个父区间、1424 个现有 refined cells、完整物理权 $S$、97 个根原子和96个外端原子均不改变。每完成一个**完整原父区间的输入源积分**，立即正式保存 body/root/outer 三个累计平方范数上界；下一次只生成缺少父区间的源 moment。

这不是把旧 run 的 panel 计数当成已存矩阵。当前 R142 owner 的旧前缀若没有这些积分球，不能凭计数进入本篇的非空前缀。已经保存的完整旧 defect、source 或 point 结论仍先按原整体对象消费，不重登记。整个新实现只准备后继；本篇没有运行数学、没有给出新的 $\epsilon$、没有修改正在运行的 R142。

## PS1. 原积分中哪一维可以分段保存

固定原 model 和一个完整源角色 $\mathsf s$，记它的 Green kernel 为 $G_{\mathsf s}(r,t)$。body 目标是

$$
 \|G_{\mathsf s}\|_{\mathrm{HS,body}}^2
 =\int_{\text{full source}}\int_{\text{full output}}
       \|G_{\mathsf s}(r,t)\|_F^2\,dr\,dt .
 \tag{PS.1}
$$

root97 和 outer96 把内层连续输出换成原有限观察的平方 Euclidean 范数；包括独立 even mean。对任意完整父区间的并 $I$, 定义三个量

$$
 B_{\mathsf s}(I)
 =\int_I\int_{\text{full output}}\|G_{\mathsf s}(r,t)\|_F^2\,dr\,dt,\qquad
 R_{\mathsf s}(I)
 =\int_I\|G_{\mathsf s,\mathrm{root97}}(t)\|_F^2\,dt,\qquad
 O_{\mathsf s}(I)
 =\int_I\|G_{\mathsf s,\mathrm{outer96}}(t)\|_F^2\,dt .
 \tag{PS.2}
$$

输入区间分开后它们严格相加。没有把两个有关联输出的范数作三角求和，也没有声称源函数在区间上恒定。这里分割的是平方可积 kernel 的**源变量**，所以每一片都保留整个径向输出和全部193个原子输出。已存片段不是一个被截短的 BVP，不需要新接口条件。

全可变源仍使用 GM.15 的逐点 PSD majorant；常源使用原 exact covariance。它们可能给 (PS.2) 的上界，但不会丢弃任何真实源列，或把父区间中的真实系数冻结为其中点。五个角色正是原 provider 的：

| 角色 | 原对象 |
|---|---|
| ordinary_raw_low_source | 原始 ordinary $L^2$ 的全193个列 |
| transformed_low_source | 原 $S^{-1}$ 源列 |
| true_coefficient_defect | 原真系数减同一个 midpoint comparison 的完整差 |
| low_second_kind_correction | 原低 second-kind 参考差 |
| centre_high0_return_source | 原 HIGH0 到完整193行，包括 mean 的实际源 |

本方法既不换 real97 cutoff，也不把这些列升级成含 family difference、CFB 或真实外块的最终逆。

## PS2. 先物化与源无关的输出协方差

沿原 exact-cell moment core 使用 $O_{L,i},O_{R,i}$ 和原 $U_i^{-1},V_i^{-1}$。为免与 body bound $B_{\mathsf s}$ 混淆，本节的 $A_i,B_i,K_i$ 专指 GM.16 的输出协方差。它们满足

$$
 A_0=0,\qquad
 A_{i+1}=U_i^{-\mathsf T}(A_i+O_{L,i})U_i^{-1},
 \tag{PS.3}
$$

$$
 B_N=0,\quad K_N=\operatorname{Gram}(\text{outer96}),\qquad
 B_i=O_{R,i}+V_i^{-\mathsf T}B_{i+1}V_i^{-1},\quad
 K_i=V_i^{-\mathsf T}K_{i+1}V_i^{-1}.
 \tag{PS.4}
$$

原 root carry 为

$$
 J_0=\operatorname{Gram}(\text{root97}),\qquad
 J_{i+1}=U_i^{-\mathsf T}J_iU_i^{-1}.
 \tag{PS.5}
$$

以上对象全部由同一个已证 comparison BVP、完整物理观察 $S$ 和原端点观察定义，与输入源 covariance $V$ 无关。代码先调用原 ParentMomentProvider 的 _prepare_parent 和 _prepare_cell，读取它们按原公式形成的 $O_L,O_R$；不调用 _moments、packet、model_source_covariance 或 source_moments。

prepare_model_template 的 $H/Q$ Taylor template 和 $U$ 是构造这些完整输出协方差的必要表示。公开文件没有这些私人矩阵，因此后继确实可能需要重新物化它们；不得把此事描述成已恢复旧 bytes，也不得把它登记成重复完成原源范数。每个私人矩阵仍按原 PackedMatrices 的逐项向外包围检查存储。

正向只保存 $A$ 和临时 $O_R$，反向形成 $B,K$ 后释放临时 $O_R$。所有 $A,B,K$ 必须覆盖全部 refined cells，才能接受下一节的任何源片段；不能因为已有一个源前缀就把其输出限制到相同前缀。原 root carry 的前缀也可按 (PS.5) 重新物化，那里没有调用或积分任何旧源 moment。

这一表示与旧 packet-first 的表示围住同一个精确对象。打包和加法次序不同，所得到的区间标量没有自动单调或速度保证。

## PS3. 每个完整父区间的真实贡献

对源角色 $\mathsf s$，原 provider 在 refined cell $i$ 返回完整输入协方差积分 $I_{L,i}^{\mathsf s},I_{R,i}^{\mathsf s}$，以及**同格两个有符号三角合成后的**有效上界 $T_i^{\mathsf s}$。本篇的逐格平方贡献是

$$
 b_i^{\mathsf s}
 =\operatorname{tr}(A_i I_{L,i}^{\mathsf s})
  +\operatorname{tr}
       \big(V_i^{-\mathsf T}B_{i+1}V_i^{-1} I_{R,i}^{\mathsf s}\big)
  +T_i^{\mathsf s},
 \tag{PS.6}
$$

$$
 r_i^{\mathsf s}=\operatorname{tr}(J_i I_{L,i}^{\mathsf s}),
 \qquad
 o_i^{\mathsf s}=\operatorname{tr}(K_i I_{R,i}^{\mathsf s}).
 \tag{PS.7}
$$

每一 trace 项沿原 positive_upper 规则作有效向上包围，$T_i$ 仍来自原 signed formula，不拆成两个独立绝对值费用。真实 cell 长度在原 packet 中保留；没有把 normalized coordinate 积分当作 $dr$。

(PS.6)–(PS.7) 逐字对应原 complete_norms_with_shared_outputs 的三个累加器。唯一改变是何时保存：完成同一父区间的全部 refined cells 和本次声明的全部源角色后，将它们加入先前**保存后读回的上端点**，形成三个新的累计球。尚未完成的当前父区间不推进 accepted cursor。

父区间内可共享原 parent source moments；完成父区间后 release_parent 释放这个缓存。一次四源 pass 仍能共享一条 $J$ 和一次 right-output congruence，未要求四次独立读取。作为可选私人载体，retain_packet 可保存已经形成的完整 defect 输入协方差，以供后面的 point 观察；此载体不是新的 defect 目标。

## PS4. 正式保存顺序和真正的恢复边界

公开 prefix 的数学字段明确包括：

- 原 source_roles 完整列表；
- 完整原父区间总数155、已完成父区间个数和相应 refined-cell cursor；
- 每个角色的 body_HS2_upper、root97_HS2_upper、outer96_HS2_upper 三个**完整 decimal balls**；
- 完整输出193原子、整径向输出、两个同格三角和 GM.1–17 约定；
- 原整体 model/refinement、真系数、source definitions 与所用源码/manifest 的 owner 准入证据。

实际 owner 应先写完整 candidate 文档，读回每个 whole ball 并核包含未序列化结果，再把**同一 bytes** 提交为正式 scientific prefix，最后推进内存 accepted cursor。若在 candidate 核验之前停止，正式文档仍是先前已核的前缀。若在正式文件写成之后停止，该文件已经包含整个新父区间。仅增加 completed counter 而没有保存三球不是本篇前缀。

读取前缀时，owner 必须核原 science、execution、manifest、全部 source hashes、model chain、refinement counts 和每个球的完整身份；不能只传一个审计 hash、stderr 摘录或 progress 数字。pure bind_saved_prefix 只在这种 whole admission 之后检查数学 schema，并把保存球上端点绑回当前相同精确模型的私人 token。

恢复时让 $p$ 为已完成父区间个数。stream_remaining_complete_parents 从第 $p$ 个父区间开始调用 provider.packet。先前各父区间的源 covariance、$Z/Y$ moments、(PS.6)–(PS.7) 和全部原源码目标都不重算。已保存的三球已经支付这些输入域的全输出贡献。只有缺少的比较表示 $A/B/K,J$ 可按 PS2 必要物化。

如果旧 R142 文件只有 private_directed_storage 的计数/峰值和 current_source_panels_completed，而 defect 和三累计球都不存在，则无法恢复旧 $Z/Y$ 或接受某个非空 (PS.2)。本篇不能从这样的旧前缀凭空跳过数学；这一限制必须在后继实际记录中明说。当前旧 owner 未公开私人 matrices 的事实也不能改写成它们已经下载、复原或核 hash。

若旧完整 defect/source/point 结论已经存在，则优先消费它；本篇仅对仍未完成的原源积分适用。尤其整体程序若在 finish_target 预算检查前已经写了一个完整标量 block，owner 应按完整字段和源码次序核验其范围，不能仅因 completed_targets 差一就重复该结论。

## PS5. 何时得到完整范数和逆结论

仅当155个父区间均已接受时，三个保存上界 $b,r,o$ 给

$$
 \|G_{\mathsf s}\|_{\mathrm{HS,body}}\le\sqrt b,\qquad
 \|G_{\mathsf s,\mathrm{atoms193}}\|_{\mathrm{HS}}\le\sqrt{r+o},\qquad
 \|G_{\mathsf s,\mathrm{complete}}\|_{\mathrm{HS}}\le\sqrt{b+r+o}.
 \tag{PS.8}
$$

此前只是 (PS.2) 的完整源子域贡献，不能报完整 $\epsilon$、完整 inverse 或通过任何收缩门。六个最终球仍按原 owner 的完整保存读回规则使用。对于原 defect，$\epsilon<1$ 的意义和 false 分支保持原义；对 R149 coercive continuation，旧 $\epsilon$ false 和独立 $\theta$ 证书保持原义。

point 目标没有改成源积分目标。它仍须保留真实 defect point covariance 和全部 whole radial boxes；若前次这些私人载体丢失，可用已发表的 Z-only helper 必要物化，不能再次求已成 defect HS、把 $\theta$ 换成 point 范数、或从已完成 box 计数杜撰未保存的最大/最小球。

## PS6. 纯实现与本次实际范围

纯实现为 [stream adapter](../scripts/fourfold_codazzi_low_centre_streamed_parent_moments.py)。它没有 IO、数值 import 或入口，不修改原 exact-moment core、provider、active owner 或 worker。它显式区分 source-independent 准备、whole-prefix 重新绑定、只生成缺少父区间、以及全部源域完成后才形成最终范数。

本篇和代码没有声明这些新 scalar 已运行，没有称原 R142 失败，也没有假定它将失败。实际 successor 的 owner、source bindings、目标范围和 manifest 必须按真实 whole 输出选择；不能在当前缺少前件时生成一个能运行的虚构 continuation。
