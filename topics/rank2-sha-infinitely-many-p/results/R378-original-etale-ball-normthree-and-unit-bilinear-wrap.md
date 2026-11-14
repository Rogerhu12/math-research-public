# R378：同一 étale 核的原逐球三次式、完整 norm-three 与单位双线性 wrap

日期：2026-11-14。**状态：以下准确加法标签、原三个测度的逐球三次／norm-three 恒等式、逐球乘法与原加法卷积的完整比较、全部循环项以及一条对每个普通 $p>7$ 为单位的双线性行均已证明。指定的两个固定负矩联合非零仍未证明。单位行包含它们以外的全部中间项，本篇没有删去这些项，也没有把逐球单位当成原 Mellin 聚合非零。主目标未完成。**

本文只使用 R316、R332、R336、R345、R376 已支付的同一原 sigma、Theta、CM 迹、周期及整测度。以下有限域等式均是原整身份的约化，不重新选择 theta 群相位。

## 1. 同一原模型、核及周期

固定
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad
D=\frac d{dz},\quad Dz=1,\quad Dx=2y,
$$
$$
x=z^{-2}+\cdots,\qquad y=-z^{-3}+\cdots,\qquad
\sigma=z+\cdots,\qquad
\Theta=x\sigma^2,\qquad C=y\sigma^3.
\tag{1}
$$
固定好普通 $p>7$，写
$$
p=6s+1,\quad
\delta=1+2\omega,\quad \delta^2=-3,\quad
\delta\bar\delta=3,\quad \bar\delta=-\delta.
\tag{2}
$$
选定原普通嵌入后，$\delta,\omega$ 的约化在 $\mathbf F_p$。

原 Frobenius 为 $\pi=\psi_{17}(\mathfrak p)$，$\pi\bar\pi=p$。
令
$$
H=\binom{3s}{s}b^s=\bar\pi\bmod p\ne0,\qquad
V=[\bar\pi]\bmod p:E_b\longrightarrow E_b.
\tag{3}
$$
它是实际可分次数 $p$ 同源，$V^*dz=Hdz$。其非零核的真实 Miller 多项式为
$$
f=P(X),\qquad X=x^3,\qquad
P\text{ monic},\quad \deg P=s.
\tag{4}
$$
非零核点的阶为 $p$，所以在那里 $x,y,Df$ 均非零。

原普通周期仍记为 $\Omega$；其整形式群同构满足
$$
\beta^*dz=\Omega\,\frac{dT}{1+T}.
$$
所有约化在同一个剩余域 $k\subset\overline{\mathbf F}_p$ 中进行。
R336 的 $D^p=HD$ 与上述形式群同构给
$$
\boxed{\Omega^{p-1}=H^{-1}.}
\tag{5}
$$
这里及以下 $\Omega$ 表示原周期的单位约化；没有任意改动加法变量。

三个原测度的完整 core 写成
$$
\nu_G|_{p\mathbf Z_p}=\lambda_G[\kappa]_*\nu_G,\qquad
\kappa=p/\bar\pi^2,\qquad G=\sigma,\Theta,C.
\tag{6}
$$
全部 $\lambda_G$ 为单位。特别
$$
\lambda_\sigma=\varepsilon^3/\bar\pi,\qquad
\lambda_\Theta=\varepsilon/\bar\pi
               =1/\bar\pi_0,
\tag{7}
$$
其中 $\pi_0=\psi_0(\mathfrak p)$ 是 $E_0:y^2=x^3+1$ 的原 Frobenius，
$\pi_0=\varepsilon\pi$，所以
$\bar\pi_0=\varepsilon^{-1}\bar\pi$。$C$ 的绝对 core 已由 R345 支付；
以下不需要用一个猜测的六次根代替 $\lambda_C$。

## 2. AS deck 常数与真正加法标签

令 $Z=D\log f$。R336 的实际 Artin–Schreier 覆盖和式 (26) 给
$$
V^*(\zeta\,dz)=d\log f,\qquad
\zeta^p-H\zeta=D^{p-2}x.
\tag{8}
$$
因此对 $q\in\ker V$，
$$
\ell(q):=Z(P_0+q)-Z(P_0)
\tag{9}
$$
与一般点 $P_0$ 无关，并满足
$$
\ell(q+q')=\ell(q)+\ell(q'),\qquad
\ell(q)^p=H\ell(q).
\tag{10}
$$
这里 $P_0$ 是变量点，不是核多项式的常数项。

这个加法映射在 $\ker V$ 上忠实。确实，(8) 是 R336 已证明几何连通的次数 $p$ AS 覆盖；其全部 deck 变换恰为这些常数平移。故非零 $q$ 的 $\ell(q)$ 非零。

还能直接在核点计算同一常数。在 $O$，
$$
Z=z^{-1}+O(z),
$$
因为 $f$ 的极阶是 $p-1$，且 $f$ 是偶函数。在非零简单零点 $q$，
$$
Z(q+z)=z^{-1}+\frac{D^2f(q)}{2Df(q)}+O(z).
$$
所以
$$
\boxed{\ell(q)=\frac{D^2f(q)}{2Df(q)}\ne0
       \quad(q\in\ker V\setminus\{0\}).}
\tag{11}
$$
特别 $D^2f(q)$ 在所有这些点也非零。若需要完全多项式式子，
$$
Df=6x^2yP',\qquad
D^2f=6x\bigl((7X+4b)P'+6X(X+b)P''\bigr).
\tag{12}
$$

下面确定原标签，而非仅给一个未定标的核点参数。沿 R376 的真实 theta 群约定
$$
A_tB_q=e_d(t,q)B_qA_t,
$$
$\rho=r_{\bar\pi}/r_\pi$ 给
$$
e_d(t,q)=
\left(\frac{\rho(P_0+t)\rho(P_0+q)}
{\rho(P_0+t+q)\rho(P_0)}\right)^d.
\tag{13}
$$
原 division 首项分别保留 $\bar\pi,\pi$。约化后
$$
r_{\bar\pi}=Hf,\qquad r_\pi=1.
\tag{14}
$$
第二式可在原整 sigma frame 中核定：$[\pi]$ 约化为 Frobenius，
原整 sigma 级数的系数在 $\mathbf F_p$，故
$\Sigma([\pi]T)=\Sigma(T)^p$；商在整个好模型上无水平或垂直除子，
其原 frame 常数为一。这里没有把 $r_{\bar\pi}$ 人为改成首一。

对 (13) 在 $t=0$ 微分得到 $-d\ell(q)$。原 Fourier 标签 $c$ 的角色是
$$
\chi_c(t)=
\bigl(1+\beta^{-1}([\bar\pi]t)\bigr)^c,
$$
其同一个微分为 $Hc/\Omega$。因此
$$
\boxed{c_d(q)=-\frac{d\Omega}{H}\ell(q).}
\tag{15}
$$
由 (5)、(10)，$c_d(q)$ 的值在 $\mathbf F_p$；因 $p\nmid d$，
这是 $\ker V\simeq\mathbf F_p$ 的真实加法标签。

今后记 $q_c$ 为 degree-one 的标签，即
$$
c=-\Omega\ell(q_c)/H.
\tag{16}
$$
**同一个 $q_c$ 在 degree two、three 中的原标签分别为 $2c,3c$。**
这两个尺度不能省略。

## 3. 三个原逐球值在同一核上

写原剩余类质量的约化为
$$
s_c=\nu_\sigma(c+p\mathbf Z_p)\bmod p,\quad
t_c=\nu_\Theta(c+p\mathbf Z_p)\bmod p,\quad
u_c=\nu_C(c+p\mathbf Z_p)\bmod p.
\tag{17}
$$
定义
$$
a_c=\frac{s_c}{\lambda_\sigma},\qquad
b_c=\frac{t_{2c}}{\lambda_\Theta},\qquad
h_c=\frac{u_{3c}}{\lambda_C}.
\tag{18}
$$
R376 的原整逐球公式是
$$
\nu_G(c_d(q)+p)=
\lambda_G
\left(\frac{\bar\pi\,r_\pi(q)}{Dr_{\bar\pi}(q)}\right)^d
f_G([\pi]q),
\qquad G=\sigma^df_G.
\tag{19}
$$
该式包含原 $p^{-1}$ Fourier 平均、全部真实 theta lift 及垂直 frame；
不能另乘或除一个 rigidification 常数。

联立 (14) 以及 $[\pi]q=\operatorname{Frob}(q)$，得到
$$
\boxed{
a_c=\frac1{Df(q_c)},\quad
b_c=\frac{x(q_c)^p}{Df(q_c)^2},\quad
h_c=\frac{y(q_c)^p}{Df(q_c)^3}
\quad(c\ne0).
}
\tag{20}
$$
零球则由 (6) 和原质量准确给
$$
\boxed{(a_0,b_0,h_0)=(0,1,-1).}
\tag{21}
$$
因此对每个 $c\in\mathbf F_p$，
$$
\boxed{h_c^2=b_c^3+b\,a_c^6.}
\tag{22}
$$
这是实际**逐球乘法**恒等式；不是把原来源乘积所给的加法卷积改写成逐点乘积。

## 4. norm-three 的共轭标签与完整逐球式

CM $\delta$ 作用在这个 étale 标签上是
$$
\boxed{c(\delta q)=\bar\delta\,c(q)=-\delta\,c(q).}
\tag{23}
$$
尤其不是 $c/\delta$；两者差真实范数三。

可直接从同一核方程证明这个方向。R336 给
$$
f(\delta P_0)=X(P_0)^{-2s}f(P_0)T_P(X(P_0)),
$$
$$
xT_P=(Df)^2-fD^2f,\qquad
DZ=-H^2x(VP_0).
\tag{24}
$$
由于 $6s=p-1$，第一式也写成
$$
f(\delta P_0)=-x(P_0)^{-p}f(P_0)^3DZ(P_0).
$$
取对数导数，再比较 $P_0+q$ 与 $P_0$。$DZ$ 是经 $V$ 拉回的函数，
其对数导数在 deck 平移下不变，而 $D(x^{-p})=0$。所以
$$
\delta\,\ell(\delta q)=3\ell(q),
$$
恰给 (23)。这也与原 Weil 配对的 Rosati 共轭方向一致。

在非零核点对 (24) 第一式求导。由于 $f(q)=0$，
$$
T_P(X(q))=\frac{Df(q)^2}{x(q)},\qquad
\boxed{\delta\,Df(\delta q)=x(q)^{-p}Df(q)^3.}
\tag{25}
$$
原 CM 坐标公式为
$$
x(\delta q)=-\frac{x(q)^3+4b}{3x(q)^2},\qquad
y(\delta q)=\frac{y(q)(x(q)^3-8b)}{\delta^3x(q)^3}.
\tag{26}
$$
将 (25)–(26) 代入 (20)，保留 $\delta^p=\delta$，得到全部逐球 norm-three：
$$
\boxed{
\begin{aligned}
a_{\bar\delta c}&=\delta\,a_cb_c,\\
b_{\bar\delta c}&=b_c^3+4b\,a_c^6,\\
h_{\bar\delta c}&=h_c(b_c^3-8b\,a_c^6).
\end{aligned}}
\tag{27}
$$
在 $c=0$，用 (21) 也逐项成立。当前 $b=17$ 时，
第二、三式的有理系数分别是 $68$、$136$。

## 5. 与真正原加法卷积同时比较

原全纯来源的完整身份为
$$
\sigma(\delta z)=\delta\sigma(z)\Theta(z),\qquad
\Theta(\delta z)=\Theta(z)^3+4b\sigma(z)^6,
$$
$$
C(\delta z)=C(z)\bigl(\Theta(z)^3-8b\sigma(z)^6\bigr),
\qquad C(z)^2=\Theta(z)^3+b\sigma(z)^6.
\tag{28}
$$
第一式是原 sigma division；后面三式由 (26) 和
$y^2=x^3+b$ 直接得到，含全部首项和相位。

因此它们在原有界测度中给真实加法卷积，例如
$$
[\delta]_*\nu_\sigma=\delta(\nu_\sigma*\nu_\Theta).
\tag{29}
$$
其余三式同样将来源乘法换成加法卷积，而不产生额外 period。

用 $*$ 表示有限加法群 $\mathbf F_p$ 上的卷积。由 (29)，
$$
s_{c/\delta}=\delta(s*t)(c).
$$
另一方面 (27) 第一式给
$$
s_{\bar\delta c}=\frac{\delta}{\lambda_\Theta}s_ct_{2c}.
$$
因 $\delta\bar\delta=3$，二者的准确比较是
$$
\boxed{(s*t)(3c)=\lambda_\Theta^{-1}s_ct_{2c}.}
\tag{30}
$$
没有省去左边的三，也没有省去右边的 $2c$。
这条式子连接了真正加法卷积与真正逐球乘法。

(22)、(27) 和 (28) 的有限卷积形式可以同时使用；它们中
$u_c$ 的绝对 $\lambda_C$ 始终按 (18) 保留。下节先推
(30) 对指定两族矩的完整乘法 Fourier 转置。

## 6. 全部循环项与准确零球质量

在本节以下公式中，$S_i,T_j$ 均表示原整单位矩的模 $p$ 约化：
$$
S_i=\int_{\mathbf Z_p^\times}x^{6i+1}\,d\nu_\sigma(x),
\qquad
T_j=\int_{\mathbf Z_p^\times}x^{6j}\,d\nu_\Theta(x),
\qquad 0\le i,j<s.
\tag{31}
$$
原 $\mu_6$ 型使其他乘法 Fourier 分量为零。特别
$$
\boxed{S_0=\Omega,\qquad T_0=1-\lambda_\Theta.}
\tag{32}
$$
第一式的非单位一阶矩有正赋值；第二式则必须扣除真实零球质量。
不能把 $T_0$ 改成全质量一。

在 $c\ne0$ 上，有限乘法 Fourier 反演给
$$
s_c=-\sum_{i=0}^{s-1}S_ic^{-(6i+1)},\qquad
t_{2c}=-\sum_{j=0}^{s-1}2^{-6j}T_jc^{-6j}.
\tag{33}
$$
负号来自 $(p-1)^{-1}=-1$，没有省去一个平均因子。

对 (30) 乘 $c^{6k+1}$ 后求和。原卷积 (29) 的同一矩为
$\delta^{6k}S_k$；将 $3c$ 换元产生 $3^{-(6k+1)}$。
再用 (33)，得到
$$
\boxed{
\sum_{\substack{0\le i,j<s\\i+j\equiv k\pmod s}}
  2^{-6j}S_iT_j
=-\frac{\lambda_\Theta}{3}
 \left(-\frac1{27}\right)^kS_k,
\qquad 0\le k<s.
}
\tag{34}
$$
这里用的是
$\delta^6/3^6=-1/27$；不是遗漏范数三后得到的 $-27$。

式 (34) 保留了 $i+j=k$ 与 $i+j=k+s$ 的全部项。
等价地，在 $k[W]/(W^s-1)$ 中，
$$
\mathscr S(W)=\sum_{i=0}^{s-1}S_iW^i,\qquad
\mathscr T(W)=\sum_{j=0}^{s-1}T_jW^j
$$
满足
$$
\boxed{
\mathscr S(W)\mathscr T(2^{-6}W)
=-\frac{\lambda_\Theta}{3}
 \mathscr S(-W/27).
}
\tag{35}
$$
因 $(-1/27)^s=\delta^{-(p-1)}=1$，右边是同一个循环代数中的合法自同构。

为与 R336 的原行明确比较，原普通正矩的三角关系也仍是
$$
\boxed{
(-27)^kS_k
=S_k+\sum_{i=0}^{k-1}
 \binom{6k+1}{6i+1}S_iT_{k-i},
\qquad 1\le k<s.
}
\tag{36}
$$
这里 $j=0$ 使用全质量一；其他 $j>0$ 才可用 $T_j$。
(34) 与 (36) 不能互相替代或混用常数项。

## 7. 一条对全部普通 p>7 为单位的 wrap

令 (34) 中 $k=0$。唯一不跨过 $s$ 的项是 $S_0T_0$。
保留 (32) 后，准确得到
$$
\boxed{
\sum_{j=1}^{s-1}2^{-6j}S_{s-j}T_j
=\left(\frac{2\lambda_\Theta}{3}-1\right)\Omega.
}
\tag{37}
$$

**右边对每个当前普通 $p>7$ 为单位。**
由 (7)，$\lambda_\Theta=1/\bar\pi_0$。若其括号为零模 $p$，则
$$
p\mid 3a_p(E_0)-2,
\qquad a_p(E_0)=\pi_0+\bar\pi_0\in\mathbf Z,
\tag{38}
$$
因为在选定普通素位 $\pi_0=0\bmod p$。

$E_0$ 有有理二挠点 $(-1,0)$，故每个好奇素数的
$\#E_0(\mathbf F_p)$ 为偶数，$a_p(E_0)$ 为偶数。
因此 (38) 的整数商 $(3a_p-2)/p$ 也为偶数。
另一方面 $p\ge13$，Hasse 界给
$$
|3a_p-2|\le6\sqrt p+2<2p.
\tag{39}
$$
最后一个不等式在 $p=13$ 已严格成立且左、右之差随 $p\ge13$ 增大。
所以该偶整数商只能为零；但 $3a_p=2$ 不可能。这证明单位性，
无需额外同余素数族或有限素数扫描。

因各项都是原整矩，(37) 还给精确的联合存在结论：
对每个普通 $p>7$，存在 $1\le j\le s-1$，使
$$
\boxed{
\int_{\mathbf Z_p^\times}x^{1-6j}\,d\nu_\sigma(x)
\quad\text{及}\quad
\int_{\mathbf Z_p^\times}x^{-6(s-j)}\,d\nu_\Theta(x)
\text{同时为单位。}
}
\tag{40}
$$
确实它们模 $p$ 分别等于 $S_{s-j}$、$T_j$，而单位和中至少
一项为单位。两个负阶的和是 $p-2$。
这是权随 $p$ 变化的联合结论，不用鸽笼把增长区间换成固定权。

## 8. 指定两个旧负矩究竟在何处

仍记原固定负矩
$$
I_\sigma=\int_{\mathbf Z_p^\times}x^{-5}\,d\nu_\sigma,\qquad
I_\Theta=\int_{\mathbf Z_p^\times}x^{-6}\,d\nu_\Theta.
\tag{41}
$$
Fermat 同余准确给
$$
I_\sigma=S_{s-1},\qquad I_\Theta=T_{s-1}\quad\bmod p.
\tag{42}
$$
原首系数
$$
\sigma=z+\frac b{210}z^7+\cdots,\qquad
\Theta=1-\frac{2b}{15}z^6+\cdots
$$
给
$$
S_1=24b\Omega^7,\qquad T_1=-96b\Omega^6.
\tag{43}
$$

当 $s\ge3$ 时，(37) 的两个端点因此准确展开为
$$
\boxed{
-\frac32b\Omega^6 I_\sigma
+1536b\Omega^7 I_\Theta
+\sum_{j=2}^{s-2}2^{-6j}S_{s-j}T_j
=\left(\frac{2\lambda_\Theta}{3}-1\right)\Omega.
}
\tag{44}
$$
空和取零。$s=2$ 时只有一个 $j=1$ 项，不能将其重复计为
两个端点；此时两个指定矩本来就是 (43) 的单位。

还可直接取 (34) 的最后一行 $k=s-1$。这一行没有 $i+j=k+s$ 项，
但保留 $T_0$ 后得到
$$
\boxed{
64\Omega I_\Theta
+\sum_{j=1}^{s-2}2^{-6j}S_{s-1-j}T_j
=(10\lambda_\Theta-1)I_\sigma.
}
\tag{45}
$$
这里 $2^{-6(s-1)}=64$，
$(-1/27)^{s-1}=-27$，故右端的 $10$ 是完整质量计算的结果。

R343/R349 的 Faber 记号与 (42) 保持原对应：
$$
I_\sigma=\Omega^{p-6}(p-6)!\,c_{s-1},\qquad
I_\Theta=\Omega^{p-7}(p-7)!\,d_{s-1}\quad\bmod p,
$$
$$
c_{s-1}=H^6[z^{-6}]P(x(z)^3),\qquad
d_{s-1}=H^6[z^{-p-7}]x(z)T_P(x(z)^3).
\tag{46}
$$
所以 (44)–(45) 确实作用于原指定线性 Faber 行 $\alpha_1$
与原完整二次行，而非核多项式的底部系数。

若这两个指定矩同时为零，(45) 的中间和必须为零，
而 (44) 的中间和必须等于已证明的单位。
目前尚未从完整 Hirota／norm-three 系统排除这两件事同时成立。
尤其不能由 (37) 的单位右端只挑出 $j=1$ 或 $j=s-1$，
不能把 R349 的临界 $pt_0=-H$、$y^p$ 修正或其它完整 Faber carry
在后续消元时省略。

本篇提供的是同一原核上的新完整联立及联合单位行 (34)–(40)。
固定两负矩的无穷素数非零，以及原秩二曲线的完整中央导数非零，
仍待后续真实算术消元。

## 仓库输入

- [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：原 sigma/Theta、同一普通周期及完整 core。
- [R332](R332-fixed-negative-original-moments-actual-soule-classes-and-reflected-root-signs.md)：两条固定负矩和 $E_0$ 的真实周期／core 比较。
- [R336](R336-ordinary-original-zeta-as-verschiebung-and-two-full-negative-rows.md)：真实 AS 覆盖、$D^p=HD$、核多项式及完整 norm-three。
- [R343](R343-original-three-torsion-phase-and-two-complete-faber-observers.md)、[R349](R349-critical-faber-cubic-row-and-complete-norm-three-projections.md)：原两条完整 Faber 观察及临界 carry。
- [R345](R345-original-degree-three-absolute-core-phase-and-middle-cartier-row.md)：$C=y\sigma^3$ 的绝对 core。
- [R376](R376-original-additive-ball-theta-group-formula-and-integral-torsion-values.md)：原 Fourier 标签、全部整 frame 和精确逐球公式。
