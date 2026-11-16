# 原完整 dual 的半坐标续接：真实断点来源、三种准确终点与一日载体

日期：2026-11-16。状态：执行契约；尚未取得当前完整 dual 运行结束后的真实 current，首请求保持 `producer_inputs_pending:true`、`completed_dual_source:null`。不停止完整运行，也不预填未来数位、产物或 SHA。

本消费者落实[半线性证明 HP.1–3](R787-original-antilinear-dual-half-coordinate-reconstruction.md)，保留[原无逆清转置证明](R787-original-inverse-free-cleared-transpose-value-acceptance.md)的准确算子和最终出口。它不接受原518位 primal 向量作为 dual 精度。

## 1. 冻结依赖与新身份

新核心为 `scripts/R787_half_coordinate_dual_CM_value_acceptance.py`。它显式导入冻结的原完整 dual 核，SHA 为

`bad9741493b550b0d3543ec953642c2b2f11f30da4433c9346f0c3215d415323`。

导入只复用原字段、原正乘算子、原读取方法、严格有理重构和准确转置验证；不调用旧 `Job.__init__()`、旧 `initial_current()` 或旧十四支完整求解。新核心有自己的初始化、完整来源、tag、恢复及终点定义，不改变父模块的全局变量或 `__file__`。

保留的数学依赖还有：原 R787 核 `93d3d72b…`、原 R781 字段核 `d024a7a6…`、原整数配对及其逆的已成来源、原四组1481个输入。新核心不重求旧 A/Schur 逆、旧 $\kappa/R$、旧1234行、旧 CM 评价、旧 eZ 或目标的共同分母。

数学 RESULT 继续为 `R787-original-cleared-dual-CM-value-acceptance`，FINAL 继续为 `p41-original-cleared-dual-CM-value-acceptance-certificate.json`；新 `source_sha256`、HP证明、执行方法、父核心及完整旧 dual 来源全部进入新 tag。共用 RESULT 便于消费同一个 A.1 答案，不表示来源与旧核心相同。

CLI 为：

```text
--config --proof --nested-proof --method --full-dual-core
--legacy-core --field-core --retained --output --budget-minutes
```

`--proof` 是正式 HP 稿，SHA `281de249137d88da3c67a25261ca744bd513ecb15b49ffb0125d82f7fb6b7c6f`；`--nested-proof` 是原清转置证明 `eb5893ec…`。原完整 dual 的方法仍按旧身份 `c6ca7d3a…` 核验，不能把新的 HP hash 填进旧阶段。

## 2. 必须来自实际结束运行的源闭包

`completed_dual_source` 只接受明确的原完整 dual 结束产物。来源必须绑定实际 run、source commit、父核心、父 wrapper、artifact、ZIP平台身份、完整 manifest、历史 README hash 以及实际允许的退出码。若外层超时没有 core receipt，仅在原 run receipt 的 `core_receipt_sha256:null` 时如实保留这个缺失；不得补造 receipt。

从同一不可变 archive 以 HTTP Range 读取：

1. 原 manifest、run/public/core（若实际存在）、原输入 receipt。
2. 原最新完整 current、其 exact-target、source-audit、历史及 index。
3. 所有仍实际存在的 `R787-cleared-dual-*.json.gz`。其中可能含下一位已成正残差/修正、已成 RR witness 或部分准确验证。它们作为旧来源保全，不假装是新算术。
4. 原四组输入 carrier、原配对来源 carrier 及其 receipt。

不从即将过期的祖先 artifact 重新搜集1481项。旧主 carrier 内成员按原 receipt 及各组 manifest 逐 SHA 检查后原字节复用。旧配对 carrier 也原样复用。旧完整 dual 的所选阶段另装 `R787-half-dual-completed-full-dual-inputs.tar.gz`，根目录为 `FULL_DUAL/`；这使后继续算不依赖旧 artifact 继续存在。

旧 current 的必要字段为 `prime`、`digits`、`modulus`、128×280的 `chi_integer_coordinates`、`exact_target`、`source_audit`、`full_square_modular_identity_verified:true`、`old_primal_precision_or_vector_reused_as_dual:false` 及原 configuration。`source_dual_digits` 必须与该真实阶段相同。

原精确目标及 current 的配置需与原四组输入、旧配对来源、原单位 chart、原 free1186、原选行/选列完全一致。新初始化逐项比对旧 full tag，不仅比较 RESULT。

## 3. 原 target、配对和 current 的消费

目标阶段的 $q,d$、完整整数 RHS、自由列 addend、CM/eZ来源全部直接复制到一个显式“来源转入”阶段；原文件和原 tag 仍保存在 `FULL_DUAL`。这个新阶段记录旧 plain spec 及 `original_target_and_denominator_recomputed:false`，不重清 content 或共同分母。

候选反固定性使用原14坐标中前7项准确为零这一必要输入。配对 $J,J^{-1}$ 直接读取 `PAIRING/` 中的原已认证阶段；不做第二次400项生成或矩阵乘回。原 $kappa$ 的后半字段和 $R_m$ 的禁用半字段只作已成坐标的准确零检查，不运行 Laurent。

若旧完整 current 的禁用半块有非零剩余类，HP.2 立即给 A.1 的严格反证。该反证同时引用旧完整模方程认证、原十四单位分支、整目标、准确半线性定理及真实原索引。它不是“新 RR 候选没过”的标签。

若禁用半块全零，则新 current 是旧完整128×280数组的显式转入；其源文件、原 configuration SHA 和原历史链都保留。新账本以真实旧数位 $n$ 为起点，下一次提升只计算 $n+1$。禁止调用旧初始模解。

## 4. 七支求解与完整十四支检查

原14个 `(B_root,s_root)` 来源按相同 B 根、相反 s 根准确分成7对。固定选择原 branch0 的 s 根，在每一个原 B 根处取该 s 根作为代表。实际 branch IDs 和配对表写入 source audit。

只把这7支的已成 Schur逆/C块转为求解矩阵；原十四支的单位证明、clear逆以及原14×14 evaluation/inverse-evaluation仍全部读取和来源绑定。无需新逆。

每一位保原正残差：先在全部原整数坐标计算 $\Theta\chi^{(n)}-b_q$，核可除 $\ell^n$，除去后取负，再求七支原 RHS。若补集 RHS 非零，仍用原 clear 逆处理补集，不能把它强置零。

七支解在 $\chi_m$ 层配对补全，符号为 $(-1)^{m-1}$。随后原 inverse-evaluation 返回128×280数组，核禁用半块为零，并使用原正乘算子求完整 $\Theta\delta$。

首先核**七个实际代表支上的所有2560条方程**。若此检查失败，属于输入/实现错误，不是 q 的反证。七支全部通过后，再比较全部35840个原输出坐标；若出现非零残差，才使用 HP.2 的必要解唯一性作严格拒证。

若完整检查通过，提交新 current。已成正残差与修正可在新 current/历史原子提交后压成 SHA 记录，不保无用的历次数组。

## 5. 已成下一位与准确 witness 不重算

完整 dual 可能停止在 $n+1$ 位的中途。若旧 archive 已有这位的完整正残差，直接继承，核其 `from_current` 为选入的旧 current、全部可除性 flag、原负号及源 SHA；不重新求该残差。若已成完整十四支修正，也直接继承，检查其奇偶性；禁用半块非零仍由原下一位模解唯一性给严格拒证，不能再跑七支求解来重复它。

若旧 RR 在数位 n 已失败，首新请求不重做同一数位 RR。若旧 RR 已形成一个完整 witness，则可继续其尚未完成的准确验证。旧完整 witness/准确块采用明确来源转入的 alias：旧字节及 tag 留在 `FULL_DUAL`，新 alias 仅重接相同的已认证 target/witness引用，并记录 `previously_completed_exact_arithmetic_recomputed:false`。未保存的临时算子不被称为已成阶段。

新完整数字及修正、七支不相容反例、完整 witness 验证都各自原子保存。若硬中断发生在七支反例已保存而终点尚未写出之间，恢复直接读取该反例，不再解同一七支。

## 6. 三种完整终点必须分开

| `decision_kind` | 何者已准确完成 | `dual_linear_system_exactly_solved` | A.1结果 |
|---|---|---:|---|
| `original-full-exact-Theta-and-Delta` | 原全部有理转置等式与自由列 $\Delta$ | true | $Delta=0$接受；非零拒绝 |
| `original-complete-current` | 已认证原模解违反 A.1 必要的奇偶性 | false | 严格拒绝 |
| `completed-seven-branch-correction` | 代表支已解，唯一必要补全不相容；或旧完整下一位违反奇偶性 | false | 严格拒绝 |

三个终点都是本有限任务的完整决定，可以 `complete:true`。后两者绝不能声称已展开全部准确 dual 坐标。普通 RR 失败或一个 RR 向量的准确乘回失败永远不构成第二、第三类。

准确重构只对17920个允许坐标作原严格 RR，其余准确补零；最后直接调用冻结完整 verifier，不删原128块、140个补集条件、20个 cusp 坐标或原 free1186。

`source_CM_Dixon_digits:518` 只描述 CM 输入；`source_completed_full_dual_digits` 是实际旧 dual 数位；`actual_new_dual_digits` 沿旧接口表示本次链上的实际 dual 精度；另给 `newly_committed_dual_digits_in_this_source_chain`，避免把总精度说成新增数位。

## 7. 运行与恢复

核心只在 `GITHUB_ACTIONS=true` 且仓库名为 `Rogerhu12/math-research-public` 时执行；公开 guard 后关闭 Python 十进制转字串长度上限。标准库 wrapper 不导入数学核心，以 AST 读取新策略，并纯 IO核来源、schema、完整输出 inventory。

同新核心续算严格比较新 tag；原始输入三 carrier 与其 receipt 全部进入每次一日 artifact。恢复保存所有同 tag 完整阶段及实际 current；历史 `complete:false` FINAL 不约束后续已原子更新的 inventory。真正 `complete:true` FINAL 则必须完整核其当前全部引用。

预算和新增位数上限不进入数学 tag。外层 timeout 为核心预算加900秒，随后 SIGTERM/短宽限/SIGKILL；写真实退出码及可取得的 receipt，留上传余量。没有 core receipt 时不伪补，有任何完整阶段都按原 manifest保全。

所有新算术仅在本公开 Actions。Git只保存源码、参数、纸面证明与简明 run/SHA 登记；current、矩阵、向量、回执及数据转入 alias 只在一日 active artifact/carrier 内续传。
