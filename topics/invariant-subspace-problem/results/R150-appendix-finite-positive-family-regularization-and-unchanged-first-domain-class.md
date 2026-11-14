# R150 附录：有限多正 first 的固定共同高阶域与正预解积不扩大行分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根完整核验混合参考态权预算、三个准确自然域和预解逐因子取消。依赖有限多正 first 共同图的系数分类；
高次必要性使用 R181 的实际乘积参考态尺度，不从一阶方差直接外推。

## 1. 结论与准确域

沿用有限正族
$$
a^\nu\ge0,\quad a^\nu\in\ell^2,\quad
X_\nu=X_{a^\nu},\quad1\le\nu\le q,\qquad
A_j=\sum_\nu a^\nu_j,
$$
允许零和可和行。取任意复 $c\in\ell^2$、$Y=Y_c$。

以下三种固定有限正则化都给同一系数条件：
$$
\boxed{
c=\sum_\nu\gamma_\nu a^\nu+e+d,\quad
e\in\ell^1,\quad d_j=0\ (A_j=0),\quad
\sum_{A_j>0}|d_j|^2/A_j<\infty.
}
\tag{1.1}
$$

**A. 全部固定共同词。** 对每个固定整数 $k\ge1$，
令 $\mathcal D_k$ 为 $X_1,\ldots,X_q$ 全部有序自然词、长度至多 $k$ 的共同域，
并同时记录所有这些词的图范数。则
$$
\boxed{\mathcal D_k\subseteq\operatorname{Dom}Y
\iff (1.1).}
\tag{1.2}
$$

**B. 各锚固定幂的交域。** 对任意固定整数 $N_\nu\ge1$，
$$
\boxed{
\bigcap_{\nu=1}^q\operatorname{Dom}X_\nu^{N_\nu}
\subseteq\operatorname{Dom}Y
\iff (1.1).
}
\tag{1.3}
$$
不把这个交域与某个完整混合词域认作相等。

**C. 全覆盖固定正预解积。** 对任意固定 $t_\nu>0$、$N_\nu\ge1$，
令
$$
R=\prod_{\nu=1}^q(I+t_\nu X_\nu)^{-N_\nu}\in A'.
\tag{1.4}
$$
按准确自然域定义 $YR$。
则
$$
\boxed{YR\text{ 在全 }H\text{ 上自然定义且有界}
\iff(1.1).}
\tag{1.5}
$$

这些条件因此都等价于
$\bigcap_\nu\operatorname{Dom}X_\nu\subseteq\operatorname{Dom}Y$。
全覆盖指每个使用的主行至少出现一次。
若只选择一个子族，则应对那个子族重新使用本定理，不可保留未使用的行。

## 2. 同一个共同核两态族的全部固定混合词预算

使用共同图分类证明中的实有限支撑列 $\theta$：
$$
\sum_j a^\nu_j\theta_j=0\quad(\nu=1,\ldots,q),\qquad
\sum_j A_j\theta_j^2\le1,\qquad
\|\theta\|_\infty\le1.
\tag{2.1}
$$
相应单位有限乘积态记为 $\xi(\theta)$。
每条纯 first 的中心
$$
\beta_\nu(\theta)
=\sum_j a^\nu_j(1-\sqrt{1-\theta_j^2})
$$
均在 $[0,1]$。

[R181](R181-bounded-coefficient-bell-polynomial-spectrum-trichotomy.md) §§2—3 在同一个任意有限乘积参考态 $h=\xi(\theta)$
的激发次数权 $\Lambda_h$ 上，给每条实际中心 first
$$
T_\nu=X_\nu-\beta_\nu I
$$
的完整域估计
$$
\|\Lambda_h^sT_\nu f\|
\le D_s\|a^\nu\|_2\|\Lambda_h^{s+1}f\|,
\qquad s=0,1,2,\ldots,
\tag{2.2}
$$
其中 $D_s$ 是只依赖模型和 $s$ 的固定常数。
真实 carry 的局部支撑与加权范数在任意参考态下都已支付。

因为 $\|\Lambda_h^kh\|=1$，
逐次使用 (2.2) 对任意有序词 $(\nu_1,\ldots,\nu_\ell)$ 得
$$
\boxed{
h\in\operatorname{Dom}(T_{\nu_1}\cdots T_{\nu_\ell}),\qquad
\|T_{\nu_1}\cdots T_{\nu_\ell}h\|
\le\left(\prod_{s=0}^{\ell-1}D_s\right)
\prod_{j=1}^{\ell}\|a^{\nu_j}\|_2.
}
\tag{2.3}
$$
这里每一步输入都在下一步所需的实际正权域；
没有先交换两个未知自然复合域。

再用 $X_\nu=T_\nu+\beta_\nu I$、$|\beta_\nu|\le1$，
每个固定有限词族的所有 $X$ 词作用都一致有界，
常数与 $\theta$ 的支撑及局部态无关。
特别，固定 $k$ 的共同词图范数、
固定各锚幂图范数，以及任何固定非交换写法的多项式
$P(X_1,\ldots,X_q)\xi(\pm\theta)$ 都有一致上界。

## 3. 共同高阶和各锚幂交域的必要性

R186 已证明全部低阶词同时记录的 $\mathcal D_k$ 图完备。
各单锚自然 $X_\nu^{N_\nu}$ 则由 R176 的单模式多项式闭性取准确闭实现；
所以它们的有限交域，配
$$
\|f\|^2+\sum_\nu\|X_\nu^{N_\nu}f\|^2,
$$
也是完备图空间。

若 (1.2) 或 (1.3) 左侧成立，
$Y$ 在对应图空间上闭，因而闭图定理给图范数界。
把 §2 的统一两态族代入，
$$
\sup_\theta\|Y\xi(\pm\theta)\|<\infty.
\tag{3.1}
$$
纯辅助的两个均值之差仍准确为
$2i\sum_jc_j\theta_j$，实际有界 carry 分别付范数。
因此 $C_0(\theta)=\sum c_j\theta_j$
在 (2.1) 的全部列上一致有界。

这正是
[有限多正 first 共同图分类](R150-appendix-finite-positive-first-joint-graph-coefficient-classification.md)
§§4—5 的输入。
在 $\mathscr E_A=c_0\cap\ell^2(A)$ 上，
对有限支撑共同线性核直接用 Hahn–Banach 延拓，
再经有限维 $\operatorname{Ran}T$ 的代数消元，给 (1.1)。
必要性不要求有限柱预先是各锚幂交域的共同图核心；
这里只需要它们真实入域及上面的闭图界。

反过来，(1.1) 已给共同一阶图包含于 $\operatorname{Dom}Y$。
(1.2) 和 (1.3) 的域各自包含于共同一阶图，
所以两个充分方向立即成立。

## 4. 正预解积的自然域、充分方向与必要预像

每个 $(I+t_\nu X_\nu)^{-1}$ 是实际正 first 的收缩预解，
属于 $A'$，保持其它 first 的完整域。
因此 (1.4) 是有界 $A'$ 算子，并且
$$
RH\subseteq\bigcap_\nu\operatorname{Dom}X_\nu,\qquad
X_\nu R\in B(H).
\tag{4.1}
$$
对最后一个结论，只需保留第 $\nu$ 个预解因子一次，
使用
$X_\nu(I+t_\nu X_\nu)^{-1}
=t_\nu^{-1}[I-(I+t_\nu X_\nu)^{-1}]$；
其余因子均有界并完整域交换。

自然 $YR$ 闭，因为 $R$ 有界而 $Y$ 闭。
其域稠密：取同时正则化全部主行及 $Y$ 的 R186 算子 $S(s)$，
使 $S(s)H\subseteq\operatorname{Dom}Y$、$S(s)\to I$ 强。
$R\in A'$ 保 $\operatorname{Dom}Y$，
故 $S(s)H\subseteq\operatorname{Dom}(YR)$。
一旦自然图有全域有界延拓，闭性及稠密性仍迫其自然域已全域。

若 (1.1) 成立，共同一阶图上的 $Y$ 界与 (4.1) 直接给 $YR$ 全域有界。

反过来，假设自然 $YR\in B(H)$。
定义固定有序自然多项式
$$
P=\prod_{\nu=1}^q(I+t_\nu X_\nu)^{N_\nu}.
$$
它在所有 §2 两态上真实有定义，且
$$
\sup_\theta\|P\xi(\pm\theta)\|<\infty.
\tag{4.2}
$$
按照完整自然词域逐个取消匹配的预解因子，
$$
RP\xi(\pm\theta)=\xi(\pm\theta).
\tag{4.3}
$$
此式只在已经付清的有限词输入上使用，
不把自然 $P$ 宣称为全域或自动闭。
令 $h_\theta=P\xi(\pm\theta)$，
由 (4.2)—(4.3) 得
$$
\|Y\xi(\pm\theta)\|
=\|YR h_\theta\|
\le\|YR\|\sup_\theta\|h_\theta\|<\infty.
$$
再用 §3 的同一两态/Hahn–Banach 输入，得到 (1.1)。
证明 (1.5)。

## 5. 其它固定预解点及边界

如果每个主行另外选定有限个真实预解点 $z_{\nu,\ell}\in\rho(X_\nu)$，
则可用任意固定乘积
$$
R=\prod_{\nu,\ell}(X_\nu-z_{\nu,\ell}I)^{-N_{\nu,\ell}},
\qquad
\sum_\ell N_{\nu,\ell}\ge1\quad\text{对每个 }\nu,
$$
替换 (1.4)，结论仍相同。
原预解都属于 $A'$；
(4.1) 用 $X_\nu(X_\nu-z)^{-1}=I+z(X_\nu-z)^{-1}$，
(4.2)—(4.3) 则用相应固定多项式。
若每条非零主行不可和，其空谱允许 $z=0$，
即得到全部固定正锚逆幂的全覆盖乘积。

本稿只处理固定有限词阶、固定有限锚族和固定有限预解积。
没有识别一般多元多项式逆的自然范围，
也不排除无限正预解乘积、无限阶分母或随测试变化的正则器。
共同高阶域、各锚幂交域与预解积的像在此不被混同；
只是它们对一阶辅助行的包含/有界性判据恰相同。
