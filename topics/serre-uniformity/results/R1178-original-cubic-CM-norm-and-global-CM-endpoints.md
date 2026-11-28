# R1178：原 cubic CM 范数与两类 CM 端点的完整全局标签

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面，所有 $p>37$，分别在所述惰性同余类中。**
本篇计算同一个原全点 moment 在 cubic CM 二次型下的正 Kummer 类，
再与 R1179 的 Gaussian 类比较合用。所得是原 proper Heisenberg
覆盖在两个有理 CM 端点的完整全局标签，因而包括中央坐标。
不要求 $B_{p-3}$ 或 $B_{p-5}$ 非零，也不要求整个全局 $H^1$ 已由圆单位生成。

令 $\delta\in\mathbb F_p^\times$ 为原固定非平方数，
$\gamma_3,\gamma_5$ 为原正 Kummer、全轨道未平均圆单位类。
$\Theta$ 是 R1146 的唯一全局 Heisenberg 提升，其 abelian quotient
为 $(\gamma_3,\gamma_5)$。写原正向有限 Frobenius 坐标为
$\operatorname{loc}_p(\Theta)=(r,s,z)$。
则两类原有理 CM fibre 的完整坐标分别为
$$
\boxed{
\begin{array}{c|c|c|c}
 & a_0&b_0&h_0\\ \hline
j=1728,\ p\equiv3\pmod4&
 \dfrac{\delta}{4}r&
 \dfrac{87\delta^2}{44}s&
 \dfrac{87\delta^3}{176}z\\[2mm]
j=0,\ p\equiv2\pmod3&
 \dfrac{2\delta}{9}r&
 \dfrac{160\delta^2}{99}s&
 \dfrac{320\delta^3}{891}z
\end{array}}
\tag{1178.1}
$$
这些是原修正第二槽及 ordered 中央槽，完整保留
$8\delta^2\gamma_5/11$。三个 Tate twists 分别为 $L_3,L_5,L_8$；
表中只省略它们的原固定基，不改变基。

## 1. 原 cubic CM 全点 moment 与合法辅助数

置
$$
K=\mathbb Q(\zeta_3),\quad \mathcal O_K=\mathbb Z[\zeta_3],
\quad p\equiv2\pmod3.
$$
先取标准 $j=0$ 曲线，其复格为 $\Lambda=\Omega\mathcal O_K$。
用 $J=[\zeta_3]$ 表示实际 CM endomorphism，定义
$$
q_J(v)=e_p(v,Jv)\in L_1.
$$
$J^2+J+1=0$。由 Weil pairing 的交替性及
$J^\vee=J^{-1}$，对 $a\in\mathcal O_K$ 有
$$
q_J(av)=N(a)\,q_J(v).
\tag{1178.2}
$$
原 coefficient map $q_J^r$ 使用通常 symmetric-power polarization。

令 $r=2,4$。R1147 的原 moment 为
$$
\mathsf M_{2r}
 =\frac{1}{k_{2r}(c)}
   \operatorname{Cor}_{E[p]\setminus O}
        \bigl(P^{2r}\otimes\kappa(\theta_c(P))\bigr),
\qquad
k_{2r}(c)=c^2-c^{-2r}.
\tag{1178.3}
$$
$\kappa$ 始终是正根 cocycle。选择一个辅助素数 $c\equiv1\pmod{12}$，
且 $c\bmod p$ 为 primitive root；CRT 与 Dirichlet 定理给出此选择。
由于 $p>37$，$k_4(c),k_8(c)$ 是模 $p$ 单位。
这里可以按 R1147 的完整 H¹ 辅助独立性作此替换，
最终返回同一个原 $c=2$ 的局部读取。

Kato theta 的 divisor 为 $c^2[O]-[E[c]]$，
并保原 distribution/base-change 规范。上述选择使
$\theta_c$ 在全部 $\mu_6$ 下作为函数不变。
例如 completed sigma ratio 的相位为
$\epsilon^{c^2-1}=1$，$\epsilon\in\mu_6$；
若以 trace-fixed theta 表达，二者只有一个与 $P$ 无关的常数。
下文的非平凡字符 augmentation 将该常数消去。
因此不把仅有绝对值不变的函数未经处理地当作 ray-field 元素。

## 2. 原六个生成元与准确的 theta 加权公式

对非平凡偶 Dirichlet 字符 $\chi$，conductor 为 $p$，
令其在 $\mathcal O_K/p$ 上的权为 $\chi\circ N$。
标记 $P_v=\Omega v/p$，$v\in(\mathcal O_K/p)^\times$。
取与该格对应的 completed theta 实函数 $F_\Lambda$，
在格点附近具有 $\log|w|^2$ 主部。

这里所需的 shifted-limit 公式沿用 R1179 §3 已证的
Mellin–Poisson–Laplacian 论证，并保任意格的面积：
$$
Z_\Lambda(w,s)=\sum_{\lambda\in\Lambda}|\lambda+w|^{-2s},
\quad
Z_\Lambda(w,0)=0,\quad
\operatorname{res}_{s=1}Z_\Lambda(w,s)=\frac{\pi}{\operatorname{Area}\Lambda}.
$$
在格点外
$\Delta Z'_\Lambda(w,0)=4\pi/\operatorname{Area}\Lambda$，
主部为 $-\log|w|^2$。
与 $-F_\Lambda(w)$ 相减后是紧 torus 上的无奇点调和函数，故
$$
Z'_\Lambda(w,0)=-F_\Lambda(w)+C.
\tag{1178.4}
$$
这保留负号，并不选一个额外的 Fourier rotation 或 Artin 方向。

$\mathcal O_K$ 的 class number 为一、单位数为六。
在 $\operatorname{Re}s>1$，逐个非零 ideal 的六个生成元给
$$
\sum_{v\ne0}\chi(Nv)
 Z_\Lambda(\Omega v/p,s)
 =
6p^{2s}|\Omega|^{-2s}L_K(s,\chi\circ N).
\tag{1178.5}
$$
各项 $Z_\Lambda(w,0)=0$，而
$L_K(0,\chi\circ N)=0$，所以微分时尺度项消失。
(1178.4) 与全点 theta ratio 给
$$
\sum_{v\ne0}\chi(Nv)\log|\theta_c(P_v)|^2
 =
-6\bigl(c^2-\chi(c^2)^{-1}\bigr)
       L'_K(0,\chi\circ N).
\tag{1178.6}
$$
逆号由真实重指标 $v\mapsto cv$ 得到。
没有除 $\mu_6$ 轨道数，也没有除 $p^2-1$ 或 $(2r)!$。

置 $\epsilon=\chi_{-3}$。Euler factors 给
$$
L_K(s,\chi\circ N)=L_{\mathbb Q}(s,\chi)L_{\mathbb Q}(s,\chi\epsilon).
$$
$\chi$ 为偶非平凡字符，故
$$
L'_K(0,\chi\circ N)
 =L'_{\mathbb Q}(0,\chi)L_{\mathbb Q}(0,\chi\epsilon).
\tag{1178.7}
$$
原全轨道圆单位的同一规范是 R1179 (GN.12)
$$
\sum_{b\ne0}\chi(b)\log|1-\xi^b|^2=-4L'_{\mathbb Q}(0,\chi).
\tag{1178.8}
$$
因此 elliptic 与 circular 两边的比例是
$$
\frac32\bigl(c^2-\chi(c^2)^{-1}\bigr)
                  L_{\mathbb Q}(0,\chi\epsilon).
\tag{1178.9}
$$
因子 $3/2$ 是全点六与圆单位四的比，不是一次平均。

## 3. 真正 ray norm 与全单位格中的类等式

令 $F=K(p)$、$L=K(\xi)$。实际 CM reciprocity、theta 的 rationality
及 integrality 使用 Flach §2.2.3 Lemma 2.2(a)–(c) 与其后 Remark：
$$
\operatorname{Gal}(F/K)
 =(\mathcal O_K/p)^\times/\mu_6,\qquad
\operatorname{Gal}(L/K)=\mathbb F_p^\times,
$$
商映射为 $[v]\mapsto Nv$。Norm-one subgroup 的阶为 $(p+1)/6$，
为 $p$ 单位；其 fixed field 正是 $L$。
$\theta_c(P_1)\in F$，其 conjugates 是实际 $\theta_c(P_v)$。
对 principal ideal $(a)$，CM reciprocity 所作的格缩放
把 theta 值送到原 $aP_1$ 处，Weil pairing 则使
$\xi\mapsto\xi^{Na}$。故本节标签方向与 (1178.6) 的重指标相同。

记 $U_c=N_{F/L}\theta_c(P_1)$。在 unit 群的加法记号中，
$$
\sum_{v\ne0}\chi(Nv)[\theta_c(P_v)]
 =6\sum_{b\ne0}\chi(b)\sigma_b[U_c].
\tag{1178.10}
$$
两边是同一个全点和，没有再反除 norm-one subgroup 的阶。

这些 theta 值在 $p$ 外为单位；$L$ 在 $p$ 上只有一个素点。
所以非平凡的 $\chi^{-1}$ 分量的 valuation 为零，属于普通单位格。
由 (1178.6)–(1178.9)，表达式
$$
\frac{1}{c^2-\chi(c^2)^{-1}}
    \sum_{v\ne0}\chi(Nv)[\theta_c(P_v)]
 -\frac32L_{\mathbb Q}(0,\chi\epsilon)
    \sum_{b\ne0}\chi(b)[1-\xi^b]
\tag{1178.11}
$$
在全部 archimedean regulator 坐标为零：
对字符值域的每个嵌入使用共轭字符公式，再用每个
$\sigma_b\in\operatorname{Gal}(L/K)$ 重指标。
这些给全部复 places，绝对值已经把共轭的一对 places 合并。
Dirichlet regulator 的单射性使 (1178.11) 在 rationalized unit 格中为零。

选字符值域在 $p$ 上的素点使 $\chi\bmod p=\omega^r$。
平滑因子约化为单位 $k_{2r}(c)$；§4 将证明
$L(0,\chi\epsilon)$ 在该处整。因此 (1178.11) 原本就在同一个
$p$-local $\chi^{-1}$-unit 格中。
这个格的 rationalization kernel 只有 roots of unity。
prime-to-$p$ roots 已消失，$p$-primary roots 的角色为 $\omega$，
与这里的 $\omega^{-2},\omega^{-4}$ 不同，所以本分量的 kernel 为零。
因此 (1178.11) 在整格中已经为零，能够约模 $p$ 作 Kummer 比较。
这没有用圆单位 index 为单位，也没有丢掉一个可能的 $\mu_p$ 相位。

## 4. conductor 3p 的整消去与两个精确余数

保持 $\chi$ 的 Teichmüller lift。
通常的 conductor $3p$ 公式为
$$
L(0,\chi\epsilon)
 =-\frac1{3p}\sum_{a=1}^{3p}a\chi(a)\epsilon(a).
\tag{1178.12}
$$
写 $a=b+jp$，$1\le b<p$、$j=0,1,2$。
因 $p\equiv-1\pmod3$，
$$
\sum_{j=0}^2\epsilon(b-j)=0,\qquad
c_b:=\sum_{j=0}^2j\epsilon(b-j)
 =\begin{cases}1&b\equiv0\pmod3,\\-2&b\equiv1\pmod3,\\1&b\equiv2\pmod3.\end{cases}
$$
$b$ 的项精确消失，得到整等式
$$
L(0,\chi\epsilon)=-\frac13\sum_{b=1}^{p-1}\chi(b)c_b.
\tag{1178.13}
$$
这先付了 $p$-整性，不将含 $1/p$ 的式子直接约模 $p$。

约 $\chi$ 为 $b^r$ 后，$\sum_{b\ne0}b^r=0$，
所以
$$
L(0,\chi\epsilon)\equiv
 \sum_{\substack{1\le b<p\\b\equiv1\ (3)}}b^r\pmod p.
\tag{1178.14}
$$
置 $p=3m+2$，右端为 $\sum_{j=0}^m(1+3j)^r$，
而 $m\equiv-2/3\pmod p$。
对 $r=2$，
$$
\sum_{j=0}^m(1+3j)^2=(m+1)\left(1+\frac92m+3m^2\right)
 \equiv-\frac29.
$$
对 $r=4$，使用固定多项式
$B_5(x)=x^5-\frac52x^4+\frac53x^3-\frac16x$，
$$
\sum_{j=0}^m(1+3j)^4
 =\frac{81}{5}\bigl(B_5(m+4/3)-B_5(1/3)\bigr)
 \equiv\frac23;
$$
这里 $B_5(1/3)=-5/243$、$B_5(2/3)=5/243$。
所用分母均为 $p$ 单位。于是
$$
\boxed{
L(0,\omega^2\epsilon)\equiv-\frac29,\qquad
L(0,\omega^4\epsilon)\equiv\frac23\pmod p.}
\tag{1178.15}
$$
结合 (1178.9)，比例分别为 $-1/3$ 与 $1$。

## 5. 返回同一个正 Kummer 类与 Q 上的下降

取 $\xi=q_J(P_1)$。它是 primitive Weil value。
(1178.2) 表明原 $q_J^r$ 推送 (1178.3) 时的权正是 $(Nv)^r$。
而原圆单位类的 restriction 是
$$
\gamma_{r+1}|_L
 =\left(\sum_{b\ne0}b^r\kappa(1-\xi^b)\right)
           \otimes\xi^{\otimes r}.
\tag{1178.16}
$$
若换 primitive $\xi$，加权和与 Tate tensor 的两个幂相消；
若原 Weil orientation 给 $\xi^{-1}$，$r=2,4$ 为偶数，同样不改类。
由 §§3–4 的整单位等式，准确得到
$$
\boxed{
(q_J^2)_*\mathsf M_4=-\frac13\gamma_3,\qquad
(q_J^4)_*\mathsf M_8=\gamma_5.}
\tag{1178.17}
$$

复共轭将 $J$ 送到 $J^2=-1-J$，
故 $q_J$ 变号，而 $q_J^2,q_J^4$ 不变。
这两个 coefficient maps 因而定义在 $\mathbb Q$ 上。
CM 的 $p$-torsion splitting field 的 degree 除 $2(p^2-1)$，
为 $p$ 单位；其 restriction 对这里的模 $p$ H¹ 单射。
于是以上等式从 splitting field 返回原 $\mathbb Q$ 底。
任意 $j=0$ twist 在 degree 至多六的扩域后与标准模型同构；
theta、全点 trace、Weil pairing 和 CM map 都自然相容。
再次用 prime-to-$p$ restriction/corestriction，(1178.17)
适用于全部所述原 CM fibre，包括使用中的 good $p$-adic 参考点。

## 6. 原 Cartan 半因子与第二槽修正后的全局标签

R1147 (1147.15)–(1147.18) 的原 Cartan 群同态是
$$
a=\frac12q_I^2x,\qquad
b=\frac12q_I^4y+\frac{8\delta^2}{11}t,\qquad
h=\frac14q_I^6z_0-\frac{4\delta}{11}q_I^4z_2
       +\frac{4\delta^2}{21}q_I^2z_4,
\tag{1178.18}
$$
其中 $I^2=\delta$，$(x,y,t)=(\mathsf M_4,\mathsf M_8,\gamma_5)$。
这里两个 $1/2$ 与第二槽修正都是原群同态的一部分，不能删。

### 6.1 Gaussian 端点

设 $I_0=[i]$、$I_0^2=-1$。因为 $p\equiv3\pmod4$，
存在 $u\in\mathbb F_p^\times$ 使 $u^2=-\delta$，取 $I=uI_0$。
由 R1179 (GN.1)
$$
q_{I_0}^2\mathsf M_4=-\frac12\gamma_3,\qquad
q_{I_0}^4\mathsf M_8=\frac52\gamma_5.
$$
所以准确的原 global labels 为
$$
a_G=\frac{\delta}{4}\gamma_3,\qquad
b_G=\left(\frac54+\frac8{11}\right)\delta^2\gamma_5
    =\frac{87\delta^2}{44}\gamma_5.
\tag{1178.19}
$$
这里的 $u$ 只是实际有限 Cartan 的系数；不声称它已给任意层
$p^n$ 的 Cartan label 提升。

### 6.2 Cubic 端点

$(2J+1)^2=-3$。因为 $p\equiv2\pmod3$，$-3$ 是非平方数，
存在 $u\in\mathbb F_p^\times$ 使 $u^2=-\delta/3$。
取 $I=u(2J+1)$，则 $I^2=\delta$，并且
$$
q_I=2u\,q_J
$$
因为 $e_p(v,v)=0$。由 (1178.17)
$$
\frac12q_I^2\mathsf M_4
 =\frac12(4u^2)\left(-\frac13\right)\gamma_3
 =\frac{2\delta}{9}\gamma_3,
$$
$$
\frac12q_I^4\mathsf M_8
 =\frac12(16u^4)\gamma_5=\frac{8\delta^2}{9}\gamma_5.
$$
加回原第二槽修正，得到
$$
a_C=\frac{2\delta}{9}\gamma_3,\qquad
b_C=\left(\frac89+\frac8{11}\right)\delta^2\gamma_5
    =\frac{160\delta^2}{99}\gamma_5.
\tag{1178.20}
$$
$\{I,-I\}$ 的两个选择给同一原 fibre map，因为所有次数均为偶数。
所有显示的四个 label 系数均为 $p>37$ 的单位。

## 7. 完整全局 Heisenberg fibre，而非只比较两个局部槽

写
$$
(x_G,y_G)=\left(\frac\delta4,\frac{87\delta^2}{44}\right),
\qquad
(x_C,y_C)=\left(\frac{2\delta}9,\frac{160\delta^2}{99}\right).
$$
两个 rational CM 点在原 proper Cartan 曲线上定义；
即使某个椭圆模型在 $2$ 或 $3$ 坏约化，R1146–R1147 的原覆盖
已在全 $S_0=\operatorname{Spec}\mathbb Z[1/p]$ proper 延拓。
由 properness，$\mathbb Q$ 点延拓为 $S_0$ 截面，
故其 fibre 仍是同一 $S_0$ 上的全局 Heisenberg 类。

R1146 已证明
$$
H^1(S_0,L_8)=H^2(S_0,L_8)=0
$$
及 $H^0(S_0,L_3\oplus L_5)=0$，对全部 $p>37$ 成立。
所以固定 global abelian pair 后，完整 Heisenberg lift 存在且唯一。
原 ordered 群律为
$$
(a,b,h)(a',b',h')=(a+a',b+b',h+h'+ab').
$$
映射
$$
[x,y]:(a,b,h)\longmapsto(xa,yb,xyh)
\tag{1178.21}
$$
是真正群同态，并保持三个原 Tate 系数。
由 (1178.19)–(1178.20) 和全局唯一性，原 CM fibre 满足
$$
\boxed{
\mathscr P_G=[x_G,y_G]_*\Theta,\qquad
\mathscr P_C=[x_C,y_C]_*\Theta
\quad\text{in }H^1(S_0,\mathcal H_{\rm Heis}).}
\tag{1178.22}
$$

这一步不需要全局 $H^1(S_0,L_3)$、$H^1(S_0,L_5)$ 的维数为一，
也不需要 $p>C_{\rm cyc}$：这里已经直接计算了两个指定 CM fibre
的类，而不是给任意 global class 选择一个圆单位基。

将 (1178.22) 作 $p$-local restriction，再用 R1151 的原整
Fontaine–Laffaille 三槽比较。该比较对实际群同态自然，
所以 (1178.21) 直接给 (1178.1)。
特别所有退化情形都保留：
$r=0$ 或 $s=0$ 时相应 abelian 槽为零，
而中央槽仍是 $x_Ey_Ez$，不因局部 abelian 消失而擅自归零。
若需将 $r,s,z$ 换成 R1152 的原 Bernoulli/有限调和数表达式，
必须使用该结果已支付的确切范围及正向 Frobenius 约定。
本篇的类级推导本身不依赖 syntomic 第二槽命名的符号。

## 8. 原最低中央投影的端点读数

令 $(Z_0,Z_2,Z_4)$ 是原 43 维 fibre 的三个 **ordered**
中央分量，分别在
$\operatorname{Sym}^{12}H(2)$、
$\operatorname{Sym}^{8}H(4)$、
$\operatorname{Sym}^{4}H(6)$。
由原群同态 (1178.18) 和 (1178.1)，有
$$
\boxed{
q_I^2 Z_4
 =
\frac{21}{4\delta^2}
 \left(x_Ey_Ez-\frac14q_I^6 Z_0
                  +\frac{4\delta}{11}q_I^4 Z_2\right).}
\tag{1178.23}
$$
因此在这两个 actual CM 参考点，
原最高和第二中央分量经 R1170–R1174 的原仿射系统取得后，
最低槽的原 Tate 投影也由同一个 global $\Theta$ 的中央值准确取得。
右侧没有一个另设的 Tate endpoint oracle。
若先算 BCH 坐标，必须用原 $+\mathfrak b(V,V)/2$ 回到
ordered 坐标再施 (1178.23)；不能将二者混用。
全部同源 shear、$\sigma$ 及 determinant twists 仍由所引原式运输。

还有一个 cubic 特有的加强。原 canonical fibre 对全部 elliptic
automorphisms 自然，所以 $Z_4$ 位于 $\mu_6$ 不变部分。
在两个 CM 本征向量 $\omega,\eta$ 上，非平凡三次自同态的权互逆；
$\operatorname{Sym}^4$ 中唯一的 $\mu_6$ 不变 monomial 是
$\omega^2\eta^2$。原 Tate twist 不改变此 automorphism 作用。
在两 CM 线之间的 Weil pairing 完美，故 $q_I$ 的 mixed 系数非零，
$q_I^2$ 在该一维空间上乘一个单位（通常 polarization 的分母为六）。
所以在 cubic 端点，(1178.23) 事实上确定 **整个 $Z_4$**。

Gaussian 的 $\mu_4$ 不变空间则有
$\omega^4,\omega^2\eta^2,\eta^4$ 三维；
(1178.23) 准确确定其中的 middle Tate 读数，
不把其余两个不变 monomials 无故删掉。

## 9. 完成范围与原未解门

本篇完成了 cubic 原全点范数的类等式、两类 actual CM
的四个 global label 及完整中央端点，包括全部局部零分支。
这些新值可直接作为原 Frobenius 或短盘表达式的端点输入。
它们不表示一个任意超奇异参考点都对应有理 CM 点。

原无 CM 候选的全局相容性、Gaussian actual good-mask
联合分离、原最低 jet 的统一非零以及整条深盘的排除仍沿 open.md 继续。
特别，端点的全局相容不把邻近的模 $p$ Cartan label 自动提升成
$p^n$ label，也不将首数字条件变成 whole-disc 唯一性。

## 来源与准确依赖

- M. Flach, *Iwasawa Theory and Motivic L-functions*,
  **Pure and Applied Mathematics Quarterly 5 (2009), 255–294**，
  [正式 PDF](https://intlpress.com/site/pub/files/_fulltext/journals/pamq/2009/0005/0001/PAMQ-2009-0005-0001-a008.pdf)，
  [作者机构书目](https://resolver.caltech.edu/CaltechAUTHORS:FLApamq09)，
  [同作者全文镜像](https://studylib.net/doc/7931909/iwasawa-theory-and-motivic-l-functions---mathematics)。
  §2.2.2 Lemma 2.1 的 theta divisor/norm/base change，
  §2.2.3 Lemma 2.2(a)–(c) 与后续 Remark 的
  CM rationality、integrality、真实格标签。
  原式 (1178.4) 的符号由热核自证；
  (1178.6) 的字符 inverse 由实际重指标自证。
- [R1179](R1179-original-Gaussian-CM-norm-and-middle-Tate-moments.md)
  §§2–5 的原 theta/shifted Epstein/全部 regulator 比较；
  (GN.1) 的 Gaussian 两个全局类，
  (GN.12) 的全圆单位对数规范。
  本篇只为不同的 cubic 单位数与 conductor $3p$ 计算新增项。
- [R1147](R1147-original-canonical-moment-Heisenberg-lift.md)
  (1147.1)、(1147.15)–(1147.18)：原 fullpoint moment、
  原 Cartan 二次型与包括半因子/第二槽修正的实际群同态。
- [R1146](R1146-original-proper-arithmetic-Heisenberg-cover.md)：
  原全 $S_0$ proper 覆盖及 global $L_8$ H¹/H² 消失。
- [R1151](R1151-original-finite-Frobenius-global-subtraction.md)：
  实际有限 Heisenberg–Fontaine–Laffaille 比较及缩放群同态。
- [R1174](R1174-original-all-supersingular-CM-references-and-two-isogeny-correlation.md)
  与 [R1170](R1170-original-supersingular-Brandt-common-kernel.md)：
  两个高中央分量的原 actual CM source、完整仿射方程与单位理想。

全篇纸面证明；没有数学程序执行或用小素数选择比例常数。
