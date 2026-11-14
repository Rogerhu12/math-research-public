# R239 附录：两普通权组加一异常位的全部出生、全部高度严格 Gram 比较

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

**状态：完整有限模型定理。** 本文关闭两个任意大小的等权组加一个独立正权位的整个模型：全部物理出生、全部组内重数、每个合法相邻高度均有严格系数一比较。新输入是同一个三矩形族的跨出生曲率约束，它支付一般第一系数的坏符号区域；第二系数由已证凹曲率两端点及这里补齐的硬边完成。

[完整精确证书](../notes/2026-11-14-all-birth-two-groups-singleton-hard-edges-and-cross-birth-0c.js)核十三组通用代数身份。本文不解决普通 ISP，不外推更多独立权组或原无限尾的混合 Gram 费用。

## 1. 全物理定理及真正分支

设有限 Boolean 删除算子 $D$ 的权分成两个普通组和一个异常位。组大小 $Q_1,Q_2\ge0$，全部权严格正。整体缩放后，普通组权为 $\sqrt z,1$，异常位权为 $\sqrt w$，$z,w>0$。总位数 $N=Q_1+Q_2+1$。

对每个合法物理出生 $s$，令
$$K_s=\ker D\cap\mathcal H_s,\qquad h=N-2s,$$
$$F_j^{(s)}=\left.\frac{D^j(D^*)^j}{(j!)^2}\right|_{\mathcal H_s},
\qquad
\Gamma_j^{(s)}=P_{K_s}(F_j^{(s)})^{-1}|_{K_s}.
$$
所有逆先在整个原物理层上取。整层满射性保证 $0\le j\le h$ 的逆合法。

**定理。** 对全部 $1\le n<h$，
$$\boxed{\Gamma_n^{(s)}(\Gamma_{n+1}^{(s)})^{-1}\Gamma_n^{(s)}
\prec\Gamma_{n-1}^{(s)}\quad\text{在整个 }K_s\text{ 上}.}\tag{1.1}$$
无合法内部高度或零空间的情形按空陈述处理。

[一般出生互补 Hankel 与完整源](R239-appendix-general-birth-dual-hankel-and-birth-two-full-source.md) §1 给原正交串分解。组内出生 $(i,j)$ 产生残余长度
$$q=Q_1-2i,\quad L=Q_2-2j,\quad t=s-i-j,$$
且 $q+L+1-2t=h$，所有分支高度相同，重数
$$\left[\binom{Q_1}i-\binom{Q_1}{i-1}\right]
\left[\binom{Q_2}j-\binom{Q_2}{j-1}\right]$$
全部保留。这些串同时约化 $D,D^*$、层 Gram、全逆和 primitive 压缩。

交换普通组后可先取 $q\le L$。相对出生 $t=0$ 为真空一维，$1\le t\le q$ 为二维，$L\ge q+1$ 时 $t=q+1$ 为饱和一维，其余低半层出生为空。$q=0$ 退化为两权模型。二维块的原出生层为 $(2t+1)$ 维，仍先全逆再压到同一个二维源。完整源公式也适用于无次序的 $t\le\min(q,L)$，故后续交换权组合法。

$t=0$ 的严格 Newton、$t=1$ 的[整个出生一](R239-appendix-birth-one-two-group-singleton-all-heights-strict-bound.md)均已付。饱和 $t=q+1$ 取 $q+1$ 个独立头位加等权池，直接由[真实饱和固定线](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md) §8.8 得
$$\gamma_n^2<\frac{q+1+n}{q+2+n}\gamma_{n-1}\gamma_{n+1}.$$
该稿证明了完整 Hilbert 最小解和全核正交，不是试探上界。更强[双侧饱和常数](R239-appendix-saturated-primitive-two-sided-weight-count-constants.md)同样严格小于一。因此只需处理 $t\ge2$ 的二维块。

## 2. 真实三矩形与同一个源的规范

固定 $t\ge2$、$t\le\min(q,L)$，$h=q+L+1-2t$。$z=1$ 归入已证两权模型；$z<1$ 交换普通组并整体缩放。因此以下取 $z>1$。

原高低首一范数为 $a_j,b_{j-1}$，原剪切为 $k_j$。完整 MP Gram 是
$$H_j=\begin{pmatrix}
a_j+wa_{j+1}+B_jk_j^2&-B_jk_j\\
-B_jk_j&B_j
\end{pmatrix},
\quad b_{\,\mathrm{high},j}=a_{j+1},\quad
B_j=\frac{wb_{j-1}b_j}{b_{j-1}+wb_j}.
\tag{2.1}$$
两个硬端准确为 $B_0=wb_0$、$B_h=b_{h-1}$。

令 $\Theta=z\partial_z$、$\kappa=z/(z-1)^2$，以及
$$\gamma_j=a_j/b_{j-1}=\Theta^2\log S_j\quad(1\le j\le h).$$
[三矩形 T-system](R239-appendix-three-rectangle-t-system-and-full-one-bit-gram-fractions.md) §§1–2 的准确族为，记 $d_0=q-t+1$，
$$S_j=s_{(t^{d_0})}(z^{[j]},1^{[h+1-j]}),$$
$$P_j=s_{((t-1)^{d_0+1})}(z^{[j+1]},1^{[h+2-j]}).$$
相应真实范数恰为
$$a_j=\frac{q!}{L!}j!(h+1-j)!\,z^{d_0}\frac{P_j}{S_j}.\tag{2.2}$$
单 Schur Toda 及所需严格导数性已有仓库自足证明；该恒等式的来源为 Suvrit Sra，署名与来源保持所引稿说明。本文的新步骤是把同一两个矩形的实际相邻缺额组合起来。

固定比较位置 $n$，令 $m=h-n$，并置
$$v=a_{n+1}/a_n,\quad f_j=a_n^{-1}v^{n-j},\quad
C=\begin{pmatrix}1&0\\k_n&\sqrt{\gamma_n}\end{pmatrix},\quad \omega=vw.$$
作同一个源合同 $\widetilde H_j=f_jC^*H_jC$。因
$f_{n-1}f_{n+1}=f_n^2$，原相邻差恰只相差共同正倍数与同一个合同；没有改变源度量。高范数的规范四元组为
$$(1/R,1,1,1/T),\qquad
R=\frac{a_n^2}{a_{n-1}a_{n+1}},\quad
T=\frac{a_{n+1}^2}{a_na_{n+2}}.$$

再记
$$F=\gamma_n/\kappa,\quad G=\gamma_{n+1}/\kappa,\quad r=G/F,\quad
\sigma=\frac1{zv^2},$$
$$A=1-Rr,\quad d=r-T,\quad
\xi=\frac A{R(m+1)},\quad \upsilon=\frac d{(n+1)T}.$$
原[全部 Pearson 与剪切消元](R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md)逐式给
$$L_0=1-n\sigma\xi,\qquad W_0=r-m\upsilon/\sigma,$$
$$\boxed{(p,Q,r_\ell,s_\ell)=(1/L_0,1,1/r,1/W_0),}\tag{2.3}$$
$$\boxed{x=-\sqrt{F\sigma}\,\xi,\qquad
y=\sqrt{F/\sigma}\,\upsilon.}\tag{2.4}$$
$L_0,W_0$ 是范数比例，不是物理池长度 $L$。严格内部有
$$0<R,T,R_2=rL_0,T_2=W_0/r^2<1,\qquad T<r<1/R.\tag{2.5}$$
硬首边 $n=1$ 时 $L_0=0,R_2=0$，硬末边 $m=1$ 时 $W_0=0,T_2=0$；未消失的比仍严格在 $(0,1)$。这些零值来自原硬约束，§7 另给准确分母，不把无穷量当作实际 Gram。

Toda 的正邻比直接给
$$\boxed{0<F<n(m+1),\qquad0<G<m(n+1).}\tag{2.6}$$
这里只使用真实 $S_j$，没有将高阶 Hankel 行列式 $\Delta_t$ 当成负实根多项式。

## 3. 真实跨出生约束

定义同一个上矩形的曲率
$$U=\frac{\Theta^2\log P_n}{\kappa},\qquad
V=\frac{\Theta^2\log P_{n+1}}{\kappa}.$$
其总变量数为 $h+3$，故
$$0<U<(n+1)(m+2),\qquad0<V<(n+2)(m+1).$$
由 (2.2) 的真实阶乘比，
$$R=\frac{n(m+1)}{(n+1)(m+2)}
\frac{P_n^2}{P_{n-1}P_{n+1}}
\frac{S_{n-1}S_{n+1}}{S_n^2}.$$
分别用两个族的 Toda，得到
$$\boxed{F=n(m+1)-R[(n+1)(m+2)-U],}\tag{3.1}$$
$$\boxed{G=m(n+1)-T[(n+2)(m+1)-V].}\tag{3.2}$$
全部共同因子和 $z$ 单项式在比中准确消去。

$P_j$ 正是相对出生 $t-1$、高度 $h+2$、位置 $j+1$ 的中矩形。该出生的低范数逐项等于当前高范数 $a_j$；其曲率比为 $r_{\rm old}=V/U$，低通道两比恰是当前 $R,T$。对这个原族使用其自身 Pearson 和严格剪切号，得到
$$\boxed{R<V/U<1/T.}\tag{3.3}$$
此处旧比较位置为 $n+1,m+1\ge2$，没有硬端，也没有使用“较低出生的矩阵定理已经成立”作循环归纳。只需已经自足证明的两权标量与 Pearson 身份。

## 4. 一般第一系数的完整支付

通用四次及其独立提取见[第一、第三系数与完整 Laurent 化](R239-appendix-birth-two-all-height-first-third-coefficients.md) §§2、7。其式子是通用代数式，代入 (2.3)–(2.4) 即适用于当前真实块。

在 $L_0,W_0>0$ 时，第一系数的正倍数为
$$E_1=RTL_0W_0r^2P_1
=T(1-R)(r-L_0W_0)+(1-RT)(r^2-W_0)
-RTW_0x^2-Ty^2-2RTrxy.$$
并有
$$E_1=C_+\sigma+C_0+C_-/\sigma,$$
$$C_+=\frac{TrA}{R(m+1)^2}
\{n(m+1)(1-R)-FA\},$$
$$C_-=\frac d{(n+1)^2T}
\{m(n+1)(1+T-2RT)-Fd\}>0.\tag{4.1}$$
$C_0$ 是所引稿的完整式，没有丢掉混合项。$C_->0$ 只用 (2.6) 及 $r<1/R$。

$r\ge1$ 的正分解，以及 $0<r<1,C_+>0$ 的仿射曲率双端点证明，只用 (2.3)–(2.6)。它们在全部 $n,m\ge1$ 仍成立：唯一需复核的 $m=1$，临界端点的因子为
$2-2(1-r)/A>0$，另一个端点的余括号为 $r^2(1-R)>0$。允许 $L_0=0$ 或 $W_0=0$ 时，$\sigma>\sigma_0$ 改为 $\sigma\ge\sigma_0$，其余严格正项仍在。因此这两个区域及硬边均直接保留严格性。

剩下 $C_+\le0$ 时必有 $r<1$。记
$$\varepsilon=1-r,\quad M=m+2,\quad
E_0=F-G>0,\quad A_0=F-RG>0,\quad D_0=G-TF>0,$$
$$\alpha=\frac{(n+1)(m+2)-U}{m+2}>0.$$
$T_2<1$ 给
$$\sigma<\sigma_*=\frac{m(r-T)}{(n+1)Tr(1-r)}.$$
$C_+\le0<C_-$ 使 $E_1$ 关于 $\sigma$ 严格递减，只须支付 $\sigma_*$ 的代数值。所引稿的一般端点身份及 (3.1) 给正倍数分子
$$\begin{aligned}
N_B/R={}&E_0^2\{(1-R)Tm(m+1)^2(n+1)-D_0\}\\
&+(1-R)D_0mM(E_0G+m\alpha A_0).
\end{aligned}\tag{4.2}$$
无需重用出生二专属相位预算。由 (3.1)–(3.3)，精确有
$$T(V-RU)=D_0+(n+1)\{T[m+M(1-R)]-m\}>0.$$
又 $D_0=G(1-T/r)<m(n+1)(1-T/r)$。两式比较得
$$\boxed{\frac{E_0}{G}=\frac{1-r}{r}
<\frac M m(1-R).}\tag{4.3}$$
将 (4.2) 重组为
$$\boxed{\begin{aligned}
N_B/R={}&(1-R)Tm(m+1)^2(n+1)E_0^2\\
&+D_0E_0\{(1-R)mMG-E_0\}\\
&+(1-R)D_0m^2M\alpha A_0>0 .
\end{aligned}}\tag{4.4}$$
中间括号由 (4.3) 和 $m\ge1$ 严格正，其余也严格正。故坏区域全部支付。整个证明包括 $n=1$ 或 $m=1$，没有从无速率极限推严格性。

第三系数由同一个真实倒数权补集及通用四次反射
$$P^{\rm rev}(1/\omega)=(r_\ell/Q)\omega^{-4}P(\omega)$$
得到严格正性；完整五系数身份已在所引证书核过。共同范数缩放的总齐次次数为七，均为正因子。

## 5. 第二系数：内部和多数硬边

其完整正倍数为
$$E_2=RR_2TT_2r^2P_2,$$
$$\begin{aligned}
E_2={}&\frac T r(1-R)(1-R_2)+(1-RT)(1-R_2T_2)
+Rr(1-T)(1-T_2)\\
&-R(T+rT_2)x^2-\frac T r(R+R_2/r)y^2
-\frac{2RT(r+1)}rxy-\frac{RT}r x^2y^2.
\end{aligned}\tag{5.1}$$
[整个出生二的第二系数证明](R239-appendix-birth-two-two-group-singleton-all-heights-strict-bound.md) §§3–6 是通用标量引理：先作真实反射使 $r\le1$，再利用 $F$ 的严格凹性和
$$F_*=\min\{F_n=n(m+1),\,F_g=m(n+1)/r\}$$
两个端点。它不依赖出生二的实际相位，只依赖 (2.3)–(2.6)。

该引理实际只要求反射后 $m\ge2,n>0$。原文所用 $a=m/(m+1)$ 此时至少 $2/3$；$3a-2\ge0$，其余严格正项仍保严格，且坏端常数
$(m^2-2)/[m(m+1)]>0$。因此全部 $n,m\ge2$ 直接支付。硬首边 $n=1,m\ge2,r\le1$ 也可直接用：允许 $R_2=0$ 不损 $F=0$ 的严格正项或任何端点论证。

唯一还需另核的是该硬首边 $r>1$ 的真实反射，即
$$m=1,\qquad0<r<1,\qquad T_2=0,\qquad
\sigma=\upsilon/r,\qquad n\ge2.\tag{5.2}$$
下一节独立支付此端点。高度 $h=2$ 的双硬端直接用[整个高度二完整定理](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)，不引入两个无穷参数。

## 6. 最后硬边的第二系数

保持 (5.2)，记 $c=n/(n+1)\in(0,1)$、$\varepsilon=1-r$、$d=r-T$、$A=1-Rr$。仍有关于 $F$ 的严格凹性，且 $F=0$ 时 (5.1) 严格正。因此只需
$$F_n=2n,\qquad F_g=(n+1)/r$$
中较小的端点。

### 6.1 $F_n\le F_g$

等价于 $2cr\le1$。将 $F=F_n$、$\sigma=\upsilon/r$ 代入 (5.1)，表达式对 $R$ 仿射，虽原写法含 $1/R$，这些分母准确相消。其 $R=0$ 代数延拓值为
$$E_n(0)=1+\frac{T\varepsilon}r
+\frac{cd(r+3)}{2r}+\frac{c^2d^2}T>0.$$
$R=1$ 的准确值为
$$E_n(1)=(1+r)(1-T)
+\frac{cd(3-6r-5r^2)}{2r}
+\frac{c^2\varepsilon d^2}T.\tag{6.1}$$
去掉最后正项后，它关于 $d\in[0,r]$ 仿射。$d=0$ 值是 $(1+r)\varepsilon>0$。$d=r$ 值是
$$1+r+\frac c2(3-6r-5r^2).$$
括号非负时显正；括号负时用 $c\le1/(2r)$，下界为
$$1+r+\frac{3-6r-5r^2}{4r}
=\frac{(1-r)(r+3)}{4r}>0.$$
故 $E_n(1)>0$，再按 $R\in(0,1)$ 仿射插值，整个 $F_n$ 端点严格正。

### 6.2 $F_g\le F_n$

此时 $2cr\ge1$。定义
$$\mathcal B=\frac{T\varepsilon(1-R)}r+1-RT+Rr(1-T).$$
完整 (5.1) 精确为
$$\begin{aligned}
E_g={}&\mathcal B+\frac d{r^2}[1-Rr(r+2)]\\
&+\frac{Ad}{4Rr^2}\{2cr(1-R)-A\}
+\frac{Ad^2}{4Rr^3T}(2cr-A).
\end{aligned}\tag{6.2}$$
两个花括号分别不小于 $-R\varepsilon$、$Rr$。因此 $E_g\ge\mathcal L$，其中
$$\mathcal L=\mathcal B+\frac d{r^2}[1-Rr(r+2)]
-\frac{Ad\varepsilon}{4r^2}+\frac{Ad^2}{4r^2T}.\tag{6.3}$$
差恰为
$$E_g-\mathcal L=
\frac{Ad(2cr-1)}{4Rr^2}
\left\{1-R+\frac d{rT}\right\}\ge0.$$
$\mathcal L$ 对 $R$ 仿射，其零端点
$$\mathcal L(0)=1+\frac{T\varepsilon}r+
\frac{d(3+r)}{4r^2}+\frac{d^2}{4r^2T}>0.$$
另一端点为
$$\mathcal L(1)=(1+r)\varepsilon
+\frac{d(4r^3-r^2-6r+3)}{4r^2}
+\frac{\varepsilon d^2}{4r^2T}.\tag{6.4}$$
去掉最后正项后，关于 $d\in[0,r]$ 的仿射式在两端分别是
$$(1+r)\varepsilon,\qquad
\frac{\varepsilon(r+3)}{4r},$$
均严格正。因此 $\mathcal L>0$，整个 $F_g$ 端点严格正。凹性完成 (5.2)，从而第二系数的全部内部与硬边均已支付。

## 7. 硬端的完整源、四次系数与正分母

这里的“无穷低范数”只是记号；实际矩阵仍是 (2.1) 的硬约束矩阵。通用四次 $P$ 对 $p$、$s_\ell$ 各自次数至多一。

首边 $n=1$ 直接取 $p$ 的一次系数
$$\overline P=[p]P,$$
等价于代数记号 $\lim_{p\to\infty}P/p$。在原矩阵中准确使用 $B_-= \omega Q$，直接有
$$\det\mathcal K=
\frac{\omega\overline P}
{(Q+\omega r_\ell)^2(c_{\rm high}+\omega d_{\rm high})s_\ell}.\tag{7.1}$$
所有分母严格正。规范后
$$E_1=RTW_0r^2\overline P_1,\qquad
E_2=RTW_0r\,\overline P_2,$$
且
$$\overline P_0=(1/R-1)(1/W_0-1/r^2)>0,\qquad
\overline P_4=(1/T-1)/(r^2W_0)>0.$$

末边直接取 $\widehat P=[s_\ell]P$，使用实际 $B_+=r_\ell$，有
$$\det\mathcal K=
\frac{\omega\widehat P}
{(p+\omega Q)(Q+\omega r_\ell)^2(c_{\rm high}+\omega d_{\rm high})}.\tag{7.2}$$
规范正因子为
$$E_1=RTL_0r^2\widehat P_1,\qquad
E_2=RTL_0r\,\widehat P_2,$$
以及
$$\widehat P_0=p(1/R-1)>0,\qquad
\widehat P_4=(1/T-1)(p/r-1)/r>0.$$
未消失的低比严格小于一，保证这些严格号。

第三系数按真实反射交换两硬端。首主子式也严格正：中心剪切为零时，它是高标量相邻差加非负剪切平方；高相邻分子三个系数为 $1/R-1$、$1/(RT)-1$、$1/T-1$，均严格正。

所以每个硬约束矩阵的四次所有系数严格正，(7.1)–(7.2) 直接给严格 Schur 正性。没有从内点的非严格极限推硬端严格性。

## 8. 完成整个空间与准确后续范围

内部同样有五个严格正系数和严格正首主子式。由原共同源合同，所有二维分支得到 (1.1)。再接 §1 的真空、饱和一维、全部短串、已付高度二和全部原组内重数，正交直和即为整个 $K_s$。这完成任意两个普通重数组加一个异常位的全部出生和全部高度。

旧出生一、出生二及高度二至四的已付证书仍是独立校准与本稿的依赖，未删除。新统一机制来自真实三矩形的跨出生曲率，而不是给 $\Delta_t$ 添加实根假设。

下一有限缺口已转为两个普通组加两个独立异常位：一般相对出生的 primitive 不再只有二维，必须重建完整源及多通道交叉 Schur。一般更多权组、原连续尾、正常正源和边界 $N=M$ 均未因此完成。普通 ISP 的 README 完成标准保持不变。

## 9. 精确核验和可恢复性

本稿证书用 BigInt 系数、完整有符号指数向量、只对单项式取逆，并拒绝未清分母的代换。它独立核最后硬边的完整七项展开、$F_n$ 的两个 $R$ 端点与仿射性、$F_g$ 的完整展开及正余项、其两个 $R$ 端点与仿射性、两个末端线性正界，以及真实跨出生差身份和一般坏第一系数的三项正分组。十三组通用身份全部通过。

根代理逐项独立推导一般规范、跨出生缺额与两个硬端，并执行完整证书通过；two_weight_general_height_1856 独立执行同一完整证书通过。前述通用四次、真实全层 MP、两向 Pearson、全矩形 Toda 与倒数源反射都有明确原稿链。未用任何参数扫描替代全参数证明。终端失联期间按根 README 的小文本回退保存，实际 pull 与 API 核查在 HANDOFF 中分别记录。
