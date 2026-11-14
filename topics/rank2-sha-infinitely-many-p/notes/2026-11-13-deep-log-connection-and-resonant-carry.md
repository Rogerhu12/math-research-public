# 原三源加二挠除子 log 后的闭合系统与相邻中央 carry

日期：2026-11-13。**状态：下述有限有理微分模、严格 log monodromy、原有限次数源的不闭合性，以及 q=2 原矩阵中的 carry 聚合均已证明。** 原三条中央导数的非零性尚未由这些结论得到。

## 1. 同一原参考及准确 log 伴随

使用 R235/R243/R245 的加法参数 $z$，令
$$
X=x_0(z),\quad Y=y_0(z),\quad U=X^2,
\qquad Y^2=X^3-X,
$$
并固定 $D=d/dz$，所以
$$
DX=2Y,\qquad DY=3X^2-1.
$$
原实际 rank-zero 参考及协变导子为
$$
S_8=-Y\vartheta(z)\sigma(z)^3,
\qquad F=S_8^{17},\qquad
V_8=DF/F,\qquad \nabla_8=D-V_8.
\tag{1}
$$
因 $\vartheta=\sigma\sqrt X$，有一个有用的原恒等式
$$
S_8=\vartheta(z)^4t,
\qquad t=-Y/X^{3/2},\quad t^2=1-U^{-1},
\qquad F=\vartheta(z)^{68}t^{17}.
\tag{2}
$$
本篇所有平方根均取原点的实际分支 $t(0)=1$。

记
$$
r=\frac{X-1}{X+1},\qquad L=\log r,\quad L(0)=0.
$$
这里 $r$ 是固定有理函数，本篇没有用这个字母表示 $(p+1)/4$。直接微分给
$$
\boxed{DL=\ell:=4X/Y,\qquad D^2L=-4-\frac8{U-1}.}
\tag{3}
$$
R245 的准确有理系数恒等式为
$$
H=\nabla_8^2 C+\beta F+\gamma\frac F{U-1},
\quad C=F\frac{XR_{14}(U)}{U^8(U-1)^7},
$$
$$
\beta=\frac{7584473604248}{1766439675},\qquad
\gamma=-\frac{541623088}{10725}.
\tag{4}
$$
因此定义**实际** log 伴随
$$
\widetilde C=C-\frac\gamma8FL,
\qquad \beta_{\mathrm{eff}}=\beta-\gamma/2
=\frac{802891497472}{27175995},
$$
准确得到
$$
\boxed{H=\nabla_8^2\widetilde C+\beta_{\mathrm{eff}}F.}
\tag{5}
$$
这里没有删去第三种有理余项；它已由 (3) 的原对数及其固定系数付出。

## 2. 包含三原来源的有限有理微分模

令
$$
K=\mathbf Q(X,Y),\qquad K'=K(\sqrt X).
$$
这是固定二次角域，$D\sqrt X=Y/\sqrt X$，故对 $D$ 稳定。旧共同单位 $\Theta_0=\vartheta(2z)^{17}$ 满足
$$
\frac F{\Theta_0}
=\left(\frac{-Y\sqrt X}{U+1}\right)^{17}.
\tag{6}
$$
因而 R244 的全部三原来源 $A,B,H$ 都属于 $K'F$；其中 $H/F$ 已在较小的 $K$ 中。若只用 $K$，不能无说明地把旧 $A,B$ 也放入同一个秩一模。

**定理 1。**
$$
\mathscr M=K'F\oplus K'FL
\tag{7}
$$
是对原 $\nabla_8$ 封闭的秩二微分模。准确公式为
$$
\nabla_8F=0,\qquad \nabla_8(FL)=\ell F,
$$
$$
\nabla_8(aF+bFL)=(Da+b\ell)F+(Db)FL,
\qquad a,b\in K'.
\tag{8}
$$
普通 $D$ 在 $K'(V_8)$ 上也封闭，因
$$
DV_8=-\frac{34(U+1)}{X(U-1)}\in K.
\tag{9}
$$
若保留 R235 的全部 $z,W$ 补偿，可用微分域 $K'(z,V_8)$；秩仍为二。(8)—(9) 是完整矩阵描述，而非有限个函数碰巧在某阶相等。

有一个全次数版本。对每个固定的原 charge 上界 $d$，把旧三源和 $\widetilde C$ 的全部次数不超过 $d$ 的乘积放入
$$
\mathscr M_d=
\bigoplus_{m=0}^d\ \bigoplus_{j=0}^m K'(z,V_8)F^mL^j.
\tag{10}
$$
径向次数导子 $E(F)=F,E(L)=0$ 与协变角导子
$\mathscr D=D-V_8E$ 给
$$
EF^mL^j=mF^mL^j,
\qquad
\mathscr D(F^mL^j)=j\ell F^mL^{j-1}.
\tag{11}
$$
它们保持 (10)，且互相交换；对系数按其实际 $D$ 作用。
因此加入这个固定对数以后，原全 core 的径向与角向微分在一个明确的有限有理微分系统中闭合。

(10) 的秩为 $\binom{d+2}{2}$。这里 $F$ 对固定角域及 $z,V_8$ 超越，可沿原实周期使用正 theta 乘子证明：$X,Y,\sqrt X$ 回到原值，$z,V_8$ 只作线性平移，而 $F^m$ 有随 $m$ 严格增加的正二次指数增长，有限个有理系数无法相消。对 $L$ 的独立性则由下一节的局部 monodromy 直接给出。

这个有限秩结论允许**有理函数系数**，不等于存在同样维数的整常系数源。其区别会在 §4 精确出现。

## 3. 非平凡 monodromy 是 log 坐标的方向

在 $T_+=(1,0)$ 和 $T_-=(-1,0)$，$r$ 的零、极点阶分别为二。因此
$$
\operatorname{res}_{T_+}(dL)=2,\qquad
\operatorname{res}_{T_-}(dL)=-2.
\tag{12}
$$
固定二次角覆盖 $K'/K$ 在这两点无分歧，留数不变。$X,Y,\sqrt X,z,V_8,F$ 在相应的小邻域中都是单值亚纯函数：$V_8=F'/F$ 即使有极点，也没有局部对数分支。因此它们的任意有理函数的导数都没有这种非零留数。

所以 (7) 的对数扩张不能在 $K'(z,V_8)$ 中分裂，也不能通过给 $FL$ 加一个该域中的 $F$ 倍数消掉非对角项 $\ell$。更强地，$L$ 对 $K'(z,V_8,F)$ 超越：若存在关于 $L$ 的多项式关系，沿 $T_+$ 连续绕任意整数圈，系数回原值而 $L$ 变为 $L+4\pi i n$，得到一个在所有整数 $n$ 上为零的非零多项式，矛盾。

原秩二模上的实际 monodromy 是
$$
F\longmapsto F,\qquad FL\longmapsto FL\pm4\pi iF.
\tag{13}
$$
在 (10) 上，它是 $L\mapsto L\pm4\pi i$ 的二项式上三角作用。其无穷小方向为 $\partial_L$，准确满足
$$
\partial_LA=\partial_LB=\partial_LH=0,
\qquad \partial_L\widetilde C=-\gamma F/8.
\tag{14}
$$
所以这确实是一个非径向的新增方向，但它固定全部三原来源。它不是 R244 所排除的、在 $(A,B,H)$ 中非零的常平移方向；特别它自动保持原次数二十四关系 $\Phi(A,B,H)=0$。

同一方向与 (5) 完全相容：$\partial_L$ 和协变角导子交换，而
$\nabla_8^2(\partial_L\widetilde C)=\nabla_8^2(-\gamma F/8)=0$。因此严格 log monodromy 本身没有给三条完整中央零一个矛盾，也没有迫使任何单个平移或移权 Mellin 值为零。

## 4. 不存在包含 log 伴随的有限常系数稳定源

**定理 2。** 在特征零中，没有包含 $FL$ 的有限维常数域向量空间对 $\nabla_8$ 稳定。

事实上对 $n\ge1$，
$$
\nabla_8^n(FL)=F D^{n-1}\ell.
\tag{15}
$$
在 $T_+$ 取实际加法局部参数 $\tau=z-z(T_+)$，则
$$
\ell=2/\tau+O(1),\qquad
D^{n-1}\ell=2(-1)^{n-1}(n-1)!\tau^{-n}+\cdots.
$$
其极点阶严格增加，故右侧函数在常数域上线性独立；乘同一个非零 $F$ 不改变这一点。这个证明也允许 $F$ 在该点有固定阶零，因为所有阶只共同平移一个固定整数。

因此 (8)、(10) 的封闭性不能被解释成免费增添有限个原多项式列后闭合。实际有限 pole budget 随反复协变微分增加；将有理系数、对数系数或新增 core 反解为原标量前缀时仍须付成本。

## 5. 原对数的第一 p 分母及固定坏素数

本节取惰性 $p=4r_p-1\ge19$，重新记 $r_p=(p+1)/4$，并置
$$
R=p^{-1/(2p)},\qquad u=X^{-1/2}=z+O(z^5).
$$
R215 的原椭圆对数和逆参数在次数 $<p^2$ 均 $p$ 整；同一原盘上 $\|u\|_R=R$。于是
$$
L=-2\sum_{\substack{j\ge1\\j\ \mathrm{odd}}}\frac{u^{2j}}j.
\tag{16}
$$
各项范数至多 $p^{v_p(j)-j/p}\le1$，故 $\|L\|_R\le1$。在 $z^{2p}$ 处，唯一的非整项是 $j=p$；其余 $j<p$ 及所用参数系数均整，$j>p$ 尚未出现。因此
$$
\boxed{\quad
[z^{2p}]L=-2/p+O_p,\qquad \|L\|_R=1.
\quad}
\tag{17}
$$
这严格大于 $R^2$。不能因 $L$ 从二阶开始，就给它原有理二阶伴随的 Gauss 界。

取原共同坏指数 $c=68c_0$，令
$$
\widehat F=e^{-cz^{p+1}}F,\quad
\widehat H=e^{-cz^{p+1}}H,\quad
\widehat{\widetilde C}=e^{-cz^{p+1}}\widetilde C.
$$
R197 的唯一坏指数删除、(2) 的整角单位及原 gauge 的整差给：$\widehat F$ 在当前第一带所读的系数均整，$\widehat F(0)=1$，并对 $z\mapsto iz$ 不变。R245 §4.1 的同一原 Gauss 界还给它及其逆的范数为一。因此
$$
p[z^{2p}](\widehat F L)\equiv-2\pmod p.
$$
R245 的有理 $C/F$ 系数分母只含
$2,3,5,7,11,13,23,31$。此外
$$
\gamma=-\frac{2^4\cdot33851443}{3\cdot5^2\cdot11\cdot13},
$$
其中 $33851443$ 是素数。因此，对本节惰性 $p\ge19$，只须再排除
$$
\boxed{p=23,\ 31,\ 33851443}
\tag{18}
$$
即可保证有理伴随在所读窗口整、且 $\gamma$ 为单位。这时准确有
$$
\boxed{\quad
p[z^{2p}]\widehat{\widetilde C}\equiv\gamma/4\pmod p.
\quad}
\tag{19}
$$
这是一个真实单位 carry；下一节定位它在原输出中的位置，并保留它的全部协变补偿。

## 6. 从 z^(2p) 到距中央一行的准确有限矩阵

令
$$
w=z^4,\qquad G=\widetilde C/z^2,\qquad
\widehat G=e^{-cw^{r_p}}G,\qquad
\theta=w\partial_w,\qquad D_4=4\theta,
\qquad W=zV_8.
$$
由于 $G$ 对 $z\mapsto iz$ 不变，它是原 $w$ 级数。直接保留算子顺序计算得到
$$
\nabla_8^2(z^2G)
=(D_4+1-W)(D_4+2-W)G.
\tag{20}
$$
共同 gauge 后置
$$
\widehat W=W-(p+1)cw^{r_p}=D_4\log\widehat F.
$$
于是 (5) 准确变成
$$
\boxed{\widehat H-\beta_{\mathrm{eff}}\widehat F
=\mathcal L_{\widehat W}\widehat G,
\qquad
\mathcal L_{\widehat W}=(D_4+1-\widehat W)(D_4+2-\widehat W).}
\tag{21}
$$
在任何共同有限窗口，若 $\widehat W_0=0$，这个原算子的下三角矩阵准确为
$$
\boxed{\quad
\mathcal L_{n,m}=
\mathbf1_{n=m}(4n+1)(4n+2)
+[\widehat W^2]_{n-m}
-(4n+4m+3)\widehat W_{n-m},\quad m\le n.
\quad}
\tag{22}
$$
这里原 $W$ 的卷积和导数都已保留，不能只留下第一项。

(19) 在 $G$ 中的位置是
$$
n_0=\frac{2p-2}{4}=2r_p-1,
$$
恰好在第二中央行 $2r_p$ 之前一行；它本身不是中央行。

更强地，在整个 $q=2$ 窗口 $k=2r_p+s<3r_p$，有
$$
\boxed{\quad
p\widehat G\equiv\frac\gamma4 w^{n_0}\widehat F\pmod p.
\quad}
\tag{23}
$$
证明仍用 (16)：当前窗口只可能遇到 $j=p$ 的一个分母；模 $p$ 的 Frobenius 给
$u^{2p}\equiv z^{2p}\pmod{z^{6p}}$，其误差远在这个窗口之外。固定有理伴随则整。因而可准确写成
$$
\widehat G=\frac\gamma{4p}w^{n_0}\widehat F+G_{\mathrm{int}},
\qquad G_{\mathrm{int}}\in O[[w]]/(w^k).
\tag{24}
$$

## 7. 完整 W 聚合消去负层；不产生额外首层中央单位

由 $\widehat W=D_4\log\widehat F$，对任意 $v$ 准确有
$$
\mathcal L_{\widehat W}(\widehat Fv)
=\widehat F(D_4+1)(D_4+2)v.
$$
特别
$$
\boxed{\quad
\mathcal L_{\widehat W}
 \left(\frac\gamma{4p}w^{n_0}\widehat F\right)
=\frac\gamma2(2p-1)w^{n_0}\widehat F.
\quad}
\tag{25}
$$
因为 $(4n_0+1)(4n_0+2)=(2p-1)2p$。所以 (19) 的单位负层在原二阶聚合中已经变为一个整项，完全不需要假设任何中央零。

相邻中央行也可逐项核准。由 (2) 与原 ODE，
$$
f_1:=[w]\widehat F=-17/6,\qquad
\widehat W_1=4f_1=-34/3.
$$
在 $n_0+1=2r_p$ 行，(24) 的两个负层系数通过 (22) 相加，准确得到
$$
\begin{aligned}
&\frac\gamma{4p}
\left((2p+3)(2p+4)f_1-(4p+3)\widehat W_1\right)\\
&\qquad=\frac\gamma{4p}\,2p(2p-1)f_1
=\frac\gamma2(2p-1)f_1\in O.
\end{aligned}
\tag{26}
$$
只保留 $G_{n_0}$、省去 $G_{n_0+1}$ 或 $W_1$，都会丢掉这里的必需抵消。其余 $G_{\mathrm{int}}$ 项也仍在 (21) 的同一个原矩阵中。

完整 Mellin 读到第二中央行时还乘原 $c^{-2}$，赋值为二。因此这份已整的贡献只能从原 $p^2$ 层开始；它没有给三条原中央共同条件增加一个 $p$ 一阶单位。R244 的低角单位三角式 $1,2,3$ 也不改变 (25)—(26)：它只是原有限源的整线性换基，不能把尚未控制的 $G_{\mathrm{int}}$ 高行删除。

所以这里得到的实际有限矩阵答案是：单位 carry 先位于非中央的 $2r_p-1$ 行，原 $W$ 补偿确实把它带入相邻中央行，但同时以 (25)—(26) 的真实特征值消去负层。要用它证明三中央非零，必须进一步控制聚合后的原高行或 R245 的完整转置桥梁；严格 log monodromy 与孤立的 (19) 都不能代替这一步。

依赖：R215 原椭圆参数的首坏项；R197 原共同 theta gauge；R235/R243/R245 的实际参考、三来源及有理协变分解；R244 的原三源关系与常方向判别。全部对数、换参、阶乘和 $W$ 项均在同一个原规范下保留。

