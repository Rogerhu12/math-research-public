# R671 — 固定 N 的原 cd 完整返回、双 Y 外部单位过滤及中央接合

日期：2026-11-15。**状态：已证明。**

本篇固定原 $N$，只让原 Y 深度 n 变化。
先支付**未附第二个 Y 条件**的原 cd 双深行，再与真正附上该条件的
R664/R668 行逐项比较。前者具有准确的 $\lambda^n$ 变化，
后者的原 S 行只有七个 $\lambda^{2n}\kappa^{an}$ 模式。
七个实际相邻深度的单位过滤因而精确恢复未切行。
原 T 行用偶数步过滤；其质量同样精确，中央 log 余项有完整的
$p^{7n-6N}$ 界。

两种外部域最终与原两个中央放在同一式中。
这不是将旧未切 cd 补偿直接用于双 Y 子域，也没有给任何外部赋零。
全文保原 $q_N$、全部 C 条件、移动观察和质量。

## 1. 固定来源、固定 N 和三个真实域

全部规范与 R664/R665/R668 相同：
$$
\mu_0=\nu_4\otimes\nu_{\rm pair}(Q,L),\quad
Q=c+2d,\quad L=2c-d,\quad
Y_0=A+Q,\quad Y_1=A+L,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1 .
$$
原 $q_i=q_N\mathsf J^{-i}$、$W_i=W\mathsf J^{-i}$，
$i=0,1$，$\mathsf J(c,d)=(d,-c)$。
固定
$$
\boxed{N\in4\mathbf Z_{\ge1},\qquad1\le j\le N,\qquad n\ge N.}
\tag{1}
$$
$\widehat P_p$ 和原全部系数在此固定；没有随着 n 另选测试。

记
$$
E_i(n)=\{Y_i\in p^n\},\quad
\mathcal D_j^{cd}=\{c,d\in p^j\}=\{Q,L\in p^j\},\quad
\Gamma_n=\{Y_0,Y_1\in p^n\}.
$$
使用原完整归一测试
$$
f_{i,n}^{Z}(u)=q_i\,
1_{\{Z_iP_{Y_i,(-\kappa)^n}^{-1}\ {\rm unit}\}}
\langle Z_iP_{Y_i,(-\kappa)^n}^{-1}\rangle^{d_pu},
\quad Z_i=Y_i\text{ 或 }W_i .
\tag{2}
$$
每个逆像仅在其原 $E_i(n)$ 整像上使用。
定义三个真正积分：
$$
\begin{aligned}
\mathcal V_{i,n}^{Z}&=\int_{E_i(n)\cap\mathcal D_j^{cd}}f_{i,n}^{Z}\,d\mu_0,\\
\mathcal I_{i,n}^{Z}&=\int_{\Gamma_n\cap\mathcal D_j^{cd}}f_{i,n}^{Z}\,d\mu_0,\\
\mathcal O_{i,n}^{Z}&=\int_{E_i(n)\cap\mathcal D_j^{cd},\
                         Y_{1-i}\notin p^n}f_{i,n}^{Z}\,d\mu_0 .
\end{aligned}
\tag{3}
$$
所以 $\mathcal O=\mathcal V-\mathcal I$ 是同一来源、同一测试的真实域差。

最后令 $\mathcal X_{i,n}^{Z}$ 为 $E_i(n)$ 内
$\mathcal D_j^{cd}$ 之外的完整部分。原算术总行严格为
$$
\boxed{
\mathcal X_{i,n}^{Z}+\mathcal V_{i,n}^{Z}
=(-1)^i\lambda^n\beta^N J_Z^*,
\qquad J_S^*=J_S,\quad J_T^*=6\delta J_T .}
\tag{4}
$$
(4) 保整个 Mellin 函数。只有在最后代入原中央假设时，
才能令其 $u=0$ 导数为零。

## 2. 未切第二条 Y 的完整 cd 返回

沿 R665/R668 记
$$
D_*=D_4-aA,\quad
\alpha=29/143,\quad C^\perp=C+\alpha D_*,\quad
H_1^\perp=H_1+\alpha gD_*,\quad
G_\perp=13H_1^\perp+gC^\perp,\quad g=3-2\omega .
$$
$\eta_A,\chi_D\in\{\pm1\}$ 分别是原 odd29 和完整 $87D_*$
degree37323 的实际标量，后者保全部六个 C 分支。
置
$$
V_i=e_i\mathcal E+v_i,\qquad
H_i=D_*+V_i,\qquad K_i=H_i-14\alpha D_* ,
$$
其中 $e_i,v_i,\mathcal E$ 是 R664 的准确行。
整个 $H_i,C^\perp,G_\perp,K_i$ 都与 $Y_i$ 正交。

在 $E_i(n)\cap\mathcal D_j^{cd}$ 上，
$Q,L\in p^j$ 且 $Y_i\in p^n$ 强迫 $A\in p^j$。
原 $q_i$ 的条件
$$
F_i-C=D_*+V_i\in p^N
$$
随后又强迫 $D_*\in p^j$，因为 $V_i\in p^j$。
这用的是原 carry 条件，而非新增的独立输入假设。

因此可在同一完整来源上用真正四轴映射
$$
M_j=P_{A,\tau}P_{Q,\tau}P_{L,\tau}P_{D_*,\tau},
\qquad \tau=\kappa^j .
$$
其来源系数是
$$
(\eta_A\chi_D)^j\lambda^{4j}.
$$
当 $j\ge1$，原 C 单位准确等价于返回后的 $C^\perp$ 单位。
令 $M=N-j\ge0$；返回后的同一个实际权为
$$
\boxed{
q^{cd}_{i;M}(\tau)=
\frac{1_{\{C^\perp\ {\rm unit},\,H_i\in p^M\}}}{b\Omega^6}
\widehat P_p(H_i/\kappa^M,\ 14C^\perp+\tau K_i,\
                       G_\perp+g\tau K_i).}
\tag{5}
$$
$M=0$ 时 $H_i\in\mathcal O$ 自动成立，不留下隐藏的深度条件。
所有原 $u_j$、$\lambda,\kappa$ 和整右逆仍在 (5)。

(5) 对 $Y_i$ 的完整正交核逐点不变。
再用原 $Y_i$ 深 $n-j$ 的真核心，就可把 (3) 第一行完全返回。
注意原 W 观察也要同序运输；准确得到
$$
Y_iP_{Y_i,(-\kappa)^n}^{-1}M_jP_{Y_i,(-\kappa)^{n-j}}
=(-1)^jY_i,
$$
$$
\boxed{
W_iP_{Y_i,(-\kappa)^n}^{-1}M_jP_{Y_i,(-\kappa)^{n-j}}
=(-1)^jb_YY_i+\tau(W_i-b_YY_i).}
\tag{6}
$$
这里 $b_Y=(20+3\omega)/17$ 是当前 ray 上的单位。
第二式的单位 cut 因 $\tau\in p\mathcal O$ 准确等于 $Y_i$ 单位。

定义不再依 n 的两个实际行
$$
\mathcal A_i^S(u)=
 \int q^{cd}_{i;M}(\tau)1_{Y_i\ {\rm unit}}
                  \langle Y_i\rangle^{d_pu}\,d\mu_0,
$$
$$
\mathcal A_i^T(u)=
 \int q^{cd}_{i;M}(\tau)1_{Y_i\ {\rm unit}}
 \langle(-1)^jb_YY_i+\tau(W_i-b_YY_i)\rangle^{d_pu}\,d\mu_0 .
\tag{7}
$$
所有 $N,j,p$ 仍在 (5)、(7) 中，仅 n 被准确移除。
于是
$$
\boxed{
\mathcal V_{i,n}^{Z}(u)
=c_j\lambda^{n+3j}\mathcal A_i^Z(u),
\qquad c_j=(\eta_A\chi_D)^j.}
\tag{8}
$$
这是未附第二条 Y 条件的完整 cd 返回，没有近似误差。

两条质量相等：
$\mathcal A_i^T(0)=\mathcal A_i^S(0)$，但一般不能删去它。
其 log 比较仍含
$\log\langle b_Y\rangle\mathcal A_i^S(0)$。
此外 $M_j$ 与原 $\mathsf J$ 交换，cd 域也不变，所以
$$
\boxed{\mathcal A_1^Z=(-1)\mathcal A_0^Z.}
\tag{9}
$$
这只是原整数旋转的完整运输，不给第二条独立算术零。

## 3. 加上第二条 Y 以后：真正固定门与原七项多项式

现在支付 (3) 第二行，不能把它与 (8) 合并。
在 $M_j$ 返回以后，额外条件正是
$Y_0,Y_1\in p^{n-j}$；R664 的整个交域核给 $\lambda^{2(n-j)}$。
故设
$$
\xi=\kappa^{n-N},\quad
H_{i,0}=D_*+e_i\mathcal E,\quad
K_{i,0}=H_{i,0}-14\alpha D_*,
$$
返回后的完整权恰为
$$
\boxed{
\begin{aligned}
\widetilde q_i(\xi)=
\frac{1_{\{C^\perp\ {\rm unit},\,H_{i,0}\in p^M\}}}{b\Omega^6}
\widehat P_p\bigl(&H_{i,0}/\kappa^M+\xi v_i,\\
 &14C^\perp+\tau K_{i,0}+\kappa^N\xi v_i,\\
 &G_\perp+g\tau K_{i,0}+g\kappa^N\xi v_i\bigr).
\end{aligned}}
\tag{10}
$$
这个门对所有 $n\ge N$ 都准确相同：
原 $H_{i,0}+\kappa^{n-j}v_i\in p^M$
等价于 $H_{i,0}\in p^M$。没有靠极限改门。
特别
$$
\boxed{\widetilde q_i(\xi)=\sum_{a=0}^6\xi^a\widetilde q_{i,a}}
\tag{11}
$$
是同一实际域上的 degree 至多六整测试多项式。
其系数准确用
$(v_i)^a(\partial_D+\kappa^N\partial_E+g\kappa^N\partial_G)^a/a!$
作用于 (10) 的原底点；全部阶乘为单位。

令
$$
w_0=(-8-18\omega)/315,\quad w_1=(-4+6\omega)/315,\quad
T_i=W_i-w_i\mathcal E-b_YY_i .
$$
$T_i\perp Y_i,\mathcal E$。
对固定奇偶性 $\epsilon=(-1)^n$，置
$$
Z_{i,\epsilon}=\epsilon b_YY_i+\tau w_i\mathcal E .
$$
因为 $j\ge1$，$Z_{i,\epsilon}$ 单位仍准确等价于 $Y_i$ 单位。
完整两个返回观察是
$$
\epsilon Y_i,\qquad
Z_{i,\epsilon}+\kappa^N\xi T_i .
\tag{12}
$$
由此定义
$$
\mathcal B_i^S(\xi,u)=
 \int\widetilde q_i(\xi)1_{Y_i\ {\rm unit}}
                  \langle Y_i\rangle^{d_pu}\,d\mu_0,
$$
$$
\mathcal B_{i,\epsilon}^T(\xi,u)=
 \int\widetilde q_i(\xi)1_{Y_i\ {\rm unit}}
 \langle Z_{i,\epsilon}\rangle^{d_pu}
 \left(1+\frac{\kappa^N\xi T_i}{Z_{i,\epsilon}}\right)^{d_pu}\,d\mu_0 .
\tag{13}
$$
于是完整同域式为
$$
\boxed{
\mathcal I_{i,n}^{Z}(u)
=c_j\lambda^{2n+2j}\mathcal B_i^Z(\kappa^{n-N},u).}
\tag{14}
$$
T 的 B 取实际 $\epsilon=(-1)^n$。
(13) 的整个 $Z_{i,\epsilon}$、七系数、log 和剩余三个伙伴都保留；
它们不是条件来源质量的替代。

结合 (8)、(14)，两个不同 cut 的严格差为
$$
\boxed{
\mathcal O_{i,n}^{Z}
=c_j\lambda^{n+3j}\mathcal A_i^Z
 -c_j\lambda^{2n+2j}\mathcal B_i^Z(\kappa^{n-N}).}
\tag{15}
$$
这是实际 cd 域内的原 Y 外部，而不是形式上添加一个自由补项。

## 4. 原 S 外部的精确单位过滤

S 的 $\mathcal B_i^S(\xi,u)$ 由 (11) 是 degree 至多六的准确多项式。
记 $\mathsf T$ 为同一固定 $N,j,p$ 下的 $n\mapsto n+1$，
取
$$
P_1(X)=\prod_{a=0}^6(X-\lambda^2\kappa^a).
$$
(15) 的第二项被这个**实际有限差分**完全杀掉。
所以
$$
\boxed{
P_1(\mathsf T)\mathcal O_{i,n}^S
=c_j\lambda^{n+3j}P_1(\lambda)\mathcal A_i^S .}
\tag{16}
$$
当前 ray 已付 $1-\lambda$ 为单位；对 $a\ge1$，
$1-\lambda\kappa^a$ 自动为单位。因此
$$
\boxed{P_1(\lambda)
=\lambda^7\prod_{a=0}^6(1-\lambda\kappa^a)\in\mathcal O^\times.}
\tag{17}
$$
原未切 cd 行于是由七步真实外部积分以单位系数准确恢复：
$$
\boxed{
\mathcal A_i^S
=c_j^{-1}\lambda^{-n-3j}P_1(\lambda)^{-1}
                 P_1(\mathsf T)\mathcal O_{i,n}^S.}
\tag{18}
$$
式 (16)–(18) 保整个 Mellin 函数，尤其同时保质量和中央导数。
序列还满足真正八阶递推
$$
(\mathsf T-\lambda)P_1(\mathsf T)\mathcal O_{i,n}^S=0.
\tag{19}
$$
这里只使用原 $n,\ldots,n+7$ 的同一 $q_N$；没有变动 N 或引入新测试。
(18) 不是声称这些外部积分已经为零。

## 5. 原 T 外部：质量精确、中央 log 的完整误差

T 必须保持奇偶性。令 $\mathsf T_2$ 是 $n\mapsto n+2$，
并取
$$
P_2(X)=\prod_{a=0}^6(X-\lambda^4\kappa^{2a}).
$$
完整低七个 $\xi$ 次数在这条实际序列中准确相消。
分母仍是单位：
$$
\boxed{P_2(\lambda^2)
=\lambda^{14}\prod_{a=0}^6(1-\lambda^2\kappa^{2a})
\in\mathcal O^\times.}
\tag{20}
$$
$a=0$ 用已付 $1-\lambda^2$，其它因子因含 p 自动为单位。

以 $\dot F=d_p^{-1}F'(0)$ 表示原 principal log 行。
(13) 的质量是 (11) 的 degree 至多六多项式，
故完整质量没有尾项：
$$
\boxed{
P_2(\mathsf T_2)\mathcal O_{i,n}^T(0)
=c_j\lambda^{n+3j}P_2(\lambda^2)\mathcal A_i^T(0).}
\tag{21}
$$
这同样不把质量认成零。

对 log 行展开 (13)。除 (11) 乘固定 $\log\langle Z_{i,\epsilon}\rangle$
所给的前七项外，其全部高系数来自
$$
\sum_{\substack{0\le a\le6\\r\ge1}}
\frac{(-1)^{r-1}\kappa^{Nr}}r\,\xi^{a+r}
 \int \widetilde q_{i,a}\,1_{Y_i\ {\rm unit}}
       (T_i/Z_{i,\epsilon})^r\,d\mu_0 .
\tag{22}
$$
所有 cut 均固定，$Z_{i,\epsilon}$ 的逆只在它的真实单位域使用。
因此第 k 项、$k\ge7$，准确有统一界
$$
v_p([\xi^k]\dot{\mathcal B}_{i,\epsilon}^T)
\ge (k-6)N-\lfloor\log_p k\rfloor .
\tag{23}
$$
在 $\xi=\kappa^{n-N}$ 上，完整尾不小于
$kn-6N-\lfloor\log_p k\rfloor$。
当前 $p\ge71,n\ge N\ge4$ 使其最小值至少 $7n-6N$。
有限过滤系数全整，所用 n 后续层只会提高这个界。

由 (15) 得
$$
\boxed{
\dot{\mathcal A}_i^T
=c_j^{-1}\lambda^{-n-3j}P_2(\lambda^2)^{-1}
       P_2(\mathsf T_2)\dot{\mathcal O}_{i,n}^T
       +p^{\,7n-6N}\mathcal O .}
\tag{24}
$$
所以沿任一 n 奇偶子列，右侧的显示实际积分有严格极限，
且该极限恰是 (7) 的同一原未切 log 行。
这里没有删去 $\log\langle b_Y\rangle$ 乘质量，
也没有把 T 的全级数截成有限多项式。

## 6. 与原两个中央的准确两外部接合

把 (16) 和 (4) 直接联立，得到整个 Mellin 函数的精确身份
$$
\boxed{
P_1(\mathsf T)\mathcal O_{i,n}^{S}
 +P_1(\lambda)\mathcal X_{i,n}^{S}
=P_1(\lambda)(-1)^i\lambda^n\beta^N J_S.}
\tag{25}
$$
这是两个显示的真实外部域与原 S 中央之间的单位返回。
$\mathcal O$ 是 cd 双深域内第二 Y 不深；
$\mathcal X$ 是原 cd 不双深的全部部分。
不能把二者当成同一事件，更不能单独置零。

T 有同样的完整等式，但必须保其真实余项：
$$
\boxed{
P_2(\mathsf T_2)\mathcal O_{i,n}^{T}
 +P_2(\lambda^2)\mathcal X_{i,n}^{T}
=P_2(\lambda^2)(-1)^i\lambda^n\beta^N\,6\delta J_T
 -\mathcal R_{i,n}.}
\tag{26}
$$
这里 $\mathcal R_{i,n}$ 定义为
$P_2(\mathsf T_2)$ 作用 (14) 的完整 T 双 Y 部分。
它的前七项准确相消，故
$$
\boxed{\mathcal R_{i,n}(0)=0,\qquad
v_p(\dot{\mathcal R}_{i,n})\ge7n-6N .}
\tag{27}
$$
这既给完整全函数余项的定义，又给实际中央所需的全尾界。

若只假设原 $J'_S(0)=J'_T(0)=0$，
(25) 的完整两外部导数组合为零；
(26) 的同一个实际组合则满足 (27) 的任意深精度。
这些是原两个假设的真实后果，不是多出的第三个中央零。
反过来，没有证明 (25)、(26) 的一个外部单项为零。

R665 的已知 $I_{\Sigma_5,-1}\ne0$ 位于另一条显示的 L 深观察，
R667 的自由差测试也保其全部浅/外部。
要将这些非零行放入 (25)、(26)，还须逐项匹配
(5)、(10) 和全部单位 cut；不能仅因它们共享原 sigma 来源而替换。
特别 (24) 恢复的是 (7) 的实际混合行，
不是无条件把它认成裸 $\Sigma_5$ 负一矩。

## 7. 已付范围与固定证书

本篇完整解决的是未切 cd 返回与真实双 Y 部分之间的比较：

- 固定 N 后，未切行的全部 n 依赖恰为 (8)；
- 额外双 Y cut 在同一来源上产生 (10)–(15)，S 是真正七项，
  T 保完整 仿射 单位和 log；
- 原外部的单位差分精确恢复 S，严格极限恢复 T；
- 两种外部与原中央准确接合为 (25)、(26)，没有被独立赋零。

主目标仍需 (25)、(26) 与已有非零行的合法同域消元。
本篇不把这个尚未完成的步骤称为已证明。

- [check-r671-fixed-depth-cd-return-and-exterior-filters.js](../scripts/check-r671-fixed-depth-cd-return-and-exterior-filters.js)
- [check-r671-fixed-depth-cd-return-and-exterior-filters.json](../scripts/check-r671-fixed-depth-cd-return-and-exterior-filters.json)

固定证书核原整个四轴词与 Y 归一、所有 q 参数、两观察、原七根过滤。
深度量词、实际积分、全部 tail 和单位分母由正文一般证明给出。

主要依赖：
[R664](R664-original-double-s-rotation-and-common-companion-gate.md)、
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)、
[R668](R668-original-double-s-shallow-annuli-and-exterior-words.md)；
固定原测试和完整 S5 张量同 R594/R653，未改其系数或物理周期。
