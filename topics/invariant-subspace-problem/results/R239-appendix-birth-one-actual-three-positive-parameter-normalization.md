# R239 附录：出生一实际三正参数归一化与共同源完整四次式

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：本文证明归一化恒等式、全部域条件及中间系数的 Laurent 一次归约。它本身没有证明一般内部高度的完整相邻比较。原权族始终是两组任意重数的正等权位加一个任意正异常位；不是抽象形式相位。第二/末第二边已有独立全域证书，其余内部边仍需支付本稿最后的标量正性。

## 1. 实际对象与已有完整最小逆

普通两组大小为整数 $q,L\ge1$，权平方分别为 $z,1$；异常位权平方为 $w>0$。记
$$
N=q+L,\qquad h=N-1,\qquad
Z_j=[x^j](1+zx)^q(1+x)^L,
\quad M_j=\Theta\log Z_j,\quad V_j=\Theta^2\log Z_j,
\quad\Theta=z\partial_z.
$$
总物理位数是 $N+1$。只处理真正内部比较
$$
2\le n\le h-2,\qquad m=h-n\ge2,
\qquad N=n+m+1.
\tag{1.1}
$$
首/末边已有任意正权出生一结论；$z=1$ 已是两权模型。若 $z<1$，交换普通组并将全删算子除以原短组权，使参数变为 $(L,q,z^{-1},w/z)$。这保持整个实际 $K_1$ 与相邻系数。因此下文可取 $z>1$。

[完整固定二维源的实际真空归约](R239-appendix-birth-one-two-group-singleton-vacuum-reduction.md)给共同首一源坐标中的四组实际范数
$$
a_j=K_0/Z_j,\qquad b_{j-1}=K_0/(Z_jV_j),\quad K_0=(q!)^2z^q,
$$
和完整 MP form
$$
H_j(w)=A_j(w)|\alpha|^2+B_j(w)|\beta+\delta_j\alpha|^2,
\quad A_j=a_j+wa_{j+1},\quad
B_j=\frac{wb_{j-1}b_j}{b_{j-1}+wb_j},
\quad\delta_j=M_{j+1}-M_j.
\tag{1.2}
$$
这些 form 来自整层逆之后的 primitive 压缩；原源 Gram $H_0$ 不被设成单位。相邻算子比较准确等价于 $H_nH_{n+1}^{-1}H_n\prec H_{n-1}$。

本稿只在 (1.1) 使用 (1.2) 的有限内部范数，不对硬端的无穷低范数作形式赋值。

## 2. 两个实际占据率及严格分配参数

定义
$$
p=\frac{q-M_n}{m+1},\qquad
r=\frac{M_{n+1}}{n+1},\qquad
A=p(1-p),\quad B=r(1-r),\quad d=r-p.
\tag{2.1}
$$
它们分别是相邻实际条件子集分布中的未选择短位比例与已选择短位比例。有限正权以及 $1\le n<n+1<N$ 保证 $0<p,r<1$。

将一个固定短位从初等对称和中删去，得到
$$
q-M_n=q\frac{Z_n^{\lnot\mathrm{short}}}{Z_n},\qquad
M_{n+1}=qz\frac{Z_n^{\lnot\mathrm{short}}}{Z_{n+1}}.
$$
对一个池位使用同样恒等式。因此
$$
\boxed{\frac{r(1-p)}{p(1-r)}=z,\qquad
c:=\frac{1-r}{1-p}>0,\qquad
\frac{Z_n}{Z_{n+1}}=\frac{n+1}{m+1}c.}
\tag{2.2}
$$
因为 $z>1$，准确有 $p<r$，故 $d>0$。

对 (2.2) 的赔率恒等式取 $\Theta$ 导数。由 $\Theta p=-V_n/(m+1)$、$\Theta r=V_{n+1}/(n+1)$，得到
$$
\frac{V_n}{(m+1)A}+\frac{V_{n+1}}{(n+1)B}=1.
$$
$V_n,V_{n+1}>0$，因为这两个实际条件分布均至少有两个合法短位占据数。置
$$
\boxed{\theta=\frac{V_{n+1}}{(n+1)B}\in(0,1),\qquad
V_n=(m+1)A(1-\theta),\qquad
V_{n+1}=(n+1)B\theta.}
\tag{2.3}
$$
再对 (2.2) 的最后一式取导数，左边为 $-\delta_n$，右边为
$-r\theta-p(1-\theta)$，故
$$
\boxed{\delta_n=p+d\theta,\qquad
q=(m+\theta)p+(n+1-\theta)r.}
\tag{2.4}
$$
以上均为实际有限系数恒等式，不需要先用一个形式 Riccati 解替代 $Z_j$。

## 3. 三个严格正参数及邻阶系数

定义
$$
\boxed{u=\frac{A(1-\theta)}{B\theta}>0,\qquad
\eta=\frac{d^2\theta}{A}>0,\qquad
 t=\frac{\theta}{1-\theta}>0.}
\tag{3.1}
$$
本节的 $t$ 是正实相位参数，原相对出生已经固定为一。特别
$$
u\eta=\frac{d^2(1-\theta)}B.
$$
普通系数的真实三项递推，或删位恒等式，给
$$
\boxed{
\frac{Z_{n-1}}{Z_n}
=c\frac{n-u\eta}{m+2},\qquad
\frac{Z_{n+2}}{Z_{n+1}}
=c^{-1}\frac{m-\eta}{n+2}.}
\tag{3.2}
$$
例如 $M_n=(n+1)r-\delta_n=nr+d(1-\theta)$，而
$$
\frac{Z_{n-1}}{Z_n}
=\frac{n-(1-z^{-1})M_n}{m+2}
=\frac{nr(1-r)-d^2(1-\theta)}{(m+2)r(1-p)},
$$
这就是第一式；第二式同理。因此真正有
$$
\boxed{a_0:=n-u\eta>0,\qquad b_0:=m-\eta>0.}
\tag{3.3}
$$

定义
$$
X=1-\frac{(m+2)u}{n-u\eta},\qquad
Y=\frac{n+2}{u(m-\eta)}-1.
\tag{3.4}
$$
实际 shear 差为
$$
x=\delta_n-\delta_{n-1}=d\theta X,\qquad
 y=\delta_n-\delta_{n+1}=d(1-\theta)Y.
\tag{3.5}
$$
一种直接核法是：令
$r_-:=M_n/n=r+d(1-\theta)/n$，由 (2.2) 的同阶赔率关系求出相邻 $p_-$；莫比乌斯差恰为
$$
p_--p=\frac{Ad(1-\theta)}{B(n-u\eta)}.
$$
再用 $\delta_{n-1}=(m+2)p_--(m+1)p$ 即得第一式。另一端取
$p_+=p-d\theta/m$，得到
$$
r-r_+=\frac{Bd\theta}{A(m-\eta)},
$$
从而得第二式。

在当前 $z>1$、$q,L\ge1$ 的非平凡实际模型中，已有自足 Schur Turán 单调性给 $\delta_{n-1}>\delta_n>\delta_{n+1}$，于是
$$
\boxed{X<0<Y.}
\tag{3.6}
$$
准确来源是 [矩形 Turán 单调性与严格性](R239-appendix-rectangular-turan-endpoints-and-sharp-curvature-caps.md) §5 对 Suvrit Sra, *Monotonicity of Turán-ratios of symmetric polynomials* (2026), Lemma 2.2 / Theorem 1.1 的署名自足证明。应用时使用有限秩交换
$Z_j/\binom Nj=e_q(z^{[j]},1^{[N-j]})/\binom Nq$；所以其严格单调性正是 $\Theta\log[Z_j^2/(Z_{j-1}Z_{j+1})]>0$。这里没有把预印本结论当成未经仓库重证的黑箱。

## 4. 保共同原源的准确规范 form

先把全部三个相邻 form 除以同一个正数 $a_n$，对所有阶使用同一个源合同
$$
\beta=\sqrt{V_n}\,\beta_{\rm new},
$$
再将第 $j$ 阶 form 乘以正几何因子 $c^{n-j}$。这些操作保持真实相邻不等式：共同源合同直接消去，而中阶夹乘与前阶的几何倍数同为 $c$。异常权参数相应仅重命名为
$$
\omega=cw>0.
$$
因此没有随阶任意重选源，也没有改动非正交源 Gram 的逆次序。

在规范形式中，高范数四元组准确为
$$
\boxed{(a,b,c_*,d_*)=
\left(\frac{m+2}{n-u\eta},\ 1,\ \frac{n+1}{m+1},\
\frac{(n+1)(n+2)}{(m+1)(m-\eta)}\right).}
\tag{4.1}
$$
为避免与 (2.2) 的几何因子混淆，下文记 $C=(n+1)/(m+1)$，$a=(m+2)/(n-u\eta)$，$D=C(n+2)/(m-\eta)$。

置
$$
A_*:=\frac{C}{u},\qquad
\ell=-\frac{nX}{(m+1)u}>0,\qquad
k=\frac{muY}{n+1}>0,
$$
$$
\boxed{R=A_*-\ell t,\qquad T=A_*^{-1}-k/t.}
\tag{4.2}
$$
则低范数四元组准确为
$$
\boxed{(p_*,Q_*,r_*,s_*)=
\left(\frac1{uR},\ 1,\ u,\ \frac{u^2}{T}\right),}
\tag{4.3}
$$
且规范 shear 差满足
$$
\boxed{x_*^2=\frac{\eta tX^2}{m+1},\quad
y_*^2=\frac{\eta Y^2}{(m+1)t},\quad
x_*y_*=\frac{\eta XY}{m+1}.}
\tag{4.4}
$$

为核 (4.3)，记 $C_j=Z_jV_j$。这里明确保留共同系数 $Z_n$，真实 Pearson 身份或 (3.5) 给
$$
\frac{C_{n-1}}{Z_n}=p(1-r)\left[n+1-\theta-
\frac{n(m+2)u\theta}{n-u\eta}\right],
$$
$$
\frac{C_{n+2}}{Z_n}=\frac{r(1-p)}{Z_n/Z_{n+1}}
\left[m+\theta-
\frac{m(n+2)(1-\theta)}{u(m-\eta)}\right].
$$
代入实际 $b_{j-1}=K_0/C_j$ 和上述共同缩放，分别得到
$$
R=\frac{C_{n-1}C_{n+1}}{C_n^2},\qquad
T=\frac{C_nC_{n+2}}{C_{n+1}^2}.
\tag{4.5}
$$
由于所有 $C_j>0$，两者严格正。旧两权完整出生一标量定理又给
$$
\boxed{0<R<1,\qquad0<T<1.}
\tag{4.6}
$$
其准确引用是 [两权全高度严格比较](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md) 主定理及完整 MP 归约；此处的低范数即该实际两权出生一固定 primitive 线的范数。

特别，(4.2) 与 $R,T>0$ 已经给出
$$
\boxed{\ell k<1,\qquad A_*k<t<A_*/\ell.}
\tag{4.7}
$$
进一步 $R,T<1$ 还给
$$
 t>\frac{A_*-1}{\ell}\quad(A_*>1),\qquad
 t<\frac{A_*k}{1-A_*}\quad(A_*<1).
\tag{4.8}
$$
这些是同一真实相位必须满足的域条件，不可遗漏。

## 5. 全四次式及第一个中间系数的精确降次

记
$$
L_0=aC-1>0,\quad L_1=aD-C>0,\quad L_2=D-C^2>0.
$$
令 $P(\omega)$ 是既有完整 $2\times2$ Schur 补行列式的清正分母四次式：
$$
\begin{aligned}
P={}&Q_*\Lambda\Phi
-\omega p_*Q_*^3r_*(C+\omega D)(r_*+\omega s_*)x_*^2\\
&-\omega Q_*^2r_*^2s_*(a+\omega)(p_*+\omega Q_*)y_*^2\\
&-2\omega p_*Q_*^2r_*s_*(1+\omega C)(Q_*+\omega r_*)x_*y_*\\
&-\omega^2p_*Q_*^3r_*^2s_*x_*^2y_*^2,
\end{aligned}
$$
$$
\Lambda=L_0+\omega L_1+\omega^2L_2,
\quad\Phi=p_*Q_*(Q_*s_*-r_*^2)
+\omega Q_*r_*(p_*s_*-Q_*r_*)
+\omega^2r_*s_*(p_*r_*-Q_*^2).
\tag{5.1}
$$
它包含所有 shear 二次项、交叉项及四次项；系数 $P_i=[\omega^i]P$。$P_0,P_4$ 由真实两条标量严格凸性直接严格正。

对 $P_1$ 精确有
$$
\boxed{RT P_1=C_+t+C_0+C_-/t,}
\tag{5.2}
$$
其中
$$
C_+=L_0u^2\ell/A_*-C u\eta X^2/((m+1)A_*),
$$
$$
C_-=L_0u^2A_*k+L_1uk-a u^3\eta Y^2/(m+1),
$$
$$
C_0=-L_0u^2\ell k+L_1u(1-A_*^{-1})
+C u\eta kX^2/(m+1)-2u^2\eta XY/(m+1).
\tag{5.3}
$$
两端系数有明确严格正因子分解：
$$
\boxed{C_+=\frac{u^2[u(m+2+\eta)-n][m+n+2+(n+1)\eta]}
{(m+1)(n-u\eta)(n+1)}>0,}
\tag{5.4}
$$
$$
\boxed{C_-=\frac{u(3m+2)[n+2-u(m-\eta)]
[m+n+2+(m+1)u\eta]}
{(m-\eta)(m+1)^2(n-u\eta)}>0.}
\tag{5.5}
$$
这是普通有限有理恒等式。它们严格正的原因仅为 (3.3)、(3.6)，不是数值抽样。

$P_2$ 和 $P_3$ 同样乘以 $RT$ 后只有 $t,1,t^{-1}$ 三个次数；[中间系数的独立严格正性引理](R239-appendix-birth-one-normalized-middle-quartic-positivity.md)已给出 $P_2$ 的全参数身份、正性及显式正下界。该引理的实际应用入口恰是 §§1–4。本文未将尚未支付的 $P_1/P_3$ 常数项或整个四次式正性视为已证。

## 6. 形式相位与实际权族的区别

任意 $u,\eta,t>0$ 都能重建一对 $0<p<r<1$：设
$$
s=ut,\quad k_0=\eta(1+t)/t,\quad
J=k_0+s^{-1}-1,\quad W=\sqrt{4k_0+J^2},
$$
$$
p=(1-J/W)/2,\qquad r=p+k_0/W,\qquad\theta=t/(1+t).
$$
直接代入给 $p(1-p)/[r(1-r)]=s$ 与 $(r-p)^2/[p(1-p)]=k_0$。但由 (2.4) 重建的 $q,L$ 未必是整数，即使它们偶然为整数，局部数据也未必等于同一个完整多项式 $Z_j$。因此不能把形式相位抽样当成实际定理或实际反例。本文的归一化方向从实际 $Z_j$ 出发，所以所有真实对象均满足本文域条件。

全部新恒等式只处理真正二维固定块。若最终支付其一般内部相邻序，还须与出生一的两个组内标准表示分支拼接；这些分支的实际 Gram 是删去相应两个等权位后的初等对称和倒数，已由 Newton 支付。

## 独立精确核验

[独立有理与符号程序](../notes/2026-11-14-birth-one-actual-three-positive-parameter-check-0c.py)从实际有限子集系数核对38组完整norm/shear、同源合同和几何因子，并明确核对两个含共同 $Z_n$ 的邻方差式；通用 $P_1$ 的 Laurent 身份和两正端系数也为有理函数恒等。它不把有限实例当作尚未完成的 $P_1/P_3$ 一般正性证明。
