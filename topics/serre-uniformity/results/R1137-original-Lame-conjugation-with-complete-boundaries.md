# R1137：原 Lamé 共轭的全部有限边界与指定源方程

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纯纸面。** 本文给原相对 Fourier--Mukai 变换下的压缩微分、
乘法 $U$、Lax 算子 $B$ 及指定一阶源 $C=UD+V$ 的完整共轭，
保留最高极、最低极和常数的全部有限边界。
指定 $\phi=\Phi(U^m)$ 满足下面 (T41) 的非齐次三阶降阶恒等式。
降阶算子 $\Lambda$ 作用于原纯极基，尚不是目标局部的低阶微分算子；
本结果没有证明 $e,K_4$ 非同时零。

## 0. 原对象与已付纯极对调

固定
$$
p=6k-1\ge41,\quad m=(p-1)/2,\quad N=k-1,\quad
E:V^2=U^3+v^2,\quad v^2=-108,\quad Q=(0,v),
$$
$$
\omega=dU/(2V),\quad DU=2V,\quad DV=3U^2,\quad
D\mathcal R=\Psi,\quad D\Psi=\delta\ne0,\quad
\Psi^2=U^p+2\delta\mathcal R .
$$
$\Phi:V_0=L((p-1)O)\to V_0$ 为
[R1061](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)
的相对、底域线性变换；其实际 Miller 核为 $K(T,R)$。
[R1095](R1095-original-theta-kernel-dual-Psi-normalization.md)
给 $H=L((p+1)O)$ 上的完整延拓 $\mathscr F=J^\#A$，
$\mathscr F\Psi=0$，并保留第三类项后定义正规常数读数。

[原短旗标笔记 §10](../notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)
已用同一 sigma 核支付以下全部式子。以原安全 additive 参数 $t$ 写
$$
U(t)=t^{-2}+\sum_{d\ge4}(d-1)G_dt^{d-2},\qquad
G_d=0\quad(d\not\equiv0\pmod6),
$$
$$
q_r=\frac{(-1)^r}{(r-1)!}D^{r-2}U-(-1)^rG_r
=t^{-r}+O(t)\quad(2\le r\le p-1).
$$
于是 $1,q_2,\ldots,q_{p-1}$ 是 $V_0$ 的原纯极基，且
$$
\Phi(q_r)=a_rq_{p+1-r}-G_r,\qquad
a_r=(-1)^r(p-r)!\delta^{r-1},\qquad
\Phi(1)=1,\quad \Phi^2=[-1]^*.
$$
特别 $G_{p-1}=0$ 是原 CM 角色给的精确零。
若 $c_s=[t^{6s+1}]U(t)^{-1/2}$，则
$$
U^m=\sum_{s=0}^{N}c_s q_{p-1-6s},\qquad c_0=1.
$$
所有非零极坐标的 $r$ 都为 $4\bmod6$。
下文沿用前述笔记的 T 编号，供相同源的后继直接引用。



## 1. 原纯极基的压缩微分、全部端点与指定源的三阶降阶关系

本节始终使用 (T28) 的相对、底域线性的原变换。等价地，先在原
$\mathbf F_p$ 模型上取其矩阵，再作底域扩张；这里不把绝对 Cartier
的半线性误写成底域线性。记 $\mathscr F=J^\#A$ 为 R1095 已付的
$H=L((p+1)O)$ 上完整延拓，故 $\mathscr F|_{V_0}=\Phi$、
$\mathscr F\Psi=0$。所有正规读数均在保留完整第三类项后才于 $Z=O$ 取常数。

### 1.1. 压缩微分与两个端点

沿用 §10 的纯极基，定义线性泛函
$$
g=\ell_0(g)+\sum_{r=2}^{p-1}\ell_r(g)q_r,\qquad g\in V_0.
$$
其中 $\ell_r(g)=[t^{-r}]g$，而 $\ell_0$ 是该基的常数坐标。
由 $q_r$ 的定义直接有
$$
Dq_r=-r q_{r+1}-rG_{r+1}\quad(2\le r\le p-2),
\qquad Dq_{p-1}=\Psi.
$$
非零 $G_{r+1}$ 只出现在偶数 $r+1$，故第一式没有另一个奇偶号。
置
$$
D_0g=Dg-\ell_{p-1}(g)\Psi,
\qquad
\Lambda1=\Lambda q_2=0,\quad
\Lambda q_r=-\delta q_{r-1}\ (3\le r\le p-1).
$$
这是两个真正的 $V_0$ 端同态。由 (T30) 的
$r a_{r+1}=\delta a_r$，全部常数恰相消，得到
$$
\boxed{\quad
\Lambda=\Phi D_0\Phi^{-1},\qquad
D\Phi^{-1}g=\Phi^{-1}\Lambda g+\delta\ell_2(g)\Psi .
\quad}
\tag{T33}
$$
第二式的末项不能丢：$\Phi^{-1}q_2=\delta q_{p-1}$，其导数恰为
$\delta\Psi$。在另一个端点，$D_0q_{p-1}=0$ 正与
$\Lambda\Phi q_{p-1}=\delta^{-1}\Lambda q_2=0$ 相合。

令 $\ell_G(1)=0$、$\ell_G(q_r)=(r-1)G_r$。在全部原基上逐项计算得
$$
\boxed{\quad
[D_0,\Lambda]=-\delta I+
 \delta\,1\otimes(\ell_0+\ell_G)
 -\delta q_2\otimes\ell_2
 -\delta q_{p-1}\otimes\ell_{p-1}.
\quad}
\tag{T34}
$$
对 $3\le r\le p-2$，右边是
$-\delta q_r+\delta(r-1)G_r$；在 $r=2,p-1$ 两端均为
$-2\delta q_r$；在 $1$ 上为零。这也独立核准了有限维交换子的零迹。
因此不能只保中间的 $-\delta I$，将 $\Lambda$ 当作某个局部坐标的乘法算子。
$D_0,\Lambda$ 的 Jordan 型虽均为 $(p-2,1)$，这本身不对指定两个读数给非零结论。

### 1.2. 第四阶 Picard 读数的真实共振常数

记 $f=U^m$、$\phi=\Phi f$。由 (T31) 的原纯极展开，
$\ell_{p-1}(f)=c_0=1$，而 $f$ 的其余非零极坐标均满足
$r\equiv4\pmod6$。特别
$$
\ell_2(\phi)=\delta^{-1},\qquad \ell_3(\phi)=0.
$$
用 $\Phi^2=[-1]^*$、(T33) 及 $D\Psi=\delta$，逐次得到
$$
\begin{aligned}
D\phi&=-\Phi\Lambda f,\\
D^2\phi&=\Phi\Lambda^2f,\\
D^3\phi&=-\Phi\Lambda^3f+\delta^3c_N\Psi,\\
D^4\phi&=\Phi\Lambda^4f+\delta^4c_N.
\end{aligned}
\tag{T35}
$$
第三行的项来自 $\Lambda^2 f$ 的 $q_2$ 坐标
$\delta^2c_N$，不是任意选择 primitive 的常数。
因此原两个指定读数也可完整写成
$$
\boxed{\quad
e=-\Phi(\Lambda f)(-Q),\qquad
16ve+4\delta^2K_4
 =\Phi(\Lambda^4f)(-Q)+\delta^4c_N .
\quad}
\tag{T36}
$$
(T32) 的最后一项正给同一常数：
$6N+4=p-1$、$D^{p-1}U=\delta$，
且 $\delta^{-6N}=\delta^4$。

此处的 $c_N$ 没有已证单位断言。为明确它与已付 Hurwitz 单位的区别，
可在同一 $O$ 处令 $y=U^{-1/2}$，
$$
t=y\,F(v^2y^6),\qquad
F(z)={}_2F_1(1/6,1/2;7/6;-z).
$$
因为 $p-4=6N+1$，Lagrange 反演在安全次数 $N<p$ 给
$$
\boxed{\quad
c_N=-\frac{(v^2)^N}{4}[z^N]F(z)^4 .
\quad}
\tag{T37}
$$
原式先为 $(v^2)^N(p-4)^{-1}[z^N]F^{-(p-4)}$；
在所用次数 $N$ 的截断环内，$F^{-p}=1$，所以本次确可只保 $F^4$。
所需 $F$ 系数的分母 $6i+1$ 至多 $p-4$，均为单位。
已付 $G_{p-5}$ 的式子则读同一 $F^7$，不能把它的单位结论搬到 (T37)。

### 1.3. 乘法和 Lax 算子的完整变换

对一般 $f\in V_0$，仍写 $\phi=\Phi f$。
从纯极基两端直接得
$$
\mathscr F(Df)=\Lambda\phi,\qquad
\mathscr F(D^2f)=\Lambda^2\phi+\delta^2\ell_2(\phi),\qquad
\mathscr F(D^3f)=\Lambda^3\phi-\delta^3\ell_3(\phi).
\tag{T38}
$$
第二式使用 $D^2q_{p-1}=\delta$；
第三式使用 $D^3q_{p-2}=2\delta$ 以及
$\ell_3(\Phi f)=-2\delta^{-2}\ell_{p-2}(f)$。
这几个输入均在 $H$ 内，但一般不都在 $V_0$ 内。

令 $A=-FR$、$a=U(R)^p$、$b=V(R)^p$、$c=\Psi(R)$，
并记 $h=h_A(T)$。原核给
$$
D_T\log K=c+h,\qquad D_Th+h^2=2U(T)+a.
$$
对完整相对 Cartier 分部积分，
$C_T(hfK\omega)=-C_T((Df)K\omega)-cC_T(fK\omega)$。
原 Lamé 式因此给
$$
\boxed{\quad
\mathscr F(Uf)
 =\frac12\Lambda^2\phi+\Psi\Lambda\phi
  +\delta\mathcal R\,\phi+\frac{\delta^2}{2}\ell_2(\phi).
\quad}
\tag{T39}
$$
不能把左边写成未定义的 $V_0$ 内乘法共轭。
其完整第三类项亦相容：
$D^2f-2Uf$ 的系数为
$-2\Psi\ell_{p-1}(f)$，正与右边
$-2\Psi C_T((Df)K\omega)$ 的该项相同。

再用原 $B=D^3-3UD-3V$，其形式伴随为 $B^*=-B$。
由上述 Riccati 式直接展开得
$$
\frac{B_TK}{K}
 =c^3+3ca+b+3cU(T)+3c^2h.
$$
这里 $b$ 的号为正，因为 $(a-U)h+V=b$。
令原
$$
n_0=\Phi(V)=\frac{V^p+U^p\Psi-\delta\mathcal R\Psi}{3}.
$$
分部积分后先消去 $\mathscr F(Df)$，再使用 (T38)，得到
$$
\mathscr F(Bf)
 =-\frac32\Psi\Lambda^2\phi
  -3n_0\phi-\frac32\delta^2\Psi\,\ell_2(\phi).
$$
记 $C=UD+V=(D^3-B)/3$，遂有
$$
\boxed{\quad
\mathscr F(Cf)=
 \left(\frac{\Lambda^3}{3}+\frac{\Psi\Lambda^2}{2}+n_0\right)\phi
 +\frac{\delta^2\Psi}{2}\ell_2(\phi)
 -\frac{\delta^3}{3}\ell_3(\phi).
\quad}
\tag{T40}
$$
$C$ 确实把 $V_0$ 送入 $H$：一般极阶最多增加三，
而最高 $q_{p-1}$ 的潜在 $p+2$ 阶系数是 $-p=0$。
$UDf$ 与 $Vf$ 单独可能越出 $H$，本证明没有分开给它们一个未付的延拓。

指定原源满足
$Cf=(2m+1)VU^m=0$。于是 (T40) 给
$$
\boxed{\quad
2\Lambda^3\phi+3\Psi\Lambda^2\phi+6n_0\phi+3\delta\Psi=0,
\qquad \phi=\Phi(U^m).
\quad}
\tag{T41}
$$
末项由 $\ell_2(\phi)=\delta^{-1}$ 强迫，不能删为齐次关系。
(T41) 是这个原源的真实有限降阶方程；
$\Lambda$ 是 (T33) 的纯极基算子，尚未识别为目标局部的低阶微分算子。
R1134 的四个有限 Euler 矩阵满秩不否定此式，
本式也不反过来排除 $e=K_4=0$。

### 1.4. 原 Hermite 源中对数导数看不见的移动极

同一原核还给一个必须保留的除子信息。
在一般 $R$ 上，令 $P_R$ 为满足 $FP_R=R$ 的几何点，$A=-FR$，则
$$
\operatorname{div}_T(U(T)^mK(T,R))
 =(A)+m(Q)+m(-Q)-p(P_R).
\tag{T42}
$$
$O$ 处的 $p-1$ 阶零和极已精确相消。
若记 $G=U^mK$，原一阶源方程等价为
$$
\boxed{\quad
U(U-a)D_TG=
 \bigl(cU(U-a)+aV-bU\bigr)G .
\quad}
\tag{T43}
$$
因为 $2m=-1$，左边的对数导数为
$c+h_A-V/U=c+(aV-bU)/(U(U-a))$。
但是特征 $p$ 的对数导数看不见 (T42) 的移动 $p$ 重极，
所以不能仅按 (T43) 的三个可见有限极，便断言已得到一个固定秩的目标
Gauss--Manin 系统。对 $R=-Q$ 的碰撞也须先合并整个除子再专化；
此时原源是 $F_Q$，而不是把一般点的各项独立代入。

来源与审计：本节只消费 §10 的原相对变换、R1061/R1095 的完整
Miller 与第三类正规读数，以及 R1113 的实际 Lax 算子。
o2_high_coefficient 已独立纸核 (T38)--(T41) 的原核展开、分部积分、
两个端点常数及指定源的末项；root 已逐式核准本结果全部纯极端点、Lagrange 范围、B/C 核展开、相对第三类项与移动 p 极；o2_high_coefficient 亦完成候选全文核对。
没有数学程序执行，未把任何新等价式称为指定两 jet 的非零证明。


## 2. 移动 p 重极给出的原 Gauss--Padé 接口

本节继续使用同一个 $\Phi$、$K$ 和指定 $f=U^m$。
所得 Padé 对不是另选的形式近似：其两个多项式均是原变换的实际输出。
所有 Cartier 均为相对、底域线性的版本；尤其下式的 $v$ 不取额外的 $p$ 次根。

### 2.1. 一个在原碰撞点仍整的差商

仍记
$$
a=U(R)^p,\quad b=V(R)^p,\quad A=-FR,\quad
G(T,R)=U(T)^mK(T,R),\quad W=-Q.
$$
因 $v^p=-v$，在目标 $R=-Q$ 处恰有 $a=0,b=v,A=W$。
原 chord 是
$$
h_A(T)=\frac{V(T)-b}{U(T)-a},\qquad
h_W(T)=\frac{V(T)-v}{U(T)}.
$$
利用 $b^2-v^2=a^3$，将下式中表面的 $1/a$ 完整消去：
$$
\boxed{\quad
q_A(T):=\frac{h_A(T)-h_W(T)}a
=\frac{V(T)-v-a^2U(T)/(b+v)}
       {U(T)(U(T)-a)} .
\quad}
\tag{T44}
$$
$b+v$ 在 $R=-Q$ 为 $2v$，因此这是真正的整参数表达。
专化后
$$
q_W(T)=\frac{V(T)-v}{U(T)^2}.
$$
这里在 $W$ 的两条简单极合并为二阶极，不能分别丢弃其中一条。

记
$$
\phi=\Phi(U^m),\qquad \phi_-=\Phi(U^{m-1}).
$$
由 (T43) 的准确对数导数与
$h_A=h_W+a q_A$，有
$$
D_TG=(\Psi(R)+a q_A-v/U(T))G.
$$
相对 Cartier 杀掉这个 exact differential，故
$$
\boxed{\quad
v\phi_-(R)-\Psi(R)\phi(R)=U(R)^p\,\chi(R),\qquad
\chi(R)\omega_Z=
C_{T,\mathrm{rel}}\!\left(G(T,R)q_A(T)\omega_T\right).
\quad}
\tag{T45}
$$

必须先核右边的极界。在一般 $R$，$q_A$ 在 $A,W$ 至多简单极，
其 $O$ 处的 chord 主部已经相消；(T42) 中 $G$ 的零分别将它们抵消。
显示分母 $U-a$ 的另一点由分子抵消，$U=0$ 的两点也由 $U^m$ 抵消。
于是输入微分仅在 $P_R$ 有至多 $p$ 阶极。
它只有一个极，留数为零；相对 Cartier 的输出至多有一个简单极，
该极的留数又为零，所以输出全纯，确为 (T45) 的标量。

此外，$q_A$ 的显示式和原核在 $R=-Q$、源 $O$ 的形式邻域内均整。
在源 $O$ 处，$G=1+O(t_O)$，$q_A=O(t_O)$。
读取该处 Cartier 输出的常数只用一个有限 Taylor 系数，
其系数对目标 $R$ 仍整。因此 $\chi$ 在 $R=-Q$ 正则。
这一步证明的是整个参数族的整性，不只是专化后另算出一个有限值。

### 2.2. contact 的首余项是已经付清的原单位

在 $R=-Q$，原 $G$ 恰为 $F_Q=U^mg_Q$。
置
$$
d_0=\frac{C_{\mathrm{rel}}(UF_Q\omega)}{\omega'}
=(2v)^{2k}\binom{3k-1}{2k}\ne0.
$$
这是原 normal 列的中列单位，也可不经变分直接核：
$$
UF_Q\omega=
\left(\frac1{3U^2}\right)^p
 (V-v)^{3k-1}(V+v)^{5k-1}\,dV.
$$
分子次数 $8k-2<2p-1$，只读 $V^{p-1}$。
反转总次数后，所需系数变成
$$
v^{2k}[z^{2k}](1-z)^{3k-1}(1+z)^{5k-1}
=(2v)^{2k}\binom{3k-1}{2k}.
$$
最后一步在次数 $2k<p$ 内使用 $(1+z)^p=1$；
等价地展开 $(1+z)^{2k-1}((1-z)/(1+z))^{3k-1}$。
二项式上、下阶都小于 $p$。

为核全部符号，直接对原有理函数作两次 exact reduction：
$$
D(F_Q/U)=-(2V+v)F_Q/U^2,
$$
$$
D(VF_Q/U)=UF_Q-(2v^2+vV)F_Q/U^2.
$$
相对 Cartier 后得到
$$
C_{\mathrm{rel}}(VF_Q\omega/U^2)
=-\frac v2 C_{\mathrm{rel}}(F_Q\omega/U^2),
$$
$$
d_0=\frac{3v^2}{2}\,
 \frac{C_{\mathrm{rel}}(F_Q\omega/U^2)}{\omega'}.
$$
因此 (T45) 的碰撞值为
$$
\boxed{\quad
\chi(-Q)=-\frac{3v}{2}\phi_{m-2}(-Q)
=-\frac{d_0}{v}\ne0,\qquad
\phi_{m-2}=\Phi(U^{m-2}).
\quad}
\tag{T46}
$$
这里只消费已付的 normal 旁列单位来确定误差首项，
没有把它认成原 $e$ 或 $K_4$。

### 2.3. 两个实际输出与精确 Padé 变量

由原纯极基的 CM 角色和 $\Phi$ 对调，
$$
\phi(R)=U(R)H(X),\qquad
\phi_-(R)=U(R)^2J(X),\qquad X=U(R)^3,
$$
$$
\deg H,\deg J\le N,\qquad N=k-1.
$$
具体地，$U^m$ 的纯极索引为 $4\bmod6$，
其像的索引为 $2\bmod6$；
$U^{m-1}$ 的索引为 $2\bmod6$，其像的索引为 $4\bmod6$。
这些给上述 degree 上界，不预先声称最高系数非零。

写原 $\Psi=VU\,S(U^3)$，其中
$$
S(X)=\sum_{j=0}^{N}a_jX^j,\qquad
a_0=\frac{\delta}{2v^2}\ne0,\qquad
\frac{a_j}{a_{j-1}}=-\frac{6j-1}{v^2(6j+2)}.
$$
在 $R=-Q$ 的局部环，
$V(R)=-v\sqrt{1+X/v^2}$，平方根常数为 $1$。
(T45) 除以 $vU^2$ 给准确的高接触式
$$
J(X)+\sqrt{1+X/v^2}\,S(X)H(X)
=X^{2N+1}\frac{\chi(R)}v.
\tag{T47}
$$
因为 $p-2=3(2N+1)$，右边的指数没有舍入误差。
左边只含 $X$，故这里 $\chi$ 的该局部展开也只含 $X$。

现在固定
$$
x=-X/v^2,\qquad
\mathsf Q(x)=H(-v^2x),\qquad
\mathsf P(x)=-J(-v^2x)/a_0.
$$
定义实际代数形式级数
$$
F(x)=\sqrt{1-x}\,\frac{S(-v^2x)}{a_0}.
$$
原 $S$ 递推直接给
$$
6x(1-x)\frac{d}{dx}S(-v^2x)
 +(2-5x)S(-v^2x)=2a_0,
$$
从而
$$
3xF'(x)+F(x)=(1-x)^{-1/2},\qquad F(0)=1.
$$
在本文所用的全部安全次数，精确地
$$
\frac{S(-v^2x)}{a_0}
={}_2F_1(1,5/6;4/3;x),\qquad
F(x)={}_2F_1(1/3,1/2;4/3;x)
=\sum_j\frac{(1/2)_j}{j!(3j+1)}x^j.
$$
第一式在模 $p$ 中因 $5/6=-N$ 终止于 $N$。
Gauss 分母 $4/3$ 的首共振在 $j=4N+3$，
而本次最高读数仅为 $2N+1$。
在首共振以后，本文仍以显示的平方根乘多项式定义 $F$，
不冒称已约化整条 characteristic-zero 超几何级数。

于是
$$
\boxed{\quad
\mathsf QF-\mathsf P
=\varepsilon_0 x^{2N+1}+O(x^{2N+2}),\qquad
\varepsilon_0
=-\frac{d_0(-v^2)^{2N+1}}{a_0v^2}\ne0,
\quad \deg\mathsf P,\deg\mathsf Q\le N.
\quad}
\tag{T48}
$$
特别 contact 恰为 $2N+1$，不只是一个下界。
$\mathsf Q\ne0$ 由原 $\Phi$ 可逆及 $U^m\ne0$ 保证。
所有式子来自同一个原核；没有重新选择一个方便的 Padé 解。

### 2.4. 原双零对应的准确缺陷

R1061 的原四阶 Picard 计算给
$$
H(0)=-\frac{e}{2v},\qquad
H'(0)=\frac{10ve+\delta^2K_4}{96v^4}.
$$
由于 $F(x)=1+x/8+O(x^2)$，(T48) 因而给
$$
\boxed{\begin{aligned}
\mathsf Q(0)=\mathsf P(0)&=-\frac{e}{2v},\\
[x]\mathsf Q&=-\frac{10ve+\delta^2K_4}{96v^2},\\
[x]\mathsf P&=[x]\mathsf Q+\mathsf Q(0)/8.
\end{aligned}}
\tag{T49}
$$
因此原 $e=K_4=0$ 等价于 $\mathsf Q$ 的前两个系数全零；
此时 $\mathsf P$ 也有同一个 $x^2$ 因子。约去这两个因子后，
原实际多项式对满足
$$
\deg\widetilde{\mathsf P},\deg\widetilde{\mathsf Q}\le N-2,\qquad
\widetilde{\mathsf Q}F-\widetilde{\mathsf P}
=\varepsilon_0x^{2N-1}+O(x^{2N}),\qquad
\widetilde{\mathsf Q}\ne0 .
$$
本节尚未排除这种特定退化。一般 characteristic-zero Padé 正常性、
实积分的正性、以及上面首余项为单位，都不能单独排除它。
尤其 $\sqrt{1-x}$ 是实际 $V/v$ 的一部分，不能删除后
套用上参数为 $1$ 的另一条 Jacobi Padé 公式。

来源与审计：原核与第三类框架来自 R1061、R1095；
本节先用 (T42)--(T43) 保留移动 $p$ 重极，再完成相对 Cartier 的全极界。
o2_high_coefficient 已独立纸核 (T44)--(T45) 的整差商、
唯一源极与 Cartier 全纯性、碰撞处整性及 (T47)--(T49) 的
原 Gauss 参数、degree 和缺陷含义。
没有数学程序执行；指定非同时零仍为后继目标。
