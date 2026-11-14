# R219 — 实际整 theta 的同一 degree-p 全纤维迹、首 Frobenius 校正与未消残余

日期：2026-11-12。**状态：原第一行模 $p^2$ 的下降、同一有理覆盖的特征零提升、全纤维迹形状及原 $K$ 的精确剩余算子已证明。没有证明原 $K$ 在无穷多个素数处非零。**

本篇使用 [R207](R207-actual-dyadic-twist-trace-and-theta-branch-identity.md)
的固定 $E^+$ 和原 degree-$p$ 参数，以及
[R213](R213-original-theta-frobenius-next-digit-and-shared-log-cancellation.md)
的实际整参考。不是用裸迹替换 theta，也不把有限代表在其他点的值冒称原 theta 的全局值。

比较的结论相当具体：同一完整迹的常数项可以含 R207 单位，但两个正中央权的完整迹均为零。原 $K$ 由非原点分支的一个明确聚合后继行与两个原对数校正给出。首行失败保证的是聚合第一行可除 $p$，并不保证各分支分别可除 $p$。

## 1. 固定商、严格参数和实际参考

令 $p=4r-1>19$ 为素数，$d=2r-1$，$O=\mathbf Z_p$。原曲线及严格二同源为
$$
E_0:y^2=x^3-x,\qquad
E^+:Y^2=X^3+4X,\qquad
X=x-x^{-1},\quad Y=y(1+x^{-2}),
$$
同一不变微分的局部原函数仍记为 $z$。置
$$
s=x^{-2},\qquad q=(X^2+4)^{-1}=\frac{s}{(1+s)^2},\qquad
\rho=\frac{1-s}{1+s}=\sqrt{1-4q}.
\tag{1}
$$
所有根号取原点常数为一的分支。严格逆函数 $s=S(q)$ 属于 $q\mathbf Z[[q]]$，由 $S=q(1+S)^2$ 唯一确定。

沿用 R213 的 $F(s)$、$L(s)=\log\vartheta^{68}$、
$\ell=[s^r]L$、$c=68k_r$ 和
$$
\widetilde\Gamma(s)=\exp(L(s)-\ell s^rF(s))\pmod{s^{2r}},
\qquad
\alpha=\overline{p\ell}=\overline{pc}=68\kappa.
\tag{2}
$$
定义真正由这个原参考构造的有限多项式
$$
\boxed{\quad
\Xi(q)=
\left[\widetilde\Gamma(S(q))(1+S(q))^{17}\right]_{\deg\le d}
\in O[q],\qquad \Xi(0)=1.
\quad}
\tag{3}
$$
它只代表原点 jet；由于下列原两列都从 $q$ 开始，次数 $d$ 已保留两个所需权。

R207 的原有理列为
$$
\begin{aligned}
a_0(q)&=
q(1-32q/5+64q^2/5)(1-4q)(1+64q^2)(1+16q-64q^2),\\
b_0(q)&=
q-\frac{72}5q^2+448q^3-5120q^4+
\frac{126976}5q^5-\frac{294912}5q^6+\frac{262144}5q^7.
\end{aligned}
\tag{4}
$$
其次数分别为八、七。实际整参考下的两列在原点准确为
$\Xi a_0,\ \Xi\rho b_0$，到本篇的两个权均成立。
令下降后的有理列为
$$
D_A(q)=\Xi(q)a_0(q),\qquad
D_B(q)=\Xi(q)b_0(q)(1-4q)^{-d}.
\tag{5}
$$
第二列使用的是准确的 $\rho^{-p}$ 扭曲：
$\Xi\rho b_0\cdot\rho^{-p}=D_B$。其模 $p^2$ 校正将在 §3 保留。

## 2. 同一 Z 的具体特征零提升，支付所需第一行精度

令 $u_+=q^{1/4}$，选 $u_+=z+\cdots$。由 (1) 直接求导，
$$
z=u_+F_+(q),\qquad
F_+(q)=\sqrt{1+S(q)}\,F(S(q)),
$$
$$
G_+(q):=F_+(q)+4qF_+'(q)=(1-4q)^{-3/4},
$$
$$
F_+(q)=
\sum_{j\ge0}
\frac{(3/4)_j\,4^j}{j!(4j+1)}q^j.
\tag{6}
$$
在次数不超过 $d$ 的范围系数均整，且其约化是次数 $r-1$ 的多项式
$$
g(q)=\sum_{j=0}^{r-1}
\frac{(-4)^j\binom{r-1}j}{4j+1}q^j,\qquad
g+4qg'=(1-4q)^{r-1}.
\tag{7}
$$
这是因为 $-3/4\equiv r-1\pmod p$，且该窗口中的 $4j+1$ 均为单位。

现在在特征零中取
$$
\widehat g(q)=
\left[F_+(q)(1-4q)^{p/4}\right]_{\deg<r}\in O[q].
\tag{8}
$$
定义原 degree-$p$ 参数的有理提升
$$
\boxed{\quad
\widehat Z=
-YX^{-2r}(X^2+4)^{r-1}
\widehat g\!\left((X^2+4)^{-1}\right).
\quad}
\tag{9}
$$
其原点表达是
$$
\widehat Z=q^{1/4}(1-4q)^{-p/4}\widehat g(q).
$$
因此 $\widehat Z=z+O(z^{p+2})$ 是特征零准确的 jet 等式。
又因 $F_+\bmod p=g$ 到次数 $d$、而
$(1-4q)^{p/4}\equiv1\pmod p$ 到这些次数，(8) 被截掉的部分在此窗口属于 $pq^rO[[q]]$。从而
$$
\widehat Z-z\in pz^{p+2}O[[z]]
\quad\text{到读取第二权所需的精度}.
\tag{10}
$$

(9) 只在 $T'=(0,0)$ 有阶数 $p$ 的极点，原点有一阶零点；其约化恰是 R207 的原 $Z$。具体地，
$$
\overline Z^{\,4}=\frac{qg(q)^4}{(1-4q)^p},\qquad
d\overline Z=\omega_+.
\tag{11}
$$
(9) 中乘 $-1$ 使严格原点首项为 $z$，与 R207 首项规范一致。
其极点处首系数约化非零，故次数准确为 $p$，不是一个更大的替代覆盖。

对任意从 $q$ 开始的整函数，(10) 有以下直接作用：

- 第一个权 $p+1$ 的系数由 $\widehat Z$ 读取，与由原 $z$ 读取**精确相同**；
- 第二个权 $2p+2$ 的系数模 $p$ 相同。

第一条是由于函数从 $z^4$ 开始，而参数误差从 $z^{p+2}$ 开始。这特别保留第一行的模 $p^2$，没有把全局 $dZ$ 无证提升到模 $p^2$。

## 3. rho 扭曲的第一 Frobenius 校正和原 K

记原两权行为 $R_1$、$\widehat R_2$，以及 R213 的
$$
u=\overline{R_1/p},\qquad
K=\overline{\widehat R_2}-\alpha u
\tag{12}
$$
（后两者只在首行失败 $R_1\in pO^2$ 后定义）。
另记 R213 已证明的原配对向量
$$
l=L_{\rm fix}+L_{\rm rem}
=[w^r]\widehat{\mathbf A}(w)\log F(s(w))\pmod p.
\tag{13}
$$
定义
$$
L_{\rho,B}=[w^r]\widehat B(w)\log\rho(s(w))\pmod p,\qquad
\eta=(0,L_{\rho,B}).
\tag{14}
$$
这些有限对数的分母都小于 $p$。

用 (9) 取下降两列的原点系数：
$$
\mathcal D_j=
\left(
\operatorname{Res}_O
\frac{D_A\,d\widehat Z}{\widehat Z^{j(p+1)+1}},
\operatorname{Res}_O
\frac{D_B\,d\widehat Z}{\widehat Z^{j(p+1)+1}}
\right)\in O^2,\qquad j=1,2.
\tag{15}
$$
式 (8)–(10) 与
$$
\rho^{-p}\equiv1-p\log\rho\pmod{p^2}
$$
准确给
$$
\boxed{\quad
\mathcal D_1\equiv R_1-p\eta\pmod{p^2}.
\quad}
\tag{16}
$$
特别 $\mathcal D_1\in pO^2$ 与 $R_1\in pO^2$ 等价；首行失败后
$\overline{\mathcal D_1/p}=u-\eta$。不能只用 $\rho^{-p}\equiv1\pmod p$ 便省掉这个下一位。

对第二行，$\rho^{-p}$ 和 (10) 的误差都是 $p$ 倍整系数，故
$\overline{\mathcal D_2}$ 等于原 $\widetilde\Gamma(P,Q)$ 的第二个 $z$ 权。
由 $s^rF(s)=w^rF(s)^{-p}$，
$$
\overline{\mathcal D_2}
=\overline{\widehat R_2}
+\overline{c-\ell}\,\overline{R_1}+\alpha l.
\tag{17}
$$
这里 $c-\ell\in O$，而非任意丢掉一个非整 gauge。
在首行失败后，(12)、(16)、(17) 给出本篇的实际比较：
$$
\boxed{\quad
K=
\overline{\mathcal D_2-\ell\mathcal D_1}
-\alpha(l+\eta).
\quad}
\tag{18}
$$
$\ell\mathcal D_1$ 在作约化之前已由首行失败证明整。

所有校正都可直接在同一 $q$ 窗口读取。例如，写
$R_A(q)=a_0(q)$、$R_B(q)=b_0(q)(1-4q)^{-d}$，则
$$
\begin{aligned}
L_{\rho,B}
&=[q^r]\bar\Xi R_B\,
 \frac{(1-4q)^{r-1}}{g(q)^2}\,
 \frac12\log(1-4q),\\
l_F&=[q^r]\bar\Xi R_F\,
 \frac{(1-4q)^{r-1}}{g(q)^2}
 \left(\log g(q)-\frac12\log(1+S(q))\right).
\end{aligned}
\tag{19}
$$
这保留了从 $s$ 到 $q$ 的真实椭圆对数修正；没有将两个混合参数直接等同。

## 4. 实际完整迹在特征零中的形状

对 (9) 的同一函数域扩张取未除 $p$ 的迹
$$
\mathcal T_F(Z)=
\operatorname{Tr}_{\mathbf Q_p(E^+)/\mathbf Q_p(\widehat Z)}D_F,
\qquad Z=\widehat Z.
$$
准确有
$$
\boxed{\quad
\mathcal T_A(Z)=\sum_{j=1}^{r+3}A_{-j}Z^{-4j},
\qquad
\mathcal T_B(Z)=C_0+\sum_{j=1}^{3}B_{-j}Z^{-4j}.
\quad}
\tag{20}
$$
允许部分系数为零。它们在所用整数模型中均整。

证明只用实际极点，不需要把 $\Xi$ 当作全局 theta。$q=\infty$
对应固定 $P_\pm=(\pm2i,0)$，二点均是 $\widehat Z$ 的简单零点。
$D_B$ 在 $q=\infty$ 的极点阶数至多
$\deg\Xi+7-d\le7$，故在每个 $P_\pm$ 至多十四；
$D_A$ 在每点至多 $2(d+8)=p+15$。
除此之外，$D_B$ 只在 $T'$ 有阶数 $4d=2p-2$ 的极点，
而 $D_A(T')=0$。$T'$ 是 $\widehat Z$ 的唯一极点，阶数 $p$，
所以迹在 $Z=\infty$ 的极点阶数至多一。
两列均为 $\mu_4$ 不变，而 $\widehat Z$ 的特征为 $i$，因此迹只含
$Z$ 的四倍幂；这个至多一次的多项式部分只能是常数。
$D_A(T')=0$ 再使其常数为零。有限极点只可能在 $Z=0$，
上述十四与 $p+15$ 的界给出 (20)。

约化 $dZ=\omega_+$ 使整个零纤维 étale；其特征零提升也由同一整局部参数给出。
各分支的 Laurent 系数均整，故 (20) 中的系数整。这一论证未要求把每个分支的第一权除 $p$。

特别，两个正中央权的完整迹在特征零就满足
$$
[Z^{p+1}]\mathcal T_F=[Z^{2p+2}]\mathcal T_F=0.
\tag{21}
$$
R207 的裸单位是 $\Xi=1$ 时 $\mathcal T_B$ 的常数项。
无论其值是否为单位，(21) 以及用于 (18) 的两个正权操作都准确消去这个常数项。

### 4.1. 实际参考怎样改变常数项

设 $B(q)=\Xi(q)b_0(q)$；其次数至多 $d+7<p$。记
$$
\mu_k=\frac{(1/4)_k}{4^k k!}\in\mathbf F_p,\qquad 0\le k<p.
$$
同一迹计算给
$$
\boxed{\quad
\overline{C_0}=
\kappa\sum_k [q^k]\bar B(q)\,\mu_k.
\quad}
\tag{22}
$$
这将 R207 的常数公式扩展到实际参考，但未将它化成裸单位。

为证明这一扩展，可在 $T'$ 取留数；由 (11)，
$$
\overline{C_0}
=-\operatorname{Res}_{q=1/4}
 \frac{\bar B(q)(1-4q)^{-r}}{qg(q)}\,dq.
$$
由 (7)，在 $q=1/4$ 附近，$g$ 到次数 $r-1$ 的 jet 是常数倍
$q^{-1/4}$，且该常数非零。对单项式 $q^k$，上式给出一个
$\binom{k-3/4}{r-1}$ 型留数，其相邻比准确为
$(k+1/4)/(4(k+1))$。$k=0$ 的规范是 R207 的 $\kappa$；
因 $k<p$，递推给 (22)。其中可能出现的零分子亦被保留。

原 $\Xi=1$ 给
$\kappa\,2261/81920$。实际 $\Xi$ 则额外有
$\kappa\sum_k[q^k]((\bar\Xi-1)b_0)\mu_k$；
首行失败未证明消去这一项。

## 5. 原 K 的具体非原点算子

令 $\mathscr F_0$ 为 $\widehat Z=0$ 的完整有限 étale 纤维，
包含 $O,P_+,P_-$ 及其余 $p-3$ 个点。定义聚合行
$$
\mathcal N_{j,F}(\Xi)=
\sum_{P\in\mathscr F_0\setminus\{O\}}
\operatorname{Res}_{P}
 \frac{\Xi(q)R_F(q)\,d\widehat Z}
      {\widehat Z^{j(p+1)+1}}.
\tag{23}
$$
对在 $P_\pm$ 有极点的项，取实际 Laurent 留数。
这是完全明确的有理线性算子，不是未知的原 theta 全局取值。
写 $\Xi=\sum_{k=0}^{d}\xi_kq^k$，它的矩阵条目就是
$$
N_{j,k,F}=
\sum_{P\in\mathscr F_0\setminus\{O\}}
\operatorname{Res}_{P}
 \frac{q^kR_F(q)\,d\widehat Z}
      {\widehat Z^{j(p+1)+1}}.
\tag{24}
$$
所有点、参数与函数均由 (4)、(8)、(9) 的固定有理公式确定；
Galois 不变性使条目在 $\mathbf Q_p$ 中，上述整分支证明其属于 $O$。

迹与留数的交换及 (21) 给特征零等式
$$
\mathcal N_j=-\mathcal D_j,\qquad j=1,2.
\tag{25}
$$
故原首行失败时，准确得到
$$
\boxed{\quad
K=
-\overline{\mathcal N_2(\Xi)-\ell\mathcal N_1(\Xi)}
-\alpha(l+\eta).
\quad}
\tag{26}
$$
这里 $\mathcal N_1\in pO^2$ 由 (16)、(25) 保证。
若将 (23) 再拆成固定 $P_\pm$ 与其余移动分支，**不能**无证分别把两组第一权除 $p$：
本篇只证明它们的聚合被 $p$ 整除。

因此，自然的全纤维正权比较并不给“裸迹单位加上首行失败后消失的项”。
其裸常数贡献准确为零；真正保留的是 (26)。
这不排除另有一条利用实际 theta 更多恒等式的新比较，
但它必须控制同一个 (23)，而不能以全迹常数代替原点分支。

## 6. 剩余算子不会仅由首行失败消去

下面分析 (26) 的矩阵本身；实际使用时始终代回 (3) 的唯一 $\Xi$。
为了识别哪些输入尚未被第一行约束，固定原 $a_0,b_0,\ell,\widehat Z$，
考察参考的高次系数方向。这不是把这些扰动冒称另一条原曲线。

沿 $q^d$、$q^{d-1}$ 改变 $\Xi$ 时，两条第一权在特征零均不变，
所以其除 $p$ 值也不变；(19) 的校正亦不变。第二行的变分矩阵准确为
$$
\boxed{\quad
\delta_{q^d}K=(1,1),\qquad
\delta_{q^{d-1}}K=(34/5,-76/5).
\quad}
\tag{27}
$$
其行列式为 $-22$，在本篇全部素数处为单位。

证明可在原点用 (7) 直接读第二行。模 $p$ 的第二权核为
$(1-4q)^{r-1}/g^3$。由于
$a_0=q+(28/5)q^2+\cdots$、$b_0=q-(72/5)q^2+\cdots$、
$g=1+(3/5)q+\cdots$，对 $A$ 的核首修正为 $6/5$；
对 $B$，还含 $(1-4q)^{-d}$，总核首修正为 $-4/5$。
这就给出 (27)。

因此聚合残余在第一行的完整核上仍有两个独立方向。它不能仅由
“首行失败”“全迹在一个固定对数方向”或极点次数界被置零。
对真正的 $\Xi$，写 $\Xi_{\rm low}=\sum_{k\le d-2}\xi_kq^k$，
同一算子给出准确的实际分解
$$
K(\Xi)=K(\Xi_{\rm low})
+\xi_{d-1}(34/5,-76/5)+\xi_d(1,1)\pmod p.
\tag{28}
$$
其中 $K(\Xi_{\rm low})$ 指 (18) 的同一线性算子，
保留原 $\ell$、同一第一行除 $p$ 和同一校正。
完整中央双零会要求这个真实高 jet 满足
$$
\xi_{d-1}=\frac{K_B(\Xi_{\rm low})-K_A(\Xi_{\rm low})}{22},
\qquad
\xi_d=-K_A(\Xi_{\rm low})-\frac{34}5\xi_{d-1}.
\tag{29}
$$
本篇未证明实际 theta 系数在无穷多个素数处违反 (29)。

还有一个针对常数迹的明确线性障碍。将 (22) 除以单位
$\kappa\mu_d$，它在最高三个方向的值，以及对应 $K$ 行，为
$$
\begin{array}{c|c|cc}
\delta\Xi&
\delta C_0/(\kappa\mu_d)&\delta K_A&\delta K_B\\ \hline
q^d&-14/195&1&1\\
q^{d-1}&112/75&34/5&-76/5\\
q^{d-2}&-2432/75&-2938/25&11472/25 .
\end{array}
\tag{30}
$$
这些数只用 (4)、(7)、(22) 的有理递推计算。
前两行迫使候选系数为
$\lambda_A=196/10725$、$\lambda_B=-322/3575$；
第三行留下
$$
-\frac{2432}{75}
-\lambda_A\!\left(-\frac{2938}{25}\right)
-\lambda_B\frac{11472}{25}
=\frac{3592}{325}.
\tag{31}
$$
其分子是 $8\cdot449$，分母为 $5^2\cdot13$，在所有本篇惰性素数处均为单位。
三个高方向的完整第一行都为零，故即使容许增加任意只依赖原第一行的线性泛函，
常数迹也不在这两个 $K$ 泛函所张的空间中。
这排除了仅凭现有线性迹与首行条件的省略法；它没有排除只对实际 (3)
成立的、另需证明的非线性 theta 恒等式。

## 7. 既有 p43 的准确校准

本节仅复用此前的 $p=43$，没有扩大素数列表。
终端失联后，以下数值在 JavaScript 精确有限域运算中生成；
(30)、(31) 用 BigInt 有理数运算生成，未冒称失联后进行了终端运行。

原 $\Xi$ 的系数从常数到次数 $21$ 为
$$
(1,37,20,22,40,9,13,1,41,1,34,10,26,34,8,32,28,5,11,6,14,29).
$$
实际完整 $B$ 迹的常数模 $43$ 为 $8$，而 R207 裸迹常数为 $21$。
另有
$$
\alpha=19,\quad L_{\rho,B}=33,\quad
l=(30,17),\quad \overline{\mathcal D_2}=(32,4),
$$
$$
\mathcal D_1\bmod43^2=(899,264).
$$
这保留了第二列的首 Frobenius 校正：
$264\equiv1683-43\cdot33\pmod{43^2}$。

采用 R213 已用过的行列式一列变换 $B-20A$，原首项可除 $43$，
其值为 $u=8$；下降后的值是 $u_D=18$。
因此下降后的聚合后继值为
$$
(4-20\cdot32)-19\cdot18=11\pmod{43}.
$$
原校正是 $\alpha(l_B-20l_A+L_{\rho,B})=42$，故
$$
K=11-42=12\pmod{43},
$$
与 R213 断开前已执行的有理计算一致。
这个样本的原第一行向量没有同时为零；本节只校准真实提升与分支公式。

## 8. 当前比较真正留下的条件

本篇已在原 $E^+$、原 degree-$p$ 约化参数和实际整 theta 参考之间，
同时保留第一权模 $p^2$、第二整权模 $p$、$\rho^{-p}$ 的首修正、
原点分支及完整纤维。固定迹单位没有丢失，而是位于 (20) 的常数权，
被本目标的正权算子准确消去。

剩下的具体对象是 (26) 的同一非原点聚合算子，
等价地是 (28)、(29) 中实际 theta 高 jet 与已保留的原第一行下一位。
它在首行核上仍有非零、满二维的高系数方向，不能无证省略。
尚须利用实际 theta 的额外性质证明这份剩余在无穷多个素数处非零，
或者给出其与另一项已知非零算术量的真正比较。
