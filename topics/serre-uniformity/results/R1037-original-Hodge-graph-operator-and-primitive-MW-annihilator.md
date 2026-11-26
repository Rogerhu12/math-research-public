# R1037：实际 Hodge graph 算子与本原整 MW 消去泛函

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126。
global_route / o2_high_coefficient / root。

**已证明：在原 $p\equiv11\bmod12$、$p>\max(37,C_*)$ 行，
由实际 Hodge graph 构造的整算子给出一个本原整 MW 消去泛函。**
这里 $C_*$ 是 R1026 已明确定义的绝对常数，
不是一个未经说明的充分大阈值。
该泛函杀原完整 Mordell–Weil 对数的饱和格，
而且在原整 Lie 对偶格中不是 $\pi_0$ 的倍数。

证明计算该算子的**真正**模 $\pi_0$ 作用，并证明其核准确一维，
全部在正 deck 角色；R1026 原负角色首 log 因而不能落入该核。
原 CM jet 在这个泛函下是否仍为单位，是另一个具体待证值，
本篇不把泛函本原性替代该横截性。

## 1. 从实际 Hodge graph 构造算子

沿用 R1035/R1036 的原对象：
$$
p=12g-1,\quad m=(p-1)/2,\quad e_0=m(p+1),\quad
\varepsilon=\pi_0^m,\quad \pi_0^{e_0}=p,
$$
$$
M=M_H\oplus M_L,\qquad
\operatorname{Fil}=\{h+\Phi(h):h\in M_H\otimes R\},
\qquad \Phi(M_H)\subset\varepsilon^2(M_L\otimes R).
\tag{1037.1}
$$
这是实际 $\mathcal G_1/R$ 的 Hodge 子格，非任意同型提升。
原整比较给 $M_L\otimes R\simeq\operatorname{Lie}\mathcal G_1$；
原 $\Pi=F\alpha^{-1}$ 是 $M_L\to M_H$ 的整单位同构。

定义
$$
\boxed{\quad
\mathcal Q=\varepsilon^{-2}\Phi\Pi
       \in\operatorname{End}_R(M_L\otimes R).
\quad}
\tag{1037.2}
$$
(1037.1) 已支付这一次除法的整性。
不把 $\mathcal Q$ 称为一个预先存在的 BT 端同态；
它是由实际 Hodge filtration 定义的 Lie 算子。

令 R1036 的完美对称型为 $B(v,w)=\langle\Pi v,w\rangle$。
实际 $\operatorname{Fil}$ 对极化各向同性，故
$$
0=\langle\Pi v+\Phi\Pi v,\Pi w+\Phi\Pi w\rangle
 =\varepsilon^2\{B(v,\mathcal Qw)-B(w,\mathcal Qv)\}.
$$
$R$ 无挠，因此
$$
\mathcal Q\text{ 对 }B\text{ 自伴}.
\tag{1037.3}
$$
原 deck 保持实际 Fil，$\Phi$ 与其两格作用相容；
$\Pi\delta=\delta^{-1}\Pi$ 遂给
$$
\mathcal Q\delta=\delta^{-1}\mathcal Q .
\tag{1037.4}
$$
它也与全部原 split-Hecke 交换。
置同一个 $D=(\delta-\delta^{-1})/(\zeta-\zeta^2)$，则
$$
\boxed{\quad
\mathscr A_{\mathcal Q}(v,w)=B(v,\mathcal QD w)
\quad}
\tag{1037.5}
$$
为整交错型，且对原 split-Hecke 平衡。
这些结论完全在实际格中取得。

## 2. 相对 Verschiebung 给准确矩阵和负号

设 $R_0=R/pR$、$I_0=(\varepsilon^2)\subset R_0$。
因为 $2mp\ge e_0$，绝对 Frobenius 杀 $I_0$。
它因而经 $S=R/(\varepsilon^2)$ 因子化。
R1035 的真实同构
$\mathcal G_1/S\simeq G_0\times_k S$ 给
$$
(\mathcal G_1/R_0)^{(p)}
       \simeq G_0^{(p)}\times_k R_0 .
\tag{1037.6}
$$
所以实际相对 Verschiebung
$$
V:(\mathcal G_1/R_0)^{(p)}\longrightarrow\mathcal G_1/R_0
$$
的源在这个比较中是真的常数群。

协变约定下 $\mathbb D(V)$ 是特殊晶体 Frobenius $F$ 的
线性化。它在 $S$ 上是原特殊 Verschiebung；
由 R1035 第二次 PD 比较的态射自然性，在 $R_0$ 的晶体矩阵
就是同一个 $F$，没有任添一个只在特殊点正确的矩阵。

源 Hodge 子格是 $M_H^{(p)}$。
$F(M_H)\subset pM_L=0$ 于 $R_0$，故此矩阵保持目标 Fil。
源 Lie 的 $M_L^{(p)}$ 经 $F$ 进入 $M_H$，
再取实际 graph 商 $h+\ell\mapsto\ell-\Phi h$，于是其 Lie 映射准确为
$$
\boxed{\quad
H_{\rm HW}=-\Phi F=-\varepsilon^2\mathcal Q\alpha
                      \pmod p .
\quad}
\tag{1037.7}
$$
负号来自实际 graph 商，不能由抽象 superspecial 类型猜出。

后面只读取这个矩阵的第 $2m$ 层。
它与 R1023 的原整参数比较不受未指定高阶基变换影响：
源的模 $\pi_0$ 恒等变换经 Frobenius 后至少是
$O(\pi_0^p)=O(\pi_0^{2m+1})$；
目标的 $O(\pi_0)$ 变换乘上已在 $F^{2m}$ 的矩阵，
也只改动第 $2m+1$ 层以上。
因此可以准确消费 R1023 完整 Hasse–Witt 首矩阵。

## 3. 原首矩阵等于一个准确的多项式商算子

本节所有模 $\pi_0$ 计算都在原特殊纤维的完美域 $k$ 中。
记
$$
r=1-b^3,\qquad A=A_p(b)=bQ_p(b^3),\qquad
d=\deg A=6g-2=(p-3)/2,\qquad k_0=8g-2.
$$
$A$ 是 R1023 的原单首 Hasse 因子，
根集 $S_{\rm ss}\subset\mathbf F_{p^2}$ 简单，且避开 $r=0$。
原最低 Lie 基写成
$$
e_s=\theta_s f_s,\qquad
a\longleftrightarrow\sum_{s\in S_{\rm ss}}a(s)e_s,
\qquad a\in k[b]/(A).
\tag{1037.8}
$$
这里 $e_1$ 是最低型 Hecke 投影；下标 $s$ 是实际尾的标号，
不把这两种下标混淆。R1023/R1036 已给原单位
$$
q_s=C_s^{p-1}\theta_s^{p+1}
    =-\frac{r_s^{k_0}}{A'(s)^2}\in\mathbf F_p^\times .
\tag{1037.9}
$$

先定义半线性算子。对 $a$ 取唯一的次数 $<d$ 多项式代表，
置
$$
\mathfrak M(a)=
 \operatorname{quo}\bigl(r^{k_0}a(b)^p,A(b)^2\bigr)\pmod A.
\tag{1037.10}
$$
$\operatorname{quo}$ 指普通 Euclidean 多项式除法的商，
不是删掉若干指定极点的任意正则部分。

R1023 的原 Hasse 方程给
$$
\mathcal L A=0,\qquad
\mathcal L=r\,\partial_b^2-4b^2\partial_b-\frac94 b .
\tag{1037.11}
$$
确切地，原 $h_p=r^{2g}A$ 代入该文的 Hasse 方程，
利用 $2g\equiv1/6\bmod p$，即得 (1037.11)。
对
$\phi=r^{k_0}a(b)^p$，有
$$
\frac{\phi'}{\phi}=\frac{4b^2}{r}=:s(b),\qquad
\frac{A''(t)}{A'(t)}=s(t)\quad(t\in S_{\rm ss}).
$$
第一式也可写成无需除以 $a$ 的多项式恒等式
$r\phi'=4b^2\phi$。
因此 $\phi/A^2$ 在所有超奇异根处的简单极部均为零；
其二阶极部系数为 $-q_ta(t)^p$。

设
$$
S_{\rm GM}(b)=\frac{b(b^3+7)}{2r^2}.
$$
根 $t$ 处，除掉该二阶极部后的局部常数为
$-q_ta(t)^p S_{\rm GM}(t)/6$。
这一次常数来自完整的原 ODE：
$$
\frac{s'}6-\frac{s^2}{12}
       -\frac{1}{3}\frac{9b}{4r}
       =\frac{S_{\rm GM}}6.
$$
减去其他全部根的二阶极部，得到
$$
\mathfrak M(a)(t)=
 \sum_{s\ne t}\frac{q_sa(s)^p}{(t-s)^2}
 -\frac{q_ta(t)^pS_{\rm GM}(t)}6 .
\tag{1037.12}
$$
这恰是 R1023 原跨尾返回矩阵的负号版本，包含对角
Schwarzian 项，故 (1037.7) 给
$$
\boxed{\quad\overline{\mathcal Q}\,\bar\alpha=\mathfrak M.\quad}
\tag{1037.13}
$$

原算术下降满足 $\alpha e_s=e_{s^p}$。
对 $a(b)=\sum_j c_jb^j$，因为 $s^{p^2}=s$，
它在上述多项式坐标中只对系数作 Frobenius：
$$
(\bar\alpha a)(t)=a(t^p)^p=\sum_j c_j^p t^j.
$$
所以实际的 **$k$-线性**算子为
$$
\boxed{\quad
\overline{\mathcal Q}(a)=
 \operatorname{quo}\bigl(r^{k_0}a(b^p),A^2\bigr)\pmod A .
\quad}
\tag{1037.14}
$$
此式的 $a(b^p)$ 保持系数 $c_j$ 不变。
不能在任意 $k$ 系数的量词下把它写成 $a(b)^p$；
两者之间正差 (1037.13) 的半线性。

也可用在 $S_{\rm ss}$ 正则的有理代表计算 (1037.10)：
若两代表相差 $Ah$，则相应有理式相差
$r^{k_0}A^{p-2}h^p$，在每个超奇异点取值为零。
“商”的含义此时是减去所有超奇异二阶极部后，
再在 $S_{\rm ss}$ 取值；其他极点不擅自删除。

特别地，对原
$$
\lambda=-\frac{6(b+1)}r
$$
有
$$
\frac{r^{k_0}\lambda^p}{A^2}
 =-\frac{6(b^p+1)}{r^{4g+1}A^2}.
$$
因此 R1023 的完整首 log 向量准确为
$$
\bar v=\lambda+R_p
       =(1-\overline{\mathcal Q})\lambda ,
\qquad v=\varepsilon^{-1}e_1\log P.
\tag{1037.15}
$$
这里 $\lambda$ 的唯一多项式代表具有 $\mathbf F_p$ 系数；
所以该处 $\mathfrak M\lambda=\overline{\mathcal Q}\lambda$。
没有删掉首 log 的 degree-$p$ 返回项。

## 4. 核准确一维，而且全部在正 deck 角色

对任意 $a$，仍置 $\phi=r^{k_0}a(b)^p$。
令 $T$ 为次数 $<d$ 的唯一多项式，满足
$$
T\equiv\frac{\phi}{A'}\pmod A.
\tag{1037.16}
$$
$A'$ 与 $r$ 在 $S_{\rm ss}$ 都是单位，且 $k$ 完美，
故 $a\mapsto T$ 是该 $d$ 维空间上的 Frobenius 半线性双射。

设 $B_T=TA'-T'A$。在每个根处，
$B_T=\phi$，且
$B_T'=TA''=\phi'$。于是
$$
\phi=A^2P+TA'-T'A,\qquad
P=\operatorname{quo}(\phi,A^2).
\tag{1037.17}
$$
后一个等式使用 $\deg(TA'-T'A)<2d$，
所以右侧正是 Euclidean 除法，没有另加多项式。

再取根处的二阶 Taylor 系数。
由
$$
B_T''=T'A''+TA'''-T''A'-T'''A,\qquad
\frac{A'''}{A'}=s'+s^2+\frac{9b}{4r}
        \quad\text{在 }A=0\text{ 处},
$$
在 $A=0$ 处第一式的末项消失。结合
$\phi''=\phi(s'+s^2)$，得到
$$
\boxed{\quad
P\equiv\frac{\mathcal L T}{2rA'}\pmod A.
\quad}
\tag{1037.18}
$$
故
$$
\mathfrak M(a)=0
 \quad\Longleftrightarrow\quad
\mathcal LT=cA\quad\text{对某 }c\in k,
\tag{1037.19}
$$
因为 $\deg\mathcal LT\le d$。

对 $0\le e<d$，直接纸面求导给
$$
\mathcal L(b^e)
 =e(e-1)b^{e-2}-(e+3/2)^2b^{e+1}.
\tag{1037.20}
$$
最后一个系数不为零：区间中的第一个可能零点是
$e=(p-3)/2=d$，已在定义域之外。
因此 $\mathcal L:k[b]_{<d}\to k[b]_{\le d}$ 单射。

它把
$$
\langle1,b^3,\ldots,b^{6g-3}\rangle
 \longrightarrow
\langle b,b^4,\ldots,b^{6g-2}\rangle
$$
以非零三角对角元映射；两边维数均为 $2g$，故为同构。
$A=bQ_p(b^3)$ 属于右边，所以存在唯一
$$
T_0\in k[b^3],\qquad \deg T_0<d,\qquad
\mathcal L T_0=A.
\tag{1037.21}
$$
由单射性，(1037.19) 的所有解恰为 $T=cT_0$。
因而
$$
\dim_k\ker\mathfrak M
 =\dim_k\ker\overline{\mathcal Q}=1.
\tag{1037.22}
$$

还须识别这个核的实际角色。
(1037.16) 对 $T_0$ 给
$a^p=T_0A'/r^{k_0}$ 于 $S_{\rm ss}$；
右侧在 $b\mapsto\zeta b$ 下不变。
Frobenius 在这个约化有限代数上单射，故 $a$ 也不变，
其唯一多项式代表属于 $k[b^3]$。

原 normalized Lie 坐标的实际 deck 作用为
$$
\delta_*a(b)=\zeta\,a(\zeta b).
\tag{1037.23}
$$
因此上述核恰在 $\delta_*=\zeta$ 的正角色中。
得到本篇最需要的精确结论：
$$
\boxed{\quad
\overline{\mathcal Q}\text{ 在原 }\delta_*=\zeta^2
\text{ 的负角色格模 }\pi_0\text{ 上单射。}
\quad}
\tag{1037.24}
$$
这不要求 $\overline{\mathcal Q}^2$ 可逆，
也没有把全部 $M_L$ 的 $\delta=1$ 旧方向删掉。

## 5. 消去完整 MW，并在原整对偶格中本原

用实际完整 $v=\varepsilon^{-1}e_1\log P$ 定义
$$
\boxed{\quad
\Lambda_{\mathcal Q}(w)=
 B(v,\mathcal QD\,e_1w),\qquad
 w\in\operatorname{Lie}\mathcal J\otimes R .
\quad}
\tag{1037.25}
$$
其整性来自 (1037.1)–(1037.5) 以及 R1023/R1029/R1035，
不涉及一个未知分母的简单商投影。

R1036 §§5–7 已支付这里所需的全部有理分解：
split-Hecke 生成真正 $F_0$，原 $D_0$ 非挠 paired block
在实际 $J_1$ 中只出现一次 $C$，且 MW 空间为 $F_0\beta$。
由于 $\mathscr A_{\mathcal Q}$ 同样交错并对 split-Hecke 平衡，
该证明逐块适用：

- $D_0$ 投影挠性的块，第一槽的完整 $v$ 为零；
- 非 CM、非挠块上，$F_0$-平衡交错性杀整个 $F_0v$；
- 原旧部分由 $D$ 杀掉；
- 在本篇 $p\equiv11\bmod12$ 行，R1026/R575/R1010
  已识别实际 CM 新 Lie 只有正 $\delta=\zeta$ 角色。
  $\mathcal Q$ 保持其 split-Hecke 块，又交换正负角色，
  所以 $\mathcal Q$ 在 CM 新 Lie 上为零。
  不同块的交叉项同样由 split-Hecke 正交消失。

因此
$$
\boxed{\quad
\Lambda_{\mathcal Q}\bigl(\log J(\mathbf Q)\bigr)=0,
\quad}
\tag{1037.26}
$$
并消去该空间在原整 Lie 格中的饱和交。
这里用的是 R1036 对原同源重数的实际证明，
没有把辅助限制标量 $C^2$ 的整个 MW 空间误认成一条
$F_0$-线。

现使用 R1026 对原完整首 log 的结论。
当 $p>\max(37,C_*)$ 时，
$$
\bar v_-\ne0
\quad\text{于原 }\delta=\zeta^2\text{ 子空间}.
\tag{1037.27}
$$
由 (1037.24)，
$\overline{\mathcal Q}\bar v_-\ne0$，位于正角色。
而 $\overline{\mathcal Q}\bar v_+$ 位于负角色，
不能与它抵消；$D$ 杀旧角色并在正、负角色上分别为 $1,-1$。
故
$$
\overline{\mathcal QD v}\ne0.
\tag{1037.28}
$$
因 $\mathcal QD$ 为 $B$-反自伴，
$$
\Lambda_{\mathcal Q}(w)=-B(\mathcal QD v,e_1w).
$$
$B$ 完美，且 $e_1\operatorname{Lie}\mathcal J$ 是原整直和因子，
(1037.28) 即证明
$$
\boxed{\quad
\Lambda_{\mathcal Q}\notin
 \pi_0\bigl(\operatorname{Lie}\mathcal J\otimes R\bigr)^\vee .
\quad}
\tag{1037.29}
$$
这是真实整格中的本原性。
虽然证明本原性只读取模 $\pi_0$ 首层，
定义 (1037.25) 和 MW 消去 (1037.26) 始终使用完整 $v$。

## 6. 原指定 CM jet 仍要求一个具体单位

令
$$
J=\sum_{s\in S_{\rm ss}}\frac{e_s}{(1-s)^2},
\qquad
K_{\mathcal Q,p}=B(\bar v,\overline{\mathcal Q}D J).
\tag{1037.30}
$$
R1032/R1033 的原盘、原参数和全部积分分母已经给出：
$$
F_{\mathcal Q}(w)=
\Lambda_{\mathcal Q}\!\left((p\varepsilon)^{-1}
          \log[x(w)-c_1]\right)
$$
整且模 $\pi_0$ 次数不超过
$n_0=4g-1=(p-2)/3$，所有原有理点的该值为零。
它的最高系数准确为
$$
-\frac{\kappa_1\sqrt{A_{\rm tail}}}{m}\,
     \lambda_0^{-n_0}K_{\mathcal Q,p}.
\tag{1037.31}
$$
原 $\kappa_1,\lambda_0,A_{\rm tail}$ 均保留，
没有将局部坐标首导数设成一。
(1037.29) 本身**不**证明 $K_{\mathcal Q,p}\ne0$，
更不证明这个多项式的最低单位项或有理盘中的唯一零点。

给出一个保全 $Q^2$ 项的准确读取接口。
对任意系数固定的 $c\in k[b]/(A)$，取次数 $<d$ 代表，定义
$$
\phi_c=r^{k_0}c(b^p),\qquad
T_c\equiv\phi_c/A'\pmod A,\quad \deg T_c<d,
\qquad
P_c=\operatorname{quo}(\phi_c,A^2).
$$
(1037.17) 对这个分子同样成立：
$$
\phi_c=A^2P_c+T_cA'-T_c'A.
\tag{1037.32}
$$
因 $T_c/A$ 的部分分式为
$$
\frac{T_c(b)}{A(b)}
   =-\sum_s\frac{q_s\,c(s^p)}{b-s},
$$
R1036 的原完美配对给
$$
2B(c,J)=\left(\frac{T_c}{A}\right)'(1).
\tag{1037.33}
$$
原 ODE 在 $b=1$ 给 $A'(1)/A(1)=-9/16$；
又 $k_0>0$ 使 $\phi_c(1)=0$。因此
$$
\boxed{\quad
2B(c,J)=P_c(1)=
 \frac{T_c'(1)+(9/16)T_c(1)}{A(1)} .
\quad}
\tag{1037.34}
$$
注意这里读取的是完整商 $P_c$ 在 $1$ 的值，
不是其模 $A$ 的剩余类在 $1$ 的值。
因为 $A(1)\ne0$，这两个读数不能混同。

利用自伴性，
$$
\boxed{\quad
K_{\mathcal Q,p}
  =B(D\overline{\mathcal Q}\bar v,J)
  =\frac12P_{D\overline{\mathcal Q}\bar v}(1),
\qquad
\bar v=(1-\overline{\mathcal Q})\lambda .
\quad}
\tag{1037.35}
$$
所以该分子包含完整的 $\overline{\mathcal Q}^2\lambda$。
没有用核的一维性删去这个项。

还可准确校验核与指定 jet 的关系：
令 $c_0$ 为核生成元，使 $T_{c_0}=T_0$ 如 (1037.21)。
在 $b=1$ 代入 $\mathcal LT_0=A$，得
$$
B(c_0,J)=-\frac18.
\tag{1037.36}
$$
因此 $J\notin\operatorname{im}\overline{\mathcal Q}$：
该像对 $\ker\overline{\mathcal Q}$ 正交。
这仍不能判定 (1037.35) 非零，因为 (1037.36)
可能只检测 CM 方向。
当前剩余问题是实际 (1037.35) 及原 $w$ 低阶系数，
不是另一个任意本原泛函是否存在。

## 7. 来源、复核与范围

本篇只消费已登记的原对象，不重跑任何有限窗口。

- [R1023：完整首 log、原 GM 与全跨尾矩阵](R1023-original-CM-divisor-complete-first-log-vector.md)，特别是原 Hasse 方程与 Schwarzian 对角项。
- [R1026：负角色完整首 log 的统一非零](R1026-original-single-remainder-and-integral-CM-annihilating-log-direction.md)，包含 $C_*$ 的明确定义与全部 CM 角色审计。
- [R1029：真正整最低型分裂](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)。
- [R1032：完整原 CM normal jet](R1032-original-lowest-type-complete-CM-normal-jet-functional.md) 与 [R1033：原有理盘准确尺度](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)。
- [R1035：两次 PD 与实际整 Lie 比较](R1035-original-lowest-type-integral-Lie-comparison-by-two-PD-thickenings.md)。
- [R1036：原 $\Pi^2=-p$、完美 $B$、全部 $F_0$ 与实际重数](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md)。

global_route、o2_high_coefficient 与 root 分别纸面核对实际
Verschiebung/Fil 的负号、半线性与系数固定的区别、
(1037.17)–(1037.24) 的完整核证明、原 MW 消去以及本原性。
端点恒等式另由 global/o2 独立导出，root 逐式复核。
没有数学程序执行；上述推导不依赖先前已登记纠正的违规数字探索。

**主目标仍 OPEN。** 本原 MW 消去泛函并不替代指定 CM
横截值的单位性、低阶唯一零点，或 O0 尚未覆盖的全局分支。
