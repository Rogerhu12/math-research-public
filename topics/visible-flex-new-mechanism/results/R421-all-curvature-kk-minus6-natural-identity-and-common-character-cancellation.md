# R421：完整 kk 负六权的全曲率身份与最后一个负六字符的消去

日期：2026-11-16。**完整原式纸面证明；没有执行新的 profile、积分、符号程序、秩、人工测试或科学运行。**

令
$$
V_{kk,-6}(k)=[h^{-6}(\log h)^0]\widehat Q_{kk}(h,k,0)\in U,
\qquad S=1+k^2.
$$
这里仍是物理 $k_s^2$ 的完整正规系数：先取原全部历史导数，再按 R129 作水平加速度分部积分，最后设 $\omega=0$。

本文证明
$$
\boxed{
\Lambda_u(V_{kk,-6}(k))
=\frac{(1+k^2)^2}{640}
\int\{5u'(u'')^4-3x(u'')^5\}.
}
\tag{1}
$$
此式对每个真实紧光滑 $u$ 及所有 $k$ 成立。不是将 R418 的 $k=0$ 答案猜测乘一个因子：一般 $k$ 新增的原 $N_0$ 势响应、真正水平导数及完整有序尾均在下文支付。

由 R412/R414 当前共同偶母的 $M_5=0$，(1)在同一个最小共同自然查询上恒为零。结合 R416、R419，原权 $-6$ 正字符最后的 $b_0(k)\ge0$ 也被迫全零。**这只消去该共同增强商的权 $-6$ 正字符；权 $-4$ 的速度矩阵和完整实际 joint 仍须继续。**

来源：R56、R73、R109、R129、R130、R367、R386、R393、R402、R412、R413、R414、R416、[R417](R417-two-term-static-minus4-natural-image-and-one-remaining-anchor.md)、[R418](R418-complete-kk-minus-six-natural-coefficient-and-common-query-cancellation.md)、[R419](R419-all-curvature-hh-minus6-natural-cancellation-and-PSD-reduction.md)。R367 仅用其独立成立的原势、Green 及有序公式；不使用已撤回的旧 H 非零断言。

## 1. 同锚原函数、水平导数与中心导数

固定一个共同右零 collar，始终取
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
二、三次输出的真实左尾不设为零。记
$$
p=u',\quad r=u'',\quad t=u''',\quad
P=J(r^2),\quad M=J(xr^2),\quad C=J(x^2r^2+2p^2),
$$
$$
R=p^2+xP,\quad T=x^2p^2+xC,\quad
L=p-xr,\quad G=u-xp/2,\quad
H=x^2r-2xp+2u.
\tag{2}
$$
$H$ 在本稿是这个局部 jet，不是第三 hook。以下 $\mathsf H=x\partial_x-1$ 才表示原 $\mathfrak{sl}_2$ 算子。

在 $h_s=0$ 的真实切片写 $w=k_s,\beta=k_{ss}$。保持
$$
Y=\partial_k+\frac1{2h}\partial_\omega
=\partial_k-\frac12\partial_d,\qquad d=h\omega-k.
\tag{3}
$$
任何一次 $Y$ 都在限制 $\omega=0$ 之前作用。

一个方便而严格的标量版本如下。令 $\mathscr A(h,k,\omega;u)$ 是下文任一完整收缩，原式中的几何坐标为 $z=x+\omega,e=hz-k$。作 $y=x+\omega$ 后，右端同时变成 $r_*+\omega$，输入变成 $u(y-\omega)$。由于原右 collar 恒零，仍是同一个实际右积分，而不是改用左锚。于是
$$
Y\mathscr A\big|_{\omega=0}
=\partial_k\mathscr A(h,k,0;u)
+\frac1{2h}\,\partial_{\rm c}\mathscr A(h,k,0;u),
\tag{4}
$$
$\partial_{\rm c}$ 表示把整个 profile 平移后的真实中心导数，原 primitive 与其左常数一起输运。

特别
$$
[h^{-6}]Y\mathscr A
=\partial_k\mathscr A_{-6}
+\frac12\partial_{\rm c}\mathscr A_{-5}.
\tag{5}
$$
(4)只用于这些完整标量，不从任意瞬时局部分量推同样的简写。等价地，所有计算可以直接用(3)。例如
$$
YG_z=-p/(4h),\qquad YL_z=-r/(2h),
$$
仍是 R418 已保留的两个不同因子。

## 2. 全曲率下新增的原势不能删

写原八算子
$$
\mathbf P=r_0,\quad\mathbf R=r_1,\quad\mathbf S=s_0,\quad
\mathbf L=p_0,\quad\mathbf U=s_1,\quad
\mathbf V=p_1,\quad\mathbf T=t_1,\quad\mathbf Y=p_2,
$$
并令
$$
\mathbf E=-\mathbf L/2+\mathbf U/4,\quad
E=\mathbf E(u,u),\quad V=\mathbf V(u,u).
$$
原 R73 给
$$
q_0=-\frac{S^2R}{8h^2}+\frac{kSE}{h}
+k^2V-\frac{ST}{8}-\frac{kh}{2}\mathbf Y(u,u),
$$
$$
q_2=m_{2,kk}(u,u)=\frac{kP}{16h^3}-\frac M{16h^2}.
\tag{6}
$$
其中
$$
E=-\frac{up}{2}+\frac{xp^2}{2}+\frac{x^2P}{8}+\frac{xM}{4},
\quad
V=-\frac{u^2}{2}+xup-\frac{x^2p^2}{2}-\frac{x^2M}{4}.
$$

R417 的完整 outer 势为
$$
[N_0]_{h^{-4}}=0,\qquad [N_0]_{h^{-3}}=kS^2\tau_3.
$$
因此
$$
[h^{-6}](-\mathcal B_{m_2}N_0)
=-\frac{k^2S^2}{16}\mathcal B_{\mathbf P}\tau_3.
\tag{7}
$$
$-\mathbf S/(16h^2)$ 所需的 $N_0,h^{-4}$ 槽为零；原参考势没有本次负幂。$\Gamma(m_2)$ 最高只需 $h^{-3}$，不贡献(7)。

下一节证明的是这个新增项的**完整自然函数为零**，不是宣称 $\tau_3$ 属于旧可调第三空间。

## 3. 原全 outer 势的独立完整自然零式

R417 用 $\tau_3=-\mathcal T_3/3$ 定义这个势。将其原六个 Volterra 映射逐一代入，并只作同右锚分部积分，得到不含 $1/x$ 的完整式
$$
\boxed{
64\mathcal T_3(f;u^2)
=f'B_u+2fR'
-2xJ(f''Ht)-2x^2J(f''Lt),
}
\tag{8}
$$
$$
B_u=-4ur-2xP+2M+x^2r^2.
$$
这里 $f$ 是独立 outer，可带真实二次左尾。比如原式中的
$J(f'''R)=-f''R-J(f''R')$ 与
$J(xf'''R')=-xf''R'-J(f''R')-J(xf''R'')$
保留了所有局部边项；正是这些项合成(8)。没有从 diagonal 身份反推全槽。

为核对 natural，暂记
$$
A_5=\int Pr^3,\quad B_5=\int pr^4,\quad C_5=\int xr^5,
\quad T_5=\mu_0M_3,\quad M_3=\int r^3.
$$
置
$$
T_\tau=\tau_3(u;u^2),\quad
s_o=\int t\,\tau_3(P;u^2),\quad
s_i=\int t\,\tau_3(u;u,P),\quad
i_\tau=\int r^2 T_\tau''.
$$
从(8)得到完整三行
$$
\boxed{
s_o=-\frac{B_5+2A_5-4C_5/15}{192},\quad
s_i=s_o+\frac{T_5}{144},\quad
i_\tau=-s_o-\frac{T_5}{288}.
}
\tag{9}
$$

列出可直接复核的中间式。由(8)，
$$
64\mathcal T_3(u;u^2)
=2(u-xp)P+2pM-\frac{2x}{3}J(xr^3)+\frac{x^2}{3}J(r^3).
\tag{10}
$$
代 $f=P$ 后，两份三阶平方原函数在收缩中准确抵消，因为
$$
\int xtJ(F)=-\int LF,\qquad
\int x^2tJ(F)=\int HF.
$$
所余是
$$
\int t\{4ur^3-2Mr^2-x^2r^4+4Ppr+2P^2\}
=B_5+2A_5-4C_5/15.
$$
对(10)求二导并乘 $r^2$，完整结果为
$-2A_5-B_5+4C_5/15+2T_5/3$。
对 inner $(u,P)$ 作真实对称极化，三阶平方及 $t'$ 项同样成对消去，所得为
$B_5+2A_5-4C_5/15-4T_5/3$。
乘 $\tau_3=-\mathcal T_3/3$ 的规范，即(9)。

原正式 pure 的完整变分给
$$
8\int t\,\pi(\mathcal B_{\mathbf P}\tau_3)
=s_o+2s_i-2i_\tau,
\qquad
\Omega_u(\mathcal B_{\mathbf P}\tau_3)=2s_o.
$$
所以在还未加入原有序尾时，
$$
\Omega_u-\frac{16}{5}\int t\,\pi
=-\frac{T_5}{120}.
\tag{11}
$$

现在取完全在右方的真实辅助包，矩为 $n$。在整个左域，(8)准确给
$$
\tau_3(f;v^2)=X_nf,\qquad
X_n=\frac{n_0\mathsf H-n_1\partial_x}{96}.
\tag{12}
$$
又有
$$
\tau_3(1;u^2)=-R'/96,\qquad
\tau_3(u;u,1)=(2pr-xr^2)/192.
$$
这里常数 $1$ 只代表实际 $P_v$ 在左域的常尾；没有将一个全局非紧常数作为新的合法 profile。

原 pure 的完整 $2+2$ 展开于是为
$$
\begin{aligned}
8\Gamma^\to
&=X_nP-\frac{n_0R'}{96}
+2n_0\tau_3(u;u,1)-2\mathbf P(u,X_nu)\\
&=-\frac{n_0P}{32}.
\end{aligned}
\tag{13}
$$
此处 $\mathbf P(u,X_nu)=
\{n_0(P-xr^2)+n_1r^2\}/192$。
因此
$$
\int t\,\Gamma^\to=-\frac{n_0M_3}{256}.
$$
按原辅助矩映射最后取 $n=\mu(u)$，自然配方的
$-32/15$ 倍该值为 $+T_5/120$，恰消(11)。证明
$$
\boxed{\widehat\Lambda_u(\mathcal B_{\mathbf P}\tau_3)=0.}
\tag{14}
$$
帽号只表示在这个原势响应上用已经逐项付清的完整 natural 配方；不把它单独冒称 $U$ 的正时间成本。

## 4. 其余原式的严格全曲率结构

R418 的原 $C_Aq_0$ 子项仍是 $-4\int a'a(u,q_0)$。
R367 对任意 $E\in E_8$ 的独立 Green 恒等，加真实有序补偿后，恰等于
$(5/4)\widehat\Lambda(\mathcal B_EN_2)$。所以本稿也先在**完整自然配方**中消去它和 $-\mathcal B_{m_0}N_2$。
静态 $b(u,q_0)$ 链、原 $-\Psi(u,n)$ 和 $ZZ$ 两份 history 不在此消项中。

记 R418 的剩余两个 raw scalar 为 $\mathscr R_Y,\mathscr R_Z$，
加速度 scalar 为 $\mathscr A_Y,\mathscr A_Z$。这些符号指 $YC,ZZ$ 配对；$Y\mathscr A$ 中的 $Y$ 才是(3)。
它们的完整原式仍取 R418(14)–(20)，但先保一般状态，再取 $\omega=0$。

二阶分量及其真实导数是
$$
A=\frac{Sr^2}{32h^3}-\frac{k(xr^2+P)}{16h^2}
+\frac{x^2r^2+2M}{32h},\qquad
A'=\frac{Qrt}{16h^3},
$$
$$
b=\frac{SR}{8h}
+k\left(\frac{up}{2}-\frac{3xp^2}{8}-\frac{xM}{4}\right)
+h\left(\frac{G^2}{2}+\frac T8\right).
\tag{15}
$$
原八矩的水平导数也可直接核为
$$
\begin{aligned}
Ym_0\big|_{\omega=0}={}&-\frac{S^2\mathbf P}{16h^3}
-\frac{kS\mathbf R}{4h^2}+\frac{kS\mathbf S}{8h^2}\\
&-\frac{(1+2k^2)\mathbf L}{2h}
+\frac{(1+3k^2)\mathbf U}{8h}
+\frac{3k\mathbf V}{2}-\frac{k\mathbf T}{8}-\frac h2\mathbf Y .
\end{aligned}
$$
最重要的真实抵消为
$$
YA=\frac{kr^2}{32h^3}-\frac{xr^2+P}{32h^2},
\qquad
\boxed{D_2=YA+q_2'/2=-P/(32h^2).}
\tag{16}
$$
因此 $D_2$ 没有 $k^3r^2h^{-3}$ 一类项。原第三分量准确为
$$
E_2=-\frac{Sr^2}{64h^3}+\frac{kxr^2}{32h^2}
+\frac{2M-2xP-x^2r^2}{64h}.
\tag{17}
$$

由(6)(15)–(17)，原四个 $h^{-6}$ scalar 均有严格形式
$$
S^2\{\mathcal F_0+k^2\mathcal F_1\}.
\tag{18}
$$
这里 $\mathcal F_0$ 是 R418 的原完整锚表，$\mathcal F_1$ 是本稿实际提取的 $k^6$ 系数；两者都是固定 profile 泛函。

给出逐幂来源以限定(18)的范围。原静态第三局部场满足 R417(18)(19)：
$$
[c_0]_{-4}=S^3C_4,\quad [c_0]_{-3}=kS^2C_3,\quad
[c_0]_{-2}=S(C_{20}+k^2C_{21}).
$$
原 $C_b=-J(QtA)/(8h^2)$ 及 $C_v$ 直接代(15)，只给 $S^3$ 与 $k^2S^2$ 两组。
加速度部分的 $h^{-6}$ 系数是 $kS^3$ 乘固定泛函；$h^{-5}$ 系数是 $S^3$、$k^2S^2$、$S^2$ 的线性组合。
用(5)和 $S^2=S^3-k^2S^2$，其正规导数仍恰有(18)。

在 $ZZ$ 中，(16)同时去掉会伪造更高 $k$ 次数的项。
原 metric 的最高相关项可直接写为
$Q(A')^2=Q^3r^2t^2/(256h^6)$，并有
$[h^2]Q^3=3S(S+4k^2)x^2$。
其余 metric、$T_s$、$K_0P/B$ 与 history 项也只有上述两组。
这里(18)是原有限多项式的逐项因子化，不依赖反射、旧 pure 的次数或某个极限。

(7)自身是 $k^2S^2$ 乘完整响应，已由(14)消去。因此整个 natural 也满足
$$
\mathcal N(V_{kk,-6}(k))
=S^2\{\mathcal N(V_{kk,-6}(0))+k^2\mathcal N(W_{kk})\},
\tag{19}
$$
其中 $W_{kk}=[k^6]V_{kk,-6}(k)\in U$。
以下独立计算 $\mathcal N(W_{kk})$，不能从(19)先设它为零。

## 5. 新最高曲率表，含完整 -Yn 与 history

为列出表格，记
$$
\mathsf A=\int Pr^3,\quad\mathsf B=\int pr^4,\quad
\mathsf C=\int xr^5,\quad\mathsf T=\mu_0M_3,
$$
$$
\mathsf K_*=\int(6xH-15x^2L)r^2t^2.
\tag{20}
$$
按原公式提取 $[h^{-6}k^6]$ 后，得到下表。**表中每一行均已乘 30720。**

| 原 scalar | $\mathsf K_*$ | $\mathsf A$ | $\mathsf B$ | $\mathsf C$ | $\mathsf T$ |
|---|---:|---:|---:|---:|---:|
| $\mathscr R_Y$ | $60$ | $-20$ | $-10$ | $4$ | $10$ |
| $\mathscr R_Z$ | $60$ | $-20$ | $-10$ | $4$ | $0$ |
| $Y\mathscr A_Y$ | $0$ | $360$ | $70$ | $50$ | $-180$ |
| $Y\mathscr A_Z$ | $0$ | $360$ | $70$ | $50$ | $0$ |

表(21)。

以下给出这张新表的原函数核对入口。写 $n_1=[k_s]n$，则
$$
[h^{-5}]n_1=-S^3J(r^3)/384,
$$
$$
[h^{-4}]n_1
=\frac{kS^2}{192}
\{xJ(r^3)+2J(xr^3)-3J(pr^2)\}.
\tag{22}
$$
最高所需下一项为
$$
\begin{aligned}
64[h^{-3}k^4]n_1={}&
(xp-u)P-pM+\frac23p^3
+3J(xpr^2)-J(x^2r^3)-J(ur^2)\\
&+2xJ(pr^2)-xJ(xr^3)-\frac{x^2}{3}J(r^3).
\end{aligned}
\tag{23}
$$
这是原 $n=\ell-\Psi(u,q_0)$ 的完整线性速度项；没有漏 $-\Psi$ 的 $P/B$ 来源。原 $C_v$ 的三个最高所需系数则为
$$
[h^{-6}k^4]C_v=-r^2t/256,\qquad
[h^{-5}k^3]C_v=xr^2t/64+r^3/768,
$$
$$
[h^{-4}k^2]C_v=-3x^2r^2t/128-Pr/256-xr^3/256.
$$
它们与 $QA_u/(2h)$ 的原三项共同给第一行中未包含(25)的部分。

对任意真实右零、可带左尾的 $f$，
$$
-\int t\,\Psi_{w=1}(u,f)
=\int\frac{r^2f}{8h}-\int\frac{Qr^2f''}{16h^3}.
\tag{24}
$$
将(22)(23)代入(24)，其 $k^6h^{-6}$ 完整值是
$$
-\mathsf A/1024-\mathsf B/6144-\mathsf C/10240
+\mathsf T/3072.
\tag{25}
$$
这是表(21)第一行中必须保留的低阶部分，不是只检查三阶平方列。

原 $ZZ$ history 仍是 R418 的 $-\int tP_{A,q_0}/h^2$，其中完整原式为
$$
\boxed{
P_{A,q_0}=
\{(Qq_0''-heq_0')A+J(Qq_0'''A)\}/(4h).
}
\tag{26}
$$
紧 outer 的一次真实 Fubini 给
$$
-\frac1{h^2}\int tP_{A,q_0}
=\frac1{4h^3}\int
\{r(QA)'q_0''+heAq_0't\}.
\tag{27}
$$
(27)仍保原输入 $q_0$ 的全部左尾；不是令它紧后所得的公式。结合(16)(17)，它给表(21)第二行，并使其三阶平方系数与第一行完全一致。

加速度两行也可单独核对。记
$$
a_Y=[h^{-6}k^7]\mathscr A_Y,\qquad
a_Z=[h^{-6}k^7]\mathscr A_Z.
$$
原式给
$$
a_Y=\mathsf A/384+\mathsf B/1536+\mathsf C/3840-\mathsf T/768,
$$
$$
a_Z=\mathsf A/384+\mathsf B/1536+\mathsf C/3840.
\tag{28}
$$
另一方面，真实中心导数满足
$$
\partial_{\rm c}[h^{-5}k^6]\mathscr A_Y
=-5\mathsf A/384-7\mathsf B/1536-\mathsf C/2560+5\mathsf T/768,
$$
$$
\partial_{\rm c}[h^{-5}k^6]\mathscr A_Z
=-5\mathsf A/384-7\mathsf B/1536-\mathsf C/2560.
\tag{29}
$$
例如 $\partial_{\rm c}M=P,\partial_{\rm c}C=2M,
\partial_{\rm c}R=P,\partial_{\rm c}R'=-r^2$；
其左端矩也同时输运。用(5)，本系数是
$7a_Y+\tfrac12(29)_Y$ 与 $7a_Z+\tfrac12(29)_Z$，准确得到表(21)后三行。
没有将 ordinary 外矩平移代替这些原算子的实际状态微分。

因此两个完整正规 scalar 的差只是
$$
\boxed{
[h^{-6}k^6]\{(\mathscr R_Y-Y\mathscr A_Y)
-(\mathscr R_Z-Y\mathscr A_Z)\}
=\frac{19\mathsf T}{3072}.
}
\tag{30}
$$
这个非零矩乘积还不能删除；下一节支付它。

## 6. 从原多线性配对精确恢复两份有序尾

表(21)中的每个 scalar 恒等对任意真实紧 $u$ 成立，不仅对偶母。
取实际不交包 $u<v$，将输入换成 $su+tv$。所有局部五次密度的 $s^3t^2$ 系数为零，而
$$
[s^3t^2]\mathsf A(su+tv)=\mu_0(v)M_3(u),
$$
$$
[s^3t^2]\mathsf T(su+tv)=\mu_0(v)M_3(u).
\tag{31}
$$
第一式使用原 $P_v$ 在左包上的真实常尾 $\mu_0(v)$，并非把它设零。

这里 scalar 极化与原两尾的因子必须分开。完整第二场中不交 mixed 输入为零；位于右方的 outer 不能看见左 inner 的右零恢复。因此
$$
[s^3t^2]\Omega(ZZ)=2\,\Omega(ZZ^\to),
\qquad
[s^3t^2]\Omega(YC)=\Omega(YC^\to).
\tag{32}
$$
$C_Aq_0$ 已成对消去的版本仍有同样的右向三角性：被减项是
$a(f,m_0(g,g))$，当 outer 在右而 inner 在左时，实际输入和它的右原函数都为零。
故(32)也适用于当前剩余的两个原 scalar 及其真实状态导数。

从表(21)，正规后的 $Y$ 在 $(\mathsf A,\mathsf T)$ 两列为
$(-380,190)/30720$；$Z$ 为 $(-380,0)/30720$。
由(31)(32)，两份真正的有序值分别是
$$
\boxed{
[h^{-6}k^6](\mathscr R_Y^\to-Y\mathscr A_Y^\to)
=-\frac{19n_0M_3}{3072},
}
$$
$$
\boxed{
[h^{-6}k^6](\mathscr R_Z^\to-Y\mathscr A_Z^\to)
=-\frac{19n_0M_3}{3072}.
}
\tag{33}
$$
第二式先由 scalar 的 $-380/30720$ 得出，再除原 $ZZ$ 的二倍因子。
本节没有用“两个 tail 应相同”作先验。

(33)对所有真实右包成立。R352 的原三矩线性尾映射及实际右包矩开像，使它准确确定整个 $n$ 映射：本系数只读 $n_0$，没有遗漏 $n_1,n_2$。最后按自然定义代 $n=\mu(u)$。

采用原配方
$$
\frac54\Lambda=(Y-Z)+\frac13Z^\to+\frac23Y^\to,
$$
(30)(33)给
$$
\frac54\Lambda_u(W_{kk})
=\frac{19\mu_0M_3}{3072}
-\frac{19\mu_0M_3}{3072}=0.
\tag{34}
$$
势响应(7)的 natural 已由独立全槽证明(14)为零。故(34)是原完整正规 $U$ 系数的自然零式。

将(34)代(19)，再代 R418 的完整锚值，证明(1)。

## 7. 同一个共同母库与负六正字符

R412/R414 的每个最终母都偶且 $M_5=0$。对任意实际幅度、中心、正宽
$$
u_i(x)=\rho_iU_i((x-\xi_i)/w_i),\qquad w_i>0,
$$
有
$$
\int u_i'(u_i'')^4=0,\qquad
\int x(u_i'')^5
=\rho_i^5w_i^{-9}\xi_iM_5(U_i)
+\rho_i^5w_i^{-8}\int y(U_i'')^5=0.
$$
(1)因此对全部这些实际 self 及其共同正仿射闭包为零。原 $\rho_i,\xi_i,w_i$ 不被更改。

(1)还是完整局部五次函数，所以任意不交辅助模板的 ordered $3+2$ 查询均为零。辅助模板不必偶、不必 $M_5=0$，也不必具有共同 $D,E_5$；不额外加入其 self 查询。于是同一个最小共同映射满足
$$
\mathcal A(V_{kk,-6}(k))=0\qquad\forall k.
\tag{35}
$$

取 R413/R414 正字符，已经由 R416、R419准确缩到
$$
\lambda\widehat Q_2=h^{-6}b_0(k)k_s^2,\qquad b_0(k)\ge0,
\quad \mu=0,\quad \lambda F_0=0.
$$
由同权 $E(U_{-6})=E(\mathcal R_{-6})$，减同权真实响应可清 whole $E$，同时保持(35)，因为自然函数杀原响应空间。
$\lambda$ 经共同增强查询下降且杀响应，故
$$
b_0(k)=\lambda V_{kk,-6}(k)=0\qquad\forall k.
\tag{36}
$$
原完整正字符约化已使其余正规族的 action 为零，所以不存在该共同增强商上的非零权 $-6$ 正字符。

这没有把 $\widehat Q_{kk}$ 本身作为 $U$ 算子设零；一般 profile 的(1)并不为零。
也没有由 signed 的零函数身份直接造一条无基准真实路径。权 $-4$ 剩余速度 PSD、低自然共同商的实际截面、同一最终 profiles 的 totals、内部条件与十三行同规范 joint 继续各自原接口。
