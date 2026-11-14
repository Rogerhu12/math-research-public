# R399：两条原 rank-two 来源的交叉四源、重叠 core 与完整碰撞域

日期：2026-11-14。**状态：已证明。** 本篇将 R398 的实际新来源与
R396 的原 $D,H$ 双谱放在同一普通测度中。所得四个全纯来源有准确的
交叉卷积身份；在一个固定无穷 ray 上，两个真正的 rank-two 目标具有
相同完整 core，两个新的 degree38 来源则有另一符号的完整 core。

进一步，原三输入中的 degree34 与 degree54 两个重叠输出分别有
带反射和不带反射的完整 core。本文支付它们在两个真实移动单位管上的
相交、换坐标、全部 tame 与中央尾。两条目标中央零因而给一族明确的
原双输入补域深度条件。未把未知参考斜率删掉，也未证明无穷素数主目标。

## 1. 固定原来源与四条全纯线

固定
$$
E_b:y^2=x^3+b,\quad b=17,\quad X=x^3,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,
$$
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad
\sigma=z+\cdots,\quad \Theta=x\sigma^2.
$$
所有来源都用这个原模型及同一普通周期 $\Omega$。沿用
$$
\begin{aligned}
P_2(X)&=X^2-\frac{4bX}{7}+\frac{16b^2}{7},\\
R_2(X)&=X^2+20bX-8b^2,\\
Q_4(X)&=(X+4b)(X^3-96bX^2+48b^2X+64b^3),\\
C&=C_{18}=\sigma^{18}(X-8b)P_2(X),\\
D&=\sigma^{16}x^2(X+b),\qquad
H=\sigma^{16}x^2R_2(X).
\end{aligned}
\tag{1}
$$
于是 $S=DC$ 是 R297 的原 rank-two 来源，$C(0)=H(0)=1$，
$D=z^6+\cdots$。

令
$$
K_{26}=\frac{\sigma(3\delta z)}{3\delta\sigma(z)}
       =\sigma^{26}xQ_4(X).
$$
本篇使用的两个新来源为
$$
\boxed{
\begin{aligned}
K&=D_{38}=K_{26}\frac{\sigma(z)^4\sigma(2z)^2}{4}
          =\sigma^{38}x(X+b)Q_4(X),\\
L&=H_{38}=K_{26}\frac{\sigma(4z)}{2\sigma(2z)}
          =\sigma^{38}xR_2(X)Q_4(X).
\end{aligned}}
\tag{2}
$$
$K=z^6+\cdots$，$L(0)=1$。两者都在整个 $\mathcal S_{38}=
\sigma^{38}L(38O)$；表达式中的商已由右边的全纯多项式支付。
它们也都是原有界整测度：每项 $\sigma^{38}x^{1+3j}$ 等于
$\sigma^{36-6j}\Theta^{1+3j}$，$0\le j\le6$。

具体除子也完全固定。$K_{26}$ 的零为
$E[3\delta]\setminus\{O\}$；
$K/K_{26}$ 的零为 $6(O)$ 加三个非零二挠点各二重；
$L/K_{26}$ 的零为 $E[4]\setminus E[2]$。
所以这些来源没有新非挠零点。

中间比值
$$
V_{22}=\frac{K_{26}}{\Theta^2}=\sigma^{22}Q_4(X)/x
$$
本身在 $x=0$ 有极；本文不用它作为有界输入。真正使用的是
$$
K=V_{22}D,\qquad L=V_{22}H.
$$
故有完整全纯身份
$$
\boxed{DL=HK=:E_{54},\qquad
T:=E_{54}C=S L=(HC)K.}
\tag{3}
$$
$E_{54}=z^6+\cdots$，$T=z^6+\cdots$，$HC(0)=1$。
R398 已严格证明 $T$ 正是新 $E_{24}$ 来源在当前 frame 的首项一版本，
并非仅同 degree 的候选。

### 1.1 实际曲线、周期和两个中央条件

取 R398 的相容同构与普通周期，实际 $E_{24}$ 来源 $\Phi_{24}$ 满足
$$
\boxed{\nu_{\Phi_{24}}=
c_*\,\nu_T=c_*\,(\nu_S*\nu_L)
=c_*\,(\nu_{HC}*\nu_K),\qquad
c_*=-102816\sqrt[3]9.}
\tag{4}
$$
$p>19$ 时 $c_*$ 是单位。这里的 $*$ 是**加法卷积**。
R398 的变量为 $\vartheta=(24/17)^{1/6}$，
$\Omega_{p,24}=\vartheta^{-1}\Omega_{p,17}$，所以没有把不在
$\mathbf Z_p$ 的代数数擅自当作测度变量缩放。

在更统一的 $E_1$ frame 中，
$S_b(z)=b^{-1}S_1(b^{1/6}z)$、
$T_b(z)=b^{-1}T_1(b^{1/6}z)$，
而 $C,H,L$ 的质量一规范在该同构下不带额外整体幂。
相容周期使两条原目标只差已列固定单位，中央零的比较无损。

用
$$
J_{G,\ell}(u)=\int_{\mathbf Z_p^\times}
 \omega_p(t)^\ell\langle t\rangle^{du}\,d\nu_G(t),\qquad d=p-1.
\tag{5}
$$
R295、R397、R400 的原中央导数在 principal 分支上与 (5) 的导数
只差明确非零尺度。因此本篇的同时失败条件准确为
$$
J'_{S,0}(0)=J'_{T,0}(0)=0.
\tag{6}
$$
$HC,K,L$ 不是新增的 rank-two 候选，不给它们预赋中央零。

## 2. 一个同时支付全部相位的固定无穷类

令 $\pi_0=\psi_0(\mathfrak p)$ 为 $E_1$ 的 $2\delta$-primary 生成元。
取
$$
\boxed{
\pi_0\equiv261631+198018\omega
\pmod{279072\mathcal O_K},\qquad279072=32\cdot27\cdot17\cdot19.
}
\tag{7}
$$
它准确等价于
$$
\pi_0\equiv-1+2\omega\pmod{32},\quad
\pi_0\equiv1\pmod{27},\quad
\pi_0\equiv\delta\pmod{17},\quad
\pi_0\equiv1\pmod{19}.
\tag{8}
$$
这是互素的真实 primary ray 类；固定 ray class 的 degree-one
素理想定理给正密度普通素数。以下删去有限的 $p\le19$ 及 $p=79$；
仍是同一固定无穷集合。

准确比值为
$$
g=\pi_0/\bar\pi_0:\quad
g\equiv27+8\omega\pmod{32},\quad
g\equiv-1\pmod{68},\quad
g\equiv39=1+38\pmod{76},\quad
g\equiv55=1+54\pmod{108}.
\tag{9}
$$
同时 $g\equiv19\pmod{36}$，所以原 $C_{18}$ 的 core 与 R396 相同。

原实际 Hecke 角色也相同，而不只是 ratio 相同：
$$
\boxed{\pi_{17}=\pi_{24}=-\pi_0.}
\tag{10}
$$
十七处由 $\delta^{48}\equiv-1\bmod17$ 给出。
二十四处用 R389 的原局部数据：二处
$(-2/N\pi_0)=-1$，三处 $\pi_0\equiv1\bmod9$ 使野三次角色平凡，
因此其相对于 $\psi_0$ 的扭曲也是负一。
这也说明共同同构根 $(24/17)^{1/6}$ 可在所选普通局部域中选取。

置
$$
\lambda=\lambda_0=1/\bar\pi_0=-1/\bar\pi_{17},\qquad
\kappa=p/\bar\pi_{17}^{\,2}.
\tag{11}
$$
$\lambda$ 为单位，$v_p(\kappa)=1$。
两条原 rank-two 目标都有实际完整 core
$$
\boxed{\nu_S|_p=-\lambda[\kappa]_*\nu_S,\qquad
       \nu_T|_p=-\lambda[\kappa]_*\nu_T.}
\tag{12}
$$
所以二者 principal 单位质量均为零。

## 3. 原 degree38、54 整块及 degree34 的反射

R396 已付偶数 $N$ 的**含中心**恒等式
$\mathsf T_{(1+N)v}=\mathsf T_v$。
因此 $g\equiv1+N\bmod2N$ 的原交织在整个 $\mathcal S_N$ 上为标量，
仍用同 degree 的真实来源定标。

对 $N=38$ 取 $\Theta((5+2\omega)z)$，
因为 $N(5+2\omega)=19$；对 $N=54$ 取
$\Theta(3\delta z)$，因为 $N(3\delta)=27$。
原 Theta core 与单位尺度已由 R316 支付。
(9) 因而给
$$
\boxed{
\nu_F|_p=\lambda[\kappa]_*\nu_F
\quad(F\in\mathcal S_{38}\ \text{或}\ \mathcal S_{54}).
}
\tag{13}
$$
它保全部 tame，不只保质量一线。特别 $K,L,DK,DL,HL$ 均适用。

degree34 的整个算子则必须保反射。$g\equiv-1\bmod68$ 时
交织为 $I_{-1}:F(z)\mapsto F(-z)$，原非零 $S$ 及 (12)
锚定其绝对标量为负一。因此
$$
\boxed{\nu_F|_p=-\lambda[-\kappa]_*\nu_F
       \quad(F\in\mathcal S_{34}).}
\tag{14}
$$
在 type0 上才可将 $[-1]_*$ 去掉。对下面未平均的联合，
不能先把 (14) 改成 R396 的 type0 简式。

原第一对仍有
$$
\boxed{
JD=aH,\qquad JH=d_1D,\qquad
a=\delta/(72b),\quad d_1=24b\delta,\quad J^2=-1,
}
\tag{15}
$$
以及 $\nu_G|_p=\lambda[\kappa]_*\nu_{JG}$，$G\in\langle D,H\rangle$。
于是 (3)、(4) 中的全部四源 core 都已付清。

整格与平移也包含在 (13)、(14) 内。使用原
$\sigma^Nx^i,\sigma^Nyx^j$ 的首阶单位基，未除以阶乘的辅助矩
逐列落在同一整 theta 格；primitive Heisenberg 交换子给不可约性。
不能只凭平移后复 degree 相同跳过这个整格步骤。

## 4. 同一个三输入中的两套完整 core

对
$$
G\in\langle D,H\rangle,\qquad F\in\langle K,L\rangle,
$$
定义实际三输入
$$
d\rho_{G,F}=d\nu_G(x_1)d\nu_F(x_2)d\nu_C(x_3).
\tag{16}
$$
记
$$
Y=x_1+x_3,\quad V=9x_1-8x_3,\qquad
Z=x_1+x_2,\quad U=19x_1-8x_2,\qquad
W=x_1+x_2+x_3.
\tag{17}
$$
$J$ 只作用第一来源 $G$，不改变量，不改 $F,C$。

### 4.1 degree54 的完整两坐标

$(x_1,x_2)\mapsto(Z,U)$ 的行列式为 $-27$，真实 Gram 为
$$
\operatorname{diag}(54,8208).
$$
整个 theta transform 为 $G(z+19v)F(z-8v)$；
交叉项 $16\cdot19-38\cdot8$ 准确为零。
所以每个 $U$ 矩截面都在整个原 $\mathcal S_{54}$。

令 $A_{54}$ 保 $U,x_3$、将 $Z$ 乘 $\kappa$。
在原输入中的矩阵是
$$
A_{54}=\frac1{27}
\begin{pmatrix}
19+8\kappa&8(\kappa-1)&0\\
19(\kappa-1)&8+19\kappa&0\\
0&0&27
\end{pmatrix}.
\tag{18}
$$
由 (13)，得到保持其余坐标的全联合式
$$
\boxed{\rho_{G,F}|_{Z\in p}
 =\lambda(A_{54})_*\rho_{G,F}.}
\tag{19}
$$
全 $(x_1,x_2)$ 深域的 core 是 $\lambda^2J$。
取消 (19) 后，其正交辅助同样有完整式
$$
\boxed{\rho_{G,F}|_{U\in p}
 =\lambda(B_{54})_*\rho_{JG,F},}
\tag{20}
$$
其中 $B_{54}$ 保 $Z,x_3$、将 $U$ 乘 $\kappa$；
$A_{54}B_{54}$ 在前两输入上准确为 $\kappa I$。

### 4.2 degree34 的完整带符号两坐标

$(x_1,x_3)\mapsto(Y,V)$ 的行列式为 $-17$，Gram 为
$\operatorname{diag}(34,2448)$。
整个 transform 为 $G(z+9v)C(z-8v)$；不作任何辅助平均。
由 (14)，令 $A_{34}$ 保 $V,x_2$、将 $Y$ 乘 $-\kappa$，则
$$
\boxed{\rho_{G,F}|_{Y\in p}
 =-\lambda(A_{34})_*\rho_{G,F},}
\tag{21}
$$
$$
A_{34}=\frac1{17}
\begin{pmatrix}
9-8\kappa&0&-8(1+\kappa)\\
0&17&0\\
-9(1+\kappa)&0&8-9\kappa
\end{pmatrix}.
\tag{22}
$$
另令 $B_{34}$ 保 $Y,x_2$、将 $V$ 乘 $-\kappa$。
因为 $G,C$ 都是偶来源，原 $(x_1,x_3)$ 同时反号保持测度；
从全部两输入深域准确得到
$$
\boxed{\rho_{G,F}|_{V\in p}
 =-\lambda(B_{34})_*\rho_{JG,F}.}
\tag{23}
$$
这里 $A_{34}B_{34}=-\kappa I$，同时反号才把它换回原全深 core。
(19)–(23) 都在同一未平均的三输入上成立，因而不需要假定两个
不同坐标系的 $\mu_6$ 投影可交换。

## 5. 两个真实碰撞管的全深度交叠

对 $n,m\ge1$，保原总输出，置
$$
\mathcal D_{n,m}
=\{Y\in p^n,\ Z\in p^m,\ W\in\mathbf Z_p^\times\}.
\tag{24}
$$
下列恒等式对任意有界输出测试 $\varphi$、对 (16) 的每个实际来源成立。

若 $n\ge m$，先用 (21) 的第 $n$ 层，
$W$ 准确变成 $x_2+(-\kappa)^nY$。
原输出为单位当且仅当 $x_2$ 为单位。
$Z$ 的深条件则准确为
$V+17x_2+8(-\kappa)^nY\in p^m$，
其中末项可在这个条件中删去，故
$$
\boxed{
\int_{\mathcal D_{n,m}}\varphi(W)\,d\rho
=(-\lambda)^n
 \int_{\substack{x_2\ {\rm unit}\\V+17x_2\in p^m}}
 \varphi(x_2+(-\kappa)^nY)\,d\rho .
}
\tag{25}
$$
若 $m\ge n$，同样用 (19)，得到
$$
\boxed{
\int_{\mathcal D_{n,m}}\varphi(W)\,d\rho
=\lambda^m
 \int_{\substack{x_3\ {\rm unit}\\U+27x_3\in p^n}}
 \varphi(x_3+\kappa^mZ)\,d\rho .
}
\tag{26}
$$
两个式子的原输出没有被换成部分输出；删去的只是已经属于指定
深度理想的条件项。

特别 $n=m=N$ 时，两个原**移动单位管**满足
$$
\boxed{
(-1)^N
 \int_{\substack{x_2\ {\rm unit}\\17Z-8Y\in p^N}}
 \varphi(x_2+(-\kappa)^NY)\,d\rho
=
 \int_{\substack{x_3\ {\rm unit}\\27Y-8Z\in p^N}}
 \varphi(x_3+\kappa^NZ)\,d\rho .
}
\tag{27}
$$
这是确切的域运输，不是矩阵可逆后预赋零。
两条管的交也能完整写出。因为
$$
\det\begin{pmatrix}-8&17\\27&-8\end{pmatrix}=-395=-5\cdot79,
$$
在本素数类上
$$
\boxed{
\{x_2\ {\rm unit},17Z-8Y\in p^N\}
\cap\{x_3\ {\rm unit},27Y-8Z\in p^N\}
=\mathcal D_{N,N}.
}
\tag{28}
$$
在右边 $x_2\equiv x_3\equiv-x_1\bmod p^N$，所以全部三个输入为单位。
它们不是 R339 的单单位深叶；交集和两个真正的补集都保留。

等价地，$A_{54}^{-N}A_{34}^N$ 在左管上是合法的部分整坐标映射，
将该受限测度送到右管，标量为 $(-1)^N$。
其全矩阵可能含 $\kappa^{-N}$；不能把它当作全 $\mathbf Z_p^3$
上的整自同构。其合法性正由 (25)、(26) 的实际域支付。

## 6. 全 tame 和原中央的收敛式

在 (25) 中取
$\varphi(t)=\omega_p(t)^\ell\langle t\rangle^{du}$。
因为 $x_2$ 为单位而 $(-\kappa)^nY$ 为深项，整条式为
$$
\begin{aligned}
&(-\lambda)^n
\sum_{j\ge0}\binom{du}{j}(-\kappa)^{nj}\\
&\qquad\cdot
\int_{\substack{x_2\ {\rm unit}\\V+17x_2\in p^m}}
 \omega_p(x_2)^\ell\langle x_2\rangle^{du}
 Y^j x_2^{-j}\,d\rho .
\end{aligned}
\tag{29}
$$
(26) 的对应式只把 $(x_2,Y,(-\kappa)^n,-\lambda)$
换成 $(x_3,Z,\kappa^m,\lambda)$。
所有 $j$ 都必须保留：移动中心已经耦合变量，
不能从原三个独立 type0 来源擅自删去 $j\not\equiv0\bmod6$。

principal 中央导数准确为
$$
\begin{aligned}
(-\lambda)^n d\bigg\{&
 \int_{\mathcal E_L}\log_p\langle x_2\rangle\,d\rho\\
&+\sum_{j\ge1}\frac{(-1)^{j+1}(-\kappa)^{nj}}j
 \int_{\mathcal E_L}Y^jx_2^{-j}\,d\rho\bigg\},
\end{aligned}
\tag{30}
$$
$\mathcal E_L$ 是 (25) 中的完整管。
第 $j$ 项赋值至少 $nj-v_p(j)$；故全部尾收敛。
$j=0$ 的实际斜率和整个碰撞域没有消失。
本节也说明 (27) 是两个完整中央观察的关系，而非仅质量等式。

## 7. 两条真实中央零给原补域的定量条件

这里回到一个直接由 (3) 得到、没有未知参考斜率的观察。
令
$$
f=\nu_S,\qquad h=\nu_L,\qquad t=f*h=\nu_T.
$$
它们的全部原 core 是 $-\lambda,\lambda,-\lambda$，
且 $f(\mathbf Z_p)=0,h(\mathbf Z_p)=1$。
对 $N\ge1$ 定义同一个原双输入补域
$$
\mathcal B_N=\{x,y\notin p^N\mathbf Z_p,\ x+y\ {\rm unit}\},
$$
以及其 Mellin $B_{N,\ell}(u)$。设
$$
\begin{aligned}
A_{N,\ell}(u)&=\iint_{x\ {\rm unit}}
 \omega_p(x)^\ell\langle x\rangle^{du}
 (1+\kappa^Ny/x)^{du}\,df(x)\,dh(y),\\
D_{N,\ell}(u)&=\iint_{y\ {\rm unit}}
 \omega_p(y)^\ell\langle y\rangle^{du}
 (1+\kappa^Nx/y)^{du}\,df(x)\,dh(y).
\end{aligned}
$$
这是两条真正的输出单位域；其中深输入的缩放还未被删去。
分割全部 $x+y$ unit 域，得到
$$
\boxed{
J_{T,\ell}(u)
=B_{N,\ell}(u)+\lambda^N A_{N,\ell}(u)
                    +(-\lambda)^N D_{N,\ell}(u).
}
\tag{31}
$$
两深输入不可能给单位输出，故没有遗漏第四项。

置 $\mu_r(G)=\int x^r\,d\nu_G$、
$I_{-r}(G)=\int_{\mathbf Z_p^\times}x^{-r}\,d\nu_G$。
本节两个输入独立且 type0，因而只有 $r\equiv0\bmod6$ 留下；
这与 (29) 的耦合管情形不同。准确有
$$
\begin{aligned}
A'_{N,0}(0)&=J'_{S,0}(0)
-d\sum_{r\ge1}\frac{\kappa^{6Nr}}{6r}
        \mu_{6r}(L)I_{-6r}(S),\\
D'_{N,0}(0)&=
-d\sum_{r\ge1}\frac{\kappa^{6Nr}}{6r}
        \mu_{6r}(S)I_{-6r}(L).
\end{aligned}
\tag{32}
$$
第二行没有 $J'_L$，因为 $S$ 的原总质量为零；
第一行的常项恰是原 $J'_S$，没有代换未知斜率。

若两条真正的中央条件 (6) 同时成立，则
$$
\boxed{
B'_{N,0}(0)=d\lambda^N
\sum_{r\ge1}\frac{\kappa^{6Nr}}{6r}
\left\{\mu_{6r}(L)I_{-6r}(S)
      +(-1)^N\mu_{6r}(S)I_{-6r}(L)\right\}
\quad(N\ge1).
}
\tag{33}
$$
所以所有这些**原补域**同时满足
$$
\boxed{v_p(B'_{N,0}(0))\ge6N.}
\tag{34}
$$
这里 $6Nr-v_p(6r)\ge6N$，全部正负矩整且测度有界。
第一项完全明确：
$$
\mu_6(S)=720\Omega^6,\qquad
\mu_6(L)=-53664\,b\,\Omega^6,
$$
$$
B'_{N,0}(0)
=d\lambda^N\kappa^{6N}\Omega^6
\left\{-8944b\,I_{-6}(S)+120(-1)^NI_{-6}(L)\right\}
+\text{赋值至少 }12N\text{ 的尾}.
\tag{35}
$$
$p>19$ 时从 $r\ge2$ 得到所列尾界。
这是真正由两固定曲线的同时失败导出的原有限域条件，
没有把 $I_{-6}$ 预设为单位。

在 (16) 的 $\rho_{D,L}$ 中，(33) 的双输入就是
$(x,y)=(Y,x_2)$。所以 $\mathcal B_N$ 是
$$
\{Y,x_2\notin p^N,\ W\ {\rm unit}\},
$$
可与 (25)–(28) 的 $Z$ 碰撞域在同一原变量上继续相交。
(33) 没有把该补域或其任意子域直接赋成中央零。

## 8. 交叉卷积的质量及另一个未知零质量来源

为保全四源，记 $g=\nu_{HC}$、$k=\nu_K$。
(3) 给 $f*h=g*k$；相应二维有界测度
$$
\mathcal W=f\otimes h-g\otimes k
$$
在总和变量上的推前恒为零，原点质量也为零。

所有输入均深的推前仍为零，因为两项具有相同 core 乘积
$-\lambda^2$。因此两个输入都为单位、总和深于任意 $p^N$ 的
**整个碰撞推前**也准确为零。这是同一实际交叉来源的完整式，
不是逐个相位或单个球的零。

在单位总和域中，混合两深输入的原边界必须保。
其第一单位输入展开的常项是 $J'_S$；
另一方向的常项则是 $-J'_K$。
$K$ 虽然在 (13) 下每个原点深球质量均为零，
仍没有被证明是另一条 rank-two Hecke 来源，故不能由 (6) 删除
$J'_K$。本篇第7节使用 $f*h$ 的原补域，正是为了给出
不含该新增未知斜率的真实后果；这不声称所有交叉余项已被消去。

## 9. 同一 degree72 的实际有限像

原两次交叉乘积可形成三个真实输出
$$
Q=(DK)C,\qquad T=(DL)C,\qquad P=(HL)C.
$$
$Q$ 从 $z^{12}$ 起，$T$ 从 $z^6$ 起，$P(0)=1$。
不能直接把它们当成 $\operatorname{Sym}^2J$ 的闭合块。

本篇另给完整有限付款。在 $b=1$ 的原基
$\sigma^{72}X^j$、$0\le j\le12$ 上，用 R398 的真实七纤维
求整个矩阵
$$
N_7=\mathscr M_{\gamma_7}/(\omega\gamma_7).
$$
十三个不同目标横坐标确定每列，完整保留
$(r_{\bar\gamma_7}/r_{\gamma_7})^{72}$。
实际
$$
(\gamma_7/\bar\gamma_7)^9\equiv91+72\omega\pmod{144},
\qquad
(\gamma_7/\bar\gamma_7)^{18}\equiv73=1+72\pmod{144}.
$$
因此 $\mathcal K=N_7^9$ 正是本 ray 在 type0 $\mathcal S_{72}$
上的归一算子；同 degree $\Theta(6z)$ 锚定全部中心。
精确矩阵给
$$
\boxed{\mathcal K^2=1,\qquad
       \mathcal KQ=Q,\qquad\mathcal KT=-T,\qquad
       (\mathcal KP)(0)=5/21.}
\tag{36}
$$
而 $\mathcal KP\notin\langle Q,T,P\rangle$：
$Q,T,P$ 的 $X^0$ 系数均零，$\mathcal KP$ 的该系数准确为
$-16777216/21$。
全部像保存在证书内，未把这条真实余列删掉。
特别 $Q$ 在这个固定 ray 上有完整 $+\lambda$ core；
它依旧不是可自由加入 (6) 的新中央零。

## 10. 已付接口与剩余的同一观察

本篇给出同两条固定 rank-two 曲线实际相连的四条全纯来源，
共同 period、原全部相位、整个 degree38/54 core，
以及未平均 degree34 的带反射 core。
由这些真实算子得到 (25)–(30) 的移动单位管交叠与全中央运输。
同时失败必须满足 (33)–(35) 的全部原补域深度条件。

后继需要比较的现已是同一 $\rho_{D,L}$ 中
$\{Y,x_2\notin p^N,W\ {\rm unit}\}$ 与
$Y,Z$ 深碰撞的完整补域，而不是任意新来源的导数。
目前没有把 (27) 的两个移动管当作 R339 的独立叶网格，
也没有把 (34) 的深整性改称导数非零。

### 证书与依赖

- [check-jzero-two-ranktwo-cross-source-and-overlap.js](../scripts/check-jzero-two-ranktwo-cross-source-and-overlap.js)：
固定 CRT、原多项式、真实 Gram/核心坐标以及整个 CM7 13维矩阵；
三十七项精确检查全部通过；所有运算是有理数和 $\mathbf Q(\omega)$ 的 BigInt 精确运算，无目标素数扫描。
- [R396](R396-original-nontrivial-quartic-ray-three-cores-and-complete-scale-boundary.md)：
含中心的偶 degree Heisenberg、原 $D,H$ 双谱及第一固定 ray。
- [R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)：
实际 $E_{24}$ 来源、全部多项式与共同正式群周期。
- [R400](R400-full-square-interpolation-determines-core-and-e24-cmseven-phase.md)：
原全部 Katz 分支决定新完整 core。
- [R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
  [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：
原整 Heisenberg 格、普通周期和 Theta 单位尺度。

终端不可用，本次依仓库授权以 GitHub 接口提交小文本，不称为 git pull。
2026-11-14 02:47:06 UTC 读取 main
e4177299da5800620b81f1820d084e643620a839；
与已读的 437dac06445a57c037862ced24d597be447e8ac6 比较，
根 README 与本课题 README 无变；此前 02:38 的两个 blob SHA
也已独立核对一致。
读号交根代理记入 HANDOFF。
