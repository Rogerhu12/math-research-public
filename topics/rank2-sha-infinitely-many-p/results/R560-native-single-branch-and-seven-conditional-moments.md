# R560 — 原 native 全域的单支归一与七个真实条件矩

日期：2026-11-14。**状态：已证明。**

本篇在 R556 的同一个原反对称积分上工作，不另选测试，不限制到
R558 的五深网格。纯 $C$ 三次旋转允许先投影整个来源，再把三条
carry 平均准确约成一条。随后用已经支付的整个 degree $14$ 核，
把原 $n\ge1$ 的受限积分化为 $\beta^n$ 乘一个**与 $n$ 无关**的
五变量积分。其域是两个显示的不交剩余条带；原 $Y/W$ 单位条件、
两个独立的对数和全部其他伴随完整保留。

同一个六次补偿多项式只读取完整 degree $14$ 纤维的七个条件
系数。第六矩的低项校正准确为 $-672b\Omega^6\Lambda_0$。
因此这里给的是原完整混合行的有限表达，不是只给一个边际或
某个非零子域。下述五变量积分的非零仍未证明，主目标未完成。

## 1. 原规范、原测试及待计算的完整行

保 R531、R536、R557 的全部普通射线、固定坏集及大 $p$ 门。
特别 $p\ge71$，$\Omega=\Omega_p$ 是原周期，

$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad\kappa=p\lambda^2.
\tag{1}
$$

原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$，原来源为

$$
\rho_0=-\nu_\sigma^{\otimes6}/84,\qquad
\eta=\omega^2H_*\rho_0,\qquad h=\eta+\rho_0/2,\qquad
\Delta=\rho_0-\eta=\tfrac32\rho_0-h .
\tag{2}
$$

这里的新 $h$ 不是 R536 的旧 $h$。反射 $R_c$ 只改变 $c$ 的符号，
R548 已付

$$
(R_c)_*\rho_0=-\rho_0,\qquad (R_c)_*h=h.
\tag{3}
$$

同一原六行框架为

$$
C=(\xi_1-\xi_3+x)/\delta,\qquad
D=\xi_1+\omega^2\xi_2-2\omega\xi_3+c+(2+3\omega)d_0,
$$
$$
F=D+C,\quad E=F+13C,\quad
G=13(-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x)+(3-2\omega)F.
\tag{4}
$$

$D$ 是 R531 的整数 degree $14$ 行，不能与 R559 的
$D_{12}=F-c$ 混名。完整原观察为

$$
Y=A+c+2d_0,\quad W=A+3\delta c+4d_0,\qquad
A=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,
$$
$$
W'=(4+4\omega)\xi_1+(2+4\omega)\xi_2+(4+4\omega)\xi_3
 +(4+2\omega)c+4d_0.
\tag{5}
$$

记 $\widehat P=\mathcal R_pP_p$，**始终是 R536 (10)–(24) 中
原七行、十列右逆已经选定的那一个多项式**。它的系数允许依赖
$p,\lambda,\kappa$，但不依赖 $n$；本篇没有重新选择右逆。
展开为

$$
\widehat P(T,E,G)=\sum_{k=0}^6P_k(E,G)T^k,\qquad
P_k\in\mathcal O[E,G]_{6-k}.
\tag{6}
$$

令 $\zeta_j=\omega^{2j}$，$D_j=F-\zeta_jC$、
$E_j=F+13\zeta_jC$、$\Gamma_{n,j}=\{C,F\text{ unit},D_j\in p^n\}$。
原整个平均测试正是

$$
q_n=\frac1{3b\Omega^6}\sum_{j=0}^2
 \mathbf1_{\Gamma_{n,j}}\,
 \widehat P(D_j/\kappa^n,E_j,G).
\tag{7}
$$

定义

$$
L=(1+3\omega)c+d_0,\quad
u=\frac{\omega c+(1-\omega)d_0}{2},\qquad
\mathcal B=\{u\in p\mathcal O,\ L\in\mathcal O^\times\},
$$
$$
\ell(Y,W)=(p-1)\left(
 \mathbf1_{Y\text{ unit}}\log\langle Y\rangle
 -\mathbf1_{W\text{ unit}}\log\langle W\rangle\right).
\tag{8}
$$

日志在各自单位域外的对应项取零。始终保留这两个不同的单位
条件；没有免费改成共同域上的 $\log(Y/W)$。

本篇计算的完整量是

$$
\mathcal N_n=
\int_{\mathcal B}
 \{q_n\ell-(q_n\ell)\circ R_c\}\,d\Delta .
\tag{9}
$$

R556 已严格证明原 R544 混合差为

$$
h(\Phi_1-\Phi_2)=\frac{\mathcal N_n}{2\lambda}.
\tag{10}
$$

## 2. 合法的纯 C 投影与完整单支式

设 $S_C=P_{C,\omega}$ 只在实际 $C$ 方向乘 $\omega$，
保持其正交补。由于 $C$ 只涉及前三条有关的第一输入，
且与 $F,G,Y,W,W',c,d_0$ 正交，$S_C$ 保持这些全部线性式。
它与 $R_c$ 交换，并准确循环 (7) 的三支。因此 (9) 的整个
测试函数在 $S_C$ 下不变。

取真正的来源投影

$$
\mathcal P_C=\frac13(I+(S_C)_*+(S_C^2)_*),\qquad
\mu_0=\mathcal P_C\rho_0,\qquad \mu_h=\mathcal P_Ch.
\tag{11}
$$

对任意 $S_C$ 不变连续测试，原来源的积分等于其 (11) 投影后的
积分。这是实际测度等式下的群平均，不是只忘掉 $C$ 后的角型
判断。特别 (9) 可以全程改用 $\tfrac32\mu_0-\mu_h$。
由 (3) 以及交换性，

$$
(R_c)_*\mu_0=-\mu_0,\qquad (R_c)_*\mu_h=\mu_h.
\tag{12}
$$

在投影来源上，(7) 的三条积分相同，$1/3$ 与三相消。
反射项也可独立作同一个循环平均，然后作 $R_c$ 换元。
记 $\mathcal B^c=R_c^{-1}\mathcal B$，于是得到原**整个**积分

$$
\boxed{
\mathcal N_n=\frac1{b\Omega^6}
 \int_{\substack{D\in p^n\\E\text{ unit}}}
 \widehat P(D/\kappa^n,E,G)\,\ell(Y,W)
 \left\{\tfrac32(\mathbf1_{\mathcal B}+\mathbf1_{\mathcal B^c})\,d\mu_0
       +(\mathbf1_{\mathcal B^c}-\mathbf1_{\mathcal B})\,d\mu_h\right\}.
}
\tag{13}
$$

这里使用 $\Gamma_{n,0}=\{D\in p^n,E\text{ unit}\}$。
$\mathcal B^c$ 中的单位条件是 $L\circ R_c$ 为单位，不能误用 $L$。

还可直接核对单支的两个反射支撑在 $\mathcal B$ 内不交：
若 $F-C$ 与 $F-2c-C$ 都深，则 $c$ 深；由 $u$ 深继而 $d_0$
深，与 $L$ 单位矛盾。这一步没有假定 $D_{12}$ 深。
原平均函数逐点可有 R556 的六条交支；(13) 是在完整来源投影
和线性积分之后得到的准确整理，没有把原逐点交支赋零。

## 3. 投影来源仍有整个 D 核

R557 已付 $\rho_0,h$ 沿三个实际 $D_j$ 的完整 scalar 核
$\beta$，包括 $\eta$ 的全部输入、半特征和绝对锚。
$S_C$ 是整单位酉变换，并把 $D$ 循环送到这些 $D_j$；
实际缩放矩阵满足共轭恒等式

$$
S_C^{-1}P_{D,t}S_C=P_{DS_C,t}.
$$

因此对 $\mu=\mu_0,\mu_h$ 仍严格有

$$
\boxed{
\mu|_{\{D\in p^n\}}=\beta^n(P_{D,\kappa^n})_*\mu,\qquad n\ge0,
}
\tag{14}
$$

其中

$$
P_{D,t}=I+(t-1)\frac{\bar D^{\,t}D}{14}.
\tag{15}
$$

这是包含所有另外五个变量的等式。
对投影后的来源使用 (14)，依靠的是三个原轴的共轭闭合；
没有假定纯 $C$ 投影与单独的 $D$ 缩放交换。

由 R531 的完整 Gram，

$$
D\perp E,G,Y,W,W',L .
\tag{16}
$$

## 4. 两个真正的五变量条带

令

$$
\boxed{
X=c-\frac D{14},\qquad
Z=d_0+\frac{1+3\omega}{14}D.
}
\tag{17}
$$

它们是原 $c,d_0$ 的 $D$ 正交投影。确切地，

$$
c(P_{D,\kappa^n}\xi)=X+\frac{\kappa^nD}{14},\quad
d_0(P_{D,\kappa^n}\xi)=Z-\frac{1+3\omega}{14}\kappa^nD.
\tag{18}
$$

因为 $n\ge1$，所有以下深一层／单位判断都只取 (18) 模 $p$，
完全独立于自由 $D$。记 $a=2+\omega$，则

$$
\boxed{
P_{D,\kappa^n}^{-1}\mathcal B
 =\mathcal B_+:=\{Z\text{ unit},\ X-aZ\in p\mathcal O\},
}
$$
$$
\boxed{
P_{D,\kappa^n}^{-1}\mathcal B^c
 =\mathcal B_-:=\{Z\text{ unit},\ X+aZ\in p\mathcal O\}.
}
\tag{19}
$$

证明第一式：$u$ 模 $p$ 为
$(\omega X+(1-\omega)Z)/2$，其零条件等价 $X=aZ$；
而此时 $L=(1+3\omega)X+Z\equiv4\omega Z$。
第二式将 $X$ 换成 $-X$，并使用真正的 $L\circ R_c$，得到同一个
$4\omega Z$。这些都是单位系数的等价式。
两域不交，因为同时成立将迫 $2aZ$ 深。

若保原线性式，(19) 等价于分别使用

$$
u_\perp=u-\frac{\omega^2}{7}D,\qquad
u^c_\perp=u\circ R_c+\frac{2+3\omega}{14}D,
$$
$$
L_\perp=L,\qquad
L^c_\perp=L\circ R_c+\frac{1+3\omega}{7}D.
\tag{20}
$$

其中 $N(u_\perp)=5/7$、$N(u^c_\perp)=1/2$；本篇不给这些新轴
另设普通核心。它们只用于准确描述已付缩放后的实际事件。

设

$$
\pi_5=(E,Y,W,W',G).
$$

由 R531 的六行框架，$(D,\pi_5)$ 是当前处的整自同构。
(17) 确实是 $\pi_5$ 的线性式，全部系数如下；表以
$\mathbb Q(\delta)$ 书写：

| 行 | $E$ | $Y$ | $W$ | $W'$ | $G$ |
|---|---:|---:|---:|---:|---:|
| $X$ | $1/182$ | $(13+27\delta)/288$ | $(-285-575\delta)/6048$ | $(75+71\delta)/6048$ | $(4+\delta)/936$ |
| $Z$ | $(1-3\delta)/364$ | $(-8-3\delta)/144$ | $(21+10\delta)/432$ | $(51-11\delta)/864$ | $(13-11\delta)/1872$ |

所有分母只含当前已经排除的固定小素数。
表由完整六乘六有理 CM 逆矩阵得出，配套脚本保存精确运算；
没有把额外输入藏到一个独立的自由变量中。

## 5. 原全行的 n 无关表达

对 $\mu=\mu_0,\mu_h$ 定义真正五变量有界测度

$$
\mathfrak M_\mu=(\pi_5)_*\{\widehat P(D,E,G)\mu\}.
\tag{21}
$$

多项式在全原输入上整且有界。
把 (14)、(16)、(18)–(19) 同时用于 (13)，得到

$$
\boxed{
\begin{aligned}
\mathcal N_n=\frac{\beta^n}{b\Omega^6}
 \int_{E\text{ unit}}\ell(Y,W)\bigl\{&
 \tfrac32(\mathbf1_{\mathcal B_+}+\mathbf1_{\mathcal B_-})
       \,d\mathfrak M_{\mu_0}\\
 &+(\mathbf1_{\mathcal B_-}-\mathbf1_{\mathcal B_+})
       \,d\mathfrak M_{\mu_h}\bigr\}.
\end{aligned}}
\tag{22}
$$

右侧除了显式的 $\beta^n$ 外，所有来源、多项式、域和权都不依赖
$n$。因而 $\beta^{-n}\mathcal N_n$ 对全部 $n\ge1$ 完全相同。
这是精确等式，不是极限或模 $p$ 的首项比较。

证明过程中 $D/\kappa^n$ 精确返回 $D$，而 $E,G,Y,W$ 全保持不动。
因此 (22) 没有遗失逆尺度或由 $\log\langle\kappa\rangle$ 产生的项；
实际上这次从未缩放任何被取对数的线性式。

结合 (10)，原混合差的完整式为 (22) 右端再除以 $2\lambda$。
该系数也是单位；没有增加新的算术中央零假设。

## 6. 整个 degree 14 纤维及七个条件系数

(21) 可以进一步写成实际有限条件源，免去一个未计算的自由
$D$ 积分。沿原 $D$ 输出的整个 theta 空间是标准 even
$\mathcal S_{14}$。R557 证明 $\eta$ 的 $D_j$ 整行同样属于该完整
空间；(11) 的三个共轭分量因此都保持它。

其完整十四基可以取

$$
\mathcal J=\{0,1,2,\ldots,12,14\},
$$
$$
\mathcal F_j(z)=
\begin{cases}
x_\wp(z)^{(14-j)/2}\sigma(z)^{14},&j\text{ 偶},\\
-y_\wp(z)x_\wp(z)^{(11-j)/2}\sigma(z)^{14},
 &j=1,3,5,7,9,11.
\end{cases}
\tag{23}
$$

除去 $\sigma^{14}$ 后，极点阶是 $14-j$，互异，且恰为
$0,2,3,\ldots,14$，故 (23) 张满整个空间，不是 jet 截断。
每条基都是已有有界来源的卷积：
偶项是 $\Theta^{(14-j)/2}\sigma^j$，奇项是
$B_3\Theta^{(11-j)/2}\sigma^j$，$B_3=-y_\wp\sigma^3$。
因此它们全是整测度来源。

将同一个完整 $(D,\pi_5)$ 推前源唯一写成

$$
(D,\pi_5)_*\mu=\sum_{j\in\mathcal J}
 \nu_{\mathcal F_j}\otimes\Lambda_{\mu,j}.
\tag{24}
$$

$\Lambda_{\mu,j}$ 是真实的五变量系数测度，允许其五个变量相互
耦合，并未分成独立的一维来源。其整有界性可直接从
$j\in\mathcal J$ 的条件 jet 得出：$\mathcal F_j=z^j+O(z^{j+6})$，
这十四行的系数矩阵三角，主对角为 $j!\Omega^j$。
因为 $j\le14<p$，这些都是单位，所以对任意五变量连续测试均可
整地解出 $\Lambda_{\mu,j}$。这也证明 (24) 不是只对一维边际成立。

前六个小正矩没有额外低项，而

$$
\mathcal F_0=\Theta^7
 =1-\frac{14b}{15}z^6+O(z^{12}),\qquad
\mathcal F_6=z^6+O(z^{12}).
$$

于是完整条件矩为

$$
\begin{aligned}
(\pi_5)_*\mu&=\Lambda_{\mu,0},\\
(\pi_5)_*(D^k\mu)&=k!\Omega^k\Lambda_{\mu,k},
 &&1\le k\le5,\\
(\pi_5)_*(D^6\mu)&=
 \Omega^6(720\Lambda_{\mu,6}-672b\Lambda_{\mu,0}).
\end{aligned}
\tag{25}
$$

特别，若把第六行误写成只剩 $\Lambda_6$，就会丢掉实际质量项。

由 (6)、(21)、(25)，所需的两个**完整**五变量来源准确为

$$
\boxed{
\begin{aligned}
\mathfrak M_\mu={}&
 (P_0-672b\Omega^6P_6)\Lambda_{\mu,0}
 +\Omega P_1\Lambda_{\mu,1}
 +2\Omega^2P_2\Lambda_{\mu,2}\\
&+6\Omega^3P_3\Lambda_{\mu,3}
 +24\Omega^4P_4\Lambda_{\mu,4}
 +120\Omega^5P_5\Lambda_{\mu,5}
 +720\Omega^6P_6\Lambda_{\mu,6},
\qquad\mu=\mu_0,\mu_h.
\end{aligned}}
\tag{26}
$$

$P_k$ 在这里是相应 $E,G$ 多项式乘子；所有隐藏条件均在
$\Lambda_{\mu,j}$ 的同一个五变量空间上施加。
其余七条 theta 基的条件系数不贡献 (21)，理由是原测试次数恰为六；
没有把整个来源的其他角型称为零。

## 7. 全部补域和未付部分

(22)、(26) 合起来是原 R556 同一 native 行的完整有限表达。
它包含 $E$ 单位、$\mathcal B_\pm$ 两条实际条带、独立的 $Y/W$
单位条件，以及全部 $W',G$ 伴随。在这一步中没有先限制
$D_{12}$、$J_{37}$、$H_1$ 或某个中央非零网格。

另一方面，它并未判定 (22) 的值非零。
原算术输入 $J'_S=J'_T=0$ 只控制 R536 的完整 $\pi_4$ 行，
不能分别把 $\mathcal B_+$、$\mathcal B_-$ 或
$\Lambda_{\mu,j}$ 的积分置零。
R558 的 $\mathcal D_n$ 也不是 $\pi_5$ 的事件；若把那个网格插回
(13)，它的 $P_{D,\kappa^n}^{-1}$ 必须完整保留，不能继续直接使用
只适用于 (9) 的 $n$ 无关结论。

实际余项现在是同一个五变量、七条件源的条带积分。
其非零、与原算术零行的合法联立及无穷素数量词继续开放。
不存在用来源张满、局部单位、深度独立或有限素数验证直接结束
主任务的步骤。

配套脚本只计算原有理 CM 六行逆、投影、精确条带系数和第六矩
校正；完整来源、普通核心、紧开域及积分恒等式的证明在本文。
