# R825 — 原全 nef 上缺量与所有有界 S 次数区域的排除

日期：2026-11-15。**状态：本篇的全 nef 恒等式、尖锐上界、原接触界及明确区域排除已证明。主目标仍未完成。**

沿用 R815 的原十九角曲面和原来源坐标 $S=a(t)Y/7$。本文将 R823 的最小面排除扩展到所有有界实际 $S$ 投影次数的原因子。核心是与 R819 下界配对的尖锐上界
$$
\boxed{(b-m)e+bm\le\kappa\le2be-m^2,}
\qquad b=Cf,\quad m=Cf_0,\quad e=CH_+,\quad\kappa=C^2.
$$
右端的损失是十九个原重数的明确平方和。结合 R805，原 $r=2,k_{\rm carry}=0$ 窗的任何实际因子都必须满足
$$
\boxed{
p\le24(e+2)D+24e-493+24\min(2,e-3).
}
$$
因此固定 $e$ 的整个区域在 $p$ 为 $D^2$ 量级时被排除。这个结论允许 $b$ 变化、全部合法 $q$ 及其移动常数因子；它不排除 $e$ 与 $D$ 一起增长的临界区。

## 1. 原曲面、亏量和完整平方和

使用 R815 的全变换基，写任意实 nef 类为
$$
C=bS_0+(u+4b)f-\sum_{i,j}\mu_{ij}E_{ij}.
\tag{1}
$$
四条负侧链为
$$
N=\{0,\alpha_+,\alpha_-,1\},\qquad (n_i)=(4,4,4,3),
$$
两条正侧链为 $P=\{d,\infty\}$，长度各二。完整 nef 条件为
$$
b\ge0,\quad \mu_{i1}\ge\cdots\ge\mu_{in_i}\ge0,\quad
\sum_j\mu_{ij}\le b,\quad u\ge\mu_{d1}+\mu_{\infty1}.
\tag{2}
$$
所以 $u\ge0$。定义
$$
m=b-\sum_j\mu_{0j},\qquad
e=u+4b-\sum_{i\in N}\mu_{i1},\qquad
\kappa=4b^2+2bu-\sum_{i,j}\mu_{ij}^2.
\tag{3}
$$
这里 $0\le m\le b$；R819 已给 $e\ge m$。对不在 $S$ 纤维中的几何整曲线，$e$ 是同一个实际 $S$ 在正规化上的总次数。

**定理 1。** 对全部 (1)–(2)，准确有
$$
\boxed{
2be-\kappa
=\sum_{i\in N}(b-\mu_{i1})^2
+\sum_{\substack{i\in N\\j\ge2}}\mu_{ij}^2
+\sum_{\substack{i\in P\\j\ge1}}\mu_{ij}^2.
}
\tag{4}
$$
特别
$$
\boxed{\kappa\le2be-m^2.}
\tag{5}
$$

**证明。** 展开 (3) 的左端，$2bu$ 抵消，余下
$$
4b^2-2b\sum_{i\in N}\mu_{i1}+\sum_{i,j}\mu_{ij}^2,
$$
恰为四个首项平方与其余平方，即 (4)。另一方面
$$
b-\mu_{01}=m+\sum_{j\ge2}\mu_{0j}\ge m.
$$
保留 (4) 中零链的首项平方，便得 (5)。所有平方来自原曲面的全变换坐标；没有另造放松曲面或换投影。证毕。

结合 R819 的原下缺量恒等式，得到
$$
\boxed{
(b-m)e+bm\le\kappa\le2be-m^2,\qquad
\chi=-K_XC\ge2b+m.
}
\tag{6}
$$
当 $b>m$ 时也可写成
$$
\boxed{
\frac{\kappa+m^2}{2b}\le e
\le\frac{\kappa-bm}{b-m}.
}
\tag{7}
$$
左除法只用于 $b>0$；右除法只用于 $b>m$。边界 $b=m$ 或 $b=0$ 使用 (6)，不作除零运算。

## 2. 上界的全部等号类

**定理 2。** (5) 取等当且仅当
$$
\begin{aligned}
&\boldsymbol\mu_0=(b-m,0,0,0),\\
&\boldsymbol\mu_i=(b,0,\ldots,0)\quad(i\in N\setminus\{0\}),\\
&\boldsymbol\mu_d=\boldsymbol\mu_\infty=0,\qquad u=e-m.
\end{aligned}
\tag{8}
$$
等价地，恰为
$$
\boxed{C=bH_++mE_{01}+(e-m)f,\qquad b\ge m\ge0,\ e\ge m.}
\tag{9}
$$

**证明。** 在 (4) 中取得 $m^2$，先迫其余三个负侧首亏量、所有后继重数及两条正链全部为零。零链首亏量则等于 $m$；代回 (3) 得 $u=e-m$。反之，(8) 逐项满足 (2)，代入 (4) 只有 $m^2$ 留下。故这份分类在实 nef 锥上完整，且 (5) 尖锐。证毕。

$E_{01}$ 仍为全变换类；不将它单独当作 nef 素除子。
整类须满足原坐标的整性；(9) 不宣称每个数值类都有不可约代表。
$e=m$ 时正好回到 R823 的最小面，而本篇允许任意更大的 $e$。

## 3. 原 t 次数和移动常数因子

现在取 R805 中同一个 primitive、几何不可约的实际多项式
$$
F(t,Y)=\sum_{n=0}^{b}f_n(t)Y^n,
$$
其严格变换类为 (1)，并保留全部原十九角。

原 $\mathbb F_4$ 的无穷框为 $T=1/t,\ Z=t^4Y$。
类 $bS_0+(u+4b)f$ 的逐 $Y$ 次系数帽给
$$
\deg f_n\le u+4n.
\tag{10}
$$
这也可直接在该无穷框中读取：$f_n(t)Y^n=T^{4n}f_n(T^{-1})Z^n$，允许的额外底极帽恰为 $u$。
吹起只添加消失条件，不扩大这个次数帽。

由 (3) 有
$$
e-m=u+\sum_{j\ge2}\mu_{0j}
+\sum_{i\in N\setminus\{0\}}(b-\mu_{i1})\ge u.
\tag{11}
$$
因此原多项式的真实 $t$ 次数满足
$$
\boxed{a=\deg_tF\le4b+u\le4b+e-m.}
\tag{12}
$$

按 R805 的已付来源分类，
$$
F(t,0)=\lambda d(t)^cH(t),\qquad d=1+8t,\quad c\ge0,\quad
z=\deg H,\quad(H,d)=1.
\tag{13}
$$
不可约非边界因子有 $F(t,0)\ne0$。由 (10) 的 $n=0$ 项，
$$
\boxed{c+z\le u,\qquad z\le e-m.}
\tag{14}
$$
这里允许 $H$ 的重根、移动根以及 $H(0)=0$。在原 $r=2$ 的所有已分类 profile 中，另由 R792/R797 有 $z\le2$，所以
$$
\boxed{m=3,\qquad e\ge3,\qquad z\le\min(2,e-3).}
\tag{15}
$$
没有把 $q(t,0)=0$ 的分支改成常数 $q$。

## 4. 所有实际 S 次数的接触上界

只在 R805 的原范围内使用以下论断：同一个
$qt^rF^3\in\overline{\mathcal W}_D$，$f_D<p$，原点光滑且
$F_Y(0,1)Q(0,1)\ne0$，以及低于首共振的真实接触
$\log(g/\psi)=t^hu(t)$，$u(0)\ne0$、$0<h<s$。
全部 tame、小次数、最高系数移动极和常数因子的成本继续按 R805 保留。

令 $\gamma$ 是正规化属，不将其与算术属相认。
R805 及 adjunction 给
$$
\begin{aligned}
h
&\le6\gamma+2a+10b+2z-6\\
&\le3\kappa-3\chi+2a+10b+2z\\
&\le3\kappa+12b+2e-5m+2z.
\end{aligned}
\tag{16}
$$
最后一步用了 (6)、(12)。再代入 (5)，得到：

**定理 3。** 对满足上述原来源条件的任意实际因子，
$$
\boxed{
h\le6be+12b+2e-3m^2-5m+2z.
}
\tag{17}
$$
特别，全部原 $r=2$ profile 同时满足
$$
\boxed{
h\le6b(e+2)+2e-42+2\min(2,e-3).
}
\tag{18}
$$

这是实际目标特征内的几何与 forcing 不等式。其证明没有固定 $b$，没有使用跨素数的有理最大子式，也没有假定正规化无奇点。

## 5. 原 r2 窗的明确区域排除

在原 $r=2,k_{\rm carry}=0$ 窗中，
$$
s=2h+2,\qquad p=6s-1=12h+11.
\tag{19}
$$
因此 (18) 给
$$
p\le72b(e+2)+24e-493+24\min(2,e-3).
\tag{20}
$$
同一个来源的完整径向预算仍为
$$
3b+\deg_YQ\le D.
\tag{21}
$$
于是
$$
\boxed{
p\le24(e+2)D+24e-493+24\min(2,e-3).
}
\tag{22}
$$

(22) 同时包含两种常数 charge 分支及其全部合法 $q$，没有删掉 $Q$ 的非恒定项。对 $e=3$，其右端正好是 $120D-421$，恢复 R823 的完整最小面界。

给定整数 $E\ge3$，(22) 的右端关于 $e$ 单调，所以
$$
\boxed{
p>24(E+2)D+24E-493+24\min(2,E-3)
\ \Longrightarrow\
\text{不存在实际 }e\le E\text{ 的上述因子}.
}
\tag{23}
$$
因此任何 $p/D\to\infty$ 的实际候选族必须有 $e\to\infty$。

特别，R819 的近最小区域
$$
\kappa-(6b-9)\le L(b-3),\qquad b>3
$$
给 $e\le3+L$。固定 $L$ 时取 $E=\lfloor3+L\rfloor$，(23) 排除该整个区域在充分大的二次临界族中出现，而不是只排除数值上的等号类。

保留稍宽的 $z\le2$，(22) 还给可直接使用的下限
$$
\boxed{
e\ge\max\left\{3,\
\left\lceil\frac{p-48D+445}{24(D+1)}\right\rceil\right\}.
}
\tag{24}
$$
若 $D\to\infty$ 且 $p/D^2\to47/8$，便有
$$
\boxed{\liminf e/D\ge47/192.}
\tag{25}
$$
若另外使用实际因子族的 $\kappa/b^2\to47/12$、$m=3$ 和 $b\to\infty$，则两侧 (7) 给
$$
\boxed{47/24\le\liminf e/b\le\limsup e/b\le47/12.}
\tag{26}
$$
(25)、(26) 是在各自明确渐近假设下的必要条件，不能相互替换，也不推出剩余区域为空。

## 6. 接续到完整原问题的范围

本篇支付了所有有界实际 $S$ 次数区域的统一排除，并准确描述上界损失和等号类。剩余二次临界区域必须允许 $e$ 随 $D$ 增长。

这些界没有给整个原 profile 的截面饱和、原 $\mathcal W_D$ 的全部左行，或指定 Schur 配对非零。原 $P_{134}$、总 charge40、十三阶前缀、全部 normal/carry、同一个 $R$ 的高尾和下一位仍在原问题中。

R822 的分歧迹与十九角边界必须在保持全部原行的联合核上比较；R821 的四个真实中央必要值也仍须接到同一个完整余核。本篇不把已排的有界 $e$ 子区域写成原全强窗或主目标的完成。

依赖：
[R815 原全 Mori/nef 锥与 S 铅笔](R815-complete-original-mori-nef-cones-and-s-fibration.md)；
[R819 原下缺量及反典范界](R819-original-nef-surplus-and-s-projection-degree.md)；
[R823 原最小面完整截面](R823-original-minimal-nef-face-complete-sections-and-serre-rows.md)；
[R805 原全部 profile 的属门](R805-original-constant-charge-genus-gate-and-all-profile-rank.md)；
[R792](R792-original-nonzero-constant-charge-classification-and-cubic-extension.md)；
[R797](R797-original-zero-constant-charge-moving-factor-and-complete-cubic-gates.md)。

全文为原交数、完整平方和与既有实际 forcing 界的符号证明；没有数学程序运行或新增可重算输出。
