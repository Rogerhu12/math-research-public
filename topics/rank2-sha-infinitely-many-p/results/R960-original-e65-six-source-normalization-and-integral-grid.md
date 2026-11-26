# R960 — 原 E65 第六来源的角帽、完整规范化与有成本整返回

日期：2026-11-26。**状态：同一次公开全源消费已通过；原第六来源的完整角 profile、六源规范化、原参数有限整性、primitive 来源、固定导子及全部整格成本均已证明。主目标仍待同格强迫与全局非零。**

**更正：原第11节的目标自同构、整个原来源核同一和125前缀成本因遗漏 $a_p$ 的一个 $p$ 已撤销；见当前第11节。第1–10节保留。**
R959 的全66列 CM 与真实六低 jet 已通过；本篇不重做该结论。
实际角多项式次数为64，四个基点均单重；它给新的斜率 $4/13$。
原草稿的 $\gcd(68g,18)=2$ 门在真实来源上不成立，实际值为6；
第5节改以四点完整纤维论证排除三次与六次中间域，没有替换原来源或重跑参数。
所用有限输入来自同一次完整 CM 的内存系数，不是另存系数表。

记原六来源的权为
$17,36,68,33,89,195$，依次为 $S,T,U,V_{66},W,Z$。
$\vartheta$ 是权一变量，实际代入
$\vartheta=\Theta=x\sigma^2,\ t=-x^{-3}$。
旧五源的完整规范化 $B^+$、导子 $c_+$ 与整模型 $R_+$ 全按 R947；
特别不把 $V_{66}$ 漏掉。

## 1. 新原来源不在旧格；两个已经付清的全源返回

R959 的同一次公开全源给 $c_{64}=1$、$c_{65}=0$、
所有 $c_j\in\mathbf Z[1/175]$，并定义
$$
Z=\vartheta^{195}f_Z(t),\qquad
f_Z(t)=\sum_{j=0}^{64}c_j(-t)^{65-j}.
\tag{1}
$$
只按该式重生系数，不将65项输出存成新输入。
因此
$$
\operatorname{ord}_{t=0}f_Z=1,\qquad\deg f_Z\le65 .
\tag{2}
$$
置 $a=t(t-1)(7+4t+16t^2)$、$d=1+8t$；
原 $S=\vartheta^{17}ad/7$。

R473 的旧 $B_{195}$ 与 R947 的新 $B^+_{195}$ 都要求含 $a^3$，
所以
$$
Z\notin B_{195},\qquad Z\notin B^+_{195}.
\tag{3}
$$
这已由原点的真实重数严格排除，无须先猜其余三个角点。

同时，完整多项式乘法和两套原角帽给
$$
\boxed{S^4Z\in B_{263},\qquad S^3Z\in B^+_{246}.}
\tag{4}
$$
第一式含 $a^4$，角次数至多85，而
$\lceil263/68\rceil=4,\ \lfloor11\cdot263/34\rfloor=85$。
第二式含 $a^3$，角次数至多80，而
$\lceil246/89\rceil=3,\ \lfloor29\cdot246/89\rfloor=80$。
这两个整返回对175、91可逆的同一个环成立；不是点值检验。
若再用已付 $c_+$，有
$c_+S^3Z\in A^{(5)}_{29129}$。
所有乘子都只用于原格表示，绝不新增它们的中央零。

本次全除法还实际给出更小且准确的返回：
$$
\boxed{S^3Z\in B_{246},\qquad S^2Z\in B^+_{229}.}
\tag{4a}
$$
前者含 $a^4$、角次数79，后者含 $a^3$、角次数74；
相应旧帽分别恰为79、74。较小的 $S$ 次数因所需 $a$ 重数不足而失败。
因此 $c_+S^2Z\in A^{(5)}_{29112}$，仍支付同一旧导子。

## 2. 准确的有理除子与同一整函数域

取三个有理不可约因子
$$
q_0=t,\qquad q_1=t-1,\qquad q_2=7+4t+16t^2,
\quad (\deg q_0,\deg q_1,\deg q_2)=(1,1,2).
$$
$q_2$ 的判别式为 $-432$，两个几何根一起保留。
让同次实际全多项式除法确定
$$
e_i=\operatorname{ord}_{q_i}f_Z,\qquad
z=\deg f_Z,\qquad e_0=1.
\tag{5}
$$
旧五源的最小有限比值只在 $a=0$ 的四点非零，且都是 $1/89$；
旧无穷远最大比值是 $29/89$。
因此完整六源的准确有理除子必须是
$$
D_6=\beta[\infty]-\sum_{i=0}^2\alpha_i\operatorname{div}_0(q_i),
\quad
\beta=\max\left(\frac{29}{89},\frac z{195}\right),\quad
\alpha_i=\min\left(\frac1{89},\frac{e_i}{195}\right).
\tag{6}
$$
没有其他有限基点，因为旧 $S,U$ 在 $a$ 以外已经无共同零点。
对应全分次格为
$$
Q_m(t)=\prod_{i=0}^2 q_i(t)^{\lceil m\alpha_i\rceil},\quad
b_m=\lfloor m\beta\rfloor-\sum_i(\deg q_i)\lceil m\alpha_i\rceil,
$$
$$
\boxed{B^{(6)}_m=\vartheta^m Q_mR[t]_{\le b_m},\qquad
B^{(6)}=\bigoplus_{m\ge0}B^{(6)}_m.}
\tag{7}
$$
不能把 $\lceil2m/195\rceil$ 免费改成 $2\lceil m/195\rceil$；
全部剩余权和全部角点都在 (7) 中。

记 $\lambda_6=\deg D_6$。由 (2)，$0$ 点的系数严格下降，
其余有限点不增且无穷远系数不减，所以
$$
\lambda_6>\frac{25}{89}.
\tag{8}
$$
这是同一二变量函数域中真实 Hilbert slope 的改善；
尚未由 (8) 宣称新的深核或无穷素数中央非零。

R473/R947 已证明旧环的全函数域为 $\mathbf Q(t,\vartheta)$；
所有新源都仍在这个域，旧源包含关系给
$$
\operatorname{Frac}A^{(6)}=\mathbf Q(t,\vartheta),\qquad
A^{(6)}=R[S,T,U,V_{66},W,Z].
\tag{9}
$$
$B^{(6)}$ 是 $R[t,\vartheta]$ 与各正确 Gauss 赋值环的交，
因此正规；$R[t,\vartheta]$ 保留所有竖直整性。
下面付真正有限整性，不能只凭赋值交便宣称 (7) 为规范化。

## 3. 实际 profile、原参数及完整整模型

将 $f_Z=Q\,G$，其中
$$
Q=\prod_iq_i^{e_i},\quad E=\deg Q=\sum_i(\deg q_i)e_i,\quad
g=\deg G=z-E,\qquad \gcd(a,G)=1.
\tag{10}
$$
用旧完整 $U=\vartheta^{68}aH/91$，作同环参数替换
$$
U_c=U+cS^4=\vartheta^{68}aH_c,\qquad
H_c=H/91+c\,a^3d^4/7^4 .
\tag{11}
$$
它的次数恒为18，$\gcd(ad,H_c)=1$。
在 $G$ 的每个根处，至多一个 $c$ 导致 $H_c$ 为零；在 $ad=0$
处则没有坏 $c$。所以 $0,\ldots,g$ 中必有
$$
\gcd(H_c,G)=1 .
\tag{12}
$$
实际 reader 取其中首个成功的整数，并完整回乘 Bézout 恒等式。

同次 reader 的实际结果为
$$
\boxed{z=64,\qquad(e_0,e_1,e_2)=(1,1,1),\qquad
Q=a,\quad g=60,\quad c=0.}
\tag{13}
$$
尤其 $U_c=U$、$H_c=H/91$ 本身已经与完整 $G=f_Z/a$ 互素；
reader 在 $c=0$ 的首项试验即给全多项式 Bézout 返回。
原先候选的 $\gcd(68g,18)=2$ 简化门没有通过：实际是6。
第5节直接付这个真实值的 primitive 证明，未更换来源或删其角点。

由 (6)，完整六源除子和斜率准确为
$$
\boxed{D_6=\frac{64}{195}[\infty]-\frac1{195}\operatorname{div}_0(a),
\qquad \lambda_6=\frac4{13},\qquad
\lambda_6-\frac{25}{89}=\frac{31}{1157}.}
\tag{14}
$$
因此 (7) 现在是
$B^{(6)}_m=\vartheta^m a^{\lceil m/195\rceil}
R[t]_{\le\lfloor64m/195\rfloor-4\lceil m/195\rceil}$；
每个旧来源和第六来源的全角多项式均已逐一回到这个完整格。
定义固定非零有理数
$$
\Delta_Z=
(68g)\operatorname{lc}(G)
\operatorname{Res}(a,G)
\operatorname{Res}(H_c,G)
\operatorname{Res}(ad,H_c),\qquad R=R_+[1/\Delta_Z].
\tag{15}
$$
以上 resultant 由同次全源和全部 Bézout 返回定义，仅存源及哈希；
不用把大整数展开入库。原系数分母175已在 $R_+$ 中可逆。
(15) 保 (5)、(10)–(12) 的实际次数、所有重数和互素性在每个
允许剩余域都不变。$2,3,5,7,13,17$ 已由旧整模型排除；
$68g$ 的素因子不超过65。

## 4. 真正无基点 pencil 与全部剩余权

置
$$
L=68\cdot195=13260,\qquad
M=68g=4080,\qquad \rho=\vartheta^LQ^{68}.
$$
则完整 Veronese 为
$$
(B^{(6)})^{(L)}
=\bigoplus_{n\ge0}\rho^nR[t]_{\le Mn}.
\tag{16}
$$
同一原权的两个参数为
$$
U_c^{195}=\rho\,
 \left(\frac{a^{195}}{Q^{68}}H_c^{195}\right),\qquad
Z^{68}=\rho\,G^{68}.
\tag{17}
$$
$e_i\le2$ 保第一个括号为真正多项式。
两式角次数分别是 $4290-68E$ 和 $68z-68E=M$；
由于 $z\ge64$，前者严格较低。
它们没有有限共同零点，由 (12)、$\gcd(a,G)=1$ 得到；
无穷远则由 $G^{68}$ 的单位首项覆盖。
因此 (17) 在整个 $\mathbf P^1_R$ 上是无基点 pencil。

对 $m=Ln+r,\ 0\le r<L$，定义
$$
Q_r=\prod_iq_i^{\lceil re_i/195\rceil},\qquad
q_r=\lfloor zr/195\rfloor-\sum_i(\deg q_i)\lceil re_i/195\rceil .
$$
完整剩余格为
$$
B^{(6)}_{Ln+r}
=\vartheta^rQ_r\,\rho^nR[t]_{\le Mn+q_r}.
\tag{18}
$$
注意 $q_r>r\lambda_6-5\ge-5$，故整数 $q_r\ge-4$。
(17) 的 Koszul 序列给
$$
0\longrightarrow\mathcal O(Mn+q_r-2M)
\longrightarrow\mathcal O(Mn+q_r-M)^{\oplus2}
\longrightarrow\mathcal O(Mn+q_r)\longrightarrow0 .
\tag{19}
$$
$n\ge3$ 时左项 $H^1=0$，所以两个原参数的乘法对完整整格满射。
保留 $0\le r<L,\ n\le2$ 的非零空间，便得到权至多
$$
M_{\mathrm{gen}}=3L-1=39779
\tag{20}
$$
的显示有限生成集合。若使用 reader 的全部13260个真实 $q_r$，
$q_r\ge-1$ 的剩余权只需 $n\le1$，可得到更小的已付界；
(20) 已足够且不删任何剩余权。
本次 reader 遍历全部13260个剩余权，准确给出只有 $r=1,\ldots,9$
需要 $n=2$；其余只需 $n\le1$，故实际充分生成权界为26529。

于是 $B^{(6)}$ 在 $R[U_c^{195},Z^{68}]$、
$R[U_c,Z]$ 和 $A^{(6)}$ 上都有限。结合正规性及 (9)，
(7) 是完整六源环的规范化，而不是仅某个 Veronese 的规范化。

## 5. 两个真实角函数、primitive 的 S 与精确扩张次数

令 $k$ 为 $\mathbf Q$ 或任一 $R$ 的剩余域，置
$$
\mathscr A=\frac{U_c^{195}}{Z^{68}}
=\frac{a^{195}H_c^{195}}{f_Z^{68}},\qquad
\mathscr C=\frac{S^4}{U_c}
=\frac{a^3d^4}{7^4H_c}.
\tag{21}
$$
(17) 付出准确约分，所以
$\deg\mathscr A=M$。第二式的完整分子、分母互素，次数为16和18，
故 $\deg\mathscr C=18$。
先在 $k$ 的代数闭包上证明，最后下降。若
$e=[k(t):k(\mathscr A,\mathscr C)]$，
塔式次数给 $e\mid\gcd(4080,18)=6$。特征不为2或3，故该扩张可分。
由 Lüroth，令其对应中间曲线参数为 $u$，写完整有限映射
$\pi:\mathbf P^1_t\to\mathbf P^1_u$，次数为 $e$。

$\mathscr C$ 的零除子恰为
$$
3\operatorname{div}_0(a)+4[-1/8]+2[\infty].
\tag{22}
$$
在四个 $a$ 根中的任一点 $P$，完整 (21) 给
$(\operatorname{ord}_P\mathscr A,\operatorname{ord}_P\mathscr C)=(127,3)$。
$\pi$ 的该点分歧指数同时整除127和3，故等于1。
因此在 $\pi(P)$，下游两函数的阶也恰为 $(127,3)$。
其整个纤维只能含 $a$ 的四根：若有别的点 $Q$，其 $\mathscr C$ 阶
必须是某个正整数乘3；(22) 的另外两种阶4和2均不可能。
特别 $\infty$ 也是两函数的共同零点，但其阶对为 $(62,2)$，
比值 $31$ 与 $127/3$ 不同，不能与 $a$ 根处在同一纤维。
$d=0$ 点的 $\mathscr A$ 为单位或有极，$H_c=0$ 点则为 $\mathscr C$ 的极；
它们也不在这些纤维中。
纤维内每个 $a$ 根又都不分歧，所以整个纤维有恰 $e$ 个不同 $a$ 根。
这些纤维分割全部四根，遂 $e\mid4$。结合 $e\mid6$ 得 $e\mid2$。
这一步使用整个纤维次数，不只使用一个点的不分歧性。

假设 $e=2$。因 $2$ 可逆，该扩张有非平凡 deck involution $\tau$，
并且 $\tau$ 固定 $\mathscr C$。
(22) 的四个三重点、唯一四重点、唯一二重点均准确，由 (15) 保持；
所以 $\tau$ 必须固定 $\infty$ 和 $-1/8$，并置换 $a$ 的四根。
特征不为二的非平凡仿射 involution 只能是
$\tau(t)=-t-1/4$。
但 $\tau(0)=-1/4$ 而
$a(-1/4)=35/16\in R^\times$，矛盾。因此
$$
k(\mathscr A,\mathscr C)=k(t).
\tag{23}
$$
这不需要以两个角函数的有限样本推断 birational。
两个映射的约分次数及零除子在 (15) 的所有剩余域保持不变；
同一论证在代数闭包给扩张次数一，因此也下降给原 $k$。

整数恒等式 $195\cdot15-68\cdot43=1$ 给
$$
\eta=Z^{15}/U_c^{43}=\vartheta\,r(t),\quad r(t)\ne0 .
$$
指数矩阵
$\left(\begin{smallmatrix}195&-68\\-43&15\end{smallmatrix}\right)$
行列式为一，所以
$$
k(U_c,Z)=k(\mathscr A,\eta),\qquad
k(S,U_c,Z)=k(t,\eta)=k(t,\vartheta).
\tag{24}
$$
由 $\eta$ 在 $k(t)$ 上超越和 $\deg\mathscr A=M$，
$$
[k(t,\vartheta):k(U_c,Z)]=M.
\tag{25}
$$
特别 $S$ 生成这个全部扩张；不是仅生成一个 proper 子域。
整个证明对 (15) 的每个允许剩余域都成立。

## 6. 实际固定导子、整返回与 p-饱和

记 $P=R[U_c,Z]$ 和 $A_0=R[S,U_c,Z]\subset A^{(6)}$。
第4节付 $S$ 在正规多项式环 $P$ 上整，第5节付其最小式次数，
所以唯一的 monic 最小式为
$$
\Psi_6(U_c,Z;X)\in P[X],\quad
\deg_X\Psi_6=M,\quad \Psi_6(U_c,Z;S)=0 .
\tag{26}
$$
系数在 $P$：它们在 $P$ 上整且属于其分式域。
原权伸缩和 monic 唯一性给
$\operatorname{wt}\Psi_6=17M$。
于是
$$
A_0\simeq R[u,z,X]/(\Psi_6),\qquad
c_6=(\partial_X\Psi_6)(U_c,Z;S),\qquad
C_6:=\operatorname{wt}c_6=17(M-1)=69343.
\tag{27}
$$
对 $X$ 求导时固定实际参数 $U_c,Z$；
代回 $U+cS^4$ 后不能误取全导数。

这是一条可重生的确定最小式，而非未付“足够大关系”：
可由 (18)–(20) 的有限模和 $S$ 的完整乘法最小式恢复；
也可消去 (21) 的两式后取唯一 monic 最小因子。
只需源、参数和哈希，无须把该大多项式存库。

与 R947 的全幂基迹配对相同，令 $\ell$ 为
$1,S,\ldots,S^{M-1}$ 基上最后坐标。配对 $\ell(xy)$ 整且完美，
且 Lagrange 插值给 $\operatorname{Tr}(x)=\ell(c_6x)$。
对任意 $b\in B^{(6)}$、$a_0\in A_0$，二者在 $P$ 上整，
故 $\operatorname{Tr}(ba_0)\in P$。完美配对于是给
$$
\boxed{c_6B^{(6)}_m\subset(A_0)_{m+C_6}
\subset A^{(6)}_{m+C_6}\quad(m\ge0).}
\tag{28}
$$
没有随权增长的分母素数。

每个允许剩余域仍满足 (25)，故 monic 约化仍最小，
$A_0/pA_0\hookrightarrow B^{(6)}/pB^{(6)}$。
(15) 保 $M$ 为单位，导数的最高项 $M X^{M-1}$ 非零且次数小于
最小式，故 $\bar c_6\ne0$ 于该整环。
若 $c_6b=pa$、$a\in A^{(6)}$，先模 $p$ 得 $b=pb_1$，
再约去 $p$ 得 $a=c_6b_1$。因此 (28) 的导子像在原来源环中
$p$-饱和。没有据此宣称任何截断 jet 的像也饱和。

## 7. 全次数、系数增长、真实全纯来源和 Hilbert 主项

(28) 的原来源表达只需 $S,U,Z$，因为
$U_c=U+cS^4$ 是保权同环替换。故
$$
\deg_{S,T,U,V_{66},W,Z}\operatorname{return}(c_6b)
\le\left\lfloor\frac{m+C_6}{17}\right\rfloor .
\tag{29}
$$
用 (18)–(20) 的有限生成集合及 $B^{(6)}_L$ 的完整单项式基，
预选固定有限乘法表及每个 $c_6g$ 的整表达。
任意 (7) 的显示基元素可分成固定剩余权基与 $O(m)$ 个
$B^{(6)}_L$ 基元素的乘积；逐次查表给
$$
\|\operatorname{return}(c_6b)\|_1
\le C^{m+1}\|b\|_{\mathrm{basis}}
\tag{30}
$$
的固定指数成本。同环替换的二项式系数也吸收入 $C^{m+1}$；
没有每个 $m$ 重新求不断扩大的逆矩阵。

$z\le65$ 保 $\beta=z/195\le1/3$。
把 (7) 展开为 $\vartheta^m t^j$ 后，所有 $j\le\lfloor m/3\rfloor$，
所以实际原函数
$$
\Theta^m t^j=(-1)^j\sigma^{6j}\Theta^{m-3j}
\tag{31}
$$
保非负幂，是真正全纯来源，没有反卷积。
原点阶至少 $6\lceil m/195\rceil$。
原 sigma/Theta 增长给与 R473/R947 相同形式
$$
|b(w)|\le C_1^{m+1}\|b\|_{\mathrm{basis}}
\exp(C_2m|w|^{1/3}),\qquad w=\zeta^6 .
\tag{32}
$$
新权帽、系数成本和固定导子偏移都保留在原全局预算中。

从 (7) 得
$$
\operatorname{rank}_R B^{(6)}_m
=\max\{0,b_m+1\}
=\lambda_6m+O(1).
$$
由 $A_0\subset A^{(6)}\subset B^{(6)}$ 与 (28)，有
$$
\dim_k A^{(6)}_m=\lambda_6m+O(1),\qquad
\sum_{j\le m}\dim_k A^{(6)}_j
=\frac{\lambda_6}{2}m^2+O(m).
\tag{33}
$$
$c_6=\Theta^{C_6}q_6(t)$ 非零，且 (7) 给实际固定 jet 平移范围
$$
\left\lceil\frac{C_6}{195}\right\rceil
\le\operatorname{ord}_{t=0}q_6
\le\left\lfloor\frac{zC_6}{195}\right\rfloor .
\tag{34}
$$
实际 (13)、(27) 使这个固定范围为 $356\le\operatorname{ord}_{t=0}q_6\le22758$。
若要在普通 Amice 坐标用其首项作单位三角搬运，
仍须支付该首项实际赋值或固定坏素数；原惰性 Gaussian、
阶乘和全部 carry 均没有由 (34) 删除。


### 7.1 全六源的原整数格、195 个剩余权和固定整数乘法

以下使用实际 (13) 的 $e_i=1,z=64,g=60$；没有扩大原来源角帽。置
$$
\Lambda^{(6)}_m=
 \vartheta^mQ_m\,\mathbf Z[t]_{\le b_m},\qquad
\Lambda^{(6)}=\bigoplus_{m\ge0}\Lambda^{(6)}_m .
\tag{35}
$$
每个 $q_i$ 都是 primitive 整多项式，故 $Q_m$ 也是 primitive。
Gauss 引理给
$$
\Lambda^{(6)}_m=B^{(6)}_m(\mathbf Q)\cap
 \vartheta^m\mathbf Z[t].
\tag{36}
$$
因而此整数格在 $\mathbf Z[t,\vartheta]$ 中饱和。
其模任意素数的显示基仍独立：公共非零因子 $\overline Q_m$
乘不同的 $t^j$，不会产生线性关系。
坏素数处可能改变次数或规范化描述，不能据此另宣称 (14) 在
那些素数仍有原 profile。

实际 (1) 的分母175和 primitive $Q$ 给
$175f_Z/Q\in\mathbf Z[t]$。
旧五来源的分母整除91；所以统一清分母
$\operatorname{lcm}(91,175)=2275$ 后，六个实际来源均在 (35)
的对应权空间。只支付一次固定缩放，不改变任何中央是否为零。

令
$$
\rho_6=\vartheta^{195}Q,\qquad
P_0=\mathbf Z[\rho_6,\rho_6t^g].
$$
对 $0\le r<195$ 保留第4节同一 $Q_r,q_r$，
$0\le i<g$，置
$$
h_{r,i}=\left\lceil\frac{i-q_r}{g}\right\rceil,\qquad
b_{r,i}=\vartheta^rQ_r\,\rho_6^{h_{r,i}}t^i.
\tag{37}
$$
$q_r\le rg/195<g$ 且 $q_r\ge-4$；
(13) 给 $g=60$，因此 $h_{r,i}\in\{0,1,2\}$。
只有 $1\le r\le9$ 可能需要 $h_{r,i}=2$，所以每个 $b_{r,i}$ 的原权至多399。

**完整自由模恒等式为**
$$
\boxed{\Lambda^{(6)}
=\bigoplus_{\substack{0\le r<195\\0\le i<g}}P_0\,b_{r,i}.}
\tag{38}
$$
其自由秩准确为 $195g=11700$。

证明必须保权。固定总权 $m=195n+r$，
$\Lambda_m^{(6)}$ 的基是
$\vartheta^rQ_r\rho_6^nt^j$，其中 $0\le j\le gn+q_r$。
唯一写 $j=gv+i$、$0\le i<g$，则该不等式等价于
$n-v\ge h_{r,i}$。于是准确有
$$
\vartheta^rQ_r\rho_6^nt^{gv+i}
=b_{r,i}\,\rho_6^{\,n-v-h_{r,i}}(\rho_6t^g)^v.
\tag{39}
$$
所有指数均非负。
独立性则在同一总权先约去共同
$\vartheta^mQ_rQ^n$，再比较不同 $t^{gv+i}$。
(39) 实际是两套整单项式基的置换，系数均为一；
不是一个带未知分母的有理坐标替换。

完整乘法也有很小的确定整数成本。
若 $r+s=195\delta+r'$、$\delta\in\{0,1\}$，则
$$
R_{r,s}(t)=
\frac{Q_rQ_s}{Q^\delta Q_{r'}}
=\prod_{\ell=0}^2q_\ell^{\epsilon_\ell},
\quad
\epsilon_\ell=
\left\lceil\frac{re_\ell}{195}\right\rceil+
\left\lceil\frac{se_\ell}{195}\right\rceil-
\left\lceil\frac{(r+s)e_\ell}{195}\right\rceil
\in\{0,1\}.
\tag{40}
$$
所以 $\deg R_{r,s}\le4$，
$\|R_{r,s}\|_1\le\|t\|_1\|t-1\|_1\|7+4t+16t^2\|_1=54$。
先算
$$
b_{r,i}b_{s,j}
=\vartheta^{r'}Q_{r'}
 \rho_6^{\,\delta+h_{r,i}+h_{s,j}}
 R_{r,s}(t)t^{i+j},
\tag{41}
$$
再逐项用 (39)。每个乘积至多有五项，
$P_0$ 系数是总次数至多五的单项式乘整数，
且整表的该行系数绝对值和至多54。
所有 carry 指数都由 (40) 的 ceiling 得到；这里没有只看
$r=0$ 或零角分量。

为了核 (41) 中逐项返回的合法性，注意
$Q_mQ_n/Q_{m+n}$ 的各指数均为0或1，且
$\lfloor m\beta\rfloor+\lfloor n\beta\rfloor
\le\lfloor(m+n)\beta\rfloor$。
所以乘积的每个角单项式都仍满足真实 (7) 的帽；
(39) 返回的两个 $P_0$ 指数自然非负。这同时证明 (35) 是整环格。

(38)–(41) 给同一个完整整数格的原坐标和乘法，
可直接定义全部有限评价映射的像、商范数及每个 $p$ 的预算。
$P_0$ 的两参数是规范化中的实际元素；它们若需回到原六来源，
仍按 (28) 支付 $c_6$ 与全部原权，不能免费认作原来源参数。
这些整数恒等式也不把中央泛函升级成乘法同态。

## 8. 唯一公开入口与实际角回执

reader 是
[original_e65_angular_profile.py](../scripts/original_e65_angular_profile.py)，
由既有完整 E65 producer 在同一次运行里调用。
它直接接当前全 CM 产生的65项及该同 job 旧 E89 产生的29项；
不重新调用 producer，不读旧输出表。
该次 job 还可消费 R961 的同一原 sigma-six 投影，
共用原 A7、A19、来源与全部 provenance。

有限 reader 对全部多项式整除、所有三有理因子（四几何点）、
最小 shear、完整 Bézout、两个原格返回及所有剩余权回乘/界逐项核验。
它只报告 profile、source/证书/resultant 哈希和必要小整数；
不以这个有限报告替代第4–7节的证明。
公开入口 source 为 `9144dc0062fd9423f8a9f94978643787b863eb36`，
[run45818310281](https://github.com/Rogerhu12/math-research-public/actions/runs/45818310281)、job `139903674795`，2026-11-26 12:23:50 UTC
实际完成，结论 `success`；原 CM、六低 jet、完整角与同 sigma-six
消费全 `PASS`，总数学耗时355.919856256秒，10个 AST 源、12项 manifest。
原 CM 全矩阵、核和来源哈希均与 R959 首次已登记运行逐项相同。

必要的小回执如下；完整输出不入库：

- $f_Z$ 角多项式 SHA-256：`94a188eb359893012e9c0a349811146d9ac0beb1243bb59cf351fbfa97063c87`。
- 全 Bézout 与来源证书 SHA-256：`cc83d968fbc173056c6fb0ea38bab2e8799e64b641bae68f756e95e4f38687fb`。
- $\operatorname{Res}(a,G)$ 哈希：`6cbdcf63ef6e730167e2563cf456364aec07fa5951cd0b4a7b771fe20bf84337`；
  $\operatorname{Res}(H_c,G)$ 哈希：`1a40ac45da7e825050f0580822640278b27da867f44aa480b8e7c4f58040b9e5`。
- $\operatorname{Res}(ad,H_c)$ 哈希：`03b7843372894bd05654106d69aa5aacc3a078243a5bcf86eb4b0be78a4f865e`；
  $\operatorname{lc}(G)$ 哈希：`53646a5d95785d66d6854a361f6a378074b2b5b9fbdc995ce08ad72adfdb8a5d`。
- reader 源 SHA-256：`54676c475e830d8ab33441aae0cb5f1557f86b5d87e799619d9e46f9d6b32b31`。
- 原 producer stdout（从实际 wrapper 逐字符截取原 result 对象，含末 newline）16550字节，SHA-256
  `a96cd6c06d334178bf61dc0e3eb0c6d962aede4bde6e461bfd6d6b24c5aba2bb`。
- 原报告的 source-manifest SHA-256：`c348470b3e911b7cd9c1af1e7fe103bdc175a18f0d52aca90be047d2d338752f`。
- 完整 job log 54187字节，SHA-256
  `3fb9db7ae82af87c4e7c97c6403fefcda61f4ec4a159d8ed35087ece3aabfff2`。

有限 reader 明确没有自行宣称函数域 primitive 或导子；
这些结论由第4–7节在实际 $z=64,g=60,M=4080$ 下完整证明。
同次 R961 的非零 sigma-six 投影另在该文消费，不把其混合切域删去。

依赖：R473 原全函数域；R947 五源完整规范化/导子及整返回；
R959 原 E65 完整算术来源、六低 jet 和通常 Selmer 桥。
本篇从不把来源环乘法解释成中央泛函的乘法性。


## 9. 真五中央必要值在同一六源整格上的完整六块运输

本节从 R943 的真实五轴必要系统接到本篇六源原格。
它不把五条或六条中央零当作来源环上的乘法恒等式，
也不由参数确定性宣称任何右核存在。
固定坏集合还包括 $c_6$ 在原点的首系数；写
$$
c_6=\Theta^{69343}q_6(t),\quad
r_c=\operatorname{ord}_{t=0}q_6,\quad
\ell_c=(-1)^{r_c}[t^{r_c}]q_6\ne0 .
\tag{42}
$$
第7节给 $356\le r_c\le22758$，故这是先于 $p,M$ 固定的有限代价。
以下 $p=6s-1$ 在所有固定坏集外，且
$$
1\le\ell,\qquad \ell+r_c<s .
\tag{43}
$$
目标物理长度 $L=5s+\ell$、$L+r_c$ 均小于 $6s=p+1$；
因整数性，$L+r_c\le p$。所有所用展开在 R614 原 addition 整窗内。

### 9.1 同一来源、整数格及实际范数

为分清完整规范化和原来源呈示，记
$$
\mathcal B_M=\bigoplus_{0\le m\le M}\Lambda_m^{(6)},\qquad
\mathcal A_N=\operatorname{im}\left\{
 \bigoplus_{\substack{e\in\mathbf Z_{\ge0}^6\\
 (17,36,68,33,89,195)\cdot e\le N}}\mathbf Z E_e
 \longrightarrow\mathbf Q[[w]],\ E_e\mapsto F^e\right\}.
\tag{44}
$$
这里 $F=(S,T,U,V_{66},W,Z)$ 仍是六个原质量零来源；
没有把 $\rho_6,\rho_6t^{60}$ 另当算术中央。
第7节的固定有限返回表给一个先于 $M$ 固定的整数 $D_{\rm ret}>0$，
令 $Q_M=D_{\rm ret}^{M+1}$，便有同一来源的整映射
$$
\iota_M:\mathcal B_M\longrightarrow\mathcal A_{M+69343},
\qquad P\longmapsto Q_Mc_6P .
\tag{45}
$$
它是单射；在所有好 $p$ 处是饱和单射。
证明逐字使用 (28) 的全整环饱和性，再保留实际分次与 $Q_M$ 的单位性；
并非从截断 jet 的秩推出来源饱和。

$\mathcal A_N$ 的实范数取 (44) 标准 Euclidean 范数的真正商范数，
有限位取同一整数像格的 gauge 范数。
$\mathcal B_M$ 则取 (35) 的同一显示整基。
(30) 的整返回使 (45) 的实算子范数至多 $\exp(O(M+1))$；
所有有限位是整映射，恢复 $Q_M$ 的代价仅在固定坏位，
合计 $(M+1)\log D_{\rm ret}$。
这正是 R957 §4–7 的实际商格论证在六个真实来源上的使用：
呈示核 primitive、真实 Taylor 前缀饱和，
全部普通测度先作原加法卷积再切单位域。
本节没有将某个随 $p$ 选择的有理补空间赋成新的整数标准格。

### 9.2 原六块环和全部物理行

置
$$
\Gamma_L^{(6)}=\mathcal O[w,\epsilon]/
 (w^s-p\epsilon,\epsilon^6,w^\ell\epsilon^5),
\quad
\Gamma_{L+r_c}^{(6)}=\mathcal O[w,\epsilon]/
 (w^s-p\epsilon,\epsilon^6,w^{\ell+r_c}\epsilon^5).
\tag{46}
$$
第一环在 $j=0,\ldots,4$ 的每块保 $w^i\epsilon^j,\ 0\le i<s$，
最后一块保 $0\le i<\ell$；第二环最后长度为 $\ell+r_c$。
这些是自由 $\mathcal O$ 基，不删除任何块内尾。

保持 R943 的同一个 $t(w)$、$a_p=p\kappa$、
$g_\circ$ 及五个实际高轴。
令
$$
h_\circ=(g_\circ/d)^{1/17},\quad
\eta_A=w^{s-5}K_A,\quad K_A=P_4+w^5H_A,\quad
h_A=h_\circ e^{\eta_A/17},
\quad \mathcal E=\frac1{17}\vartheta\partial_\vartheta.
\tag{47}
$$
$H_A$ 是原三角坐标 $u$ 确定的整个尾，不取任意替代。
对 $P=\sum_mP_m\in\mathcal B_M$ 定义
$$
\mathcal J_{6,A}(P)_j
=\left[\sum_{i=0}^j
 \frac{a_p^i}{i!}p^{j-i}\mathscr S^{j-i}
 (\mathcal E^iP)(t(w),h_A(w))\right]_{<m_j},
\quad
m_0=\cdots=m_4=s,\quad m_5=\ell .
\tag{48}
$$
$\mathscr S$ 为准确的 $s$ 阶系数移位。
(48) 等价于把
$P(t(w),h_A(w)\exp(a_p\epsilon/17))$
在整个 (46) 中求值；分母 $17,1!,\ldots,5!$ 都是单位。
源的任何整多项式恒等关系仍为零，因此也定义在 (44) 的完整原像格上。

在原算术值 $A^*$ 处，
$h_{A^*}=\Theta\exp(-\kappa w^s/17)$。
故原物理系数 $r_k(f)=[w^k]f$ 与 (48) 准确相连：
$$
\mathcal J_{6,A^*}(f)_{j,i}
=p^j r_{js+i}(f).
\tag{49}
$$
对非齐次 $f$ 逐真实权求和；没有统一改成错误的相对 charge。
这条式子与 ordinary 完整矩读取同一个 $r_k$，不将其单位切域混作 (49)。

### 9.3 导子主块、真实全尾和固定跨界成本

$\mathcal J_{6,\circ}(c_6)$ 在完整较长目标内准确为
$w^{r_c}U_{c,\circ}$，其中 $U_{c,\circ}$ 是整单位。
可直接取
$$
U_{c,\circ}
=(t/w)^{r_c}\frac{q_6(t)}{t^{r_c}}\,
 h_\circ^{69343}\exp(4079\,a_p\epsilon).
\tag{50}
$$
其常数是 $\ell_c$；式 (50) 保整个 $q_6,t,h_\circ$ 和 Gaussian。
对 $P$ 的每个真实权 $m$，总 Euler 为
$$
\mathcal E_{\mathrm{tot}}=\mathcal E+4079,
\qquad
\mathcal E_{\mathrm{tot}}P_m=\frac{m+69343}{17}P_m .
\tag{51}
$$
于是 (45) 在原六块目标的整个评价矩阵满足
$$
\boxed{\;
\mathcal M^c_A(P):=\mathcal J_{L+r_c,A}(Q_Mc_6P)
=Q_MU_{c,\circ}
 \sum_{j=0}^{5}\frac{(p\epsilon)^j}{j!}\,
 w^{r_c-5j}K_A^j\,
 \mathcal J_{6,\circ}(\mathcal E_{\mathrm{tot}}^jP).
\;}
\tag{52}
$$
等式在 (46) 中准确成立，并保所有高尾和后续折回。

证明先在同一非齐次来源逐权展开
$e^{\eta_A\mathcal E_{\mathrm{tot}}}$。
$j$ 次项首阶是 $r_c+j(s-5)$。
因 $r_c\ge356$，$j\le5$ 的 $r_c-5j$ 均非负，
可以真正使用
$w^{r_c+j(s-5)}=(p\epsilon)^j w^{r_c-5j}$，
而不是引入负幂后删项。
对 $j\ge6$，最早的 $j=6$ 与目标之差为
$$
r_c+6(s-5)-(5s+\ell+r_c)=s-\ell-30>0,
$$
因为 (43) 给 $s-\ell>r_c\ge356$。
后续项首阶递增，故全部超出完整目标。
取 $j=0$ 时需要 $\mathcal J$ 到 $L$；$j>0$ 的有效位移更大，
所以 (48) 的同一全窗口已经足够，没有少读输入尾。
这也付清各项作为 (46) 两环之间映射的边界关系。

单独的真实乘法
$$
m_{r_c}:\Gamma_L^{(6)}\longrightarrow\Gamma_{L+r_c}^{(6)},
\qquad x\mapsto w^{r_c}x
\tag{53}
$$
有准确 Smith 数据：$5r_c$ 个指数一，其余源指数零，
另有 $r_c$ 个自由余目标方向。
这是因为五个满块各有恰 $r_c$ 个末位跨界，
$w^i\epsilon^j\mapsto p\,w^{i+r_c-s}\epsilon^{j+1}$，
而末短块由 (43) 不跨界。
各像坐标互不重叠，最前 $r_c$ 个物理方向为空。
完整单位 (50) 和好位单位 $Q_M$ 不改变这些数据。
因此导子返回在目标的固定 torsion 费用为 $5r_c$；
不能把这项再作为原评价的独立单位秩相加。

### 9.4 真实中央零给出的同一个矩阵模 $p^6$

R943 的五条原中央同时零时，实际五轴满足
$u^*\equiv u^\dagger\pmod{p^5}$；
$u^\dagger$ 是固定原 $g_\circ,t,a_p$ 的五行 Hensel 零点。
(47) 从 $u$ 到整个 $K_A$ 是整线性映射，所以
$K_{A^*}-K_{u^\dagger}\in p^5\mathcal O[[w]]$。
(52) 的每个非常数参数项已有一个 $p$，从而
$$
\boxed{\mathcal M^c_{A^*}\equiv\mathcal M^c_{u^\dagger}
                   \pmod{p^6}}
\tag{54}
$$
在同一 (45)、同一完整目标和所有非齐次列上成立。
不是重新挑选源基，也不是只比较末度或一组左行。
任何给定源向量及其五个允许修正，在这两个完整矩阵下的
$p^6$ 成员性完全相同。

对整个原来源格还可准确界定未使用导子的有限差。
若 $f\in\mathcal A_N$ 的所有权都大于 $4\cdot195=780$，
(7) 迫其各项在 $(t,h_A)$ 代入后含 $w^5$；
$\mathcal E$ 及所有单位 Gaussian 保留这个因子。
当 $u-v\in p^5$ 时，模 $p^6$ 的差只剩
$p^5w^{s-5}(K_u-K_v)/p^5$ 乘一次 Euler 评价。
这里的 $w^5$ 使 $w^s=p\epsilon$ 再给一个 $p$。因此
$$
\mathcal J_{6,u}(f)\equiv\mathcal J_{6,v}(f)\pmod{p^6}
\quad(f\in\mathcal A_{N,>780},\ u-v\in p^5).
\tag{55}
$$
较高差次项已含 $p^{10}$。
在 $p$ 的正特征剩余系数中，(55) 也可从 (48) 的整多项式直接展开；
没有使用含 $p!$ 分母的无限形式指数。

所以 (54) 并非仅说明一个大导子平移：
五条真实中央的必要值已确定整个高权来源的六块矩阵模 $p^6$。
完整来源余下的差只读取固定、真实的 $\mathcal A_{\le780}$，
其维数不随 $N$ 增长；这些列仍须保留。
因为同一角函数域中不同 $\vartheta$ 权独立，
(44) 的权分解也是实际整数直和，此处没有把物理 Taylor 的互相抵消
误认作不同权之间的永久关系。
第六原来源及 R962 的过定行正落在这份低权格，不能删去。

## 10. 指定必要值的全部修正族与第六行的准确联立

固定好 $p$、同一预算和指定的整首来源 $P_0\in\mathcal B_M$。
在 (54) 的同一个完整矩阵
$N=\mathcal M^c_{u^\dagger}$ 下，真正待判集合是
$$
\mathfrak F_{p,M}(P_0)=
\{(P_1,\ldots,P_5):
 N(P_0+pP_1+\cdots+p^5P_5)\in p^6\Gamma_{L+r_c}^{(6)},
 \ P_i\in\mathcal B_{M,i}^{\rm allowed}\}.
\tag{56}
$$
$\mathcal B_{M,i}^{\rm allowed}$ 表示该问题原先允许的准确整来源；
若各页相同才取整个 $\mathcal B_M$。
(54) 证明这份指定族与实际 $A^*$ 的族完全相同。
(45) 及来源饱和性保证每一步所写的 $P_i$ 都回到同一原六源预算，
系数范数费用仍是 $\exp(O(M))$，没有除 $p$ 后改用较大的有理来源。

(56) 有不丢行、可逐页判定的准确条件。
先验 $\bar NP_0=0$。若已保
$N(P_0+\cdots+p^{j-1}P_{j-1})\in p^j\Gamma$，
第 $j$ 页的整个实际目标是
$$
y_j=-\,N(P_0+\cdots+p^{j-1}P_{j-1})/p^j\bmod p
 \ \in\ \bar N(\mathcal B_{M,j}^{\rm allowed}\bmod p),
\qquad 1\le j\le5 .
\tag{57}
$$
该式对每个已给定的前缀是充要条件；
分子包含所选整提升的全部下一位，所有六块及其跨界都在同一自由目标内。
只有在这个完整像中找到 $P_j$ 后，才能进入下一页。
第7.1节的自由基置换和固定整数乘法表使两边都是同一可重生整呈示，
而不是另立的抽象有限商。这里没有声称 (56) 非空或将其替换为
选定 normal 行的通过。

第六中央的实际条件必须与 (56) 保在一起。令旧五源为 $F_\nu$，
$q_\nu=d_\nu/17$，$q_Z=195/17$。
从 R959 同次六低 jet 取
$$
b_\nu=(\lambda_{\nu,5},\ldots,\lambda_{\nu,1}),\quad
B_5=(b_\nu)_\nu,\quad
c=b_ZB_5^{-1},\quad
\Delta=Z-\sum_{\nu=S,T,U,V,W}c_\nu F_\nu .
\tag{58}
$$
$B_5$ 在指定好位为单位，全部系数和固定分母先于 $p$ 确定。
真实低 jet 给 $\Delta\in w^6\mathbf Q[[w]]$，
且 $[w^6]\Delta=-\det(B_6)/\det(B_5)\ne0$。
置同一实际低权来源
$$
H=\mathcal E^{-1}\Delta
=\frac{Z}{q_Z}-\sum_\nu\frac{c_\nu F_\nu}{q_\nu}.
\tag{59}
$$
此处只在六个非零实际权上取逆，$p>211$ 保其分母为单位；
并未把 $\mathcal E$ 在常数列或权为 $p$ 倍数的整格上求逆。
固定清分母后，(58)–(59) 都属于 (44) 的真实 $\mathcal A_{\le195}$。

R943 的归一中央式第一位是
$F_\nu(u)\equiv [w^s]\widehat F_{\nu,A}/q_\nu\pmod p$。
故六个原中央同时零必给同源的确定必要条件
$$
\boxed{[w^s]H\in p\mathcal O.}
\tag{60}
$$
这里原质量零保证 $[w^s]H$ 与 regularized 版本完全相同，故该系数整。
其参数不变性也可直接核：
$\mathcal EH=\Delta$ 的前五项准确为零，
$\eta_A$ 从 $w^{s-5}$ 起，第一扰动从 $w^{s+1}$ 才进入；
第二及更高扰动在 $s>9$ 时也越过 $w^s$。
Gaussian 首变化为 $w^s\mathcal EH$，同样不改变这个系数。
所以 (60) 的 $H$ 是原物理来源，不能用任意参考高尾替代。

更高精度须采用 R962 的完整过定余式，
包括六个原 Newton 的全部尾和实际五行 Hensel 提升；
(60) 不替代它们。
(56)–(60) 已将实际必要值、高权同格修正族与固定低权第六行
写成同一来源内可判的联合条件。
仍需在这份指定联合条件中证明不可相容，或实际完成一个
可消费的深核估计；未从其表示法或 Hilbert 常数宣称主目标完成。


## 11. 更正：撤销原 $\epsilon$ 平移及其三项推论

2026-11-26 13:44 UTC 复核发现本节原证明遗漏了 $a_p=p\kappa$ 中的一个 $p$。
原稿见提交 `4b637b2e95654b7b0753c28f519701c6529ecb15`；
本节原 (63)–(71) 的自同构、完整核同一及 $125\log p$ 前缀成本现全部撤销，
不能在后续证明中使用。原给定首项修正族同一性也随之撤销。

在原
$$
\Gamma_{5s+m}=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^6,w^m\epsilon^5)
$$
中，若
$$
\eta_u-\eta_v=p^5w^{s-5}V(w),\qquad a_p=p\kappa,
$$
则正确的平移量为
$$
\frac{\eta_u-\eta_v}{a_p}
=p^4\kappa^{-1}w^{s-5}V(w).
\tag{61-corrected}
$$
因此拟议替换 $\epsilon\mapsto\epsilon+(\eta_u-\eta_v)/a_p$ 给
$$
w^s-p\epsilon\longmapsto
-p^5\kappa^{-1}w^{s-5}V(w),
\tag{62-corrected}
$$
右边一般不属于 $p^6\Gamma_{5s+m}$。例如 $V=1$ 时，
$w^{s-5}$ 是原自由基中的一个元素，该项模 $p^6$ 非零。
所以这甚至不是原有限目标环模 $p^6$ 上的良定义映射；
不能只修改旧成本常数来修复原证明。

本更正不撤销第1–10节的既有结论。特别，第9节在
$\eta_u-\eta_v$ 本身上使用真实 $p^5$，高权来源含 $w^5$，
由 $w^s=p\epsilon$ 再取得一个 $p$，并没有除以 $a_p$。
同样，导子块在原固定首阶下保留全部 carry。
故已付的是导子像及原权 $>780$ 的完整矩阵模 $p^6$ 比较；
完整低权块仍须逐项处理，不得借此宣称整个原来源核相等。
第10节的全部允许修正和实际全目标像条件继续保留。

后继工作必须直接在原完整来源格和原行序计算低权扰动，
连同所有五修正的真实像与剩余余核；在新的完整证明之前，
不给它赋自同构、全核同一、固定前缀费用或深核存在性。
