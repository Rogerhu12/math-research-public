# 首次新输入：整 ell-half 在已付 z 非零图的三仿射均值与十个原兼容式

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（Asia/Taipei）。
- 状态：未执行；不预报新 gcd、纯权覆盖或整支排空。
- 建议源名：2026-11-28-unit211-Phi-zero-corrected-ell-half-z-blowup-original-affine-compatibility-8542.py。
- Git blob：f77b3eb1163c1606c4eddc4e7f4e8a8c3d920b2d。
- SHA256：965aa4db96787a17f8f1772929d80adf7e6e9a7ef91eb4643b89e9a63e150b32。
- 源 15438 字节；唯一首次 120 秒、1 GiB，外层可为 135 秒。

## 1. 新目标与原范围

当前正确 $\Phi=0$、distinct-singleton、物理 $D\ne0$ 图已付 $z=Qt\ne0$。在整个

$$
\ell=\frac12,\qquad Q=4(u-1)(u-2)
$$

上，令

$$
\epsilon=\lambda-\frac12,\qquad
\tau=T+\frac12,\qquad r=\tau/z.
\tag{1}
$$

这是已付 $z$ 开图的真实双向坐标，逆为 $\tau=rz$。没有支付新的仿射头、$r$、$\epsilon$、$\tau$ 或 $D$。

此前唯一实际直接原门已给 $C_{20}(u)z\in I_6$，$C_{20}$ 二十次、QQ 不可约且重数一。本次**不重放**其 $20\times18$ 矩阵、Bareiss 目标、六个最终乘子、旧 C20 分母或 C114 模块，也不读取它们的系数载荷。

新固定目标是：从 (1) 的三条原仿射均值及 N1、NS、PS 构造十个 $(u,r)$ 必要多项式，再仅对这一组新多项式在 $\mathbb Q(u)[r]$ 求一次完整 Bézout 目标。若真返回常数，清回所有实际纯 $u$ 分母并回到六个完整原式，得到

$$
C_{\rm new}(u)z^N\in I_6.
\tag{2}
$$

若未返常数，只保新的 $(u,r)$ 必要关系及全部旧 C20 原纤维，不换序、增限或续同一门。

## 2. 唯一依赖与必要定义边界

唯一依赖：

- 2026-11-28-unit211-Phi-zero-corrected-ell-half-direct-raw-degree-three-z-certificate-8542.py。
- Git blob 6ee987687964a48e1d4ffec6abf1230018de5263。
- 完整 SHA256 32e949c11469da6350c0403e2aead13d3558fce80f64b78021e3f1f65d87b15e。

runner 将该既有小源码放在新源同目录同 basename。先核完整 SHA，然后只取从首个 ctx 定义到 monomials 定义之前的 **6013 字节原六式定义**，并另核其 SHA256：

$$
\texttt{17df64c95494142eaae3d137442d464bdc87d7f0d881ca41d0910d50b6abdba9}.
$$

这一段包含正确的完整 Gram、true dual 乘法、六个未约化原多项式及其归一；不包含任何旧矩阵构造、旧 gcd、旧目标或旧覆盖参数。它没有资源、timer、文件或 import 动作，旧 say 在新命名空间静音。新源从最初到最后只有一个 real-time 120 秒预算。

原系数只沿已付

$$
u(u-1)(u-2)(1-Q)(2u-1)
       \bigl(2(u-1)^2-3\bigr)
\tag{3}
$$

局部化。各因子的完整原来源沿[已刊 C20 原证明](../results/R150-appendix-unit211-Phi-zero-corrected-entire-ell-half-direct-original-z-and-20-weight-cover.md) §1，不恢复错误 compact 均值链。

## 3. 必须逐式核的 z 除法

原六式记为

$$
(F_1,\ldots,F_6)=(E_1,E_{B,e},E_{B,o},N_1,NS,PS).
$$

记 $D_i(u)F_i$ 为其原分子，其中每个 $D_i$ 只有 (3) 的已付支持。先作整个多项式替换 $\tau=rz$。

前三式除以 $z$ 不能只从“没有常数与 $\epsilon$ 项、次数二”猜测。源另外核前三式原 $\epsilon$ 次数至多一，并实际返回

$$
D_iF_i(u,\epsilon,rz,z)=zL_i(u,r,\epsilon,z)
\qquad(1\le i\le3)
\tag{4}
$$

的多项式精确整除及全式乘回。每个

$$
L_i=a_i(u,r)\epsilon+b_i(u,r)z+c_i(u,r)
\tag{5}
$$

都逐项重组检查。

N1 不经过这一步 z 除法。它的 $\epsilon^2$ 系数明确要求非零，保整个二次多项式。NS、PS 保各自完整三次，不以零边界值或三生成元余式替代。令

$$
J=(L_1,L_2,L_3,\ D_4F_4,\ D_5F_5,\ D_6F_6)
\tag{6}
$$

于吹胀坐标中。这里后三式也已经作 $\tau=rz$。由 (4)，$J$ 中的每个原组合都属于只反演旧权与 $z$ 的原 $I_6$；后面会把所有 $z$ 逆真正清成正幂。

## 4. 固定三仿射兼容式，头零全保

设 $H$ 的三行为 $(c_i,a_i,b_i)$。取其第一列的三个余子式 $\gamma_i$，直接有

$$
\sum_{i=1}^3\gamma_iL_i=\det H.
\tag{7}
$$

源返回完整原多项式身份。它不倒 $\det H$，也不从 $(1,\epsilon,z)$ 三坐标假设自由代数。

对固定三个无序对 $(1,2),(1,3),(2,3)$，定义

$$
\begin{aligned}
\Delta_{ij}&=a_ib_j-a_jb_i,\\
E_{ij}&=b_ic_j-b_jc_i,\\
Z_{ij}&=a_jc_i-a_ic_j.
\end{aligned}
$$

源逐对返回

$$
\Delta_{ij}\epsilon-E_{ij}=b_jL_i-b_iL_j,\qquad
\Delta_{ij}z-Z_{ij}=-a_jL_i+a_iL_j.
\tag{8}
$$

$\Delta_{ij}$ 从未被反演。所有仿射系数矩阵秩一或秩零的原纤维都在这些整式身份内保留。

## 5. N1 与整个 NS、PS 的九个头零兼容式

依次取 (6) 的 N1、NS、PS 原分子 $P$，分别使用固定次数 $d=2,3,3$。写

$$
P=\sum_{a+b\le d}p_{ab}(u,r)\epsilon^az^b.
$$

对每个固定对 $(i,j)$，取

$$
R_{P,ij}
=\sum_{a+b\le d}p_{ab}E_{ij}^aZ_{ij}^b
                    \Delta_{ij}^{d-a-b}.
\tag{9}
$$

这是固定齐次代入所得的 $(u,r)$ 多项式，在 $\Delta_{ij}=0$ 仍有定义。实际来源不是在开图代入后猜测延拓。令

$$
\begin{aligned}
U&=\sum p_{ab}\Delta^{d-a-b}(\Delta z)^b
       \sum_{k=0}^{a-1}(\Delta\epsilon)^{a-1-k}E^k,\\
V&=\sum p_{ab}\Delta^{d-a-b}E^a
       \sum_{k=0}^{b-1}(\Delta z)^{b-1-k}Z^k,
\end{aligned}
$$

空和取零，则整式

$$
R_{P,ij}
=\Delta^dP-U(\Delta\epsilon-E)-V(\Delta z-Z)
\tag{10}
$$

配 (8) 给出完整六个 $J$ 来源的原组合。源每一条都在完整 $(u,r,\epsilon,z)$ 多项式环乘回。

仅当所有六个**实际乘子**有共同多项式因子时，才同步精确约除这六个乘子及右侧，并再次完整返回。这个取消不把共同因子支付为单位，其零集由取消后的整多项式身份继续覆盖。

最终固定十条输入次序为：三仿射式的 (7)；三个 N1 式；三个 NS 式；三个 PS 式。没有增加或改选来源。

## 6. 新 r Bézout 目标与所有纯 u 极点

每个 (7)、(9) 都在 $\mathbb Q[u,r]$。在 $\mathbb Q(u)[r]$ 上只按上述固定次序做逐条完整扩展 Euclid。每步短除法完整乘回；每次合并后返回该 gcd 对全部十个原必要多项式的 Bézout 组合。

只有 gcd 实际为常数，才取十个实际 Bézout 多项式的纯 $u$ 分母 LCM。乘回后得到

$$
C_0(u)=\sum_{j=1}^{10}B_j(u,r)R_j(u,r)
      =\sum_{i=1}^6 A_i(u,r,\epsilon,z)J_i.
\tag{11}
$$

每个等号都全多项式返回。所有中间 Euclid 主元的零点不被省去：只有最终原组合中真正未约消的纯 $u$ 支持进入覆盖；它们不被称为物理单位。

把 $r=\tau/z$ 代回。对前三个 $J_i$ 还要计入 (4) 的额外一个 $z^{-1}$。选

$$
N=\max\left(0,\ 
 \max_{i,\,u^ar^b\epsilon^cz^d\text{ 出现在 }A_i}
 [\,b-d+\mathbf1_{i\le3}\,]\right).
\tag{12}
$$

于是所有代回乘子乘 $z^N$ 后均为普通多项式。乘回原 $D_i$ 并合并成六个完整原乘子，再只取消右侧 $C_0$ 与这六个最终乘子的真实公共纯 $u$ 因子，实际核

$$
C_1(u)z^N=\sum_{i=1}^6\Omega_iF_i.
\tag{13}
$$

核对在清原已付 $D_i$ 的共同分母后的整个多项式环中进行。最后只从 $C_1$ 剥 (3) 的已付支持，得到 (2)。所有未知纯 $u$ 零纤维仍在 $C_{\rm new}=0$；没有反演新几何量。

如果新 gcd 非常数，准确输出其次数并保整 $(u,r)$ 必要曲线、全部 C20 原支；没有继续更大矩阵或更高次目标。

## 7. 与已刊 C20 的严格比较，或新的紧凑参数入口

只有完成 (2) 的 checkpoint 后，才对新 $C_{\rm new}$ 作它首次完整 QQ 因式分解。先全因子乘回，再把各因子取首一归一、记录规范 profile。

已刊首一 C20 的规范 SHA256 是

$$
\texttt{01e360b988892d68755864adae1520933535e6c79faf79bb667f1eec33eeb3cb}.
$$

这里两次 profile 坐标均为四元指数，纯 $u$ 多项式的后三个指数均零，因此归一后的参数表示一致。本次不读取或再生旧 C20 系数。

若新完整 QQ 因子中没有这个二十次不可约因子，已刊 $C_{20}(u)=0$ 与新 $C_{\rm new}(u)=0$ 无共同复根，因此可关闭整个当前 ell-half 物理支。此推论使用 C20 的真实 QQ 不可约性；不是模因式猜测或只按次数判断一个未经分解的大因子。

若这个因子确实出现，只把本次新原支持中 SHA 一致的因子视为 C20 的紧凑定义入口。整 $\mathbb Q[u]/C_{20}$、所有复嵌入与全部原值纤维仍保留；本源不在同一预算里追加另一个常数域矩阵门。

因式未返回时，已完成的 (2) 可以准确登记，不能宣布与 C20 的相交已经解决。任何失败保唯一真实回执；不提高资源、不重排或重跑旧门。
