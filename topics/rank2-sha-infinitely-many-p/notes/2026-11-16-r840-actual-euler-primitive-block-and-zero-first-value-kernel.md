# 原 Euler 原函数整块的三长交零与第一法向值为零的完整核

日期：2026-11-16。**状态：下述实际子格的三长交零、整个第一法向值为零分支的同来源呈示，以及它在负纤维上的读取已证明。受限像中的指定总 forcing 仍未判定，主目标未完成。**

本注接 [R836](../results/R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)、[R840](../results/R840-original-double-ramification-euler-image-and-unique-normal-tail.md) 及 [原 Euler 原函数的提升缺陷](2026-11-16-r842-euler-primitive-lift-defect-and-zero-charge-repair.md)。后者已指出：来源上的 Euler 逆不保持原前缀，也不下降到任意法向值商。本注在原三个长块上直接读这个逆的真实像，不使用上述两项未经支付的保持性。

## 1. 同一原格和严格长度

保留原十九角曲面及同一实际因子
$$
C=(F),\quad P=(0,1),\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
N=\mathcal O_C(C),\quad
\kappa=C^2,\quad\chi=-K_XC.
$$
$C$ 几何整，$P$ 光滑，$e=\mathcal EF$ 在 $P$ 为单位，$\mathcal E=Y\partial_Y$ 是原相对 Euler。设
$$
b=\deg_YF,\qquad F_0(t)=F(t,0)\ne0,\qquad 3b<p.
\tag{1}
$$
沿原分支 $Y=\psi(t)$ 写
$$
g(t)=\psi(t)\exp\eta(t),\qquad \operatorname{ord}_t\eta=h.
$$
以下指数只表示所需有限 Taylor 展开；全部分母 $2,3$ 在当前特征中为单位。设
$$
\boxed{
h<T\le2h,\qquad T-h>\kappa,\qquad T>3z_-,
}
\quad
z_-=C.H_-.
\tag{2}
$$
第二个不等式必须严格。它连同 $T\le2h$ 给 $h>\kappa$ 和 $T>2\kappa$，因此也满足 R836 的原三长门。

所有来源已按原返回
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D},
\qquad q_{\rm src}(P)\ne0
\tag{3}
$$
进入同一原矩阵。原物理三个长块的准确长度仍是
$$
\boxed{T=T_M=s-r-13.}
\tag{4}
$$
不以相对 $J$ 的 $s-r$ 替换 (4)。在已经成立的原 $r=2$、$k_{\rm carry}=0$ 强窗，$s=2h+r$、$h\ge\kappa+14$，所以
$$
T=2h-13,\qquad T-h=h-13\ge\kappa+1.
$$
原完整 profile 又有 $z_-\le2$，故 $T>3z_-$。这只说明这些已付强窗满足 (2)，不凭空断言存在这样的因子或首核。

按 R833 的全十九角计算，原 charge 零格准确是
$$
\mathcal H_j^0
=d^{j\mu_{d,1}}k[t]_{\le jz_-},
\qquad d=1+8t.
\tag{5}
$$
特别 $d(P)=1$，非零 $\mathcal H_3^0$ 截面在 $P$ 的阶至多 $3z_-$。原各格按 $Y$ 的非负 charge 分解；$\mathcal E_+^{-1}$ 对正 charge $n$ 逐项除以 $n$。因为 $n\le3b<p$，它保同一原 Gauss 格，全部分母为单位。此处不声称它保物理前缀或原像饱和。

记原实际三长核
$$
K_{3,T}=
\{G\in\mathcal H_3:
G(t,g),\,\mathcal EG(t,g),\,\mathcal E^2G(t,g)
\in t^T k[[t]]\}.
\tag{6}
$$

## 2. 一个新的实际来源整块

定义
$$
\boxed{
\mathcal J
=\mathcal E_+^{-1}\bigl(F^2\mathcal H_1^{>0}\bigr)
\oplus\mathcal H_3^0
\subset\mathcal H_3.
}
\tag{7}
$$
$F^2L$ 对 $L\in\mathcal H_1^{>0}$ 没有 charge 零，且确属 $\mathcal H_3$。两项直和由 charge 零投影得到，不是从物理像中任选补空间。原整 Gauss 提升中的乘法和逐 charge 单位除法也给 (7) 的实际整列。

**定理 1。** 在 (1)–(4) 下，
$$
\boxed{\mathcal J\cap K_{3,T}=0.}
\tag{8}
$$

**证明。** 写
$$
G=\mathcal E_+^{-1}(F^2L)+G_0,\qquad
L\in\mathcal H_1^{>0},\quad G_0\in\mathcal H_3^0.
$$
在原来源环内准确有
$$
\mathcal EG=F^2L,\qquad
\mathcal E^2G=2FeL+F^2\mathcal EL.
\tag{9}
$$
用下标 $C$ 表示同一曲线限制，沿 $g=\psi e^\eta$ 展开。由于 $T\le2h$，
$$
(\mathcal E^2G)(t,g)
=2e_C^2\eta L_C\pmod{t^T}.
\tag{10}
$$
被删各项含 $\eta^2$；所有局部系数在光滑 $P$ 正则，且 $e_C(P)$ 为单位。因此第三长行为零准确迫
$$
\operatorname{ord}_P L_C\ge T-h>\kappa=\deg N.
$$
整射影曲线上次数为 $\kappa$ 的线束不存在这种非零截面，故 $L_C=0$。原限制序列的核是 $kF$，于是 $L=cF$。但 $L$ 的 charge 零为零，而 $F_0\ne0$，所以 $c=0$。

此时 $G=G_0$。第一长行及 (5) 给 $G_0=0$，因为 $T>3z_-$。证毕。

这里第三长行先检测 $L$，第一长行再检测 $G_0$，给一个真实下三角单位块。由 R495 的原 Riemann–Roch 公式，
$$
\boxed{
\dim\mathcal J
=\left(\frac{\kappa+\chi}{2}+1-(z_-+1)\right)
 +(3z_-+1)
=\frac{\kappa+\chi}{2}+2z_-+1.
}
\tag{11}
$$
所以在这个显示子格的任一原整提升上，约化三长评价满列秩，存在相应大小的单位子式。经过 (3) 已付的完整单位下三角运输，同一结论适用于该显示子格的原物理长行。它不允许删去 $w^{13}$ 或把这些列添到另一预算。

尤其不能把 (11) 与 R834 的 $F\mathcal H_2+e\mathcal H_2$ 单位块秩直接相加；联合像的交仍须另证。本注也不宣称 $\mathcal E_+^{-1}$ 保持 (6)。

## 3. 整个第一法向值为零分支

为避免只排一个子格而遗失余核，定义
$$
K_{3,T}^{(1=0)}
=\{G\in K_{3,T}:(\mathcal EG)|_C=0\}.
\tag{12}
$$
这是 R836 的实际唯一伴随 $V_1$ 为零的分支，不是把任意来源的第二个目标自由设为零。

若 $G$ 属于 (12)，原限制序列唯一给
$$
\mathcal EG=F A,\qquad A\in\mathcal H_2.
\tag{13}
$$
取 charge 零得 $F_0A_0=0$。因 $F_0\ne0$，准确有 $A\in\mathcal H_2^{>0}$。定义
$$
I(A)=\mathcal E_+^{-1}(FA)\in\mathcal H_3^{>0}.
\tag{14}
$$
于是所有满足 (13) 的真实来源恰为
$$
G=I(A)+G_0,\qquad G_0\in\mathcal H_3^0.
\tag{15}
$$
没有遗漏整局部补项，且没有使用常规第一上同调来代替截面格。

**引理 2（准确的 $2\eta$ 镜轴）。** 对 (13)–(15)，第三长行等价于
$$
\boxed{
A(t,\psi e^{2\eta})=0\pmod{t^T}.
}
\tag{16}
$$
一旦 (16) 成立，第二长行自动成立。

**证明。** 写 $f_2=(\mathcal E^2F)|_C$，实际乘积法则和有限 Taylor 给
$$
\begin{aligned}
(\mathcal E^2G)(t,g)
&=(eA+F\mathcal EA)(t,g)\\
&=e_C A_C
 +\eta\{2e_C(\mathcal EA)_C+f_2A_C\}
 \pmod{t^T}.
\end{aligned}
\tag{17}
$$
若此式为零，先模 $t^h$ 得 $A_C\in t^h$。于是
$\eta f_2A_C\in t^{2h}\subset t^T$，除以单位 $e_C$ 后恰得
$A_C+2\eta(\mathcal EA)_C=0\bmod t^T$，即 (16)。

反过来，(16) 也先给 $A_C\in t^h$，然后 (17) 为零。再由
$F(t,g)\in t^h$、$A(t,g)\in t^h$，可知
$(\mathcal EG)(t,g)=F(t,g)A(t,g)\in t^{2h}\subset t^T$。证毕。

特别这个 $2\eta$ 是同一个 $F,A,g$ 的实际镜轴。它不等于 R836 中为一般两值修正所需的 $3\eta$，不可互换。

## 4. 唯一 charge 零修正及完整前缀行

对满足 (16) 的 $A$，由于 $(\mathcal EI(A))|_C=0$ 及 $T\le2h$，
$$
I(A)(t,g)=I(A)|_C\pmod{t^T}.
\tag{18}
$$
定义原单位框中的实际轴函数
$$
J_A(t)=d^{-3\mu_{d,1}}\,I(A)|_C\in k[[t]].
\tag{19}
$$
它由整个同来源 $A$ 决定，不能单独选择系数。

由 (5)，第一长行能用 $G_0$ 修正，当且仅当
$$
\boxed{
[t^j]J_A=0
\quad(3z_-+1\le j<T).
}
\tag{20}
$$
若成立，唯一修正是
$$
\boxed{
G_0(A)=-d^{3\mu_{d,1}}\,[J_A]_{\le3z_-}.
}
\tag{21}
$$
因为 $T>3z_-$，(21) 中每个系数都已被原第一长行唯一读出，既无自由常数也无额外尾列。

令
$$
\mathscr A_T=
\{A\in\mathcal H_2^{>0}:
\text{同一个 }A\text{ 满足 (16)、(20)}\}.
\tag{22}
$$

**定理 3（整个零第一值分支）。** 有准确的同来源线性同构
$$
\boxed{
\mathscr A_T\xrightarrow{\sim}K_{3,T}^{(1=0)},
\qquad A\longmapsto I(A)+G_0(A).
}
\tag{23}
$$
该分支的真实第二法向值为
$$
\boxed{
V_2=(\mathcal E^2G)|_C=e_C A_C.
}
\tag{24}
$$
而且 (24) 在 (23) 上单射。

**证明。** (13)–(21) 逐步给出双向构造，$A$ 由 $\mathcal EG/F$ 唯一恢复，故 (23) 为同构。式 (24) 由原乘积法则得到。若 $V_2=0$，整曲线上 $e_C\ne0$，故 $A_C=0$，原限制序列给 $A=FL$、$L\in\mathcal H_1$。由 $A_0=0$ 和 $F_0\ne0$，$L$ 也属正 charge。于是 $G$ 落入 (7)，定理 1 迫 $G=0$。证毕。

因此原全三长核上
$$
G\longmapsto\bigl((\mathcal EG)|_C,(\mathcal E^2G)|_C\bigr)
\tag{25}
$$
也单射：其共同核正是定理 3 中 $V_2=0$ 的情形。这里没有断言第一分量单独单射，更没有给所有 $V_2$ 任意赋值。

(22) 是实际矩阵：其列恰为原 $\mathcal H_2^{>0}$，第一组行是同一 $2\eta$ 镜轴至长度 $T$，第二组行是固定原函数 (19) 的指定系数。全十九角和高尾都在这些列中。它尚未被证明零核或满射，不能把 (23) 当成 forcing 已消失。

## 5. 负纤维读取只剩同一个低 charge 多项式

现在明确加上原 $r=2$、$q_{\rm src}=Y\widetilde q$ 的分支，使用 [完整负纤维 trace](2026-11-16-r842-complete-negative-fiber-trace-and-original-source.md) 的同一有限纤维。设 $Q$ 是非固定负水平点，$t_Q\ne0$，取
$$
x=Y,\qquad F(t_Q,x)=x^\ell u_Q(x),\qquad u_Q(0)\ne0,
$$
并令 $D_Q$ 为同一局部实际 Cartier 纤维，代数为 $k(Q)[x]/x^\ell$。这里的 $\ell$ 是该纤维长度，不是原物理第四短块参数。

因为 $A\in\mathcal H_2^{>0}$，有
$$
(FA)(t_Q,x)\in x^{\ell+1}k(Q)[x].
$$
原 $\mathcal E_+^{-1}$ 只对各 $x^n$ 除以单位 $n\le3b$，故
$$
\boxed{
I(A)|_{D_Q}=0,\qquad
G|_{D_Q}=G_0(A)(t_Q).
}
\tag{26}
$$
这是包含非约化及奇异分支的概形限制，不只读取约化点值。

记 $S_Q(x)=\operatorname{Tr}(1/T_i'(x))$ 为该文的真实 Weierstrass 全分支 trace，$W_Q=W_s(t_Q)$。则本分支的完整负行准确为
$$
\boxed{
b_Q(G)=
-c_s t_Q^rW_Q\,G_0(A)(t_Q)\,
\operatorname{CT}_x
\left\{
S_Q(x)(x\partial_x+1)^2\widetilde q(t_Q,x)
\right\},
}
\tag{27}
$$
对非有理点还取完整剩余域迹。每个 $G_0(A)(t_Q)$ 都是 (21) 中同一个次数至多 $3z_-\le6$ 的多项式在 $t_Q$ 的值，再乘同一原固定因子 $d(t_Q)^{3\mu_{d,1}}$；并不是各纤维可独立指定的值。若相应有限 Jacobian 行为零，(27) 随之为零；本注不把其最高局部单位系数误当作 (22) 的像满射。

在非固定 ramification 的原 $Z^\circ$ 上，(13) 还给
$\mathcal EG=0$、$\mathcal E^2G=0$ 模 $(F,e)$。所以指定原 trace 在这个分支上只读同一
$$
t^r(\mathcal E^2q_{\rm src})G
\tag{28}
$$
的对应 Grothendieck residue。如果 $q_{\rm src}$ 真仅依赖 $t$，该 trace 为零；一般 $q_{\rm src}=Y\widetilde q$ 不能使用这个特例。式 (28) 不删除原固定补零支的边界，也不将 (27) 单独认成整个 trace。

## 6. 原目标、短行和未闭的同来源约束

本注所有实际列都在 (3) 内。原 $P_{134}/U_0$、总 charge 四十及 $q_{\rm src}$ 的 Euler 导数仍由完整单位下三角运输保留。第四短行仍是 R836 的准确长度
$$
\ell_{\rm eff}=\max(\ell_{\rm phys}-r,0),
$$
并读取 (23) 唯一确定的同一个 $G$。原三个十三行 carry、整提升中的更高位和整个 $\mathcal W_D$ 的其它列不得由本注删去。

对真正 $W_T$／三长核上的指定类，(23)–(27) 只是给一个可直接读取的实际分支：它要求同一 $A$ 同时通过镜轴与原函数前缀，并且全部负行共享同一个 $G_0(A)$。正水平、十九角、conductor 和原 $r\le11$ 的准确 $P$ 短尾继续来自同一个 $G$；没有证明这些余行的和非零或为零。

下一步仍须判断 (22) 的实际像及它与其它非零第一值分支的联合关系。特别不能把本注新单位块与旧单位块相加，也不能由来源端的单位积分替换原物理高前缀的饱和条件。

本注仅使用原已付截面序列、十九角 charge 分解和有限 Taylor 恒等；没有新增数值运行。
