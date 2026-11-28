# R1164 — 原系数的 pointed Miller 根线与全塔 Čech symbol

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本篇为 R1163 的实际椭圆乘积模型提供
原系数 $P^d$ 的有限函数与根线代表。每一条系数都使用同一
原点、切向量和 Weil pairing；加法、$p$-层过渡及
prime-to-$p$ isogeny 的比较由实际刚化函数支付。
这给原 all-vector theta moment 的指定 Čech Kummer 输入，
不是只在 Picard 群中重新写一次 $P$。

本篇不把泛纤维的 Miller 函数当作坏特征处的整单位。
整代表是下文的刚化 line pair；它的局部 transition units
才进入原 scalar syntomic symbol map。
实际 PD normal coefficients、中央 $F_0$ 与 global subtraction
的非零性仍未由此计算。

## 1. 原曲线、第一槽 Weil 规范与整 pointed torsor

设 $p>37$、$N=p^r$，
$\mathcal E/\mathcal O_L$ 是 R1163 的同一 good elliptic curve，
$L/\mathbb Q_p$ 可以分歧，$E=\mathcal E_L$。
取同一原短 Weierstrass 模型
$
y^2=x^3+Ax+B,\qquad t=-x/y,\qquad \omega=dx/(2y).
$
在原点 $O$，有 $dt/\omega=1$。
本篇不改变这一切向量，也不另选 Weil root。

记原第一槽 character 为
$
\chi_P(T)=e_N(P,T),\qquad P,T\in\mathcal E[N].
\tag{1164.1}
$
它是整 group-scheme Weil pairing 给出的
$\mathcal E[N]\to\mu_N$ map，不仅是泛纤维点集上的 pairing。

实际 finite-flat torsor
$[N]:\mathcal E\to\mathcal E$
沿 (1164.1) 的 pushout 记为
$
\mathscr K_N(P)
 =\mathcal E\times^{\mathcal E[N],\,\chi_P}\mu_N .
\tag{1164.2}
$
约定
$
(R+T,z)\sim(R,\chi_P(T)z).
$
原点上指定 $[O,1]$。这一定义适用于
$P\in\mathcal E[N](\mathcal O_L)$；
任意 $P\in E[N](L)$ 都由 properness 唯一延伸为这样的 section。
在特殊纤维，(1164.2) 是 fppf torsor；
本篇不把 $[N]$ 或 $\mu_N$ 宣称为 étale。

等价地，取对应于 $P\mapsto\mathcal O(P-O)$
的 bi-rigidified Poincaré line bundle，拉回得
$\mathcal L_P$，并保原点 rigidification
$r_P:O^*\mathcal L_P\simeq\mathcal O_L$。
由 $NP=O$ 得唯一保持 rigidification 的同构
$
\tau_{P,N}:\mathcal L_P^{\otimes N}\xrightarrow{\sim}\mathcal O_{\mathcal E}.
\tag{1164.3}
$
torsor 是 $\tau_{P,N}(v^{\otimes N})=1$ 的局部向量 $v$，
原点上取 $r_P(v)=1$。
这里也可不预设一个仅在 generic fibre 定义的 character
已经整延伸：rigidified degree-zero line 的 theorem-of-the-cube
同构给 $[N]^*\mathcal L_P\simeq\mathcal L_P^{\otimes N}$。
因此 (1164.3) 将其拉回平凡化；deck action 产生整
$\mathcal E[N]\to\mu_N$ character。
§3 的 generic Miller 计算将它识别为 (1164.1)。
finite-flat 系数模没有底的 torsion，故 generic 上的
这一相等给同一整 morphism。
这同时核准 (1164.2) 与 line-pair 描述的方向。

这里的“唯一”包括必要的常数门。
rigidified degree-zero line bundle 没有非平凡的
rigidification-preserving automorphism：
其 automorphism 是底上的 unit，而在 $O$ 的值须为 $1$。
因此 tensor、base-change、加法及重复 $p$-乘法的
rigidified isomorphisms 一旦存在便唯一，并满足全部 coherence。
generic fibre 上固定同一 Picard 类的两个
$\mu_N$-classes 相差底的 $H^1(L,\mu_N)$；
在 $O$ 指定实际 point 恰将该差消掉。
这不是只断言两条未刚化 line 的 Picard classes 相等。

## 2. leading 为一的实际弦函数

记
$
D_P=[P]-[O],\qquad D_O=0,\qquad
\varepsilon_P=\begin{cases}1&P\ne O,\\0&P=O.\end{cases}
$
对 $P,Q\in E[N]$，定义唯一函数 $b_{P,Q}$ 满足
$
\operatorname{div}b_{P,Q}=D_P+D_Q-D_{P+Q},\qquad
b_{P,Q}=t^{-\varepsilon_P-\varepsilon_Q+\varepsilon_{P+Q}}(1+O(t)).
\tag{1164.4}
$
它可以逐项写成原弦函数：
$
b_{P,Q}=
\begin{cases}
1,&P=O\text{ 或 }Q=O,\$2mm]
x-x(P),&Q=-P\ne O,\$2mm]
-\dfrac{y-y(P)-m_{P,Q}(x-x(P))}
        {x-x(P+Q)},&P,Q,P+Q\ne O,
\end{cases}
\tag{1164.5}
$
其中 $m_{P,Q}$ 是通常 chord slope，
$P=Q$ 时取实际 tangent slope。
因为 $N$ 为奇数，非零 $N$-点不可能是二挠点，
所以此处 tangent 分母不在相应情形中为零。

第三行的负号必须保留。
在 $t=-x/y$ 处，分子首项为 $-t^{-3}$，
分母首项为 $t^{-2}$，所以显示的负号正使 leading 为一。
第二行的 pole order 是二，不可套用第三行的一阶 pole。

比较除子与同一 leading 得到严格函数恒等式
$
b_{P,Q}=b_{Q,P},\qquad
b_{P,Q}b_{P+Q,R}=b_{Q,R}b_{P,Q+R}.
\tag{1164.6}
$
这些等式包含所有零点、相反点和重复点情形。
两边比值的除子为零，故为常数；同一 $O$-leading 将常数锁为一。

令 $B_0(P)=B_1(P)=1$，并用
$
B_{a+b}(P)=B_a(P)B_b(P)b_{aP,bP}.
\tag{1164.7}
$
则
$
\operatorname{div}B_m(P)=mD_P-D_{mP},
$
且 leading 为一。
因此
$
f_{P,N}:=B_N(P),\qquad
\operatorname{div}f_{P,N}=ND_P,\qquad
t^{N\varepsilon_P}f_{P,N}(O)=1.
\tag{1164.8}
$
(1164.7) 可按 binary addition chain 形成有限
straight-line expression；不必展开一个庞大多项式。
本篇没有运行该算法，也不由表达式的存在估计原 PD 读取的运行时间。

对所有 $P,Q\in E[N]$，有
$
\boxed{\quad
f_{P,N}f_{Q,N}
 =f_{P+Q,N}\,b_{P,Q}^{\,N}.
\quad}
\tag{1164.9}
$
再次是相同除子加 leading 一，因而没有未知常数。

## 3. 原第一槽对应 inverse Miller 根

在泛纤维上，取满足
$
X_{P,N}^{\,N}=f_{P,N}^{-1},\qquad
X_{P,N}/t^{\varepsilon_P}\longrightarrow1
\quad\text{于选定的 }O\text{-分支}
\tag{1164.10}
$
的根。它是 line-torsor 的有理坐标，
不是声称 $X_{P,N}$ 是 $E$ 上单值 rational function。
可以在以 $O$ 为基点的共同 étale universal cover 中取这些根；
在 $O$ 的未分歧局部支上，显示的 formal root 唯一。
$P=O$ 时取 $X_{O,N}=1$。

必须核准 inverse，而不能只因最后使用偶数 $d$ 就略去它。
取 rational $g_{P,N}$ 满足
$
g_{P,N}^{\,N}=f_{P,N}\circ[N].
$
对 $P\ne O$，因为 $[N]^*t=Nt+O(t^2)$，
原归一准确是
$
g_{P,N}=\frac1{Nt}(1+O(t)),
\tag{1164.11}
$
不是 leading 一。若先取 leading 一的函数，
其 $N$ 次方会多出 $N^N$。

Silverman III.8 的实际定义为
$
\frac{g_{P,N}(R+T)}{g_{P,N}(R)}=e_N(T,P).
\tag{1164.12}
$
所以 inverse root 在 deck $T$ 下的 character 是
$e_N(T,P)^{-1}=e_N(P,T)$，恰为 (1164.1)。
并且 $[N]^*X_{P,N}=g_{P,N}^{-1}$，
其相对于底参数 $[N]^*t$ 的 leading 恰为一。
这同时识别 (1164.2)、(1164.3) 与 (1164.10)。

因而
$
K_N(P):=[\mathscr K_N(P)_L]
 =\kappa_N(f_{P,N}^{-1})
\quad\text{在其实际 unramified line-pair 延拓意义下，}
\tag{1164.13}
$
并在 geometric cohomology 中准确对应
$
P\longmapsto(T\longmapsto e_N(P,T))
 \in H^1(E_{\bar L},\mu_N).
$
这就是 R1163 (1163.5)，没有换位的 Weil pairing。
(1164.11) 中出现的 $N^{-1}$ 只用于泛纤维识别，
没有被拿来除一个整 trace、整 projector 或 FL lattice。

## 4. 实际同根加法及完整 $p^r$ 过渡

由 (1164.9)，根比值
$
\frac{b_{P,Q}X_{P,N}X_{Q,N}}{X_{P+Q,N}}
$
为常数 $\mu_N$。
(1164.10) 的同一原点分支使其值为一，故
$
\boxed{\quad
X_{P+Q,N}=b_{P,Q}X_{P,N}X_{Q,N}.
\quad}
\tag{1164.14}
$
这正是由乘 $b_{P,Q}$ 给出的 rigidified
$\mathcal L_P\otimes\mathcal L_Q\simeq\mathcal L_{P+Q}$。
(1164.6) 支付三次加法的真实 coherence；
没有先把一个 Picard 等式误写为根的等式。

对 $P\in E[pN]$、$Q=pP$，置
$
b_p(P)=B_p(P)=\prod_{k=1}^{p-1}b_{kP,P}.
$
其除子为 $pD_P-D_Q$。同一归一给
$
f_{P,pN}=f_{Q,N}b_p(P)^N,\qquad
\boxed{\quad X_{Q,N}=b_p(P)X_{P,pN}^{\,p}.\quad}
\tag{1164.15}
$
当 $Q=O$ 时右边准确为 $1$，不是另丢弃一个
未确定的 constant root。
两次 (1164.15) 与直接 $p^2$ 乘法相容：
反复应用 (1164.7)，其函数 correction 都是
同一个 leading 一的 $B_{p^2}(P)$；
根的原点值也相同。
因此这些是全塔真实过渡，而非每层分别选择的 cohomology classes。

所有原点分支、函数和 line isomorphisms 均对
base-change 及 Galois 重指标相容。
若暂在 splitting field 上写为 $\mu_N$ 的指数，
使用原既定的相容 $\zeta_{p^r}$，不更换相位。
不在 splitting field 时，以上各式直接是
$\mu_N$-valued torsor 等式。

若原运算已经采用另一套根
$\widehat X_{P,N}=\rho_{P,N}X_{P,N}$，
则 $\rho_{P,N}\in\mu_N$ 是实际零次数据。
令 Galois 在 label families 上按
$(g\rho)(P)=g(\rho(g^{-1}P))$ 作用，则其 cochains 满足
$
\widehat a_N=a_N+d\rho_N.
\tag{1164.16}
$
这里加法 notation 表示同一个 $\mu_N$ 模；
乘法写法是 $\widehat a_N/a_N=(g\rho_N)/\rho_N$。
(1164.14)、(1164.15) 对任意原根的缺陷，
分别就是
$
\frac{\rho_P\rho_Q}{\rho_{P+Q}},
\qquad
\frac{\rho_{P,pN}^{\,p}}{\rho_{pP,N}}.
\tag{1164.17}
$
这些相位须与原 theta norm roots 一同保留；
本篇只对显示的 pointed 根令其为一。

## 5. 坏特征中可直接使用的整 Čech 数据

(1164.8) 的 generic leading 一不意味着
$f_{P,N}$ 在特殊纤维的 valuation 为零。
尤其 $P$ 可能与 $O$ 相遇；
不能沿用泛纤维的某个 rational frame 而省去其 vertical 因子。

整输入来自 (1164.3)。取将 $\mathcal L_P$
平凡化的实际 open cover $\{U_i\}$，局部 generator 为 $e_i$，
定义
$
u_i=\tau_{P,N}(e_i^{\otimes N})\in\mathcal O(U_i)^\times,
\qquad e_j=g_{ij}e_i .
$
则
$
\boxed{\quad
u_j=g_{ij}^{\,N}u_i,\qquad
a_i^N=u_i^{-1},\qquad
a_j=g_{ij}^{-1}a_i .
\quad}
\tag{1164.18}
$
这是实际 fppf Kummer torsor 的有限 Čech presentation。
generic rational frame 中可写
$
e_i=s_i,\qquad u_i=f_{P,N}s_i^N,\qquad
a_i=X_{P,N}/s_i.
\tag{1164.19}
$
在 $O$ 的 generic chart，取 $s_O=t^{\varepsilon_P}$，
于是 $u_O(O)=a_O(O)=1$。

这些公式给出函数、overlap 和实际根三种数据。
换整 frame $e_i'=r_i e_i$ 时，
$
u_i'=r_i^N u_i,\qquad a_i'=r_i^{-1}a_i
$
是准确等式；不出现未经给定的 $\mu_N$ 选择。
原点 rigidification 与 $\tau$ 的存在由整 Poincaré
line pair 支付，即使某个 generic $s_i$ 不为整 frame 也成立。
计算时须真的换到这些整 frames，不能删除 (1164.19)
中的 $N$ 次幂因子后把裸 $f_{P,N}$ 送入 PD 窗口。

(1164.18) 正是 R1163 所消费的 scalar unit-symbol/Čech
输入。其 generic image 是 (1164.13)，加法及过渡使用
§4 已给的实际 morphisms。
它没有先求一个抽象 cohomology 原像、再任选同名的根函数。
对于 theta 值 $\theta_c(P)\in L^\times$，若它不是
$\mathcal O_L^\times$，应保留其
uniformizer power 及 unit part，用原 vertical log
Kummer symbol；不将其擅自视为普通 unit symbol。

## 6. prime-to-$p$ isogeny 的方向、leading 与 norm 点

令 $\varphi:\mathcal E\to\mathcal E'$ 为原 degree $n$
isogeny，$(n,p)=1$，并取实际 dual $\widehat\varphi$。
保原微分的比例
$
\varphi^*\omega'=c_\varphi\omega .
$
在 good integral models 的原 unit frames 下，
$c_\varphi\in\mathcal O_L^\times$。
设 $P'\in E'[N]\setminus O$，$P=\widehat\varphi P'$；
因为 $n$ 与 $N$ 互素，$P\ne O$。

由实际 dual-isogeny identity，
$\varphi^*D_{P'}-D_P$ 为 principal divisor。
其在 $O$ 的 coefficient 为零，故可取唯一
$
\operatorname{div}r_{\varphi,P'}=\varphi^*D_{P'}-D_P,
\qquad r_{\varphi,P'}(O)=1.
$
比较 leading 给
$
\boxed{\quad
\varphi^*f_{P',N}
 =c_\varphi^{-N} f_{P,N}r_{\varphi,P'}^{\,N},
\qquad
\varphi^*X_{P',N}
 =c_\varphi r_{\varphi,P'}^{-1}X_{P,N}.
\quad}
\tag{1164.20}
$
第二式是相应 line-isomorphism 下的根表达式。
$c_\varphi$ 不能从实际 root comparison 中删掉，
即使其 $N$ 次幂在 Kummer class 中消失。

于是原 coefficient pullback、trace 准确为
$
\varphi^*K_N(P')=K_N(\widehat\varphi P'),\qquad
\varphi_*K_N(P)=K_N(\varphi P).
\tag{1164.21}
$
第一式也直接由原 Weil adjoint identity 验证。
对第二式，先用完整 Kummer cohomology 中的
$\varphi_*\varphi^*=n$，以及
$\widehat\varphi\varphi=[n]$，即可得到显示公式；
这里只反除 $n$，不反除 $p$。

norm 的实际原点也能直接指定。
对 $Q\in\ker\varphi$，因 $[N]$ 在该 prime-to-$p$
有限群上是 automorphism，有唯一
$R\in\ker\varphi$ 满足 $[N]R=Q$。
这给 (1164.2) 在每个 $Q$ 上的 canonical point；
其 norm 给 $\varphi_*\mathscr K_N(P)$ 在 $O'$ 上的 point。
故 (1164.21) 不是只在 geometric cohomology 中成立、
而可能相差一条底 Kummer class 的等式。
此论证包括 $n=2$，不要求 $\sum_{Q\in\ker\varphi}Q=O$。

## 7. 原 $P^d$ 的 scalar symbol 与 theta moment

对 $d=4,8,12$，在 $E_L^d$ 上取
$
\mathcal C_{d,N}(P)=
\epsilon_d\bigl(
 \operatorname{pr}_1^*K_N(P)\cup\cdots\cup
 \operatorname{pr}_d^*K_N(P)\bigr).
\tag{1164.22}
$
$\epsilon_d$ 必须是 R1163 (1163.4) 的 signed projector。
几何 factor permutation 自带 degree-one 的 Koszul 符号，
故不能改为无符号几何平均。

沿 R1163 (1163.6)，(1164.22) 准确对应
$
P^d\in\operatorname{Sym}^dE[N].
\tag{1164.23}
$
每个 factor 已是原 first-slot Weil 类；
pure tensor $P^{\otimes d}$ 被 normalized symmetrizer 固定。
因此没有额外 $d!$、$1/d!$ 或 $2$。
若改用 R1147 §20 的 completed group-ring exponential，
则必须照原式另乘 $d!$ 才取得 (1164.23)；
本篇没有混用这两种 normalization。

固定同一原辅助 $c$ 和 trace-fixed theta。
在 $E_L^d$ 的 generic open 上，
(1164.22) 与原 theta Kummer 类的 actual symbol 为
$
\epsilon_d\{
 \theta_c(P),\,f_{P,N}(T_1)^{-1},\ldots,
                    f_{P,N}(T_d)^{-1}\}_N,
\tag{1164.24}
$
并用 (1164.18) 延拓各 coefficient factor。
括号表示按显示顺序的 Kummer cup；
不是把这个多重 symbol 改成反对称中央 primitive。
theta 在第一槽，所有 $d$ 为偶数，
故移到 coefficient block 后方也不添 shift 符号。

若 $F$ 是原底，令
$\mathcal A_r=E[p^r]\setminus0$，并按实际闭点分解为
$\operatorname{Spec}L_\nu$，标记点为 $P_\nu$。
在 generic fibre 上对 (1164.24) 取真实 finite-étale
corestriction，得到
$
\mathcal M^{\mathrm{Mil}}_{d,r}
 =k_d(c)^{-1}
   \sum_\nu\operatorname{Cor}_{L_\nu/F}
    \bigl(\kappa_N(\theta_c(P_\nu))\cup
                       \mathcal C_{d,N}(P_\nu)\bigr).
\tag{1164.25}
$
在原 coefficient complex 中，它准确是
$
\boxed{\quad
\mathcal M^{\mathrm{Mil}}_{d,r}
 =k_d(c)^{-1}\operatorname{Cor}_{\mathcal A_r/F}
           \bigl(P^d\otimes\kappa_N(\theta_c(P))\bigr)
 =\widetilde{\mathsf M}_{d,r}.
\quad}
\tag{1164.26}
$
最后一项正是 R1147 (1147.59) 的原 all-vector moment。
没有除 $\#\mathcal A_r$，也没有将 closed-point Cor
换成各标记值的无 multiplicity 平均。
$\theta_c$ 的 $p$-单位分母照原 Kummer group
automorphism 解释，不能改成一个 $p$ 次幂后的替代源。

原 primitive moment 仍为
$(1-p^d)\widetilde{\mathsf M}_{d,r}$；
该式及其 actual same-root gauge 直接消费 R1147 §§17–18。
本篇不由 (1164.26) 的 class 等式将原 gauge 设为零。

## 8. 同根修正、完整 tensor 与 syntomic 的准确接口

coefficient 过渡 (1164.15) 与 theta 过渡是两个不同操作。
后者仍使用 R1147 (1147.56) 的原 norm：
若 $z_P^{pN}=\theta_c(P)$，则
$
z_Q=\prod_{pP=Q}z_P^{\,p},\qquad z_Q^N=\theta_c(Q),
\quad Q\ne0.
\tag{1164.27}
$
前者是单点系数的 chord correction；
后者是整 fibre 的 root norm。
二者不能互相替代，更不能把 norm 的 degree
误放入 $P^d$ 的 coefficient transition。

在实际共同 bar/Čech resolution 中，
若 closed degree-one factors 满足
$a_j'=a_j+d\rho_j$，则保序 product 的差有显式同伦
$
\prod_{j=1}^m a_j'-\prod_{j=1}^m a_j=d\mathcal Q,\qquad
\mathcal Q=
 \sum_{j=1}^m(-1)^{j-1}
 a_1'\cdots a_{j-1}'\,\rho_j\,
                  a_{j+1}\cdots a_m .
\tag{1164.28}
$
对每项微分，prefix 的 degree $j-1$
恰消显示的符号；剩余式逐项 telescope。
本式给 (1164.16)–(1164.17) 在 (1164.24) 中的实际
ordered correction，而非只知道它代表零类。

对 corestriction，仍使用原同一套 cosets、root relations
及 R1159 的 projection-formula homotopies。
(1164.25) 不授权删除 crossed terms。
其 $p^r$ reductions 由 (1164.15)、(1164.27)
及原 quotient-torsor morphisms共同指定；
没有先在每层任取 $P$ 的 Tate-module lift。

现在应用已发布的 R1163：
scalar Kummer/Čech map、实际 external products、
$\epsilon_d$ 及全部 $P_r$ 将上述指定输入送到同一
finite integral syntomic complexes。
最高 product 对应原 $\Pi_0$；
低两个 $\Pi_2,\Pi_4$ 与常数
$\lambda_\infty x\gamma_5$ 使用 R1163 §§8–10
已经校准的同一十二因子模型和 Poincaré coevaluation。
不另引入一份未经校准的 contraction。

对分歧标记域，这里的 Cor 首先是已给的原 generic
Galois/étale Cor；其指定 object 与 morphisms 按
R1163 (1163.31) 运输。
本篇不据此额外宣称一个尚未写出的 ramified PD trace
逐坐标公式。
原指定中央 primitive 连同 (1164.28)、
R1159–1160 的所有 ordered corrections 一起运输，
不能由 abelian class 已确定就自由选择另一中央 lift。

本篇现在给出了实际计算的输入清单：
原 normalized Miller addition chain、
整刚化 line frames 的 $u_i,g_{ij}$、
原 theta roots、实际 cosets、
以及上文明确的 root/chord 同伦。
把这些输入投到原 adapted integral frame，
再计算 R1155 §16、R1162 的 selected normal coefficients，
仍是后续的实质工作。
特别没有将 $P^d$ 的有限 coefficient jet
误当作 Miller 函数只需十二阶的 $z$-jet，
也没有把已得到的 Frobenius matrix 再施一次 Frobenius。

## Primary、规范与证明范围

- J. H. Silverman, *The Arithmetic of Elliptic Curves*,
  second edition, III.8（印刷 pp.93–98）及 XI.8：
  [原文](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf)。
  本篇亲读实际 $g(X+S)/g(X)$ 的槽序、
  dual-isogeny identity 及层间 Weil compatibility；
  原 leading 的 $N^{-1}$ 在 (1164.11) 明写。
- J. Sprang, *The algebraic de Rham realization of the elliptic
  polylogarithm via the Poincaré bundle*,
  Algebra & Number Theory **14** (2020), §4.1：
  [作者稿](https://arxiv.org/pdf/1802.04996)。
  本篇只消费任意 locally noetherian base 上的
  rigidified Picard/Poincaré 描述与无 automorphism 性；
  不据其 de Rham logarithm theorem 宣称 supersingular
  integral Frobenius 的未知值。
- R1163 使用的已刊 scalar syntomic comparison、symbol maps
  及全部 projectors 保持其原文范围。
  本篇的新内容是上述实际 Miller/line/root representatives
  与原 moment 的完整规范及过渡。

全部为纸面推导，无数学程序执行。


## 9. 实际 PD unit symbol：保留任意 $1+J$ 的对数

本节把 §5 的实际 line frames 变成可送入 R1163 的
整 syntomic 代表。它不要求 supersingular 椭圆曲线本身有
Frobenius lift，也不把标记域的 Frobenius 当成该 lift。

沿 Tsuji 的实际 simplicial embedding system，局部记
$D$ 为 $p$-完备、$p$-torsion-free 的 PD envelope，
$J=\ker(D\to\mathcal O_{\mathcal E})$，$\Phi$ 为其
compatible Frobenius。各 PD pieces 的 flatness 和 reduction
compatibility 取 Tsuji §2 的 condition 2.1；在本处由该节
Lemma 2.2 的 regular immersion criterion 保证。
取 $D$ 时连同实际 faces、degeneracies 和原点 morphism一起取；
以下的 overlap 公式均在相应 simplicial level 上理解。
不存在全局 lift 的问题通过该 embedding system 处理，
不以任意两个局部 Frobenius 已经相同为假设。

记 $S_N(r)$ 为这个系统中的 mapping-fibre complex，
$N=p^r$ 中的 $r$ 仅表示系数精度；下文用 $w$ 表示
syntomic weight。固定微分约定
$$
d_{\rm syn}x=(dx,(1-\Phi/p)x),\qquad
d_{\rm syn}(\omega,y)=
 \bigl(d\omega,(1-\Phi/p)\omega-dy\bigr)
\tag{1164.29}
$$
于 weight one。这里 $\Phi$ 在 forms 上也包含其
pullback；例如 $\Phi(d\log U)=d\log\Phi(U)$。
这就是 mapping fibre $1-\varphi_1$ 的一种明确 cone
约定；若使用第二坐标相反的 cone，必须同时改变第二坐标
与微分，而不改变正 Kummer symbol 的第一坐标。

对实际 unit lift $U\in D^\times$，令
$$
C(U)=\left(
 d\log U,\quad
 \frac1p\log\frac{U^p}{\Phi(U)}
 \right)\in S_N(1)^1.
\tag{1164.30}
$$
因 $\Phi(U)\equiv U^p\pmod{pD}$，第二坐标是整的。
直接微分给
$$
d_{\rm syn}C(U)=0,\qquad C(UV)=C(U)+C(V).
\tag{1164.31}
$$
(1164.30) 是正 Kummer 类 $\kappa(U)$ 的 symbol；
本篇 inverse-Miller torsor 使用其负号。
这与 Tsuji §2 的 (2.6)、Appendix Lemma A2 在
(1164.29) 下的写法一致；不通过忽略根槽来判断其正负号。

若 $H=1+h\in1+J$，定义
$$
\log_{\rm PD}H=
 \sum_{m\ge1}(-1)^{m+1}(m-1)!\,\gamma_m(h).
\tag{1164.32}
$$
一般 $J$ 不包含于 $pD$，也不假定 $J$ 的 powers
在 $p$-adic topology 中一致趋零。
本式的收敛由 $v_p((m-1)!)\to\infty$ 和
$\gamma_m(h)\in D$ 支付。
PD identities 又给
$h^m=m!\gamma_m(h)$，故该式与其在 $D[1/p]$
中的通常 logarithm 一致。
因此在 $1+J$ 上它具有乘法到加法、Frobenius 及微分相容性。
$\Phi(J)\subset pD$ 保证 $\Phi(\log_{\rm PD}H)/p$ 整，
从而
$$
C(H)=d_{\rm syn}\log_{\rm PD}H .
\tag{1164.33}
$$
这里右侧的 degree-zero 项确实在 $J=S_N(1)^0$，
不是任意 $D[1/p]$ 的 logarithm。

本节只对已证明属于 $1+J$ 的比值取
$\log_{\rm PD}$。尤其当 $G^N\in1+J$ 而
$G\notin1+J$ 时，不允许把
$\log_{\rm PD}(G^N)$ 改写成 $N\log_{\rm PD}G$。
这个区别正是保留 $\mu_N$ transition 的必要条件。

## 10. 原 pointed Miller torsor 的完整总 Čech cocycle

在 §5 的实际整 line frames 上，取 unit lifts
$$
U_i\mapsto u_i,\qquad G_{ij}\mapsto g_{ij}.
$$
它们在共同 embedding system 的各 intersections 上比较。
设
$$
H_{ij}=\frac{U_j}{G_{ij}^{\,N}U_i}\in1+J.
\tag{1164.34}
$$
定义总 degree-one cochain
$$
\boxed{\quad
\mathfrak k_{P,N}=
 \left(
   c_i=-C(U_i),\quad
   v_{ij}=-\log_{\rm PD}H_{ij}
 \right).
\quad}
\tag{1164.35}
$$
第一项的 Čech degree 为零、internal degree 为一；
第二项的 Čech degree 为一、internal degree 为零。
总微分取
$d_{\rm tot}=\delta+(-1)^{\text{Čech degree}}d_{\rm syn}$。

**闭性。**
由 (1164.31)–(1164.34)，
$$
\delta c_{ij}
 =-N C(G_{ij})-d_{\rm syn}\log_{\rm PD}H_{ij}
 =d_{\rm syn}v_{ij}\pmod N.
\tag{1164.36}
$$
在 triple overlap 上，实际 $g_{ij}g_{jk}=g_{ik}$，故
$$
K_{ijk}=\frac{G_{ij}G_{jk}}{G_{ik}}\in1+J,\qquad
\frac{H_{ij}H_{jk}}{H_{ik}}=K_{ijk}^{-N}.
$$
因此
$$
\delta v_{ijk}=N\log_{\rm PD}K_{ijk}=0\pmod N.
\tag{1164.37}
$$
(1164.36) 正抵消总微分中的
$\delta c-d_{\rm syn}v$，而每个 $c_i$ 内部闭。
故 (1164.35) 是完整总 cocycle，不只是 local forms 的集合。

**实际 Kummer 相位。**
Tsuji 的 symbol chain
$[1+J\to M_D^{\rm gp}]\to S_N(1)[1]$
在本约定下为 (1164.30)、(1164.32)；
将 §5 的根粘接
$a_i^N=u_i^{-1}$、$a_j=g_{ij}^{-1}a_i$
代入，所得总 cocycle 正是 (1164.35)。
它在原 period map 下对应 $\mathscr K_N(P)$ 的
实际 generic étale/nearby-cycle 类；不将特殊纤维上的
有限平坦 $\mu_N$-torsor 称为 étale cover。

一个必要的检查是局部 $u_i=1$、而
$g_{ij}\in\mu_N$ 的情形。取 $U_i=1$ 时，
(1164.35) 的 overlap 仍为
$$
v_{ij}=+\log_{\rm PD}(G_{ij}^{\,N}).
\tag{1164.38}
$$
这正保留 Tsuji (2.7) 的 degree-zero root symbol。
尽管 (1164.38) 的 argument 是 $N$ 次幂，
它一般不能作为 $N$ 倍一个已定义的 PD logarithm 删掉。
所以本构造没有把实际 root transition 降成仅有
Picard class 或仅有局部 $d\log u_i$ 的资料。

**lift 与 frame 的精确改变。**
若 $U_i'=R_iU_i$、$G_{ij}'=S_{ij}G_{ij}$，
其中 $R_i,S_{ij}\in1+J$，则
$$
\mathfrak k_{P,N}'-\mathfrak k_{P,N}
 =d_{\rm tot}\{-\log_{\rm PD}R_i\}\pmod N.
\tag{1164.39}
$$
因为新 overlap 的差为
$-\delta\log_{\rm PD}R+N\log_{\rm PD}S$。
若真正换整 frame $e_i'=r_i e_i$，并选相容 lift
$T_i\mapsto r_i$，取
$U_i'=T_i^N U_i$、
$G_{ij}'=T_jG_{ij}T_i^{-1}$，则两套 (1164.35)
在模 $N$ complex 中逐项相同；
非相容选择的差仍准确由 (1164.39) 给出。
这里 $N C(T_i)=0$ 是对已整的 degree-one symbol
取系数约化，不能与 (1164.38) 的非法对数相除混同。

**原点。**
原 $O$-rigidification 使原点 chart 的
$u_O(O)=1$。若其 lift 在原点 PD base 上为
$U_O|_O\in1+J$，则
$-\log_{\rm PD}(U_O|_O)$ 就是
$O^*\mathfrak k_{P,N}$ 的指定 null-homotopy。
也可用这个实际 base unit 归一 lift，使 $U_O|_O=1$。
这两种写法由 (1164.39) 精确对应，
没有另选一个 $\mu_N$ 值来刚化。

## 11. 弦加法和 $p$-降层的实际 PD 同伦

先固定三个实际 line frames
$e_{P,i}=s_{P,i}$、$e_{Q,i}=s_{Q,i}$、
$e_{P+Q,i}=s_{P+Q,i}$。
刚化 line-isomorphism (1164.9) 在此 frames 中的比值为
$$
r_i^{P,Q}=
 \frac{b_{P,Q}s_{P,i}s_{Q,i}}{s_{P+Q,i}}
 \in\mathcal O(U_i)^\times.
\tag{1164.40}
$$
它是整 unit 的理由是原刚化 line-isomorphism 为整的；
不是先断言 rational 弦函数 $b_{P,Q}$ 单独为 unit。
实际关系为
$$
u_{P,i}u_{Q,i}=(r_i^{P,Q})^N u_{P+Q,i}.
$$
取 unit lift $R_i^{P,Q}$ 并设
$$
H_i^{P,Q}
 =\frac{U_{P,i}U_{Q,i}}
        {(R_i^{P,Q})^N U_{P+Q,i}}\in1+J.
$$
则原 inverse 类的有序加法为
$$
\boxed{\quad
\mathfrak k_{P,N}+\mathfrak k_{Q,N}
             -\mathfrak k_{P+Q,N}
 =d_{\rm tot}\{-\log_{\rm PD}H_i^{P,Q}\}
 \pmod N.
\quad}
\tag{1164.41}
$$

证明在 local internal degree 中直接用
$
-C(U_P)-C(U_Q)+C(U_{P+Q})
=-N C(R_i^{P,Q})-C(H_i^{P,Q}).
$
在 overlap 上，实际
$r_j^{P,Q}/r_i^{P,Q}=g_{P,ij}g_{Q,ij}/g_{P+Q,ij}$。
故
$
L_{ij}=
\frac{R_j^{P,Q}G_{P+Q,ij}}
 {R_i^{P,Q}G_{P,ij}G_{Q,ij}}\in1+J,
$
而 overlap 的差与
$-\delta\log_{\rm PD}H_i^{P,Q}$
只相差 $-N\log_{\rm PD}L_{ij}$。
它模 $N$ 为零，完整证明 (1164.41)。
同一证明包括 $P=0$、$Q=0$、$P+Q=0$；
原 $b$ 仍取 §2 的实际退化定义。

三点相加时，§2 的准确弦 identity
$b_{P,Q}b_{P+Q,R}=b_{Q,R}b_{P,Q+R}$
使两条 (1164.41) 同伦之差成为
$N$ 倍一个明确 $1+J$ 比值的 PD logarithm。
所以约化后 associativity 的这份 cochain coherence
也成立；不借 H¹ 的维数或 central uniqueness 替代它。

现在取 $P\in E[pN]$、$Q=pP$，并在高低层使用
§4 的同一 pointed roots。
实际 line-isomorphism
$\mathcal L_P^{\otimes p}\to\mathcal L_Q$
的 frame ratio 为
$$
r_{i,\downarrow}=\frac{b_p(P)s_{P,i}^{\,p}}{s_{Q,i}}\in
\mathcal O(U_i)^\times,\qquad
u_{P,pN,i}=(r_{i,\downarrow})^N u_{Q,N,i}.
\tag{1164.42}
$$
若 $R_{i,\downarrow}$ 是其 lift，设
$$
H_{i,\downarrow}=\frac{U_{P,pN,i}}
 {(R_{i,\downarrow})^N U_{Q,N,i}}\in1+J.
$$
则
$$
\boxed{\quad
\operatorname{red}_{pN\to N}\mathfrak k_{P,pN}
       -\mathfrak k_{pP,N}
 =d_{\rm tot}\{-\log_{\rm PD}H_{i,\downarrow}\}.
\quad}
\tag{1164.43}
$$
局部证明与 (1164.41) 相同；
overlap 使用 $r_{j,\downarrow}/r_{i,\downarrow}=g_{P,ij}^{\,p}/g_{Q,ij}$。
这是与根 morphism
$X_{Q,N}=b_p(P)X_{P,pN}^{\,p}$ 相应的实际同伦。
重复降层的 coherence 由原 normalized $B_{p^2}$
identity 保证，不需选择一个有限 $P$ 的任意
Tate-module lift。

整个 §11 没有除 $N$。
unit 的 $N$ 次幂只产生 $N C(R)$，
而只在已属于 $1+J$ 的比值中用
$\log_{\rm PD}(H^N)=N\log_{\rm PD}H$。
原 theta fibre-norm transition (1164.27) 仍单独保留；
(1164.43) 不能替代它。

## 12. 保序乘法、有限精度与原 coefficient cone 的输入

将 (1164.35) 的实际各 factor 拉到同一个 embedding/Čech
系统，再用 Tsuji 的 product、R1163 的 signed projectors
和原 $\Pi_0,\Pi_2,\Pi_4$ 做 (1164.24)。
例如固定一个 cone product 时，对内部 degree $k$ 的
$(\alpha,\beta)$ 和 $(\gamma,\delta)$ 取
$$
(\alpha,\beta)\star(\gamma,\delta)=
 \left(\alpha\gamma,\,
       \beta\gamma+(-1)^k\varphi_w(\alpha)\delta\right),
\tag{1164.44}
$$
其中 $\varphi_w=p^{-w}\Phi$ 是第一个 factor 的
实际 divided Frobenius，包含 form degree。
总 Čech product 另外保留其 usual Koszul sign。

若改用把 Frobenius 放在另一个 factor 的 cone product，
须同时带上显式 homotopy
$K=(0,(-1)^k\beta\delta)$；
若将另一 product 记为
$(\alpha\gamma,\beta\varphi_{w'}(\gamma)+(-1)^k\alpha\delta)$，
则第一种减第二种正是 $dK+K d$；
degree-one factors 的对应项是 $-\beta\delta$。
不能在已经选择 ordered central coordinate 后，
把两种 product 仅当作 cohomology 相同而删除这一项。
同样，(1164.39)、(1164.41)、(1164.43)
对多重 symbol 的修正通过原 (1164.28) 逐槽展开；
这给指定根 morphisms 的实际 ordered 同伦。

上述输入具有有限的精度描述。
对固定目标模 $p^a$，(1164.32) 可截在 $m\le pa$：
$m\ge pa+1$ 时
$v_p((m-1)!)\ge a$，所以尾项全在 $p^aD$。
这不是把 argument 的函数 $z$-jet 截到 $pa$。
另一方面，写
$W=(U^p/\Phi U-1)/p\in D$，则
$$
\frac1p\log(1+pW)
 =\sum_{m\ge1}
     \frac{(-1)^{m+1}p^{m-1}}m\,W^m.
\tag{1164.45}
$$
每个系数整，尾部按
$m-1-v_p(m)$ 判断。
特别当 $a\le29$、$p>37$ 时，
计算模 $p^a$ 只需 $m\le a$；
其后 $a<m<p$ 的 valuation 至少 $a$，
$m\ge p$ 的 valuation 至少 $p-2>a$。
计算 $W$ 本身时保留实际除 $p$ 所需的一位额外精度。
若后续有 $p^{-i}$ 的 divided-Frobenius 读取，
必须先以足够高的 $a$ 保留该除法所需精度；
不能先模 $p$ 截断再除 $p^i$。

因此本节已经给出从原
$
\bigl(u_i,g_{ij};\ b_{P,Q},b_p(P);\ 
      \text{pointed roots 与 theta norm roots}\bigr)
$
到实际整 syntomic symbols 和全部显示同伦的操作：
选择 compatible PD unit lifts、形成 (1164.34) 的比值、
应用 (1164.30)、(1164.32)，然后按原顺序相乘并取
已校准的 projectors。
任意 lift 选择的影响都由上文显示的 integral cochains 控制。

从这些 symbols 到原 $\omega,x\omega$ adapted
coefficient frame 的投影，仍须保完整 relative/log
de Rham differential 与 divided Frobenius。
本节不把它缩成标记域上的一个 field Frobenius，
也不声称已读出原 $F_0$、$z_{12}$ 或其单位性。
R1155 §16、R1162 的有限 normal 窗口只能在完成这个
实际 frame 投影后消费；并不授权把任意 raw scalar
Frobenius matrix 当作原四十三维矩阵再施一次 Frobenius。

新增 primary：
T. Tsuji, *On $p$-adic nearby cycles of log smooth families*,
Bull. Soc. Math. France **128** (2000), 529–575，
[正式原文](https://www.numdam.org/article/BSMF_2000__128_4_529_0.pdf)。
本节亲读 §2 pp.539–543 的 embedding system、
condition 2.1、Lemmas 2.2–2.3、(2.5)–(2.7)，
及 Appendix Lemma A2 p.562 的 actual symbol。
本节的 Čech formulas、signs、chord/tower homotopies
与精度界由 (1164.29)–(1164.45) 逐项自证。
