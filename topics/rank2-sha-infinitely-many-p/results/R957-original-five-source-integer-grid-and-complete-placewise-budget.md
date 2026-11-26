# R957 — 原五来源的全 89 余权整数格、真实 jet 与全部位预算

日期：2026-11-26。**状态：以下完整来源格、全部 89 个剩余权、固定导子整返回、同一整数商格上的普通与惰性 jet 预算，以及无旧公共载体的五块评价已证明。没有从五条中央同时为零推出整个来源格的深核；主目标未完成。**

本篇使用 R947 的完整五来源环。新增的格包含原五个来源及其全部合法乘积；它的整数格由实际五源单项式的像定义，实范数取同一呈示的 Euclidean 商范数。不会用一个随素数改变的有理基替换该整数格，也不把旧十九角模型、旧 $G_0$、十三行或其 Smith 结论移入新格。

## 1. 固定原输入、导子与权

沿用共同 $E_1:y^2=x^3+1$ 模型，令
$$
t=-x^{-3},\qquad \Theta=x\sigma^2,\qquad
w=z^6,\qquad
a=t(t-1)(7+4t+16t^2).
\tag{1}
$$
原五函数依次记为
$$
F=(S,T,U,V,W)=(S_{34},T_{72},U_{136},V_{66},W_{178}),
$$
$$
\mathbf d=(17,36,68,33,89).
\tag{2}
$$
这里 $d_\nu$ 是 $\Theta$ 权，物理 theta degree 为 $2d_\nu$。
每个 $F_\nu=w+O(w^2)$。五个完整角多项式、CM 相位和各自通常 Selmer 桥仍取 R821、R943 的原对象。

使用 R947 的固定整环 $R=\mathbf Z[1/N_0]$；可将其有限有理数局部化统一写成这种形式。特别 $R$ 包含该文两次真实 resultant 和首项所需的固定坏集。置
$$
A^{(5)}=R[S,T,U,V,W],
$$
$$
B_m=\Theta^m a^{k_m}R[t]_{\le e_m},\qquad
k_m=\lceil m/89\rceil,\quad
e_m=\lfloor29m/89\rfloor-4k_m,\qquad
B=\bigoplus_{m\ge0}B_m.
\tag{3}
$$
负帽表示零空间；$B_0=R$。R947 已证明 $B$ 是 $A^{(5)}$ 的完整规范化，并已处理全部剩余域、实际全函数域和整性。

本篇固定的返回乘子始终是同一个
$$
c=\Psi_Z(U+S^4,W;S),\qquad c_0=28883,
\tag{4}
$$
其中 $\Psi(u_+,w;Z)$ 是 R947 的 monic $1700$ 次最小式。求 $\Psi_Z$ 时保持 $u_+,w$ 不动。已有的实际包含是
$$
cB_m\subset R[S,U,W]_{m+c_0}\subset A^{(5)}_{m+c_0}.
\tag{5}
$$
其返回表达原总次数至多 $\lfloor(m+c_0)/17\rfloor$，系数只含固定坏分母，复 $\ell^1$ 范数至多 $C^{m+1}$。

写
$$
c=\Theta^{c_0}q_c(t),\qquad
r_c=\operatorname{ord}_{t=0}q_c,\qquad
\ell_c=[w^{r_c}]c(w).
\tag{6}
$$
R947 给 $q_c\in a^{325}R[t]$、$\deg q_c\le9411$，故
$$
325\le r_c\le9411,\qquad
\ell_c=(-1)^{r_c}[t^{r_c}]q_c\ne0.
\tag{7}
$$
以下所有固定好位还排除 $\ell_c$ 的分子、分母，以及原五源规范所需的固定有限坏集。需要五轴参数时另外保留 R943 的 $p>211$ 和 $B_5$ 行列式坏集。这些集合均先于 $M,k,p$ 固定。

## 2. 全 89 余权的一个准确自由模块

令
$$
X=\Theta^{89}a,\qquad Z=Xt^{25}.
\tag{8}
$$
这两个元素属于 $B_{89}$。它们是规范化中的两个具体来源，**不先验属于**原 $A^{(5)}$；其回返仍须乘 (4)。本节不把 $X,Z$ 当作新增自由算术中央。

对 $0\le r<89$ 定义
$$
\epsilon_r=\mathbf1_{r>0},\qquad
q_r=\lfloor29r/89\rfloor-4\epsilon_r.
$$
则对每个 $n\ge0$，准确有
$$
B_{89n+r}
=\Theta^r a^{\epsilon_r}X^n
 R[t]_{\le25n+q_r}.
\tag{9}
$$
对 $0\le i<25$ 再置
$$
\delta_{r,i}=\left\lceil\frac{i-q_r}{25}\right\rceil,\qquad
h_{r,i}=\Theta^r a^{\epsilon_r}X^{\delta_{r,i}}t^i.
\tag{10}
$$
这里 $-4\le q_r\le24$，所以 $\delta_{r,i}\in\{0,1,2\}$，没有负幂。
当 $\delta=2$ 时 $q_r\le-2$，从而 $1\le r\le9$；其余 $\delta\le1$。因此所有 $h_{r,i}$ 的权都不超过 $187$。

**定理 1。** 在原整环 $R$ 上，
$$
\boxed{B=\bigoplus_{\substack{0\le r<89\\0\le i<25}}
 R[X,Z]\,h_{r,i}.}
\tag{11}
$$
这是秩 $89\cdot25=2225$ 的自由模分解，保留全部 89 个权余类。

**证明。** 对 (9) 的一个显示单项式写 $j=25v+i$，其中 $v\ge0$、$0\le i<25$。允许的帽恰等价于
$$
25v+i\le25n+q_r
\quad\Longleftrightarrow\quad n-v\ge\delta_{r,i}.
$$
故该单项式唯一等于
$$
h_{r,i}\,X^{n-v-\delta_{r,i}}Z^v.
\tag{12}
$$
反向也逐项满足原帽。不同 $r$ 的 $\Theta$ 权模 89 不同。固定总权 $89n+r$ 后，先约去共同的非零因子 $\Theta^{89n+r}a^{n+\epsilon_r}$；剩下的幂恰为 $t^{25v+i}$，不同 $i$ 的次数模 25 不同，且该次数唯一确定 $v$。逐项比较遂得 (12) 中所有单项式线性独立；这里没有对未约去的 $a$ 展开后直接使用次数模 25。这同时证明 $X,Z$ 代数独立和 (11) 的整自由性。$\square$

特别这里保留 $r=1,\ldots,9$ 中确实需要 $\delta=2$ 的基；把所有负 $q_r$ 一概只乘一个 $X$ 会漏掉这些列。

完整维数可写成不省余权的有限式
$$
n_B(M)=
\sum_{r=0}^{88}
\sum_{\substack{n\ge0\\89n+r\le M}}
\max\{0,25n+q_r+1\}.
\tag{13}
$$
因此
$$
n_B(M)=\frac{25}{178}M^2+O(M+1).
\tag{14}
$$
常数只依赖固定的 89 个 $q_r$。公式 (11) 给一个无需十九角曲面就可使用的完整来源呈示；它没有免费比较旧评价矩阵。

## 3. 固定坏分母的完整清除

需要把 (5) 的 $R$-返回变为真正的 $\mathbf Z$-多项式来源。R947 §6 的构造使用一份先于 $m$ 固定的有限乘法表和有限多个 $cg$ 的整返回；每个显示基
$$
b_{m,j}=\Theta^m a^{k_m}t^j,\qquad 0\le j\le e_m
\tag{15}
$$
只需 $O(m+1)$ 次该表的运算。

取这些固定表、固定终端返回表达全部有理系数分母的一个共同倍数，并把固定的线性步数常数吸收进其一个固定整数次幂。于是存在明确由这份有限资料定义的整数 $D_0\ge1$，其素因子仍全在一个固定有限集合内，使
$$
D_0^{m+1}c\,b_{m,j}
\in\mathbf Z[S,U,W],
$$
$$
\deg_{S,T,U,V,W}\le
\left\lfloor\frac{m+c_0}{17}\right\rfloor,\qquad
\|\operatorname{return}(D_0^{m+1}c\,b_{m,j})\|_1
\le C_0^{m+1}.
\tag{16}
$$
这是一份固定有限表的定义，不是每个 $m$ 重新求大矩阵逆并允许新分母。分母在相乘时至多乘其共同倍数；有限表每步的 $\ell^1$ 算子范数相乘，给 (16)。换 $U+S^4$ 回原 $U,S$ 的二项式增长已在 R947 的同表成本中支付。

对整段 $m\le M$ 可统一使用
$$
Q_M=D_0^{M+1}.
\tag{17}
$$
由 (16)，所有 $Q_Mc b_{m,j}$ 都是原五变量的整数多项式，权 $m+c_0$，总次数至多 $(M+c_0)/17$，返回系数范数至多 $C_1^{M+1}$，其中常数不依赖 $m,j,M$。

此清分母不是零成本：在无穷位 $\log Q_M=(M+1)\log D_0$。若从已清的来源恢复未清的 $cb$，有限位代价只在 $p\mid D_0$ 出现，恰为
$$
(M+1)v_p(D_0)\log p,\qquad
\sum_{p\mid D_0}(M+1)v_p(D_0)\log p=(M+1)\log D_0.
\tag{18}
$$
所以全部指数清分母成本为 $O(M+1)$，并且仅落在固定坏位；没有未付的随 $M$ 增长的新素数集合。

## 4. 真正的完整五源整数格及其同一范数

置 $N=M+c_0$，并令
$$
\mathcal I_N=
\{e\in\mathbf Z_{\ge0}^5:\mathbf d\cdot e\le N\},\qquad
P_N=\bigoplus_{e\in\mathcal I_N}\mathbf Z\,E_e.
$$
原评价呈示是
$$
\operatorname{ev}:P_N\longrightarrow\mathbf Q[[w]],
\qquad E_e\longmapsto F^e.
$$
定义
$$
\boxed{\Lambda_M=\operatorname{im}(\operatorname{ev}),\qquad
\mathscr K_N=\ker(\operatorname{ev}),\qquad
\Lambda_M=P_N/\mathscr K_N.}
\tag{19}
$$
因此 $\Lambda_M$ 本身包含所有权不超过 $N$ 的原五源整数单项式，特别包含 $1,S,T,U,V,W$。这里没有只保留导子理想，也没有用贪心有理基来替换这个整数像格。预算变量是新的 $M$，实际权上界始终为 $N=M+28883$，不与旧十九角的 $D$ 相认。

$\mathscr K_N$ 是 primitive 子格：若 $nP$ 评价为零，则 $P$ 已评价为零。故 $\Lambda_M$ 是自由有限秩 $\mathbf Z$-模。其有理空间准确是 $A^{(5)}_{\le N}\otimes\mathbf Q$。由 (17)，同一个格中有显式独立主块
$$
Q_Mc\bigoplus_{m\le M}\bigoplus_{0\le j\le e_m}\mathbf Z\,b_{m,j}
\ \subset\ \Lambda_M.
\tag{20}
$$
上、下均在 $B$ 中比较，得到
$$
n_B(M)\le n_M:=\operatorname{rank}\Lambda_M\le n_B(M+c_0),
$$
$$
\boxed{n_M=\frac{25}{178}M^2+O(M+1),\qquad
n_M-n_B(M)=O(M+1).}
\tag{21}
$$
因此需要补到整个五源空间的有理维数只有 $O(M)$。这不是断言任意补的有理基都在每个 $p$ 饱和。

(20) 的源用 (15) 的标准系数格。由 (16)–(17)，这个实际包含的实算子范数至多 $\exp(O(M+1))$，在每个有限位是整映射；全部位均是同一整数多项式返回。固定好位处，R947 的 $cB$ 在 $A^{(5)}$ 中的 $p$-饱和性、权分解与 $Q_M$ 为单位，还给 (20) 在 $\Lambda_M$ 中的 $p$-饱和性。这个饱和性属于来源格，不声称截断 jet 的像饱和。

在无穷位，把 $P_N\otimes\mathbf R$ 的标准 Euclidean 范数下降为
$$
\|f\|_{\infty,\Lambda}
=\inf_{\operatorname{ev}(x)=f}\|x\|_2.
\tag{22}
$$
在每个有限位，单位球准确取
$$
\Lambda_M\otimes\mathbf Z_p
=\operatorname{im}\bigl(P_N\otimes\mathbf Z_p\bigr),
\tag{23}
$$
并用相应的 lattice gauge 范数。全部位、全部前缀始终使用这同一格。
由于 $\mathscr K_N$ primitive，(23) 是整商格，不是将有理商任意定成一个 $p$-整标准格。

还须支付实商范数的算术次数。对一个 $\mathscr K_N$ 的整数基扩成 $P_N$ 的整数基，正交投影到其正交补并用 Gram 行列式的 Schur 补，得到
$$
\operatorname{covol}(\Lambda_M)
=\operatorname{covol}(\mathscr K_N)^{-1}.
$$
$\mathscr K_N$ 的 Gram 行列式是正整数；秩零时取一。因此
$$
\boxed{\widehat{\deg}\Lambda_M
:=-\log\operatorname{covol}(\Lambda_M)\ge0.}
\tag{24}
$$
没有把这个方向反写为一个未经证明的上界。

### 4.1 全部真正饱和前缀

对 $k\ge0$ 定义唯一的实际系数行
$$
r_k(f)=[w^k]f(w),\qquad
K_{M,k}=
\Lambda_M\cap\ker_{\mathbf Q}(r_0,\ldots,r_{k-1}),
\qquad \varphi_M^k=r_k|_{K_{M,k}\otimes\mathbf Q}.
\tag{25}
$$
每个 $K_{M,k}$ 都在 $\Lambda_M$ 中饱和，且
$$
K_{M,k}\otimes\mathbf Z_p
=(K_{M,k}\otimes\mathbf Q_p)\cap
(\Lambda_M\otimes\mathbf Z_p).
\tag{26}
$$
实范数为 (22) 的限制；有限位范数为 (23) 的限制。其随后的一维商再取商范数。

有限维实际函数空间由其全部 Taylor 系数分离，所以此旗标最终为零。令其全部非零层的指标为
$0\le k_1<\cdots<k_{n_M}$。每层恰降一维。primitive 性和正交商的行列式相容给
$$
\widehat{\deg}\Lambda_M=\sum_i\widehat{\deg}
(K_{M,k_i}/K_{M,k_i+1}).
$$
若一维商的整数生成元为 $\gamma_i$，且
$a_i=r_{k_i}(\gamma_i)\in\mathbf Q^\times$，乘积公式逐层给
$$
\sum_v\log\|\varphi_M^{k_i}\|_v
=\log|a_i|_\infty-\log\|\gamma_i\|_\infty
+\sum_p\log|a_i|_p
=-\log\|\gamma_i\|_\infty.
$$
因此
$$
\boxed{0\le\widehat{\deg}\Lambda_M
=\sum_{i=1}^{n_M}\sum_v\log\|\varphi_M^{k_i}\|_v.}
\tag{27}
$$
这些正是同一整数格的真实非零跳跃；未用任何指定矩形窗替代它们。

## 5. 所有列先证全纯，再作 Cauchy

(15) 的角多项式展开只含
$$
k_m+j\le n\le4k_m+j\le\lfloor29m/89\rfloor<m/3
\quad(m>0).
$$
在原函数中逐项准确有
$$
\boxed{\Theta^m t^n=(-1)^n\sigma^{6n}\Theta^{m-3n}.}
\tag{28}
$$
所有指数非负。因此 (15)、(10) 及它们的所有乘积都是原正 degree 的真正全纯 theta 截面；它们是六重不变函数，遂为 $w$ 上整函数。这一步没有把形式角坐标 $t$ 当成全局整函数。

由于
$$
a=-7t+3t^2-12t^3+16t^4,
$$
其幂的系数 $\ell^1$ 范数至多 $38^{k_m}$。sigma 准周期式和原 $\Theta=x\sigma^2$ 的全纯性给固定 $C$，使
$$
|\sigma(z)|,\ |\Theta(z)|
\le C\exp(C|z|^2)
$$
（把有限基本平行四边形上的已消极部分一并支付）。
结合 (28) 得
$$
|b_{m,j}(w)|\le C^{m+1}\exp(Cm|w|^{1/3}).
\tag{29}
$$
乘 (4)、(17) 只把权加 $c_0$ 并增 $O(M)$ 系数成本。

对于真正的 $\Lambda_M$，还可直接从其全部原五源单项式取得同一界。每个单项式次数至多 $N/17$，且
$$
|\mathcal I_N|\le(1+\lfloor N/17\rfloor)^5.
\tag{30}
$$
取 (22) 的最小实提升，用 Cauchy–Schwarz 控制其系数 $\ell^1$ 范数，只增加 $\sqrt{|\mathcal I_N|}$。
于是同一个商范数的实际系数行满足，对全部 $M\ge0,k\ge1$，
$$
\boxed{
\log\|\varphi_M^k\|_\infty
\le-3k\log k+3k\log(M+1)+O(k+M+1).}
\tag{31}
$$
证明是在 $|w|=R$ 取
$R^{1/3}$ 为 $k/(M+c_0+1)$ 的固定倍数；小时取 $R=1$。
固定 $c_0$、$D_0$、全部系数表及 (30) 均只进入统一常数。
这里没有先将未证全纯的形式 $B$-基放进 Cauchy 估计。

## 6. 同一 ordinary 整测度、卷积后切域与真正前缀

对固定坏集外的 $p\equiv1\pmod6$，R316 §3 在同一个 CM 形式群单位周期 $\Omega_p$ 下已证明
$$
\sigma(\Omega_p\log(1+Z)),\quad
\Theta(\Omega_p\log(1+Z))\in\mathcal O[[Z]]
$$
整且有界；三次 CM 使所需 Gaussian 修正为零。共同 $E_1$ 模型与五条曲线各自尺度的比较仍取 R469、R820、R943 的已付桥；没有把一个固定代数数任意当作 $\mathbf Z_p$ 测度变量的缩放。

令 $\nu_\nu$ 的 Amice 变换准确为
$F_\nu(\Omega_p\log(1+Z))$。由 (28) 和原五角多项式，它们都是有界整测度。每个真实单项式的测度定义为
$$
\boxed{\nu_e=\nu_S^{*e_S}*\nu_T^{*e_T}*
\nu_U^{*e_U}*\nu_V^{*e_V}*\nu_W^{*e_W}.}
\tag{32}
$$
零指数全部为空时取 $\delta_0$。有限乘积是加法卷积，因此仍整且有界。对一个原整数多项式取对应测度的整数线性组合；若两个表达定义同一 $f\in\Lambda_M$，其 Amice 变换相同，测度也相同。这证明 $\nu_f$ 真正下降到 (19)，没有依赖某个有理表达。

**完整单位切域必须在卷积之后。** 若把各因子变量统记为 $x_{\nu,j}$，置
$Y=\sum_{\nu,j}x_{\nu,j}$。单项式的真实单位 Mellin 行为
$$
\boxed{
J_{e,p}(u)=
\int
\mathbf1_{Y\in\mathbf Z_p^\times}
\langle Y\rangle^{(p-1)u}
\prod_{\nu,j}d\nu_\nu(x_{\nu,j}).}
\tag{33}
$$
其中央导数在同一个域中插入
$(p-1)\log_p\langle Y\rangle$。没有将该域换成
“每个输入都是单位”，也没有把 (33) 写成五个 Mellin 函数的乘积。
五原中央零只在五个原一阶单项式上给相应的零；它不自动给 (32) 的乘积中央零。

对于全部 $f\in\Lambda_M\otimes\mathbf Z_p$，同一测度的完整矩严格为
$$
\int x^{6h}d\nu_f
=\Omega_p^{6h}(6h)!\,r_h(f),\qquad
\int x^j d\nu_f=0\quad(6\nmid j).
\tag{34}
$$
所有这类 $f$ 都有 $P_N\otimes\mathbf Z_p$ 的整提升，所以测度范数至多一；不需选择一个未付分母的 $\mathbf Q_p$-基。

若再 $f\in K_{M,k}\otimes\mathbf Z_p$，所有低于 $6k$ 的矩准确为零。将
$$
(x)_{6k}=\prod_{j=0}^{6k-1}(x-j)
$$
代入测度；它在整个 $\mathbf Z_p$ 上属于 $(6k)!\mathbf Z_p$。
利用 (34) 的同一低前缀，有
$$
\Omega_p^{6k}(6k)!\,r_k(f)
=\nu_f((x)_{6k})\in(6k)!\mathcal O.
$$
单位周期和最高阶乘准确抵消，故
$$
\boxed{\|\varphi_M^k\|_p\le1}
\tag{35}
$$
对全部好 ordinary $p$、全部 $M,k$ 成立。等价地，原 Amice 变换在此前缀下从 $Z^{6k}$ 起，其首系数恰为 $\Omega_p^{6k}r_k(f)$。这证明的是实际饱和 jet 的整性，而不只是五个单独函数的整性。

## 7. 全 inert 成本与固定坏位

取固定坏集外的 $p=6s-1$。保持 R301/R418 的真实半径
$$
\rho_p=p^{-p/(p^2-1)}.
\tag{36}
$$
在任意物理圆盘半径 $r<\rho_p$ 上，原 Gaussian 及其逆真正收敛且范数一，并有
$$
\|\Theta\|_r=1,\qquad \|t\|_r=r^6,\qquad
\|F_\nu\|_r\le r^6.
\tag{37}
$$
最后一式对五个完整角多项式成立：各有整系数、首 $t$ 项为单位并从 $t$ 起。新 $W$ 不使用旧十九角界；它直接用 R943 的完整 $f_W$ 和 R947 的整模型。

因此每个 $\Lambda_M$ 单位球元素在该圆盘范数至多一。趋向 $\rho_p$ 得
$$
\boxed{
\log\|\varphi_M^k\|_p\le
e_p(k)\log p,\qquad
e_p(k)=\left\lfloor\frac{6kp}{p^2-1}\right\rfloor.}
\tag{38}
$$
取整合法，因为 $r_k(f)\in\mathbf Q_p$。限制到 (25) 的真正核不增范数。此式没有将临界圆周的指数当作仍收敛。

导子主块的逐列起阶也可准确保留：对固定好位，
$$
\|b_{m,j}\|_r=r^{6(k_m+j)},\qquad
\|c\|_r=r^{6r_c},\qquad |Q_M|_p=1.
$$
于是其列在 $k<r_c+k_m+j$ 时系数为零，其他系数的上界可将 (38) 中 $k$ 换成 $k-r_c-k_m-j$。这是实际列阶收益；整个 $\Lambda_M$ 含常数列，不能将每一列都按该最低阶处理。

和 R418 一样，固定模六的素数 Mertens 公式、一次取整误差和
$p/(p^2-1)-1/p$ 的可和误差给
$$
\boxed{\sum_{p\equiv5(6)}e_p(k)\log p
=3k\log k+O(k+1).}
\tag{39}
$$
在固定坏位，为五个固定真实函数选一个共同的正收敛半径和有界较小闭盘。单项式次数至多 $N/17$，故逐系数 Cauchy 给
$$
\log\|\varphi_M^k\|_p\le C_p(k+M+1).
$$
坏位有限，合并成本为 $O(k+M+1)$。式 (18) 的清分母/恢复费用也只增加这里的 $O(M+1)$ 项。没有删去任何尚未估计的无限位集合。

## 8. 在新整数格上定义实际五块评价

本节给明确的新矩阵，而不是将旧 $M_D$ 改名。固定 $p=6s-1>211$，
$1\le\ell<s$，$L=4s+\ell$，并置
$$
\Gamma_L=\mathcal O[w,\varepsilon]/
(w^s-p\varepsilon,\varepsilon^5,w^\ell\varepsilon^4).
\tag{40}
$$
其 $\mathcal O$-基是 $w^i\varepsilon^j$，$j=0,1,2,3$ 时 $0\le i<s$，$j=4$ 时 $0\le i<\ell$。

保持 R943 的**实际** $\kappa$、$a_p=p\kappa\in\mathcal O^\times$、$t(w)$，置 $d(t)=1+8t$，并令
$$
h_A=(g_A/d)^{1/17},\qquad
\mathcal E=\frac1{17}\Theta\partial_\Theta.
\tag{41}
$$
这里为免混淆，R943 的指数扰动另记为 $\eta_A(w)$；于是
$g_A=g_\circ e^{\eta_A}$、
$h_A=h_\circ e^{\eta_A/17}$。
在实际 $A=A^*$ 时，
$$
h_{A^*}=\Theta\exp(-\kappa w^s/17).
\tag{42}
$$
原 R614 addition 整窗和 R943 的整指数论证，保证 $t,h_A$ 在本节 $L<5s<p$ 的全窗口整；取 $1/17$ 次根用单位导数的形式 Hensel，保全系数，不仅取首项。

对源多项式 $P(t,\Theta)$ 定义
$$
P_i(w)=(\mathcal E^iP)(t(w),h_A(w)).
$$
令 $\mathscr S$ 为准确的 $s$ 阶系数移位。新完整五块评价为
$$
\boxed{
\mathcal J_{5,A}(P)_j
=\left[\sum_{i=0}^j
\frac{a_p^i}{i!}p^{j-i}\mathscr S^{\,j-i}P_i
\right]_{<m_j},
\quad m_0=m_1=m_2=m_3=s,\quad m_4=\ell.}
\tag{43}
$$
所有分母 $17,i!$ 在当前为单位。各列使用其真实总权；不存在旧相对 charge 加四十的约定。

在实际 $A^*$ 上，若 $\mathcal J$ 的 $(j,i)$ 坐标按 (40) 读取，则
$$
\boxed{\mathcal J_{5,A^*}(f)_{j,i}
=p^j\,r_{js+i}(f).}
\tag{44}
$$
证明先对一个权 $n$ 的完整列使用
$$
f=e^{(n/17)\kappa w^s}P(t,h_{A^*}),
$$
再对第 $j$ 块取系数并乘 $p^j$，逐项正是 (43)；一般源线性相加。
因此 (34) 的 ordinary 矩与 (44) 的 inert 五块读取都来自 (25) 中同一份物理系数 $r_k$。本节没有把 ordinary 单位切域当作 (44)。

$\mathcal J$ 也可看成把真实乘法按 $w^s=p\varepsilon$ 逐项折回的环评价；Gaussian 为
$\exp((n/17)a_p\varepsilon)$ 的实际截断。R418 的实际 $t,\Theta$ 代数独立性保证呈示核中的关系就是同一 $R[t,\Theta]$ 里的多项式恒等式。故原五源的全部整多项式关系在这里仍准确为零，(43) 从整个单项式呈示下降到
$\Lambda_M\otimes\mathcal O$。没有把呈示中的永久关系误算成新首核。

### 8.1 完整参数运输：第一项没有免费的一次 $p$

沿 R943 §9 写
$$
\eta_A(w)=w^{s-5}K_A(w),\qquad
K_A=P_4+w^5H_A,\qquad P_4=u_0+\cdots+u_4w^4.
$$
由于 $s>35$，所有 $j\ge6$ 的扰动首阶超过 $5s$，而 $j=1,\ldots,5$ 必须按真实 $w$ 阶先折回。得到
$$
\boxed{\begin{aligned}
\mathcal J_{5,A}={}&\mathcal J_{5,\circ}
+w^{s-5}K_A\,\mathcal J_{5,\circ}\mathcal E\\
&+\frac{p\varepsilon}{2}w^{s-10}K_A^2
       \mathcal J_{5,\circ}\mathcal E^2
+\frac{p^2\varepsilon^2}{6}w^{s-15}K_A^3
       \mathcal J_{5,\circ}\mathcal E^3\\
&+\frac{p^3\varepsilon^3}{24}w^{s-20}K_A^4
       \mathcal J_{5,\circ}\mathcal E^4
+\frac{p^4\varepsilon^4}{120}w^{s-25}K_A^5
       \mathcal J_{5,\circ}\mathcal E^5 .
\end{aligned}}
\tag{45}
$$
所有乘积继续在整个 (40) 中折回，保 $H_A$ 的完整高尾。公式来自
$j(s-5)=(j-1)s+(s-5j)$，没有负形式幂或提前删 $\varepsilon^5$ 的步骤。

特别第一项的扰动没有旧 $w^{13}$ 将它推出当前块。因此在这个新格上不能引用旧 $\bar M_A=\bar M_\circ$。准确地
$$
\overline{\mathcal J}_{5,A}-\overline{\mathcal J}_{5,\circ}
=w^{s-5}P_4(w)\,
       \overline{\mathcal J}_{5,\circ}\mathcal E.
\tag{46}
$$
其行支持在四个完整块的
$$
[(j+1)s-5,(j+1)s),\qquad j=0,1,2,3,
\tag{47}
$$
以及最后短块与 $[5s-5,5s)$ 的交。总行数准确至多
$$
20+\max\{0,\ell-s+5\}\le24.
\tag{48}
$$
对任意长度 $K\le L$ 的**同一个有序前缀**，两个模 $p$ 秩之差绝对值不超过 (47)–(48) 与 $[0,K)$ 的交集基数。因 $\mathcal E$ 保权，而所有权 $n>356$ 的 $B_n$ 已从 $w^5$ 起，(46) 还只读取
$A^{(5)}_{\le356}$ 的固定低权部分；权零常数被 $\mathcal E$ 杀掉。

这是有限行支持的准确界，不是主阶改进。更高精度的 (45) 仍读完整高尾，不能从 (48) 给全部 Smith 指数预设上界。

### 8.2 同一导子主块的实际平移和固定 carry

若另有
$$
r_c+\ell<s,
\tag{49}
$$
则在物理目标 $\Gamma_{L+r_c}$ 中，局部归一的 $c$ 准确为
$w^{r_c}$ 乘一个整单位，再乘同权 Gaussian
$\exp(c_0a_p\varepsilon/17)$。令所得完整单位为 $U_{c,A}$。
对主块 (20) 有准确同源式
$$
\boxed{
\mathcal J_{L+r_c,A}(Q_M cP)
=Q_M U_{c,A}\,m_{r_c}\mathcal J_{L,A}(P),}
\tag{50}
$$
其中 $m_{r_c}$ 就是乘 $w^{r_c}$，所有 $P\in B_{\le M}$。
$U_{c,A}$ 保整个 $q_c,t,h_A$，不能只取其常数；
$Q_M$ 在固定好位为单位。

在 (49) 下，四个完整块各有恰 $r_c$ 个坐标跨界，
$$
w^i\varepsilon^j\longmapsto
p\,w^{i+r_c-s}\varepsilon^{j+1}
\quad(s-r_c\le i<s,\ j=0,1,2,3).
$$
其它坐标乘一；最后短块不跨界。像坐标互不重叠，最前 $r_c$ 个物理目标方向为空。因此 $m_{r_c}$ 的 Smith 数据是：

- $4r_c$ 个指数一；
- 其余源指数零；
- $r_c$ 个自由余目标方向。

所以该主块的固定 torsion 成本为 $4r_c$，在 (7) 的固定范围内。
这只比较 (50) 的同一主块；不能把整个 $\Lambda_M$ 的其它列与它的秩相加。
在 (49) 不成立时仍用 (43)–(45) 的完整真实折回，不能继续套用上述简化成本。
本篇没有使用旧十三行、旧 $P_{134}$、旧 $U_0$ 或旧52成本。

## 9. 新格的严格全次数门及准确消费范围

对新的真实 $\Lambda_M$，已证明：

- 秩 $n_M=(25/178)M^2+O(M)$，含全部五源合法乘积；
- 复侧是 (31)，普通全部实际饱和层成本为非正；
- 惰性无条件完整包络为 (38)–(39)，固定坏位及清分母成本为 $O(k+M+1)$；
- 物理五块矩阵为 (43)，参数变化和所有导子跨界为 (45)、(50)。

若以后在**同一个** (19)、(25) 上由五条原中央失败证明
$$
\sum_{p\equiv5(6)}\log\|\varphi_M^k\|_p
\le a\,k\log(M+1)+b\,k\log k+O(k+M+1),
\tag{51}
$$
对所有 $M,k$ 的真实非零层统一成立，且 $a,b\ge0$，则
$$
\boxed{a+2b<3}
\tag{52}
$$
仍给全局矛盾。这里没有只在 $p\asymp M^2$ 的一个有限窗假设 (51)。

为核定此门也适用于实商范数，用 (27) 对全部真实跳跃求和。记
$S_M=\sum_i k_i$，并约定 $0\log0=0$。因指标互异，
$S_M\ge n_M(n_M-1)/2\gg M^4$。
凸性给
$$
\sum_i k_i\log k_i
\ge S_M\log(S_M/n_M)
\ge S_M(2\log(M+1)-O(1)).
$$
当 (52) 成立时 $b<3$，于是 (31)、(35)、(51) 使 (27) 的右端至多
$$
(a+2b-3)S_M\log(M+1)+O(S_M+n_M(M+1)),
$$
对充分大 $M$ 严格负，矛盾。$n_M(M+1)=O(M^3)$ 已被准确比较；
固定导子的大常数和所有指数系数费用都未进入主项。

当前 (39) 仍是 $(a,b)=(0,3)$。本篇支付的是一个真实、完整、可承载第五来源的整数格及其所有位成本；它没有凭 Hilbert 常数或低行支持达到 (52)。
五条原中央的必要条件仍为 R943 的实际 $u^*\equiv u^\dagger\pmod{p^5}$。
要消费这些值，须把它们作用到 (43) 的具体来源或同一真实仿射修正族；不能把五个原测度的中央零移给 (32) 的所有卷积，也不能把新格的全 $p^2$ 核换成旧 parity 子块核。

本篇没有数学数值运行或素数扫描，没有保存可重算表。所有有限格和系数常数由 R947 的同一已付有限资料定义；全 $M,k,p$ 论证由正文逐式给出。

## 依赖

- [R947](R947-original-e89-normalization-and-integral-conductor.md)：实际 $W$、完整规范化、同环 $U+S^4$、唯一 $\Psi$、权28883导子及固定有限返回表。
- [R943](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md)：第五原算术来源、共同高轴、完整 Newton 必要值与真实整窗口。
- [R821](R821-original-four-central-axes-and-complete-four-block-carries.md)：原四来源及准确尺度；本篇没有搬入其旧公共载体。
- [R316 §3](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：同一 $\sigma,\Theta,\Omega_p$ 的真实有界整 Amice 测度及原 CM Gaussian 规范。
- [R473 §5–5.1](R473-three-source-function-field-normalization-and-integral-conductor.md)：全纯非负幂返回、整测度与实际 jet/抽象饱和的区别。
- [R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)：原真实解析半径与完整惰性素数和；本篇已在新的完整整数商格上重付全旗标及严格门。
- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：原 regularized $\Theta$ 与 $t$ 的 addition 整窗，供 (41)–(45) 使用。
