# R1006：原端列的线性循环维数与无限素数族上的不稳定性

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**状态：已证明。** 本文保留 R968/R992 的实际列、原本原筛选和原 Legendre 因子。
结论排除“所有充分大允许素数上原筛选空间对 R992 算子稳定”这条路线。
它不证明原 CM 标记为零，也不否定同一标签非零或特定 Hasse 商的包含；
Serre 主目标仍开放。证明不使用新的素数扫描或有限秩拟合。

## 1. 原对象与结论

令 $p=6N+5\ge41$ 为素数，$k=\lfloor p/12\rfloor$，并使用
$$
X=E_4,\quad Y=E_6,\quad z=X^3/Y^2.
$$
R992 将实际空间 $M_{p-5}(\mathbb F_p)$ 写成
$Y^N\mathbb F_p[z]_{\le k}$。原端列的归一多项式是
$$
P_p(z)=Y^{-N}(p-7)!\,Z_{p-7,1}.
\tag{1006.1}
$$
记 R992 的准确 Jacobi 算子为
$$
\mathscr G=z(1-z)\partial_z^2+
 \left(\frac43-\frac73z\right)\partial_z-\frac{55}{144}.
\tag{1006.2}
$$

**定理。** 存在绝对常数 $c>0$，使每个充分大的
$p\equiv5\pmod6$ 都满足
$$
\dim_{\mathbb F_p}
\operatorname{span}\{P_p,\mathscr GP_p,\mathscr G^2P_p,\ldots\}
\ge cp.
\tag{1006.3}
$$
进而存在一个约化素数等差族，全部属于原
$p\equiv2,5\pmod9$ 允许类，且 $5\nmid p+1$，使该族所有充分大素数
的真实筛选空间 $V_p$ 均满足
$$
\boxed{\mathcal G(V_p)\not\subset V_p.}
\tag{1006.4}
$$
这里 $\mathcal G(Y^NP)=Y^N\mathscr GP$，与 R992 完全相同。

证明分为固定特征零源、固定微分方程、谱支撑和原筛选计数四部分。

## 2. 原端列的固定有理 germ

取 $q=e^{2\pi i\tau}$、$Q=q^{1/6}$、
$\delta=q\,d/dq$ 和 $\Theta_Q=6\delta$。
消费 R964/R1002 已证明的完整原 CM 源
$$
g=H_{12}^{\rm inv}=\eta^4E_4E_6=\sum_{n\ge1}a_nQ^n.
$$
定义固定的特征零级数
$$
W=\sum_{n\ge1}a_n n^{-10}Q^n,\qquad
U=\sum_{n\ge1}a_n n^{-11}Q^n,\qquad
f_\infty=\eta^{-4}W.
\tag{1006.5}
$$
只有 $n\equiv1\pmod6$ 的项非零，所以 $f_\infty\in\mathbb Q[[q]]$。
令 $D_w=\delta-wE_2/12$，并定义
$$
\begin{aligned}
C_\infty={}&432D_{-7}D_{-9}D_{-11}f_\infty
 +75E_4D_{-11}f_\infty-9E_6f_\infty,\\
P_\infty={}&E_6^{5/6}C_\infty.
\end{aligned}
\tag{1006.6}
$$
所有 cusp 根取常数项 $1$。由于
$z=1+1728q+O(q^2)$，$P_\infty$ 是 $z=1$ 处的有理 Taylor germ。

有以下准确约化：
$$
\boxed{P_p\equiv P_\infty\pmod{p,(z-1)^p}.}
\tag{1006.7}
$$

证明：R964 的完整 $Q$ 级数恒等式给
$\Theta_Q^{10}W_{p-9}=g\pmod p$。
在 $f=W_{p-9}/\eta^4$ 的 $q^p$ 前，只需理想范数
$n\le6p-5<6p+1<p^2$。$p$ 在 $\mathbb Q(\sqrt{-3})$ 惰性；
若一个非零理想项的范数被 $p$ 整除，则它被 $p^2$ 整除。
故该精度内所有可能非零的 $n$ 均可逆，逐项得到
$f\equiv f_\infty\pmod{p,q^p}$。
这里没有对 $\Theta_Q$ 的零特征值求逆。

R1002(1002.31) 给准确原列
$$
(p-7)!Z_{p-7,1}=432D^3f+75XDf-9Yf.
$$
$f$ 的实际权为 $p-11$，连续三个权模 $p$ 为 $-11,-9,-7$，
故正好得到 (1006.6) 的三个导数。
又 $N=(p-5)/6$，所以
$$
E_6^{-N}=E_6^{5/6}E_6^{-p/6}
 \equiv E_6^{5/6}\pmod{p,q^p}.
$$
最后一步可在 $\mathbb Z_{(p)}[[q]]$ 中逐系数构造
$H^6=E_6^{-1}$、$H(0)=1$，因为 $6$ 可逆；然后
$H^p\equiv H(q^p)\equiv1\pmod{p,q^p}$。
形式逆换元的线性系数 $1728$ 也是单位，得到 (1006.7)。

## 3. 一个完全指定的固定 Fuchs 方程

设
$$
t=E_6^{1/6},\quad a=z^{2/3},\quad r=a(z-1),\quad
h=\left(\frac{z-1}{1728}\right)^{1/6}.
$$
局部选择使
$$
E_4=t^4z^{1/3},\quad E_6=t^6,\quad
\eta^4=t^2h,\quad
\delta=t^2r\partial_z,\quad
E_2=t^2a+12trt'.
\tag{1006.8}
$$
Ramanujan 方程直接给
$$
t''+P t'+Q_0t=0,\qquad
P=\frac2{3z}+\frac1{z-1},\quad
Q_0=\frac7{144z(z-1)}.
\tag{1006.9}
$$
其无穷远指数为 $1/12,7/12$。
此外 $\tau'=1/(2\pi i\,t^2r)$，故
$W(t,t\tau)=1/(2\pi i r)$；由于 $P=r'/r$，$t\tau$ 确是第二解。

以下递归完全指定九次对称幂的首一算子：
$$
A_0=1,\quad A_1=\partial_z,\quad
A_{j+1}=(\partial_z+jP)A_j+j(10-j)Q_0A_{j-1}
\quad(1\le j\le9),\qquad S_9=A_{10}.
\tag{1006.10}
$$
算子从右到左作用。
令 $u=t^9W$。有准确 Bol 恒等式
$$
\delta^{10}(t^{-9}u)=t^{11}r^{10}S_9u.
\tag{1006.11}
$$
两边的最高阶系数均为 $t^{11}r^{10}$，齐次核均由
$t^9,t^8(t\tau),\ldots,(t\tau)^9$ 张成，这同时证明恒等式。
由 $\Theta_Q^{10}W=g$ 得
$$
S_9u=Rt,\qquad
R=6^{-10}h z^{1/3}r^{-10},\qquad
b=R'/R=-\frac{19}{3z}-\frac{59}{6(z-1)}.
\tag{1006.12}
$$
因此明确的十二阶有理算子
$$
L_u=\big((\partial_z-b)^2+P(\partial_z-b)+Q_0\big)S_9
\tag{1006.13}
$$
杀掉 $u$。设 $v=u/h$，则
$L_v=h^{-1}L_uh$ 杀掉 $v$；完全展开时只需把每个
$\partial_z$ 替成 $\partial_z+1/[6(z-1)]$。
这些算子在 $0,1,\infty$ 均正则奇异。
无穷远指数来自 (1006.9) 的对称幂、已显示的有理指数扭曲和
合成时的整数位移，故全部有理。

原输出也可完全指定。令 $T=(z-1)\partial_z$。
由 (1006.8) 有
$$
D_w(t^w\phi)=t^{w+2}a(T-w/12)\phi.
$$
因 $f_\infty=t^{-11}v$，代入 (1006.6) 得 $P_\infty=Ov$，其中
$$
\begin{aligned}
O={}&432z^2
 \left(T+\frac7{12}+\frac{4(z-1)}{3z}\right)
 \left(T+\frac9{12}+\frac{2(z-1)}{3z}\right)
 \left(T+\frac{11}{12}\right)\\
 &+75z\left(T+\frac{11}{12}\right)-9.
\end{aligned}
\tag{1006.14}
$$
其表观分母完全消去：
$$
\begin{aligned}
O={}&432z^2(z-1)^3\partial_z^3
 +(3132z^2-864z)(z-1)^2\partial_z^2\\
 &+(4761z^2-2661z+96)(z-1)\partial_z
 +(4301z^2-3685z+316)/4.
\end{aligned}
\tag{1006.15}
$$

所以 $P_\infty$ 满足一个固定的非零有理标量方程
$$
LP_\infty=0,\qquad \operatorname{ord}L\le12,
\tag{1006.16}
$$
且 $L$ 在无穷远正则奇异，全部无穷远指数有理。
这里无需猜测 $L$：写 $L_v$ 的十二维 companion 矩阵为 $C$，
写 $O$ 的输出行为 $a_0$，递归
$a_{j+1}=a_j'+a_jC$。首个依赖
$a_m=\sum_{j<m}b_ja_j$ 给
$L=\partial_z^m-\sum_{j<m}b_j\partial_z^j$，全部在 $\mathbb Q(z)$ 中。
其完整解空间是原解空间经过 $O$ 的像。
正则奇异解的有限有理幂与对数展开经有理微分算子仍有这种形式，
指数只发生整数位移或首项消失；故此像的标量方程仍正则奇异，
指数仍有理。新增的有限奇点至多表观，不影响以下证明。

## 4. 固定源没有任何有限 Jacobi 谱关系

我们证明比“$P_\infty$ 不是多项式”更强的事实：
$$
H(\mathscr G)P_\infty\ne0
\quad\text{对每个 }0\ne H\in\mathbb C[X].
\tag{1006.17}
$$

由原完整源，
$g(-1/\tau)=-\tau^{12}g(\tau)$。
固定 Eichler 积分为
$$
U(\tau)=\frac{(2\pi i/6)^{11}}{10!}
 \int_{i\infty}^{\tau}(\tau-z)^{10}g(z)\,dz.
$$
直接换元 $z=-1/w$ 得
$$
U(-1/\tau)=-\tau^{-10}(U(\tau)+\Pi(\tau)),\qquad
\Pi(\tau)=\frac{(2\pi i/6)^{11}}{10!}
 \int_0^{i\infty}(\tau-z)^{10}g(z)\,dz.
\tag{1006.18}
$$
$\Pi$ 为次数至多十的多项式。Mellin 积分给
$$
\Pi(0)=-L(H_{12}^{\rm inv},11)\ne0.
\tag{1006.19}
$$
非零只用 R964 的明确 CM Hecke 角色：其无穷型为十一，
该 Euler 乘积在 $11>11/2+1$ 绝对收敛，所有局部因子非零。
这是绝对收敛区的非零，不是未知的中央值非零假设。

令 $c_0=6/(2\pi i)$、$K(\tau)=\tau\Pi'(\tau)-10\Pi(\tau)$。
则 $\deg K\le9$、$K(0)=-10\Pi(0)\ne0$。微分 (1006.18) 得
$$
W(-1/\tau)=-\tau^{-9}
 \{\tau W-10c_0U+c_0K\}.
\tag{1006.20}
$$
沿 $S$ 延拓的根满足
$t(-1/\tau)=\epsilon\tau t$、$h(-1/\tau)=-\epsilon^{-2}h$，
其中 $\epsilon^6=1$。因此 $v=t^9W/h$ 的该分支是
$$
\epsilon^{11}\frac{t^9}{h}
 \{\tau W-10c_0U+c_0K\}.
\tag{1006.21}
$$
前两项只有整数 $q$ 指数，乘至多一次 $\log q$；
最后一项有非零的 $q^{-1/6}K(\tau)$ 部分。
原输出 $O$ 在此指数的 cusp 指标值是
$$
432\left(\frac5{12}\right)\left(\frac7{12}\right)
 \left(\frac9{12}\right)+75\left(\frac9{12}\right)-9=126\ne0.
\tag{1006.22}
$$
所以最高对数次数的该分数指数项经过 $O$ 后仍非零，
不能被整数指数项抵消。这确实是 $P_\infty$ 的解析延拓分支：
$z$ 为模函数，连接 $\tau$ 与 $S\tau$ 的避开奇点路径映到 $z$ 平面的环路。

另一方面，令 $w=z-1$，则
$$
\mathscr G(w^\alpha)=-\alpha^2w^{\alpha-1}+O(w^\alpha).
$$
若 $\deg H=m>0$，$H(\mathscr G)$ 在 $w=0$ 正则奇异，
指标多项式为非零常数乘
$$
\prod_{j=0}^{m-1}(\alpha-j)^2.
$$
其所有局部指数均为整数，不能有上述非零的 $q^{-1/6}$ 分支。
常数非零 $H$ 的情形直接成立。由此证明 (1006.17)。

## 5. 固定 Fuchs 方程迫使谱支撑有界或线性增长

以下引理将有限复杂度的特征零方程用于全部素数，
并不将固定低谱和随 $p$ 移动的高谱混淆。

设有理 germ $F$ 满足固定有理方程 $L$，
$L$ 在无穷远正则奇异且其指数全部有理。
设 $\deg F_p\le\lfloor p/12\rfloor$，并有
$F_p\equiv F\pmod{p,(z-1)^p}$。
在 Jacobi 基
$$
B_n={}_2F_1(-n,n+4/3;4/3;z)
\tag{1006.23}
$$
中，$F_p$ 的非零支撑个数要么被固定常数 $B$ 控制，
要么至少为 $cp$，其中 $B,c>0$ 与 $p$ 无关。

### 5.1 先得到实际多项式方程

清掉 $L$ 的分母，记阶为 $r_0$，其多项式系数为 $a_j$，
$C_0=\max_j(\deg a_j-j)$。
由 jet 匹配，$LF_p$ 在 $z=1$ 零阶至少 $p-r_0$，而
$$
\deg(LF_p)\le\lfloor p/12\rfloor+C_0<p-r_0
$$
对充分大 $p$ 成立。因此严格有 $LF_p=0$，没有把有限 jet
直接冒充全局方程。

再乘 $z^{r_0}(1-z)^{r_0}$，必要时乘额外多项式，使每个 $a_j$
被 $z^j(1-z)^j$ 整除，且
$D=\max_j(\deg a_j-j)\ge1$。
定义其无穷远增长指标多项式
$$
I(n)=\sum_{\deg a_j=D+j}[z^{D+j}]a_j\,(n)_{\underline j}.
\tag{1006.24}
$$
它非零，全部根有理；正则奇异性保证最高阶项也达到该 $D$，
所以这确为无穷远指标多项式，而非任意头项截取。

### 5.2 准确带宽与两个端点系数

在 $\mathbb Q$ 上用内积
$\langle f,g\rangle=\int_0^1 f(z)g(z)z^{1/3}\,dz$。
$B_n$ 的首项系数及平方范数是
$$
\ell_n=(-1)^n\frac{(n+4/3)_n}{(4/3)_n},\qquad
h_n=\frac{(n!/(4/3)_n)^2}{2n+4/3}.
\tag{1006.25}
$$
它们由 Jacobi 正交性或 Rodrigues 公式直接得到。
形式伴随
$$
L^\dagger=\sum_j(-1)^jz^{-1/3}\partial_z^j(z^{1/3}a_j\,\cdot)
$$
仍为多项式微分算子：所加的 $z^j(1-z)^j$ 同时消去分母和
全部分部积分边界。它的度位移仍为 $D$，
$$
I^\dagger(n)=I(-n-D-4/3).
\tag{1006.26}
$$
正交性和度给
$$
LB_n\in\operatorname{span}\{B_j:\max(0,n-D)\le j\le n+D\}.
\tag{1006.27}
$$
最高、最低系数准确为
$$
[B_{n+D}]LB_n=\frac{\ell_n}{\ell_{n+D}}I(n),
\tag{1006.28}
$$
$$
[B_{n-D}]LB_n=
 \frac{h_n}{h_{n-D}}\frac{\ell_{n-D}}{\ell_n}I(-n-4/3)
 \quad(n\ge D).
\tag{1006.29}
$$
后一式来自 $\langle B_n,L^\dagger B_{n-D}\rangle$；
(1006.26) 中的 $D$ 因而恰消去。

以上等式可准确约化模 $p$。
只要 $n\le k+2D$ 且 $p>24D+8$，(1006.25) 中所有非固定的
正整数因子均小于 $p$：最大不超过 $6n+4<p$。
故首项、范数、固定移位比值以及三角基变换均为单位。
固定有理系数只排除有限个坏素数。特别是两个端点系数的零点
正是 (1006.28)–(1006.29) 已列的零点。

### 5.3 支撑分量的两种尺度

写 $F_p=\sum c_nB_n$，将非零支撑中相邻距离不超过 $2D$ 的项
连接为分量。不同分量经 $L$ 后可能出现的输出区间互不相交，
所以每个分量分别被 $L$ 杀掉。
一个分量的最大支撑 $b$ 在唯一最高输出 $b+D$ 给 $I(b)=0$。
最小支撑 $a$ 若 $a\ge D$，则唯一最低输出给
$I(-a-4/3)=0$；否则 $a\in\{0,\ldots,D-1\}$。
分量个数至多 $\deg I$。

所有可能端点都在一个固定有限集的有理仿射轨迹
$n=\lambda p+\mu$ 上。确实，若 $A/B$ 为 $I$ 的有理根，
$Bn-A=mp$，而 $0\le n\le p/12+O(1)$ 只容许固定有限个整数 $m$；
最低端点同理。
令 $A_0$ 界住全部 $|\mu|$，令 $\Delta>0$ 为不同斜率间最小正差。
两端同斜率的分量跨度至多 $2A_0$；不同斜率的分量跨度至少
$\Delta p-2A_0\ge\Delta p/2$，而相邻非零支撑间距不超过 $2D$，
故该分量至少含 $\Delta p/(4D)$ 个支撑。
因此总支撑要么不超过
$B=(\deg I)(\lfloor2A_0\rfloor+1)$，要么至少为 $cp$。
若只有一个斜率，只有有界分支。引理得证。

## 6. 排除有界分支，包括随 $p$ 移动的谱

将第5节用于 $F=P_\infty$ 和 (1006.7)。
R992 的本征值
$$
\lambda_n=-(n+5/12)(n+11/12),\qquad0\le n\le k
$$
两两不同，因此非零谱支撑个数恰为 $\mathscr G$ 循环维数。

由 (1006.17)，有理 Taylor germs
$P_\infty,\mathscr GP_\infty,\ldots,\mathscr G^BP_\infty$
线性无关。故存在一枚固定有限的
$(B+1)\times(B+1)$ Taylor 系数子式 $\Delta_0\in\mathbb Q^\times$。
只排除其有限个分子、分母坏素数。
(1006.7) 经至多 $2B$ 次微分后，对充分大 $p$ 仍覆盖该固定子式
的全部行，所以相应 $P_p$ 子式等于 $\Delta_0\bmod p$ 且非零。
于是循环维数大于 $B$，无论支撑在固定低 $n$ 还是在 $n\sim\lambda p$。
第5节立即给 (1006.3)。

这里不需要声称“有界支撑必在固定低谱”，也不使用这种错误特化。

## 7. 返回原本原与 Legendre 筛选

选有限平方自由整数 $M$，使
$$
(M,30)=1,\qquad\frac{\varphi(M)}M<3c.
$$
由素数倒数和发散，取足够多的 $\ge7$ 素数之积即可做到。
选择等差条件
$$
p\equiv-1\pmod{6M},\qquad
p\equiv2\pmod9,\qquad
p\equiv1\pmod5.
\tag{1006.30}
$$
这些条件相容，并给模 $90M$ 的约化剩余类。
Dirichlet 定理给无穷多素数，全部属于原允许类，且 $5\nmid p+1$。

写 $p+1=6Mt$。原标签恰为
$h=6j+1$、$1\le j\le Mt-1$。
R971 的计数直接给
$$
\dim V_p\le t\varphi(M)-1
 =\frac{(p+1)\varphi(M)}{6M}-1<cp
\tag{1006.31}
$$
对充分大 $p$ 成立；其余本原因子和 Legendre 筛选只会减少列数。

另一方面，R996 对同一个原端标签 $h=p-4$ 给
$(h,p+1)=1$（因为 $5\nmid p+1$），且
$P_{h-1}(1/s)=19/9$ 为单位。
所以 $V_p$ 含原端列的非零标量倍。
若 $\mathcal G(V_p)\subset V_p$，归一后必含该端列的整个循环空间；
(1006.3) 和 (1006.31) 矛盾，证明 (1006.4)。

## 8. 准确边界与后继

R992 的条件命题“原 $V_p\ne0$ 且稳定则同一标签非零”仍正确。
本结果证明其中稳定性不能成为一个覆盖所有充分大允许素数的普遍输入。
原标记泛函可以在不稳定空间上非零；本证明没有给任何一个
原同标签三因子全部为零的素数，也没有排除特定 $A/E_4$ 的包含。

因此后继应直接研究原标记或特定包含、原完整源的其它关系，
不能继续把原空间的全素数稳定性当待证普遍定理。
O2 的原高坐标单位、O0 的全局覆盖和真正高度仍须独立处理。

## 来源与已成输入

- [R964](R964-inverse-conductor-two-s-CM-family-and-original-sigma-heat-channel.md)：原 conductor-$2s$ 逆角色、完整 $H_{12}^{\rm inv}$ 与 $\Theta_Q^{10}$ 身份。
- [R1002](R1002-ten-step-theta-companion-and-four-free-CM-jets.md)：真实权 $p-11$ 与准确端列 $432D^3f+75XDf-9Yf$。
- [R992](R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md)：原归一坐标、准确 Jacobi 算子、完整简单谱及条件同标签桥。
- [R996](R996-original-end-column-cusp-unit-and-filtered-space-nonzero.md)：同一端列的两个原筛选因子。
- [R971](R971-complete-Wilson-Fourier-source-and-filtered-span-obstruction.md)：原本原标签计数；本篇无需重算旧满秩点。
