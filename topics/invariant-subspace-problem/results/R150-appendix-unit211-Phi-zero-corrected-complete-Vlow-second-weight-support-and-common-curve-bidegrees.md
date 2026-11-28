# 正确 Phi：完整 Vlow 的第二非零纯权支持与公共曲线双次数界

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：唯一首次实际完成；得到新的非零纯权必要条件，尚未排除公共权曲线。** 完整原 $Vlow$ 与既有全图六次式给一个固定 14 阶结式
$$
G(u,Q)\in I_6+(Vlow),\qquad
G\ne0,\qquad \deg G\le730.
\tag{1}
$$
它包括全部原最高系数为零的纤维。与既有固定 12 阶非零支持 $F(u,Q)\in I_6$ 比较，本次实际支付
$$
\deg_uF=402,\quad \deg_QF=222,\quad
642\le\deg_uG\le643,\quad \deg_QG=371.
\tag{2}
$$
设 $H=\gcd_{\mathbb Q[u,Q]}(F,G)$，同一次完整切片返回还严格给出
$$
\boxed{\deg_uH\le41,\qquad \deg_QH\le68.}
\tag{3}
$$
(3) 只是特征零公共因子的保守上界；没有识别任何模因子为 QQ 因子，也没有证明 $H$ 为常数。整权零集还可能含不在 $H=0$ 上的孤立交点，不能把这些点漏掉。

## 1. 全原来源与固定 14 阶定义

在当前正确 $\Phi=0$、distinct singleton、物理 $D\ne0$ 规范的已付权环中，沿用[全图六原乘子](R150-appendix-unit211-Phi-zero-corrected-whole-t-sextic-six-original-multipliers-and-H28.md)及[完整 Vlow 的两原八次式](R150-appendix-unit211-Phi-zero-corrected-t-complete-Vlow-original-mean-trace-and-two-octics.md)。其中
$$
C_6(t)\in I_6,\qquad C_{8,N}(t)\in I_6+(Vlow)
\tag{4}
$$
是完整原来源身份。它们在 $\mathbb Q[u,Q,t]$ 中的实际次数为：

| 原多项式 | $u$ 次数 | $Q$ 次数 | $t$ 次数 | 总次数 |
|---|---:|---:|---:|---:|
| $C_6$ | 36 | 23 | 6 | 44 |
| $C_{8,N}$ | 60 | 36 | 8 | 71 |

本次只再生这些唯一参数的必要定义并核对既有 SHA，不重复旧原迹、两 cofactor、六最终乘子或头因式证明。把两个参数分别乘以非零有理常数
$$
2^{30}=1073741824,\qquad
2^{47}=140737488355328
$$
得到原整数多项式 $\widehat C_6,\widehat C_8$；没有除任何权因子。

令 $S_{14}$ 的行依次为
$$
\widehat C_6,t\widehat C_6,\ldots,t^7\widehat C_6,\qquad
\widehat C_8,t\widehat C_8,\ldots,t^5\widehat C_8,
$$
列依次为 $1,t,\ldots,t^{13}$，并定义
$$
G=\det S_{14}.
\tag{5}
$$
普遍伴随身份
$$
e_0^{\,t}\operatorname{adj}(S_{14})S_{14}=G e_0^{\,t}
\tag{6}
$$
给出 $G$ 是这些原多项式行的组合，再由 (4) 返回 $I_6+(Vlow)$。无需展开大的 QQ 二元行列式或伴随矩阵；(6) 是固定原矩阵的多项式身份。

尤其 (6) 不倒任何 $t$ 首项，故同时包含 $C_6$ 或 $C_{8,N}$ 降次、两头同时为零等全部权纤维。本文没有将 scalar 分母较小误作新的全原表示；(4) 的完整来源在此前已付。

## 2. 全局总次数与两个固定坐标次数

对 $S_{14}$ 的前八行赋权 $44+r$、后六行赋权 $71+r$，列 $t^j$ 赋权 $-j$。110 个实际非零原条目全部满足该总次数上界。因此每个行列式项的权之和为
$$
8\cdot44+6\cdot71-48=730,
$$
证明 (1) 的总次数界。全局非零性由下节的严格最高系数见证支付。

用于比较的 $F$ 是[既有非零纯权支持](R150-appendix-unit211-Phi-zero-corrected-nonzero-weight-support-and-whole-dimension-one.md)中的同一固定 12 阶 $\lambda$ 结式，只改非零有理常数整数尺度，继续有 $\deg F\le444$。本次没有重复它的旧单点非零门。

对任一变量 $x\in\{u,Q\}$，从每个原矩阵条目的真实 QQ 次数 $d_{ij}$ 取得整数对偶
$$
d_{ij}\le a_i+b_j,\qquad B=\sum_i a_i+\sum_j b_j.
$$
完整匹配与所有边不等式均返回，所以 $B$ 是原 QQ 行列式的次数上界。令
$$
H_{ij}(y)=[x^{a_i+b_j}]S_{ij}(x,y),
$$
其中 $y$ 是另一个权坐标，则普遍有
$$
[x^B]\det S=\det H(y).
\tag{7}
$$
这些 Laurent 权尺度只用于证明次数，不作为物理单位反演。

唯一素数为事前固定的 $1009$，两个事前固定切片为 $Q=2$ 和 $u=2$。完整最高矩阵返回如下：

| 支持 | 当前变量 | QQ 上界 $B$ | 固定模最高矩阵秩 | 固定模最高行列式 | 保全局、切片及模次数 |
|---|---|---:|---:|---:|---|
| $F$ | $u$ | 402 | 12 | 564 | 是 |
| $G$ | $u$ | 643 | 13 | 0 | 否 |
| $F$ | $Q$ | 222 | 12 | 992 | 是 |
| $G$ | $Q$ | 371 | 14 | 592 | 是 |

四个最高矩阵的全部行变换身份共 680 个坐标返回。非零的三个最高行列式通过 (7) 同时支付 QQ 真次数、固定有理切片保度和模 1009 保度。

$G$ 的 $u$ 方向最高矩阵奇异，因此只保 $\deg_uG\le643$。完整模行列式的实际 $u$ 次数 642 给下界 642，但不把它说成全 QQ 精确次数。$Q$ 方向的非零最高见证则给 $\deg_QG=371$，特别证明 $G\ne0$。

## 3. 两条完整切片的实际共同 gcd

源码在这两个固定切片上计算完整 $\mathbb F_{1009}[x]$ 固定行列式，Bareiss 的每一步多项式精确除法均乘回。临时主元仅用于精确算法，不成为原权单位。实际结果为：

| 固定切片 | $\deg\overline F$ | $\deg\overline G$ | $\deg\gcd(\overline F,\overline G)$ |
|---|---:|---:|---:|
| $Q=2$，变量 $u$ | 402 | 642 | 41 |
| $u=2$，变量 $Q$ | 222 | 371 | 68 |

两次完整 Bézout 恒等式均返回。第一条 gcd 的 profile 为 42 个非零项、SHA
78de5139abb1c11d3c503f80f376c3b5457bdc99d1d5a3cf369571c505a8cd52；
第二条为 3 个非零项、SHA
63a175cbb4ebf53179e30818700b10f95b46bf070c47f02eeb3fe1f0341af495。

两条 gcd 都非常数，因此预定的“模 gcd 为一且保度”公共曲线排除条件都没有满足。没有删除任何看似来自已付权单位的模因子；没有换素数、换切片或事后补点。也不从第二个 gcd 只有三项猜测其特征零因子来源。

## 4. 严格特征零公共因子上界

虽然两条 gcd 不为一，保度见证仍能严格支付 (3)。

先取
$$
R_u=\mathbb Z_{(1009)}[Q]_{(1009,Q-2)}.
$$
这是整闭的局部环，分式域为 $\mathbb Q(Q)$。$F$ 的全局 $u^{402}$ 系数在其剩余域中的值为 $564\ne0$，所以它在 $R_u$ 中是单位。将 $F$ 除以该系数得到 $R_u[u]$ 中的首一多项式。

令 $h_u$ 是 $\mathbb Q(Q)[u]$ 中 $F,G$ 的首一 gcd。首一整多项式的首一因子系数对 $R_u$ 整；它们又在 $\mathbb Q(Q)$ 中，故整闭性给
$$
h_u\in R_u[u].
$$
因为 $h_u$ 首一，除 $F,G$ 的多项式短除也在 $R_u[u]$ 内进行；在分式域中余式为零，故环中同样为零。将其约化到 $R_u/(1009,Q-2)=\mathbb F_{1009}$，首一性保留全部 $u$ 次数，并且约化后仍整除两条完整模输入。因此
$$
\deg_u h_u\le41.
\tag{8}
$$

同理，在
$$
R_Q=\mathbb Z_{(1009)}[u]_{(1009,u-2)}
$$
上，$F$ 的 $Q^{222}$ 系数约化为 $992\ne0$。应用同一首一因子整性论证，$\mathbb Q(u)[Q]$ 中首一共同 gcd 的 $Q$ 次数至多 68。

二维多项式 gcd $H$ 在 $\mathbb Q(Q)[u]$ 中只丢掉纯 $Q$ 内容，而这不改变其 $u$ 次数；在 $\mathbb Q(u)[Q]$ 中同理。因此得到完整双次数上界 (3)，包括公共因子的全部重数。第二方向也控制纯 $Q$ 公共因子，不能由第一方向代替。

这不是在模因式与 QQ 因式之间建立一一对应。实际 $H$ 可能次数更低，甚至为常数；当前尚未确定。若 $H$ 非常数，所有共同曲线都在 $H=0$ 上，且 $\deg H\le41+68=109$。不在该曲线上的共同零点来自去掉 $H$ 后的两个多项式之交；它们不能因 (3) 被删除。

## 5. 唯一实际身份

- 首次 run：[46156015273](https://github.com/Rogerhu12/math-research-public/actions/runs/46156015273)；job：141012730204；attempt 1。
- 冻结源码 blob：079cc6744ab5ac9d95cc9ea649d94e7a34af9f3c；SHA256：060d321f863b93ef8d1825ca3dc86d41f12573101257b1ace3c3a6ac8e24e2f7。
- 源提交：cf226ce2333689bc8202a3eacb751347cc4bd42f。
- 实际规则读取：2026-11-28 14:42:26.629998 UTC；真实 pull 后提交 0481a16fa180ef7d977814267edd981ac330f4ab；两份规则无变化。
- 内层数学 3.455845477 秒；driver 3.530707191 秒；最大 RSS 64972 KiB；源退出码 0。
- stdout 11684 字节；SHA256：991fd157a07150cce8d8aa0e0cd23d3f19938f7c1d304ca5d45d2f596af38d3f。
- 实际完整返回：680 个最高矩阵坐标，2650 个新多项式 Bareiss 乘积，519 个新多项式 Euclid 乘积。
- [冻结原输入](../notes/2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542-input.md)、[完整源码](../notes/2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542.py)、[小回执](../notes/2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542-execution.json)。

四个依赖的完整 SHA 在任何定义执行前核对。只再生必要唯一参数，没有执行旧原均值迹、旧 cofactor/乘子证明、原固定 12 阶单点门或任何冻结失败。未保存展开 QQ 二元行列式或系数载荷。

## 6. 当前边界与后继要求

本条已付新的全图非零必要支持 $G$、其明确次数界，以及 QQ 公共曲线的双次数上界。它没有支付“$F,G$ 无共同曲线”，所以不能使用条件式 $444\cdot730$ 来宣称整个权零集有限；也没有得到全 Phi 排空。

[完整六式全权十三生成](R150-appendix-unit211-Phi-zero-corrected-original-N1-highest-unit-and-whole-I6-thirteen-generators.md)是独立纸面结果，保证未作几何局部化的必要代数对权环有限。本次公共权曲线仍可能存在；有限权纤维不等于有限个权点。

若下一输入剥除某些旧已付权因子，必须先提供原 QQ 多项式或固定原矩阵中的真实整除身份及重数，再据该身份处理全权支持。不能直接删除本次模 gcd 的任何因子。原最高系数零面、$G$ 的一阶 $u$ 次数差和两个非恒定共同 gcd 全部保留。
