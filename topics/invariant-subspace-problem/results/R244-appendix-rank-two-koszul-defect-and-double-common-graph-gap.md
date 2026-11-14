# R244 后续附录：秩二共同预解缺陷的有界链与交替型商

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明的中间结构结论。本文把秩二真见证的共同域缺陷放到一个完全有界的两步链中，并证明其非零中间约化商必为无限维、没有循环向量，并迫共同正则图、共同最小图与最大交域之间两级商均无限维。它没有把这个 $H^{(2)}$ 旗子商认作原 $H$，也没有据此排除真见证。

## 0. 既有结论的扣除

已对照 R2、R58、R88、R169、R184 的完整相关源，以及 R53/R212/R233 的中央等向图段落：

- R2 讨论预解向量生成的几乎不变半空间，不含本稿的有界二元链。
- R58 从一个指定等向临界核构造闭平方零模映射；其双线性型是对称型，并非本稿 $J^2=-I$ 的中间商。
- R88 §10 提供全部有界交换子的原 $C$ 对称性，本稿直接使用，不重新登记为新结果。
- R169 §§2--5 和 R184 §§7--8 已在另有快 Bézout / 强主理想证书时证明约化 Koszul 正合及原参数核心。本稿不重复这个正合定理，也不预设本稿两个分母有该证书。
- R53/R212 的等向核及中央商由具体核方程产生；中央共轭的平方为 $I$。R233 处理其非对角闭商域，不含这里的反对称商结构。

本稿保留的新增接口是：任意两个原 $C$ 对称交换分母的中间缺陷具有显式反线性等距 $J^2=-I$；真秩二正矩给其非零类；由共同最小图的循环性进一步迫两个严格图缺口。

## 1. 实际设置与有界链

仍记 $\mathfrak C=A'$，每个 $\mathfrak C$ 元满足 $FC=CF^*$；$C$ 是原 Haar 共轭，内积对第一变量线性。

给任意相互交换的 $R_1,R_2\in\mathfrak C$，定义
$$
d_0:H\longrightarrow H\oplus H,\qquad
d_0x=(R_2x,R_1x),
$$
$$
d_1:H\oplus H\longrightarrow H,\qquad
d_1(x_1,x_2)=R_1x_1-R_2x_2.
\tag{1.1}
$$
交换性准确给 $d_1d_0=0$。置
$$
N=\overline{\operatorname{Ran}d_0},\qquad
K=\ker d_1,\qquad
Q=K\ominus N.
\tag{1.2}
$$
这是二元 Koszul 链的中间约化商的正交实现；本稿只用 (1.1)--(1.2) 的显式公式，不引用任何抽象精确性。

$K,N$ 均为 $A^{(2)}$ 不变闭空间，且 $N\subset K$。诱导的有界算子为
$$
T=P_QA^{(2)}|_Q.
\tag{1.3}
$$
一般 $Q$ 本身不被 $A^{(2)}$ 保持；始终保留这个压缩。

## 2. 交替反线性等距给完整商对称

定义反线性等距
$$
J(x_1,x_2)=(Cx_2,-Cx_1).
\tag{2.1}
$$
则 $J^2=-I$。由各 $R_i$ 的 $C$ 对称性，
$$
Jd_0x=(R_1^*Cx,-R_2^*Cx)=d_1^*Cx.
$$
取闭包得到
$$
JN=\overline{\operatorname{Ran}d_1^*}=K^\perp.
\tag{2.2}
$$
因为 $J$ 是满反线性等距，它保持正交补，故
$$
JK=N^\perp,\qquad
\boxed{JQ=Q.}
\tag{2.3}
$$
所以 $J$ 与 $P_Q$ 交换，这不是未经核验地把原共轭 $C^{(2)}$ 下传给商。

原 $A$ 的 $C$ 对称性给
$JA^{(2)}=(A^*)^{(2)}J$。结合 (2.3)，在 $Q$ 上有
$$
\boxed{JT=T^*J.}
\tag{2.4}
$$
这里 $T^*=P_Q(A^*)^{(2)}|_Q$ 是压缩的通常伴随。

在 $Q$ 上定义连续双线性型
$$
\beta(x,y)=\langle x,Jy\rangle.
$$
$J^2=-I$ 及反线性等距性给
$$
\beta(y,x)=-\beta(x,y),
\tag{2.5}
$$
而 (2.4) 给
$$
\beta(Tx,y)=\beta(x,Ty).
\tag{2.6}
$$
因此对任意 $x\in Q$、整数 $m,n\ge0$，
$$
\begin{aligned}
\beta(T^mx,T^nx)
 &=\beta(x,T^{m+n}x)\\
 &=-\beta(T^{m+n}x,x)
 =-\beta(x,T^{m+n}x)=0.
\end{aligned}
\tag{2.7}
$$
于是每个闭循环轨道
$$
L_x=\overline{\operatorname{span}\{T^nx:n\ge0\}}
$$
都满足
$$
\boxed{L_x\perp JL_x.}
\tag{2.8}
$$
若 $x\ne0$，则 $JL_x\ne0$，所以 $L_x\ne Q$。

**结论 2.1。** 若 $Q\ne0$，$T$ 没有循环向量。对每个 $x\ne0$，$L_x$ 是一个非零真闭 $T$ 不变子空间。

本结论讲的是有界商算子 $T$，不讲原 $A$ 的普通不变格。

这里的 $J$ 始终作用在 (1.1) 的分母坐标 $(y_1,y_2)$ 上。无论分母由哪些有界单位或有界扰动产生，只要 $R_i\in\mathfrak C$，(2.2)--(2.4) 均使用同一个无权的 $J$。没有把它通过非酉的三角图坐标变换搬回原 $(x,M_1x,M_2x)$ 并仍声称无权；也没有声称两个不同预解参数所给的正交商之间存在保持 $J$ 的酉同构。

## 3. 原强多项式单位迫非零商无限维

[R23](R23-strong-star-polynomials-and-tail-block-projections.md) §3 给实际多项式
$$
E_\ell=e_\ell(A),\qquad
\|E_\ell\|\le1,\qquad E_\ell\to I\text{ 强*},
$$
其最低非零次数 $b_\ell\to\infty$。

由于 $K,N$ 都被 $A^{(2)}$ 保持，多项式商演算准确给
$$
e_\ell(T)=P_QE_\ell^{(2)}|_Q.
\tag{3.1}
$$
故 $e_\ell(T)$ 是收缩且强趋于 $I_Q$。特别，$T$ 单射且稠密像：若 $Tx=0$，充分大的 $e_\ell(T)x=0$；而 $e_\ell(T)Q\subset\operatorname{Ran}T$。

另外，
$$
T^n=P_Q(A^n)^{(2)}|_Q,\qquad
\|T^n\|\le\|A^n\|.
$$
原 $A$ 范数拟幂零，因而 $T$ 也范数拟幂零。若 $0<\dim Q<\infty$，$T$ 的单射性使它可逆，与拟幂零矛盾。因此
$$
\boxed{Q=0\quad\text{或}\quad \dim Q=\infty.}
\tag{3.2}
$$
同一个论证适用于 $T$ 的每个闭不变旗：$e_\ell(T)$ 的收缩强单位下降到对应子商。所以每个非零闭 $T$ 不变空间都是无限维。结合 (2.8)，每个非零循环轨道 $L_x$ 还具有无限余维。

这些结论没有把环境空间的稠密像无证下传；使用的是同一组实际多项式强单位。

## 4. 秩二真正态如何迫使该商非零

取
$$
\rho=f_1\otimes f_1+f_2\otimes f_2\ne0,\qquad
M_i=X_{Cf_i},\qquad
\tau=\|f_1\|^2+\|f_2\|^2.
$$
$M_i$ 是原最小闭乘子。假设实际单射 $S\in\mathfrak C$ 满足
$\phi_\rho(S\mathcal A)=0$。

现在假设两行都存在广义预解数据
$$
L_i=M_iU_i+F_i,\qquad
U_i\in\mathfrak C^\times,\quad F_i\in\mathfrak C,\quad
\lambda_i\in\rho(L_i).
$$
记
$$
R_i=(L_i-\lambda_iI)^{-1},\qquad
B_i=F_i-\lambda_iI,
$$
$$
D_i=M_iR_i=U_i^{-1}(I-B_iR_i)\in\mathfrak C.
\tag{4.1}
$$
[R244 预解图附录](R244-appendix-empty-resolvent-and-common-graph-vacuum-defect.md) 的实际配对论证及广义有界恒等式给
$$
h=D_1R_2f_1+D_2R_1f_2=0.
\tag{4.2}
$$
这里 $R_1R_2H$ 已实际落入两个最小域，因此 (4.2) 不使用未知自然乘积。

定义两个真正的 $H^{(2)}$ 向量
$$
g_i=(L_i-\lambda_iI)1,\qquad
z_i=D_i^*Cf_i,\qquad
g=(g_1,g_2),\quad z=(z_1,z_2).
\tag{4.3}
$$
因 $1\in\operatorname{Dom}M_i$，$g_i$ 确实属于 $H$。真实逆等式给
$$
R_ig_i=1,\qquad d_1g=0,
\tag{4.4}
$$
故 $g\in K$。另一方面由 $C$ 对称性及 (4.2)，
$$
d_0^*z
=R_2^*D_1^*Cf_1+R_1^*D_2^*Cf_2
=Ch=0.
\tag{4.5}
$$
所以 $z\in N^\perp$。

最后的配对是严格正的：
$$
\begin{aligned}
\langle g,z\rangle
 &=\sum_i\langle D_ig_i,Cf_i\rangle\\
 &=\sum_i\langle M_iR_i(L_i-\lambda_iI)1,Cf_i\rangle\\
 &=\sum_i\|Cf_i\|^2=\tau>0.
\end{aligned}
\tag{4.6}
$$
第二行先使用 $R_i(L_i-\lambda_iI)1=1\in\operatorname{Dom}M_i$，逐项支付域。

若 $Q=0$，则 $K=N$，(4.4)--(4.5) 会给 $\langle g,z\rangle=0$，矛盾。因此
$$
\boxed{Q\ne0.}
\tag{4.7}
$$
更准确，置 $q=P_Qg$，则
$$
\tau=\langle q,P_Qz\rangle,\qquad
\|q\|\ge\frac{\tau}{\|P_Qz\|}\ge\frac{\tau}{\|z\|}>0.
\tag{4.8}
$$
这把原正迹变成了有界链上一个实际非零中间商类。由 §§2--3，该商必无限维，其诱导 $A$ 算子没有循环向量。

若两行本身 $0\in\rho(M_i)$，可取 $U_i=I,F_i=0,\lambda_i=0$。
此时 $D_i=I$，$g=z=(Cf_1,Cf_2)$，所以
$$
\boxed{
(Cf_1,Cf_2)\in Q,\qquad
J(Cf_1,Cf_2)=(f_2,-f_1)\in Q.
}
\tag{4.9}
$$
这两向量正交、等范数且非零；正交性直接是 (2.5)，不依赖两个 $f_i$ 相互正交。

### 4.1 分母在缺陷商上准确为零

每个 $\mathfrak C$ 元的对角放大保持 $K,N$，故可在 $Q=K/N$ 上诱导。对 $v=(x_1,x_2)\in K$，实际关系 $R_1x_1=R_2x_2$ 给
$$
R_1^{(2)}v=d_0x_2,\qquad R_2^{(2)}v=d_0x_1.
$$
因此
$$
\boxed{(R_1)_Q=(R_2)_Q=0.}
$$
广义预解恒等式 $U_iD_i+B_iR_i=I$ 下降为
$$
(U_i)_Q(D_i)_Q=I_Q.
$$
$U_i$ 及其实际有界逆均保持该旗，所以 $(D_i)_Q=(U_i)_Q^{-1}$ 为单位。
这解释了为何不能在此商中将 $R_i^{-1}D_i$ 自动视为稠密定义的单值算子：其分母恰好为零而分子是单位。R184 的规范分母另有普遍强主理想单位；这里没有该前提。

## 5. 与共同最小图的准确连接及边界

将共同图中的坐标
$(x,M_1x,M_2x)$ 用真实有界三角变换改为
$$
(x,(L_1-\lambda_1I)x,(L_2-\lambda_2I)x).
$$
在其像中都有 $x=R_1y_1=R_2y_2$。删除第一坐标是有界单射，逆为
$(y_1,y_2)\mapsto(R_1y_1,y_1,y_2)$。
事实上，整个 $K$ 对应准确的最大交域图
$$
\Gamma_{\max}
=\{(x,M_1x,M_2x):x\in\operatorname{Dom}M_1\cap\operatorname{Dom}M_2\}.
$$
对任意 $(y_1,y_2)\in K$，逆映射为
$$
(y_1,y_2)\longmapsto(R_1y_1,D_1y_1,D_2y_2);
$$
因为 $R_1y_1=R_2y_2$，它确实属于两个实际最小乘子的域。这是有界图范数同构。原共同最小图则准确对应一个闭 $A^{(2)}$ 不变空间
$$
K_0=\overline{\{(p(A)g_1,p(A)g_2):p\in\mathbb C[z]\}}
\subseteq K.
\tag{5.1}
$$
原共同正则图对应 $N$；前一附录的包含给 $N\subseteq K_0$。

故 $P_QK_0$ 是 $Q$ 中由 $q=P_Qg$ 生成的闭循环 $T$ 不变空间，且 $q\ne0$。
由 §2，它严格小于 $Q$。特别，真见证不仅迫共同正则图不等于共同最小图，还迫
$$
\boxed{N\subsetneq K_0\subsetneq K.}
\tag{5.2}
$$
第二个严格包含不能从每个单独二坐标图稠密性看出；它来自交替型商无循环向量以及共同最小图的循环性。

第 3 节的同一组强多项式单位还作用于 $T$ 的限制 $P_QK_0$ 及商 $Q/P_QK_0$。两者非零，故都无限维：
$$
\boxed{\dim(K_0/N)=\dim(K/K_0)=\infty.}
$$
在原图坐标中，记共同最小图为 $\Gamma_{\min}$、共同正则图为 $\Gamma_R$，相应地得到
$$
\Gamma_R\subsetneq\Gamma_{\min}\subsetneq\Gamma_{\max},
\qquad
\dim(\Gamma_{\min}/\Gamma_R)
=\dim(\Gamma_{\max}/\Gamma_{\min})=\infty.
$$
这些是闭子空间的商维数；没有断言上述有界坐标同构是酉同构。

这个新缺口仍不构成矛盾。不能把 $JQ=Q$ 改成 $J(P_QK_0)=P_QK_0$：由 (2.8)，这两个非零空间反而正交。不能取消旗子商或将 $K_0/N$ 搬回原 $H$。下一步若要用此接口排见证，需要额外证明本题的该有界链精确、或共同最小图已达到 $K$；二者当前均未得到。普通 Hilbert ISP 尚未完成。
