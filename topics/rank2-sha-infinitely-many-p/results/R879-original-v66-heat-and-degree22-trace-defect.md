# R879 — 原 V66 的第一次热连接与完整 degree22 trace 缺陷

日期：2026-11-16。状态：以下是同一个原 $V_{66}$ 的完整热伴随及范数三 trace 的手证。它不从原 $\mathfrak B(V)=0$ 推出热伴随的中央零，也不将固定 CM trace 误当作在横向参数上恒定的算子。

## 1. 固定来源和延拓

使用 R855 的通用曲线与热连接
$$
y^2=x^3-\frac{g_2x}{4}-\frac{g_3}{4},\quad b=-g_3/4,\quad
\mathcal H_M=\mathcal L-\frac{M-1}{2}x-\frac{D^2}{2M}.
\tag{1}
$$
其中 $\mathcal Lx=2x^2-g_2/3$、$\mathcal Ly=3xy$，
$\mathcal L$ 在参数上是完整 $L_2$。
先对 R816／R856 已指定的原多项式
$$
R_V=X(X+b)(X-8b)^2(X+4b)
 (7X^2-4bX+16b^2)
 (X^3+228bX^2+48b^2X+64b^3)/7
\tag{2}
$$
应用 (1)，最后才取 $g_2=0$。
这正是原首 $z^6$ 归一的 $V=\sigma^{66}R_V$；
其系数按 $b=-g_3/4$ 延拓，没有添加新的 $g_2$ 项。
由于 $L_2b=-g_2^2/12$，(2) 的系数导数在此次 CM 特化为零；
这并不允许在后续第二次热导数中继续删去横向项。

记
$$
V^{[1]}=\left.\sigma^{66}\mathcal H_{66}R_V\right|_{g_2=0}.
\tag{3}
$$
它是原 whole degree66、型四截面，而非一个可另赋中央零的来源。
原 $V=z^6+\cdots$ 与 R855(13)还给
$V^{[1]}=-(5/22)z^4+\cdots$。

以下 $\delta^2=-3$，$\mathrm T_{\delta,m}$ 始终取 R877(1)–(4) 的准确 theta trace：
$$
\mathrm T_{\delta,m}(\sigma^{3m}R)
=\sigma^m\operatorname{Tr}\frac{R}{(\delta x)^m}.
\tag{4}
$$
所有 $\delta$ 幂、三纤维和标准半特征保留。

## 2. 热连接在同一 trace 商上的准确共轭

在 CM 点，置
$$
a=-\frac{x^3+4b}{3x^2},\qquad
r=\frac{R}{(\delta x)^m}.
$$
对于本篇这样没有额外 $g_2$ 系数项的 $R(x,b)$，
直接对 (1) 作乘积求导，得到
$$
\boxed{
(\delta x)^{-m}\mathcal H_{3m}R
=\mathscr J r-\frac1{6m}D^2r+\frac{m-1}{2}a\,r,
}
\tag{5}
$$
其中这里的实际作用是
$$
\mathscr J
=\mathcal L-\frac23\frac yxD,\qquad
\mathscr J r=\frac23\left(x^2-\frac{2b}{x}\right)\partial_xr.
\tag{6}
$$
式(6)仅读本篇的有理 $r(x,b)$，并不是把 $\mathcal L$
错误地下传成固定 CM 曲线上的参数零导子。

为核 (5) 的全部零阶项，准确有
$$
x^{-m}D^2(x^m r)
=D^2r+4m\frac yxDr+
\left((4m^2+2m)x+(4m^2-4m)\frac b{x^2}\right)r.
$$
与 $\mathcal L(x^m)/x^m=2mx$ 合并后，
零阶余项为
$-(m-1)(x+4b/x^2)/6=(m-1)a/2$，
得到 (5)。

完整函数域迹满足
$$
\operatorname{Tr}(D^2r)=\delta^2D_a^2\operatorname{Tr}(r),
\tag{7}
$$
其中 $D_a$ 是目标不变导子。
R877 已对原 $V$ 支付 $\operatorname{Tr}r_V=0$。
因此 (5) 中后两项的整个迹准确消失，留下
$$
\boxed{
\mathrm T_{\delta,22}V^{[1]}
=\sigma^{22}\operatorname{Tr}(\mathscr J r_V).
}
\tag{8}
$$
不能把第一项也当作零；它正是本篇要读出的原横向缺陷。

## 3. 同一三点纤维的线性系数变分

引入仅供计算完整有理迹的参数 $\rho$：
$$
P_\rho(x)=x^3+3ax^2+\rho x+4b.
\tag{9}
$$
在 $\rho=0$，其根就是原三点纤维。
由 $P_x=3x^2+6ax$ 及原方程直接核
$$
P_x\,\mathscr Jx=6a^2x^2-12bx.
$$
另一方面
$\partial_ax=-3x^2/P_x$、$\partial_\rho x=-x/P_x$。
所以对任一固定有理 $r(x,b)$，
$$
\operatorname{Tr}(\mathscr Jr)
=-2a^2\partial_a\operatorname{Tr}_{P_0}(r)
+12b\,\left.\partial_\rho\operatorname{Tr}_{P_\rho}(r)\right|_{\rho=0}.
\tag{10}
$$
这只是对原完整纤维的精确微分恒等式；并未把 $\rho$ 当成一个新的算术自由参数。
对 $r=r_V$，第一项由原 trace 恒等零消失。

R877 的实际 $C_{30}$ 分解使剩余微分很短。
置
$$
B(x)=7x-4b x^{-2}+16b^2x^{-5},\qquad
Q(a)=a(a^3+b)(a^3-8b).
$$
从 $V=C_{30}\sigma(6z)/6$ 和全部原 $\delta$ 倍率，得到
$$
r_V=\frac{\delta^{-8}}7\,Q(a(x))B(x),
\qquad a(x)=-\frac{x^3+4b}{3x^2}.
\tag{11}
$$
在 (9) 的实际商环内，
$$
a(x)=a+\frac{\rho}{3x}.
$$
故对整个迹求导，而不是只求外部系数，得到
$$
\left.\partial_\rho\operatorname{Tr}r_V\right|_0
=\frac{\delta^{-8}}7\left\{
Q(a)\left.\partial_\rho\operatorname{Tr}B\right|_0
+\frac{Q'(a)}3\operatorname{Tr}_{P_0}\frac Bx
\right\}.
\tag{12}
$$

为完全核定这两个实际迹，令逆根的方程为
$$
u^3+\frac{\rho}{4b}u^2+\frac{3a}{4b}u+\frac1{4b}=0.
$$
Newton 公式逐项给
$$
\left.\partial_\rho\operatorname{Tr}x\right|_0
=\left.\partial_\rho\operatorname{Tr}x^{-2}\right|_0=0,
\qquad
\left.\partial_\rho\operatorname{Tr}x^{-5}\right|_0
=-\frac{45a^2}{64b^3}.
$$
于是
$$
\left.\partial_\rho\operatorname{Tr}B\right|_0=-\frac{45a^2}{4b}.
\tag{13}
$$
同一递推还给
$\operatorname{Tr}x^{-3}=-3/(4b)$、
$\operatorname{Tr}x^{-6}=-27a^3/(32b^3)+3/(16b^2)$，
从而
$$
\operatorname{Tr}_{P_0}(B/x)=27-\frac{27a^3}{2b}.
\tag{14}
$$
全部数值都是三个根的完整迹；没有省略任何伙伴或改取边际。

## 4. 原 V 的完整四坐标热伙伴

将 $Q=a^7-7ba^4-8b^2a$ 代入 (12)，准确得到
$$
\left.\partial_\rho\operatorname{Tr}r_V\right|_0
=\frac{\delta^{-8}}7
\left(-\frac{171a^9}{4b}
+\frac{1071a^6}{4}-126ba^3-72b^2\right).
$$
再用 (8)、(10)、$\delta^8=81$，令目标 $X=a^3$，得到本篇结论：
$$
\boxed{
\mathrm T_{\delta,22}V^{[1]}
=-\frac{\sigma^{22}}{21}
 \left(19X^3-119bX^2+56b^2X+32b^3\right).
}
\tag{15}
$$
这与 R877 的 $\mathrm T_{\delta,22}V=0$ 同时成立。
其非零常数系数 $-32b^3/21$ 已说明：把这个固定 trace
在热方向误作恒定会丢掉一个真实来源。

在 R876 使用的全四维基
$b^{3-j}\sigma^{22}X^j$ 中，(15)的坐标准确为
$$
\boxed{\frac1{21}(-32,-56,119,-19)^{\mathsf t}.}
\tag{16}
$$
它与原 $H_{22}$ 的 $(0,464,-380,65)^{\mathsf t}$
处于同一个已付 whole 空间，但本篇没有把它们认成同一个向量、
同一个 Hecke 线或同一个指定读数。

## 5. 指定除 p 行仍保完整热与 trace 缺陷

(15)可以直接送入 R855/R856 的同一整读者；
其 Fourier、Mumford、Frobenius 初始资料都没有更换。
但有三个不同操作必须保持：

1. 先对原 $R_V$ 作完整 $\mathcal H_{66}$，再在 CM 特化，得到 (3)。
2. 对这个 whole 截面作原完整三点 trace，得到 (15)。
3. 对指定截面用原 $\mathcal D_{m,p,k}$ 或中心零格上的 $\mathfrak B$ 读取。

本篇只支付前两步及其精确差。式(10)的第二项已经证明，
第一个零 trace 不能越过热连接；同样，不能未经证明将第三步越过 trace。
原 $\mathfrak B(V)=0$ 不给 $\mathfrak B(V^{[1]})=0$，
也不使 (15) 的相应高阶除 $p$ 行为零。
后续须在 R856(39)–(41)的完整双变量整递推中保留这枚四坐标伙伴及 trace 的实际余项。

这是一条原 $V$ 到实际 degree22 来源的固定关系，不是新的任意输入。
全文为手工有限有理迹计算，没有数学数值运行或目标素数扫描。

依赖：[R855 原完整热连接](R855-original-full-heat-connection-and-canonical-divided-jet.md)；
[R856 原整除 p 递推](R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)；
[R877 同一范数三 trace 与原 V](R877-original-norm-three-common-source-and-h22-partner.md)；
[R876 原 H22 四维完整算子](R876-original-h22-complete-cm-source.md)；
[R816 原 V66 全来源](R816-original-minus-eleven-rank-two-schwartz-and-degree66-source.md)。


## 附录 A. 原 H22 的实际 CM 词返回与指定 D5 的 Fermat 缺陷

本附录继续使用同一个原 $V$、(3)的热伴随和(15)的全迹。
记
$$
G_{22}:=\mathrm T_{\delta,22}V^{[1]},\qquad
H_{22}=\sigma^{22}X(65X^2-380bX+464b^2).
\tag{A1}
$$
以下恒等式没有新增数学执行；有限算子的全部原数据来自
[R876 的实际公开运行](R876-original-h22-complete-cm-source.md)，
其余是对这些特征零算子及 R856 原整行的手工代数运算。

### A.1 同一四维来源上的固定 CM 词

固定 R876(3)–(4) 的完整标准 theta 算子
$$
A=\mathcal N_{3+\omega},\qquad B=\mathcal N_{4+\omega},
\qquad
\mathsf U=2A+B,\quad \mathsf V=B/\delta,\quad
\mathsf J=\mathsf U\mathsf V.
\tag{A2}
$$
这里仍有全部纤维、sigma 比和 $1/\gamma$；
$\mathsf U,\mathsf V$ 不是重新归一的特征值。
由 R876 的全空间身份 $B=-A^3$、$A^4-A^2+I=0$，准确有
$$
\mathsf U^2=3I,\quad \mathsf V^2=I/3,\quad
\mathsf J=(I-2A^2)/\delta,\quad \mathsf J^2=I.
\tag{A3}
$$

在(16)的同一基 $b^{3-j}\sigma^{22}X^j$ 中，令
$g=(-32,-56,119,-19)^{\mathsf t}/21$。
将 R876 的完整两个矩阵作用于此实际向量，得到
$$
\mathsf Ug=\frac1{21}(-176,-24,48,-23)^{\mathsf t},
$$
$$
\mathsf Vg=\frac1{189}(112,984,1200,85)^{\mathsf t},\qquad
\mathsf Jg=\frac1{189}(96,2664,1071,-39)^{\mathsf t}.
\tag{A4}
$$
这些是原公开完整算子的四个有理向量相乘；不是辅助模素数的计算。
例如将四列统一乘以 $189$，其准确列矩阵为
$$
\begin{pmatrix}
-288&-1584&112&96\\
-504&-216&984&2664\\
1071&432&1200&1071\\
-171&-207&85&-39
\end{pmatrix}.
$$
与列向量 $(-983808,191849,54621,150360)^{\mathsf t}$ 相乘，
逐坐标准确等于
$189\cdot10362(0,464,-380,65)^{\mathsf t}$。
故得到指定来源的恒等式
$$
\boxed{
10362H_{22}
=\bigl(-983808I+191849\mathsf U+
54621\mathsf V+150360\mathsf J\bigr)G_{22}.
}
\tag{A5}
$$
新分母 $10362=6\cdot11\cdot157$ 在原 $p>211$ 范围全为单位。
原 $b$ 的尺度由 R876(13)统一运输，因而(A5)对原单位 $b$
完整成立，不限于 $b=1$。

这已经将 R863(A20)–(A22) 的指定 $H_{22}$ 返回为
**原 $V$ 的第一次热连接、原三点 trace、固定 CM 词**。
特别可把(A5)逐项代入 R863 的两个完整低卷积；
但必须把每个 CM 词放在实际输入中，不能未经证明移到读者另一侧，
也不能只代第一配对而删掉 $q_F C_0$ 的第二配对。

### A.2 原 CM 纤维的准确拉回除 p 公式

固定 R856(39)的特征零原提升 $H_p$ 和 $C_p=L_2H_p$。
在原 $p=6s-1$ 的 CM 纤维，
$$
H_p=0,\qquad
\widehat c_p:=C_p(0,-4b)
=(p+1)\binom{3s-1}{2s-1}b^s.
\tag{A6}
$$
$\widehat c_p$ 的模 $p$ 值为既有 $c_p$。
以下除法先在特征零中进行，不能将 $\widehat c_p$
提前换成任意同余提升。

对任一原 whole degree $m$ 截面 $F$，写
$[\delta]^*F(z)=F(\delta z)$，其 degree 为 $3m$。
由于 $j_r([\delta]^*F)=\delta^rj_r(F)$，
直接代入同一指定整行，得
$$
\boxed{
\begin{aligned}
\mathcal D_{3m,p,k}([\delta]^*F)
={}&\delta^{p+k}\mathcal D_{m,p,k}(F)\\
&+mk\,\widehat c_p\,\delta^{k-1}
 \epsilon_{\delta,p}\,j_{k-1}(F),
\end{aligned}
\qquad
\epsilon_{\delta,p}:=\frac{\delta^{p+1}-3}{p}.
}
\tag{A7}
$$
这是 CM 纤维上的特征零等式。
其中 $k=0$ 的第二项按零解释；$k\ge1$ 按显示式。
除 $p$ 的整性来自 $\delta^p\equiv-\delta\pmod p$，
而不是删去这项。

为保绝对符号，令
$t_p=\delta^{p+1}/3=-(-3)^{(p-1)/2}$。
它是有理整数，$t_p\equiv1\pmod p$，且
$t_p^2=3^{p-1}$。因此在
$q_p(3)=(3^{p-1}-1)/p$ 的原规范下，
$$
\boxed{\epsilon_{\delta,p}\equiv\frac32q_p(3)\pmod p.}
\tag{A8}
$$
当 $k=1$ 且原 $F$ 的质量准确为零时，(A7)的第二项才消失；
它不能在下述 $k=5$ 行中消失。

### A.3 同一 V 热源的 old／new 分解与真实 D5 行

按 R877 的 canonical deck 投影，定义
$$
V^{[1]}_{\mathrm{new}}
=V^{[1]}-\frac13[\delta]^*G_{22}.
\tag{A9}
$$
由于 $\mathrm T_{\delta,22}[\delta]^*=3I$，
这是原 whole degree66 中的准确截面，并满足
$\mathrm T_{\delta,22}V^{[1]}_{\mathrm{new}}=0$。
这项的来源不是新的任意输入，但其 trace 为零也不是中央条件。

对(A9)使用(A7)，先保完整整式：
$$
\boxed{
\begin{aligned}
\mathcal D_{66,p,k}(V^{[1]})
={}&\mathcal D_{66,p,k}(V^{[1]}_{\mathrm{new}})
+\frac{\delta^{p+k}}3\mathcal D_{22,p,k}(G_{22})\\
&+\frac{22k\,\widehat c_p\,\delta^{k-1}}3
  \epsilon_{\delta,p}\,j_{k-1}(G_{22}).
\end{aligned}
}
\tag{A10}
$$
两来源的型均为四；原第一相容余行是 $k=5$。
由(15)，准确有
$$
j_4(G_{22})=-\frac{152}{7},\qquad
\delta^{p+5}/3\equiv9\pmod p,\quad \delta^4=9.
$$
所以(A10)给出
$$
\boxed{
\begin{aligned}
\mathcal D_{66,p,5}(V^{[1]})
\equiv{}&
\mathcal D_{66,p,5}(V^{[1]}_{\mathrm{new}})
+9\mathcal D_{22,p,5}(G_{22})\\
&-\frac{75240}{7}c_pq_p(3)\pmod p.
\end{aligned}
}
\tag{A11}
$$
若暂不代入(A8)，末项准确为
$-50160\,c_p\epsilon_{\delta,p}/7$。
这里的 $q_p(3)$ 来自原倍点与原 degree 的不同比例，
不是额外选取的参考 Gaussian。

### A.4 与原 V 全参数读者的同源接合

对 R856(41)取 $m=66,k=5$，再在原 $R_V$ 上求值。
完整对偶热连接满足
$$
(\nabla\ell)(R_V)=L_2\bigl(\ell(R_V)\bigr)
-\ell(\mathcal H_{66}R_V).
$$
原 $j_2(R_V)=j_4(R_V)=0$ 在特征零参数环内恒等成立；
其余显示 $g_2$ 项在最后 CM 特化时为零。
因此得到精确等式
$$
\boxed{
\mathcal D_{66,p,5}(V^{[1]})
=
\left.L_2\bigl(\mathcal D_{66,p,5}(R_V)\bigr)\right|_{\rm CM}
-\frac1{132}
 \left.\mathcal D_{66,p,7}(R_V)\right|_{\rm CM}.
}
\tag{A12}
$$
这里的 $L_2$ 作用于原完整双变量参数多项式；
不能先取 CM 值再对其零值求导。
尤其型别虽使 $\mathcal D_{66,p,5}(R_V)|_{\rm CM}=0$，
并不使(A12)中的参数导数为零。
$\mathcal D_{66,p,7}$ 也仍使用原
$7\cdot66\,\widehat c_pj_6(R_V)$ 的完整减项。

将(A12)代入(A11)，便把原 $V$ 的两条指定高行、
其真实 trace 零热余项、实际 degree22 伙伴和明确 Fermat 项
放入同一个等式。原 $\mathfrak B(V)=\mathcal D_{66,p,1}(R_V)=0$
没有单独使这些项中的任何一项为零。
同样，(A5)允许返回 R863 的整个指定低配对，
并没有把该低配对等同于 $\mathcal D_{22,p,5}$。
下一步仍须处理两种实际读者的完整连接与(A11)中的余项；
本附录没有由有限来源循环性、非零向量或 Fermat 商系数的单位性
推出四个原 $\mathfrak B$ 不能同时为零。


## 附录 B. 原 S／V 的两个高端消元与同一 Fermat 项的消去

本附录只用原 $C=C_{30}$ 及
$$
B_4=\frac{\sigma(2z)}2,\qquad
B_a=\frac1a[a]^*B_4=\frac{\sigma(2az)}{2a},\qquad
A_a=CB_a,\quad a\in\{1,3\}.
\tag{B1}
$$
其实际 degree 是 $30,4a^2,30+4a^2$，
$A_1=S$、$A_3=V$。
特别 $j_5(C)=120$、$j_1(B_a)=1$、
$j_7(B_a)=1536a^6b$，而 $j_6(A_a)=720$。
全部 sigma 输入均为原规范，没有新增算术来源。

简记
$$
O_C=\frac{j_p(C)}p,\quad
D_6^C=\mathcal D_{30,p,6}(C),\quad
D_2^B=\mathcal D_{4,p,2}(B_4),\quad
D_7^{(a)}=\mathcal D_{30+4a^2,p,7}(A_a).
\tag{B2}
$$
这些均为同一 whole 格的原整行；$O_C$ 的整性使用
R856(20)和 $j_1(C)=0$。下文的等式读模 $p$，
但首先对这些准确特征零分子作除法。

### B.1 全部高端和严格低于 p 的 cross

定义没有删项的低卷积
$$
\mathcal X_a=
-5040\!\!
\sum_{\substack{11\le r\le p-6\\r\equiv5\ (6)}}
\frac{j_r(C)\,j_{p+7-r}(B_a)}
 {r(r-1)(r-2)(r-3)(r-4)(r-5)(r-6)(r-7)}.
\tag{B3}
$$
这里两个 jet 指标都严格小于 $p$，所有显示分母均为单位。
则有
$$
\boxed{
\begin{aligned}
D_7^{(a)}={}&
7D_6^C+1536a^6b\,O_C+2520a^2D_2^B\\
&+\bigl(21600+22032a^2+
20160a^2q_p(a)\bigr)c_p+\mathcal X_a .
\end{aligned}
}
\tag{B4}
$$
约定 $q_p(1)=0$，$q_p(3)$ 与(A8)相同。

为证明(B4)，完整 Leibniz 和式只有三个高端：
$$
\begin{aligned}
j_{p+7}(CB_a)={}&
(p+7)j_{p+6}(C)
+\binom{p+7}{7}j_p(C)j_7(B_a)\\
&+\binom{p+7}{5}j_5(C)j_{p+2}(B_a)
+\sum_{\substack{11\le r\le p-6\\r\equiv5\ (6)}}
 \binom{p+7}{r}j_r(C)j_{p+7-r}(B_a).
\end{aligned}
\tag{B5}
$$
原完整减项为 $5040(30+4a^2)\widehat c_p$。
同一 whole 递推准确给
$$
j_{p+6}(C)=21600\widehat c_p+pD_6^C,\qquad
j_{p+2}(B_a)=8a^2\widehat c_p+
p\,\mathcal D_{4a^2,p,2}(B_a).
\tag{B6}
$$
整数倍点的实际除 $p$ 行是
$$
\mathcal D_{4a^2,p,2}(B_a)
=a^{p+1}D_2^B+8a^2\widehat c_pq_p(a)
\equiv a^2D_2^B+8a^2c_pq_p(a)\pmod p.
\tag{B7}
$$
这由 $j_r(B_a)=a^{r-1}j_r(B_4)$ 直接证明，
仍不改变原 $\widehat c_p$ 的提升。

需要保到模 $p^2$ 的二项式恰为
$$
\binom{p+7}{5}
\equiv21+\frac{459}{20}p\pmod{p^2},
\qquad
\binom{p+7}{7}\equiv1\pmod p.
\tag{B8}
$$
第一式的系数是
$21(1/3+1/4+1/5+1/6+1/7)=459/20$。
对(B5)最后一段，
$$
\frac1p\binom{p+7}{r}
\equiv
-\frac{5040}{r(r-1)\cdots(r-7)}\pmod p,
\tag{B9}
$$
因为实际 $r\equiv5\pmod6$ 为奇数。
将(B6)–(B9)代入，两个 Hasse 主项恰为
$151200\widehat c_p+20160a^2\widehat c_p$，
与原减项完全相消。其余为
$21600c_p$、$22032a^2c_p$ 及(B4)各项，证明结束。

### B.2 两个实际差分分别消掉哪个高端

对 $a=3$ 和 $a=1$ 作差，(B4)给
$$
\boxed{
\begin{aligned}
\mathcal D_{66,p,7}(V)-\mathcal D_{34,p,7}(S)
={}&1118208\,b\,O_C+20160D_2^B\\
&+176256c_p+181440c_pq_p(3)
+\mathcal X_3-\mathcal X_1.
\end{aligned}
}
\tag{B10}
$$
因此同一个 $D_6^C$ 已准确消失；没有先将它赋零。

若改取原不同 degree 所决定的系数九，则
$$
\boxed{
\begin{aligned}
\mathcal D_{66,p,7}(V)-9\mathcal D_{34,p,7}(S)
={}&-56D_6^C+1105920\,b\,O_C\\
&-172800c_p+181440c_pq_p(3)
+\mathcal X_3-9\mathcal X_1.
\end{aligned}
}
\tag{B11}
$$
这次 $D_2^B$ 和与它同尺度的 $22032a^2c_p$ 同时消掉。
(B10)、(B11)不是额外中央条件，而是同一原 $S,V$ 的准确高行关系。

原首行仍可在同一个 $C$ 上读取：
$$
\mathcal P_S=
\sum_{\substack{5\le r\le p-6\\r\equiv5\ (6)}}
 \frac{j_r(C)j_{p+1-r}(B_4)}{r(r-1)},
\qquad
\boxed{\mathfrak B(S)=O_C-\mathcal P_S.}
\tag{B12}
$$
故原 $S$ 中央首必要零使 $O_C=\mathcal P_S$。
这是使用原零条件后的一次合法高端消去；
它不让(B10)、(B11)左端的 $D_7$ 行为零。

### B.3 与附录 A 的同一 Fermat 项精确联立

保留(A11)的三个真实来源，记
$$
\mathcal T_p=
\mathcal D_{66,p,5}(V^{[1]})
-\mathcal D_{66,p,5}(V^{[1]}_{\mathrm{new}})
-9\mathcal D_{22,p,5}(G_{22}).
\tag{B13}
$$
于是 $\mathcal T_p=-75240\,c_pq_p(3)/7$。
因为
$209\cdot181440=(3528/7)\cdot75240$，
(B11)与(B13)准确给出不含显式 Fermat 商的关系
$$
\boxed{
\begin{aligned}
&209\bigl(\mathcal D_{66,p,7}(V)
 -9\mathcal D_{34,p,7}(S)\bigr)+3528\mathcal T_p\\
&\qquad=
209\left(
-56D_6^C+1105920b\,O_C-172800c_p
+\mathcal X_3-9\mathcal X_1
\right)\pmod p.
\end{aligned}
}
\tag{B14}
$$
其中 $209=11\cdot19$ 也在原范围内为单位。
在原 $\mathfrak B(S)=0$ 下，可以且仅可以按(B12)
把右端 $O_C$ 换成实际低卷积 $\mathcal P_S$。
(A12)还可逐式替换(B13)中的第一项，
保留原全参数 $L_2\mathcal D_{66,p,5}(R_V)$；
没有将其冻结为零。

(B14)同时消掉了同一个 degree4 高行和显式 $q_p(3)$，
因此不需要假设任何 Fermat 商在无限多素数处非零。
但它仍包含原 $C_{30}$ 的 $D_6^C$、两个实际 $D_7$、
原热 trace 零余项和所有低 cross。
R863(A22)的 $H_{22}$ 低配对须按(A5)整个运输；
它依然不同于(B13)的 $\mathcal D_{22,p,5}$。
本附录没有把两种读者相认，也没有从所示单位常数推 forcing。
所得是原两中央、原 V 热返回与全部伙伴之间的一条准确消元，
后续必须在同一原来源上控制其余项。


## 附录 C. 同一个 C30 热余项的 degree10 返回与原 Theta 行

这里继续处理(B14)中同一个 $D_6^C$。
所有热作用仍先在原双变量模型形成，再作 CM 特化。
固定
$$
R_C=-x^2y(7X^2-4bX+16b^2)(X-8b)/7,\qquad
C^{[1]}=\left.\sigma^{30}\mathcal H_{30}R_C\right|_{\rm CM}.
\tag{C1}
$$
这就是原 $C_{30}$ 的规范延拓，不加入新的 $g_2$ 项。
它是 whole degree30、型三截面，且
$C^{[1]}=-z^3/3+\cdots$。

### C.1 保 y 项的完整三点热迹

仍用(6)的算子 $\mathscr J$，但现在必须保它对 $y$ 的作用：
$$
\mathscr Jx=\frac23(x^2-2b/x),\qquad
\mathscr Jy=xy.
\tag{C2}
$$
这些值来自完整 $\mathcal L$ 后的 CM 特化。
不能将 $\mathscr J$ 冒充固定方程 $y^2=x^3+b$ 上的切向导子；
其原 $g_2$ 横向作用仍在(C2)的推导内。

令目标坐标仍为 $(a,c)$，并置
$$
B(x)=7x-4b x^{-2}+16b^2x^{-5},\qquad
c=-\frac{y(X-8b)}{3\delta X}.
$$
R877 的同一实际商为
$$
r_C=\frac{R_C}{(\delta x)^{10}}=\frac{3\delta^{-9}}7cB(x),
\qquad \operatorname{Tr}r_C=0.
\tag{C3}
$$
共轭公式(5)对这个含 $y$ 的原表达式仍成立：
其证明只展开 $D^2(x^{10}r)$ 和 $\mathcal L(x^{10}r)$，
不要求 $r$ 仅依赖 $x$。
因而 $D^2r_C$ 与 $ar_C$ 的完整迹为零，留下
$$
\mathrm T_{\delta,10}C^{[1]}
=\frac{3\delta^{-9}}7\sigma^{10}c
 \operatorname{Tr}\left(\mathscr JB+B\,\frac{\mathscr Jc}{c}\right).
\tag{C4}
$$

由(C2)准确得到
$$
\mathscr JB=\frac{14}{3}x^2-\frac{4b}{x}
-\frac{64b^2}{x^4}+\frac{320b^3}{3x^7},
$$
$$
\frac{\mathscr Jc}{c}
=x\,\frac{X^2+8bX-32b^2}{X(X-8b)}.
\tag{C5}
$$
第二式的 $y$ 导数项不能删除。
用原纤维 $x^3+3ax^2+4b=0$ 的完整 Newton 和，
$$
\operatorname{Tr}x^2=9a^2,\quad
\operatorname{Tr}x^{-1}=0,\quad
\operatorname{Tr}x^{-4}=\frac{9a^2}{8b^2},\quad
\operatorname{Tr}x^{-7}=-\frac{63a^2}{64b^3},
$$
可得 $\operatorname{Tr}\mathscr JB=-135a^2$。
另一个完整有理函数准确分解为
$$
B\,\frac{\mathscr Jc}{c}
=7x^2+\frac{27b}{x}-\frac{24b^2}{x^4}
+\frac{64b^3}{x^7}+\frac{81b x^2}{X-8b}.
\tag{C6}
$$
R877(15) 的同一三点迹给
$\operatorname{Tr}(x^2/(X-8b))=0$；
也可用 $X-8b=-3(ax^2+4b)$ 和
$\operatorname{Tr}(1/(ax^2+4b))=3/(4b)$ 直接核。
所以(C6)的迹为 $-27a^2$。

合并两项并用 $\delta^9=81\delta$，得到
$$
\boxed{
\mathrm T_{\delta,10}C^{[1]}
=\frac{2\delta}{7}\,\sigma^{10}x^2y.
}
\tag{C7}
$$
这里的两项分别贡献 $-135$ 与 $-27$，不是对原零 trace
作一个未经证明可交换的热导数。

记
$$
B_{10}=\sigma^{10}x^2y.
$$
实际 canonical old 与其真实余项因此为
$$
\begin{aligned}
C_{\rm old}^{[1]}
&=\frac{2\delta}{21}[\delta]^*B_{10}
=\frac67\sigma^{30}yX(X+4b)^2(X-8b),\\
C_{\rm new}^{[1]}&=C^{[1]}-C_{\rm old}^{[1]},\qquad
\mathrm T_{\delta,10}C_{\rm new}^{[1]}=0 .
\end{aligned}
\tag{C8}
$$
这使用准确的
$[\delta]^*B_{10}=-3\delta\,\sigma^{30}yX(X+4b)^2(X-8b)$。
$C_{\rm new}^{[1]}$ 的首项是 $11z^3/21$；
本节没有因其 trace 为零而令它的任何除 $p$ 行为零。

### C.2 同一个 D6C 的准确热行

对(C8)用(A7)取 $m=10,k=4$。
因为 $j_3(B_{10})=-6$，完整模 $p$ 式为
$$
\boxed{
\mathcal D_{30,p,4}(C^{[1]})
=
\mathcal D_{30,p,4}(C_{\rm new}^{[1]})
+\frac{18}{7}\mathcal D_{10,p,4}(B_{10})
-\frac{2160}{7}c_pq_p(3).
}
\tag{C9}
$$
所有系数仍由同一个 $\epsilon_{\delta,p}$ 取得：
在代入(A8)之前，最后一项是
$-1440c_p\epsilon_{\delta,p}/7$。

另一方面，R856(41)在原 $R_C$ 上取 $m=30,k=4$；
原 $j_1(R_C)=j_3(R_C)=0$，其余 $g_2$ 项最后特化为零。
因此准确有
$$
\boxed{
\mathcal D_{30,p,4}(C^{[1]})
=
\left.L_2\bigl(\mathcal D_{30,p,4}(R_C)\bigr)\right|_{\rm CM}
-\frac1{60}D_6^C.
}
\tag{C10}
$$
这里依然是原参数多项式的完整导数，
不是对其 CM 零值作导数。
(C9)–(C10)可以直接接(B14)的同一个 $D_6^C$，
且全过程保持同一个 $C_{30}$。

### C.3 degree10 旧行只有原 sigma 伙伴和完整低 cross

(C9)中的旧行还能在原来源内进一步展开。
置
$$
F_2=\sigma^2,\qquad
U_6=\frac{[\delta]^*F_2}{\delta^2}=x^2\sigma^6,\qquad
B_{10}=-B_4U_6 .
\tag{C11}
$$
各 degree 依次为 $2,6,10$；首项分别为
$z^2,z^2,-z^3$。定义严格低于 $p$ 的完整和
$$
\mathcal Y_p=
24\!\!
\sum_{\substack{8\le r\le p-3\\r\equiv2\ (6)}}
\frac{j_r(U_6)j_{p+4-r}(B_4)}
 {r(r-1)(r-2)(r-3)(r-4)}.
\tag{C12}
$$
则对乘积(C11)逐项保高端，得到
$$
\boxed{
\mathcal D_{10,p,4}(B_{10})
=-4\mathcal D_{6,p,3}(U_6)-12D_2^B-92c_p+\mathcal Y_p.
}
\tag{C13}
$$
为核其符号和常数，两个高端准确为
$-(p+4)j_{p+3}(U_6)$ 与
$-2\binom{p+4}{2}j_{p+2}(B_4)$。
代入
$j_{p+3}(U_6)=36\widehat c_p+p\mathcal D_{6,p,3}(U_6)$、
$j_{p+2}(B_4)=8\widehat c_p+pD_2^B$，
再扣除原 $-240\widehat c_p$ 主项，
余常数就是 $-36-56=-92$。
低端的
$\binom{p+4}{r}/p=-24/(r)_5$
又与(C11)的负号相消，正给(C12)。

同一原 $\delta$ 拉回的精确式还给
$$
\mathcal D_{6,p,3}(U_6)
=\delta^{p+1}\mathcal D_{2,p,3}(F_2)
+12\widehat c_p\epsilon_{\delta,p}
\equiv3\mathcal D_{2,p,3}(F_2)+18c_pq_p(3)\pmod p.
\tag{C14}
$$
没有把 $U_6$ 当作未变 degree 的裸坐标代换。

### C.4 用原 Theta 的 Wronskian 保全部高端

仍使用原 $\Theta=x\sigma^2$。
准确 whole 来源身份是
$$
B_4=\frac12\bigl(\Theta DF_2-F_2D\Theta\bigr).
\tag{C15}
$$
单独的导数可能含准周期项，但(C15)的完整 Wronskian
正是原 $\sigma(2z)/2$，没有改动 theta frame。
再定义全部严格低于 $p$ 的和
$$
\mathcal Z_p=
-\!\!
\sum_{\substack{6\le i\le p-5\\i\equiv0\ (6)}}
\frac{(2i-3)j_i(\Theta)j_{p+3-i}(F_2)}
 {i(i-1)(i-2)(i-3)}.
\tag{C16}
$$
对(C15)的指定 $p+2$ jet，完整高端合成
$$
\frac12j_{p+3}(F_2)
+\frac{(p+2)(1-p)}2j_{p+1}(\Theta).
$$
低端则是
$\tfrac12[\binom{p+2}{i}-\binom{p+2}{i-1}]$，
其除 $p$ 值正给(C16)。于是
$$
\boxed{
D_2^B
=\frac12\mathcal D_{2,p,3}(F_2)
+\mathcal D_{2,p,1}(\Theta)-c_p+\mathcal Z_p.
}
\tag{C17}
$$
特别 $\mathcal D_{2,p,1}(\Theta)$ 使用的是
$(j_{p+1}(\Theta)-2\widehat c_p)/p$；
$\Theta$ 的质量是一，故它绝不是可任意赋零的中央首行。

将(C14)、(C17)代入(C13)，得到(C9)旧行的完整表达
$$
\boxed{
\begin{aligned}
\mathcal D_{10,p,4}(B_{10})
={}&-36D_2^B+24\mathcal D_{2,p,1}(\Theta)
-116c_p-72c_pq_p(3)\\
&+24\mathcal Z_p+\mathcal Y_p.
\end{aligned}
}
\tag{C18}
$$
这样，原 $C_{30}$ 热 trace 的 degree10 部分只使用
(B4)已保的同一个 $B_4$ 行、原 $\Theta$ 的指定残行
和(C12)、(C16)两个完整低卷积；
没有留下一个未说明来源的 degree10 数值。

(C7)–(C18)全部保持原 sigma、canonical 三点投影和特征零 Hasse 提升。
它们没有为 $C_{\rm new}^{[1]}$、$B_{10}$、$F_2$ 或 $\Theta$
添加算术中央条件，也没有把 $\Theta$ 的真实 Frobenius 初始资料换成自由常数。
将这些式子与(B14)联立时，仍须控制同一个原热余项、
同一参数导数以及全部低 cross；
不能只由其中 $c_p$ 的单位系数断定四条原首行不相容。


## 附录 D. 余项所需的原 degree2 小格及固定代数水平框

本附录只具体化(C17)–(C18)已经出现的 $F_2=\sigma^2$、
$\Theta=x\sigma^2$ 两条原来源及其参数导数。
它不把 $\Theta$ 的质量一改成中央零，也不把本节的固定水平框
误当作原 $P_{2,M}$ 的固定替代。

### D.1 k=1 的完整热余项

R855 的原连接在 whole degree2 基上准确为
$$
\mathcal H_2(F_2)=-\Theta/2,\qquad
\mathcal H_2(\Theta)=-5g_2F_2/24.
\tag{D1}
$$
第二式由
$\mathcal Lx=2x^2-g_2/3$、$D_z^2x=6x^2-g_2/2$
直接代入原 $\mathcal H_2$ 得到。

记参数导子为 $L=L_2$，避免与物理 $D_z$ 混淆。
R856(39)在本小格的 $k=1$ 热递推可以完整写为
$$
\boxed{
\mathcal D_{2,p,3}
=4\nabla\mathcal D_{2,p,1}
+8\mathcal R_pJ_0-\frac{g_2}{3}(p+1)J_{p-1},
}
\tag{D2}
$$
其中 $\mathcal R_p=(L^2H+g_2H/12)/p$，
$H,C_p=LH$ 仍是原特征零多项式。
证明将
$J_{p+3}=4\nabla J_{p+1}-g_2p(p+1)J_{p-1}/3$
与
$J_{p+1}=HJ_2+2C_pJ_0+p\mathcal D_{2,p,1}$
代入；使用
$\nabla J_2=J_4/4+g_2J_0/6$、
$\nabla J_0=J_2/4$ 和
$LC_p=-g_2H/12+p\mathcal R_p$，
全部原低项正好合成(D2)。

因此在原 CM 点，
$$
\boxed{
\mathcal D_{2,p,3}(F_2)
=4L\bigl(\mathcal D_{2,p,1}(F_2)\bigr)
+2\mathcal D_{2,p,1}(\Theta).
}
\tag{D3}
$$
所有参数导数在特化前形成。结合(C17)，得到
$$
\boxed{
D_2^B
=2L\bigl(\mathcal D_{2,p,1}(F_2)\bigr)
+2\mathcal D_{2,p,1}(\Theta)-c_p+\mathcal Z_p
\quad\bmod p.
}
\tag{D4}
$$
不能从 $\mathcal D_{2,p,1}(F_2)|_{\rm CM}=0$ 删除它的参数导数。

### D.2 先于 p 固定的代数曲线

令
$$
\Delta=g_2^3-27g_3^2\ne0
$$
为同一参数导子下的常数。一次性在特征零系数域内选
$\mathfrak f$ 满足 $\mathfrak f^4=16\Delta$；
这与任何目标 $p$ 无关。
取固定仿射曲线
$$
\mathcal C_{\mathfrak f}:\quad
F(u,v):=uv(u^4-v^4)=\mathfrak f.
\tag{D5}
$$
定义两个准确不变量
$$
\begin{aligned}
I_8&=u^8+14u^4v^4+v^8,\\
I_{12}&=u^{12}-33u^8v^4-33u^4v^8+v^{12}.
\end{aligned}
$$
直接多项式展开给
$$
I_8^3-I_{12}^2=108F^4.
\tag{D6}
$$
所以
$$
g_2=I_8/12,\qquad g_3=I_{12}/216
\tag{D7}
$$
准确映到原固定判别式参数曲线。
这里的全部常数由(D6)固定，不留一个未定复周期倍率。

曲线的投射闭包是
$uv(u^4-v^4)=\mathfrak f w^6$。
在 $\mathfrak f$ 和 $6$ 可逆时它光滑：
有限处由 $w$ 偏导数判断；$w=0$ 时二元六次式
$uv(u^4-v^4)$ 的六个根均简单。
故这是先于 $p$ 固定的光滑平面六次曲线，亏格十。
(D7)为有限态射。为见其函数域次数，
一般点令 $z=(u/v)^4$；它满足
$$
(I_8)^3 z(z-1)^4
=\mathfrak f^4(z^2+14z+1)^3.
$$
这是六次方程。再用
$$
(u/v)^2=
\frac{\mathfrak f^2(z^3-33z^2-33z+1)}
     {I_{12}(z-1)^2}
$$
及
$$
v^2=\frac{I_8(u/v)(z-1)}
          {\mathfrak f(z^2+14z+1)}
$$
一般依次各取两个平方根，得到次数 $24$。
同一次数也可直接由完整极除子读取：六个无穷远点上 $I_8$ 均非零（在 $u=0,v=0,u^4=v^4$ 三类分别为 $v^8,u^8,16v^8$），故 $g_2$ 各有八阶极点、总次数48；目标参数椭圆曲线上的 $g_2$ 次数为2，因而原覆盖次数准确为24。
这些一般点公式只用于确定次数；CM 点在曲线本身上读取，
不把公式中的暂时分母当作必须在 CM 点求值的坐标。

### D.3 原完整连接的显式水平基

(D5)上的实际参数导子是
$$
\boxed{
Lu=\frac{u(u^4-5v^4)}{24},\qquad
Lv=\frac{v(v^4-5u^4)}{24}.
}
\tag{D8}
$$
它满足 $LF=0$。逐项求导还给
$$
LI_8=I_{12}/3,\qquad LI_{12}=I_8^2/2,
$$
所以(D7)准确满足 $Lg_2=6g_3$、$Lg_3=g_2^2/3$。
再算一次(D8)，得到
$$
L^2u=5g_2u/48,\qquad L^2v=5g_2v/48.
\tag{D9}
$$
于是同一个原 whole degree2 格的两个截面
$$
\boxed{
h_u=\sigma^2(2Lu+ux),\qquad
h_v=\sigma^2(2Lv+vx)
}
\tag{D10}
$$
由(D1)、(D9)准确水平。
它们在 $(F_2,\Theta)$ 中的系数矩阵行列式为
$$
2(vLu-uLv)=F/2=\mathfrak f/2,
\tag{D11}
$$
在原好素数域内为单位。
因此(D10)是完整基，不是仅一个参数微分方程的两条形式解。

确切地，
$$
\boxed{
F_2=\frac2{\mathfrak f}(v h_u-u h_v),\qquad
\Theta=\frac4{\mathfrak f}(Lu\,h_v-Lv\,h_u).
}
\tag{D12}
$$
选任一覆盖点 $P$ 位于原 CM 点之上，并将(D12)的系数冻结在 $P$，
就得到原两个物理纤维的水平延拓。
其质量函数分别为
$$
f_{F_2}^{\flat}
=\frac2{\mathfrak f}\bigl(v(P)u-u(P)v\bigr),
\qquad
f_\Theta^\flat
=\frac4{\mathfrak f}\bigl((Lu)(P)v-(Lv)(P)u\bigr).
\tag{D13}
$$
这用完整原截面相等固定了绝对尺度。
不需要猜一个 theta 常数或重选准周期相位；
换覆盖点或水平基时，(D12)仍恢复同一个原 $F_2,\Theta$。

### D.4 原除 p 读者在这两个固定函数上的准确表示

仍令 $N=(p+1)/2$。采用已付原水平标量算子
$$
T_0=1,\quad T_1=L,\qquad
T_{r+1}=LT_r-\frac{r(2r-1)}{24}g_2T_{r-1}.
\tag{D14}
$$
R855 的完整热递推给
$j_{2r}(h_u)=4^rT_ru$，同样适用于 $h_v$。
因此定义
$$
\boxed{
K_{u,p}=
\frac{4^NT_Nu-4H\,Lu-2C_pu}{p},
\qquad
K_{v,p}=
\frac{4^NT_Nv-4H\,Lv-2C_pv}{p}.
}
\tag{D15}
$$
它们就是实际 $\mathcal D_{2,p,1}(h_u)$ 和
$\mathcal D_{2,p,1}(h_v)$。
其整性直接由原 R856 whole 行及(D10)的整基给出；
不是从一个模 $p$ 的抽象水平解任意选除法。

(D12)遂将两个所需原行准确化为
$$
\boxed{
\begin{aligned}
\mathcal D_{2,p,1}(F_2)
&=\frac2{\mathfrak f}(vK_{u,p}-uK_{v,p}),\\
\mathcal D_{2,p,1}(\Theta)
&=\frac4{\mathfrak f}(Lu\,K_{v,p}-Lv\,K_{u,p}).
\end{aligned}
}
\tag{D16}
$$
这些式子在完整参数覆盖上成立，再在原 $P$ 特化。
特别相容的参数导数为
$$
L\mathcal D_{2,p,1}(F_2)
=\frac2{\mathfrak f}(vLK_{u,p}-uLK_{v,p})
-\frac12\mathcal D_{2,p,1}(\Theta).
\tag{D17}
$$
所以(C18)、(D4)中全部小格余项已具有两条先于 $p$
固定的函数 $u,v$ 和准确的(D15)读者，
连同指定系数导数；没有偷偷改变 $F_2$ 的参数延拓。

这里固定的是曲线、水平基和物理来源。
(D15)中的 $N,H,C_p$ 与原除 $p$ 高算子仍依赖于 $p$，
并且必须保留其原模 $p^2$ 数据。
本附录未把它称作一条固定 holomorphic Hasse–Witt 行，
没有删去(C18)的低 cross，更没有由覆盖有限或基行列式为单位
推出 $K_{u,p},K_{v,p}$ 的指定组合非零。


## 附录 E. 原质量一 Theta 行的完整 native Gaussian 规范

本附录把(C18)、(D16)中的同一个
$\mathcal D_{2,p,1}(\Theta)$ 接回
[R861](R861-original-hasse-aligned-gaussian-and-three-hurwitz-readers.md)
的完整物理矩阵。与该文第2节以后相同，本节固定共同模型 $b=1$。
一般单位 $b$ 的(A6)不被未经重标地塞进原 $M$。

记
$$
\mathcal C_p=(p+1)\binom{3s-1}{2s-1},\qquad
U_p=\frac{(p+1)!}{p}\in\mathbf Z_{(p)}^\times,\qquad
w=z^6 .
\tag{E1}
$$
$\mathcal C_p$ 正是(A6)的准确 $\widehat c_p$ 在 $b=1$ 的值，
不是其任意模 $p$ 提升。R861 的 Hasse 对齐来源为
$$
\kappa^\flat=-34\mathcal C_p/p,\qquad
g^\flat=d\Theta^{17}e^{-\kappa^\flat w^s}.
$$
因此取常数项一的准确十七次根，得到
$$
\boxed{
\Theta^\flat:=(g^\flat/d)^{1/17}
=\Theta\exp(2\mathcal C_pw^s/p).
}
\tag{E2}
$$
这个根是原 Gaussian 重标中的同一来源。
R861 的原整重标及 R602 的 Hurwitz 整性在 $s<p$ 的窗口给
$\theta_s^\flat:=[w^s]\Theta^\flat\in\mathcal O$。
没有将未正则化的 $\Theta$ 第 $s$ 系数先当作整数。

在 $w^s$ 处，(E2)精确给
$$
[w^s]\Theta=\theta_s^\flat-2\mathcal C_p/p.
$$
故原指定行准确等于
$$
\boxed{
\mathcal D_{2,p,1}(\Theta)
=U_p\theta_s^\flat
-\frac{2\mathcal C_p(U_p+1)}p.
}
\tag{E3}
$$
两项均整：Wilson 恒等式给 $U_p\equiv-1\pmod p$。
若使用标准 Wilson 商
$$
W_p=\frac{(p-1)!+1}{p},
$$
则还准确有
$$
\frac{U_p+1}{p}=(p+1)W_p-1.
$$
因此
$$
\boxed{
\mathcal D_{2,p,1}(\Theta)
\equiv-\theta_s^\flat-2c_p(W_p-1)\pmod p.
}
\tag{E4}
$$
这里不假设 $W_p$ 在任何素数族中非零。

为了核定没有借参考重标改变此行，回到原任一
$\kappa=34c_\sigma+\Delta$、$a=p\kappa$，并置
$$
\widehat\Theta=(g/d)^{1/17}
=\Theta e^{-\kappa w^s/17},\qquad
\widehat\theta_s=[w^s]\widehat\Theta.
$$
同一个准确系数恒等式给
$$
\boxed{
\mathcal D_{2,p,1}(\Theta)
=U_p\widehat\theta_s+
\frac{U_pa/17-2\mathcal C_p}{p}.
}
\tag{E5}
$$
最后一个分子整，因为 R861(3)给
$a\equiv-34c_p\pmod p$。
若 $\kappa\mapsto\kappa+\varepsilon$ 是原整重标，则
$$
a\mapsto a+p\varepsilon,\qquad
\widehat\theta_s\mapsto\widehat\theta_s-\varepsilon/17.
$$
(E5)两项的改变准确相消。
这与 R861(9)–(11)逐列保持同一个完整 $M$ 一致；
三条十三行 carry、原公共来源和后两位都未被重选。

将(E3)与(D16)相接，得到固定水平框与原 native 系数的准确等式
$$
\boxed{
\left.
\frac4{\mathfrak f}
(Lu\,K_{v,p}-Lv\,K_{u,p})
\right|_P
=
U_p\theta_s^\flat-
2\mathcal C_p\bigl((p+1)W_p-1\bigr).
}
\tag{E6}
$$
因此(C18)中的 degree10 旧行也可直接写为
$$
\boxed{
\begin{aligned}
\mathcal D_{10,p,4}(B_{10})
\equiv{}&
-36D_2^B-24\theta_s^\flat-68c_p
-48c_pW_p-72c_pq_p(3)\\
&+24\mathcal Z_p+\mathcal Y_p\pmod p.
\end{aligned}
}
\tag{E7}
$$
两个低卷积仍为(C12)、(C16)的完整原值。

$\theta_s^\flat$ 是整个正则化 $\Theta^\flat$ 的第 $s$ 系数。
R828 的四个近顶轴及其 $H_p/h_1$ 读的是
$t^{s-4},\ldots,t^{s-1}$；R861(7)–(8)明确这些轴在上述
Gaussian 重标下保持，而完整低余项须同步变化。
因此(E3)–(E7)没有把 $\theta_s^\flat$ 认成 $H_p,h_1,L_1$
或原 $K_1$ 末三尾之一。
若要消去该行，仍须同一个物理来源中的实际关系；
质量一、水平基行列式为单位或本节的整规范都不提供新的中央零。
