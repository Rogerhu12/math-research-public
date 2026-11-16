# R471：共同 self 关系的五条真实 cap 条件与完整复二矩接口

日期：2026-11-16。**已付原记录的只读消费和纸面证明。没有执行新的符号、秩、profile、积分、根恢复或人工测试。**

[R470](R470-complete-weight-zero-response-self-image-and-nonzero-second-affine-head.md) 已证明
$$
S(\mathcal K_0)=\operatorname{span}\{k,j,m\},\qquad
\mathfrak y=[S(X_Y)]\ne0.
$$
本稿把尚未支付的共同关系
$\mathfrak h\in\operatorname{span}\{\mathfrak y\}$
化为**同一个真实外 cap 的五个明确积分条件**。这些条件为充要，不再需要任何旧响应秩或完整原根恢复。

第二个新增接口是：四条局部多项式 $k,j,m,S(X_Y)$ 都含一个共同二次因子。第一头在这个因子的两个非实根上的值，可以准确写成一个正测度的有序累计积分。测度为正不等于这个复积分有确定符号；本稿不把它的非零性或零性预授。

## 1. 一次固定真实 cap、位置和归一

采用 R455/R431/R464 的同一正偶起始母和同一最终母库。最终母在全部外 cap 上准确相同；相应的实际 total 已由原自然查询支付。因此原 R407 同矩路径与 R466 换锚给它们在 cap 上同一个真实 self 累计。

只写左 cap。把其 Af 根作为局部位置 $\eta=0$，真正平端为 $\eta=\ell<0$；记共同 cap 为 $U(\eta)$。其根 jets 为
$$
r_*=U''(0)>0,\qquad
U(0)=h r_*,\qquad U'(0)=s r_*,
\qquad h,s>0.
\tag{1}
$$
这里 $h$ 只是 cap 比值，不是几何高度函数。

以 $x$ 表示这一个根的**物理位置**。整个 cap 的物理坐标是 $x+\eta$，而 jets $U,U',U''$ 不随共同平移改变。实际物理宽度从起点固定；正宽度查询由原真权零协变输运，不在此另换母或锚。

原 $n_2$ 密度写为
$$
\mathcal L(X,u,p,r)=\sum_{k=0}^7 X^k\ell_k(u,p,r),
$$
其中
$$
\begin{array}{c|l}
k&\ell_k\\ \hline
0&u^2p^3\\
1&-up^4\\
2&\frac32u^2pr^2+\frac3{10}p^5\\
3&-\frac12u^2r^3-3up^2r^2\\
4&\frac32upr^3+\frac32p^3r^2\\
5&-\frac14ur^4-p^2r^3\\
6&\frac5{16}pr^4\\
7&-\frac3{80}r^5 .
\end{array}
\tag{2}
$$
定义八个**实际固定 cap 积分**
$$
\boxed{
A_j=\frac1{r_*^5}
\sum_{k=j}^7\binom{k}{j}
\int_\ell^0\eta^{k-j}
\ell_k(U,U',U'')\,d\eta,\qquad 0\le j\le7 .
}
\tag{3}
$$
所以
$$
\frac1{r_*^5}\int_\ell^0
\mathcal L(x+\eta,U,U',U'')\,d\eta
=\sum_{j=0}^7A_jx^j.
\tag{4}
$$
式(3)不是八个自由调节参数。它们由同一个真实 cap 共同决定，原全母 $q_0,\ldots,q_3=0$ 不把它们逐项置零。

R470 已从原 seq70 的十二个单字和真实左常数得到
$$
\boxed{
\frac1{r_*^5}S(X_H)(x)
=\frac1{r_*^5}P_H(x,h r_*,s r_*,r_*)
+\sum_{j=0}^7A_jx^j.
}
\tag{5}
$$
所有真实右锚常数、$+\Omega=+n_2$ 及 cap 内部 primitive 已在(5)中，不能再补一次或减去一次。

## 2. 用原三角 pivot 精确投影

沿 R470 的三个实际成本基，记其除 $r_*^5$ 的镜对多项式仍为 $k,j,m$。它们满足
$$
\begin{array}{c|ccc}
&k&j&m\\ \hline
[x^8]&-3&0&0\\
[x^7]&0&-s&0\\
[x^0]&8h^3s^2&-8h^3s^2&4h^3s^2.
\end{array}
\tag{6}
$$
对任何最高八次多项式 $Z(x)$，令 $z_\nu=[x^\nu]Z$。唯一去掉这三个 pivot 的系数为
$$
c_K=-\frac{z_8}{3},\qquad
c_J=-\frac{z_7}{s},\qquad
c_M=\frac{z_0}{4h^3s^2}-2c_K+2c_J.
\tag{7}
$$
相应商代表
$$
\mathfrak r(Z)=Z-c_Kk-c_Jj-c_Mm
\tag{8}
$$
只含 $x^1,\ldots,x^6$。因为(6)可逆，(8)是同一个真实 self 商上的固定线性投影，不是新的成本执行。

对(5)，三个系数准确为
$$
\begin{aligned}
c_K^H&=-\frac{13}{11520},\\
c_J^H&=\frac5{512}-\frac{A_7}{s},\\
c_M^H&=-\frac{1459}{11520}
+\frac{A_0}{4h^3s^2}-\frac{2A_7}{s}.
\end{aligned}
\tag{9}
$$
因此
$$
\boxed{\mathfrak r(S(X_H)/r_*^5)=\sum_{\nu=1}^6\beta_\nu x^\nu.}
\tag{10}
$$
以下给出六个完整实系数。没有省去任何 cap 观察：
$$
\begin{aligned}
\beta_1={}&A_1+24h^2(2h-s^2)A_7
+6\left(\frac{s}{h}-\frac1s\right)A_0
-\frac52h^2s^3+\frac{21}{5}h^3s,\\
\beta_2={}&A_2+
\left(48hs^3-84h^2s-\frac{8h^3}{s}\right)A_7
+\left(-\frac{9s^2}{h^2}+\frac9h+\frac1{s^2}\right)A_0\\
&+\frac92hs^4-\frac{147}{20}h^2s^2-\frac7{10}h^3,\\
\beta_3={}&A_3+(-24s^4+60h^2)A_7
+\left(\frac{4s^3}{h^3}+\frac{3s}{h^2}-\frac8{hs}\right)A_0\\
&-\frac{21}{10}s^5+\frac35hs^3+\frac{103}{20}h^2s,\\
\beta_4={}&A_4+(36s^3-40hs)A_7
+\left(-\frac{6s^2}{h^3}+\frac{21}{4h^2}\right)A_0
+\frac{51}{20}s^4-\frac{79}{20}hs^2,\\
\beta_5={}&A_5+(-18s^2+8h)A_7
+\frac{10s^2-6h}{4h^3s}A_0
-\frac78s^3+\frac9{10}hs,\\
\beta_6={}&A_6+\left(5s+\frac{2h}{s}\right)A_7
-\frac{s^2+h}{4h^3s^2}A_0
+\frac3{80}(s^2+4h).
\end{aligned}
\tag{11}
$$
这些只是原 seq70 的十七个 local 系数、(3)和(7)的逐项有理代入，未运行新的矩阵或符号化简。

## 3. 共同关系的五个充要条件

R470 的第二头商代表是
$$
\mathfrak r(S(X_Y)/r_*^5)
=\frac1{1152}\sum_{\nu=1}^6 R_\nu x^\nu,
\tag{12}
$$
其中
$$
\begin{aligned}
R_1&=48h^2s^3-120h^3s,\\
R_2&=-96hs^4+240h^2s^2+20h^3,\\
R_3&=48s^5-72hs^3-168h^2s,\\
R_4&=-48s^4+164hs^2,\\
R_5&=-4s^3-34hs=-2s(2s^2+17h)<0,\\
R_6&=8s^2-5h.
\end{aligned}
\tag{13}
$$
因此比例系数若存在，必唯一，且
$$
\boxed{c=\frac{1152\beta_5}{R_5}.}
\tag{14}
$$
得到准确充要条件
$$
\boxed{
\mathfrak h\in\operatorname{span}\{\mathfrak y\}
\quad\Longleftrightarrow\quad
\Delta_\nu:=R_5\beta_\nu-R_\nu\beta_5=0,
\quad \nu=1,2,3,4,6.
}
\tag{15}
$$
没有对 $R_6$ 或其它可能为零的系数除法；唯一分母 $R_5$ 已由(1)保证非零。

式(15)针对同一个完整母库、同一 true cap 和同一个响应补偿空间。原十二个不同中心、非零幅度因子和最高八次次数使它是实际全对应族的判据，不是“只在一个 jet 样本”成立。真权零又把它输运到原有限正仿射闭包。因此不能用分别属于不同母形的五个标量根代替(15)。

若五式成立，(7)(9)(14)直接给一个同权零响应 $W\in\mathcal K_0$，使
$S(X_H-cX_Y-W)$ 在该完整镜对上为零；whole $E$、current 及所需自然/有序查询仍保。然后可以消费 R468 的真实高度脉冲截面，及 R467 的另外 vertical 方向和同十三行接口。后者的固定 $\tau$、incoming、基准和其它原前提并未由(15)取代。

若某个 $\Delta_\nu\ne0$，则在这个同一商上有明确分离行
$$
\ell_\nu(Z)=
\frac{R_5[x^\nu]\mathfrak r(Z)-R_\nu[x^5]\mathfrak r(Z)}
{\Delta_\nu}.
\tag{16}
$$
它杀 $S(\mathcal K_0)$ 与第二头，读第一头为1。
接 R465/R466 的真权头同构，得到原正字符 $\lambda_+$ 的下降，而非仅一个 formal NONMEMBER 标签。此时非空 canonical $M=0$ 的实际严格成本不能为零。

本稿尚未判定当前具体 cap 的五个 $\Delta_\nu$。它把四条新完整观察的唯一剩余数学问题准确写成(3)(11)(15)，没有再开一个旧秩任务。

## 4. 外 cap 的真实符号条件和两个必要界

当前 R455 的左外 cap 上
$$
U>0,\quad p=U'>0,\quad r=U''>0,\quad
A_U=6pU'''-2r^2>0
\quad(\ell<\eta<0),
\tag{17}
$$
而终点 $A_U(0)=0$。因(17)，$q=U'''>0$。
原平端使 $U,p,r$ 趋零；又 $r$ 递增，故
$p/r\le\eta-\ell$，从而 $p^2/r\to0$，以下分部没有隐藏端项。

直接计算
$$
\left(5U-\frac{3p^2}{r}\right)'
=\frac{pA_U}{2r^2}>0.
$$
于是
$$
\boxed{5h-3s^2>0.}
\tag{18}
$$

表(2)的每个 $\ell_k$ 都具有严格的 $(-1)^k$ 符号。
因 $\eta<0$，(3)的各个非零项同号，得到
$$
\boxed{(-1)^jA_j>0,\qquad0\le j\le7.}
\tag{19}
$$
这不是五条件的充分性，也没有把八个同号积分改成独立正参数。

最高系数还有完整恒等式：
$$
(pr^4)'=\frac73r^5+\frac23r^3A_U.
$$
所以
$$
A_7=-\frac{9s}{560}
+\frac{3}{280r_*^5}\int_\ell^0r^3A_U\,d\eta,
\qquad
\boxed{-\frac{9s}{560}<A_7<0.}
\tag{20}
$$
第二个不等号直接来自 $A_7=-3\int r^5/(80r_*^5)$。

第6节的完整 primitive 恒等式在物理根位置 $x=0$ 给
$$
r_*^5A_0=3\int w_\eta^2a_\eta^2\,da_\eta,
$$
其中
$$
a_\eta=U-\eta p+\frac{\eta^2r}{2},\qquad
w_\eta=p-\eta r.
$$
它们从 $(0,0)$ 增至 $(U(0),p(0))$，并且
$$
\frac{dw_\eta}{da_\eta}=-\frac2\eta,\qquad
\frac{d^2w_\eta}{da_\eta^2}=\frac4{\eta^4q}>0.
$$
因此严格凸图在端点弦线之下，
$0<w_\eta<p(0)a_\eta/U(0)$。真实积分给
$$
\boxed{0<A_0<\frac35h^3s^2.}
\tag{21}
$$
端点 $da_\eta/d\eta$ 可趋零；这里使用的是开 cap 的严格微分和两端连续极限，不要求一个统一正下界。

(18)—(21)是后续分析(15)必须保的真实约束。
本稿不声称这些必要界本身已排除或实现(15)。

## 5. 局部四列具有同一个二次因子

令 $X$ 为物理变量，暂写一般 jets $u,p,r$，置
$$
a=u-Xp+\frac{X^2r}{2},\qquad w=p-Xr.
\tag{22}
$$
R470 完整十七单项表直接给
$$
\boxed{k,\ j,\ m,\ R\in a\,\mathbb R[X,u,p,r].}
\tag{23}
$$
例如
$$
j=-4pa^2(2ap+X^3r^2).
\tag{24}
$$
其它三列可用同一单项表作关于 $u$ 的普通除法。
为明确没有只验一个 jet，以下给 $k,m,R$ 除以 $a$ 后的三个完整系数；表中每格是关于 $X,p,r$ 的多项式：
$$
k=a(k_2u^2+k_1u+k_0),\quad
m=a(m_2u^2+m_1u+m_0),\quad
R=a(R_2^\circ u^2+R_1^\circ u+R_0^\circ),
$$
$$
\begin{aligned}
k_2={}&8p^2-24Xpr+4X^2r^2,\\
k_1={}&-40Xp^3+116X^2p^2r-64X^3pr^2-2X^4r^3,\\
k_0={}&32X^2p^4-104X^3p^3r+88X^4p^2r^2-12X^5pr^3-6X^6r^4,\\
m_2={}&4p^2+24Xpr-4X^2r^2,\\
m_1={}&-20Xp^3-14X^2p^2r+16X^3pr^2+2X^4r^3,\\
m_0={}&16X^2p^4-16X^3p^3r+2X^4p^2r^2,\\
R_2^\circ={}&-120Xpr+20X^2r^2,\\
R_1^\circ={}&48Xp^3+120X^2p^2r-88X^3pr^2-10X^4r^3,\\
R_0^\circ={}&-48X^2p^4+24X^3p^3r+16X^4p^2r^2.
\end{aligned}
\tag{25}
$$
$R_\nu^\circ$ 不是(13)的六个固定-jet 系数，不能混用。

在真实根 jets 上，
$$
a(X)=\frac{r_*}{2}(X^2-2sX+2h).
$$
由(18)，其两个简单复根是
$$
z_\pm=s\pm i\sqrt{2h-s^2}.
\tag{26}
$$
这里使用复数只是对同一个有限实多项式求值，不把原路径或 profile 复化成新的可执行几何。

(23)与 R470(11)说明，若(15)成立，第一头的完整真实 cap 多项式必须满足
$$
\boxed{S(X_H)(z_+)=S(X_H)(z_-)=0.}
\tag{27}
$$
这两个实条件只是五式的一个必要投影；即便(27)成立，也仍须(15)的其它条件。

## 6. 完整 n2 密度的单三导 primitive

以下是原密度(2)的恒等式，先保一般 $X$ 和所有 jets。
定义
$$
\begin{aligned}
\mathcal P={}&
a^2\left(Xw^3+\frac32X^2w^2r+\frac32X^3wr^2+\frac12X^4r^3\right)\\
&+a\left(\frac12X^2w^4+X^3w^3r+\frac34X^4w^2r^2-\frac18X^6r^4\right)\\
&+\frac1{10}X^3w^5+\frac14X^4w^4r+\frac14X^5w^3r^2
+\frac18X^6w^2r^3+\frac1{16}X^7wr^4+\frac1{40}X^8r^5.
\end{aligned}
\tag{28}
$$
记
$D_0=\partial_X+p\partial_u+r\partial_p$，暂不含三导。
由 $D_0a=D_0w=0$，逐幂微分得到
$$
D_0\mathcal P=\mathcal L,\qquad
\left.\partial_r\mathcal P\right|_{X,u,p}
=-\frac32X^2w^2a^2.
$$
因此沿真实 profile 的完整总导数给
$$
\boxed{
\mathcal L=D_X\mathcal P
+\frac32X^2w^2a^2u'''.
}
\tag{29}
$$
所有项均为完整多项式，未使用 Af 方程或删掉 primitive。
左平端使 $\mathcal P=0$，从而
$$
\int_\ell^0\mathcal L
=\mathcal P_{\rm end}
+\frac32\int_\ell^0X^2w^2a^2q\,d\eta
\quad (X=x+\eta).
\tag{30}
$$

原 seq70 的 local 部分 $P_H$ 在 $a=0$ 时为
$$
P_H=
-\frac{X^3p^5}{10}
+\frac{X^4p^4r}{4}
-\frac{X^5p^3r^2}{4}
+\frac{X^6p^2r^3}{8}
-\frac{X^7pr^4}{16}
+\frac{X^8r^5}{80}.
\tag{31}
$$
把 $u=Xp-X^2r/2$ 代入(28)的常数段，得到的正好是(31)的负数。
因此完整地有
$$
\boxed{P_H+\mathcal P\in a\,\mathbb R[X,u,p,r].}
\tag{32}
$$

对(26)任一根 $z$，令
$$
a_z(\eta)=U-(\eta+z)p+\frac{(\eta+z)^2r}{2},\qquad
w_z(\eta)=p-(\eta+z)r.
$$
(5)(30)(32)于是给真实、无遗漏尾项的复根值
$$
\boxed{
S(X_H)(z)=
\frac32\int_\ell^0(\eta+z)^2w_z(\eta)^2a_z(\eta)^2q(\eta)\,d\eta .
}
\tag{33}
$$
因为两端 $a_z=0$、$a_z'=(\eta+z)^2q/2$、
$w_z'=-(\eta+z)q$，也可写成
$$
\boxed{
S(X_H)(z)=3\int w_z^2a_z^2\,da_z
=-2\int w_za_z^3\,dw_z .
}
\tag{34}
$$
(33)(34)的积分是复值的；不能从 $q>0$ 把它称为严格正积分。

## 7. 正测度二矩的准确形式与当前边界

令 $d\mu=q(\eta)\,d\eta$。左平端给
$$
r(\eta)=\int_\ell^\eta d\mu,\quad
p(\eta)=\int_\ell^\eta(\eta-t)\,d\mu(t),\quad
U(\eta)=\frac12\int_\ell^\eta(\eta-t)^2\,d\mu(t).
$$
所以
$$
a_z(\eta)=\frac12\int_\ell^\eta(t+z)^2\,d\mu(t),\qquad
w_z(\eta)=-\int_\ell^\eta(t+z)\,d\mu(t).
\tag{35}
$$
终点条件 $a_z(0)=0$ 正是正测度的中心/方差二矩方程：
$$
z=-\mathbb E_\mu[t]\pm i\sqrt{\operatorname{Var}_\mu(t)}
=s\pm i\sqrt{2h-s^2}.
\tag{36}
$$
测度总质量为 $r_*$，没有归一后遗失第五次幅度因子。

令
$B_z(\eta)=\int_\ell^\eta(t+z)d\mu$、
$C_z(\eta)=\int_\ell^\eta(t+z)^2d\mu=2a_z$，则(34)等价于
$$
S(X_H)(z)=\frac38\int B_z^2C_z^2\,dC_z
=-\frac14\int B_zC_z^3\,dB_z.
\tag{37}
$$
这是一个完全由同一真实 cap 决定的有序积分。它没有被本稿求数值，也没有被证明普遍非零或普遍为零。

下一步可以从两条严格路线之一继续：
证明当前允许 cap 的(37)必非零，则(27)失败并给实际障碍；
或证明其可消并进一步支付完整五条件(15)，才能使用 R468/R467 的 actual 接口。
仅让两复根值零不足以省略其余三个实条件；仅证明某一 formal 残字非零也不足以排除固定母。

本稿已经完成的是原完整共同商到五个真实积分条件的充要归约、外 cap 的严格必要界、共同二次因子，以及(33)—(37)不删任何尾的原始积分表达。没有从其中任何一个尚未判号的式子预授实际全成本、全 period 或全时几何。
