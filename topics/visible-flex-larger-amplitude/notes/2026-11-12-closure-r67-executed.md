# R67 实际外局部接口：执行与恢复记录

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-12。

完整证明已放在
[R67](../results/R67-actual-local-schur-and-shared-centre.md)。本记录只保留
执行和续作位置，不另声称完整外头闭合。

## 已完成的同源真实流

`closure_outer_taylor_shared_flow.py` 在原 g、原真实 source 表、固定
global μ11 下完成 cells11/10、m2/m4、共同斜率中心列和两独立基列。
全部18段、3,478个 Taylor 面板、8个临界根括号，11门均真。

旧 session 34414 的工具句柄后来过期；保存的 resource 包已直接记录
wait4 child exitcode 0、signal null、110.074442 s、30,824 KiB。
此退出事实没有由句柄过期推断。

冻结的24件清单是
[outer Taylor manifest](2026-11-12-closure-outer-taylor-flow-stable-manifest.json)，
SHA256 `776227de0d94d74605e596c902b83d1a16a43336427580a98d195cc225316f2f`。

## 三个已执行的小账本

| 入口 | 正式退出 | wait4 秒 | 峰 KiB | 已付范围 |
|---|---:|---:|---:|---|
| `closure_outer_shared_schur_cut.py` | 0 | 0.530611 | 29896 | 同斜率 Möbius cut 项、两行×全46参数、明确 C²候选重设、完整 mean 域 |
| `closure_r67_fraction_bounds.py` | 0 | 0.179320 | 11520 | 21个严格数界和10个多项式恒等式，纯 Fraction |
| `closure_outer_linear_cancellation.py` | 0 | 0.405787 | 14884 | 完整候选线性 forcing 与端点准确合并，纯 Fraction |

三次 resource JSON 都保存完整可重复命令、源 SHA 和真实 wait4 状态。
第三次 session 69324 另由工具正式 poll 得 exit0。

第一项最关键的数值事实是：原 m2 cut-only 差经真实背景图传播后约为
R61 参数轴的3198.48倍。保持 g/H 的 dyadic cut jet 重设将该分量降到
小于0.000298351轴，但补偿的线性 forcing 并未被删除。

第三项准确计算整个线性相消后的
$q_m-Q^{\rm saved}_{R,m}/S_{0,m}$：m2 在 node11/10 约为
$9.6530184\,10^{-48}$、$1.9102867\,10^{-47}$，远大于仅 cut 动量差。
这两个点是可重新选取的内部候选节点，不能当成课题额外固定的边界条件。
完整非线性外源尚需加上，未据当前数值宣称外问题无解。

## 量纲与关联必须保留

- $H_m=r^4Q_m$，此转换没有 $w$。
- $K$ 与 canonical μ11 动量的转换是
  $c_b=\sqrt{12}\mu_{11}/(b^4w_b^2)$。
- 分子与分母必须保留同一个 $s_m=\widehat s_m+\delta s_m$。
- `cut_only_axis_ratio_lower` 对包含零的 m4 使用宽 Arb 实区间，保存的
  下界可以略小于0；这仍是保守下界，本文只使用其严格上界，没有宣称
  非负量本身为负。
- 全46输入头导数、完整高 trace 和完整 mean 继续沿用 R61；本文只支付
  两个低输出，不能据两行的小范数代替完整外 Schur 逆。

## 当前直接续作

原 `tail_outer_candidate_defect.py` 可在不改 source 的情况下插入只读
`full_mean_residual_bounds` 回调，对每个原 material 面板记录完整 N 源。
下一件 owned `closure_*` 记录器将保留面板位置、真实 $w,r,r_x$，以及
完整 mean/逆分母下 N2/N4 的符号包围。

接有序背景 Green 功能时，source-x 的 N 进入 global v_x 的系数必须是

$$
(r/r_c)^{m^2-4}\frac{r^4w^2}{\sqrt{12}\mu_{11}}.
$$

不能把整胞元最大的 N 与另一个位置最大的 $w^2$ 同时代入；也不能把
候选线性源、cut 差和背景列各自绝对值后丢失 R67(67.35) 的恒等相消。
记录器和有源 Green 尚未执行，不包含在本批完成声明中。
