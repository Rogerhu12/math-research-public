# 原完整 Popov 商的 native cyclic 返回及标量厚度恢复：隔离软件候选

本稿说明未绑定生产的 original_cyclic_denominator_return.py。它只接受原完整方阵 M，保留原系数环、原基和全部生成行。没有原 rank 306 几何计算、性能结果或 PASS 声明；当前 v15 不改。

## 1. 实际源码入口与完整 Popov 性质

原 original_native_pair_reset.py 的 prepare_backend 用固定 19 处文本替换生成完整 R975 reducer。本候选先调用原准备函数，随后在它的隔离副本中仅把 ast.parse(source) 前的停止点改为返回已经生成的 source 和原 native 模块。逆替逐字恢复原 prepare_backend；返回 source 的 SHA256 必须等于原准备回执的 exact_generated_function_sha256。没有重写 19 处替换，更没有复制 Sage 库实现。

对这个相同 source，只在原 record() 中插入实际多项式系数捕获。原 swap/add/scale/Bezout 所记录的完整系数进入已通过公开软件检查的 CompleteRowOperationStream。截断点严格在

    delta = popov(0, m, [0]*n, "whole unshifted Popov")

之后。这个原 popov 并非只有互异 leading positions：它随后对每个完整行降低所有非本行 pivot 列，核每步 own leader 不变、所有列次数严格低于对应 pivot 次数，再按 leading column 排序。故返回完整 P 满足：

- P[j,j] 单首，次数 d_j；
- 每个 i≠j 都有 deg P[i,j] < d_j；
- 第 i 行的完整 leading pair 是 (d_i,i)；
- δ=Σ_j d_j 是整个原商长度。

本候选再次逐项核这些条件。调用结束时的 P 是原完整记录 E 的结果 P=E M，不是另取的近似或仅同 determinant 的矩阵。

非素系数不自动降层。候选只沿原 _entire_prime_subfield_inputs 对每个实际系数及反向完整多项式进行验证。没有全部下降时，进入原完整算法的同输入回退。

## 2. 完整商及 native Krylov 返回

取 k 为此次被验证的原素子域，R=k[t]。上列完整 Popov 性质给出原商

    Q = R^n / row(P)

的全部标准单项式基

    { t^a e_j : 0 ≤ a < d_j }.

其大小恰为 δ，所有重复因子和幂零元均留在 Q。没有取 radical、残域、半单商或抽样秩。

令 T 为乘 t。非边界单项式按次数移一位；第 j 个边界的精确像是

    t^d_j e_j = -(P_j - t^d_j e_j)   in Q.

右侧每一列已满足对应标准次数界，所以可直接写入全部 δ 个坐标。零度列的 e_j 则由完整第 j 行给出负的非对角部分。代码用一张 δ×q 的 packed native 边界矩阵，加全部移位坐标表示 T，其中 q 为 d_j>0 的列数。

固定原最后基向量 e=e_(n-1)，不搜索更方便的输入或生成元。构造全部列

    K = [ e, Te, ..., T^(δ-1)e ]

以及全部目标 T^δ e 和 e_0,...,e_(n-2)。采用 Sage 10.6 自带的 Matrix_modn_dense_float，并在唯一增广矩阵上调用 echelonize(algorithm="linbox_noefd")。必须检查前 δ 列全部为 pivot；仅增广矩阵满秩不够。满秩后仍完整核

    K * solution = all_targets.

若秩小于 δ，该原向量不是 cyclic，候选立即转同一原 M 的原完整算法；不删缺失分量，不更换生成元，也不把较小的 annihilator 冒作原商。

满秩时得到唯一 q(t)=t^δ−Σ q_a t^a 以及 f_i(t)，满足 q(T)e=0 和 e_i=f_i(T)e。于是完整上行 Hermite 候选为：

- 第 i<n−1 行：e_i−f_i(t)e_(n−1)；
- 末行：q(t)e_(n−1)。

其前 n−1 个 pivot 为 1，末 pivot 单首且次数 δ。原末基向量是 K 的首列，其余原基向量全部作为目标，故这确为整个商的 presentation，不是部分 cyclic 子商。δ=0 时单独返回完整单位商；它并不意味着原 scalar content 可以丢弃。

实际原接口核对依据是固定 Sage 10.6 的 matrix_space.py 和 matrix_modn_dense_template.pxi：

- https://github.com/sagemath/sage/blob/10.6/src/sage/matrix/matrix_space.py
- https://github.com/sagemath/sage/blob/10.6/src/sage/matrix/matrix_modn_dense_template.pxi

显式实现名是 linbox-float，不能误写 linbox。linbox_noefd 在该源码中执行完整 reduced row echelon 并保 rank/pivots 缓存。此处调用库入口，未复制其实现。

## 3. 完整 polynomial C 与实际 U

商坐标只提供候选 H。代码随后在原 prime P 上对 H 的每个完整行作多项式除法：

1. 取 current 的完整最大 leading pair (d,j)；
2. 若 d<d_j，则它不是零余数，必须拒绝；
3. 用 current[j].quo_rem(P[j,j]) 得完整商 q；
4. 对全部列执行 current←current−qP_j，并在第 j 个多项式坐标累加 q；
5. 逐步核完整 leading pair 严格下降。

这不是“末位一次回代”假设。每个完整行必须归零，最后完整核 C P=H。全部算术在原 polynomial ring，未作分式求逆或清分母。

若原记录为 P=E_s⋯E_1 M，则已通过公开软件验证的 reverse_right_return 给

    U = C E_s⋯E_1.

操作按逆时间右乘；add 对应列更新，Bezout 同时用两旧列，所有实际系数保留。最终调用已通过的 restore_complete_denominator_transform，在 unchanged original coefficient ring 再核：

- 完整 C P=H；
- 完整 U M=H；
- 动态 current _hermite_remainder_rows(M,H) 为零；
- 每个 H pivot 单首非零，H 为完整上行 Hermite；
- 完整 determinant polynomial 及其 degree；
- 所有输入数值、原环和 caller mutability 不变。

因此纵使候选商坐标实现有错误，同 determinant 或同 rank 的错误矩阵也不能通过最终验收。双包含与非奇异 H 同时认证原完整行模和 U。这里不伪造原 full_polynomial_left_division 已执行的回执。

## 4. 标量 content 恢复

令 h 为 M 所有 entry 的实际单首 gcd，逐 entry 精确除得 M0，完整核 h M0=M。只有 gcd 已为 1 时才能提前结束 gcd 扫描；即使如此，每个原 entry 的除法与回乘仍全部核验。

若 P0=E M0、C P0=H0，则取

    P=hP0,   H=hH0,   U=C E.

由于 h 为中心标量，P=E M 且 U M=H；C 及所有实际行操作系数不变。每个 pivot 与同列非 pivot 同乘 h，Hermite 次数不等式保留。完整 determinant 与长度是

    det H = h^n det H0,
    length = n deg h + length(row(M0)).

代码按原 M/P/H 做完整返回，并核原 determinant hash。绝非只对 M0 出回执；所有 h 的非约化厚度完整保留。

在实际原 algebra 的乘 D 矩阵中，旧证已给完整单位坐标 e，使 e M_D=D。原乘法表在 R 上整，故 D 的所有坐标 content 除 M_D 的所有 entry；反向由 e M_D=D 得到同一个单首 content。这解释可选先扫 D 坐标的等价性。本软件实现仍直接扫原 M entry，不假设当前 MD 真有非平凡 content，也没有计算其数值。

## 5. 完整同输入回退与作用范围

以下实际失败都返回原未除 h 的完整 M，调用原 R975 的完整 reducer：

- M0 不能沿原验证降到素子域；
- 最后原基向量的全部 δ 列不能生成 Q；
- native 分配或估计运算超过明确工作预算。

回退同样捕获全操作实系数，取 P=H、C=I，再由已通过的 reverse return 得全 U。完整原 determinant、余数和 nilpotent 长度不变。运行中若完整多项式坐标、回放、时间或操作预算耗尽，则明确拒绝，不把中间结果冒作 PASS。

没有新 production bind，也没有修改原 general reducer、division、projector、geometry 或 v15。新 API 不接受 attached block；该范围只针对整个方阵 denominator image。软件还在实际 complete_returns wrapper 安装后分别复核 cyclic 及非素回退两路，动态余数入口必须与当前绑定一致。

## 6. 资源与软件检查边界

显式 native 数组存储估计为

    3δ² + δq + 4δn + 4δ + q

个 4-byte field cell，保守包含 K、边界、全部 targets、augment 临时矩阵及其 mutable copy、解和完整乘积返回。该数不含 FFPACK 内部工作区、Python对象、原多项式 P/C/H/U 或 native polynomial rows，不能当总峰值。先前单张 δ×(δ+n) 增广矩阵约58MB的估算不是整个算法内存。

native solve 仍有完整 δ³ 量级工作；Krylov 乘法还保完整 δ²q。C 的全 Popov 除法与逆序 U 可能成为新的主要开销。这些均有明确操作/存储预算，可调整但不能通过减少商长度来规避。没有 δ≤256 的数学接口限制，也没有对原306/3670实例作速度承诺。

固定 420 秒检查安排 14 组完整比较、17 组拒错。完整比较包括：

- 原 column-reduced Popov 尚非 HNF 的实例；
- 幂零 cyclic 商、immutable 原输入；
- 真正二次系数的 scalar content 和全部厚度恢复；
- content 后单位商、rank-one 完整厚度；
- last vector 不生成全商、真正非cyclic 非约化商；
- 非素 whole quotient 的 unchanged 原算法回退；
- 两个原 prime29/41；
- 明确工作预算回退；
- 96维完整幂零商；
- 当前原 native full-return wrapper 绑定后的两路。

每一例均和未改原 HNF 以及 Sage 10.6 官方完整 (H,U) 比较全矩阵，并核全部原余数与完整长度。拒错覆盖错误原输入、错误 Popov 条件、非整包含、同 determinant 错候选、仅 rank 错候选以及完整工作预算。

这些是待公开 Actions 执行的软件要求。当前仅完成静态原文/接口/文本逆替及 hashes 核查，未本地运行语法或数学。

## 7. 固定公开软件请求与准确源码

2026-11-28 UTC，root已全文审阅 helper/checker/proof，核原生成 source 的逆替、完整标准基、K 全秩判定、C/U 返回和 content 厚度。修正显式内存计数为3δ²，并把末原基向量准确记为 generator、其余为 targets；未进行本地语法或数学执行。

本请求复用原 `.github/workflows/rank2-sha-complete-quadratic-api.yml`，固定 Sage10.6 镜像 `19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb`、host420秒及原4CPU/16GB上限。既有selector只加这个白名单分支，workflow及原生产文件均不改。完整21源闭包在 `ci/original-complete-quadratic-api-request.json`，所有旧源pin不变。实际执行前无PASS或原306/3670性能声称。

| 文件 | bytes | SHA256 |
|---|---:|---|
| scripts/original_cyclic_denominator_return.py | 30907 | 4ebbe8018347d9bf6269d6e0d83960224bb399fa5ae1998b7d91e3c1ba96fbf1 |
| scripts/check-original-cyclic-denominator-return.py | 21976 | 6113c7b4eb46c00b40cad02028a8e97705e219cbef8175ac5d4e6ed1ef35f396 |
| scripts/check-original-complete-quadratic-api.py | 10711 | 1b85e87d39721e220e18ad5564835768d01351af1b6664370b98f98bfe0d55af |
| ci/original-complete-quadratic-api-request.json | 3013 | 5403859a01e98332776bb58c64c7a99b82fd46c26ca05becbbfdcca490d16dde |

目前v15仍唯一原heavy：run46112816717/job140879915022；06:39:19UTC状态为step4 in_progress、日志BlobNotFound，无原完整数学返回。软件检查完成后消费实际完整日志、全source hashes和全矩阵回执；未完成则根据真实首处故障修复。主目标仍是固定rank≥2曲线于无穷p的通常全Sha有限，软件不替代该目标。
