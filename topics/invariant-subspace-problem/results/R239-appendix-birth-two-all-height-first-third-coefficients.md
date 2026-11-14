# R239 附录：出生二全部内部位置的第一、第三中系数严格正性

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文在原五维全逆之后的同一个二维源上，证明二普通权组加一个异常位的出生二四次式中 $P_1,P_3>0$，覆盖全部组大小、全部正权和全部合法内部高度。首末前两边已有完整证明；新的论证支付任意 $n,m\ge3$。同时给出剩余 $P_2$ 的完整 Laurent 化。一般出生二相邻比较尚未完成，第二中系数或完整四次式的正性仍需证明；普通 ISP 仍开放。

入口是[一般高度实际相位与完整四次式](R239-appendix-birth-two-actual-phase-and-common-source-quartic.md)，其中全部矩阵先在真实五维出生层取全逆，再压到固定二维源。配套[自含精确代数证书](../notes/2026-11-14-birth-two-all-height-first-third-coefficients-0c.js)在 BigInt 整式环核本文全部展开和通用四次反射，未从数值样点推断正性。

## 1. 实际参数和两点曲率上界

沿入口记号，普通组大小 $q,L\ge4$，权平方 $z,1$，异常位权平方 $w>0$。整体出生高度 $h=q+L-3$；取尚未支付的位置 $3\le n\le h-3$，记
$$m=h-n,\quad M=m+2,\quad N=n+2,\quad H=M+N.$$
两个组的对称分支已由 Newton 或完整出生一支付，只需入口中的新二维块。$z=1$ 属已证两权模型；$0<z<1$ 交换普通组并整体缩放。因此先取 $z>1$。

入口实际三参数 $u,\eta,\tau>0$ 满足
$$\alpha=N-1-u\eta>0,\quad\beta=M-1-\eta>0,$$
$$J=u(M+1+\eta)-N+1>0,\quad K=N+1-u\beta>0,$$
$$R=\frac N{Mu}-\frac{(N-1)J\tau}{Mu\alpha},\qquad
T=\frac{Mu}N-\frac{(M-1)K}{N\beta\tau},\qquad 0<R,T<1.$$
它们来自同一个原二项式矩族，不是任选的 Hankel 数据。定义
$$F=\eta\phi_0,\qquad G=\eta\phi_1,\qquad \rho=G/F,\qquad \sigma=\tau/u.$$
由 $J+\alpha=u(M+1)$、$K+u\beta=N+1$ 和入口的两个曲率公式直接得到
$$\boxed{F=n(m+1)-(m+2)\alpha R,\qquad
G=m(n+1)-(n+2)\beta T.}\tag{1.1}$$
因此
$$0<F<n(m+1),\qquad0<G<m(n+1).\tag{1.2}$$

置
$$A=1-R\rho,\qquad d=\rho-T.$$
原完整 Pearson 剪切的符号给 $A,d>0$，即
$$T<\rho<1/R.$$
消去两侧外曲率后，规范低范数为
$$(p,Q,r,s)=\left(\frac1{uL},1,\frac u\rho,\frac{u^2}W\right),$$
其中
$$L=1-\frac{n\sigma A}{R(m+1)},\qquad
W=\rho-\frac{md}{\sigma(n+1)T}.$$
实际两权全部出生定理给
$$\boxed{0<R_2=\rho L<1,\qquad0<T_2=W/\rho^2<1.}\tag{1.3}$$
特别 $L,W>0$。两剪切为
$$x^2=\frac{F\sigma A^2}{R^2(m+1)^2},\qquad
y^2=\frac{Fd^2}{\sigma(n+1)^2T^2},\qquad
xy=-\frac{FAd}{R(m+1)(n+1)T}.\tag{1.4}$$
(1.4) 保留实际负交叉项；没有把剪切独立放大或改变源。

## 2. 第一中系数的完整 Laurent 式

令 $P(\omega)=\sum_{i=0}^4P_i\omega^i$ 为入口的完整四次式，规范高范数为
$$(a,b,c,d_*)=(1/(uR),1,u,u^2/T).$$
定义正倍数
$$E=\frac{RTL W\rho^2}{u^2}P_1.$$
直接从完整四次式提取一次项：
$$\boxed{E=T(1-R)(\rho-LW)+(1-RT)(\rho^2-W)
-RTW x^2-Ty^2-2RT\rho xy.}\tag{2.1}$$
代入 (1.4) 得
$$\boxed{E=C_+\sigma+C_0+C_-/\sigma,}\tag{2.2}$$
$$C_+=\frac{T\rho A}{R(m+1)^2}
\{n(m+1)(1-R)-FA\},\tag{2.3}$$
$$C_-=\frac d{(n+1)^2T}
\{m(n+1)(1+T-2RT)-Fd\},\tag{2.4}$$
$$C_0=(1-RT)\rho(\rho-1)+
\frac{Ad}{R(m+1)^2(n+1)}
\{-nm(m+1)(1-R)+FmA+2F\rho R(m+1)\}.\tag{2.5}$$
证书独立核 (2.1) 与原四次一次项相等，再清分母核 (2.2)；不是把同一实现的输出再作数值检查。

全实际域有 $C_->0$。事实上，由 $Fd=G(1-T/\rho)$ 和 (1.2)，花括号严格大于
$$m(n+1)T(1+1/\rho-2R)>m(n+1)T(1-R)>0.\tag{2.6}$$
令
$$\sigma_0=\frac{md}{(n+1)T\rho}.$$
$W>0$ 等价于 $\sigma>\sigma_0$，并有恒等式
$$C_0=(1-RT)\rho(\rho-1)+
\frac{2F\rho Ad}{(m+1)(n+1)}-C_+\sigma_0.\tag{2.7}$$

## 3. 区域一：$\rho\ge1$

此时 $A\le1-R$，由 (1.2) 有 $C_+>0$。将 (2.7) 代入：
$$E=C_+(\sigma-\sigma_0)+(1-RT)\rho(\rho-1)
+\frac{2F\rho Ad}{(m+1)(n+1)}+\frac{C_-}{\sigma}>0.\tag{3.1}$$
各严格条件都由实际范数给出，包含 $\rho=1$。

## 4. 区域二：$C_+\le0$

上一节说明此区域必有 $0<\rho<1$。这里确实需要出生二的实际相位信息，不能只用曲率上界。

### 4.1 从实际相位支付一个定量预算

置 $\delta=Mu-N$。由 (1.1) 和实际 $R,T$ 身份，
$$n(m+1)(1-R)-FA=R(m+1)(K/\tau-\delta).\tag{4.1}$$
因此 $\delta>0$、$\tau\ge K/\delta$。另一方面 $R>0$、$\alpha<N-1$ 给 $\tau<N/J$。因 $J=K+2\delta$，
$$KJ<N\delta,\qquad K^2<\delta(N-2K),\qquad K<N/2.\tag{4.2}$$
实际 $R$ 公式还给
$$1-R>\frac{(\delta+K)^2}{\delta Mu}>\frac1M.\tag{4.3}$$
末一步使用 $\delta+K=1+u+u\eta$ 同时严格大于 $\delta$ 和 $u$。

我们需要的预算是
$$\boxed{\sigma G<(1-R)m^2(m+1)^2.}\tag{4.4}$$
由实际曲率公式，
$$\sigma G=\frac{K(M-1)}u+
\frac{MK-2(H-1)}u\,\tau.\tag{4.5}$$
若第二项的斜率非正，(4.2) 和 $u>N/M$ 给
$\sigma G<M(M-1)/2$。若斜率正，再用 $\tau<N/J$、$K/J<1$，得到
$\sigma G<M(3M-1)/2$。

对 $m\ge4$，写 $v=m-4\ge0$，有完整正多项式
$$2m^2(m+1)^2-M^2(3M-1)
=2v^4+33v^3+189v^2+408v+188>0.$$
结合 (4.3) 即得 (4.4)。

对 $m=3,M=5$，斜率非正时 $\sigma G<10<144/5$。斜率正时，
$K>2N/5$，由 (4.2) 得 $\delta>4N/5$、$u>9N/25$。由 (4.5) 再估计
$$\sigma G<7N/u<175/9<144/5.$$
再用 (4.3)，同样得到 (4.4)。全部 $m\ge3$ 均已支付。

### 4.2 在真实上端点给正分解

记 $\varepsilon=1-\rho>0$。由 $T_2<1$，
$$\sigma<\sigma_*=\frac{m(\rho-T)}
{(n+1)T\rho(1-\rho)}.\tag{4.6}$$
保持其余参数不变时，(2.2) 关于 $\sigma$ 严格递减，因为 $C_+\le0<C_-$。所以只需证明 $E(\sigma_*)>0$。端点仅用于代数比较，不要求它本身是另一个可实现相位，也不要求端点的 $L$ 为正。

置
$$E_0=F-G>0,\quad A_0=F-RG>0,\quad D=G-TF>0.$$
将 (2.2) 代入 (4.6)，乘正因子
$R(1-\rho)m(m+1)^2(n+1)F^2/\rho$，得到分子
$$\begin{aligned}
N_B={}&(1-R)\{RT E_0^2m(m+1)^2(n+1)
+nm^2(m+1)DA_0\}\\
&-D\{m^2A_0^2-2RE_0m(m+1)A_0+RE_0^2(m+1)^2\}.
\end{aligned}\tag{4.7}$$
利用实际 $F=n(m+1)-M\alpha R$，精确整理成
$$\boxed{\begin{aligned}
N_B/R={}&E_0^2\{(1-R)Tm(m+1)^2(n+1)-D\}\\
&+(1-R)DmM(E_0G+m\alpha A_0).
\end{aligned}}\tag{4.8}$$
$W>0$ 给 $D<\sigma(n+1)TG/m$，再用 (4.4)，第一行花括号严格正。第二行同样严格正。因此 $N_B>0$，从而 $E(\sigma)>E(\sigma_*)>0$。

证书分别核一般 $\sigma_*$ 端点桥和 (4.8)，并核支付 (4.4) 的移位多项式。未把某个有负系数的中间展开误当成逐系数正。

## 5. 区域三：$0<\rho<1$ 且 $C_+>0$

这是最后的区域。固定 $R,T,\rho,\sigma,n,m$ 后，(2.1) 关于 $F$ 是仿射函数，且 $L,W$ 不依赖 $F$。置
$$F_{\rm crit}=\frac{n(m+1)(1-R)}A,\qquad
F_{\rm cap}=\frac{m(n+1)}\rho.$$
由当前区域和 (1.2)，
$$0<F<\min(F_{\rm crit},F_{\rm cap}).\tag{5.1}$$
在 $F=0$，(1.3) 给 $LW<\rho$、$W<\rho^2$，所以 (2.1) 严格正。只需证明上端点 $F_*=\min(F_{\rm crit},F_{\rm cap})$ 也正；这些端点只是同一仿射表达式的比较参数，不宣称另有对应二项式族。

### 5.1 $F_{\rm crit}\le F_{\rm cap}$

代入 $F=F_{\rm crit}$ 后 $C_+=0$、$C_->0$，故 $E$ 对 $\sigma$ 递减。仍有 $\sigma<\sigma_*$，而端点的准确值为
$$\boxed{E(\sigma_*)=\rho(1-R)
\left\{\varepsilon T+\frac{nd}{n+1}
\left(2-\frac{\varepsilon(m+1)}{mA}\right)\right\}>0.}\tag{5.2}$$
这里 $A=1-R\rho>\varepsilon$，故括号中的第二因子
$2-\varepsilon(m+1)/(mA)>2-(m+1)/m>0$。于是当前上端点正。

### 5.2 $F_{\rm cap}\le F_{\rm crit}$

在 $F=F_{\rm cap}$ 有 $C_+\ge0$、$C_->0$。又
$\sigma_0<\sigma<\sigma_*$，恒等整理给
$$E=C_+(\sigma-\sigma_0)+
C_-\left(\frac1\sigma-\frac1{\sigma_*}\right)+S,\tag{5.3}$$
$$S=\rho^2\varepsilon(1-R)+d\left\{
\frac{2mA}{m+1}-\varepsilon(1+\rho-R\rho)\right\}.$$
最后的花括号有正分解
$$\boxed{\frac{\varepsilon(m-1)}{m+1}
+\rho(1-R)\left(\frac{2m}{m+1}-\varepsilon\right)>0.}\tag{5.4}$$
因此 $E>0$。等号 $F_{\rm cap}=F_{\rm crit}$ 由任一端点论证覆盖。

由仿射插值，(5.1) 中的实际 $F$ 严格正。三域穷尽实际参数，得到 $P_1>0$。

## 6. 第三系数的实际倒数反射

先不规范 $Q$，对入口的通用四次式作数据反射
$$(a,b,c,d;p,Q,r,s;x,y)\longmapsto
(d,c,b,a;s,r,Q,p;y,x),$$
记得到的多项式为 $P^{\rm rev}$。直接逐项恒等为
$$\boxed{P^{\rm rev}(1/\omega)=\frac rQ\,\omega^{-4}P(\omega).}\tag{6.1}$$
因此 $P_3=(Q/r)P^{\rm rev}_1$。证书在十个独立变量的整式环核全部五个系数，不借相邻正定性的结论倒推系数。

这也是真实模型的反射。[实际 Pearson 与全部剪切消元](R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md) §4 的原坐标补集给
$$a_j(z)=z^q a_{h+1-j}(1/z),\quad
b_j(z)=z^q b_{h-1-j}(1/z),$$
$$k_j(z)=k_{h-j}(1/z),\qquad x_n(z)=y_{h-n}(1/z).$$
故在 $n'=h-n,z'=1/z,w'=1/w$ 上，原高低四元组恰为上述反射数据的同一个正倍数，剪切交换。通用 $P$ 对八个范数总齐次次数为七，故共同倍数仍只带来严格正的整体倍数。规范源合同及异常权的正线性重标也只改变各系数的正倍数；没有使用随高度任意改变的源。

反射家庭仍是已覆盖的二普通组加一个异常位家庭，所以其第一系数严格正。由 (6.1)，原 $P_3>0$。

配合[出生二首末前两边](R239-appendix-birth-two-two-group-singleton-second-and-penultimate-edges.md)，$P_1,P_3>0$ 覆盖全部合法内部位置和全部正权。$P_0,P_4$ 与首主子式已有实际两权严格定理支付。

## 7. 第二中系数：已完成的恒等式与尚未支付的符号

为避免把剩余问题藏在一般矩阵记号中，给出其完整 Laurent 式。置 $\lambda=1/\rho$，并记
$$\xi=\frac{\lambda-R}{R(m+1)\lambda}=\frac A{R(m+1)},\qquad
\upsilon=\frac{1-T\lambda}{(n+1)T\lambda}=\frac d{(n+1)T}.$$
于是
$$R_2=\lambda^{-1}-n\xi\sigma/\lambda,\quad
T_2=\lambda-m\lambda^2\upsilon/\sigma,$$
$$x^2=F\sigma\xi^2,\quad y^2=F\upsilon^2/\sigma,\quad xy=-F\xi\upsilon.$$
取正倍数
$$E_2=\frac{RR_2TT_2}{u^3\lambda^2}P_2.$$
完整四次式直接给
$$\begin{aligned}
E_2={}&\lambda T(1-R)(1-R_2)+(1-RT)(1-R_2T_2)
+(R/\lambda)(1-T)(1-T_2)\\
&-R(T+T_2/\lambda)x^2
-T\lambda(R+\lambda R_2)y^2
-2RT(1+\lambda)xy-RT\lambda x^2y^2 .
\end{aligned}\tag{7.1}$$
保留最后的四次剪切费用后，
$$E_2=K_+\sigma+K_0+K_-/\sigma,\tag{7.2}$$
$$K_+=n\xi(1+T-2RT)-R(1+T)F\xi^2,$$
$$K_-=m\lambda\upsilon(1+R-2RT)
-T\lambda(1+R)F\upsilon^2,$$
$$\begin{aligned}
K_0={}&(\lambda-1)\{T(1-R)-R(1-T)/\lambda\}
-mn\lambda(1-RT)\xi\upsilon\\
&+Rm\lambda F\xi^2\upsilon+Tn\lambda F\xi\upsilon^2
+2RT(1+\lambda)F\xi\upsilon-RT\lambda F^2\xi^2\upsilon^2.
\end{aligned}$$
证书独立核 (7.1) 与通用四次的第二系数相等，再核 (7.2)。固定其他参数时，$E_2$ 是 $F$ 的严格凹二次式，不能仿照第一系数丢掉负二次项。

由 (1.2)，$\rho\ge1$ 时 $K_+>0$，$\rho\le1$ 时 $K_->0$；另外 $K_+\le0$ 必推出本文 $C_+<0$，因为其相关花括号满足
$$n(m+1)(1+T-2RT)-FA(1+T)
=(1+T)\{n(m+1)(1-R)-FA\}+n(m+1)R(1-T).$$
这些是后续可以继续使用的已证输入，尚未给出 $E_2>0$。当前只剩 $P_2$ 的全域符号，或无需逐系数正的完整 $P(\omega)>0$ 论证；不能因此宣布整个出生二或 ISP 完成。

## 8. 核验与恢复说明

精确证书使用 BigInt 系数稀疏整式环。非负指数编码逐乘检查每位次数小于基数，并检查编码整数安全范围；独立四次桥使用有符号指数元组键，避免编码碰撞。它核通用 $P_1,P_2$ 身份、一般上端点、实际相位后的正分解、两个仿射上端点、全部高度的常数多项式以及完整反射五个系数。根代理已逐项审读全部不等式，并在可用 JavaScript 运行时执行证书，全部通过。终端当前失联，未声称另一次终端重跑。

以上证书承担有限整式身份核验；实际域、严格不等式与原五维同源入口的证明分别见正文和所引完整稿。没有自由相位取样、普通数值近似或改变 MP 度量。
