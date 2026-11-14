# R150 附录：全部固定逆幂与有限多项式分母的一阶域分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf / normal_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根与 normal 均回读 R181 §§2—3 并完整核验全部固定幂的产品态预算及自然商域。承接已推一阶有界比率充要分类，新增全部固定逆幂和有限多项式分母的准确相同边界。
R201/R181 旧 all-powers 反例只作为先前范围扣除，不重复计作新反例。

## 1. 定理

设
$$
a_j\ge0,\qquad a\in\ell^2\setminus\ell^1,\qquad
X=X_{\sum a_j\chi_j},\qquad L=X^{-1},
$$
并取任意复 $c\in\ell^2$、实际 $Y=X_{\sum c_j\chi_j}$。
固定整数 $N\ge1$。
则下列条件等价：

1. $\operatorname{Dom}X^N\subseteq\operatorname{Dom}Y$。
2. 自然算子 $YL^N$ 的域为全 $H$，且它有界。
3. 存在固定 $M_N<\infty$，对全部有限 Walsh 柱 $f$ 有
   $$
   \|Yf\|\le M_N\|X^Nf\|.
   \tag{1.1}
   $$
4. $\operatorname{Dom}X\subseteq\operatorname{Dom}Y$。
5. 存在唯一 $\gamma\in\mathbb C$，以及 $e\in\ell^1$、复行 $d$，使
   $$
   \boxed{
   c=\gamma a+e+d,\qquad
   d_j=0\ (a_j=0),\qquad
   \sum_{a_j>0}\frac{|d_j|^2}{a_j}<\infty.
   }
   \tag{1.2}
   $$

因此一个固定正次数逆幂不能给一阶辅助行扩大相对域范围。
等价地，对每个 $N\ge1$，
$$
\boxed{
\operatorname{Dom}X^N\subseteq\operatorname{Dom}Y
\iff
\operatorname{Dom}X\subseteq\operatorname{Dom}Y.
}
\tag{1.3}
$$
不将这个结论扩到无限阶分母。

还可把 $X^N$ 换成任意一个固定自然多项式
$$
P(X)=\sum_{k=0}^NE_kX^k,\qquad
E_k\in A',\quad E_N\in(A')^\times,\quad N\ge1.
\tag{1.4}
$$
R134/R176 给其准确闭域 $\operatorname{Dom}X^N$ 和实际有界逆。
自然 $YP(X)^{-1}$ 全域有界当且仅当 (1.2) 成立。

## 2. 自然商的闭性与充分方向

自然定义
$$
\operatorname{Dom}(YL^N)
=\{h:L^Nh\in\operatorname{Dom}Y\}.
$$
因为 $L^N$ 有界而 $Y$ 闭，$YL^N$ 闭。
又 $L^NH=\operatorname{Dom}X^N$，所以条件1等价于自然域全 $H$；
闭图定理给条件1与2等价。

这个自然域本身稠密：
取 [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) 同时正则化 $X,Y$ 的 $R(t)$，其像在 $\operatorname{Dom}Y$，
且 $R(t)\to I$ 强。
$L^N\in A'$ 保 $\operatorname{Dom}Y$，故
$$
R(t)H\subseteq\operatorname{Dom}(YL^N).
$$
因此若自然图仅被声称有一个全域有界延拓，闭性和稠密性仍迫其自然域全域。
这里没有使用未识别的初始商。

条件2给条件3，因为有限柱属于每个实际自然 $X$ 幂域，
且 $L^NX^Nf=f$。

[一阶完整系数分类](R150-appendix-positive-anchor-first-ratio-complete-coefficient-classification.md)
已证明条件4与5等价。
若条件4成立，则 $YL$ 有界，实际完整域给
$$
YL^N=(YL)L^{N-1}\in B(H),
$$
所以条件2成立。

剩下的唯一新增方向是条件3迫条件5。
必须为分类稿的全部两态测试支付固定 $X^N$ 界；
一阶方差本身不能替代这个步骤。

## 3. R181 的真实高次输入对全部两态统一适用

对实有限支撑列 $\theta$，假设
$$
\sum_ja_j\theta_j=0,\qquad
\sum_ja_j\theta_j^2\le1,\qquad
\|\theta\|_\infty\le1.
\tag{3.1}
$$
沿用完整分类稿的单比特单位态
$$
\xi_{\theta_j}
=\cos\beta_j\,1+i\sin\beta_j\,\chi_j,\qquad
\beta_j=-\tfrac12\arcsin\theta_j,
$$
及有限乘积
$$
\xi(\theta)=\bigotimes_j\xi_{\theta_j}.
$$
其纯主行均值
$$
\beta(\theta)=
\sum_j a_j\left(1-\sqrt{1-\theta_j^2}+i\theta_j\right)
=\sum_j a_j\left(1-\sqrt{1-\theta_j^2}\right)
$$
在 $[0,1]$，对 $\pm\theta$ 相同。

[R181](R181-bounded-coefficient-bell-polynomial-spectrum-trichotomy.md)
§§2—3，特别式 (3.6)，对任意有限乘积参考态给
$$
\boxed{
\xi(\theta)\in\operatorname{Dom}X^k,\qquad
\|(X-\beta(\theta)I)^k\xi(\theta)\|
\le C_k\|a\|_2^k.
}
\tag{3.2}
$$
这里取该稿的尾起点 $m=0$。
它的 §§2—3 估计不使用后面全平面谱的相位假设；
故可用于当前正空谱行。

为明确 carry 已支付：
R181 在以任意参考态为真空的激发次数权 $\Lambda_h$ 上证明
$$
\|\Lambda_h^s(X-\beta I)f\|
\le D_s\|a\|_2\|\Lambda_h^{s+1}f\|,
$$
其中
$$
D_s=6(2^s+2)+
18\|\eta\|_2\sum_{\ell\ge1}(\ell+2)^s\eta_*^{\ell-1}.
$$
每个真实 carry 字串只作用有限长度的位集合，
换参考态不改变其支撑和范数；
全部局部级数在这个加权算子范数中绝对收敛。
逐次闭性遂给实际自然域及
$C_k=\prod_{s=0}^{k-1}D_s$，$C_0=1$。
常数与 $\theta$ 的有限支撑和具体局部态无关。
这里没有把一个一般有界 carry 当作自动保持纯算子高幂域。

对固定 $N$，在已付清的自然域上使用标量二项式及 $|\beta|\le1$，
$$
\boxed{
\|X^N\xi(\pm\theta)\|
\le K_{N,a}:=
\sum_{k=0}^N\binom Nk C_k\|a\|_2^k<\infty.
}
\tag{3.3}
$$
这正是条件3所需的统一高次测试预算。

## 4. 两态测试、连续延拓和相同分类

设条件3成立。
由 (3.3)，
$$
\|Y\xi(\pm\theta)\|\le M_NK_{N,a}.
$$
对纯辅助算子 $Y^0=\sum c_jS_j$，
两个均值的准确差为
$$
\langle Y^0\xi(\theta),\xi(\theta)\rangle
-\langle Y^0\xi(-\theta),\xi(-\theta)\rangle
=2i\sum_jc_j\theta_j.
$$
真实 carry $E_c=Y-Y^0$ 有界，
$\|E_c\|\le8\|\eta\|_2\|c\|_2$；分别对两次均值付其范数，
得到
$$
\left|\sum_jc_j\theta_j\right|
\le M_NK_{N,a}+\|E_c\|.
\tag{4.1}
$$

这就是完整一阶分类稿 §4 的同一个泛函输入，只有常数改变。
为使逻辑闭合，重述其后续步骤。
在
$$
\mathscr E=c_0\cap\ell^2(a),\qquad
\|z\|_{\mathscr E}=
\max(\|z\|_\infty,\sqrt{\sum a_j|z_j|^2})
$$
中，(4.1) 通过齐次性和实虚分开，给
$C_0(z)=\sum c_jz_j$
在有限支撑 $\ker A_0$ 上有界，
其中 $A_0(z)=\sum a_jz_j$。

这个核稠密，因为
$h_F=1_F/\sum_Fa_j$ 满足 $A_0h_F=1$、$\|h_F\|_{\mathscr E}\to0$。
所以 $C_0|_{\ker A_0}$ 连续延拓为 $\ell\in\mathscr E^*$，
并且 $C_0-\ell=\gamma A_0$ 于有限支撑列。
将 $\mathscr E$ 等距嵌入
$c_0\oplus_\infty\ell^2$，
复 Hahn–Banach 给 $\ell=e+d$，
其中 $e\in\ell^1$、$d_j=\sqrt{a_j}b_j$、$b\in\ell^2$。
这正是 (1.2)，包括零 $a_j$ 位的可和条件。
唯一 $\gamma$ 已由原分类稿的有限集部分和比证明。
因此条件3迫条件5，完成全部等价。

## 5. 任意固定有限多项式分母

对 (1.4)，令
$$
Q=E_N+\sum_{k<N}E_kL^{N-k}
=E_N(I+LD)
$$
其中 $D\in A'$ 有界。
$L$ 拟幂零且与 $D$ 交换，所以 $I+LD$ 是实际单位。
R134/R176 给
$$
P(X)=QX^N,\qquad
\operatorname{Dom}P(X)=\operatorname{Dom}X^N,\qquad
P(X)^{-1}=L^NQ^{-1}.
\tag{5.1}
$$
其逆的像准确为 $\operatorname{Dom}X^N$。

因此自然 $YP(X)^{-1}$ 全域当且仅当
$\operatorname{Dom}X^N\subseteq\operatorname{Dom}Y$；
一旦全域，闭图定理给有界。
由主定理，这又当且仅当 (1.2)。

这包括任意固定的有限乘积
$\prod_\nu(X-z_\nu I)^{m_\nu}$ 及其逆，
只要总次数至少1。
所有 $z_\nu\in\mathbb C$ 均为 $X$ 的预解点，
但不需要用一个形式分式来替代其自然域。

## 6. 与旧障碍及剩余问题的区别

此前 R201 的两块非比例正行，以及随后的 all-fixed-power 审计，
已经给具体辅助行在每个固定逆幂后仍无界。
本稿把这些例子提升为任意复 $\ell^2$ 辅助行的完整系数等价分类，
并付清了相同两态族的每个真实固定高次幂。

若 (1.2) 失败，则对每个固定 $N\ge1$，
自然 $YL^N$ 均非全域有界，且没有全域有界延拓；
每个固定 (1.4) 分母也一样。
这不排除无限阶、非多项式或随测试改变的正则器，
不推出对应点态多项式有非零核，
也不解决一般正常见证的聚合成本或完整 ISP。
