# R1081. 原47角代数的非退化迹与4513的十六个实际整一维Hecke块

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

**状态：已证明，含精确计算。**
在原 $X=X_{\rm ns}^+(47)$、$J=\operatorname{Jac}(X)$ 上：

1. R1078 的23个非恒等角对应在 $\operatorname{End}_{\mathbf Q}(J)$ 中线性独立，
   其生成的有理代数维数为23，trace-zero 子空间维数为22。
2. 原实际对称对应 $Z=13R_0+4R_2$ 满足
   $$
   \boxed{\quad \operatorname{Tr}Z=0,\qquad
   \operatorname{Tr}(Z^2)=336288>0.\quad}
   \tag{1081.1}
   $$
   因此 $Z$ 在原 Jacobian 上确实非零。
3. 在 $\ell=283$，完整原整 Hecke 代数是有限 étale 最大整序，
   但没有 $\mathbf Z_{283}$ 直因子。
4. 在 $\ell=4513$，完整原整 Hecke 代数也是有限 étale 最大整序，
   且**恰有16个 $\mathbf Z_{4513}$ 直因子**。
   原 good-reduction Hodge/Lie 格在此整 Hecke 代数上自由、秩一。
   一个具体一维块由
   $$
   \mathfrak m=(4513,\ T_2+2T_3+4T_5-434)
   \tag{1081.2}
   $$
   指定，属于R1080的16维有理新形式因子。

这些结论仍不提供 Mordell–Weil 格的局部饱和、CM对数非零首项、
高度的赋值一，或八个原CM圆盘内的有理点唯一性。

## 1. 实际角对应及完整迹来源

所有 $R_C$、其 degree、fixed divisor、CM/cusp重数及composition，
均是R1078的原几何对象。
程序首先按该文原加权角纤维求 $E_4,E_3,n_C$，
以
$$
\tau_C=d_C-E_4(C)/4-E_3(C)/3-23n_C/2
$$
取得实际Hodge trace；再核其完整二次字符闭式。
$C=0$、零radicand和全部23个cusps均保留。

另外真正构造全部 $x^2=-I$ 的迹零矩阵并除 $\pm$，
取得1081个原necklaces。
对每个目标角，枚举全部中间necklaces，核全部输入角对的
composition重数；因此读到的是R1078的实际finite moduli fiber。

以 $\{\operatorname{id},R_0,R_2,\ldots,R_{23}\}$ 为24个输入，
准确Gram矩阵为
$$
G_{A,B}=73\mathbf1_{A=B}d_A+\sum_Dn_{A,B}^D\tau_D
$$
及identity行 $\operatorname{Tr}R_C=\tau_C$。
有理数的完整Schur补消元给：
$$
\operatorname{rank}G=23,\qquad
\dim\ker G=1,\qquad G\text{ 正半定}.
\tag{1081.3}
$$
唯一核由已知实际关系
$\operatorname{id}+\sum_CR_C=j^*j_*=0$ 生成。

每个对应Rosati自伴，所以 $\operatorname{Tr}(F^2)=0$
当且仅当 $F$ 在Hodge空间、进而在实际Jacobian上为零。
因此(1081.3)证明所有非恒等 $R_C$ 线性独立；
它们的代数包含identity，维数23。
trace在identity上为73，故trace-zero子空间维数22。
读出指定 $Z$ 的二次型值就是(1081.1)。
没有以permutation representation的非零代替Jacobian上的非零。

## 2. 完整原Hecke空间及两个认证算子

重建R1080的精确有理modular symbols，只用于本次新的Hecke输入，
不重跑该文已完成的$L'$认证。
实际Fricke矩阵从全157维新空间中识别出16、24、33三个正号因子。

在同一个完整73维Hodge空间上取
$$
H_t=T_2+tT_3+t^2T_5.
$$
本次请求限定 $1\le t\le16$，逐素数取首个满足完整特征多项式
模 $\ell$ squarefree 的 $t$；实际在 $t=1,2$ 即全部完成：

| 素数 | 实际算子 | 完整特征多项式次数 | 模该素数 |
|---:|---|---:|---|
| 283 | $H_1=T_2+T_3+T_5$ | 73 | squarefree |
| 4513 | $H_2=T_2+2T_3+4T_5$ | 73 | squarefree |

按三个原有理新形式因子分组，全部不可约模因子的次数为：

| 有理因子维数 | 在283的次数 | 在4513的次数 |
|---:|---|---|
| 16 | $4,12$ | $1^{\times6},2^{\times2},3^{\times2}$ |
| 24 | $4^{\times3},12$ | $1^{\times10},2^{\times4},3^{\times2}$ |
| 33 | $11,22$ | $11,22$ |

这些是完整73次多项式的分解，因子无重根且跨三个有理因子也不相撞。
所以283没有线性因子，而4513恰有16个。
在16维因子的4513分解中，$H_2$ 的根434是一个简单线性根，
给出(1081.2)。另一个属于24维因子的例子是根1054。

## 3. 为何这确实付款原整Hecke分块

设 $\mathbb T$ 是原Jacobian上实际整Hecke对应生成的代数，
$T_{\mathbf Q}=\mathbb T\otimes\mathbf Q$。
R1080及new multiplicity one给 $\dim_{\mathbf Q}T_{\mathbf Q}=73$。

对上节相应的 $H$，其完整特征多项式 $P$ 是整、首一、degree73；
$P\bmod\ell$ squarefree迫 $P$ 在特征零也无重根。
因此 $H$ 的最小多项式degree73，并有
$$
\mathbf Q_\ell[H]=T_{\mathbf Q}\otimes\mathbf Q_\ell.
\tag{1081.4}
$$
整代数 $\mathbf Z_\ell[H]$ 是有限étale，其有理化就是(1081.4)，
故它已是该有理代数的最大整序 $\mathcal O$。
其它所有实际整Hecke算子的特征值是代数整数，所以
$$
\mathbf Z_\ell[H]\subseteq
 \mathbb T\otimes\mathbf Z_\ell\subseteq\mathcal O
 =\mathbf Z_\ell[H].
\tag{1081.5}
$$
于是两边相等。

这同时排除了非极大整序和不同特征零因子的剩余congruence歧义；
不能只凭一个系数域的某个根在 $\mathbf Q_\ell$ 中就跳过(1081.5)。
线性模因子经Hensel提升与整CRT给真正幂等元，
对应的完整局部Hecke代数就是 $\mathbf Z_\ell$。

这些算子是原 $X_{\rm ns}^+(47)$ 上的实际Hecke对应；
Chen同源仅识别其有理特征多项式，没有搬用平方水平曲线的整基。

因 $\ell\ne47$，原曲线/Jacobian有良好约化，
原Hodge格 $M=H^0(J_{\mathbf Z_\ell},\Omega^1)$ 是秩73的自由
$\mathbf Z_\ell$ 格，并稳定于(1081.5)。
将有限étale代数分解为若干非分歧DVR $O_i$。
每个 $e_iM$ 在 $O_i$ 上无挠；由generic multiplicity one，
其 $O_i$-秩为一，故在DVR上自由秩一。
因此
$$
M\simeq\mathbb T\otimes\mathbf Z_\ell
\quad\text{作为Hecke模，非规范地。}
\tag{1081.6}
$$
非分歧trace对偶也自由秩一，同理给原Lie格。
每个4513的一维块由此确实给原微分/Lie的一条整直和线，
并非只存在于未比较的有理模型上。

## 4. 真实公开执行与摘要

- run [45936209617](https://github.com/Rogerhu12/math-research-public/actions/runs/45936209617)，
  job **140299891342**，attempt1，success。
- 源 **48868923fb4980038fbadfaa6a6cdf625c9d6e89**。
- 完成 **8.576810260秒**，数学预算600秒、预留30秒。
- 脚本 [full_p47_Cartan_Hecke_certificate.py](../scripts/full_p47_Cartan_Hecke_certificate.py)，
  SHA-256 **522f41e56d17fe3aabea7167f6f1d2c8f006eadf7275dcd06c2dad45786552e2**。
- 请求 [full-p47-Cartan-Hecke-request.json](../notes/full-p47-Cartan-Hecke-request.json)，
  SHA-256 **68ed263279a0c0d5d81ec419f1f92312009b5da89e051da846716770ff74156a**。
- 方法 [full-p47-Cartan-Hecke-method](../notes/2026-11-27-full-p47-Cartan-Hecke-method.md)，
  SHA-256 **6e1f282cb0cec38a48f8cbedb12b3216268a860bac1b21a41646397ae4bd630f**。
- Sage10.6、固定官方image digest及两README/源码SHA见请求和preflight。
  整数、有理数、有限域步骤均为exact，无浮点输入。

| 输出来源 | SHA-256 |
|---|---|
| 原fixed-cycle trace rows | a1023cd15725ca809ab28958acab25290364b8f29f63eb16776105cba581a4f3 |
| 原composition tensor | 62e18e4507fb2fb1bfecd4438ac3bfc54c28c332d2bf6884c83b75e37dec57a6 |
| 实际Gram矩阵 | 0196fe99de7f8a8f9486e385f15d81eb4cf0070db48979b299cc1ca08acbf253 |
| 完整有理LDL pivots | 44f6510795bcec67aa783530f5857213d4916ea6d93ff46e0f3dca83384c685e |
| $H_1$完整整特征多项式 | e7fedef7a3571d75ffddf49f5d586069282ffad8c8593967ad13b9fbb211d7b2 |
| $H_2$完整整特征多项式 | 875bf6df79fb850ce65cf162917456ff9c8495947b2780fe9f1e02f8c8dc0fb4 |

原necklace、tensor、Gram、系数数组仅在runner内，
不提交或上传artifact/Release；重建只需上述脚本和请求。

## 5. 准确后继边界

原非零trace-zero方向、full47秩73，以及4513的十六个整一维块现在均已付款。
但R1074的辅助同点识别发生在283，不能自动换成4513；
新的完整4513标签比较必须包括特殊scalar Cartans和全部coarse自同构。

即使选定(1081.2)的块，仍要付该块的Mordell–Weil对数格、
指定CM除子的局部对数首层及完整高度消去。
此外，$Z$的trace为零并不表示其在指定剩余块上的特征值为零；
这个实际特征值或另选对应也尚须计算。
本结果不含盘内有理点唯一性或全素数Serre结论。
