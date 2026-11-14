# R376：原加法小球的整 theta 群公式、挠点值与逐球单位

日期：2026-11-14。**状态：以下完整 Fourier 小球公式、真实整 theta
群传送、原 $S$ 的全部非原点小球单位、$D_7$ 的全部小球单位，以及
$\mathcal E_{56}$ 的有限坏类和统一深层单位均已证明。**
原 $p^{-n}$、division 函数的首项、原周期以及完整 core 标量全部保留。
本篇不把这些非零加法观察等同于原 principal 对数聚合非零。

## 1. 原对象与准确结论

固定本课题的
$$
E=E_{17}:y^2=x^3+17,\quad
K=\mathbf Q(\omega),\quad\delta=1+2\omega,\quad\gamma=3+\omega,
$$
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\sigma=z+\cdots,\quad dz=dx/(2y).
$$
取普通 $p>7$、原
$$
\pi=\psi_{17}(\mathfrak p),\quad
\bar\pi=\psi_{17}(\bar{\mathfrak p}),\quad
\pi\bar\pi=p,\quad \kappa=p/\bar\pi^2.
\tag{1}
$$
原形式群同构固定为
$$
\beta:\widehat{\mathbf G}_m\longrightarrow\widehat E,\qquad
\beta^*dz=\Omega_p\,dT/(1+T).
\tag{2}
$$
其选择与 R295、R300、R316 相同，后文不另换周期。

对 $G=\sigma^d f_G\in\mathcal S_d=\sigma^d L(dO)$，
设原整有界测度的完整 core 已经独立证明：
$$
\nu_G|_{p\mathbf Z_p}=\lambda_G[\kappa]_*\nu_G,
\qquad \lambda_G\in\mathcal O_p^\times.
\tag{3}
$$
本篇实际使用的 $d$ 是 $1,2,7,34,56$，均与当前 $p$ 互素。
设 $n\ge1$，记
$$
m=p^n,\qquad a=\pi^n,\qquad b=\bar\pi^n,\qquad ab=m.
\tag{4}
$$
这里 $b$ 仅在本篇同源公式中表示 $\bar\pi^n$；
曲线的常数项始终写作 $17$。

对于任一奇范数 CM 元素 $h$，保持原 division 函数
$$
r_h(z)=\frac{\sigma(hz)}{\sigma(z)^{Nh}},
\qquad r_h(z)=h\,z^{1-Nh}+\cdots.
\tag{5}
$$
特别不除去其首项 $h$，也不改成 monic 多项式。

第3节将用 (2) 与真实 theta 群明确指定一个双射
$$
c\bmod p^n\longleftrightarrow q_c\in E[\bar\pi^n],
\qquad q_0=O.
\tag{6}
$$
若 $c\ne0\bmod p^n$，则准确公式为
$$
\boxed{
\nu_G(c+p^n\mathbf Z_p)
=\lambda_G^n
 \left(\frac{b\,r_a(q_c)}{D r_b(q_c)}\right)^d
 f_G(aq_c),\qquad D=d/dz.
}
\tag{7}
$$
所有函数、导数和同源都在同一原模型及微分上。
$p^{-n}$ 的整个 Fourier 和已包含在证明中；
(7) 不是未经规范的裸 theta 值。
因子
$$
\boxed{b\,r_a(q_c)/D r_b(q_c)\in\mathcal O_p^\times}
\tag{8}
$$
是真正的单位。
原点小球则是
$$
\boxed{\nu_G(p^n\mathbf Z_p)=\lambda_G^nG(0).}
\tag{9}
$$

以下直接推论与原目标来源有关：

1. 对原
   $$
   S=-\frac1{84}
   \sigma(z)\sigma(2z)\sigma(\delta z)\sigma(2\delta z)
   \sigma(\gamma z)\sigma(\bar\gamma z),
   $$
   每个 $c\ne0\bmod p^n$ 的 $\nu_S(c+p^n\mathbf Z_p)$ 都是单位，
   而 $\nu_S(p^n\mathbf Z_p)=0$。
2. 对 $D_7=-\sigma^7x^2y$，每个 $c\bmod p^n$ 的小球质量都是单位。
   $\Theta=x\sigma^2$ 同样如此；$\sigma$ 的全部非原点小球也是单位。
3. 对 R367 的实际 $\mathcal E=\mathcal E_{56}$，每层至多有五十六个
   非单位小球。事实上其数为六的倍数、至多五十四。
   对所有 $n>56$ 和所有 $c\in\mathbf Z_p^\times$，
   $$
   \boxed{\nu_{\mathcal E}(c+p^n\mathbf Z_p)\in\mathcal O_p^\times.}
   \tag{10}
   $$
   这些结论对全部当前普通素数成立，不只对 R370 的共同子族。

## 2. 原 division 同构在整模型上的全部常数

在包含原普通系数和所需 étale 挠点的严格 Hensel 完备无分歧
离散赋值环 $R$ 上工作。$\mathscr E/R$ 是原椭圆曲线的好约化模型。
$[a]$ 的核连通，$[b]$ 的核 étale；二者在 $E[m]$ 中互补。
令
$$
\mathscr L=\mathcal O_{\mathscr E}(dO),\qquad
\mathscr L_a=[a]^*\mathscr L,\qquad
\mathscr L_b=[b]^*\mathscr L.
$$
用 $\mathbf1_a,\mathbf1_b$ 表示相应的标准有理截面。
原 (5) 给实际同构
$$
\boxed{
\Phi:\mathscr L_b\longrightarrow\mathscr L_a,\qquad
\Phi(\mathbf1_b)=\rho^d\mathbf1_a,\qquad
\rho=r_b/r_a.
}
\tag{11}
$$
其除子恰为 $d[b]^*O-d[a]^*O$。
R300、R368 已支付奇范数的原 sigma 半特征，因此 (11)
没有额外平坦扭转。

必须核对 (11) 的 vertical 因子。
在 $O$，
$$\rho(O)=b/a,$$
确有赋值 $-n$；不能直接将它称为单位或手动除掉这个常数。

取实际整参数 $t=-x/y$。两个拉回的整局部基是
$$
e_a=t([a]P)^{-d}\mathbf1_a,\qquad
e_b=t([b]P)^{-d}\mathbf1_b.
$$
在这些基中 (11) 的系数准确为
$$
\boxed{
\frac{\Phi(e_b)}{e_a}
=\left(\rho(P)\frac{t([a]P)}{t([b]P)}\right)^d.
}
\tag{12}
$$
其常数不是 $b/a$，而是
$$
(b/a)^d(a/b)^d=1.
\tag{13}
$$
这里的第二因子是拉回整局部基本身的变化，不是重新规范
$\Phi$ 的标量。

更强地，原 Mazur–Tate sigma 为
$$
\Sigma(t)=\sigma(\log_Et)\in tR[[t]],\qquad \Sigma(t)/t\in1+tR[[t]].
$$
真实 division 恒等式给
$$
\rho(P)\frac{t([a]P)}{t([b]P)}
=
\frac{\Sigma([b]P)/t([b]P)}
     {\Sigma([a]P)/t([a]P)}\in R[[t]]^\times.
\tag{14}
$$
故 (11) 在形式邻域已经是整同构。
它在泛纤维没有其他零极；光滑整模型的特殊纤维不可约，
任何可能的 vertical 除子只能是该纤维的整数倍。
(13)–(14) 迫该整数为零，所以**原来的** $\Phi$ 在整个整模型上
是同构。

定义原形式 theta frame
$$
\epsilon=\Sigma(t)^{-d}\mathbf1,\qquad
\epsilon_a=[a]^*\epsilon,\quad\epsilon_b=[b]^*\epsilon.
$$
(14) 所包含的准确强式是
$$
\boxed{\Phi(\epsilon_b)=\epsilon_a.}
\tag{15}
$$
本篇所有平均和纤维求值都使用 (15)；
没有丢弃 $(b/a)^d$，也没有改变原 trace 或 $\lambda_G$。

## 3. 真正的两个 deck lifts 与小球标签

置
$$K_a=E[a],\qquad K_b=E[b].$$
$\mathscr L_a$ 有 $K_a$ 的 canonical deck 作用，记作 $A_t$。
$\mathscr L_b$ 有 $K_b$ 的 canonical deck 作用；经原 (11) 传送后，
在 $\mathscr L_a$ 上记作 $B_q$。
它们是整线丛同构，阶数就是相应平移的阶数。
没有从 projective 作用另挑根单位。

具体地，若截面在标准有理 frame 中写成 $F(P)\mathbf1_a$，则
$$
A_tF(P)=F(P+t),\qquad
\boxed{B_qF(P)=\frac{\rho(P)^d}{\rho(P+q)^d}\,F(P+q).}
\tag{16}
$$
这完整指定了绝对相位。两个作用的交换子定义为
$$
A_tB_q=e(t,q)B_qA_t.
\tag{17}
$$
由 (16)，它也等于独立于 $P$ 的有理式
$$
\boxed{
e(t,q)=
\left(\frac{\rho(P+t)\rho(P+q)}
           {\rho(P+t+q)\rho(P)}\right)^d.
}
\tag{18}
$$

配对 $K_a\times K_b\to\mu_m$ 是完美的。
为核定这一点，$\mathscr L_a$ 的 degree 是 $dm$。
theta 群交换子在 $E[m]$ 上是通常 $m$-Weil 配对的 $d$ 次幂。
这也直接由原 sigma 准周期和 Legendre 关系得到：
在周期辛基中，对
$t=(u_1\omega_1+u_2\omega_2)/m$、
$q=(v_1\omega_1+v_2\omega_2)/m$，
交换子为
一个 primitive $m$ 次根的 $d(u_1v_2-u_2v_1)$ 次幂。
这里用这个周期计算核定非退化性；后文的绝对根单位、
方向和标签均由 (16)、(18)、(20) 的实际有理公式指定，
不另选一个 Weil 配对符号。
$K_a,K_b$ 是互补循环直和因子，而 $p\nmid d$，
故限制配对仍完美。这个证明包含中心，不只使用两个底层平移。

原 (2) 在连通核上给 $\mu_m\simeq K_a$。
因为 $b$ 在该核上可逆，定义实际字符
$$
\zeta_b(t)=1+\beta^{-1}([b]t)\in\mu_m,\qquad
\chi_c(t)=\zeta_b(t)^c.
\tag{19}
$$
现在 (6) 的准确定义是
$$
\boxed{e(t,q_c)=\chi_c(t)\quad\text{对全部 }t\in K_a.}
\tag{20}
$$
完美配对保证存在、唯一及可加性。
这是真正的原 Fourier 标签，不是事后任意排列小球。
特别
$$
\operatorname{ord}(q_c)
=\operatorname{ord}(aq_c)
=p^{\,n-v_p(c)}
\quad(c\ne0\bmod p^n).
\tag{21}
$$
$[a]$ 在 $K_b$ 上是自同构。特殊纤维上 $K_b$ 仍 étale，
所以约化保持 (6) 的一一对应及 (21) 的精确阶数。

## 4. 保留完整 Fourier 和后得到原小球公式

令 $s_G=f_G\mathbf1$ 是实际代数截面，置
$$h=\Phi[b]^*s_G\in H^0(\mathscr E,\mathscr L_a).$$
由构造，
$$B_qh=h\qquad(q\in K_b).$$
在 $\epsilon_a$ frame 中，(15) 使其形式函数恰为原
$\widehat G([b]P)$。

在泛纤维定义完整投影
$$
P_c=\frac1m\sum_{t\in K_a}\chi_c(t)^{-1}A_t.
\tag{22}
$$
这就是原 $p^{-n}$ 平均，没有先删掉任何支。
在 $\beta(T)$ 坐标中，$[b]$ 是 $(1+T)^b-1$，
而 $[b]t$ 对应 $\zeta_b(t)$。
因此 $P_ch$ 的形式函数准确为
$$
\boxed{
\int_{c+p^n\mathbf Z_p}(1+T)^{bx}\,d\nu_G(x).
}
\tag{23}
$$
尤其在 $O$ 的值是所求小球质量。

对 $c=0$，现在使用已经独立证明的完整 (3)：
$$
\begin{aligned}
(P_0h)(\beta(T))
&=\lambda_G^n\int(1+T)^{b\kappa^nx}\,d\nu_G(x)\\
&=\lambda_G^n\int(1+T)^{ax}\,d\nu_G(x),
\end{aligned}
$$
其中 $b\kappa^n=a$ 完全准确。
故形式函数及全局截面同时满足
$$
\boxed{P_0h=\lambda_G^n[a]^*s_G.}
\tag{24}
$$
全局相等由同一泛纤维上的形式展开相等得到。
(24) 没有另猜一个 norm-$p^n$ trace 的标量。

由 (17)、$B_qh=h$ 及 (20)，
$$
B_{q_c}P_0h
=\frac1m\sum_t e(t,q_c)^{-1}A_th=P_ch.
$$
所以
$$
\boxed{P_ch=\lambda_G^n B_{q_c}[a]^*s_G.}
\tag{25}
$$
右边的整传送已经在 §2 付清，这同时说明原 (22) 的分母
如何在全部非平凡字符上消掉。

为得到没有未知 sigma 点值的实际公式，取 $q=q_c\ne O$。
由 (16)，(25) 在 $\epsilon_a$ frame 中是
$$
\lambda_G^n
\left(\frac{\Sigma([a]P)\rho(P)}{\rho(P+q)}\right)^d
 f_G([a]P+aq).
$$
原 division 恒等式给 $\Sigma([a]P)\rho(P)=\Sigma([b]P)$。
在 $P\to O$ 时
$$
\Sigma([b]P)=bz+\cdots,\qquad
\rho(P+q)=\frac{D r_b(q)}{r_a(q)}z+\cdots.
$$
于是 (7) 得证。
这里 $D r_b(q)$ 保留实际周期与相位；
没有将它未经证明替成 $b/\sigma(q)^m$。
$q=O$ 的 (25) 则直接给 (9)。

### 4.1 因子确实是单位

$r_a$ 的约化没有非原点零极，因为 $[a]$ 的特殊纤维是纯
Frobenius 同源。它的 vertical 赋值为零：
在原形式群中
$\Sigma([a]P)/\Sigma(P)^m$ 的约化是非零常数，
其最低项由 $[a]t$ 的 Frobenius 首项给出。
因此 $r_a$ 在每个非零 étale $q\in K_b$ 都是单位。

$r_b$ 的约化有且仅有那些非零 étale 核点的简单零，
极点在 $O$。
其原首项 $b$ 是单位，没有 vertical 因子。
$d z$ 是好约化处的非零不变微分，所以
$D r_b(q)$ 在这些简单零处为单位。
$b$ 也是单位，证明 (8)。

这也可从 §2 的整 $B_q$ 纤维同构看出，但以上计算另外把
单位因子写成了固定 division 函数的明确代数式。

## 5. 本篇来源的原积分格

公式 (7) 使用全局整截面，不能只知道某个复 Taylor 系数。
这里该条件由原来源完整支付。

对于 $\mathcal O(dO)$，标准有理基为
$1,x^i,yx^j$ 中极阶不超过 $d$ 的那些项。
乘 $\Sigma(t)^d$ 后，首阶分别覆盖
$0,1,\ldots,d$ 中除 $d-1$ 外的全部阶，
首系数为 $\pm1$，其余正式系数均整。
因此任何属于该固定 theta 空间、且原形式展开整的截面，
按互异首阶消元后的全部基系数都整。
这是 R300 的原整格论证，逐字适用于当前 $d$。

$\sigma,\Theta,D_7,S$ 的原整性已分别在 R316、R368、R300 给出。
$\mathcal E_{56}$ 的原整性来自 R367 的实际三输入有界核
$$
\nu_{\mathcal E}
=\frac1{12\delta\Omega_p^3}
 R_*(Y_A^3\,\nu_\sigma^{\otimes3});
$$
分母在当前素数处是单位。
其形式展开在同一个 $\mathcal S_{56}$ 中，故上述消元证明
它是完整的整截面，而非仅一个有界局部函数。

这些截面都由固定的有理模型定义。
对于 $\mathcal E$，这一点也可不用另读多项式：
R367 的
$$
\mathcal E(w)=\frac1{2\delta}[z^3]\,
 \sigma(z-7w)\sigma(2(z+w))\sigma(\delta(z+w))
$$
中，用
$\sigma(2u)\sigma(\delta u)=-2\delta\sigma(u)^7x(u)y(u)$，
$\delta$ 准确消掉。
所以全部系数在 $\mathbf Q$，并由上述整格在特殊纤维上
给出 $\mathbf F_p$ 定义的非零截面。
$\mathcal E(O)=1$ 保证其约化不恒零。

## 6. 原 S、sigma、Theta 与 D7 的逐球单位

### 6.1 原目标来源 S

原六因子乘法身份已经在 R297、R333 支付，其完整零除子为
$$
\boxed{
\operatorname{div}_0(S)
=[1]^*(O)+[2]^*(O)+[\delta]^*(O)+[2\delta]^*(O)
 +[\gamma]^*(O)+[\bar\gamma]^*(O).
}
\tag{26}
$$
总 degree 为
$1+4+3+12+7+7=34$。
全部支撑都属于固定的二、三、七挠点。
$S$ 的原点零阶为六、首项为一，故没有额外 vertical 标量；
$1/84$ 对当前素数也是单位。

对 $c\ne0\bmod p^n$，点 $aq_c$ 及其约化都有非平凡 $p$ 幂阶。
它们不可能属于 (26) 的 prime-to-$p$ 支撑。
好约化在固定 prime-to-$p$ 挠群上单射，
所以此处不仅特征零值非零，而且整截面值确是单位。
再用 (7)、(8) 和 R300 的 $\lambda_S=\bar\pi^{-1}$，
得到
$$
\boxed{
\nu_S(c+p^n\mathbf Z_p)\in R^\times
\quad(c\ne0\bmod p^n),\qquad
\nu_S(p^n\mathbf Z_p)=0.
}
\tag{27}
$$

### 6.2 三条低 degree 来源

$\sigma$ 的零除子只有 $O$，故它的全部非原点小球质量是单位，
原点小球为零。

令 $Q_\pm=(0,\pm\sqrt{17})$。原
$\Theta=x\sigma^2$ 的零除子为 $Q_++Q_-$；
这些是三挠点而非原点。
所以其所有小球质量，包括原点小球，都是单位。

原 $D_7=-\sigma^7x^2y$ 的零除子准确是
$$
\boxed{
2Q_++2Q_-+
 \sum_{T\in E[2]\setminus\{O\}}T.
}
\tag{28}
$$
它同样避开整个 étale $p$-primary 子群的约化。
$D_7(O)=1$，原 $\lambda_7$ 是单位。
故
$$
\boxed{\nu_{D_7}(c+p^n\mathbf Z_p)\in R^\times
\quad\text{对全部 }c\bmod p^n.}
\tag{29}
$$
这里使用的是真正截面的完整除子、原 Fourier 标签及整纤维，
没有单凭复零点支撑就预支一个未经规范的小球结论。

## 7. E56 的坏类界与统一深层单位

固定 $n$。由 (7)、(8)，非原点小球非单位，恰当且仅当
$\overline{s_{\mathcal E}}$ 在约化点 $\overline{aq_c}$ 为零。
这些点按 (6)、(21) 互不相同。
非零整截面 $\overline{s_{\mathcal E}}$ 的零除子总 degree 是五十六，
故每层至多五十六个坏类。原点类由 (9) 为单位。

$\mathcal E$ 为 $\mu_6$ 型零，原测度在 $\mu_6$ 缩放下不变。
所以坏类按 $\mu_6$ 组成轨道。
非零 $c\bmod p^n$ 的这些轨道均长六，因为 $p>3$ 时任意
$\zeta\ne1$ 的 $\zeta-1$ 是单位。
因此坏类数实际至多五十四。

还有一个不依赖目标素数扫描的统一深层界。
若 $c$ 为单位且是坏类，$\overline{aq_c}$ 是一个精确阶数
$p^n$ 的零点。
该零点作为 $\mathbf F_p$ 定义的 degree 五十六除子的支撑点，
定义在某个 $\mathbf F_{p^e}$ 上，其中 $e\le56$。
于是
$$p^n\mid\#E(\mathbf F_{p^e}).$$
即使用最粗的点数界，也有
$$
\#E(\mathbf F_{p^e})\le2p^e+1<p^{e+1}\quad(p>3).
$$
所以 $n\le e\le56$。
这证明 (10)。更一般地，
$$
\boxed{
\nu_{\mathcal E}(c+p^n\mathbf Z_p)\notin R^\times
\ \Longrightarrow\
n-v_p(c)\le56
\quad(c\ne0\bmod p^n).
}
\tag{30}
$$
这里没有假设 $\mathcal E$ 的特征零零点都是挠点；
其真实 degree 和 $\mathbf F_p$ 定义已经足够。
浅层坏类继续完整保留。

## 8. 原叶平均的真正单位权与可用逆小球权

采用 R367 的原坐标
$$
Y_A=X_1+2X_2+\delta X_3,\quad
Q=\delta X_2+2X_3,\quad
R=2X_2+\delta X_3-7X_1.
$$
其整个联合已经证明为
$$
\mathsf P_Q\mathsf P_R(Y_A,Q,R)_*\nu_\sigma^{\otimes3}
=\nu_A\otimes\nu_{D_7}\otimes\nu_{\mathcal E},
\tag{31}
$$
其中 $A=\sigma(z)\sigma(2z)\sigma(\delta z)$。
R367 六支并是
$$
\mathcal U_N=
\{Y_A\text{ unit},\,Q\in p^N,\,
 R+7\xi^{-1}Y_A\in p^N\text{ 对某个 }\xi\in\mu_6\}.
$$
它对两个实际辅助投影不变，六支两两不交。
其原权仍为
$$
w_N(y)=6\lambda_7^N\nu_{\mathcal E}(-7y+p^N).
$$
所以 (10) 给
$$
\boxed{w_N(y)\in R^\times
\quad(N\ge57,\ y\in\mathbf Z_p^\times).}
\tag{32}
$$
原点总质量与单位总质量均没有被用来替代这个平移球。

现在可以合法构造一个**实际辅助权**
$$
\boxed{
g_N(r)=
\begin{cases}
\nu_{\mathcal E}(r+p^N)^{-1},&r\in\mathbf Z_p^\times,\\
0,&r\in p\mathbf Z_p.
\end{cases}
}
\tag{33}
$$
它有界、整、模 $p^N$ 局部常数，且 $\mu_6$ 不变。
在每个单位小球上，它把该小球质量准确变为一。
因此其完整总质量为
$$
\boxed{\int g_N\,d\nu_{\mathcal E}
       =(p-1)p^{N-1}.}
\tag{34}
$$
这个数在 $N>1$ 时不是单位，不能再删掉 $p^{N-1}$。

(31) 与所有原部分输出一起给两个真正的式子：
$$
\boxed{
(Y_A)_*\bigl(1_{\mathcal U_N}g_N(R)\nu_\sigma^{\otimes3}\bigr)
=6\lambda_7^N\,\nu_A^\times,
}
\tag{35}
$$
而仅限制辅助 $Q\in p^N$、保持全部 $R$ 的对应输出是
$$
\boxed{
(Y_A)_*\bigl(1_{Q\in p^N}g_N(R)\nu_\sigma^{\otimes3}\bigr)
=\lambda_7^N(p-1)p^{N-1}\nu_A.
}
\tag{36}
$$
(35) 的证明在给定 $y$ unit 后，只是六个不同单位小球各贡献一；
$Q$ 深球贡献 $\lambda_7^N$。
这是原辅助-only 权，不是在未知中央行上另做除法。

若接回其余三个原输入与
$Y_B=2\delta X_4+\gamma X_5+\bar\gamma X_6$，
原 $\eta_6=-\nu_\sigma^{\otimes6}/84$ 使 (35) 成为
$$
\boxed{
\int_{\mathcal U_N}g_N(R)\Phi(Y_A+Y_B)\,d\eta_6
=-\frac{\lambda_7^N}{14}
 \int_{y\ {\rm unit}}\!\int\Phi(y+Y_B)
       \,d\nu_A(y)d\nu_\sigma^{\otimes3}.
}
\tag{37}
$$
任何实际其余输入限制也可一同保留。
相应的 (36) 对同一整个输出则是
$$
\boxed{
\int_{Q\in p^N}g_N(R)\Phi(Y)\,d\eta_6
=\lambda_7^N(p-1)p^{N-1}\int\Phi\,d\nu_S.
}
\tag{38}
$$
可在两式使用原全部 tame Mellin 测试及其中央导数。

(37)、(38) 支付了新的非退化辅助滤波。
它们的积分域不同：原另外五支以及 $\mathcal U_N$ 的补域仍存在。
即使原 $J'_S(0)=0$，(38) 的零也只给 (37) 与其补域相消，
不允许单独将 (37) 置零。所有部分输出和这个剩余量词在本篇保持。

## 9. 对原中央观察的实际范围

(27) 已证明原测度在每个非原点有限加法小球上都原始，
它比仅证明测度不恒零更具体。
但原 principal 中央导数是
$$
J'_S(0)=(p-1)\int_{\mathbf Z_p^\times}\log_p\langle x\rangle\,d\nu_S(x).
$$
有限层的准确近似仍为
$$
(p-1)\sum_{c\in(\mathbf Z/p^n)^\times}
  \log_p\langle\widetilde c\rangle\,
       \nu_S(c+p^n\mathbf Z_p),
$$
并按原连续积分极限读取。
(7) 为其中每一个质量给出完整代数挠点公式；
它不把这些带对数的项的聚合当成一个单独的非零项。

本篇提供的是同一原中央核可直接使用的全小球公式、
真实单位界及 (37)–(38) 的原辅助权。
主目标的跨素数中央非零仍须通过这些准确关系继续证明。

## 依赖与提交

- [R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)：
  原 division、整 theta 格、原 $S$ 的完整 core。
- [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：
  同一 MT sigma、原周期、低次完整 core。
- [R333](R333-six-original-sigma-inputs-and-two-quadratic-negative-moment-return.md)：
  原六 sigma 来源与全部原系数。
- [R367](R367-original-degree-seven-fifty-six-joint-and-translated-leaf-balls.md)：
  实际 $\mathcal E$、整有界核、两个投影及六支叶域。
- [R368](R368-original-degree-seven-absolute-core-and-fixed-prime-unit-tubes.md)、
  [R374](R374-original-degree-seven-reciprocity-fixed-sextic-curves-and-periods.md)：
  七次原相位、两个固定角色及准确周期比较。
- [R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)：
  原来源与其固定乘法除子。

本条以 GitHub Contents API 提交小文本；没有声称本地执行 git pull。
提交前两 README 已逐文比较，均与已读基准
35e391cd9a73d5a514d252312d3ff61962ddbc70 相同；
内容 blob 仍为 f787a306d90892d8dec765dc59747d60ba39f055、
f8dd8071ac0c2b31f344a40c15ac2a42796bf9af。
核心同步记录由根代理维护。
