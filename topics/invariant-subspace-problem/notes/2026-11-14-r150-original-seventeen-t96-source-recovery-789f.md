# R150：T96 九目标正常形证书回到原十七式的完整回代接口

日期：2026-11-14。会话：Astra-ISP-789f / normal_annihilator。

**状态。** 本文的来源恒等式、反向恢复算法和次数界已证明。对应 C++ 在本地恢复环境中以 `g++ -O2 -std=c++17` 编译成功，编译界为 30 秒/512 MiB；Python runner 已通过语法解析。**尚未运行数学回代**，因为固定 T96 图运算尚未提供已完成的九目标系数。不能将接口准备写为原十七式证书已取得。

本接口承接 [固定 T96 完整图变序及投影判据](2026-11-14-r150-reweighted-graph-projection-789f.md)，使用同一原 17 式和原 6188 Macaulay 行；不补成全矩阵零条件，不删低次梯度方程，也不作特征零提升声明。

## 1. 准确对象和输入身份

在原参数 $y=v(s)=(1,s,\ldots,s^5)$ 下，原方程记为

$$
I_0(s,m),\ldots,I_{16}(s,m).
$$

其中前 11 个是原物理 $N$ 多项式的 11 个系数方程，后 6 个是原完整 $\Gamma$ 方程。令

$$
D=23366320238786911411830138211362846399922176000
$$

为已核固定公共分母，$c_i$ 为已记录的 17 个常数行 content。正常形程序使用的 primitive 方程为

$$
P_i=(D/c_i)I_i.
$$

D 和全部 c_i 模 31 都是单位。因此这一步只用常数域单位，不引入参数例外。

原 6188 行为所有 $|\mu|\le3$ 的 $m^\mu P_i$，准确编号

$$
r=17u+i+1,\qquad u=0,\ldots,363,\quad i=0,\ldots,16.
$$

u 是原 364 个 m 单项式乘子的顺序。源码以同一 base-8 指数 key 重建所有乘子，并逐一核原 3333 预基源和原 2195 正常形源的 r、i、$\mu$，不使用新的枚举替代原行编号。

原 9 个物理目标仍为

$$
t_j(s,m)=\left(\sum_{a=0}^j {j\choose a}(-s)^{j-a}m_a\right)^2,
\qquad j=2,\ldots,10.
$$

目标系数输入必须是已完成的 `R150TC31`：全部 2195 源，全部 9 目标，24 次首一 h_31，每个源的原 6188 编号、真实次数 $\delta_j$ 和完整升幂系数。runner 要求先前回执准确包含

$$
RC=h_{31}T,\qquad
\deg C_j\le146-\delta_j,
$$

以及逐系数全恒等式已通过的成功字段。前缀、只有标量投影、只算了目标正常形的记录均不接受。

## 2. 原预基补偿的精确符号

令 B 是原同 m 次数 RREF 常预基，E 是正常形非主元坐标的嵌入。原 2195 真实行与原九目标满足

$$
F=BH+ER,\qquad t=BJ+ET.
$$

这里 H、J 完全由原正常形 trace 给出；每条记录的身份是

$$
\mathrm{NF}=\mathrm{raw}-\sum a\,s^kB_b.
$$

因此

$$
h_{31}t-FC
=B(h_{31}J-HC)+E(h_{31}T-RC)
=B\beta,\qquad
\beta=h_{31}J-HC.
$$

程序对每个真实源记录加 $-a s^kC_j$ 到对应 B 系数，对每个真实目标记录加 $a s^kh_{31}$ 到对应目标槽。九个目标在同一 32-bit word 的低 9 bit 上并行，五个位平面表示 $\mathbb F_{31}$。完整 normal trace 的 25305683 次记录全部读取，输入与目标顺序全部核对。

原已证来源界是

$$
\deg H_j\le\delta_j-10,\qquad\deg J\le20.
$$

于是

$$
\deg\beta
\le\max(24+20,(\delta_j-10)+(146-\delta_j))
\le136.
$$

源码为 137 个完整参数层分配容量；任何实际越界立即失败，不截断。

## 3. 3333 常预基 DAG 的反向恢复

后向 RREF 的一条实际行运算是

$$
B_c^{\mathrm{new}}
=B_c^{\mathrm{old}}-aB_q.
$$

恢复一个系数线性组合时，按实际运算的逆序更新

$$
\beta_q\gets\beta_q-a\beta_c.
$$

完整后向文件的 1010703 个运算逐条反向恢复；同一记录的 q 均不同于 c，因而可先保存 $\beta_c$ 再传播，不能把原正向顺序直接套到系数上。

前向预基的一条定义为

$$
B_j=\alpha_j\left(F_{r_j}
-\sum_{i<j}a_{ji}B_i\right),
\quad \alpha_j\in\mathbb F_{31}^{\times}.
$$

按 $j=3333,\ldots,1$ 逆序，把 $\alpha_j\beta_j$ 加到原 r_j 行系数，再把 $-a_{ji}\alpha_j\beta_j$ 加到更早预基系数。完整前向文件的 782976 条依赖全部保留，并检查每个依赖确实指向更早的行。

这些运算只乘域常数，不提高 s 次数。合并最初原 2195 源的 C 后，得到全部 6188 primitive 原行的系数，次数至多 136。

最后乘各行固定比例 $D/c_i$，把 primitive 方程系数运输成实际原方程 I_i 的系数。该比例的逆 $c_i/D$ 用于恢复原方程多项式供最终乘法。两者在域中逐项相乘为 1，且原 D/content 字符串、残数和输入哈希都保存在回执。

## 4. 对原十七式的最终完整乘法

最终验证直接重新生成原九个物理目标 $t_j$，以及原 17 个方程 I_i 的线性/二次项。计算

$$
\sum_{r=1}^{6188} c_{rj}(s)m^{\mu(r)}I_{i(r)}(s,m)
-h_{31}(s)t_j(s,m)
$$

的全部系数。

原最高 m 次数为 5；非恒定 m 单项式共 4367 个。原 N 的参数次数至多 10，原 $\Gamma$ 至多 5，所以检验保留 s 次数 $0,\ldots,146$；目标本身次数至多 $24+20=44$。九目标同时逐系数核，不能只看目标的一个投影。

只有全余项为零，原编号全部吻合，常预基 trace 完整，行正规化比例通过，才输出

    status = full-original-seventeen-lift-complete
    fullOriginalSeventeenEquationIdentity = true
    fullOriginalMacaulayIdentity = true
    originalRowScaleTransportVerified = true.

这里的意义是原 17 式在 $\mathbb F_{31}[s,m]$ 中的完整九目标来源恒等式。即使完成，也不等于特征零同一 h_0 的恒等式。

## 5. 哈希、程序及有界执行

输入模型及正常形 DAG 锁定：

| 对象 | SHA256 |
|---|---|
| 原 model input | 291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6 |
| 原 NF matrix | eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840 |
| forward DAG | 66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e |
| backward DAG | cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f |
| complete normal trace | e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b |

程序：

- [完整回代 C++](2026-11-14-r150-original-seventeen-t96-lift-789f.cpp)；
- [有界 runner](2026-11-14-r150-original-seventeen-t96-lift-runner-789f.py)。

调用：

    python3 notes/2026-11-14-r150-original-seventeen-t96-lift-runner-789f.py
      --coefficients COMPLETE_T96_COEFFICIENTS.bin.gz
      --coefficient-receipt T96_TARGET_LIFT_RECEIPT.json
      --nf-dir REGENERATED_COMPLETE_NATIVE_NF_DIRECTORY
      --work TEMPORARY_WORK_DIRECTORY --out SMALL_RESULT_DIRECTORY
      --seconds 60 --memory-mib 512

编译单独限制 30 秒/512 MiB，选用 `-O2`；数学回代单次 60 秒/512 MiB。runner 记录实际阶段、返回码及最后一个进度，不把返回码 0 单独当成功。若失败，必须按实际停止阶段继续决定工作，不能写证书已完成。

完整二进制格式为 `R15017F1`，包含 6188 原行、九目标、h_31、原 D/content 残数、每行的真实编号/方程编号/乘子 key，以及九个升幂多项式系数。完整文件保存为 gzip。若压缩文件超过仓库 5000000 字节限制，按每片至多 4000000 字节保存完整有序 gzip 分片，并保存整体压缩/解压后 SHA256、各片偏移/大小/SHA256 和重组清单；拼接后先核整体 gzip 哈希，再解压核原二进制哈希。同一次恢复的完整系数因而可持久重组，不仅留在临时目录。不得丢掉恒等式项或更改文件限制。

## 6. 实际保存范围

旧恢复目录仍为 `math-research-public`，根在新 `math-research-recovered` 检出独占 git。本代理只写本页及上述独占 helper，不修改共享状态，不提交推送。根可把这些完整文件搬运后立即登记已证明的接口。

截止本页写入时，只有编译和语法结果，未执行原十七式数学恢复。当前完整 R150 有限复参数问题、特征零来源分母，以及主不变子空间问题均仍未闭合。

模型及回执输入兼容 CI 小结果中的 `native-normal-form-input.txt`、`native-normal-form-receipt.json` 文件名；原始 `normal-form-*` 名也接受，哈希验证完全相同。三个 `nf-*.bin` DAG 仍从恢复 artifact 按原名组合至 `--nf-dir`。
