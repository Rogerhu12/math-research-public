# R239 附录：普通两组权比有界时一个任意异常位的全部出生一高度严格系数一

日期：2026-11-14（UTC）。作者：two_weight_general_height_1856 / Astra-ISP-0c017065（根代理贡献完整 P2 正性引理）；AI-assisted，GPT-6 Astra Pro。

状态：下述有限模型定理已证明。本稿给实际全高度的权比范围，不把它扩成任意三权、任意出生或普通 ISP 的完成证明。

## 1. 完整定理

在有限 Boolean Hilbert 空间上取
$$
D=a\sum_{i=1}^qE_i+b\sum_{i=q+1}^{q+L}E_i+cE_{q+L+1},
\qquad q,L\ge1,\quad a,b,c>0.
$$
置
$$
h=q+L-1,\quad K_1=\ker D\cap\mathcal H_1,\quad
F_j=D^j(D^*)^j|_{\mathcal H_1}/(j!)^2,\quad
\Gamma_j=P_{K_1}F_j^{-1}|_{K_1}.
$$
逆始终先在整个 $\mathcal H_1$ 上取，再压缩。实际有限正权保证所有 $0\le j\le h$ 的完整逆存在。

记两组普通权的平方比与对称反差为
$$
z=\max\{a^2/b^2,b^2/a^2\}\ge1,
\qquad \lambda=\frac{(z-1)^2}{z}.
$$
**定理。** 若
$$
\boxed{\lambda\le\frac{12}{5},\quad\text{即}\quad
z\le\frac{11+4\sqrt6}{5},}
\tag{1.1}
$$
则对全部合法 $1\le j<h$，在整个原 $K_1$ 上严格有
$$
\boxed{\Gamma_j\Gamma_{j+1}^{-1}\Gamma_j\prec\Gamma_{j-1}.}
\tag{1.2}
$$
异常权 $c$ 没有大小限制。

更具体地，当 $h\ge6$ 固定时，可把 (1.1) 放宽为
$$
\boxed{\lambda\le\frac{12(h+2)}{5(h-2)}.}
\tag{1.3}
$$
$h\le5$ 时所有比较均已被首两/末两边覆盖，无需权比限制。定理的严格号不要求普通权互异；$z=1$ 直接属于已证两权模型。

## 2. 已付边界、完整源和实际相位

所用的完整有限模型输入为：

- [R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md)：任意正权的出生一首边；配合真实倒数权对偶支付末边。
- [任意两普通组加一位的第二/末第二边](R239-appendix-birth-one-two-group-singleton-second-and-penultimate-edges.md)：整个出生一空间的全域整数证书。
- [R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)：实际两权低范数的全部高度严格比较。
- [R239-appendix-primitive-gram-reciprocal-weight-duality-all-births](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)：真实倒数权反向对偶及其相邻逆次序。
- [实际三正参数归一化](R239-appendix-birth-one-actual-three-positive-parameter-normalization.md) §§1–4：原完整逆、实际共同源和真实联合可行域。

因此只须处理
$$
n\ge3,\qquad m=h-n\ge3.
\tag{2.1}
$$
归一普通池权为一、普通短组权平方为 $z>1$。前稿从实际
$Z_j=[x^j](1+zx)^q(1+x)^L$ 定义两个占据率
$$
p=\frac{q-\Theta\log Z_n}{m+1},\qquad
r=\frac{\Theta\log Z_{n+1}}{n+1},\qquad0<p<r<1,
$$
及 $0<\theta<1$，严格满足
$$
\frac{r(1-p)}{p(1-r)}=z,
\quad V_n=(m+1)p(1-p)(1-\theta),
\quad V_{n+1}=(n+1)r(1-r)\theta.
$$
令
$$
u=\frac{p(1-p)(1-\theta)}{r(1-r)\theta},\qquad
\eta=\frac{(r-p)^2\theta}{p(1-p)},\qquad
 t=\frac\theta{1-\theta}.
$$
同一个源合同和每阶共同正几何倍数后，完整相邻 form 的高、低范数及 shear 差为
$$
(a,1,C,D)=\left(\frac{m+2}{n-u\eta},1,
\frac{n+1}{m+1},\frac{(n+1)(n+2)}{(m+1)(m-\eta)}\right),
$$
$$
(p_*,1,u,s_*)=\left(\frac1{uR},1,u,\frac{u^2}T\right),
\qquad x^2=\frac{\eta tX^2}{m+1},\quad
y^2=\frac{\eta Y^2}{(m+1)t},\quad xy=\frac{\eta XY}{m+1},
\tag{2.2}
$$
其中
$$
X=1-\frac{(m+2)u}{n-u\eta}<0,
\qquad Y=\frac{n+2}{u(m-\eta)}-1>0,
$$
$$
A=\frac C u,\quad\ell=-\frac{nX}{(m+1)u}>0,
\quad k=\frac{muY}{n+1}>0,
\quad R=A-\ell t,\quad T=A^{-1}-k/t.
$$
全部对象均为实际归约；特别
$$
\alpha:=n-u\eta>0,\quad\beta:=m-\eta>0,
\qquad0<R,T<1,\qquad\ell k<1.
\tag{2.3}
$$
源归一化对全部高度共同实施：把所有 form 除以同一个 $a_n$，使用 $\beta_{\rm old}=\sqrt{V_n}\beta_{\rm new}$，再将第 $j$ 阶乘以 $c_0^{n-j}$，其中 $c_0=(1-r)/(1-p)$。异常参数成为 $\omega=c_0w>0$。这些操作保持真实 Schur 比较；没有把源 Gram 换成单位。

以下中文证明只用上述已经支付的实际归约与有限有理恒等式。

## 3. 统一简记及决定性的四次式

置
$$
M=m+1,\quad N=n+1,\quad H=M+N,
$$
$$
J=u(m+2+\eta)-n>0,\quad K=n+2-u(m-\eta)>0,
$$
$$
\delta=Mu-N,\quad V=1+u(\eta+1),\quad
H_+=H+N\eta,\quad H_-=H+Mu\eta.
\tag{3.1}
$$
于是 $J=V+\delta$、$K=V-\delta$，且
$$
\boxed{JK<\frac{MN u\alpha\beta}{nm}.}
\tag{3.2}
$$
它准确来自 $\ell k=nmJK/(MN u\alpha\beta)<1$。

令 $P(\omega)=\sum_{i=0}^4P_i\omega^i$ 为完整 $2\times2$ Schur 补行列式的既有清正分母四次式。其完整生成公式见三参数入口稿 (5.1)，包含二次 shear、交叉项与 $x^2y^2$ 四次项。

$P_0,P_4>0$ 已由两条实际低范数严格凸性和高范数严格 Newton 给出。下面支付三个中间系数。只要它们严格正，就有 $P(\omega)>0$ 对所有异常权 $\omega>0$ 成立。另一个 Sylvester 主子式严格正，因为
$$
(A_-A_+-A_0^2)=(aC-1)+\omega(aD-C)+\omega^2(D-C^2)>0.
$$
所以四次式的正性准确给完整二维相邻 Schur 补正定。

## 4. 全域中间系数 $P_2$：根代理的正性引理

本节重述[完整P2全参数正性](R239-appendix-birth-one-normalized-middle-quartic-positivity.md)的有限代数引理，使本稿的全高度结论可自足核查。该引理由根代理证明，另一代理独立核验。

置 $D_0=\beta M^2\alpha>0$。准确有
$$
D_0\,RT\,P_2/u=N_+t+N_0+N_-/t,
$$
$$
N_+=u(2M+\beta)JH_+>0,\qquad
N_-=(2N+\alpha)KH_->0,
$$
$$
N_0=-[V+3(n+m)+4]JK
+V[J\beta(u\eta+1)+Ku(m+2)(\eta+1)].
\tag{4.1}
$$
这些恒等式按完整四次式逐项清分母得到，没有删去负的四次 shear 费用。

由 (3.2)、$\alpha<n$、$\beta<m$，
$$
2\sqrt{N_+N_-}>4JK\sqrt{H_+H_-}.
$$
而
$$
\sqrt{H_+H_-}\ge H+\eta\sqrt{uMN}\ge H+\eta u.
$$
最后一个不等式的依据是 $u<N$：$Y>0$ 给 $u(m-\eta)<n+2$，再加 $u\eta<n$ 得 $um<2N$；因 $m\ge2$，确有 $u<N<MN$。

因此
$$
4\sqrt{H_+H_-}-[V+3(n+m)+4]
>H+1-u+3\eta u>0.
$$
在 (4.1) 中用正数 AM–GM 得 $N_+t+N_-/t\ge2\sqrt{N_+N_-}$，从而
$$
\boxed{P_2>0.}
\tag{4.2}
$$
这个引理只需 $R,T>0$，不需要当前权比限制。

## 5. 第一个中间系数的两个严格正性区域

定义
$$
B=mH-N(M+1)\eta,\qquad
G=2H+\eta(n+mu-u\eta)>0,
\qquad D_1=\alpha\beta M^2N/u>0.
$$
三参数入口的 Laurent 身份等价于
$$
\boxed{D_1RT P_1=
 uM\beta JH_+t-JKB-MN\delta G
 +N(3m+2)KH_-/t.}
\tag{5.1}
$$
本节证明
$$
\boxed{P_1>0\quad\text{只要}\quad\delta\le0\ \text{或}\ B\ge0.}
\tag{5.2}
$$
第二个区域使用 $n,m\ge3$。

### 5.1 $\delta\le0$

若 $B\le0$，(5.1) 中所有项非负且两个端项严格正，结论直接成立。若 $B>0$，两个正端项的几何均值除以 $JK$ 后，由 (3.2) 得
$$
\frac{2\sqrt{uMN\beta(3m+2)JKH_+H_-}}{JK}
>2\sqrt{\frac{nm(3m+2)H_+H_-}{\alpha}}
>2\sqrt{m(3m+2)}\,H.
$$
右边严格大于 $mH\ge B$。故两个正端项已严格支付 $JKB$，而 $-MN\delta G\ge0$，证明此域。

### 5.2 $\delta>0$ 的一个真实域上界

先证明
$$
\boxed{K<Nm/M.}
\tag{5.3}
$$
令 $u=(N+\delta)/M$，则
$$
u\beta=N+1-K,\qquad
M\alpha=N(M+1)-m\delta-MK,\qquad J=K+2\delta.
$$
由 (3.2)，
$$
F(K,\delta):=MN\alpha(N+1-K)-nmK(K+2\delta)>0.
\tag{5.4}
$$
在实际正域 $\alpha>0$、$N+1-K=u\beta>0$ 上，$F$ 对 $K$ 严格递减。展开也给
$$
F(K,\delta)=F(K,0)
-m\delta[N(N+1)+(N-2)K],
$$
故对 $\delta\ge0$ 同样严格递减。若 $K\ge K_*:=Nm/M$，沿 $K$ 从 $K_*$ 到当前值，两个正因子仍为正；因此
$$
F(K,\delta)\le F(K_*,0)
=\frac{N^2}{M^2}[2M(M+N)-nm^3]<0,
$$
矛盾。最后一个严格号对 $n,m\ge3$ 是显式整数正性：写 $n=3+x,m=3+y$，则
$$
nm^3-2(m+1)(m+n+2)
=17+19x+57y+25xy+25y^2+9xy^2+3y^3+xy^3>0.
$$
这证明 (5.3)。

### 5.3 $\delta>0$、$B\ge0$

由 $T=A^{-1}-k/t$ 精确有
$$
\delta=\frac{mK}{\beta t}-N(1-T).
$$
代回 (5.1)，得到保留正补偿项的身份
$$
D_1RT P_1=uM\beta JH_+t-JKB
+\frac{NK}{\beta t}\mathcal R+MN^2G(1-T),
\tag{5.5}
$$
其中
$$
\mathcal R=(3m+2)\beta H_--MmG
=mB+2M\eta(Nm-MK)>mB\ge0.
\tag{5.6}
$$
最后一步使用刚证的 (5.3)。若 $B=0$，(5.5) 已严格正。
若 $B>0$，两个正端项的 AM–GM 及 (3.2) 给
$$
\frac{2\sqrt{uMNJKH_+\mathcal R}}{JK}
>2\sqrt{\frac{nmH_+\mathcal R}{\alpha\beta}}
>2\sqrt{mH_+B}>B.
$$
最后一步使用 $B\le mH\le mH_+$。于是它们严格支付 $JKB$，剩余 $MN^2G(1-T)>0$，证明 (5.2)。

## 6. 真实反射与 $P_3$

先对全部物理权取倒数，再乘同一正标量并交换两普通组，使普通平方比仍为 $z>1$。普通占据率反射为
$$
p'=1-r,\quad r'=1-p,\quad\theta'=1-\theta.
$$
因此规范相位准确变成
$$
\boxed{(n,m,u,\eta,t,\omega)
\longmapsto(m,n,u^{-1},u\eta,t^{-1},\omega^{-1}).}
\tag{6.1}
$$
特别 $R'=T,T'=R$，$\delta'=-\delta/u$。

不仅相邻 Schur 序由真实对偶反转，清分母四次式本身也有精确恒等式
$$
\boxed{P(\omega)=u^4C^2\omega^4P'(\omega^{-1}),\qquad C=N/M.}
\tag{6.2}
$$
可直接逐项核验：高范数变为 $(D/C,1,1/C,a/C)$；低范数变为 $(s_*/u,1,1/u,p_*/u)$；两个 shear 的平方互换后同乘 $u/C$，交叉项也同乘 $u/C$。将它们代入完整四次式，五个系数均给 (6.2)，并保留全部四次费用。

所以对反射参数使用 §5 即给 $P_3>0$。特别，若
$$
\boxed{B=mH-N(M+1)\eta\ge0,\qquad
B'=nH-M(N+1)u\eta\ge0,}
\tag{6.3}
$$
则无论 $\delta$ 的符号如何，均有 $P_1,P_3>0$。与 §4 及 $P_0,P_4>0$ 拼合，这支付当前完整二维比较。

## 7. 从实际普通权比得到全高度范围

实际赔率恒等式给
$$
\lambda=\frac{(z-1)^2}{z}
=\frac{(r-p)^2}{p(1-p)r(1-r)}.
$$
因此由 $0<\theta<1$，
$$
\boxed{\eta=\lambda r(1-r)\theta<\lambda/4,
\qquad u\eta=\lambda p(1-p)(1-\theta)<\lambda/4.}
\tag{7.1}
$$
这些是严格实际方差上界，不是形式相位假设。

若 $n,m\ge3$，则
$$
\frac{mH}{N(M+1)}
=\frac m{m+2}\left(1+\frac{m+1}{n+1}\right)>rac35,
$$
且反射的 $nH/[M(N+1)]>3/5$ 同样成立。因此 $\lambda\le12/5$ 与 (7.1) 严格保证 (6.3)，完成全部内部二维比较。

对固定 $h=n+m\ge6$，两个阈值在 $n,m\ge3$ 上的最小值准确为
$$
\frac{3(h+2)}{5(h-2)}.
$$
例如第一阈值写成 $m(h+2)/[(h-m+1)(m+2)]$，其对 $m$ 严格增加；最小值在 $m=3$。这就给 (1.3)。

最后，将二维固定源与两组内标准表示的完整正交分解拼接。两个组内部分的实际 $\Gamma_j$ 分别为
$$
e_j(z^{[q-2]},1^{[L]},w)^{-1}I,\qquad
e_j(z^{[q]},1^{[L-2]},w)^{-1}I,
$$
不存在的零维部分删去。严格 Newton 支付全部合法相邻阶；固定块首两/末两由 §2 的现成完整定理支付。于是 (1.2) 在整个原 $K_1$ 上成立。

## 8. 核验和范围

独立可执行核验为 [精确恒等式程序](../notes/2026-11-14-birth-one-bounded-ordinary-contrast-allheight-check-0c.py)：它检查 (5.1)、(5.5)、(5.6)、域多项式与 $K_*$ 值、整数平移的全部正系数，以及五个四次系数的反射恒等式。正性论证为 §§4–7 的自足解析证明，不以有限点抽样替代。

本稿仍未支付 $\lambda>12/5$ 时所有高度的完整固定块，也没有把该有限出生一模型推广到任意出生、任意多权、原无限尾的返回费或普通 ISP。异常位权从始至终任意正，全部逆、共同源和表示分支均保留。
