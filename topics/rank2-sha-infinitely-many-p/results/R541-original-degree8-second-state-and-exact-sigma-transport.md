# R541 — degree8 第二态的原双 sigma 身份与完整三支域运输

日期：2026-11-14。**状态：已证明。**

[R539](R539-original-degree8-mixed-st-core-and-amplified-central-domain.md)
的第二态并不是需要另行猜测的 theta 来源。保同一个完整原六输入，
它准确又是两个独立原 sigma 经一个固定整有理酉矩阵的推前。
此外，它与原 $L$ 反射态的差也是一个真正双 sigma 来源。
本篇付清这三个来源的绝对常数、全部隐藏坐标和任意实际 cut 的转置。

第三支在原 $Y$ 观察下只需 $[2]$ 覆盖，得到一个明确的
degree136 截面。反射支和第二态一般仍需 $[4]$ 覆盖，不能删去。
本篇没有给这两个新边际预设算术中央零。

## 1. 原来源和 whole 核

沿用原规范
$$
\omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad
\alpha=\omega\bar\gamma=1+3\omega,
$$
$$
b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\qquad
\rho_0=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
原六输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。
本篇的三个矩阵只作用于最后两个原独立输入，逐个固定前四个。

令
$$
A=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma x,
\qquad L=\alpha c+d_0,\quad M=c-\bar\alpha d_0.
$$
于是
$$
Y=A+aL+b_M M,\qquad W=A+a_WL+b_M M,
$$
$$
a=-3\omega/8,\qquad a_W=a+2,\qquad b_M=-(1+6\omega)/8.
\tag{2}
$$
原两个 sigma 的完整生成函数为
$$
F_0(l,m)=\sigma(\alpha l+m)\sigma(l-\bar\alpha m)
\in\mathcal S_8^{\rm even}\otimes\mathcal S_8^{\rm even}.
\tag{3}
$$
这里的 even 指标准偶半特征，不是分别偶函数。

R539 已在 entire degree8 格支付全部中心和真实 Theta 锚：
$$
K_8=-R_8J_2,\qquad
J_2=\frac12\sum_{t\in E[2]}\mathsf T_t^8-I,\qquad
K_8^2=I.
\tag{4}
$$
令
$$
P_2=\frac14\sum_{t\in E[2]}\mathsf T_t^8.
$$
在 $P_2$ 的像上 $R_8=I$，故在 (3) 上
$$
F_1:=K_{8,L}F_0=F_0(-l,m)-2P_{2,L}F_0.
\tag{5}
$$
所有 $\mathsf T_t$ 都是原 canonical lift；没有更换半周期规范。

## 2. 完整二挠投影

记 $X=\wp(z)^3$。对于非零二挠点 $t$，令 $e=\wp(t)$，则
$e^3=-b$，canonical lift 给
$$
\mathsf T_t^8[\sigma^8P(\wp)]
=\frac{(\wp-e)^4}{9e^4}\,\sigma^8
 P\!\left(\frac{e\wp+2e^2}{\wp-e}\right).
\tag{6}
$$
这里的 $1/(9e^4)$ 是实际八次半周期常数：
标准 degree2 矩阵的平方先给 $c_t^4=1/(3e^2)$，再平方即得。
特别没有留下可任意选择的四次根。

将 (6) 对三个根完整相加，得到
$$
\boxed{
P_2(\sigma^8)=\frac{\sigma^8(X+b)}{3b}
             =\frac{\sigma(2z)^2}{12b},\qquad
P_2(\sigma^8X)=\frac23\sigma^8(X+b)
             =\frac{\sigma(2z)^2}{6}.
}
\tag{7}
$$
可直接以
$$
\operatorname{Tr}_{e^3=-b}((x-e)^4e^2)=12bx^3+3b^2,
$$
$$
\operatorname{Tr}_{e^3=-b}((x-e)(x+2e)^3e^2)=-15bx^3-24b^2
$$
核定 (7)，无需采样。

R539 的完整平移恒等式
$\mathsf T_{L,t}F_0=\mathsf T_{M,\alpha t}F_0$
在 $E[2]$ 上仍成立。因此 $P_{2,L}F_0$ 在两个轴上都属于
$[2]^*\mathcal S_2$。基可取 $\sigma(2z)^2,\Theta(2z)$，
其中 $\Theta=\wp\sigma^2$。
同时 $\mu_6$ 型为 $2$，所以完整联合只能是
$$
c\,\sigma(2l)^2\Theta(2m)+
e\,\Theta(2l)\sigma(2m)^2.
$$

用实际 CM7 除法恒等式
$$
\sigma(\gamma z)=\gamma\sigma(z)^7(X-r_\gamma),\quad
r_\gamma=\frac{2-6\delta}{7}b,\quad
r_{\bar\gamma}=\frac{2+6\delta}{7}b
\tag{8}
$$
及 (7)，两个轴的系数准确为
$$
c=\frac{\alpha(2-r_{\bar\gamma}/b)}{12}
  =-\frac{\omega^2}{2},\qquad
e=-\frac{\bar\alpha(2-r_\gamma/b)}{12}
  =\frac{\omega}{2}.
$$
故
$$
\boxed{
P_{2,L}F_0
=-\frac{\omega^2}{2}\sigma(2l)^2\Theta(2m)
+\frac{\omega}{2}\Theta(2l)\sigma(2m)^2.
}
\tag{9}
$$
两个系数不同，完整中心和 CM 共轭不能在这里省掉。

## 3. 三个真正双 sigma 来源

原 sigma 加法公式给
$$
\begin{aligned}
&\omega^2\sigma(2l)^2\Theta(2m)
-\omega\Theta(2l)\sigma(2m)^2\\
&\hspace{18mm}=
\omega^2\sigma(2l+2\omega m)\sigma(2l-2\omega m),
\end{aligned}
\tag{10}
$$
因为 $\Theta(\omega z)=\Theta(z)$ 而
$\sigma(\omega z)^2=\omega^2\sigma(z)^2$。
由 (5)、(9)，实际第二态因此满足
$$
\boxed{
\begin{aligned}
F_1(l,m)
&=F_0(-l,m)
  +\omega^2\sigma(2l+2\omega m)\sigma(2l-2\omega m)\\
&=-\sigma(\gamma l+m)\sigma(l-\bar\gamma m).
\end{aligned}}
\tag{11}
$$

第二个等号的完整证明如下。三个双 sigma 乘积的两个 Gram
对角都为 $8$，交叉项都为零；两个半特征都为标准偶半特征，
所以它们确在同一 $\mathcal S_8\otimes\mathcal S_8$ 中。
差具有同时 $\mu_6$ 型 $2$。
在两个变量的矩形 jet $0\le i,j\le8$ 中，只可能出现总阶
$2,8,14$。用
$$
\sigma(z)=z+\frac b{210}z^7-\frac{b^2}{1801800}z^{13}
+O(z^{19}),
$$
$$
\Theta(z)=1-\frac{2b}{15}z^6+\frac{4b^2}{17325}z^{12}
+O(z^{18})
\tag{12}
$$
直接展开，附证书准确核定这三整层的全部系数差均为零。
这是整个截面的判定：degree8 非零截面不能在一点有九阶零；
先对每个 $l$-jet 应用这个事实于 $m$，再对 $l$ 应用一次，
完整差只能为零。故这不是由少量数值 jet 外推的身份。

(11) 的第一、第二个等号也分别由附证书核定。
整个恒等式对一般 $b$ 成立；三层中的 $b$ 次数分别为 $0,1,2$。

## 4. 原六输入的真实物理矩阵

设
$$
A_\alpha=\begin{pmatrix}\alpha&1\\1&-\bar\alpha\end{pmatrix},
\quad
A_\gamma=\begin{pmatrix}\gamma&1\\1&-\bar\gamma\end{pmatrix},
\quad
A_\eta=\begin{pmatrix}2&2\\2\omega&-2\omega\end{pmatrix}.
$$
定义只作用于 $(c,d_0)$ 的矩阵
$$
\boxed{
\mathcal G=A_\alpha^{-1}A_\gamma
=\frac14\begin{pmatrix}
-1-4\omega&-2-\omega\\
1-\omega&3+4\omega
\end{pmatrix},
}
\tag{13}
$$
$$
\boxed{
\mathcal H=A_\alpha^{-1}A_\eta
=\frac12\begin{pmatrix}
-1-\omega&-1-2\omega\\
2+\omega&-1-\omega
\end{pmatrix},
}
\tag{14}
$$
$$
\boxed{
\mathcal R=A_\alpha^{-1}
 \begin{pmatrix}-1&0\\0&1\end{pmatrix}A_\alpha
=\frac14\begin{pmatrix}
-3&2+3\omega\\
-1-3\omega&3
\end{pmatrix}.
}
\tag{15}
$$
它们都是实际酉矩阵，
$\det\mathcal G=1,\det\mathcal H=\omega,\det\mathcal R=-1$。
当前所有普通处的 $2$ 都是单位，所以它们是原完整整格的自同构。
$\mathcal R$ 是真实 $L$ 反射，固定 $M$ 和其余四个原输入。
不将 $\mathcal G$ 误当成反射或有限阶矩阵。

令 $\rho_1=K_{8,L}\rho_0$，则 (11) 在原完整六输入上准确给
$$
\boxed{
\rho_1=-\mathcal G_*\rho_0
       =\mathcal R_*\rho_0+\omega^2\mathcal H_*\rho_0.
}
\tag{16}
$$
原 $-1/84$ 在三项中完全相同。
原四个 sigma 以及它们的所有独立隐藏条件保持，未先取共同
$A$ 的边际。整个来源具有整 Amice 变换；(13)–(16) 是整测度
推前身份，不需要反卷积或新的射线细分。

因此对任意实际可测域 $\mathcal E$ 和可积测试 $f$，
$$
\boxed{
\begin{aligned}
-&\int_{\mathcal G^{-1}\mathcal E} f(\mathcal G\xi)\,d\rho_0(\xi)\\
={}&\int_{\mathcal R^{-1}\mathcal E}f(\mathcal R\xi)\,d\rho_0(\xi)
+\omega^2\int_{\mathcal H^{-1}\mathcal E}
 f(\mathcal H\xi)\,d\rho_0(\xi).
\end{aligned}}
\tag{17}
$$
这就是同一原来源的三支完整域关系；不同分支的真实域按表中的
矩阵分别转置，不能只保第一边际。

## 5. 原 R536 测试怎样逐支运输

避免与 $\mathcal G$ 混淆，将 R536 的第三隐藏行记成 $G_{\rm hid}$。
该测试 $\mathfrak q_{n,p}$ 只依赖 $C,F,G_{\rm hid}$。
其实际两个 sigma 部分为
$$
C_{c,d_0}=0,\qquad F_{c,d_0}=M,\qquad
(G_{\rm hid})_{c,d_0}=(3-2\omega)M.
$$
写 $F=F_*+M$、
$G_{\rm hid}=G_*+(3-2\omega)M$，其中 $F_*,G_*$ 不依赖
$c,d_0$。三个来源的准确替换为
$$
\begin{array}{c|c|c}
& C& M\ \text{在 }F,G_{\rm hid}\text{ 中的替换}\\ \hline
\mathcal R&C&M\\
\mathcal G&C&c-\bar\gamma d_0\\
\mathcal H&C&2\omega(c-d_0)
\end{array}
\tag{18}
$$
所以 $\mathfrak q_{n,p}\circ\mathcal R=\mathfrak q_{n,p}$。
另外两支要按 (18) 改动全部 cubic carry、$D_j/\kappa^n$、
$E_j$、$G_{\rm hid}$ 和它们的完整 $\lambda,\kappa$ 系数。
不能把 $\mathcal G$ 或 $\mathcal H$ 也当成测试不变。

原网格
$$
\mathcal D_n=
\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n,\ x\ {\rm unit}\}
\tag{19}
$$
在三个矩阵下都保持，因为它们只对两个同时深的输入作整可逆
变换。因此 (17) 可以直接限制在同一个 $\mathcal D_n$ 上。
这只说明三条按 (18) 转置的实际局部行满足身份；
不能由此把其中每条局部中央单独置零。

## 6. 所有奇偶深都能返回原 S/T，但须用准确的归一测试

令 R539 的实际物理缩放为 $P_{L,t},P_{M,t}$。
对任意 $r,s\ge0$，设
$$
\varepsilon\equiv r+s\pmod2,\qquad
\mathcal A_{r,s}
=P_{L,\kappa^r}P_{M,\kappa^s}\mathcal G^\varepsilon.
$$
R539 的真实两态矩形与 (16) 合起来给
$$
\boxed{
\rho_0|_{\{L\in p^r,M\in p^s\}}
=\beta^{r+s}(\mathcal A_{r,s})_*\rho_0.
}
\tag{20}
$$
这里 $\lambda^{r+s}(-1)^\varepsilon=\beta^{r+s}$，
完整符号已经吸收，不能遗漏奇深的负号。
$\mathcal A_{r,s}$ 是原整格到这个矩形的双射。
其逆
$$
\mathcal A_{r,s}^{-1}
=\mathcal G^{-\varepsilon}P_{M,\kappa^{-s}}P_{L,\kappa^{-r}}
\tag{21}
$$
只在相应矩形上使用，因此所有归一坐标整。

令
$$
q_{n;r,s}=\mathfrak q_{n,p}\circ\mathcal A_{r,s}^{-1},
\quad
Y_{r,s}=Y\circ\mathcal A_{r,s}^{-1},
\quad
W_{r,s}=W\circ\mathcal A_{r,s}^{-1}.
$$
R536 的完整纤维推前身份直接给
$$
\boxed{
\begin{aligned}
\int_{\substack{L\in p^r,M\in p^s\\Y_{r,s}\ {\rm unit}}}
 \langle Y_{r,s}\rangle^{du}q_{n;r,s}\,d\rho_0
 &=\beta^{n+r+s}J_S(u),\\
\int_{\substack{L\in p^r,M\in p^s\\W_{r,s}\ {\rm unit}}}
 \langle W_{r,s}\rangle^{du}q_{n;r,s}\,d\rho_0
 &=6\delta\beta^{n+r+s}J_T(u).
\end{aligned}}
\tag{22}
$$
对所有奇偶 $r+s$ 都成立。这给原两个中央的真实附加归一域，
不需要给第二态未移动的 $Y/W$ 边际认定中央零。

R539 已付的局部非零与严格零质量也能保其原测试完整运输。
取偶数 $m$、$1\le m<n$，在 (22) 的逆坐标中再施加
$L\in p^m$，并用 R539 的 $Y_m$ 或 $W_m$：
$$
\mathcal E^Y_{m;r,s}
=\mathcal A_{r,s}\{L\in p^m,\ Y_m\ {\rm unit}\},\qquad
\mathcal D_{n;r,s}=\mathcal A_{r,s}\mathcal D_n.
$$
完整积分返回
$\beta^{r+s}\lambda^m\beta^nJ_S$；
$W$ 行同样返回 $6\delta J_T$。
在真实子管 $\mathcal D_{n;r,s}$ 上，权和测试都按 (21) 拉回，
故质量仍严格为零，中央的准确赋值仍为 $n-m$。
完整补域恰为
$$
\mathcal A_{r,s}
 \bigl(\{L\in p^m,Y_m\ {\rm unit}\}\setminus\mathcal D_n\bigr),
\tag{23}
$$
$W_m$ 亦然。它没有消失，也没有被改成原未移动单位域。

## 7. 原两条补域在一层核后的准确差

这里给一个可继续使用的同源补偿式，而非只登记额外的深域。
记
$$
Y_\kappa^{\mathcal G}
=Y\circ P_{L,\kappa}\mathcal G
=A+\kappa a(\gamma c+d_0)+b_M(c-\bar\gamma d_0),
$$
$$
W_\kappa^{\mathcal G}
=A+\kappa a_W(\gamma c+d_0)+b_M(c-\bar\gamma d_0).
\tag{24}
$$
二者之差是 $2\kappa(\gamma c+d_0)$，故其单位条件完全相同。
记该完整单位域为 $\mathcal U_\kappa$。
因为原测试被 $P_{L,\kappa}$ 保持，(20) 的一层式准确给
$$
\begin{aligned}
\beta^nJ'_S
={}&I_{Y,n}
+\beta\int_{\mathcal U_\kappa}
 d\log\langle Y_\kappa^{\mathcal G}\rangle\,
       (\mathfrak q_{n,p}\circ\mathcal G)\,d\rho_0,\\
6\delta\beta^nJ'_T
={}&I_{W,n}
+\beta\int_{\mathcal U_\kappa}
 d\log\langle W_\kappa^{\mathcal G}\rangle\,
       (\mathfrak q_{n,p}\circ\mathcal G)\,d\rho_0,
\end{aligned}
\tag{25}
$$
其中
$$
I_{Y,n}=\int_{\{L\ {\rm unit},Y\ {\rm unit}\}}
 d\log\langle Y\rangle\,\mathfrak q_{n,p}\,d\rho_0,
\quad
I_{W,n}=\int_{\{L\ {\rm unit},W\ {\rm unit}\}}
 d\log\langle W\rangle\,\mathfrak q_{n,p}\,d\rho_0.
$$
若原两个中央都为零，则
$$
\boxed{
I_{Y,n}-I_{W,n}
=-\beta\int_{\mathcal U_\kappa}
 d\log\!\left(
 \frac{Y_\kappa^{\mathcal G}}{W_\kappa^{\mathcal G}}
 \right)(\mathfrak q_{n,p}\circ\mathcal G)\,d\rho_0.
}
\tag{26}
$$
比值属于 $1+p\mathcal O$，右端确为整有界测试下的 $p$ 倍数。
左端仍完整包含两条不同的 $L$ 单位补域，包括 $Y/W$ 的单位
条件不同时的部分。(26) 只把两个深分支合法合到一个真正公共
单位域，没有把左边的不同补域删掉。

还可以将 (17) 用于 (25) 的任意剩余 cut；必须同时保留
$\mathcal R^{-1}\mathcal E,\mathcal H^{-1}\mathcal E$ 和 (18)。
这些是后续原 S/T 与第三算术来源可以比较的确切输入。

## 8. 第三支的 degree136 第一边际

定义第三实际来源
$$
\rho_\eta=\omega^2\mathcal H_*\rho_0,\qquad S_\eta=Y_*\rho_\eta.
$$
由 (14)，
$$
(Y\mathcal H)_{c,d_0}
=\left(\frac\gamma2,\frac{\omega^2\gamma_{13}}2\right),
\qquad\gamma_{13}=4+\omega.
$$
因此
$$
\boxed{
S_\eta(2z)
=-\frac{\omega}{84}
 \sigma(2\delta z)\sigma(4\delta z)
 \sigma(2\gamma z)\sigma(2\bar\gamma z)
 \sigma(\gamma z)\sigma(\gamma_{13}z)
\in\mathcal S_{136}.
}
\tag{27}
$$
这是同一完整第三支的真实第一边际。没有依靠质量或小谱样本来
认曲线。

若 $S_2(z)=S(2z)$，令
$$
R_2(X)=X^2+20bX-8b^2,
$$
$$
Q_{13}(X)=X^2+(8+12\omega)bX+\frac{64+48\omega}{13}b^2.
$$
准确的 CM13 除法式为
$$
\sigma(\gamma_{13}z)=
\gamma_{13}\sigma(z)^{13}Q_{13}(X).
\tag{28}
$$
它在 odd degree13 的相应三维型中，由 $z,z^7,z^{13}$ 三个
三角系数直接决定；附证书记录全部有理数计算。
利用 $\sigma(2z)\sigma(4z)=8\sigma(z)^{20}(X+b)R_2(X)$，
得到完整有理函数比值
$$
\boxed{
\frac{S_\eta(2z)}{S_2(z)}
=\frac{\omega\gamma\gamma_{13}(X-r_\gamma)Q_{13}(X)}
       {8(X+b)R_2(X)}.
}
\tag{29}
$$
等式在分母非零处成立并按 (27) 全纯延拓；计算实际多项式时
必须在整个 $S_2$ 中整除，不能任意反卷积该因子。

供后续比较，另两支在原 $Y$ 观察的最后两个系数是
$$
(Y\mathcal G)_{c,d_0}
=\left(\frac{1-6\omega}{4},\frac{4+7\omega}{4}\right),
$$
$$
(Y\mathcal R)_{c,d_0}
=\left(\frac{-5-6\omega}{4},\frac{8+3\omega}{4}\right).
\tag{30}
$$
所以一般需要保 $[4]$ 覆盖的 degree544 来源。
本篇不由第三支在 degree136 就把这两支也降到同一空间。
(16)、(17) 的完整五伴随与各 cut 仍然是比较这些边际的基础。

## 结论和保留的缺口

实际第二态、三支 sigma 身份、所有原输入物理矩阵，以及奇偶
深度的原 S/T 测试返回都已完整支付。(26) 还给原两个真实单位
补域之间的同源差，并使其深分支的单位条件严格相同。

仍需支付的是该公共域与三支转置补域的进一步算术关系，
包括 (27) 的完整 CM 投影如何在同一个实际 cut 中使用。
局部非零和 degree136 边际本身没有完成原无限普通素数目标。

## 精确证书与依赖

- [check-r541-original-degree8-second-state.js](../scripts/check-r541-original-degree8-second-state.js)
- [全部二挠 trace、三层完整 theta jet、物理矩阵 JSON](../scripts/check-r541-original-degree8-second-state.json)
- [R539：原 entire degree8 核与完整两态矩形](R539-original-degree8-mixed-st-core-and-amplified-central-domain.md)
- [R536：完整纤维补偿、严格零质量和三支测试](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)

证书已在当前 JavaScript 环境精确执行。所有 CM 系数用 BigInt
有理数表示；完整有限 jet 判定所需的每一项均已检查，矩阵是
实际六输入上的固定子块，非只在边际上推测的作用。
