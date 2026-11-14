# 有界二阶头行列式、最大闭分式与半阶根的定义域界线

日期：2026-11-12（UTC）。独占作者：critical_kernel。
状态：以下实际 Schur 等价、闭分式接口和抽象定义域障碍均已证明。
按根代理安排，本稿是 R143 的独立补充，不另占结果号。

## 1. 有界最低位分解

考虑有界二阶实际乘子，减去可能的核参数后写成

$$
S=C+Y_0B,\qquad C,B\in\mathcal A_2
=\overline{\mathbb C[I,A^2]},
\tag{1.1}
$$

其中 $B$ 是一个非零的有界一阶尾乘子。
这里 $C$ 可以是任意有界尾代数元素，不要求它也是一阶。

对通常二阶 Walsh 写法

$$
X_f=H+V_0Z,\qquad
Z=X_{a_0+\sum_{j>0}b_{0j}\chi_j},
$$

若 $X_f$ 有界，R92先给 $f\in L^\infty$；物理首位条件期望及差
给有界尾符号，再由R92得到有界的 $H,Z$。
一阶有界性迫相应行属于 $\ell^1$。取

$$
C=H+Z-\lambda I,\qquad B=-2Z
$$

便得 (1.1)。此处只处理有界二阶版本；
没有对任意无界尾块直接写 bounded Schur 行列式。

R125 给非零 $B$ 在全 $H$ 上单射、值域稠密。
因 $B,C$ 属于 $\mathcal A_2$，在最低物理位分解
$H=\mathbb C^2\otimes\widehat H$ 中它们在头上为恒等。
下文用同一记号表示对应尾算子。

真实归一化头矩阵为

$$
N_0=
\begin{pmatrix}0&t\\I&0\end{pmatrix},
\qquad t=\eta_0\widehat N_1.
\tag{1.2}
$$

$t$ 为有界单射、稠密值域、拟幂零尾算子，且与 $B,C$ 交换。
直接计算

$$
Y_0=(I-t)^{-1}
\begin{pmatrix}-t&t\\I&-t\end{pmatrix}.
$$

因此乘以实际有界单位 $I-t$ 后，

$$
(I-t)S=
\begin{pmatrix}P&tB\\B&P\end{pmatrix},
\qquad P=(I-t)C-tB.
\tag{1.3}
$$

记

$$
\Delta=P^2-tB^2,\qquad L=\ker\Delta\subseteq\widehat H.
\tag{1.4}
$$

所有块在尾代数中交换；本稿的行列式是这个实际交换块矩阵的恒等式。

## 2. 平方差核与原核的精确关系

令 $M=\ker S$。

若 $(x,y)\in M$，则

$$
Px+tBy=0,\qquad Bx+Py=0.
\tag{2.1}
$$

交换消元给 $\Delta x=\Delta y=0$，所以 $x,y\in L$。

反向，对任意 $u\in L$，

$$
\boxed{
(Pu,-Bu)\in M,\qquad
(tBu,-Pu)\in M.
}
\tag{2.2}
$$

由 $B$ 单射，第一条映射 $u\mapsto(Pu,-Bu)$ 单射。
因此得到真正的核等价

$$
\boxed{\ker S=0\quad\Longleftrightarrow\quad
\ker(P^2-tB^2)=0.}
\tag{2.3}
$$

(2.3) 没有使用 $B^{-1}$ 的有界性。

还有一个必须准确解释的形式事实：相对于尾变量 $A^2$，
$t$ 的形式阶为1。若 $P$ 的首阶为 $p$、$B$ 的首阶为 $b$，
则 $P^2$ 的阶为 $2p$，$tB^2$ 的阶为 $1+2b$；二者奇偶不同。
因此 $\Delta$ 是非零的尾代数元素（$P=0$ 时亦然）。
这个事实仅排除全空间算子恒等式 $P^2=tB^2$，
并不排除非零 $\ker\Delta$，所以不能代替 (2.3) 所剩的核问题。

### 2.1 最大闭商参数式

令

$$
J=B^{-1}P,\qquad
\operatorname{Dom}J
=\{y\in\widehat H:Py\in\operatorname{Ran}B\}.
\tag{2.4}
$$

$B^{-1}$ 只定义在 $\operatorname{Ran}B$ 上。
该最大算子闭：若 $y_n\to y,Jy_n\to x$，则
$Bx=\lim BJy_n=\lim Py_n=Py$，从而 $y\in\operatorname{Dom}J$、
$Jy=x$。此外

$$
\operatorname{Ran}B\subseteq\operatorname{Dom}J,\qquad JB=P.
\tag{2.5}
$$

故 $J$ 稠密定义，因为 $B$ 全空间值域稠密。

若 $y\in L\cap\operatorname{Dom}J$，则
$B\Delta Jy=P\Delta y=0$，由 $B$ 单射得 $Jy\in L$。
式 (2.1) 给完整参数式

$$
\boxed{
M=\{(-Jy,y):y\in L\cap\operatorname{Dom}J\}.
}
\tag{2.6}
$$

验证反向时第二式自动成立；将第一式左边乘以 $B$ 后得到
$-\Delta y=0$，再用 $B$ 单射即可。
没有把一个仅必要的 Schur 方程误写成充分条件。

### 2.2 两个投影的闭包与尚未得到的稠密性

两个头投影在 $M$ 上都单射。
事实上 $(x,0)\in M$ 时 $Bx=0$；
$(0,y)\in M$ 时 $tBy=0$；
$t,B$ 的单射性均已建立。

R143 的真实 $A$ 不变图论证给

$$
K:=\overline{P_0M}=\overline{P_1M}\subseteq L.
\tag{2.7}
$$

也可直接使用
$A=\begin{pmatrix}0&B_{\rm shift}\\\alpha_0I&0\end{pmatrix}$：
两个投影闭包均为尾移位不变，
$\alpha_0P_0M\subseteq P_1M$、
$B_{\rm shift}P_1M\subseteq P_0M$，
尾移位在每个不变限制上值域稠密，故两个闭包相同。

由 (2.2) 还得到

$$
\boxed{
\overline{BL}\subseteq K\subseteq L,\qquad
\overline{PL}\subseteq K.
}
\tag{2.8}
$$

一般不能把 (2.8) 的第一个包含升级为 $K=L$：
$B$ 的全空间稠密值域并不自动给 $\overline{BL}=L$。

## 3. 一个使最大闭商具有图核心的充分条件

假设 $B$ 具有以下严格的有限放大性质：

> 对每个有限 $d$ 和每个闭尾移位放大不变空间
> $\mathcal M\subseteq\widehat H^{\oplus d}$，
> $\overline{B^{(d)}\mathcal M}=\mathcal M$。

R140 的全有限放大结论提供这样的分母类，
包括适用的真实快尾一阶乘子。
若从原 $A$ 的有限放大结论转到尾模型，
可把 $\mathcal M$ 提升成最低头的两个相同副本：
R143中真实的头矩阵作用保持这个提升，
而 $B$ 在两个头副本上作用相同。
因此无需假设任意正交压缩保留有限放大性质。

### 3.1 $K=L$

$L$ 是闭尾移位不变空间，上述性质给
$\overline{BL}=L$。由 (2.8)，

$$
\boxed{K=L.}
\tag{3.1}
$$

此时 $J_L:=J|_{L\cap\operatorname{Dom}J}$ 是 $L$ 上闭、
稠密定义的算子；其值域也在 $L$ 中。
它单射：若 $Jy=0$ 且 $y\in L$，则 $Py=0$，
继而 $tB^2y=P^2y=0$，所以 $y=0$。

### 3.2 全尾最大商的图核心

$J$ 的图

$$
\mathcal G_J=\{(y,Jy):y\in\operatorname{Dom}J\}
$$

闭且为尾移位的二次放大所不变。
其不变性直接来自 $B,P$ 与尾移位交换及 (2.4)。

有限放大性质给
$\overline{B^{(2)}\mathcal G_J}=\mathcal G_J$。
又

$$
B^{(2)}(y,Jy)=(By,BJy)=(By,Py),
$$

所以

$$
B^{(2)}\mathcal G_J
\subseteq\{(Bu,Pu):u\in\widehat H\}
\subseteq\mathcal G_J.
$$

故

$$
\boxed{
\operatorname{Ran}B\text{ 是全尾最大闭商 }J
\text{ 的图核心}.
}
\tag{3.2}
$$

相同论证对 (2.6) 的核图给
$\operatorname{Ran}(B|_L)$ 是 $J_L$ 的图核心。
这是真正的图范数结论，不仅是普通范数下的域稠密。

### 3.3 全尾的 $C$ 自伴性

记尾共轭为 $\widehat C$。因 $B,P$ 属于尾范数代数，

$$
B^*=\widehat C B\widehat C,\qquad
P^*=\widehat C P\widehat C.
$$

先令 $J_0$ 为 (2.5) 在 $\operatorname{Ran}B$ 上的限制：
$J_0(Bu)=Pu$。由伴随的定义，

$$
y\in\operatorname{Dom}J_0^*
\Longleftrightarrow
P^*y\in\operatorname{Ran}B^*,\qquad
J_0^*y=(B^*)^{-1}P^*y.
$$

因 $B^*$ 单射，此值唯一。因此

$$
J_0^*=\widehat C J\widehat C.
$$

(3.2) 给 $\overline{J_0}=J$，遂有

$$
\boxed{J^*=\widehat C J\widehat C.}
\tag{3.3}
$$

这只证明**全尾**最大商的 $C$ 自伴性。
不自动有 $\widehat C L=L$，故不能把 (3.3) 直接限制成
$J_L$ 的某个 $C$ 自伴性结论。

若没有本节有限放大稠密假设，(2.4) 仍给最大闭商，
但本稿没有证明 $\operatorname{Ran}B$ 是其图核心，
也没有把它列入 R135 已建立的解析分式域。

## 4. 平方关系的最大版本与自然域版本

仍在 §3 的假设下。
对 $u\in L$，$B^2u\in\operatorname{Dom}J_L^2$，且

$$
J_L(B^2u)=BPu,\qquad
J_L^2(B^2u)=P^2u=tB^2u.
\tag{4.1}
$$

对任意 $y\in\operatorname{Dom}J_L^2$，同样由有界等式得到

$$
B^2J_L^2y=P^2y=tB^2y.
$$

$B^2$ 单射，所以

$$
\boxed{J_L^2y=ty
\quad(y\in\operatorname{Dom}J_L^2).}
\tag{4.2}
$$

其自然定义域包含 $B^2L$；后者在 $L$ 中稠密。
于是

$$
\boxed{\overline{J_L^2}=t|_L.}
\tag{4.3}
$$

证明：自然平方的图包含有界算子 $t|_L$ 在稠密子域 $B^2L$ 上的图，
且由 (4.2) 包含于它的全图。取闭包即得。

(4.3) 不等于 $\operatorname{Dom}J_L^2=L$，
也不允许推出 $J_L$ 有界。
闭算子的自然平方未必闭，这里必须保留闭包记号。
下一节给一个直接的抽象反例，说明即使再加 $C$ 自伴也不能省略这一步。

## 5. 严格的抽象平方障碍

取任意 Hilbert 空间 $H_0$ 上有界、单射、值域稠密、
拟幂零的 $Q$，并取共轭 $C_0$ 使 $Q^*=C_0QC_0$。
例如可取本课题实际 $A$，但本节随后使用其无限放大，
并不宣称它是本题某个未知不变限制。

令

$$
\mathscr K=\bigoplus_{n\ge1}(H_0\oplus H_0),\qquad
t_{\rm ex}=\bigoplus_{n\ge1}
\begin{pmatrix}Q&0\\0&Q\end{pmatrix}.
$$

定义

$$
J_{\rm ex}(x_n,y_n)_{n\ge1}
=(ny_n,n^{-1}Qx_n)_{n\ge1},
$$

$$
\operatorname{Dom}J_{\rm ex}
=\left\{(x_n,y_n)\in\mathscr K:
\sum_{n\ge1}n^2\|y_n\|^2<\infty\right\}.
\tag{5.1}
$$

它是一个无界闭算子：第一分量是闭对角算子，
第二分量是有界算子；有限块向量给稠密域。
$Q$ 单射给 $J_{\rm ex}$ 单射；
第一像分量可任取 $\ell^2$ 向量，
第二像分量包含有限块的 $n^{-1}\operatorname{Ran}Q$，
因此像稠密。

定义共轭

$$
\mathscr C(x_n,y_n)=(C_0y_n,C_0x_n).
$$

直接计算伴随及其域：

$$
J_{\rm ex}^*(x_n,y_n)
=(n^{-1}Q^*y_n,nx_n),\qquad
\operatorname{Dom}J_{\rm ex}^*
=\left\{\sum_n n^2\|x_n\|^2<\infty\right\}.
$$

故

$$
J_{\rm ex}^*=\mathscr C J_{\rm ex}\mathscr C.
\tag{5.2}
$$

此外 $J_{\rm ex}$ 把自己的域映入自身：
输出第二分量乘以 $n$ 后是 $(Qx_n)$，属于 $\ell^2$。
于是自然平方的域恰为原域，且

$$
J_{\rm ex}^2=t_{\rm ex}
\quad\text{在 }\operatorname{Dom}J_{\rm ex}\text{ 上},\qquad
\overline{J_{\rm ex}^2}=t_{\rm ex}.
\tag{5.3}
$$

$t_{\rm ex}$ 有界、单射、稠密、拟幂零；
$J_{\rm ex}$ 与它含域交换，且 $J_{\rm ex}$ 仍无界。

还可令

$$
T_{\rm ex}=\sqrt{\alpha_0}\,J_{\rm ex}^{-1}.
$$

它闭、单射、稠密定义且值域稠密，包含定义域的交换关系为
$T_{\rm ex}t_{\rm ex}=t_{\rm ex}T_{\rm ex}$，
并且对每个 $x\in\operatorname{Dom}T_{\rm ex}$，

$$
t_{\rm ex}T_{\rm ex}x\in\operatorname{Dom}T_{\rm ex},
\qquad
T_{\rm ex}t_{\rm ex}T_{\rm ex}x=\alpha_0x.
\tag{5.4}
$$

这可直接由 $x=J_{\rm ex}v$、
$J_{\rm ex}\operatorname{Dom}J_{\rm ex}\subseteq
\operatorname{Dom}J_{\rm ex}$ 和 (5.3) 验证。

因此，闭性、$C$ 自伴性、单射稠密、与有界拟幂零尾交换，
乃至 R143 形式的准确 $TtT$ 域方程，
都不能单独迫使图算子有界或核空间为零。

本节不是实际 $A$ 的不变子空间构造：
$t_{\rm ex}$ 是明确的无限放大，
没有证明它可在本题未知尾不变子空间上实现；
也没有给本题的二阶 $B,P$ 产生这个例子。

### 5.1 高位 WOT 标量极限本身也不能去掉这个障碍

还可以把 $Q$ 选成本题的实际尾权移，使用它的相应归一化高位幂。
若 $Q_{j,F}$ 是任意固定有限高位积的归一化算子，则

$$
Q_{j,F}\xrightarrow{\mathrm{WOT}}2^{-|F|}I,
\qquad \sup_j\|Q_{j,F}\|<\infty.
$$

其无限放大在 $\mathscr K$ 上仍满足完全相同的 WOT 极限。
证明时先把两个测试向量截到有限多个 $n$ 块，在有限块上逐个使用
原极限，再用一致范数界控制两个截断余项。
继续作任何有限放大也保留该极限。
R23 的一致有界强近似单位同样可传到这个无限放大。

所以即使把 R140 使用的全部固定高位 WOT 标量极限、
它们在有限放大中的版本及强近似单位，一并加入闭图方程，
这里的无界 $J_{\rm ex},T_{\rm ex}$ 仍然存在。
要排除本题实际核，仍须用真实一阶分母、二阶分子或原表示的额外结构；
上述极限单独不包含所需的域或乘法刚性。

## 6. 对当前临界行问题的含义

(2.3) 给的是完整的实际平方差核等价；
(2.6) 给最大闭分式的准确域。
若分母 $B$ 有 R140 的全有限放大稠密性质，
则进一步有 $K=L$、全尾商的图核心与 $C$ 自伴性。

剩余问题不是形式恒等式本身，
而是如何利用**本题真实二阶来源**排除
$L=\ker(P^2-tB^2)\ne0$。
即便 $J$ 的最大闭商已经 $C$ 自伴，
其在未知 $L$ 上的限制也未必继承该结构；
自然平方与平方闭包之间仍有严格域差别。

一般慢第一行缺少 §3 的有限放大稠密性质。
本稿没有为它假定图核心，也没有用形式指数的奇偶性排除
未证明属于特定解析分式域的闭算子。

