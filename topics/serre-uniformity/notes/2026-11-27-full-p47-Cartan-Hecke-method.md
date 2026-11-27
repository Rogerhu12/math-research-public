# full47 原角迹配对与辅助整 Hecke 分解请求

日期：2026-11-27（Asia/Taipei）；Astra-serre-24b8836b-20261126。

本次是新的两个有限输入，不重跑 R1080 的导数或 R1074 的辅助筛选。
数学来源为已纸证 R1078 和已认证 R1080。
脚本仅在本公开仓库 Actions 执行，数学总预算600秒、预留30秒。

## 1. 原 Cartan 对应的实际迹配对

按 R1078 的二十三个角类 $C\ne\pm1$：
先用原 $\mathcal F_4^*,\mathcal F_3^*$ 的加权角纤维、实际非零 cusp 参数，
得到 $E_4,E_3,n_C$ 及准确 Hodge trace $\tau_C$；
再与同文完整二次字符闭式比较，保 $C=0$ 和零 radicand 特例。

composition 的公式来源已在 R1078 §7 完整证明。
执行中另构造全部原 $x^2=-I$ trace-zero matrices 并除 $\pm$，
得到实际1081个 necklaces；固定一端点，对每个目标角枚举全部中间点，
核所有输入角对与目标角的 composition 重数。
这是实际有限 moduli fiber 的实现，不用另一条曲线的近似矩阵。

以 identity 和23个原对应为24个输入，计算
$$
\operatorname{Tr}(R_AR_B)=
73\mathbf1_{A=B}d_A+\sum_D n_{A,B}^D\tau_D.
$$
identity 行为 $\operatorname{Tr}R_C=\tau_C$。
用有理数的完整 Schur complement/LDL 消元给迹配对的准确 rank、
正半定性和全部零空间维数；同时核每行在
$\operatorname{id}+\sum_CR_C=j^*j_*=0$ 上消失。

对实际 $Z=13R_0+4R_2$，读取 $\operatorname{Tr}Z$ 和
$\operatorname{Tr}Z^2$。由 Rosati 正性，后者正才证明
$Z$ 的实际 Jacobian endomorphism 非零。
程序不预设 rank 或这个数值，不把 permutation representation
的非零当成 Jacobian 上的非零。

## 2. 真正的整 Hecke 分块

为这个新输入重建 R1080 的精确完整 new Fricke-positive modular-symbol
空间；不重算 L′。三个正号因子维数必须是16、24、33，
并由 actual Fricke 矩阵在全157维new空间中再次识别。

在同一个73维 Hodge 空间上取真实整 Hecke endomorphism
$$
H_t=T_2+tT_3+t^2T_5,\qquad t=1,\ldots,16.
$$
对 $\ell=283,4513$ 分别找首个使完整73次特征多项式
模 $\ell$ squarefree 的 $t$。
这是有明确范围的新输入搜寻；若16个都不满足，只记录未认证，
不判该素数的整 Hecke 代数不分裂。

若 $P_t\bmod\ell$ squarefree，则
$\mathbf Z_\ell[H_t]$ 是秩73的 finite étale order。
其有理化已等于完整 multiplicity-one Hecke algebra：
$H_t$ 的最小多项式具有73个不同根，因此degree为73。
finite étale order在此有理代数中就是最大整order。
全部原整 Hecke operators 的 eigenvalues 为代数整数，故
$$
\mathbf Z_\ell[H_t]\subseteq
 \mathbb T\otimes\mathbf Z_\ell\subseteq
 \mathcal O_{\mathbb T\otimes\mathbf Q_\ell}
 =\mathbf Z_\ell[H_t].
$$
这证明两个包含都是等号。

因此完整模 $\ell$ 因式分解的**线性因子**确实给
$\mathbb T_{\mathfrak m}\simeq\mathbf Z_\ell$，
并给原 good-reduction Hodge 格的一个rank-one整直和块。
这比局部类型的character field分裂条件更强：
它同时排除了其它因子与该根的剩余 congruence，以及非极大order的歧义。

所有 $T_n$ 都是原 $X_{\rm ns}^+(47)$ 的实际 Hecke 对应；
Chen同源仅用于识别其有理特征多项式。
不将平方水平曲线的某个整微分基未经尺度比较搬过来。
因 $\ell\ne47$、原 $X$ good reduction，这些整对应真实作用于原Hodge格。
squarefree给出的幂等元就在整Hecke代数内，故其rank-one结论属于原整格。

消费者输出每个新形式因子的完整 residue degrees 和线性根，
以及整特征多项式SHA；大矩阵、可重算多项式和数组不保存。

## 3. 执行来源与边界

采用与R1080相同的官方Sage10.6 digest，
先核Actions/仓库、实际只读checkout引用、请求及所有源码/README SHA。
精确有理分解用proof.all(True)及通常decomposition()，
不传Sage10.6不支持的QQ-kernel显式proof关键字。
全部有限域、整数和有理运算是exact；此请求没有浮点步骤。

即使取得非零trace-zero对应和degree-one整块，
仍未计算这些块的Mordell–Weil饱和指数、局部对数首项或高度。
$\ell=283$上的同点筛选不能无证明移到4513；
完整辅助源、scalar特殊行及真正盘内排除另行处理。

脚本、请求、方法、run和摘要哈希入库；
原necklace数组、composition tensor、Gram矩阵和Hecke多项式只在runner内，
不上传artifact或Release。
