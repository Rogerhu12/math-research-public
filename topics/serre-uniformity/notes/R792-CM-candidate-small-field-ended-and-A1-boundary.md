# 原CM短候选的小数域检验已完成，准确接受仍待单值零证

**实际结果：七项必要数域条件全部成立；原点坐标尚未被接受。**
本记录只关闭本次有限候选检验，不把518位一致性或曲线关系提升为原点的准确坐标。

## 实际执行

公开 [run43777163403](https://github.com/Rogerhu12/math-research-public/actions/runs/43777163403)，
compute job133006019703，source ea5996fe16ed1bfbc61df059a8bf8451a9acd260。
数学0.04833186599989858秒，两个新数学stage；
2026-11-15T23:53:09.651598+00:00正常结束，退出码0、error=null。
核心53bfaa736c8f8eba351aba26f2ede6c10b12a52e8c87fd0633da8833bf723668，
wrapper2d19d987a18417a0c84990169103cbdded50d84b44f5d5ce5b9f0484f2a655d2。
原185件来源由R841的小载体逐SHA续传；旧CM、Dixon、RR和原h0没有重算。

令 \(q,d\) 为那两组已登记的14坐标RR建议。
程序只把它们准确换回原 \(b,\zeta\) 基，且仅一次使用
\(B=\lambda b,\ s=1+2\zeta\)。
用同一个原h0置
\[
w=q^2-b,\qquad \widehat x=3h_0w/d.
\]
实际原数域算术证明了：

| 条件 | 实际结果 |
|---|---|
| c(q)=−q | true |
| c(d)=−d | true |
| w≠0 | true |
| d≠0 | true |
| xhat³=w | true |
| c(xhat)=ζ²xhat | true |
| d=3h0 xhat² | true |

最后五个零余式在原 \(b,\zeta\) 两多项式基中都准确归约成分母1的零，
不是只在辅助素数处测试；两个非零条件也由原数域的准确表示判断。
这给[单值准确接受判据](R787-original-short-CM-candidate-exact-acceptance.md)
所需的小数域部分。

## 尚缺的那个真实等式

仍必须另外证明原响应的
\[
A_0-qB_0=0
\tag{C1}
\]
为准确原数域等式。当前未得(C1)。

若将来有这个原大零证，则 \(q=y(P)\)，由上述非零条件和原Fb立方根唯一性，
立即有 \(\widehat x=x(P)\) 且 \(d=y'_z(P)\)；
不需第二个大零证，也不需重新跑21维范数选根。
这个条件性后果已在原接受判据中证明，本次没有另创一个精度阈值。

实际final始终保留以下false：
original_value_rowspace_zero_A1_proved、original_coordinates_accepted、
expanded_original_coordinates_exactly_certified、old_R792_success_recipe_produced、
actual_eta_or_height_computed。
degree21_cubic_root_norm_algorithm_executed同样为false。
workflow成功只表示本次有限必要条件检验完成。

## 一日来源与摘要

| 项目 | bytes | SHA256 |
|---|---:|---|
| final certificate | 5653 | 4d9a6ec5dd9c8b627b1aafd40e8baebbfc3736dffdecc16cfd3f130ede9c1b84 |
| 准确原数域候选输入stage | 10248 | e1dde57831c44df4d16b89b8b8f6a87d6ffd3975162eb2b1d80247665697cdaa |
| 七条件准确恒等式stage | 6733 | 1a5afab93ff2a7a263bc2539c97f92612ccac1a58d52afcc392a662eb99a96ef |
| stage manifest | 2131 | bb8b5249148afded4aa9aa12dcd193a22b2ff5c2021d5bcc900c6a52cdd9af60 |
| full manifest，10条 | 1528 | ce1d0e39104aade8673208d2e1210ea1d9054c37469d69e2a0bfd2fab65d15a9 |
| 原185件输入carrier | 1255615 | cba50eca45ae1490109303e67d7a73ebe43e29bd5792a116266e267332b3db6f |

配置指纹d65bf573d8a2b92a9cec8d07f5380b728c4e3d6229a9260c631269e4f414550e。
artifact14186558953，名称serre-global-R792-CM-candidate-field-checks-43777163403-1，
1371791 bytes、12成员，完整ZIP SHA256
4683b467922436bd9d9d69d1cd38938ef9c01eb3147fa3f658475f96f8940e06，
到期2026-11-16T23:53:10Z。
本地只完整下载并SHA核对这个1.37MB ZIP与12个成员、读取flags，
没有执行新的数域算术；不将这些机器stage写入Git。

这七项对当前同一候选已经关闭，不重跑。
继续原(C1)的来源正确零证，或直接消费R841的准确单位解点表达式；
原点非挠的独立有限证明使用真实518位响应，不依赖本候选被接受。
