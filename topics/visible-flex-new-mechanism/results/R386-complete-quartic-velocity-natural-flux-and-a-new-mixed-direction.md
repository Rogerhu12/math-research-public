# R386：完整四次速度成本的局部自然通量与一个新混合方向

日期：2026-11-15。**完整原式纸面证明；没有执行新的积分、符号程序、研究计算、人工检查或参数求根。**

[R370](R370-complete-quartic-velocity-cost-and-exact-C2-total-flux.md) 已支付完整纯 $\delta^4$ 成本。
本稿保留原 $C_A m_2$、$-\Psi(u,n)$、$ZZ$ 的两类 history 导数和两个有序真实尾，
完成所有速度方向的同一个自然读出。
使用的是 [R382](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md) 已更正的完整 H 零身份，不使用已经撤回的 H 非零或秩结论。

固定实际状态 $h>0,d=h\omega-k$，置
$$
e=hx+d,\qquad Q=1+e^2,\qquad
v=u',\quad r=u'',\quad t=u'''.
$$
对任意两个实速度分量 $(\gamma,\delta)$，令
$$
l=\gamma v-(\gamma x+\delta)r.
$$
记 $\mathcal Q_S[\gamma,\delta]$ 为原完整正规四次速度成本在这些真实水平坐标中的值。
主结论为
$$
\boxed{
\Lambda_u\bigl(\mathcal Q_S[\gamma,\delta]\bigr)
=-\frac1{32h^8}\int_I Q\,l^4t,
\qquad u\in C_c^\infty(I).
}
\tag{1}
$$
尽管右边写有一次 $u'''$，它准确等于一个只使用 $u',u''$ 的局部五次多项式泛函。
没有未控制的 primitive、左尾或 $C^2$ 余项。

式(1)是原完整系数的读出，不是将某一个 ambient 响应当作 $U$ 成员。
它不计算完整 $U/\mathcal R$，也不把系数的线性跨度当成实际几何的联合可达性。

## 1. 固定原锚、读出和速度坐标

全部右积分均为
$$
JF(x)=\int_x^{r_*}F(y)\,dy.
$$
$u$ 在共同双 collar 为零。由 $u$ 生成的二次、三次输出只要求原右零；其真实左尾保留。

采用 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 的原自然读出
$$
\Lambda_u(V)=\int tV(u^2,0)
-\frac{16}{5}\int t\,\pi V(u)
-\frac{32}{15}\int t\,\mathscr G_{V,u}(\mu(u)).
\tag{2}
$$
最后一项是实际位于左包右方的辅助包所定义的有序 $2+2$ 三矩尾。
它不是任意选择的补偿；最后按原三矩线性读出代入 $\mu(u)$。

为同时保留速度变化及正规势，先固定一个方向 $(c,\eta)$，令
$$
h_s=c\alpha,\qquad d_s=\eta\alpha,\qquad
\beta=\alpha_s,\qquad
\vartheta=cx+\eta,\qquad l=cv-\vartheta r.
\tag{3}
$$
状态方向在导数权四的显示系数上为
$$
D=c\partial_h+\eta\partial_d.
$$
这些最高导数权系数不依赖独立的 $k$：
原框架 $k$ 项和 $K_0$ 项均在较低导数权，不能混入本稿的四次速度系数。

真实水平关系仍是
$$
k_s=2\omega h_s-2d_s.
$$
从原 $(h_s,k_s)$ 正规式换到(3)，加速度平方及 H 层会产生附加项；
它们的完整自然读出分别由
[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)
和 R382 逐状态为零。因此下面的完整正规四次读出就是原 $U$ 中相应正规系数的真实线性组合。

## 2. 原二次分子和三个必要恒等

令 $a=a_S^{c,\eta}(u,u)$ 为原第二局部第一分子的单位速度系数。
由 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、
[R76](R76-local-third-exact-loops-and-weight-three-control.md)，
$$
a'=\frac{Ql\,t}{8h^3},\qquad a(r_*)=0.
\tag{4}
$$
原速度二次矩阵作用为
$$
q=m_2^{c,\eta}(u,u)
=\frac{2\vartheta a}{h}+\frac{Ql^2}{8h^4}.
\tag{5}
$$
这是原八矩输出，不是新增的二次输入。它的右值为零，左侧是真正仿射尾。

置
$$
c_1=\frac{2e\vartheta}{Q}-\frac ch,\qquad
b=\frac{\vartheta-ce/h}{h}.
$$
特别 $b_x=0$。逐原导数有
$$
\boxed{
\begin{aligned}
q'&=\frac{2ca}{h}+\frac{el^2}{4h^3},\\
q''&=\frac{l^2}{4h^2}-2c_1a',\\
(Da)'&=\left(c_1-\frac{2c}{h}\right)a'.
\end{aligned}}
\tag{6}
$$
前两式使用 $l'=-\vartheta t$；(5)中两份含 $t$ 的项在第一次导数时恰好抵消。
第三式只用 $Dl=0,DQ=2e\vartheta$。

记
$$
j=J(Qt a),\qquad j_D=J(Qt Da),\qquad
L=a(\ell),\qquad B=(Da)(\ell).
\tag{7}
$$
$j_D$ 不等于 $Dj$；后者还含 $J(2e\vartheta t a)$。
$L,B,j(\ell),j_D(\ell)$ 均不置零。

## 3. 原第三局部项以及完整 N2 校正

原第三局部第一分子的导数权二部分为
$$
c_3=\beta C_b+\alpha^2C_v,
$$
$$
C_b=-\frac{j}{8h^2},\qquad
C_v=-\frac{j_D}{8h^2}-\frac{Ql a'}{8h^3}.
\tag{8}
$$
它来自 R56 的全部 $T_{sx},P_s,P_x,B_x$ 项。
此前 H 更正中第三 history 的 $P/B$ 链项也必须保留，不能再只留 $T_s$。

原第三 characteristic 密度的权三部分准确为
$$
n^{[3]}=2\alpha\beta T+\alpha^3n_0,
$$
$$
T=\frac{Ql a-\vartheta j}{8h^3},\qquad
\Sigma(F)=\frac{Ql F-\vartheta J(QtF)}{4h^3},
$$
$$
\boxed{n_0=\Sigma(Da+c_1a)-\Psi_{c,\eta}(u,q).}
\tag{9}
$$
其中 R73 的完整链式项为
$$
-\Psi_{c,\eta}(u,f)
=\frac{bvf}{4}+\frac{cQvf'}{8h^3}
+\frac{\vartheta}{8h^3}J(Qrf''+2h^2vf').
\tag{10}
$$

还须扣除原正规密度 $L_4=v_4-\mathcal B_{m_2}N_2$ 的完整校正。
这里不能只扣其三阶平方主部。

为明确这个消去对一般方向仍成立，令
$$
a_q=a(u,q),\quad A_q=a_q(\ell),\quad
S=-\int qT''',\quad p=q_{\rm left}.
$$
[R367](R367-exact-N2-Green-contraction-and-nonzero-quartic-velocity-correction.md)
的原同锚 Green 配对记为 $\mathcal G(p,T_{\rm left})$。由真实对称极化
$$
a_q'=\frac{Q}{16h^3}\{t\,l_q+q'''l\},
$$
三次 Green 身份给
$$
-4\int a'a_q=2(S+2LA_q).
$$
原 $C_s$ 中 $-K(u,m_2)$ 的 self 贡献就是左边。
其实际有序尾贡献为 $2\mathcal G$。
按照原 $2/3$ 的 $YC$ 尾权重，合计为
$$
2(S+2LA_q)+\frac43\mathcal G
=\frac54\,\widehat\Lambda(\mathcal B_{m_2}N_2).
\tag{11}
$$
最后一个等式正是 R367(24) 的完整 $8/5$ 规范。
所以原正规化减去 $\mathcal B_{m_2}N_2$ 时，
这一份 $C_A m_2$ **连同其非紧 Green 和实际尾整项消去**。
下文系数表均在这次准确消去之后书写。

## 4. 一个保任意真实左尾的简短收缩

定义
$$
\mathscr D(f)=-\int t\,\Psi_{c,\eta}(u,f).
$$
$f$ 只需原右零，可以带真实左尾。
由(10)和紧 outer 的两次分部积分，
$$
\mathscr D(f)=\frac1{8h^3}\int
\{Qr(\vartheta r-2cv)f''
-c(Qr^2+2h^2v^2)f'-2h^3br^2f\}.
$$
进一步准确化为
$$
\boxed{
\mathscr D(f)=2\int a'f'-\frac1{2h^2}\int eltf.
}
\tag{12}
$$
证明中令
$$
M=her(2cv-\vartheta r)-ch^2v^2.
$$
则
$$
M'=-h^3br^2+2helt.
$$
$M$ 在两 collar 为零，故其边项为零而不要求 $f(\ell)=0$。
这也说明(12)不是一次未经说明的左尾删项。

由(9)直接得到
$$
T'=\frac{2hel a+Ql a'-cj}{8h^3},
$$
$$
\boxed{
\mathscr D(T)
=\frac1{4h^3}\int\{Ql(a')^2+h c_1a'j\}.}
\tag{13}
$$
这两式只用 $j'=-Qt a$ 和 $l'=-\vartheta t$。

## 5. 完整 self 的原系数表

令 $D_1=Da+q'/2$、$E_1=eD_1+\vartheta a-hq$。
原第二场协变导数的权二平面为
$$
(\beta a+\alpha^2D_1,\ e\beta a+\alpha^2E_1).
$$
定义原 $ZZ$ 的 normal 配对
$$
P_a=-\frac{ea^2}{2}+\frac1{2h}J(Q(a')^2),\qquad
B_a=\frac{Qa^2}{2h},
$$
$$
P_{a,q}=
\frac{(Qq''-heq')a+J(Qq'''a)}{4h},\qquad
B_{a,q}=\frac{(heq-Qq'/2)a}{2h}.
\tag{14}
$$
$P_{ZZ,s}$ 和 $B_{ZZ,s}$ 的两份真实 history 导数分别给
$-2P_{a,q}$、$-2B_{a,q}$。不先将累计 history 值设零再求导。

把每个 scalar 收缩写成
$a_\bullet\beta^2+\sigma_\bullet\alpha^2\beta+\rho_\bullet\alpha^4$。
原 $ZZ$ 精确给
$$
\begin{aligned}
a_Z&=\frac1{2h^2}\int tQa^2,\\
\sigma_Z&=\int t\left\{\frac{a(D_1+eE_1)}{h^2}
-\frac{2\vartheta P_a+2cB_a}{h^2}\right\},\\
\rho_Z&=\int t\left\{\frac{D_1^2+E_1^2}{2h^2}
-\frac{\vartheta DP_a+cDB_a}{h^2}
+\frac{2\vartheta P_{a,q}+2cB_{a,q}}{h^2}\right\}.
\end{aligned}
\tag{15}
$$

对原 $YC$，先将所有 $c_{3,s}$ 作真实 $s$ 分部积分。
因为 $(Da)'=(c_1-2c/h)a'$，它们合为
$$
-4\beta\int a'c_3+\frac{8c}{h}\alpha^2\int a'c_3.
$$
再加完整(10)，得到
$$
\begin{aligned}
a_Y&=-4\int a'C_b,\\
\sigma_Y&=-4\int a'C_v+\frac{8c}{h}\int a'C_b+2\mathscr D(T),\\
\rho_Y&=\frac{8c}{h}\int a'C_v+\mathscr D(n_0).
\end{aligned}
\tag{16}
$$
(15)(16)都保留了第三 $-\Psi(u,n)$ 的全部 $P/B$ 项。
第三局部 normal 分量的其他项及原框架系数在本处是较低导数权，不被冒充为四次项。

## 6. 两个有序真尾：仿射 q 尾的两份交叉都要保

先取真正位于 $u$ 右侧的辅助包，全部尾对其三矩线性解释。
最后按(2)代入 $\mu(u)$，于是原分子尾是 $L$，其状态导数是 $B$。
(5)在左域准确给
$$
p=q_{\rm tail}=\frac{2\vartheta L}{h}.
\tag{17}
$$
除纯 $\delta$ 方向外，它不是常数；不能删除其导数。

置
$$
F=Qr-2hev+2h^2u,\qquad F'=Qt,\qquad
H=Ql+\vartheta F,\qquad H'=2hel+cF.
$$
原第三尾恢复为
$$
C_{bt}=\frac{LF}{8h^2},\quad
C_{vt}=\frac{BF}{8h^2},\quad
T_t=\frac{LH}{8h^3},\quad
n_{0t}=\frac{BH}{4h^3}.
\tag{18}
$$
其中 $n_{0t}$ 使用准确抵消
$$
\Sigma(c_1L)-\Psi_{c,\eta}(u,p)=0.
$$
例如
$$
J\{(2e\vartheta-cQ/h)t\}
=-(2e\vartheta-cQ/h)r+2h\vartheta v-2hcu
$$
直接支付该式的同锚常数。

令
$$
D_t=B+cL/h,\quad E_t=eD_t-\vartheta L,\quad
P_t=-eaL/2,\quad B_t=QaL/(2h).
$$
这次两个 $P$ 交叉都存在：
$$
\begin{aligned}
P_{a,p}&=-\frac{ecLa}{2h},&
P_{L,q}&=\frac L4(eq'-2hq),\\
B_{a,p}&=\frac{La}{2h}(2e\vartheta-cQ/h),&
B_{L,q}&=\frac L{2h}(heq-Qq'/2).
\end{aligned}
\tag{19}
$$
右方输出在左域是原常数分子，不是任意截断的多项式输入。

两个尾的完整系数是
$$
\begin{aligned}
a_{Zt}&=\frac1{2h^2}\int tQaL,\\
\sigma_{Zt}&=\int t\left\{
\frac{aD_t+D_1L+eaE_t+eE_1L}{2h^2}
-\frac{2\vartheta P_t+2cB_t}{h^2}\right\},\\
\rho_{Zt}&=\int t\left\{
\frac{D_1D_t+E_1E_t}{2h^2}
-\frac{\vartheta DP_t+cDB_t}{h^2}
+\frac{\vartheta(P_{a,p}+P_{L,q})
+c(B_{a,p}+B_{L,q})}{h^2}\right\},
\end{aligned}
\tag{20}
$$
$$
\begin{aligned}
a_{Yt}&=-4\int a'C_{bt},\\
\sigma_{Yt}&=-4\int a'C_{vt}
+\frac{8c}{h}\int a'C_{bt}+2\mathscr D(T_t),\\
\rho_{Yt}&=\frac{8c}{h}\int a'C_{vt}+\mathscr D(n_{0t}).
\end{aligned}
\tag{21}
$$
所有 $D$ 都对真实右包三矩保持固定；不得只匹配瞬时尾值而停止对它求状态导数。

## 7. 加速度项和真实速度势准确抵消

从(14)–(16)及(6)，原 $ZZ$ 的速度势系数先准确化为
$$
\sigma_Z=\frac1{h^2}\int Qt\,aDa
+\frac1{h^3}\int Ql(a')^2.
\tag{22}
$$
用(13)和 $(Da)'=(c_1-2c/h)a'$，另一份给
$$
\boxed{
\sigma_Y-\sigma_Z
=-\frac{L j_D(\ell)+B j(\ell)}{2h^2}.}
\tag{23}
$$
这里确实使用了非零边项
$$
\int a'j_D=-L j_D(\ell)+\int Qt\,aDa,\qquad
\int(Da)'j=-B j(\ell)+\int Qt\,aDa.
$$

独立化简(20)(21)则给
$$
\boxed{
\sigma_{Zt}=\sigma_{Yt}
=\frac{L j_D(\ell)+B j(\ell)}{2h^2},\qquad
\rho_{Zt}=\rho_{Yt}=\frac{B j_D(\ell)}{2h^2}.}
\tag{24}
$$
例如(12)(18)给
$\mathscr D(T_t)=-L\int c_1a'F/(4h^2)$，
再用 $F'=Qt$，直接得到 $YC$ 两式。
$ZZ$ 两式从(20)代入(5)(6)(19)得到；
其消去尤其依赖两份 $P$ 和两份 $B$ 交叉全部存在。

加速度系数同样准确为
$$
a_Y-a_Z=-\frac{Lj(\ell)}{2h^2},\qquad
a_{Zt}=a_{Yt}=\frac{Lj(\ell)}{2h^2}.
$$

原 self、pure、ordered 尾的固定合成规范是
$$
\frac54\Lambda
=\Omega(YC)-\Omega(ZZ)
+\frac13\Omega(ZZ_t)+\frac23\Omega(YC_t).
\tag{25}
$$
因此其 $\beta^2$ 及 $\alpha^2\beta$ 系数**逐状态准确为零**。
按原正规化，速度势应减 $D\sigma/3$；在(25)中该完整系数已经为零，
所以它没有被忽略，而是与真实尾一起抵消。
剩余四次系数准确是
$$
\boxed{
\frac54\Lambda(\mathcal Q_S[c,\eta])
=\rho_Y-\rho_Z+\frac{B j_D(\ell)}{2h^2}.}
\tag{26}
$$

## 8. 从原 primitives 到局部式的可审消元

下面给出(26)不依赖猜测的中间表。
令
$$
j_c=J(Qt c_1a),\qquad
U=J(Qrq''+2h^2vq'),\qquad N=-\Psi_{c,\eta}(u,q).
$$
由(6)和一次同锚积分分部，
$$
\boxed{
U=2j_c+2Qr c_1a-4h\vartheta va-\frac{Qvl^2}{4h^2}.}
\tag{27}
$$
核对时先把 $-2Qr c_1a'$ 积分分部，
再用 $(Qc_1)'=2h\vartheta$；
剩余积分密度恰是
$(4h\vartheta va+Qvl^2/(4h^2))'$。
右端 $v=0$ 支付常数，没有删除左值。

原(16)可写为
$$
\begin{aligned}
\rho_Y={}&\frac1{h^3}\int Ql a'(Da)'
+\frac1{2h^3}\int Ql c_1'a a'
+\frac1{2h^2}\int(Da)'j_D\\
&+\frac1{2h^2}\int c_1a'j_c+\mathscr D(N).
\end{aligned}
\tag{28}
$$
这里
$$
\begin{aligned}
\mathscr D(N)=\int\bigg\{&
\frac{Ql a'q''}{4h^3}
+\frac{c a'(Qr-2hev)q'}{4h^3}\\
&+\frac{b a'(Qr-2hev)q}{2Q}
-\frac{c_1a'U}{4h^2}\bigg\}.
\end{aligned}
\tag{29}
$$
最后一个分母是 $4h^2$。

从(15)独立得到
$$
\begin{aligned}
\rho_Z={}&\int t\left\{
\frac{Q(Da)^2}{2h^2}
+\left(b^2+\frac{c^2}{h^4}\right)a^2
+\frac{\vartheta al^2}{8h^5}
+\frac{Ql^4}{128h^8}\right\}\\
&+\frac1{h^3}\int Ql a'(Da)'
+\frac1{2h^3}\int Ql c_1(a')^2+\mathcal H,
\end{aligned}
\tag{30}
$$
$$
\mathcal H=\int\left\{
\frac{elaq''}{h^2}+\frac{Ql a'q''}{2h^3}
+\frac{cet\,aq}{h^2}
-\frac{(he\vartheta+cQ)t\,aq'}{2h^3}\right\}.
\tag{31}
$$
(31)是(14)两个 history 配对的完整收缩；
处理 $J(Qq'''a)$ 时用的是紧 $(\vartheta r-cv)=-l$，
并未要求 $q$ 左紧。

在(28)中，
$$
\int(Da)'j_D=-B j_D(\ell)+\int Qt(Da)^2.
$$
第一项恰被(26)的真实尾消去，第二项与(30)的第一项消去。
随后(27)使两个 $j_c$ 项准确相消。
再用(5)(6)以及
$Qc_1'=2h(\vartheta-ec_1)$，其余项逐项合为
$$
\boxed{
\begin{aligned}
\frac54\Lambda(\mathcal Q_S[c,\eta])=\int\bigg\{&
-\frac{\vartheta b}{h}a^2t
+\frac{al^2t}{8h^5}
\left[\vartheta(5e^2-1)-\frac{2ceQ}{h}\right]\\
&-\frac{eal^3}{4h^4}
-\frac{Q(1+2Q)l^4t}{128h^8}\bigg\}.
\end{aligned}}
\tag{32}
$$
这一步已无 $j,U$，但还保留真实 $a$。

最后只需两个由紧 $l$ 支付的积分分部。
因 $b_x=0$、$l'=-\vartheta t$，
$$
-\int\frac{\vartheta b}{h}a^2t
=\int\frac b h a^2l'
=-\frac1{4h^4}\int bQal^2t.
$$
所以(32)中 $al^2t$ 的完整系数变为
$3\vartheta(e^2-1)/(8h^5)$。
再用 $(l^3)'=-3\vartheta l^2t$，得到
$$
\int\frac{3\vartheta(e^2-1)}{8h^5}al^2t
=\int\frac{eal^3}{4h^4}
+\int\frac{(e^2-1)Ql^4t}{64h^8}.
$$
第一项消掉(32)中的另一份 $a$。
剩余恰为
$$
\boxed{\frac54\Lambda(\mathcal Q_S[c,\eta])
=-\frac5{128h^8}\int Ql^4t.}
\tag{33}
$$
乘原 $4/5$ 就是(1)。
全过程未令 $a_L$ 或任何原三矩为零。

## 9. 准确 C² 呈示和新的混合系数

式(1)可直接无分母地降低 profile 导数阶。
定义两个有限多项式
$$
F_4(v,r,\vartheta)=\int_0^r(cv-\vartheta z)^4\,dz,\qquad
G_3(v,r,\vartheta)=\int_0^r(r-z)(cv-\vartheta z)^3\,dz.
$$
这里的积分只是关于辅助变量 z 的多项式原函数，不是新的空间 history。
固定 $v,r$ 后，它们没有 $\vartheta=0$ 的奇点。
准确有
$$
\boxed{
\Lambda(\mathcal Q_S[c,\eta])
=\frac1{32h^8}\int
\{2he\,F_4+4cQ\,G_3\}.}
\tag{34}
$$
因为
$D_xF_4=l^4t+c\partial_\vartheta F_4+r\partial_vF_4$
且后两项之和为 $4cG_3$。
$F_4$ 在两 collar 为零，故(34)严格证明完整泛函连续于 $C^2$。

纯 $\delta$ 方向 $c=0,\eta=1$ 给
$$
\Lambda(\mathcal Q_\delta)
=\frac1{80h^7}\int(hx+d)r^5,
$$
在 $h=1$ 准确回到 R370。

新的 $\gamma\delta^3$ 完整系数为
$$
\boxed{
[\gamma\delta^3]\Lambda(\mathcal Q_S)
=\frac1{160h^8}\int
\{(4xQ'-Q)r^5-5Q'v r^4\}.}
\tag{35}
$$
在 $h=1,d=0$，
$$
\boxed{
[\gamma\delta^3]\Lambda(\mathcal Q_S)
=\frac1{160}\int(7x^2-1)r^5
-\frac1{16}\int xv r^4.}
\tag{36}
$$
这不是重新使用一个已撤回的 H principal；
它是(1)中实际完整四次系数的准确低阶值。

为了说明(36)确给 R384 两个泛函之外的方向，取一个实偶紧母函数 $u_0$，
使 $M=\int(u_0'')^5\ne0$。
这样的函数可按 R384 的三个不交偶 bump 二次原函数构造。
将同一母函数平移到中心 b，记 $u_b(x)=u_0(x-b)$。
由偶性，
$$
\int(u_b'')^5=M,\quad
\int x(u_b'')^5=bM,\quad
\int xu_b'(u_b'')^4=\int y u_0'(u_0'')^4.
$$
所以(36)在此族上的值是
$$
\frac{7M}{160}b^2+\text{一个与 b 无关的常数}.
\tag{37}
$$
选一个共同窗口容纳 b 的小开区间即可。
二次式(37)不在 $X(u)=\int xr^5$、$M(u)=\int r^5$ 的线性包中。
因此完整 Q4 的自然函数像至少含一个此前纯 $\delta$ 族没有的方向。
这是函数像结论，不是实际三维控制。

## 10. 可用符号与实际范围

还有一个不需求值的真实符号检查。
先取上面的偶母函数，再作足够小的正伸缩
$u_\epsilon(x)=u_0(x/\epsilon)$，把其中心固定在0。
式(36)的最低伸缩项是
$$
-\frac{\epsilon^{-9}M}{160},
$$
其余两项为 $O(\epsilon^{-7})$，故在某个固定有限正 $\epsilon$ 下严格非零。

在同一个状态 $h=1,d=0$、同一个偶 profile 上，
原(1)因 x 反射恰只含
$\gamma\delta^3$ 和 $\gamma^3\delta$ 两个速度单项式。
固定充分小的非零 $\gamma$，取 $\delta=1$ 与 $\delta=-1$，
便得到两个严格相反的自然通量值。
这是真实有限速度方向的符号，不是将一个线性系数的负数自动当作可执行路径。

要把多个 profile 的这些值同时实现为真实闭路成本，
仍需共同有限正核、全部矩阵和 frame 桥、真实非零基准、
原倒行的完整第四传递及有限参数的向量 IFT。
本稿不以(37)替代这些步骤。

本稿完成的是：整个 Q4 的五个速度槽、完整正规势、$N_2$ 校正以及两份有序真尾的准确自然读出。
原 Q2、静态成本、整个 $U$ 的像、同一个固定度量上的联合校正、
全 period、嵌入和厚度均未由(1)自动支付。
