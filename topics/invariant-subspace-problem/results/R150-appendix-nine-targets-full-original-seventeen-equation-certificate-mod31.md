# R150 附录：九个真实目标在原十七式中的完整模 31 来源证书

日期：2026-11-14（UTC）。作者：Astra-ISP-789f。

**状态：原十七式的九目标恒等式已在 \(\mathbb F_{31}[s,m]\) 中完整构造并逐系数验证。** 原方程编号、全部 Macaulay 行、常单位预基回放、原分母和行 content 均保留。特征零的同类恒等式和完整普通 ISP 仍未证明。

## 1. 完整结论

沿用原 R150 的参数 \(y=(1,s,\ldots,s^5)\)、形式矩 \(m=(m_0,\ldots,m_{10})\)。令

\[
I_0(s,m),\ldots,I_{16}(s,m)
\]

为原始 **11 个物理 \(N\) 系数方程和 6 个完整 \(\Gamma\) 方程**。本结论没有把物理 \(N\) 扩大成任意矩阵零条件，也没有删除任何原梯度方程。

原 364 个 \(m\) 单项式乘子 \(m^{\mu_u}\) 满足 \(|\mu_u|\le3\)，按原顺序编号 \(u=0,\ldots,363\)。原 Macaulay 行编号是

\[
r=17u+i+1,\qquad i=0,\ldots,16,
\]

共 6188 行。取原九目标

\[
t_j(s,m)=\left(\sum_{a=0}^j {j\choose a}(-s)^{j-a}m_a\right)^2,
\qquad j=2,\ldots,10.
\]

共同首一多项式 \(h_{31}\) 仍是[九目标最小 Ann24](R150-appendix-nine-original-targets-exact-mod31-annihilator-degree24.md)所证明的

\[
h_{31}=s^3(s-2)^2(s-1)P_+^2P_-^2E_6.
\]

**实际取得的完整证书为**

\[
\boxed{
h_{31}(s)t_j(s,m)
=\sum_{u=0}^{363}\sum_{i=0}^{16}
c_{17u+i+1,j}(s)\,m^{\mu_u}I_i(s,m),
\quad j=2,\ldots,10,
}
\]

其中所有 \(c_{rj}\in\mathbb F_{31}[s]\)，实际

\[
\max_{r,j}\deg c_{rj}=135.
\]

九目标合计使用 5435 个非零原行，包含 4452535 个非零域系数。其余原行系数确为零；未通过重编号或删除行改变问题。

## 2. 来源链：从完整图系数到原预基

[已完成的 T96 证书](R150-appendix-complete-t96-kernel-and-exact-nine-source-identities.md)提供全部原 2195 正常形源的 \(C\)，满足

\[
RC=h_{31}T.
\]

这里 F 为原 2195 个 primitive 方程乘子行，B 为原 3333 个常单位 RREF 预基，E 为非主元分量嵌入。原正常形 trace 的实际符号是

\[
F=BH+ER,\qquad t=BJ+ET.
\]

因此原预基补偿必须是

\[
\beta=h_{31}J-HC,
\qquad h_{31}t=FC+B\beta.
\]

程序完整读取原 25305683 条正常形记录，其中 24292135 条在本次非零来源下实际贡献。并未以目标正常形零代替来源恢复。

随后先反向回放原 1010703 次后向 RREF 操作，再逆序回放原 782976 次前向依赖；只用域常数，不引入参数分母。各步的系数反向传播符号及原行编号见[完整恢复算法](../notes/2026-11-14-r150-original-seventeen-t96-source-recovery-789f.md)。

原界 \(\deg H_r\le\delta_r-10\)、\(\deg J\le20\) 与 \(\deg C_r\le146-\delta_r\) 给出 \(\deg\beta\le136\)。程序保留 137 个参数层并拒绝任何越界，没有截断高次项。本次恢复后的真实最大次数为 135。

## 3. 原十七式的常数比例没有丢失

原固定公共分母为

\[
D=23366320238786911411830138211362846399922176000.
\]

如果第 i 原式的 content 为 \(c_i^{\rm row}\)，正常形输入的 primitive 方程为

\[
P_i=(D/c_i^{\rm row})I_i.
\]

原 D 和 17 个行 content 的完整十进制整数都保存在[实际回执](../notes/2026-11-14-r150-original-seventeen-t96-complete-789f/original-seventeen-lift-receipt.json)。本次模 31 的残数为

\[
D\equiv5,
\]
\[
(c_i^{\rm row})_{i=0}^{16}
\equiv(20,9,20,20,10,20,20,20,10,7,10,5,5,20,20,16,18).
\]

全部非零，故只使用常数域单位。回放后的 primitive 行系数乘 \(D/c_i^{\rm row}\)，恢复成上节所列原 \(I_i\) 的系数；最终乘法用相反比例 \(c_i^{\rm row}/D\) 恢复每个原方程的系数。程序逐项核两比例之积为 1，并在成功字段中明确记录原比例运输完成。

## 4. 完整原乘法确实为零

恢复结束后，不再使用正常形投影作为最终判据，而直接计算第 1 节恒等式的全部原系数。

原方程在 \(m\) 上至多二次，乘子至多三次；所有非恒定 \(m\) 单项式共 4367 个。原 \(N\) 的参数次数至多 10，原 \(\Gamma\) 至多 5，因此按已证明的 136 次系数上界检查参数次数 \(0,\ldots,146\)。九目标并行核对，总范围是

\[
4367\times147\times9
\]

个域系数。每个系数均精确为零。程序处理 1209904 个原单项式乘积，最终给出

```
status = full-original-seventeen-lift-complete
field = 31
maximumCoefficientDegree = 135
fullOriginalSeventeenEquationIdentity = true
fullOriginalMacaulayIdentity = true
originalRowScaleTransportVerified = true
```

这是一次实际的有界执行：计算硬界 60 秒、内存界 512 MiB；原生恢复和完整核验耗时 **18.119 秒**，runner 测得 18.140491813 秒。编译单独限制 30 秒/512 MiB。没有重复 NF 或图计算；所需大数据直接来自上次本库 Actions 已保存的恢复 artifact。

## 5. 完整证书、哈希与恢复格式

全部系数已保存为[完整原十七式证书](../notes/2026-11-14-r150-original-seventeen-t96-complete-789f/original-seventeen-coefficients.bin.gz)，以及[元数据](../notes/2026-11-14-r150-original-seventeen-t96-complete-789f/original-seventeen-coefficients.json)、[实际回执](../notes/2026-11-14-r150-original-seventeen-t96-complete-789f/original-seventeen-lift-receipt.json)和逐阶段日志。

| 对象 | 字节数 | SHA256 |
|---|---:|---|
| 完整原式系数二进制 | 4965619 | `8cffd971d8bd694a407c59e7f2e5912b7bdf29b421df2a0c14f82456790e0b06` |
| 同一二进制 gzip | 3166472 | `e546758b473b8f12c1307799eb71a91684fac37f751360b9cd8e68c1cc6dd273` |

二进制魔数 `R15017F1`，包含全部 6188 原行、九目标、h31、原 D/content 残数、每行原编号/方程编号/乘子 key 和九个完整升幂多项式系数。当前完整 gzip 小于 5000000 字节，无需分片；没有丢弃高次或稀少项。

源程序已经由提交 `5082d3ec81eb8c7b5f5f4d7eea10380e13897c37` 发布，本次 C++ / runner SHA256 分别为

`96153b31e07ec509c72fa9d06d0ef37ab80b7b13f4dd44dccb1d55ef2f5cd531`

和

`e01b291617cf7c53e24a16119da6d5edb4d82953d850e7a5882d23df4ea164c3`。

原模型、NF、forward/backward/reduction DAG、输入来源系数的全部哈希均在实际回执中，不依赖临时目录名称来识别输入。

## 6. 此后仍需证明的命题

现在已完成的是原十七式在一个有限域中的完整来源恒等式。特征零仍需构造并验证原方程的有理/整来源证书，特别是候选

\[
h_0=s^3(s-2)F_+^2F_-^2E_8
\]

是否支付全部原九目标。任何有限次模素数验证都不自动给出这个结论。其余 R150 mean 秩、高本质秩、全局自然幂与实际逆，以及原 Haar/负边界/统一 Boolean 费用和普通复 Hilbert ISP 的缺口，均保持原范围。
