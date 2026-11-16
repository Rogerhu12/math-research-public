# R890 — 原全分歧有限类的加权临界值矩阵与真实系数读者

日期：2026-11-16。**状态：下列原次数帽内的完整值像、行列式常数、任意 DVR 上的有限障碍行，以及固定十九角和全球连接类的读取均已证明。没有证明原 $M$ 强迫这些行同时为零，也没有求出 $\mathfrak o_D(K_2)$ 的像。**

本篇把 [原有限纤维商](../notes/2026-11-16-r872-native-finite-fiber-quotient-and-cubic-ramification.md) 中“其余分歧条件”写成有限矩阵。非固定首一图上的矩阵只有 $b\times b$，其行列式准确为原 $\operatorname{Norm}(YF_Y)$ 的三次方乘显示的单位。矩阵读取整个纤维的概形，不要求曲线光滑或分歧点简单。固定角、无穷远和真实 $H^1$ 连接核另以同一个原格的明确矩阵保留。

## 1. 同一原来源和全局类

保持
$$
\mathcal W_D=\bigoplus_{n=0}^{D}Y^nq_n(t)k[t]_{\le e_{n+1}},
\qquad L=E+40,\qquad E=Y\partial_Y,
$$
原 $F$、$b=\deg_YF$、十九角及
$$
\boxed{D\ge4b,\qquad p>D+40,\qquad p>211.}
\tag{1}
$$
原 $F$ 不可约、不是 $Y$，且物理点有 $F_Y(0,1)\ne0$，因此
$$
\gcd(F,YF_Y)=1\quad\text{于 }k(t)[Y].
\tag{2}
$$
置
$$
\mathscr V_j=\mathcal W_D\cap F^jk(t)[Y],\quad
\mathscr J_3=L^{-1}\mathscr V_3,\quad
\mathfrak o_D(R)=[R]\in
\mathcal W_D/(\mathscr V_1+\mathscr J_3).
\tag{3}
$$
$\mathfrak o_D$ 是全球原来源类，包含全部有限纤维和实际连接类。
本文的矩阵是 (3) 的读者，**不是另加到原 $M$ 上的算术零行**。

以下所有 $\operatorname{rem}_F$ 都是首一多项式除法，取次数严格小于 $b$ 的余数。
$L^{-1}$ 只把 $Y^n$ 的系数除以 $40+n$；(1) 支付用到的全部分母。

## 2. 非固定首一图的真实 b 列

令 $\mathcal O$ 为底曲线某个非固定点的 DVR，均匀元为 $\pi$，
分式域为 $K$。
这里原来源局部恰为
$$
\mathscr W_{\mathcal O}=\mathcal O[Y]_{\le D}.
$$
假设原 $F$ 在此图的最高 $Y$ 系数是单位，除去这个底单位后写成
$$
F\in\mathcal O[Y],\qquad F\text{ monic},\qquad\deg_YF=b .
$$
令
$$
A_F=\mathcal O[Y]/F,\qquad e=YF_Y\in A_F.
$$
定义原加权临界值矩阵
$$
\boxed{
\mathsf T_F=
\left(
 [Y^i]\operatorname{rem}_F
       L^{-1}(F^3Y^j)
\right)_{0\le i,j<b}.
}
\tag{4}
$$
它的每一列都来自原局部来源，次数至多 $4b-1\le D$。
没有把 $Y$ 的 $p$ 次幂或新的 theta 列加入来源。

**命题 1（完整局部像）。** 同一原 $\mathbf J_3$ 在 $A_F$ 上的值像准确为
$$
\boxed{
\operatorname{im}(\mathbf J_3\longrightarrow A_F)
=\mathsf T_F\mathcal O^b.
}
\tag{5}
$$
因此整个本纤维有限商准确为
$$
\boxed{\mathscr T_{D,\mathcal O}\simeq
        \operatorname{coker}_{\mathcal O}\mathsf T_F.}
\tag{6}
$$

**证明。** 每个 $J\in\mathbf J_3$ 唯一写成
$J=L^{-1}(F^3A)$，其中 $\deg A\le D-3b$。
对于任意 $\deg B\le D-4b$，
$$
L(F^4B)=F^3\bigl(4eB+FLB\bigr).
\tag{7}
$$
所以从 $A$ 减去 $4eB+FLB$，只使 $J$ 减去 $F^4B$，
不改变其在 $A_F$ 的值。

若 $A$ 的最高次数为 $n\ge b$，取 $k=n-b$。
因 $F$ monic，
$$
4eY^k+FL(Y^k)
=(40+4b+k)Y^{b+k}+\text{较低次项}.
\tag{8}
$$
这里 $k\le D-4b$，所以 $40+4b+k\le D+40<p$，是原单位。
依次选择 $B$ 的最高系数即可在 $\mathcal O$ 内消去所有 $n\ge b$。
每一步的 $F^4B$ 仍有次数至多 $D$；没有借用无帽的高 charge 除法。
最后得到次数小于 $b$ 的 $A_{\rm red}$，其值正是 (4) 的列组合。
反向由 (4) 本身成立。这证明 (5)。

又 $\mathscr W_{\mathcal O}\to A_F$ 满射，核恰为
$\mathbf V_1$，因为 $F$ monic 且 $D\ge b$。
再模掉 (5) 即得 (6)。$\square$

上述消去使用的是原一阶算子 (7)，不是把 $A$ 普通除以 $F$。
系数 $40+4b+k$ 和范围 $k\le D-4b$ 是同预算返回必需的部分。

## 3. 行列式的准确常数

**定理 2。** 在上述任意 DVR 上，
$$
\boxed{
\det\mathsf T_F=
\frac{(-6)^b}
 {\displaystyle\prod_{n=0}^{4b-1}(40+n)}
 \operatorname{Norm}_{A_F/\mathcal O}(e)^3 .
}
\tag{9}
$$
右侧的显示常数为单位。这个恒等式在范数不是单位、
特殊纤维不约化或原曲线奇异时仍成立。

**证明。** 先只用次数至多 $4b-1$ 的自由多项式，考虑方阵映射
$$
\mathcal M:
\mathcal O[Y]_{<4b}
\longrightarrow
\mathcal O[Y]_{<3b}\oplus\mathcal O[Y]_{<b},
\qquad
W\longmapsto
\bigl(\operatorname{rem}_{F^3}LW,\operatorname{rem}_FW\bigr).
\tag{10}
$$
首一 $F$ 给源的 $F$-adic 基
$$
Y^iF^j,\qquad 0\le i<b,\quad 0\le j\le3,
$$
和第一目标的对应三层基。
它们对按次数排序的普通幂基都是首一三角变换，行列式为一。

先把第二目标的 $b$ 行移到最前面，再用它消去源的 $j=0$ 块。
这个行排列的符号是
$(-1)^{3b^2}=(-1)^b$。
剩下源的 $F,F^2,F^3$ 三层到第一目标的三个对角块，
准确是乘
$$
e,\qquad 2e,\qquad 3e
$$
的 $b\times b$ 矩阵。
零阶 $40$、$E$ 对低次系数的作用以及除法产生的其它项只进入较高的 $F$ 层。
因此
$$
\det\mathcal M=(-1)^b6^b\operatorname{Norm}(e)^3.
\tag{11}
$$

另一方面，源取另一组真基：
$$
L^{-1}(1),\ldots,L^{-1}(Y^{3b-1}),\quad
L^{-1}(F^3),\ldots,L^{-1}(F^3Y^{b-1}).
$$
未作 $L^{-1}$ 前，这仍是首一三角基。
作 $L^{-1}$ 的行列式是
$\prod_{n=0}^{4b-1}(40+n)^{-1}$。
在这组基下，(10) 的前 $3b$ 个目标行为
$(I_{3b},0)$，最后 $b$ 个列的末块恰为 $\mathsf T_F$。
所以
$$
\det\mathsf T_F
=\det\mathcal M\prod_{n=0}^{4b-1}(40+n)^{-1}.
$$
与 (11) 合并得到 (9)。整个证明在原自由模中进行，
未把 $e$ 取逆。$\square$

还可准确写成
$$
\operatorname{Norm}(e)=
\operatorname{Res}_Y(F,YF_Y)
=(-1)^{b(b+1)/2}F(t,0)\operatorname{disc}_YF.
\tag{12}
$$
用范数版本 (9) 可以避免不同判别式号约定。
条件 (2) 保证此范数在 $K$ 内非零；
在 DVR 中可以有任意已由原 $F$ 决定的正估值。

## 4. 同一个 R 的有限障碍行：不需要逆矩阵精度

令
$$
r_F(R)=\operatorname{rem}_FR\in\mathcal O^b,\qquad
d_{\mathcal O}=3v_\pi(\operatorname{Norm}(e)).
\tag{13}
$$
由 (9)，$d_{\mathcal O}=v_\pi(\det\mathsf T_F)$。
定义原同来源有限读取
$$
\boxed{
\Omega_{\mathcal O}(R)=
 \operatorname{adj}(\mathsf T_F)\,r_F(R)
 \pmod{\pi^{d_{\mathcal O}}}
 \quad\in(\mathcal O/\pi^{d_{\mathcal O}})^b.
}
\tag{14}
$$
$d_{\mathcal O}=0$ 时目标为零，正好对应局部矩阵可逆。

**推论 3。** 对任意原 $R$，
$$
\boxed{
\Omega_{\mathcal O}(R)=0
\iff r_F(R)\in\mathsf T_F\mathcal O^b
\iff \mathfrak o_D(R)\text{ 的本纤维分量为零}.
}
\tag{15}
$$

事实上在 $K$ 中唯一的系数向量是
$$
A_{\rm red}
=\frac{\operatorname{adj}(\mathsf T_F)\,r_F(R)}
       {\det\mathsf T_F}.
$$
分母是 $\pi^{d_{\mathcal O}}$ 乘单位。
故它整当且仅当 (14) 为零，再用命题 1。
这既处理单位范数，也处理非单位范数；没有用一个只在可逆点成立的公式
去外推整个分歧纤维。

式 (14) 可能含冗余行，但其**联合核准确**。
它不声称这些 $b\,d_{\mathcal O}$ 个剩余域坐标独立，
也不把所有局部 Smith 因子认成同一个 $\operatorname{Norm}(e)^3$。
它给原有限商到显示目标的一个单射，而不是满射。

如果只要判断 (14) 是否为零，在准确 $d_{\mathcal O}$ 已知后，
$\mathsf T_F$ 和 $r_F(R)$ 模 $\pi^{d_{\mathcal O}}$ 足够；
只计算伴随矩阵和乘法，不展开任何分母单位的逆。
若要读取 $A_{\rm red}$ 的具体负幂系数，才须另外保相应分母单位的精度。
本篇不把后一问题偷换为前一精度门。

$F$ monic 时，(4) 和 (14) 都可仅用原多项式乘法、
逐 charge 除以 $40+n$ 及首一余式计算。
它们对同一 $R$ 是明确的有限系数线性行。
对闭点须保全部 $k(\mathcal O)/k$ 坐标；
若改写成对偶行，应使用完整残域迹配对，不能只取一条迹或遗漏闭点次数。

## 5. 原十九角和非首一图的完整整矩阵

(4) 不适用于把原固定角格擅自放宽为
$\mathcal O[Y]_{\le D}$ 的情形。
若最高 $Y$ 系数不是单位，也不能直接先除以它再忘记来源帽。
以下给这些纤维的同来源矩阵。

仍令 $c=C_D$，在系数记录中用
$$
\widehat R=d^cR,\qquad
\widehat F\in k[t,Y]\text{ 为原本原代表}.
$$
按原有限纤维证明的 Gauss 值，置
$$
\begin{aligned}
\alpha_{j,n,\nu}
 &=\max\left(0,
 \left\lceil\frac{c_\nu-jv_\nu(\widehat F)-w_\nu n}{e_\nu}
 \right\rceil\right),\\
\beta_{j,n}
 &=\left\lfloor\frac{9n+2c+8+jv_\infty(\widehat F)}2\right\rfloor,\\
\ell_{j,n}
 &=\beta_{j,n}-\sum_\nu\alpha_{j,n,\nu}\deg\nu .
\end{aligned}
\tag{16}
$$
各有限角的 $(e_\nu,w_\nu,c_\nu)$ 依次为
$(4,-1,-2)$（$t,h_7$）、$(3,-1,-1)$（$t-1$）、
$(2,1,2c)$（$d$），无穷远下界为 $-2c-8$。
$j=0,1,3,4$，次数范围为 $0\le n\le D-jb$。

在有限角 $\nu$ 的 DVR 中取
$$
r_{j,n}=\pi_\nu^{\alpha_{j,n,\nu}};
$$
在底无穷远 $T=1/t$ 中取
$$
r_{j,n}=T^{-\beta_{j,n}}.
$$
在非固定有限点取 $r_{j,n}=1$。
这些分别是原 coefficient 线束的局部生成元；
可以同时乘实际单位，但不能独立改变它们的阶。

写 $\widehat F_i=[Y^i]\widehat F$，
$\widehat F^{(3)}_i=[Y^i]\widehat F^3$，负下标记零。
以 $r_{0,i}Y^i$ 为原目标基，构造
$$
\boxed{
\begin{aligned}
\mathsf C^{(1)}_{i,n}
 &=\frac{r_{1,n}}{r_{0,i}}\,\widehat F_{i-n},
   &&0\le n\le D-b,\\
\mathsf C^{(3)}_{i,n}
 &=\frac{r_{3,n}}{(40+i)r_{0,i}}\,
                       \widehat F^{(3)}_{i-n},
   &&0\le n\le D-3b,\\
\mathsf C_{\mathcal O}
 &=(\mathsf C^{(1)}\mid\mathsf C^{(3)}).
\end{aligned}}
\tag{17}
$$
由原 Gauss 乘积准则，每一项都是本 DVR 的整元素。
这个陈述包括无穷远真实框；此处不能仅按原多项式的裸次数判断整性。

输入仍为同一个原来源：
$$
\mathbf r_{\mathcal O}(R)
=\left(\widehat R_i/r_{0,i}\right)_{0\le i\le D}.
\tag{18}
$$
(17) 的像准确是 $\mathbf V_1+\mathbf J_3$，
因两组列分别是原剩余线束的真实局部基。
其泛点满秩，由原
$\mathbf V_1\cap\mathbf J_3=\mathbf V_4$
及 (1) 的秩计算保证。

因此，在任意这些 DVR 上作真实 Smith 消元
$$
U_{\mathcal O}\mathsf C_{\mathcal O}V_{\mathcal O}
=(\operatorname{diag}(\pi^{a_0},\ldots,\pi^{a_D})\mid0),
$$
就得到准确有限行
$$
\boxed{
[U_{\mathcal O}\mathbf r_{\mathcal O}(R)]_i
 \pmod{\pi^{a_i}}\quad(0\le i\le D).
}
\tag{19}
$$
这里 $U_{\mathcal O},V_{\mathcal O}$ 是该 DVR 的单位矩阵，
$a_i\ge0$。它们可由 (17) 的原有限多项式／有理系数计算，
没有新算术输入或自由观测列。

(17)–(19) 保留所有固定角、正水平、
同一底纤维中的多个分支、非首一系数和奇点。
若本纤维属于第2节的首一无角图，则其零条件与 (14) 完全相同；
两种读取不产生两份可独立赋值的障碍。

## 6. 读完全部纤维后仍须同一连接类

各局部有限行都为零，只得到
$$
\widehat R\in H^0(\mathbf V_1+\mathbf J_3).
$$
不能由此直接删掉全球拼接。
原正合列给唯一相应的连接类
$$
\delta_R\in
\mathscr E_D=
\ker\!\left[
H^1(\mathbf V_4)\longrightarrow
H^1(\mathbf V_1)\oplus H^1(\mathbf J_3)
\right].
\tag{20}
$$
它来自**同一个** $R$ 的局部分解。

具体地，在各底开集选 (17) 的实际局部解
$\widehat R=V_a+J_a$。
交叠上 $(V_a-V_b,J_a-J_b)$ 必为
$(\widehat F^4A_{ab},-\widehat F^4A_{ab})$。
这些 $A_{ab}$ 在原剩余束 $\mathscr A_4$ 中组成一个
Čech 上同调类，就是 (20)。
其消失当且仅当可改这些同一局部解而拼成原全局分解。
改变局部解只加一个 coboundary。

全矩阵来自
$$
A\longmapsto
\left(\widehat F^{\,3}A,\;
 -4(E\widehat F)A-\widehat F LA\right):
\mathscr A_4\longrightarrow\mathscr A_1\oplus\mathscr A_3.
\tag{21}
$$
每个负次数项的 Laurent 余类都须保其 (16) 的固定角框。

在当前真实 $t^3F^4q$ 窗口，原两 charge 连接核证明又给：
若 quartic 余乘子最低 $Y$ 次数为 $j$，则 $j\le2$；
$\delta_R$ 只可能有 charge 零、一分量。
记这些实际类为 $a_0,a_1$，
$f_0=[Y^0]\widehat F$、$f_1=[Y^1]\widehat F$。
它们满足
$$
[f_0a_0]_{3,0}=0,\qquad
[41f_0a_1+44f_1a_0]_{3,1}=0.
\tag{22}
$$
式 (22) 描述连接核所在的真实空间；
要使 $\delta_R=0$，还必须让由该 $R$ 算出的类本身为零，
不能另选一个满足 (22) 的零代表替换它。

若 $j=0$，原连接核已证明为零；此时全部 (14)、(19) 为零
确实足以判定 $\mathfrak o_D(R)=0$。
$j=1,2$ 时仍保 (20)，其维数上界分别为三、十四。

## 7. 不经局部分解的全来源实现

也可以把相同条件直接做成一个有限域矩阵，保留所有全球边界。
对每个 $\ell_{j,n}\ge0$，令
$$
q_{j,n}^{\rm res}(t)=\prod_\nu\nu(t)^{\alpha_{j,n,\nu}},
$$
取
$$
Y^nq_{j,n}^{\rm res}(t)t^a,\qquad0\le a\le\ell_{j,n}
$$
为 $\mathscr A_j$ 的原全局基。
负次数项不提供全局列，但仍通过第6节的连接类解释局部／全局差异。

在原 $\mathscr W$ 的全局基中，将所有
$$
\widehat F\,Y^nq_{1,n}^{\rm res}t^a,\qquad
L^{-1}\!\left(\widehat F^3Y^nq_{3,n}^{\rm res}t^a\right)
\tag{23}
$$
写成系数列。
Gauss 准则保证它们都是真来源；沿每个 charge 除原固定乘子后，
剩余次数帽由 (16) 已支付。
记所得矩阵为 $\mathsf C_{\rm glob}$。
那么
$$
\boxed{
\mathfrak o_D(R)=0
\iff \mathbf r_{\rm glob}(R)\in\operatorname{im}\mathsf C_{\rm glob}.
}
\tag{24}
$$
取 (23) 的完整左核即可得到无须逐点拼接的全球有限行。
这些行与第4–6节有相同联合核；不能把它们解释成
$\bar M$ 的左核，更不能分别向每个行赋来源。

因此，给定原 $F,D,p$ 和同一个真实修正 $R$ 后，
(4)、(9)、(14) 及 (17)、(20) 提供全分歧读数；
(23)–(24) 则提供一个直接的完整实现。
没有要求先找到所有曲线几何分支、假设判别式平方自由，
或把普通曲线环换成正规化而漏掉 conductor。

## 8. 原 M 的实际范围与下一门

原 $M$ 在同一物理轴上给的是有限长的实际 jet／carry 条件。
现有 $p^3$ 推导确实固定了 $R|_C$ 的 $s$ 长前缀以及
$ER|_C$ 的 $s-1$ 单位首项，并保全部已付 normal 短段。
它尚未证明 (14)、(19) 在所有其它纤维同时为零。

在[同修正零类反门](../notes/2026-11-16-r872-same-corrector-finite-class-and-normal-return.md)
的已付范围，实际 $R$ 反而必须使至少一个真实局部行或其连接类非零。
该断言不能定位到物理零纤维，更不能把本篇新增读者另当作四条中央已经杀掉的行。

固定同一 $P$ 后，允许保持 $p^3$ 的改动来自整个 $K_2$，
所以必须把同一个 $Z\in K_2$ 的 (14)、(19)、(20)
与 $R$ 联合代入。未加前缀的局部完整像 (5)
不决定 $\mathfrak o_D(K_2)$。
[R888](R888-original-factor-lift-invariance-of-the-actual-finite-class.md)
还保证合法改变因子化整提升只加 $\mathscr V_3$，
不会改变这些全球类或把它们变为自由选项。

本篇完成的是这个真实障碍的可计算全行及其准确常数。
没有用矩阵的单位行列式或局部长度宣布指定 forcing 为零或非零，
也没有新增数学运行、扫描或证书数据。
