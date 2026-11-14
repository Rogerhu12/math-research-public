# R244 后续附录：秩二共同图的交换 Lagrangian 完成与全谱 C 自伴扩张

日期：2026-11-13（UTC）。作者：normal_resume_1cf；Astra-ISP-1cf8c51d 已核查不变等向极大化、商共轭、原图伴随及实参数条件。
状态：已证明，完整的闭域存在性结论。在真正秩二见证产生的严格共同图缺口中，可以选一个仍与整个 A' 域交换的 C 自伴中间闭图，且它包含共同最小图。已有比例全谱定理使这些扩张仍具有整个复平面谱。这里的 C 自伴不等于通常 Hilbert 自伴，不提供共同最小图核心。

已核对 R53、R58、R65 的相关完整源，未见下面同时保交换代数不变性的 Lagrangian 完成。本文给出自含证明，不声称文献新颖性。

## 1. 交换交替型中的不变 Lagrangian 完成

设 $\mathcal H$ 为复 Hilbert 空间，J 为反线性等距满射，满足 $J^2=-I$。
记
$
 \beta(x,y)=\langle x,Jy\rangle,\qquad
 L^\beta=\{x:\beta(x,L)=0\}=(JL)^\perp.
$
β 是连续、非退化、交替的复双线性型。

设 $\mathfrak B\subset B(\mathcal H)$ 为交换的含幺代数，且
$
 JF=F^*J\qquad(F\in\mathfrak B).
$
因此
$
 \beta(Fx,y)=\beta(x,Fy). \tag{1.1}
$
称闭空间 L 等向，是指 $L\subset L^\beta$；称其 Lagrangian，是指 $L=L^\beta$。

**定理 1.1。** 每个闭的 $\mathfrak B$ 不变等向空间 $L_0$，都包含于某个闭的 $\mathfrak B$ 不变 Lagrangian 空间 L。

证明：考虑包含 $L_0$ 的全部闭不变等向空间，按包含排序。
一条链的并之闭包仍不变、仍等向：任意两个并中向量均位于链中某一个共同成员，连续性再支付闭包。由 Zorn 引理可取极大成员 L。

由 (1.1)，$L^\beta$ 也 $\mathfrak B$ 不变。
若 $L^\beta\ne L$，在实际闭旗 $L\subset L^\beta$ 中置
$
 Q_L=L^\beta\ominus L.
$
有
$
 JL^\beta=L^\perp,\qquad JL^\perp=L^\beta,
$
所以 $JQ_L=Q_L$。商表示
$\pi_L(F)=P_{Q_L}F|_{Q_L}$
仍交换，且满足
$J\pi_L(F)=\pi_L(F)^*J$。

选 $0\ne q\in Q_L$。其闭代数循环轨道
$
 Y=\overline{\{\pi_L(F)q:F\in\mathfrak B\}}
$
等向。确实对 F、G，
$
 \begin{aligned}
 \beta(\pi_L(F)q,\pi_L(G)q)
 &=\beta(q,\pi_L(FG)q)\\
 &=-\beta(\pi_L(FG)q,q)
 =-\beta(q,\pi_L(FG)q)=0.
 \end{aligned}
$
最后用闭包连续性。

于是 $L\oplus Y\subset L^\beta$ 是一个更大的闭不变等向空间。
不变性须按旗核验：对 $y\in Y$，Fy 在 $L^\beta$ 中，而它的商投影在 Y，所以 $Fy\in L\oplus Y$；L 本身也不变。
与 L 的交叉 β 配对为零，Y 内部配对也为零。
这与极大性矛盾。故 $L=L^\beta$。证毕。

当 $\mathcal H\ne0$ 时，L 和 JL 互相正交，且
$
 \mathcal H=L\oplus JL.
$
这不是把 JL 声称为原代数不变空间；它一般为伴随代数不变。

## 2. 应用于实际秩二共同预解图

沿用已证 [R244 秩二设置](R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)：$R_1,R_2\in A'$ 为两个原最小乘子的广义预解子，均单射且稠密像，并有 $R_ig_i=1$。
定义
$
 N=\overline{\{(R_2h,R_1h):h\in H\}},\qquad
 K=\{(y_1,y_2):R_1y_1=R_2y_2\},
$
$
 K_0=\overline{\{(Fg_1,Fg_2):F\in A'\}},\qquad Q=K\ominus N.
$
真秩二正见证已给
$
 N\subsetneq K_0\subsetneq K.
$
在 $H^{(2)}$ 上取
$J(y_1,y_2)=(Cy_2,-Cy_1)$。
已证 $JN=K^\perp$、$JQ=Q$，压缩的整个 A' 代数交换且 J 对称。

令 $L_0=K_0\ominus N\subset Q$。
它是由非零 $q=P_Q(g_1,g_2)$ 生成的闭循环轨道，因而等向。
定理 1.1 给闭的不变 Lagrangian $L\subset Q$，满足 $L_0\subset L$。
取其原旗中的逆像
$
 E=N\oplus L.
$
则 E 闭、被每个 $F^{(2)}\ (F\in A')$ 保持，且
$
 N\subsetneq K_0\subseteq E\subsetneq K. \tag{2.1}
$
最后两个端点均严格：E 包含非零 L_0，故 E≠N；非零交替型 Q 中 Lagrangian L 不能等于 Q，故 E≠K。
不声称 $K_0\subset E$ 必严格。

在原 $H^{(2)}$ 的同一个 β 中有
$
 N^\beta=K,\qquad
 E^\beta=N\oplus L^\beta_Q=E. \tag{2.2}
$
第二式需要先注意：E 含 N，所以 E^\beta 包含于 K；E 包含于 K，所以 E^\beta 含 N。之后才能在 Q 中计算其商正交补。

## 3. 原 H 上的准确 C 自伴中间算子

已证比例图恒等式为
$
 N=\operatorname{Graph}T_{\min},\qquad
 K=\operatorname{Graph}T_{\max},
$
$
 T_{\min}=X_h,\quad h=R_1g_2,\qquad
 T_{\max}=R_2^{-1}R_1=T_{\min}^{\top},
 \quad T^\top=CT^*C.
$
其中 $T_{\min}$ 是原最小闭乘子，$T_{\max}$ 取准确最大商域。

由 $N\subset E\subset K$，E 是某个单值、稠密定义闭算子 $T_E$ 的图：单值性来自 E 包含于 K，稠密定义性来自它含 N。
并且每个 $F\in A'$ 都保持其域，满足
$
 T_EFv=FT_Ev\qquad(v\in\operatorname{Dom}T_E).
$

对任意稠密定义闭算子 T，图的 β 正交补准确等于
$
 \operatorname{Graph}T^\top
   =(\operatorname{Graph}T)^\beta.
$
这是等式
$B(u,Tv)=B(w,v)$ 对全部 $v\in\operatorname{Dom}T$
与 $w=T^\top u$ 的定义。
所以 (2.2) 给
$
 \boxed{T_E=CT_E^*C,\qquad
  T_{\min}\subsetneq T_E\subsetneq T_{\max}.} \tag{3.1}
$
它包含原共同最小图 K_0 的比例实现，两个极端域又都没有被误作相等。

[R244 比例全谱稿](R244-appendix-resolvent-minimal-cores-and-intermediate-ratio-spectra.md)已证：在这个真正态的非零图缺口中，每个闭的 A' 交换中间图，只要含 N 且包含于 K，其每个广义有界单位/扰动都没有预解点。
因此本稿存在的这些 C 自伴扩张仍满足
$
 \boxed{\sigma(T_EU+F)=\mathbb C
       \quad(U\in(A')^\times,\ F\in A').} \tag{3.2}
$
该结论没有因 C 自伴而恢复任何预解。其既有证明的核心是：若某个广义预解存在，有界逆 P 的真空原像使 1 成为原多项式图核心，迫 $T_E=X_h=T_{\min}$；再由全 C 伴随域迫 $T_{\min}=T_{\max}$，与 N≠K 矛盾。

## 4. 真正实参数时可同时保持点态实结构

若两个 R_i 都 J_0 实，且 $J_0f=\overline f$，那么 N、K、K_0、Q 都 J_0 实。
这里 g_i 也实，因为 $R_ig_i=1$ 的唯一解在 J_0 下仍是同一个解。
$J_0^{(2)}$ 与 J 交换。

此时定理 1.1 的 Zorn 构造可以限制在同时 J_0 实的闭不变等向空间中。链闭包仍实。
若余商非零，它继承点态共轭，可选一个非零实向量 q；整个商代数在 J_0 共轭下封闭，所以 q 的闭代数循环轨道仍实。
同一个反证给实 Lagrangian L。

于是可令 E 同时 J_0 实，得到
$
 J_0\operatorname{Dom}T_E=\operatorname{Dom}T_E,\qquad
 J_0T_E=T_EJ_0,\qquad
 \mathcal RT_E\mathcal R=T_E^*,
 \quad\mathcal R=CJ_0.
$
这仍是无限正负指数的 Krein 型；(3.2) 依然成立。
一般复参数只有已证带权 $\Theta_Q$ 实结构，本节不把它换成无权点态共轭。

## 5. 尚未得到的共同核心

本稿补全的是实际图缺口内可选择的闭 C 自伴扩张，未证明共同最小图 K_0 已是任何最大域的核心。存在中间 C 自伴扩张反而保留了 $T_{\min}\ne T_{\max}$ 的准确边界。
Zorn 的不变 Lagrangian 位于一个二重放大的旗子商；没有据此向原 A 输送非零真不变子空间。普通 Hilbert ISP 的完成标准未改变。
