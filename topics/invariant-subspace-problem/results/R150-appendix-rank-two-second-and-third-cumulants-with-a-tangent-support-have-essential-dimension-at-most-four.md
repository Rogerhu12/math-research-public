# R150 附录：rankH2 与 rankV2 中任一非约化支撑都不产生本质五维临界点

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 对原完整临界点，若 $\operatorname{rank}H=\operatorname{rank}V=2$，且二者唯一物理长度二除子中至少一个为二重 jet，则 $\dim\operatorname{ess}(T_3)\le4$。所有无穷远、零 value 系数及退化原 Gram 都在证明中。这里不声称本质四维层已经关闭；两个支撑都约化时的一个原 Gaussian 例外也不在本定理中排除。

## 1. 原对象、全梯度和结论

沿用[原完整三阶矩公式](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)：
$$
p=Ky,\quad F=\tfrac12y^{\mathsf T}Ky,\quad
b_0=p^{\mathsf T}Hp,\quad\tau_2=\operatorname{tr}((KH)^2),
$$
$$
T_3=y^3-6yH+4V,
$$
$$
\Gamma=(F^2-2b_0+2\tau_2)y-4FHp+8HKHp+
4V(p,p,\cdot)-8V:(KHK),
\tag{1.1}
$$
$$
N=Fyy^{\mathsf T}-2FH-2\{y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\}
+4HKH+4V_p.
\tag{1.2}
$$
完整临界性给
$$
\Gamma=0,\qquad k_x^{\mathsf T}Nk_x\equiv0,\qquad
P(x)^3-6P(x)G_H(x)+4V(k_x,k_x,k_x)\equiv0,
\tag{1.3}
$$
其中 $k_x=Ku(x)$、$P(x)=y^{\mathsf T}Ku(x)$、$G_H(x)=u(x)^{\mathsf T}KHK u(x)$。第二式恰是十一条原 H 梯度，第三式恰是十六条原 V 梯度；并未替换为仅沿参数流形取导。

**定理。** 若完整临界点有
$$
\operatorname{rank}H=\operatorname{rank}V=2
$$
且至少一个唯一长度二物理除子非约化，则
$$
\boxed{\dim\operatorname{ess}(T_3)\le4.}
\tag{1.4}
$$

[有限低秩 Hankel jet 引理](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md) §6 保证秩二的两种且仅两种表示：两个不同物理点，或一个真正 first jet。$T_3$ 支持于
$$
E=\mathbb Cy+\operatorname{Ran}H+\operatorname{Ran}V,\qquad\dim E\le5.
$$
所以反设 (1.4) 失败即有 $\operatorname{ess}(T_3)=E$、$\dim E=5$。于是任何下面选取的 $(y,z,w,u,v)$ 都线性无关：$z,w$ 为 H 的两列，$u,v$ 为 V 的两列。尤其两物理除子彼此不交，$y\ne0$。

原 $K$ 在六维上非退化（$\det K=-25600$）。任何五空间的限制型秩至少四：
$$
\dim\operatorname{rad}(K|_E)\le\dim E^{\perp_K}=1,\qquad
\operatorname{rank}K|_E\ge4.
\tag{1.5}
$$
下面的矛盾都针对这个必要下界。

## 2. 可逆尺度规范和两个通用原梯度后果

约化 H 可准确规范为
$$
H=\tfrac12(z^2+w^2),
\tag{2.1}
$$
把两个非零系数的平方根吸收进物理代表即可。此时 $zKz=wKw=0$，记
$$
g=zKw,\qquad a=p^{\mathsf T}z,\qquad b=p^{\mathsf T}w.
$$
(1.1) 的 Gaussian 部分在 $(y,z,w)$ 基中的三个系数给
$$
F^2-a^2-b^2+g^2=0,\qquad Fa=gb,\qquad Fb=ga.
\tag{2.2}
$$
V 部分支持于独立的 $\operatorname{span}(u,v)$，所以不能抵消这些系数。

非约化 H 可准确规范为
$$
H=z\otimes w+w\otimes z.
\tag{2.3}
$$
原表示 $h z_0^2+k(z_0w_0+w_0z_0)$、$k\ne0$，先令 $z=z_0$、$w=kw_0+(h/2)z_0$ 即得 (2.3)。$z$ 仍为物理值，$w$ 为一个非零缩放、允许加值向量的真正切向代表。故
$$
zKz=zKw=0,\qquad \delta=wKw.
$$
此时
$$
Hp=bz+aw,\quad HKH=\delta z^2,\quad\tau_2=0.
$$
Gaussian 三系数准确为
$$
F^2-4ab=0,\qquad Fa=0,\qquad Fb=2\delta a.
$$
若 $F\ne0$，后两式给 $a=b=0$，与第一式矛盾。因此
$$
\boxed{F=0,\qquad ab=0,\qquad\delta a=0.}
\tag{2.4}
$$

约化 V 可规范为
$$
V=\tfrac12(u^3+v^3)
\tag{2.5}
$$
（吸收两个非零系数的立方根）。记 $e=uKv$、$x=p^{\mathsf T}u$、$t=p^{\mathsf T}v$。独立的两个 V 系数给
$$
x^2=2G_H(u),\qquad t^2=2G_H(v).
$$
最高式分别在两个原物理点评价，利用 $uKu=vKv=0$，再给
$$
\boxed{x^3=t^3=e^3.}
\tag{2.6}
$$
若 $e=0$，即 $x=t=0$。若 $e\ne0$，$x/e,t/e$ 都是三次单位根。把 $u$ 乘以 $t/e$、$v$ 乘以 $x/e$，仍保持 (2.5)，并使新的记号满足
$$
\boxed{x=t=e\ne0.}
\tag{2.7}
$$
这是可逆尺度变换，不漏掉任一三次根分支。

非约化 V 保全部 value 系数：
$$
V=c u^3+d\operatorname{Sym}_{\Sigma}(u^2v),\qquad d\ne0,
\tag{2.8}
$$
其中 $c$ 可零，$uKu=uKv=0$，记 $\epsilon=vKv$。两个完整 V 系数给
$$
x^2=2G_H(u),\qquad xt=2H(Ku,Kv).
$$
最高式在物理值 $u$ 处的最后项为零，故 $x^3-6xG_H(u)=-2x^3=0$。于是
$$
\boxed{x=0,\quad G_H(u)=0,\quad H(Ku,Kv)=0,\quad V_p=dt\,u^2.}
\tag{2.9}
$$

各式均在一般原 H、V 三阶项保全之后推得。下文只用这些必要原条件。对 H 梯度，除了实际物理值的 $N(z,z)=0$，在切向点也可用 $N(z,w)=0$：这是零多项式 $N(u(s),u(s))$ 的一次局部导数，再加允许的 value 倍数，不是新增独立变分假设。

## 3. 约化 H 与非约化 V

使用 (2.1)、(2.8)，置四个真实交叉配对
$$
A=zKu,\quad B=wKu,\quad C=zKv,\quad D=wKv.
$$
(2.9) 给
$$
A^2+B^2=0,\qquad AC+BD=0.
\tag{3.1}
$$

### 3.1 原 H 两点非正交时

设 $g\ne0$。由 (2.2)，$F=0$ 会迫 $a=b=0$ 并继而 $g=0$，所以 $F\ne0$。仍保留全部两种 Gaussian 可能：
$$
\begin{cases}
a=b=0,\quad F^2=-g^2;\\
(a,b)\ne(0,0),\quad F^2=g^2.
\end{cases}
\tag{3.2}
$$
特别没有删掉零 $Hp$ 例外。

用 (1.2) 在两个 H 物理值评价，并用 $Fa=gb,Fb=ga$，准确得到
$$
N(z,z)=-F(a^2+g^2)+4dt A^2=0,
$$
$$
N(w,w)=-F(b^2+g^2)+4dt B^2=0.
$$
相加，再用 (3.1)、(2.2)，得
$$
F(F^2+3g^2)=0.
$$
而 (3.2) 的两种可能分别使括号为 $2g^2$ 或 $4g^2$，都非零。矛盾。

### 3.2 原 H 两点正交时

设 $g=0$。(2.2) 给 $F=0$、$a^2+b^2=0$。H 的整个二空间全等向，$HKH=0$。此时在两物理值评价 N 给
$$
dt A^2=dt B^2=0.
$$
若 $dt\ne0$，则 $A=B=0$。最高式在 $z,w$ 处的 H 项及 V 项均零，故 $a^3=b^3=0$，即 $Hp=0$。于是 $N=4dt\,u^2$，其原极线二次式 $4dt(k_u)^2$ 非零，与完整 H 梯度矛盾。因此 $t=0$。

现在 $V_p=0$，且
$$
N=-2\{y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\}.
$$
其原极线恒等式为 $P\,k_{Hp}=0$。$P\ne0$，多项式环无零因子且 K 可逆，因此 $Hp=0$，也就是 $a=b=0$。所以 $y$ 与全部 $z,w,u,v,y$ 正交，是 $K|_E$ 的根向量。

(3.1) 迫
$$
M=\begin{pmatrix}A&C\\B&D\end{pmatrix}
$$
秩至多一：若第一列为零则显然；否则它是二维标准型的一条等向线，第二列与它正交，故属于同一条线。H 块的 Gram 为零，V 块的 Gram 只可能有一个非零对角项 $\epsilon$。因此
$$
\operatorname{rank}K|_E
=\operatorname{rank}
\begin{pmatrix}0_2&M\\M^{\mathsf T}&\operatorname{diag}(0,\epsilon)\end{pmatrix}
\le2\operatorname{rank}M+1\le3,
$$
违反 (1.5)。这一类型全部排除。

## 4. 非约化 H 与约化 V

使用 (2.3)、(2.5)，仍记 $A,B,C,D$ 为上节四个交叉配对。由 (2.6)，先分 $e$。

若 $e\ne0$，采用 (2.7)。V 两个 mean 系数是
$$
4AB=e^2,\qquad4CD=e^2.
\tag{4.1}
$$
由 $F=0$，N 在 $z$ 的物理值和一次 jet 给
$$
N(z,z)=2e(A^2+C^2)=0,
$$
$$
N(z,w)=-2\delta a^2+2e(AB+CD)=0.
$$
(2.4) 已给 $\delta a=0$。于是后一式迫 $AB+CD=0$，与 (4.1) 的 $AB+CD=e^2/2\ne0$ 矛盾。因此
$$
e=0,\qquad x=t=0,\qquad AB=CD=0.
\tag{4.2}
$$

此时 $V_p=0$，完整 H 极线式准确为
$$
P(a k_w+b k_z)=\delta(k_z)^2.
\tag{4.3}
$$
若 $a\ne0$，(2.4) 给 $b=\delta=0$，则 (4.3) 是 $aP k_w=0$，不可能。
所以 $a=0$，(4.3) 除去非零多项式 $k_z$ 后成为
$$
bP=\delta k_z.
$$
若 $b\ne0$，K 可逆使 $y$ 与 $z$ 成比例（$\delta=0$ 时甚至 $y=0$），均违反五列独立。因此
$$
a=b=\delta=0.
\tag{4.4}
$$
现在 $y$ 与全部 E 正交，H 和 V 的两个 Gram 块都为零。

最高式在 H 物理值 $z$ 及其一次 jet 评价给
$$
A^3+C^3=0,\qquad A^2B+C^2D=0.
\tag{4.5}
$$
第一式和 (4.2) 已足够：若 $A=0$，则 $C=0$；若 $A\ne0$，则 $C\ne0$，继而 $B=D=0$。两种情形都使交叉矩阵 M 秩至多一。因此 $K|_E$ 的秩至多二，违反 (1.5)。这一类型全部排除。

## 5. H 与 V 都为非约化长度二

使用 (2.3)、(2.8)。由 (2.9)，
$$
x=0,\qquad AB=0,\qquad AD+BC=0,\qquad V_p=dt\,u^2.
\tag{5.1}
$$
由 (2.4)，$F=0,ab=0,\delta a=0$。完整 N 在两个物理值 $z,u$ 的评价给
$$
dt A^2=0,\qquad\delta A^2=0.
\tag{5.2}
$$

### 5.1 若 $A\ne0$

(5.1)—(5.2) 给 $B=D=\delta=t=0$。于是 $N=-2\operatorname{Sym}_{\Sigma}(y\otimes Hp)$，它的原极线式再次给 $Hp=0$，所以 $a=b=0$。$y$ 正交于全部 E，H 的 Gram 为零，而 M 秩至多一、V 的 Gram 秩至多一。故整个限制型秩至多三，违反 (1.5)。

### 5.2 若 $A=0$

最高式在 H 值 $z$ 处给 $a^3=0$，所以 $a=0$；(5.1) 给 $BC=0$。记两个不同物理值的极线为
$$
L=k_z,\qquad A_0=k_u.
$$
完整 N 极线式准确化为
$$
\boxed{bP L=\delta L^2+dt A_0^2.}
\tag{5.3}
$$

若 $b=0$，两个独立极线 $L,A_0$ 的平方也独立，故 (5.3) 给 $\delta=dt=0$，即 $\delta=t=0$。这时 $y$ 正交于全部 E，H 的 Gram 为零，而 $\det M=-BC=0$；如前，限制型秩至多三，矛盾。

只余 $b\ne0$。在 H 物理值处选任意局部坐标及非零齐次平凡化。$a=0$ 且 $b\ne0$ 意味着
$$
\operatorname{ord}P=1.
\tag{5.4}
$$
因为 $w$ 是非零缩放的真正一阶 jet 加值向量，$b=p(w)$ 就是非零缩放的一阶导数。

原自接触表给
$$
r=\operatorname{ord}L\in\{2,3,4\},\qquad
\delta\ne0\ \Longleftrightarrow\ r=2.
\tag{5.5}
$$
见[共同 jets 原接触表](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md) §1；有限特殊点为 $2,-6$ 的三接触和 $0$ 的四接触，无穷远亦为四接触。等价性也直接来自沿物理曲线对 $uKu=0$ 二次求导：$K(u,u'')=-K(u',u')$。允许的切向缩放和加值项不改变零性或根阶。

又因 $A=0$ 且 $z,u$ 不同，$m=\operatorname{ord}A_0\ge1$。若 $\delta\ne0$，(5.3) 左边阶数为三，右边第一项阶数四，第二项若非零则阶数为偶数 $2m$。右边若有低于四的项，其最低阶是二；否则其阶数至少四。均不可能等于三。

若 $\delta=0$，则 $r=3$ 或 $4$。式 (5.3) 两边非零，故 $dt\ne0$，并有
$$
r+1=2m.
$$
$r=4$ 使奇数五等于偶数，不可能。$r=3$ 只能使 $m=2$。这时
$$
uKz=uKw=0,\qquad zKz=zKw=wKw=0,\qquad uKu=0.
$$
三个独立物理列 $(z,w,u)$ 张成一个全等向的 $2z+u$ jet 三空间。这已被[全等向长度三物理 jets 的完整分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md)排除：原型只有 $W_+$、$W_-$ 的三个不同点，不存在 $2+1$ 型。故最后一支也不可能。

上述局部论证原样覆盖无穷远，没有除掉任何无穷远最高系数，也没有另假设异点根皆简单。

## 6. 结论及保留的范围

至少一个非约化支撑的三种配对已全部排除五维反设，故定理 (1.4) 成立。它是对原完整 rankH2、rankV2 层的真实维数排除；不把本质四维点误作已消去。

两个支撑都约化时，(2.2) 还有
$$
g\ne0,\quad a=b=0,\quad F^2+g^2=0
$$
这一完整 Gaussian 分支。本稿始终保留该分支，在 §3 仅因 V 非约化才把它排掉；对约化 V 不能套用 §3 的 $A^2+B^2=0$。因此本稿不声称整个 rankH2 层的本质五维部分已经关闭。

证明只用显示的原完整梯度、可逆尺度规范、实际物理值及一阶 jet、六维非退化型的秩下界，以及已登记的接触表/无全等向 $2+1$。没有新的未执行计算门；既有精确门也不重跑。普通 ISP、原全局 Jacobian 自然幂和算子逆仍不由本结论完成。

**后续完整闭合（2026-11-26）：** [原两个H值方程的17矛盾](R150-appendix-rank-two-second-and-third-cumulants-have-essential-dimension-at-most-four.md)现已排尽最后双约化Gaussian规范，整个rankH=rankV=2的本质维数至多四。本文必要归约保持有效；旧规范不再需要额外物理投影消元。
