# R587 — 惰性最小极点原函数与原 Gaussian 连接的准确 p 曲率

日期：2026-11-14。**状态：已证明。**

本篇在原 $b=17$ 曲线上给第一类微分的唯一 $L(pO)$ 有理原函数，
准确比较 R356 的原点正则参数，并计算同一 Gaussian 连接的全局
$p$ 曲率及单位首项。短对数连接确可下降，但全部 Frobenius 修正仍在；
原 Gaussian theta 连接的曲率非零，不能因 $D^p=0$ 而当成水平有理来源。
本文没有证明 R586 两指定系数非零或原中央非零。

## 1. 原规范与最小极点原函数

取 $p=6s-1>71$、$b=17\bmod p$，完美剩余域 $k$ 包含 $\mu _6$。
记
$$
E_b:y^2=x^3+b,\qquad \omega_E=\frac{dx}{2y},\qquad
Dx=2y,\quad Dy=3x^2 .
\tag{1}
$$
$O$ 是原点。沿用
[R356](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)
的原 Cartier 常数与已证明的等式
$$
c_p=\binom{3s-1}{2s-1}b^s\in\mathbf F_p^\times,\qquad
\mathcal C(\omega_E)=0,\quad \mathcal C(x\omega_E)=c_p\omega_E,
\quad D^p=0,\quad D^{p-1}(-x)=c_p.
\tag{2}
$$

定义
$$
t_0=\frac1{2b},\qquad
t_j=-\frac{6j-1}{(6j+2)b}t_{j-1}\quad(1\le j<s),
$$
$$
T_p(x)=\sum_{j=0}^{s-1}t_jx^{3j+1},\qquad Z_*=yT_p(x).
\tag{3}
$$
显示分母均为 $p$ 单位，且各 $t_j\ne0$。直接求导给
$$
D(yx^{3j+1})=(6j+5)x^{3j+3}+(6j+2)b x^{3j}.
\tag{4}
$$
(3) 使所有相邻项抵消；首项为 $2bt_0=1$，
末项为 $(6s-1)t_{s-1}x^{3s}=0$。所以
$$
\boxed{DZ_*=1,\qquad Z_*\in L(pO),\qquad (Z_*)_\infty=pO.}
\tag{5}
$$
极阶恰为 $p$，因为最高非零项 $t_{s-1}yx^{3s-2}$ 的极阶为
$3+2(3s-2)=p$。

其最高系数准确为
$$
\boxed{t_{s-1}=c_p^{-1}.}
\tag{6}
$$
证明如下。由 $6s=1$，换元 $l=s-j$ 得
$$
\prod_{j=1}^{s-1}\frac{6j-1}{6j+2}
=\prod_{l=1}^{s-1}\frac{2l}{2l-1}
=\frac{4^{s-1}}{\binom{2s-2}{s-1}}.
$$
又
$$
\binom{3s-1}{s}
=\prod_{j=1}^s\frac{3s-j}{j}
\equiv \frac{(-1)^s}{4^s}\binom{2s}{s}.
$$
与 (3) 相乘后，
$$
t_{s-1}c_p=-\frac18
\frac{\binom{2s}{s}}{\binom{2s-2}{s-1}}
=-\frac{2s-1}{4s}=1,
$$
其中最后一步仍用 $6s=1$。

取原点参数 $u=x^{-1/2}$ 和原支
$y=-u^{-3}\sqrt{1+bu^6}$。由 (5)–(6)，
$$
\boxed{Z_*=-c_p^{-1}u^{-p}+O(u).}
\tag{7}
$$
确实，$D=(\sqrt{1+bu^6})\,d/du$，
$DZ_*=1$ 排除了所有其他负幂；型 $+1$ 排除常数。

**唯一性。** (3) 的 $\mu _6$ 型为 $+1$。
若另有同型 $Z_1\in L(pO)$ 满足 $DZ_1=1$，则
$Z_1-Z_*\in\ker D=k(E_b)^p$。
此核等式来自一变量函数域的 $p$-基：
$[k(E_b):k(E_b)^p]=p$，而 $D\ne0$。
差的 $p$ 次根属于 $L(O)=k$，所以差为常数；
型 $+1$ 迫其为零。

## 2. 与原正则参数的完整 Frobenius 差

R342/R356 的实际原点正则参数是
$$
\mathscr R_p(x)=\frac12\sum_{j=0}^{3s-1}
 \binom{3s-1}{j}b^{3s-1-j}\frac{x^{3j+1}}{3j+1},
\qquad Z=\frac{\mathscr R_p(x)}{y^p}.
\tag{8}
$$
分母均为 $p$ 单位。原文已付 $DZ=1$ 及
$Z=z+O(u^{5p})$；这里 $z$ 只指原形式对数在已付整窗口内的约化，
不将它当成全局有理函数。

置 $r=x^2/y$。整个原函数域中准确有
$$
\boxed{Z_*-Z=c_p^{-1}r^p.}
\tag{9}
$$
乘 $y^p$ 后，分子为
$$
Q(x)=(x^3+b)^{3s}T_p(x)-\mathscr R_p(x),\qquad \deg Q\le2p .
$$
因 $D(Q/y^p)=0$，有 $Q'(x)=0$，故 $Q\in k[x^p]$。
$Q$ 的 $\mu _6$ 型为 $4$；可能的 $1,x^p,x^{2p}$ 中，
只有 $x^{2p}$ 为此型。其最高系数为 $t_{s-1}=c_p^{-1}$，即得 (9)。

另一个有用的整个函数域等式为
$$
\boxed{D^{p-2}(-x)=c_pZ_*.}
\tag{10}
$$
由 (2)，左端除以 $c_p$ 的导数为一，型为 $+1$，
且属于 $L(pO)$；第 1 节的唯一性给出 (10)。

(9) 说明 $Z_*$ 不能直接代入原正则测试：
一个在 $O$ 有极，一个在 $O$ 正则，必须保留完整的 Frobenius 差。

## 3. 原 Gaussian 连接的整个 p 曲率

保持 R356 原 sigma 归一，其实际有理比较函数为
$$
G_\sigma=\sum_{i=0}^{p-2}
 \frac{(-1)^iZ^{i+1}D^i(-x)}{(i+1)!},
\qquad DG_\sigma=-x+c_pZ^{p-1}.
\tag{11}
$$
原文完整支付了它与原 Gaussian 正则化 $\zeta_\sigma$ 在
$z^{5p-2}$ 之前的比较以及唯一 $z^p$ 共振的归一。

对 (11) 再求 $p-2$ 次导数，Wilson 等式、(9)–(10) 给
$$
\begin{aligned}
D^{p-1}G_\sigma
&=D^{p-2}(-x)+c_p(p-1)!Z\\
&=c_p(Z_*-Z)=r^p .
\end{aligned}
\tag{12}
$$
这是全局有理等式，不只是原点的低阶计算。

允许 R356 的全部整 Gaussian 重标
$$
G_\kappa=G_\sigma-\delta Z^p,\qquad \delta\in k.
\tag{13}
$$
仍有 $D^{p-1}G_\kappa=r^p$。令 $H_\kappa=G_\kappa+r$。
对任意 $n\in\mathbf F_p$，同一个秩一连接
$\nabla_D=D-nG_\kappa$ 的准确曲率为
$$
\boxed{\psi_p(\nabla)(D)=-nH_\kappa^p.}
\tag{14}
$$
这里 $D^p=0$，所以没有额外的 $\nabla_{D^{[p]}}$ 项。
所用 restricted-power 恒等式是
$$
(D-a)^p=D^p-D^{p-1}a-a^p.
$$
可直接证明：与任一乘法算子的交换子表明左边减 $D^p$ 是乘法算子；
在 $1$ 上的微分乘积展开，按 $p$ 个位置的循环平移归并集合分拆。
非固定轨道有 $p$ 项而消失；固定分拆仅全单点和单一整块，
分别留下 $-a^p$ 与 $-D^{p-1}a$。取 $a=nG_\kappa$ 便得 (14)。

所有 (13) 都有
$$
\boxed{
H_\kappa=\frac{3b}{5}z^5+O(z^{11}),\qquad
\operatorname{ord}_O\psi_p(\nabla)(D)=5p\quad(n\ne0).
}
\tag{15}
$$
首系数为 $-n(3b/5)^p\ne0$。确实，原展开给
$$
G_\sigma=z^{-1}+\frac b{35}z^5+O(z^{11}),\qquad
x=z^{-2}-\frac b7z^4+\cdots,\qquad
y=-z^{-3}-\frac{2b}{7}z^3+\cdots,
$$
从而
$$
r=-z^{-1}+\frac{4b}{7}z^5+O(z^{11}).
$$
两者相加给 $3b/5$，而 $\delta Z^p$ 从 $z^p$ 起。
亦可由准确式
$$
DH_\kappa=\frac{3bx}{y^2}+c_pZ^{p-1}
\tag{16}
$$
读出同一首项。

特别 $n=6$ 正是 R586 两个实际 forcing 的 sigma 次数。
曲率非零，所以此连接在 $k(E_b)$ 中没有非零水平解。
在任意有限可分扩张中也没有：$D$ 唯一延伸，$D^p$ 仍为零，
而 (14) 作用于一个非零水平解会给矛盾。
这没有将特征零 sigma 整体约化；它明确排除了由短窗口比较
免费得到全局水平代数化的做法。

## 4. 短对数连接的下降与全部修正

若 $N$ 是定义在 $\mathbf F_p$ 上的常矩阵，
$N^{q+1}=0$、$q<p$，则实际 unipotent 对数连接满足
$$
(D-N)^p=0,\qquad
\mathcal U_*=\sum_{j=0}^q\frac{N^jZ_*^j}{j!},
\qquad D\mathcal U_*=N\mathcal U_* .
\tag{17}
$$
因此它的 $p$ 曲率确为零。用 $Z$ 定义 $\mathcal U$，则 (9) 给
$$
\boxed{\mathcal U_*=\mathcal U\,
 \exp(Nc_p^{-1}r^p).}
\tag{18}
$$
指数是终止于 $q$ 的有限和。最后一矩阵是一个矩阵的逐项 Frobenius 像，
但在比较原点及实际测试点时仍须保留各项。
$\mathcal U_*$ 的条目在 $O$ 可有至多 $qp$ 阶极，
所以此下降没有免费支付原固定来源预算。

对任意有理微分 $\eta$、$0\le j<p$，准确的 Cartier 比较是
$$
\boxed{
\mathcal C(Z^j\eta)=
\sum_{i=0}^j\binom ji(-c_p^{-1})^{j-i}r^{j-i}
\,\mathcal C(Z_*^i\eta).
}
\tag{19}
$$
将 $(Z_*-c_p^{-1}r^p)^j$ 作有限二项式展开，再用
$\mathcal C(f^p\eta)=f\mathcal C(\eta)$ 即得。
特别 $j=2,5$ 的求和不能截成只有 $i=j$ 的一项。
含原 Gaussian theta 的形式微分也不能未经证明当成有理微分；
(14)–(15) 给出了对应的明确曲率障碍。

## 5. 特征零提升的真实首整商

将 (3)、(8) 的同一有理系数提升到 $\mathbf Z_{(p)}$，
记为 $\widetilde Z_*,\widetilde Z,\widetilde t=t_{s-1}$。
保留 (4) 的末项，精确得到
$$
\boxed{D\widetilde Z_*=1+p\widetilde t\,x^{3s}.}
\tag{20}
$$
另一原参数仍满足 R356 的
$$
D\widetilde Z=1-3p\frac{x^2\mathscr R_p(x)}{y^{p+1}}.
$$
由 (9)，下式是指定的整有理函数：
$$
\mathcal B_p=
\frac{\widetilde Z_*-\widetilde Z-\widetilde t\,r^p}{p}
\in\mathbf Z_{(p)}[x,y,y^{-1}]/(y^2-x^3-b).
\tag{21}
$$
整性可乘 $y^p$ 后由第 2 节的多项式恒等式逐系数核定。
直接求导，得到完整的下一位
$$
\boxed{
D\mathcal B_p=
\widetilde t\,x^{3s}
+3\frac{x^2\mathscr R_p(x)}{y^{p+1}}
-\widetilde t\,r^{p-1}\frac{x(x^3+4b)}{y^2}.
}
\tag{22}
$$
三个实际项全部保留。若用于 R356 (29) 或 R577/578 的同一修正，
还须运输原 frame、原预算及完整 carry；
模 $p$ 的 (9) 不能升级为模 $p^2$ 的无修正等式。

## 6. 当前实际边界

R586 的指定首 forcing 为
$$
c_4=[z^{p-1}](x\sigma^6),\qquad
c_1=[z^{p-4}](-xy\sigma^6).
$$
它们处于首个 Gaussian 之前的整窗口。
本文没有将 (15) 的高阶曲率首项换成这两个系数，
也没有证明两者联合非零。

新增的已证输入为唯一最小极点原函数、原参数的整个 Frobenius 差、
原 Gaussian 连接的全局非零曲率及单位首项、
短对数下降的全部求和，以及指定特征零首整商。
继续原系数和原完整评价矩阵时必须保留这些修正；
$D^p=0$ 不给整个 theta 连接零曲率，更不支付原中央非零。

全部论证对每个允许的 $p$ 统一成立，未增加目标素数扫描。

