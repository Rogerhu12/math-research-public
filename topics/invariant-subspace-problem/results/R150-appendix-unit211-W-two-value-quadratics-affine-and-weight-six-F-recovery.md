# R150：两条原值二次的同 S 一次关系与权六次例外外的 F 唯一恢复

会话 Astra-ISP-8542378f-20261127。日期2026-11-27 UTC。当前原一般 LS、Delta=0、W=0 的既有已付域。两个新的原恒等输入均已实际返回；所有新首项零面均保留，尚未排空 W。

## 1. 原 r2 与完整 NV 二次必须在同一个 S 处成立

沿用[完整 NV 直接 T 二次](R150-appendix-unit211-W-entire-NV-direct-T-quadratic-and-complete-leading.md)的 N2，以及原 q4 对 q3 的完整二次余式 r2。若 beta2=[T²]q3，则

$$
r_2=q_4-(T-\beta_2)q_3.
$$

源码坐标 S=T-2lambda 中 beta2=[S²]q3-6lambda，完整三四次消去身份实际核回。

写

$$
r_2=a_2S^2+a_1S+a_0,\qquad N_2=b_2S^2+b_1S+b_0.
$$

新的全图原组合为

$$
L=b_2r_2-a_2N_2
=(b_2a_1-a_2b_1)S+(b_2a_0-a_2b_0).
$$

本次实际逐项核回 L+a2N2=b2r2，未倒置 a2 或 b2。尤其 H411=0、a2=0 及二者同时为零的整个纤维均保留；原 q3、r2、N2 也仍全部保留，未用 L 取代两条原二次而丢失信息。

对 L 清除已付分母、只剥已付公共内容后，得到

$$
L_1(e,k,\lambda)S+L_0(e,k,\lambda)=0.
$$

| 系数 | 次数(e,k,lambda) | 项数 | 完整编码字节 | SHA256 |
|---|---:|---:|---:|---|
| L0 | (19,22,9) | 3429 | 85067 | 6317e0107a4a9a392979a2749abff04bd805ee7c5f62cc7d615934dfb99f1ae7 |
| L1 | (18,22,8) | 2922 | 71711 | 36e4c5a04d5749483f6872dcf83804c24445279f537f4ec2723e13ce57546e8c |

每个原系数都实际乘回清理前的表达式。L1 经全部既有单位剥除后仍为同一非恒定多项式，没有被支付。整个 L1=0 面保留 L0=0 和原两二次。本次没有构造全 W 的 S 唯一恢复。

## 2. 三条真实 F 系数上的权矩阵

采用[四行三列原耦合](R150-appendix-unit211-W-coupled-original-Gram-value-four-by-three-complete-minors.md)中的原三行 R_i=A_i(S)+B_i(S)F，依次对应 E1、EBe、N1。它们来自真实原式，只清除已付分母和内容。

本次实际核实所有三个 B_i 都精确为

$$
B_i(S)=c_i+\alpha_i\lambda+\beta_iS,
$$

其中 ci、alphai、betai 只依赖权 e,k，且分母均已付。将这九个系数组成

$$
\mathcal B=
\begin{pmatrix}
c_0&\alpha_0&\beta_0\\
c_1&\alpha_1&\beta_1\\
c_2&\alpha_2&\beta_2
\end{pmatrix}.
$$

取最后两列的三维叉积 omega。真实的全部三列乘回给

$$
\omega^{\mathsf T}\mathcal B=(\Delta_B,0,0),
\qquad
\sum_i\omega_iB_i(S)=\Delta_B(e,k).
$$

没有依据抽样秩作结论。完整权行列式非零，且所有有理因子、重数实际相乘返回如下准确表达式：

$$
\begin{aligned}
\Delta_B={}&\frac12\,e\,k^3(k+2)(2e+1)(ek-2)
(ek-1)^2 P^2 V^5(k+4)^6 M_{13}G_{36},\\
P={}&2ek-k^2-5k-8,\qquad V=(e+1)k+2.
\end{aligned}
$$

M13 与原权身份 M=-u²M13/(kV²) 保持上一页定义。除 G36 外，所列全部因子均已在当前 W 支支付。

G36 是本次完整因式分解中36项的实际整数因子，次数(e,k)=(6,8)，总次数12；规范系数编码591字节，SHA256

4285ef8a1f8bd40aa3e0adf6b245842c1ec7419ab7fa8f19a17b72cfbc5cf5b3。

其完整36个系数在小回执中保留；该规范因子是固定源对 DeltaB 的完整分解所定义的，不是另取一条同次数曲线。e 六次系数准确为 32k^6，且 k 已付。故整个 G36=0 可以置于

$$
\mathbb Q[k,k^{-1}][e]/(G_{36}/(32k^6))
$$

这一首一六次环境中处理。此环境自由六维，不代表在其上进一步局部化物理权单位后仍自由；全部其它单位、真逆和其范数零纤维仍须分别保留。

## 3. 准确的 F 恢复补图与完整例外

仅在明确补图 G36 非零时，DeltaB 才是已付单位。第二节的原恒等式直接给

$$
F=-\frac{\sum_i\omega_iA_i(S)}{\Delta_B}.
$$

右侧对 S 至多二次，所有分母来自已付权单位及本补图明确的 G36。其完整原来源为

$$
\sum_i\omega_iR_i=
\Delta_B\left(F+\frac{\sum_i\omega_iA_i(S)}{\Delta_B}\right).
$$

这是由已经实际返回的三列恒等式直接推出的精确恢复，不需要 A143、任何 Bi 的几何逆或物理 D 的逆。

因此在这个补图，可以将全部原方程继续放到原首一 q3 的三列环境中；必须同时代回 qF 和每条完整原行，不能只保新恢复公式。本文没有实际展开该补图上的全部新三列 N/P。

G36=0 的整个权曲线仍开，不把它删除或声称已付。原先 F 消去定理中所有 Bi 同时为零的情形也不因当前补图而丢失。当前三个主要未付面为 H411=0、L1=0、G36=0；它们均有明确原式保留，而没有被一次分式操作隐藏。

## 4. 唯一真实执行

源码：

[2026-11-27-unit211-W-two-original-value-quadratics-affine-and-F-weight-Cramer-8542.py](../notes/2026-11-27-unit211-W-two-original-value-quadratics-affine-and-F-weight-Cramer-8542.py)

SHA256 47f12807255484c3d3dbebdb4e2a44d1b464ee78d7bffe2ecce4150c7d9b3e6e；5949字节；blob333c216cc8caf0f798128fe27f9fda592ff99b5e。固定1be650dd原构造前缀及其依赖，截在旧首项分解之前。没有重跑旧N4、旧首项因子分解或旧参数cofactor门。

实际run46037841703、job140637686750，inner exit0：

- 两条新的完整原身份、系数回乘和权行列式完整因子分解：2.276889439秒；
- 驱动墙钟2.314822503秒；
- RSS71760KiB；
- stdout7328字节，SHA256 f4523687a7fe0ceeb736de5e50b66219245841c8becb25d579f016852aa5518b；
- 限额180秒、4GiB。

真实pull于2026-11-27 16:57:13.169189 UTC完成，从04b40bc5bf2bcb5a08c3024955892fa9f8a6eee3更新至bf4ac54ca4e811a20c027a8ddb0ec3ad5b085ace；两个README blob均未变。此处准确记录真实pull的不同前后提交。源冻结提交仍为04b40bc5...，实际source blob和SHA保持上述固定身份。
