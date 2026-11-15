# R246：十一维响应模的完整多平台接口、唯一修正与十三条相容关系

日期：2026-11-15。**完整纸面证明；没有新增科学计算、profile 求积、旧响应重编或目标评价。**

本稿接 [R244](R244-eleven-dimensional-response-module-pays-first-platform-and-eight-fluxes.md)。该文证明同一十一维真实响应模可以同时支付首平台双尾与八个 d 退化通量。本稿进一步把八个对应的局部平台都保留，给出这一响应模的准确像、唯一修正公式和全部有限线性相容关系。

关键新结论是：八个 d 通量加八个 e 平台已经在该模上单射。所以 R244 留下的一维不能同时保持其余全部 e 平台。加入八个 d 平台后，二十四个观测的像恰为十一维，有十三条独立相容关系；下文给出它们的构造公式，不把分别可修的条件当成可以顺序任意修复。

这只刻画已证明的十一维模 $\mathcal M$。没有把 $\mathcal M$ 替换成完整响应空间 $\mathcal R_0=\mathcal R\cap\ker\pi$，也没有把下文十三条关系称为整个 $\mathcal R_0$ 的消去泛函。完整 R225 period 商仍有其他活动区、通量、内部 Laurent 条件和平端 germ。

## 1. 固定同一个合法圆和全部实际平台

沿用 R244 最终选定的 R225 合法解析圆。在共同辅助坐标中，八个完整基本 pair 的平移与幅度为

$$
t_j=jL,\qquad
a_j=(-1)^j\binom7j^{1/3},\qquad
w_j=a_j^4>0,\qquad 0\le j\le7.
\tag{1}
$$

每个基本 pair 都包括自己的三个左矩补偿和原矩形四 step。最终正仿射压回物理 I 和共同归一化已由 R244 支付。以下在辅助坐标写公式；实际变换只改变已明确的可逆算子和非零行因子。

在第 j 个 packet 的原 f 上升 step 之前，取其左补偿已经结束后的共同零 gap，记为 $C_j$。所有 profiles 在 $C_j$ 上均为零，右方仍保留该矩形及后续完整 packet。

对 whole pure 零输出写

$$
V_\theta=\sin^2\theta\,V_d+
2\sin\theta\cos\theta\,V_e.
\tag{2}
$$

定义两个平台观测

$$
D_j(V)=[x^2]V_d|_{C_j},\qquad
E_j(V)=[x^2]V_e|_{C_j}.
\tag{3}
$$

本稿用于 $\mathcal M$ 的原式均在这些 gap 留下二次以下多项式，故 (3) 精确等价于对应目标二阶导数的一半。对更大的目标类，只要沿用 R230 的真实 canonical 平台二次界，仍可按 (3) 读取；若另采用不具有该界的目标空间，应改用固定 gap 内的实际二阶导数查询，并另外保留整个平台函数门，不能把一个数代替整个函数。

八个 d 通量仍为 R219 的带平台修正量：

$$
\begin{aligned}
F_j(V)
={}&\int_{a+t_j}^{x_*+t_j}
 f'(x)V_d''(x)\,dx\\
&-\{f(x_*+t_j)-f(a+t_j)\}V_d''(a+t_j).
\end{aligned}
\tag{4}
$$

这里 a 是基本 pair 原 f 上升端，$x_*$ 是 R215 的
$A_f(x_*)=0$、$f_*'(x_*)>0$、$f_*''(x_*)>0$ 内部点。所有右锚、补偿和其他 packet 的二次尾保留。

对任意允许的全 I 光滑 gauge w，$L_f(w)''=0$ 于每个 f 常平台；又 R181 的通量身份使式 (4) 为零。因此 (3)、(4) 都是完整 period range 的必要观测，而不是只对局部支撑 gauge 成立。

## 2. 已付十一维模及三个尾算子

R244 已证明

$$
\mathcal M=\operatorname{span}\{e_0,\ldots,e_{10}\}
\subset\mathcal R_0,\qquad
\dim\mathcal M=11,
$$

$$
e_n=\frac{(-1)^n(10-n)!}{10!}\delta^nK,\qquad
Ne_n=ne_{n-1}.
\tag{5}
$$

记基本包的 d 通量为 $\mathcal F_*$，并置

$$
F_m^*=\mathcal F_*(e_m),\qquad
F_0^*=-\frac8{45}\bigl(f_*''(x_*)\bigr)^5\ne0.
$$

若 $A=\sum u_ne_n$，定义其准确多项式坐标

$$
P_A(t)=\mathcal F_*(\mathcal T_tA)
=\left(\sum_{m=0}^{10}\frac{F_m^*}{m!}D_t^m\right)
\sum_{n=0}^{10}u_nt^n.
\tag{6}
$$

$A\mapsto P_A$ 是
$\mathcal M\simeq\operatorname{Pol}_{\le10}$ 的线性同构，且

$$
F_j(A)=a_j^5P_A(t_j).
\tag{7}
$$

令 $\ell_d,\ell_e$ 为一个完整基本 pair 的全左二次尾，$\ell_{\rm c}$ 为该 pair 的整个左补偿的 d 二次尾。补偿的 e 输出在整个 $\mathcal M$ 上恒零，已由 R244 的 pure 零双线性式与单层原积分分解支付。

对任意一个这种真实线性泛函 $\ell$，定义

$$
\mathfrak d_\ell(z)
=\frac{\displaystyle\sum_{m=0}^{10}
 \ell(e_m)z^m/m!}
 {\displaystyle\sum_{m=0}^{10}
 F_m^*z^m/m!}
\pmod {z^{11}}.
\tag{8}
$$

分母常数项非零，故它是在
$\mathbb R[z]/(z^{11})$ 中唯一确定的有限多项式。没有把原积分值独立赋值；式 (8) 每个系数都来自同一个固定基本 pair 的完整原式。

简记

$$
\mathfrak d_d=\mathfrak d_{\ell_d},\qquad
\mathfrak d_e=\mathfrak d_{\ell_e},\qquad
\mathfrak d_c=\mathfrak d_{\ell_{\rm c}}.
$$

准确有

$$
\ell(\mathcal T_tA)=\mathfrak d_\ell(D_t)P_A(t).
\tag{9}
$$

R244 已核的首项尤其给

$$
\boxed{\mathfrak d_e(z)=z^3C(z),\qquad
C(0)=\gamma=
\frac{\mathsf J}{45F_0^*}\ne0,}
\qquad
\mathsf J=\int g_*f_*''(f_*''')^2.
\tag{10}
$$

可取 $\deg C\le7$；作为算子时，它作用在下文正确的多项式空间上，而不是在无限函数空间中形式求逆。

## 3. 八个平台的完整前缀公式

在 $C_j$ 上，所有编号小于 j 的完整 packet 已位于查询点左方，真实响应输出为零。编号大于 j 的包留下全左二次尾。当前 j 包的左补偿也已经结束，必须从当前包全尾中减去它的原尾。

本链具有 R219 已证明的局部四次密度加单层右积分结构，所以该分解准确，无嵌套历史交叉项遗漏。由四次幅度齐次性，

$$
\boxed{
E_j(A)=\sum_{k=j}^7w_k\,
\mathfrak d_e(D)P_A(t_k),
}
\tag{11}
$$

$$
\boxed{
D_j(A)=\sum_{k=j}^7w_k\,
\mathfrak d_d(D)P_A(t_k)
-w_j\mathfrak d_c(D)P_A(t_j).
}
\tag{12}
$$

式 (12) 的补偿减项对每个 j 都存在，不能只在第一个 packet 保留。它是实际已经越过补偿支撑的因果修正，不是重置原右锚。

定义终止记号

$$
E_8(A)=0.
\tag{13}
$$

它代表最后完整 packet 右方的零输出，并非增加第九个未知平台值。于是

$$
\boxed{
\frac{E_j(A)-E_{j+1}(A)}{w_j}
=\mathfrak d_e(D)P_A(t_j).
}
\tag{14}
$$

真实右 collar 的零值是式 (13) 的来源。若改用更大的非右锚目标类，其右端条件必须另列，不能把未知右尾擅自设零。

## 4. 八个 d 通量加八个 e 平台已经单射

**定理 1。** 在上述同一个合法圆上，映射

$$
A\longmapsto
(F_0(A),\ldots,F_7(A),E_0(A),\ldots,E_7(A))
\quad(A\in\mathcal M)
\tag{15}
$$

单射，其真实秩为十一。

**证明。** 若全部 E 为零，式 (14) 使多项式

$$
R_A(t)=\mathfrak d_e(D)P_A(t)
=D^3C(D)P_A(t)
$$

在八个互异节点 $t_j$ 为零。由 $\deg P_A\le10$，有
$\deg R_A\le7$，故 $R_A\equiv0$。

$C(0)=\gamma\ne0$，所以 $C(D)$ 在每个有限次数多项式空间上都可逆，并与 $D^3$ 交换。因此 $R_A=0$ 等价于
$D^3P_A=0$，即 $\deg P_A\le2$。再由全部 F 为零及式 (7)，这个二次以下多项式在八点全零，故 $P_A=0$。由式 (6) 的同构得 $A=0$。证毕。

由完整 period range 必须消掉式 (15)，立即得

$$
\boxed{
\mathcal M\cap
\{A:\ A_d,A_e\in L_f(\mathcal X)\}
=\{0\}.
}
\tag{16}
$$

因此完整 R225 障碍映射在 $\mathcal M$ 上的像也恰为十一维。这个结论不需要把尚未评价的端点 germ 当成零；一个已付的有限必要观测组已经分离了整个模。

特别地，R244 十观测共同核是一维。其中非零向量的八个 F、首 d/e 平台都为零，但至少一个其他 $E_j$ 必须非零。否则它会落入式 (15) 的零核。这一维不能被当成保持全部平台的剩余自由控制。

## 5. 十六观测的五条准确相容关系与唯一右逆

现在给出式 (15) 对任意指定数据的完整成员判据，不只报告秩。

设目标数据为

$$
\mathbf f=(\mathsf f_0,\ldots,\mathsf f_7),\qquad
\mathbf e=(\mathsf e_0,\ldots,\mathsf e_7),
\quad \mathsf e_8:=0.
\tag{17}
$$

### 5.1 由 e 平台准确重建七次多项式

定义

$$
h_j=\frac{\mathsf e_j-\mathsf e_{j+1}}{w_j},
$$

$$
R_{\mathbf e}(t)=
\sum_{j=0}^7h_j
\prod_{k\ne j}\frac{t-t_k}{t_j-t_k}.
\tag{18}
$$

这是唯一满足 $R_{\mathbf e}(t_j)=h_j$ 的次数至多七多项式。

任选一个固定积分基点 $t_b$，例如辅助坐标中的 $t_b=0$，定义真实多项式积分

$$
\mathcal I_{t_b}^3R(t)
=\frac12\int_{t_b}^{t}(t-s)^2R(s)\,ds.
\tag{19}
$$

它的三阶导数为 R，在 $t_b$ 的零、一次、二次导数为零；次数至多十。

在 $\operatorname{Pol}_{\le10}$ 上写

$$
C(D)=\gamma\,(\mathrm{id}+B(D)),\qquad B(0)=0.
$$

D 在此空间上满足 $D^{11}=0$，所以 $B(D)^{11}=0$，有限逆准确为

$$
C(D)^{-1}
=\gamma^{-1}\sum_{n=0}^{10}(-B(D))^n.
\tag{20}
$$

取

$$
P_{\mathbf e}^0
=C(D)^{-1}\mathcal I_{t_b}^3R_{\mathbf e}
\in\operatorname{Pol}_{\le10}.
\tag{21}
$$

于是 $\mathfrak d_e(D)P_{\mathbf e}^0=R_{\mathbf e}$。所有解准确为

$$
P=P_{\mathbf e}^0+q,\qquad \deg q\le2.
\tag{22}
$$

改变式 (19) 的基点仅使两个三重积分之差为二次以下多项式；$C(D)^{-1}$ 保该子空间。因此式 (21) 的改变仍可完全吸收在 q 中，不影响下面的判据或最终 P。

### 5.2 前三个 F 值确定全部二次自由度

由 j=0,1,2 的目标值，定义

$$
r_j=\frac{\mathsf f_j}{a_j^5}-P_{\mathbf e}^0(t_j),
$$

$$
q_{\mathbf f,\mathbf e}(t)
=\sum_{j=0}^2r_j
\prod_{\substack{0\le k\le2\\k\ne j}}
\frac{t-t_k}{t_j-t_k}.
\tag{23}
$$

令

$$
P_{\mathbf f,\mathbf e}
=P_{\mathbf e}^0+q_{\mathbf f,\mathbf e}.
\tag{24}
$$

它是唯一可能同时匹配全部 E 与前三个 F 的多项式。剩余五个 F 必须并且只须满足

$$
\boxed{
\mathsf f_j=a_j^5P_{\mathbf f,\mathbf e}(t_j),
\qquad j=3,\ldots,7.
}
\tag{25}
$$

这些就是式 (15) 像的五条完整相容关系。

若它们成立，式 (6) 的有限逆给唯一响应：

$$
p_A=
\left(\sum_{m=0}^{10}
 \frac{F_m^*}{m!}D^m\right)^{-1}
 P_{\mathbf f,\mathbf e},\qquad
A=\sum_{n=0}^{10}[t^n]p_A\,e_n.
\tag{26}
$$

这个逆同样是有限多项式逆，常数项 $F_0^*\ne0$。没有重新编译任何原列，也没有把 tail 值当成自由符号来求解。

**独立性。** 八个 E 与前三个 F 可任意指定：式 (18)–(24) 对它们给唯一 P。式 (25) 分别确定其余五个 F 坐标，因此五条线性关系彼此独立。像维数恰为 $16-5=11$，与定理 1 一致。

## 6. 加上八个 d 平台：十三条独立相容关系

再指定

$$
\mathbf d=(\mathsf d_0,\ldots,\mathsf d_7).
$$

在式 (25) 已成立时，唯一候选 $P=P_{\mathbf f,\mathbf e}$ 还必须满足

$$
\boxed{
\mathsf d_j
=\sum_{k=j}^7w_k\mathfrak d_d(D)P(t_k)
-w_j\mathfrak d_c(D)P(t_j),
\qquad 0\le j\le7.
}
\tag{27}
$$

**定理 2。** 二十四个指定数据 $(\mathbf f,\mathbf e,\mathbf d)$ 可由同一个
$A\in\mathcal M$ 取得，当且仅当五条式 (25) 和八条式 (27) 全部成立。成立时 A 由式 (26) 唯一给出。

证明是式 (7)、(11)、(12) 的必要性，以及式 (18)–(26) 的构造充分性；不是只由维数计数推出存在。

十三条关系确实独立：以八个 E 与前三个 F 为自由坐标，式 (25) 分别解出另五个 F，式 (27) 再分别解出八个 D。每条新增式在一个独有的指定数据坐标前系数为 1。故二十四观测像是一个十一维线性图，其余维数为十三。

式 (27) 中不可删去 $w_j\mathfrak d_c(D)P(t_j)$。若误用全左尾代替局部 gap，得到的会是另一套不对应实际圆的关系，R244 的十观测满射也随之失去原证明。

## 7. e 通量的准确接口，不作未付零宣称

八个原 d 通量并不代表 e 通量。对 e 目标另定义

$$
\begin{aligned}
F_j^e(V)
={}&\int_{a+t_j}^{x_*+t_j}
 f'(x)V_e''(x)\,dx\\
&-\{f(x_*+t_j)-f(a+t_j)\}V_e''(a+t_j).
\end{aligned}
\tag{28}
$$

对单基本 pair 记相应实际泛函为 $\mathcal G_*$。设

$$
G_m^*=\mathcal G_*(e_m),\qquad
\mathfrak d_g(z)=
\frac{\displaystyle\sum_{m=0}^{10}G_m^*z^m/m!}
{\displaystyle\sum_{m=0}^{10}F_m^*z^m/m!}
\pmod {z^{11}}.
\tag{29}
$$

与 R219 完全相同的单层分包及平台减项给

$$
\boxed{F_j^e(A)=a_j^5\mathfrak d_g(D)P_A(t_j).}
\tag{30}
$$

这是一个真实单包泛函接口，保全部右尾和 mixed 规范。本文没有评价 $G_m^*$，没有把它们冒作零，也没有把它们和 $F_m^*$ 当成任意独立参数。

当式 (25)、(27) 已给唯一 A 时，指定八个 e 通量是否可同时取得，准确等价于再检验式 (30) 的八条值。不存在一个尚可任意使用的 $\mathcal M$ 核来继续调整它们。对于含全部这些三十二个数的目标列表，前面的唯一右逆仍适用；额外数据必须与这个同一 A 相符。

## 8. 与完整 R225 range、端点 germ 和真实响应空间的边界

### 8.1 哪些首端结构已继承

R226 已证明每个 $\delta^nK$ 在各完整 packet 的相应原 f-up 左端，按实际平移、宽度及有符号幅度都有

$$
G=P_2+p^4R,\qquad R\in\mathscr A.
\tag{31}
$$

因此 $\mathcal M$ 在这些端点的首一次层和二次主部都为零。若相应真实平台另已付，扣去该平台后的零左通量 germ 自动光滑。

但这只涵盖这些 f-up/g=0 左端。其他 f 下降端可能有非零常值 g；补偿包可能有内部 p 零点；其他 A 零点及各活动包右端还有自己的通量和延拓条件。本文没有把式 (31) 外推到所有端点，也没有借有限维性删除任何 R225 条件。

### 8.2 对一个实际目标的唯一候选

设 V 是固定圆上的实际 whole pure 零目标。要用 $\mathcal M$ 修正它的完整 period，必须先取其真实
$(\mathbf f,\mathbf e,\mathbf d)$。若式 (25) 或 (27) 失败，则不存在
$A\in\mathcal M$ 使 $V-A$ 通过这组必要观测。

若这些式子成立，式 (26) 给唯一候选 A。然后必须对同一个 $V-A$ 检查：

- 式 (28) 的 e 通量及各活动包其他总通量；
- 全部其他平台的完整函数条件；
- R225 内部 p/A 零点的 Laurent 条件；
- 每个真实左右端 germ；
- 原共同右锚的两个积分常数。

必要时可使用 R225 在真实有限 U 上的完整观测商；本文没有计算该商，也没有证明所列有限观测已经忠实于全部 U。唯一性只是指 $\mathcal M$ 中的候选，不是说实际所有 gauge 或完整 $\mathcal R_0$ 中的候选唯一。

### 8.3 不能把本模的关系扩大为全响应障碍

式 (25)、(27) 是准确消掉 $\mathcal M$ 的十三条数据关系。它们尚未被证明消掉
$\mathcal R_0$ 的其他真实响应；若一个实际目标违反其中一条，只能据此排除用本模完成修正，不能立即判完整 period 不可解，不能判 $\lambda_+$ 已经由它读出。

同样，式 (16) 说明本模在完整固定圆 period 商中单射，而不是说整个响应空间在该商中单射。R213 的合法八矩 gauge 子族本来就可以提供其他落入完整 $L_f$ 像的响应。

本稿由此把后继研究变成一个准确的问题：在已经被八个 e 平台与八个 d 通量唯一锁定的本模修正之外，完整 $\mathcal R_0$ 还有哪些方向能支付余下相容关系及完整 R225 障碍？新增单个本模列或继续顺序修复同一平台，不会增加可用自由度。所有实际成本实现、完整基准及同一个 period/ruling gauge 的联合义务仍另行保留。

