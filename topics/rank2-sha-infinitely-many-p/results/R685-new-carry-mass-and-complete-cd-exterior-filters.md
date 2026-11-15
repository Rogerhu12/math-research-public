# R685 — 同一十二次 carry 的完整角域质量、cd 外部消去与原 T 过滤转置

日期：2026-11-15。**状态：已证明。**

本篇使用 R679 已构造的同一个 $q_N^\sharp$。原两份冻结来源和未切另一条 Y 的 cd 端点都准确等于 S。本文把它代入 R678/R682 的有限原角域，保新十二次项允许的非零质量，并把全部外部分成 cd 同深之内、之外两部分。

得到的两步实际过滤在整个 Mellin 函数上消掉 cd 之外的部分。剩下的 cd 内部补偿与角域准确相反；其 T 中央有严格非零赋值，而 S 中央更深。这个过滤同时消掉原中央的系数，所以它不是新的中央零传播。最后支付与 R671/R679 的原十三步 T 过滤比较时真正的 $\kappa^{3M}$ 共轭及三个未被杀掉的高模式。

## 1. 固定实际测试和全部规范

沿用 R679 的原 ray、固定坏集及相对密度一子族：
$$
b=17,\quad \lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times,\quad
N\in4\mathbf Z_{>0}.
\tag{1}
$$
固定 N、p 后，$q_N^\sharp$ 不随下面的 r、m、M 或观察深度变化。
其真实生成权是
$$
\mathcal P^\sharp(D,E,G)=
 \frac{\widehat P_6(D,E,G)}{b\Omega^6}
 +\frac{\widehat P_{12}(D,E,G)}{b^2\Omega^{12}},
\tag{2}
$$
两项分别齐次六次、十二次，全部实际整系数取 R679(18) 的十九阶逆。
第二旋转支始终取 $q_1^\sharp=q_0^\sharp\circ J^{-1}$，
$J(c,d)=(d,-c)$；包括 $G_1=G\circ J^{-1}$，不另选测试。

R679 已付
$$
(\pi_4)_*(q_N^\sharp\mu_0)=\beta^N(\pi_4)_*\mu_0,\qquad
\mathscr U_0=\mathscr U_1=\mathscr B_{\rm cd}=S,
$$
$$
K_2:=\int_{\mathcal G_*}
 \frac{\partial_{v_N}^2\mathcal P^\sharp(X_*)}{2}\,d\nu_4
=\frac{\lambda^N\kappa^{-2N}}{2b\Omega^2}.
\tag{3}
$$
这里
$$
\begin{gathered}
\mu_0=\nu_4\otimes\nu_{\rm pair}(Q,L),\qquad
Q=c+2d,\quad L=2c-d,\quad Y_0=A+Q,\quad Y_1=A+L,\\
W_0=A+b_QQ+b_LL,\qquad W_1=A-b_LQ+b_QL,\\
a=-\frac{5+6\omega}{29},\quad b_F=\frac{5+6\omega}{5},
\quad\ell_0=-\frac{3\omega}{5},\quad g=3-2\omega,\\
b_Q=\frac{11+6\omega}{5},\quad b_L=\frac{2+12\omega}{5},
\quad b_Y=\frac{20+3\omega}{17},\\
\mathcal G_*=\{C\ {\rm unit},D_*\in p^N\},\quad
X_*=(D_*/\kappa^N,D_*+14C,13H_1+g(D_*+C)),\\
v_N=(\kappa^{-N},1,g).
\end{gathered}
\tag{4}
$$
所有旧伴随坐标仍属同一完整来源。后文
$\dot F=d_p^{-1}\partial_wF(0)$；每条 T 行均保自己的真实单位 cut。

## 2. 同八个原角域及两套完整观察

取 r 偶，$M\ge2$，先要求 $r>N+M+3$。定义
$$
k_m=r+m,\quad n_j=r+M+j,\quad
x=\kappa^r,\quad z_m=\kappa^m,\quad t_j=\kappa^{M+j},
$$
$$
\mathcal D_{r,m,j}
=\{A\in p^{2r},\
Q\in p^{k_m}\mathbf Z_p^\times,\
L\in p^{n_j}\mathbf Z_p^\times\},
\quad m=0,1,\quad0\le j\le3 .
\tag{5}
$$
这些是原来源上的八个互不相交的域。它们准确具有
$Y_0$ 环带 $k_m$、$Y_1$ 环带 $n_j$，且 $c,d$ 同属环带 $k_m$。
特别每个域都包含于 $\mathsf{CD}_N=\{c,d\in p^N\}$。

实际返回为
$$
A_{\rm old}=x^2A,\qquad Q_{\rm old}=xz_mQ,\qquad
L_{\rm old}=xt_jL,\qquad
\text{来源标量 } \lambda^{2r}\beta^{k_m+n_j}.
\tag{6}
$$
返回域保 $\mathcal G_*$ 以及 Q、L 双单位。两套权准确是
$$
q_i^\sharp\circ B_{r,m,j}
=1_{\mathcal G_*}\mathcal P^\sharp(X_*+s_i v_N),
$$
$$
s_0=ax^2A+b_Fxz_mQ+\ell_0xt_jL,\qquad
s_1=ax^2A-\ell_0xz_mQ+b_Fxt_jL.
\tag{7}
$$
令 $\epsilon_m=(-1)^m,\epsilon_j=(-1)^{M+j}$。完整归一观察为
$$
\begin{aligned}
S_0&=\epsilon_m(Q+xz_m^{-1}A),\\
T_0&=b_YS_0+(b_Q-b_Y)xz_mQ+(1-b_Y)x^2A+b_Lxt_jL,\\
S_1&=\epsilon_j(L+xt_j^{-1}A),\\
T_1&=b_YS_1-b_Lxz_mQ+(1-b_Y)x^2A+(b_Q-b_Y)xt_jL.
\end{aligned}
\tag{8}
$$
第一套两个单位 cut 均为 Q 单位；第二套均为 L 单位。
$xt_j^{-1}A=x^2A/(\kappa^{n_j})$ 仍在 (8)，没有冻结。

记 $\mathcal K^{i,Z}_{r,m,j}(w)$ 为 (5) 上原 $q_i^\sharp$
和原 $Z_iP_{Y_i,(-\kappa)^{d_i}}^{-1}$ 的完整单位 Mellin 积分，
其中 $Z=S,T$ 分别取 $Y_i,W_i$，$d_0=k_m,d_1=n_j$。
它们的返回恰为 (6)–(8)。

置
$$
D_\kappa=(1-\kappa)(1-\kappa^2)(1-\kappa^3),\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\frac{(\kappa^3,-\kappa-\kappa^2-\kappa^3,1+\kappa+\kappa^2,-1)}
 {D_\kappa},
$$
$$
A_\kappa(z)=\sum_{j=0}^3\alpha_jz^j
=-\frac{(z-1)(z-\kappa)(z-\kappa^2)}{D_\kappa}.
\tag{9}
$$
定义同一个实际有界差商
$$
\mathcal B^{i,Z}_{r,M}
=\sum_{j=0}^3\alpha_j\lambda^{-2r}
 \left(\beta^{-r-n_j}\mathcal K^{i,Z}_{r,0,j}
      -\beta^{-r-1-n_j}\mathcal K^{i,Z}_{r,1,j}\right).
\tag{10}
$$
再令
$$
\sigma_M=(-1)^{M+1}\frac{1+\kappa^2}{(1-\kappa)^2},\qquad
\mathcal D^Z_{r,M}=\kappa^{3M+3}\mathcal B^{1,Z}_{r,M}
                         -\sigma_M\mathcal B^{0,Z}_{r,M},
$$
$$
\mathfrak D_{r,M}
=\left.\frac1{d_p}\partial_w
 \left(\mathcal D^T_{r,M}(w)
       -\langle b_Y\rangle^{d_pw}\mathcal D^S_{r,M}(w)\right)\right|_{w=0}.
\tag{11}
$$
(11) 含完整质量乘 $\log\langle b_Y\rangle$，不是只写
$\dot{\mathcal D}^T-\dot{\mathcal D}^S$。

## 3. 新十二次项的完整质量

定义同一个真实条件系数
$$
K_8(x)=\int_{\mathcal G_*}
 \frac{\partial_{v_N}^8\mathcal P^\sharp
       (X_*+ax^2Av_N)}{8!}\,d\nu_4.
\tag{12}
$$
它是 $x^2$ 的 degree 至多四多项式，对固定 r、N 不依 m、j、M。
六次块对 (12) 为零。因为 (12) 的底点在 $\mathcal G_*$ 上整，
$r>N$ 时
$$
v_p(K_8(x))\ge-8N.
\tag{13}
$$

原两单位 pair 角型只允许正总次数 $2\bmod6$。
在 (2) 内只有总次数二、八。总次数二被 (9) 的三个根完全杀掉；
总次数八经 m 差、j 差以后只保 L 次数 $3,5,6,7$。
令 $E_a=1-\beta\kappa^a$。同一个完整 S5 分离给
$$
\begin{aligned}
M_{5,3}=M_{3,5}&=4320b\Omega^8E_5E_3,\\
M_{2,6}&=480b\Omega^8E_2E_6,\\
M_{1,7}&=-3960b\Omega^8E_1E_7,
\end{aligned}
\qquad
M_{a,b}=\int_{Q,L\ {\rm unit}}Q^aL^b\,d\nu_{\rm pair}.
\tag{14}
$$
例如原低展开准确为
$$
\begin{gathered}
-xy\sigma^5=1+\tfrac b6z^6+\cdots,\quad
x^2\sigma^5=z-\tfrac{11b}{42}z^7+\cdots,\quad
x\sigma^5=z^3+\cdots,\quad \sigma^5=z^5+\cdots,\\
\sigma(z)\sigma(2z)=2z^2+\tfrac{13b}{21}z^8+\cdots .
\end{gathered}
$$
各正矩乘自己的 $E_a$，没有用全矩替代单位矩。

取 $(q_0,l_0)=(b_F,\ell_0)$，
$(q_1,l_1)=(-\ell_0,b_F)$。则两个 Mellin 质量完整相等，且
$$
\boxed{
\begin{aligned}
\mathcal B^{i,S}_{r,M}(0)
=\mathcal B^{i,T}_{r,M}(0)
=x^8K_8(x)\sum_{\ell\in\{3,5,6,7\}}
 &\binom8\ell q_i^{8-\ell}l_i^\ell
 (1-\kappa^{8-\ell})\\
 &{}\cdot\kappa^{M\ell}A_\kappa(\kappa^\ell)
 M_{8-\ell,\ell}.
\end{aligned}}
\tag{15}
$$
证明是先在 (7) 对 pair 两变量作精确多项式展开，再积分全部第一四输入。
任何 $ax^2A$ 均已在 (12)，不会被遗漏为另一个自由项。
(15) 不声称为零。它给
$$
v_p(\mathcal D^S_{r,M}(0))
=v_p(\mathcal D^T_{r,M}(0))
\ge8r+3M+3-8N
\tag{16}
$$
中的共同下界；若质量为零，赋值按 $+\infty$ 理解。

## 4. 同一个三次项仍严格返回原正矩

R679 的 (3) 与已付六的倍数齐次权三次稳定说明可直接应用。
理由是原四输入的角型为四：在一次低阶展开中，第一四输入次数为
$6d-j+a_q+a_\ell$；总 x 次数至多三时，唯一可保的项为
$j=2,a_q=a_\ell=0$、log 一次线性项。这个判断对 d=1、2 相同。
所以完整原负一矩在 (11) 三次项中准确相消，留下
$$
\boxed{
\mathfrak D_{r,M}
=\frac{(-1)^M\lambda^N\kappa^{3r+4M+5-2N}}
 {b(1-\kappa)(1-\kappa^3)}
 [B_0+B_1\kappa^{M+1}]
+p^{4r-4N-M-9}\mathcal O ,
}
\tag{17}
$$
其中
$$
\begin{gathered}
B_0=4C_a(1+\kappa)^2(1-\beta)(1-\beta\kappa^2),\qquad
B_1=3C_b(1+\kappa^2)(1-\beta\kappa)^2,\\
C_a=\frac{3\cdot1847(3+20\omega)}{125\cdot349},\qquad
C_b=\frac{54796+55860\omega}{43625}.
\end{gathered}
\tag{18}
$$
$C_a,B_0$ 为当前原 ray 上的单位，$C_b,B_1$ 整。
这里 $N(C_a)=9\cdot1847^2/(5^6\cdot349)$；
两个新表面素因子模64为55、29，已被原 $p\equiv7\bmod64$ 排除。
不增射线，也不需要 $I_{\Sigma,-1}$ 的赋值门。

高次权不改变尾界：在
$x=\kappa^{N+M+3}X$ 后，(7) 的整有限多项式和 (8) 的全部 log
都在 $\mathcal O[[X]]$。最坏 $t_j^{-1}$ 已支付。
第一套的真正 y 三阶差商再保其 $\kappa^{3M+3}$。
这给 (17) 的全部尾，未省任何高次项。

还可准确区分 S 中央：
$$
\boxed{v_p(\dot{\mathcal D}^S_{r,M})\ge4r-4N-M-9.}
\tag{19}
$$
证明不将 log 当角常数略去。固定 $\log\langle Q\rangle$ 或
$\log\langle L\rangle$ 的部分，在总 pair 次数二仍被 (9) 杀掉，
次数八始于 $x^8$。移动 log 中，若 A 次数为 d、pair 权次数为 e，
角型要求 $e-d\equiv2\bmod6$；d 正时最低 $e+d$ 为四。
其余所有 $ax^2A$ 只提高 x 次数。于是两个 S 行的前三次均严格消失，
再用同一个整展开得 (19)。第一套不含 $t_j^{-1}$，
其整展开半径 $\kappa^{N+1}$ 已足，亦满足显示的较弱共同界。

## 5. 全 cd 外部现在只有一条固定混合 T 行

下面的域均在原六输入上，不能由返回坐标猜测：
$$
\mathsf E_i(d)=\{Y_i\in p^d\},\qquad
\mathsf{CD}_N=\{c,d\in p^N\},\qquad
\mathsf V_i(d)=\mathsf E_i(d)\cap\mathsf{CD}_N,\qquad
\mathsf X_i(d)=\mathsf E_i(d)\setminus\mathsf{CD}_N.
\tag{20}
$$
每个实际角域 $\mathcal D_{r,m,j}\subset\mathsf V_i(d_i)$。
逐项定义其 cd 内补域
$\mathsf V_i(d_i)\setminus\mathcal D_{r,m,j}$，
使用同一个 $q_i^\sharp$ 和深度 $d_i$ 的原 S/T 观察。
然后按 (10)、(11) 作同一加权组合，记为 $\mathcal R^Z$；
按相同系数组合 $\mathsf X_i(d_i)$，记为 $\mathcal X^Z$。
这些是逐项真实域差；加权域之间可能重叠，保原重数，不另认一条无权集合。

R671 取 $j=N$ 的完整四轴返回适用于 (2)。
此时 $N-j=0$，返回权准确为
$$
q^{cd}_{i}
=1_{\{C^\perp\ {\rm unit}\}}
 \mathcal P^\sharp(H_i,\ 14C^\perp+\kappa^N K_i,\
                           G_\perp+g\kappa^N K_i),
\tag{21}
$$
$$
H_i=F_i-C,\qquad K_i=H_i-\frac{406}{143}D_*.
$$
这里 $C^\perp,G_\perp$ 及其完整半特征取 R671(5)。
$H_i\in\mathcal O$ 自动满足；不额外加深门。
该权对真实 $Y_i$ 核保持。

R679 的整个 cd 端点 S 给
$$
\mathcal A_0^S=J_S,\qquad \mathcal A_1^S=-J_S.
$$
定义同一个固定混合观察
$$
\boxed{
\mathcal A_T(w)=
 \int q^{cd}_0\,1_{\{Y_0\ {\rm unit}\}}
 \langle b_YY_0+\kappa^N(W_0-b_YY_0)\rangle^{d_pw}\,d\mu_0 .
}
\tag{22}
$$
R671 的完整 J 运输给 $\mathcal A_1^T=-\mathcal A_T$。
它不依 r、m、M 或 d。两个单位 cut 相同，所以
$\mathcal A_T(0)=J_S(0)=0$；但没有给 $\dot{\mathcal A}_T$ 赋零。
其精确差为
$$
\dot{\mathcal A}_{\rm rel}
:=\left.\frac1{d_p}\partial_w
(\mathcal A_T-\langle b_Y\rangle^{d_pw}J_S)\right|_0
=\int q^{cd}_0\,1_{Y_0\ {\rm unit}}
 \log\left(1+\frac{\kappa^N(W_0-b_YY_0)}{b_YY_0}\right)d\mu_0
\in p^N\mathcal O .
\tag{23}
$$

保 R682 原全算术系数
$$
\begin{aligned}
c_0&=2\lambda^{-2r}\beta^{N-r-M}A_\kappa(\beta^{-1}),\\
c_1&=(-1)^{M+1}\lambda^{-2r}\beta^{N-r}
             (1-\beta^{-1})A_\kappa(-1),\\
c_D&=\kappa^{3M+3}c_1-\sigma_Mc_0\in\mathcal O^\times .
\end{aligned}
\tag{24}
$$
因为整个 cd 返回将原 $\epsilon_i\lambda^{d_i+N}$ 换为
$\epsilon_i\lambda^{d_i+3N}$，得到完整 Mellin 恒等式
$$
\boxed{
\begin{array}{ll}
\mathcal D^S+\mathcal R^S=\lambda^{2N}c_DJ_S,&
\mathcal X^S=c_D(1-\lambda^{2N})J_S,\\[1mm]
\mathcal D^T+\mathcal R^T=\lambda^{2N}c_D\mathcal A_T,&
\mathcal X^T=c_D(6\delta J_T-\lambda^{2N}\mathcal A_T).
\end{array}}
\tag{25}
$$
两行相加都是原完整算术总行。未将 T 的 $\mathcal X$ 认成 S 的
$\mathcal X$；(22) 正是两者之间必须保留的具体观察。

## 6. 两步过滤准确消去全部 cd 外部

固定 N、r，仅在有限合法窗口内令 $M\mapsto M+2$，记移位为
$\mathsf U$。所有使用的深度都要满足 $r>N+M_{\max}+3$。
定义
$$
\widehat{\mathcal F}_{r,M}=\beta^{r+M}\mathcal F_{r,M}
\quad(\mathcal F=\mathcal D,\mathcal R,\mathcal X),\qquad
\widehat c_D=\beta^{r+M}c_D .
$$
由 (24)，在固定奇偶性上
$$
\widehat c_D=a_0+a_1(M),\quad
a_0=-2\sigma_M\lambda^{-2r}\beta^NA_\kappa(\beta^{-1}),\quad
\mathsf Ua_0=a_0,\quad
\mathsf Ua_1=\lambda^2\kappa^6a_1 .
\tag{26}
$$
于是完整实际过滤
$$
\boxed{\mathcal Q(\mathsf U)
=(\mathsf U-1)(\mathsf U-\lambda^2\kappa^6)}
\tag{27}
$$
给
$$
\boxed{
\mathcal Q\widehat{\mathcal X}^S
=\mathcal Q\widehat{\mathcal X}^T=0,\qquad
\mathcal Q\widehat{\mathcal R}^Z
=-\mathcal Q\widehat{\mathcal D}^Z\quad(Z=S,T).
}
\tag{28}
$$
同时整个 cd 未切行也被杀掉。以上都是全函数身份，不只中央或质量；
没有假设原两个中央为零。

把 (17) 的两个 M 模式 $\lambda^2\kappa^8,\lambda^2\kappa^{10}$
逐项代 (27)，置
$$
V_4=(\lambda^2\kappa^8-1)(\kappa^2-1),\qquad
V_5=(\lambda^2\kappa^{10}-1)(\kappa^4-1).
$$
它们是单位，得到
$$
\boxed{
\begin{aligned}
\mathcal Q(\beta^{r+M}\mathfrak D_{r,M})
={}&
\frac{(-1)^M\beta^{r+M}\lambda^{N+2}
 \kappa^{3r+4M+11-2N}}
 {b(1-\kappa)(1-\kappa^3)}
 [B_0V_4+B_1\kappa^{M+1}V_5]\\
&+p^{4r-4N-M-13}\mathcal O .
\end{aligned}}
\tag{29}
$$
尾界取真正三个窗口 $M,M+2,M+4$，不把有限窗口延为固定 r 下的
无限序列。若
$$
\boxed{r\ {\rm 偶},\qquad r>2N+5M+24,}
\tag{30}
$$
则 (29) 的准确赋值为 $3r+4M+11-2N$。

质量也须经过这个实际过滤。(15) 的最低 M 模式是第一套
$\ell=3$ 的 $\lambda^2\kappa^6$，被 (27) 准确杀掉；
次低是 $\ell=5$，其过滤乘数有赋值六。
第二套因额外 $\kappa^{3M+3}$ 更深。因此
$$
\boxed{
v_p(\mathcal Q\widehat{\mathcal D}^S(0))
=v_p(\mathcal Q\widehat{\mathcal D}^T(0))
\ge8r+5M+9-8N .
}
\tag{31}
$$
再由 (19)，
$$
v_p(\dot{\mathcal Q\widehat{\mathcal D}^S})
\ge4r-4N-M-13 .
\tag{32}
$$
(31) 的尺度 log 项比 (29) 主项严格更深，故绝对 T 中央也有
$$
\boxed{
v_p(\dot{\mathcal Q\widehat{\mathcal D}^T})
=v_p(\dot{\mathcal Q\widehat{\mathcal R}^T})
=3r+4M+11-2N,
}
\tag{33}
$$
而其 S 行满足 (32)。这里 (33) 的第二个等式准确来自 (28)。

例如同一个有限选择 $N=4,M=2,r=44$ 给
$$
A\in p^{88},\quad Q\text{ 环带 }44,45,\quad
L\text{ 环带 }46,\ldots,53,
$$
$$
v_p(\dot{\mathcal Q\widehat{\mathcal D}^T})=143,\qquad
v_p(\dot{\mathcal Q\widehat{\mathcal D}^S})\ge145,\qquad
v_p(\mathcal Q\widehat{\mathcal D}^Z(0))\ge339.
\tag{34}
$$
这是重叠窗口合并后的十六个原角域及其显示权；
cd 内部补偿逐项保留同样观察。

## 7. 与原十三步 T 过滤比较时，三个高模式不能删除

R679 的共同来源在 $\xi=\kappa^{n-N}$ 上为 degree 至多十二。
对 T 必须保完整 log 尾，并保持深度奇偶。取原深度移位
$\mathsf T_2:n\mapsto n+2$，定义
$$
P_{13}(X)=\prod_{a=0}^{12}(X-\lambda^4\kappa^{2a}).
\tag{35}
$$
$a=0$ 也在内；只用 R679 的纯 S 十二因子不能消 T 的常数混合来源。

在本篇**已规范化**的 opposite 行中，
$\beta^{r+M}$ 准确取消 (10) 的 $\beta^{-n_j}$ 对 M 的变化：
$$
\beta^{r+M}\beta^{-r-n_j}=\beta^{-r-j}.
$$
因此余下外部 M 权正是 $\kappa^{3M+3}$，其真实共轭为
$$
\boxed{
P_{13}(\mathsf U)\bigl(\kappa^{3M+3}F_{n(M)}\bigr)
=\kappa^{3M+3}P_{13}(\kappa^6\mathsf T_2)F_n .
}
\tag{36}
$$
若未先保这个 $\beta$ 规范，(36) 不能直接套原未规范角域。
第一套的 Y 深度 $k_m$ 不随 M 变，故这里也不把它误作同一个
$n\mapsto n+2$ 词。

原共同模式 $\lambda^{2n}\xi^a$ 在 (36) 的特征为
$\lambda^4\kappa^{2a+6}$。所以 (35) 只杀
$$
a=0,\ldots,9,
$$
而 $a=10,11,12$ 三条完整来源仍在。对这三项准确有
$$
\boxed{v_p\bigl(P_{13}(\lambda^4\kappa^{2a+6})\bigr)=156.}
\tag{37}
$$
这三个系数不是条件来源质量，不能因 R679 的冻结常数为 S 而删除。

同一十二次权把 R671 的 log 高系数界准确改为
$$
v_p([\xi^k]\dot{\mathcal B}_{i,\epsilon}^T)
\ge(k-12)N-\lfloor\log_pk\rfloor,\qquad k\ge13.
\tag{38}
$$
其证明仍在 R671 的固定 $Y_i$ 单位域：
每个高项含 $\kappa^{N(k-a)}/(k-a)$，$0\le a\le12$，
不改变单位 cut。结合 (37)–(38)，被保留的整个共同部分在
质量及中央上都有界
$$
\boxed{p^{\,10(n-N)+156}\mathcal O.}
\tag{39}
$$
质量只有三个显示的有限高项；中央还保 (38) 的全部尾。
这里只对 opposite 部分调用该同深结论，不据此估计第一套的另一种 cut。

未切 cd 的 T 行却具有 $\lambda^n$ 模式，所以
$$
v_p\bigl(P_{13}(\kappa^6\lambda^2)\bigr)=66;
\tag{40}
$$
它没有被消掉。其完整来源仍是 (22) 的 $\mathcal A_T$。
这正是把原十三步过滤真正搬到本篇角域以后需要保的项。

供比较，若直接对整个 $\widehat{\mathcal D}$ 作 (35)，其两个已付
首模式的乘数为
$$
P_{13}(\lambda^2\kappa^{2s})
=\lambda^{26}\kappa^{s(25-s)}U_s,\quad s=4,5,
$$
$$
U_s=(1-\lambda^2)
 \prod_{h=1}^{s}(\kappa^{2h}-\lambda^2)
 \prod_{h=1}^{12-s}(1-\lambda^2\kappa^{2h})\in\mathcal O^\times.
\tag{41}
$$
因此其相对中央主赋值为 $3r+4M+89-2N$，
全尾至少 $4r-4N-M-35$；例如
$r>2N+5M+124$ 使主项严格支配。该过滤的真正窗口到 $M+26$。
它保原中央系数为单位：$P_{13}(1)$ 是单位，
另一个系数模式的贡献由 (40) 严格更深。
但它也保同一个 $\mathcal A_T$ 系数，不能只保一列、删另一列。

## 8. 完整算术关系与当前确切边界

未过滤的整个原关系始终是 (25)：
$$
\mathcal D^Z+\mathcal R^Z+\mathcal X^Z
=c_D(J_S,6\delta J_T)_Z.
\tag{42}
$$
若原两个中央同时为零，它只给三项完整中央的准确和为零。
本篇已经从 $\mathcal X^T$ 中剥出唯一具体的
$\mathcal A_{\rm rel}$，而非另引入无定义的外部量。

(27) 消去整个 cd 外部的同时，也消去 (42) 的原中央系数。
这是 (26) 的同一列恒等式：任意仅依 M 的标量有限过滤，
若要对任意未知 $\mathcal A_T$ 消掉它的系数
$\lambda^{2N}\widehat c_D$，必然也消掉 $\widehat c_D$。
所以 (28)、(33) 是真实补偿的精确定位，不是一条附加算术零。
剩余为 $\mathsf V_i(d_i)\setminus\mathcal D_{r,m,j}$ 中同 q、
同归一观察的完整行。

另一方面，保原中央列的 (35) 也保 (22) 的混合观察，
并且在 opposite 词里留下 (37) 的三条高来源和 (38) 全尾。
这些显示的项必须继续与原 Y/W 核、各失败支同域联立。
本篇没有以局部非零代替主目标所需的完整中央非零。

## 复现与引用

固定检查脚本：
[check-r685-new-carry-mass-and-actual-outside-filters.js](../scripts/check-r685-new-carry-mass-and-actual-outside-filters.js)。

运行：
~~~sh
node topics/rank2-sha-infinitely-many-p/scripts/check-r685-new-carry-mass-and-actual-outside-filters.js
~~~

脚本只向标准输出给可重算报告，不写仓库数据文件。
固定参数为原 $b,\Omega$ 齐次恢复、辅助低展开 $b=\Omega=1$；
首次实际运行环境为 functions V8，标签 `R685-exact-18`；它不是 GitHub Actions run_id。
公开 Actions [run 43679602653](https://github.com/Rogerhu12/math-research-public/actions/runs/43679602653)
已在提交 `199268b852c965c65b6f65932a547ab68ebbbf97` 按上式、无额外参数执行成功。
输出3001字节，SHA256与下列首次输出完全相同；未持久保存报告数据。
本证明不以附带有限检查替代正文的全参数论证。
它准确检查四条完整正矩、所有质量次数、两个实际过滤模式、
十三因子赋值及两个有限窗口。一般的来源运输、半特征、
单位 cut、整解析尾与实际全 Mellin 身份由正文及所引完整结果支付，
不以有限数值检查替代。

本次标准输出 SHA256：`eb0a2b8c8116fad75b02d7849a557341b43c6d294fce8e4850f8416e16df0c3f`。

主要依赖：
[R679](R679-neutral-degree-twelve-three-s-and-exterior-return.md)；
[R678](R678-original-finite-word-corners-and-negative-one-return.md)；
[R682](R682-original-opposite-corners-and-uniform-unit-difference.md)；
[R671](R671-fixed-depth-cd-return-and-original-exterior-filters.md)；
[三次稳定说明](../notes/2026-11-15-principal-carry-corner-third-jet-stability.md)。
