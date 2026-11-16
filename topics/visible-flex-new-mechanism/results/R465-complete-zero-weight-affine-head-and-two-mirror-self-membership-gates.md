# R465：完整增强零权商的七比五 self 化与两个原头的准确 lift 门

日期：2026-11-16。**原已付结果的只读消费和纸面推论。没有执行原根恢复、旧秩、符号程序、profile 评价、求积、人工检查或新科学。**

[R463](R463-real-partial-quotients-translation-defect-and-finite-affine-control-interface.md) 已指出：当前同宽全角色 partial 给真实额外商，纯平移不能替代旧缩放截面；补有限仿射闭包后，$D$ 单独也因非零零权类而不可逆。不过，同一个完整商上的 $DQ+NQ=Q$ 已足以使用真实双参数放大。它准确等价于 $Q_0\subseteq NQ_1$，不能只在自然 $\mathfrak d$ 多项式像上检验。

本文将这一个新的完整 lift 门进一步化为准确的有限 self 问题。记 $J_{\rm aff}$ 为 R463 的同一完整增强，$Q=J_{\rm aff}(U)/J_{\rm aff}(\mathcal R)$。定义
$$
\mathcal W_0=U_0\cap\ker E\cap\ker\mathscr C,\qquad
\mathcal K_0=\mathcal R_0\cap\ker E\cap\ker\mathscr C,
$$
其中 $\mathscr C$ 是整个三后缀形式 Af current，采用原 $\mathcal K/4$ 规范。令 $S$ 为当前共同母的两个完整 self partial 平移多项式，保持原累计锚及全部常数。结论是一个自然商同构：
$$
\boxed{
Q_0/NQ_1
\ \simeq\
S(\mathcal W_0)/S(\mathcal K_0).
}
\tag{1}
$$
这里 $\dim\mathcal W_0=7$、$\dim\mathcal K_0=5$ 都由旧完整结果推出，**不是**新观察秩。于是新的双参数线性条件准确为
$$
\boxed{S(\mathcal W_0)=S(\mathcal K_0).}
\tag{2}
$$

两个待判类可以固定为经过同权完整 current 补偿的 $H_*+J_4$ 与 $J_4-J_6$。本文给出它们为何恰为两个、为何必须同一五维响应像同时支付、为何真实全角色零迫整个 current 零，并从原 R350 得到第二个头 $C_{20}$ 的一个小而完整的原 self/pure 入口。尚未得到(2)的肯定或否定数值；不把维数、自然投影或已付同宽十九行右逆冒成这个成员结论。

直接来源：
[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)、
[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md)、
[R316](R316-complete-weight-zero-self-membership-and-positive-character-representative.md)、
[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)、
[R356](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md)、
[R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md)、
[R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md)、
[R454](R454-complete-response-self-principal-trace-and-seven-ordered-current-invariants.md)、
[R456](R456-two-highest-ordered-current-invariants-on-real-mirror-copy-families.md)、
[R457](R457-natural-seven-current-quotient-complete-normalization-and-weight-zero-witness.md)、
[R459](R459-one-common-signed-witness-for-all-internal-fluxes-of-the-equal-width-library.md)、
[R462](R462-five-dimensional-complete-weight-zero-current-kernel-and-all-width-self-interface.md)、
R463。R406 的结论在这里也可直接经 R457/R459 的已列原身份消费。

## 1. 必须使用同一个稳定的增强映射

保 R459 从起点选择的共同物理宽度、当前母库、原全部复制、真实 suffix、共同右锚及允许的支持窗口。置
$$
J_0=(E,\mathcal A,\mathcal O_{\rm all}),\qquad E=(\pi,\mathcal Q).
\tag{3}
$$
$J_0$ 是 R433 的原共同映射。$\mathcal A$ 已含所需有限正仿射查询；它不是 universal self natural 函数。$F$ 是原库所有角色、所有实际 Af 镜点的 $H_d,H_e$，并沿 R463(2)先在整个 $U$ 上用真实相位查询延拓。

使用 R463 的最小仿射行闭包
$$
F_{\rm aff}
=\operatorname{span}\{FN^j\Pi_\sigma:
-9\le\sigma\le3,\ 0\le j\le\sigma+9\},\qquad
J_{\rm aff}=(J_0,F_{\rm aff}).
\tag{4}
$$
这是有限真实查询的行空间；可由十三个近一正 $H$ 配完整小平移闭包确定。不得对不同宽度分别选择不相同的响应成本。

$\ker J_{\rm aff}$ 对 $D,N$ 稳定，$\mathcal R$ 也稳定。因此
$$
P=J_{\rm aff}(U),\quad L=J_{\rm aff}(\mathcal R),\quad Q=P/L
\tag{5}
$$
有同一个真权分解，$D,N$ 均在 $Q$ 上良定义。只有在(4)以后，下面的 $Q_0,NQ_1$ 才有所需含义。

记
$$
\mathcal Z_0=U_0\cap\ker J_{\rm aff}.
\tag{6}
$$
由稳定的真权投影，
$$
\boxed{
Q_0/NQ_1
\simeq U_0/(\mathcal R_0+NU_1+\mathcal Z_0).
}
\tag{7}
$$
证明只是先将 $J_{\rm aff}:U_0\to P_0$ 除其核，再除响应及平移像。这里 $NQ_1$ 来自整个 $U_1$；没有要求其前像先在 $\ker J_0$。

## 2. R196 已经准确给出唯一一条平移像

R196 的完整原函数核给
$$
\dim U_0=19,\qquad \dim\mathcal R_0=16,\qquad
U_0/\mathcal R_0
=\operatorname{span}\{[C_2],[C_4],[C_6]\}.
\tag{8}
$$
该稿(2)与§3末段还给出更强的准确身份：
$$
\boxed{
(\mathcal R_0+NU_1)/\mathcal R_0=\mathbb R[C_6].
}
\tag{9}
$$
不是只知道 $C_6$ 有一个平移前像；整个同权平移像恰为这条线。因而原二维头为
$$
\mathcal H_0:=U_0/(\mathcal R_0+NU_1),\qquad
\dim\mathcal H_0=2.
\tag{10}
$$

R333 的完整 whole-$E$ 零代表满足
$$
H_*-C_2\in\mathcal R_0,\qquad
J_4-C_4\in\mathcal R_0,\qquad
J_6-C_6\in\mathcal R_0.
\tag{11}
$$
R196 的全部两参数头泛函 $\lambda_{x,y}$ 在这三条上的值是
$$
\lambda_{x,y}(H_*)=-x-y,\qquad
\lambda_{x,y}(J_4)=y,\qquad
\lambda_{x,y}(J_6)=0.
\tag{12}
$$
它们杀整个 $\mathcal R$ 和 $NU_1$。特别 $\lambda_+=\lambda_{-1,0}$，而 $\lambda_{0,1}$ 只是另一条真实线性头坐标，不是非负字符。

因此 $H_*+J_4$ 与 $J_4-J_6$ 在(10)中分别有坐标
$$
\bigl(\lambda_+,\lambda_{0,1}\bigr)=(1,0),\qquad(0,1).
\tag{13}
$$
这两个类不能由一条 $\lambda_+=1$ 的核见证一起代替。

R457 另给
$$
C_{20}=C_4-C_6+R_*,\qquad R_*\in\mathcal R_0.
\tag{14}
$$
$C_{20}$ 是原 $\bar A_{hh}$ 的状态系数 $h^{-2}$。式(14)在本稿只按其完整原关系使用；没有猜测未逐项列出的 $R_*$ 系数，也没有把未经 pure/self 修正的 $C_{20}$ 直接称为 $J_4-J_6$。

## 3. 在权零上，J0 的核准确就是 whole-E 核

R333(20)—(21)与 R316 旧结果给
$$
\dim(U_0\cap\ker E)=9,\qquad
\dim(\mathcal R_0\cap\ker E)=6.
\tag{15}
$$
而且
$$
U_0\cap\ker E
=(\mathcal R_0\cap\ker E)
\oplus\operatorname{span}\{H_*,J_4,J_6\}.
\tag{16}
$$

全部响应的完整 natural 函数恒零。对原三头，R406/R457/R459 给
$$
\Lambda(H_*)=n_2,\qquad
\Lambda(J_4)=\Lambda(J_6)=0.
\tag{17}
$$
$n_2$ 是局部五次函数；当前已初选母及全部规定正仿射查询使其为零。局部性也使其有序 $3+2$ 交叉为零。因此(16)的每个成本都杀(3)中另外两部分，得到
$$
\boxed{U_0\cap\ker J_0=U_0\cap\ker E.}
\tag{18}
$$
这是在**当前母库与真权零**上的结论。它不声称 $\ker E\subseteq\ker J_0$ 于所有权，也不把 $n_2$ 当成 universal 零函数。

## 4. 整个权零 current 核确为七维

R462 已从完整 current 协变证明：39坐标形式空间中，权零只可能是
$$
C=A_1^{[2]},\qquad B=A_2^{[1]}.
\tag{19}
$$
上标为真实 suffix 矩编号。完整响应的该像恰为非零直线
$$
2C+B=0.
\tag{20}
$$
其来源是 R454 的全响应像 $\ker D$；R462 的同权投影保证(20)来自真正 $\mathcal R_0\cap\ker E$。

对 $H_*$，R457 给
$$
\mathfrak d(H_*)=-3x^5/128,\qquad
[x^5]\mathfrak d=2C+B.
\tag{21}
$$
故其 current 不在(20)。由(19)，整个 $U_0\cap\ker E$ 的 current 像准确为二维。

所以
$$
\boxed{
\dim\mathcal W_0=9-2=7,\qquad
\dim\mathcal K_0=6-1=5.
}
\tag{22}
$$
这里只组合了(15)、R462完整像与(21)，没有再做旧矩阵或函数秩。

为使两个新目标可直接按原件组装，R316(1)、R333(10)给
$$
\begin{aligned}
X_H:=H_*+J_4={}&C_2+C_4+\frac{31}{32}R_2-\frac3{128}R_3
+\frac{31}{64}R_4-\frac{39}{32}R_5+\frac{27}{128}R_9,\\
X_Y:=J_4-J_6={}&C_4-C_6+\frac{35}{256}R_2-\frac3{1024}R_3
+\frac{35}{512}R_4-\frac{39}{256}R_5
-\frac1{64}R_7+\frac{27}{1024}R_9 .
\end{aligned}
\tag{22a}
$$
这里所有 $R_j$ 都是 **R126 原 old-column 标签**，不是紧缩位置。
这些仅为已付两个式子的有理合并；其完整 self partial 是新的待读目标，不能从旧 whole-$\mathcal Q$ 零值冒称已经读出。

二者都有 $J_0=0$ 与 $\mathfrak d=0$。因此二者的 current 都在(20)。
固定同一条原响应 $R_C\in\mathcal R_0\cap\ker E$，使
$$
\mathscr C(R_C):\quad C=1,\ B=-2.
$$
它的存在由 R454/R462 的已付完整 lift 保证。若需要一个固定原件，可用 R434 原日志 seq707 的完整成本 $V_{707}$：
$$
\begin{aligned}
V_{707}={}&-\frac7{49920}\mathcal B_YH_4
+\frac7{109824}\mathcal B_VH_5
+\frac{29}{2196480}\mathcal B_TH_5\\
&-\frac{29}{3294720}\mathcal B_LH_6
+\frac{29}{3294720}\mathcal B_UH_6
+\frac{17}{2080}\mathcal B_YJ_2\\
&-\frac{576}{143}\mathcal B_Y\chi_{40}
+\mathcal B_Y\chi_{104}.
\end{aligned}
\tag{22b}
$$
该已付原件 current 为 $C=-69/9152,\ B=69/4576$，
故取 $R_C=-9152V_{707}/69$。原 payload 指纹为
$\texttt{729055c2e1075378e3ac5e771e24a6dd4ca824c8c4aa9fab800dd25eb7614e6b}$；
这里仅消费已付八项与 current，不重新验证其旧 whole-$E$ 或旧 current 映射。
$V=\Phi_{p_1}$、$Y=\Phi_{p_2}$，不与成本的泛称 $V$ 混用。

令
$$
c_H=C(\mathscr C(X_H)),\qquad
c_Y=C(\mathscr C(X_Y)),
$$
并定义
$$
\boxed{
V_H=X_H-c_HR_C,\qquad
V_Y=X_Y-c_YR_C.
}
\tag{23}
$$
这两个是同权完整成本，均在 $\mathcal W_0$；不在每个角色上另选补偿。
由(13)，
$$
\boxed{
\mathcal W_0
=\mathcal K_0\oplus\mathbb RV_H\oplus\mathbb RV_Y.
}
\tag{24}
$$
不同合法的完整 current lift 只把 $V_H,V_Y$ 分别改变一个 $\mathcal K_0$ 元素；后面的 self 商类因此不变。

## 5. 全角色 F 零在权零上必迫整个 current 零

这一必要性不能仅由“形式 current 比实际评价更强”倒推。
这里使用 R456 已付的实际最后 low/high 角色，真实 $n_0\ne0$，以及原十二个不同中心。

按 R456 原 $\gamma^7$ 归一，两镜点的完整 ordered 组合是
$$
E_\varepsilon(t)
=r_*^{-3}F_{\rm cur}
(t-\varepsilon b,h_*r_*,\varepsilon s_*r_*,r_*;n(t)),
$$
其中
$$
n(t)=(n_0,n_1+tn_0,n_2+2tn_1+t^2n_0).
\tag{25}
$$
$\varepsilon=+1$ 为左根，$h_*,s_*,b>0$。这两个多项式次数至多七；至少八个已有中心的准确零值使其恒零。

在权零情形(19)，R456(18)(19)的原系数准确为
$$
[t^6]E_\varepsilon
=\varepsilon\frac{s_*n_0}{3}(5C+2B),
\tag{26}
$$
$$
\frac12[t^5](E_++E_-)
=-n_0\left(\frac{h_*}{6}+2s_*^2+\frac{10bs_*}{3}\right)(2C+B).
\tag{27}
$$
不存在其它权零 current 坐标可以补偿这两个式子。所有显示乘子非零，
而 $5C+2B=2C+B=0$ 迫 $C=B=0$。

另一方面，原组合 $T_iH_d+R_iH_e$ 恰消去 self 项，只保(25)的完整 ordered current。所以得到
$$
\boxed{
V\in U_0\cap\ker J_0,\quad F(V)=0
\ \Longrightarrow\ \mathscr C(V)=0.
}
\tag{28}
$$
真实 $R/T$ suffix、镜点偏移 $b$、共同幅 $\gamma^7$ 均保留。
这比 R463 只用(27)读取 $D_5$ 更强，但完全是两个原系数的纸面联用；没有新取样或求秩。

## 6. 七维空间上的完整 self 映射 S

对 $V\in\mathcal W_0$，记完整 self 输出
$$
\Sigma_V(u)=V(u^2,0),\qquad
h_\pm(c;V)
=\int_{\ell}^{c\pm b}
u_c'\,\Sigma_V(u_c)'',\quad
u_c(x)=u(x-c).
\tag{29}
$$
共同参考母、原左累计端及算子右锚均按 R459 输运。
定义根坐标的归一多项式
$$
P_-(x;V)=r_*^{-5}h_-(x+b;V),\qquad
P_+(x;V)=r_*^{-5}h_+(x-b;V),
$$
$$
S(V)=(P_-,P_+).
\tag{30}
$$
这里 self 没有除以4；(25)的 ordered current 使用另一已明示规范。

R356/R459 的完整低层身份给
$$
N^9V\in U_{-9},\qquad \Sigma(U_{-9})=0.
$$
因此(30)为次数至多八的完整平移多项式；两个八次项相同。可取固定有限目标空间
$$
\mathscr P_8=
\{(P_-,P_+)\in\operatorname{Pol}_{\le8}^2:
[x^8]P_-=[x^8]P_+\},
\tag{31}
$$
其形式维数17不是 $S$ 的像秩。

R459 §7 的同三矩内区路径论证对 $\mathcal W_0$ 全部成本适用：左 cap 外二导因 whole-$Q$ 保持，右 cap 另用(18)中的真实总 natural 查询零。因此最终全部母的 partial 可用同一个参考母(29)表达；不能只以 jets 相同代替这一步，也不能对另一不连通矩纤维外推。

对整个形式 current 零的成本，R459(17)(18)于是给每个实际 role
$$
H_{d,i,\pm}=a_i^3R_i\,h_{i,\pm},\qquad
H_{e,i,\pm}=-a_i^3T_i\,h_{i,\pm}.
\tag{32}
$$
选原 low 或 high 角色，其 $a_i,R_i$ 均非零；十二个已有中心的 $H_d=0$ 使两条至多八次多项式在至少九个不同位置为零，故(30)整对为零。共同复制幅只产生原非零第五次因子，不改变结论。

反过来，若 $S(V)=0$，则(32)使全部位置、全部角色两通道零。对任意允许的小平移也同样成立。因为 $V$ 是真权零，
$$
T_cD_HV=T_cV.
$$
故原有限正伸缩闭包没有再添新的条件。这一步在先有(28)及真正权零以后使用，不能用于 R459 的最终混权见证。

综上得到关键的**核等号**
$$
\boxed{\mathcal Z_0=\ker(S|_{\mathcal W_0}).}
\tag{33}
$$
它同时支付了必要的 E/current 消失和充分的全部真实 self partial，不是仅一边包含。

## 7. 原二维头与七维空间之间没有隐藏的平移核

由(13)(23)，$\mathcal W_0$ 到原头 $\mathcal H_0$ 的自然映射满射。
其核准确为 $\mathcal K_0$。

为核后一断言，取
$$
V\in\mathcal W_0\cap(\mathcal R_0+NU_1).
$$
由(9)(11)，可写
$$
V=R+aJ_6,\qquad R\in\mathcal R_0 .
$$
$E(V)=E(J_6)=0$ 迫 $R\in\mathcal R_0\cap\ker E$。
再用完整自然读出
$$
\mathfrak d(R)=0,\quad \mathfrak d(V)=0,\quad
\mathfrak d(J_6)=3x^5/128
$$
迫 $a=0$。于是 $V=R$ 且其完整 current 零，即 $V\in\mathcal K_0$。
反向包含显然，所以
$$
\boxed{
\mathcal W_0\cap(\mathcal R_0+NU_1)=\mathcal K_0,\qquad
\mathcal W_0/\mathcal K_0\simeq\mathcal H_0.
}
\tag{34}
$$
这里使用的是实际 $N$ 像只有(9)，并非把 $\mathfrak d$ 的所有多项式前像当作完整前像。

## 8. 完整商同构与两条成员门的充要性

由(7)、(34)，$\mathcal W_0$ 也满射到 $Q_0/NQ_1$。
其核为
$$
\mathcal W_0\cap
(\mathcal R_0+NU_1+\mathcal Z_0)
=\mathcal K_0+\mathcal Z_0,
$$
因为 $\mathcal Z_0\subseteq\mathcal W_0$。因此
$$
Q_0/NQ_1\simeq
\mathcal W_0/(\mathcal K_0+\mathcal Z_0).
\tag{35}
$$
再用(33)，第一同构定理准确给
$$
\mathcal W_0/(\mathcal K_0+\ker S)
\simeq S(\mathcal W_0)/S(\mathcal K_0).
$$
这证明(1)。

同构可以不选坐标直接描述：$V\in\mathcal W_0$ 的全增强成本类映到
$[S(V)]$。若改变 $V$ 一个原响应或可消失查询成本，恰改变 $\mathcal K_0+\ker S$；故不是两个恰好同维空间之间的非规范比较。

结合(24)，R463 双参数线性条件的充要判据是
$$
\boxed{
S(V_H),\ S(V_Y)\in S(\mathcal K_0).
}
\tag{36}
$$
两条成员必须在同一个五维完整响应空间、同一实际母及同一全镜对定义下成立。若成立，选 $W_H,W_Y\in\mathcal K_0$，则
$$
V_H-W_H,\quad V_Y-W_Y
\in \mathcal Z_0
$$
分别保(13)的两个独立原头，直接证明原二维头被查询核覆盖。

还得到准确而尚未赋值的维数式
$$
\boxed{
\dim(Q_0/NQ_1)
=\operatorname{rank}S|_{\mathcal W_0}
-\operatorname{rank}S|_{\mathcal K_0}\in\{0,1,2\}.
}
\tag{37}
$$
R462 只已知
$3\le\operatorname{rank}S|_{\mathcal K_0}\le5$。
不能把成本维数7、5代进(37)直接宣余商为2，也不能把已知三个 self 列称为五个。

## 9. 第二原头 C20 的完整小公式

这一节推进(36)的实际原式入口，不重做旧成本秩。
其系数来自 R350(8)(14)(17)，由同锚分部积分即可得到。

用 profile 记号
$$
p=u',\quad r=u'',\quad t=u''',\quad
Jf(x)=\int_x^{r_*}f(y)\,dy,\quad
C=J(x^2r^2+2p^2).
$$
为取 $\bar A_{hh}$ 的 $h^{-2}k^0\omega^0$ 系数，在几何 $k=\omega=0$ 的状态 Laurent 式中令
$$
Q=1+h^2x^2,\qquad L=p-xr.
$$
R350 的二阶局部速度分量为
$$
a=-\frac1{8h^3}J(QLt)
=h^{-3}A_0+h^{-1}A_2,\qquad
A_2=-\frac18J(x^2Lt).
\tag{38}
$$
定义
$$
B=C+2xp^2-2x^2pr+x^3r^2.
$$
逐项微分给
$$
B'=-2x^2Lt,\qquad B(r_*)=0,
$$
所以
$$
A_2=-B/16.
\tag{39}
$$
在整个真左 collar，$B=\mu_2(u)$；这个常数一般非零。

由完整 self $\bar A_{hh}(u^2,0)=-Qa^2/(2h^2)$，取唯一 $h^{-2}$ 项即得
$$
\boxed{\Sigma_{C_{20}}(u)=-\frac{x^2B^2}{512}.}
\tag{40}
$$
它不是只保最高 jet 的式子。其 whole-self 左二次尾为
$$
\boxed{\mathcal Q(C_{20})(u)=-\mu_2(u)^2/2048,}
\tag{41}
$$
所以原 $C_{20}$ 本身不在 whole-E 核，不能拿(40)直接代替(23)中 $V_Y$ 的 self。

原 pure 的三阶几何伙伴同样保留。令
$$
J_1=J(x^2tB),\qquad J_2=J(x^2tJ_1).
$$
R350(17)中
$j=J(Qt\,a)$ 的最高 $h$ 项是 $-hJ_1/16$，
$k_1=J(Qt\,j)$ 的最高项是 $-h^3J_2/16$。
故原 $qq''$ 伙伴的同系数为
$$
\beta_{20}=\frac{-x^2LJ_1+xJ_2}{128}.
$$
保持 raw pure $=16\pi$ 的规范，得到
$$
\boxed{
16\pi C_{20}(u)
=-\frac{x^2B^2}{512}
+\frac{x^2(p-xr)J_1}{128}
-\frac{xJ_2}{128}.
}
\tag{42}
$$
$J_1,J_2$ 各自真实左尾也保留；没有假设它们紧支撑。

若仅需这个原头的一个 Af 部分积分入口，两次原分部给
$$
\int_{\ell}^{x}p\,\Sigma_{C_{20}}''
=-\frac1{512}
\left\{(2xp-x^2r)B^2+2x^2pBB'
+\int_{\ell}^{x}y^2u'''(y)B(y)^2\,dy\right\}.
\tag{43}
$$
在 $A_u=0$ 处，$pt=r^2/3$，于是中间项为
$-\tfrac43x^4r^2(p-xr)B$。
左端分部边界因真实输入 $p,r$ 零而消，并未把 $\Sigma$ 的二次左尾删除。

(40)—(43)是新纸面入口，不是已付两条成员的结论。继续到 $V_Y$ 必须先做**同一个完整成本**的 pure、whole-self 和 current 补偿，或使用已付完整关系(14)及 R333 的原 $J_4,J_6$ 组合。不能只删(41)，也不能用总 natural 恒零代替(43)的部分积分。

## 10. 对后继最小消费的准确要求

R462 已固定
$$
\mathcal K_0=
\operatorname{span}\{K_8,V_{51},V_{52}\}\oplus\mathscr B_2,
\qquad \dim\mathscr B_2=2.
\tag{44}
$$
前面三条是完整成本并已有完整 self current；后两条成本的 self 尚未支付。
本稿不重做 R316 的十三列、旧 whole-Q 秩7、R443十九行或 R434三十二行。

若纸面不能直接完成(36)，真正的新小目标应是：

1. 从已有完整原关系选择(44)的两个成本余部，保原 old-column 编号、完整 roots 与 SHA；新读它们的同锚 self 部分积分。
2. 固定(23)的两个完整目标，并将其完整 self 镜对读到同一个 $S$，保 whole-$E$ 和 current 补偿成本。
3. 用已有三个 self 列及这两个新 self 列，对两目标作一次共同成员比较；每个肯定成员仍要从原成本组合重构差并验证整个镜对多项式，而非仅若干最高系数。
4. 若目标的完整 self 还含固定 cap 的真实积分，必须保该输入和锚；不能擅用局部 jets 式代替。R459 的同矩 cap 转移负责最终全母库一致性，不能改成每母独立拟合。

以上是有限新目标的范围说明；本稿没有执行这些研究。式(40)—(43)可减少第二头需要恢复的原数据；但原 $C_{20}$ 的补偿关系仍须完整保留。新增计算如确必要，仍只由单独公开 Actions 入口执行，公开仅源/参数/metadata与人类结论，原 payload 只按既有规则临时消费。

## 11. 新增 partial 后，最低偶权 −8 可完整付清

本节给一个实际的后继闭合，不只是再次列出未付条件。
原 K 轨道的种子记为 $K_{\rm seed}$，即 R459 的 $K_0$；它是
$\mathcal R_{-8}$ 中的完整响应。这里不与五维空间 $\mathcal K_0$ 混淆。

R356 对整个 $U_{-8}$ 给
$$
\pi V=0,\qquad
\Sigma_V(u)=a\,\mathcal T_R(u)+b\,r^4,\qquad
\Lambda_{\rm all}(V)=0,
$$
$$
\mathcal T_R=4J^2(r^2t^2)-4J(prt^2)-r^4.
\tag{45}
$$
$a,b$ 依赖同一个成本 $V$，不依赖输入 profile 或根。$\mathcal T_R$ 的真左尾只为仿射，$r^4$ 左尾为零，故
$\mathcal Q(V)=0$。于是整个 $U_{-8}$ 都在 $\ker J_0$；universal natural 零也直接杀全部 ordered 行。

R462 的完整39 current 权表最低为 $-6$。故(45)层的形式 current 必零。这不是只在某个镜点的观察。
R459(21)—(23)保原同锚身份
$$
\mathcal T_R=-\frac16r^4-\frac13L_u\{P(u,u)\},
\qquad
\Sigma_{K_{\rm seed}}=-\frac13r^4,\qquad
P(u,u)=J(r^2).
\tag{46}
$$
因此同一个完整响应
$$
R_V=\left(\frac a2-3b\right)K_{\rm seed}
$$
满足
$$
\Sigma_{V-R_V}=-\frac a3L_u\{P(u,u)\}.
\tag{47}
$$
对真左锚到任意 Af 点 $\alpha$，原恒等式是
$$
\int_{\ell}^{\alpha}p\,L_u(P)''
=\left[A_u(pP''-rP')\right]_{\ell}^{\alpha}=0.
\tag{48}
$$
$P$ 在左侧可以有非零常数；消边项的是原输入 jets 和 Af 因子，并非虚构左紧性。式(48)不除以 $p$，也不依赖只存在一对根。

$V-R_V$ 的完整 current 零，故(32)同时消全部角色的右 suffix 项；(47)(48)消每一包的 self partial。它们对任意允许 profile、原宽度和平移都成立。因此也支付(4)的整个有限仿射闭包：
$$
\boxed{J_{\rm aff}(U_{-8})=J_{\rm aff}(\mathcal R_{-8}).}
\tag{49}
$$
反向包含由 $\mathcal R\subseteq U$，不需新的像计算。
同理 $\Sigma(U_{-9})=0$ 和原 pure/natural 零给
$J_{\rm aff}(U_{-9})=0$，但这里只需(49)排候选偶权 $-8$。

所以任何经这一次同一个 $J_{\rm aff}$ 下降、杀响应的 $-8$ 字符都为零。该结论没有使用(36)，也没有把 R356 夸成 $U_{-8}=\mathcal R_{-8}$ 的完整成本等式。

## 12. 其余实际满锥义务必须在同一增强上支付

若(36)成立，(1)只给同一 $Q$ 的 $DQ+NQ=Q$。
R463 的真实双参数引理还要求同一增强映射的满闭锥、原 prototype 正配平、真实桥、两次商基准与共同窗口。不能把有号 $W_H,W_Y$ 直接串接成负路径。

另一方面，若(36)不成立，则原双参数放大的这个 minor 不满；它不证明实际半群永远不能支付该目标。新的真实桥族、别的几何参数或其它实际构造仍需各自原式，不能从一个零权余商推出一般不可能性。

对满闭锥，(4)已使原 R127/R145 的单权提取合法；但旧 R433 的负权等式只匹配旧 $E,\mathcal A,\mathcal O_{\rm all}$。任何排字符时使用
$$
J(V-NZ-R)=0
$$
的地方，都必须在这一次同一原成本上保 $F_{\rm aff}$。自然 $\mathfrak d$ 的一致、旧 whole-E 等像或逐目标 signed 截面均不够。

即使(36)为真，权零正字符还需准确判定：$Q_0\subseteq NQ_1$ 会使所有同时杀 $N$ 与响应的增强权零字符为零，但只有当字符确经(4)下降时才能用此结论。本稿(49)已付最低偶权，原 $-2$ 的 whole-$U$ 排除与 $U_2=\mathcal R_2$ 也可按原范围保留。仍关键的是 $-6,-4$：旧 static、加速度与速度四次层所用的核身份必须在同一增强上保这些新 partial；若仍用 action/PSD 排除，必须保持同一个真实乘子及完整 prototype 基准。这里没有将它们重命名为已经完成的门。

本稿付清的是(1)的自然商同构、权零全角色核的精确必要充分形状、两个不可合并的原头、第二头的完整小 self/pure 原式，以及新增强的最低偶权(49)。下一决定性工作是(36)在同一五维响应镜对像中的实际成员性及同一个增强满锥；不是再增加固定宽度的 mixed-weight signed 列数。
