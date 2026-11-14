# 新接受 q098 场的完整径向 jet 与 patch/mean 同场接口

作者：`/root/geometry_audit`（GPT-6 Astra Pro，AI 辅助），2026-11-13。

**已实际读取原 q098 接受场的全部物理 quintic 系数，对2211个完整径向区间、85个状态的 Y、Y_s、Y_ss 给出准确有理 Bernstein 包围；正式 exit 0。** 本结论针对原保存多项式定义的连续区间值。它不将该有限多项式等同真 PDE 解，也未证明相邻原多项式的二阶导数完全相等。

与实际数据一同保存的 contract 明确要求后续完整 Cartesian patch、同一均值测度与全局锚、profile/材料坐标桥、闭面装配和 reach 所需字段。contract 的结构合法不等于这些数学义务已经支付。尚未支付的字段没有填入样本值冒充证书。

## 1. 绑定实际接受场，保完整 H

输入是原接受 p31 主包，而非计划候选或改标签的旧证书：

| 原实际输入 | SHA256 |
| --- | --- |
| q098 physical primary | `88175797998edbbe6d7ed18065fb8786cc58cec5e255b0efb95da9d08c728699` |
| q098 raw collocation | `03f1ed050abfd3a4cbafc7a23c7c60a63aa415085c149db9b5e401320e7e4b35` |
| final actual tail response 0003 | `1e0af8ea57b700b46c78e1fb09cc5babd72c54dd7132e2cb3be377979e62ca57` |

程序要求 physical/raw 均已成功且非待审计状态，原配置为实际非线性尾。完整 x、y、p、cubic、rms raw chunks、原物理 quintic chunks 的 SHA 和形状逐项读取。M=28、物理状态数3M+1=85、原参数数M+3=31；全部2212个节点、2211个区间、每个状态的六个物理 quintic 系数都必须存在。

主包和 raw 的 gauge、冻结 profile、材料角参考系数/频率、数值材料图、物理尾参数及 cut 身份逐项相同。原 terminal nonmean state 重新计算的全部28项 H 与最后请求、checkpoint cutHeight 逐 bit 相等；最终响应已收敛且保存完整 height-J。原 port SHA、固定 source revision `869436630c99aa5a68afb55bd8877c826034d117` 和 source-origin 同时绑定。

同场 witness 保留原 fullmean interior audit 的原 input SHA，不将原 primary 的 witness 重标为 fixed-view。其有限样本峰只是后续网格见证，不作为本次区间包围的输入或证明。

## 2. 对每个原区间的精确证明

令区间为 `[s_i,s_{i+1}]`，`h=s_{i+1}-s_i>0`，原保存的某状态多项式为

\[
P(s)=\sum_{k=0}^5 c_k(s-s_i)^k.
\]

全部 c_k、s_i 都按原 binary64 的准确有理值解释。对 d=0、1、2，令 u=(s-s_i)/h。则

\[
P^{(d)}(s)=\sum_{j=0}^{5-d}a_j u^j,
\qquad a_j=c_{j+d}\frac{(j+d)!}{j!}h^j.
\]

令 N=5-d，幂基到 Bernstein 基的系数恒等式是

\[
b_i=\sum_{j=0}^{i}\frac{\binom{i}{j}}{\binom{N}{j}}a_j,
\quad 0\le i\le N.
\]

因此在整个 u∈[0,1] 上，P^(d) 位于所有准确 b_i 的最小值与最大值之间，因为 Bernstein 基函数非负且和为1。程序用 fmpq 准确完成以上式子；最后将最小值向下、最大值向上取128bit dyadic，并逐端点反解比较方向。负端点使用真正 floor/ceiling，不以绝对值舍入后恢复符号。

每个区间有85状态×3导数×2端点，共510个方向比较；2211区间总计1127610个。这个证明没有用有限节点的极值代替连续极值，也没有以 ODE 右端代替保存 quintic 的真实导数。

## 3. 输出结构与实际执行

源是 `computations/strong_newg_patch_mean_packet.py`。原运行 manifest SHA256：

`d93c66e2aa87da353c667eec9231e7b1661db8847c8d51c4a32fcc1cf0f5013b`。

实际 formal exit 0、无 signal，77.158266783秒，峰86228 KiB。未运行 Flow、RHS、Newton、Node、源积分或新几何采样。

35份径向 chunk 完整覆盖区间索引 `[0,2211)`，每份最多64个区间，压缩后均小于0.67 MB。每行包含准确物理 s 区间、原 raw t 区间、全部85状态三阶次的上下端及完整角周期请求。符号端点统一表示为 `[integer_mantissa,binary_exponent]`，区间为 `[lower,upper]`。

角坐标以原计算 ψ 的 turns 给出96个闭区间 `[j/96,(j+1)/96]`，对应212256个前缀 Cartesian patch 请求。96仅定义完整 cover 的请求分区；目前没有宣称这些角盒已有 Cartesian 区间值。完整 mean 请求始终覆盖整个原 ψ 周期，原定义为1360角均值规则、原区间 Gauss6 积分，以及唯一全局 `s=0, mean height=0` 锚，不能按区间重置。

稳定 archive manifest 将原执行中的路径、SHA 映射到仓库实际保存的文件。原执行 manifest 和全部 chunk 的字节保留，未为改路径重写数学包。

## 4. 下一层实际消费者必须满足的接口

`packet-contract.json` 为新 g 的完整同场证书规定以下原生数据，且每项带实际生产者/证明身份：

- 全径向×全角 patch 的 X、Xs、Xθ、Xss、Xsθ、Xθθ 区间及严格 rho、area、P、W、D 下界。
- 与同一全局 frame/height 锚和原均值测度关联的 m、m_s、primitive H；angular alias、Gauss6、浮点和 C2 状态修补的 A0/A1/A2 误差逐项支付。
- 全 prefix、tail、实际 closing caps/marker 的覆盖、连接、C2 seam、相位装配和单射性证明。
- 明确固定 H 区 patch 集、非空内部、所有相位逐点保持及所需直径下界。这里的固定 H 区与尾高度向量 H 是不同对象。
- 全闭面直径上界、局部曲率和实际近邻路径费、全部非局部 patch 对的连续 normal-chord margin；最后才消费 R11/R16 的 reach 充分条件。
- 同一个真实 g 的连续度规误差和后续加密序列身份，不借旧 q096、旧 source/candidate 或旧尾 H 的证书。

本包只完成第一层的全部原保存径向状态 jet 供给及其同场接口。新 profile/材料坐标的连续桥、均值、完整 Cartesian 量与闭面装配继续由实际消费者完成，不能由此包的 `finished=true` 推断本题完成。
