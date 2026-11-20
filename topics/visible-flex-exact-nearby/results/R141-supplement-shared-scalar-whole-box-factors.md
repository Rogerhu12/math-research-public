# R141 补篇：同一模型的短程共同标量包围

2026-11-20，`visible-exact-astra-ac637-20261120`。

本篇只替换 R141 的 `local_factors` 包围方式。精确比较生成器、原155个 panel、真实根和长度、实际 $S$、真实 hybrid 系数、source roles、193个 atoms 和所有 Gram/投影公式保持不变。配套纯模块 `fourfold_codazzi_low_centre_shared_scalar_factors.py` 没有 import、IO 或运行入口；登记时仅作文本和 AST 检查，实际科学求值为0。尚未声称任何缺陷或逆门通过。

## 1. 要处理的具体依赖损失

原 R141 `local_factors` 对整个 $\tau$-box 向 `arb_mat.exp` 传入矩阵 $\tau H_i$ 的 entrywise ball。这个调用是有效的包含，但在指数内部会覆盖矩阵各项独立变化的更大集合。对长 panel 上的共同标量变化，这可能比真正的一参数曲线宽很多。下面只对**固定点矩阵**求 matrix exponential，先将整个 box 的共同标量展开成短程幂级数，再取有限矩阵区间包围。

该方法仍返回普通矩阵 balls，并不宣称在返回之后维持所有 entries 的相关性。它也不收紧原 parent coefficient packet；实际缺陷始终仍是 $A_L^c(r)-H_i/h_i$。

## 2. 内部相似坐标不替换实际 $S$

对原 panel $i$，声明一个精确正 dyadic 数 $b_i$，置

$$
 B_i=\operatorname{diag}(I_{96},b_iI_{97}),\qquad
 K_i=B_iH_iB_i^{-1}.
 \tag{V.1}
$$

$b_i$ 可取已完成 balanced-v3 `complete_plan` 中 binary64 `q_balance` 的**准确二进制值**。这是试探相似坐标的定义，不是将实际 reference $q_i$ 改成浮点数。实际 observation 仍用原 $S_i$，外部因子为 $S_iB_i^{-1}$；source 仍是原 raw $W(r)$，内部输入为 $B_iW(r)$。

这样可以在认证精度下重新构造精确 dyadic $b_i$ 与其有向逆，而不用把 context 在320 bits准备的 $q_i$ ball 的表示宽度放入长程 matrix exponential。原 $q_i$ 的 ball 仍完整保留在真正的 $S_iB_i^{-1}$ 中。没有改变 R141 的 source/observation 单位。

## 3. 原完整等分计划和短程矩阵

令 $n_i$ 为已经声明的完整等分数。其 cuts 必须准确等于

$$
 0,1/n_i,\ldots,n_i/n_i.
$$

模块只接受这份计划中的整个小格；若需要不同划分，必须明确声明新的计划。第 $j$ 小格内写

$$
 \tau=\frac{2j+1+t}{2n_i},\qquad -1\le t\le1,
 \qquad D_i=\frac{K_i}{2n_i}.
 \tag{V.2}
$$

这里的归一化坐标和原 $H_i$ 完全相同。真实质量仍由原 Gram adapter 按 $h_i/n_i$ 计算，不以浮点长度替代它。

## 4. 保共同标量的有限 Taylor 项与完整余项

固定一个有限整数 $p\ge1$，定义准确矩阵

$$
 C_k=D_i^k/k!,\qquad
 M_{ab}\ge |(D_i)_{ab}|,
 \qquad M_{ab}\ge0.
 \tag{V.3}
$$

实现以有向 `magnitude` 给出每个 $M_{ab}$ 的一个固定上界。$M$ 是一个非负点矩阵 majorant，不含小格参数 $t$。令

$$
 T_p(M)=e^M-\sum_{k=0}^p\frac{M^k}{k!}.
 \tag{V.4}
$$

其各 entry 非负。若 $[-1,1]C_k$ 表示共同标量 $t^k$ 的矩阵区间外包，构造

$$
 \mathbb V_i=
 \sum_{\substack{1\le k\le p\\k\text{ odd}}}[-1,1]C_k
 +\sum_{\substack{1\le k\le p\\k\text{ even}}}[0,1]C_k
 +[-T_p(M),T_p(M)].
 \tag{V.5}
$$

**命题 V1。** 对每个 $t\in[-1,1]$，都有

$$
 e^{tD_i}-I\in\mathbb V_i,
 \qquad e^{-tD_i}-I\in\mathbb V_i.
 \tag{V.6}
$$

**证明。** 对矩阵乘法的 entrywise 绝对值，有 $|D^k|\le |D|^k\le M^k$。因此余项逐 entry 满足

$$
 \left|\sum_{k=p+1}^{\infty}\frac{t^kD^k}{k!}\right|
 \le\sum_{k=p+1}^{\infty}\frac{M^k}{k!}=T_p(M).
$$

有限项使用奇次幂 $t^k\in[-1,1]$、偶次幂 $t^k\in[0,1]$。这两个区间分别包围真实共同参数的所有取值；之后放弃它们之间的相关性只会扩大包围。将 $t$ 换成 $-t$ 不改变两个幂范围，故同一个 $\mathbb V_i$ 同时适用两种符号。证毕。

实现中的 $C_k$ 用 signed matrix multiplication 递推后再乘幂区间；不先将 $D$ 换为绝对值。只有完整余项使用 $M$。式(V.4)用定向 matrix exponential 减去定向有限和；每个结果 ball 包围实际非负尾，故其 upper endpoint 给出有效的非负 cap。代码保留有限性和非负 upper 检查；不把一个未经证明的负结果任意裁成零。零尾若因向外舍入得到跨零 ball，使用其非负 upper 仍是有效包含。

此处没有 Frobenius 统一余项充满所有 entries；正矩阵尾保留 $M$ 的传播结构。默认 $p=64$ 只是确定的有限算法参数，调用方也可事先声明128等其他阶数；包含定理对任意声明的 $p\ge1$ 均成立，且不要求数值先证明某个额外小量门。`current_remainder_infinity_upper()` 返回当前 panel 的有向尾矩阵无穷范数上界；它只是 enclosure 的辅助量，不是一条已完成的 source norm。

## 5. 中点 carriers 的同一模型递推

沿用 R141 的准确 node frame

$$
 F_i=(L_i,R_i),\qquad F_i^{-1}=\binom{\ell_i}{\rho_i}.
$$

定义本 panel 第 $j$ 小格中点的 balanced matrices

$$
 X_j=e^{(2j+1)D_i}B_iF_i,
 \qquad
 Y_j=F_i^{-1}B_i^{-1}e^{-(2j+1)D_i}.
 \tag{V.7}
$$

只需对固定点矩阵 $\pm D_i$ 求有向指数，即得初值

$$
 X_0=e^{D_i}B_iF_i,\qquad
 Y_0=F_i^{-1}B_i^{-1}e^{-D_i}.
$$

同一个准确生成器满足

$$
 X_{j+1}=e^{2D_i}X_j,\qquad
 Y_{j+1}=Y_je^{-2D_i}.
 \tag{V.8}
$$

$e^{\pm2D_i}$ 由 $e^{\pm D_i}$ 平方向外包围。反复使用同一个已包围矩阵会有 interval dependency 损失，但每次乘法仍包围准确(V.8)，不会改变模型。无需每个小格重新计算一个长程 $e^{\tau H_i}$。

模块只保存当前一个 panel 的短程变化、两个 step matrices、首中点和当前中点。顺序访问只做(V.8)。若请求更早的小格，从已保存首中点重新递推；它不留下每个 box 的历史缓存。

## 6. 完整 signed 因子的包围

对 whole box 上的原 source $W(r)$，准确因子满足

$$
 (O_L,O_R)
   =S_iB_i^{-1}e^{tD_i}X_j,
 \qquad
 \binom{I_L}{I_R}
   =Y_je^{-tD_i}B_iW(r).
 \tag{V.9}
$$

由命题 V1，下面的矩阵区间都是包含：

$$
 \mathbb O=S_iB_i^{-1}(X_j+\mathbb V_iX_j),
$$
$$
 \mathbb I=Y_j(B_i\mathbb W)
             +Y_j\mathbb V_i(B_i\mathbb W).
 \tag{V.10}
$$

其中 $\mathbb W$ 是原 `source_matrix(..., box, role)` 给出的完整 whole-box enclosure。特别地，零阶项 $Y_j(B_i\mathbb W)$ 先按真实 signed source matrix 相乘，短程变化才另行加入。$\mathbb O$ 前97列和后96列分别给 $O_L,O_R$；$\mathbb I$ 前97行和后96行给 $I_L,I_R$。没有删除 mean、source 方向或任何中间模式。

如果 $W$ 随 $r$ 变化，式(V.10)仍对每个真实 $r$ 成立；将 $t$ 与 $W(r)$ 的依赖放宽为同一 whole box 的独立包含只使外包更大。没有断言将任意乘子范数换成 RMS。

## 7. 与 R141 原 Gram 的明确连接

addon 提供三个显式入口：

* `SharedScalarFactorProvider(api, km, core, model, step_counts, balances, order=64)`；
* `panel_gram_packet(provider, panel, cuts, source_role)`；
* `whole_box_projection_bound(provider, panel, box, defect_packets, defect_source_covariances, body_output_norm, epsilon)`。

后两个 wrappers 逐式保留 R141 原函数中的 Gram、质量、两个同 panel 三角、点接收器、点源列和实际投影公式，只将局部因子求值改成显式 `provider.local_factors`。没有 monkeypatch 被 pin 的 core。返回 packets 仍携带同一个 model token，并交回原 `complete_gram_norm`、`source_covariances` 和 `actual_low_source_bound`。193 atoms 的 carriers 和两个端点的观测完全由原 core 处理，未在本 addon 中替换。

## 8. 静态成本与实际范围

对一个 panel，准备工作为三个 $193\times193$ 的点 matrix exponentials（$D_i,-D_i,M$）、两组共 $2p$ 次 factorial-power matrix multiplications、两个 step squares 和两个首中点乘积。默认 $p=64$。每个后续小格用两个中点递推乘积；完整 factors 使用一个 output variation 乘积和三个 source 乘积，另有便宜的对角缩放。实际 $W$ 的列数可能小于193。

因此不再为每个 box 调两次 whole-interval matrix exponential；按155个 panel、1424个声明小格计，指数调用数的静态比较是 $3\cdot155$ 与 $2\cdot1424$。这只是调用结构，不是6小时以内的运行承诺。Gram、真正的高精度 inverse 和原模型的 directed chart 构造仍有其成本。

缓存只保留一个 panel；它不会随累计请求的 source panels 或 boxes 二次增长。为另一条 source role 重用同一模型时，若访问顺序重新开始，私有因子可重新物化，但不得把已经完成的 norm 目标登记成新目标重算。

本改动不解决原155个 panel内部 carriers 可能存在的条件数问题，也不保证 axis-aligned factor balls 的最终 Gram 足够紧。特别地，分别包围 $O^TO$ 与 $II^T$ 后取 trace，会放松两 covariance 共同 carrier 基变换的关联；单 panel 较长时，即使 Taylor 尾很小，放大仍可能呈指数规模。提高 $p$ 不能证明这一风险已消失。它不收紧320-bit context 中真实系数的数学包络，也不使原 whole-parent 缺陷自动变小。如果这些仍阻止严格门，必须改进同一系数 adapter 或明确细分同一比较模型；不能把成功的 floating endpoint 节点指标改称 directed 全区间证据。

