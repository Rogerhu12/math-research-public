# 原 cubic Euler 子格的真实 native Bockstein 配对

日期：2026-11-16。**状态：以下原 $\Lambda_0$ 首 Bockstein 读取、同一临界值的低纤维坐标及后续同源修正范围已证明。没有判定该泛函在完整高前缀子格上的像，也没有从值阶至少 $s$ 推出首 Bockstein 消失。**

本注接[原 charge 四十的 cubic 原函数格](2026-11-16-r872-native-cubic-euler-primitive-and-tail-nullspace.md)、[原值像与水平消失](2026-11-16-r872-primitive-value-image-and-cubic-horizontal-vanishing.md)和[原零纤维有限商](2026-11-16-r872-native-zero-fiber-three-layer-quotient.md)。所有矩阵均为 [R872](../results/R872-actual-quartic-third-carry-and-central-first-digit.md) 的同一个原矩阵；不更换 $P,R,S$、Gaussian、公共来源单位或目标长度。

## 1. 同一子格与实际四行

沿用
$$
p=6s-1>211,\qquad r=3,\qquad
\tau=3+2h-s\in\{1,2,3\},
\qquad \tau<\ell\le h-1,\qquad h<s-4 ,
\tag{1}
$$
以及 $D\ge4b$、$p>D+40$。置 $T=s-13$。
在同一原目标
$$
\Gamma=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3)
$$
中，全部 $w^{13}$、$c_*U_0$、$P_{134}$、十九角及三条十三行带均保留。

令
$$
L=Y\partial_Y+40,\quad
\mathscr V_j=\mathcal W_D\cap F^j k(t)[Y],\quad
\mathscr J_3=L^{-1}\mathscr V_3,\quad K_1=\ker\bar M .
$$
取同一个 $J\in\mathscr J_3\cap K_1$，写
$$
LJ=F^3A,\qquad A\in t^2k[[t]][Y].
\tag{2}
$$
后一个阶数是原零角帽所迫，不是额外可选的归一化。

原完整参考上的读取记为
$$
W_i(J)=U(w)(L^iJ)(t(w),\bar g_{\Theta,\circ}(w)),\qquad
F(t(w),\bar g_{\Theta,\circ}(w))=w^h u(w).
\tag{3}
$$
$U$ 是原固定公共单位；$t_1=(t/w)(0)$、$U(0)$、$u(0)$ 与
$e_0=(EF)(0,1)$ 均按同一规范保留。

已付的准确阶为
$$
W_1\in w^{3h+2},\qquad W_2\in w^{2h+2},\qquad
W_3\in w^{h+2},\qquad W_0\in w^T .
\tag{4}
$$
特别 (1) 中 $h\ge17$，所以前三者的所有四次以下系数均为零。

取原四个真实 $w^{13}$ 行的组合
$$
\boxed{
\Lambda_0=-68880[w^{13}]
+\frac{5042}{a}[\epsilon w^{13}]
-\frac{246}{a^2}[\epsilon^2w^{13}]
+\frac6{a^3}[\epsilon^3w^{13}].
}
\tag{5}
$$
这里 $a=-34\mathcal C_p\in\mathcal O^\times$ 是已固定的 Hasse 对齐值。
四行均存在于原目标，因 $\ell>0$。
系数多项式正是
$$
(X-40)(X-41)(X-42)
=X^3-123X^2+5042X-68880.
$$
原 $t^0$ 来源帽只有 $Y^0,Y^1,Y^2$，故 (5) 杀 $\bar M$ 的全部像。
这仍是原 native 左行，没有增加来源或算术零。

## 2. 完整首 carry：值项不能省去

对 $J\in K_1$，用任一同格整提升 $\widetilde J$ 定义
$$
\lambda(J):=\bar\Lambda_0\beta_1(J)
=\Lambda_0M\widetilde J/p\pmod p .
\tag{6}
$$
若换提升 $\widetilde J+pZ$，其变化为
$\bar\Lambda_0\bar MZ=0$，所以 (6) 是真实第一余类的标量。

先在原 $M_0=M(0)$ 参考中读取四行。
由完整 $w^s=p\epsilon$，各 $\epsilon^j w^{13}$ 行在除一个 $p$ 后的首折回依次读
$$
[w^s]W_0,\qquad a[w^s]W_1,\qquad
\frac{a^2}{2}[w^s]W_2 .
$$
不发生折回的四行合并为
$$
U(0)\bigl(L^3-123L^2+5042L-68880\bigr)
\widetilde J(0,1)=0
$$
的整恒等式：每个原常数 charge 恰是 $40,41,42$。
两次以上折回在本页含额外 $p$。

还须保实际矩阵的 $pH_pA_1$，而非直接将 $M_0$ 当原矩阵。
R872 的完整式给其在 (5) 上的首商贡献
$$
\frac{H_p}{a}[w^4]\,
B(w)\bigl(5042W_1-246W_2+3W_3\bigr).
\tag{7}
$$
由 (4) 这整项确实为零，**即使 $\ell\le4$ 也如此**。
$A_2,A_3,A_4$ 前置的 $p^2,p^3$ 使它们不进入首 Bockstein；
这里没有删除它们在更高页的作用。

因此
$$
\boxed{
\lambda(J)=\frac1a[w^s]\bigl(5042W_0(J)-246W_1(J)+3W_2(J)\bigr).
}
\tag{8}
$$
原参考轴换回实际轴时，可能进入该系数的第一高轴差仍由
$[w^4]BW_{i+1}$ 给出，亦由 (4) 为零；更高差已超出所读阶。
所以 (8) 同时是原实际 $g$ 的读取，没有留下一个可自由选的参考项。

## 3. 唯一边界 normal 项及其准确系数

定义同一个实际余乘子的首系数
$$
\alpha_A=[w^2]A(t(w),\bar g_{\Theta,\circ}(w)).
\tag{9}
$$
$A$ 不被自由赋值：它始终由 (2) 和原全部角帽确定。

由
$$
L^2J=3F^2eA+F^3LA,\qquad e=EF,
$$
有
$$
[w^{2h+2}]W_2(J)=
3U(0)u(0)^2e_0\,\alpha_A .
\tag{10}
$$
$F^3LA$ 的阶至少 $3h+2$，不进入 (10)。

若 $\tau=1$，则 $s=2h+2$。式 (4)、(8)–(10) 给
$$
\boxed{
\lambda(J)=\frac1a
\left(
5042\,[w^s]W_0(J)
+9U(0)u(0)^2e_0\,\alpha_A
\right).
}
\tag{11}
$$
若 $\tau=2$ 或 $3$，则 $s<2h+2$，准确变为
$$
\boxed{
\lambda(J)=\frac{5042}{a}[w^s]W_0(J).
}
\tag{12}
$$
不要求 $5042$ 是单位，也不由显示的乘子为单位推出
$[w^s]W_0$ 或 $\alpha_A$ 非零。

原三条首 carry 带在 $\mathscr J_3$ 上通过，恰好是
$W_0(J)\in w^s$。这个条件没有杀掉 (11)–(12) 中的第 $s$ 系数。
因此
$$
W_0(J)\in w^s
\quad\text{不蕴含}\quad
\lambda(J)=0,
$$
更不能据此宣称整个 $\beta_1(J)$ 为零。

## 4. normal 首值与另外两个零纤维支来自同一列

以下只是在零纤维的实际局部系数框中写出 (9)，不改变原因子分解。
可用一个 $t$ 的单位使 $F(0,Y)=F_0(Y)$ monic；
相应将 $A$ 乘逆三次单位。式 (10) 的
$u(0)^2e_0\alpha_A$ 不变。

由原帽，
$$
A=t^2(a_0+a_1Y)+O(t^3),\qquad
\boxed{\alpha_A=t_1^2(a_0+a_1).}
\tag{13}
$$
令
$$
b_i=\bigl[L^{-1}(Y^iF_0^3)\bigr]\in k[Y]/F_0
\quad(i=0,1),\qquad v_i=b_i(1).
\tag{14}
$$
这正是前注两个真实 primitive 列。
同一个 $J$ 的 $t^2$ 值是 $a_0b_0+a_1b_1$。
由于其物理分支值阶至少 $T>2$，必要地
$$
\boxed{a_0v_0+a_1v_1=0.}
\tag{15}
$$

写 $F_0=(Y-1)G_0$，令 $c_i=\operatorname{rem}_{G_0}b_i$。
若 $\gcd(F_0,YF_0')=1$ 且 $(v_0,v_1)\ne(0,0)$，前注证明
$b_0,b_1$ 独立。因此存在唯一同一标量 $\gamma$，使
$$
(a_0,a_1)=\gamma(v_1,-v_0),\qquad
[t^2]J|_{\text{其余有限二次块}}
=\gamma(v_1c_0-v_0c_1),
\tag{16}
$$
其中 $v_1c_0-v_0c_1\ne0$，且
$$
\boxed{\alpha_A=t_1^2\gamma(v_1-v_0).}
\tag{17}
$$
没有证明 $v_1-v_0$ 非零，也没有证明完整高前缀允许任意 $\gamma$。

若 (16) 前的两个非退化条件不同时成立，仍保原两系数 (13)–(15)，不硬降成一维。
这些式子解释 (11) 的 normal 首值如何由真正的临界值列读取；
它和物理第 $s$ 系数不能分别从两个不同 $A$ 拼接。

## 5. 全局值像、同预算和后续页

由原 Euler Taylor，$\mathscr J_3$ 在同物理分支上有
$$
e^{40\zeta}J(t,\bar g_{\Theta,\circ})
=J|_C+O(w^{4h+2}),
\qquad \zeta=\log(\bar g_{\Theta,\circ}/\psi).
$$
由于 $s<4h+2$，若已通过三条带而 $W_0\in w^s$，
则
$$
[w^s]W_0=U(0)[w^s]J|_C .
\tag{18}
$$
式 (18) 不是把 $U(w)$ 任意改为常数；只有在前缀低于 $s$ 全为零之后才可这样读取首系数。

同时，原值像仍满足
$$
J|_C\in
H^0\!\left(C,\mathcal O_C(B_D)
(-sP-3D_--3D_+)\right).
\tag{19}
$$
若这条线束的次数为负，即
$$
B_D\cdot C<s+3z_-+3e_+,
\tag{20}
$$
则 $J|_C=0$；已付真交
$\mathscr J_3\cap\mathscr V_1=\mathscr V_4$
迫 $J\in\mathscr V_4$。原零角的四次余乘子至少含 $t^3$，所以此时 $[w^s]W_0=0$ 且 $\alpha_A=0$，(11)–(12) 的两项均为零。
这里只是明确条件门；没有声称当前全部 profile 满足 (20)。

一般情况下，(11) 是同一个实际值截面在物理第 $s$ 行和零纤维临界值中的联合读取。
全球连接类、其它有限纤维和全高前缀仍须按原来源处理。

在原第二页固定 $P$ 改 $R\mapsto R+\widetilde J$，或第三页固定
$P,R$ 改 $S\mapsto S+\widetilde J$，$\bar J\in\mathscr J_3\cap K_1$
确实保持上一页，并且原三尾 $\Pi(J)$ 为零。
但下一页沿**完整** $\beta_1(J)$ 移动，(11)–(12) 正是其中原
$\Lambda_0$ 所见的分量。
所以从有限纤维商把某个修正拆成 $FH+J$ 后，
不能只因 $\Pi(J)=0$ 或 (19) 就将 $J$ 从同一 $R/S$ 的后续方程删除。

本注不构造新的中央零，也不以一个有限纤维单位替代完整 $K_1$ 的像。
无新增数学数值运行。
