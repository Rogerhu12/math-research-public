# R142：实际 AS 共同零理想与 Hecke 二阶判别式

状态：**已证明**。日期：2026-11-12。

完整论证：
[实际 AS 坐标与判别式](../notes/2026-11-12-actual-as-basepoints-and-hecke-discriminant.md)。
本结果保留 R137 的原 $C_p$ 环类覆盖、全部 $U$ 迹及原 CM 标签；
不宣称指定纤维的二阶行已经非零。

## 结论与证明

令 $\pi:Y\to Z$ 为实际 étale $C_p$ 覆盖，
$\Gamma=\langle\tau\rangle$，$B$ 为原完整迹函数，置
$$
 n=N_\Gamma B,\qquad
 A=\sum_{j=0}^{p-1}j\tau^jB,\qquad
 F_2=\sum_{j=0}^{p-1}\binom j2\tau^jB.
\tag{1}
$$
群环计算给
$$
                       \tau A=A-n,\qquad
                       \tau F_2=F_2+n-A.
\tag{2}
$$
在任一 ordinary 底点的完备离散赋值环 $R$ 上，原覆盖代数可写成
$S=R[y]$，$y^p-y=c\in R$、$\tau y=y+1$。
这是原 torsor 的整坐标：取迹为 $1$ 的 $e\in S$，
令 $y=-D_1e$；其共轭差为非零 $\mathbb F_p$ 常数，
故 Vandermonde 行列式为单位，给出该 AS 代数的同构。

由 (2) 有唯一 $a,g\in R$，满足
$$
              A=-ny+a,\qquad
              F_2=\frac n2y(y+1)-ay+g.
\tag{3}
$$
换 $y$ 为 $y+b$ 时，$a$ 变为 $a+nb$，
$g$ 变为 $g+ab+nb(b-1)/2$。
因此
$$
                             (n,a,g)\subset R
\tag{4}
$$
是规范理想。它准确等于 $F_2$ 在有限自由 $R$-模 $S$ 中的系数
理想，因为 (3) 的次数小于 $p$。对参数 $t$，有
$F_2\in t^eS$ 当且仅当 $n,a,g\in t^eR$。

**CM 曲线 $E_{17}$ 的零总迹。**
R137 有 $n=0$，故整纤维失败的理想正是 $(a,g)$。
R137 又给 $A\ne0$、$F_2\ne0$，所以
$$
             \mathcal R=-F_2/A,\qquad
             \tau\mathcal R=\mathcal R+1
\tag{5}
$$
生成原 AS 函数域扩张。它不能排除 $(a,g)$ 的共同零点。
$W=A\,dF_2-F_2\,dA$ 下降到底曲线，至多有二阶超奇异极点；
共同零阶 $e$ 至少给 $W$ 的二重阶 $2e$，但这里不预设 $W\ne0$。

**非 CM 曲线 $E_{389}$ 的简单总迹。**
R141 的实际函数为 $g_p=\Theta^{p-2}\bar f/H^p$，原总迹为
$n=a_\ell(E)g_p$。对其中合法的源 split 素数及非退化源点，
$n$ 在带原 CM 标签的底点 $z$ 有简单零点。
定义真正不变量
$$
                  \mathscr D=A^2-nA-2nF_2
                             =a^2-na-2ng\in k(Z).
\tag{6}
$$
其不变性直接由 (2) 验证。在 $n(z)=0$ 处，
$\mathscr D(z)=a(z)^2$；当 $a(z)=0$ 时，
$d\mathscr D(z)=-2g(z)\,dn(z)$。于是准确有
$$
 \boxed{\quad
 F_2|_{\pi^{-1}(z)}=0
       \quad\Longleftrightarrow\quad
                     v_z(\mathscr D)\ge2 .
 \quad}
\tag{7}
$$
恒零的 $\mathscr D$ 按无穷阶解释，不假设其平方自由。

若 (7) 的失败纤维发生，由 $v_z(n)=1$ 知 (4) 恰为 $(t)$，
所以 $F_2,A\in tS\setminus t^2S$。首个正规 jet 为
$$
 \frac A t=-n_1y+a_1,\qquad
 \frac{F_2}t=
       \frac{n_1}{2}y^2+
       \left(\frac{n_1}{2}-a_1\right)y+g_1,\qquad n_1\ne0.
\tag{8}
$$
故至少 $p-2$ 个几何分支的 $F_2$ 零阶准确为 $1$。
若原算术纤维是非平凡次数 $p$ 扩域，剩余 $y$ 的次数为 $p$，
(8) 的低次多项式都不能消失；每个算术分支的阶准确为 $1$，
且 $v_z(N_{Y/Z}F_2)=p$。

非 CM 的 $W$ 一般不下降，而是
$(\tau-1)W=F_2\,dn-n\,dF_2$。特别总迹的简单零点不能先被用来
宣称 $W(z)\ne0$。

## 与原 Sha 充分检验的准确关系

R135 的 $E_{17}$ 纤维值为 $-\bar a_p s\,\bar z_Q$。
R134、R139 的 $E_{389}$ 原去 $p$ 迹为
$s(s-\bar a_p)\bar z_Q$，其中 $z_Q=\log_0(Q)/p$，
规范由原 Frobenius 群环单位保持整性。
这些都是实际完成/置换模中的群环单位，并与 $D_2$ 交换。
因此任一原纤维上的 $F_2$ 非零给原半局部充分检验非零，
从而推出 $\Sha(E/\mathbb Q)[p^\infty]=0$。

对非 CM 输入，现在具体需要证明 (6) 在指定 CM 点满足
$\mathscr D(z)\ne0$ 或 $d\mathscr D(z)\ne0$。
一般 étale 性、泛点的 Hecke 行非零、总迹简单零都尚未支付这一条件。
有限行在全部 $p$ 位为零也不反向证明 Sha 无限或全局 $\delta^2$ 除性。

## 来源

群环、整 AS 坐标及 (3)–(8) 均由上述证明完成。
实际对象与单位比较使用 R134、R135、R137、R139、R141；
其原始文献包括 Buium–Poonen（2009）Theorem 3.17、
Corollary 3.19，Cais–Conrad（2006 作者版）Theorems 2.2–2.3。
准确 URL、规范和完整纤维证明见所链笔记。
