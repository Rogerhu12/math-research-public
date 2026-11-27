# 原 psi4 双核的 canonical 正槽与 degree102 负槽

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**状态：本文的完整有限角色、局部向量、原 canonical 正槽、
wild3 负槽、两条三挠 Weyl 译像及其 degree102 多项式已证明。
这是新的 weight3 几何输入；不是把原十八阶最高线改名。
原 canonical 坏条件只控制后续同一单参数族的指定斜率。
本文不预付该斜率非零或通常全 Sha 结论。**

## 1. 必须同时更换的有限角色

令 $K=\mathbf Q(\omega)$、$\delta=1+2\omega$，
$\delta^2=-3$，并保持 R290 的原加性角色和微分。
记 $\psi_0,\psi_4$ 分别为 $y^2=x^3+1$ 与
$y^2=x^3+4$ 的 Hecke 角色；$\psi_k$ 对应
$y^2=x^3+17^k$，$k=1,3,5$。
下标4在这里指方程常数4，不指 $17^4$。
令 $\nu$ 为相应 unitary avatar，并置
$$
\eta_k=\psi_k/\psi_4,\qquad
\pi_4=\operatorname{AI}_{K/\mathbf Q}(\nu_4^2),\qquad
\chi_k=\eta_k\nu_4^{-1}=\nu_k\nu_4^{-2}.
\tag{1}
$$
R991 的实际同构 $I_4(x,y)=(t^2x,2y)$、$t^3=2$，
与 R306 的完整六次剩余公式共同确定(1)，不只确定无穷型。

以下均是 **idèle 单位值**；主理想值与它们互逆：
$$
\begin{array}{c|ccc|c}
 &\nu_4&\nu_k&\eta_k&\chi_k\\ \hline
\mathcal O_{K,2}^{\times}&\epsilon_2^{-1}&\epsilon_2&
 \epsilon_2^{-1}&1\\
2&-1&-1&1&-1\\
\mu_6\subset\mathcal O_{K,3}^{\times}&u^{-1}&u^3&
 u^4&u^{-1}\\
\delta&i&-i&-1&i\\
\mathcal O_{K,17}^{\times}&1&u^{48k}&u^{48k}&u^{48k}\\
17&-1&-1&1&-1 .
\end{array}
\tag{2}
$$
所有未写的主单位由原导子决定。
$\eta_k$ 恰有阶6；它可由实际六次扭曲
$17^k/4$，或等价整代表 $16\cdot17^k$，定义。
三个有限域都包含在同一个原 full306 CM torsion 扩张中；
其中的 $t$ 已由原3挠点坐标支付。

原 Rankin 参数在 $K$ 上分解为
$$
\left.\pi_4\right|_{W_K}\otimes\chi_k^{-1}
 =
 \underbrace{\nu_4^4\nu_k^{-1}}_{\lambda_k^{\rm u}}
 \ \oplus\ \underbrace{\nu_k^{-1}}_{\beta_k^{-1}},
\qquad
\lambda_k=\psi_4^4/\psi_k,\quad\beta_k=\psi_k .
\tag{3}
$$
特别 $k=1$ 的 positive 因子就是原 rank2 曲线的 $\psi_{17}$。
$\lambda_1$ 的全有限表为
$$
\begin{array}{c|cc}
 &\text{单位}&\text{uniformizer}\\ \hline
2&\epsilon_2&-1\\
3&u^{-1}&i\text{ 于 }\delta\\
17&u^{-48}&-1 .
\end{array}
\tag{4}
$$
它的无穷型为 $(3,0)$、导子 $34\delta^2$，
weight4 theta level 为31212。
这是一个新最高表示；不能将其写成原
$\psi_0^3\eta_j^{-1}$ 的十八阶家族。
由 $\psi_4^3=\psi_0^3$，
$\lambda_k=\psi_0^3\eta_k^{-1}$；这个等式仍保留(2)的
wild3 部分。

## 2. 新局部 Hom 确实全部匹配

在2处，$\pi_{4,2}$ 是原 depth-zero supercuspidal，
其 $\mathrm{GL}_2(\mathbf F_2)=S_3$ 类型为 sign。
sign 在非裂 torus $C_3=\mathbf F_4^\times$ 上平凡，
恰与(2)的 $\chi_{k,2}$ 相符；uniformizer2是中心，
两边均为 $-1$。
所以支撑在 $\mathbf Q_2^\times\mathrm{GL}_2(\mathbf Z_2)$
的原 compact-type 向量有非零 toric functional。
这里使用真正 full2 标记及 sign，不能用旧
$\pi_{27,2}$ 的三个二商 wavelet 冒替。

在3处，$\nu_{4,3}^2=(\nu_{27,3}^2)^c$，
包括单位与 $\delta$，故
$$
\pi_{4,3}\simeq\pi_{27,3}.
$$
而新 $\chi_{k,3}$ 的完整表恰是 R991(20) 的
$u^{-1},\delta\mapsto i$。因此同一个
$$
I^+=\left\{\begin{pmatrix}a&b\\3c&d\end{pmatrix}:
a,d\in1+3\mathbf Z_3\right\},\quad
\Lambda\!\left(\begin{pmatrix}a&b\\3c&d\end{pmatrix}\right)
=\omega^{b-c},\quad\Lambda(\delta)=i
\tag{5}
$$
及 $J=\mathbf Q_3^\times I^+\sqcup
\delta\mathbf Q_3^\times I^+$ 给实际支撑在 $J$ 的向量。
R991 的全部 Mackey 陪集已经证明该向量位于正确的表示、
全 toric Hom 为一维，非只检查一个候选。
旧 E4 的3处 Hom 为零结论使用的是旧 $\eta_j$；
它的单位型为 $u$，不适用于(2)。

在17处，$\pi_{4,17}$ unramified，$\chi_{k,17}$ 的导子为1。
在原 $\mathbf P^1(\mathbf F_{17})$ 模型中取
$$
v_{17,k}=\sum_{\tau\in C_{18}}
 \chi_{k,17}(\tau)^{-1}e_{\tau\infty}.
\tag{6}
$$
这是非零特征向量；三条角色的阶分别为6、2、6，均非平凡。
全部18项仍须保留。其余有限位用原 unramified 或 split
Kirillov 向量。

无穷处 $\pi_4$ 为最低权3，toric 角色的权为1，
所以匹配的是 division algebra 的无穷处；
全 Rankin 符号为 $-1$。原 $\beta_1=\psi_{17}$ 的符号为
$+1$，且 R290 已付其中央值为零。因此 $\lambda_1$ 的符号为
$-1$，而完整 Rankin 中央零阶至少3。
这说明不能期待由普通的一阶 Gross–Zagier 端点自动取得
新非零值；本文构造的是指定权族及其零真空斜率。

## 3. positive 槽是原 S，不是另一条同角色来源

保持原 Hermitian 类 $\alpha=17$ 和
$G=51\sqrt3$。R306 已给三条完整有限函数
$$
\phi^+_{k,2}=f_A+t_+f_B,\quad
\phi^+_{k,3}=\mathbf1_{3^{-1}\mathbf Z_3},\quad
\phi^+_{k,17}=\sum_a f_k(a)\mathbf1_{a/17+\mathbf Z_{17}},
\tag{7}
$$
其中 $f_k$ 是原刚性化 Weil projector 的实际向量，
17处标签依次为 $j=12,0,6$，并非任取 eigenvector。
R290/R306 的原 Fourier 支撑、Gaussian 与 R297 的完整
十三点 trace 唯一识别(7)为
$$
S,\ H_3,\ H_5 .
$$
在同一个 $b=1$ 模型中
$$
S=\sigma^{34}R_S(x),\qquad
R_S=\frac{x^2}{7}(X+1)(X-8)(7X^2-4X+16),
\quad X=x^3,
\quad [z^6]S=1 .
\tag{8}
$$
其 CM13 值为 $-1$，并且是原完整质量观测的唯一核。
R306/R307 已付 $H_3,H_5$ 的非零中央质量与完整
同方程周期尺度；不重新计算它们，也不把它们的未知
权导数设为零。

固定 weight3 split character $\nu_4^2$，沿已付双核的
$\mu=\nu_0$ 规范，两个 rank-one characters 为
$$
\widetilde\alpha_{1,k,n}
 =\eta_k^{-1}\nu_4^{-(2n+1)}\nu_0,\qquad
\widetilde\alpha_{2,k,n}
 =\eta_k\nu_4^{2n+5}\nu_0 .
\tag{9}
$$
其乘积准确为 $(\nu_4^2\nu_0)^2$，是实际 seesaw 的
相容条件。
两个 Hecke 因子分别为
$$
\eta_k\psi_4^{2n+1},\qquad
\eta_k\psi_4^{2n+5}.
\tag{10}
$$
当 $n\equiv4\bmod6$，令 $m=n+2\equiv0\bmod6$。
因 $\eta_k^6=1$，第二项 **全局严格等于**
$$
\eta_k\psi_4^{2m+1}=\psi_k^{2m+1}.
\tag{11}
$$
因此 positive 的第 $n+2$ Hermite 槽正是(7)的原
$S/H_3/H_5$，不是只根据 conductor 或同一 Hecke 名称相认。
对 $k=1,n=4$，它是原首6槽；在负二端点它是原零质量槽。

## 4. 负槽的 wild3 函数及完整相位

(10)第一因子在合法 $n$ 的有限单位表为
$$
2:\epsilon_2^{-1},\qquad
3:u,\ \delta\mapsto-i,\qquad
17:u^{48k},
\tag{12}
$$
三个有理 uniformizer 仍为 $-1$。
2处因此用 $v_-$；17处保同一个 $f_k$。
3处不能继续用(7)的球。

现直接在原 Yang lattice model 支付该处。
令 $F=\mathbf Q_3,E=K_3$，
$$
\Psi'(z)=\psi_{F}\!\left(
 \operatorname{Tr}_{E/F}(17\delta z/4)\right),\qquad
L=\delta^{-1}\mathcal O_E
 =\mathbf Z_3+\tfrac{\delta}{3}\mathbf Z_3 .
$$
若 $z=a+b\delta$，则
$\Psi'(z)=\psi_F(-51b/2)$。
原 conductor1 splitting 是平凡的；
(12)与它的比在单位上为 $u^{-2}$。
Yang Proposition1.2 的实际 Hilbert90 式给
$$
\xi_{\rm new}(\omega)=\omega^2,\qquad
\xi_{\rm new}(-1)=1 .
\tag{13}
$$
更具体地，改变 splitting 后两种 $\xi$ 的比是
$(\chi_{\rm new}/\chi_{\rm old})(\delta(g-1))$；因为
$\delta(g-1)/\overline{\delta(g-1)}=g$，这是同一个
Hilbert90 lift，旧新相同的 Hilbert 符号相消。该比在
$\delta$ 上为1、单位上为 $u^{-2}$，所以
$\delta(\omega-1)=3\omega^2$ 直接给(13)。
此角色在 $1+\delta^2\mathcal O_E$ 上平凡。

取 lattice 函数 $f_w$，支撑 $w+L$，
在其中取值 $\Psi'(w\bar z)$。
对 $w=1/3$，原 norm phase 是
$$
\Psi'(-w\bar w\,\omega)
 =\psi_F(17/12)=\omega .
\tag{14}
$$
两个陪集 $w+L,-w+L$ 不交；由 $G/G_1=\{\pm1\}$ 的
完整作用，$f_{1/3}+f_{-1/3}$ 是旧 lattice 表示中
特征 $\xi_{\rm new}^{-1}$ 的非零向量。
这是 Yang lattice Theorem0.1 的具体两个陪集，(14)
同时锁定了哪个三次角色。

原 Schrödinger 变换
$$
\rho(f)(u)=\int_{F/(F\cap L)}
 f(u\delta+y)\Psi'(-\delta uy)\,dy
$$
在 $f_{\pm1/3}$ 上分别给
$\psi_F(\pm17u)\mathbf1_{3^{-1}\mathbf Z_3}(u)$。
故准确新向量为
$$
\boxed{
\phi^-_{k,3}(u)
 =\bigl(\psi_3(17u)+\psi_3(-17u)\bigr)
      \mathbf1_{3^{-1}\mathbf Z_3}(u)
 =3\mathbf1_{\mathbf Z_3}(u)
       -\mathbf1_{3^{-1}\mathbf Z_3}(u).
}
\tag{15}
$$
它的三个陪集值是 $2,-1,-1$，自对偶范数平方为6。
整个负向量是
$$
\phi^-_{k,\rm fin}
 =(f_A+t_-f_B)\otimes\phi^-_{k,3}
   \otimes\sum_a f_k(a)\mathbf1_{a/17+\mathbf Z_{17}}
   \otimes\!\!\bigotimes_{\ell\ne2,3,17}\!\!
                    \mathbf1_{\mathbf Z_\ell}.
\tag{16}
$$
(13)--(15)支付了完整主单位与 uniformizer，不仅是一个
剩余角型。

在原有理支撑 $n/102$ 上，(15)恰给
$$
w_3(n)=
 \begin{cases}2,&3\mid n,\\-1,&3\nmid n.\end{cases}
 =\omega^n+\omega^{-n}.
\tag{17}
$$
若 $F_{\rm old}(Z)$ 专指 **未乘 Gaussian 的 Fourier 和**，
则
$$
F_-(Z)=F_{\rm old}(Z+1/3)+F_{\rm old}(Z-1/3).
\tag{18}
$$
其系数周期是204，原整 theta 格
$\Lambda=\delta^{-1}\mathcal O_K$ 缩为
$\delta\Lambda=\mathcal O_K$，指数3。
所以这是真 degree102 来源；不能仍称 degree34。

## 5. canonical k1 的 old 负向量回到原 S

为把(18)完全代数化，先给其 old Fourier 来源的实际规范。
令 $\Pi_2$ 为原 whole $\mu_6$ 型2投影；在
$\sigma^{34}P(x)$ 上准确保留 $x^{1+3r}$ 项。
原二挠点 $(-1,0)$ 的 canonical Weyl 算子为
$$
\mathsf U_{-1}(\sigma^{34}R)
 =(-\delta)^{-17}(x+1)^{17}\sigma^{34}
       R\!\left(\frac{2-x}{x+1}\right).
\tag{19}
$$
它只作用 dyadic 因子，和完整17处 torus 逐项交换。
对(8)，原 off-diagonal Pauli 系数非零；
全部多项式可以直接展开，得到
$$
\boxed{
D_{\rm old}:=21\delta\,\Pi_2\mathsf U_{-1}S
 =\sigma^{34}x(X+1)(X-8)
      (X^3-30X^2-144X-32).
}
\tag{20}
$$
因此
$$
R_{\rm old}(x)=\sum_{a=1,4,7,10,13,16}r_a x^a,\qquad
(r_a)=(256,1376,1216,58,-37,1),
\quad [z^2]D_{\rm old}=1 .
\tag{21}
$$
这是(16)在移去 wild3 因子后的同一有限线，
其实际相位由(19)及原 $S$ 锁定。

一个不需谱重算的展开证法如下。
将(8)代入(19)，乘 $21\delta$ 后，type2投影可在
$x^3=X$ 下取相关常数项。需要的多项式是
$$
Q_{\rm num}=7(2-x)^6-4(2-x)^3(x+1)^3+16(x+1)^6.
$$
其 $x^0$ 和 $x^2$ 模 $x^3-X$ 系数分别为
$27(X^2-28X+16)$ 与1944。
代入 $(X-2-3x)Q_{\rm num}/27$ 即给(20)。
特别没有通过少数 Taylor 项拟合整来源。

## 6. 两条真实三挠 Weyl 词和完整 degree102 多项式

令 $q=(0,1)\in E_0[3]$；交换 $q,-q$ 不改变下式。
在实周期规范中它可取 $-\Omega_0/3$。
倍点及准周期公式给
$$
\zeta(q)=\eta_1q/\Omega_0,\qquad
c_q=e^{-\zeta(q)q/2}\sigma(q),\qquad
c_q^3=-1/2,\quad c_q=-2^{-1/3}.
\tag{22}
$$
最后实支由 $q<0$ 及原奇 sigma 决定。
例如令
$A_q(w)=e^{-\zeta(q)w}\sigma(w+q)/\sigma(q)$。
三重零及首项给
$A_q(w)^3=-(y(w)+1)\sigma(w)^3$；
在 $w=q$ 再用 $2q=-q-\Omega_0$ 的准周期，直接得到
$c_q^3=-1/2$。
这是原 lift 的值，不另选一个立方根。

对 reduced theta source，(18)必须写成
$$
\mathsf T_{\pm q}^{34}F(z)
 =e^{-34\zeta(\pm q)(z\pm q/2)}F(z\pm q).
\tag{23}
$$
在原无量纲坐标 $Z$ 中，(23)的 multiplier 正是
$e^{-34\sqrt3\pi(\pm2Z/3+1/9)}$。
所以这里保留了 Fourier shift 所需的整个 Gaussian，
没有把(18)错误地施于已经 reduced 的 sigma 来源。

定义
$$
g_\pm(z)=
 \frac{e^{\mp\zeta(q)z}\sigma(z\pm q)}
      {\sigma(z)\sigma(\pm q)} .
$$
三重零与首 $1/z$ 同时给
$$
g_\pm^3=-(y\pm1),\qquad
g_\pm(\delta z)=-\frac{y\mp\delta}{\delta x},
\qquad
\sigma(\delta z)=\delta x\sigma(z)^3 .
\tag{24}
$$
最后两式的立方与极点可直接核定，首
$1/(\delta z)$ 排除了额外三次根。
原三同源及加法公式进一步给
$$
x(\delta z)=-\frac{X+4}{3x^2},\quad
y(\delta z)=\frac{y(X-8)}{\delta^3X},\quad
x(\delta z\pm q)=
 \mp\frac{2\delta x(y\pm\delta)}{(y\mp\delta)^2}.
\tag{25}
$$
因此(20)的两条完整 Weyl 词在 $\delta$ pullback 后为
$$
\boxed{
(\mathsf T_q^{34}+\mathsf T_{-q}^{34})
 D_{\rm old}(\delta z)
 =c_q^{34}\sigma(z)^{102}R_{102}(x,y),
}
\tag{26}
$$
其中左侧表示先对 $D_{\rm old}$ 作(23)，再令变量为
$\delta z$，且
$$
\begin{split}
R_{102}=\sum_{a=1,4,7,10,13,16}r_a x^a
\bigl[&
 (-2\delta)^a(y+\delta)^a(y-\delta)^{34-2a}\\
 &+(2\delta)^a(y-\delta)^a(y+\delta)^{34-2a}
\bigr].
\end{split}
\tag{27}
$$
所有指数非负。两项由 $y\mapsto-y$ 交换，
故(27)是 $x$ 的有理多项式。
在 $y^2=X+1$ 中约化可见
$R_{102}=xP_{16}(X)$，不需要把可重算的17个系数展开存库。

其首项也可完整手算。
$a=1$ 的两项最高奇 $y$ 项相消，下一项是
$-372r_1xy^{32}$；$a=4$ 的最高项为
$288r_4x^4y^{30}$。其余项的极阶至多92。
故
$$
[z^4]\sigma^{102}R_{102}
 =-372\cdot256+288\cdot1376
 =301056=2^{11}\cdot3\cdot7^2 .
\tag{28}
$$
于是准确的原模型规范为
$$
\boxed{
D_-=\frac{\sigma^{102}R_{102}}{301056},\qquad
[z^4]D_-=1,\qquad
(\mathsf T_q^{34}+\mathsf T_{-q}^{34})
 D_{\rm old}(\delta z)=\frac{147}{t}D_-(z).
}
\tag{29}
$$
$D_-$ 的有理式分母只涉及固定的2、3、7；
极处已在(27)中全部消除。
这是真正可供惰性 Newton 使用的固定 degree102 来源，
不是从若干特征样本猜出的 theta。

## 7. 原双核如何读取两个实际槽

使用已经逐坐标支付的 Borade/Chan split seesaw 与
Hermitian 对角化；本次只将固定 splitting 改为
$\chi=\nu_4^2$，使用(9)。
在每个有限处，取 partial Fourier 与该坐标变换的准确逆像，
使两个 rank-one 输入就是(16)和(7)。
这定义了具体 binary Schwartz 函数；所有 finite supports、
原3处 phase、full2 sign 和17处18项都保留。
不从相同 Hecke 标签任取另一条 binary 向量。

无穷处仍用同一个 $a=17/2$、
$G=51\sqrt3$、chirped Gaussian 及
$$
h_\infty=\frac{\sqrt{51\sqrt3}}{204\pi i}.
$$
原正常序的双变量 Hermite 积分于是给第 $n$ 与第 $n+2$
两个槽，$n\equiv4\bmod6$。
positive 的实际函数是(8)。
negative 在原 coherent 变量中必须是
$$
\boxed{
D_-\!\left(\frac{\Omega_0h_\infty T}{\delta}\right),
}
\tag{30}
$$
并保(19)、(22)、(29)全部固定幅度。
(30)的 $\delta^{-n}$ 不能删掉或并入一个随 $n$ 重新选择的
规范。

特别 $k=1,n=4$ 的两个原模型系数分别为
$[z^4]D_-=1$、$[z^6]S=1$。
两个原 finite 向量与 partial Fourier 均非零，
故该实际正权 toric 值非零，可以作为本族的真 anchor。
它是 $(4,6)$ 槽；不是旧 variable-weight 的 $(4,0)$，
更不是从 $S(0)=0$ 构造不存在的真空倒数。
所有整体常数由本节所定义的实际 Fourier 函数和(19)、(29)
固定；后继若改用单位 sigma 来源，须同时运输这些幅度。

## 8. 新旧几何范围

新输入在2处用 $\pi_{4,2}$ 的 full2 sign，17处用(6)的
十八个实际 degree17 同源；旧 full54 的三个二商 wavelet
属于 $\pi_{27,2}$，不能直接移到这里。
新 highest、Artin 字符与(3)相符，包含(2)的 wild3。
本文证明完整 theta source；实际 fulllevel 图的
fp 端点与权族比较须以这一新输入逐项支付。

它的原 $S(0)=0$ 并不是失败的归一化。
$n=4$ 的 $(4,6)$ 非零锚和 $n=-2$ 的零真空处于不同的
无穷权范围，准确表如下：
$$
\begin{array}{c|cc}
 &n=4&n=-2\\ \hline
3+2n\text{（toric/raised权）}&11&-1\\
2n+1\text{（negative Hecke型）}&9&-3\\
2n+5\text{（positive Hecke型）}&13&1\\
\epsilon_\infty(\text{negative})&i&-i\\
W(\text{negative})&+1&-1\\
W(\text{positive})&+1&+1 .
\end{array}
\tag{32}
$$
这里 unitary gamma 的无穷 epsilon 依赖绝对角权。
$n=-2$ 的 negative 因子是 $\lambda_k^{-1}$ 的 unitary
实现，不能把它当成正权 type3 来保留旧无穷 epsilon。

固定族的实际 toric 角色为
$\xi_{k,n}=\eta_k^{-1}\nu_4^{-(3+2n)}$。
$n=4$ 与 $n=-2$ 的比 $\nu_4^{-12}$ 在2、3、17的
全部单位及所定 uniformizer 上为1；这保(2)的全部有限
Hom。好 split 位的 unramified 参数仍随权变化，实际
球函数相同，不声称完整有限 Hecke 角色恒定。
在无穷处，$D_3$ 有 raised $K$-type11，却没有
$K$-type $-1$。所以正权周期可用 split torus，而
负二端点是 AJ 型的非经典配对。
完整 Rankin 符号由 $+1$ 变 $-1$ 恰发生在这一墙上，
不构成(28)的非零正权来源与(3)的矛盾。

## 9. 两个 completion 的精确区别

本节记录后继必须消费的固定规范，不预付新共同因子在
augmentation 的单位性。
写 $d=p+1$，保持原 $E_0$ sigma：
$$
C_+=34c_\sigma,\qquad C_-=102c_\sigma=3C_+,\qquad
c_\sigma=[z^d]\log(\sigma_0/z).
\tag{33}
$$
negative 的(30)使其 natural coherent completion 为
$C_-\delta^{-d}$；positive 是 $C_+$。
由 $\delta^p\equiv-\delta\pmod p$，
$$
q_\delta:=\delta^d/3\in1+p\mathcal O.
\tag{34}
$$
差别是一个真正整 gauge，但不是零；全部权上必须保留
$q_\delta^{-v}$。

定义两个原 Newton 函数
$$
J_-(v)=\sum_{h\ge0}C_-^{-h}
 [z^{dh-2}](D_-e^{-C_-z^d})(v)_h=pvK_-(v),
$$
$$
J_S(v)=\sum_{h\ge0}C_+^{-h}
 [z^{dh}](Se^{-C_+z^d})(v)_h .
\tag{35}
$$
对每个正整数 $r$，准确的 Newton 消去给
$$
J_-(r)=r!C_-^{-r}[z^{dr-2}]D_-,
\qquad
J_S(r)=r!C_+^{-r}[z^{dr}]S.
$$
所以完整两个 coherent 槽严格满足
$$
\boxed{
\delta^{-(dr-2)}[z^{dr-2}]D_-\,[z^{dr}]S
=-3q_\delta^{-r}
 \frac{C_+^{2r}}{(r!)^2}J_-(r)J_S(r).
}
\tag{36}
$$
这里只有 $q_\delta^{-v}$ 可直接延拓。
$C_+^{2r}/(r!)^2$ 仍须在合法正权的实际公共比较中消去，
不能沿整数权自行取负二极限。

原 $J_S(0)=0$，且原 canonical 坏条件是 $J_S'(0)=0$。
在正确公共正权比较并除去一个 $pv$ 后，尚待消费的
完整解析源是
$$
-3q_\delta^{-v}K_-(v)J_S(v).
\tag{37}
$$
其常数为零，$u$-斜率为
$-3(p-1)K_-(0)J_S'(0)$。
但(37)与实际几何族之间的共同因子是否在0非零，
以及 $K_-(0)$ 是否为单位，不能由(28)或一个复正权锚代替。
这些准确范围保留到后继同一参数证明。

## 原始来源与依赖

- R290、R297、R306、R307：原 $S/H_3/H_5$ 的完整
  $2/3/17$ 函数、sigma 模型、canonical 幅度与全权平方。
- R991：三条 cubic twists 的实际同构、完整 character 表、
  全局部 Hom、实际 compact vector；本文的 $\eta_k$ 已改变，
  所以逐项重核后使用该局部证明。
- R798、R855：原 canonical 半周期和全 theta 热规范。
- T. Yang, “Eigenfunctions of the Weil representation of unitary group
  of one variable”, Trans. AMS 350 (1998), Theorem0.1：
  https://people.math.wisc.edu/~tonghaiyang/lattice.pdf 。
- T. Yang, “Nonvanishing of central Hecke L-values and rank of certain
  elliptic curves”, Compositio117 (1999), Proposition1.2、Corollary1.3
  及式(1.6)：https://people.math.wisc.edu/~tonghaiyang/rank.pdf 。
  本文(13)--(15)将具体两个 lattice 陪集与转模全部算出。
- 已发布未平方 theta 来源与完整 geometric cross 笔记中的
  Borade/Chan 坐标、原 Gaussian、Kriz/BDP 局部端点规范。
  本文只支付新有限来源，不把旧 degree34 图或旧端点直接移名。


## 10. 同一十七向量下，原正负来源的绝对 raw 比例

以下只补原来源的绝对归一；不从端点根号或常项零推出新中央零。固定
$E_0:y^2=x^3+1$、$x=\wp(z)$、$y=\wp'(z)/2$、$X=x^3$、
$\delta=i\sqrt3$，及 R735/R806 的真实正实周期 $\Omega _0$。
全程使用 R290 的同一个十七向量
$f_{17}=9\sqrt{17}\Pi_{12}e_0$。原正来源为
$$
S(z)=\frac17\sigma(z)^{34}x^2(X+1)(X-8)(7X^2-4X+16),
\qquad [z^6]S=1.
$$
以实际 Fourier 系数定义
$$
S_{\rm raw}(Z)=s_S S(\Omega _0Z),\qquad
S_{\rm raw}(Z)=e^{aZ^2}\sum_{n\in\mathbf Z}
 v_+(n)f_{17}(3n)q^{n^2}e^{2\pi inZ},
\quad a=34\sqrt3\pi .
$$
这里 $v_\pm=(1,t_\pm,-1,t_\pm)$，
$t_\pm=(1\pm\sqrt3)/\sqrt2$，$q$ 为 R290(32) 的同一参数。
令 $F_{\rm old,raw}$ 只把 $v_+$ 换成 $v_-$，其余有限向量和
Gaussian 均不变。

### A. 二挠 Weyl 相位与 type2 来源

取 $T=\Omega _0/2$，对应 $(-1,0)$。令
$c_T=e^{-\zeta(T)T/2}\sigma(T)>0$。
原规范的二次 theta 平移满足
$$
\mathcal T_T^{\,2}\sigma^2
=c_T^2\sigma^2(x+1).
$$
这里左上的 $2$ 表示线丛次数；连续施加两个该算子为恒等。
由 $x(P+T)+1=3/(x+1)$ 得 $3c_T^4=1$，所以
$c_T^2=1/\sqrt3$。因而原代数 Pauli lift
$$
U_{-1}(\sigma^{34}Q)=
(-\delta)^{-17}\sigma^{34}(x+1)^{17}
 Q\!\left(\frac{2-x}{x+1}\right)
$$
与实际 Weyl 平移满足精确相位
$$
U_{-1}=i\,\mathcal T_T^{\,34}.
$$
此处 $U_{-1}^2=-1$，而实际 $\mathcal T_T^{\,34}$ 的平方为 $1$；
两者不能在不留 $i$ 的情况下混用。

把 $\mathcal T_T^{\,34}$ 作用于上面的完整 Gaussian Fourier 源，
Gaussian 与 Weyl 指数准确抵消，剩下 $(-1)^n$。
在 $(f_A,f_B)$ 两列上它是 $\operatorname{diag}(1,-1)$。直接解两列得到
$$
\operatorname{diag}(1,-1)v_+
=-\frac1{\sqrt3}v_+
 +\left(1+\frac1{\sqrt3}\right)v_-.
$$
十七向量保持不变，第二项正是所需的完整 type2 投影。
采用已付的整六列
$$
D_{\rm old}=21\delta\,\Pi_2U_{-1}S
=\sigma^{34}x(X+1)(X-8)(X^3-30X^2-144X-32)
$$
（$\sigma^{34}x(1,X,\ldots,X^5)$ 坐标为
$(256,1376,1216,58,-37,1)$，首 $z^2$ 系数为 $1$），遂得
$$
F_{\rm old,raw}(Z)=s_{\rm old}D_{\rm old}(\Omega _0Z),
\qquad
\boxed{s_{\rm old}=-\frac{s_S}{21(1+\sqrt3)}}.
$$
这是同一个十七向量的 raw 比例，不是只由两来源的 Hecke 标签推定。

### B. 三挠 lift 的实际常数和 degree102 首项

令 $S_3=(0,1)=-\Omega _0/3$，
$c_3=e^{-\zeta(S_3)S_3/2}\sigma(S_3)$。
由 $x(S_3)=0$ 的 zeta duplication 及 $2S_3=-S_3-\Omega _0$，
$3\zeta(S_3)=-\eta_{\Omega _0}$。
再对
$$
A_+(z)=e^{-\zeta(S_3)z}
       \frac{\sigma(z+S_3)}{\sigma(S_3)},\qquad
A_+(z)^3=-\sigma(z)^3(y+1)
$$
在 $z=S_3$ 取值，并使用原 sigma 准周期式，得到
$c_3^3=-1/2$。实嵌入下 $\sigma(S_3)<0$，故
$c_3=-2^{-1/3}$，没有任意立方根相位。

令 $A_-$ 为负支的相同规范。原 division 恒等式给
$$
A_\pm(\delta z)=-\sigma(z)^3(y\mp\delta).
$$
对任一
$D=\sigma^{34}x(p_0+p_1X+\cdots)$，两支完整 Weyl 和的首四阶为
$$
[z^4]\left\{
(\mathcal T_{S_3}^{\,34}D)(\delta z)
+(\mathcal T_{-S_3}^{\,34}D)(\delta z)\right\}
=12c_3^{34}(24p_1-31p_0).
$$
确切地，
$x(\delta z\pm S_3)=\pm2\delta z+18z^4+O(z^7)$，
$A_\pm(\delta z)^{34}=1\pm34\delta z^3+O(z^6)$；
两支三次以下奇项相消，四阶即上式。
代入 $p_0=256,p_1=1376$ 得
$$
[z^4]\mathcal D_{\rm sum}
=301056c_3^{34}=\frac{147}{2^{1/3}},
\qquad
\mathcal D_{\rm sum}(z)=
\sum_\pm(\mathcal T_{\pm S_3}^{\,34}D_{\rm old})(\delta z).
$$
以此真实非零数归一 $D_-$，使 $[z^4]D_-=1$。

新三处函数
$3\mathbf1_{\mathbf Z_3}-\mathbf1_{\frac13\mathbf Z_3}$
在实际 $n/102$ 格上的乘子为 $2$（$3\mid n$）和 $-1$（其余）。
所以其 raw 源准确为
$$
F_{\rm new,raw}(Z)
=\sum_{\epsilon=\pm1}
 e^{-a(2\epsilon Z/3+1/9)}
 F_{\rm old,raw}(Z+\epsilon/3).
$$
必须保这两个 Gaussian 指数，不能写成没有指数的字面平移。
因此
$$
F_{\rm new,raw}(Z)
=s_{\rm new}D_-(\Omega _0Z/\delta),
\qquad
\boxed{s_{\rm new}
=-\frac{7s_S}{2^{1/3}(1+\sqrt3)}}.
$$
$1/\delta$ 是原 coherent 变量的实际缩放；其 $n$ 阶费用
$\delta^{-n}$ 在全权公式中另行保留。

### C. 完整 Yang 范数中的对应比例

沿 R290(25)–(38) 的自对偶测度，若 $n_{17}=\|f_{17}\|^2$，
原正向量与新负向量的有限范数分别是
$$
3(3+\sqrt3)n_{17},\qquad
6(3-\sqrt3)n_{17}.
$$
两者的 Hermitian 参数 $\alpha=17$、无穷 Hermite 规范和好处球相同。
Yang 的 $S_1$ 仍是非分歧而角色分歧的 $\{2,17\}$；
三处为 $K/\mathbf Q$ 的分歧处，不能因为新三处向量改变而加进 $S_1$。
故 $c(0)=17/27$ 和体积比 $6$ 保持原值。
把范数归一还原到 raw theta，得
$$
\frac{C_{\rm new}}{C_S}=\frac{2+\sqrt3}{2},\qquad
\boxed{\frac{C_{\rm new}s_{\rm new}^{\,2}}{C_Ss_S^{\,2}}
=\frac{49}{4\,2^{2/3}}}.
$$
此式比较相同的原 Hermite 变量；上一节的 $\delta^{-n}$ 不包含在这个
常数里。若某处改用 $\Pi_{12}e_0$，而另一处仍用
$9\sqrt{17}\Pi_{12}e_0$，raw 比例须相应乘除 $9\sqrt{17}$；
平方范数恰有其平方费用，故 $Cs^2$ 比例不变。
这给正负全源的可检验绝对常数，并未把正权平方公式外推为
$n=-2$ 端点的非零真空。


## 11. 两条真实秩零参考的完整负源与绝对幅度

本附节使用 R307(3) 的原 $H_{3,1},H_{5,1}$，各自质量为 $1$。
其原 Fourier 向量分别保持 R306 的十七角色 $j=0,6$，二处仍为
$v_+$，三处为原 $\mathbf1_{\frac13\mathbf Z_3}$。
不把它们当作目标角色的幂，也不改各自的原 period。

设 $X=x^3$，$H_{k,1}=\sigma^{34}Q_k(x)$，其中
$$
\begin{aligned}
Q_3={}&x^{17}-208x^{14}+400x^{11}
       +8128x^8+12032x^5-2048x^2,\\
Q_5={}&x^{17}+272x^{14}-272x^{11}
       -14912x^8-6784x^5+1024x^2 .
\end{aligned}
$$
沿前附节的绝对 Pauli lift 定义
$$
E_k=\Pi_2U_{-1}H_{k,1},\qquad
M_k(x)=(1+x)^{17}Q_k\!\left(\frac{2-x}{1+x}\right).
$$
因为 $(-\delta)^{-17}=\delta/19683$，
$E_k$ 正是 $\delta\sigma^{34}/19683$ 乘 $M_k$ 中指数
$1,4,7,10,13,16$ 的六项。此定义保完整六列，后面仅提取所需的三个
确切系数。

对原单项式 $x^r$，$r=2,5,8,11,14,17$，相应的三个提取行如下：
$$
\begin{array}{c|rrrrrr}
r&2&5&8&11&14&17\\ \hline
[x](2-x)^r(1+x)^{17-r}
 &56&304&1280&1024&-65536&-1114112\\
[x^4](2-x)^r(1+x)^{17-r}
 &3745&3050&-4256&16640&-207872&19496960\\
[x^{16}](2-x)^r(1+x)^{17-r}
 &11&-2&-7&16&-25&34
\end{array}
$$
这是完整二项式乘积的提取，不是由低阶数值拟合。第一行一般为
$2^{r-1}(34-3r)$，第三行为 $(-1)^r(17-3r)$；第二行直接是
$$
\sum_{j=0}^4(-1)^j2^{r-j}
 \binom rj\binom{17-r}{4-j}.
$$
把上面两个原列相乘，得到
$$
\begin{array}{c|rrr}
k&[x]M_k &[x^4]M_k &[x^{16}]M_k\\ \hline
3&4096\cdot6561&9728\cdot6561&-14\cdot6561\\
5&-6144\cdot6561&768\cdot6561&18\cdot6561
\end{array}
$$
从 $\sigma^{34}x^{16}=z^2+\cdots$，原首项准确为
$$
\boxed{a_3=[z^2]E_3=-14\delta/3,\qquad
       a_5=[z^2]E_5=6\delta.}
$$
因此可定义实际首二阶规范 $D_{{\rm old},k}=E_k/a_k$。
写
$D_{{\rm old},k}=\sigma^{34}x(p_{k,0}+p_{k,1}X+\cdots+X^5)$，
两条所需低坐标为
$$
\boxed{
(p_{3,0},p_{3,1})=(-2048/7,-4864/7),\qquad
(p_{5,0},p_{5,1})=(-1024/3,128/3).
}
$$
这同时固定了整个来源：省略的四项仍由同一个完整 $M_k$ 提取，
不是额外可选择的自由系数。

令 $S_3=(0,1)$，并保前附节的实际
$c_3=e^{-\zeta(S_3)S_3/2}\sigma(S_3)=-2^{-1/3}$。定义全两支和
$$
\mathcal D_k(z)=
\sum_{\epsilon=\pm1}
(\mathcal T_{\epsilon S_3}^{\,34}D_{{\rm old},k})(\delta z).
$$
由已逐支证明的首项公式
$$
[z^4]\mathcal D_k
=12c_3^{34}(24p_{k,1}-31p_{k,0})
$$
得
$$
\boxed{\ell_3=-\frac{312}{7\,2^{1/3}},\qquad
       \ell_5=\frac{68}{2^{1/3}}.}
$$
两者确非零，故 $D_{{\rm new},k}=\mathcal D_k/\ell_k$
均是原 degree102 来源，且 $[z^4]D_{{\rm new},k}=1$。
这没有作任何随 $p$ 变化的单位推断。

最后，设各自实际正 Fourier 源为
$F_{k,+,{\rm raw}}(Z)=s_kH_{k,1}(\Omega _0Z)$。
逐个保持相同的原十七向量；前附节已经证明的
$U_{-1}=i\mathcal T_{\Omega _0/2}^{34}$ 与二处完整投影给
$$
\frac{s_{{\rm old},3}}{s_3}=-\frac{14}{1+\sqrt3},
\qquad
\frac{s_{{\rm old},5}}{s_5}=\frac{18}{1+\sqrt3}.
$$
三处准确改成 $3\mathbf1_{\mathbf Z_3}
-\mathbf1_{\frac13\mathbf Z_3}$ 后，Gaussian 两平移保持原式。
因此
$$
F_{k,{\rm new,raw}}(Z)
=s_{k,{\rm new}}D_{{\rm new},k}(\Omega _0Z/\delta),
$$
$$
\boxed{
\frac{s_{3,{\rm new}}}{s_3}
=\frac{624}{2^{1/3}(1+\sqrt3)},\qquad
\frac{s_{5,{\rm new}}}{s_5}
=\frac{1224}{2^{1/3}(1+\sqrt3)}.
}
$$
连同目标 $k=1$，三个分子统一为
$r_1=-7,r_3=624,r_5=1224$。
各自十七范数在同一行的正负比较中抵消，故同原 Hermite 变量下
$$
\boxed{
\frac{C_{k,{\rm new}}s_{k,{\rm new}}^2}{C_{k,+}s_k^2}
=\frac{r_k^2}{4\,2^{2/3}}.
}
$$
仍须独立保 $\delta^{-n}$ coherent 变量尺度。
若使用 $E_{17^k}$ 自身的原微分，则沿 R307(4)、(17) 同时搬运
$\Omega_{17^k}$ 与原坐标，不能只改多项式系数。
$s_k$ 的绝对符号保持其原 Fourier 定义；这里给的是相对于该实际
正来源的确切有符号幅度，不通过任选平方根重新定标。


三条归一负源均在同一个 $b=1$、degree102 theta 线丛中，
使用同一个实际物理变量 $z$，所以负二 completion 都是
$C_{102}=102c_\sigma$。在原 Hermite 变量上，
$z=\Omega_0h_\infty T/\delta$ 也逐条相同；与正34框的
Gaussian 比准确为 $3/\delta^{p+1}=q_\delta^{-1}$。
这只统一线丛、连接和尺度；各条完整有限 Hecke 角色仍按
$k=1,3,5$ 保留，不能把它们改作一个特征源。
