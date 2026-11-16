# R866 — 原 Hom 的有限模函数证书、level-nine 小模型与完整 541 项输入

日期：2026-11-16。

**状态：本篇证明原 X0(2601) 上的模函数有限认证门，并给出无需复周期的确定性重建程序及完整原 CM 系数公式。实际参数化坐标、最小整 Hom 分母和非零原 shadow 仍待计算。本篇不把形式积分、一个有限近似或原 canonical 类的 7993 读数当作原端点循环的非零。**

本篇接 R862 的同一个三维新因子、同一三枚原角色和规范 Hom。
有限代数常数使用 R864 的实际公开证书；下面的模函数程序不另选角色、
不删2处 Euler 项，也不更换 R831 的两个退化映射。

## 1. 固定输入与一个更小的实际椭圆模型

沿 R862，固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
L=K(a),\quad a^3=17,\quad H_9=K(h),
$$
以及
$$
\alpha=-1+2\omega,\qquad c=-1-19\omega,\qquad b^3=c,
\qquad \ell=\alpha h/h^\sigma,\quad N_{L/K}(\ell)=c.
\tag{1}
$$
这里 $\sigma$ 是原7理想的 Artin 元；其限制 $\tau$ 生成
$\operatorname{Gal}(L/K)$。不得按任意三次根选择重置 $\tau$。

R864 的公开证书给
$$
v=\frac{h^3}{2^{32}}
=-122465-47628a-\frac{314892}{17}a^2,
\qquad
v^3+367395v^2+147v+\frac1{17}=0.
\tag{2}
$$
原曲线 $C_h:y^2=x^3+h^6$ 可以准确改写为
$$
\boxed{C_v:\ Y^2+vY=X^3.}
\tag{3}
$$
从 (3) 到 $C_h$ 的实际同构是
$$
x=2^{22}X,\qquad y=2^{33}Y+2^{32}v,
\qquad
\omega_C=\frac{dx}{2y}
=2^{-11}\frac{dX}{2Y+v}=2^{-11}\omega_v.
\tag{4}
$$
代入方程逐项得到 (4)，没有任意最小模型倍率。
特别地
$$
\Delta(C_v)=-27v^4.
$$
由 (2)，$v\equiv1\bmod2$，所以 (3) 在所有2上方的位均为好约化模型。

在17处用 $v_L(a)=1$ 的离散规范。由于
$314892\equiv1\bmod17$，(2) 的唯一最低项给 $v_L(v)=-1$。
置
$$
X=a^{-2}X',\qquad Y=a^{-3}Y'.
$$
则模型和微分准确变为
$$
Y'^2+17vY'=X'^3,\qquad
\omega_v=a\,\frac{dX'}{2Y'+17v}.
\tag{5}
$$
其系数整，$v_L(17v)=2$，判别式赋值为8，故这是17处的最小模型
（可再缩小的整 Weierstrass 模型会把赋值减12，不可能）。
(4)、(5) 只剥掉已显示的模型尺度，**不证明 Manin 因子为1**。

令 $\Theta_i:A\to C_h$ 是 R862 的三个规范准同态。
经 (4) 反向同构得到 $\widetilde\Theta_i:A\to C_v$。
实际计算采用更小的规范准同态
$
\boxed{\Xi_i=2^{-11}\widetilde\Theta_i,\qquad
       \Xi_i^*\omega_v=H_i(q)\frac{dq}{q}.}
\tag{6}
$
设 $d=h/2^{11}$，则 $d^3=v/2$，到原 $E_0$ 的实际同构是
$
\kappa:C_v\longrightarrow E_0,\qquad
(X,Y)\longmapsto(X/d^2,\ 2Y/v+1),\qquad
\kappa^*\omega_0=d\,\omega_v.
\tag{6a}
$
所以 R862 的原 $\mathcal A_i$ 准确等于 $2^{11}\kappa\Xi_i$。
我们在仅三次域 $L/K$ 内重建 $n\Xi_i$ 的有理函数，再用
$(2^{11}/n)\kappa(n\Xi_i)$ 表示同一原 $\mathcal A_i$。
原整数 $n$、$2^{11}$、$h$ 和 Artin 系数全部保留。
这避免先重建一个额外的 $[2048]$ 倍映射；也不声称 $n=1$ 已整。

## 2. 原曲线的两个小模函数

定义
$$
T(z)=\left(\frac{\eta(z)}{\eta(9z)}\right)^3
=q^{-1}\prod_{m\ge1}
  \frac{(1-q^m)^3}{(1-q^{9m})^3},
\qquad q=e^{2\pi iz}.
\tag{7}
$$
其 eta 指数为 $r_1=3,r_9=-3$。
两个变换和分别是 $-24,24$，总权为0，平方条件是 $9^{-3}=3^{-6}$。
Ligozat 的变换及 cusp 阶公式遂给
$$
\operatorname{div}_{X_0(9)}(T)=[0]-[\infty].
\tag{8}
$$
具体地，分母层为 $d=1,3,9$ 的四个 cusp 上，
阶分别为 $1,0,-1$；$d=3$ 有两个 cusp。
eta 在上半平面没有零极点。因此 (8) 是全部除子。
它证明 $T$ 是 $X_0(9)\simeq\mathbf P^1$ 的有理参数，
且 $T=q^{-1}+\mathbf Z[[q]]$。

现在取原
$$
C=X_0(2601),\qquad
S=T(z),\quad U=T(17z),\quad V=T(289z).
\tag{9}
$$
由于17素于9，
$$
[\Gamma_0(9):\Gamma_0(2601)]=17(17+1)=306.
$$
两个端点函数已经生成全原函数域：
$$
\boxed{\mathbf Q(C)=\mathbf Q(S,V).}
\tag{10}
$$
一种直接证明是在上半平面上使用 $T$ 为 Hauptmodul：
同时固定 $T(z)$ 和 $T(289z)$ 的群恰为
$$
\Gamma_0(9)\cap
\begin{pmatrix}289&0\\0&1\end{pmatrix}^{-1}
\Gamma_0(9)
\begin{pmatrix}289&0\\0&1\end{pmatrix}
=\Gamma_0(2601).
$$
等价地，一般非 CM 椭圆曲线及其给定9子群的两个端点，
唯一确定所给 cyclic $17^2$ isogeny（允许的符号不改变子群）。
有理 $q$-展开再给 (10) 的 $\mathbf Q$ 下降。

$S,V:C\to\mathbf P^1$ 的次数都为306。
令
$$
D=(S)_\infty+(V)_\infty.
$$
则
$$
\boxed{\deg D=612,\qquad
\operatorname{ord}_\infty S=-1,\quad
\operatorname{ord}_\infty V=-289.}
\tag{11}
$$
这两个端点是 (9) 的实际坐标，不把中间17同源或原 $q_0/q_2$ 互换。

## 3. 两个 degree18 方程给原非回溯 degree306 分支

存在唯一 monic 多项式
$$
\Phi_{17}(S,V)\in\mathbf Z[S,V],\qquad
\Phi_{17}(T(z),T(17z))=0,
$$
其实际根为
$$
T(17z),\qquad T((z+r)/17)\quad(0\le r<17).
\tag{12}
$$
这里每个根均带原 level9 的 cyclic 子群结构。
17同源保持 cusp 的9-primary分母层，因此 (12) 的初等对称函数
只在 $T=\infty$ 有极点；它们是 $T$ 的多项式。
$T=q^{-1}+\mathbf Z[[q]]$ 和根的对称性给整系数。
双同源给 $\Phi_{17}(S,V)=\Phi_{17}(V,S)$。

对 (7) 逐项乘根，精确有
$$
T(q^{17})\prod_{r=0}^{16}T(\zeta_{17}^rq^{1/17})=T(q)^{18}.
$$
原因是对 $17\nmid m$，
$\prod_r(1-\zeta_{17}^{rm}q^{m/17})=1-q^m$，
对 $17\mid m$ 则为 $(1-q^{m/17})^{17}$；
分母的9只置换这些根。故
$$
\boxed{\Phi_{17}(S,0)=S^{18}.}
\tag{13}
$$
此外每个非常数初等对称系数的极阶至多17：
选一个 $q^{-17}$ 根和至多16个 $q^{-1/17}$ 根后取整数阶。
因此
$$
\Phi_{17}(S,V)=V^{18}+\sum_{i=1}^{17}A_i(S)V^i+S^{18},
\quad A_i\in\mathbf Z[S],\quad\deg A_i\le17.
\tag{14}
$$
其中 $A_{17}$ 的首项为 $-S^{17}$。

原 $C$ 可在小 tower 中处理：
$$
\Phi_{17}(S,U)=0,\qquad
B(S,U,V)=
\frac{\Phi_{17}(U,V)-\Phi_{17}(U,S)}{V-S}=0.
\tag{15}
$$
第一步 degree18，第二步 degree17。
一般17同源链的唯一回溯边是对偶 isogeny，此时 $V=S$；
除去它后，复合的核为 cyclic $17^2$，反之亦然。
所以 (15) 的非回溯函数域恰为 (10)，总次数306。
几何连通性也由 $\Gamma_0(2601)$ 的上述单一群商得到。

使用 (15) 时必须取该函数域的光滑正规化。
在特殊 cusp 或分歧点处，两分支可相交；
(15) 不是许可删去这些点、重数或闭点迹的约定。

### 3.1 可直接公开执行的精确生成法

本节把 (12) 给成有限整数运算，避免使用经典 level2601 的庞大
$j$-模多项式。

写
$$
A(q)=qT(q)=\sum_{n\ge0}a_nq^n,\qquad a_0=1.
$$
由 (7) 的对数导数，
$$
na_n=\sum_{r=1}^n d_r a_{n-r},\qquad
d_r=-3\sigma_1(r)+27\,1_{9\mid r}\sigma_1(r/9).
\tag{16}
$$
所有 $a_n$ 都是整数；生成时保留并核对整除 $n$。

Faber 多项式 $F_m(X)$ 由
$$
-\log\bigl(A(q)-Xq\bigr)
=\sum_{m\ge1}F_m(X)\frac{q^m}{m}
\tag{17}
$$
定义。若 $b_1=a_1-X$、$b_r=a_r\ (r\ge2)$，则
$$
F_m=-mb_m-\sum_{i=1}^{m-1}F_i b_{m-i}.
\tag{18}
$$
故 $F_m\in\mathbf Z[X]$、首项 $X^m$，且
$F_m(T(q))=q^{-m}+O(q)$，常数项为0。
此 Faber 性质可直接从两个形式变量证明：把
$u(T(u)-T(q))$ 分解为 $(1-u/q)(1-uqB(u,q))$，
其中 $B(u,q)\in\mathbf Z[[u,q]]$，再取负对数。
第一因子的 $u^m$ 系数是 $q^{-m}/m$，第二因子的每项都含正次 $q$，
恰给上述断言。

对 $1\le k\le18$，令
$$
T(q)^k=\sum_{n\ge-k}c_{k,n}q^n.
$$
(12) 的第 $k$ 次幂和准确为
$$
T(q^{17})^k+17\sum_n c_{k,17n}q^n.
$$
其非正次项唯一确定对应的多项式，故这个幂和是
$$
\boxed{
P_k(X)=
\sum_{n=-k}^{-1}c_{k,n}F_{-17n}(X)
+17\!\!\sum_{\substack{-k\le n<0\\17\mid n}}
 c_{k,n}F_{-n/17}(X)+18c_{k,0}.
}
\tag{19}
$$
只须 $F_1,\ldots,F_{306}$，以及 $A^k$ 的前 $k+1$ 项。
最后 Newton 恒等式
$$
E_0=1,\qquad
mE_m=\sum_{k=1}^m(-1)^{k-1}E_{m-k}P_k
\tag{20}
$$
给
$$
\Phi_{17}(X,Y)=\sum_{m=0}^{18}(-1)^mE_m(X)Y^{18-m}.
$$
(12)–(20) 证明该程序构造的是原 Hecke 方程；
(13)、(14)、对称性和所有整除可在公开运行中逐项核验。
输出只需方程哈希及小摘要；全部系数由同一脚本重算，不存数据表。

## 4. 原 Hom 的 541 项严格认证门

原曲线的群指数和 cusp 数为
$$
\mu=2601(1+1/3)(1+1/17)=3672,\qquad
c_{\rm cusp}=(3+1)(17+1)=72.
$$
3排除椭圆阶2固定点，$9\mid2601$ 排除阶3固定点。因此
$$
\boxed{g(C)=1+\frac{3672}{12}-\frac{72}{2}=271,\qquad
\deg K_C=540.}
\tag{21}
$$

固定 R862 的某一规范准同态及正整数 $n$。
其目标可以是原 $E_0$，或 (3) 的 $C_v$。
相应的指定全纯微分记为 $\xi_n$；例如在 (3) 上
$$
\xi_n=nH_i(q)\frac{dq}{q}.
\tag{22}
$$
设候选 $x,y\in L(C)$ 在完整函数域中严格满足
$$
y^2+vy=x^3,
\tag{23}
$$
且不恒定，$\infty$ 映到 (3) 的原点 $O$。
则 (23) 自动给从光滑完备曲线 $C$ 到 $C_v$ 的真实态射 $f$。
特别地 $f^*\omega_v$ 是全纯微分。

如果
$$
\boxed{
[q^m]\left(q\,\frac{dx/dq}{2y+v}
                  -nH_i(q)\right)=0
\quad(1\le m\le541),
}
\tag{24}
$$
则 $f^*\omega_v-\xi_n$ 在 $\infty$ 的零阶至少541。
非零全纯微分的零除子次数仅540，故差严格为0。
基点已固定，特征零 Abel-Jacobi/Hom 的微分单射再给
$$
\boxed{f=n\Xi_i}
\tag{25}
$$
（含原 $J_0(2601)\to A$ 和 Abel 映射）。

(24) 无需预先知道 $f$ 的映射次数。
它也不表示只要541项形式近似就有态射；
**完整函数域等式 (23) 和原点条件是认证的前提。**
对原 $E_0$ 使用 $y^2=x^3+1$、$dx/(2y)$，证明完全相同。

## 5. 明确极界下的有理重建与终止

令 $\mathcal V_d$ 为 $S,V$ 中 total degree 至多 $d$ 的多项式
在原函数域中的像。由 (11)，每个非零 $P\in\mathcal V_d$ 满足
$$
(P)_\infty\le dD,\qquad \operatorname{ord}_\infty P\ge-289d.
\tag{26}
$$
函数域中的零多项式关系须先按 (15) 消掉，不能让其伪装成候选分母。

设某个真实函数 $x$ 有表示 $P_0/Q_0$，
$P_0,Q_0\in\mathcal V_d$、$Q_0\ne0$。
若另一候选 $P,Q\in\mathcal V_d$、$Q\ne0$ 满足
$$
P-xQ=O(q^M),
$$
则
$$
PQ_0-P_0Q=Q_0(P-xQ)
$$
在 $\infty$ 的阶至少 $M-289d$，而其极除子次数至多
$2d\deg D=1224d$。因此
$$
\boxed{M=1513d+1\quad\Longrightarrow\quad P/Q=x.}
\tag{27}
$$
同样的界适用于 $y$，不需要预先给它的极点位置。

这给出一个确定性、保证终止的重建程序：

1. 对整数对 $(n,d)$ 按有限对角顺序枚举；$n,d\ge1$。
2. 从原完整 (22) 求形式参数与 (3) 的两个 Laurent germ。
   这是特征零有限计算，保全部积分分母。
3. 对两条 germ 分别解
   $P-x_{\rm form}Q=O(q^{1513d+1})$ 的有限线性方程，
   其中 $P,Q\in\mathcal V_d$、$Q$ 在函数域非零。
   Laurent 截断保留所有负次，并按乘法所需精度计算输入。
4. 把候选代入原函数域，严格检查 (23)、$\infty\mapsto O$
   和 (24)。任何一步不合格即继续枚举。
5. 三个 $i$ 可以同时寻找同一 $n$；或者分别成功后取清分母的公倍数。

R862 的准同态存在性及 (6) 证明存在某个 $n$ 将三条 $\Xi_i$ 清为真实同态；
(10) 使它们的坐标总能用某个有限 $d$ 表示。
达到该 $(n,d)$ 时，(27) 保证每个非零分母候选都是真坐标，
而 (23)、(24) 必通过。因此算法终止。

这里未给最小 $n$ 或运行复杂度的有效小界。
一旦获得一个认证的 $n$，它已是原 Hom 的**实际可用**
清分母整数，无须先证明它最小。

还可从成功候选读出次数上界。
若 $y=P/Q$、$P,Q\in\mathcal V_d$，则
$\deg(y)_\infty\le1224d$。
(3) 上 $Y$ 的极阶为3，故
$$
\boxed{\deg f\le408d.}
\tag{28}
$$
这是一份认证后的真实 degree 上界；
不是把 Fourier 精度541当作映射次数。

## 6. 541 项的完整原 CM 输入可以全在三次域计算

本节给出第4节需要的原系数，避免一个未定 period 或任意新形式表。

在 $\mathbf F_{289}^{\times}$ 中使用固定
$\alpha=-1+2\omega$。
R862 的 $\alpha^{48}=-\omega$、$\alpha^{96}=\omega^2$ 表明其阶为288。
记
$$
r(u)=\log_\alpha(u\bmod17)\pmod9,\qquad
\zeta=b/\alpha,\quad \zeta^3=\omega^2.
$$
对任意素于 $17\delta$ 的 $u=A+B\omega$，设
$\epsilon_\delta(u)=1$ 或 $-1$，对应 $A+B\equiv1$ 或 $-1\bmod3$。
原 primitive Hecke 角色的完整主理想公式简化为
$$
\boxed{\beta_{10}((u))=\epsilon_\delta(u)\,u\,\zeta^{r(u)}.}
\tag{29}
$$
在素于2处，由 R862 的 $\psi_0\eta^{-2}$ 逐项相消得到；
因右侧已在2处有定义，它也给正确的 primitive 扩充。
特别地 $r(2)=0\bmod9$，所以 $\beta_{10}((2))=-2$。
乘 $u$ 以任意 $\mu_6$ 单位时，右侧不变，故是真理想函数。

$K$ 的类数1，故对每个 $m\le541$ 可以枚举
$$
A^2-AB+B^2=m,
$$
取各 $\mu_6$ 轨道一次，删去且仅删去 $17\delta$ 的倍数。
由 (29) 求和得到
$$
[q^m]F_0=f_{m,0}+f_{m,1}b+f_{m,2}b^2,\qquad f_{m,i}\in K.
\tag{30}
$$
不需素数扫描，也不需研究素数 $p$；
这是固定原来源的有限系数运算。

保 R862 的
$$
u_1=\tau^2\ell,\qquad u_2=c/\ell .
$$
若需要完全从 R864 的小模型恢复 $\tau$，使用
$$
\tau(v)=\alpha^3v/\ell^3,
\tag{31}
$$
而不按任意 $a\mapsto\omega a$ 的选择改 Artin 方向。
由 $H_i=\frac13\sum_j b_j^iG_jF_j$ 和 $b^3=c$，
三个完整原系数准确是
$$
\boxed{
\begin{aligned}
[q^m]H_0&=f_{m,0}+u_1f_{m,1}+u_2f_{m,2},\\
[q^m]H_1&=u_1f_{m,0}+u_2f_{m,1}+cf_{m,2},\\
[q^m]H_2&=u_2f_{m,0}+cf_{m,1}+cu_1f_{m,2}.
\end{aligned}}
\tag{32}
$$
证明只用 $\frac13\operatorname{Tr}_{K(b)/K}(b^r)$
在 $3\nmid r$ 时为0、在 $r=3s$ 时为 $c^s$。
所有输出在 $L$，第一项为 $(1,u_1,u_2)$。
特别地第4项是 $-2(1,u_1,u_2)$；
这保留了原二处项，而不是用 depleted form 替换。

公开 producer 可以直接输出 (14)、(32) 的规范序列哈希及少量
已显示的检验值。完整可重算序列不入仓库或 Release。
本篇不宣称这些新输入已经执行；数学公式不依赖其数值运行。

## 7. 原第一因子也有同样的有限证书

若需要重建原 $E_{17}$ 第一因子的实际映射，
完全相同的方法可在 $X_0(10404)$ 使用。
这是原 R831 共同源，不是新的曲线或新循环。

对 $N=10404=4\cdot9\cdot17^2$，
$$
\mu=22032,\quad c_{\rm cusp}=216,\quad e_2=e_3=0,\quad g=1729.
$$
所以 exact 椭圆方程和原基点成立后，
**前3457项**指定全纯微分便认证原第一 Hom。
使用 $T(z),T(1156z)$ 时，两函数次数均1836，总极除子次数3672，
$\infty$ 最大极阶1156；故 (27) 的相应界是
$$
\boxed{M=8500d+1,\qquad \deg f\le2448d.}
\tag{33}
$$
原 $E_{17}$ 的固定微分、到 $E_0$ 的 sextic 尺度及 R839 的系数
均须乘入该认证。它并未由 R862 的三次 packet 自动取代。

## 8. 认证后的有限域 shadow

一旦成功得到函数域坐标，原 R859 的交点读取保持为
$$
\operatorname{Alb}(b\circ q_2)_*
   (a\circ q_0-\varphi_r\circ F)^*[O].
\tag{34}
$$
使用同一源曲线的光滑正规化和同一原闭点迹；
清出的 $n$ 并入既有整数 $D$。
先通过 (23)、(24) 认证特征零原映射，再选择其好整模型归约。
不能直接把含 $1/m$ 的形式积分逐项约模来定义 (34)。

本篇没有给一个非零 (34)，没有给 canonical 比例，也没有从
有限系数认证推出跨 $p$ 的非零。
新的内容是：原 Hom 不再只能由未展开 Jacobian 对应命名；
有同源小函数域、确定的原系数、明确的有限认证界和保证终止的
坐标重建方法。最小清分母与实际成功坐标是下一步可计算目标。

## 9. 原文与来源

- G. Ligozat, *Courbes modulaires de genre 1*, Mémoires de la SMF **43**
  (1975), §1.3 的 genus 公式、§3.2 Proposition3.2.1 与
  Proposition3.2.8 的 eta 变换及 cusp 阶。
  <https://www.numdam.org/article/MSMF_1975__43__5_0.pdf>。
  本文的 level9、2601、10404 值均在上文逐项计算。
- González–Lario 的原 CM Hom 定理及规范，沿
  [R862](R862-original-seventeen-torsion-product-and-complete-cubic-hom-matrix.md)
  的完整引用及其实际基；不使用 Gross 曲线的专门 Manin 单位结论。
- [R864](R864-original-seventeen-torsion-exact-field-and-cocycle.md)：
  原17挠点乘积的公开有限证书、(2) 小三次模型、原 $\ell$ 和 $\tau$。
- [R831](R831-original-dyadic-old-space-and-unique-endpoint-class.md)、
  [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)：
  原共同曲线、两退化映射、固定原 Hom 和全部 Artin 系数。
- [R859](R859-original-supersingular-shadow-and-integral-aj-detection.md)：
  原整 shadow、实际交积和商模型的闭点迹规范。

全文新数学为符号推导；新的整数 producer 仅提交公开 Actions，
未在本地或 V8 执行数学计算。
