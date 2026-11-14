# R404 — 两条原 rank-two 来源的完整 Riemann 联合、CM7/13/19 相位与二维中央运输

日期：2026-11-14。**状态：本篇证明同一原 S34、T72 的两个真实 mixed 十二 sigma 来源、全部半特征和 CM 相位、普通双输出各层 carry，以及惰性整 Gaussian 与收敛二维 Newton 恒等式。两条真正的中央失败给出完整 mixed 和的双轴二重零；没有给其中任一 mixed 单项预赋零或 scalar core。原无穷素数主目标仍未完成。**

## 1. 固定原来源和精确双变量结论

在 $E_b:y^2=x^3+b$ 上用原微分和 reduced sigma：
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad \sigma=z+\cdots,\quad
\delta^2=-3,\quad\omega=(-1+\delta)/2.
$$
置
$$
\gamma_7=(5+\delta)/2,\quad
\gamma_{13}=(7+\delta)/2,\quad
\gamma_{19}=4+\delta,\quad
\mathcal C(z)=
 \sigma(\delta z)\sigma(2\delta z)
 \sigma(\gamma_7z)\sigma(\bar\gamma_7z).
\tag{1}
$$
三个 $\gamma$ 的范数分别为 $7,13,19$，$\mathcal C$ 的 degree 为二十九。
R333、R398 的两条**原来源**是
$$
S(z)=-\frac{\mathcal C(z)\sigma(z)\sigma(2z)}{84},\qquad
T(z)=-\frac{\mathcal C(z)\sigma(3\delta z)\sigma(4z)}{504\delta}.
\tag{2}
$$
二者从 $z^6$ 起，首系数都是一。$b=17$ 时 $S$ 是原 $E_{17}$ 来源；
$T$ 是同一物理 frame 中的 $E_{24}$ 来源，准确关系为
$$
\nu_{\Phi_{24}}=c_*\nu_T,\qquad
c_*=-102816\sqrt[3]9,\qquad
\Omega_{p,24}=(24/17)^{-1/6}\Omega_{p,17}.
\tag{3}
$$
因此下文 $J_T'=0$ 与实际新曲线失败等价。不能只因两个 degree 相近认来源。
R401 又已给 $\kappa_{24}=1/(6\sqrt[3]3)$；其在 $p>3$ 为单位，
没有新增不确定的中央常数。

对两个独立变量 $z,w$，令
$$
x_0=\frac{3z}{2},\quad u_0=-\frac z2,\quad
y_0=\frac{(4+3\delta)w}{2},\quad v_0=\frac{(-4+3\delta)w}{2}.
$$
定义两个**完整** mixed 来源
$$
\begin{aligned}
B_2(z,w)&=\frac{\mathcal C(z)\mathcal C(w)}{42336\delta}
 \sigma(x_0+v_0)\sigma(x_0-v_0)
 \sigma(y_0+u_0)\sigma(y_0-u_0),\\
B_3(z,w)&=\frac{\mathcal C(z)\mathcal C(w)}{42336\delta}
 \sigma(x_0+y_0)\sigma(x_0-y_0)
 \sigma(u_0+v_0)\sigma(u_0-v_0).
\end{aligned}
\tag{4}
$$
本篇的基本原恒等式为
$$
\boxed{S(z)T(w)=B_2(z,w)+B_3(z,w).}
\tag{5}
$$
这是双变量、全函数身份，保留原两个输出；不是先取 $w=z$ 后猜测
Mellin 乘法。

## 2. Riemann 公式、绝对单位和两个真实整矩阵

原 sigma 加法公式是
$$
\frac{\sigma(x+u)\sigma(x-u)}{\sigma(x)^2\sigma(u)^2}
=x(u)-x(x).
\tag{6}
$$
右边的 $x(\cdot)$ 是 Weierstrass 横坐标。此式由两边的椭圆除子、
双极及 $u\to0$ 首项确定，没有未定常数。
将三个乘积除以
$\sigma(x)^2\sigma(y)^2\sigma(u)^2\sigma(v)^2$，
以下关系归结为四个横坐标间的二次多项式恒等式：
$$
\begin{aligned}
&\sigma(x+u)\sigma(x-u)\sigma(y+v)\sigma(y-v)\\
&\quad=\sigma(x+v)\sigma(x-v)\sigma(y+u)\sigma(y-u)
+\sigma(x+y)\sigma(x-y)\sigma(u+v)\sigma(u-v).
\end{aligned}
\tag{7}
$$
代入 (4) 给 (5)，包括 $84\cdot504=42336$ 及正负号。

若将原四个 active 参数写为 $(a,b,c,d)$，则 (7) 的两个运输矩阵为
$$
H_2=\frac12
\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
1&-1&1&1\\
-1&1&1&1
\end{pmatrix},\qquad
H_3=\frac12
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
\tag{8}
$$
两者都对称，$H_j^2=I$，且 $H_j^*H_j=I$；行列式是单位。
这里 $(a,b,c,d)=(z,2z,3\delta w,4w)$。
对应 active Hermitian Gram 是 $\operatorname{diag}(5,43)$；
加上两边各自的四个公共因子，完整 Gram 准确为
$$
\boxed{\operatorname{diag}(34,72),\qquad\text{交叉项为零}.}
\tag{9}
$$

### 2.1 半特征必须支付：共同的双 [2] 拉回

(4) 的单独线性形式含 $1/2$，因此不凭 (9) 就把它们称为
$E\times E$ 上原双线丛的截面。先对全体来源作
$(z,w)\mapsto(2z,2w)$，得到共同 degree $(136,288)$ 模型。

沿第一轴平移 $\lambda\in\Lambda$，两个 mixed 项的四个 active
增量分别是 $(3,3,-1,\pm1)\lambda$，模 $2\Lambda$ 全等于 $\lambda$。
沿第二轴，其四个增量均模 $2\Lambda$ 等于 $\delta\lambda$。
因此原 sigma 四个半特征乘积分别为
$\chi(\lambda)^4=\chi(\delta\lambda)^4=1$。
公共八因子本来都是偶拉回，半特征也为一。
连同 (9)，这证明双 [2] 后的**完整**线丛及 Gaussian 规范相同；
没有遗漏一个二挠 twist 或选取 projective lift。

普通局部测度可以直接使用 $1/2\in\mathbf Z_p$。
若使用上述全局双 [2] 模型，其全 tame Mellin 另乘
$$
\omega_p(2)^{\ell_1+\ell_2}
 \langle2\rangle^{(p-1)(u+v)}.
\tag{10}
$$
本篇所有原公式用拉回前的 (4)，故没有暗中删去 (10)。

### 2.2 对角的准确 CM7/13/19 式

$j=0$ 的规范给 $\sigma(\zeta z)=\zeta\sigma(z)$，$\zeta\in\mu_6$，
这是绝对恒等式，不只是有限表示中的项目相位。
令 $w=z$。$B_2$ 的四个 active 参数及 $B_3$ 的四个参数分别为
$$
\begin{array}{c|c}
B_2&B_3\\ \hline
\omega\bar\gamma_7&
 -\omega^2\bar\gamma_{19}\\
-\omega\gamma_{19}&\omega^2\gamma_7\\
-3\omega^2&\omega\gamma_{13}\\
-\omega^2\bar\gamma_{13}&-3\omega
\end{array}
\tag{11}
$$
每格还乘 $z$。两列的单位乘积准确为 $-1,+1$。于是
$$
\boxed{
\sigma(z)\sigma(2z)\sigma(3\delta z)\sigma(4z)
=\sigma(3z)\left[
 \sigma(\bar\gamma_{19}z)\sigma(\gamma_7z)\sigma(\gamma_{13}z)
-\sigma(\gamma_{19}z)\sigma(\bar\gamma_7z)\sigma(\bar\gamma_{13}z)
\right].
}
\tag{12}
$$
例如
$\bar\gamma_{19}\gamma_7\gamma_{13}=41+4\delta$，
其共轭为 $41-4\delta$，所以两边首项同为 $24\delta z^4$。
(11) 支付每个原方向的单位，而不从首项校准整条身份。

乘 $\mathcal C(z)^2/(42336\delta)$ 后，(12) 就是同一
$S(z)T(z)$ 的 degree106 恒等式。
其加法卷积中央导数不等于两个原导数的乘积；
后者必须通过 (5) 的两个独立输出来读。

## 3. 普通素数下的原十二输入联合

固定 $p>19,p\equiv1\pmod3$，用同一 $E_{17}$ 普通周期 $\Omega_p$。
令 $\nu=\nu_{\sigma,17}$ 为 R316 的原有界整测度：
$$
\mathcal A_\nu(Z)=\sigma(\Omega_p\log(1+Z)).
$$
取十二个独立原输入，公共八个分别记为 $a_1,\ldots,a_4$、
$b_1,\ldots,b_4$，active 四个记为 $t_1,\ldots,t_4$，测度为
$\mu=\nu^{\otimes12}$。置
$$
A=\delta a_1+2\delta a_2+\gamma_7a_3+\bar\gamma_7a_4,\qquad
B=\delta b_1+2\delta b_2+\gamma_7b_3+\bar\gamma_7b_4 .
$$
三个真实双输出是
$$
\begin{aligned}
Y_0&=A+t_1+2t_2,& V_0&=B+3\delta t_3+4t_4,\\
Y_2&=A+(3t_1+3t_2-t_3+t_4)/2,\\
V_2&=B+\{(-4+3\delta)t_1+(4-3\delta)t_2
                  +(4+3\delta)(t_3+t_4)\}/2,\\
Y_3&=A+(3t_1+3t_2-t_3-t_4)/2,\\
V_3&=B+\{(4+3\delta)(t_1-t_2)
                   +(-4+3\delta)t_3+(4-3\delta)t_4\}/2.
\end{aligned}
\tag{13}
$$
定义 $\eta_j=(42336\delta)^{-1}(Y_j,V_j)_*\mu$。
Amice 变换的唯一性和 (5) 给完整测度身份
$$
\boxed{\eta_0=\nu_S\otimes\nu_T=\eta_2+\eta_3.}
\tag{14}
$$
这也直接来自
$\nu^{\otimes4}=(H_2)_*\nu^{\otimes4}+(H_3)_*\nu^{\otimes4}$。
所有测度有界整，常数在当前素数是单位。

对任意 tame $\ell_1,\ell_2$，令 $d=p-1$，
$$
K_{\ell,u}(x)=\mathbf1_{x\ {\rm unit}}\,
 \omega_p(x)^\ell\langle x\rangle^{du}.
$$
则 (14) 准确给
$$
\boxed{
\int K_{\ell_1,u}(Y)\,K_{\ell_2,v}(V)\,d(\eta_2+\eta_3)
=J_{S,\ell_1}(u)J_{T,\ell_2}(v).
}
\tag{15}
$$
两个指示函数各自施加于 (13) 的实际完整输出。
它包括任意输入单位相消、非单位相加、所有公共输入和全部补域；
不是一个只在单叶或某个 active 子域上的身份。

在 principal 分支上 $J_S(0)=J_T(0)=0$。
若两条真正的曲线导数同时失败，(15) 的完整 mixed 和属于
$$
\boxed{u^2v^2\mathcal O\langle u,v\rangle.}
\tag{16}
$$
更强的测度表述为：若 $J'_S(0)=0$，则对任意连续 $\varphi$，
$$
\int \mathbf1_{Y\ {\rm unit}}d\log_p\langle Y\rangle\,
                   \varphi(V)\,d(\eta_2+\eta_3)=0.
\tag{17}
$$
另一个轴的对应式同样成立。这里的 $d\log_p\langle Y\rangle$
表示标量 $(p-1)\log_p\langle Y\rangle$，不是外微分。
(17) 只限制两个 mixed 来源之和；没有各自删去它们的未知中央行。

## 4. 原 primitive-input 的全部双输出环带

保同一真实 Hecke 规范
$$
\pi=\psi_{17}(\mathfrak p),\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p),\quad
\zeta=\psi_{24}(\mathfrak p)/\psi_{17}(\mathfrak p)\in\mu_6,
$$
$$
\kappa=p/\bar\pi^2,\quad
\lambda_S=\bar\pi^{-1},\quad
\lambda_T=\zeta/\bar\pi,\quad
\lambda_\sigma=\varepsilon^3/\bar\pi,\quad
\beta=\bar\pi^{-2}.
\tag{18}
$$
R316、R400 的实际完整 core 给
$$
\nu|_p=\lambda_\sigma[\kappa]_*\nu,\quad
\nu_S|_p=\lambda_S[\kappa]_*\nu_S,\quad
\nu_T|_p=\lambda_T[\kappa]_*\nu_T.
\tag{19}
$$
最后一式的物理核定是：
$\bar\pi_{24}=\zeta^{-1}\bar\pi$、
$\kappa_{24}=\zeta^2\kappa$，而原 $T$ 是 type0，
故 $[\zeta^2]_*\nu_T=\nu_T$。不能只把两个 Frobenius 宣布相同。
在 R399 的共同 ray 上 $\zeta=1$，所以两条目标 core 确相同。

令 $\mathcal D$ 表示十二个输入不全在 $p\mathbf Z_p$。
由于 $H_2,H_3\in\operatorname{GL}_4(\mathbf Z_p)$，
$\mathcal D$ 在两个 active 运输下不变。
因此 (14) 对同一个真实 $\mathcal D$ 的受限来源仍成立。
十二输入全在 $p$ 内的准确系数为
$$
a=\lambda_\sigma^{12}=\bar\pi^{-12}.
\tag{20}
$$
对 $n,m\ge0$，定义真实归一输出环带
$$
\mathfrak M_{j;n,m}
=\frac1{42336\delta}(Y_j/p^n,V_j/p^m)_*
 \left(\mathbf1_{\mathcal D,\ v_p(Y_j)=n,\ v_p(V_j)=m}\mu\right).
$$
写 $\nu_G^\times=\nu_G|_{\mathbf Z_p^\times}$。
从整条输出环带减去 (20) 的全深输入，准确得到
$$
\boxed{
\mathfrak M_{2;n,m}+\mathfrak M_{3;n,m}
=\lambda_S^n\lambda_T^m c_{n,m}
 [\beta^n,\beta^m]_*
  (\nu_S^\times\otimes\nu_T^\times),
}
\tag{21}
$$
其中
$$
c_{n,m}=
\begin{cases}
1,&\min(n,m)=0,\\
1-\zeta^{-1}\bar\pi^{-10},&n,m\ge1.
\end{cases}
\tag{22}
$$
证明只用 $a/(\lambda_S\lambda_T)=\zeta^{-1}\bar\pi^{-10}$。
若一条输出为单位，全深输入没有贡献；若两条均深，则同时把
两个环带深度减一再乘 $a$。没有遗漏“一条输出深、一条输出单位”的情形。

(22) 的第二常数是确定非零代数数：
若它等于零，则复绝对值给 $p^5=1$，矛盾。
本篇不额外宣称它对每个 $p$ 是单位。

全部 tame Mellin 的右边为
$$
\lambda_S^n\lambda_T^m c_{n,m}
 \omega_p(\beta)^{n\ell_1+m\ell_2}
 \langle\beta\rangle^{d(nu+mv)}
 J_{S,\ell_1}(u)J_{T,\ell_2}(v).
\tag{23}
$$
这保留每条轴自己的尺度及质量项。
在两原 principal 导数失败时，所有 (23) 同时属于 $u^2v^2$。
不能由此将任意更细输入域也设成零；本篇能受限的域恰由 (21)
所支付，不能删除其完整相加补域。


### 4.1 同一原双轴及全深输入的相容正则化

这里还能给这组实际超平面的共同正则化，不假定新增 mixed 单项
各自有 scalar core。对非零输出 $Y,V$，写
$n=v_p(Y),m=v_p(V)$，以其原单位部分 $p^{-n}Y,p^{-m}V$ 测试。
先取 $|q_1|_p,|q_2|_p<1$，在任一输出为零处把测试函数定义为零。
于是
$
q_1^nq_2^m
 K_{\ell_1,u}(p^{-n}Y)K_{\ell_2,v}(p^{-m}V)
\tag{23a}
$
是全空间上的连续测试函数；双环带和确实收敛到其测度积分。
记对 $\eta_2+\eta_3$ 的该积分为 $\mathcal R$，对同一原
$\mathcal D$ 来源之和的积分为 $\mathcal R_{\mathcal D}$。
置
$
\begin{aligned}
b_1(u)&=\lambda_S\omega_p(\beta)^{\ell_1}
                      \langle\beta\rangle^{du},\\
b_2(v)&=\lambda_T\omega_p(\beta)^{\ell_2}
                      \langle\beta\rangle^{dv},\\
e(u,v)&=a\omega_p(\beta)^{\ell_1+\ell_2}
                      \langle\beta\rangle^{d(u+v)} .
\end{aligned}
$
(19)、(21) 给真正的收敛等式
$
\boxed{
\mathcal R(q_1,q_2;u,v)
=\frac{J_{S,\ell_1}(u)J_{T,\ell_2}(v)}
 {(1-q_1b_1(u))(1-q_2b_2(v))},
\qquad
\mathcal R_{\mathcal D}=(1-q_1q_2e(u,v))\mathcal R.
}
\tag{23b}
$
第二式中 $q_1q_2e$ 正是十二输入同时深一层的真实贡献，
不是另选的归一化。

因此这两个**完整混合和**在 $(q_1,q_2)=(1,1)$ 有唯一的有理延拓。
中心的 $1-b_1(0)$、$1-b_2(0)$ 和 $1-e(0,0)$ 都非零：
其待减项的复绝对值分别为 $p^{-1/2},p^{-1/2},p^{-6}$。
这里有限 Teichmüller 值是代数根单位；此论证不把这些分母称为
$p$ 单位。取 $u,v$ 足够小，所有延拓都在同一个解析芽内。
先按第一轴再按第二轴、反向次序，或先消原全深输入因子，
都得到 (23b) 的同一个函数。原共同因子
$1-q_1q_2e$ 的可能极、零已经显式保留，不存在次序歧义。

principal 分支上，原质量为零使归一全对数行满足
$
\left(\frac{J_S(u)}{1-\lambda_S\langle\beta\rangle^{du}}\right)'_{u=0}
=\frac{J'_S(0)}{1-\lambda_S},
\qquad
\left(\frac{J_T(v)}{1-\lambda_T\langle\beta\rangle^{dv}}\right)'_{v=0}
=\frac{J'_T(0)}{1-\lambda_T}.
\tag{23c}
$
特别
$
\boxed{
\partial_u\partial_v\mathcal R(1,1;0,0)
=\frac{J'_S(0)J'_T(0)}
 {(1-\lambda_S)(1-\lambda_T)}.
}
\tag{23d}
$
这个结论只支付 (13) 的两个真实输出及共同 all-input 深缩放，
并且只对两个 mixed 来源的完整和成立。
它不建立每个单项的有理延拓，也不自动延拓到任意第三条新线性
输出。其价值是 (5)、原 $\mathcal D$ 和两种正则化次序已经在同一个
实际联合上严格相容，无需删去任何 unit 补域。

## 5. 一个实际辅助矩列，明确 mixed 来源并未各自消失

两条新联合的首个有用辅助矩也可显式给出。置
$$
E(z)=\frac{11}{4032\delta}\mathcal C(z)
 \left[
  \Theta(3z/2)\sigma(z/2)^2+
  \sigma(3z/2)^2\Theta(z/2)
 \right],\qquad\Theta=x\sigma^2.
\tag{24}
$$
这是实际有界整局部来源，在双 [2] 的同一全局模型中有已付半特征。
直接微分 (4) 得
$$
\boxed{[w^6]B_2(z,w)=S(z)/2+E(z),\qquad
       [w^6]B_3(z,w)=S(z)/2-E(z).}
\tag{25}
$$
具体地，$\mathcal C(w)=-42w^4+O(w^{10})$。
令 $q=3z/2,r=z/2$，
$a=(-4+3\delta)/2$、$b_1=(4+3\delta)/2$；
两个 active 乘积的 $w^2$ 系数分别为
$$
\sigma(q)^2\sigma(r)^2\{a^2x(q)+b_1^2x(r)\},\quad
-\sigma(q)^2\sigma(r)^2\{b_1^2x(q)+a^2x(r)\}.
$$
用 $a^2+b_1^2=-11/2$、$a^2-b_1^2=-12\delta$ 及 (6)
即得 (25)，包括所有常数。其差项从
$-55z^6/(192\delta)$ 起，并非零来源。

因此普通测度的准确辅助六次矩为
$$
\int V^6\,d\eta_2=\;720\Omega_p^6\,d\nu_{S/2+E},\qquad
\int V^6\,d\eta_3=\;720\Omega_p^6\,d\nu_{S/2-E}.
\tag{26}
$$
(26) 表示保留 $Y$ 推前后的测度等式。相加只返回原 $S$；
单项仍含实际 $E$ 的完整中央斜率。
这是把 (17) 的辅助列写到具体原来源，避免把所有 mixed 行
误称为原两条曲线的单线。

## 6. 惰性素数：整的二维 Gaussian 不是逐项假设

现在在 $E_1$ 的共同物理变量上用 (1)–(5)，即
$S=A_{34},T=A_{72}$。固定 $p>19,p\equiv5\pmod6$，
$$
d=p+1,\quad c=[z^d]\log(\sigma(z)/z),\quad v_p(c)=-1,\quad
R=p^{-1/(2p)}.
\tag{27}
$$
R301、R402 已完整证明
$$
\widehat\sigma(t)=\sigma(t)e^{-ct^d},\qquad
\|\widehat\sigma\|_R\le R,\qquad
\|\log(\sigma/t)-ct^d\|_R<p^{-1/(p-1)}.
\tag{28}
$$
这里 $\widehat\sigma=t\exp(\log(\sigma/t)-ct^d)$ 是实际解析定义；
单独的 $e^{-ct^d}$ 不需要在整个圆盘收敛。

将 $B_j$ 的十二个实际线性形式记为 $L_{j,i}(z,w)$，保留 (4) 的
整体常数，定义
$$
\Delta_j(z,w)=\sum_{i=1}^{12}L_{j,i}(z,w)^d
                       -34z^d-72w^d.
$$
惰性时系数的 $p$ 次幂模 $p$ 是 CM 共轭，故
$$
(az+bw)^{p+1}\equiv
N(a)z^{p+1}+\bar a b\,z^pw+a\bar b\,zw^p+
N(b)w^{p+1}\pmod p.
$$
(9) 的完整 Hermitian Gram 因而准确给
$$
\boxed{\Delta_j\in p\mathcal O[z,w].}
\tag{29}
$$
这不是令 $\Delta_j=0$。真正共同 Gaussian 的余项是
$$
\boxed{
\widehat B_j
=B_j e^{-34cz^d-72cw^d}
=\frac1{42336\delta}
 \prod_{i=1}^{12}\widehat\sigma(L_{j,i})\,
                    \exp(c\Delta_j).
}
\tag{30}
$$
全部 $L_{j,i}$ 的系数在 $\mathcal O$ 中整，线性形式在双 $R$ 圆盘
范数不超过 $R$。
由 (29)，$c\Delta_j$ 的加权赋值至少 $d/(2p)>1/(p-1)$，
所以 (30) 的最后指数收敛且范数一。于是
$$
\boxed{\|\widehat B_j\|_{R,R}\le R^{12}.}
\tag{31}
$$
这支付真正 mixed 来源的全部 Gaussian，包括高阶项，
而非从某个裸 mod $p$ Cartier 或总次数推出解析控制。

双 [2] 时，(27) 中两个 Gaussian 同时乘 $2^d$；
其系数缩放与两个 Newton 分母准确相消。
所以 (30) 与 §2.1 的全局模型相容，并未把 $[2]$ 当成无成本换源。

## 7. 完整二维 Newton、全尾和两条失败的实际后果

定义
$$
a_{j;h,k}=(34c)^{-h}(72c)^{-k}
 [z^{dh}w^{dk}]\widehat B_j,\qquad
\mathcal N_j(u,v)=
 \sum_{h,k\ge0}a_{j;h,k}(u)_h(v)_k .
\tag{32}
$$
由于两个公共四因子分别在对应轴至少四阶为零，
$h=0$ 或 $k=0$ 的系数都为零。由 (31)，其余系数满足
$$
\boxed{
v_p(a_{j;h,k})\ge
 \left\lceil\frac{(p-1)(h+k)+12}{2p}\right\rceil
\quad(h,k\ge1).
}
\tag{33}
$$
故 $\mathcal N_j\in p^2uv\mathcal O\langle u,v\rangle$，并过收敛。
对全部非负整数 $r,t$，有限 Newton 卷积准确给
$$
\boxed{
\mathcal N_j(r,t)=
r!t!(34c)^{-r}(72c)^{-t}
 [z^{dr}w^{dt}]B_j.
}
\tag{34}
$$
阶乘、权三十四与七十二均按各自原轴保留。

完整 (5) 和共同 (30) 现在给
$$
\boxed{\mathcal N_2(u,v)+\mathcal N_3(u,v)
                =J_{34,p}(u)J_{72,p}(v).}
\tag{35}
$$
右边是 R301/R303 和 R402 的两个**实际半因子**，不是
给 mixed 单项另设的 signed Selmer 来源。精确物理缩放为
$
S_{17}(z)=17^{-1}A_{34}(17^{1/6}z),\qquad
\Phi_{24}(z)=C_{24}A_{72}(24^{1/6}z),\quad
C_{24}=-6048\sqrt[3]9.
$
各自 Gaussian 的 $c$ 同时乘 $17^{d/6}$ 或 $24^{d/6}$，所以逐个
Newton 系数给
$
J_{S_{17},p}=17^{-1}J_{34,p},\qquad
J_{\Phi_{24},p}=C_{24}J_{72,p}.
$
这些固定标量在当前范围都是单位。因此 (35) 的失败条件确为
同两条固定曲线的原条件。

对任何 $H\ge2$，截断到 $h+k\le H$ 的整条 Taylor–Newton 尾、
以及在单位双盘上的任一单次轴导数和双一次导数，其赋值至少
$$
\boxed{
\left\lceil\frac{(p-1)(H+1)+12}{2p}\right\rceil .
}
\tag{36}
$$
因为 $(u)_h$ 及其一次导数的整数系数范数不超过一，
(33) 逐项给此界，且该下界随总指标趋于无穷。
中央双一次系数的准确全行特别是
$$
\sum_{h,k\ge1}(-1)^{h+k}(h-1)!(k-1)!
       (a_{2;h,k}+a_{3;h,k})
 =J'_{34,p}(0)J'_{72,p}(0).
\tag{37}
$$
更完整的一轴行保留任意另一轴：
$$
\sum_{h,k\ge1}(-1)^{h-1}(h-1)!
       (a_{2;h,k}+a_{3;h,k})(v)_k
=J'_{34,p}(0)J_{72,p}(v),
\tag{38}
$$
并有交换两轴的对应式。

若两个实际导数均为零，R303、R402 的整二次比较分别给
$J_{34}\in p^2u^2\mathcal O\langle u\rangle$、
$J_{72}\in p^2v^2\mathcal O\langle v\rangle$，所以
$$
\boxed{\mathcal N_2+\mathcal N_3
        \in p^4u^2v^2\mathcal O\langle u,v\rangle.}
\tag{39}
$$
(39) 保留了整个 mixed Gaussian、原高位进位和全部两轴系数。
不能将 (37) 的乘积为零单独反推某一条不为零；
真正新增的接口是 (38)、(39) 的全行及其明确尾界。

## 8. 另一个原 Riemann 式：CM7 对的纯二、三挠返回

下面的低 degree 身份也可直接核定，不需要新矩阵。
在 (7) 中取
$$
x=5z/2,\quad u=\delta z/2,\quad y=3z/2,\quad v=-z/2.
$$
第一项为 $\sigma(\gamma_7z)\sigma(\bar\gamma_7z)\sigma(z)\sigma(2z)$。
第二项中
$(3+\delta)/2=-\omega\delta$、
$(3-\delta)/2=\omega^2\delta$，两单位乘积为负一。
第三项中 $(\delta-1)/2=\omega$、$(\delta+1)/2=-\omega^2$，
两单位乘积也为负一。因此
$$
\boxed{
\sigma(\gamma_7z)\sigma(\bar\gamma_7z)\sigma(z)\sigma(2z)
+\sigma(2z)\sigma(3z)\sigma(\delta z)^2
=-\sigma(4z)\sigma(z)^3.
}
\tag{40}
$$
与原 $S$ 相乘后得到两条完整六 sigma 输入：
$$
\boxed{
S=\frac1{84}\left[
 \sigma(\delta z)^3\sigma(2\delta z)\sigma(2z)\sigma(3z)
+\sigma(\delta z)\sigma(2\delta z)\sigma(4z)\sigma(z)^3
\right].
}
\tag{41}
$$
它们的 degree 都是三十四，首项分别为 $108z^6$ 和 $-24z^6$，
准确返回原首项一。这里的固定二、三挠除子来自真恒等式，
不是另一个任意 degree34 全纯来源。
(41) 的测度式也保完整相加输出；不能对其中两项各自预赋中央零。

## 9. 已付范围及后继原观察

(5)、(11)–(14) 给了同两条固定曲线的实际 mixed 来源，
(21)–(23) 支付原 primitive-input 的全部双输出环带。
惰性时 (29)–(39) 又把这两个 mixed 来源送到同一原二维 Newton，
保留完整高位差而非只保首层同余。

目前尚未证明 (16) 或 (39) 与一个已证非零的原 mixed 行矛盾。
也未声称两个 mixed 来源分别具有原 $S$ 或 $T$ 的 Hecke 角色、
在整个 finite theta 空间上有 scalar core，或定义新的 rank-two 曲线。
后继可以在 (13) 的同一输出域比较 CM7/13/19 及实际二、三挠关系；
所有进一步域限制须由完整原联合支付。

直接依赖：
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、
[R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)、
[R333](R333-six-original-sigma-inputs-and-two-quadratic-negative-moment-return.md)、
[R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)、
[R400](R400-full-square-interpolation-determines-core-and-e24-cmseven-phase.md)、
[R401](R401-e24-exact-central-constant-from-four-original-modular-symbols.md)、
[R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)。

当前终端不可用；本篇按根规矩八用小文本 GitHub Contents API 提交，
不是本地 git pull。2026-11-14 03:02:45 UTC 读取 main
23ad2ab7143b72cab09c1908df23bd2897870d4e；
根 README blob 为 f787a306d90892d8dec765dc59747d60ba39f055，
本课题 README blob 为 f8dd8071ac0c2b31f344a40c15ac2a42796bf9af，
两者均与已读版本相同，无需重读。读号交根代理记入 HANDOFF。
