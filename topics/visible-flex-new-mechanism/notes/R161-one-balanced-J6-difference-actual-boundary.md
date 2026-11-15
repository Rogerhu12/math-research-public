# R161：唯一 J6 balanced 原差的完整实际与未决边界

日期：2026-11-15。**已完成的公开实际回执；没有新增完整成员或非成员定理。**

本次严格消费 [R160](../results/R160-general-pure-J6-identity-and-balanced-mixed-entry.md) 已证明的 pure 有理身份，按 [R159](../results/R159-balanced-mixed-faithfulness-after-pure-cancellation.md) 只检验一条 balanced mixed 原差。实际成功完成，但 sound 代表仍有 176 项，因此完整 $J_6=K_6$ **尚未证明**。这也没有证明该身份错误或 $J_6$ 非成员。

不因 job success 把数学未决记作通过，不因不完备归约的非零余项登记新的真实维数。本稿读取已有公开输出，没有重新执行研究目标。

## 1. 同一个完整目标与已付 pure 前提

目标是 R136/R141 的完整正规加速度系数

$$
J_6=[h^{-2}]\bar A_{kk},
$$

其 family 为 `A_kk`、状态键为 `[-2,0,0,0]`，真实 profile 仿射权为 $-2$。这里与弯曲相位模式 $-2$ 的编号区分。

R160 的准确完整响应组合为

$$
\boxed{
K_6=-\frac1{64}C_0-\frac1{64}C_{88}
-\frac1{128}C_{41}-\frac1{32}C_{73}
-\frac5{128}C_{81}+\frac1{256}C_{193}.
}
\tag{1}
$$

全局列号沿用 $C_{8j+a}=\mathcal B_{P_a}(W_j)$，均为完整两模式真实响应。R160 已经通过完整原差证明

$$
\pi J_6=\pi K_6,
\qquad H_6=J_6-K_6\in U_{-2}\cap\ker\pi.
\tag{2}
$$

本次消费 run43660884663/source b41c6f13ffbe56543d3593acb0b9023d8320e93c 的成功证书，核对其 307 项 pure 原差 SHA 和原差零结论，再读取 (1) 的六项准确字符串分数。没有重新运行 pure 归约、有理求解或旧 31 条关系。

由 R159，本次唯一新目标是

$$
\boxed{\Xi(H_6)=\bigl((J_6)_{-2}-(K_6)_{-2}\bigr)_{(2,2)}.}
\tag{3}
$$

$\Xi$ 只取 $q,\bar q$ 各二次的完整原式。若 (3) 取得 sound 零证明，结合 (2) 才可推出完整 $J_6=K_6$。本次没有取得这个零证明。

## 2. 完整原根与真实同一性

只解码七个已发表 mixed 原根：

- R136 的 `family_0191_-2`，SHA256 `19e1c92b975c9e59df6e2e09432a5cb9c824412fface2b85b47161a7aa10e18f`；
- R131 完整权 $-2$ 原导出中对应 (1) 的六个 mixed 响应。

R160 九基局部编号、R116 全局编号、二次和第三模板号、第三原模板 SHA、原 pure SHA 与本次六个完整 mixed 列逐项同源。因此没有把一个 pure 列的系数套到另一条 mixed 响应上。

目标和六列均为同一右锚的完整原函数。原输入扫描最高 profile jet 为 4，颜色为 $q,\bar q$，共 1124 个 reachable atoms。没有代入任何具体 profile、幂尾或几何。

原代数中右原函数的颜色次数来自它内部所有 jets。筛选 (3) 不改积分边界、不把 $q$ 与 $\bar q$ 合并，也不将 ordinary complex products 改成模平方。归约使用已冻结的有色 word/IBP 规则，保留

$$
I(F)(\xi)=\int_r^\xi F(\eta)\,d\eta
$$

及全部共同右 collar 条件。左尾未删除，途中未重锚。

## 3. 实际完整输出

[公开 run43661460271](https://github.com/Rogerhu12/math-research-public/actions/runs/43661460271)，source：

~~~text
ae7e5af322c13ba8bbff6130a284272b48446568
~~~

lane 为 `J6_balanced_original_difference`，attempt 1。实际 `completion=complete`，耗时 **0.508613037 秒**，峰值 RSS **69.4140625 MiB**。

| 对象 | 原项数 | SHA256 |
|---|---:|---|
| 未投影完整 mixed 差 | 1335 | 66fbaaf034c8aebef06b08217380aac5d17b4344269b226b98ba9426a05e7c7f |
| 唯一 balanced 原差 | 502 | b9de00e7990fa22153498a8f909ee43098083435fea0610bad8a8fe09f178391 |
| sound word 代表 | 176 | 2bdbf31812a548604e6eace83a1d67db8d11e9d416414b1da6b6537d8806c07c |

余项的最高局部 jet 为 3、最高 word 长度为 2，颜色仍为 $q,\bar q$。本次统计为 493 次 primitive 调用、291 次 unique-high-jet IBP、18 次非空 word 多项式 IBP、8 次全深度 shuffle 调用和 45 次 cycle fallback。

Cycle fallback 按既有 sound 规则保留原 word，不强行判零。这里既没有证明剩余项来自某一种缺失恒等式，也没有从余项反推原函数非零。归约不完备的范围始终保留。

主结果字段准确为：

~~~text
status = undecided_one_balanced_original_remainder
completed_pure_identity_consumed = true
balanced_original_identity_proved = false
complete_two_mode_J6_equals_exact_R160_response_combination = false
complete_J6_nonmember_proved = false
kernel_or_extended_comparison_membership_searched = false
~~~

两个 `...proved=false` 表示本次没有获得该证明，不是已经证明相反结论。

## 4. 本次工作量与来源

新源码为

~~~text
scripts/literature_J6_balanced_original_difference.py
31517 B
SHA256 5994a0837aa7e9a4657de09b085b93b6b23ca0ba8fbe809b2914dec2264e1022
~~~

同 job 的八项新增人工 all_passed，耗时 0.005980184 秒、峰值 RSS 27.79296875 MiB。它们只核准确系数/编号、颜色投影、同锚 IBP、未决口径和原导出往返，不读取研究原根。

| 工作 | 本次数量 |
|---|---:|
| 新 balanced 完整原差 | 1 |
| 新 pure 目标或 pure 求解 | 0 |
| 已发表 mixed 原根解码 | 7 |
| 新 response/forcing/几何编译 | 0 |
| 旧 31 条核关系重证 | 0 |
| 旧 40 列重生成或逐列正规化 | 0 |
| profile、几何、幂尾评价 | 0 |
| 新秩、43 枢轴或 Schur 分离分支 | 0 |

实际来源和输出均由 publication receipt 保留；本次读取主报告、人工报告和 receipt。压缩大证书不通过 API 解码读取。后继可以直接读取已发表的同一原差，不必重构 (3)。

## 5. 完整可复用证书

公开目录为

~~~text
topics/visible-flex-new-mechanism/notes/actions-43661460271-1-J6_balanced_original_difference
~~~

| 文件 | bytes | SHA256 |
|---|---:|---|
| J6-balanced-original-difference.json | 66143 | 932cd382bdec6909f090dfca703698332f71cf4d1912600fcb655a0bb19cebc6 |
| receipt.json | 37457 | 255c964d54ed356b8aef61d33861519bcecb6f159d8dd6ddd52c2afa2ee2fc99 |
| J6-balanced-development.json | 51316 | a46541c93eff318c069eaa370dc9e5df65a44fedebe727adb05aa10d3546dd10 |
| J6-balanced-original-difference-certificate.json.gz | 37430 | 94ded571b17e0a54e1d6988fdf8726274f66a787bdea7b889503cbe58829c029 |
| 上一证书解压原文 | 226858 | 9f886d3f104eb031e2a4c5f936a42bfd2bcb9eff92b34050a43680efbb99fd25 |

完整证书保存 10 个原根：J6 mixed、六个旧 mixed 输入、固定有理组合、未投影 mixed 差和 balanced 差。另保完整 176 项 word 代表、固定有理系数、R160 pure 先决证明绑定及全部旧原导出来源。

本次 main 没有触发输出上限或 fallback；不存在因预算退出而缺失的目标结论。保存全部余项是为了后续消费，不意味着余项已证明独立或非零。

## 6. 对正字符的准确影响：当前没有新增零条件

R141 的权 $\sigma=-2$ 正仿射字符满足

$$
c_0=\lambda(J_6),\qquad b_1=\lambda(J_4),
$$

以及

$$
a_0\ge0,\quad a_2\ge0,\quad c_0\ge0,\quad
4a_2c_0-b_1^2\ge0.
\tag{4}
$$

如果未来完整 $J_6\in R$ 被证明，$\lambda(R)=0$ 才给 $c_0=0$，随后 (4) 才迫 $b_1=0$。**本次没有支付这个前提**，所以不能新增这两个零条件，也不能据此简化 R152 的固定 h action。

即使未来取得该完整身份，这个 R141 推论也仅针对所指定的 $\sigma=-2$ 字符；它不会自动排除整个 $U$ 的全部正字符、证明闭成本锥等于 $U$，或支付真实半群、完整 ruling 与有限等距族。

## 7. 留给后继的唯一边界

R159/R151 已有的 31 维响应 pure 核和 R157 的 34 维扩展 pure 核保持有效。若继续问 $J_6\in R$，应检查准确 pure-zero 代表相对于前者；若问它是否独立于 $R+\operatorname{span}\{N^3G,J,D_0\}$，比较对象才是后者。

本次没有进行任何一个完整空间的成员搜索，也未执行此前设计的旧枢轴隐式 Schur 原评价。因此 (3) 只留下明确且有完整原数据的未决问题，不是新的否定结果。旧 pure 阳性、既有真实维数和所有成本可达范围均保持原结论。

## 后续严格结论（2026-11-15）

[R162](../results/R162-J6-original-separation-and-35-dimensional-balanced-kernel.md) 的新原式44阶非零子式已经证明 J6 不属于包含 K6 的完整43维比较空间。因此完整候选 J6=K6 现已排除；本说明保留R161当时的176项余式仅未决这一历史事实。该否定来自后续原式评价，不来自R161的不完备NF，也不排除 J6 在完整字符分母 R−2+N U−1 中为零。
