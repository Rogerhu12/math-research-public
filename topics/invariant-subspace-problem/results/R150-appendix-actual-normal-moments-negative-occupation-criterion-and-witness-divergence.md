# R150 附录：完整实际正常矩的负占据权充要判据与真见证全权发散

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；根代理核验准确逆像、同一强单位及源极限。

状态：完整证明。[R244 聚合逆图判据](R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)已经给一般分母的有限 Gram 充要条件。本稿将实际正 first 热分母的整个 Gram 判据准确化为一个显式对角加权平方和，并识别真实聚合源的极限。由此，真慢湮灭见证的完整有限头代表在每个正 $\ell^2$ 占据负权下仍趋于无穷。不是对任意正常态构造所需上界。

## 1. 实际矩、热因子与已付双侧范数

沿用
$$
\mathfrak C=A',\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
B(f,g)=\langle f,Cg\rangle,
$$
其中内积对第一变量线性，$B$ 连续、对称、非退化。
原实际 Cayley 元记为 $V_j$，满足
$$
V_F=\prod_{j\in F}V_j,\qquad
V_F1=\chi_F,\qquad
C\chi_F=(-1)^{|F|}\chi_F.
\tag{1.1}
$$
所有 $V_F\in\mathcal A$，且每个 $\mathfrak C$ 元素均为 $C$ 对称。

固定任意非负 $a\in\ell^2$ 及 $t>0$，记
$$
a(F)=\sum_{j\in F}a_j,\qquad
\beta=2t,\qquad W_\sigma=e^{\sigma\mathcal N_a},
\qquad P=e^{-tX_a}.
$$
[准确热值域](R150-appendix-exact-weighted-occupation-ranges-of-positive-semigroups.md)
及其双侧范数节给一个实际有界单位 $U$，使
$$
P=W_{-\beta}U=U^\tau W_{-\beta},
\qquad U^\tau=CU^*C,
\qquad \|U\|,\|U^{-1}\|\le M:=M_{0,t}.
\tag{1.2}
$$
于是
$$
\operatorname{Ran}P=\operatorname{Dom}W_\beta,\qquad
G=P^{-1}=U^{-1}W_\beta,
\tag{1.3}
$$
$$
M^{-1}\|W_\beta u\|
\le\|Gu\|\le M\|W_\beta u\|,
\quad u\in\operatorname{Dom}W_\beta.
\tag{1.4}
$$
同时对全部 $h\in H$，
$$
M^{-1}\|W_{-\beta}h\|
\le\|Ph\|\le M\|W_{-\beta}h\|.
\tag{1.5}
$$
(1.4) 为逆图范数；(1.5) 为输入负权范数，二者不混同。

所有有限 Walsh 柱均在 $\operatorname{Ran}P$。
特别，令
$$
g=G1,\qquad q_F=G\chi_F,
$$
则由 $P$ 与 $V_F$ 交换及 $P$ 单射，
$$
q_F=V_Fg.
\tag{1.6}
$$
$g$ 循环：其闭多项式轨道被 $P\in\mathfrak C$ 保持，因 $Pg=1$ 而包含原循环向量 $1$。
这里的保持性由 R88 的有界强多项式逼近支付。

R88 §7 的范数级结论表明
$\operatorname{span}\{V_F\}$ 在 $\mathcal A$ 中范数稠密；
其一致有界强逼近又把 $\mathcal A$ 的正常配对延到全部 $\mathfrak C$。
确切来源为
[R88](R88-riesz-basis-bounded-multipliers-strong-closure.md)
§7 的 (7.7)--(7.9)，连同 §6 的准确柱乘子式。
所以 $\operatorname{span}\{q_F\}$ 在 $H$ 稠密。

## 2. 显式加权平方和

令 $\phi$ 为 $B(H)$ 上任意迹类正常泛函。
定义完整实际矩
$$
m_F=\phi(V_F),\qquad
H_p=\sum_{F\subseteq[0,p)}(-1)^{|F|}m_F\chi_F.
\tag{2.1}
$$
$H_p$ 只截取矩坐标，不截断 $V_j$ 的实际 carry。
记
$$
K_p^2=
\|W_{-\beta}H_p\|^2
=\sum_{F\subseteq[0,p)}e^{-2\beta a(F)}|m_F|^2.
\tag{2.2}
$$
这些量单调不减，且
$$
K_\infty^2=
\sum_{F\ {\rm finite}}e^{-4t a(F)}|\phi(V_F)|^2
\in[0,\infty].
\tag{2.3}
$$
这里始终是实际算子 $V_F$ 的正常矩，不是 $\rho$ 的普通 Walsh 系数或其对角矩阵元。

## 3. 全部热聚合表示的准确充要条件

**定理3.1。** 以下条件等价：

1. $K_\infty<\infty$。
2. 存在 $h\in H$，使
   $$
   \phi(PQ)=B(Qh,1)\qquad(Q\in\mathfrak C).
   \tag{3.1}
   $$
3. 存在 $h\in H$，使
   $$
   \phi(Q)=B(h,Qg)\qquad(Q\in\mathfrak C).
   \tag{3.2}
   $$

这些表示中的 $h$ 相同且唯一。
当条件成立时，存在以下实际范数极限：
$$
\boxed{
k=\lim_{p\to\infty}W_{-\beta}H_p,\qquad
h=U^\tau k=\lim_{p\to\infty}PH_p.
}
\tag{3.3}
$$
并且
$$
\boxed{
M^{-1}K_\infty\le\|h\|\le MK_\infty.
}
\tag{3.4}
$$

### 3.1 加权平方和推出实际源及全部表示

若 $K_\infty<\infty$，正交级数给
$W_{-\beta}H_p\to k$。
由 (1.2)，$PH_p\to U^\tau k=:h$，并给 (3.4)。

固定有限 $F$，对充分大的 $p$，利用 $P$ 的 $C$ 对称性及 $Pq_F=\chi_F$，
$$
B(PH_p,q_F)=B(H_p,\chi_F)=m_F.
$$
因此
$$
B(h,V_Fg)=B(h,q_F)=\phi(V_F).
\tag{3.5}
$$
先以 $\operatorname{span}\{V_F\}$ 的范数稠密性将 (3.5) 延到 $\mathcal A$。
再给任意 $Q\in\mathfrak C$ 取 R88 的一致有界强多项式逼近：
正常泛函对这样的强逼近连续，且多项式作用于固定 $g$ 强收敛。
于是得到 (3.2)。

将其中 $Q$ 换成 $PQ$，使用 $Pg=1$、交换性和 $C$ 对称性，
$$
\phi(PQ)=B(h,PQg)=B(h,Q1)=B(Qh,1),
$$
证明 (3.1)。
因为 $\mathfrak Cg$ 稠密，(3.2) 中 $h$ 唯一；
也可由 (3.1) 对全部 $A^n$ 测试及 $1$ 循环性直接证明唯一性。

### 3.2 从热表示返回未经阻尼的全部矩

这一步须使用同一组真实强单位，不能把 $P^{-1}$ 当成有界元。
置
$$
D_m=\exp\!\left(t\sum_{j<m}a_jV_j\right)\in\mathcal A,
\qquad
K_m^{\rm su}=PD_m
=e^{-tX_{a\mathbf1_{j\ge m}}}.
$$
前稿已证明
$$
\|K_m^{\rm su}\|\le1,\qquad
K_m^{\rm su}\longrightarrow I\quad\mathrm{SOT}.
\tag{3.6}
$$

假设 (3.1) 成立。将其中 $Q$ 换成 $D_mV_F$，得到
$$
\phi(K_m^{\rm su}V_F)
=B(D_mV_Fh,1)=B(h,D_m\chi_F).
\tag{3.7}
$$
左侧由正常性和一致有界强收敛趋于 $m_F$。
右侧则有准确等式
$$
D_m\chi_F=D_mPq_F=K_m^{\rm su}q_F\longrightarrow q_F.
$$
所以仍得到 (3.5)。
对任意有限柱 $u=\sum_Fu_F\chi_F$，
$$
\left|\sum_Fu_Fm_F\right|
=|B(h,Gu)|
\le\|h\|\|Gu\|
\le M\|h\|\|W_\beta u\|.
\tag{3.8}
$$
有限维对角 Hilbert 对偶对每个头给
$$
K_p\le M\|h\|.
$$
令 $p\to\infty$，得到 $K_\infty<\infty$。
已经证明的方向和唯一性随后识别 (3.3)。

若直接从 (3.2) 出发，(3.8) 立即成立。
至此全部等价与真实源极限均已付清。

## 4. R244 的完整有限 Gram 成本已被对角化

对有限头定义原准确逆图成本
$$
c_p(P,\phi)
=\sup_{0\ne u\in\operatorname{span}\{\chi_F:F\subseteq[0,p)\}}
\frac{|\phi(X_u)|}{\|Gu\|}.
\tag{4.1}
$$
因为
$$
X_u=\sum_Fu_FV_F,\qquad
\phi(X_u)=\sum_Fu_Fm_F,
$$
(1.4) 与有限维对角对偶给
$$
\boxed{
M^{-1}K_p\le c_p(P,\phi)\le MK_p.
}
\tag{4.2}
$$
常数只依赖指定 $a,t$，不依头长度 $p$ 或该正常泛函。

又因 $\operatorname{span}\{q_F\}$ 稠密，
$$
\sup_pc_p(P,\phi)=\|h\|
$$
在定理条件成立时准确成立。
当 $K_\infty=\infty$ 时，两者均趋于无穷。

有限层的最小 Gram 代表不应直接等同于 $PH_p$。
后者确实在该有限层上表示所需泛函：
$$
B(PH_p,Gu)=B(H_p,u)=\phi(X_u).
$$
但它未必属于该有限层表示空间
$C\operatorname{span}\{q_F:F\subseteq[0,p)\}$。
最小代表是 $PH_p$ 到这个空间的正交投影；
其范数才准确等于 $c_p$。
本文的 (3.3) 是在条件成立时整个实际源序列的极限，不删除有限层的这个区别。

## 5. 真慢湮灭者的每个负占据权都发散

固定在全 $H$ 单射的实际慢符号 $T\in\mathfrak C$。
设
$$
\phi(TQ)=0\qquad(Q\in\mathcal A).
\tag{5.1}
$$
有界强逼近与正常性将其延到全部 $Q\in\mathfrak C$。

若定理3.1成立，则对所有 $Q\in\mathfrak C$，
$$
0=\phi(PTQ)=B(QTh,1).
$$
原真空循环性与 $B$ 非退化给 $Th=0$。
$T$ 的全空间单射性于是给 $h=0$。
由 (3.2)，
$$
\phi|_{\mathfrak C}=0.
\tag{5.2}
$$
等价地，先由 (3.1) 得 $\phi(PQ)=0$，
再用同一收缩强单位可得原正常泛函在整个交换子上为零。

因此，只要 $\phi|_{\mathfrak C}\ne0$，
对每个非负 $a\in\ell^2$ 及每个 $t>0$ 都必须有
$$
\boxed{
\sum_{F\ {\rm finite}}
e^{-4t a(F)}|\phi(V_F)|^2=\infty.
}
\tag{5.3}
$$
特别，每个非零正正常湮灭见证满足 $\phi(I)=\operatorname{Tr}\rho>0$，
所以满足 (5.3)。
矩坐标的平方和单调性还给真正的极限，而不只是无界子列：
$$
\boxed{
\|e^{-2t\mathcal N_a}H_p\|\longrightarrow\infty,
\qquad
\|PH_p\|\longrightarrow\infty.
}
\tag{5.4}
$$
用双侧输入范数中相同的伴随比较，也有 $\|P^*H_p\|\to\infty$。
$a$ 可依该见证选取；(5.3) 仍对每个这样的固定选择成立。

## 6. 原正密度的有限头代表与真实擦除源也继承此约束

对 $\rho\ge0$、$\tau=\operatorname{Tr}\rho$，
[R230 完整头矩附录](R230-appendix-first-walsh-observability-and-canonical-positive-head-moments.md)
定义同一前 $p$ 位的真实有限头算子 $V_j^{[p]}$，并令
$$
v_p=\sum_{F\subseteq[0,p)}
(-1)^{|F|}\phi(V_F^{[p]})\chi_F.
\tag{6.1}
$$
它是原正密度在有限头代数中的准确代表；
由于 $V_F^{[p]}$ 一般不属于原 $\mathfrak C$，
不能未经成本控制就拿它去测试 (5.1)。

该稿的实际局部差与范数界为
$$
\|V_j-V_j^{[p]}\|\le18\theta_{j,p},\qquad
\theta_{j,p}=\prod_{\ell=j}^{p-1}\eta_\ell\le\eta_{p-1},
\qquad
\|V_j\|,\|V_j^{[p]}\|<3.
$$
乘积望远镜和全部头坐标的平方和给，对 $p\ge1$，
$$
\begin{aligned}
\|H_p-v_p\|
&\le
\tau\left(\sum_{F\subseteq[0,p)}
\|V_F-V_F^{[p]}\|^2\right)^{1/2}\\
&\le6p\,\eta_{p-1}\,10^{p/2}\tau
\longrightarrow0.
\end{aligned}
\tag{6.2}
$$
因 $W_{-\beta}$、$P$ 均为收缩，(6.2) 也控制加权及热作用后的差。
所以真实非零正湮灭见证必满足
$$
\boxed{
\|e^{-2t\mathcal N_a}v_p\|\to\infty,\qquad
\|e^{-tX_a}v_p\|\to\infty
\quad\text{对每个 }a\ge0\text{ 的 }\ell^2\text{ 行和每个 }t>0.
}
\tag{6.3}
$$

对于有限秩见证，该 R230 稿 §6 的实际完整尾擦除源
$\widetilde v_p=\sum_{F,i}V_FW_{F,i}^{(p)}f_i$
还满足相同的已付估计
$$
\|\widetilde v_p-v_p\|
\le6p\,\eta_{p-1}\,10^{p/2}\tau\to0.
$$
因此 (6.3) 同样传到这个实际聚合源。
这里没有把完整非正交叉密度或未知重构误差省略；
使用的是该明确恒等重构表和已证明的实际头差。

## 7. 范围

本稿为热分母给出了完整、可计算的正常矩充要判据，
并对真正慢见证的明确头源给出所有正 $\ell^2$ 占据负权下的必要发散。
它没有从一般正性推出某个加权平方和有限；
既有 R240 的非湮灭正常态障碍仍然存在。

$a\in\ell^1$ 或 $a=0$ 时，相关权有界可逆，判据退回原矩平方可和情形；
不可和 $a\in\ell^2$ 则给实际非有界逆域的准确识别。
任意可数权图核心的稠密性也不说明指定真实见证已经满足本判据。
正常见证的上界构造与普通 Hilbert ISP 均未在本文解决。

## 8. 随有限头自适应的有界平方预算也不能阻尼真源

本节强化 §5 的量词；仍以一个固定非零真正常湮灭见证为前提。
把热时间吸收到正行中，固定时间 $1/2$，写
$$
D_a=e^{-\mathcal N_a},\qquad P_a=e^{-X_a/2},
\qquad a\ge0,\quad a\in\ell^2.
$$
原 $e^{-tX_b}$ 对应这里的 $a=2tb$。

对固定 $R<\infty$，定义有限头的最优平方预算
$$
\mathfrak e_p(R)=
\inf_{\substack{a\ge0\\\|a\|_2\le R}}
\|D_aH_p\|^2
=
\inf_{\substack{a\ge0\\\|a\|_2\le R}}
\sum_{F\subseteq[0,p)}
e^{-2a(F)}|\phi(V_F)|^2.
\tag{8.1}
$$
每个被最小化的式子只依前 $p$ 个坐标，
所以可把其余坐标取零；有限维紧致性保证下确界实际可达。
$\mathfrak e_p(R)$ 随 $p$ 单调不减。

**命题8.1。** 对每个固定 $R<\infty$，
$$
\boxed{\mathfrak e_p(R)\longrightarrow\infty.}
\tag{8.2}
$$

若不成立，存在 $p_k\to\infty$ 与
$a^{(k)}\ge0$、$\|a^{(k)}\|_2\le R$，
使 (8.1) 的对应平方和一致有界。
正 $\ell^2$ 球弱序列紧，
故取子列可令 $a^{(k)}\rightharpoonup a\ge0$、$\|a\|_2\le R$。
每个坐标以及每个固定有限和 $a^{(k)}(F)$ 都趋于 $a(F)$。
固定头 $q$，对充分大 $k$ 有 $q\le p_k$，
因此有限项取极限给
$$
\sum_{F\subseteq[0,q)}
e^{-2a(F)}|\phi(V_F)|^2\le C.
$$
令 $q\to\infty$，得到一个固定 $a\in\ell^2_+$ 的有限全矩平方和，
与 §5 的真见证发散矛盾。
这证明 (8.2)，没有交换无限和与弱极限。

### 8.1 精确热常数在平方预算球上一致

还须控制随 $a$ 变化的单位，不能仅引用每个固定 $a$ 的有限常数。
准确热值域稿给
$$
M_{0,1/2}(a)
\le
\exp\!\left[
\int_0^{1/2}
\left(
\sum_ja_j\sinh(2ra_j)+K_a(2r)
\right)\,dr
\right],
$$
其中
$$
K_a(\sigma)
\le18\Bigl(\sum_ja_j\eta_j\Bigr)
\sum_{\ell\ge1}
e^{\sigma\|a\|_2\sqrt{\ell+1}}\eta_*^{\ell-1},
\qquad \eta_*=\sup_j\eta_j.
$$
若 $\|a\|_2\le R$，
则 $\|a\|_\infty\le R$，
$$
\sum_ja_j\sinh(2ra_j)
\le2r\cosh(2rR)R^2
\le R^2\cosh R
\quad(0\le r\le1/2),
$$
且 $\sum a_j\eta_j\le R\|\eta\|_2$。
所以可以统一取
$$
\boxed{
M_R=
\exp\!\left[
\frac{R^2\cosh R}{2}
+
9R\|\eta\|_2
\sum_{\ell\ge1}e^{R\sqrt{\ell+1}}\eta_*^{\ell-1}
\right]<\infty.
}
\tag{8.3}
$$
在 $R=0$ 时该值为1。
本节不追求此常数最优。

输入负权比较因而给
$$
\boxed{
\inf_{\substack{a\ge0\\\|a\|_2\le R}}
\|P_aH_p\|
\ge M_R^{-1}\sqrt{\mathfrak e_p(R)}
\longrightarrow\infty.
}
\tag{8.4}
$$

### 8.2 原实际有限头与擦除源

§6 的 $\|H_p-v_p\|\to0$ 和
$\|\widetilde v_p-v_p\|\to0$
与 $a$ 无关。
每个 $D_a$ 与 $P_a$ 都收缩，所以它们作用后的差在整个平方预算球上仍一致趋零。
故 (8.2)、(8.4) 对真实 $v_p$ 也成立，
并在有限秩时对该稿指定的实际擦除源 $\widetilde v_p$ 成立。

特别，若某列随头选择的正行 $a^{(p)}$
使 $\|D_{a^{(p)}}v_p\|$ 或 $\|P_{a^{(p)}}v_p\|$ 一致有界，
则必须有
$$
\boxed{\|a^{(p)}\|_2\longrightarrow\infty.}
\tag{8.5}
$$
若仅有无穷个头的平方预算不超过某个 $R$，
(8.2) 或 (8.4) 已在该子列给出矛盾。

本节没有得到 $\mathfrak e_p(R)$ 的发散速度，
也不把平方预算发散本身当作一般正常见证不存在性。
它准确排除了：通过随有限头改变正热锚、同时保持其有效 $\ell^2$ 预算有界，
来把该实际真源压成一个有界 Hilbert 族。
