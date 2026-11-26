# R947 — 原 E89 新来源环的完整规范化、同环参数替换与权 28883 整导子

日期：2026-11-26。**状态：已证明。** 本篇支付 R943 §8 留下的新增来源环成本。实际公开计算先发现旧 $U,W$ 的角因子共有一个四次因子；因此不能直接把它们当作有限参数。随后在同一来源环内作 $U_+=U+S^4$，完整角多项式的 Bézout 恒等式给新参数互素。本篇证明全部剩余权的有限整性、准确全函数域、一个实际定义的固定导子及整返回的次数和系数成本。

这里的 $W$ 是 R943 的完整 $W_{178}$，没有换掉其 CM 来源、原相位或任何高次系数。$U_+$ 只用于来源环的代数表示；本篇没有为 $U_+$、规范化元素或导子乘积新增中央消失断言。主课题的无穷素数非零与完整 Selmer 门仍须另证。

## 1. 原来源及两次公开有限计算

沿 [R473](R473-three-source-function-field-normalization-and-integral-conductor.md) 与 [R943 §8、§12](R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md)，置
$$
a=t(t-1)(7+4t+16t^2),\qquad d=1+8t,\qquad f=ad/7,
$$
$$
S=\vartheta^{17}f,\quad
T=\vartheta^{36}fV,\quad
U=\vartheta^{68}aH/91,\quad
W=\vartheta^{89}f_W.
\tag{1}
$$
$V$、$H$ 是 R473 的完整次数六、十八多项式。特别
$$
\begin{aligned}
H={}&(8t^2+20t-1)
(256t^4-1024t^3+1536t^2-52t+13)\\
&\cdot(1792t^4-3136t^3+2112t^2-40t+1)\\
&\cdot(32768t^8-851968t^7+1949696t^6-2111488t^5\\
&\hspace{15mm}+439040t^4-49408t^3+58688t^2+1232t-1).
\end{aligned}
\tag{2}
$$
$\vartheta$ 权为一，故四个原生成元的权为 $17,36,68,89$。实际函数的代入是 $\vartheta=\Theta=x\sigma^2$、$t=-x^{-3}$；R473 已付 $\Theta$ 的超越性与原全函数域。

新的 $f_W$ 每次从完整 CM7、CM13 算子同次重生，定义为
$$
f_W(t)=\sum_{j=0}^{28}c_j(-t)^{29-j},\qquad
G=f_W/a.
\tag{3}
$$
不把旧 run 的二十九个系数写进输入。两次运行均核定
$$
\deg f_W=29,\qquad \deg G=25,\qquad
\operatorname{ord}_{0}f_W=\operatorname{ord}_{1}f_W
=\operatorname{ord}_{\alpha_1}f_W
=\operatorname{ord}_{\alpha_2}f_W=1,
\tag{4}
$$
其中 $\alpha_1,\alpha_2$ 是 $7+4t+16t^2$ 的两根；还核定
$$
f\mid f_W,\qquad \operatorname{ord}_{-1/8}f_W=1,
\qquad \deg\gcd(H,G)=4.
\tag{5}
$$
最后这个实际四次公因子使 $U^{89},W^{68}$ 有共同有限零点。旧参数的无基点性、映射次数 $1700$ 或相关导子均不能由它们直接推出。

作同环齐次替换
$$
\boxed{U_+=U+S^4=\vartheta^{68}aH_+,\qquad
H_+=H/91+a^3d^4/7^4.}
\tag{6}
$$
第二次实际计算给
$$
\deg H_+=18,\quad
\gcd(H_+,G)=1,\quad
\gcd(H_+,ad)=1,\quad
\gcd(a,G)=1.
\tag{7}
$$
其中 $\gcd(H_+,G)=1$ 由完整多项式 Bézout 回乘核验，未只比维数或少数值。又
$$
R[S,U_+,W]=R[S,U,W]
\tag{8}
$$
因为两个方向的替换均在同一环内，且都保权。

此替换有确定的一般来源。令
$H_c=H/91+c\,a^3d^4/7^4$。在 $a$ 或 $d$ 的根处，其值等于 $H/91$，非零；其十八次首项也不变。在每个 $G$ 的根处，至多一个 $c$ 导致 $H_c$ 消失；若该根是 $d=0$，则没有坏 $c$。因此 $0,\ldots,25$ 中必有可用整数。公开 reader 实际只经过 $c=0$ 的 gcd 度四和 $c=1$ 的 gcd 度零，不以存在性替代实际参数。

## 2. 固定整模型与正确的有理除子

先沿用
$$
R_0=\mathbf Z[1/(2\cdot3\cdot7\cdot13\cdot17)].
$$
(3) 的系数分母整除 $91$；$a$ 的首项 $16$ 在 $R_0$ 中为单位，故精确除法给 $G\in R_0[t]$。定义一个明确非零有理数
$$
\Delta=5\,\operatorname{lc}(G)\,
\operatorname{Res}_t(a,G)\,
\operatorname{Res}_t(H_+,G),
\qquad R=R_0[1/\Delta].
\tag{9}
$$
这是固定整模型；所删素数是这些固定有理数的分子、分母素因子，不随预算或目标素数改变。定义 (9) 不需要把大 resultant 的整数展开存进仓库。第 8 节列出其重生方法及精确哈希。

R473 的原证书给 $ad$ 平方自由、$\gcd(ad,H)=1$、$\gcd(ad,V)=1$，以及所有有关首项在 $R_0$ 中为单位。因为 $H_+-H/91$ 被 $a^3d^4$ 整除，$\gcd(ad,H_+)=1$ 对每个 $R$ 的剩余域仍成立，且 $\deg H_+=18$ 不降。(9) 保证 (7) 中其余互素性、$\deg G=25$、(4) 的四点简单性也在每个剩余域成立。$d\mid G$ 在整模型上成立；其重数在剩余域允许上升，以下证明不要求它仍为一。

令
$$
A^+=R[S,T,U,W]\subset R[t,\vartheta].
$$
在 $a$ 的每个几何根处，旧源的最小比值是 $1/68$，而 $W$ 的比值为 $1/89$。其余有限点的最小比值为零。在无穷远，新的最大角次数比值是 $29/89$，大于旧 $22/68=11/34$。相应的有理除子准确为
$$
\boxed{
D^+=\frac{29}{89}[\infty]
-\frac1{89}\operatorname{div}_0(a),\qquad
\deg D^+=\frac{25}{89}.}
\tag{10}
$$
对所有 $m\ge0$ 定义
$$
\boxed{
B^+_m
=\vartheta^m a^{\lceil m/89\rceil}
R[t]_{\le\lfloor29m/89\rfloor-4\lceil m/89\rceil},
\qquad B^+=\bigoplus_{m\ge0}B^+_m.}
\tag{11}
$$
负次数上界表示零空间。这正是
$\vartheta^m H^0(\mathbf P^1_R,\mathcal O(\lfloor mD^+\rfloor))$ 的显示写法，包含全部 $m$，没有只保留一个 Veronese 子环。

四个原源均属于 (11)：其角次数依次为 $5,11,22,29$，各含 $a$。在 $a$ 的各不可约因子处给 $\vartheta$ Gauss 权 $-1/89$，在无穷远给权 $29/89$。这些赋值非负与属于 $R[t,\vartheta]$ 的条件逐项恰为 (11)。所以 $B^+$ 是正规环与赋值环的交，因而正规；$R[t,\vartheta]$ 保留了所有竖直整性。

但这一步尚未证明它在 $A^+$ 上整。下节给真正有限的整扩张。

## 3. 无基点 pencil、全部 6052 个剩余权与有限整性

置
$$
L=68\cdot89=6052,\qquad
\rho=\vartheta^L a^{68},\qquad D=1700.
$$
准确有
$$
(B^+)^{(L)}=\bigoplus_{n\ge0}\rho^nR[t]_{\le Dn}.
\tag{12}
$$
同一权的两个实际源为
$$
U_+^{89}=\rho\,a^{21}H_+^{89},\qquad
W^{68}=\rho\,G^{68}.
\tag{13}
$$
括号内的角式次数分别为
$$
4\cdot21+18\cdot89=1686,\qquad25\cdot68=1700.
$$
将它们都齐次化为次数 $D$ 后，有限点无公共零点：$G$ 与 $aH_+$ 互素。无穷远由 $G^{68}$ 的单位首项覆盖。依 (9)，这在整个 $\mathbf P^1_R$ 上是无基点 pencil，而不只是在特征零的断言。

写 $m=Ln+r$，$0\le r<L$，并置
$$
k_r=\lceil r/89\rceil,\qquad
q_r=\lfloor29r/89\rfloor-4k_r.
$$
完整剩余权空间准确为
$$
B^+_{Ln+r}
=\vartheta^r a^{k_r}\rho^n
R[t]_{\le Dn+q_r}.
\tag{14}
$$
由 (13) 的 Koszul 序列，
$$
0\longrightarrow\mathcal O(Dn+q_r-2D)
\longrightarrow\mathcal O(Dn+q_r-D)^{\oplus2}
\longrightarrow\mathcal O(Dn+q_r)
\longrightarrow0.
\tag{15}
$$
当 $Dn+q_r-2D\ge-1$ 时，左项的 $H^1$ 为零，故两个实际源的乘法对该整格满射。

具体地，$q_r\ge-4$；只有 $r=1,\ldots,9$ 满足 $q_r\le-2$，$r=10,11,12$ 时 $q_r=-1$，其余 $q_r\ge0$。因此：

- $r=1,\ldots,9$ 保留 $n\le2$ 的非零空间，之后由 (15) 递推；
- 所有其余剩余权保留 $n\le1$ 的非零空间，之后递推。

所以 $B^+$ 在 $R[U_+^{89},W^{68}]$ 上由 (11) 中权至多
$$
\boxed{M=2L+9=12113}
\tag{16}
$$
的有限多个显示基元素生成。进而它在 $R[U_+,W]$、$R[S,U_+,W]$ 和 $A^+$ 上都是有限模。

R473 已证明
$$
\operatorname{Frac}R[S,T,U]=\mathbf Q(t,\vartheta).
$$
因此 $A^+\subset B^+$ 与旧环有相同的全函数域。结合正规性与有限整性，得到：

**定理 1。** (11) 是 $A^+$ 的完整规范化。对每个 $R$ 的剩余域 $k$，把原生成元映到 $k[t,\vartheta]$ 后所得来源环的规范化，也由 (11) 逐项约化给出。

这里的剩余域陈述指实际生成元的像；没有仅凭有限整性宣称任意给定关系呈示在约化后都无新增关系。后面对三生成元子环给出确切 monic 呈示。

## 4. 实际新参数的 1700 次覆盖及完整 birational 证明

以下 $k$ 可取 $\mathbf Q$ 或任一 $R$ 的剩余域。设
$$
\mathscr A=\frac{U_+^{89}}{W^{68}}
=\frac{a^{21}H_+^{89}}{G^{68}},
\qquad
\mathscr C=\frac{S\,U_+^{22}}{W^{17}}
=\frac{a^6dH_+^{22}}{7G^{17}}.
\tag{17}
$$
由 (7)，$\mathscr A$ 已约分，其分子、分母次数是 $1686,1700$。$\mathscr C$ 仅从显示分子、分母约去一个 $d$：$G$ 被 $d$ 整除，而 $aH_+$ 与 $G$、$d$ 的相应交叉因子互素。约分后次数为 $420,424$。所以
$$
\deg\mathscr A=1700,\qquad \deg\mathscr C=424.
\tag{18}
$$
这些是实际 $H_+$ 的次数；原 $H$ 与 $G$ 的四次 gcd 已经排除，不能在旧 $U$ 上使用 (18)。

**引理 2。** $k(\mathscr A,\mathscr C)=k(t)$。

**证明。** 可在代数闭包后计算有限曲线映射的次数。记
$e=[k(t):k(\mathscr A,\mathscr C)]$。由两个塔式次数，
$$
e\mid\gcd(1700,424)=4.
\tag{19}
$$
因 $2$ 可逆，这个扩张可分。两个函数共同零点的准确赋值对为
$$
\begin{array}{c|c}
\text{点}&(v(\mathscr A),v(\mathscr C))\\ \hline
a=0\text{ 的四点}&(21,6)\\
H_+=0\text{ 的重数 }j\text{ 点}&(89j,22j)\\
\infty&(14,4).
\end{array}
\tag{20}
$$
令 $P$ 为 $\infty$ 在中间曲线上的像。其分歧指数 $e_\infty$ 同时整除 $14,4$，故为一或二。

若 $e_\infty=1$，则 $v_P(\mathscr A,\mathscr C)=(14,4)$。表中没有别的点的赋值对是此对的正整数倍，故该纤维只有 $\infty$，纤维次数给 $e=1$。

若 $e_\infty=2$，则 $v_P(\mathscr A,\mathscr C)=(7,2)$。表中只有 $a$ 的根可能成为其他纤维点，所需分歧指数为三；但它与 $\infty$ 已贡献 $2+3=5>e$，违反 (19)。所以该纤维仍只有 $\infty$，给 $e=2$。

只须排除后一种情况。令 $d=0$ 处 $G$ 的重数为 $j\ge1$；其极点赋值对为
$$
(-68j,1-17j).
\tag{21}
$$
其他 $G$ 根的极点对为 $(-68h,-17h)$，两分量的比恒为四，而 (21) 的比不为四。因此 $d=0$ 在其中间纤维中也是唯一一点。

若 $e=2$，非平凡 deck involution 必须固定 $\infty$ 和 $-1/8$。特征不为二，故它只能为
$$
\tau(t)=-t-\frac14.
\tag{22}
$$
它还须保持 (20) 中的 $(21,6)$ 位置，于是把 $a$ 的四点互相置换。但
$$
\tau(0)=-1/4,\qquad a(-1/4)=35/16\in R^\times,
$$
矛盾。这里额外删除的素数五正是在 (9) 中支付的。故 $e=1$。$\square$

再置
$$
\eta=W^{13}/U_+^{17}.
$$
整数恒等式 $89\cdot13-68\cdot17=1$ 给
$\eta=\vartheta\,r(t)$，其中 $r(t)\ne0$。指数矩阵
$$
\begin{pmatrix}89&-68\\-17&13\end{pmatrix}
$$
的行列式为一，所以
$$
k(U_+,W)=k(\mathscr A,\eta),\qquad
k(S,U_+,W)=k(\mathscr A,\mathscr C,\eta)=k(t,\vartheta).
\tag{23}
$$
$\eta$ 在 $k(t)$ 上超越，故
$$
\boxed{[k(t,\vartheta):k(U_+,W)]=1700.}
\tag{24}
$$
这同时证明 $U_+,W$ 代数独立，且 $S$ 生成 (24) 的全部扩张。整个证明在每个允许剩余域有效，不要求 $G$ 或 $H_+$ 的所有根简单。

## 5. 一个实际固定导子及整返回

记
$$
P=R[U_+,W],\qquad A_0=R[S,U_+,W]=R[S,U,W].
$$
第 3 节使 $S$ 在正规多项式环 $P$ 上整；第 4 节给其最小多项式的准确次数。因此唯一的 monic 最小式为
$$
\boxed{
\Psi(U_+,W;Z)\in P[Z],\qquad
\deg_Z\Psi=1700,\qquad\Psi(U_+,W;S)=0.}
\tag{25}
$$
其系数属于 $P$：它们在 $P$ 上整且位于 $\operatorname{Frac}P$，而 $P$ 正规。按原权伸缩并用 monic 唯一性，
$$
\operatorname{wt}\Psi=1700\cdot17=28900.
\tag{26}
$$
因此
$$
A_0\simeq R[u_+,w,Z]/(\Psi),\qquad
H_{A_0}(q)=\frac{1-q^{28900}}
{(1-q^{17})(1-q^{68})(1-q^{89})}.
\tag{27}
$$
这是一条确切关系的定义，不是未界定的“足够大关系”。例如，消去 $t$ 的两式
$$
u_+^{89}G(t)^{68}-w^{68}a(t)^{21}H_+(t)^{89}=0,
$$
$$
7Z\,u_+^{22}G(t)^{17}-w^{17}a(t)^6d(t)H_+(t)^{22}=0
\tag{28}
$$
在 $\mathbf Q(u_+,w)$ 上给同一最小式；取其 monic 最小因子并使用 (25) 的整性，恢复唯一 $\Psi$。也可直接从第 3 节的有限模求 $S$ 的乘法最小式。没有必要打印或保存这个大多项式。

定义
$$
\boxed{
c_+=\Psi_Z(U_+,W;S)\in(A_0)_{28883}.}
\tag{29}
$$
导数是在保持两个 Noether 参数 $U_+,W$ 不变时对 $Z$ 取的；代回 $U_+=U+S^4$ 之后，不能误换成对原 $S$ 的全导数。其准确权为
$28900-17=28883$。

**定理 3。** 对每个 $m\ge0$，
$$
\boxed{c_+B^+_m\subset(A_0)_{m+28883}
\subset A^+_{m+28883}.}
\tag{30}
$$
这是在固定整模型 $R$ 上成立的包含，不增加任何随 $m$ 增长的分母素数。

**证明。** $A_0$ 在 $P$ 上的基为
$1,S,\ldots,S^{1699}$。令 $\ell$ 为最后一个系数的泛函。配对
$(x,y)\mapsto\ell(xy)$ 的矩阵为反三角、反对角为一，因此整且完美。设 $K=\operatorname{Frac}P$，$L_0=K(S)$。对 monic 可分式的 Lagrange 插值给
$$
\operatorname{Tr}_{L_0/K}(x)=\ell(c_+x),\qquad x\in L_0.
\tag{31}
$$
该等式也可先对幂基逐项核定，再线性推广。

取 $b\in B^+$ 与 $a_0\in A_0$。二者都在 $P$ 上整，所以
$\operatorname{Tr}(ba_0)$ 在 $P$ 上整且属于 $K$，从而属于 $P$。
由 (31)，$\ell(c_+ba_0)\in P$ 对每个 $a_0$ 成立。完美配对遂给
$c_+b\in A_0$。全程保齐次权，得到 (30)。$\square$

对每个 $R$ 的剩余域，(24) 仍为 $1700$，所以 (25) 的 monic 约化仍是最小式，给
$$
A_0/pA_0\hookrightarrow B^+/pB^+.
\tag{32}
$$
又 $p\nmid1700$（$2,5,17$ 均已删除），故导数的最高项
$1700Z^{1699}$ 非零；次数小于最小式，保证
$\bar c_+\ne0$ 于整环 $B^+/pB^+$。

此外，$c_+B^+$ 在 $A^+$ 中为 $p$-饱和子模。确实，若
$c_+b=pa$，$a\in A^+$，先在 $B^+/pB^+$ 中用 $\bar c_+\ne0$ 得
$b=pb_1$，再约去 $p$ 得 $a=c_+b_1$。这个论证无需先宣称整个
$A^+/pA^+$ 已嵌入 $B^+/pB^+$。它也不声称实际截断 jet 的像饱和。

## 6. 全次数、系数范数与原全纯来源成本

(11) 的完整显示基是
$$
b_{m,j}=\vartheta^m a^{k_m}t^j,\qquad
k_m=\lceil m/89\rceil,\quad
0\le j\le\lfloor29m/89\rfloor-4k_m.
\tag{33}
$$
定理 3 的返回表达只需原 $S,U,W$，且可选成原权齐次。于是普通总次数有确定上界
$$
\boxed{
\deg_{S,T,U,W}(c_+b)\le
\left\lfloor\frac{m+28883}{17}\right\rfloor.}
\tag{34}
$$
把 $U_+$ 换回 $U+S^4$ 保权；其中最小生成元权仍为十七，所以没有把参数替换的次数免费忽略。

返回系数也可控制为
$$
\|\operatorname{return}(c_+b)\|_1
\le C^{m+1}\|b\|_{\rm basis}
\tag{35}
$$
的形式，$C$ 为固定常数，$\|b\|_{\rm basis}$ 是 (33) 的系数 $\ell^1$ 范数。以下给具体有限构造。

第 3 节在 $R[U_+^{89},W^{68}]$ 上给有限基生成集合 $\mathcal G$，其中权不超过 $12113$。再取 $B^+_L$ 的 $D+1$ 个显示单项式
$\rho,\rho t,\ldots,\rho t^D$。对每个该单项式与每个 $g\in\mathcal G$ 的乘积，预选一次由 (15) 给出的整来源表达。这是固定有限乘法表，系数属于同一个 $R$，且保权；不随 $m$ 求越来越大的逆矩阵。

任意 (33) 可按 (14) 写为一个固定有限剩余权基元素与至多 $O(m)$ 个 $B^+_L$ 单项式的乘积。具体地，若 $q_r\ge0$ 从 $n=0$ 开始，若 $q_r<0$ 从 $n=1$ 开始；允许的 $t$ 次数恰可分成一个初始次数与若干个 $0,\ldots,D$ 中的次数。逐次查上述有限表，系数范数每次至多乘固定常数。最后，对有限多个 $c_+g$ 预选 (30) 在 $A_0$ 中的整表达。由此得到 (35)。换回 $U+S^4$ 所产生的二项式系数也至多指数增长，吸收入同一 $C$。

把角多项式展开为 $t^n$ 后，总有
$$
n\le\lfloor29m/89\rfloor<m/3\qquad(m>0).
$$
所以原实际函数中
$$
\boxed{\Theta^m t^n=(-1)^n\sigma^{6n}\Theta^{m-3n}}
\tag{36}
$$
的所有幂指数都非负。每个 (33) 因此仍是原 $\mathcal S_{2m}$ 中的真正全纯来源，并由原 $\sigma,\Theta$ 的整测度作有限乘法得到有界整测度。其原点阶至少为 $6\lceil m/89\rceil$。这里没有测度反卷积，也没有给这些乘积赋中央零。

同 R473 的原增长估计，存在固定常数使
$$
|b(w)|\le C_1^{m+1}\|b\|_{\rm basis}
\exp(C_2m|w|^{1/3}),\qquad w=z^6.
\tag{37}
$$
因此 Cauchy 优化的主项仍按同一原权支付，返回增加固定偏移与 $O(m)$ 系数成本。

为计入实际形式 jet 的固定平移，将
$$
c_+=\Theta^{28883}q_+(t).
$$
由 (11) 与 (29)，
$$
q_+\in a^{325}R[t],\qquad \deg q_+\le9411.
$$
它非零，故
$$
\boxed{325\le\operatorname{ord}_{t=0}q_+\le9411.}
\tag{38}
$$
这给原 $w$-jet 的固定非零首阶范围。若要作普通 Amice 坐标中的单位三角运输，还须像 R473 §5.1 一样删除该固定首项的分子、分母素数，或保留其真实赋值；惰性处的阶乘、Gaussian、原公共单位及 carry 仍不能由 (38) 删除。

## 7. 真实增长改善及它没有替代的原门

从 (11) 得
$$
\operatorname{rank}_R B^+_m
=\max\{0,\lfloor29m/89\rfloor-4\lceil m/89\rceil+1\}.
\tag{39}
$$
由 $A_0\subset A^+\subset B^+$ 与 (30) 的固定权平移，
$$
\dim_k A^+_m=\frac{25}{89}m+O(1),\qquad
\sum_{j\le m}\dim_k A^+_j=\frac{25}{178}m^2+O(m).
\tag{40}
$$
相较 R473 的 $9/34$ 与 $9/68$，线性、累积主项分别增加
$49/3026$ 与 $49/6052$。这是同一二变量函数域中来源空间的真实扩大，没有把第四生成元当成第四个代数独立变量。

R943 的 $W\notin B_{89}$ 结论原封保留；本篇给的是新增环的 $B^+$，并已支付其独立的有限整性和权 $28883$ 导子。不能把它不付成本地代入旧 $B$ 或旧完整评价矩阵。

本篇允许在 (11) 的完整来源格中构造候选后，按 (30)、(34)、(35) 整地返回原四源。若要由五条原中央同时消失控制这个扩大后的全部来源，仍需同一实际测试映射与完整深核的证明；中央泛函不具有所需的乘法性。原 306 维几何、完整除子及 shadow 的运行也未因此得到新的 PASS。

### 7.1 全部五个真实来源的同一规范化

为免漏掉原第四个算术来源，另记它为 $V_{66}$，与 (1) 中 $T$ 的六次角因子 $V$ 区分。
[R821 §1(3)—(7)](R821-original-four-central-axes-and-complete-four-block-carries.md) 已完整给出
$
V_{66}=\vartheta^{33}\frac{a d^2(4t-1)(-1+228t-48t^2+64t^3)}7,
\qquad \deg f_{V_{66}}=10.
$
该次数是十；原 sigma 表达的常数系数为零，不能误取为十一。
这条旧结论不重做。由 (11) 直接有
$
B^+_{33}=\vartheta^{33}aR[t]_{\le6},\qquad V_{66}\in B^+_{33}.
$
于是全部五个真实来源的环
$
A^{(5)}=R[S,T,U,V_{66},W]
$
满足 $A^+\subset A^{(5)}\subset B^+$。第3节的有限生成集合仍生成 $B^+$ 作为
$A^{(5)}$ 的模，全函数域不变，所以其完整规范化也恰为 $B^+$。
同一个已证明的导子满足
$
c_+B^+_m\subset(A_0)_{m+28883}\subset A^{(5)}_{m+28883}.
$
第5节的剩余域非零与 $p$-饱和证明逐字适用，第6节的原 $S,U,W$ 返回及全部成本也不变。
上下夹住各权空间，(40) 的两个真实 Hilbert 主项同样适用于 $A^{(5)}$。
这是对已知第四来源的完整纳入；不产生第六个自由中央条件，也不把
$V_{66}$ 或 $c_+V_{66}$ 的乘法关系解释为中央泛函的乘法性。

## 8. 可重现的公开回执

唯一 reader 为
[check-original-e89-angular-profile.py](../scripts/check-original-e89-angular-profile.py)，参数为空；它在同 job 内调用
[check-r943-degree178-full-cm-source.py](../scripts/check-r943-degree178-full-cm-source.py)
的 --workers=4，固定 python-flint 0.9.0。完整 CM 矩阵哈希固定为
6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665。
原 CM producer 的 SHA256 为
b5c2e3f6781e1a788e2d3fd749f10e2ecab9e6c58e2950aecc9acf727f237e67。

| 检查 | Source commit | Run / job | 实际输出 |
|---|---|---|---|
| 原四点及旧参数 | d2856ef101891f008ef125d219468a226903bace | 45773031338 / 139749954422 | 四点与 $d$ 均简单；$\deg\gcd(H,G)=4$ |
| 同环参数替换 | f9c9f614ea40a699e26a765b480aa51022830d1f | 45773737555 / 139752282740 | $c=0$ 度四，$c=1$ 度零；完整 Bézout 与 resultant 通过 |

首次 reader SHA256：
e30590582a6ff26761bebd879133d9f139cdf99c1009eba0d65e4fdd3476aa36。
首次 stdout 为 2025 bytes，SHA256：
a19ba0f2e4aaa541468a901bb8d7687677b22419f45ee89e5c80fae6b34e4e43。
首次完整日志 UTF-8 保 BOM 为 15083 bytes，SHA256：
e66fdbf91c8eeb4c704bc6abffeb254c039b6c75073d46efa877be82f268a267。

第二次 reader SHA256：
483e259dc60b9778404ae68be4e632cf6e6166b4c71f1879d7951afd3b5a2229。
第二次 stdout 为 3051 bytes，SHA256：
47e60f4436fb873b805b24ea41856f2f9052a6818154e87498c8ca5ba6e10d70。
第二次完整日志 UTF-8 保 BOM 为 16174 bytes，SHA256：
971c33d36dd6a5785ea045674fa86ff360c768266e0f9793968caba978a37dff。

两次共同的原系数规范字符串 SHA256 为
2615abc0aff959f74d81660a681e33a57d6a10a5bd6d6c09268ab088de9d49ac；
完整 $f_W$ 角系数规范 JSON 的 SHA256 为
7fbad6a6407c938654454c0c6c1fb8e221e02dfeab73b8fd55d192d76a045adb。
这些系数只在运行内存中重生。

$\operatorname{Res}(a,G)$ 的确切有理数字符串 SHA256 为
30943e5bdbf01df1cbf3bd49b1a521ae571d8a5619a34e6648dacaa384e67a38
（分子 272 bits、分母 23 bits）。
$\operatorname{Res}(H_+,G)$ 的确切有理数字符串 SHA256 为
b65bd1ec9cdfa4755e6416b5e5698d4fbd641b9c5657406bd1c31654259b0bac
（分子 1951 bits、分母 457 bits）。
包含全部 $H_+,G$ 和两个 Bézout 乘子的规范 JSON SHA256 为
5845e05ef1e2284ad9e6092d74fe143d2a0d1aee1c57f8958f724482a96ff562。
reader 在记录该 hash 前回乘全部系数，核定和恰为一。

只提交源、参数、run 与哈希；没有保存 CM 矩阵、系数表、Bézout 表、resultant 展开或日志。第 3—6 节的有限整性、函数域与导子论证是显示证明，有限计算只负责 (4)—(7) 的固定实际输入。
