# R931 基础 helper 的精确接口和实现证明

日期：2026-11-20。状态：代码已作 AST 检查，root/deep 全文独立核验真实原 API、数学与完整返回；没有本地数学执行，也没有公开运行回执。本说明不把 helper 写成原四交除子、Miller 配对或 shadow 的实际 PASS。

文件：original_ys_artinian_norm_tools.py。

## 1. 原对象及入口

入口是

    tools = OriginalArtinianNormTools(
        engine, affine_context, original_basis_identity, original_omega,
        progress=progress)

engine 必须是同进程的 OriginalAffineIdealEngine。它的 chart 保留同一 certified fast operation summary；该 summary 的原乘法 signature 必须等于 affine_context 的全乘法回执。原有两图表均可用，但一个 tools 只消费它自己的 chart 和该 engine 实对象产生的理想。

原常数域严格是调用者的 k=F_(r²)，r=29 或 41；omega 必须已经属于这个实际 k。构造器核 omega²+omega+1=0、omega≠1，不能在 helper 中另取根。原完整 306 元基、全部权数、权和 864、46971 个完整原乘积、曲线层 3468、属 559、原 M2 基身份均核回。基础理想、矩阵、分式都不得从另一个同构模型直接导入。

original_basis_identity 沿原 bridge 的三个键：

- original_curve = X0(3468)；
- original_complete_normalization_signature；
- original_Y_M2_basis。

其中哈希只是来源标识；以下运算的相等均由完整原对象、完整 HNF 或完整回代验证，绝不以哈希代替等式。

## 2. 方法契约

每个公开运算返回 (value, receipt)。

| 方法 | value | 完整接受门 |
|---|---|---|
| ideal_sum(I,J) | 原完整理想 I+J | 全 HNF 变换及两个包含 |
| effective_quotient(I,C) | I:C，要求 I⊂C | 完整饱和核、真正商的整性、全乘回 (I:C)C=I |
| split_support(I,J) | 字典含 bad、good、两 CRT 幂等元 | 全厚 Fitting 稳定、和为 A、乘积为 I、全长度相加 |
| fraction_graph(N,D) | 同一原函数的全 paired 图核和真实 pole ideal | 原 Dn=Nd 全身份、完整饱和核、整个分母投影 |
| recover_fraction(I,(N,D),graph=None) | A/I 中的原分式整值 | 同图核组合分母模 I 为 1、全局交叉式及全厚回代 |
| inverse_unit(I,h) | A/I 中的逆元 | 完整 R 模求解及乘积模整个 I 为 1 |
| norm_unit(I,h) | 原 k 中的范数 | 全 π 因式、每一完整层的诱导算子、所有层厚度、原 k resultant |

这里 I(D) 始终表示完整厚除子的消失理想。split_support 的 bad 是 J 在剩余点处全部为零的整个局部分量；good 是互补的整个局部分量。bad_idempotent 在 bad 为 1、good 为 0，good_idempotent 相反。二者是在父商 A/I 内返回的完整多项式向量。

分式用同 chart 的原 306 坐标向量对 (N,D)，D≠0。可显式保留 fraction_graph 的返回上下文以复用；recover_fraction 会要求 graph 的 tools 实对象、完整 N、完整 D 全部相同。没有自动无限图核缓存。

I=A 的空商单独处理：分式值及逆返回零向量，空除子的范数为原 k 的 1。

## 3. 有效理想商及准确早停

写 R=k[ξ]，I=I(D)，C=I(C_div)。先以全部 HNF 行核 I⊂C，所以 C_div≤D；在已认证的原 Dedekind 环 A 中，真正 J*=I:C 是整理想，且

    Norm_R(J*) = Norm_R(I)/Norm_R(C).

这两个 monic 多项式的整除在代码中实际核回。初始候选 J_0=A。对 C 的第 j 个完整 R 基行 c_j，代码以完整饱和核

    (J_(j−1)·M_(c_j)) stacked with (−H_I)

取得全部 (u,v) 满足 u J_(j−1) M_(c_j)=v H_I。第一投影乘 J_(j−1) 恰给

    J_j = {x∈J_(j−1): c_j x∈I}.

这是一个 A 理想；每一步均有 J*⊂J_j。故 Norm_R(J_j) 整除真正商的 norm。一旦两 monic norm 相等，有限商 J_j/J* 的长度为零，因此 J_j=J*，可以停止；没有假定两个生成元已足，也没有默认执行全部 306 个独立核。

最后仍实际构造 J_j C，并要求其完整规范 HNF 等于 H_I。这是整商的全返回门。只比较范数、只验某些行或清分母后的分式域核都不合格。

## 4. 全厚 Fitting 分离及图核回收

从 K_0=I+J 开始，每步取 K_next=I+K²。整个 K² 由原 engine 的已证明完整理想乘法取得；每步加回 I，所以指数虽倍增，当前商长度始终不超过 dim_k(A/I)。实际完整 HNF 相等才接受稳定。在每个局部分量上，J 的像为单位理想或幂零理想；稳定的幂等理想只能是整个局部环或零。因此稳定 K 准确是 I(D_bad)，而 I:K 是完整 I(D_good)。

代码另核 K+(I:K)=A、K(I:K)=I 和全部长度。若要求幂等元，则用完整多项式 HNF 变换求 x+y=1，x∈K、y∈I:K。x 是 good 幂等元，y 是 bad 幂等元；全商中的和为 1、乘积为 0 实际核回，因而两份幂等身份全部成立。没有只保约化支集。

对原 f=N/D，全饱和图核

    {(n,d)∈A² : Dn=Nd}

的分母投影恰是 {d∈A:fd∈A}=I(Pole f)。若它与 I 生成 A，则完整 HNF 变换给同一组多项式系数 β_j，使 b=Σβ_j d_j≡1 mod I。相同系数给 a=Σβ_j n_j，并有完整全局身份 aD=bN。因此 f mod I=a mod I，保任意共同零及全部厚度。代码还回代原交叉式；单独求 D x=N mod I 没有被当作唯一值。

## 5. 每个 π 层的完整范数

令 monic(det H_I)=∏π^e。完整因式实际乘回原多项式。对每个 π，从 H_0=A 开始迭代

    H_(j+1)=I+π H_j=I+π^(j+1)A.

取完整包含坐标 C_j，使 H_(j+1)=C_j H_j，并核 πH_j⊂H_(j+1)。乘原整代表 h 在 H_j 的完整坐标算子记为 M_j；所有原多项式坐标回代。于是

    V_j = H_j/H_(j+1)
        = k_π^306 / rowspan(C_j mod π).

代码对这个全关系行空间取确定商基，令投影为 P、商代表为 S，实际核 SP=1、C_jP=0，以及全部 306 行的 M_jP=P B_j。因而 B_j 是完整诱导算子，不是任意主子式。每一层另核

    det H_(j+1) = det H_j · π^(dim V_j).

完整 H_j=H_(j+1) 才停；有限 π 主模的 Nakayama 引理证明该主分量已耗尽。末端实际核 det H_j=π^e、Σ_j dim V_j=e。全局实际核

    Σ_(π,j) deg(π) dim_(k_π)(V_j) = deg det H_I.

ActualFiniteFieldQuotient 仅构造指定 k_π=k[ξ]/π 的本机表示，带原 k 的正反映射；并逐 π 核原 omega 回传。每层范数使用

    Res_ξ(π, lift(det B_j)) ∈ k，

π 首一，所以这是准确的相对范数。代码还沿原 k 嵌入核其等于 (det B_j)^((#k_π−1)/(#k−1))。从不调用可能默认降到 F_r 的 absolute norm。

所有层 det B_j 非零与全长度门合起来，也证明 h 在整个厚商上是单位。不同整代表之差属于 I；I·H_j⊂I⊂H_(j+1)，所以全部层算子及最终范数与整代表选择无关。

官方 API 依据：

- Sage 多项式矩阵完整核/HNF：https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_polynomial_dense.html
- 指定多项式商的 field_extension 正反映射：https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_quotient_ring.html
- 多项式 resultant：https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_element.html

## 6. 当前范围与成本

本 helper 尚不构造四原 E，不自行识别 ramified/common/O 部分，也不构造原椭圆点和 Miller 链。那些部分须按 R931 用这里的完整基础操作另接；最终 Artin、18×9、双轴及乘 6 的 Tate 规范仍由原消费器保持。

所有理想/图核均在 306 秩 R 模中，图核输入 612 行、306 列；Fitting 每次当前长度≤原 I 长度，实际中间平方理想长度≤其两倍。全图核的两个投影及原 N/D 算子只随返回上下文保留，不自动无限缓存。范数只保一个 π 的当前两份 HNF、完整算子及≤306 维 k_π 商矩阵；k_π 的次数及原多项式次数仍可很大。没有将“矩阵阶≤306”写成固定小 RAM、短耗时或已实测加速。

实际运行仍必须在公开 Actions，完成回执之前只有代码/证明准备状态。
