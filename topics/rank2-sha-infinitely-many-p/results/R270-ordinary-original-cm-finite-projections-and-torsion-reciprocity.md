# R270 — 普通三原源的真实 CM 有限权投影、首非中央 carry 与十七挠值互反

日期：2026-11-13。**状态：以下有限系数公式、完整中央零的前三层必要条件、固定十七挠点的精确互反及原有限系数对其余商项的检测均已证明。没有把固定挠值对数当作完整中央导数；无穷多个目标素数的非零仍开。**

本篇沿 R55/R60、R263/R266 的**同一个普通测度**继续。R268 的裸 de Rham 方向只有乘回原 frame 后才能使用；本文最后明确这个乘子。所有求系数都是统一代数公式，不扫描目标素数。

## 1. 三个真实来源与共同首对角

在 $E_0:y^2=x^3-x$ 上取 $dz=dx/(2y)$，并置
$$
u=x^{-1/2},\qquad v=u^4,\qquad t=\sqrt{1-v},\qquad
z=uF(v),
$$
$$
F(v)=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+1)}v^n,\qquad
\Theta(v)=\vartheta(z(v)).
\tag{1}
$$
所有平方根都取原点常数一的支；$u=z+\cdots$。准确有
$$
\frac{dz}{du}=\frac1{\sqrt{1-v}},\qquad
\frac{\Theta'}{\Theta}
=\frac1{4\sqrt{1-v}}
 \sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+3)}v^n.
\tag{2}
$$

取 R243/R263 同一规范
$$
S_A=A_{17}(2z)/16,\qquad S_B=A_{34}(z),\qquad S_H=A_{136}(z).
\tag{3}
$$
三者首项均为 $z^4$，共同 theta charge 为 $68$。这三条曲线的参数分别为
$17,34^2,136$，没有把第二条误写为参数 $34$。

记
$$
Q(s)=s+\frac35s^2-\frac15s^3+\frac15s^4.
$$
令 $P_{34},P_{15}$ 为 R115、R243 已给出的固定多项式，明确为
$$
P_{34}(U)=\frac15U(U-1)(U+1)^2(U^2-2U+5)(5U^2-2U+1)Q_8(U),
$$
$$
Q_8=U^8+364U^6-1088U^5+1190U^4-1088U^3+364U^2+1,
$$
$$
P_{15}(U)=
\frac{(U+1)(U^2-6U+1)(5U^2-2U+1)}{55}Q_{10}(U),
$$
$$
Q_{10}=11U^{10}-54U^9+899U^8+1176U^7-9066U^6+
9500U^5-6114U^4+5080U^3-2625U^2+170U-1.
$$
定义固定多项式
$$
\begin{aligned}
Q_A(v)&=\frac{(1+v)^{17}}{16}
 Q\!\left(\frac{16v(1-v)^2}{(1+v)^4}\right),\\
Q_B(v)&=v^{17}P_{34}(1/v),\\
Q_H(v)&=v^{16}P_{15}(1/v).
\end{aligned}
\tag{4}
$$
第一式中分母已经被 $(1+v)^{17}$ 清除；三式首项都是 $v$。原来源准确为
$$
S_A=\Theta^{68}Q_A,\qquad
S_B=\Theta^{68}Q_B,\qquad
S_H=\Theta^{68}tQ_H.
\tag{5}
$$
因此放入**实际 residue 换元**后的三个角因子是
$$
a_A=Q_A/t,\qquad a_B=Q_B/t,\qquad a_H=Q_H.
\tag{6}
$$
第三条的平方根与 $dz/du$ 准确相消。这个相消发生在原权系数内，不是删除第三来源的 theta frame。

同时令 $S_0=\vartheta$、$c_0=1$、$a_0=1/t$，而 $c_A=c_B=c_H=68$。
对 $i\in\{0,A,B,H\}$ 写 $b_{i,n}=[z^n]S_i$。形式 residue 换元直接给
$$
\boxed{
b_{i,4k}=[v^k]\,a_i(v)\Theta(v)^{c_i}F(v)^{-4k-1}.
}
\tag{7}
$$
这里 $a_i$ 已包含 $(1-v)^{-1/2}$，不得再加一次 Jacobian。

固定普通素数
$$
p=4r+1\ge13,\qquad p\ne17.
\tag{8}
$$
所有三源和参考在该素位整。定义
$$
W_i=a_i\Theta^{68}=\sum_n w_{i,n}v^n,\quad
I_i=\sum_n\frac{w_{i,n}}{4n+1}v^n
\qquad(i=A,B,H).
$$
R263 的原中心质量零与 (7) 给 $w_{i,r}\in p\mathcal O$，且
$$
\boxed{
\frac{b_{i,p-1}}p
\equiv[v^r](I_i-W_i\log F)\pmod p.
}
\tag{9}
$$
证明和 R55 相同：$W_i(0)=0$，所需 $F$ 仅到 $r-1$，故
$F^{-p}=1-p\log F\bmod p^2$；首项必须保留 $w_{i,r}/p$ 的真实下一位。

## 2. 普通 CM division 对原低 theta frame 的精确代替

令
$$
\pi=\pi_0,\qquad b_0=\bar\pi,\qquad \pi b_0=p,
\qquad v_p(\pi)=1.
\tag{10}
$$
$\pi$ 是 $E_0$ 在所选普通素位的实际 Frobenius Gaussian 整数，采用 R266 的原正式群规范。
定义
$$
r_\pi(z)=\frac{\sigma(\pi z)}{\sigma(z)^p}=R(U),
\qquad U=x^2,\qquad \deg R=r.
\tag{11}
$$

**引理 1。** 原除法多项式满足
$$
R\in\mathcal O[U],\quad R(0)=1,\quad R(U)\equiv1\pmod p,
\quad [U^r]R=\pi.
\tag{12}
$$
令
$$
R^*(v)=v^rR(1/v),\qquad E(v)=R^*(v)/\pi.
\tag{13}
$$
则 $E(0)=1$，其次数小于 $r$ 的系数整，且
$$
[v^r]E=1/\pi.
\tag{14}
$$
原变量准确满足
$$
\boxed{
\begin{aligned}
\vartheta(\pi z)&=\vartheta(z)^pR(v),\\
u(\pi z)&=u\,\frac{R^*(v)}{R(v)},\\
v_\pi:=v(\pi z)&=\pi^4v\left(\frac{E(v)}{R(v)}\right)^4,\\
F(v)&=\frac{E(v)}{R(v)}F(v_\pi).
\end{aligned}}
\tag{15}
$$

**证明。** R266 的实际整正式 sigma 函数 $\Sigma$ 给
$r_\pi=\Sigma([\pi]\tau)/\Sigma(\tau)^p$。$[\pi]$ 的约化是实际 Frobenius，
故 $r_\pi\equiv1\bmod p$。其唯一极为 $O$ 处的 $p-1$ 阶极，且它在 $i$ 下不变，
所以它是次数 $r$ 的 $U$ 多项式；在 $O$ 的首项是 $\pi z^{1-p}$。
整性由原正式系数及互异单位首项的三角消元得出。

还须确定常数，不能只用模 $p$ 的近似。设 $T_0=(0,0)$、
$\tau_0(P)=P+T_0$。R266 的准确二挠除子计算给
$$
\epsilon=
\frac{r_\pi^2(x\circ[\pi])}{x^p(r_\pi\circ\tau_0)^2}\in\{1,-1\}.
$$
在 $O$ 比较首项，得到 $\epsilon R(0)^2=1$，从而 $R(0)^4=1$。
结合 $R(0)\equiv1\bmod p$、$p\ne2$，得 $R(0)=1$，故 $\epsilon=1$。
于是
$$
x(\pi z)=x\left(\frac{U^rR(1/U)}{R(U)}\right)^2.
$$
取与 $u(\pi z)=\pi u+\cdots$ 相符的平方根，得到 (15) 第二式。
第一式由 $\vartheta=\sqrt{x}\sigma$ 和同一个平方根规范逐项代入。
最后比较 $z=uF(v)$ 在 $\pi z$ 处的两种表达，得最后一式。
(13)–(14) 则直接来自 (12)。$\square$

这里 $R(v)$ 与 $R(U)$ 是同一个多项式在互为倒数的变量中取值。
恒等式 (15) 的第一式是**实际 theta division**；它没有创造一个可任意替代原源的分数 theta 次数。

## 3. 有限代数系数与模 $p^4$ 的第一非中央修正

令
$$
d=p-1,\qquad n_j=jd,\qquad j=1,2,3.
$$
定义完全由原 $R,E,a_i$ 得到的有限系数
$$
\boxed{
B_{i,j}=[v^{jr}]\,
 a_i(v)R(v)^{n_j+1-c_i/p}E(v)^{-n_j-1},
}
\tag{16}
$$
以及
$$
C_{i,j}=[v^{jr-1}]\,
 a_i(v)R(v)^{n_j-3-c_i/p}E(v)^{-n_j+3}.
\tag{17}
$$
$R^{-c_i/p}$ 的定义是次数 $3r$ 内的
$\exp(-c_i\log R/p)$。因为 $R-1\in p v\mathcal O[v]$ 且 $3r<p$，
所需指数阶乘都是单位，全部系数整。$E$ 的唯一非整系数已在 (14) 明确保留。

**定理 2。** 对所有 $i\in\{0,A,B,H\}$，
$$
\boxed{
b_{i,n_j}
=B_{i,j}+\frac{c_i\pi^4}{12p}C_{i,j}
       +O(p^{\,5-j}),\qquad j=1,2,3.
}
\tag{18}
$$
这里 $O(p^a)$ 指实际所选普通完备整数环中的 $p^a\mathcal O$，不隐藏周期。
特别地
$$
v_p(B_{0,j})=-(j-1).
\tag{19}
$$

**证明。** 由 (15) 的实际 theta 等式和常数一规范，
$$
\Theta(v)^{c_i}
=R(v)^{-c_i/p}
 \exp\!\left(\frac{c_i}{p}\log\Theta(v_\pi)\right).
\tag{20}
$$
对次数至多 $3r$，(2) 中 $H$ 所需分母 $4n+3$ 不被 $p$ 整除：
第一次出现的是 $4n+3=3p$、$n=3r$，而这只影响 $\log\Theta$ 的 $3r+1$ 次项。
积分和指数所除整数也小于 $p$，故 $\log\Theta$、$\Theta$ 在此范围内均整。

用权界
$$
v_p([v^k]E^aR^b)\ge-\left\lfloor k/r\right\rfloor
\tag{21}
$$
处理任意本证明所用整数 $a$ 及整低阶 $R^b$。
(21) 来自 $E$ 唯一的 $p^{-1}$ 系数位于次数 $r$，并在乘法、整数幂及单位逆下保持。
$F$ 到 $3r$ 的系数至多只有 $[v^r]F$ 带一个 $p$ 分母；下一次可能分母为 $5p$，
已超出范围。因而
$$
v_p([v^k](F(v_\pi)-1))
\ge4-\left\lfloor(k-1)/r\right\rfloor.
\tag{22}
$$
另一方面 $\log\Theta(v)=v/12+\cdots$，所以
$$
\frac{c_i}{p}\log\Theta(v_\pi)
=\frac{c_i\pi^4}{12p}\,v(E/R)^4+\text{余项}.
$$
在指数化后，余项系数的界至少为
$6-\lfloor(k-2)/r\rfloor$；$\log\Theta$ 的二次及以上项更有
$7-\lfloor(k-2)/r\rfloor$ 的界。

将这些式子代入 (7) 和 $F=(E/R)F(v_\pi)$。
常数部分给 (16)，指数的第一项给 (17)。
所有剩余正次数因子与 (21) 相乘，在次数 $jr$ 的总损失至多 $j-1$，
因为相应非负次数之和至多 $jr-1$。
最低剩余界来自 (22)，即 $4-(j-1)=5-j$，得到 (18)。

最后，R266 已确定 $M_\vartheta(0)=1-b_0^{-1}$ 为单位。
故所有正 principal 权的真实参考矩均为单位；
原周期和 Euler 因子也为单位，而
$v_p(n_j!)=j-1$。所以 $v_p(b_{0,n_j})=-(j-1)$。
(18) 的修正相对提高至少三阶，故 (19) 成立。$\square$

令 $M_i(u)$ 是 R263 的完整普通单位 Mellin 变换，
$$
q_i(u)=M_i(u)/M_\vartheta(u),\qquad
\widetilde q_{i,j}=B_{i,j}/B_{0,j}
\quad(i=A,B,H).
\tag{23}
$$
其变量按 $x^{du}$ 规范。$q_i$ 是整 Iwasawa 级数在这个解析变量中的值，$q_i(0)=0$。
真正的正权比值含各自 Euler 因子：
$$
q_i(j)=
\frac{1-b_i^{-1}(p/b_i^2)^{n_j}}
     {1-b_0^{-1}(p/b_0^2)^{n_j}}\,
 \frac{b_{i,n_j}}{b_{0,n_j}}.
\tag{24}
$$
同一正式周期和同阶阶乘在这里准确相消；单位缩放 (3) 已包括在 $b_{i,n}$ 中。
Euler 比值与一之差的估值至少为 $n_j$，故在本文模 $p^4$ 精度内可以由明示尾界省去。

定义真实非中央 tame $-4$ 行
$$
\boxed{
Z_i=\frac1{24}\,
 \frac{b_{i,p-5}}{b_{0,p-1}}\pmod p.
}
\tag{25}
$$
分母是单位，故定义无歧义。则
$$
\boxed{
q_i(j)\equiv\widetilde q_{i,j}
+\frac{17}{3}p^3b_0^{-4}
 j(j+1)(j+2)(j+3)Z_i
\pmod{p^4}.
}
\tag{26}
$$

**证明。** $\widetilde q_{i,j}$ 整，且属于 $p\mathcal O$，因为 $q_i(0)=0$，
$q_i(j)\in p\mathcal O$，而 (18) 的相对修正从 $p^3$ 才开始。
在 (18) 的分母展开中，参考的 $p^3$ 修正再乘 $\widetilde q_{i,j}\in p\mathcal O$，
故模 $p^4$ 消失。因 $\pi^4/p=p^3b_0^{-4}$，只需证明
$$
\frac{C_{i,j}}{B_{0,j}}
\equiv j(j+1)(j+2)(j+3)Z_i\pmod p.
\tag{27}
$$
(7)、(15) 与同一误差估计把左端模 $p$ 识别为
$b_{i,n_j-4}/b_{0,n_j}$。
R63 的**完整 Euler 分布**同样适用于 tame $-4$ 的正权：
所有 $n_j-4>0$，且在单位群上
$x^{n_j-4}\equiv x^{-4}\bmod p$。
因此它们的真实单位矩模 $p$ 相同；参考 principal 矩模 $p$ 也相同。
周期比给同一个 $\Omega_0^4$，而
$$
\frac{n_j!}{(n_j-4)!}
\equiv j(j+1)(j+2)(j+3)\pmod p.
$$
在 $j=1$ 时此积为 $24$，准确得到 (27)。
结合 $c_i/12=68/12=17/3$，证明 (26)。$\square$

这一步只使用 tame $-4$ 行的实际同余，未宣称它为单位或由三中央零控制。

## 4. 三条完整中央零的合法聚合条件

**定理 3。** 若任一原来源满足完整 $M_i'(0)=0$，则
$$
\boxed{
\begin{aligned}
\widetilde q_{i,1}&\in p^2\mathcal O,\\
4\widetilde q_{i,1}-\widetilde q_{i,2}&\in p^3\mathcal O,\\
3\widetilde q_{i,1}-\frac32\widetilde q_{i,2}
 +\frac13\widetilde q_{i,3}
 +68p^3b_0^{-4}Z_i&\in p^4\mathcal O.
\end{aligned}}
\tag{28}
$$
故三条完整中央导数同时为零时，(28) 对 $A,B,H$ 的同一 $R,E$ 同时成立。
它是一组明确的真实有限系数必要条件；没有把三个正权分别设为零。

**证明。** 对 $q=q_i$ 令
$$
\Delta_s=\sum_{j=0}^s(-1)^{s-j}\binom sjq(j).
$$
R60 的整 Iwasawa 商给 $\Delta_s\in p^s\mathcal O$。
完整导数零与收敛 Newton 对数公式给
$$
\sum_{s\ge1}\frac{(-1)^{s+1}}s\Delta_s=0.
$$
$p\ge13$ 时截到 $s=1,2,3$ 的尾界分别为 $p^2,p^3,p^4$。
前三个部分和明确是
$$
q(1),\qquad 2q(1)-\tfrac12q(2),\qquad
3q(1)-\tfrac32q(2)+\tfrac13q(3).
$$
代入 (26)，前两层的修正达到各自尾界。第三层中
$$
3\cdot24-\tfrac32\cdot120+\tfrac13\cdot360=12;
$$
再乘 $17/3$，所得系数正是 $68$。$\square$

特别地，第三层不能只写为三个 $\widetilde q$ 的齐次行关系。
$\vartheta(\pi z)$ 的首项在原聚合中留下 (25) 的实际非中央矩；
该项是随原共同 charge $68$ 出现的，不是独立可删的规范误差。

## 5. 固定十七挠点的精确 CM division 互反

以下固定
$$
\beta=4-i,\qquad N\beta=17,
$$
与普通 $\pi$ 区分。R248/R261 的实际 sigma division 多项式是
$$
\boxed{
K_\beta(U)=(4-i)U^4+(-12+20i)U^3
 +(28+10i)U^2+(-20-12i)U-i,
}
\tag{29}
$$
$$
r_\beta(z)=\frac{\sigma(\beta z)}{\sigma(z)^{17}}=K_\beta(x^2).
$$
特别地 $K_\beta(0)=-i$；不能把固定 $\beta$ 当作 (12) 规范中的 Frobenius $\pi$。
两者的单位相位不同。

对非零 $P\in E_0[\beta]$，定义固定非零代数数
$$
c_P=\left.\frac d{dz}r_\beta(z)\right|_{P}
 =4x(P)y(P)K_\beta'(x(P)^2).
\tag{30}
$$
这些数与目标普通素数 $p$ 无关。

**定理 4。** 对所有 (8) 中的 $p$ 及每个上述 $P$，
$$
\boxed{
r_\pi(P)^{17}
=\beta^{1-p}\frac{c_P^p}{c_{[\pi]P}}.
}
\tag{31}
$$
所有 $c_P$ 和 $r_\pi(P)$ 在 $p\nmid34$ 的素位都是单位。
对 $p$-adic 对数，准确有
$$
17\log_p r_\pi(P)
=(1-p)\log_p\beta+p\log_p c_P-\log_p c_{[\pi]P}.
\tag{32}
$$

**证明。** 两个实际 sigma division 的复合给完整有理恒等式
$$
r_\beta(z)^p r_\pi(\beta z)
 =r_\pi(z)^{17}r_\beta(\pi z).
\tag{33}
$$
它没有未定的指数因子或常数：两边展开均为
$\sigma(\pi\beta z)/\sigma(z)^{17p}$。
在 $z=P+w$ 比较一次项。左边是
$$
(c_Pw)^p\bigl(\pi(\beta w)^{1-p}+\cdots\bigr),
$$
右边是
$$
r_\pi(P)^{17}\bigl(c_{[\pi]P}\pi w+\cdots\bigr).
$$
消去共同 $\pi w$，得到 (31)。

在 $p\nmid34$ 的好约化中，$\beta$ 核是有限 étale，所有非零点保持非零，
且没有一点化成二挠点。故 $x(P),y(P)$ 及不同四元轨道间的
$x(P)^2$ 差都是单位。多项式 (29) 的首系数也是单位，因此 (30) 为单位。
$\pi$ 与 $\beta$ 互素，$r_\pi$ 在这些点无零极，(31) 再给其单位性。
对数是群同态且杀根单位，故 (32) 成立。$\square$

### 5.1 Gaussian Frobenius、角色与单位因子

取一个非零生成元 $P_*$，用
$P_a=[a]P_*$、$a\in(\mathbb Z[i]/\beta)^\times\simeq\mathbb F_{17}^\times$
编号。对任一非平凡角色 $\chi$ 定义
$$
L_\chi(c)=\sum_a\chi(a)\log_p c_{P_a},\qquad
L_\chi(r_\pi)=\sum_a\chi(a)\log_p r_\pi(P_a).
$$
由 (32) 的置换求和，
$$
\boxed{
17L_\chi(r_\pi)
=(p-\chi(\pi)^{-1})L_\chi(c).
}
\tag{34}
$$
由于 $\chi(\pi)$ 是阶整除 $16$ 的根单位，
$$
p-\chi(\pi)^{-1}\in\mathcal O^\times.
\tag{35}
$$
所以这个因子不会在任何允许的普通 $p$ 产生新的共振。

$r_\beta(iz)=r_\beta(z)$ 给
$$
c_{iP}=i^{-1}c_P,\qquad \log_pc_{iP}=\log_pc_P.
$$
故 $\chi(i)\ne1$ 时两边角色和均为零。
可能非零的只有 $\mathbb F_{17}^\times/\mu_4$ 的四个角色；
它们的值在 $\mathbb Q(i)$，普通 $p$ 的 Frobenius 固定这些角色值。
平凡角色也有准确公式：
$$
17\sum_a\log_pr_\pi(P_a)
=(p-1)\left(\sum_a\log_pc_{P_a}-16\log_p\beta\right).
\tag{36}
$$

这里的 arithmetic Frobenius 在剩余域上为 $x\mapsto x^p$。
在原 $\beta$ 挠点域中，它准确作用为 $P\mapsto[\pi]P$，
因为 $[\pi]$ 是 $E_0$ 的实际 Frobenius，且 $\beta$ 挠点在该素位 étale。
从而 $\sigma_{\mathfrak p}(c_P)=c_{[\pi]P}$。
对一般十六阶角色若同时作用其系数，必须把 $\chi$ 改成 $\chi^p$；
(34) 本身只作点的置换，并未偷偷假设所有十六阶角色值都被固定。

(34) 不自行证明某个 $L_\chi(c)$ 非零；它证明实际除法值的相应角色分量
与一个固定代数数对数分量相差明确单位。

## 6. 原有限系数到底读到了哪些十七挠点信息

把 (29) 的变量改记为 $v$，令
$$
\mathcal B_p=\mathcal O[v]/(K_\beta(v)).
$$
它在当前素位是四维有限 étale 代数。设 $\sigma_\pi$ 为
$v=x(P)^2\mapsto x([\pi]P)^2$ 的置换自同构。
这个自同构完全由 $\pi\bmod\beta$ 确定；例如乘三的实际生成元为 R248 的
$$
g(v)=\frac{(1+4i)v^3-(20+12i)v^2+(-11+28i)v+14-20i}{4},
\qquad g^4(v)=v\quad\bmod K_\beta.
\tag{37}
$$

定义固定单位
$$
D(v)=256v^3(v-1)^2K_\beta'(v)^4\in\mathcal B_p^\times.
\tag{38}
$$
由 (30) 的椭圆方程，$D(x(P)^2)=c_P^4$。因此
$$
\ell_\beta=\tfrac14\log_pD\in\mathcal B_p
$$
在每个四元轨道取值 $\log_pc_P$。

另一方面，(12) 保证
$$
L_p(v)=\frac1p\log R(v)\in\mathcal O\langle v\rangle,\qquad L_p(0)=0.
\tag{39}
$$
这是整个闭单位圆盘上的 restricted series，不只是原点形式记号。
对首系数为单位的 $K_\beta$ 作收敛的单项式除法，唯一得到
$$
\boxed{
L_p(v)=I_p(v)+K_\beta(v)Q_p(v),\qquad
\deg I_p<4,\quad Q_p\in\mathcal O\langle v\rangle.
}
\tag{40}
$$
由 (32)，其四维余式是明确的
$$
\boxed{
17p\, I_p
=(p-\sigma_\pi)\ell_\beta+(1-p)\log_p\beta
\quad\text{于 }\mathcal B_p.
}
\tag{41}
$$
右边除以 $17p$ 后仍整，因为左边来自 (39) 的原除法值。

公式 (41) 给出了真实、固定十七挠值的全部四维投影；
对非平凡四次角色，它就是 (34)，且 (35) 保证没有隐藏的 $p$ 因子。
有限精度计算也完全明确：例如模 $p^k$、$1\le k\le4$，
$$
L_p(v)\equiv
\frac1p\sum_{a=1}^{k}\frac{(-1)^{a+1}}a(R(v)-1)^a
\pmod{p^k\mathcal O\langle v\rangle}.
\tag{42}
$$
这里 $p\ge13$ 保证被省略的全部对数尾项达到该界，所需最高多项式次数为 $kr$。

然而原有限权系数 (16) 是
$$
\boxed{
B_{i,j}
=[v^{jr}]\,a_i(v)R(v)^{n_j+1}E(v)^{-n_j-1}
 \exp_{\le3r}\!\bigl(-c_i[I_p(v)+K_\beta(v)Q_p(v)]\bigr).
}
\tag{43}
$$
指数在原点的常数确为零；不得分别对可能非零的两个常数作无收敛保证的 $p$-adic 指数。
式 (43) 和 (41) 是原前三权与固定挠点投影的准确连接：
它同时保留 reciprocal $E$、共同 charge、以及未被四维余式控制的 $Q_p$。

这个商项确实被原首权读到。对三个原源的实际首权有限线性泛函
$$
\Lambda_i(h)
=[v^r]\,a_i(v)R(v)^{p-68/p}E(v)^{-p}h(v)
\qquad(i=A,B,H)
$$
有
$$
\boxed{
\Lambda_i(v^{r-1}K_\beta(v))=K_\beta(0)=-i.
}
\tag{44}
$$
证明只需 $a_i(v)=v+\cdots$，其余因子常数均为一。
该输入在 $\mathcal B_p$ 中为零，且原点常数为零，
但 (44) 是单位。因此原首权泛函**不经由**
$\mathcal O[v]\to\mathcal B_p$ 因子化。

(44) 是对原有限系数泛函的严格结论，不是假造一个满足全部 CM division 条件的
任意 $R$ 变形。它准确说明：从 (41) 返回 (28) 时，必须控制
$K_\beta Q_p$ 的实际贡献；仅知道四个固定挠值对数，不能将它删掉。

这些角色投影也不是 R263 的 $p$ 个加性余类。
后者由 $\mathbb Z_p$ 的 $a+p\mathbb Z_p$ 或原正式群的 $p$ 核抽取定义，
而 (41) 是固定 $\beta$ 核的乘性角色投影。
把两者比较须使用原 theta 平移及迹的完整 frame；R248/R265 支付的是来源恒等式，
并未给未经证明的完整 Mellin 等变性。

## 7. 接回 R268 时的实际正权乘子

最后明确和 R268 的 de Rham 方向相接所需的原乘子。沿用
$$
W=-y\vartheta\sigma^{67},\qquad
F=S_8^{17}=W\,U^8(U-1)^8,
$$
以及 R264 的水平多项式 $P_8$。
对 $Q\in\mathbb Q[U]_{\le16}$，R268 给
$$
\eta_Q=
\frac{4P_8(U)(U-1)Q(U)}{xU^8}\,dz
=d\mathcal R_Q+\lambda\ell(Q)x\,dz,
\tag{45}
$$
其中 $\mathcal R_Q=yR_Q(x)$、
$\lambda=2^{34}/644658718275$。

要恢复**正权原来源** $WQ\,dz$，准确乘子是
$$
\boxed{
G_+=\frac{Fx}{4P_8(U)(U-1)^9},\qquad
G_+\eta_Q=WQ\,dz.
}
\tag{46}
$$
相邻来源 $(W/x)Q$ 才使用少一个 $x$ 的 $G_-=F/[4P_8(U)(U-1)^9]$。
因此，若 $a=1/[4P_8(U)(U-1)^9]$、$\nabla_F=\partial-F'/F$，准确有
$$
\boxed{
WQ=\nabla_F(Fxa\,\mathcal R_Q)
       -F(xa)'\mathcal R_Q
       +\lambda\ell(Q)Fx^2a.
}
\tag{47}
$$
所有 $P_8$ 零点处的 apparent poles 必须在整式 (47) 中聚合；
不能分别删除它们，也不能把水平 $P_8/(U-1)^8$ 自动命名为秩零参考。

在模 $p$ 的实际 Cartier 比较中，R266(39) 对这个同一 $G_+$ 给出的连接项仍是
$$
-\mathcal C(\mathcal R_{Q,\bar\pi}\,dw),
\qquad
w=r_{\bar\pi}^{\,N}(f\circ[\bar\pi])
\quad(G_+=\sigma^N f).
$$
若所用 frame 需共同 $[2]$ 拉回，先作该真实拉回，按同一公式处理。
普通情形裸 $\mathcal C(x\,dz)=0$ 不会使带 $w$ 的项自动消失。
式 (43) 中 reciprocal、$K_\beta Q_p$ 和 (28) 中 tame $-4$ carry，
均属于返回原来源时需要保留的实际数据。

本篇没有对 Gross–Koblitz 或任何有限挠点插值式作未经证明的权导数。
目前新增的可用条件是 (28)、(41)、(43) 的同时成立；
所缺输入是原三源对 $Q_p$ 贡献或等价完整连接行的进一步约束。

