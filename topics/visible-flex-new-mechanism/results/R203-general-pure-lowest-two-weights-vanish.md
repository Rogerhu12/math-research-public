# R203：一般 pure 成本的最低两整权恒零与剩余纯闭锥权 −6、−4

日期：2026-11-15。**完整纸面证明；无新的 profile 评价、原式编译或研究消元。** 推导与整理：tail_cost。本文从 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 的真实恢复式重新推导一般动态输入的前两层，保留全部 s 导数、实际 histories、共同右锚与局部端势；对本文结论负责。

## 1. 结论及其准确对象

沿 R105、R130，令 U 为实际同 scalar 常值 germ、frame $I\to I$、$M=T=0$ 的完整 canonical 第四成本的真实线性 span，令 R 为完整第四响应空间。记

$$
\pi V=V_{-4},\qquad
U=\bigoplus_\sigma U_\sigma,\qquad
\mathcal P=\pi(U).
$$

相位下标 $-4$ 与 profile 的真仿射权 $\sigma$ 不同。$\pi$ 始终是任意光滑输入上的一般 pure 算子，不是单个幂尾。

**定理。** 对任一有限光滑、同 scalar 常值端口、frame $I\to I$ 的真实零矩路径 B，不要求其第三算子为零，有

$$
\boxed{\Pi_{-9}\pi V_B=0,\qquad \Pi_{-8}\pi V_B=0.}              \tag{1}
$$

从而

$$
\boxed{\pi(U_{-9})=\pi(U_{-8})=\{0\}.}                          \tag{2}
$$

这些是同一个真实右锚下的完整函数身份。特别，结合 R202 的纯成本闭锥定理，若纯成本闭凸锥仍是真子锥，其非零单整权正仿射字符只可能具有权

$$
\boxed{\sigma\in\{-6,-4\}.}                                   \tag{3}
$$

本文不判定这两个权，不把闭锥结论变成实际有限成本半群的满射，也未支付完整第四 period、ruling 或更高阶。

R85、R88 只证明纯幂尾的最低两项消去；本文没有从那些单输入结果外推 (1)。一般输入的双线性公式在第 3 节直接由 R56 推得。第 8 节另外解释局部窄化阶与真全局权的区别。

## 2. 同右锚窄化与完整恢复规范

固定一条真实路径 $s\in[0,L]$，满足

$$
h>0,\qquad \omega_s=\frac{k_s}{2h}.
$$

先选一个真实合法右端 c，使全路径 $c+\omega$ 有正间隙。令

$$
\xi=c+\epsilon x,\qquad \epsilon>0,\qquad x\le0.
$$

在一个固定紧 x 区间上取任意光滑动态 profiles $\phi(s,x),\chi(s,x)$，它们及全部所需 s 导数在同一个 $x=0$ 右 collar 为零。以下 profile 撇号表示 $\partial_x$；下标 s 表示真实 s 导数。定义

$$
J(F)(x)=\int_x^0F(t)\,dt,\qquad I=-J.
$$

因此在每次使用中保留右端常数：

$$
J(F')=-F,\qquad J^2(F')=-JF,\qquad J^2(F'')=F,                 \tag{4}
$$

其中前两式要求 $F(0)=0$，末式还要求 $F'(0)=0$。本文各次应用中的 F 都是具有该零 collar 的 profile 或其导数、乘积、原函数。

几何量仍按 R56 定义：

$$
z=\xi+\omega,\quad e=hz-k,\quad Q=1+e^2,\quad
\gamma=h_s,\quad
\lambda=\frac{\gamma z-h\omega_s}{h^2},
$$

$$
K_0=kz^2-\frac{k^2+1}{h}z,\qquad K=K_0+\lambda_s.
$$

在未注明时，本稿后面的几何系数均在 $\xi=c$ 求值，$\partial_\xi$ 则先在原几何表达式中求导、再取 $\xi=c$。尤其

$$
e_s=h^2\lambda,\qquad Q_\xi=2he.                              \tag{5}
$$

对任意 R56 forcing H，其真实 scalar 为 W，完整 normal 数据为 P、B，令

$$
\widetilde W=W+\lambda P,\qquad
\psi=W+2Q I_\xi\left(\frac{\eta_0}{hQ}\right),                 \tag{6}
$$

其中 $I_\xi(F)=\int_c^\xi F$。两者都是沿同一实际 history 定义的局部变量，绝不重新指定积分初值。R56 原式准确给

$$
\widetilde W_s
=\frac{T_s}{2h^2}+KP+\frac{K_0}{z}B-\frac{\gamma}{h^2}B_s,     \tag{7}
$$

以及

$$
\boxed{
\psi-\widetilde W
=Q I_\xi\left[
-\frac{T_{s\xi}}{h^2Q}
+\frac{\gamma B_\xi}{h^2Q}
-\frac{P_s}{hQ}
-\left(\frac{\lambda}{Q}\right)_\xi P
\right].
}                                                            \tag{8}
$$

式 (8) 是把 $\lambda P_\xi$ 项准确分部积分后的身份，右端 P 在共同 collar 为零。常值 scalar germs 上 $\lambda=0$，但 $\psi-W$ 内含的 history 导数通常不为零；后文逐项处理它。

## 3. 任意两动态 profiles 的主层、次层原公式

定义三个固定双线性算子

$$
P_*(a,b)=J(a''b''),\qquad
R_*(a,b)=a'b'+xP_*(a,b),\qquad
S_*(a,b)=J^2(a''b'')+xP_*(a,b).                               \tag{9}
$$

为避免与恢复的 P 数据混淆，三个算子在本节保留下标星号。置

$$
f=\frac{Q}{8h^2},\qquad C=\frac{KQ}{8h},\qquad D=\frac{Ke}{4},
\qquad
\mathcal Q_s=(C_\xi-D)R_*+DS_*.                              \tag{10}
$$

$\mathcal Q_s$ 的 s 是其几何系数的标记，不是对算子 Q 再求一次导数。

**双线性引理。** 对 forcing $H(Y_\phi,Y_\chi)$，真实正交 scalar (6) 的前两窄化层为

$$
\psi_s
=\epsilon^{-3}C P_*(\phi,\chi)
+\epsilon^{-2}\{\mathcal Q_s(\phi,\chi)+\mathcal L(\phi,\chi)\}
+O(\epsilon^{-1}),                                           \tag{11}
$$

其中

$$
\boxed{
\mathcal L(\phi,\chi)
=J^2\left[
2f\,\phi_s''\chi_s''
-\bigl((f\phi_s)_s\bigr)'\chi'''
-\phi'''\bigl((f\chi_s)_s\bigr)'
\right].
}                                                            \tag{12}
$$

同一 forcing 的规范差准确为

$$
\psi-\widetilde W
=\epsilon^{-2}\mathcal E(\phi,\chi)+O(\epsilon^{-1}),\qquad
\boxed{
\mathcal E(\phi,\chi)
=-\frac{f_s}{2}\phi'\chi'
-fJ^2(\phi_s'\chi'''+\phi'''\chi_s').
}                                                            \tag{13}
$$

输入可以乘不同的整体 $\epsilon$ 幂；双线性使 (11)–(13) 同时乘相应幂。实际 canonical histories 将在这些一般公式建立后才代入。

### 3.1 直接从原分子算出 P、B 的两层

记 $v=(1,0,e)$、$e_3=(0,0,1)$，本段 v 的几何值在 c。输入分子准确为

$$
V_\phi=-\frac{1}{2\epsilon}v\phi'
+h\left(\phi-\frac{x}{2}\phi'\right)e_3.                       \tag{14}
$$

因此 R56 的 $P=-I_\xi(T_\xi)/(2h)$、$B=J_H/(2h)$ 给

$$
P_H=\epsilon^{-3}\frac{Q}{8h}P_*(\phi,\chi)
+\epsilon^{-2}\frac e8\{\phi'\chi'+2S_*(\phi,\chi)\}
+O(\epsilon^{-1}),                                           \tag{15}
$$

$$
B_H=\epsilon^{-2}\frac{Q}{8h}\phi'\chi'+O(\epsilon^{-1}).        \tag{16}
$$

这里用的是同右锚的准确身份

$$
J(xF)=xJF+J^2F,\qquad
J\bigl((\phi'\chi')'\bigr)=-\phi'\chi'.
$$

例如 (15) 的次项来自
$-eJ(\phi''\chi'+\phi'\chi''-2x\phi''\chi'')/8$。
没有令任何原函数尾值独立或为零。

### 3.2 全部 s 导数给出规范差，而非可丢的局部项

真实 frame 协变导数满足

$$
\nabla_s v=(0,hz,e_s)=:a_v.
$$

所以 $T_s$、$T_{s\xi}$ 的所需首层是

$$
T_s=\frac{\epsilon^{-2}}4
\left[
Q\phi_s'\chi_s'+ee_s(\phi_s'\chi'+\phi'\chi_s')
+\lVert a_v\rVert^2\phi'\chi'
\right]+O(\epsilon^{-1}),                                    \tag{17}
$$

$$
T_{s\xi}=\frac{\epsilon^{-3}}8
\left[
Q(\phi_s'\chi''+\phi''\chi_s')
+ee_s(\phi'\chi''+\phi''\chi')
\right]+O(\epsilon^{-2}).                                    \tag{18}
$$

将 (15)–(18) 代入准确式 (8)。令 $u=Q/(8h)$，原函数 $P_*$ 前面可能出现的额外系数恰为

$$
\frac{u_s}{h}
+\left(\lambda_\xi-\lambda\frac{Q_\xi}{Q}\right)u
=\frac e4\left(\frac{e_s}{h^2}-\lambda\right)=0.               \tag{19}
$$

这是使用真实水平关系 (5) 后的零，不是先冻结 histories。其余时间项使用

$$
J(\phi_s'\chi'')+J^2(\phi_s''\chi'')
=-J^2(\phi_s'\chi''')
$$

及交换后的同式。局部项的系数为
$-ee_s/(8h^2)+\gamma Q/(8h^3)=-f_s/2$，于是得到完整 (13)。

### 3.3 真实密度与规范差导数相加，得到 (11)

再用 $\psi_s=\widetilde W_s+(\psi-\widetilde W)_s$。式 (7) 的 KP 次项给

$$
(C_\xi-D)xP_*+DS_*+\frac D2\phi'\chi'.
$$

式 (17)、(16) 与 (13) 的直接 $\phi_s'\chi'$ 交叉项准确相消。剩余动态项利用

$$
J^2\bigl((\phi_s'\chi_s')''\bigr)=\phi_s'\chi_s'
$$

成为 (12)。

余下静态 $\phi'\chi'$ 系数为

$$
\frac{\lVert a_v\rVert^2}{8h^2}
+\frac{K_0Q}{8hz}
-\frac{\gamma u_s}{h^2}-\frac{f_{ss}}2
=C_\xi-\frac{3D}{2}.                                        \tag{20}
$$

(20) 可由下面两项直接核对：

$$
h^2z^2+\frac{hQK_0}{z}
=hQ(K_0)_\xi-h^2eK_0,\qquad e_s=h^2\lambda.
$$

前式代入 $K_0=kz^2-(k^2+1)z/h$ 后余下
$hz(k+e-hz)=0$；对 $u,f$ 作真实 s 微分后，后式支付全部 $\lambda_s$ 项。故加上 KP 中的 $D/2$，总系数是 $C_\xi-D$，恰得 (10)–(11)。

至此一般 profile 引理完全来自原 R56、真实 frame 导数和同锚分部积分。它并不依赖只在 $t^m$ 上观察到的消去。代入两个动态单项式会恢复 R88 的常数公式，但这里只把它作为一致的解释。

## 4. 为什么真实恢复场的正交余项不影响这两层

由 (6) 的定义，R88 的准确向量分解为

$$
Z_H=-Y_\psi+\frac Fz
\left[
(zP+B)(0,1,0)+\frac{h(\psi-W)}Q(-e,0,1)
\right].                                                     \tag{21}
$$

括号中的余分子准确垂直于 $(1,0,e)$。

若 $\psi$ 从 $\epsilon^j$ 开始，$Y_\psi$ 的分子从 $\epsilon^{j-1}$ 开始，余分子从 $\epsilon^j$ 开始。与另一个主层 $Y_\phi$ 配对时：

- 对 P，profile 微分后的最早交叉项仍在固定首向量 v 上正交，因此其原本可能贡献的次层准确为零；首个贡献再高一层。
- 对 B、$T_s$，没有额外两次 profile 微分，交叉项已高于所需次层。
- 对进入 (8) 的 $T_{s\xi}$，只有一次 profile 微分再一次右积分，交叉项也高于所需次层。
- 两个余分子相乘更高。

真实 s 微分不会降低 $\epsilon$ 阶，因为几何和 history 沿固定 s 路径求导。因此计算第二、第三和第四 scalar 的最低两层时，可以在 (11)–(13) 中使用主 profile $-\,\psi$；这只是准确截断，未把完整余场删掉。所有其余项仍属于实际成本的更高窄化层。

## 5. 真实 canonical 第二、第三 histories

采用与 R85 一致的 pure 规范：

$$
Y=Y_q,\qquad Z_2=\mathcal I H(Y,Y),\qquad
U_3=\mathcal I H(Y,Z_2),
$$

$$
H_4=-\frac1{16}H(Z_2,Z_2)-\frac14H(Y,U_3).                    \tag{22}
$$

q 与 s 无关，但第二、第三 histories 均保留真实 s 演化。以下简记 $P=P_*$、$R=R_*$、$S=S_*$，并置

$$
A=P(q,q),\qquad B=P(q,A),\qquad
\tau=-\frac13J((q'')^3).
$$

展开实际正交 scalars：

$$
\psi_2=\epsilon^{-3}bA+\epsilon^{-2}d+O(\epsilon^{-1}),
$$

$$
\psi_3=\epsilon^{-6}u+\epsilon^{-5}v+O(\epsilon^{-4}),
$$

$$
\psi_4=\epsilon^{-9}w+\epsilon^{-8}z+O(\epsilon^{-7}).          \tag{23}
$$

其中 b 是几何 scalar，d、u、v、w、z 是 q 的真实函数，不被当作独立形式 histories。

式 (11) 给

$$
b'=C,\qquad b(0)=0,\qquad d'=\mathcal Q_s(q,q),\qquad d(0)=0,
$$

$$
u'=-C P(q,bA),\qquad
\boxed{u=-\frac{b^2}{2}B.}                                   \tag{24}
$$

第二、第三式中的负号来自恢复场 (21) 的 $-Y_\psi$。在一般 profile 上，(24) 是算子组成的真实第一积分；不是将一条幂尾的系数平方冒充完整第三场。

### 5.1 第三次层的非零初始规范修正

由 (12)、(4)，

$$
\mathcal L(q,bA)
=-J^2\bigl(q'''((fb')'A)'\bigr)
=(fb')'\tau,
$$

因为 $A'=-(q'')^2$。所以

$$
v'=-C P(q,d)-b\mathcal Q_s(q,A)-(fb')'\tau.
$$

令

$$
\boxed{\bar v=v+fb'\tau.}                                    \tag{25}
$$

则

$$
\bar v'=-C P(q,d)-b\mathcal Q_s(q,A).                          \tag{26}
$$

必须核其初值。初始实际 W3 为零、$\lambda=0$、$f_s=0$，但 $b'(0)=C(0)$ 通常非零。由 (13) 及 forcing 的负号，

$$
v(0)=-f(0)b'(0)\tau,
$$

故恰为 $\bar v(0)=0$。这里完整保留了该初始端势，没有给正交第三 scalar 另置零锚。

## 6. 第四次层的动态项全部成为一个真实端势

定义仅依赖 q 的三个函数

$$
M=J^2((A'')^2),\qquad
N=J^2(A'A'''),\qquad
K_q=J^2(q'''B'),\qquad
G_q=\frac N8+\frac{K_q}{4}.                                  \tag{27}
$$

直接由 (4) 得

$$
M+N=\frac{(A')^2}{2}=\frac{(q'')^4}{2}.                       \tag{28}
$$

另有

$$
\tau''=(q'')^2q''',\qquad
\boxed{P(q,\tau)=-\frac{(q'')^4}{4}.}                         \tag{29}
$$

在第四次层中，把 (25) 代回 $C P(q,v)/4$，并完整保留 (12) 的两次贡献。所需式子是

$$
\mathcal L(bA,bA)=2f(b')^2M-2b(fb')'N,\qquad
\mathcal L(q,u)=(fbb')'K_q.
$$

因此全部动态余项恰为

$$
\begin{aligned}
\mathcal D_4
={}&-\frac{f(b')^2}{4}P(q,\tau)
-\frac{f(b')^2}{8}M
+\frac{b(fb')'}8N
+\frac{(fbb')'}4K_q\\
={}&(fbb')'G_q
-f(b')^2\left\{\frac{M+N}{8}+\frac{P(q,\tau)}4\right\}\\
={}&\boxed{\partial_s(fbb'G_q)}.
\end{aligned}                                                \tag{30}
$$

最后一步用 (28)–(29)。若删除第三次层的 $-fb'\tau$，就会留下一个假的 $f(b')^2$ 项；这正是一般输入版本中必须保留的真实 history 修正。

置

$$
\boxed{\bar z=z-fbb'G_q.}                                    \tag{31}
$$

余下精确方程为

$$
\begin{aligned}
w'={}&-\frac{C}{16}P(bA,bA)+\frac C4P(q,u),\\
\bar z'={}&-\frac1{16}\{2C P(bA,d)+\mathcal Q_s(bA,bA)\}\\
&+\frac14\{C P(q,\bar v)+\mathcal Q_s(q,u)\}.
\end{aligned}                                                \tag{32}
$$

(24)、(26)、(32) 已没有未支付的动态 forcing，但 d、u、$\bar v$ 仍是沿路径的真实积分。

### 6.1 转回原第四 period 的端值

初始 $b=0$、$u=0$，且 $u'=-bb'B=0$。由 (13) 及 (22)，第四规范差的次层仅由

$$
-\frac1{16}\mathcal E(bA,bA)+\frac14\mathcal E(q,u)
$$

给出；每项在初端均为零。因此 $w(0)=z(0)=\bar z(0)=0$。

若总二阶矩阵 M 为零，原第二 scalar 末值是整个零算子。末端 $\lambda=0$，而 (13) 比主层高一层，所以

$$
b(L)P(q,q)=0\quad\text{对所有 q},\qquad \boxed{b(L)=0}.        \tag{33}
$$

不需要使用 d(L) 的值。由 (24)，也有 $u(L)=u'(L)=0$。常值末 germ 给 $f_s(L)=\lambda(L)=0$。再看同一第四规范差，其次层各项都有 $b^2$、$bb'$、u 或 $u'$ 因子，因此末值也为零；(31) 的端势同样为零。故原始 pure 第四成本的两个窄化系数准确为

$$
[\epsilon^{-9}]\pi V_B=w(L),\qquad
[\epsilon^{-8}]\pi V_B=\bar z(L),                             \tag{34}
$$

本式暂按 c 处的缩放输运理解。没有先将内部 b、d、v 置为末值，也没有要求完整第三算子为零。

## 7. 剩余两层的有限代数流与准确零值

这一节只使用一个有限次数的形式系数 ODE，作为 (24)、(26)、(32) 的记账工具；不假设某个新的 profile PDE 有收敛流，更不把它当作实际几何控制。

给每个二次算子 A 配向量场 $X_A(q)=A(q,q)$。使用括号

$$
[X,Y](q)=\mathrm dY(q)[X(q)]-\mathrm dX(q)[Y(q)].
$$

同右锚分部积分直接给

$$
P(q,R(q,q))-R(q,P(q,q))=\tau,
$$

$$
P(q,S(q,q))-S(q,P(q,q))=3\tau.                               \tag{35}
$$

第一式也是 R71 §6 的已付原身份。第二式可用
$S(q,q)'=-x(q'')^2$ 直接算两项之差为 $-J((q'')^3)$。

更关键的是

$$
\mathrm d\tau(q)[P(q,q)]
=-J((q'')^2(P(q,q))'')
=-\frac{(q'')^4}{2}
=2P(q,\tau).
$$

所以

$$
\boxed{[X_P,\tau]=0,\qquad
\operatorname{ad}_{X_P}^2X_R
=\operatorname{ad}_{X_P}^2X_S=0.}                             \tag{36}
$$

这里 (35) 的向量场括号分别是 $-2\tau,-6\tau$；没有省掉极化因子。

令 $\eta^2=0$ 只标记次层，再令 t 标记二次迭代次数。考虑至 $t^3$ 的有限形式方程

$$
F_s=t\{C(s)X_P+\eta X_{\mathcal Q_s}\}(F),\qquad F(0)=q.
                                                                    \tag{37}
$$

逐系数比较 (24)、(26)、(32) 得

$$
[t]F=bA+\eta d,\qquad
[t^2]F=-2(u+\eta\bar v),\qquad
[t^3]F=-16(w+\eta\bar z).                                    \tag{38}
$$

先取 $\eta=0$，(37) 只是同一个二次向量场 $X_P$ 按累计时间 $tb(s)$ 的有限形式流。由 $b(L)=0$，其终值为 q，因此 $w(L)=0$。

再取 $\eta$ 一次项。令 $F=\Phi^P_{tb(s)}(Y)$，其中 $\Phi^P$ 只表示这个有限形式主流。扰动向量场是 $X_{\mathcal Q_s}$ 的 pullback。按本节的括号方向，$\partial_b(\Phi_b^P)^*X|_{b=0}=[X_P,X]$；因为 $\mathcal Q_s$ 逐点属于 $\operatorname{span}(R,S)$，(36) 使共轭级数在一次括号后准确终止：

$$
X_{\mathcal Q_s}+tb(s)[X_P,X_{\mathcal Q_s}].
$$

因为 $\eta^2=0$，右侧在这一层只须作用于 q。最后主流终累计时间是 $tb(L)=0$，所以准确有

$$
F(L)=q+\eta t\int_0^L X_{\mathcal Q_s}(q)\,ds
+\eta t^2\int_0^L b(s)[X_P,X_{\mathcal Q_s}](q)\,ds
\pmod{(t^4,\eta^2)}.
$$

其中没有 $\eta t^3$ 项。因此

$$
[t^3\eta]F(L)=0,\qquad \boxed{\bar z(L)=0}.                   \tag{39}
$$

这项论证可完全放在模 $(t^4,\eta^2)$ 的有限多项式代数中：共轭的二阶系数是 $\operatorname{ad}_{X_P}^2X_{\mathcal Q_s}/2=0$，无需讨论无穷级数或 flow 的实际存在性。它也没有要求 $\int\mathcal Q_s\,ds=0$；零矩的主条件 (33) 已足够。

结合 (34)，在每个真实合法 c 的一般 profile 窄化中，两个系数都为零。

## 8. 局部窄化与真全局整权之间的桥

不能把上一节固定 c 的局部窄化阶直接叫作全局真权。两者在有坐标多项式时不同。

R105 给完整 canonical 成本的 universal 多项式—Volterra 延拓；R190 已证明其真权支撑在 $[-9,3]$，并保留全部实际 histories。令

$$
(T_cV)(q)(x)=V(C_{1,c}q)(x+c),\qquad
C_{\epsilon,c}q(\xi)=q((\xi-c)/\epsilon).
$$

同右锚正仿射输运准确给

$$
V(C_{\epsilon,c}q)(c+\epsilon x)
=(D_\epsilon T_cV)(q)(x),\qquad
D_\epsilon|_{U_\sigma}=\epsilon^\sigma.
                                                                    \tag{40}
$$

因此固定 c 的两个局部系数是

$$
\Pi_{-9}T_c(\pi V_B),\qquad \Pi_{-8}T_c(\pi V_B),
$$

并非未经平移的两权。第 2–7 节在每个足够大的合法 c 上，对所有同右 collar q 都证明它们为零。这里可取任意紧支撑于 $x<0$ 的测试输入，右侧保持共同空 collar；这些输入足以分离所用有限仿射不变真函数空间，因为 [R96](R96-single-profile-faithfulness-for-affine-Volterra-spaces.md) 第 2–3 节的单输入构造可在任意预留开子区间取得 faithful 查询（实输入分离 pure 的极化理由见 R199 第 2 节），所以此处确为算子零。

R105 的平移表示是 c 的有限多项式。故上面两个真实函数空间值多项式在一个开放半轴上为零，必在 c=0 也为零；于是得到 (1)。等价地，可以在已经付清无移动极点的 universal 延拓中直接令 c=0，再以整体缩放读出两权；但这一步是算子延拓，不能冒称每条真实路径上 $\xi=0$ 都物理合法。

这里正是同右锚所需的处理：实际局部计算始终在 $c+\omega>0$ 的区间、以 c 为真实右端；整体输运同时搬动 profile 和右 collar。没有用任意原函数常数填补不合法的零坐标，也没有把仅一个幂尾上的两个零系数当作多项式函数身份。

## 9. 真实 U 的后果与未付范围

对定义 U 的每条实际 $M=T=0$ 成本路径，(1) 成立；线性取 span 后得到 (2)。由于 $\pi$ 与真权投影交换，也可写为

$$
\mathcal P_{-9}=\mathcal P_{-8}=0.
$$

更一般的同端口、frame I、M0 而 T 非零成本也符合本稿：其实际 scalar 递推根本未用 T0。若需要确认它属于 U，R83/R84 的真倒行给
$V_{BB^{\rm rev}}=2V_B$ 且 $M_{BB^{\rm rev}}=T_{BB^{\rm rev}}=0$，故归属已付；这不把倒行当作负成本。

R202 的纯闭锥若为真子锥，则有权 $-8,-6,-4$ 中一个非零正仿射字符。现在 $-8$ 的整个 pure 空间为零，因此排掉这一权，得到 (3)。

本文没有证明 $U_{-8}=0$，也没有证明 $U_{-8}=R_{-8}$：mixed 成本可能仍非零。它没有证明其余所有 pure 成本都在响应像，更没有宣称实际有限路径能同时支付完整纯 period。新结论只把一个完整纯权严格消去，并为后续 $-6,-4$ 的最小原式问题提供准确边界。

