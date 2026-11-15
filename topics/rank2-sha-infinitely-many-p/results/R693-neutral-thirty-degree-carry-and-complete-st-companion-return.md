# R693 — 中性三十次权、完整半周期关系与同一伴随门的双 S/T 返回

日期：2026-11-15。**状态：已证明。**

本文构造一个新的原六支测试 $q_N^{\natural}$。它保原完整 $\pi_4$
返回，使两份冻结 S34 来源分别为 $c_0S$、零，原 cd 端点为 S，
而该端点的**未缩放原 W 来源**恰为 $6\delta T$；同一实际二阶系数
仍准确规范为一。$c_0$ 是保全部 $\lambda,\kappa,u$ 的整单位。

关键是一个完整来源级半周期关系。它支付第三十一行，
所以所需实际逆是显示的三十阶子式；本文没有把辅助模 1009 的
一个左核直接提升为特征零关系。新增原权最高三十次，全部 C 高矩、
两个 C 核分支、不同冻结系数及原 T 补域均保留。

## 1. 原来源、参数和固定中性列

沿 R594、R664、R665、R679、R686、R690 的原固定 ray 与坏集，保
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad \Omega\in\mathcal O^\times,
\quad N\in4\mathbf Z_{>0},\quad u=\kappa^N.
\tag{1}
$$
所有普通地点仍取原 $(\pi_0)$。本文只再删显示的固定分母坏集和
第6节的固定 CM 多项式稀疏坏集，不重定义任何已付射线模数。

用 $\mu_0$ 记带原 $-1/84$ 常数的六 sigma 来源，必要时先作
R590 的完整六支 C 平均；两种表示给这里同一全部观察。
$$
\mu_0=\nu_4\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),\qquad
Q=c+2d,\quad L=2c-d,
$$
$$
Y_0=A+Q,\qquad Y_1=A+L,\qquad
W=A+3\delta c+4d,\qquad \epsilon_i=(-1)^i.
\tag{2}
$$
原归一是
$$
(Y_0)_*\mu_0=\nu_S,\qquad W_*\mu_0=6\delta\nu_T.
\tag{3}
$$
第二支仍由实际整数旋转 $\mathsf J(c,d)=(d,-c)$ 转置，
$\,\mathsf J_*\mu_0=-\mu_0$；其权、G 观察及所有门同时运输。

原输出与权变量为
$$
\pi_4=(Y,W,W',G),\qquad D=F-C,\quad E=F+13C,\quad
G=13H_1+(3-2\omega)F.
\tag{4}
$$
R594 的实际九乘二十矩阵、整右逆和核投影写作
$$
A_p,\qquad
R_p=\mathsf B(\tau)\bigl(A_p\mathsf B(\tau)\bigr)^{-1},\qquad
\Pi_p=I-R_pA_p,\qquad\tau=(1+\lambda)^{-1}.
\tag{5}
$$
这里保 $\mathsf B(\tau)=(\mathsf B_0+\tau\mathsf B_1)/(\tau-1)$
及原实际 E 次数逆 $(1+\lambda\kappa^r)^{-1}$，不先改成其余式。

在 R594 二十列的原顺序取
$$
\mathcal I=(0,1,2,3,4,13,15,16,17,18,19).
$$
令 $\delta q_{j,N}$ 是 $\Pi_pe_{\mathcal I_j}$ 对应的完整六支
carry 差测试。由 R679 的真实正交性和投影公式，对全部 $h\ge0$，
$$
h_{h,j,N}=\frac{G^{6h}}{b^h\Omega^{6h}}\delta q_{j,N},
\qquad
(\pi_4)_*(h_{h,j,N}\mu_0)=0.
\tag{6}
$$
这保任意完整 $\pi_4$ 测试。G 是实际 $\pi_4$ 输出，且在原 D
返回和 E 单位逆下不动；(6) 不是形式变量的乘法假设。

本文仅用以下 **29 条固定原列**：
$$
\begin{array}{c|l}
h&j\\ \hline
0&0,1,\ldots,10\\
1&0,1,\ldots,10\\
2&0,3,4\\
3&3,4\\
4&3,4
\end{array}
\tag{7}
$$
按 $11h+j$ 展平，其索引为
$$
\boxed{0,1,\ldots,22,\ 25,26,\ 36,37,\ 47,48.}
\tag{8}
$$
虽然公开脚本还计算了 B 方向，(7)–(8) 不使用任何 B 列，
也不使用 $G^{30}$ 块。最高权次数是 $6+24=30$。

## 2. 全参数来源算子和实际二阶行

原 R594 测试记为 $q_N$。新测试将定义为
$$
q_N^\natural=q_N+\sum_{\ell\in\mathcal J}a_\ell h_{\ell,N},
\tag{9}
$$
其中 $\mathcal J$ 是 (8)，系数由第5节实际逆确定。
其生成权准确写为
$$
\mathcal P=\sum_{h=0}^{4}
 \frac{\widehat P_{6+6h}(D,E,G)}{b^{h+1}\Omega^{6+6h}}.
\tag{10}
$$
每块齐次次数为下标，并保原六支平均、C 单位门、D 深门及
$D/\kappa^N$ 的实际参数。由于 (7) 的列只乘 G，
原 E 次数逆及全部 C 分支仍按 R594 的完整规则作用。

为完整定义两冻结来源，置
$$
\mathcal E=5A-29(Q+L),\quad
e_0=-\frac{170+117\omega}{9135},\quad
e_1=-\frac{170+291\omega}{9135},
$$
$$
h_0=-5-9\omega,\quad h_1=-5-3\omega,\quad g=3-2\omega,
$$
$$
\begin{aligned}
H_0(t)&=D_*+e_0\mathcal E+\frac{h_0t}{315}(5A+39c-92d),\\
H_1(t)&=D_*+e_1\mathcal E+\frac{h_1t}{315}(5A-24c+97d),\\
K_i(t)&=H_i(t)-\frac{406}{143}D_*.
\end{aligned}
\tag{11}
$$
仍令
$$
E_\perp=14C^\perp,\qquad
G_{00}=G_\perp-\frac{-789+526\omega}{1596}E_\perp,\qquad
\eta=\pm1.
$$
全部实际参数下，归一来源算子为
$$
\begin{aligned}
\mathscr S_i(\mathcal P;t)(z)=\epsilon_i\int e^{Y_i z/\Omega}
\bigl\{&
\mathcal P(H_i(t),E_\perp+uK_i(t),G_\perp+guK_i(t))\\
&-\eta\lambda\mathcal P(H_i(t),\kappa E_\perp+uK_i(t),
G_{00}+\kappa(G_\perp-G_{00})+guK_i(t))
\bigr\}\,d\mu_0 .
\end{aligned}
\tag{12}
$$
第二项是整个 $C^\perp$ 深补项。定义
$$
\mathscr U_i=\mathscr S_i(\mathcal P;0),\qquad
\mathscr B=\mathscr S_0(\mathcal P;1).
\tag{13}
$$
完整旋转仍给 $\mathscr S_1(\mathcal P;1)=\mathscr B$。
它们属于同一标准 even34 零角型空间；伴随微分次数提高到三十
不改变 R669/R679 已付的正交 Gaussian 和半特征。

在端点 $t=1$，写
$$
E_{YW}=(5+6\omega)A-29c-(58+87\omega)d,\quad
H=D_*-\frac{E_{YW}}{29},\quad K=H-\frac{406}{143}D_*.
$$
同一个权在原未缩放 W 下的整个来源为
$$
\begin{aligned}
\mathscr W(\mathcal P)(z)=\int e^{Wz/\Omega}\bigl\{&
\mathcal P(H,E_\perp+uK,G_\perp+guK)\\
&-\eta\lambda\mathcal P(H,\kappa E_\perp+uK,
G_{00}+\kappa(G_\perp-G_{00})+guK)
\bigr\}\,d\mu_0 .
\end{aligned}
\tag{14}
$$
R686/R690 证明 (14) 全部微分方向与 Y、W 同时正交。
故 $\mathscr W\in\mathcal S_{72}^{(0)}$，不是缩 Z 的另一个观察。

最后保 R665 的同一四 sigma 门
$$
\mathcal G_*=\{C\ {\rm unit},D_*\in p^N\},\quad
E_*=D_*+14C,\quad G_*=13H_1+g(D_*+C),\quad\ell_0=-3\omega/5.
$$
定义
$$
J_a(\mathcal P)=\ell_0^a[z^a]\int_{\mathcal G_*}
 \mathcal P(D_*/u+z/u,E_*+z,G_*+gz)\,d\nu_4 ,
$$
$$
\boxed{\mathfrak j_2(\mathcal P)
=\frac{2b\Omega^2}{\ell_0^2}\lambda^{-N}u^2J_2(\mathcal P).}
\tag{15}
$$
(15) 由实际 $D_*,C^\perp$ 全核计算，保所有高矩；
三十次项要使用真正二十八次矩，不能沿用六次权的四次简化。

## 3. 完整半周期引理：准周期代表和绝对号

本节对任意 (14) 的实际多项式权成立，不依赖其适配系数。

**引理。** 设同一完整共同隐藏权的 Y、W 来源写为
$$
B_Y=\sum_{j=0}^{5}b^{j-1}s_j\,\sigma_b^{34}x_b^{17-3j},
\qquad
B_W=\sum_{j=0}^{12}b^{j-1}w_j\,\sigma_b^{72}x_b^{36-3j}.
$$
则
$$
\boxed{
\ell_{72}(B_W)=3^9\delta\,\ell_{34}(B_Y),\qquad
\ell_{34}(B_Y)=\sum_{j=0}^{5}(-1)^js_j,\quad
\ell_{72}(B_W)=\sum_{j=0}^{12}(-1)^jw_j .
}
\tag{16}
$$

**证明。** 先在 $b=-1$ 的复规范上定绝对号。
取正实 primitive 周期 $\Omega_0$，另一周期为 $\omega\Omega_0$，
$\omega=e^{2\pi i/3}$，$t_0=\Omega_0/2$。
写 $\eta_1$ 为全周期 $\Omega_0$ 的 zeta 准周期。
CM 和原 Legendre 约定给
$$
\eta_{\omega\Omega_0}=\omega^2\eta_1,\qquad
(\omega-\omega^2)\eta_1\Omega_0
=\delta\eta_1\Omega_0=2\pi i.
\tag{17}
$$
对完整共同隐藏参数，令它在原 c、d 两 sigma 上的加量为
$h_c,h_d$。因为 Y/W 的前四输入完全相同，且
$$
W-Y=2((1+3\omega)c+d),
$$
两个观察的同时 Hermitian 正交性，取差后严格给出
$$
\boxed{h_d=(2+3\omega)h_c.}
\tag{18}
$$
这是整个隐藏参数恒等式，不是其质量或有限 Taylor 截断。

在 $z=t_0$，c 参数从 $t_0+h_c$ 到 $3\delta t_0+h_c$，
准确相差 $(1+3\omega)\Omega_0$；d 参数从
$2t_0+h_d$ 到 $4t_0+h_d$，相差 $\Omega_0$。
原 odd sigma 特征
$$
\chi(m\Omega_0+n\omega\Omega_0)=(-1)^{m+n+mn}
$$
在这两个代表上均为 $-1$，乘积为 $+1$。用完整准周期式
$$
\sigma(z+\Lambda)=\chi(\Lambda)
 e^{\eta_\Lambda(z+\Lambda/2)}\sigma(z),
$$
两个 sigma 的原函数比准确为
$$
\exp\!\left[
 \frac{8-3\omega}{2}\eta_1\Omega_0
 +\eta_1\bigl((-2-3\omega)h_c+h_d\bigr)\right].
\tag{19}
$$
原第一四个 sigma、$-1/84$ 归一常数及全部 C 平均系数在两侧相同。
(18) 消去 (19) 的**整个**隐藏参数项。

标准 degree M 的 canonical 半周期值取
$$
(\mathsf T_{t_0}^{(M)}B)(0)
=e^{-M\eta_1\Omega_0/8}B(t_0).
$$
因此 72 与 34 的 prefactor 比为
$e^{-19\eta_1\Omega_0/4}$，与 (19) 相乘得
$$
\boxed{
(\mathsf T_{t_0}^{(72)}B_W)(0)
=e^{-3\delta\eta_1\Omega_0/4}
(\mathsf T_{t_0}^{(34)}B_Y)(0)
=i\,(\mathsf T_{t_0}^{(34)}B_Y)(0).
}
\tag{20}
$$
这里 $e^{-3\pi i/2}=+i$，并未任意选择一个平方根。

令 $h=x_b(t_0)$、$c_t=e^{-\eta_1\Omega_0/8}\sigma_b(t_0)$。
原 canonical 二挠公式是
$$
h^3=-b,\qquad c_t^4=(3h^2)^{-1}.
\tag{21}
$$
在 $b=-1$ 的所选正实半周期，$h=1$、$c_t>0$，所以
$c_t^2h=1/\sqrt3$。用真实复 CM homothety 回到原 $b=17$，
$c_t\mapsto a^{-1}c_t,\ h\mapsto a^2h$；
故 $c_t^2h$ 保持。原半周期代表和全部常数同时运输。

逐个基元代 (21)，准确得到
$$
(\mathsf T_t^{(34)}B_Y)(0)
=\frac{c_t^2h}{3^8b}\sum_{j=0}^{5}(-1)^js_j,\qquad
(\mathsf T_t^{(72)}B_W)(0)
=\frac1{3^{18}b}\sum_{j=0}^{12}(-1)^jw_j.
\tag{22}
$$
将 (22) 代 (20)，因 $i3^{10}/\sqrt3=3^9\delta$，即得 (16)。

最后，(18) 对 (14) 的完整主项及整个 C 深补项逐项成立：
$H,E_\perp,G_\perp,G_{00},K$ 都与 Y/W 正交，
任意 $\kappa,u$ 线性组合仍如此。
所以可以对 (20) 取任意所需伴随导数，再作完整 C 平均/单位减深。
(16) 是特征零、完整参数下的来源等式。证毕。

原 S 和 $6\delta T$ 在这个半周期均为零：
原六 sigma 的末因子分别为 $\sigma(2z)$、$\sigma(4z)$。
等价地，其原椭圆多项式有 $X+b$ 因子。因此
$$
\ell_{34}(S)=0,\qquad \ell_{72}(6\delta T)=0.
\tag{23}
$$

## 4. 有限空间和全部高矩

标准零角型基为
$$
\Xi_j=\sigma^{34}x^{17-3j}\quad(0\le j\le5),\qquad
\Psi_j=\sigma^{72}x^{36-3j}\quad(0\le j\le12).
\tag{24}
$$
它们的首阶分别为 $6j$，首系数一。
六个 S jet 和十三个 W jet 对整条来源的恢复因此是单位下三角。
我们已先支付完整线丛、角型和半特征，才使用这些有限 jet。

由于最高伴随次数三十，所需原总矩至多 $72+30=102$。
删除固定素数 $p\le103$ 及所列有限几何分母后，所需阶乘均单位。
实际 $b,\Omega$ 的归一沿 R679：
次数 $6d$ 的权除 $b^d\Omega^{6d}$，
第 $z^{6j}$ 系数乘 $b^{1-j}$。所有行在原 $b=17$ 上完整恢复。

原 C 因子是
$$
B_C(s)=-y(s/\delta)\sigma(s/\delta)^3.
\tag{25}
$$
公开算法保 (25) 的 $s^0,s^6,\ldots,s^{30}$ 全部系数。
其余五输入仍为
$$
\frac{f_1(Z_f)\Sigma(Q_f)-f_3(Z_f)\Theta(Q_f)}{42}
 \sigma(r)\sigma(c)\sigma(d),
$$
$$
f_1=-xy\sigma^6,\quad f_3=-y\sigma^6,\quad
\Sigma=\sigma^2,\quad\Theta=x\sigma^2.
\tag{26}
$$
通过原 $x''=6x^2,\ \zeta'=-x,\ \sigma'=\zeta\sigma$ 的准确递推，
(25)–(26) 生成全部有限矩，不读可重算 JSON 作为输入。

对每个纯 G 块，只有在主项和 C 零分支**分别完整代入**
$G_{00}=G_\perp-rE_\perp$ 之后，才利用原 D/E 总次数至多六来裁剪。
不在代入前丢掉会由 G 重新进入的 E 幂。
这正是公开脚本的两个独立生成分支。

## 5. 一个显示的实际三十阶系统

令 $\mathbf s$ 为原 S 的六个归一 jet，令
$\mathbf t_{\le66}$ 为 $6\delta T$ 的 $z^6,z^{12},\ldots,z^{66}$
十一个归一 jet。对每个实际权 P 定义三十行
$$
\mathscr R(P)=
\bigl(\operatorname{jet}_6\mathscr U_0(P),\
      \operatorname{jet}_6\mathscr U_1(P),\
      \operatorname{jet}_6\mathscr B(P),\
      \operatorname{jet}_{6,\ldots,66}\mathscr W(P),\
      \mathfrak j_2(P)\bigr)^{\mathsf t}.
\tag{27}
$$
前29列是 (7) 的实际 $\mathscr R(h_{\ell,N})$；
最后一列是 $(-\mathbf s,0,0,0,0)^{\mathsf t}$。
这个三十乘三十矩阵记为 $\mathbb M^\natural(\lambda,\kappa,u,\eta)$。

原旧权 $q_N$ 的同一完整向量为 $v_{\rm old}$。
准确地定义
$$
\boxed{
\begin{pmatrix}(a_\ell)_{\ell\in\mathcal J}\\ c_0\end{pmatrix}
=(\mathbb M^\natural)^{-1}
\left[
 (0,0,\mathbf s,\mathbf t_{\le66},1)^{\mathsf t}
 -v_{\rm old}\right].
}
\tag{28}
$$
它指定的整个来源条件是
$$
\mathscr U_0=c_0S,\quad \mathscr U_1=0,\quad \mathscr B=S,
\quad [z^{6j}]\mathscr W=[z^{6j}](6\delta T)\ (1\le j\le11),
\quad\mathfrak j_2=1.
\tag{29}
$$
第一冻结行的系数不是预设一；第二冻结来源准确为零。
$c_0$ 只是 (28) 的归一未知数，不是新增的一条测试。

因为 $\mathscr B$ 与 $\mathscr W$ 是同一个权的两个推前，
它们总质量相同；$\mathscr B=S$ 给 $\mathscr W(0)=0$。
于是 (24)、(29) 迫
$$
\mathscr W-6\delta T=a\,\sigma^{72}.
$$
将 (16)、(23) 用于该同一实际权，有
$\ell_{72}(\mathscr W)=3^9\delta\ell_{34}(S)=0$。
又 $\ell_{72}(\sigma^{72})=1$，故 $a=0$。因此
$$
\boxed{
\mathscr U_0(q_N^\natural)=c_0S,\quad
\mathscr U_1(q_N^\natural)=0,\quad
\mathscr B(q_N^\natural)=S,\quad
\mathscr W(q_N^\natural)=6\delta T,\quad
\mathfrak j_2(q_N^\natural)=1.
}
\tag{30}
$$
这一步确切支付了未放进 (27) 的 W 第72阶行。

## 6. 实际参数曲线上的整逆、分母和深度成本

(12)、(14)、(15)、(27) 定义固定
$\mathbf Q(\omega)(\lambda,\kappa,u)$ 有理式矩阵；
原 $b,\Omega$ 行列缩放均为已显示单位。
其全部分母来自：固定几何/阶乘分母、R594 的 $D_{594}$、
$\tau-1$、原有限组 $1+\lambda\kappa^r$、
$\det(A_p\mathsf B(\tau))$，以及 (28) 的新子式。
实际 $A_p\mathsf B(\tau)\equiv I$，原射线给 $1+\lambda$、
$\tau-1$ 单位。这里没有负 u 次数藏进新矩阵。

公开计算使用辅助剩余域
$$
\mathbf F_{1009},\quad\omega=374,\quad
\tau=2,\quad\lambda=-1/2,\quad\kappa=u=0,\quad b=\Omega=1.
\tag{31}
$$
按 (27)–(28) 的固定行列顺序，准确输出
$$
\boxed{
\det\overline{\mathbb M}^{\natural}_{+}=151,\qquad
\det\overline{\mathbb M}^{\natural}_{-}=967,\qquad
\overline c_0=381\quad(\eta=\pm1).
}
\tag{32}
$$
公开脚本原31行中的所选行是 $0,\ldots,28,30$；
所选测试列是 (8)，另加其第66列即第一 S 归一列。
第67列、所有 B 列的系数取零。
整条31行的辅助身份也逐项验证，但特征零缺行是由第3节证明，
不是由这个验证代替。

明确说明怎样回到实际 $\kappa=p\lambda^2,\ u=\kappa^N$。
分别对 $\eta=\pm1$ 清完上述固定分母，
令 $d_\eta(L,K,U)$ 为子式的固定多项式分子，
$n_\eta(L,K,U)$ 为 Cramer 定义的 $c_0$ 分子。
(32) 证明
$$
d_\eta(L,0,0)\ne0,\qquad n_\eta(L,0,0)\ne0
\quad\text{在 }\mathbf Q(\omega)[L]\text{ 中}.
\tag{33}
$$
相应分母在 (31) 定义，所以其边界多项式也不恒零。
取足够大的固定幂清掉 $L=-1/T$ 的负次数，
对全部固定非零多项式应用
[固定 CM 单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)。

由此在原固定 ray 的相对密度一子族上，所有这些实际分子、分母
同时为单位。删除的新增坏素数在 $p\le X$ 中为
$O(\sqrt X\log X)$，外加固定有限分母集；原 Chebotarev 正密度
因而仍给无穷多个 p。该引理保固定系数域共轭范数及固定整数根分支。

对其中每个 p，因 $\kappa\in p\mathcal O$ 且
$u=\kappa^N\in p\mathcal O$，统一有
$$
d_\eta(\lambda,\kappa,\kappa^N)
 \equiv d_\eta(\lambda,0,0)\pmod p,
$$
相应分子/分母同理。故
$$
\boxed{
\mathbb M^\natural_{N,p}\in\mathrm{GL}_{30}(\mathcal O),\quad
a_\ell\in\mathcal O,\quad c_0\in\mathcal O^\times
\quad\text{对全部 }N\in4\mathbf Z_{>0}\text{ 同时成立}.
}
\tag{34}
$$
这也直接证明新子式在实际 $\lambda,\kappa,u$ 参数族上不恒零：
不是把独立形式参数的某个非零值当成实际曲线上的结论。

特别 $v_p(\det\mathbb M^\natural)=0$，没有新增行列式深度损失。
原测试中的 $D/\kappa^N$ 只在实际 D 深门上使用，
故 (9) 仍整有界；(15) 的原 $\lambda^N\kappa^{-2N}$ 则明确保留。
$a_\ell,c_0$ 可依 p、N，但对固定 p、N 不依观察深度 n。
不能把变动 N 的测试族免费用于固定多项式的 N 递推。

## 7. 原完整 π4 返回和同一 E 深/浅门的双来源

由 (6)、(9)，全部原观察严格满足
$$
\boxed{
(\pi_4)_*(q_N^\natural\mu_0)=
\beta^N(\pi_4)_*\mu_0 .
}
\tag{35}
$$
N 为四的倍数，$\beta^N=\lambda^N$。
所有原 S/T Mellin 总行、旋转支及物理 word 的转置因此保持；
(30) 没有取代 (35) 的完整范围。

置 $\mathcal E_N=\{E_{YW}\in p^N\}$。
R690 第5节的真实返回只用共同隐藏性、同一原门和完整
$D_*/E_{YW}$ 核，因而对 (10) 任意有限整权线性成立。
它严格给
$$
\boxed{
\begin{aligned}
Y_*(1_{\mathcal E_N}q_N^\natural\mu_0)&=\lambda^{2N}\nu_S,\\
W_*(1_{\mathcal E_N}q_N^\natural\mu_0)&=\lambda^{2N}6\delta\nu_T,\\
Y_*(1_{\mathcal E_N^c}q_N^\natural\mu_0)
 &=(\lambda^N-\lambda^{2N})\nu_S,\\
W_*(1_{\mathcal E_N^c}q_N^\natural\mu_0)
 &=(\lambda^N-\lambda^{2N})6\delta\nu_T.
\end{aligned}}
\tag{36}
$$
这是原未缩放 Y、W 的整个来源身份。推导使用
$E_{YW},D_*$ 双深的完整返回，而非把 cd 同深事件直接相认成
较大的 E 深事件。其 $C^\perp$ 单位补项正是 (12)、(14)。

例如令
$$
f_w(X)=1_{X\ {\rm unit}}\langle X\rangle^{d_pw},
\quad d_p=p-1,\quad
J_S(w)=\int f_w\,d\nu_S,\quad J_T(w)=\int f_w\,d\nu_T.
$$
(36) 直接给相同系数乘 $J_S(w),6\delta J_T(w)$。
两原质量本来为零；若两原中央导数也为零，
则这四个显示的完整中央行均为零。
这里来源系数没有观察变量缩放，不额外产生一个 scale log。

R686 的原两个横向轴仍为
$$
Z=W-b_YY,\quad b_Y=(20+3\omega)/17,\qquad
V=36Y-(17-3\omega)W,\qquad
\gamma=\chi_{29}\chi_{E_{YW}}\in\{\pm1\}.
$$
q、E 门及全部隐藏参数与 Y/W 同时正交。
完整 Z 核为 $\gamma\lambda R_Y$，V 核为
$\gamma\lambda K_W$。S 偶，且 $K_{72}T=T$，
所以对每个 $m\ge0$，
$$
\boxed{
\begin{aligned}
Y_*(1_{\mathcal E_N}1_{\{Z\in p^m\}}q_N^\natural\mu_0)
 &=\lambda^{2N}(\gamma\lambda)^m\nu_S,\\
W_*(1_{\mathcal E_N}1_{\{V\in p^m\}}q_N^\natural\mu_0)
 &=\lambda^{2N}(\gamma\lambda)^m6\delta\nu_T.
\end{aligned}}
\tag{37}
$$
精确环带再乘 $1-\gamma\lambda$；E 浅门把 $\lambda^{2N}$
换成 $\lambda^N-\lambda^{2N}$。
真实 $\gamma=\pm1$ 和原 $1\pm\lambda$ 单位性质均保留。
(37) 只用于所显示的横轴和相应观察，未把四个单位切集相互交换。

R638/R692 的三态为
$$
e_0=\mu_0,\quad e_1=K_W\mu_0,\quad
e_2=h_W-e_1,\qquad h_W=-\tfrac12H_{2,W}\mu_0.
$$
由于当前权及门是 W 的真伙伴，(36) 在完整三态上给
$$
\boxed{
W_*(1_{\mathcal E_N}q_N^\natural(e_0,e_1,e_2))
=\lambda^{2N}6\delta(\nu_T,\nu_T,-\nu_T).
}
\tag{38}
$$
这里使用原 $H_2T=0$，不是沿用旧权一般 $B_W$ 的质量推论。
相应 W-unit 质量也全为零。本文的 $h_W$ 不与旧其他两态的 h 混同。

## 8. 两冻结系数对实际外部的不同贡献

保持 R679 的整个域、原归一观察及同一个固定 N 测试：
$$
\begin{aligned}
\mathsf E_i(n)&=\{Y_i\in p^n\},&
\mathsf{CD}_N&=\{c,d\in p^N\},\\
\Gamma_n&=\mathsf E_0(n)\cap\mathsf E_1(n),&
\mathsf I_n&=\Gamma_n\cap\mathsf{CD}_N,\\
\mathsf V_{i,n}&=\mathsf E_i(n)\cap\mathsf{CD}_N,&
\mathsf O_{i,n}&=\mathsf V_{i,n}\setminus\mathsf I_n,\\
\mathsf X_{i,n}&=\mathsf E_i(n)\setminus\mathsf{CD}_N.
\end{aligned}
$$
各行仍用自己的 $Y_i/(-\kappa)^n$ 单位 Mellin 观察。
原 C/D 门、第二支实际旋转和所有 $\lambda,\kappa$ 系数全保。

因 $\mathscr B=S$，未过滤的整 Mellin 身份对 $n\ge N$ 为
$$
\mathcal V_{i,n}^{S,\natural}
=\epsilon_i\lambda^{n+3N}J_S,\qquad
\mathcal X_{i,n}^{S,\natural}
=\epsilon_i\lambda^{n+N}(1-\lambda^{2N})J_S.
\tag{39}
$$
但两冻结来源不同。完整地写
$$
\mathscr S_i^\natural(t)=c_iS+
 \sum_{a=1}^{30}t^aT_{i,a,N,p},\qquad (c_0,c_1)=(c_0,0).
$$
令 $\mathsf T$ 是实际序列 $n\mapsto n+1$，并置
$$
P_{30}=\prod_{a=1}^{30}(\mathsf T-\lambda^2\kappa^a),\quad
U_{30}=\prod_{a=1}^{30}(1-\kappa^a),\quad
V_{30}=\prod_{a=1}^{30}(1-\lambda\kappa^a).
$$
则三条整个实际行准确为
$$
\boxed{
\begin{aligned}
P_{30}\mathcal I_{i,n}^{S,\natural}
 &=\epsilon_i c_i\lambda^{2n+2N+60}U_{30}J_S,\\
P_{30}\mathcal O_{i,n}^{S,\natural}
 &=\epsilon_i\left[
 \lambda^{n+3N+30}V_{30}
 -c_i\lambda^{2n+2N+60}U_{30}\right]J_S,\\
P_{30}\mathcal X_{i,n}^{S,\natural}
 &=\epsilon_i\lambda^{n+N+30}(1-\lambda^{2N})V_{30}J_S.
\end{aligned}}
\tag{40}
$$
每一移位保自己的真实域与移动观察，$c_0$ 固定 p、N 后不依 n。
(40) 保了第二支冻结来源为零的实际差别，没有把两个系数重新设成一。
它是完整纯 S 外部的返回，不给同域上的另一 T 观察免费赋零。

## 9. 同一个负一深支、全部新高项和完整 T 补偿

(15) 与 (30) 给
$$
\boxed{J_2^\natural
=\frac{\ell_0^2}{2b\Omega^2}\lambda^N\kappa^{-2N}.}
\tag{41}
$$
原角型仍迫第2节四 sigma 平均只有
$$
a\in\mathcal A=\{2,8,14,20,26\}.
$$
这些都是同一个实际 q 的条件系数；除 $J_2$ 外不指定其值。
整性给
$$
v_p(J_a^\natural)\ge-aN.
\tag{42}
$$

用 R679 第9节相同的完整函数
$$
\begin{aligned}
\mathscr H_a(t)={}&
6b\sum_{\substack{k\ge1\\k\equiv1(6)}}
 \frac{h^kt^k}{k}I_{\Sigma_5,-k}M_{X_5,k+a}\\
&+6b\sum_{\substack{k\ge1\\k\equiv3(6)}}
 \frac{h^kt^k}{k}I_{X_5,-k}M_{\Sigma_5,k+a}
+3\sum_{\substack{k\ge1\\k\equiv5(6)}}
 \frac{h^kt^k}{k}I_{Z_5,-k}M_{Z_5,k+a},
\end{aligned}
\tag{43}
$$
$h=b_L/b_Y$；负矩保原 Q-unit，正矩保完整 L 总输入。
原 R665 两个真实 log 观察之差在同一 L 深支为
$$
\boxed{
\Delta^\natural_{N,n}
=2\beta^n\sum_{a\in\mathcal A}
  \kappa^{an}J_a^\natural\mathscr H_a(\kappa^n).
}
\tag{44}
$$
没有删任何新负矩或高正矩。

$k=1,a=2$ 的首项用 $M_{X_5,3}=6\Omega^3$，给
$$
72b\Omega^3h\,\beta^n\kappa^{3n}
 J_2^\natural I_{\Sigma_5,-1}.
$$
其余 $k=1$ 项均含同一个 $I_{\Sigma_5,-1}$；
由 (41)–(42)，相对首项多至少 $(a-2)(n-N)$ 层。
对奇 $k\ge3$，保 log 分母的估计
$kn-v_p(k)\ge3n$ 给最浅尾界 $5n-2N$。
所有 $a>2$ 的尾又至少多 $(a-2)(n-N)$ 层。

所以 R655 已付的同一个原 $I_{\Sigma_5,-1}\ne0$ 给
$$
\boxed{
v_p(\Delta^\natural_{N,n})
=3n-2N+v_p(I_{\Sigma_5,-1})
\quad(n>N,\ 2n>v_p(I_{\Sigma_5,-1})).
}
\tag{45}
$$
本文不把这个原负矩改称单位，也不把固定 CM 多项式密度引理用于它。

三十次权允许更多原 pair 正矩，因此旧六次测试或旧八角域的
零质量不移用。所有相对 Mellin 都保持完整质量项，例如
$T-\langle b_Y\rangle^{d_pw}S$ 的导数仍含
$-d_p\log\langle b_Y\rangle\,S(0)$。

若原 $J'_T(0)=0$，原 R662/R665 完整分解仍是
$$
\boxed{
\mathcal E_+^\natural-\mathcal E_-^\natural+
\mathcal R_{N,n}^\natural=-\Delta^\natural_{N,n}.
}
\tag{46}
$$
$\mathcal E_\pm$ 是两条原 T 外部，$\mathcal R$ 是完整 L 浅补域；
各自移动 W-unit cut、q 转置、$\kappa$ 尺度及 log 质量全部保留。
(36)–(38) 新增的是特定 E/Z/V 真门下的完整原 T 返回。
尚不能把 (46) 的不同混合域直接认成这些门的组合。

特别 R685 的 $A_T$ 观察仍是
$b_YY+\kappa^N(W-b_YY)$ 且保 Y-unit，
本篇 $\mathscr W$ 则是未缩放原 W，二者不能因 (30) 而等同。
下一问题是以 (36)–(38) 的新同源中央行控制 (46) 的完整补偿。
主目标未在本文宣称完成。

## 10. 公开复现和范围

脚本：
[check-r693-neutral-g12-four-source-adaptation.js](../scripts/check-r693-neutral-g12-four-source-adaptation.js)。
文件名保早期实验名称；下面实际参数产生本篇次数 6、12、18、24、30
五个 G 块。附加 B 块只供显示对照，(7) 的最终构造不使用它。

~~~sh
node topics/rank2-sha-infinitely-many-p/scripts/check-r693-neutral-g12-four-source-adaptation.js --max-block=4 --taus=2,3 --with-b --free-normalizations
~~~

已成功公开运行：

- GitHub Actions run：43684255990；
- job：132721269948；
- source commit：e335b329641fbc78c451bafa6285bf9be66a2ff1；
- 脚本 SHA256：
  fba29350375f415a76e13f3f1b498de4abdf77113aa3a6e368a794668a182d5e；
- 原 R594 生成算法 SHA256：
  34b630315837c5418d05f6c2984c93c29a680f7802b26dd85391303eee387873；
- stdout：21012 字节；
- stdout SHA256：
  c8b41f63aff1365eb652767e11abec1f5a00961433bc2c81bb64a3673101a5ca。

[公开运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43684255990)。

全部矩阵、全31行验证、C 至三十次和实际选列均在算法内存中重建；
仓库不保存可重算输出。辅助计算只用于 (32)–(33) 的固定分子非零。
第3节独立支付特征零半周期关系，第6节支付实际参数曲线和整逆；
没有把辅助秩、辅助解或一个非零子域当成主中央非零。

主要依赖：
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md)；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md)；
[R669](R669-original-double-s-six-dimensional-source-return.md)；
[R679](R679-neutral-degree-twelve-three-s-and-exterior-return.md)；
[R686](R686-original-yz-core-and-same-source-st-unit-failures.md)；
[R690](R690-native-w-source-of-the-same-adapted-cd-carry.md)；
[R638](R638-original-yw-three-state-and-word-compensation.md)；
[R655](R655-original-sigma-five-schwartz-and-rank-one-negative-moment.md)；
[固定 CM 单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)。
