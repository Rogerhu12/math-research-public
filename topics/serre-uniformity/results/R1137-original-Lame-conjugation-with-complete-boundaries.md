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
