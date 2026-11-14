# R505 — 实际接触 Bockstein、同预算 F² 嵌入与完整 ξ 项吸收

日期：2026-11-14。**状态：已证明。** 本篇把 R502 仍然有效的整个 $\xi$ 向量识别为一个更短、但同样实际的接触 Bockstein，经原 $F^2$ 来源嵌入后在 $\operatorname{coker}\bar J$ 中的像。不是将 $\xi$ 任意置零，也不把三厚化中的 $\zeta^3$ 从原目标删掉。

接触长度为 $q=h-k$。R498 真左行的 $A$ 层恰是这个接触矩阵的几何对偶，准确配对为 $3\operatorname{Res}Ae^3\xi\,dt$。若接触 Bockstein 为零，整个 $\xi$ 向量由同一原来源修正吸收；特别当 $q<-K_XC$ 时自动成立。剩余真实 carry、低行右逆的全部高尾、原 $M$ 的两条十三行边界与第三精度均保留。高 $b$ 临界区未因此解决。

## 1. 原实际范围与符号

保 R491、R495、R498 和 R502 的原对象。取
$$
p=6s-1>83,\qquad f_D<p,\qquad
\mathcal O/\mathbf Z_p\ \text{有限非分歧},\quad k=\mathcal O/p.
$$
原相对目标及其约化为
$$
\Gamma=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),
\qquad
\bar\Gamma=k[w,\epsilon]/(w^s,\epsilon^3,w^\ell\epsilon^2).
\tag{1}
$$
仍使用原 $t(w)=-w+\cdots$、$Y=\mathscr R$、$\mathcal E=Y\partial_Y$、
$d=1+8t$ 以及原 Gaussian 已删的实际 $g$。
物理评价是 $Y_{\rm phys}=g(w)e_2(a\epsilon)$，其中 $a=p\kappa_{\rm Gauss}$ 为单位。

取一个实际约化立方首核
$$
d^{C_D}\bar P=t^rF^3Q,\qquad
F\in k[t,Y]\text{ 不可约},\quad
F(0,1)=0,\quad F_Y(0,1)Q(0,1)\ne0.
\tag{2}
$$
$C$ 是 R495 同一十九次固定吹起面 $X$ 上的严格变换，$P=(0,1)$ 是未动的光滑点。记
$$
\kappa=C^2,\qquad \chi=-K_XC\ge2\deg_YF>0.
\tag{3}
$$
本篇保 R502 的低 $\ell$ 可读范围
$$
1\le\ell\le r<h<s,\qquad
k=2h+r-s,\qquad 0\le k<\ell.
\tag{4}
$$
这里 $h$ 是原 $F(t,\bar g)$ 的接触阶。定义
$$
S=s-r=2h-k,\qquad q=h-k=s-r-h>0.
\tag{5}
$$
本篇小写 $q$ 只表示这个接触长度，与余因子 $Q$ 不同。

按 R491 选择保持全部角条件及次数帽的整因子 $\widetilde F,\widetilde Q$，使
$$
P^{\rm fact}=d^{-C_D}t^r\widetilde F^{\,3}\widetilde Q\in\mathcal W_D.
\tag{6}
$$
令 $\widetilde\psi$ 是 $\widetilde F=0$ 的同一整正规分支，$\psi$ 为其约化。
R502 的实际低阶正规分解为
$$
\eta=\log(g/\widetilde\psi)=t^hu+p\xi\pmod{p^2},
\qquad \deg_t\xi<h.
\tag{7}
$$
只有本题已付窗口内的有限 log 展开用于此式；$\xi$ 来自真实整轴，不是可任取的多项式。下文模 $p$ 公式中的 $u,\xi$ 均指其约化。另记单位
$$
e=(\mathcal EF)|_C,\qquad
q_C=(d^{-C_D}Q)|_C.
\tag{8}
$$
$e(P)=F_Y(P)$ 为单位。

## 2. 因子的一倍截面格也是真实有限自由格

令 $\mathcal H_1$ 是同一整吹起模型上 $\mathcal O(\widetilde C)$ 的显示多项式截面格。具体地，它由与 $\widetilde F$ 相同的纤维次数帽、各系数次数帽及十九个中间例外除子条件给出。其约化准确为
$$
\overline{\mathcal H}_1=H^0(X,\mathcal O_X(C)).
\tag{9}
$$

这里的整性并非从特征零维数推断。每个中间 Gauss 条件都逐 $Y^i$ 等价于指定的角整除阶；无穷远条件则给该系数的次数上界。将同一系数所有下界取最大值后，可写成
$$
\mathcal H_1=\bigoplus_i
Y^iD_i(t)\mathcal O[t]_{\le m_i},
\tag{10}
$$
其中 $D_i$ 是固定互素 monic Hensel 角因子的乘积；$m_i<0$ 的项省去。R491 的互素性保证约化保持这些准确整除及次数条件。所以 (10) 有限自由，约化核恰为 $p\mathcal H_1$，且 $\widetilde F\in\mathcal H_1$。所有中间吹起条件均在 (10) 中，没有只保每条链的末端。

R495 已付整个三倍线性系包含于原来源。因此
$$
\boxed{\quad
\iota:\mathcal H_1\longrightarrow\mathcal W_D,\qquad
H\longmapsto d^{-C_D}t^r\widetilde Q\,\widetilde F^{\,2}H
\quad}
\tag{11}
$$
是同一预算内的整来源包含：$F^2H$ 是同一三倍类的截面，乘固定 $d^{-C_D}t^r\widetilde Q$ 后仍满足原每条 $q_n$ 及其次数帽。它不要求任意三倍截面都能写成乘积。

(11) 还是 $p$ 饱和的来源包含。若其像可在原格被 $p$ 整除，约化后多项式域中的非零因子 $t^rQF^2$ 迫 $\bar H=0$；再由 (10) 得 $H\in p\mathcal H_1$。此结论只关于来源，不声称任何物理评价像饱和。

$\mathcal H_1$ 仅用于构造同一原修正；它不是新算术来源，也没有得到新的中央零。

## 3. 更短的实际接触矩阵及其 Bockstein

定义整有限矩阵
$$
E_q:\mathcal H_1\longrightarrow\mathcal O[t]/(t^q),
\qquad
H\longmapsto H(t,g(t))\pmod{t^q}.
\tag{12}
$$
$q\le h<s$，所以这里只读取原实际整轴的已付低阶系数。原 $t/w$ 单位和参数逆在这个窗口整可逆，没有跨过 $w^s=p\epsilon$ 去作未付除法。

因为 $\bar g-\psi$ 的阶为 $h\ge q$，(12) 的约化准确分解为
$$
H^0(X,\mathcal O_X(C))
\longrightarrow H^0(C,N_C)
\longrightarrow N_C|_{qP},
\qquad N_C=\mathcal O_C(C).
\tag{13}
$$
局部用原多项式截面的同一框识别最后一项为 $k[t]/(t^q)$。第一箭头满射、核为 $kF$，由 $H^1(X,\mathcal O_X)=0$ 得到。又
$$
H^1(C,N_C)=H^0(C,\omega_C\otimes N_C^{-1})^*=0
$$
因为后者线束的次数是 $K_XC=-\chi<0$。这里 $C$ 是 R495 已付的几何整 Cartier 曲线；允许其在 $P$ 外奇异，Gorenstein 对偶仍适用。

因此有准确等式
$$
\boxed{\quad
(\operatorname{coker}\bar E_q)^*
=
H^0\bigl(C,\omega_C\otimes N_C^{-1}(qP)\bigr)
=
H^0\bigl(C,K_X|_C(qP)\bigr).
\quad}
\tag{14}
$$
没有剩余的正则对偶商。

$F\in\ker\bar E_q$。取 (6) 的真实提升，定义
$$
\mu_F=\overline{E_q(\widetilde F)/p},\qquad
\beta_{\rm cont}(F)=[\mu_F]\in\operatorname{coker}\bar E_q.
\tag{15}
$$
这是整矩阵 (12) 的普通首次 Bockstein。若将 $\widetilde F$ 换成同一格中的
$\widetilde F+pH$，$\mu_F$ 改变 $\bar E_q(\bar H)$，所以 (15) 的类不变。

**引理 1。** 在同一个 $k[t]/t^q$ 中，
$$
\boxed{\mu_F=e\xi.}
\tag{16}
$$

**证明。** 用 (7) 在真实正规分支展开
$$
\widetilde F(t,\widetilde\psi e^\eta)
=(\mathcal E\widetilde F)|_{\widetilde C}\,\eta
+\tfrac12(\mathcal E^2\widetilde F)|_{\widetilde C}\,\eta^2+\cdots.
$$
模 $t^q$ 时 $t^hu$ 消失，且模 $p^2$ 时含 $(p\xi)^2$ 的项消失。故这个实际值为 $p e\xi\bmod(p^2,t^q)$。这证明 (16)，而非将正规坐标的任意变动当作原来源修正。$\square$

## 4. 同一原首像中的严格交换图

定义一个真实目标尾嵌入
$$
T:k[t]/t^q\longrightarrow\bar\Gamma,\qquad
f\longmapsto
2a\epsilon\,t^{r+h}q_Ce^2u\,f.
\tag{17}
$$
所有单位都在原 $t$ 变量中取实际截断。(5) 给
$s-(r+h)=q$，所以 (17) 在第二块准确保留 $q$ 个系数，并且是单射。

**定理 2。** 整来源包含 (11) 与实际矩阵满足
$$
\boxed{\bar J\,\bar\iota=T\,\bar E_q.}
\tag{18}
$$
这是原目标全部三块中的等式。

**证明。** 令 $\eta_0=t^hu$。在约化的原物理评价中
$Y=\psi e^{\eta_0}e_2(a\epsilon)$。对 $t^r(d^{-C_D}Q)F^2H$ 展开：

第一块至少有 $t^{r+2h}=t^{s+k}$，故在原第一块为零。第三块始终含 $t^r$，而 $r\ge\ell$，故在原第三块为零。第二块的唯一可见项是
$$
2a\epsilon\,t^r
(d^{-C_D}Q)(t,\bar g)\,
F(t,\bar g)(\mathcal EF)(t,\bar g)H(t,\bar g).
$$
其余项含 $t^rF(t,\bar g)^2$，由 $r+2h\ge s$ 消失。可见项中用
$F(t,\bar g)=e\eta_0+O(\eta_0^2)$，
并将其他因子换成沿 $C$ 的值；全部误差同样至少含 $t^r\eta_0^2$。所得恰为
$$
2a\epsilon\,t^{r+h}q_Ce^2u\,H(t,\psi),
$$
最后只读 $q$ 阶，故等于 (17) 作用于 (12) 的约化。$\square$

本定理只声称模 $p$ 的严格交换，不把它提升为模 $p^2$ 的交换；R502 的 carry 正是后者不能自动成立的原因。

由 (18)，$T$ 诱导一个有定义的余核映射
$$
\bar T:\operatorname{coker}\bar E_q
\longrightarrow\operatorname{coker}\bar J.
\tag{19}
$$
它未被证明单射：其他原来源列仍可吸收它的像。

R502 的整个 $\xi$ 向量为
$$
\beta_\xi=
6a\epsilon\,t^{r+h}q_Ce^3u\xi.
\tag{20}
$$
结合 (16)、(17)，得到实际完整恒等
$$
\boxed{\quad
\beta_\xi=3T(\mu_F),\qquad
[\beta_\xi]=3\bar T\bigl(\beta_{\rm cont}(F)\bigr).
\quad}
\tag{21}
$$
(21) 不是只比较一个首系数；它包含 (20) 的全部可见第二块尾。

## 5. R498 真行的 A 层正是接触对偶

取 R498 的一条通过所有原列测试的真左行。保该文实际低行右逆及全部高尾，并在其高目标用同一 $t^rQ/d^{C_D}$ 作规范化。由于 $\ell\le r$，高目标是
$$
k[[t]][\epsilon]/(t^S,\epsilon^2).
$$
相应三厚化行可写成
$$
\Phi=(A+B\zeta+C_2\zeta^2)
\frac{dt\wedge d\zeta}{\zeta^3},
\qquad \zeta=\log(Y/\psi)\pmod{F^3},
\tag{22}
$$
互为对偶的线束框仍按 R498 使用。这里用 $C_2$ 避免与曲线 $C$ 混淆。准确主部条件是
$$
A,B,C_2\in t^{-S}k[[t]],\qquad
A-2\eta_0B\in k[[t]].
\tag{23}
$$
于是
$$
\operatorname{pole}_P(A)\le S-h=q.
\tag{24}
$$

**定理 3。** (19) 的对偶将 $\Phi$ 送到 (14) 中的真实全局行
$$
\boxed{\quad
\Lambda_A(H)=\operatorname{Res}_{P}A e^2 H\,dt.
\quad}
\tag{25}
$$
特别地
$$
\boxed{\quad
\langle\Phi,\beta_\xi\rangle
=3\langle\Lambda_A,\beta_{\rm cont}(F)\rangle
=3\operatorname{Res}_{P}Ae^3\xi\,dt.
\quad}
\tag{26}
$$

**证明。** (17) 没有低行输出，故对它进行 R498 的实际低行消元时，低行右逆的系数为零；没有在这里漏掉一条高尾。再在真实高块除去 $t^rQ_{\rm phys}/d^{C_D}$，(17) 化为
$2a\epsilon\,e^2\eta_0 f$。全 $Q_{\rm phys}$ 的逆在这个高块只取所需两层；其额外项乘 $\epsilon^2$，在此为零。

R498 对 $z_0+\epsilon z_1$ 的行读法是
$$
\operatorname{Res}\left(C_2z_0+\frac{B-\eta_0C_2}{a}z_1\right)dt.
$$
作用于上述目标得
$$
2\operatorname{Res}e^2\eta_0(B-\eta_0C_2)f\,dt
=\operatorname{Res}Ae^2f\,dt.
$$
第一处删项合法，因为 $2h\ge S$，故 $\eta_0^2C_2$ 正则；第二处由 (23) 得到。这证明局部等式，并已由 (18) 保证其杀掉 $\operatorname{im}\bar E_q$。

全局线束身份也可直接核清。局部用 $1/F^3$ 平凡化
$\mathcal O_{3C}(3C)$；(22) 的双线束积限制到 $C$ 时，系数为
$$
\frac{Ae^3}{\psi}\,dt\wedge dY,
$$
因为 $F/\zeta\to e$ 且 $d\zeta=dY/\psi$ 于相对正规方向。
与 $N_C$ 的局部截面 $H/F$ 配对，再沿 $C$ 取伴随留数，得到
$$
\frac{Ae^3}{\psi F_Y}H\,dt=Ae^2H\,dt.
$$
(24) 给其至多 $qP$ 的极，$P$ 外的全局正则则来自 R498 同一个
$H^0(3C,\operatorname{Hom}(\mathscr I_\eta,K_X|_{3C}))$。
所以它确在 (14) 中，而不是任意指定的 Laurent 多项式。最后用 (16)、(21) 得 (26)。$\square$

只有通过全部原列测试的 $\Phi$ 才是原真行；本定理未把整个几何对偶空间冒称原左核，也未声称所有接触对偶行都能提升为这样的 $\Phi$。

## 6. 真正的来源吸收及显式充分范围

**定理 4。** 若 $\beta_{\rm cont}(F)=0$，则可在同一原来源中选一个首次修正，吸收整个 (20)。具体地，取 $H\in\mathcal H_1$ 满足
$$
\bar E_q(\bar H)=\mu_F.
$$
则
$$
R_\xi=-3\iota(H)\in\mathcal W_D,\qquad
\bar J\bar R_\xi=-\beta_\xi.
\tag{27}
$$
它的约化第一块及第三块均为零，低第二块也为零。

等价地，可以合法换用同一格中的因子提升
$\widetilde F_{\rm new}=\widetilde F-pH$。其接触值满足
$$
E_q(\widetilde F_{\rm new})=0\pmod{p^2},
$$
而实际立方来源的差为
$$
d^{-C_D}t^r\widetilde Q
(\widetilde F_{\rm new}^{\,3}-\widetilde F^{\,3})
=pR_\xi\pmod{p^2\mathcal W_D}.
\tag{28}
$$
新因子仍在同一一倍截面格、约化仍为 $F$，故全部角条件和原预算保留。由于 $e$ 为单位，新 $\xi$ 的前 $q$ 项为零，恰好使其原可见向量 (20) 为零。这个选择由真实 (12) 的可解性支付，不能在接触类非零时任意作出。

特别有统一的充分范围
$$
\boxed{\qquad q=h-k<\chi=-K_XC
\quad\Longrightarrow\quad
\beta_\xi\in\operatorname{im}\bar J.
\qquad}
\tag{29}
$$

**证明。** (27)、(28) 由 (18)、(21) 和立方展开得到。(29) 则因为 (14) 的线束次数为 $q-\chi<0$，没有非零截面，故 $\bar E_q$ 满射。$\square$

等号 $q=\chi$ 不包含于 (29)：此时零次线束可能平凡，不能仍以负度消失处理。本定理不要求原 $\gamma=0$ 或整个 $\bar J$ 满射，因而不是 R444 既有无首缺陷吸收范围的重复。

(27) 保持的是首次提升方程中已选低行修正的约化输出。若继续算原第三精度，必须把这个同一 $R_\xi$ 带入 R481；它在模 $p^2$ 的高尾及 carry 不能再删。

## 7. 未被吸收的完整 carry 与原 M

为了明确 (21) 只处理了哪一项，保 R502 的
$$
b_s=(t/w(t))^s,\qquad
V_0=q_Ce^3,
$$
$$
V_1=
\left.d^{-C_D}\left((\mathcal EQ)e^3+
\tfrac32Qe^2\mathcal E^2F\right)\right|_C.
\tag{30}
$$
其原全部首次 Bockstein 向量准确为
$$
\begin{aligned}
\beta_J(P^{\rm fact})
={}&
\epsilon V_0b_st^{h+k}u^3
+3a\epsilon^2V_0b_st^ku^2\\
&+\epsilon V_1b_st^{2h+k}u^4
+\beta_\xi .
\end{aligned}
\tag{31}
$$
于是余核中准确有
$$
[\beta_J(P^{\rm fact})]
=[\beta_{\rm carry}]
+3\bar T(\beta_{\rm cont}(F)),
\tag{32}
$$
其中 $\beta_{\rm carry}$ 就是 (31) 的前三项，不作进一步删减。
当 $r>2k$ 时 $V_1$ 项仍然可见；原 raw $\bar\Gamma$ 中
$\zeta^3=3a\eta_0^2\epsilon$ 仍可能非零。本篇既未改变这两个事实，也未把整原目标换成 $3C$ 的商后重算 (31)。

若保 R502 同一个低行右逆，令其归一化高尾贡献为
$\Lambda_{\rm low}$，并记 $f_2=(\mathcal E^2F)|_C$，则对 R498 真行的完整读法是
$$
\begin{aligned}
\langle\Phi,\beta_J(P^{\rm fact})\rangle
={}&
\operatorname{Res}\Big[
\frac{b_s}{a}e^3u^3t^{h+k-r}B\\
&\quad+
\frac{b_s}{a}u^4t^{2h+k-r}
\left(\tfrac32e^2f_2B-e^3C_2\right)
\Big]dt-\Lambda_{\rm low}\\
&+3\langle\Lambda_A,\beta_{\rm cont}(F)\rangle .
\end{aligned}
\tag{33}
$$
全 $Q_{\rm phys}$ 的逆在 R502 中已准确使其径向导数取消；(33) 仍保真正的 $f_2$ 项和实际低行高尾。即使 (29) 成立，(33) 前两行及 $\Lambda_{\rm low}$ 也不因此为零。

反向也须严格区分：$\beta_{\rm cont}(F)\ne0$ 不推出原首次 Bockstein 非零。首先 (19) 可能有核；其次 (32) 的两项可能在原余核相消。必须使用真正的原行与全部 carry 才能判定。

恢复物理矩阵继续使用
$$
M=c_*U_0m_{13}J,\qquad
K_2^{\rm red}(M)=\ker(\pi\beta_J),\qquad
G_2=C_2(J)/\overline H.
\tag{34}
$$
$P_{134}/U_0$、十三自由行、两条十三行 carry、R479 的同一来源边界输出及 R481 的同一修正第三精度全部保留。(21) 是相对 $J$ 中的准确像身份；它没有将任何相对必要条件直接升级成未付边界的全 $M$ 条件。

## 8. 真高轴与首共振的准确边界

由 $k<\ell\le r$ 得 $r-k\ge1$，所以
$$
q\le h\le\frac{s-1}{2}<s-3
\tag{35}
$$
最后一步使用 $p>83$。因此在 R498 所讨论的实际整高轴族
$$
g\longmapsto g\exp H,\qquad
H\in t^{s-3}\mathcal O[[t]]\pmod{p^2}
\tag{36}
$$
中，(12) 的整个矩阵及 (15) 的接触类不变。这里固定其余原低轴，且 (36) 只指已经支付的实际整高轴变化；没有把完整中央的真实参数另设为自由数。

(35) 也准确说明本篇的接触降阶没有补到 R467 位于 $t^{s-1}$ 的首共振。R498 原行的 Padé 转置仍只成立到其真实长度；本篇未将低阶等号延长成完整 ODE。

在典型高 $b$ 维数临界窗，$h$ 和 $q$ 可为 $b^2$ 量级，而 $\chi$ 仅为 $b$ 量级，(29) 因而不能自动覆盖。此时剩下的是实际有限矩阵 (12) 的特定 Bockstein (15)，其到原余核的真实像 (19)，以及 (33) 中不能省掉的 carry 配对。三条原完整中央也没有因此传播为任意 $H$ 或 $F^2H$ 的中央零；全局跨 $p$ 非零仍待证明。

本篇为精确来源、上同调与局部展开证明，没有新增素数扫描。R502 的固定实际证书仍只承担该文已声明的核验范围，不冒称已核验本篇的新交换图。
