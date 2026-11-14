# 新实源 strong M20：外 0–11 胞元接口与第二次环境中断恢复

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**恢复后的当前状态。** 原 13 端口作业 72511 的未推 JSON 随执行器消失；现已用原 SHA 源和原 SHA 输入真正重算，新包 port-norms-recovery.json 已正式 exit 0，详见第 6 节。没有从历史数字拼造旧 JSON。109 原 segment 端点仍从未运行。

## 1. 已保全和已恢复的对象

当前外头真实输入为：

| 文件 | 完整 SHA256 |
|---|---|
| closure-newg-strong-m20-frozen-d12-f225-response.json.gz | 528fd51921f7cad71445d76669b44e60279c0fc31cddf9041f8ea5b1f7477962 |
| root-real-outer-radius-v4-recovered-full.json | 28d491b998174029a80daf41e9365de6ab2c54757419de7b64f54445047b717f |
| closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |

表中文件名前缀均为 notes/2026-11-12-。

实际 M20 新实源响应的原 residual 为 $1.0904156886053144\times10^{-10}$，保留全部 20 个输入高度、865 个 40 维状态和 13 个 raw ports。它源于旧 q085 实际成功向量在有理深源新 $g$ 上的重解；不是 q095/q105 另一组强前缀，也没有因为改深源成为旧 $g$ 的精化。

已恢复文本清单为：

    notes/2026-11-12-tail-outer-text-recovery-manifest.json

其 SHA 为 c1977460c8ce9aa1b19669587bdef38d997b8b2416cadbf28eb883e7d6fe63a3。R41、13port 源、R41 polynomial helper、109 源四件均重现中断前原 SHA；通用根 note/helper 从本轮完整文本恢复，旧环境尚未记录它们的 SHA。没有将旧数值摘要填成 JSON。

## 2. 原 13port 作业做了什么

计算脚本 tail_outer_saved_port_norms.py（原 SHA 663e2f06db45ae701d6d04907231ad557d939951ec93db86f18a014ce2739e2e）先验证真实源模型、全部 160 个浅校准参数和所有物理几何字段，使用 R26 的真实端口半径与 $w,w_r,\mu$。

随后保存的 binary $Q$ 与新 NumPy finite-root 返回的 binary $L$ 定义一个**指定有限角候选**。Arb 包络该候选在所有实角上的范数及 leading/$D$/$S$。这不认证 NumPy root、finite projection 或 quadrature 误差，也不认证端口间径向轨道。

历史作业 72511 正式 exit 0，耗时 $0.743708334$ 秒、peak RSS $41772$ KiB。原输出为 319136 bytes、SHA e41fa524b12f746218310a990445dbd1d1af86449821583a4e77436182ae5a48；**当前此原文件不可用**。

历史观测如下，只用于恢复后核对，不替代新的包：

- 13 个端口指定候选的零 strip 一阶非mean范数均小于 $1/64$。
- cut 范数约 $0.0150896132936293904$；$\tau=1/64$ 时约 $0.0155698765624014559<1/64$。
- cut 全角 leading 下界大于 $0.9995727689525$。
- node 12 的同口径范数约 $1.1714360060584313\times10^{-30}$。
- $37339139/2147483648$ 只是该有限候选可接受的有理 strip，不是真实整尾解析宽度。

重算命令（在课题目录，使用新输出名）：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python computations/tail_outer_saved_port_norms.py \
      --response notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-response.json.gz \
      --radius-ledger notes/2026-11-12-root-real-outer-radius-v4-recovered-full.json \
      --ready-reference notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
      --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
      --out notes/2026-11-12-tail-outer-strong-m20-port-norms-recovery.json

原依赖 SHA：

| 源文件 | SHA256 |
|---|---|
| closure_real_outer_radius.py | bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe |
| closure_real_head_source_enclosure.py | 97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47 |
| tail_r33_middle_ordered_physical.py | ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e |

重算的 elapsed/RSS 字段通常改变，故不能要求新文件原 SHA 相同；应保存新的真实输出及资源记录，再比较数学字段。

## 3. R41 支付的严格角向误差桥

[R41](../results/R41-exact-angular-connection-inverse.md) 不依靠有限 root 的内部收敛声称。它直接由完整 $P,G$ 构造真实全角连接根，保留全部非线性 high modes 和 mean。输入

$$
\eta=\|P\|_{\tau,1}+\|P_\theta\|_{\tau,1}
+\|G\|_{\tau,1}\leq1/32,\qquad 0<w\leq1/2
$$

时，$\|K\|_{\tau,1}\leq9\eta/8$，且根号、分母和 Darboux leading 全角为正。

对含完整 mean 的有限候选 $\widehat K$，若另有
$\|\widehat K\|_{\tau,1}\leq1/16$，R41B 用最高频至多 $8m_{\max}$ 的完整有限多项式 $\mathcal E$ 证明

$$
\|K-\widehat K\|_{\tau,1}\leq\frac47\|\mathcal E\|_{\tau,1}.
$$

故可以认证保存有限候选与完整点态根的差，而不遗漏角 quadrature、mean 或生成的高频。通用候选根笔记进一步给不用统一 $\eta$ 小球的 Wiener 逆与实际分支余量门；当前通用 helper 也只是准备源，未执行数值。

## 4. 109 原 segment 端点的准备方案

脚本 tail_outer_saved_segment_norms.py 原 SHA 为
7c3f5f709a5204c3cbdc1e993e6f5286bff9e0fff251c1e7d61d8b05bb879bbb。
每胞元 9 个 segment、每段 8 个 shooting parts。cell $n$ 的 segment $j$（内到外编号）的外端对应

$$
i=72n+8(8-j),\qquad
r=r_{n+1}+\sum_{\ell=0}^{j}\operatorname{width}_{n,\ell}.
$$

所有宽度来自已经证明的 R26 ledger，不重新积分。$j=8$ 的端口将保存的 $\Pi$ 乘真实 $\rho=2^{11/4}$；其他同胞元端点不乘。最后附 node 12（index 864、cell 11 segment 0 的内端），共 109 点。

在最外 cut 上，工具保留**全部原 binary $H$**，即真实半径上的 $Q=H/R_{\rm out}^4$。这与 13port 旧工具在真实半径直接沿用 binary $Q$ 定义的是两个明确不同的候选；不能混用其范数。其余点仍只由保存的 $Q$ 定义候选。

准备命令（未执行）：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python computations/tail_outer_saved_segment_norms.py \
      --response notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-response.json.gz \
      --radius-ledger notes/2026-11-12-root-real-outer-radius-v4-recovered-full.json \
      --ready-reference notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
      --source-topic /workspace/scratch/c0de65fac774/visible-flex-source/topics/visible-flexible-closed-surface \
      --polynomial-state-index 0 \
      --out notes/2026-11-12-tail-outer-strong-m20-segment-norms.json.gz

其中 basic polynomial helper 原 SHA 为
81d5da68b0065c9e24978875c0d03cb96b6600252634c6bb028294db8e955e1e。
当前仅完成 AST/文本静态核对，没有用新源产生数据。

## 5. 端点以后仍要支付什么

109 个端点的 $\eta$ 或分支余量通过，也不推出整个径向区间的强范数。下一具体接口是沿同一个真实 source 参数 $x$，对完整候选 $P,K$ 的一阶方程建立连续残差和全频修正盒；完整推导另见 tail-outer-source-coordinate-defect.md。

现有 R29/R33/R42 的真 Green 数据只覆盖 cell $12,\ldots,224$。幅度重标不能添加缺失的 $0,\ldots,11$ 两点核。高频的深端两个 trace 分量必须共同向外处理，其可能放大不可忽略。低 46 模需新的外头两点列和深图真实导数/Schur 门；高频 cut 数据须与产生的 trace 及强前缀共同匹配，不能同时任意固定 cut 高模和完整深端两分量。

因此当前完成的是：完整代数逆与误差桥、恢复好的可运行源、明确真实半径/规范/固定 $H$ 的输入。连续外头存在、同前缀的精确匹配和完整闭曲面的全时几何仍然开放。

## 6. 新环境的正式 13port 重算

上述重建命令已经真实执行，exec chunk 810fcd 正式返回 exit 0；工具等待 $0.582993301$ 秒，脚本内计 $0.1794004750000795$ 秒，peak RSS $43652$ KiB，没有持续 session 或遗留作业。

新正式输出为：

    notes/2026-11-12-tail-outer-strong-m20-port-norms-recovery.json

该完整包重现先前记录的候选门：cut 的 $\tau=0$ 范数为
$0.0150896132936293904\ldots$，$\tau=1/64$ 范数为
$0.0155698765624014559\ldots$，不要混淆这两个口径。13 点的指定有限候选零 strip 门均通过，cut leading 下界大于 $0.9995727689525$，node 12 范数约 $1.1714360060584313\times10^{-30}$。

旧完整 JSON 已丢失，不能声称把新包的每个字段都与旧包逐项比较。当前新文件、当前源及依赖的实际 SHA、资源和数学字段去运行时间后的 payload SHA，均写入
tail-outer-restored-run-manifest.json。精确 R41 角根残差与 109 端点核算仍未运行；此重算也没有支付端点间的径向误差。
