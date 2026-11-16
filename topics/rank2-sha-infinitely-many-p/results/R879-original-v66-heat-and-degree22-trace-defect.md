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
