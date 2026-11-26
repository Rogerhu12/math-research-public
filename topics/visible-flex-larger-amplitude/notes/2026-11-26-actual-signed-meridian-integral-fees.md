# 同一实际场的完整 signed meridian 积分与费用

完整实现为
[so3_actual_signed_meridian_integrals.py](../scripts/resume_20261126/so3_actual_signed_meridian_integrals.py)。
完整源码53812字节，SHA256 `1a46002ad6b1763479340b4f16472983c88d4f11c6530ce5465f78bfc64c3c4b`。
完整600秒[待用参数](../computations/resume-20261126-axisymmetric-signed-integral-first-step.json)为4493字节，SHA256 `a295d1ef36076618964988103951996b0832590e1783d269ec1221135915203b`，尚未排队或执行。
它组合已刊 a846 全胞/全角 B/L 包络、1371 实际节点向外费用及 R694 低阶积分核。
只计算 $T,T_\phi,T_{\phi\phi}$ 的完整积分与带符号部分积分。
core/cap、$\Delta$ 算术、完整 $F$ 六 jet、Gram、reach 和闭 flex 不由本件认证。

本件执行入口严格限定公开仓库 Actions。交付时没有科学试算或 fixture；
静态检查与独立源码审查不冒作实际 bound 返回。
固定 scalar profile、全部物理 omega/core/H、准确网格和实际目标均未更改。

## 1. 完整同场输入

`SignedMeridianIntegrals(actual,node,*,envelope_report,envelope_journal)` 保留
`.actual is actual`、`.node is node`、`.q is node.q`。
严格核 a846 ActualInput、1371 NodeOutwardEvaluator、7f26 完整实际算子、
30ae 误差核的实际文件 SHA 与完整 model identity。

输入 a846 包络必须真正完成全部 922 胞，且每胞覆盖整个准确径向区间和全角。
入口核对：

- report schema/source、选定 actual binding、完整 source roles、全部当前目标/场系数；
- journal 实际 SHA/字节数与完整连续 hash chain，胞号必须原顺序无缺漏；
- identity 中准确整数 SCALE、sqrt precision、全部 subdivision；
- 每个分片准确 local endpoints 和原 affine physical endpoints；
- 每胞 B/L 必须等于完整分片的逐项最大值；
- 准确单位 $T$ 的 $B_0=1$，固定 chart 未换成当前 core；
- 报告的宽度盒与同准确 affine width 的独立盒相交；
- 原实际 complete-integrator width 的 literal word。

不接受 a846 的 partial journal，不把部分 B/L 上界扩充成全域。
重新核宽度只是同一准确符号跨度的包围，不重新求解或替换 scalar profile。

同一个 q 的全部 Gauss 节点和 whole weights 取其真实 binary64 words：
$$
u_l=\operatorname{Fraction}(q.gauss_u[l]),\qquad
g_l=\operatorname{Fraction}(q.gauss_w[l]).
$$
全胞宽 carrier 取实际 `_integrate` 使用的 `np.diff(q.mesh)`：
$\widehat\ell_c=\operatorname{Fraction}(\text{该 word})$。
不假设这些浮点节点/权具备理想 Gauss 多项式精度；mass defect 全付。

## 2. 完整胞积分的中心与严格费用

记第 $c$ 胞准确宽 $\ell_c\in[\ell_c^-,\ell_c^+]$，
某角导阶数的真向量为 $X(s)$，完整包络给
$$
|X|\le B_c,\qquad |\partial_sX|\le L_c.
$$
每个实际节点的工作向量为 $\widehat X_{cl}$，1371 给
$$
|X(s_c+\ell_cu_l)-\widehat X_{cl}|\le e_{cl}.
$$

本件重建的中心是准确有理向量
$$
\widehat Q_c=\widehat\ell_c\sum_lg_l\,
 \operatorname{Fraction}(\widehat X_{cl}).
$$
这个量没有额外浮点加乘，不能与原 `q._integrate` 的浮点规约混为一谈。
后者的真实算术差由 root 的完整场消费者另行比较和支付。

令 Peano measure 为 $du-\sum_lg_l\delta_{u_l}$，
mass 为 $m$，累计函数的准确 $L^1$ 范数为 $\kappa$。
R694 给完整费用
$$
E_c=
 \ell_c^+|m|B_c+(\ell_c^+)^2\kappa L_c
 +\delta\ell_c\sum_l|g_l|B_c
 +\widehat\ell_c\sum_l|g_l|e_{cl},
$$
其中
$$
\delta\ell_c=\max(|\ell_c^--\widehat\ell_c|,
                 |\ell_c^+-\widehat\ell_c|).
$$
因此
$$
\left|\int_{s_c}^{s_{c+1}}X\,ds-\widehat Q_c\right|\le E_c.
$$
节点 shift、准确 Hermite width 与 numerical carrier 的差已经包含在 1371
节点费用中；权的物理 width 另按上式完整支付，没有丢失其中任一项。

所有三个角阶数使用同一全节点集合，不丢任何 mode 或输入位置。
准确 prefix/total 及其费用为
$$
\widehat I_c=\sum_{k<c}\widehat Q_k,\quad
E_{<c}=\sum_{k<c}E_k,\qquad
\widehat I_*=\sum_k\widehat Q_k,\quad E_*=\sum_kE_k.
$$
所有和与误差累计均为 Fraction。

## 3. 当前胞的真正 signed Peano

取任一原准确胞中的 literal 查询 $u$，以及原 `q.make_query` 返回的
工作 lift word
$$
\eta=\operatorname{Fraction}(\widehat h).
$$
整个 $1-\eta$ 用此同一 rational 作准确减法；
若真实场中的浮点 `1-h` 又有舍入，该差属于后继实际 field arithmetic 费用。

目标 signed functional 是
$$
\mathcal S_\eta[X]
 =\eta\int_0^sX\,dt-(1-\eta)\int_s^SX\,dt.
$$
查询的 `query.partial` 已含工作物理宽。逐 word 取
$$
p_l=\operatorname{Fraction}(\text{query.partial}_l),\qquad
\lambda_l=p_l/\widehat\ell_c-(1-\eta)g_l.
$$
这里分母用真实 complete-integrator width。
即使 query 内部计算 width 的 word 与它不同，上式仍准确重建实际 $p_l$；
不另加未经证明的逐位相等门。

当前胞的连续密度是左半 $\eta$、右半 $-(1-\eta)$，在准确 literal $u$ 分裂。
因此完整当前胞 Peano measure 是
$$
d\mu=
 \{\eta{\bf1}_{[0,u]}-(1-\eta){\bf1}_{[u,1]}\}\,dt
 -\sum_l\lambda_l\delta_{u_l}.
$$
每个实际符号、重复节点和非零 mass 都交给 R694。
不把当前胞改成两个独立积分误差再取绝对值，从而保留 signed 抵消。

对应的准确有理中心可写成
$$
\widehat{\mathcal S}_\eta
 =\widehat I_c+\sum_lp_l\widehat X_{cl}
   -(1-\eta)\widehat I_*.
$$
等价地，之前整胞系数是 $\eta$，之后整胞系数是 $-(1-\eta)$，
当前胞中心是 $\widehat\ell_c\sum_l\lambda_l\widehat X_{cl}$。

若 R694 对该当前胞密度和权给 $E_c^{\rm signed}$，总费用为
$$
E^{\rm signed}
 =|\eta|\sum_{k<c}E_k
  +|1-\eta|\sum_{k>c}E_k
  +E_c^{\rm signed}.
$$
这是源码 `query` 的全部公式，完整包括 current mass、宽度和每个 signed node fee。
没有假定 $\eta$ 恰在 $[0,1]$；任何 finite 实际 word 均按真系数支付。

## 4. 完整准备与可恢复的逐胞支付

`prepare(phi, journal_directory=..., resume=False, admission_seconds=...)`
以一个明确 literal angle block 为单位，按原胞号逐胞读取全部 Q 个积分节点。
同一 angle block 的全 J angular-node 张量由1371真实缓存复用。
每个完整胞立即保存 raw gzip：

- 全部 T/Tp/Tpp 工作向量的 binary64 hex；
- 每节点的准确 Fraction norm fee；
- 准确有理 cell quadrature 和完整 R694 cell fee；
- actual checkpoint、完整 field/source、完整 envelope record、literal 节点/角身份。

raw chunk 先原子落盘，然后原子更新完整 hash-chain journal 和 state。
若中断发生在 chunk 已完整落盘而 journal 尚未提交之间，
续接会严格重绑该 chunk、重算其准确有理和/费用并接入同一个 chain，
不重新读取已经付款的 T/F，不覆盖异源内容。
已提交 journal 逐胞核 hash、字节数、身份、节点和 shape。

恢复确实执行必要的准确有理重建，但这些也只在 Actions；
它不被记成新的物理 T/F 求值。
新节点计数、恢复胞计数和恢复孤立原子 chunk 计数分开记录。

自然预算检查在每个完整胞之前。
partial 返回 `complete=False` 与已完成胞数；不暴露 total，不允许 `query`。
同对象再次 prepare 可继续，新进程使用同 journal/phi 显式 resume。
只有全部 922 胞真实完成后，`.complete` 才为 True。
换 angle block 会重置所有旧数组与完成标志，不能借旧 total；
未持久化且未完成的已付节点不能被静默替换。

## 5. 固定接口与 shape

积分键固定为 `('T','Tp','Tpp')`，分别对应角导数 0/1/2。
设 $C=922$、每胞 Q 个实际节点、当前角 block 大小 $A$：

| 公开属性 | 形状/含义 |
|---|---|
| `.phi` | 只读 literal float64(A) |
| `.complete` | 同一 phi 的全部 C 胞真正准备完毕 |
| `.integrated_working[key]` | float64(CQ,A,3)，按原 cell-major/Q 顺序 |
| `.integrated_error[key]` | Fraction(CQ,A) |
| `.cell_exact[key]` | Fraction(C,A,3) |
| `.cell_error[key]` | Fraction(C,A) |
| `.prefix_exact[key]` | Fraction(C+1,A,3)，首项准确零 |
| `.prefix_error[key]` | Fraction(C+1,A) |
| `.total_exact[key]` | complete 后才有 Fraction(A,3) |
| `.total_error[key]` | complete 后才有 Fraction(A) |

partial 时仅前 completed_cells 个胞及其 prefix 有效，
其余缓存不得读取为科学数据；所有全积分消费者必须先核 `.complete`。
完成后各公开数值/准确数组设只读。

`query(cells,u)` 返回：

- 原 `query` 对象，供后继同场 `fields_torch` 直接使用；
- `signed_exact[key]` Fraction(P,A,3)；
- `signed_error[key]` Fraction(P,A)；
- 准确 rational `hhat` 与 `normalized_partial_exact`；
- 原实际 partial 数组、current signed Peano 的 mass/kappa/weights；
- 同一当前完整 node-read identity。

本件不会调用 core inverse、闭合、完整 field 或 Gram。
后继可将 `.integrated_working` 交给同一个 `q._integrate`，
再与本件有理中心比较其实际规约；不能把这里的“准确有理中心无浮点费用”
误解为原 integral/closure/field 的浮点费用为零。

## 6. CLI 与有限范围

入口消费和1371相同的实际文件，另必须提供
`--envelope-report`、`--envelope-journal`。
默认查询全部原7377观察地址和原513个quarter-angle地址；
也可显式提供 REQUEST_SCHEMA 的 literal cells/u/phi，只声明该有限集合。

CLI 按原 angle block 外层运行。
每个 angle block 的 node准备写独立 `integrals-angle-XXXX` 目录，
完成准备后逐 query block 保存 signed exact/fee 的 raw gzip 与完整外层 journal。
600秒自然预算可以在准备阶段或查询阶段返回；
续接复用实际已付款节点和已提交查询，不将 partial maxima 升为完整范围。

所有 raw 目录必须在 Git 仓库之外，原始数据只在 runner。
report 只声称所列有限查询的完整积分费用；
它不把这些点、全角 B/L 或全922胞节点覆盖冒作最终连续曲面 Gram/reach 结论。
