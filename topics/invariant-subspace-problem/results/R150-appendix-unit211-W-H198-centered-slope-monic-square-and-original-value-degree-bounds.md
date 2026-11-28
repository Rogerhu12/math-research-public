# R150：H198 补图的无新逆中心坐标、首一平方与原值 λ 次数界

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 完整代数结论

沿已刊 [N1 的 H198 坐标](R150-appendix-unit211-W-N1-H198-weight-curve-and-two-generator-monic-square.md)，在 $R=A_W[H198^{-1}][\lambda]$ 中写

$$
p_0=A\lambda^2+B\lambda+C,\quad
p_1=a\lambda+b,\quad p_2=c\lambda+d,\quad
\Delta=ad-bc,\quad z=ax+cy.
\tag{1}
$$

$A,B,C,a,b,c,d$ 全是纯权系数；不是原物理权的同名符号。原 N1 余式是 $n=p_0+p_1x+p_2y$。定义

$$
w=z+A\lambda+B.
\tag{2}
$$

这是 R 上的可逆多项式平移，无新分母，逆为 $z=w-A\lambda-B$。由此前完整 N1 坐标逆，模 n 直接得到

$$
x=\frac{(c\lambda+d)w-Ad\lambda+cC-dB}{\Delta},
\tag{3}
$$

$$
y=\frac{-(a\lambda+b)w+Ab\lambda+bB-aC}{\Delta}.
\tag{4}
$$

把 (2) 代入旧逆式并展开即可逐项证明 (3)–(4)：两项 $\lambda^2$ 精确相消。两个式现在对 lambda 均至多一次；其系数对 w 至多一次。不要求 a、b、c、d 分别非零或可逆。

## 2. 首一平方的两个系数均至多 λ 二次

此前三条原 mean 的真实平方约化为

$$
z^2\equiv r_0+r_1x+r_2y\pmod{I_{\rm mean}},
\quad
\deg_\lambda r_0\le2,\quad
\deg_\lambda r_1,\deg_\lambda r_2\le1.
\tag{5}
$$

次数界来自已实际逐系数检查的三条均值规则：替换 $x^2,xy,y^2$ 不增加 $\lambda,x,y$ 总次数。全权分母不含 lambda。

令 $\phi=A\lambda+B$，并把 (3)–(4) 写作 $x=X_1w+X_0,y=Y_1w+Y_0$；四个 X/Y 系数的 lambda 次数均至多 1。把 (5) 改写为

$$
q_w=w^2+\gamma_1(\lambda)w+\gamma_0(\lambda),
$$

$$
\gamma_1=-2\phi-r_1X_1-r_2Y_1,\qquad
\gamma_0=\phi^2-r_0-r_1X_0-r_2Y_0.
\tag{6}
$$

所以

$$
\boxed{\deg_\lambda\gamma_0\le2,\quad
\deg_\lambda\gamma_1\le2.}
\tag{7}
$$

式 (6) 就是已付 $q_z(z)$ 在 $z=w-\phi$ 下的像，故保同一原 I4 身份。旧 z 坐标中平方常数项的 lambda 三次部分在这里必然精确相消，不是根据一次采样预测。整个 H198 零支仍在补图之外保留；(2) 没有把它支付为全域单位。

明确环境 $R[w]/(q_w)$ 自由二维；其任何原方程商均不由此获得自由性。此前精确十五行二列或新的十行二列均可作同一平移，原理想与规范点完全不变。

## 3. 全部原值先降次后的统一界

给 $\lambda,x,y$ 总次数 1，给纯权系数次数 0。若一个完整原多项式 P 的总次数至多 d，按同一三条原均值规则降成

$$
P\equiv r_0+r_1x+r_2y\pmod{I_{\rm mean}},
$$

则归纳有 $\deg_\lambda r_0\le d$、$\deg_\lambda r_1,r_2\le d-1$。代入 (3)–(4) 后，两个 w 坐标系数均至多 lambda d 次。这里只用实际原理想重写，不把三生成元当自由代数或假设其裸矩阵交换。

在已刊完整原值定义中，$q_{T,4}$ 的总次数至多 4，$R_6=MK^2-4m^2D^3$ 至多 6；$N_{\rm low},P_{\rm low},V_{\rm low}$ 均至多 5。最后三条的计数直接来自 D 二次、K 三次、个别 N/P 的原 Gram 三次和整个 $N_4(V_0+sV_1)$ 的二次型展开。因此先原均值降次、再一次换基后的两列行满足：

| 完整原值 | 两个 w 系数的 lambda 次数上界 |
|---|---:|
| $q_{T,4}$ | 4 |
| $R_6$ | 6 |
| $N_{\rm low}$ | 5 |
| $P_{\rm low}$ | 5 |
| $V_{\rm low}$ | 5 |

这也给已经定义的新固定 cofactor 的先验界：$R_6,V_{\rm low}$ 配对至多 11 次，$N_{\rm low},P_{\rm low}$ 配对至多 10 次。

## 4. 此平移不产生可重复运行的旧目标

对固定两行的 z 系数矩阵，平移右乘

$$
U=\begin{pmatrix}1&0\\-\phi&1\end{pmatrix},
\qquad\det U=1.
$$

故其原 determinant 完全不变；两个消去第二列的乘子也保持为 $(B_1,-A_1)$。约去这两个实际乘子的共同因子以后，常数目标同样不变。另行只用纯权单位作行归一，也不改变 lambda 次数界。

因此 (2) 可用于下一项真正新的低次原输入，却不能作为重算旧已成或冻结 cofactor、Norm、结果式的理由。本稿没有执行新的计算，也不声称新的原单位、有限投影或分支排除。现有冻结的全原二十行源保持不动；上述结论是对其原定义的精确代数推论。
