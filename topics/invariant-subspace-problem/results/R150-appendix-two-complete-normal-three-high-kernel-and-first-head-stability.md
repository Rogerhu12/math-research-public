# R150 补篇：$s=2$ 完整正常三次高核恰二维，全部三次校正不扩大一阶首项

日期：2026-11-15。作者：Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 完整高块及真实特征零上界

固定原 $s=2$ 系数及全部次数至多三的来源乘子。正常三次目标有
$$
165\cdot6=990
$$
个坐标，包括所有切向次数零、一、二的部分。正常二次来源共有 $2295$ 行；其常数作用记为
$$
H_3\in\mathbb Q^{2295\times990}.
$$
另 $2805$ 个正常三次来源在这个目标扇区上的作用恰为原 $F_0$ 的纯切向项。由于 $g(2)=0$，这些行准确全零。因此 $H_3$ 的核就是保留全部 $5100$ 个高来源行后的完整正常三次高核。

[纯三次及切向耦合构造](R150-appendix-two-pure-cubic-high-kernel-uniqueness-and-unchanged-first-heads.md)已给出两条真实有理核列
$$
\nu_{\rm cub}=w^{\otimes3},\qquad \nu_{\rm tan}.
$$
后一条取值为
$$
\nu_{\rm tan}(n_i n_j n_k)
=v_iw_jw_k+w_iv_jw_k+w_iw_jv_k,
$$
$$
\nu_{\rm tan}(cn_i n_j n_k)=a w_iw_jw_k,\quad
\nu_{\rm tan}(dn_i n_j n_k)=b w_iw_jw_k.
$$
本次又将这两列乘回全部 $5100$ 个原高来源行，$10200$ 个有理坐标均为零；实际取出的纯/切向两行的 $2\times2$ 行列式非零。这直接给出特征零上界
$$
\operatorname{rank}_{\mathbb Q}H_3\le988.
\tag{1.1}
$$
这里使用的是真有理来源，不是把某个有限域核提升为有理核。

## 2. 单个固定素数的严格下界

逐行从原十七式生成全部 $H_3$ 系数，并在每行内先通分，再除去非零整数内容。每一步都逐系数核验为非零有理行缩放，故得到的整数矩阵 $\widetilde H_3$ 与 $H_3$ 有相同的有理秩。

仅对预先固定的素数 $11$ 作一次有限域秩计算，实际结果为
$$
\operatorname{rank}_{\mathbb F_{11}}\overline{\widetilde H_3}=988.
\tag{2.1}
$$
有限域非零子式是原整数子式的非零约化，所以
$$
988\le\operatorname{rank}_{\mathbb Q}\widetilde H_3
=\operatorname{rank}_{\mathbb Q}H_3.
$$
结合 (1.1)，得到
$$
\boxed{\operatorname{rank}_{\mathbb Q}H_3=988,\qquad
\ker_{\mathbb Q}H_3=\operatorname{span}_{\mathbb Q}
\{\nu_{\rm cub},\nu_{\rm tan}\}.}
\tag{2.2}
$$

本次行内容缩放仅用于证明一个常数矩阵的有理秩下界；没有将它解释为原参数族在 $\mathbb Z_{(11)}$ 上的单位运输，也没有从它推断任何完整参数连接的有限域秩。

## 3. 对一阶左 jet 的完整正常三次结论

设
$$
A_0^{\mathsf T}\lambda_1+A_1^{\mathsf T}\lambda_0=0,
\qquad A_0^{\mathsf T}\lambda_0=0,
$$
且允许 $\lambda_1$ 的全部正常次数至多三的目标坐标。完整常数左核的 $\lambda_0$ 只有正常次数至多一。因而 $A_1^{\mathsf T}\lambda_0$ 在正常次数二、三的来源行上为零，即使保留原非零纯一阶项 $g'(2)t\,d^2$ 也一样。

在这些高来源行上，$\lambda_1$ 的低正常部分同样没有贡献。因此其三次部分必须属于 (2.2) 的准确二维空间。于是全部此类一阶 jet 都归约到已经[实际完成的两列联合低行系统](R150-appendix-two-tangent-coupled-cubic-correction-and-unchanged-fifteen-heads.md)：
$$
[B,C,C_{\rm cub},C_{\rm tan}]\in\mathbb Q^{1088\times609},
$$
其秩 $592$、完整核维数 $17$、首项像维数 $15$ 均已逐原式核验。

由此本篇得到的是完整的正常次数三范围结论：
$$
\boxed{\text{允许全部正常三次校正后，真实一阶首项仍恰为旧十五维空间。}}
\tag{3.1}
$$
而且其三次部分必为零。证明是：每个这样的首项已有旧的低支撑一阶代表；两代表之差属于完整常数左核，后者没有三次部分。

九个原目标 $t_j=n_j^2$ 的一阶读数仍全部为零。正常次数四、五的校正尚未由 (2.2) 覆盖，所以这里仍不称完整第一连接的秩恰为七，也不证明原 $h_0$ 目标的局部成员性。

## 4. 实际记录

实际运行：run $43736746064$，步骤 `two-complete-cubic-high-field-rank`，执行来源 `3fca6ece7dc1f778bffeb0b79f7af3a1016822ae`。数学时间 $1.604522462$ 秒，其中有限域 RREF 为 $0.249778605$ 秒；退出码零。

- [完整实际回执](../notes/r150-local-projection-session-789f/43736746064-two-complete-cubic-high-field-rank.json)。
- 源码 `notes/2026-11-15-r150-two-complete-cubic-high-field-rank-789f.py`，SHA256：`5185c04088c17950fe2f0c401ef7f95b07d2d0af02c25d463d499fcc7afa4e08`。
- 原始数学回执 $3840$ 字节，SHA256：`789f932ef1669ba6fe721f5d7db940bf66059227375df0f8ef6f10b535420a02`。
- 完整原稀疏矩阵、行缩放和坐标字典的临时输入 payload SHA256：`5e9047c5c1e8684fcb56dffd43cc7a9eac399fe1889a8d964b171a94316ab5ea`。
- 实际有限域主元列逻辑 SHA256：`ae122f39fcc855605a2e9a55f55c35f152157316fd1977b261af2a47652a7d74`。
- 两条真实有理核列的逻辑 SHA256 为 `e1dd76784833bdd14ce91fc72d740633038a6578e0b17df4036297cde966251e`、`fc25498e8fb70c05e79c0efcff7b91f44ab432d2dd11d60f90a6190edb482ce9`。

全体来源行都保留，没有作 $990$ 列的有理 RREF，没有重做旧单位或旧右端；可重算大数组仅为临时任务数据。
