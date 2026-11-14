# R236 附录：迟首二次核与同一个正正规两行湮灭者

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / central_review；AI 辅助：GPT-6 Astra Pro。根全文及原始引理核验，normal_complex 独核同一正态/商关系；首位辅助条件已订正。
状态：以下条件连接完整证明。它没有证明所构造的正正常湮灭者不存在，也没有排除所假设的二次核；普通 Hilbert ISP 仍开。

本稿只处理有界的可和主行。所有算子、商表示及配对均在真实 Haar 模型中定义，不把有限 Boolean 近似当成原核，也不把一般 first 在未知限制上的像声明为稠密。

## 1. 结论与固定记号

沿用
$$
H=L^2(\mathbb Z_2,\mu),\qquad
(Af)(y)=\omega(y)f(y-1),\quad \omega>0\ \text{a.e.},
$$
以及原单射拟幂零 $A$、真空 $\Omega$、反射共轭 $C$ 与
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
B(f,g)=\int f(y)g(-1-y)\,d\mu(y).
\tag{1.1}
$$
A 的谱为零，原 Haar odometer 遍历。
所有 A 的有界交换子对同一个 C 对称。
记
$$
N_j=A^{2^j}/d_j,\qquad
R_j=(I-N_j)(I+N_j)^{-1},\qquad Q_j=R_j-I.
\tag{1.2}
$$
实际事实为
$$
N_j^2=\eta_jN_{j+1},\quad
0<\eta_j\le e^{-770\,16^j},\quad
\|N_j\|\le1,\quad N_j\rightharpoonup I/2.
\tag{1.3}
$$

取
$$
a,c\in\ell^1(\mathbb C),\qquad
j_0=\min\{j:a_j\ne0\},\qquad m_0=2^{j_0},
$$
并假设
$$
c_j=0\quad(0\le j\le j_0).
\tag{1.4}
$$
定义居中的真实有界 first 与辅助行为
$$
X=\sum_j a_jQ_j,\qquad
Y=\sum_j c_jQ_j,\qquad
B_0=\sum_j a_j^2Q_j^2,
$$
$$
T=X^2-B_0+Y.
\tag{1.5}
$$
这里把二阶补项记为 B_0，以免与双线性配对 B 混淆。
全部和在算子范数中绝对收敛，均属于 Acal，字符为零。
局部二阶消去给
$$
B_0\in\mathcal G.
\tag{1.6}
$$
这是[统一近共振稿](R236-appendix-next-order-quadratic-resonance-and-resolvent-criterion.md)
与 R270 局部消去使用的同一个快补项。
本稿不把 Y 自动放入 G。

假设 T 不是零作用。
例如 a 有至少两个非零位置时，T Omega 的二次 Walsh 系数
2 a_i a_j 非零，因此此前提自动成立。
在点态记号
$$
u=\sum_j a_j(\chi_j-1)
$$
下，准确源是
$$
T\Omega
=u^2+\sum_j(2a_j^2+c_j)(\chi_j-1).
\tag{1.7}
$$

**定理 1.1。** 若真实闭核 M=ker T 非零，则存在一个 dyadic 根 zeta、一个真解析芽 h_zeta 及一个非零向量 h，使以下结论同时成立。置
$$
H_\zeta=h_\zeta(A),\qquad h_\zeta(0)=0,\qquad
S_\zeta=X+H_\zeta.
\tag{1.8}
$$
则 S_zeta 是非零实际算子，在全 H 上单射且像稠密。存在闭的完整交换子不变旗
$$
N=\overline{S_\zeta M}\ \varsubsetneqq\ M,
\qquad
0\ne h\in M\ominus N.
\tag{1.9}
$$
同一个正迹类密度
$$
\rho=h\otimes h,\qquad \tau=\|h\|^2>0,\qquad
\varphi_\rho(R)=\langle Rh,h\rangle
\tag{1.10}
$$
满足
$$
\boxed{
\varphi_\rho(S_\zeta R)
=\varphi_\rho(TR)
=\varphi_\rho((Y-B_0+H_\zeta^2)R)=0
\quad(R\in\{A\}').
}
\tag{1.11}
$$
这些是同一个 rho 的三个等式。

更强地，在非零 Hilbert 商 Q=M/N 上有契约表示 pi，且
$$
\boxed{
\pi(S_\zeta)=\pi(T)=0,\qquad
\pi(X)=-\pi(H_\zeta),\qquad
\pi(Y)=\pi(B_0-H_\zeta^2).
}
\tag{1.12}
$$
不把 C 下传到 Q，也不假设 CM=M。

下一各节构造 zeta、H_zeta、N 与 h，并证明全部量词。

## 2. 每个准许 dyadic 差的真实一次因式

令
$$
\Gamma=\bigcup_{J\ge0}\mu_{2^J},\qquad
U_\zeta f=\chi_\zeta f,\qquad
\chi_\zeta(y)=\zeta^{\,y\bmod 2^J}
\quad(\zeta^{2^J}=1).
$$
于是
$$
\gamma_\zeta(A):=U_\zeta A U_\zeta^*=\zeta A.
$$
固定满足
$$
\zeta^{m_0}\ne1
\tag{2.1}
$$
的 zeta，取 J 使 zeta 的阶整除 2^J。对 j>=J，
R_j 在该 gauge 下不变。因此三个差
$$
D_\zeta=\gamma_\zeta(X)-X,\qquad
E_\zeta=\gamma_\zeta(Y)-Y,\qquad
F_\zeta=\gamma_\zeta(B_0)-B_0
\tag{2.2}
$$
都是真正有限和的解析函数 A。

具体地，置标量真解析芽
$$
r_j(z)=\frac{1-z^{2^j}/d_j}{1+z^{2^j}/d_j},
\qquad q_j(z)=r_j(z)-1.
$$
则 D_zeta 的标量芽为
$$
d_\zeta(z)=\sum_{j<J}a_j[q_j(\zeta z)-q_j(z)].
$$
其首项是
$$
-\frac{2a_{j_0}}{d_{j_0}}(\zeta^{m_0}-1)z^{m_0}.
\tag{2.3}
$$
所以
$$
D_\zeta=A^{m_0}U_\zeta^{\rm an},
\tag{2.4}
$$
其中 U_zeta^an 是 Acal 的实际单位，并有真解析逆。
该记号不表示乘法酉算子 U_zeta。

由 (1.4)，E_zeta 的解析阶至少为 2m_0；
若 c 全零则 E_zeta=0。
每项 q_j^2 的阶为 2^{j+1}，故 F_zeta 的阶也至少为 2m_0。
因此
$$
K_\zeta=D_\zeta^2+E_\zeta-F_\zeta
$$
具有至少 2m_0 的解析阶。
标量芽的除法
$$
h_\zeta(z)=
\frac{d_\zeta(z)^2+e_\zeta(z)-f_\zeta(z)}
     {2d_\zeta(z)}
\tag{2.5}
$$
是真正收敛的解析芽，并且
$$
\operatorname{ord}h_\zeta\ge m_0,\qquad h_\zeta(0)=0.
$$
在 A 上求值时，分母的 A^m0 已在标量芽中精确消掉；
没有在 H 上调用 A 的有界逆。

因 A 拟幂零，任何在零点附近收敛的芽都可合法求值于 A。
由全部有界交换因子在全 H 上的展开，
$$
\begin{aligned}
\gamma_\zeta(T)-T
 &=2D_\zeta X+D_\zeta^2+E_\zeta-F_\zeta\\
 &=2D_\zeta(X+H_\zeta).
\end{aligned}
$$
即
$$
\boxed{\gamma_\zeta(T)-T=2D_\zeta S_\zeta.}
\tag{2.6}
$$
本式没有自然域遗漏：本稿 X、T、S_zeta 均全域有界。
H_zeta 属于 G，但 X+H_zeta 在未知限制上的密度仍未被假定。

## 3. 两个真实核之间只付一次左因子密度

令
$$
M_\zeta=U_\zeta M=\ker\gamma_\zeta(T).
$$
对 f in M、g in M_zeta，完整 C 对称配对给
$$
B((\gamma_\zeta(T)-T)f,g)
=B(f,\gamma_\zeta(T)g)-B(Tf,g)=0.
$$
与 (2.6) 合并：
$$
B(D_\zeta S_\zeta M,M_\zeta)=0.
\tag{3.1}
$$

对任何闭 A 不变 M，实际 WOT 单位 (1.3) 直接给
$$
\overline{A^{m_0}M}=M.
\tag{3.2}
$$
确实，当 2^j>=m_0 时，N_jM 包含于 A^m0 M；
闭线性空间的弱闭性和 N_j f 趋弱 f/2 给 (3.2)。
U_zeta^an 及其逆在 Acal 中，均保持 M，故 (2.4) 给
$$
\overline{D_\zeta M}=M.
$$
S_zeta 有界、保持 M，且与 D_zeta 交换。因此
$$
\overline{D_\zeta S_\zeta M}
=\overline{S_\zeta D_\zeta M}
=\overline{S_\zeta M}.
$$
由 (3.1) 得到准确结论
$$
\boxed{B(S_\zeta M,M_\zeta)=0.}
\tag{3.3}
$$

若另有
$$
B(M,M_\zeta)\ne0,
\tag{3.4}
$$
则 (3.3) 迫
N=closure(S_zeta M) 真小于 M。
这里仅删除了真正解析因子 D_zeta；
没有从 S_zeta 在全 H 单射稠密推其在 M 稠密。

## 4. 必有一个非平凡 gauge 产生非零配对

需要同时保证 (2.1)、(3.4) 和 S_zeta 实际非零。

### 4.1 T 的稳定子只有有限多个元素

定义
$$
\Gamma_T=\{\zeta\in\Gamma:\gamma_\zeta(T)=T\}.
$$
这是子群。若它等于全部 Gamma，则 T 与全部 dyadic 字符乘法交换，
从而与完整 L-infinity 乘法 von Neumann 代数交换。
故 T 是某个有界函数的乘法算子 M_t。

T 又与 A 交换，且原权 omega>0 几乎处处，所以
t(y)=t(y-1) 几乎处处。
遍历性迫 t 为常数。T 的字符为零，故 T=0，与前提矛盾。
所以 Gamma_T 是 Prüfer 2 群的真子群，因而有限：
若某子群有无界的 2 阶幂阶数，它已包含每个有限 dyadic 群，便是整个 Gamma。

取一个有限 dyadic 群 G_*，包含 Gamma_T 与 mu_(m0)。
对 zeta 不在 G_*，(2.1) 成立，且
gamma_zeta(T)-T 非零。
由 (2.6)，此时 S_zeta 不是零算子。

### 4.2 每个非零不变空间包含一个全本质支撑向量

这里给出所需 Fourier 步骤的完整证明。
令 M 非零且闭 A 不变。
取 M 中可数稠密的归一向量族 f_n，并令
$$
E=\bigcup_n\{y:f_n(y)\ne0\}.
$$
M 的每个向量均在 E 外为零。
A 不变性及 omega>0 给 E+1 包含于 E（模零集）。
Haar 测度保持迫 E+1=E；遍历性及 M 非零迫 E 几乎处处为全空间。

考虑
$$
g_t=\sum_{n\ge1}2^{-n}t^n f_n,\qquad 0<t<1.
$$
该级数在 H 中绝对收敛，故 g_t 属于 M。
又
$$
\int\sum_n2^{-n}|f_n(y)|\,d\mu(y)<\infty,
$$
所以对几乎每个 y，它定义 t 的解析函数。
由于至少一个 f_n(y) 非零，该函数不恒零，实区间 (0,1) 中的零集测度为零。
Fubini 给某个 t，使
$$
g:=g_t\in M,\qquad g(y)\ne0\quad\text{a.e.}
\tag{4.1}
$$

### 4.3 有限 Fourier 支撑强迫有限维

反设对每个 zeta 不在 G_* 都有 B(M,U_zeta M)=0。
对任意 f,g in M，令
$$
F_{f,g}(y)=f(y)g(-1-y)\in L^1.
$$
由所选字符约定，
$$
B(f,U_\zeta g)
=\zeta^{-1}\int F_{f,g}(y)\overline{\chi_\zeta(y)}\,d\mu(y).
\tag{4.2}
$$
所以 F_(f,g) 的 Fourier 支撑包含于 G_*。
L1 Fourier 唯一性给
$$
F_{f,g}\in
\operatorname{span}\{\chi_\xi:\xi\in G_*\}.
\tag{4.3}
$$
也可先用每一级有限条件期望证明 (4.3)，再取 L1 极限。

固定 (4.1) 的全支撑 g。
映射 f -> f(y)g(-1-y) 是从 M 到 (4.3) 有限维空间的线性单射。
因此
$$
\dim M\le |G_*|<\infty.
$$
但原 A 单射且拟幂零，不允许非零有限维 A 不变空间：
其有限维限制若单射就有非零特征值，与原 A 的谱为零矛盾。

反设不成立。因此存在 zeta 不在 G_* 满足 (3.4)。
此 zeta 同时使 D_zeta 的真解析首项非零、S_zeta 实际非零。
注意这一步只证明存在某个 zeta，未把它指定为 -1。

## 5. 真实有限旗商及同一个正密度

固定第4节得到的 zeta，并置
$$
S=S_\zeta,\qquad H_*=H_\zeta,\qquad
N=\overline{SM}\varsubsetneqq M.
$$
M=ker T 对全部 A' 不变，因为 T 属于 Acal。
S 也属于 Acal，故对每个 R in A'，
$$
RSM=SRM\subset SM.
$$
所以 N 同样对全部 A' 不变。

在 Hilbert 商 Q=M/N 上定义
$$
\pi(R)(f+N)=Rf+N,\qquad R\in A'.
\tag{5.1}
$$
这是全有界的契约、含单位的代数表示：
norm pi(R)<=norm R。
它不是一个星表示，也没有使用 C 的商实现。

S M 包含于 N、T M=0，故
$$
\pi(S)=\pi(T)=0.
$$
由 S=X+H_* 与 T=X^2-B_0+Y，得到
$$
\pi(X)=-\pi(H_*),\qquad
0=\pi(H_*^2-B_0+Y).
\tag{5.2}
$$
即定理 (1.12)。这里只作真实有界算子的有限代数运算。

选任意非零
$$
h\in M\ominus N
$$
并定义 (1.10) 的 rank-one 正迹类密度。
若 pi(W)=0，则 W h 属于 N。
对任意 R in A'，R h 属于 M，且 pi(WR)=0，所以
$$
\varphi_\rho(WR)=\langle WRh,h\rangle=0.
$$
分别取 W=S、T、Y-B_0+H_*^2，便得 (1.11)。

这是同一个 h 和同一个 rho。
未将不同 gauge 产生的密度相加，也没有用 signed 密度代替正性。

### 5.1 first 加解析快项在全 H 单射稠密

对任意 xi in Gamma，
$$
\gamma_\xi(S)-S
=\gamma_\xi(X)-X+\gamma_\xi(H_*)-H_*.
$$
第一项为有限真解析和；后两项也为真解析芽求值。
所以每个 gauge 增量属于 G。

S 实际非零，且字符为零，故非标量。
[R151 定理4.1](R151-quartic-analytic-approximation-gauge-stability.md)
直接给 S 在 H 单射稠密。
也可引用 R152 的有界 first 加 G 结论；无需 R270 中更晚的自然域重证。
这一全空间结论不与 N 真小于 M 冲突。

## 6. 商中允许取消哪些快因子

本节把实际可用的矛盾证书说清。

由 (1.3) 的弱单位，在 Q 中仍有
$$
\pi(N_j)\rightharpoonup I_Q/2.
\tag{6.1}
$$
这由 Q=M orthogonal-minus N 的实现直接验证矩阵元。
若 pi(A^r)v=0，则充分大的 j 有 pi(N_j)v=0，(6.1) 迫 v=0。
同样，pi(N_j)Q 包含于 pi(A^r)Q 的闭包，故
$$
\pi(A^r)\text{ 单射且像稠密}\quad(r\ge1).
\tag{6.2}
$$
因此每个非零真解析芽 f(A)=A^r u(A)，u(0)非零，
都在 Q 中单射稠密：pi(u(A)) 有由 pi(u(A)^-1) 给出的有界逆。

更一般，R151 定理3.1给每个非零 G 元素在每个非零不变 Hilbert 子商中不为零并保精确型；R153 的快分式子商结论给相应单射稠密。
本稿无需将这些性质推广到一般 G[X] 元素。

于是如果能在真实有界代数中产生
$$
0\ne F\in\mathcal G,\qquad
F\in\overline{S A'+T A'}^{\|\cdot\|},
\tag{6.3}
$$
则 pi(F)=0，与 R151 的非零子商结论矛盾。
尤其一个有限、已清分母的证书
$$
F=U S+V T,\qquad U,V\in A',\quad
0\ne F=f(A)
\tag{6.4}
$$
已足够。

对 (6.4) 还可不经过商直接使用正密度。
写 f(A)=A^r u(A)，u(0)非零。对 2^j>=r，令
$$
R_j=u(A)^{-1}A^{2^j-r}/d_j\in A'.
$$
则 F R_j=N_j，(1.11) 迫 phi_rho(N_j)=0；
真实弱极限却给 phi_rho(N_j)->tau/2>0，矛盾。
这里每个 R_j 都是真正有界算子，未要求其范数统一有界。

尚未构造 (6.3) 或 (6.4)。
仅写形式分式、假设 S 在 M 稠密、或在 pi(S)=0 后形式除以 S，都不能替代它。

### 6.1 同一个正常泛函上的整函数精确替换

固定本文已经选出的同一个 $\zeta$、$H=H_\zeta$ 与 $\rho$，
并置
$$
G=B_0-H^2,\qquad S=X+H,\qquad Z=Y-G.
\tag{6.5}
$$
$H,G\in\mathcal G$，且二者常数特征均为零。
这里 $H$ 是真解析芽；$G$ 只使用已证的 $\mathcal G$ 身份，
不假设 $B_0$ 或 $G$ 是一个收敛标量解析芽。

原二次式准确给
$$
T=S(X-H)+Z,\qquad
SA'+TA'=SA'+ZA'.
\tag{6.6}
$$
因此对这个同一个 $\varphi_\rho$，
$\varphi_\rho(SR)=\varphi_\rho(ZR)=0$ 对全部 $R\in A'$ 成立。

对任意两个复变量的整函数 $F(\xi,\upsilon)$，
有实际有界算子恒等式
$$
\boxed{
F(X,Y)-F(-H,G)=S\,U_F+Z\,W_F,
}
\tag{6.7}
$$
其中可以明确取
$$
U_F=\int_0^1
(\partial_1F)(-H+tS,G+tZ)\,dt,\qquad
W_F=\int_0^1
(\partial_2F)(-H+tS,G+tZ)\,dt.
\tag{6.8}
$$
所有参与算子在原有界交换代数中。
整函数双级数在每个有界算子多圆盘绝对收敛，
故沿 $t\in[0,1]$ 可按算子范数微分并积分，得到 (6.7)；
两个积分是真正的 $\mathcal A$ 元素，不是形式分式。

右乘任意实际 $R\in A'$ 后，由 (6.6) 得
$$
\boxed{
\varphi_\rho(F(X,Y)R)
=\varphi_\rho(F(-H,G)R)
\qquad(R\in A').
}
\tag{6.9}
$$
这不更换见证，不跨不同 $\zeta$，也不需要把商上的逆提升为 $M$ 上的逆。

特别，对任意 $z,w\in\mathbb C$，
$$
\boxed{
\varphi_\rho(e^{zX+wY}R)
=\varphi_\rho(e^{-zH+wG}R).
}
\tag{6.10}
$$
若把右过滤看作 $A'$ 的正常泛函，令
$$
\|\psi\|_{(A')_*}
=\sup_{\|R\|\le1,\ R\in A'}|\psi(R)|,
$$
则
$$
\boxed{
\|\varphi_\rho(e^{zX+wY}\,\cdot)\|_{(A')_*}
\le\tau\,\|e^{-zH+wG}\|,
\qquad \tau=\operatorname{Tr}\rho.
}
\tag{6.11}
$$
该上界同时控制所有随 $(z,w)$ 变化的有界右测试；
不只是固定 $R$ 的标量增长界。

### 6.2 已付快型上界及其不能替代的条件

由 [R151 定理3.1](R151-quartic-analytic-approximation-gauge-stability.md)，
每个非零零字符的 $\mathcal G$ 元素均有严格正四次幂型。
因此存在 $c_H,c_G>0$ 与 $M_H,M_G\ge1$，使
$$
\|H^n\|\le M_He^{-c_Hn^4},\qquad
\|G^n\|\le M_Ge^{-c_Gn^4}\qquad(n\ge0).
\tag{6.12}
$$
若某个算子为零，取任意正 $c$ 并把零次幂单独包含在 $M\ge1$ 中即可。
这里没有将 $\mathcal G$ 的范数稠密性当作型控制；
用的是已证的严格正 $\tau_4$。

对固定 $c>0$，Young 不等式给
$$
nL-cn^4
\le C_cL^{4/3}-\frac c2n^4\qquad(n,L\ge0).
$$
故 (6.12) 的实际指数级数满足
$$
\|e^{zH}\|
\le C_H\exp\!\left[C_H(\log(2+|z|))^{4/3}\right],
$$
$G$ 同理。二者交换，因此 (6.11) 推出
$$
\boxed{
\|\varphi_\rho(e^{zX+wY}\,\cdot)\|_{(A')_*}
\le C\tau\exp\!\left[
C(\log(2+|z|+|w|))^{4/3}
\right].
}
\tag{6.13}
$$
常数只依这里固定的 $H,G$，不依参数或右测试。

对整单项式应用 (6.9)，还有
$$
\varphi_\rho(X^pY^qR)=
\varphi_\rho((-H)^pG^qR),
$$
$$
\boxed{
\|\varphi_\rho(X^pY^q\,\cdot)\|_{(A')_*}
\le \tau M_HM_G
e^{-c_Hp^4-c_Gq^4}\qquad(p,q\ge0).
}
\tag{6.14}
$$
这些都是同一准确理想关系的必要后果。

[固定正正常态的实际全右测试增长审计](R230-appendix-fixed-positive-normal-state-and-fast-entire-growth-for-all-commutant-tests.md)
已证明：在 $3/2<\alpha<3$ 的超指数余族中，
另有一个固定正秩一正常态，对两条慢行、局部二阶修正和固定零常数多项式，
也能同时满足有限 $\log^{4/3}$ 增长上界及相应的混合矩快衰减。
该构造没有给出本稿的准确零式。
因此不能仅将 (6.13) 或 (6.14) 与一般正性、正常性相接就宣布矛盾；
仍须使用 (6.6)、真核结构，或构造 (6.3) 的实际非零快证书。
左反射产生的真实源项仍须处理；不同 $\zeta$ 的见证也不能据此合并。

## 7. 首位翻转的精确特例及 a² 尾审计

### 7.1 首位翻转仅是一个有条件分支

令 zeta_0 是一个满足
$$
\zeta_0^{2^{j_0}}=-1,\qquad
\zeta_0^{2^{j_0+1}}=1
$$
的 dyadic 根。
它只改变非零主行的首位 R_(j0)，后续所有 R_j 不变。
c_j 在此前及该位全为零，所以
$$
D_{\zeta_0}=a_{j_0}(R_{j_0}^{-1}-R_{j_0}),
\qquad E_{\zeta_0}=0.
$$
有准确恒等式
$$
D_{\zeta_0}^2-F_{\zeta_0}
=-2a_{j_0}D_{\zeta_0}Q_{j_0}.
$$
因此
$$
\boxed{
H_{\zeta_0}=-a_{j_0}Q_{j_0},\qquad
S_{\zeta_0}=\sum_{j>j_0}a_jQ_j.
}
\tag{7.1}
$$
在 j0=0 时 zeta0=-1。

**只有当**
B(M,U_(zeta0)M) 非零时，
才能按此特定 zeta0 取同一个正密度。
在该分支，第二行进一步精确为
$$
\boxed{
Y-B_0+H_{\zeta_0}^2
=\sum_{j>j_0}c_jQ_j
-\sum_{j>j_0}a_j^2Q_j^2.
}
\tag{7.2}
$$
第4节的存在论证没有保证 zeta0 满足这个额外非零配对。

### 7.2 近共振的 a² 一次项已经抵消

实际恒等式是
$$
Q_j^2=\frac{4N_j^2}{(I+N_j)^2}
=4\eta_jN_{j+1}(I+N_j)^{-2}.
\tag{7.3}
$$
所以 B_0 与 (7.2) 中的 a_j² Q_j² 尾都是既有局部二阶快项。
例如取 $a_j\ge0$、$\kappa>2$，并令 $c_j=a_j^\kappa$ 对 $j>j_0$、$c_j=0$ 对 $j\le j_0$。此时
(5.2) 给的是
$$
\pi\!\left(\sum_{j>j_0} a_j^\kappa Q_j\right)
=\pi(B_0-H_*^2).
\tag{7.4}
$$
其第二慢行是正 $c$ 行；右侧为 $\mathcal G$ 快项。若改写成全部 $j$ 的正 $a_j^\kappa$ 行，右侧须准确加上 $\pi(a_{j_0}^\kappa Q_{j_0})$；这个有限首项也是真解析快项，不能省略。
不能把 (7.4) 重新解释成一个尚未抵消的正 a² 慢行。

若另从普通二次 Bell 源加普通小辅助出发，令其实际实现为
$$
T_{\rm ord}=X^2+G_2+\sum_j d_j'Q_j,
\qquad
G_2=\sum_j a_j^2(I-R_j^2).
$$
则准确有
$$
G_2=-2\sum_j a_j^2Q_j-B_0,
$$
$$
T_{\rm ord}=X^2-B_0+\sum_j(d_j'-2a_j^2)Q_j.
\tag{7.5}
$$
只有这个不同的有效辅助行，才出现正 a² 主尾（乘一个非零标量后）
加更小的 d' 及快误差。
其首位有效系数通常非零，往往已经落在首支撑有序定理；
不能把 (7.5) 的 a² 主尾搬进当前迟首近共振条件 (1.4)。

## 8. 对原正密度矩工具的准确接合

S 是实际 Acal 元素、全 H 单射，且同一个 rho 满足
phi_rho(S A')=0。
因此既有规范头矩构造可以直接用于这一个 rho。
令
$$
v_m(\rho)=
\sum_{F\subset[0,m)}
(-1)^{|F|}
\operatorname{Tr}(\rho V_F^{[m]})\chi_F,
\qquad V_j^{[m]}=R_j^{[m]}.
$$
其准确有限头性质为
$$
\langle Rv_m(\rho),\Omega\rangle=\varphi_\rho(R)
\quad(R\in\mathcal A_m),\qquad
\|\Phi_{v_m(\rho)}|_{\mathcal A_m}\|=\tau.
$$
[实际次数选择器](R230-appendix-actual-cayley-selectors-and-sparse-walsh-escape.md)
及规范正头矩的既有证明给
$$
\|v_m(\rho)\|\longrightarrow\infty.
\tag{8.1}
$$
其理由只需单射 S，不要求 S 是原某个固定的 j^-2 模式。
[所有固定阶实际矩](R230-appendix-all-fixed-order-actual-moment-tensors-and-injective-norm.md)及[正密度小迹尾改进](R230-appendix-positive-density-walsh-truncation-and-small-trace-tail-improvement.md)
因而都能用在这一具体 $\rho$ 上。

额外信息是：这里的 rho 仍同时满足 T 与第二行
Y-B_0+H_*² 的真实湮灭式，而非只有 S 一行。
对这些式在有限头中的变化测试，仍须支付对应实际 carry；
本稿没有把完整实际零式自动搬成每个有限头的零式。

## 9. 当前准确未闭步骤

非零迟首二次核已经被转成一个具体的、非零的正常正 rank-one 密度，
以及一个非零 Hilbert 子商上的两个真实慢行约束。
其中 first 加解析快项在全 H 单射，
但在该未知限制上像不稠密，这是构造本身的结论。

可以继续检查同一正密度的联合矩，
或尝试从两行关系构造 (6.3) 的真实非零快证书。
本稿未完成这两步，也未给一般最小原像的 subquartic 上界。
不从当前连接声称原二次核为空。
