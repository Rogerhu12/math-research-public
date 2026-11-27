# R271 附录：两对等权与两个独立权的完整联合来源及七位五权值族

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 状态：本稿全部 S1/S2 与以下七位完整首末边结论已证明。
- 唯一精确源：[原三塔与双交叉源码](../notes/2026-11-28-two-pairs-two-independent-original-joint-three-tower-8542.py)，Git blob 31fc1f24557da7073b58e67a6cda4bc50365adf6。

## 1. 整个原物理来源的两个新结论

取六位物理权
$$
b=(\sqrt x,\sqrt x,\sqrt y,\sqrt z,1,1),\qquad x,y,z>0.
$$
令 $K=\ker d\cap H_2$、$L=\ker d\cap H_1$，
原维数分别为九和五。沿用 R275 的完整最小逆 Gram
$G_j=\Gamma_{j,2}$、$L_j=\Gamma_{j,1}$，定义
$$
C_i=G_i^{-1},\qquad F=C_1^2-C_2,\qquad B=d_{b^3}|_K,
$$
$$
\Delta=(C_1B^*L_3-B^*L_2)/2,\qquad
A=(C_1B^*L_2+B^*L_2L_3^{-1}L_2)/2.
$$
所有 MP 都先在完整物理层中形成，再取原 primitive 来源；
所有伴随使用原物理内积。

**定理 1。** 对全部 $x,y,z>0$，
同一个完整九维/五维来源严格满足
$$
\boxed{
F-\Delta L_3^{-1}\Delta^*>0,\qquad
I_L-A^*G_1A-L_1L_2^{-1}L_1>0.
}
\tag{1.1}
$$
深真空塔、两个 S2 交叉项及全部非活跃块均保留。

**定理 2。** 对任意 $a,x,y,z>0$，七位权
$$
(a,\sqrt x,\sqrt x,\sqrt y,\sqrt z,1,1)
$$
的整个十四维出生二 primitive 空间，在全部两个合法内部高度严格有
$$
\boxed{\Gamma_j\Gamma_{j+1}^{-1}\Gamma_j\prec\Gamma_{j-1},
\qquad j=1,2.}
\tag{1.2}
$$
固定 $x,y,z$ 后，可以选择同一个不依赖新增位 $a$ 的常数
$c(x,y,z)<1$ 同时替代 (1.2) 右侧系数一；准确常数见 §7。
这里没有给出对全部三比率统一小于一的数值常数。

[旧 R292](R292-appendix-main-parameter-s2-and-all-two-exceptional-birth-two-first-edges.md)
已经给这个六位族的普通首边，本篇不重计。
新增的是该六位族自身的完整 S1/S2，
以及再加一位后一般五种权值的七位整源首末边。
一般七位五权值行不属于旧“两普通组加两异常位”的四值范围。
本稿也不重跑已冻结的六个独立权特征门。

## 2. 全部物理块，无遗漏低来源

两个二位等权组各有长度二对称串与出生一 singlet，
两个单独位各为长度一串。共同约化分块为：

| 二位组的 singlet 数 | 上相对出生与维数 | 下相对出生与维数 |
|---|---|---|
| $0$ | 出生二，$4$ 维 | 出生一，$3$ 维 |
| $1$，两个选择 | 出生一，各 $2$ 维 | 真空，各 $1$ 维 |
| $2$ | 真空，$1$ 维 | 无 |

一个 singlet 的块是余下四个物理位的出生一共同约化部分。
[全部正权出生一 S1](R288-appendix-birth-one-s1-diagonal-reduction-and-degree-nine-integer-certificate.md)
和[全部正权出生一 S2](R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)
已支付它们。
两个 singlet 的块只余两个不同正权的真空，桥为零；
其 $F=(y+z)^2-yz=y^2+yz+z^2>0$。

故只需支付同一个四维上源和三维低源，
其结论按真正正交直和返回全部九维/五维。
不把未约化试源或单条上升塔当作完整核。

## 3. 旧八维聚合来源的实际原式

采用 [R273 八维完整物理核](R273-appendix-eight-dimensional-aggregate-polynomial-gram.md)
的原固定来源，组容量为
$$
c=(2,1,1,2),\qquad I=(i,j,k,\ell),\qquad
p_I=\binom2i\binom2\ell x^iy^jz^k .
$$
聚合坐标的物理范数为 $\sum |g_I|^2/p_I$。
令
$$
(v_I)_O=\prod_{\nu=1}^4\binom{I_\nu}{O_\nu},\qquad
\mathcal F_{r,j}=\sum_{|I|=r+j}p_Iv_Iv_I^*.
\tag{3.1}
$$
求和保所有合法输入，各个非零高度均先在完整物理层取逆。

写 $A_0=X-J,\ B_0=Y-J,\ C_0=Z-J$。源列为
$$
E_1=(A_0,B_0,C_0),\qquad
E_2=(A_0^2,A_0B_0,A_0C_0,B_0C_0).
\tag{3.2}
$$
它们分别穷尽四维一层内的三维核及八维二层内的四维核。
令
$$
U_0=E_2^*P_2^{-1}E_2,\qquad
\Lambda_j=E_1^*\mathcal F_{1,j}^{-1}E_1,\quad j=0,1,2,3.
$$
$j=0$ 时 $\mathcal F_{1,0}=P_1$。

三次下降在此为
$x\partial_X+y\partial_Y+z\partial_Z+\partial_J$。
其真实两次来源为
$$
K_B=
\begin{pmatrix}
2(x-1)&y-1&z-1&0\\
0&x-1&0&z-1\\
0&0&x-1&y-1
\end{pmatrix},
$$
$$
K_Y=2((x-1)^2,(x-1)(y-1),(x-1)(z-1),(y-1)(z-1)).
\tag{3.3}
$$
源码在全四维/八维层逐项核 primitive 方程、
第一次桥 $d_{b^3}E_2=E_1K_B$，
以及连续第二次桥到真空的 (3.3)；
没有只检查列维数。

## 4. 新原 S1/S2 矩阵

置 $S=2x+y+z+2$，
$$
\widehat H=E_2^*P_2^{-1}
 \operatorname{diag}(S-2(ix+jy+kz+\ell))E_2,
$$
$$
\widehat F_2=E_2^*P_2^{-1}\mathcal F_{2,2}P_2^{-1}E_2,\quad
M=K_B^*\Lambda_2K_B,\quad
N=K_B^*\Lambda_2\Lambda_3^{-1}\Lambda_2K_B .
$$
原第四真空系数 $e_4=\sum_{|I|=4}p_I>0$。
[R288 全三塔身份](R288-appendix-general-birth-three-tower-s1-schur-cancellation.md) §6 准确给
$$
\mathcal E_1=
\widehat H U_0^{-1}\widehat H-\widehat F_2
-MU_0^{-1}M+2N+K_Y^*K_Y/(4e_4).
\tag{4.1}
$$
它是原 S1 在同一四维物理源上的二次型。
末项是真正深塔，$U_0^{-1}$ 是同一源度量，
$\widehat F_2$ 不是 $G_2^{-1}$。

同一原两塔身份给
$$
C=\widehat H-M=U_0H_1^{-1}U_0>0,\qquad
H_1=E_2^*\mathcal F_{2,1}^{-1}E_2.
$$
定义
$$
Y=U_0^{-1}K_B^*\Lambda_2,\quad
Z=K_B^*\Lambda_2\Lambda_3^{-1}\Lambda_2,\quad
D=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1 .
$$
原三维低源上的 S2 缺陷准确为
$$
\mathcal E_2=D-\frac14(CY+Z)^*C^{-1}(CY+Z).
\tag{4.2}
$$
这里在完整四维上源取 $C^{-1}$，两项 cross 全保。
并没有从旧普通首边推新联合来源。

## 5. 全参数正系数证明与重复权边界

交换两个二位组并共同缩放，可以取 $x\ge1$；
再交换两个单独位，可以取 $y\ge z>0$。
因此以下规范覆盖整个原正权族：
$$
x=1+U,\qquad y=V+W,\qquad z=W,
\qquad U,V\ge0,\quad W>0.
\tag{5.1}
$$
没有额外假定两个独立权也大于一。

所有完整物理层 Gram、源度量和所需压缩 Gram 在此连通域严格正定。
有理生成链中的分母是这些非零物理因子之积；
约分后的分母也不消失，故用 $(U,V,W)=(0,0,1)$ 准确定号。

唯一源码从 §3 的原有限求和直接生成 §4 两式，
逐项核对完整 primitive 方程、两次真实三次桥，
并对每个实际逆完整乘回。
全部七个前导主子式已经实际计算。
定号后结果如下：

| 原缺陷 | 阶数 | 分子次数 | 分子项数 | 负系数 | 分母次数 | 分母项数 | 正 $W$ 轴项数 | 一个严格正轴项 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| S1 | $1$ | $24$ | $1233$ | $0$ | $22$ | $799$ | $11$ | $11664W^2$ |
| S1 | $2$ | $27$ | $2042$ | $0$ | $24$ | $1038$ | $14$ | $34992W^2$ |
| S1 | $3$ | $30$ | $2409$ | $0$ | $26$ | $1100$ | $14$ | $104976W^2$ |
| S1 | $4$ | $28$ | $2565$ | $0$ | $26$ | $1153$ | $16$ | $1049760W^2$ |
| S2 | $1$ | $50$ | $10614$ | $0$ | $50$ | $10614$ | $27$ | $120932352W$ |
| S2 | $2$ | $58$ | $19071$ | $0$ | $59$ | $19420$ | $34$ | $10883911680W$ |
| S2 | $3$ | $58$ | $19071$ | $0$ | $60$ | $19420$ | $34$ | $6802444800W$ |

每个分子的全部系数非负，所列单个 $W$ 轴项已在每个 $W>0$ 上严格正。
故 $U=0$ 或 $V=0$ 的重复权边界同样严格，
不从内部极限免费把半正提升为严格正。
$U=V=W=0$ 对应零权，不是本定理的允许点，也没有被用作定号点。

Sylvester 判据遂给
$$
\mathcal E_1>0,\qquad \mathcal E_2>0
\tag{5.2}
$$
于同一四维上源、三维低源。
将 (5.2) 与 §2 的两个出生一块及真空块正交合并，
得到整个九维/五维上的 (1.1)。

按源码的有理系数与升幂元组排序规范，
七个完整分子 SHA-256 依表格顺序为：

- 2dd7a2ce2563080036b189dcf72d1a563195b741c6802fbb1487102c74264d21
- b5643e028f2fa2e13d9ff37b2a119555cbbd1b9aebed25affcf0e83865b76542
- 2779de84be59ad855622c7693199c822480a5fad89497abc02f4d266485932df
- 7b57b443658cc4584c504ac60647fe7ec644223e4a586fc548d5899ca5db862c
- e8ead920e8c806ffb305219988fd43832cbb010140c6c5088e14eaf8b1e081e1
- ea35501b229fcd006dda54da3869870f71770759db246431df8ed729ba864a35
- 538e43dfa77168f856a8b69094701fc4084969bcfddee56a42cee4ba8318bf27

## 6. 唯一实际执行与保存范围

唯一首次运行是 run 46066453231、job 140732835842，
固定源码提交 3dc85411af1ef916e34ed9501ac1a4672bfe4b81。
源自身限额 180 秒、4 GiB；
实际进程 20.882163528 秒、最大 RSS 174260 KiB、退出码零。

完整原来源和两次桥在 0.003474085 秒返回；
所有完整低核及源度量逆已逐一乘回。
S1 的四项全部在 1.044721771 秒之前返回；
S2 最后第三项在 20.814239530 秒返回。
20.815006624 秒的最终事件明确给
S1_all_passed=true、S2_all_passed=true、all_passed=true。
本证明用的是七个完整分子及原物理身份，
并非单凭外层绿色或某个中间矩阵已形成。

源码 SHA-256：
15190e4cfa161958d8313708f427327d53cbb0593451c46023670c4ce20c7312。

标准输出只有 4826 字节，SHA-256：
8d5aa24130da41c740dea8508f0c4e9ac3ace3a8e1c143a606cfbb6a15cfeae4。

本稿仅保存原紧凑定义、可读源码和上述小数学回执；
不另保存可重算展开矩阵、参数文件、数据片或编码载荷。

## 7. 返回原十四维七位首末边及同新增权无关的常数

把 $a>0$ 作为新增位。旧六位模型的上 S1 和同低 S2 已由定理 1 支付；
同一个旧低出生一的真正内部第二边由
[完整六位内部 half](R271-appendix-six-site-internal-half-complete-ordered-difference-certificate.md)
给出：
$$
L_2L_3^{-1}L_2<\frac12L_1 .
$$
这不是将其首边或末边改作第二边。

于是 [R275 原三块平方分解](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md)
§4 的全部来源都正定，新增位平方 $a^2$ 所需同余可逆。
原 $P(a^2)>0$，并且
$M(a^2)=P(a^2)+W_{a^2}W_{a^2}^*>0$。
经过同一个真实 Schur 补和原共同来源合同，
给出整个十四维新出生二的严格首边。

还可由[已付的原定量返回](R271-appendix-quantitative-one-bit-source-transfer-and-six-site-319-over-320.md)
给明确的实际有限参数。对固定的旧六位模型，定义
$$
\varepsilon=\lambda_{\min}(C_1^{-1}FC_1^{-1})\in(0,1],
$$
$$
\kappa=\|F^{-1/2}\Delta L_3^{-1}\Delta^*F^{-1/2}\|<1,\qquad
\sigma=\|A^*G_1A+L_1L_2^{-1}L_1\|<1.
$$
正性与严格界均在整个九维/五维来源上取。
置
$$
\alpha=\min\{1-\sqrt\sigma,\,
 (1-\sqrt\kappa)(1-1/\sqrt2)\}>0,
$$
$$
c_0(x,y,z)=1-\alpha\varepsilon/2<1.
$$
这个 $c_0$ 不依赖新增位 $a$，并给上述首边的相同定量系数。

全部倒数权仍属于同一个七位族，三个旧比率变为
$(x^{-1},y^{-1},z^{-1})$。
按[倒数权的准确相邻次序](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md) §5，
高度 $h=3$ 的另一条内部边由倒数模型首边返回，
不使用未经证明的自由倒序。
所以
$$
\boxed{
c(x,y,z)=
\max\{c_0(x,y,z),c_0(x^{-1},y^{-1},z^{-1})\}<1
}
$$
同时支付 (1.2) 的两条实际边，证明定理 2。

一般六个独立正权的全部 S1/S2、更高出生联合来源、
原无限 carry 的可求和物理费用、同一 $W$ 的 Green 来源和 $N=M$
仍未由这些有限结论完成。
