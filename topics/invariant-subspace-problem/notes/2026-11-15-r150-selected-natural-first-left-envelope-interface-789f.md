# R150：同 I,J 的特征零自然一阶左校正小包络

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro。日期：2026-11-15。

## 1. 本次只支付一个新的有理连接上界

本入口使用同一原自然参数 $u=1/s$，原 $17$ 式、$4354$ 个选来源 $J$、$4354$ 个选输出 $I$：

$$
B(u)=B_0+uB_1+\cdots=A^h(u)_{I,J}.
$$

[完整常数秩证明](../results/R150-appendix-selected-second-transverse-rank556-constant4318-and-infinity-order50.md)已付

$$
\operatorname{rank}_{\mathbb Q}B_0
=\operatorname{rank}_{\mathbb F_{31}}\overline B_0=4318.
$$

[同原自然一阶接口](../results/R150-appendix-natural-first-connection-complete49-36-and-output-restriction4340.md)已付 $\operatorname{rank}_{\mathbb F_{31}}\overline\beta_1=3$。常数单位块在 $\mathbb Z_{(31)}$ 可逆，因此同一真有理连接已有下界 $3$。

本次目标是构造足够多的**原选输出左一阶 jet**，给特征零连接上界。它不再求巨大有理来源核，不新增 Dixon 位，不改素数，不把模 $31$ 的完整 Smith 长度直接当成特征零长度。

## 2. 完整常数左核与有限支持

令 normal 次数为 $m_0,\ldots,m_8$ 的总次数，$c=m_{10},d=m_9$。

原 $F_{i,0}$ 在纯切向平面恒为零。已付同选常数秩夹逼还给全部 normal 至少三的输出空间包含于选来源像。因此同一 $I$ 的常数左余空间都支撑在 normal 至多二。

完整 $585$ 低投影的 $29$ 维有理左核为 $L$。在原 $I$ 删去的三行求

$$
Z=\ker(L_E),\qquad \operatorname{rank}L_E=3.
$$

$LZ$ 给同选低输出的 $26$ 维左核；再加入 $I$ 内十个纯输出，得到完整、独立的

$$
\Lambda\in\mathbb Q^{4354\times36},\qquad
B_0^{\mathsf T}\Lambda=0.
$$

源码将每个常数列清分母并 primitive 化为整数；这是非零有理列缩放，不改变其空间。随后重新核验**全部 $4354$ 个原选来源**上的常数左产品。没有只检查旧 $954$ 个低来源后遗漏其它原列。

允许一次左校正 $\lambda_1$ 支撑在 $I$ 的 normal 一、二、三输出。这些坐标总数准确为

$$
(135-3)+450+990=1572.
$$

纯输出上的 $\lambda_1$ 不影响 $B_0^{\mathsf T}\lambda_1$，可以取零。又可利用已经构造的 $26$ 个低常数左核，把 $\lambda_1$ 的 $26$ 个独立 gauge 坐标设零。代码仅对 $26\times585$ 的已知核作小消元选这些坐标，并核其秩；由对应 $26\times26$ 子块可逆，任何允许的 $\lambda_1$ 都可作此归一，原像不变。

故实际新校正变量为 $1572-26=1546$ 个，加 $36$ 个初始左核系数，一共 **1582 列**。

## 3. 为什么只需乘子 normal 至多二的原行

考察

$$
B_0^{\mathsf T}\lambda_1+
B_1^{\mathsf T}\Lambda c=0.
\tag{3.1}
$$

若原来源乘子的 normal 次数至少三，则：

- $F_{i,0}$ 至少含一个 normal，乘积 normal 至少四，无法与 normal 至多三的 $\lambda_1$ 配对；
- 任意 $F_{i,1}$ 的单项式 normal 次数非负，乘积至少三，无法与 normal 至多二的 $\Lambda c$ 配对。

所以这些原行在 (3.1) **严格为零**。这里不假设 $F_{i,1}$ 的 pure 部分为零；实际该布尔值仅照实记录。

其余原 $J$ 来源取全，数量不超过完整 $17$ 式的

$$
17\left(10+54+135\right)=3383.
$$

代码逐一遍历全部 $4354$ 个原来源，构造前述整数行，并对被省略的每行再次直接核零。所用 $F_1$ 是已经核过的原 primitive $L_9/G_4$，没有把共动连接误作 natural 连接，也没有删掉 $A_0(Dh)$ 在同选余空间中的成本。

## 4. 小系统的秩如何给真连接上界

按变量顺序先列 $1546$ 个校正系数，再列 $36$ 个 $c$。设完整原整数矩阵为

$$
M=[M_0\ M_1].
$$

精确有理 RREF 允许从所有核向量中取出其 $c$ 投影；其维数准确为

$$
d=36-\bigl(\operatorname{rank}M-
                  \operatorname{rank}M_0\bigr).
\tag{4.1}
$$

实际源码对每个自由 $c$ 坐标取一个完整核向量，将所有校正和初始系数一起清分母，先保存整个整数 jet，再逐条乘回原未缩放整数行。自由 $c$ 坐标块为非零对角块，故这些 $c$ 独立；$\Lambda$ 本来是独立基，所以得到 $d$ 个独立的真实左初值。

每个满足 (3.1) 的初值在真对偶第一连接的核中。因此

$$
3\le \operatorname{rank}_{\mathbb Q}\beta_1
\le36-d.
\tag{4.2}
$$

若实际 $d=33$，即得同 $I,J$ **有理第一连接秩准确为三**。这只需要本次构造出的 $33$ 个正证书，不需要先证明所有可能的左校正都落本次支持。

若 $d<33$，仍保 (4.2) 的合法上界，但不能据此判定更大支持的校正不存在，更不能说真有理连接秩等于 $36-d$。回执始终保

`higherTransverseLeftCorrectionsRuledOut=false`。

同样，本次若闭合第一连接，也只闭合第一层的 $31$ 单位秩；更高 $u$-Smith 阶数、最终首项 $31$ 单位和原九目标特征零成员性另需继续支付。

## 5. 丢失旧临时左核后的真实接法

旧会话的 $709321$ B 有理左核已经消失，不能假称当前还在。新上层 runner 先核本次最小重建的完成回执：

- 原 wrapper 为 `bb4a217827ff7a8ac8faf9c0f1b2c5255e302c3bcc66f644cd31a8f8f50312c6`；
- 全 $51$ 个已发布前十六阶来源、Schur 和原余量系数比较为真；
- 原 lean $I,J$、自然第一步及所有文件 SHA 与该回执相同。

然后只运行一次原已提交的

`2026-11-15-r150-selected-second-transverse-projection-789f.py`，

SHA256 `d94b1f0be704c5eb7aee756a98a5d7a2097e66a331709c4e300434f78dbd7e9d`。

它从同一原 point 与同一 $I,J$ 重建已丢失的 $954\times585$ 有理常数左核，保全部旧乘回、自由坐标和秩 $556$ 完成条件。这个必要重建不做 $4318$ 消元，也不做新的 $1603$ 来源求解。完成后缓存全部实际文件的大小、SHA；若以后重入，不再重算该有理左核。

因此两层的术语分别是：外层明确记“丢失有理 $585$ 缓存需要重建”；新的主包络核心只消费已经重建并完整核验的左核，没有在其内部重复旧 $585$ RREF。

## 6. 冻结源码与 CLI

核心：

- `notes/2026-11-15-r150-selected-natural-first-left-envelope-789f.py`；
- blob `c56bf87e3bf5cd332aa77a027ed88319bb12fdf6`；
- 20823 B；
- SHA256 `4901fa8fcebbda69a9c6042cdf20f622083c8e75285b19051bba47f435dc2ac9`。

真实重建适配：

- `notes/2026-11-15-r150-selected-natural-first-left-envelope-rebuilt-runner-789f.py`；
- blob `5069dd2cfd6ee2f66be9bc1efd321a929ae33bb7`；
- 12026 B；
- SHA256 `3e7b9ea6875f52961ddfaff2615afd3481ef85bbd75b8b1d5b76cebb94ee9bf2`。

二者均对完整本地字节实际通过 AST；没有先运行数值。root 实际调度：

~~~text
python -B {scripts}/2026-11-15-r150-selected-natural-first-left-envelope-rebuilt-runner-789f.py
  --rebuild-root {work}/selected-natural-u-rebuilt
  --point-model {selected_model}
  --projected-engine {scripts}/2026-11-15-r150-selected-second-transverse-projection-789f.py
  --envelope-engine {scripts}/2026-11-15-r150-selected-natural-first-left-envelope-789f.py
  --out {work}/selected-natural-first-left-envelope
  --seconds 60 --memory-mib 1024
~~~

这里只需 python-flint 与标准库，没有 native 编译或 NumPy。旧 projection 脚本保持原字节；适配器只把已证明同 $I,J$ 的新文件实际身份交给它，并将当前自然第一绑定和当前有理投影绑定交给核心。每个最终矩阵和来源完成条件仍由核心自己完整核验。

## 7. 预算、恢复和小回执

数学共享 $60$ 秒，每进程 $1024$ MiB。重建有理 $585$ 在独立子进程中执行，至多用 $30$ 秒且不超过剩余共享时间。新的有理 RREF 也在独立子进程中运行，父进程在实际剩余时间到时终止它；不会因为不可中断的 native 调用而把请求时长冒称真实时长。

临时阶段依次为：

| 阶段 | 保存内容 | 续接行为 |
| --- | --- | --- |
| `rebuilt-rational585/` | 完整原投影、真实左核、乘回回执 | 完整缓存成立后不重建 |
| `left-envelope/same-original-natural-left-envelope-integer-input.json.gz` | 全部相关原整数行、原来源对应、严格零省略行 | 绑定相同即可复用 |
| `left-envelope/complete-left-envelope-rref.json.gz` | 完整非零 RREF 行及全部主元 | 原库返回后立即保存 |
| `left-envelope/complete-original-left-first-jets.json.gz` | 完整初始/校正整数候选 | 保存后才乘回，乘回不完可续 |

RREF 在库调用内部尚未完成时不能假称有内部 checkpoint；此时只保存真正已完成的原输入。RREF 或候选已经完整保存时，续接严格使用它们，不重走完成阶段。大数组只留当前 job 临时目录。

主小回执是

`selected-natural-first-left-envelope-rebuilt-pipeline-receipt.json`。

真实完成只有两个 outcome：

1. `same-selected-first-rank-three-proved`；
2. `restricted-left-support-upper-bound-only`。

另有 `checkpointed-time-budget` 和 `failed-or-incomplete`，均不是数学负结论。

完成回执必须同时保：

- `all4354OriginalConstantLeftProductsZero=true`；
- `all4354OriginalFirstLeftJetProductsZero=true`；
- `allSelectedOutputSupportVerified=true`；
- `allHeadProjectionFreeCoordinatesIndependent=true`；
- `completeFixedSupportEnvelopeComputed=true`；
- 实际 `leftHeadImageDimension`、上下界和 `selectedFirstConnectionRankExactly3`。

永久只保存源码、参数、run、哈希和小回执；不上传重建的有理左核、RREF 或完整左 jet。根代理继续独占 Git/main 与共享索引。
