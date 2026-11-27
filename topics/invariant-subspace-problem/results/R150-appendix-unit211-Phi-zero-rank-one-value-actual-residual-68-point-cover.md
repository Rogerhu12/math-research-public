# R150 补充：真正 1105 次余式的原 Gauss 返回与 68 个不同基点

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 结论与已付输入

继续有序 $h=1$ 的 $\Phi=0,z_n=0$ 原图。由
[六个 QQ 因子与 1105 次原覆盖](R150-appendix-unit211-Phi-zero-rank-one-value-six-QQ-factors-and-1105-original-cover.md)，已有真正的

$$
R_*=\frac{R}{\operatorname{LC}(R)Q_{840}}
\in\mathbb Z_{(1009)}[\lambda],
\qquad \deg R_*=1105,
$$

且 $R_*$ 首一、约化保持度数。$Q_{840}$ 的全部原复数零纤维已由原单位和整 $c=1/2$ 返回支付，所以它在任何实际原解处非零。

**本稿结论：该选定有序图中，不同实际 $(\lambda,\rho)$ 参数点至多 68 个，保留原首一 $\ell$ 二次后，不同三元组至多 136 个。** 这里没有证明 68 个候选存在，也没有把它们全部排空。$k=1$ 的另一有序图仍由 B/C 交换另行覆盖，未合并计成同一个 68。

新增计算是真正余式对原完整投影的直接 Bézout，补齐了分裂模因子的重数细节；不是把先前的 908 次模 gcd 除掉 840 次后直接认作新的 gcd。

## 2. 实际一元输入

仍令 $F,G$ 为原 $(E_1,E_C)$ 与 $(N_1,\ell N_1)$ 的必要 core，令 $C_E$ 为原 $(E_1,\ell E_1)$ 的 core，$C_B$ 为原 $(E_1,E_B)$ 的 core。其固定次数及原点必要性均已支付。定义真实 QQ 整系数投影

$$
P=\operatorname{Res}_{\rho}(C_E,G),\qquad
P_B=\operatorname{Res}_{\rho}(C_B,G).
$$

这两个固定原 Sylvester 的阶数为 28，模输入的 $\rho$ 次数保持。虽然没有要求它们自己的 QQ 最高次数在 1009 下保持，其完整模多项式仍是同一固定 QQ 行列式的真实约化，这已经足够用于下面的 Gauss 上界。

本次从主 $\overline R$ 实际除去已经在 QQ 中支付的首一 $\overline Q_{840}$，完整回乘得到 1105 次余式。源码先直接核验

$$
\gcd(\overline{R_*},\overline Q_{840})=1.
$$

随后实际计算并完整乘回

$$
a\overline{R_*}+b\overline P=g_{68},\qquad
c\overline{R_*}+d\overline P+e\overline{P_B}=g_{68}. \tag{2.1}
$$

有理最高系数归一化只改变非零模常数，不改变这些 gcd。两次实际 gcd 均为 68 次，第二次没有进一步缩小。最终标签次数为 $1936,1036,-1$；全部多项式乘积和相加结果都已验证。68 次 gcd 的系数 SHA256 为

$$
\texttt{51ff3c9fba943f174369ce7beff7b81cd6b6505be5f3180f4de966b1bfe542a6}.
$$

## 3. 从真正首一覆盖提升到 QQ

令

$$
H=\gcd_{\mathbb Q[\lambda]}(R_*,P,P_B)
$$

取首一规范。$H$ 是首一的 1009 整多项式：例如用离散赋值 Gauss 内容乘法，$R_*=HK$ 的两首一因子均有内容赋值不大于 0，而内容赋值之和为 0，因此两者均为 1009 整。等价地可用整闭性或根整性。

因为 $H$ 首一，$\deg\overline H=\deg H$。对整多项式 $P,P_B$ 作 $H$ 的首一除法，商也为 1009 整，因此 $\overline H$ 整除 (2.1) 的三个输入。于是

$$
\deg H=\deg\overline H\le\deg g_{68}=68. \tag{3.1}
$$

这里没有从一般多变量模空性推 QQ 空性，也没有把模 68 次多项式本身猜作 QQ 覆盖；使用的是已经支付的真实首一 $R_*$ 及它的 QQ 公共因子。

## 4. 各参数纤维的原重数给不同基点数

固定一个有限 $\lambda_0$，令 $r$ 为该纤维中不同实际 $\rho$ 值的数目。由原 $F,G$ 在 QQ 中互素，它们没有共同垂直整线，所以这一集合有限，且至少一条非零专门化多项式的次数不大于 14，故 $r\le14$。

每个原 $\rho$ 值同时使 $F,G,C_E,C_B$ 为零。其幂列

$$
(1,\rho,\ldots,\rho^{N-1})^\mathsf T
$$

分别给原 $R$ 的 27 阶矩阵及 $P,P_B$ 的 28 阶矩阵的右核向量。$r$ 个不同 $\rho$ 值给 $r$ 个独立 Vandermonde 列，故

$$
r\le\operatorname{ord}_{\lambda_0}R,\qquad
r\le\operatorname{ord}_{\lambda_0}P,\qquad
r\le\operatorname{ord}_{\lambda_0}P_B.
$$

若任一输入在 $\lambda_0$ 处降阶，甚至某两个投影输入都为零多项式，核列论证仍成立；没有除去这些参数纤维。因为 $Q_{840}(\lambda_0)\ne0$ 对任何实际原解成立，

$$
\operatorname{ord}_{\lambda_0}R_*
=\operatorname{ord}_{\lambda_0}R.
$$

因此

$$
r\le\operatorname{ord}_{\lambda_0}H.
$$

对全部实际 $\lambda_0$ 相加，再用 (3.1)，得到不同原基点数至多 68。原 $\ell$ 二次的全部根保留，遂得 136 个不同三元组上界。

## 5. 可再生源与真实执行

源：
[真正 1105 余式原 Gauss 输入](../notes/2026-11-27-unit211-Phi-zero-rank-one-value-actual-1105-residual-Gauss-input-8542.py)。

- 源 blob：$2711018345a6ece1954b44d3c84b41eea904f82e$；
- 源 SHA256：$415b702b78c8eab35217529f5d8f8185a715e1d4afa2057cb9e09dbb0f469588$；
- Actions run/job：45999545362 / 140507384078；
- 实际内层 exit：0；3.690168307 秒；52380 KiB；
- stdout：13561 字节，SHA256 $f232f146f472b74bb7cdd2e15dce8de8ae9243e9d27a602fd9185712cc3d2e5f$；
- 实际源 main：$a66e9299ad72ebe87aef17b3683a619518618f52$；
- 12:33:03.929555 UTC 的实际 pull 后两 README blob 均无变。

这是一条真实有限覆盖结论，尚未排除全部原点或完成 ordinary ISP。
