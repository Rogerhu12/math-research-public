# R271 附录：缩放回文四头的真实两费反例与同源规范负图

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：完整解析证明。** 本文给出固定四维 nilpotent 头、固定十一位 Boolean 尾的一族真实来源，其左最小费用为一，而完整裸费及准确变换源费用同时趋零。再用同一正滤波，反例保留在真实同返回源规范负图内。所有右侧最小化、物理高低旗与全来源对偶都保留。

因此，在任意 nilpotent 头和任意正权 Boolean 尾这一类中，不存在只依赖头高度 $h$ 的两费常数。本文不是原固定 $A_m$、原连续尾或同一个实际 $w\in W$ 的反例。后续若要证明原目标，必须使用其实际权或同一来源的额外性质。

本稿使用并重写
[旧回文四头模型](R271-appendix-palindromic-four-head-actual-minimal-sources-and-two-form-nonuniformity.md)
的完整有限参数化。旧稿只排两形式比较；本文改变头与尾的相对尺度，并对**全部来源自由的完整右链**证明对偶界，所以结论不依赖“某个完整能量很大便推出其逆很小”这一错误推理。

## 1. 实际模型与两种费用

取 $0<a\le1$，置
$$
b=\frac14,\qquad c=a,\qquad
\varepsilon=a^{15},\qquad \beta=a^{10},
$$
$$
C_a=cA_\varepsilon,\qquad
A_\varepsilon=
\begin{pmatrix}
0&1&b&0\\
0&0&\varepsilon&b\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
\tag{1.1}
$$
这是一个高度 $h=4$ 的单链 nilpotent 头。其实际首、末跃迁为 $a$，两条长跃迁为 $a/4$，中间跃迁为 $a^{16}$；尾的三个权为 $1$，另八个权为 $\beta=a^{10}$。不以含混的整体强弱标签替代这些具体比例。

尾空间为十一位标准 Boolean Hilbert 空间，$D$ 为真实正权删除。记
$$
E_{j,p}=\ker D^j\cap\mathcal H_p,\qquad q=1.
$$
完整右域的第 $j$ 段为
$$
\mathscr C_j=
\bigoplus_{i=0}^{4-j}e_iE_{4-i,1+j},
\qquad 1\le j\le4,
$$
并使用全部方程
$$
Fc=Dc_1,\qquad
C_ac_j+Dc_{j+1}=0\quad(j<4),\qquad
C_ac_4=0.
\tag{1.2}
$$
第 $j$ 段的高输入是
$$
\bigoplus_{i=0}^{4-j}e_iE_{j-1,1+j}.
\tag{1.3}
$$
裸链是原低输出核中的真实低输入代表，不是任意删去一部分系数。记其最小列为 $J_b$，完整右最小列为 $J_f$，左最小列为 $U$。在共同实际来源空间上，
$$
L=U^*U,\qquad B=J_b^*J_b,\qquad H=J_f^*J_f.
$$
置
$$
\mu(r)^2=\langle Lr,r\rangle,\qquad
\alpha(r)^2=\langle Br,r\rangle,
$$
$$
\operatorname{flat}(r)^2
=\langle H^{-1}Lr,Lr\rangle,\qquad
\Xi(r)^2=\alpha(r)^2+\operatorname{flat}(r)^2.
\tag{1.4}
$$
这些均为有限维的真实最小费用。$B\le H$ 来自完整链的正交低投影；没有交换最小逆与高低压缩。

在 $S_3\times S_8$ 固定块中，以 $x^u y^v$ 记两个群的物理平均占据向量。准确地，
$$
D=\partial_x+\beta\partial_y,\qquad
\|x^u y^v\|^2=
\frac1{\binom3u\binom8v}.
\tag{1.5}
$$
物理强次数只能为 $u\le3$。定义
$$
g_0=\beta x-y,\qquad
z_\beta=\|g_0\|^2=\frac{\beta^2}{3}+\frac18,\qquad
g=g_0/\sqrt{z_\beta},
$$
以及来源
$$
\boxed{r_a=c(e_2+be_1)g=C_a(e_3g).}
\tag{1.6}
$$

**主结论。** 对所有 $0<a\le1$，
$$
\boxed{
\mu(r_a)=1,\qquad
\alpha(r_a)^2\le256a^2,\qquad
\operatorname{flat}(r_a)^2\le40000a^6.
}
\tag{1.7}
$$
因此 $\Xi(r_a)\to0$。

## 2. 对称约化与准确左泛函

两置换群以酉方式保持 $D,D^*$、全部幂核旗、完整方程及裸低方程。来源 (1.6) 固定。群平均保持可行性且不增加范数，故其真实最小者就在固定块中。

同样，对下文的任意完整右链，来源的指定固定泛函不受群平均改变。因此证明这个泛函的全链对偶上界时，也可先作群平均。这里没有把完整 Boolean 空间的最小化换成一个非约化试探子空间。

左方程为
$$
C_av_0+Dv_1=0,\qquad C_av_1=r_a.
$$
源方程逐头迫使
$(v_1)_3=g$、$(v_1)_2=(v_1)_1=0$。由于 $Dg=0$，取
$v_0=0$ 及其他自由分量为零即可达到最小。故
$$
\boxed{Ur_a=e_3g,\qquad\mu(r_a)=1.}
\tag{2.1}
$$

更一般地，设 $s$ 是任何合法来源，$v=Us$。源方程总给
$$
(v_1)_3=s_2/c.
$$
所以在**整个共同来源空间**上，
$$
\boxed{
\langle Lr_a,s\rangle
=\langle e_3g,Us\rangle
=\langle g,s_2/c\rangle.
}
\tag{2.2}
$$
若群平均后 $s_2=c\sigma g_0$，则这个泛函的绝对值是
$|\sigma|\sqrt{z_\beta}$。其他源头分量没有被固定或删除。

## 3. 一个真实裸候选及统一小量

本节先使用未归一化的 $g_0$。令
$$
\theta=\frac{\varepsilon}{6b\beta}
=\frac23a^5,
$$
并取
$$
Z=\frac{x^3g_0}{6}-\frac{g_0^4}{6\beta^3},
$$
$$
W=\frac{\theta}{6}x^3g_0^2
-\frac{\theta}{2\beta^2}xg_0^4
+\frac{\theta}{3\beta^3}g_0^5.
\tag{3.1}
$$
这些完整组合的 $x^4,x^5$ 项准确相消，故是合法物理向量。
它们满足 $D^3Z=g_0$、$D^4W=0$。

原未缩放头 $A_\varepsilon$ 的完整链可以取
$$
\begin{array}{lll}
q_{1,1}=bD^2Z,&q_{1,2}=D^2Z,&q_{1,3}=-D^3W,\\
q_{2,0}=-2bDZ,&q_{2,1}=bD^2W-\varepsilon DZ,&q_{2,2}=D^2W,\\
q_{3,0}=\varepsilon Z-2bDW,&q_{3,1}=-\varepsilon DW,&\\
q_{4,0}=\varepsilon W.&&
\end{array}
\tag{3.2}
$$
其来源为 $(e_2+be_1)g_0$。逐行乘 $c^j$ 后，即为缩放头 $C_a$ 的同源完整候选；最后再除以 $\sqrt{z_\beta}$。

其完整范数可以很大，但真正低投影有以下合法代表。第1、2段保持 (3.2)，第3、4段只加相应高旗
$\chi_p=y^{p-3}g_0^3$ 的倍数。准确得到
$$
\begin{array}{lll}
q_{1,1}=b xg_0,&q_{1,2}=xg_0,&q_{1,3}=-\theta g_0^2,\\
q_{2,0}=-b x^2g_0,&
q_{2,1}=b\theta xg_0^2-\varepsilon x^2g_0/2,&
q_{2,2}=\theta xg_0^2,\\
\widetilde q_{3,0}=\dfrac{\varepsilon}{6\beta}x^2yg_0,&
\widetilde q_{3,1}=-\dfrac{\varepsilon\theta}{2\beta}xyg_0^2,&\\
\widetilde q_{4,0}=\dfrac{\varepsilon\theta}{6\beta^2}xy^2g_0^2.&&
\end{array}
\tag{3.3}
$$
每项都是物理强次数至多3的多项式。改变只在高输入内，所以低投影仍是同一个真实裸可行链。

对 $0<a\le1$，$\beta,\varepsilon\le1$、$\theta\le2/3$，
且 $\varepsilon^2=\beta^3$。由物理单项式范数至多1、系数三角不等式，(3.3) 四段的平方范数分别至多
$$
12,\qquad11,\qquad2,\qquad1.
$$
例如最后一项的系数和至多
$2\varepsilon\theta/(3\beta^2)=4/9$；没有留下一个负次幂。
因为 $z_\beta^{-1}\le8$，缩放、归一后有
$$
\alpha(r_a)^2
\le8(12c^2+11c^4+2c^6+c^8)
\le208c^2\le256a^2.
\tag{3.4}
$$

## 4. 完整右链的全来源对偶界

本节允许第零、第一源头的**全部合法自由度**。取任意完整右链 $q$，令其范数为 $E=\|q\|$，并先作群平均。写
$$
Fq=s,\qquad s_2=c\sigma g_0.
$$
把第 $j$ 段除以 $c^j$，得到未缩放头的完整内部方程。其危险坐标准确具有
$$
\begin{array}{lll}
c^{-1}q_{1,2}=D^2Z,&
c^{-1}q_{1,3}=-D^3W,&
c^{-2}q_{2,2}=D^2W,\\
c^{-2}q_{2,1}=bD^2W-\varepsilon DZ,&
c^{-3}q_{3,0}=\varepsilon Z-2bDW,&
c^{-4}q_{4,0}=\varepsilon W,
\end{array}
\tag{4.1}
$$
其中 $D^3Z=\sigma g_0$、$D^4W=0$。

确实，从最后一段定义 $W=c^{-4}q_{4,0}/\varepsilon$，第三段方程给
$c^{-3}q_{3,1}=-\varepsilon DW$；第二段第一头、再第一段第二头依次给
$q_{2,2}$ 与 $q_{1,3}$。定义
$Z=(c^{-3}q_{3,0}+2bDW)/\varepsilon$，剩下的两个内部头方程给 (4.1) 中的 $q_{2,1},q_{1,2}$。
这个推导没有使用或固定 $s_0,s_1$。

所有合法物理 $Z,W$ 都准确写为
$$
Z=\frac{\sigma x^3g_0}{6}+u x^2g_0^2+v xg_0^3
-\left(\frac{\sigma}{6\beta^3}+\frac u{\beta^2}+\frac v\beta\right)g_0^4,
$$
$$
W=\frac{\theta}{6}x^3g_0^2+\frac{\zeta}{2}x^2g_0^3
-\left(\frac{\theta}{2\beta^2}+\frac{\zeta}{\beta}\right)xg_0^4
+\left(\frac{\theta}{3\beta^3}+\frac{\zeta}{2\beta^2}\right)g_0^5.
\tag{4.2}
$$
这是 $D=\partial_x$（固定 $g_0$）的一般解，再由强次数至多3消去非法最高项；不丢自由参数。

定义五个无量纲坐标
$$
U=\beta u,\quad V=\beta^2v,\quad
A=\frac{\beta\theta}{\varepsilon},\quad
B_1=\frac{\beta^2\zeta}{\varepsilon},
$$
$$
X=V-bB_1,\qquad
Z_1=-\frac{\sigma}{6}-U-V+bA+2bB_1,\qquad
W_1=\frac A3+\frac{B_1}{2}.
$$
它们有准确的线性恒等式
$$
\boxed{
-\frac{\sigma}{6}
=X+\frac b2B_1+U+Z_1-3bW_1.
}
\tag{4.3}
$$

下面只读取真正物理坐标：

- $q_{1,2}$ 的 $y^2$ 系数是 $2cu$；
- $q_{2,2}$ 的 $y^3$ 系数是 $-c^2\zeta$；
- $q_{2,1}$ 的 $y^3$ 系数是 $c^2(\varepsilon v-b\zeta)$；
- $q_{3,0}$ 的 $y^4$ 系数是 $c^3\varepsilon Z_1/\beta^3$；
- $q_{4,0}$ 的 $y^5$ 系数是 $-c^4\varepsilon^2W_1/\beta^4$。

由于 $\|y^2\|^{-1}=\sqrt{28}$、
$\|y^3\|^{-1}=\|y^5\|^{-1}=\sqrt{56}$、
$\|y^4\|^{-1}=\sqrt{70}$，这些坐标给
$$
|U|\le\sqrt7\,\frac{\beta}{c}E,
$$
$$
|B_1|,\ |X|
\le\sqrt{56}\,\frac{\beta^2}{c^2\varepsilon}E,
$$
$$
|Z_1|\le\sqrt{70}\,\frac{\beta^3}{c^3\varepsilon}E,\qquad
|W_1|\le\sqrt{56}\,\frac{\beta^4}{c^4\varepsilon^2}E.
\tag{4.4}
$$
将 (4.4) 代入 (4.3)，并保来源归一化，得到
$$
\begin{aligned}
|\sigma|\sqrt{z_\beta}
\le6\sqrt{z_\beta}\bigg[
&\sqrt{56}\left(1+\frac b2\right)
 \frac{\beta^2}{c^2\varepsilon}
+\sqrt7\frac{\beta}{c}\\
&+\sqrt{70}\frac{\beta^3}{c^3\varepsilon}
+3b\sqrt{56}\frac{\beta^4}{c^4\varepsilon^2}
\bigg]E.
\end{aligned}
\tag{4.5}
$$
原具体参数给四个幂
$$
\frac{\beta^2}{c^2\varepsilon}=a^3,\quad
\frac{\beta}{c}=a^9,\quad
\frac{\beta^3}{c^3\varepsilon}=a^{12},\quad
\frac{\beta^4}{c^4\varepsilon^2}=a^6.
$$
又 $z_\beta<1$、$b=1/4$，所以统一地
$$
\boxed{
|\sigma|\sqrt{z_\beta}\le200a^3\|q\|.
}
\tag{4.6}
$$
(4.6) 对所有完整右链成立，而非只对来源 (1.6) 的最小链成立。

## 5. 为什么 (4.6) 正好支付真实 flat

把完整源映射仍记为
$F:\mathcal Y_f\to\mathscr R$。其实际源 Gram 是
$G=FF^*=H^{-1}$。因此
$$
\operatorname{flat}(r_a)^2
=\|F^*Lr_a\|^2
=\sup_{q\in\mathcal Y_f,\ q\ne0}
\frac{|\langle Lr_a,Fq\rangle|^2}{\|q\|^2}.
\tag{5.1}
$$
若以一个更大的完整右环境取上确界，也只会给上界；本文并不依赖删除共同来源限制。

根据 (2.2)，群平均后的分子准确为
$|\sigma|^2z_\beta$。因此 (4.6) 直接给
$$
\boxed{\operatorname{flat}(r_a)\le200a^3.}
\tag{5.2}
$$
这是全来源算子对偶估计，严格保留 $H^{-1}Lr_a$ 的顺序。
它没有从 $H(r_a)$ 的大值推断 $H^{-1}$ 在另一方向上的大小。

(2.1)、(3.4)、(5.2) 合在一起即证明 (1.7)。

## 6. 反例仍可放进准确的同源规范负图

为明确量词，下面在同一个有限来源空间上作一次已付正滤波。
设
$$
S_b=L+B,\qquad S_f=L+H,\qquad
\mathcal E=S_b^{-1}L-S_f^{-1}L.
\tag{6.1}
$$
有
$$
S_b\mathcal E=(H-B)(L+H)^{-1}L.
\tag{6.2}
$$
所以 $\mathcal Er$ 对 $\ker(H-B)$ 为 $S_b$ 正交。
这里 $\ker C_{\rm s}$ 上两种右费用确实相同：因 $C_a$ 是单链，任何这类合法来源写成 $r=e_0h$。单首段 $(e_0D^\dagger h,0,0,0)$ 是完整右可行链；$C_a$ 与尾上的 $D^\dagger$ 交换，且 $C_ae_0=0$。首段没有高输入可删除，完整与裸链都受方程 $Dc_1=r$ 的相同最小范数下界约束，上述候选同时达到它。因此 $\langle(H-B)r,r\rangle=0$；由 $H-B\ge0$ 得 $(H-B)r=0$。故
$$
\operatorname{Ran}\mathcal E
\subseteq(\ker(H-B))^{\perp_{S_b}}
\subseteq(\ker C_{\rm s})^{\perp_{S_b}}.
\tag{6.3}
$$

这里也可用有限矩阵直接核滤波预算。以 $L^{1/2}$ 作等距坐标，置
$$
X=L^{-1/2}BL^{-1/2},\qquad
Y=L^{1/2}H^{-1}L^{1/2}.
$$
因为 $B\le H$，有 $Y\le X^{-1}$。滤波变为
$$
E=I-X(I+X)^{-1}-Y(I+Y)^{-1},
$$
从而
$$
0\le E\le I,\qquad I-E\le X+Y,
$$
$$
E\le(I+X)^{-1},\qquad E\le(I+Y)^{-1}.
$$
后两式分别给
$EXE\le E-E^2$、$EYE\le E-E^2$。因此
$$
E(X+Y)E\le2E(I-E)\le2(X+Y),
$$
以及 $(I-E)^2\le I-E\le X+Y$。还原原度量便得
$$
\boxed{
\mu(r-\mathcal Er)\le\Xi(r),\qquad
\Xi(\mathcal Er)^2\le2\Xi(r)^2.
}
\tag{6.4}
$$
这段证明不需要 $\mathcal E$ 与 $X,Y$ 交换。

取 $r=r_a$，由 (1.7)
$$
\mu(\mathcal Er_a)\ge1-16a-200a^3.
$$
例如 $0<a\le1/64$ 时该值大于 $1/2$。定义同源规范来源
$$
\widehat r_a=
\frac{\mathcal Er_a}{\mu(\mathcal Er_a)}.
$$
则
$$
\boxed{
\begin{aligned}
&\widehat r_a\in(\ker(H-B))^{\perp_{S_b}}
 \subseteq(\ker C_{\rm s})^{\perp_{S_b}},\qquad
\mu(\widehat r_a)=1,\\
&\Xi(\widehat r_a)^2
\le2048a^2+320000a^6\longrightarrow0.
\end{aligned}
}
\tag{6.5}
$$
这是原来源空间内的线性滤波和归一化，不是另选一个尾模型或丢掉返回方程。

## 7. 严格排除的范围

本族始终保持：

- 头高度 $h=4$、单链及反序共轭对称；
- 十一位完整正权 Boolean 尾；
- 原物理 Hilbert 度量及全部高低输入旗；
- 左、裸右、完整右的真正最小化；
- $H^{-1}Lr$ 的准确全来源对偶；
- 以及 (6.5) 的同返回源规范负图。

故不存在只依赖 $h$ 的有限常数 $\kappa(h)$，使这一整个模型类都满足
$$
\mu(r)^2\le\kappa(h)
\left[\alpha(r)^2+\operatorname{flat}(r)^2\right]
$$
——即使只要求它在 (6.5) 的规范负图上成立。

尾中的强权始终为1，弱权为 $a^{10}$；头首末权为 $a$，中间权为 $a^{16}$。例如首末权与弱尾之比为 $a^{-9}$，但它仍小于固定强尾1。不能用一个笼统的头尾强弱说法代替本族的具体尺度。

此处没有把任一 $C_a$ 认作原固定 $A_m$，没有把有限两档尾认作原连续尾，也没有构造原实际同一个 $w\in W$ 的来源。反例排除了只靠 nilpotence、通用源收缩及同源规范便推出维数型常数的路线；原连续模型的实际权与同来源性质仍须继续使用，原 $N=M$ 未完成。
