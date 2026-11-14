# R55：两材料真实核与低近端二次导数界

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

**已证明。** 本文给出有限 2×2 Fourier 系数的完整界、同一连续 strip 上两种真实径向材料的独立 Green 上界及同 g 的胞元常数重标定理。末节单独记录已支付的实际强输入局部边；未把该局部账本宣称为完整强 641 行存在证明。

本文证明两个可直接用于 R50 联合比较的收紧，不改变真实度规、辅助中心、完整 mean、连续 strip 或 R18 深图。源码是 [tail_high_two_material_kernel.py](../computations/tail_high_two_material_kernel.py)。第 6 节记录已正式完成的最小实际材料核；该包只覆盖指定方向和频窗，不声称强输入联合门已通过。

## 1. 为什么必须区分材料

R33 §16 的二次主部写为

$$
Q(u)=\mathscr P_\perp\left[
E d_1(\partial_\theta u_2-u_1/B)^2+
\epsilon_\lambda d_\lambda
\left\{(u_2+\partial_\theta u_1/B)^2+
w^2\left(2u_2\partial_\theta u_1/B+
(\partial_\theta u_1/B)^2-(u_1/B)^2\right)\right\}\right],
$$

其中 $d_1=V^2/(rw)$、$d_\lambda=|\lambda|V^2/w$、$\lambda=w_r/w$，$E=1+w^2$。完整源仍为 $f=Q+R$；R33 已证明的完整 $216$ 余项界全部保留。

实际强输入的第一次 641 行浮点提案未给出正权，后续分量定位指出 low cell 13 与 near cell 12 的两向反馈。高侧旧最大窗是 94–96；低侧主要来自辅助中心修正的 `corr` 核。这个记录只定位比较界，既不是严格不可能性结论，也不是原方程无解的证据。对应数据为 [强分量定位](../notes/2026-11-12-closure-strong-split-components-r1.json)。

原来的统一系数 $3$ 同时乘两材料之和。下面证明跨低近端接口的 $d_\lambda$ 系数很小，但 $d_1$ 项不能一起乘上这个改进。

## 2. 保留两个物理分量的有限系数矩阵

取中心频率 $j$、变化频率 $b$、输出 $m=j+b$，写 $a=|j|$、$c=|b|$、$D=(1+a)(1+c)$。中心、变化的两个分量分别使用已经先取径向 supremum 的强质量

$$
\eta_{j,k}=(1+a)\sup_r e^{\tau(r)a}|L_{k,j}(r)|,
\qquad
x_{b,l}=(1+c)\sup_r e^{\tau(r)c}|v_{l,b}(r)|.
$$

令

$$
\omega_{mjb}=\sup_r e^{\tau(r)(|m|-a-c)}\le1.
$$

由 R33.92 的精确导数式，两个非负系数矩阵可以取为

$$
M_1(j,b)=\frac{2E\omega_{mjb}}{D}
\begin{pmatrix}B^{-2}&c/B\\a/B&ac\end{pmatrix},
\tag{55.1}
$$

$$
M_\lambda(j,b)=\frac{2\omega_{mjb}}{D}
\begin{pmatrix}(Eac+w^2)/B^2&Ea/B\\Ec/B&1\end{pmatrix}.
\tag{55.2}
$$

行分别是中心分量，列分别是变化分量。对每个 $j,b$，源质量由

$$
\sum_{k,l}\bigl[d_1(M_1)_{kl}+d_\lambda(M_\lambda)_{kl}\bigr]
\eta_{j,k}x_{b,l}
$$

支配。证明只需把 $A_j=(-1/B,ij)$、$C_j=(ij/B,1)$、$S_j=(ij/B,0)$、$T_j=(1/B,0)$ 代入 R33.92，再取各个系数的绝对值。例如 $d_\lambda$ 的 $(1,1)$ 系数是 $2|Ej b+w^2|/B^2$，其模至多 $2(Eac+w^2)/B^2$。两个混合分量的 $w^2$ 项与原 $C_jC_b$ 合并成 $E$，没有遗漏，也没有用截断代替完整二次主部。

这里的双线性强范数常数是矩阵**最大单项**的上界，不是把四项再相加：

$$
\sum_{k,l}M_{kl}\eta_kx_l
\le(\max_{k,l}M_{kl})\left(\sum_k\eta_k\right)
\left(\sum_lx_l\right).
$$

随后按 $j+b=m$ 求和，非负卷积质量之和不超过两输入质量之积。所有共轭 signed 频率均在和中，既不省去复半幅，也不额外乘频数。每项质量的定义已经先取径向 supremum；不存在把点态和换成强范数的问题。

### 2.1. 低输入到近端输出

假设 $B\ge120$、$0<w\le1/2$，中心与输入都支持 $2\le|j|,|b|\le92$，输出 $94\le|m|\le184$。两个输入必须同号，$a+c\ge94$，于是

$$
D=(1+a)(1+c)\ge3\cdot93=279.
$$

又 $Ea/B,Ec/B\le(5/4)(92/120)<1$，

$$
\frac{Eac+w^2}{B^2}
\le\frac{(5/4)92^2+1/4}{120^2}<1.
$$

所以 (55.2) 每项都不超过 $2/279$。(55.1) 每项不超过 $2E$。若 $\|L\|_{\mathcal X}\le1$，则低输入产生的近端二次中心源由

$$
\boxed{\bigl(2E d_1+(2/279)d_\lambda\bigr)\,\|v_{\mathrm L}\|_{\mathcal X}}
\tag{55.3}
$$

与相应固定谱卷积质量支配。源码在每个真实面板分别使用 $2(1+w_{\max}^2)$，没有把 $E$ 统一放大到 $5/4$。

输出 $|m|\ge186$ 时低输入的整个 $DQ(L)v_{\mathrm L}$ 为零；这是 R50 的带宽支持结论。它不删除 $Q(v)$、完整 $R$、far graph 或其它高输入列。

### 2.2. 近端输入到低输出

保持 $B\ge120$、$w\le1/2$。此时 $a\in[2,92]$、$c\in[94,184]$、$|m|\le92$，故中心与输入异号，$D\ge3\cdot95=285$。(55.2) 的 $(2,2)$ 项至多 $2/285$；其它三项分别受

$$
\frac{2E}{B(1+c)},\qquad
\frac{2E}{B(1+a)},\qquad
\frac{2E}{B^2}+\frac{2w^2}{285B^2}
$$

控制，均小于 $2/285$。特别地，第二个粗界为 $1/144<2/285$。因此 $d_\lambda$ 的导数系数可用 $2/285$，$d_1$ 仍需自己的 (55.1) 界。还有真实角权因子 $\omega=e^{-2\tau a}$ 可继续保留，但本文源码尚未使用这项额外改进。

**不能将 $2/285$ 乘到原先合并的 `corr` 核上。** `corr` 同时积分 $\varepsilon(r)d_1$ 和 $\varepsilon(r)d_\lambda$；只有单独的材料核或严证的径向比例才能支付这种替换。

## 3. 保存面板给出的两个实际材料积分

固定一个已保存的真实面板 $J$，取其严格正值域 $V_\pm$、$a_\pm$，其中 $a=V/w$。令

$$
R_J=\int_J\frac{dr}{r},\qquad
T_J=\int_J|d\log w|,\qquad
T_{-,J}=\int_J(-d\log w)_+.
$$

既有连续 strip 面板包分别保存 `radial_log_increment`、`log_w_variation`、`log_w_down_variation`，故

$$
\int_J d_1\,dr\le V_+a_+R_{J,+},\qquad
\int_J d_\lambda\,dr\le V_+a_+T_{J,+}.
\tag{55.4}
$$

这些是同一个真实 $r,w,V$ 的正积分界，没有重算源、ODE 或新的径向数值积分。使用真实半径增量也没有把源角当作 Cartesian 角。

令 $\chi=(d_1+d_\lambda)/(kV)$。既有 `material_cV_over_w` 恰为 $\int_Jk\chi$，从而提供 $J_-\le\int_J\chi\le J_+$。对频窗 $m_-\le|m|\le m_+$ 取

$$
q=(1-m_-/B)_+,\quad
G=e^{qT_{-,J,+}},\quad
P=e^{qT_{-,J,+}-m_-J_-},
$$

$$
C_J=\frac{k_+V_+}{m_-}(1-e^{-m_-J_+}).
$$

R33 的同一对数范数与有序变分公式给两材料的源发射上界

$$
E_1=G\min(V_+a_+R_{J,+},C_J),\qquad
E_\lambda=G\min(V_+a_+T_{J,+},C_J).
\tag{55.5}
$$

**证明。** 每个材料都不超过 $d=kV\chi$，故原来的有序阻尼积分给 $GC_J$。另一方面舍去负阻尼，仅保留整个面板的正增长，得到 $G\int_Jd_i$。二者都是同一准确响应的上界，取较小者有效。对于面板中的任意中间端点，完整面板的正增量、正材料积分、$1-e^{-mJ_+}$ 都不减，因此同一上界也覆盖整个面板。证毕。

若入口的加权物理 $\ell^1$ 值域为 $Y$，分别更新

$$
Y_{\mathrm{end}}\le PY+E_i,\qquad
\sup_J\frac{e^{\tau|m|}|Y(r)|_1}{V(r)}
\le\frac{GY+E_i}{V_-}.
\tag{55.6}
$$

两个物理分量分别先取径向 supremum 仍保留原来的安全因子 $2$。因此一个输出胞元的强核上界是 $2(1+m_+)$ 乘 (55.6) 的所有面板最大值。

低到近端的第三套状态直接用混合源 (55.3)。其发射为

$$
G\min\left(2E_+V_+a_+R_{J,+}
 +(2/279)V_+a_+T_{J,+},\;2E_+C_J\right).
\tag{55.7}
$$

该第三态保留两材料在相同面板中的位置，通常比先取两个全胞元最大核再相加更紧。三套状态均在源胞元零入口启动；其外侧胞元只有齐次传播，跨接口乘 $\max(1,B_{\rm next}/B_{\rm old})$，同时严格核对旧连续 strip 向外不增。

## 4. 同一 strip 的实际强输入重标

同 R42/R51 已准备的强包，明确选择 $\tau_s(r)=\tau_q(r)$，且 $V_{s,n}=\sigma_nV_{q,n}$。物理齐次传播不变，两个材料均在源胞元乘 $\sigma_n^2$，输出强范数除以 $\sigma_k$，所以

$$
\Gamma^{(i),s}_{kn}
\le\frac{\sigma_n^2}{\sigma_k}\Gamma^{(i),q}_{kn},
\qquad i=1,\lambda,\text{T3}.
\tag{55.8}
$$

源码从两份精确 dyadic `canonical_total_envelope` 之比建立 $\sigma_n$，并逐项核对 $B$、真实材料参数及全部端点角宽。它还要求目标 density 的 `continuous_strip_origin` 明确指向原 q density 的路径与 SHA；仅有端点相等不算整个连续函数相同。

这给新的材料核，但不自动替换原 641 行。替换时必须保留 low/near/rest/infinite 各自的支持量词，重新计算原行包含和加权导数门；不能仅凭一条两循环减小声称整个正矩阵收缩。

## 5. 准备好的最小实际命令

下面只读已保存的 cell 12/13 面板，不重建其它十个胞元。它使用 192-bit Arb、逐面板流式读取和 100 MiB RSS 上限。这是第 6 节的原执行命令；重算时须另给 fresh 输出名。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python computations/tail_high_two_material_kernel.py \
  --material-summary notes/2026-11-12-tail-r33-plateau2-continuous-strip-panels-assembled-recovered-r1-summary.json \
  --q-density notes/2026-11-12-tail-r33-plateau2-density-window.json.gz \
  --same-tau-density notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz \
  --source-cell 13 --target-first 12 --band 94:96 \
  --rss-limit-mib 100 \
  --out notes/2026-11-12-tail-strong-two-material-high-13to12-r1.json
```

下一步若需完整近端块，应依次保留原五个窗 94:96、98:104、106:112、114:128、130:192。最后一窗仍只用作实际 130–184 输出的比较上界，186–192 不成为近端未知。外部的真实候选插值、径向缺陷和连接 Green 账本仍独立待付。

## 6. 最小真实材料核已完成

执行 session `26265` 正式退出码为 0。总耗时 10.364 秒，峰 RSS 36,328 KiB；cell 13 的 1,975 个面板和 cell 12 的 1,873 个面板全部覆盖，没有新增源函数评估、ODE、基本矩阵积分或径向数值积分。

结果 [强两材料高侧 13→12](../notes/2026-11-12-tail-strong-two-material-high-13to12-r1.json) 的 SHA256 为 `ece2c8e70f29ae2f65fde0dd70c98c5c34c0179f8ef021ff03b4a2ea27dc5814`。在实际强 same-q-strip 归一中，94–96 窗得到

$$
\Gamma_{12,13}^{(1)}<0.001156927438393592,
\qquad
\Gamma_{12,13}^{(\lambda)}<29.74769938614251,
$$

而直接积 (55.7) 的结果为

$$
\boxed{\Gamma_{12,13}^{\mathrm{low}\to\mathrm{near}}
<0.215559016401676.}
$$

这些显示数字都向外取宽，完整端点保存在 JSON。混合核本身已经包含 $DQ$ 的系数 $2E$ 和 $2/279$，接入联合矩阵时**不再乘 $3$**。其辅助低场输入半径仍为完整强范数，不能把该数字复制给未核算的其它窗或其它源胞元。

原强比较对应的同一高侧最大窗为 94–96，统一中心源系数导致约 $3\times29.88$ 的上界。这里约 416 倍的改进来自真实材料分离与有限卷积支持；没有同范数换权，也没有降低原方程的验收门。反向 low 13←near 12、其余频窗与全部原 641 行仍需各自核算。


## 7. 同一源胞元的完整近端比较窗已经补齐

第二次串行执行 session `42692` 正式退出 0；16.796 秒、峰 RSS 36,596 KiB。结果为 [另外四个近端比较窗](../notes/2026-11-12-tail-strong-two-material-high-13to12-near-rest-r1.json)，SHA256 `17bff82e7ed70c6e40f193746c1bab04e79c892405b880b40bd21c6b50a4e597`。它使用第 6 节完全相同的源、材料、归一、精度和程序，只改变频窗；每窗完整读取相同的 3,848 个真实面板。

以下每项均为已经包含 $DQ$ 系数的强输入 source 13→target 12 混合列上界，显示值向外取宽：

| 实际比较窗 | $2E d_1+(2/279)d_\lambda$ 的完整列上界 |
|---|---:|
| 94–96 | 0.215559016401676 |
| 98–104 | 0.166240293088551 |
| 106–112 | 0.090820952021908 |
| 114–128 | 0.052640237159041 |
| 130–192 | 0.020307498787352 |

最后一个窗只包围实际近端输出 130–184，186–192 没有成为新的近端未知。源谱质量先按真实不相交输出频率分配，再用五窗最大核控制其和。因此这整条有限近端边已严格支付：

$$
\boxed{\left\|\mathscr P_{94\le|m|\le184}
G_{12,13}DQ(L_{13})v_{\mathrm L,13}\right\|_{\mathcal X_{12}}
<0.215559016401676\,\|v_{\mathrm L,13}\|_{\mathcal X_{13}}.}
\tag{55.9}
$$

这里 $L_{13}$ 为已付 R39 强辅助低场，采用明确选择的 same-q-strip 物理强范数；其全部 46 个非均值方向保留。结论允许使用其完整单位范数盒，不要求把辅助低场精确化为模式 2。反向低边、其它源胞元和整个强 641 行仍必须重新支付。

第二次原命令与第 5 节相同，只把频窗参数改为
`--band 98:104 --band 106:112 --band 114:128 --band 130:192`
并使用新输出 `notes/2026-11-12-tail-strong-two-material-high-13to12-near-rest-r1.json`。复算须再另给 fresh 输出名。
