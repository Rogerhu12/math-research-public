# R271 附录：三对正权的完整联合来源与七位出生二首末边

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 状态：完整原 S1/S2 及以下七位整源结论已证明。
- 唯一精确输入：[原三塔与双交叉源码](../notes/2026-11-28-three-pairs-original-joint-three-tower-8542.py)，Git blob 7d4bdca36ff96157111f715add4987037764f075。

## 1. 完整物理结论及与旧结果的区别

六位原物理权为
$$
b=(\sqrt x,\sqrt x,\sqrt y,\sqrt y,1,1),\qquad x,y>0.
$$
记整个原上、低 primitive 空间为
$$
K=\ker d\cap H_2,\quad \dim K=9,\qquad
L=\ker d\cap H_1,\quad \dim L=5.
$$
沿用 [R275](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 的实际算子：
$$
G_j=\Gamma_{j,2},\quad L_j=\Gamma_{j,1},\quad
C_1=G_1^{-1},\quad C_2=G_2^{-1},\quad F=C_1^2-C_2,
$$
$$
B=d_{b^3}|_K,\qquad
\Delta=\frac12(C_1B^*L_3-B^*L_2),
$$
$$
A=\frac12(C_1B^*L_2+B^*L_2L_3^{-1}L_2).
$$
所有 $\Gamma$ 先取完整层 MP 逆再压缩，所有伴随使用原物理内积。

**定理 1。** 对全部 $x,y>0$，整个九维 $K$ 和五维 $L$ 上严格有
$$
\boxed{
F-\Delta L_3^{-1}\Delta^*>0,\qquad
I_L-A^*G_1A-L_1L_2^{-1}L_1>0.
}
\tag{1.1}
$$
这同时支付真实 S1 创新与同源 S2，两种来源和两个 cross 均保留。

**定理 2。** 对任意 $a,x,y>0$ 的七位权
$$
(a,\sqrt x,\sqrt x,\sqrt y,\sqrt y,1,1),
$$
整个十四维出生二 primitive 空间的两个合法内部高度均严格满足
$$
\boxed{
\Gamma_j\Gamma_{j+1}^{-1}\Gamma_j
\prec\Gamma_{j-1},\qquad j=1,2.
}
\tag{1.2}
$$
而且固定 $x,y$ 后，可取一个不依赖新增位 $a$ 的共同常数
$c(x,y)<1$ 替代 (1.2) 右侧的系数一；具体实际定义见 §7。
不声称该常数对全部 $x,y$ 还有已知统一小于一的上界。

旧[两组加一位全出生全高度](R239-appendix-two-weight-groups-one-exceptional-all-births-all-heights-strict-bound.md)
及[两组加两异常位出生二首边](R292-appendix-main-parameter-s2-and-all-two-exceptional-birth-two-first-edges.md)
不包含一般四种权值的 $2+2+2+1$ 七位族。
旧[三对全部正权偶相位](../notes/2026-11-14-three-pairs-all-weight-complete-even-phase-bound-789f-next.md)
确已处理同一六位九维模型的另一算子 $\Phi$，但没有给出 (1.1) 的原两项联合费用；
本篇不重算其相位证书。

## 2. 整个原空间的正交块

每个二位等权组按真实正交串分成出生零、长度二的对称串，
和出生一、长度零的 singlet。
所有组内串同时约化 $d,d^*$、三次下降、完整层 Gram、完整逆和 primitive 投影。

| 组内 singlet 数 | 上相对出生 | 上维数合计 | 下相对出生 | 下维数合计 |
|---|---:|---:|---:|---:|
| $0$ | $2$ | $3$ | $1$ | $2$ |
| $1$ | $1$ | $3$ | $0$ | $3$ |
| $2$ | $0$ | $3$ | 无 | $0$ |

一个 singlet 的三个块，各是其余两组的实际出生一及真空来源。
[任意正权出生一严格 S1](R288-appendix-birth-one-s1-diagonal-reduction-and-degree-nine-integer-certificate.md)
及[出生一原 S2 至多 $2/3$](R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)
直接支付这些完整共同约化块。

两个 singlet 的三个块只剩一组的真空源，桥为零；
若剩余组权为 $c>0$，则 $C_1=2c^2,C_2=c^4$，
所以 S1 差为 $3c^4>0$，没有低 S2 源。
因此唯一未由旧结果支付的块正是三个长度二串的
同一个三维上源和二维低源。所有重数均保留，上、下分别合为九维和五维。

## 3. 原完整计数核、源度量和真实桥

以下只在上述唯一共同约化块内工作。
聚合占据为
$$
I=(i,j,k)\in\{0,1,2\}^3,\qquad
p_I=\binom2i\binom2j\binom2k x^iy^j.
$$
聚合系数的实际范数为 $\sum_I|g_I|^2/p_I$。
在该坐标中，下降是 $\partial_X+\partial_Y+\partial_Z$。
完整除阶下降的列是
$$
(v_I)_O=\prod_{\nu=1}^3\binom{I_\nu}{O_\nu},
$$
因此完整物理核准确为
$$
\mathcal F_{r,j}=\sum_{\substack{I\in\{0,1,2\}^3\\|I|=r+j}}
 p_Iv_Iv_I^* .
\tag{3.1}
$$
所有合法输入都在求和中，没有只留某条上升塔。

在完整三维低层、六维上层中分别取 primitive 系数列
$$
E_1=(X-Z,\ Y-Z),
$$
$$
E_2=((X-Z)^2,\ (X-Z)(Y-Z),\ (Y-Z)^2).
\tag{3.2}
$$
这些列分别穷尽相应 primitive 核。令
$$
U_0=E_2^*P_2^{-1}E_2,\qquad
\Lambda_j=E_1^*\mathcal F_{1,j}^{-1}E_1,\quad j=0,1,2,3,
\tag{3.3}
$$
其中 $P_r=\operatorname{diag}(p_I:|I|=r)$，$\mathcal F_{r,0}=P_r$。
所有非零高度先对完整三维低核取逆，再压到二维源，
从未用压缩后的普通逆替换完整 MP。

真实三次下降变成 $x\partial_X+y\partial_Y+\partial_Z$。
它的上下源坐标与再到真空的坐标准确为
$$
B_0=
\begin{pmatrix}
2(x-1)&y-1&0\\
0&x-1&2(y-1)
\end{pmatrix},
$$
$$
Y_0=2\bigl((x-1)^2,\ (x-1)(y-1),\ (y-1)^2\bigr).
\tag{3.4}
$$
这些是作用在源列上的实际映射；后续每个逆源度量都保留，
不是把非正交坐标中的普通转置当作物理伴随。

## 4. 保留深塔的 S1 与完整双交叉 S2

置 $S=2x+2y+2$，
$$
\widehat H=E_2^*P_2^{-1}
 \operatorname{diag}\bigl(S-2(ix+jy+k)\bigr)E_2,
$$
$$
\widehat F_2=E_2^*P_2^{-1}\mathcal F_{2,2}P_2^{-1}E_2,
\quad
M=B_0^*\Lambda_2B_0,\quad
N=B_0^*\Lambda_2\Lambda_3^{-1}\Lambda_2B_0.
$$
真空第四阶 $e_4=\sum_{|I|=4}p_I$ 严格正。
[R288 完整三塔身份](R288-appendix-general-birth-three-tower-s1-schur-cancellation.md) §6 给
$$
\boxed{
\mathcal E_1=
\widehat H U_0^{-1}\widehat H-\widehat F_2
-MU_0^{-1}M+2N+\frac{Y_0^*Y_0}{4e_4}.
}
\tag{4.1}
$$
它是原 S1 差在同一个三维物理源上的二次型。
末项是实际连续两次三次桥的真空塔，不能删除。
$\widehat F_2$ 是完整第二物理 Gram 的直接压缩，
不是 $G_2^{-1}$。

同一原两塔身份还给
$$
C=\widehat H-M=U_0H_1^{-1}U_0>0,\qquad
H_1=E_2^*\mathcal F_{2,1}^{-1}E_2.
$$
令
$$
Y=U_0^{-1}B_0^*\Lambda_2,\qquad
Z=B_0^*\Lambda_2\Lambda_3^{-1}\Lambda_2,\qquad
D=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1.
$$
则同一二维低源的 S2 缺陷准确是
$$
\boxed{
\mathcal E_2
=D-\frac14(CY+Z)^*C^{-1}(CY+Z).
}
\tag{4.2}
$$
$C^{-1}$ 在整个三维上源中取，
两个交叉项保留于同一个平方中。
式 (4.1)–(4.2) 没有替换任意试源或使用迹上界。

## 5. 覆盖整个正权域的精确正系数证明

三个二位组可物理酉置换，全部权可共同缩放，
故可令 $x\ge y\ge1$，并准确代入
$$
x=1+U+V,\qquad y=1+V,\qquad U,V\ge0.
\tag{5.1}
$$
整个闭象限都对应严格正的实际权。
原完整核、源度量和全部所需压缩 Gram 在此严格正定。
所有约分后的分母都是这些已知非零因子之积的约因子，
故在连通象限中不变号，可在 $(U,V)=(0,0)$ 准确定号。

源码从 (3.1)–(3.4) 直接重建两式，
逐项以有理多项式核对原 primitive 方程和真实三次桥，
对每个实际逆完整乘回，再构造全部五个前导主子式。
准确定号后的分子结果如下：

| 原缺陷 | 前导阶 | 分子次数 | 分子非零项 | 负系数 | 分母次数 | 分母项 | 分子常数项 |
|---|---:|---:|---:|---:|---:|---:|---:|
| S1 | $1$ | $20$ | $210$ | $0$ | $18$ | $169$ | $1944000$ |
| S1 | $2$ | $22$ | $261$ | $0$ | $19$ | $189$ | $5832000$ |
| S1 | $3$ | $19$ | $200$ | $0$ | $18$ | $162$ | $29160000$ |
| S2 | $1$ | $39$ | $742$ | $0$ | $39$ | $742$ | $5832000000000$ |
| S2 | $2$ | $45$ | $1003$ | $0$ | $46$ | $1037$ | $1093500000000000$ |

所以每个分子在 $U,V\ge0$ 上严格正，
包括重复组权 $U=0$ 或 $V=0$ 的全部边界。
Sylvester 判据直接给
$$
\mathcal E_1>0,\qquad\mathcal E_2>0 .
\tag{5.2}
$$
这不是从内点的非严格极限推重复权的严格性。

按源码的完整有理系数规范，
五个分子 SHA-256 依表格顺序为：

- 283476750d69d9f82c5abb29541d320ba4afaa78507f3ca94fbf933bd0dd223d
- 8f00537e5c5c0c0ae959bb0b72c1b3587e0784a5241d0e4affebea282d65d63d
- f1e1b32878e739e04e49128eedd2db4342d9b415c1d64697483e0396bfd330f0
- 9f75b8cffa77959af76023e6e0614e344344abb395276fe7923adfa2da03952e
- 8b25ecdc95b3fc565b73293d36a77886f19c1e2b8352acb7be17d339b274cfc3

本证明由可读源码和确定的原有限输入完全恢复；
不另保存展开矩阵、编码数据或可重算参数文件。

## 6. 唯一实际执行与整源合并

唯一首次实际执行是 run 46063673245、job 140723733730，
原提交 80a051c1dc1b4556974d5e06ad0a544e64ed83ff。
源自身资源界为 180 秒、4 GiB；实际进程
0.231146555 秒、最大 RSS 41652 KiB、退出码零。
S1 全三项和 S2 全两项都完整返回，
最终分别为 S1_all_passed=true、S2_all_passed=true。
原数学完成事件在 0.163731998 秒出现。

源码 SHA-256：
4678824d9b0d2c049b15c85b2daa7a165288fa70efa472791a116142a31df617。

原标准输出为 3352 字节，SHA-256：
843a76ea669d97adcd7f213fb9536ab943334d9ecfe46baa374c592cc90b0921。

上述状态用于定位已实际发生的完整代数证明；
数学通过来自 §5 的全部系数及原度量身份，
不来自外层绿色或单一退出码。

把 (5.2) 与 §2 的三个出生一块及三个真空块作实际正交直和，
得到原完整九维/五维上的 (1.1)，证明定理 1。

## 7. 同一原 R275 返回与十四维首末边

把任意 $a>0$ 视为新增位，旧六位正是已付的定理 1。
同一旧低出生一的内部第二边由[六位完整内部 half](R271-appendix-six-site-internal-half-complete-ordered-difference-certificate.md)支付：
$$
L_2L_3^{-1}L_2<\frac12L_1.
$$
因此 R275 §4 的原三块平方分解中，
S2 块严格正，S1 和第二低边均正；
新增位平方 $a^2>0$ 的指定同余可逆。
原 $P(a^2)>0$，且 $M(a^2)=P(a^2)+W_{a^2}W_{a^2}^*>0$。
经过同一个真实 Schur 补和原共同源合同，
得到整个十四维新 $K_2$ 的首边严格系数一。

还可使用[已付原定量返回](R271-appendix-quantitative-one-bit-source-transfer-and-six-site-319-over-320.md)。
在固定的旧六位模型中，定义实际有限常数
$$
\varepsilon=\lambda_{\min}(C_1^{-1}FC_1^{-1})>0,
$$
$$
\kappa=\|F^{-1/2}\Delta L_3^{-1}\Delta^*F^{-1/2}\|<1,\qquad
\sigma=\|A^*G_1A+L_1L_2^{-1}L_1\|<1 .
$$
又 $0<\varepsilon\le1$。
令
$$
\alpha=\min\left\{1-\sqrt\sigma,\,
(1-\sqrt\kappa)(1-1/\sqrt2)\right\}>0,
\quad c_0(x,y)=1-\frac{\alpha\varepsilon}{2}<1 .
$$
这些常数都不依赖新增位 $a$，
该定量定理于是给首边系数 $c_0(x,y)$。

七位族对全部倒数权及共同缩放封闭。
按[原倒数权对偶的准确相邻次序](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md) §5，
高度 $h=3$ 的末边可取 $c_0(x^{-1},y^{-1})$。
因此
$$
c(x,y)=\max\{c_0(x,y),c_0(x^{-1},y^{-1})\}<1
$$
同时支付两条实际边，证明定理 2。
未把该有限参数常数冒称为所有 $x,y$ 的统一数值上界。

一般六个独立正权的完整 S1/S2、更多独立值或更高出生来源、
原无限 carry、同一 $W$ 的实际 Green 费用和 $N=M$ 仍保持未闭。
