# R854：原 N112 精度耗尽后的同核 N224 续接

日期：2026-11-16。本文登记真实结束点、同一数学身份的续接方式及精度边界。它不改原 R854 核心、DVR helper、包装器、方法或原 U.1 规范解；不把待执行的 N224 层写成已经完成。

## 1. 真实结束点

原公开 run 为 43880489423，job 133344905148，source commit 为 20984736d0376b262b83e9173bcfc4c3205f6056。其原始 core receipt 明确记录：

- exit_code 为 125；
- error 为 “NeedPrecision: Original p41 saturation has no further known B digit.”；
- seconds 为 11477.056374425；
- 原 run 的 outer_timeout 为 false；
- unit_minor_and_left_inverse_bound 为 null；
- four_response_balls 为 null，四响应认证标志为 false。

实际末尾日志依次保存了 R854-p41-N000112-saturation-000111 的全部行块、矩阵与右端索引、完整状态、上一工作状态的退休回执，以及 R854-p41-saturation-profile-000111.json.gz，随后正常写出阶段清单和不完整 FINAL。因此本次是已知统一化元精度耗尽；不是未知原因的超时，也没有取得四个原 41 响应球。

原配置 SHA256 仍是
227767127d21d420d5ffdcef87c8f18627cdc92fd22b4d7cf9b5d036c997f10f。

| 原件 | 字节数 | SHA256 |
|---|---:|---|
| 全输出 manifest，1184 项 | 200277 | 729e2eb287cf2680e2698fea2b4b0286f7293a27e82e6b37fbaf9813c1b74726 |
| manifest reference | 223 | 74ddaa1667a66072d66da18b1eace4e3dba4c7da679366d02aace5eea9ea6fed |
| core receipt | 12847 | 170642c6c53173eb287e22a060bbdfad76491a67fd37e8e735248da32617456a |
| 不完整 FINAL | 13177 | 37314bcb4a957c167898e1d3e6a470a40932f7d5729a063335e08e3f3c18e7ed |
| 数学阶段 manifest | 64717 | 9a7e2c4221eb1134eb3a84556e96bd73b5296ca99761532f1b54046bb31ce998 |
| 原输入 carrier | 135471278 | bca10118a3f81600c83f5bf4232090555da2527cb8a3bdbb79ffff70fb70d104 |

恢复使用原 artifact 14248459820，名称 serre-global-R854-original-p41-four-responses-43880489423-1，266362302 字节，完整 ZIP 身份为
3780001833a13e866fcdd4802234b892c4d49ac73ead623809956d0e10cdfd66。
其平台到期时间是 2026-11-17T17:10:18Z。

上述小件的纯 IO 来源为 run 43919701128、read job 133483549799 的标签 R854-original-N112-actual-ended。该读取只核实际选中原件，不声称重新哈希了原 archive 的每个字节；其小 metadata 包没有代替完整恢复所需的原输入 carrier 和算子阶段。

## 2. 同一核心和数学身份

原文件保持：

- core R854_original_p41_response_solver.py：
  1feb579a88879739a250f889ab1818019acb8f1156a0e3f34d57b8524024125f；
- helper R854_p41_DVR_linear_algebra.py：
  fa545b181fa5b77758622d1862adfd4445cd05d44fdc65dda92f738ebe522c0d；
- wrapper R854_public_original_p41_response_solver.py：
  f6b97a7d0640a03fa099d3b0b04541318e53ddbcf611a876f877b3dc42c7f0ae。

仍按 [原 R854 方法](R854-original-41-cleared-row-saturation-and-four-responses.md) 和 [几何整化补节](R854-original-41-geometric-row-scaling.md)，以原 $B=\lambda b$ 为统一化元，对原 $M_0=S\mathcal M$ 及同一 free1186 右端求解。原十四坐标、原 2560 行、2420 未知、原 CM 四泛函与 82 尺度全部不变。

新的请求相对本次真实结束请求，只改变：

1. operator_B_precision 从 112 改为 224；
2. resume 改为上述真实已结束 artifact，接受本次真实退出码 125。

预算仍为 300 分钟，请求四球绝对 $B$ 精度仍为 7。发布者可以另更新其已经真实读取的规则 commit；该 IO 元数据不改变数学身份。

原 wrapper 的 stable_job 明确排除 resume、预算、规则登记、operator_B_precision 和 requested_response_B_precision。原核心 tag 也不把请求精度计入身份。因此没有另立核心身份、修改旧阶段 tag 或伪造 source receipt 的需要。

## 3. 必须复用什么，新增计算是什么

恢复先按完整原 manifest 核输入 carrier、1645 个数学来源成员及 parent metadata，恢复实际仍存在的所有原子数学阶段和退休回执。完整清单是当前事实；历史不完整 FINAL 不覆盖它。

旧 saturation-profile-000000 至实际 000111 的行列选择、剩余域逆、组合矩阵和输入剩余 SHA 保持原字节。新精度层每次先比较实际剩余矩阵 SHA，再读取旧 profile，不能重新 RREF、重新选图或把旧行操作计划冒充新结论。当前没有已经完成的 Dixon 数字可继承；这不授权借用原辅助素数的任何数字。

N224 的算子阶段有自己的 N000224 前缀。冻结核心会在较大模数下形成新代表，然后逐坐标核与实际旧 N112 低位相容，并把原低位嵌回新数据；旧阶段文件本身不改。若两精度对应同一整数模数，则已有分支直接复用原整数系数。

必须如实区分成本：当前核心不是只对高位差分运行的优化 kernel。它需要在新精度矩阵上应用原已知行组合及除 $B$ 操作，以取得原状态在更高精度下的新值。这些是新精度层的算术，不能称零成本 IO；但其旧 rank/profile/逆/组合不重算，也不会重建原相位、Laurent 源或辅助素数图。后续预算停点仍按原子行块、状态和退休回执继续。

## 4. 饱和次数的准确含义

以下是对现有算法的精确停止解释，不需要新计算 Smith 分解。

令 $\mathcal O=\mathcal O_{L_{41}}$，$\pi=B$，$n=2420$。令 $\Lambda_h\subset\mathcal O^n$ 是第 $h$ 次饱和后全部真实行生成的整行格。原 U.1 已证明 $\mathcal M$ 列满秩，而几何行尺度可逆，故 $\Lambda_0$ 为满秩子格。

第 $h$ 步选择剩余域独立行 $x_i$，并把其他行减去实际整 lift 组合，得到
$$
d_j=x_j-\sum_i c_{ji}x_i\in\pi\mathcal O^n.
$$
算法下一行格由 $x_i$ 与 $d_j/\pi$ 生成，且恰有
$$
\Lambda_{h+1}=\pi^{-1}\Lambda_h\cap\mathcal O^n. \tag{854N.1}
$$

一边包含显然。反向若 $\pi y\in\Lambda_h$ 且 $y\in\mathcal O^n$，用 $x_i,d_j$ 表示 $\pi y$；对模 $\pi$ 的独立行约化，$x_i$ 的所有系数必须可除 $\pi$。除一次 $\pi$ 后，$y$ 就在算法的新行格内。该证明同时覆盖冗余行和准确零行，并不把零行反复相除看作进展。

设 $\Lambda_0$ 的 Smith 指数为
$$
0\le a_1\le\cdots\le a_n.
$$
只为证明选取一个整基；执行时不需物化此基。由 (854N.1)，第 $h$ 步的指数为 $\max(a_i-h,0)$，从而
$$
r_h=\#\{i:a_i\le h\},\qquad h_*=\min\{h:r_h=n\}=a_n. \tag{854N.2}
$$
这也恢复原子式理想的严格下降证明。

本次在 $h=111$ 仍没有单位图，所以已证
$$
h_*\ge112.
$$
没有读取或推测具体 $r_{111}$。旧有限 profile 序列不能单独给 $a_n$ 的上界：保持前 112 层相同而提高未出现指数，仍可产生同样已见秩。故 N224 是合法的下一有限精度层，**不是**单位图或四球必成功的高度保证。

## 5. 单位图出现后的严格充分精度

一旦真实单位图在深度 $h_*$ 出现，源码保存：

- 原单位子矩阵；
- 固定解分母 $\delta=h_*-q$，其中 $0\le q\le h_*$ 为实际证明可除去的右端整因子；
- 原左逆下界 $w_*=\min_{i\in I_*}w_i$；
- 四个准确泛函共同的 $41$ 分母指数 $s\ge0$。

这些量在当前终点尚未全部产生，不能预填。

对于新的原算子精度 $N>h_*$，单位矩阵至少保有 $N-h_*$ 位；右端除去 $q$ 后至少保有同样精度。真实单位方程的整解因此由 Dixon 得到 $N-h_*$ 位。令其选定有限多项式代表为 $\widehat u$。因为 $M_0$ 整，全部原整化残差分子满足
$$
v_B(M_0\widehat u-B^\delta b_0)\ge N-h_*.
$$
原 R854 仍实际检查所有残差，不以这个理论下界替代乘回。

源码最终报告的共同四响应保证精度为
$$
\min\{N-\delta,\ R_{\rm num}-\delta+w_*\}-7s, \tag{854N.3}
$$
其中 $R_{\rm num}$ 是完整原残差分子的实际已证下界。因此以下是充分条件：
$$
N\ge R_{\rm requested}+h_*+\delta-w_*+7s. \tag{854N.4}
$$
原变换下界从零开始，每步至多降低 1，故 $-h_*\le w_*\le0$，且 $\delta\le h_*$；更保守的
$$
N\ge R_{\rm requested}+3h_*+7s \tag{854N.5}
$$
也充分。两式只是单位图产生后的严格规划界；不能在尚未知 $h_*,w_*,\delta,s$ 时把它们解释成 N224 已足够。

原满列秩保证 $h_*<\infty$，而原泛函分母有限，所以持续增加真实精度在数学上有有限充分终点；它不提供当前 scope 的时间保证。最终成功仍要求原单位逆、全残差证书和四球各真实精度达标，A.1、原单 Z 和原高度标志继续为 false。

## 6. 执行边界

当前交付只含真实续接请求和本文，无新数学运行、无新核心/包装器、无第二次 dispatch。旧原件只读，发布与实际启动由主分支负责人执行。新运行若预算停或再次请求精度，应继续保留它实际完成的层和真实原因，不回退到旧 N56/N112，也不把未出现的四球填入后继 R858。
