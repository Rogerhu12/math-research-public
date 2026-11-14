# R236 附录：实际尾真空分离、精确支持提升与不一致的列修复

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的辅助结论。** 本文补足 R236 完整 good 首列稿的精确适用范围，并证明该范围在池宽可增长时不能仅用小的列残量替代。没有证明一般联合尾理想具有 good 支持，也未排除正常见证或关闭普通 ISP。

## 1. 实际尾真空分离全部尾块系数

沿用实际 Haar 张量表示，固定起点 $n$ 和有限池宽 $M$，写
$$
\mathscr H_n=K_M\otimes\mathscr H_{n+M},\qquad
K_M=(\mathbb C^2)^{\otimes M},\qquad
e_Mh=\Omega_M\otimes h.
$$
完整实际交换子为 $\mathcal C_j=\{\widehat N_j\}'$。
真实 dyadic 幂恒等式给
$$
\mathcal C_n\subset M_{2^M}(\mathcal C_{n+M}).
\tag{1.1}
$$
令 $\Omega=\Omega_{n+M}$。尾 $\Omega$ 对真实范数代数
$\mathcal B_{n+M}=\overline{\mathbb C[I,\widehat N_{n+M}]}$ 循环：
每个有限尾 Walsh 向量满足
$$
V_F\Omega=\chi_F,\qquad
V_F=\prod_{j\in F}(I-N_j)(I+N_j)^{-1}\in\mathcal B_{n+M}.
\tag{1.2}
$$
因此 $\Omega$ 对 $\mathcal C_{n+M}$ 分离。事实上，若
$b\in\mathcal C_{n+M}$ 且 $b\Omega=0$，则
$bV_F\Omega=V_Fb\Omega=0$；有限 Walsh 向量稠密，故 $b=0$。
这里不需要预先对 $\mathcal C_{n+M}$ 使用交换性。

**命题 1（任意头支持的单向量判据）。**
对任意 $G\in\mathcal C_n$ 和任意头正交投影 $P\in B(K_M)$，以下条件等价：
$$
(I-P\otimes I)G\Omega_n=0;
\tag{1.3}
$$
$$
(I-P\otimes I)Ge_M=0;
\tag{1.4}
$$
$$
\operatorname{Ran}(Ge_M)\subset\operatorname{Ran}P\otimes\mathscr H_{n+M}.
\tag{1.5}
$$

证明：后两式等价，(1.4) 显然蕴含 (1.3)。选取 $K_M$ 的任意正交基，
把列 $(I-P\otimes I)Ge_M$ 写成有限个系数 $b_i$。
由 (1.1)，每个 $b_i\in\mathcal C_{n+M}$。
若 (1.3) 成立，则各 $b_i\Omega=0$；分离性逐项给 $b_i=0$，即 (1.4)。证毕。

这个等价不要求 $P$ 为物理坐标投影，也不要求其支持向上闭。
更一般地，对任意固定有限头矩阵 $Q$，
$QG\Omega_n=0$ 与 $QGe_M=0$ 等价。
它只提升**精确的零式**，没有给从 $\|QG\Omega_n\|$ 到
$\|QGe_M\|$ 的统一算子范数逆估计。

## 2. 对实际 good 目标范围的加强

对 $F\subset\{1,\ldots,M\}$，令
$$
\mathcal G_{q,M}=
\left\{F:\max_{1\le r\le M}
\bigl(2|F\cap\{1,\ldots,r\}|-r\bigr)\ge q\right\},
$$
并令 $P_{q,M}$ 为对应物理坐标投影。
R236《吸收路径的完整源因式分解与指定目标费用》§10 已证明：
对 $M\ge q\ge512$，若实际 $G\in\mathcal C_n$ 满足完整首列条件
$(I-P_{q,M})Ge_M=0$，则
$$
|\omega_n(G)|\le a_{n,q,M}\|G\|,
\qquad
a_{n,q,M}=4\sqrt2\,e^{-q/64}
\left(1+2M10^{M/2}\bar\eta_n\right).
\tag{2.1}
$$
其中 $\omega_n(G)=\langle G\Omega_n,\Omega_n\rangle$，
$\bar\eta_n\le e^{-770\cdot16^n}$ 是实际 carry 上界。

命题 1 表明，(2.1) 的假设可以等价写成单向量条件
$$
\boxed{G\Omega_n\in\operatorname{Ran}P_{q,M}\otimes\mathscr H_{n+M}.}
\tag{2.2}
$$
因此原稿 §10.1 和 §10.7 中“不足以只知道单个 $G\Omega$ 的精确支持”的守卫可去掉；
精确支持本身已足够。其余实际 carry、$M=o(16^n)$、统一范数和正常配对预算原样保留。
特别，在 $n,q\to\infty$、$q\le M=o(16^n)$ 下，
全部满足 (2.2) 的 $G/\|G\|$ 仍一致 WOT 趋零，并对每个固定正常泛函一致趋零。

这个加强没有声称任意 $G\in\mathcal C_n$ 或完整联合尾交中的元素都满足 (2.2)。

## 3. 近支持不能替代精确支持：实际单位的反例

以下构造完全使用实际单位算子，因而不受 carry 影响。
取 $G=I\in\mathcal C_n$。令 $\varepsilon_1,\ldots,\varepsilon_M$ 为独立均匀的 $\pm1$，
$S_r=\sum_{j=1}^r\varepsilon_j$。参考向量的物理坐标均匀，故
$$
p_{q,M}:=\|(I-P_{q,M})\Omega_M\|^2
=\mathbb P\left(\max_{r\le M}S_r<q\right).
\tag{3.1}
$$
对 $q\ge1$，在首次到达 $q$ 后反射余下路径，是从
$\{\max S_r\ge q,S_M<q\}$ 到 $\{S_M>q\}$ 的概率保持双射。
结合终点分布关于零对称，得到准确恒等式
$$
p_{q,M}=\mathbb P(-q\le S_M<q).
\tag{3.2}
$$
该半开区间中至多有 $q$ 个可能终点。二项分布的最大单点概率满足
$$
\max_k2^{-M}{M\choose k}\le\sqrt{\frac2{M+1}}.
\tag{3.3}
$$
为自足地验证此界，置 $b_l=4^{-l}{2l\choose l}$。
$b_0=1$ 且 $b_{l+1}/b_l=(2l+1)/(2l+2)$。
不等式
$(2l+1)^2(l+2)\le4(l+1)^3$
归纳给 $b_l\le1/\sqrt{l+1}$；奇数长度的最大质量不大于相邻偶数长度的 $b_l$。
这就给出 (3.3)。

于是
$$
p_{q,M}\le q\sqrt{\frac2{M+1}},\qquad
\boxed{
\|(I-P_{q,M})I e_M\|=\sqrt{p_{q,M}}
\le2^{1/4}q^{1/2}(M+1)^{-1/4}.
}
\tag{3.4}
$$
这里左侧是**完整列算子范数**，不仅是单向量误差。

例如取 $q=n\to\infty$、$M=n^4$，则 $M=o(16^n)$、
完整坏列范数为 $O(n^{-1/2})\to0$，但
$$
\|G\|=\omega_n(G)=1.
\tag{3.5}
$$
故在现有合法池宽预算内，连“完整列到 good 空间的相对距离趋零”
也不能代替精确支持来推出统一弱零。
这不是实际联合尾理想的反例，因为单位没有被置入该理想。

## 4. 精确解析修复的费用确实爆炸

令 $B_{n,q,M}\in\mathcal C_n$ 为坏列的真实 Walsh 提升：
$$
B_{n,q,M}=\mathfrak L_M(I-P_{q,M}),\qquad
B_{n,q,M}e_M=(I-P_{q,M})e_M.
\tag{4.1}
$$
这是 R236 算子值首列稿 §7 的完整实际提升；其条目为池后标量单位，
故此 $B$ 还属于实际范数尾代数。忠实首列使它唯一。
令 $A_{n,q,M}=I-B_{n,q,M}$。它的首列准确支持 good，且
$$
\omega_n(B_{n,q,M})=p_{q,M},\qquad
\omega_n(A_{n,q,M})=1-p_{q,M}.
$$
由 (2.1)，
$$
\boxed{
\|B_{n,q,M}\|
\ge\frac{1-p_{q,M}}{a_{n,q,M}}-1.
}
\tag{4.2}
$$
在 $q=n,M=n^4$ 下，$p_{q,M}\to0$，carry 因子趋一，所以
$$
\|B_{n,n,n^4}\|
\ge\left(\frac1{4\sqrt2}+o(1)\right)e^{n/64}-1,
\qquad
\|B_{n,n,n^4}e_{n^4}\|=O(n^{-1/2}).
\tag{4.3}
$$
因此小的完整坏列在提升回实际交换子后，所需范数确实可以指数增长。
这不是仅仅现有提升上界过粗的可能性。

还可给一个不依赖指定修复的算子距离结论。令
$$
\mathcal S_{n,q,M}
=\{F\in\mathcal C_n:(I-P_{q,M})Fe_M=0\}.
$$
若 $a_{n,q,M}<1$，对任意 $F\in\mathcal S_{n,q,M}$、$d=\|I-F\|$，
有 $1-d\le|\omega_n(F)|\le a_{n,q,M}(1+d)$。故
$$
\boxed{
\frac{1-a_{n,q,M}}{1+a_{n,q,M}}
\le\operatorname{dist}(I,\mathcal S_{n,q,M})\le1.
}
\tag{4.4}
$$
沿上述尺度，该距离趋一，尽管单位的完整首列到 good 支持空间的距离趋零。

## 5. 对当前实际问题的准确影响

精确的单向量零式可以利用尾循环性升级成所有尾向量的列零式；
这适用于全部实际交换子，不限制路径表示或两模式多项式。
另一方面，小的正常态尾误差、小的真空向量误差、甚至小的完整列误差，
若没有同时支付解析提升的实际范数，均不能直接替代该精确零式。
完整联合尾理想是否具有某种可支付的来源特殊修复、或可获得非零正常锚，仍为原问题。

### 已使用的仓库内完整证明

- R253《正部分迹、有限 dyadic 相位乘积消元与正常尾的必要下界》§1：实际尾真空循环性。
- R236《算子系数 Walsh 首列提升、联合最大子式与精确一次尾交》§§2–3、7：真实块系数、忠实首列及完整交换子提升。
- R236《吸收路径的完整源因式分解与指定目标费用》§10：带实际 carry 的统一 good 支持锚上界。
