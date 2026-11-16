# R426：零曲率 kk 负四锚的完整自然值与共同查询归约

日期：2026-11-16。**原式纸面证明；没有执行新的 profile、求积、符号程序、原根恢复、秩、人工测试或科学运行。**

本稿计算同一个真实正规二速度成本的完整锚
$$
V_0=[h^{-4}]\widehat Q_{kk}(h,0,0).
$$
这里先保全部水平导数、加速度势、真实左右尾和两个原势响应，再取状态及 Laurent 系数。主结论是
$$
\boxed{
\Lambda_u(V_0)
=-\frac1{32}\int uu'(u'')^3
+\frac3{64}\int x(u')^2(u'')^3
-\frac3{128}\int x^2u'(u'')^4
+\frac3{640}\int x^3(u'')^5 .
}
\tag{1}
$$
这是对任意实紧光滑 $u$ 的完整自然函数身份。右边没有剩余 primitive、矩乘积、Green 常数或三阶平方余项。

更准确地，记 R393 的 Q4 函数
$$
F_{Q4}(u)=\int(u'-xu'')^4u'''
=-2\int(u')^3(u'')^2+2\int x(u')^2(u'')^3
-\int x^2u'(u'')^4+\frac15\int x^3(u'')^5 .
$$
则
$$
\boxed{
\Lambda_u(V_0)=\frac3{128}F_{Q4}(u)
+\frac1{64}\int\{3(u')^3(u'')^2-2uu'(u'')^3\}.
}
\tag{2}
$$
最后一项平移不变，并在任一中心偶母及其全部真实幅宽中心副本上为零。因此，R412–R414 从起点保持共同 $D,E_5$ 的同一个最小查询映射，对本锚准确得到 $3F_{Q4}/128$；无需新增 $M_{25}$ 观察。相应单权平移不变正字符在此锚的值为零，但自然查询本身一般不为零。

本稿不从 $k=0$ 外推全部曲率，不宣布整个负四字符已排除。R425 已付完整 $hh$ 与 PSD 交叉项；全 $k$ 的 $kk$ 仍须单独完成。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R367](R367-exact-N2-Green-contraction-and-nonzero-quartic-velocity-correction.md)、[R386](R386-complete-quartic-velocity-natural-flux-and-a-new-mixed-direction.md)、[R393](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md)、[R402](R402-complete-static-low-layer-natural-flux-with-original-potential-and-tails.md)、[R413](R413-common-mother-Q4-chain-and-exact-low-layer-character-reduction.md)、[R418](R418-complete-kk-minus-six-natural-coefficient-and-common-query-cancellation.md)、[R421](R421-all-curvature-kk-minus6-natural-identity-and-common-character-cancellation.md)、[R423](R423-complete-static-potential-inputs-for-the-all-curvature-kk-minus4-coefficient.md)、[R425](R425-complete-hh-minus4-natural-identity-and-PSD-cross-cancellation.md)。

## 1. 原右锚、真实水平导数与完整正规项

固定原共同合法窗口及双 collar，$u\in C_c^\infty(I)$，始终使用
$$
Jf(x)=\int_x^{r_*}f(y)\,dy .
$$
只将 $u$ 及其 jets 视为紧；中间二、三次输出保持真实左尾。

令
$$
p=u',\quad r=u'',\quad t=u''',\quad
P=J(r^2),\quad M=J(xr^2),\quad C=J(x^2r^2+2p^2),
$$
$$
R=p^2+xP,\quad T=x^2p^2+xC,\quad F=x^2P-C,\quad
L=p-xr,\quad G=u-xp/2,\quad H=x^2r-2xp+2u.
\tag{3}
$$
其原矩为
$$
\mu_0=P(\ell),\qquad \mu_1=M(\ell),\qquad \mu_2=C(\ell).
$$
特别 $\mu_2$ 包含 $2p^2$。有
$$
P'=-r^2,\quad M'=-xr^2,\quad C'=-x^2r^2-2p^2,
$$
$$
R'=2pr+P-xr^2,\quad R''=2Lt,\quad
T'=x^2R'-F,\quad T''=2x^2Lt-2L^2.
\tag{4}
$$

写 $w=k_s,\beta=k_{ss}$，在真实 $h_s=h_{ss}=0$ 切片上保持
$$
Y=\partial_k+\frac1{2h}\partial_\omega
=\partial_k-\frac12\partial_d,\qquad d=h\omega-k.
$$
原完整密度是
$$
L_2=v_2-\mathcal B_{m_0}N_2-\mathcal B_{m_2}N_0-\Gamma(m_2).
\tag{5}
$$
若其中 scalar 项为 $\beta\mathscr A+w^2\mathscr R$，正规化给
$\mathscr R-Y\mathscr A$。常值端 germs 使原速度边势准确为零。**先求 $Y$，再取 $k=\omega=0$。**

R130 保证整个正规 Laurent 系数 $V_0$ 属于原 $U$。分开的 ambient 响应不因此自动属于 $U$。自然读出采用原完整配方
$$
\Lambda_u(V)=\int tV(u^2,0)-\frac{16}{5}\int t\pi V(u)
-\frac{32}{15}\int t\mathscr G_{V,u}(\mu(u)).
\tag{6}
$$
对右辅助包矩求状态导数时固定其真实矩 $n$，最后才代 $n=\mu(u)$。

## 2. 复用原完整 scalar，不以低层锚代替导数

以下完整源式就是 R418(14)–(20)。列出它们，以使本层新表可从原式直接核对。

一般状态设
$$
z=x+\omega,\quad e=hx+d,\quad Q=1+e^2,\quad
K_0=kz^2-(k^2+1)z/h,
$$
$$
G_z=u-zp/2,\quad L_z=p-zr,\quad
A_u=K_0r-K_0'p+2ku,\quad A_u'=K_0t.
$$
原第二局部分子为 $(wA,b,ewA)$，
$$
A=\frac{Qr^2+2hJ(er^2)}{32h^3},\qquad A'=\frac{Qrt}{16h^3}.
$$
置 $j_A=J(QtA)$，并对原右零输出 $q$ 写
$$
c_q(q)=\frac{Qr q'}{16h^2}+\frac{(hp-er)q}{8h}
+\frac{J_e(u,q)}{16h^2}.
$$
第三局部第一分量的系数是
$$
c_0=-\frac{G_zb'}{4h}+\frac{L_zb}{8h}+c_q(q_0),\quad
C_b=-\frac{j_A}{8h^2},
$$
$$
C_v=-\frac{QrA'}{16h^3}-\frac{Yj_A}{8h^2}+c_q(q_2).
\tag{7}
$$
其中 $q_0=m_0(u,u)$、$q_2=m_{2,kk}(u,u)$，$J_e$ 是原 R56 双线性 primitive。

原 $YC$ 先作真实 $s$ 分部积分。其 $C_Aq_0$ 子项
$-4\int a'a(u,q_0)$ 连同原有序 Green，按 R367(24)、R386(11)准确抵消
$-\mathcal B_{m_0}N_2$。静态 $b(u,q_0)$ 链和完整 $-\Psi(u,n)$ 均保留。消去后
$$
\begin{aligned}
\mathscr A_Y&=\int\left\{\frac{QA_utC_b}{2h}-4A'c_0\right\},\\
\mathscr R_Y&=\int\frac{QA_utC_v}{2h}
-\int\frac{tG_z}{2h}b(u,q_2)+\mathscr D(n_1),
\end{aligned}
\tag{8}
$$
$n_1=[w]n$ 是原第三 characteristic 的系数。最终状态下
$$
\mathscr D(f)=-\int t\Psi_{w=1}(u,f)
=\int\frac{r^2f}{8h}-\frac{Qr^2f''}{16h^3}.
\tag{9}
$$
(9)对有真实左尾的 $f$ 也成立；边界由紧 $p,r$ 支付。

另令
$$
D_0=q_0'/2-kb,\quad E_0=eq_0'/2-b-hq_0,\quad
D_2=YA+q_2'/2,\quad E_2=eD_2-A/2-hq_2,\quad
M_1=Yb+(k+e)A.
$$
完整 $ZZ$ 给
$$
\mathscr A_Z=\int\left\{
\frac{tA}{h^2}\left(\frac Q2q_0'-(k+e)b-ehq_0\right)
-\frac{r(b')^2}{4h^3}\right\},
$$
$$
\begin{aligned}
\mathscr R_Z=\int\bigg\{&
\frac t{h^2}(D_0D_2+E_0E_2+M_1^2/2)\\
&+\frac{A_u}{2h}\{Q(A')^2+2heAA'+h^2A^2\}
+\frac{(ke-1)tQA^2}{2h^2}-\frac{tP_{A,q_0}}{h^2}\bigg\},
\end{aligned}
$$
$$
P_{A,q_0}=\frac{(Qq_0''-heq_0')A+J(Qq_0'''A)}{4h}.
\tag{10}
$$
最后一项是原 $P_{ZZ,s}$ 的两份 history；其完整收缩也可写成
$$
-\int\frac{tP_{A,q_0}}{h^2}
=\frac1{4h^3}\int\{r(QA)'q_0''+heAq_0't\}.
\tag{11}
$$
不能仅保 $T_s$ 或只代一份交叉。

在本锚，
$$
A=\frac{r^2}{32h^3}+\frac{x^2r^2+2M}{32h},\quad
b=\frac R{8h}+h\left(\frac{G^2}{2}+\frac T8\right),
$$
$$
q_0=-\frac R{8h^2}-\frac T8,\qquad q_2=-\frac M{16h^2}.
\tag{12}
$$
原 R73 的真实导数是
$$
Ym_0|_0=-\frac{\mathbf P}{16h^3}-\frac{\mathbf L}{2h}
+\frac{\mathbf U}{8h}-\frac h2\mathbf Y,
$$
$$
YA|_0=-\frac{xr^2+P}{32h^2},\quad
Yb|_0=\frac P{16h^2}+\frac C{16}-\frac{xM}{8}
-\frac{xp^2}{8}+\frac{up}{4},
$$
$$
YG_z=-\frac p{4h},\qquad YL_z=-\frac r{2h}.
\tag{13}
$$
粗体分别表示原 $r_0,p_0,s_1,p_2$ 算子；它们不是(3)的积分记号。

## 3. 本层新增原函数与导数证据

原完整第三密度的单位 $w$ 项可不作任何低幂猜测地写成
$$
\begin{aligned}
n_1={}&\frac{G_z\{Yb+(k+e)A\}}{2h}-\frac{pb}{8h^2}
+K_0P_A+\frac{K_0}{z}B_A\\
&-\frac{pq_0}{8h}-\frac{J_e(u,q_0)}{16h^3},\\
P_A&=\frac{(Qr-hep)A+j_A}{4h},\qquad
B_A=\frac{(heu-Qp/2)A}{2h}.
\end{aligned}
\tag{14}
$$
这是 R56 的完整 $T_s,K_0P,K_0B/z$ 与 $-\Psi(u,q_0)$，保原右锚。在锚上它化为
$$
n_1=\frac{G\,Yb}{2h}-\frac{pG^2}{16h}
+\frac{QLA}{4h^2}-\frac{xj_A}{4h^2}
-\frac{J_e(u,q_0)}{16h^3}.
\tag{15}
$$
例如 $b+hq_0=hG^2/2$，且 $G(k+e)A/(2h)$ 的 $xGA/2$ 与原 $P_A,B_A$ 对应项抵消；没有删除原势。

令 $N_j=[h^{-j}]n_1$、$V=x^2r^2+2M$。本层需要
$$
64N_3=(u-xp)P+pM-p^3/3+J((u-xp)r^2)-xJ(xr^3)/3,
$$
$$
\begin{aligned}
128N_1={}&x^2LV-xJ(tx^2V)+4G(C-2xM)+8pG^2\\
&+J(x^2rT''+2pT').
\end{aligned}
\tag{16}
$$
直接求真导数得
$$
\begin{aligned}
128N_1'={}&8u^2r-16xupr+4x^2p^2r+4x^2ur^2
-2x^3pr^2\\
&-2xrC-8GM-J(tx^2V).
\end{aligned}
\tag{17}
$$
原两份含 $t$ 的局部项相消；(17)的最后一个 $J$ 仍保留。

另外，(7)完整满足
$$
c_0'=-\frac{G_zb''}{4h}
+t\left\{-\frac{zb}{8h}+\frac{Qq_0'}{16h^2}
-\frac{eq_0}{8h}\right\}.
\tag{18}
$$
以下短式固定新表所用的加速度导数：
$$
\begin{aligned}
128([h^{-2}]c_0)'&=-t(8GL+T'+x^2R'),\\
128([h^{-3}]Yc_0)'&=t(4xpr+xP+M-2x^2r^2),\\
128([h^{-1}]Yc_0)'&=t\{-8u^2+16xup-7x^2p^2-12x^2ur\\
&\hspace{29mm}+12x^3pr-\tfrac72x^4r^2+xC+x^2M\}.
\end{aligned}
\tag{19}
$$
各原右值均为零，故(19)也固定其真实积分常数。最后
$$
[h^{-2}]C_v=-\frac{x^4r^2t}{256}-\frac{HP}{256}
-\frac{x^3r^3}{768}+\frac{J((u-xp)r^2)}{128}.
\tag{20}
$$
低两幂沿 R418 原式保留，而非从本幂外推。

## 4. 两个完整 scalar 的 h−4 表

定义实际积分
$$
B_1=\int xp^2r^3,\quad B_2=\int x^2pr^4,\quad B_3=\int x^3r^5,
\quad U_p=\int upr^3,\quad U_x=\int xur^4,
$$
$$
A_1=\int xPpr^2,\quad A_3=\int x^2Pr^3,\quad A_4=\int Cr^3,
\quad V_1=\int Mpr^2,\quad V_2=\int xMr^3,
$$
$$
M_3=\int r^3,\quad M_{13}=\int xr^3,\quad P_{12}=\int pr^2,
\quad H_s=\int x^2r^3-2\int xpr^2,\quad H_1=M_{13}-3P_{12}.
\tag{21}
$$
这些只是原积分名称，不假定它们独立。

把(12)–(20)代入(8)–(11)，对同一个完整水平导数先作正规化，置
$$
\mathcal Y=[h^{-4}](\mathscr R_Y-Y\mathscr A_Y),\qquad
\mathcal Z=[h^{-4}](\mathscr R_Z-Y\mathscr A_Z).
$$
全部局部项为：

| 左式 | $U_p$ | $U_x$ | $B_1$ | $B_2$ | $B_3$ |
|---|---:|---:|---:|---:|---:|
| $6144\mathcal Y$ | $-16$ | $-8$ | $24$ | $-8$ | $-16/5$ |
| $6144\mathcal Z$ | $192$ | $8$ | $-192$ | $48$ | $-16/5$ |

表(22)。

同两行的全部非局部与矩乘积项分别为
$$
\begin{aligned}
6144\mathcal Y:\quad&
24A_1-12A_3+4A_4+72V_1-48V_2\\
&+6\mu_0H_s+24\mu_1M_{13}-36\mu_1P_{12}-2\mu_2M_3,\\
6144\mathcal Z:\quad&
24A_1-12A_3+4A_4-72V_1.
\end{aligned}
\tag{23}
$$
因此还未加有序尾时，
$$
\begin{aligned}
6144(\mathcal Y-\mathcal Z)={}&
-208U_p-16U_x+216B_1-56B_2+144V_1-48V_2\\
&+6\mu_0H_s+24\mu_1M_{13}-36\mu_1P_{12}-2\mu_2M_3.
\end{aligned}
\tag{24}
$$
不能在这里就声称局部。

列出三条保全部左常数的积分原函数，供直接复核(22)(23)。任意所需实际密度 $f$ 有
$$
\int Lt\,Jf=\frac12\int(R'-\mu_0)f,
$$
$$
\int x^2Lt\,Jf
=\int(x^2pr-x^3r^2/2-xp^2-C/2+\mu_2/2)f,
$$
$$
\int xGt\,Jf=\int(xGr-up-C/2+\mu_2/2)f.
\tag{25}
$$
例如第二个括号的导数准确为 $x^2Lt$，左值为零。原 $J(r^m t)$ 的符号始终按 $(Jf)'=-f$；没有把一个带尾的 primitive 视为紧。

在(10)的 $2heAA'$ 项，本锚的 $h^{-4}$ 部分准确为
$$
\frac1{256}\int xLrt(x^2r^2+M).
\tag{26}
$$
这里已经乘外面的 $A_u/(2h)=L/(2h^2)$。这个 $1/2$ 与(11)的真实 history 同样必要。

## 5. 从原极化得到有序尾，不能仅凭 self 局部项

取实紧右辅助包 $v$，$\operatorname{supp}u<\operatorname{supp}v$，
其原矩为 $n=(n_0,n_1,n_2)$。原全部二次 mixed 输出在不交输入上为零。
原右锚恢复又使
$C(v;u^2)=0$，而 $C(u;v^2)$ 是准确的右包三矩尾作用。

因此，对(8)(10)尚未缩成表格的真正场表达式作五次极化，有
$$
[s^3t^2]\mathcal Z(su+tv)=2\mathcal Z^\to(u;n),\qquad
[s^3t^2]\mathcal Y(su+tv)=\mathcal Y^\to(u;n).
\tag{27}
$$
第一式的 $2$ 来自 $ZZ$ 的两份交叉；第二式的唯一槽是
外 $u'''$、$Y_u$ 和 $C(u;v^2)$。

(27)在前述 $C_Aq_0/N_2$ 消去后仍成立，而非对任意人为改写 self 所作的假定。具体地，被减的 self 是
$-4\int a'a(u,q_0)$。由于 $a'$ 局部，其 $s^3t^2$ 系数恰为
$-4\int a'(u,u)a(u,p_{m_0}(n))$。R367 原
$a(u,p)=c\ell_pF_u/2$ 给此值 $2\mathcal G(p,T_{\rm left})$，
正是那份被减的真实 $YC$ 尾。故相同消项在两边同时成立。
状态微分与有限极化交换，$n$ 始终固定。

现在可对已经完全等值的(22)(23)取该系数。左域内
$$
P\mapsto s^2P+t^2n_0,\quad M\mapsto s^2M+t^2n_1,\quad
C\mapsto s^2C+t^2n_2;
$$
右域上的所有含左 profile 的局部 jets 或右零原输出为零。
例如 $A_1,A_3,A_4,V_1,V_2$ 的 $s^3t^2$ 系数依次为
$$
n_0\int xpr^2,\quad n_0\int x^2r^3,\quad n_2M_3,\quad
n_1P_{12},\quad n_1M_{13}.
$$
连同(23)的原矩乘积，准确得到
$$
\boxed{
\begin{aligned}
6144\mathcal Z^\to(u;n)&=-6n_0H_s+2n_2M_3-36n_1P_{12},\\
6144\mathcal Y^\to(u;n)&=-6n_0H_s+2n_2M_3
+36n_1P_{12}-24n_1M_{13}.
\end{aligned}}
\tag{28}
$$
这里 $ZZ$ 已除过(27)的 $2$。

原自然配方的固定权重给
$$
\frac54[h^{-4}]\widehat\Lambda\!\left(
\operatorname{IBP}(v_2-\mathcal B_{m_0}N_2)\right)\Big|_{k=\omega=0}
=\mathcal Y-\mathcal Z+\frac13\mathcal Z^\to(u;\mu)
+\frac23\mathcal Y^\to(u;\mu)
$$
于本层。于是
$$
\begin{aligned}
6144\{\mathcal Y-\mathcal Z+\mathcal Z^\to/3+2\mathcal Y^\to/3\}
={}&-208U_p-16U_x+216B_1-56B_2\\
&+144V_1-48V_2+8\mu_1H_1 .
\end{aligned}
\tag{29}
$$
$\mu_0,\mu_2$ 乘积已消；第一矩尾仍未消。

## 6. N0 原势响应的三个完整槽

R423 的四势身份在本锚准确只留下
$$
-[h^{-4}]\mathcal B_{m_{2,kk}}N_0=\mathcal B_{\mathbf S}\tau_0/16,
\qquad \mathbf S=\Phi_{s_0}.
\tag{30}
$$
$\Gamma(m_{2,kk})$ 在此只有 $h^{-2}$，故不贡献本层。不是将其一般删除。

R402 原独立外槽为
$$
64\tau_0(f;g^2)=2fF_g'-f'F_g+xJ(f'F_g''),
\qquad F_g=x^2J((g'')^2)-J(x^2(g'')^2+2(g')^2).
\tag{31}
$$
outer 可带原二次左尾。令
$$
I=\int t\tau_0(M;u^2),\quad
J_*=\int t\tau_0(u;u,M),\quad
K=\int t\mathbf S(u,\tau_0(u;u^2)).
$$
所需两个原式是
$$
F_{u,M}=-x^2J(r^3)/3-J(x^2r^3)+2J(xpr^2),
$$
$$
64(\tau_0(u;u^2))''=2LR'+(8GL-F)t.
\tag{32}
$$
由(31)(32)，完整三槽表为
$$
\begin{aligned}
64I={}&22B_1/3-6B_2+2B_3-2A_1+A_3+A_4/3-12V_1+4V_2,\\
64J_*={}&\mathcal J-\mu_2M_3/3-\mu_0H_s,\qquad
64K=-\mathcal J,
\end{aligned}
$$
$$
\mathcal J=8U_p/3-4U_x/3-14B_1/3+13B_2/3-B_3+A_3-2A_1+A_4/3.
\tag{33}
$$
例如第二行可从
$$
64J_*=\int\{r^2F_{u,M}-prF_{u,M}'
-(2ur+p^2-xpr)F_{u,M}''\}
$$
直接复核；其中 primitive 合成的真实边项正是
$-\mu_2M_3/3-\mu_0H_s$。第三行只用紧 outer，
$K=\int xr^2(\tau_0(u;u^2))''$，没有要求三次输出左紧。

对此势的 pure 有序尾必须另按原三槽计算。
置 $D_-=\partial_x,D_+=x^2\partial_x-2x$，
$$
X_n=(n_2D_--n_0D_+)/64.
$$
原右尾给
$$
\tau_0(f;v^2)=X_nf,\quad p_{\mathbf S}(n)=n_1,\quad
\tau_0(n_1;u^2)=n_1R/16,\quad \tau_0(u;u,n_1)=0.
$$
故
$$
8\Gamma^\to_{\pi\mathcal B_{\mathbf S}\tau_0}(u;n)
=q_{X_n\cdot\mathbf S}(u)+n_1R/16.
$$
由原同锚作用 $D_-\cdot\mathbf S=\mathbf P$、
$D_+\cdot\mathbf S=-2\mathbf U$，以及
$\int tP=M_3,\int t\mathbf U(u,u)=3H_s/2,\int tR=H_1$，
$$
\boxed{512\int t\Gamma^\to(u;n)=n_2M_3+3n_0H_s+4n_1H_1.}
\tag{34}
$$
这里的第一矩项不可从 R402 的不同 outer 旧尾表省略。

原正式 pure 的 $1/8$ 与 self 两倍因子给
$$
\widehat\Lambda(\mathcal B_{\mathbf S}\tau_0)
=\frac85I-\frac45J_*+\frac45K-\frac{32}{15}\int t\Gamma^\to(u;\mu).
$$
由(33)(34)准确得到
$$
\boxed{
240\widehat\Lambda(\mathcal B_{\mathbf S}\tau_0)
=72B_1-62B_2+18B_3-16U_p+8U_x-72V_1+24V_2-4\mu_1H_1.
}
\tag{35}
$$
此单项仍非局部；不能单独删去 $V_1,V_2$ 或左矩。

## 7. 全部原尾合成后才得到局部身份

在 $6144(5/4)\Lambda$ 的统一规范内，(30)(35)贡献
$$
-32U_p+16U_x+144B_1-124B_2+36B_3-144V_1+48V_2-8\mu_1H_1.
$$
与(29)相加，得到
$$
6144\,\frac54\Lambda_u(V_0)
=-240U_p+360B_1-180B_2+36B_3.
\tag{36}
$$
所有 $V_1,V_2,\mu_1H_1$ 至此才准确抵消。乘 $4/5$ 即(1)。

因此(1)已经包含原 $v_2$、完整 $C_Aq_0/N_2$ 消去、加速度正规化、
$-\Psi(u,n)$ 的全部 $P/B$ 链、两个 $ZZ$ history 交叉、原 $N_0$ 三槽和正式 pure/ordered 补偿。
本证明没有从某些显式主项相消推测其余低阶项，也没有把旧 pure 坐标当作完整自然值。

## 8. 与旧 Q4 像及真实共同母库的关系

按 R393 的完整 C² 呈示，(1)逐系数恰给(2)。记
$$
G_{\rm tr}(u)=\int\{3p^3r^2-2upr^3\}.
$$
它无显式坐标，故 $G_{\rm tr}(u(\cdot-c))=G_{\rm tr}(u)$。
若 $U$ 为中心偶母，两个密度均为奇函数；所以对任何实际
$$
u_i(x)=\rho_iU_i((x-\xi_i)/w_i),\qquad w_i>0,
$$
即使不同 $U_i,\rho_i,w_i,\xi_i$，都有
$$
G_{\rm tr}(u_i)=0,\qquad
G_{\rm tr}(C_{H,c}u_i)=0\quad(H>0).
\tag{37}
$$
这里保全部真实宽度与中心，不假设末母相同或同宽。共同合法窗口按 R414 的明确实施前提从起点固定；不任意扩张旧冻结几何。

若母库还满足原 $M_5(U_i)=0$，则 R413 的原平移公式给
$$
F_{Q4}(C_{H,c}u_i)
=-4D(U_i)\rho_i^5(Hw_i)^{-7}(H\xi_i+c).
$$
于是
$$
\boxed{
\Lambda_{C_{H,c}u_i}(V_0)
=-\frac{3D(U_i)}{32}\rho_i^5(Hw_i)^{-7}(H\xi_i+c).
}
\tag{38}
$$
若写成原成本正仿射作用，另乘原协变的共同 $H^2$；不能遗漏这个外因子。
等价地，直接平移斜率为
$$
\frac3{64}\left(\int p^2r^3-\int xpr^4\right)
+\frac9{640}\int x^2r^5=-\frac3{32}D(u)
$$
于中心偶 $M_5=0$ 母。其 $M_{25}$ 项准确抵消，不须新增该观察。

(1)和(2)均为完整局部五次泛函。因此对任意不交的实际 $v,w$，
$$
[s^3t^2]\Lambda_{sv+tw}(V_0)=0.
\tag{39}
$$
辅助矩基不必偶、不必与实际母有相同 $D,E_5$；最小共同映射只取所需 ordered 系数，不擅自加入辅助包自身的自然查询。

综上，R414 同一个最小共同自然映射 $\mathcal A$ 准确满足
$$
\boxed{\mathcal A(V_0)=\frac3{128}\mathcal A(F_{Q4}).}
\tag{40}
$$
右边解释为 Q4 中一个已有实际线性系数的自然函数像；(40)不是两个完整成本的身份。

## 9. 共同负四字符的锚值为零，仍不能外推全曲率

按原从起点的 $F^\star$ 选择，全部最终母保共同 $D_0,E_0$，
$D_0-E_0>0$，或保同一非一比例。
R413 证明在这个共同商上 Q4 的权 $-4$ 像全在真实平移像中。
具体其 $NH=F_{Q4}/2-3G_{Q4}$ 的共同查询为
$6(E_0-D_0)c$，而 $F_{Q4}$ 的为 $-4D_0c$；
真实幅宽因子和全部 ordered 零行相同。
因此(40)也在这个真实平移像中。

若 $\lambda$ 经共同 $J=(E,\mathcal A)$ 下降、杀响应、为权 $-4$ 的平移不变字符，
R323 的同权 $E$ 响应等像先允许对该自然像关系补齐全部 $E$ 坐标；
补偿响应的自然查询为零。随后 $\lambda N=0$ 给
$$
\boxed{\lambda(V_0)=0.}
\tag{41}
$$
这不说 $\mathcal A(V_0)=0$，也不把签名线性成本当作一条无基准的实际路径。

R425 已独立支付所有曲率的 $hh$ 自然身份，并在同一个候选 PSD 字符下清交叉项。
本稿仅新增 $kk$ 在 $k=0$ 的完整锚，准确给剩余标量 $b_0(0)=0$。
一个非负曲率多项式仍可在零点取零而在别处非零；
因此必须继续处理全 $k$ 的剩余原系数。
R423 的四势响应在该后继中均须保留，本稿未授 $(1+k^2)$ 整除或全曲率零值。

全部实际共同正锥、有限截面、未付内部 partial、平台和同一规范 period 仍按原范围保留。
