# R191：两个具体慢符号的精确混合型与快分式域外的超越方向

日期：2026-11-12（UTC）。作者：root。l2_moments 独立核验主要矩阵元、Cayley 模型误差及分式反证。

状态：完整证明。本稿给原全空间上的精确范数幂型，并证明 R185/R188 的两个具体慢符号不属于快分式域。没有把边界范数测试向量送入未知 Haar 不变空间，因而未声明相同混合型在所有限制或子商上成立。

## 1. 两个实际慢元素

沿用
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
N_j=A^{2^j}/d_j,\quad d_j=\|A^{2^j}\|,\qquad
Y_j=N_j(I+N_j)^{-1}.
$$
取
$$
a_j=(j+1)^{-2},\qquad M=\sum_{j\ge0}a_j\le2,
$$
并定义
$$
S=\sum_{j\ge0}a_jN_j,\qquad
S_1=\sum_{j\ge0}a_jY_j.
\tag{1.1}
$$
两级数均按算子范数绝对收敛。
R185、R188 已证明它们在原 $H$ 上单射、像稠密，
但各自的范数闭主理想均不包含任何 $A^n$。
$S_11$ 是明确的连续、非负、零锚第一阶符号。

记
$$
c_*=\frac{100}{15},\qquad
\tau_4(T)=\liminf_{n\to\infty}\frac{-\log\|T^n\|}{n^4}.
$$

**主定理。** 对任意整数 $r,k\ge0$，
$$
\boxed{\tau_4(A^rS^k)=\tau_4(A^rS_1^k)=c_*r^4.}
\tag{1.2}
$$
特别两个慢符号的每个正次幂都具有零四次型。

令 $\mathcal G$ 为 R151 的快解析逼近代数，
$K=\operatorname{Frac}\iota(\mathcal G)$。
则
$$
\boxed{\iota(S),\iota(S_1)\notin K,\qquad S-S_1\in\mathcal G.}
\tag{1.3}
$$
它们给同一个非零加性类模 $K$，该类超越于 $K$。
更强地，对任意在零附近解析的非恒定标量函数 $q$，
$$
\boxed{\iota(q(S)),\iota(q(S_1))\notin K.}
\tag{1.4}
$$
这里 $q(S)$ 使用拟幂零有界算子的真实解析演算。

## 2. 实际权和原全空间精确型

R174 的连续边界表示作用于 $\ell^2(\mathbb N_0)$：
$$
B=\pi_-(A),\qquad Be_0=0,\qquad
Be_n=\alpha_{v_2(n)}e_{n-1}.
$$
全部权正，且
$$
\|B^n\|=\|A^n\|=W_n,\qquad
(B^*)^ne_0=W_ne_n.
\tag{2.1}
$$
因此对任意向量 $v$，
$$
\langle B^nv,e_0\rangle=W_n\langle v,e_n\rangle.
\tag{2.2}
$$
本稿只需 $\pi_-$ 为收缩表示，故边界矩阵元给原算子范数的下界。
它不提供未知 Haar 限制上的下界。

实际权公式是
$$
-\log d_j=100\,16^j-105\,8^j+(150j+25)2^j,
\qquad W_n=\prod_{\text{二进位 }j\text{ 为1}}d_j.
\tag{2.3}
$$
记 $D_4(n)=\sum_{j:n_j=1}16^j$。
则
$$
-\log W_n=100D_4(n)+O(n^3+n\log(n+1)).
\tag{2.4}
$$
有 $n^4\le15D_4(n)$。可按最高位归纳：
若 $n=a+x$、$a$ 为2的幂、$0\le x<a$，
则 $(a+x)^4-x^4\le15a^4$，再用归纳假设。

对固定 $r\ge1$，取
$$
n_j=\left\lfloor\frac{2^j-1}{r}\right\rfloor,\qquad
rn_j=2^j-t_j,\quad1\le t_j\le r.
$$
补位公式给
$$
D_4(rn_j)=\frac{16^j-1}{15}-D_4(t_j-1).
$$
所以
$$
\boxed{
\liminf_{n\to\infty}\frac{-\log W_{rn}}{n^4}=c_*r^4.
}
\tag{2.5}
$$
$r=0$ 时 $W_0=1$，相应极限为0。

对任意固定有界交换因子 $T$，
$$
\|A^{rn}T^{kn}\|\le W_{rn}\|T\|^{kn}.
$$
因此 (1.2) 的型下界立即成立。
剩下要证明混合幂不会比 $W_{rn}$ 多损失四次尺度。

## 3. 正慢符号 S 的精确选孔矩阵元

在边界上记
$$
\mathsf N_j=B^{2^j}/d_j,\qquad T=\pi_-(S)=\sum_j a_j\mathsf N_j.
$$
若整数 $\ell$ 的第 $j$ 位为1，则实际进位公式给
$$
\boxed{\mathsf N_j e_\ell=e_{\ell-2^j}.}
\tag{3.1}
$$
这是准确等式，不含尾误差。
若该位为0，仍只产生非负实系数的加权后移。

固定 $r\ge0,k\ge1$，令
$$
p=kn,\qquad
m=\left\lceil\log_2((r+k+1)n+1)\right\rceil+3,
\qquad
J=\{m,m+1,\ldots,m+p-1\}.
\tag{3.2}
$$
于是 $rn<2^m$。
置
$$
\ell=rn+\sum_{j\in J}2^j.
$$
输入 $e_\ell$ 的低头为 $rn$，选定 $p$ 个高位全有孔。

在 $T^p$ 的展开中，从这 $p$ 个不同指标各取一次。
任意顺序都可用 (3.1) 精确消去对应的孔，且共有 $p!$ 个次序。
其他全部路径的矩阵元非负，所以
$$
\langle T^pe_\ell,e_{rn}\rangle
\ge p!\prod_{j\in J}a_j.
\tag{3.3}
$$
范数收敛和非负系数允许从有限部分和通过极限保留这个下界。
由 (2.2)，
$$
\boxed{
\|A^{rn}S^{kn}\|
\ge\|B^{rn}T^p\|
\ge W_{rn}\,p!\prod_{j=m}^{m+p-1}a_j.
}
\tag{3.4}
$$

对每个选定位有 $a_j\ge(m+p)^{-2}$。
所以
$$
p!\prod_{j=m}^{m+p-1}a_j\ge(m+p)^{-2p}
=\exp(-O_{r,k}(n\log(n+1))).
\tag{3.5}
$$
由 (2.5)，额外对数项是 $o(n^4)$，
得到
$$
\tau_4(A^rS^k)=c_*r^4.
$$

## 4. Cayley 慢符号 S1 的全边界范数模型

Cayley 系数可能有交替符号，不能直接对 $S_1^p$ 使用正路径论证。
本节用可量化的整个边界算子范数逼近保留同一个矩阵元。

记纯孔消灭算子为 $\mathsf E_i$。
实际递推展开给
$$
\mathsf N_i
=\mathsf N_i^{[m]}
+\frac{\alpha_m}{\alpha_i}
 \mathsf E_i^*\cdots\mathsf E_{m-1}^*\mathsf N_m
\quad(i<m),
\tag{4.1}
$$
其中 $\mathsf N_i^{[m]}$ 是低 $m$ 位有限头算子，扩张时在尾上张量恒等。
因此这次有真正的全空间范数估计
$$
\|\mathsf N_i-\mathsf N_i^{[m]}\|
\le\alpha_m/\alpha_i.
\tag{4.2}
$$

实际及有限头的 $(I+\mathsf N_i)^{-1}$ 范数均小于3。
由逆差恒等式，
$$
\|\mathsf Y_i-\mathsf Y_i^{[m]}\|
\le9\alpha_m/\alpha_i
\quad(i<m),
\tag{4.3}
$$
其中 $\mathsf Y_i=\mathsf N_i(I+\mathsf N_i)^{-1}$。
对尾位则由
$\mathsf N_i^2=\eta_i\mathsf N_{i+1}$ 得
$$
\|\mathsf Y_i-\mathsf E_i\|\le4\eta_i.
\tag{4.4}
$$
这些均是算子范数估计，不涉及某个未知向量的尾速率。

定义
$$
T_1=\pi_-(S_1),\qquad
C_m=T_{1,m}\otimes I+\sum_{j\ge m}a_j\mathsf E_j,
\tag{4.5}
$$
其中 $T_{1,m}=\sum_{i<m}a_i\mathsf Y_i^{[m]}$。
尾级数按范数收敛。
有
$$
\|T_1\|\le6,\qquad \|C_m\|\le8,
$$
以及
$$
\begin{aligned}
\|T_1-C_m\|
&\le9\sum_{i<m}a_i\frac{\alpha_m}{\alpha_i}
 +4\sum_{i\ge m}a_i\eta_i\\
&\le13M\eta_{m-1}\le26\eta_{m-1}.
\end{aligned}
\tag{4.6}
$$
于是有限幂的望远镜恒等式给
$$
\boxed{\|T_1^p-C_m^p\|
\le26p\,8^{p-1}\eta_{m-1}.}
\tag{4.7}
$$
这里不需要 $T_1$ 与 $C_m$ 交换。

## 5. 模型的矩阵元及误差支付

继续使用 (3.2) 的 $p,m,J,\ell$。
在 $C_m^p$ 中，欲把 $p$ 个高孔全部消去并到达 $e_{rn}$，
每一步都必须取一个高尾消灭项。
任何低头项都不能改变高孔数；
只有 $p$ 步，使用低头项后就不可能清完全部 $p$ 个高孔。
因此
$$
\boxed{\langle C_m^p e_\ell,e_{rn}\rangle
=p!\prod_{j\in J}a_j.}
\tag{5.1}
$$
这一等式没有要求头算子的矩阵元为正。

记右侧为 $c_n>0$。
由 (3.5)，$-\log c_n=O(n\log(n+1))$ 的上界足够。
而 (3.2) 使 $m=O(\log n)$，同时
$$
16^{m-1}\ge256((r+k+1)n+1)^4.
$$
结合 $\eta_{m-1}\le e^{-770\,16^{m-1}}$，
$$
26p8^{p-1}\eta_{m-1}=o(c_n).
\tag{5.2}
$$
这是明示常数和已选范数测试向量的比较；
没有拿一个无速率的强极限去除慢系数。

所以充分大 $n$ 时，由 (2.2)、(4.7)、(5.1)，
$$
\begin{aligned}
\|A^{rn}S_1^{kn}\|
&\ge\|B^{rn}T_1^p\|\\
&\ge W_{rn}\left(c_n-26p8^{p-1}\eta_{m-1}\right)\\
&\ge\tfrac12 W_{rn}c_n.
\end{aligned}
\tag{5.3}
$$
结合上界及 (2.5)，得到
$$
\tau_4(A^rS_1^k)=c_*r^4.
$$
$k=0$ 是 (2.5)，$r=k=0$ 是恒等算子。
主定理 (1.2) 的全部情形已完成。

## 6. 快逼近与谐和型的准确输入

R151 给以下事实：

- 每个 $0\ne b\in\mathcal G$ 有真实解析逼近 $b_n(A)$，
  其余项 $E_n=b-b_n(A)$ 满足 $\tau_4(E_n)\to\infty$；
- 有限形式 jet 最终精确一致；
- 若 $\operatorname{ord}\iota(b)=r$，则
  $\tau_4(b)=c_*r^4$；
- 当 $n$ 足够大时，
  $b_n(A)=A^rU_n$，其中 $U_n$ 是真实解析单位。

各 $U_n$ 的范数及逆范数可以依赖 $n$。
每次型计算先固定这个逼近指标，再令幂次趋无穷。

若有限多个有界交换算子 $T_i$ 满足 $\tau_4(T_i)\ge b_i>0$，
交换幂展开及
$$
\sum_i b_i n_i^4
\ge\frac{(\sum_i n_i)^4}{(\sum_i b_i^{-1/3})^3}
$$
给
$$
\boxed{
\tau_4\left(\sum_iT_i\right)
\ge\left(\sum_i b_i^{-1/3}\right)^{-3}.
}
\tag{6.1}
$$
指数多项式系数只增加 $O(n)$ 对数项。
无穷型按逆三次方根为0处理；严格论证可先取任意有限下界再上升。
乘以一个固定有界交换因子不降低型；
乘以一个固定有界交换单位则准确保持型。

## 7. 两个慢符号及其解析函数不在 K

统一取 $T=S$ 或 $T=S_1$。
它的形式阶为1，首系数为 $a_0/d_0\ne0$。
设 $q$ 为非恒定真实解析芽，写
$$
q(T)-q(0)I=T^kV,\qquad k\ge1,
\tag{7.1}
$$
其中 $V$ 是有界解析单位，属于 $\mathcal A$。
因此
$$
\operatorname{ord}\iota(q(T)-q(0)I)=k,
\qquad
\tau_4(A^r(q(T)-q(0)I))=c_*r^4
\tag{7.2}
$$
对每个 $r\ge0$ 成立。

假设 $\iota(q(T))\in K$。
因为常数属于 $K$，存在 $a,b\in\mathcal G$、$b\ne0$，使
$$
\iota(q(T)-q(0)I)=\frac{\iota(a)}{\iota(b)}.
$$
有限清分母及 $\mathcal A$ 中形式嵌入的忠实性给真实有界恒等式
$$
a=b(q(T)-q(0)I).
\tag{7.3}
$$
设 $\operatorname{ord}b=r$。
由 (7.2)，$\operatorname{ord}a=r+k$，故
$$
\tau_4(a)=c_*(r+k)^4.
\tag{7.4}
$$

选 §6 的快逼近
$$
b=A^rU_n+E_n.
$$
(7.3) 给
$$
A^rU_n(q(T)-q(0)I)
=a-E_n(q(T)-q(0)I).
\tag{7.5}
$$
左侧由 (7.2) 和单位 $U_n$ 具有精确型 $c_*r^4$。
右侧第一项具有 (7.4) 的严格更大型；
第二项的型至少为 $\tau_4(E_n)\to\infty$。
由 (6.1)，右侧的型下界趋于
$$
c_*(r+k)^4>c_*r^4,
$$
矛盾。
$r=0$ 时左侧型为0，右侧充分大时已经有严格正型，同样矛盾。

故 (1.4) 成立；取 $q(t)=t$ 即得到两个符号都不在 $K$。

该结论比“它们不属于 $\mathcal G$”更强。
分式分母可能有任意有限正阶，(7.5) 已完整处理这种情形，
没有只比较 $T$ 自身的零型与快代数的正阶型。

## 8. 它们具有同一个显式非零加性类

实际恒等式给
$$
N_j-Y_j=N_j^2(I+N_j)^{-1}
=\eta_jN_{j+1}(I+N_j)^{-1}.
$$
所以
$$
\boxed{
S-S_1=\sum_{j\ge0}
a_j\eta_jN_{j+1}(I+N_j)^{-1}.
}
\tag{8.1}
$$
每个 $(I+N_j)^{-1}$ 是真实解析芽在 $A$ 上的求值，范数统一小于3。
把它除以3后，系数变为 $3a_j\eta_j$。
这些系数满足
$$
-\log(3a_j\eta_j)\ge770\,16^j-O(1),
$$
故重排后三次衰减指标为无穷。
这正落入 R179 的真实快尾子代数 $\mathcal T$：
$$
S-S_1\in\mathcal T\subseteq\mathcal G.
\tag{8.2}
$$
这里每项解析因子及归一化幂 $N_{j+1}$ 都已明确，
不是仅用一个范数小量把差收入 $\mathcal G$。

对每个 dyadic gauge，充分高的 $N_j,Y_j$ 均固定，
所以 $\gamma_\zeta S-S$ 和 $\gamma_\zeta S_1-S_1$ 只含有限个真实解析项，
均属于 $\mathcal G$。

因此
$$
[\iota(S)]=[\iota(S_1)]\ne0
\quad\text{于 }\mathbb C((z))/K.
\tag{8.3}
$$
R166 的加性类代数独立定理应用于这个单一非零类，得到
$$
\boxed{\iota(S)\text{ 和 }\iota(S_1)\text{ 各自超越于 }K.}
\tag{8.4}
$$
不是说它们彼此代数独立；恰相反，(8.2) 给它们之间的一次快系数关系。

## 9. 与限制值域问题的关系

本稿的范数下界使用边界的指定有限支持测试向量。
边界表示的收缩性允许将下界传回原全空间算子范数，
却不能把这些向量放入任意未知 Haar 不变空间或子商。

所以 (1.2) 没有被外推为
$$
\tau_4(A_Q^rS_Q^k)=c_*r^4
$$
对所有非零 $Q$ 成立。
R189 的普遍范围证明需要的正是子商版本的混合型；
那里使用准增生逆的预解式和固定子商向量完成下界。
R190 已说明当前两个代数内分母的闭逆没有那种准增生性。

这里新增的是实际全空间的精确型、严格的快分式域非成员证明，
以及一个明确的非零超越加性类。
原慢第一阶的限制像稠密性、一般慢 Bell 单核与完整 Hilbert 不变子空间问题仍未解决。

## 10. 依赖

- R32：$\mathcal A$ 的忠实形式系数及连续有限 jet。
- R140：实际权与子商型背景；本稿所需全空间权极限已在 §2 直接核对。
- R151：快解析逼近、精确 jet 和非零快元素精确型。
- R166：非零加性类的代数独立结论。
- R174：真实负整数边界及 $(B^*)^ne_0=W_ne_n$。
- R179：逐项真实解析的快尾子代数。
- R185/R188：两个具体慢元素、有限头记号和非标准理想。
- R190：仅用于 §9 比较方法边界，不用于本稿主要证明。
