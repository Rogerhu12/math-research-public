# R271 附录：低端新增次数的真实 Schur 费用与有限维异常源

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。
状态：已核验的部分相邻结论；给出部分相邻估计及准确剩余矩阵，不宣称一般相邻系数一或权无关全局常数。

## 1. 扣除已有范围与固定模型

[R239 一参数稿](R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)
§10 已给全部相对出生的完整多重仿射 Moore–Penrose 最小化，
包括每阶非法状态约束、原始源 Gram 和两个端点；其 §10.4
已付所有合法中段的相邻粗界。其 §9 还已付倒数第二出生的全部端点。
本文仅处理该 §10.4 未直接覆盖的低边，保留逐阶新释放的齐次次数。

取 $q\ge2$ 个正头权 $a_i$ 与 $L\ge q$ 个单位权池位，仍为同一个
Boolean 删除算子
$$
D=\sum_{i=1}^q a_iE_i+D_{\rm w}.
$$
置
$$
A_R=\prod_{i\in R}a_i^2,\qquad a_R=\prod_{i\in R}a_i,\qquad
2\le\delta\le q,\quad s=q-\delta,\quad h=L-q+2\delta.
$$
源坐标 $x=(x_I)_{|I|=\delta}$ 对应
$$
f_x(X)=\sum_{|I|=\delta}x_I X_I,\qquad X_I=\prod_{i\in I}X_i.
$$
源嵌入及完整逆沿用所引 §10：
$$
H_k=\mathcal E_\delta^*
\left(\frac{D^k(D^*)^k}{(k!)^2}\Big|_{\mathcal H_s}\right)^{-1}
\mathcal E_\delta .
$$
这是先取完整逆再压原始核的实际 Gram；源基一般非正交。

固定
$$
1\le n<\delta,\qquad j=\delta-n-1\in\{0,\ldots,\delta-2\}.
\tag{1.1}
$$
由于 $L\ge q$，这三个相邻阶均合法，且不同时碰到高端约束。

## 2. 三个相邻可行空间

记 $\mathcal P_{[b,c]}$ 为齐次次数在 $b,\ldots,c$ 之间的多重仿射
多项式空间；空区间给零空间。R239 §10 的真实非法状态约束在此准确化为
$$
\begin{array}{c|c|c}
\text{阶} & \text{可行多项式} & \text{合法状态}\\ \hline
n-1 & f_x+\mathcal P_{[j+2,\delta-1]} & |R|\ge j+2\\
n & f_x+\mathcal P_{[j+1,\delta-1]} & |R|\ge j+1\\
n+1 & f_x+\mathcal P_{[j,\delta-1]} & |R|\ge j .
\end{array}
\tag{2.1}
$$
相应权准确为
$$
w_-(R)=\frac{A_R}{\binom L{|R|-j-2}},\quad
w(R)=\frac{A_R}{\binom L{|R|-j-1}},\quad
w_+(R)=\frac{A_R}{\binom L{|R|-j}} .
\tag{2.2}
$$
每个权只在其合法状态上使用。

定义辅助正 Gram $B$：在 $n+1$ 阶的真实权 $w_+$ 下，仅禁止新释放的
$j$ 次项，即
$$
x^*Bx=
\min_{P\in\mathcal P_{[j+1,\delta-1]}}
\sum_{|R|\ge j} w_+(R)|f_x(R)+P(R)|^2.
\tag{2.3}
$$
其中 $|R|=j$ 的函数值自动为零。$B$ 是同一原像空间中多加该线性约束后的
最小费用；实际 $H_{n+1}$ 还须继续消去 $j$ 次项，不能把二者混同。

## 3. 已支付的正基线

在共同合法状态中，
$$
\frac{w(R)}{w_-(R)}
=\frac{|R|-j-1}{L-|R|+j+2}
\le M:=\frac{q-j-1}{L-q+j+2},
\tag{3.1}
$$
$$
\frac{w_+(R)}{w(R)}
=\frac{|R|-j}{L-|R|+j+1}
\ge\frac1L.
\tag{3.2}
$$

取 $H_{n-1}$ 的真实极小多项式作为 $H_n$ 的试探代表。
它在新状态 $|R|=j+1$ 仍为零，故 (3.1) 给
$$
H_n\preceq M H_{n-1}.
\tag{3.3}
$$
另一方面，$B$ 与 $H_n$ 具有同一可行低次参数空间，
且两者的 $|R|=j$ 项为零；对全部这些参数逐项使用 (3.2) 后取最小值，得到
$$
B\succeq L^{-1}H_n.
\tag{3.4}
$$
因此完整取逆和合同给出真正的基线
$$
\boxed{
H_nB^{-1}H_n\preceq C_0H_{n-1},\qquad
C_0=\frac{L(q-j-1)}{L-q+j+2}
\le\frac{q(q-j-1)}{j+2}.
}
\tag{3.5}
$$
最后一个不等式由 $L\ge q$ 及 $j\le q-2$ 直接交叉相乘得到。
这里没有把不同权下的极小代表作未经证明的替换。

## 4. 新释放次数的完整 Schur 补

在有限 Hilbert 空间
$$
\mathscr H_+=\ell^2\bigl(\{R:|R|\ge j\},w_+\bigr)
$$
中按点值嵌入多项式。记
$$
\mathscr N=\mathcal P_{[j+1,\delta-1]},\qquad P_{\mathscr N}
\text{ 为该实际权下的正交投影}.
$$
令 $F x=(I-P_{\mathscr N})f_x$。则 $F^*F=B$。

对新次数采用实际头权归一的基：
$$
K y=\sum_{|I|=j}\frac{y_I}{a_I}X_I,\qquad
V=(I-P_{\mathscr N})K,
\qquad
T=V^*V,\quad U=F^*V.
\tag{4.1}
$$
当 $j=0$ 时只有常数基 $1$。最低次到最高次的布尔值三角反演保证
$F$ 与 $V$ 的全部列合起来独立：若它们的线性组合属于 $\mathscr N$，
所得多项式在所有 $|R|\ge j$ 状态为零；在更小状态也自动为零，
所以全部多重仿射系数为零。因此
$$
\begin{pmatrix}B&U\\U^*&T\end{pmatrix}>0.
$$

现在对全部新增参数真正最小化，而不是仅取一个试探值，得到
$$
\boxed{H_{n+1}=B-UT^{-1}U^*.}
\tag{4.2}
$$
再记
$$
S=T-U^*B^{-1}U.
\tag{4.3}
$$
它也有一个直接的完整投影解释：
$$
y^*Sy=
\min_{P\in\mathcal P_{[j+1,\delta]}}
\|Ky-P\|_{\mathscr H_+}^2.
\tag{4.4}
$$
在每一个最低合法状态 $R$、$|R|=j$，右侧的 $P(R)=0$，
$Ky(R)=y_R/a_R$，而 $w_+(R)=A_R$。
仅这些真实状态已经付出 $\sum_{|R|=j}|y_R|^2$。故有准确下界
$$
\boxed{S\succeq I.}
\tag{4.5}
$$
这不是假定一个未知最小逆有统一下界，而是由新出现的最低物理状态逐项支付。

Woodbury 恒等式在已证严格正矩阵上合法，给
$$
\boxed{
H_nH_{n+1}^{-1}H_n
=H_nB^{-1}H_n+Z S^{-1}Z^*,
\qquad Z=H_nB^{-1}U.
}
\tag{4.6}
$$
因此所有未付费用均准确落在 $Z$ 的像中；其秩至多
$$
m_j=\binom qj.
$$

## 5. 有限维异常源与准确剩余判据

合并 (3.5)、(4.5)、(4.6)：
$$
\boxed{
H_nH_{n+1}^{-1}H_n
\preceq C_0 H_{n-1}+Z S^{-1}Z^*
\preceq C_0 H_{n-1}+ZZ^*.
}
\tag{5.1}
$$
特别，对明确的源坐标子空间
$$
\mathcal V=\ker Z^*,\qquad
\operatorname{codim}\mathcal V\le\binom qj,
$$
实际相邻费用满足
$$
x^*H_nH_{n+1}^{-1}H_nx
\le C_0\,x^*H_{n-1}x
\qquad(x\in\mathcal V).
\tag{5.2}
$$
由有限维极小极大原理，一般化特征值对
$(H_nH_{n+1}^{-1}H_n,H_{n-1})$
至多有 $\binom qj$ 个特征值严格超过 $C_0$，按重数计。

若要证明全部源的某个指定常数 $C>C_0$，定义已确定严格正的
$$
\Delta_C=C H_{n-1}-H_nB^{-1}H_n
\succeq(C-C_0)H_{n-1}>0.
$$
真正剩余条件准确为
$$
\boxed{
H_nH_{n+1}^{-1}H_n\preceq C H_{n-1}
\iff
Z^*\Delta_C^{-1}Z\preceq S.
}
\tag{5.3}
$$
证明是将 $ZS^{-1}Z^*\preceq\Delta_C$ 作两侧正平方根合同，
再使用矩形算子 $R$ 的 $RR^*\preceq I\iff R^*R\preceq I$。
(5.3) 的右侧大小只有 $\binom qj$，但其上界仍须实际证明。

最后一个低边 $n=\delta-1$ 恰有 $j=0$，因而只有一个新增常数：
$S$ 是实正标量且 $S\ge1$，(5.3) 是单个标量不等式。
此时
$$
C_0=\frac{L(q-1)}{L-q+2}\le\frac{q(q-1)}2.
\tag{5.4}
$$
最小的新非平凡例 $q=4,\delta=2,n=1$ 有六维真实源；
对所有 $L\ge4$ 及全部正头权，至多一个相邻一般化特征值超过
$$
C_0=\frac{3L}{L-2}\le6.
$$
其余源方向的估计已由 (5.2) 支付；例外方向的费用没有被省去。

全部公式使用同一非正交源基。实际 $\Gamma_k$ 的坐标是 $H_0^{-1}H_k$，
其复合及源内积准确消去 $H_0$ 后，正好回到上述 Gram 序。
因此这些结论是实际 primitive 压缩的结论。

## 6. 直接中间 Cauchy–Schwarz 替换为什么不成立

下面给同一真实模型内的有理数校准，保留此前推导中容易漏掉的误差。
取
$$
q=L=4,\qquad a_i=1,\qquad\delta=2,\ n=1,\qquad
f(X)=\sum_{i<j}X_iX_j.
$$
在秩 $r=|R|$ 上，$f(R)=r(r-1)/2$。置 $R_1(X)=\sum_iX_i$。
全对称性及正交平均保证此源的各线性极小代表是 $f+cR_1$。

中间阶的秩总质量依次为
$$
r=1,2,3,4:\qquad 4,\ \frac32,\ \frac23,\ \frac14.
$$
所以
$$
\langle R_1,R_1\rangle_1=20,\qquad
\langle R_1,f\rangle_1=15,\qquad
\langle f,f\rangle_1=\frac{33}2.
$$
真实中间极小代表为
$$
g_1=f-\frac34R_1,\qquad H_1[f]=\frac{21}4.
$$
下一阶禁止常数的 $B$ 使用秩 $r=0,\ldots,4$ 各为一的总质量，
故其极小代表为
$$
b_2=f-\frac76R_1,\qquad B[f]=\frac{31}6.
$$
然而实际中间交叉项是
$$
\boxed{\langle f,b_2\rangle_1=-1\ne H_1[f]=\frac{21}4.}
\tag{6.1}
$$
准确的差项为
$$
\langle f-g_1,b_2-g_1\rangle_1=-\frac{25}4.
$$
这里 $g_1$ 在中间权下正交全部线性，但 $b_2$ 只在下一阶权下有该正交性。
因此不能先用前一阶代表替换 $g_1$，再对下一阶极小代表直接作点态
$w^2\le w_-w_+$ 的 Cauchy–Schwarz，而把所得交叉项认作 $H_1$。

这不是实际相邻系数一的反例：本例仍是等权模型，
$H_0[f]=21$、真实 $H_2[f]=7/2$，
原相邻比为 $3/8$。它只准确否定上述不合法的代表替换。

## 7. 保留的缺口

本文新增的是低端层变化的显式有限秩费用、其最低状态下界及已付的
余维估计。原先的中段结论没有被重复记为新结果。
在异常源上，(5.3) 仍是未付条件；目前没有由 $S\succeq I$ 推出
$Z$ 的权无关统一上界，也没有推出与出生、头数无关的普遍相邻常数。

这里没有使用头相似条件数。它也没有把有限池固定块替换为原连续尾，
或把一个低维异常空间免费排除于原窄返回源之外。原 $N=M$ 主问题及
真实返回源的异常费用仍须继续处理。
