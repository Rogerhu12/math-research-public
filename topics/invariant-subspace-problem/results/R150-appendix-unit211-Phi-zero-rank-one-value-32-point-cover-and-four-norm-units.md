# R150 补充：真正 1069 次余式的 32 点覆盖与四个原二次范数单位

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 结论与范围

继续有序 $h=1$ 的 $\Phi=0,z_n=0$ 原图。使用 [H4/H20 整纤维排除与 QQ 整除](R150-appendix-unit211-Phi-zero-rank-one-value-H4-H20-complete-fibers-and-QQ-divisibility.md)，取全部因子的首一规范，已有
$$
Q_{876}=Q_{840}\phi_4^4\phi_{20}\mid R,\qquad
R_{1069}=\frac{R}{\operatorname{LC}(R)Q_{876}}
\in\mathbb Z_{(1009)}[\lambda].
$$
$R_{1069}$ 首一且次数恰为 1069；$Q_{876}$ 在所有实际原点处非零。

本稿有两个新结论：

1. 不同实际 $(\lambda,\rho)$ 基点至多 32 个，保留原首一 $\ell$ 二次后，不同三元组至多 64 个。
2. 在全部剩余实际原点上，原二次代数中的
$$
\operatorname{Nm}(\ell),\quad
\operatorname{Nm}(u),\quad
\operatorname{Nm}(u-\ell),\quad
\operatorname{Nm}(b)
$$
都非零。因此这四个元素可以合法使用伴随元除以其范数作逆。

第二项比原 $\ell,u,u-\ell,b$ 自身非零更强：它同时排除同一二次关系另一根上的零值影响。没有将原单位的范数自动视为单位，也没有重做此前的四个原权面排除。结论仍限于此有序图；交换得到的 $k=1$ 图另行覆盖，未合并计为同一个 32 点界。

## 2. 真正 1069 余式的直接模返回

仍用固定 27 阶原 $R=\operatorname{Res}_\rho(F,G)$、固定 28 阶原
$$
P=\operatorname{Res}_\rho(C_E,G),\qquad
P_B=\operatorname{Res}_\rho(C_B,G).
$$
本次在 1009 下实际构造完整 $\bar Q_{876}$，从完整 $\bar R$ 除去，并完整乘回。所得余式次数为 1069，首一化后的 SHA256 为
$$
\texttt{5ce316bc5c08ba15adbbeeaa5a34e1628fc64597852ca9a74e2068bc14d3cc5c}.
$$
实际又核得它与 $\bar Q_{876}$ 互素，未从旧因子整体重数推断分裂模因子的余量。

接着直接实际扩展 Euclid，完整乘回
$$
a\overline{R_{1069}}+b\bar P+c\bar P_B=g_{32}. \tag{2.1}
$$
三个输入次数为 $1069,2005,2096$，标签次数为 $1972,1036,-1$；前两个输入的 gcd 已为 32 次，第三个保持 32 次。$g_{32}$ 的系数从常数到最高次为
$$
\begin{aligned}
(&722,278,731,355,485,40,431,879,886,775,986,900,350,67,972,697,\\
 &900,306,248,789,718,976,181,674,177,210,486,428,438,486,520,1003,1).
\end{aligned}
$$
其 SHA256 为
$\texttt{a97d9ceb641c3c5162af051160864103b4dc8d6a0431a740e3c932378d4f9dec}$。

取首一
$$
K=\gcd_{\mathbb Q[\lambda]}(R_{1069},P,P_B).
$$
作为首一 1009 整多项式的首一因子，$K$ 也为 1009 整。其约化保持次数，并整除 (2.1) 的三个输入，所以
$$
\deg K=\deg\bar K\le32. \tag{2.2}
$$
对固定 $\lambda_0$ 的每个不同实际 $\rho$，三个固定 Sylvester 都有对应的幂列核向量。不同 $\rho$ 的这些列线性无关，因此该纤维实际 $\rho$ 数不超过三个结式消失阶的最小值。由于 $Q_{876}(\lambda_0)\ne0$，它也不超过 $\operatorname{ord}_{\lambda_0}K$。对全部纤维求和得到 32 点界；原二次 $\ell$ 关系给 64 个三元组界。首项降阶和零多项式专门化均保留。

## 3. 原范数零面的完整无除法一元覆盖

原二次代数写成
$$
\ell^2+\alpha\ell+\beta=0.
$$
对 $U=a+d\ell$，其真实乘法范数为
$$
N_U=a^2-\alpha ad+\beta d^2,\qquad
U\big((a-\alpha d)-d\ell\big)=N_U. \tag{3.1}
$$
对 $U=\ell,u,u-\ell,b$，源码在原二次代数中完整核对 (3.1)。只清已付基础参数单位之后，每个范数的分子成为一个真正的 $\rho$ 二次
$$
q_U(\lambda,\rho)=A_U(\lambda)\rho^2+B_U(\lambda)\rho+C_U(\lambda).
$$

本次从同一原 $F,G,C_E,C_B$ 对 $q_U$ 做无除法伪余式。逐步完整乘回
$$
A_U^{e_j}F_j=Q_jq_U+V_j+U_j\rho. \tag{3.2}
$$
没有倒置 $A_U$，也未删除其零纤维。因此实际原点如果满足 $N_U=0$，必同时使以下真正的一元多项式为零：
$$
A_UV_j^2-B_UU_jV_j+C_UU_j^2,\qquad
U_iV_j-U_jV_i. \tag{3.3}
$$
即使 $A_U=0$ 或余线性式首项为零，(3.2)–(3.3) 仍然成立。

对全部 (3.3) 在 QQ 中实际扩展 Euclid、完整乘回并因式分解，得到四个非零首一 gcd。其次数与全部不同因子支持如下。记
$$
A_2=2\lambda^2-2\lambda+1,\quad
B_{3q}=4\lambda^2-2\lambda+1,\quad
C_2=3\lambda^2-2\lambda+1.
$$

| 原范数 | QQ 覆盖次数 | 不同因子支持 |
|---|---:|---|
| $N_\ell$ | 293 | $C_2,J_{\ell,12},2\lambda-1,B_{3q},\lambda-1,A_2$ |
| $N_u$ | 153 | $C_2,2\lambda-1,B_{3q},\lambda-1,A_2$ |
| $N_{u-\ell}$ | 221 | $C_2,2\lambda-1,B_{3q},\lambda-1,A_2$ |
| $N_b$ | 285 | $C_2,J_{b,12},2\lambda-1,B_{3q},\lambda-1,A_2$ |

两个十二次整数多项式按常数到最高次为
$$
\begin{aligned}
J_{\ell,12}:\;&(9,-108,654,-2580,7329,-15720,26056,\\
&-33600,33456,-25088,13440,-4608,768),\\
J_{b,12}:\;&(2,-24,147,-590,1719,-3816,6612,\\
&-9000,9528,-7616,4320,-1536,256).
\end{aligned}
$$
四项全部幂次、精确有理常数、每个原输入与 Bézout 标签身份均在小回执中。这里只需要不同因子支持，而非将某个单位面的 $\lambda$ 像自动删除。

## 4. 新完整 32 对 32 Bézout 支付范数单位

令真正的整数多项式
$$
Z_{32}=C_2J_{\ell,12}(2\lambda-1)B_{3q}(\lambda-1)A_2J_{b,12}.
$$
其次数为 32。所有第 3 节的 QQ 覆盖的根都属于 $Z_{32}=0$。

从本次实际 $g_{32}$ 和上述精确整数因子，另用纯 V8 小有理余数程序实际完成 33 步 Euclid。全部标量逆、每步多项式除法和每步标签都完整乘回，最终得到
$$
a_{31}g_{32}+b_{31}\overline{Z_{32}}=1. \tag{4.1}
$$
两个完整标签均为 31 次，所有系数已保存在专门小回执；实际耗时 7 毫秒。

如果存在实际原点使四个范数中的一个为零，第 3 节给该点的 $\lambda$ 是 $Z_{32}$ 的根，同时第 2 节给它是 $K$ 的根。于是 $\gcd_{\mathbb Q[\lambda]}(K,Z_{32})$ 是一个非平凡首一因子。它作为首一 $K$ 的因子为 1009 整，约化保持次数，并同时整除 $g_{32}$ 和 $\overline{Z_{32}}$，与 (4.1) 矛盾。这就支付了四个范数全体非零。

由 (3.1)，现在可在这个实际原图上合法使用
$$
U^{-1}=\frac{(a-\alpha d)-d\ell}{N_U}
\quad(U=\ell,u,u-\ell,b). \tag{4.2}
$$
这只授权这四个已付范数；尚未把 $N_{T_0}$、$N_{P_f}$ 或任意新范数当成单位。

## 5. 冻结源与真实执行

Python 原源：
[真正余式与原单位面像](../notes/2026-11-27-unit211-Phi-zero-rank-one-value-original-unit-face-image-input-8542.py)。

- source blob：$6d55fc76ffe3f1922c074f8ccc7a68a0e0a3b7e1$；
- SHA256：$f66e913c9508536a4213b6164bd133a0404f048ad9fbb9b72114f686542c84a3$；
- Actions run/job：46003172567 / 140519731590；
- 内层实际 exit：0；5.042920521 秒；71108 KiB；
- stdout：38966 字节，SHA256 $bd1fe2176b320e1b931c5b343e1515407decefe8653d8b2cb4bef7dcb6942b71$；
- main：$97974e6ed90b9ab0f7f56efb51315be9b9eaea21$；
- 12:59:22.554070 UTC 的实际 pull 后两 README blob 均无变。

新增 V8 源：
[四个范数覆盖的完整小 Bézout](../notes/2026-11-27-unit211-Phi-zero-rank-one-value-four-norm-units-Bezout-8542.js)。

该文件是供 $\,\texttt{Function(source)()}\,$ 调用的完整函数体；源 SHA256
$\texttt{ac4869b2b6b01e0f71ecdcfb34d18cbcfe074da0d83a73bc922ad1e50f6b386d}$，
3563 字节，实际执行返回完整两个 32 项标签，7 毫秒，无外部输入。此次小执行专门支付 (4.1)，没有重跑前述 QQ 局部或大结式。

仍未排空该碰撞图、整个 $\Phi=0$ 面或 ordinary ISP。
