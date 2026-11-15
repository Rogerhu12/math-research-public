# 原四个单反射、分别偶两态及保第四输入的完整边界

日期：2026-11-15。**状态：已证明。**

本注沿原六输入来源，支付同一个 $h_W=e_1+e_2$ 在四个原输入单反射下的完整作用。来源 $h_+=h_W+e_0/2$ 在这四个输入分别偶；其整个共同二倍覆盖有显示的四变量多项式，不只给边际或质量。由已付 whole $\mathcal S_4$ 核得到原坐标全部独立深度矩形，最后准确给出保 $\xi_2,x,d$ 的边界。

原最终 $q_N^*$ 仍真正依赖 x。下面所有带权返回保完整 $q_N^*$、原单位指示和 Y/W 观察的实际转置；未加权边界不被代入丢失三个输入的混合切集。

## 1. 同一六输入与四 sigma 恒等式

保原规范
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\qquad
e_0=-\nu_\sigma^{\otimes6}/84
$$
及物理输入
$$
(\xi_1,\xi_2,\xi_3,x,c,d).
$$
在选定四输入 $I=(\xi_1,\xi_3,x,c)$ 上使用 R493 的同一个矩阵
$$
H=\begin{pmatrix}
1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1
\end{pmatrix},\qquad
E=\operatorname{diag}(1,\omega,\omega^2,1),\qquad A=EH/2.
\tag{1}
$$
R493 的完整来源身份为
$$
h_W=-A_*e_0=\omega^2\mathcal T_*e_0 .
\tag{2}
$$
另外两个输入 $\xi_2,d$ 不动。本文的 $h_W$ 不与第三 sigma 分支中另一个同名 h 混用。

对四个复变量 w，记
$$
F(w)=\prod_{j=1}^4\sigma(w_j),\qquad
G(w)=\prod_{j=1}^4\sigma((Hw)_j/2).
$$
令 $r_j$ 只把 $w_j$ 反号。准确的四 sigma 加法式是
$$
\boxed{G(w)-G(r_jw)=F(w)\qquad(1\le j\le4).}
\tag{3}
$$
为直接核定常数，置
$$
a=(w_1+w_2)/2,\ b_0=(w_3+w_4)/2,\quad
c_0=(w_1-w_2)/2,\ d_0=(w_3-w_4)/2.
$$
则 G 是
$\sigma(a+b_0)\sigma(a-b_0)\sigma(c_0+d_0)\sigma(c_0-d_0)$，
而四个 $G(r_jw)$ 都是
$\sigma(a+d_0)\sigma(a-d_0)\sigma(c_0+b_0)\sigma(c_0-b_0)$。
原 sigma 加法式给二者之差
$\sigma(a+c_0)\sigma(a-c_0)\sigma(b_0+d_0)\sigma(b_0-d_0)=F(w)$。
所以 (3) 不含一个未定的平方根、相位或比例常数。

E 与每个 $r_j$ 交换，且
$F(Ew)=F(w)$，因为 $1\cdot\omega\cdot\omega^2\cdot1=1$。
原联合生成函数准确为
$$
\mathcal F_{e_0}
=-\frac{\sigma(z_2)\sigma(z_d)}{84}F(z_I),\qquad
\mathcal F_{h_W}
=\frac{\sigma(z_2)\sigma(z_d)}{84}G(Ez_I).
\tag{4}
$$
因此，对四个**物理**单反射
$R_j,\ j\in I$，得到完整六变量恒等式
$$
\boxed{(R_j)_*e_0=-e_0,\qquad
(R_j)_*h_W=e_0+h_W.}
\tag{5}
$$
它保全部未反射输入，没有先取某个边际。

## 2. 分别偶的实际来源

定义
$$
h_+=h_W+\frac12e_0.
\tag{6}
$$
由 (5)，
$$
\boxed{(R_j)_*h_+=h_+\quad(j\in I).}
\tag{7}
$$
另外 $\xi_2,d$ 仍各有原独立 sigma 因子，所以在这两轴分别为奇。
这给同一个原两态的精确奇偶分解，而不是从总角型猜各坐标的奇偶性。

下面给出 (6) 的整个代数 theta 表达。对四个代数变量 $X_i$ 定义
$$
D_{ij}=(X_i-X_j)^2,\qquad
A_{ij}=X_iX_j(X_i+X_j)+2b,\qquad
B_{ij}=X_i^2X_j^2-4b(X_i+X_j),
$$
$$
\boxed{\mathcal K(X_1,X_2,X_3,X_4)
=D_{12}B_{34}+D_{34}B_{12}-2A_{12}A_{34}.}
\tag{8}
$$
这里的 $A_{ij},B_{ij}$ 是本式多项式，不是某个新物理轴。

在四个选定输入上取原共同二倍覆盖，而保持 $\xi_2,d$ 不变。令
$$
(X_1,X_2,X_3,X_4)
=\bigl(x_b(z_1),\ \omega x_b(z_3),\
       \omega^2x_b(z_x),\ x_b(z_c)\bigr).
$$
则准确有
$$
\boxed{
\begin{aligned}
&\mathcal F_{h_+}(2z_1,z_2,2z_3,2z_x,2z_c,z_d)\\
&\quad=\frac{\sigma_b(z_2)\sigma_b(z_d)}{84}
 \sigma_b(z_1)^4\sigma_b(z_3)^4
 \sigma_b(z_x)^4\sigma_b(z_c)^4
 \mathcal K(X_1,X_2,X_3,X_4).
\end{aligned}}
\tag{9}
$$

为证明全式，先不加 E 的单位缩放，写
$x_i=x_b(z_i)$、$y_i=y_b(z_i)$，其中 $y_i^2=x_i^3+b$。
两点加法给
$$
x(z_i\pm z_j)=\frac{A_{ij}\mp2y_iy_j}{D_{ij}},\qquad
A_{ij}^2-4y_i^2y_j^2=D_{ij}B_{ij}.
\tag{10}
$$
把两对 $(z_1,z_2),(z_3,z_4)$ 代入原 sigma 加法式，得到
$$
G(2z)=\prod_i\sigma(z_i)^4
 \left(\mathcal K(x_1,x_2,x_3,x_4)+8y_1y_2y_3y_4\right).
\tag{11}
$$
原倍点规范是 $\sigma(2z)=-2y(z)\sigma(z)^4$，
故 $F(2z)/2=8\prod_i y_i\sigma(z_i)^4$。
(4)、(6) 消去该项。再用
$x(\omega z)=\omega x(z)$、
$x(\omega^2z)=\omega^2x(z)$ 和
$\prod_iE_i^4=1$，即得 (9)。
本证明先在 (10) 分母非零处成立，随后由全纯恒等延拓；
(8) 已是多项式，没有剩余除式或未消极点。

## 3. 全部半特征和 whole 四度核

在 (9) 的共同覆盖上，每个选定变量属于标准偶半特征的
$\mathcal S_4$；另外两变量保原 odd $\mathcal S_1$。
也可直接从 (4) 看出：$A=EH/2$ 是 Hermitian unitary，
共同乘二后各第一列的四个 sigma 系数都是 CM 单位，
总 degree 四，和其余三列的 Hermitian 交叉为零。
四个 odd 半特征的乘积为标准 even 特征。
因此整个两态落在同一个
$$
\mathcal S_4^{\boxtimes4}\boxtimes
\mathcal S_1\boxtimes\mathcal S_1
\tag{12}
$$
的实际张量格中，没有随伙伴变化的 flat twist。

保
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda,\qquad\kappa=p\lambda^2 .
$$
R506 已在现射线 $g=\pi_0/\bar\pi_0\equiv3\bmod8$ 上支付完整中心
及 $\sigma(2z)$ 的绝对锚，得到
$$
K_4=R
\tag{13}
$$
于整个标准 $\mathcal S_4$。
(12) 允许把它逐个应用在四个原输入上，保全部另外五个输入；
共同二倍因子是 p-unit，原普通限制与该固定倍点严格相容。

所以四个选定轴在基 $(e_0,h_W)$ 上具有**同一个**来源矩阵
$$
\mathcal A=
\begin{pmatrix}-1&1\\0&1\end{pmatrix},
\qquad\mathcal A^2=I,
\tag{14}
$$
且真实外部标量为 $\lambda$。
在 $(e_0,h_+)$ 基中则为 $\operatorname{diag}(-1,1)$。
另外两条原 sigma 轴的外核均为 $\beta$。
这里没有把 whole $\mathcal S_4$ 的结论延到任意未支付覆盖。

## 4. 原坐标所有独立深度及完整带权转置

令 $\boldsymbol n=(n_1,n_2,n_3,n_x,n_c,n_d)$，各 $n_j\ge0$。
记
$$
s=n_1+n_3+n_x+n_c,\qquad t=n_2+n_d,\qquad
P_{\boldsymbol n}
=\operatorname{diag}(\kappa^{n_1},\kappa^{n_2},
 \kappa^{n_3},\kappa^{n_x},\kappa^{n_c},\kappa^{n_d}),
$$
$$
\mathcal D_{\boldsymbol n}
=\{\xi_j\in p^{n_j}\text{ 对所有六输入}\}.
$$
这些是同一原坐标的真实矩形。由整张量核和 (14)，
$$
\boxed{
\begin{aligned}
e_0|_{\mathcal D_{\boldsymbol n}}
 &=\beta^{s+t}(P_{\boldsymbol n})_*e_0,\\
h_+|_{\mathcal D_{\boldsymbol n}}
 &=\lambda^s\beta^t(P_{\boldsymbol n})_*h_+,\\
h_W|_{\mathcal D_{\boldsymbol n}}
 &=\lambda^{s+t}(-1)^t(P_{\boldsymbol n})_*
 \left(h_W+\frac{1-(-1)^s}{2}e_0\right).
\end{aligned}}
\tag{15}
$$
每个方向的物理缩放都与其余五个坐标的限制相容，
故 (15) 可逐轴证明，不依赖“质量相同”或“边际相同”。

特别对原 $\mathsf{CD}_N=\{c,d\in p^N\}$ 和 $N\in4\mathbf Z_{>0}$，
$$
\boxed{
(e_0,h_W,h_+)|_{\mathsf{CD}_N}
=\lambda^{2N}(P_{c,\kappa^N}P_{d,\kappa^N})_*
 (e_0,h_W,h_+).
}
\tag{16}
$$
奇数 N 的 $h_W$ 行则是
$-\lambda^{2N}P_*(h_W+e_0)$，不能沿用 (16)。

(15)–(16) 对有界测试成立，但权必须完整转置。例如对任意
真实附加域 $\mathcal B$ 和有界 f，
$$
\begin{aligned}
\int_{\mathsf{CD}_N\cap\mathcal B}f\,q_N^*\,dh_W
=\lambda^{2N}\int
 1_{\mathcal B\circ P}\,(f\circ P)\,(q_N^*\circ P)\,dh_W,\qquad
P=P_{c,\kappa^N}P_{d,\kappa^N}.
\end{aligned}
\tag{17}
$$
此处 $q_N^*\circ P$ 一般不同于 $q_N^*$。
写 $u=\kappa^N$，则原 carry 行准确变为
$$
C\circ P=C,\quad
F\circ P=F+(u-1)\bigl(c+(2+3\omega)d\bigr),\quad
G\circ P=G+(3-2\omega)(u-1)\bigl(c+(2+3\omega)d\bigr).
\tag{18}
$$
原观察同时是
$$
Y\circ P=A+u(c+2d),\qquad
W\circ P=A+u(3\delta c+4d).
\tag{19}
$$
因此 (17) 保原六支 $D_\zeta/\kappa^N$、
全部 E-unit 条件、两个 C 返回补项、最高30次权及
(19) 各自的 unit/Mellin 测试。
(16) 本身不表示 cd 返回权 $\Phi_N$ 被 $\mathcal T$ 固定。

## 5. 保 x 的完整三变量边界及其准确范围

令 $\pi_x$ 保留 $(\xi_2,x,d)$，忘去 $(\xi_1,\xi_3,c)$。
在 (9) 中取被忘变量的生成参数为零。
多项式 $\mathcal K$ 的对应项是
$X_1^2X_2^2X_4^2$，系数一；
其单位缩放给 $\omega^2$。
因此
$$
\boxed{
(\pi_x)_*e_0=0,\qquad
(\pi_x)_*h_W=(\pi_x)_*h_+
=\frac{\omega^2}{84}\,
 \nu_\sigma\boxtimes[1/2]_*\nu_{\sigma^4}\boxtimes\nu_\sigma .
}
\tag{20}
$$
也可从 (4) 直接令三个参数为零：
$G(E(0,0,z_x,0))=\omega^2\sigma(z_x/2)^4$。
所以 (20) 保完整 x 生成函数，绝非只给某个正矩或质量。

对这条边界的 x 深度，真实核是 $+\lambda$；
对两个保留的 sigma 方向仍是 $\beta$。
例如所有三轴 unit 的校准矩为
$$
\int \xi_2x^4d\,
1_{\xi_2,x,d\ {\rm unit}}\,d(\pi_x)_*h_+
=\frac{\omega^2\Omega^6}{56}
 (1-\beta\kappa)^2(1-\lambda\kappa^4).
\tag{21}
$$
它只核定 (20) 的尺度及核心号，不被当作原中央的非零证明。

原 $q_N^*$ 的三个 x 系数为
$$
C_x=F_x=1/\delta,\qquad G_x=(32+31\omega)/3,
$$
而 Y、W 也含被 $\pi_x$ 忘去的输入。
所以一般不能将
$\int q_N^*1_{Y\ {\rm unit}}\log\langle Y\rangle\,dh_W$
写成对 (20) 的积分。
只有完整测试已经通过 $\pi_x$ 因子化时，才能使用 (20)；
否则必须使用 (17) 或整个 (9)，保所有被积变量。

## 6. 同一原 CD/O 域的三阶像

记 $c_j=c\circ\mathcal T^j$，$j=0,1,2$。由原矩阵，
$$
c_1=\frac{-\omega\xi_1+\xi_3-\omega^2x-\omega c}{2},\qquad
c_2=\frac{\omega^2\xi_1-\omega\xi_3+x-\omega^2c}{2},
$$
$$
\boxed{c_0+\omega^2c_1+\omega c_2=0,\qquad
W_j:=W\circ\mathcal T^j=Y+(3\delta-1)c_j+2d.}
\tag{22}
$$
因此三个 cd 域是
$$
\mathsf{CD}_{j,N}
=\{c_j,d\in p^N\}=\mathcal T^{-j}\mathsf{CD}_N.
\tag{23}
$$
任意两个 (23) 的交等于三个的共同交，
但三个单域一般不相等。

对 R713 原 $Y_1=Y+c-3d$，当 $n\ge N$，
$$
\mathcal O_{j,n}
=\mathcal T^{-j}
 \{Y\in p^n,\ c,d\in p^N,\ Y_1\notin p^n\}
=\{Y\in p^n,\ c_j,d\in p^N,\ c_j-3d\notin p^n\}.
\tag{24}
$$
$\mathcal T$ 固定 Y，且为 Hermitian unitary，
所以它与原正交 $P_{Y,s}$ 交换。
在 (24) 上原完整 T 观察变成
$$
W_j\circ P_{Y,(-\kappa)^n}^{-1};
\tag{25}
$$
不可仍写为 $W\circ P_{Y,(-\kappa)^n}^{-1}$。

最终权的真实 $\mathcal T$ 不变性已由前一短注支付。
故对任一原域 $\mathcal D$ 和有界 f，定义
$$
J_j(\mathcal D,f)=
\int_{\mathcal T^{-j}\mathcal D}
 (f\circ\mathcal T^j)\,q_N^*\,de_0 .
$$
原两态 $(\mathcal T_*)^2+\omega\mathcal T_*+\omega^2I=0$ 给
$$
\boxed{J_2+\omega J_1+\omega^2J_0=0.}
\tag{26}
$$
(26) 是三个真实转置域的完整关系。
它没有把三个 (24) 相认，也没有把 (25) 的移动观察删去。
原 $O_i/X_i$、E 浅门、参考和全部 log 质量继续保留；
下一步仍须将这些同域项同原已识别中央行比较。

## 依赖

- [R493](../results/R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)：原四 sigma 变换及完整来源常数。
- [R506](../results/R506-original-reflection-axis-four-core-and-complete-w-c-rectangles.md)：whole $\mathcal S_4$ 的完整中心和绝对反射锚。
- [R713](../results/R713-symmetric-frozen-sources-and-exact-paired-mixed-remainder.md)：原 CD/O 域和各自归一观察。
- [R734](../results/R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：实际最终 $q_N^*$。
- [最终 carry 的 T 不变性](2026-11-15-final-carry-t-invariance-and-same-weight-states.md)：原50列、双修正和完整六支转置。

本注使用原 sigma 加法式、whole 四度核及明确矩阵，
没有新增数值执行、辅助模数检查或可重算输出。
