# R790 增补 — 移动常数项、两个原短块长度与实际因子 Schur 类

日期：2026-11-15。**状态：本增补的完整原首次提升和实际因子转置已证明；指定全左对的非零、原同一个修正的下一位及主目标仍未完成。**

本增补覆盖 R792/R797 尚未排除的零常数 charge 分支。
基准因子可有 $G(t,0)=H(t)$，包括 $H(0)=0$；不把它换成常数 $1$，
也不把原 $q=Y\widetilde q$ 换成存在性分类中的 scalar mask。
同时保 $r=2$ 的两个合法长度 $\ell=1,2$：
后一长度必须多保原第三块的一条实际行，不能沿用只有一个第三行的矩阵。

新增内容是这两个范围的同源接合。R790 已付的 $\ell=1,G(t,0)=1$ 公式作为特例保持；
本增补没有重新声称已判定那个指定余类。

## 1. 原对象与不得投影的两个单位

保持
$$
p=12h+11=6s-1>101,\qquad s=2h+2,\qquad
r=2,\quad k_{\rm carry}=0,\quad \ell\in\{1,2\},\quad
h>13,\quad f_D<p,
$$
$$
P^{\rm fact}=t^2\widetilde q\,\widetilde F^{\,3}
\in\mathcal W_D,\qquad
F(0,1)=0,\quad (\mathcal EF)(0,1)q(0,1)\ne0,
\quad \operatorname{ord}_tF(t,\bar\rho)=h.
\tag{A1}
$$
这里 $\widetilde q$ 是原余因子的整提升，不以其零次 $Y$ 系数替代。
$F$ 是原几何整因子，$C$ 是同一十九角曲面 $X$ 上的严格变换。
令 $\kappa=C^2$、$\chi=-K_XC$。

在 R792/R797 的实际 $b_0=m_F=3$ 范围，可写
$$
F(t,0)=\lambda d^cH(t),\qquad
G=F/(\lambda d^c),\qquad
\mathfrak q=\lambda^3d^{3c}q,\qquad d=1+8t.
\tag{A2}
$$
原来源准确仍是 $t^2\mathfrak qG^3$。
$q(t,0)\ne0$ 时 $H=1$；$q(t,0)=0$ 时
$$
q=Yq^\circ,\quad q^\circ(0,Y)\in k^\times,\qquad
\deg H\le2,
$$
且 $H(0)$ 允许为零。
以下全部矩阵保 $H$ 的真实低系数；没有除以 $H$。
尤其
$$
Q(0)=\mathfrak q(0,1)\ne0
$$
与可能为零的 $\mathfrak q(t,0)$ 是不同的量。

沿 R790 的同一个原低轴和换参，置
$$
N=s-13=2h-11,\qquad L=N-h=h-11>0,
$$
$$
\rho=d\exp\!\left(\sum_{n\ge1}
 \frac{17}{3n}\frac{(1/3)_n}{(5/6)_n}t^n\right),
\quad
\mathcal H(t)=\sum_{n\ge0}
\frac{\binom{2n}{n}}{4^n(6n+1)}t^n,
\quad w=-t\mathcal H^6.
\tag{A3}
$$
所有使用位置严格低于 $s$；这段 $\rho$ 是原 regularized $g$ 的实际有理前缀，
按原整环读取模 $p^2$。
完整 $b_s=(t/w)^s$ 在这些 $<p$ 位置约化为 $\mathcal H^{-1}$；
不在原全目标中删除 $H^{-p}$。

定义
$$
e=(\mathcal E\bar G)(t,\bar\rho),\qquad
V=t^{-h}\bar G(t,\bar\rho),\qquad
Q=\bar{\mathfrak q}(t,\bar\rho)
\pmod{t^L},
$$
$$
B_h=\overline{\frac{\pi_{<h}G(t,\rho)}p},\qquad
\mathcal B=\frac{Q_0e_0V_0^2}{a}\in k^\times.
\tag{A4}
$$
除 $p$ 只作用于已知可除的低前缀，除 $t^h$ 只在真实接触验证后进行。
$B_h$ 由同一给定整因子计算，不是可自由选择的高轴。

R790 引理1的证明只用 $F_Y(0,1)\ne0$、真实接触及同一低轴，
并未使用 $G(t,0)=1$。因此在本范围仍有
$$
u=V/e\pmod{t^L},\qquad e\xi=B_h\pmod{t^{L-2}}.
\tag{A5}
$$
$H(0)=0$ 不影响原点 $(0,1)$ 处的单位 $e_0$。

## 2. 完整 forcing 与 ell=2 的原第二条第三块行

定义
$$
T_{\rm nor}=
\frac{t^hQ}{a}\bigl(\mathcal H^{-1}V^3+
6at^2eVB_h\bigr)\pmod{t^N},
$$
$$
\boxed{\mathcal C_\ell=
\frac6a\,\mathcal H^{-1}QeV^2\pmod{t^\ell}.}
\tag{A6}
$$
第一普通块的首商为零，第一 Gaussian 块仍是
$aT_{\rm nor}$。
第三块的完整原物理首商为
$$
\boxed{
3a\,w^{13}\mathcal H(t(w))^{-1}
Q(t(w))e(t(w))V(t(w))^2
\pmod{w^{13+\ell}}.}
\tag{A7}
$$

**证明。** 使用 R755 的完整展开。第一 Gaussian 块的 $C_4$、
$\mathcal E q$ 及二次 normal 项从 $2h$ 起，超过 $N$；
native 项精确是 $6at^{h+2}QeVB_h$，不投影 $q$。
第三块的 native 项含 $t^r=t^2$，在两个 $\ell\le2$ 窗口均不可见；
所有含 $C_4$ 的项至少从 $t^h$ 起。
唯一留下的是 $3ab_s q_Ce_C^3u^2$。
在 $<\ell<h$ 中可用原实际轴值替换曲线值，再用 (A5)，得到 (A7)。
这里没有把第三块的 $w^{13}$ 改写成 $t^{13}$。$\square$

第一、第二块的原不可除初始十三行和第三块的 $w^{<13}$ 行均为零，
理由与 R790 相同且不涉及 $G(t,0)$。
仅在这个已经证明的共同像内，用
$w^{13}f(t(w))\mapsto f(t)$ 选第三块坐标，并除单位 $a^2/2$，
才得到 (A6) 的 $\mathcal C_\ell$。
对 $\ell=1$ 它是 $6\mathcal B$；
对 $\ell=2$ 必须保其整个一次项。

## 3. 同一个 R 的全部原列及完整余列矩阵

对原基
$$
\Phi_{n,j}=Y^nq_n(t)t^j,\qquad
0\le n\le D,\quad 0\le j\le e_{n+1},
$$
置 $c(n,j)=q_n\bar\rho^nt^j$。
逆整个 $c_*U_0$、按原共同 charge 作完整三角居中后，
同一个原矩阵在上述共同像上的准确坐标为
$$
\boxed{
\mathsf A^{(\ell)}(R)=
\bigl(R(t,\bar\rho)\bmod t^N,\
(\mathcal ER)(t,\bar\rho)\bmod t^N,\
(\mathcal E^2R)(t,\bar\rho)\bmod t^\ell\bigr).
}
\tag{A8}
$$
每条列准确是 $(c,nc,n^2c)$，三个截断长度分别为 $N,N,\ell$。
所有 $q_n$ 高尾及原帽均保留。

因此准确有
$$
\boxed{
M(P^{\rm fact}+pR)\in p^2
\iff
\mathsf A^{(\ell)}(R)=(0,-T_{\rm nor},-\mathcal C_\ell).
}
\tag{A9}
$$
这里的整个 $M$ 仍是 $c_*U_0w^{13}J$。
没有从相对 $J$ 的 $p^2$ 必要条件偷换到 (A9)。

三条常数行仍是原 $n=0,1,2$ 的单位 Vandermonde；
它们给
$$
R(0,Y)=-3\mathcal B(Y-1)^2.
$$
保原完整列
$$
Q_2=1-2Y-(1+9t)q_2Y^2
=(Y-1)^2-\frac{9t^2Y^2}{d},
\qquad q_2=(t-1)/d,
$$
并写
$$
R=-3\mathcal BQ_2+Z,\qquad
Z\in W_D^{(1)}=\bar{\mathcal W}_D\cap t\,k[t,Y,d^{-1}].
$$
这个子格仍使用 R790 的全部原列，不限于 $F^2$ 整除子格。
(A9) 等价于同一个 $Z$ 的
$$
\boxed{
\begin{aligned}
Z(t,\bar\rho)&=3\mathcal BQ_2(t,\bar\rho)\pmod{t^N},\\
(\mathcal EZ)(t,\bar\rho)
&=3\mathcal B(\mathcal EQ_2)(t,\bar\rho)-T_{\rm nor}
 \pmod{t^N},\\
(\mathcal E^2Z)(t,\bar\rho)
&=3\mathcal B(\mathcal E^2Q_2)(t,\bar\rho)-\mathcal C_\ell
 \pmod{t^\ell}.
\end{aligned}}
\tag{A10}
$$
第三右端的常数为 $6\mathcal B-6\mathcal B=0$。
$\ell=1$ 时第三式已空；$\ell=2$ 时它是一条必须保留的真余行，
并与前两式使用同一个 $Z$。

## 4. 移动 H 的真实因子格及合法点归一

使用 R491/R495 的同一整截面格
$$
\boxed{
\mathscr H_1=H^0(X,\mathcal O_X(C)),\qquad
\mathcal A_C=(\lambda d^c)^{-1}\mathscr H_1.
}
\tag{A11}
$$
这里是**零阶截面空间**，不是第一上同调 $H^1$。
在整模型上按原全部十九个累计角条件取有限自由格；
其来源饱和由 R491/R495 保持，不推出物理评价像饱和。

$\mathcal A_C$ 含同一个 $G$。
不假设常数 $1$ 在其中，亦不固定或丢弃它允许的零次 $Y$ 系数。
对于当前 $G(t,0)=H$，这些正是移动 $H$ 必须保留的实际低列。
$\mathcal E$ 逐 charge 乘整数，保全部角条件和帽，所以
$$
\mathcal EG\in\mathcal A_C,\qquad
(\mathcal EG)(0,1)\in\mathcal O^\times.
\tag{A12}
$$

若需 $G(0,1)=0$ 的整点归一，可合法取
$$
G_*=G-\frac{G(0,1)}{(\mathcal EG)(0,1)}\mathcal EG .
\tag{A13}
$$
该系数在 $p\mathcal O$ 中，故约化和同一曲线 $C$ 不变。
而 $\mathcal EG(t,0)=0$，所以 (A13) **保持原整个 $H(t)$**，
包括 $H(0)=0$ 的情形。
这没有在格中加入常数 $1$，更没有令整个 $B_h$ 为零。

任意 $A\in\mathcal A_C$ 都有真实同预算返回
$$
\boxed{3t^2\mathfrak qG^2A\in W_D^{(1)}.}
\tag{A14}
$$
证明是全部十九个角的逐项乘法：$A$ 的角值不低于 $G$ 的对应值，
径向帽不超过 $b$，所以乘积不超原 $t^2\mathfrak qG^3$。
它的系数含 $t^2$。全部混合项
$t^2\mathfrak qG^{3-j}A^j$ 也按同一个理由返回。

若改变整因子为 $G+pA$，必须把
$$
R\longmapsto
R-\frac{t^2\mathfrak q(G+pA)^3-t^2\mathfrak qG^3}{p}
\tag{A15}
$$
同时运输。右侧分子在原整格中可除 $p$，
其完整商由上述混合来源支付。
(A15) 保持 $P^{\rm fact}+pR$ **整式相同**，
故加同一个 $p^2T$ 后也保全部第三精度，
不是为各块另选修正。

## 5. 强窗中较小真格的一维接触核与准确 Schur 商

定义同一有限整矩阵
$$
\mathsf C_h^C:\mathcal A_C\longrightarrow\mathcal O[t]/t^h,\qquad
A\longmapsto A(t,\rho)\bmod t^h.
\tag{A16}
$$
若
$$
\boxed{h>\kappa,}
\tag{A17}
$$
则
$$
\boxed{\ker\bar{\mathsf C}_h^C=k\bar G.}
\tag{A18}
$$
在再加入第 $h$ 行后，矩阵满列秩且有单位最大子式。

**证明。** 因 $\psi\equiv\rho\bmod t^h$，
(A16) 的模 $p$ 零向量在 $C$ 上给 $N=\mathcal O_C(C)$ 的截面，
并在原光滑点 $P$ 消至少 $h$ 阶。
$\deg N=\kappa<h$，故这个截面为零。
原限制序列的核是 $kF$，运输后即 (A18)。
再加入第 $h$ 行，它在唯一核向量上的值为 $V_0\ne0$，
所以秩增加一。$\square$

此结论只针对 (A11)。
它不把整个五型、六十四型或更大 profile 的接触核也认作一维；
那些格仍用 R795/R802 的准确交数门。

为完全指定整商，取 $\mathcal A_C$ 的整基，以给定 primitive $G$ 为第一列；
记 (A16) 为 $(c,B)$。
$B$ 模 $p$ 满列秩，可取其单位最大子式行集 $I$。置
$$
\boxed{\Delta=c-BB_I^{-1}c_I\in p\,\mathcal O[t]/t^h.}
\tag{A19}
$$
$\Delta_I=0$。因 $c=\pi_{<h}G(t,\rho)$，
$$
\boxed{\beta_{\mathsf C^C}(\bar G)=[B_h]=[\Delta/p]
\quad\text{于 }\operatorname{coker}\bar{\mathsf C}_h^C.}
\tag{A20}
$$
矩阵有 $\operatorname{rank}\mathcal A_C-1$ 个单位 Smith 因子；
最后一因子的指数是 $\min_i v_p(\Delta_i)$，
若 $\Delta=0$ 则为零因子。
没有由下一行单位猜这个指数恰为一。
(A19) 是同一个给定因子的实际 Schur 缺陷，不重新选择 $H$ 的系数。

## 6. 两个短长度的全余列左对与唯一原配对

令 $(\lambda_0,\mu,\tau)$ 分别作用于
$t\,k[t]/t^N$、$t\,k[t]/t^N$、$t\,k[t]/t^\ell$，
并对 (A10) 的**每条完整原余列**满足
$$
\boxed{
(\lambda_0+n\mu+n^2\tau)
(q_n\bar\rho^n t^j)=0.
}
\tag{A21}
$$
其原指标仍为 $n=0,1,2$ 时 $j\ge1$，$n\ge3$ 时 $j\ge0$，
全部保原 $e_{n+1}$ 帽。
当 $\ell=1$ 时第三空间为零，$\tau=0$。
在写常数项时统一以零延拓这些泛函。

定义
$$
\nu(f)=\mu(6t^{h+2}QeVf).
\tag{A22}
$$
由 (A14)，其普通值从 $2h+2>N$ 起，
第三 Euler 值含 $t^2$，在两个 $\ell\le2$ 窗口均为零；
唯一可见的一阶 Euler 值正是 (A22) 中的乘子。
所以
$$
\boxed{\nu\bar{\mathsf C}_h^C=0.}
\tag{A23}
$$
这逐项支付了转置，包括 $\ell=2$ 的附加第三行；
不是因子格含常数 $1$ 的推论。
$\nu$ 只读严格 $<h-13$ 的前缀。

令
$$
K_n=(\lambda_0+n\mu+n^2\tau)(q_n\bar\rho^n),
\qquad n=0,1,2.
$$
$Q_2$ 中的额外 $9tq_2Y^2$ 是 (A21) 已包含的真实列，
故整个固定主部的配对仍为 $3\mathcal B(K_0-2K_1-K_2)$。
(A10) 在这个全左对上的准确右端为
$$
\boxed{
\begin{aligned}
\mathscr O_{\lambda_0,\mu,\tau}
={}&3\mathcal B(K_0-2K_1-K_2)
-\mu(a^{-1}t^hQ\mathcal H^{-1}V^3)\\
&-\tau(\mathcal C_\ell)
-\left\langle\nu,\beta_{\mathsf C^C}(\bar G)\right\rangle .
\end{aligned}}
\tag{A24}
$$
最后一项可准确用 $\nu(\Delta/p)$ 计算。
若更改在常数项上的延拓，(A24) 的**整个组合**不变；
特别第三常数的变化在 $3\mathcal B\mathcal E^2Q_2$ 与
$\mathcal C_\ell$ 之间相消。

有限线性代数给完整充要条件：
原同一个首次提升 (A9) 可解，当且仅当 (A24)
对全部满足 (A21) 的实际左对为零。
$\ell=1$ 时 (A24) 回到 R790(30)；
$\ell=2$ 时 $\tau$ 项和 (A21) 的 $n^2\tau$ 必须共同保留，
不能只在旧式右端添一条独立观察。

## 7. 范围与接续

本增补没有用 R792/R797 的 scalar 投影替换原 $q$，
没有把 $H(0)$ 当单位，没有固定掉移动 $H$ 的低列，
也没有把较小 $\mathscr H_1$ 的一维核外推到全 profile 或全 $\mathcal W_D$。
原全部非 $F^2$ 余列已经在 (A21) 中。

(A24) 尚未被证明非零或恒零。
通过首次提升后，原两条十三行 carry、
低行右逆高尾、$U_1/p$、同一 $R$ 的完整第二代表及 $p^2T$
仍必须按 R687/R481 联立。
这里没有把 native $B_h$ 设成自由值，
也没有用整来源饱和代替原物理像饱和。

依赖：
[R790](../results/R790-original-cube-full-forcing-and-factor-contact-bockstein-pairing.md)；
[R792](../results/R792-original-nonzero-constant-charge-classification-and-cubic-extension.md)；
[R797](../results/R797-original-zero-constant-charge-moving-factor-and-complete-cubic-gates.md)；
[R491](../results/R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R495](../results/R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R755](../results/R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md)；
[R795](../results/R795-original-factor-contact-one-dimensional-kernel-and-unit-next-row.md)。
