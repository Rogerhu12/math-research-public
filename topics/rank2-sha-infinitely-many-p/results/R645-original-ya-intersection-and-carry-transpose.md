# R645 — 原 Y/A 真交域、同一 q 的完整转置与强制四阶补偿

日期：2026-11-15。**状态：已证明。**

R638 的原 $Y$ 一层与原 $A$ 两层具有同一个三态源矩阵。
本篇在这两个真实域的交集上比较它们，不取消不同支持上的矩阵。
原 $\mu_0$ 的交域有已定标的完整 $A/Q_5$ 返回；两个正确归一
观察和两个不同的 $q$ 转置均可显式写出。

对原 $Y$ 中央，共同部分中两个 carry 门的交集强迫归一后的
$A$ 非单位，因而与 $A$ 词的实际单位观察严格不交。
这给同一个原来源、同一个 $q$ 的真实支域分解。
此外，R594 的全部十一维自由补偿不能使 $q$ 在 $A$ 方向不变：
它的第四法向 jet 被原条件 $L_4=1$ 强制为模 $p$ 单位。
最后给出两条原算术总行、全部外部补偿及稳定门上的首阶公式。
这里没有把一个强制多项式 jet 当成其受限积分非零。

## 1. 原来源、旧三态与同一测试

沿用 R594、R634、R638 的同一普通 ray、所有固定坏集和规范：
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times .
\tag{1}
$$
仍取 $p\ge71$。原六个独立物理输入按
$(\xi_1,\xi_2,\xi_3,x,c,d)$ 排列，且
$$
\rho_0=-\nu_\sigma^{\otimes6}/84,\qquad
\mu_0=\mathcal P_{6,C}\rho_0,\qquad
\mu_W=K_W\mu_0,\qquad
h_W=-\tfrac12\mathsf H_{2,W}\mu_0 .
\tag{2}
$$
$h_W$ 专指 R638 的二挠来源，不是其他结果中的
$\eta+\rho_0/2$。

原观测与两个低 degree 轴是
$$
\begin{aligned}
A&=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\\
Q_5&=c+2d,\qquad L_5=2c-d,\\
Y&=A+Q_5,\qquad W=A+3\delta c+4d .
\end{aligned}
\tag{3}
$$
$A,Q_5,L_5$ 相互正交，范数为 $29,5,5$。
原其余三个 $A$ 伴随全部保留。设
$$
P_{L,t}=I+(t-1)\bar L^{\,t}L/N(L)
\tag{4}
$$
为只把物理 $L$ 乘 $t$、固定其正交伙伴的真实线性映射。

在 $(\mu_0,\mu_W,h_W)$ 上，R638 已付
$$
\mathsf D=\begin{pmatrix}1&0&0\\0&-1&0\\0&1&1\end{pmatrix},
\qquad
\begin{aligned}
\mu|_{Y\in p}&=\lambda(P_{Y,-\kappa})_*\mathsf D\mu,\\
\mu|_{A\in p^2}&=\lambda^2(P_{A,\kappa^2})_*\mathsf D\mu .
\end{aligned}
\tag{5}
$$
第二式来自 R488 的完整 odd29/quarter 规范；$C\perp A$，
故整个 $C$ 平均与之交换。特别 $\mathsf D\mu_0=\mu_0$。

固定一个 carry 深度 $N\ge1$，本篇始终使用 R594 的同一个
正分支测试
$$
\boxed{
q=
\frac{\mathbf1_{\{C,F\ {\rm unit},\ F-C\in p^N\}}}{b\Omega^6}
\widehat P_p\bigl((F-C)/\kappa^N,F+13C,G\bigr).
}
\tag{6}
$$
这里 $\widehat P_p=\widehat{\widetilde P}_p$ 包括全部实际
$u_j=(1+\lambda\kappa^j)^{-1}$ 和完整九行整右逆，绝不改成模 $p$
近似。在 (6) 的深条件下，原 $E=F+13C$ 单位条件与显示的
$C,F$ 单位条件等价。单支与六支的整体关系沿用 R590/R594；
本篇没有再除或乘六。

R638 的完整 $\pi_4=(Y,W,W',G)$ 中性为
$$
(\pi_4)_*(q\mu)=\beta^N(\pi_4)_*\mu,\qquad
\mu=\mu_0,\mu_W,h_W .
\tag{7}
$$
$Y_*\mu_0=\nu_S$、$W_*\mu_0=6\delta\nu_T$。
(7) 不能在任意隐藏子域上逐项使用。

## 2. 同一原来源的完整交域返回

现 ray 已有 $g_\pi=\pi_0/\bar\pi_0\equiv1\bmod10$。
整个标准 odd $\mathcal S_5$ 的核心为
$\chi_5 I$，其中
$$
\chi_5=\chi_{65}\in\{1,-1\}.
\tag{8}
$$
这是 R370 的奇中心规范及 R513 的非零
$[\gamma_{13}]^*\mathcal S_5\subset\mathcal S_{65}$ 绝对比较，
不是按需要选择符号。

这里直接核原 joint：在 $Q_5,L_5$ 的对偶变量上，
两个原 sigma 是
$$
\sigma(q+2l)\sigma(2q-l).
\tag{9}
$$
两轴交叉 Gaussian 为零，各恰有一个 odd 系数，故 (9) 在
完整标准 odd $\mathcal S_5\boxtimes\mathcal S_5$。
坐标行列式为 $-5$，普通处为单位。$C$ 平均只作用前四个原
输入，所以保持 (9) 的全部两个轴及所有伴随。因此
$$
\mu_0|_{Q_5\in p^m}
=(\chi_5\lambda)^m(P_{Q_5,\kappa^m})_*\mu_0.
\tag{10}
$$
不在这里把 (10) 免费扩展到 $\mu_W,h_W$。

定义两个实际域及其交集
$$
\mathcal Y_n=\{Y\in p^n\},\quad
\mathcal A_n=\{A\in p^{2n}\},\quad
\Gamma_n=\mathcal Y_n\cap\mathcal A_n,\qquad n\ge1.
$$
由 $Y=A+Q_5$，准确有
$$
\boxed{\Gamma_n=\{A\in p^{2n},\ Q_5\in p^n\}.}
\tag{11}
$$
$A,Q_5$ 正交，(5)、(10) 的完整限制交换。置
$$
t=\kappa^n,\quad s=(-1)^n,\quad
B_n=P_{A,t^2}P_{Q_5,t},\quad
g_n=\chi_5^n\lambda^{3n}.
$$
则
$$
\boxed{\mu_0|_{\Gamma_n}=g_n(B_n)_*\mu_0.}
\tag{12}
$$
原 $L_5$ 及三个 $A$ 伴随全部固定且不限。
$A$ 深不是四个原 sigma 各深，(12) 也没有作这种替换。

## 3. 原 A 操作确实改变 q 和四输出

为避免只看总 degree，列出全部原三行：
$$
\begin{aligned}
C&=(\xi_1-\xi_3+x)/\delta,\\
D&=\xi_1+\omega^2\xi_2-2\omega\xi_3+c+(2+3\omega)d,\\
F&=D+C,\qquad E=F+13C,\\
H_1&=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x,\qquad
G=13H_1+(3-2\omega)F .
\end{aligned}
\tag{13}
$$
这些 $C,F,G$ 都与 $Y,W,W'$ 正交；但 $F,G$ 不与 $A$ 正交。

记
$$
a=-\frac{5+6\omega}{29},\quad
b_Q=\frac{11+6\omega}{5},\quad b_L=\frac{2+12\omega}{5},
\quad b_Y=\frac{20+3\omega}{17},\quad g=3-2\omega,
\quad b_F=\frac{5+6\omega}{5}.
\tag{14}
$$
完整 $A$ 变化为
$$
\boxed{
\begin{array}{c|c}
\text{输出}&\text{与原值之差，作用 }P_{A,z}\\ \hline
Y,\ W&(z-1)A\\
W'&(z-1)(28+4\omega)A/29\\
C&0\\
F&(z-1)aA\\
G&(z-1)gaA .
\end{array}}
\tag{15}
$$
其中 $N(a)=31/29^2$；$31$ 已由 $p\equiv7\bmod64$ 排除。
特别 (15) 的显示系数是当前单位。

整个 $(C,F,Y,W,W',G)$ 是单位框架，行列式为
$3744-14976\omega$。在它里面
$$
\begin{aligned}
A={}&\frac{1+6\omega}{13}F
+\left(\frac{73}{72}-\frac{5\omega}{48}\right)Y
+\left(-\frac1{756}+\frac{295\omega}{3024}\right)W\\
&+\frac{-353+83\omega}{3024}W'
+\left(-\frac7{936}+\frac{5\omega}{234}\right)G .
\end{aligned}
\tag{16}
$$
$F$ 系数非零。因此原 $A$ 操作不下降为 $\pi_4$ 上的变换；
(7) 不使 $q\circ P_{A,z}$ 自动等于 $q$。

定义真正的两个正交余行
$$
F_\perp=F-aA-b_FQ_5,\qquad
G_\perp=G-gaA-gb_FQ_5 .
\tag{17}
$$
它们与 $A,Q_5$ 均正交，完整原行在证书中给出。
$C$ 也与二者正交，而 $G-gF=13H_1$ 在 $A$ 变化下固定。

## 4. 两个正确归一总行及所有真实外部部分

对 $Z=Y,W$，记
$$
J_Z(u)=\int_{Z\ {\rm unit}}\langle Z\rangle^{d_pu}\,d\mu_0,
\qquad J_Y=J_S,\quad J_W=6\delta J_T .
$$
定义两个真正的完整行
$$
\begin{aligned}
\mathcal F_{Y,n}^{Z}(u)
&=\int_{\mathcal Y_n}q\,
 \mathbf1_{ZP_{Y,st}^{-1}\ {\rm unit}}
 \langle ZP_{Y,st}^{-1}\rangle^{d_pu}\,d\mu_0,\\
\mathcal F_{A,n}^{Z}(u)
&=\int_{\mathcal A_n}(q\circ P_{A,t^2}^{-1})\,
 \mathbf1_{ZP_{A,t^2}^{-1}\ {\rm unit}}
 \langle ZP_{A,t^2}^{-1}\rangle^{d_pu}\,d\mu_0 .
\end{aligned}
\tag{18}
$$
逆像只在各自的真实整像上使用。第一行的 $q$ 不变是因为
$C,F,G\perp Y$；第二行必须保留显示的转置。

用 (5)、(7) 得整个 Mellin 身份
$$
\boxed{
\mathcal F_{Y,n}^{Z}(u)=\lambda^n\beta^N J_Z(u),\qquad
\mathcal F_{A,n}^{Z}(u)=\lambda^{2n}\beta^N J_Z(u).
}
\tag{19}
$$
因此 $\lambda^n\mathcal F_{Y,n}^{Z}=\mathcal F_{A,n}^{Z}$；
这里是原同一个 $S$ 或 $T$，没有识别新的算术来源。

分别令 $\mathcal I_{Y,n}^{Z},\mathcal I_{A,n}^{Z}$ 为 (18)
限制到 $\Gamma_n$ 的积分，$\mathcal O_{Y,n}^{Z},
\mathcal O_{A,n}^{Z}$ 为各自剩余整域上的积分。准确有
$$
\boxed{
\lambda^n\mathcal O_{Y,n}^{Z}-\mathcal O_{A,n}^{Z}
=\mathcal I_{A,n}^{Z}-\lambda^n\mathcal I_{Y,n}^{Z}.}
\tag{20}
$$
外部域分别是 $\mathcal Y_n\setminus\mathcal A_n$、
$\mathcal A_n\setminus\mathcal Y_n$，仍保 (18) 的不同测试。

现在才用 (12)。设
$$
q_Y=q\circ B_n,\qquad q_A=q\circ P_{Q_5,t}.
$$
共同归一后的观察完整为
$$
\boxed{
\begin{aligned}
z_Y^Y&=s(tA+Q_5),&
z_A^Y&=A+tQ_5,\\
z_Y^W&=t^2A+b_QtQ_5+b_LL_5+
       b_Y(s-t)(tA+Q_5),&
z_A^W&=A+b_QtQ_5+b_LL_5 .
\end{aligned}}
\tag{21}
$$
故
$$
\boxed{
\mathcal I_{j,n}^{Z}(u)
=g_n\int q_j\mathbf1_{z_j^Z\ {\rm unit}}
                  \langle z_j^Z\rangle^{d_pu}\,d\mu_0,
\qquad j=Y,A .}
\tag{22}
$$
原 $Y$ 两 cut 是 $Q_5$ 单位与 $A$ 单位。
原 $W$ 两 cut 保 (21)，不能改成相同一个单位条件。

各完整总行在 $u=0$ 的质量为零，但 (22) 的两条质量不必为零。
因此
$\mathcal O_{j,n}^{Z}(0)=-\mathcal I_{j,n}^{Z}(0)$。
若原 $J'_S=J'_T=0$，则准确有
$$
\boxed{(\mathcal O_{j,n}^{Z})'(0)
=-(\mathcal I_{j,n}^{Z})'(0),\quad j=Y,A,\quad Z=Y,W.}
\tag{23}
$$
(23) 保整个外部部分，不将共同部分或任一质量赋零。

## 5. 同一个 q 的两个门以及真实单位分离

在 (22) 的共同原整变量中置
$$
F_Y=F_\perp+a t^2A+b_FtQ_5,\qquad
F_A=F_\perp+aA+b_FtQ_5 .
$$
相应
$$
G_j=G_\perp+g(F_j-F_\perp),\quad
D_j=F_j-C,\quad E_j=F_j+13C,\quad
\mathcal G_j=\{C,F_j\ {\rm unit},D_j\in p^N\}.
$$
于是
$$
\boxed{
q_j=\frac{\mathbf1_{\mathcal G_j}}{b\Omega^6}
          \widehat P_p(D_j/\kappa^N,E_j,G_j),\qquad
F_A-F_Y=(1-t^2)aA .}
\tag{24}
$$
(24) 是整个真实权，包含门与多项式，不只是 Taylor 首项。

因为 $(1-t^2)a$ 是单位，
$$
\boxed{
\mathcal G_Y\cap\mathcal G_A
=\mathcal G_Y\cap\{A\in p^N\}
=\mathcal G_A\cap\{A\in p^N\}.}
\tag{25}
$$
证明是将两个深条件相减；反方向代回即得。
$C$ 单位与其中一个深条件保证另一个 $F_j$ 也为单位。
没有新增或删除一个 $L_5$ 条件。

特别原 $Y$ 的 $A$ 词观察要求 $A$ 单位，所以
$$
\boxed{\mathcal G_A\cap\{z_A^Y\ {\rm unit}\}
       \ \subset\ \mathcal G_A\setminus\mathcal G_Y.}
\tag{26}
$$
这是同一来源的逐点分离：$A$ 词在共同几何域上的整个归一
$Y$ 中央行，实际上落在另一 carry 门的失败支。
并不是这条行等于零。

一般 $Z=Y,W$ 的 (22) 完整分成三个不交门
$$
\mathcal G_Y\cap\mathcal G_A,\quad
\mathcal G_Y\setminus\mathcal G_A,\quad
\mathcal G_A\setminus\mathcal G_Y .
\tag{27}
$$
在第一门上设 $v=(1-t^2)aA$，则整个多项式差准确是
$$
\boxed{
\begin{aligned}
&\widehat P_p((D_Y+v)/\kappa^N,E_Y+v,G_Y+gv)
-\widehat P_p(D_Y/\kappa^N,E_Y,G_Y)\\
&=\sum_{r=1}^{6}\frac{v^r}{r!}
  (\kappa^{-N}\partial_D+\partial_E+g\partial_G)^r
  \widehat P_p(D_Y/\kappa^N,E_Y,G_Y).
\end{aligned}}
\tag{28}
$$
因 $v\in p^N$，全部显示项整。即使在这一共同门上，
两个 Mellin 观察仍是 (21)，还须保测试本身的差。
另两个门在 (27) 中完整留下，不能由 (28) 代掉。

## 6. 原自由 q 系数不能消去 A 转置

R594 的实际完整九行右逆给
$$
\boxed{
L_4=\sum_{j+\ell=2}a_{4j\ell}
       (1+\lambda\kappa^j)^{-1}e_x^j g_x^\ell=1,\quad
e_x=(-14-28\omega)/3,\quad g_x=(32+31\omega)/3.}
\tag{29}
$$
注意这里 $g_x$ 与 (14) 的 $g=3-2\omega$ 不同。
$\widehat P_p$ 的所有系数整，(29) 对实际 $\lambda,\kappa$
严格成立，而非只对模 $p$ 矩阵成立。

设
$$
\mathcal V_N=\partial_D+\kappa^N\partial_E
                              +g\kappa^N\partial_G .
$$
由 (29) 及 $N\ge1$，
$$
\boxed{
\frac1{4!}
(\mathcal V_N^4\widehat P_p)(0,e_x x,g_x x)
\equiv x^2\pmod p.}
\tag{30}
$$
因为模 $p$ 的 $\mathcal V_N$ 就是 $\partial_D$，
且完整第四导数在 $D=0$ 恰读 (29)。
当前 $4!$ 为单位。

若同一个多项式在某个 $P_{A,z}$、$z$ 非单位根的缩放下不变，
沿真实 $A$ 变量展开，各个正次数的系数乘 $z^j-1\ne0$，
于是它必须与 $A$ 无关。由 (15)，这迫
$\mathcal V_N\widehat P_p=0$，与 (30) 矛盾。
所以 R594 的十一维自由核中，没有仍满足 (29) 而删除该
$A$ 转置的选择。特别不能靠“二十列多于九行”认定可解这一
额外要求。

(30) 是真实多项式的单位 jet；它没有给带 (21)、(25)、(27)
及 log 权的积分赋非零值，也没有替代原算术零的传播。

## 7. 固定门上的实际首阶及完整 log 质量

现在令 $n\ge N$。两个门在 $t=\kappa^n$ 下准确稳定为
$$
\mathcal G_0=\{C\ {\rm unit},F_\perp-C\in p^N\},\qquad
\mathcal G_1=\{C\ {\rm unit},F_\perp+aA-C\in p^N\}.
\tag{31}
$$
其交集仍为 $\mathcal G_0\cap\{A\in p^N\}$。
定义三元组
$$
X_0=((F_\perp-C)/\kappa^N,F_\perp+13C,G_\perp),
\quad
X_1=X_0+(aA/\kappa^N,aA,gaA),
$$
以及
$$
p_i=\frac{\widehat P_p(X_i)}{b\Omega^6},\qquad
p_i^{[1]}=\frac{b_FQ_5}{b\Omega^6}
 (\kappa^{-N}\partial_D+\partial_E+g\partial_G)
                   \widehat P_p(X_i),\quad i=0,1.
\tag{32}
$$
$p_i$ 只在其相应 $\mathcal G_i$ 上使用，因此整有界；
$p_i^{[1]}\in p^{-N}\mathcal O$。
共同来源、原全部四个伙伴均保在这些函数中。

对原 $Y$ 行，根单位 $s$ 的 principal 对数为零。
设
$$
\begin{aligned}
K_{Y,0}&=\int_{\mathcal G_0,\ Q_5\ {\rm unit}}
                      p_0\log\langle Q_5\rangle\,d\mu_0,\\
K_{A,0}&=\int_{\mathcal G_1,\ A\ {\rm unit}}
                      p_1\log\langle A\rangle\,d\mu_0,\\
K_{Y,1}&=\int_{\mathcal G_0,\ Q_5\ {\rm unit}}
 [p_0A/Q_5+p_0^{[1]}\log\langle Q_5\rangle]\,d\mu_0,\\
K_{A,1}&=\int_{\mathcal G_1,\ A\ {\rm unit}}
 [p_1Q_5/A+p_1^{[1]}\log\langle A\rangle]\,d\mu_0 .
\end{aligned}
\tag{33}
$$
则准确有
$$
\boxed{
\frac{(\mathcal I_{Y,n}^{Y})'(0)}{d_pg_n}
 =K_{Y,0}+\kappa^nK_{Y,1}
       +p^{\,2(n-N)+1}\mathcal O,\qquad
\frac{(\mathcal I_{A,n}^{Y})'(0)}{d_pg_n}
 =K_{A,0}+\kappa^nK_{A,1}
       +p^{\,2(n-N)+1}\mathcal O .}
\tag{34}
$$
这里 $N,p,\lambda,\kappa,q$ 固定，只有 $n$ 变化。
$K_{j,0}\in p\mathcal O$，$K_{j,1}\in p^{1-N}\mathcal O$。
式 (33) 的两个带 log 的法向项正是 $q$ 运动的真实补偿，
不能只保 $A/Q_5$ 或 $Q_5/A$。

证明是对 (24) 作有限次数六的准确展开，并分别展开
$\log\langle Q_5+tA\rangle$、$\log\langle A+tQ_5\rangle$。
$q_Y$ 还有 $a t^2A$ 变化，全部从二阶进入余项。
每个多项式法向次数最多引入一个 $\kappa^{-N}$，
而常数单位对数属于 $p\mathcal O$；所有二次及以上项遂至少在
$p^{2(n-N)+1}$。log 的更高分母只给 $v_p(k)$，
$p\ge71$ 保同一界。固定门保证整个展开在原真实域上一致收敛。

质量也完整有相应有限多项式展开；尤其 (22) 的质量首项分别是
$$
g_n\int_{\mathcal G_0,Q_5\ {\rm unit}}p_0\,d\mu_0,\qquad
g_n\int_{\mathcal G_1,A\ {\rm unit}}p_1\,d\mu_0 .
\tag{35}
$$
这些量没有零理由。若以后改用其他物理尺度归一，
其 log 乘 (35) 的项仍须添加，不能援引全局质量零删掉。

## 8. 原算术条件给出的准确未闭合向量

在原两中央同时为零的反证条件下，(23)、(34) 给
$$
\boxed{
-\frac{(\mathcal O_{j,n}^{Y})'(0)}{d_pg_n}
 =K_{j,0}+\kappa^nK_{j,1}
     +p^{\,2(n-N)+1}\mathcal O,\qquad j=Y,A .}
\tag{36}
$$
因此两个外部部分的真实归一极限分别是 $K_{Y,0},K_{A,0}$；
减去该极限后的差商分别回到 $K_{Y,1},K_{A,1}$。
这四条是 (33) 显示的同一原来源上的完整积分，不是新增一池
未知算术来源。相同的原 $T$ 总行仍由 (20)–(22) 给出，
其中必须保持 $L_5$ 和两条实际 $W$ 单位 cut。

与 R638 的 $Y/W$ 词比较，那里所有物理操作都固定 $q$，
首差商回原 $M_1$；本篇 $A$ 方向额外留下 (28)、(33)。
式 (30) 证明这些转置不能在原整九行家族中逐点抹掉；
式 (25)、(26) 则给它们准确所在的门。
目前尚未证明这些完整积分之间有足以消去外部补偿的关系。
特别没有从 $\lambda^n\mathcal F_Y=\mathcal F_A$、
源矩阵同为 $\mathsf D$、或者一个多项式 jet 为单位，
推出原 $S/T$ 全中央非零。主目标仍未完成。

## 精确证书与依赖

- [精确脚本](../scripts/check-r645-original-ya-intersection-and-carry-transpose.js)
- [完整证书](../scripts/check-r645-original-ya-intersection-and-carry-transpose.json)
- [R638：原三态整核、全词及原中央补偿](R638-original-yw-three-state-and-word-compensation.md)
- [R488：原 odd29 与真实三态 A 两层返回](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)
- [R370：标准 odd5 的完整中心和绝对平方](R370-original-degree-five-core-and-common-infinite-six-phase-primes.md)
- [R513：odd5 与 odd65 的同一绝对符号](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)
- [R594：同一 q 的实际九行右逆、全部 lambda/kappa](R594-two-source-six-carry-compensation.md)

脚本使用自含 BigInt $\mathbf Q(\omega)$ 算术，精确核全部原行、
完整 Gram、(15)–(17)、六维框架双侧逆、(21) 的两种符号、
两门之差和所有固定系数；没有以有限素数采样替代证明。
整奇 theta 归属、实际核心、无限深度、carry 支撑及对数估值
由正文逐项证明。