# 既成正区闭行到完整帽区本征常数的最小消费合同

## I.1 范围和输入

本消费者仅在公开 Actions 内读取已经完成的 4650 行 certificate，将它限制到准确帽区 $[9/10,25/8]$，输出 $\beta,\gamma,K$ 的完整径向上界。原 target、ODE、FFT、三次 trial、连续修补和 intrinsic 网格均不重新计算。

完整原 gzip 的 SHA256 为 ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d，原字节数 6223338。它只按 notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json 的原四个 parts 恢复。该 manifest SHA256 为 32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3；不新拆分、不改 gzip 容器或数值行。

原 producer scripts/fourfold_codazzi_current_positive_complete_coefficients.py 的 SHA256 为 1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c。它在帽区每行的 intrinsic 字段完整保存 beta、gamma、K 的原闭球，另有 interval、actual_scalar_germ 和 intrinsic_provenance。

## I.2 身份和覆盖

消费者先核验原 kind、complete、coefficient_cover_complete、无 failure、空 pending、4650 行及完整区间 $[0.2384058742994,25/8]$。原 native 的 producer、candidate、intrinsic object 和 cap-cache SHA 均必须原样相同。

原 affine 本征参数中心按 object JSON 的 delta_fraction 精确读取，等于 $-7789843107295549/4611686018427387904$；原参数半宽为 $10^{-9}$。这里继续包含同固定物理 $\eta_0$，不是物理参数为零。原 compact 参数为 $\nu_0=-2572625729470897/72057594037927936$，原 alpha 与完整 M32 candidate 身份也严格保留。帽上 compact bump 恒为零，但本消费者不把其它改变本征参数的对象纳入范围。

完整原行首先逐行核无缝覆盖。对与帽区有正长度交集的每个原闭行 $I_i$，使用准确有理交段 $J_i=I_i\cap[9/10,25/8]$。所有 $J_i$ 按序必须无隙、无重复地覆盖准确帽区；单个共享端点由闭包保证。原 actual_scalar_germ 必须覆盖该完整原行，且每个选中行的 intrinsic_provenance.kind 必须是 same_intrinsic_cap_v2。其 row 是原 1334 行缓存的合法索引，不允许用原根附近新构造的闭行冒充帽缓存。

不在 binary64(0.9) 处截断。即使原行跨 $9/10$，其完整原球也包围真正交段，因此无需新求该交段上的 target。

## I.3 原球与三个上界

令原闭球为 $\boldsymbol\beta_i,\boldsymbol\gamma_i,\boldsymbol K_i$。以有向算术计算

$$
b_*=\max_i\sup|\boldsymbol\beta_i|,\qquad
g_*=\max_i\sup\boldsymbol\gamma_i,\qquad
K_*=\max_i\sup\boldsymbol K_i,\qquad
k_*=\max(1,K_*).
$$

每个选中 $\boldsymbol\gamma_i$ 和 $\boldsymbol K_i$ 必须严格正。输出的三组常数给出

$$
|\beta(r)|\le b_*,\qquad
0<\gamma(r)\le g_*,\qquad
|K(r)|\le K_*\le k_*
\quad(9/10\le r\le25/8).
$$

原 K 球中已经支付的全正区 floor/intersection 是原 native 的一部分，不在此次重新证明或改写。消费者不把 field-dependent radial_speed 误作 gamma，也不从有限角样本或浮点中点取最大值。原闭球的完整半径参与上端计算。

原 $\beta,\gamma,K$ 不依赖对 moving $u,v$ 做的连续修补；因此该同本征对象的上界适用于相同固定 $\eta_0$ 的帽合同。任何改变本征对象或改变其有效参数域的结论都仍须另证。

## I.4 已成联合界只作原证据输入

公开 run 43674204314 / 1 已完成完整 $Z$ 的 660 个帽片联合界，native SHA256 为 dd236bb30e17ed457a45bd38a24ff3188d896562e5e2e4189d5f3a5579cdc39c。此次仅读取其原 complete-cap-Z-joint-summary.json 和原 process.json：

- summary SHA256 为 67fa3c6664ab90a1dbbc91960b10f4f75c8f6372fee272ddca8f780f834efb86；
- process SHA256 为 61896c151fcd7593076195e0d320713f829a087cb9e3b597bbbd61b0c650ae61。

必须核同完整 Z 定义、同帽区、660 片、10 门全过和实际 child0。原联合范数不重新计算，也不据此增加新的 Bernstein 格。此次新常数和原联合界可以作为后续合同的两个独立已付输入；本消费者不先行声称该后续小量门或边界逆已经通过。

## I.5 收据、恢复与限制

每个选中行保留完整原行的确定 JSON SHA256、原区间、准确交段、germ、provenance 及原三闭球。每 64 行保存实际前缀，复用仅接受同 source、同六项 input SHA 和同原有序行的准确前缀。已完成数学可在后续出版失败后原字节复用；有真实数学 failure 的对象不得无修改重跑。

最终记录选中行数、上界球、取得最大上端的原行、全部覆盖门和 0 个旧数学重算。原完整 gzip 留在 Actions artifact；原四片和原容器来源不变。真正摘要必须小于 60000 UTF8 字节，不能人工分片原过程绕过文本限制。

范围只到上述完整帽区本征常数；不授未知 full-high 逆、真正参数响应、非线性同域解或全 Schur 闭合。
