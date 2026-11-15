# R789 — 同一 CM 帽的有限解析芽、完整质量与原 T 外部的非零差

日期：2026-11-15。**状态：下列真实域、完整 Mellin 恒等式与有限外部非零已证明。**

本文保持 R734 的最终 $q_N^*$，接 R784 的完整 216 分支第三中央式，不另选测试。首先证明：奇数 W 深度 $m\ge n$ 返回后，整个共同帽准确成为一个固定域。因此 R784 的逆 Y 帽行及其 E 浅补域除以 $\lambda^m$ 后已经稳定；其中所有 CM 尺度质量项仍保留。

同一个固定域也给 R783 的固定观察 $\mathcal C_N(z)$ 一个完整解析芽。将相邻两个奇数深度的**整个 Mellin 行**按 $\lambda^2$ 作差，局部质量和固定 t-log 项同时准确消去。所得原 T 外部是一个有限、质量严格为零且中央导数非零的实际组合。它位于原 CD 全失败域，所有 E 分割保持。最后，完整 CM 源恒等式迫其余 215 分支的外部作相应的非零补偿。

这没有给原第三中央增加独立零：逆 Y 观察的同一个差算子准确为零，而固定观察的非零项位于另一块补域。本文逐式保留这一区别。

## 1. 原来源、固定参数和真正帽域

保 R783—R785 的原射线、全部固定坏集、$p>163$、周期 $\Omega$ 及纯 C 六角平均。置
$$
\omega^2+\omega+1=0,\quad
a=1+3\omega,\quad a\bar a=7,\quad
b_Y=\frac{20+3\omega}{17},\quad
\alpha_W=17-3\omega,
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad d_p=p-1.
\tag{1}
$$
$q=q_N^*$，$N\in4\mathbf Z_{>0}$，$n>N$。域恒等式对这些 n 都成立；调用 R783 的非零定理时取原 $n=N+300$ 及该定理的 N 范围。

两态与真实观察为
$$
B_0=\frac{e_0-\omega(e_1+e_2)}{1-\omega^2},
\qquad B_1=K_WB_0,
$$
$$
P=b_YY+Z_0,\qquad W=P-at,\qquad V_t=\bar aP+29t.
\tag{2}
$$
全部来源已带同一个原 C 平均。q 只依 C、$H_1$、J，这三条伙伴均垂直于 Y、$Z_0$、t，故 q 被本文所有真实 W 和 P 返回逐点固定。

记
$$
u_J=\frac{7(4+9\omega)}{72},\qquad
u_Z=-\frac{68+33\omega}{144},
$$
$$
\mathcal H=\{Y\ {\rm unit},\ J,Z_0\in p^N,\
                          u_JJ+u_ZZ_0\notin p^n\},\qquad
\mathcal K=\mathcal H\cap\{t\ {\rm unit}\}.
\tag{3}
$$
这是原 $\hat s,\hat d$ 帽及原 U 失败门，不删 J 截距。物理 E 是
$$
E=e_ZZ_0+h_0t+e_JJ,\quad
e_Z=-\frac{17(25+48\omega)}{144},\quad
h_0=17+3\omega,\quad e_J=-\frac{1841}{72}.
\tag{4}
$$
设 $\mathcal E=\{E\in p^N\}$。在 $\mathcal K$ 上 E 为单位，故 $\mathcal K\subset\mathcal E^c$。

本文使用的原 Mellin 测试为
$$
f_w(v)=1_{v\ {\rm unit}}\langle v\rangle^{d_pw}.
\tag{5}
$$
所有导数均在 $w=0$ 取值；$v_p(p)=1$。旧 R410 已支付 $1-\lambda^2\in\mathcal O^\times$。原 q 在其完整支撑上整有界，不能将其带深度分母的多项式脱离支撑单独使用。

## 2. W 返回后的帽在有限深度已经准确稳定

定义真正 W 正交的三条行
$$
y^\circ=Y-\frac{\alpha_W}{36}W,\qquad
z^\circ=Z_0-\frac4{17}W,\qquad
t^\circ=t+\frac{\bar a}{36}W.
\tag{6}
$$
由原 Gram，这三行与 J 都垂直于 W。又有准确恒等式
$$
\boxed{b_Yy^\circ+z^\circ=a t^\circ.}
\tag{7}
$$
确实 $b_Y\alpha_W/36+4/17=29/36$，而 $a\bar a=7$。

对 $x=\kappa^m$，真实 W 缩放逐项为
$$
\begin{aligned}
Y\circ P_{W,x}&=y^\circ+\frac{\alpha_W}{36}xW,\\
Z_0\circ P_{W,x}&=z^\circ+\frac4{17}xW,\\
t\circ P_{W,x}&=t^\circ-\frac{\bar a}{36}xW,\\
P\circ P_{W,x}&=a t^\circ+\frac{29}{36}xW.
\end{aligned}
\tag{8}
$$
E 和 q 严格不动。置固定域
$$
\boxed{
\mathcal D^\circ=
\{y^\circ\ {\rm unit},\ J,z^\circ\in p^N,\
                       u_JJ+u_Zz^\circ\notin p^n\}.
}
\tag{9}
$$

若 $m\ge n$，则
$$
\boxed{\mathcal H\circ P_{W,\kappa^m}=\mathcal D^\circ.}
\tag{10}
$$
证明是有限同余而非极限：在 (8) 中所有改变均属于 $p^m$；它们不改变 Y 的单位条件、深 N 条件或模 $p^n$ 的失败条件。原格和所有显示常数均在当前 p 整。

在 $\mathcal D^\circ$ 上，(7) 使 $t^\circ$ 为单位；(4)、(6) 又给
$$
E=e_Zz^\circ+h_0t^\circ+e_JJ,
$$
故 E 为单位。这里**没有**推出原输入 Y 为单位。后文出现的 $\mathcal D^\circ\cap\{Y\ {\rm unit}\}$ 是另一个必须保留的真实条件。

以下 m 始终为满足 $m\ge n$ 的奇数。因此 W 核把 $B_0$ 返回 $B_1$，外部系数为 $\lambda^m$。

## 3. 全部 CM 分支与两种局部质量

照 R695/R784 的 canonical 规范，
$$
\alpha=\alpha_{j,k}=(4+\omega)^j(5+2\omega)^k,\quad
0\le j\le17,\quad k\in\{0,1\},
$$
$$
r_\alpha=\bar\alpha/\alpha,\qquad
s=\zeta r_\alpha\ (\zeta\in\mu_6),\qquad
a_s=\frac{\omega^{2j}(-\omega)^k}{216}.
\tag{11}
$$
在原 first-$2Y$、degree136 的完整 lift 上，
$$
\mathcal Q_\alpha F
=\sum_{\tau\in E[\alpha]}
       \mathsf T^{136}_{\bar\alpha\tau,\,2Y}F,\qquad
\sigma_{s,i}=\alpha^{-1}(D_s)_*\nu_{\mathcal Q_\alpha B_i},
$$
$$
D_s:(Y,Y^\perp)\longmapsto(sY,Y^\perp),\qquad
\mathcal P_U B_i=\sum_s a_s\sigma_{s,i}.
\tag{12}
$$
原半特征、中心、全部纤维及 $1/\alpha$ 不变。特别
$$
\mathcal P_U B_0=0
\tag{13}
$$
是完整联合来源恒等式，其依据可以逐项定位，不能仅从 Y 边际引用：

R483(25) 给 $P_{\rm new}\mathcal F_0^L=0$，因为原第一态的整个 $N_7^9=-1$ 块与 new 的 $+1$ 块互斥。R493(17)、(18) 则给
$$
h_W=\omega^2\mathcal T_*\rho_0,\qquad
\mathcal T^3=I,\qquad \mathcal T\bar{\mathcal T}^{\,t}=I,\qquad
Y\circ\mathcal T=Y .
\tag{13a}
$$
在同一原六输出框架中，R493(25)、(27) 精确为
$$
L\mathcal T L^{-1}=\operatorname{diag}(1,D_5),\qquad
\nu_{h_W^L}=\omega^2[I_Y,D_5]_*\nu_{\mathcal F_0^L}.
\tag{13b}
$$
第一 Y 轴的每个 canonical CM 纤维、中心相位及角投影因此逐项与这个真正伙伴变换交换。R493(28) 明确给出完整 $P_{\rm new}h_W^L=0$。由 (2) 的线性组合即得 (13)，不是把 $Y_*B_0=0$ 升为联合零。本文原 C 平均与 q 都在 Y 的正交伙伴上，亦与这些第一轴操作交换；故 (13) 可乘整个 q 并施任意完整六变量测试。

恒等分支 $s=1$ 唯一，其系数为 $1/216$，来源为 $B_i$。其余 215 分支不单独为零。

同一个固定域 (9) 上须区分
$$
\mu_\alpha^\circ=\int_{\mathcal D^\circ}q\,d\nu_{\mathcal Q_\alpha B_1},
\qquad
\mu_\alpha^Y=\int_{\mathcal D^\circ}1_{Y\ {\rm unit}}q\,
                                      d\nu_{\mathcal Q_\alpha B_1}.
\tag{14}
$$
两者之差准确为 $\mathcal D^\circ\cap\{Y\in p\}$ 的积分。没有已付结论令它为零。原所有 finite lifts 都整有界，故这些质量以及下文的单位分母正矩属于同一整系数环。

## 4. 逆 Y 的第三中央行：固定有限来源与全尺度项

记 R784 的实际行
$$
W_s=b_Ys^{-1}Y+Z_0-at,\qquad
M_{s,m}=D_sP_{W,\kappa^m}D_s^{-1},
$$
$$
Y_s^{[-m]}=
Y+\frac{s\alpha_W}{36}(\kappa^{-m}-1)W_s.
\tag{15}
$$
定义其帽项及整个 E 浅补项
$$
\begin{aligned}
\mathcal A_{s,m}(w)
 &=\int_{\mathcal H,\ W_s\in p^m}
                    f_w(Y_s^{[-m]})q\,d\sigma_{s,0},\\
\mathcal U_{s,m}(w)
 &=\int_{(\mathcal E^c\cap\{W_s\in p^m\})\setminus\mathcal H}
                    f_w(Y_s^{[-m]})q\,d\sigma_{s,0}.
\end{aligned}
\tag{16}
$$
R784 已付 $\mathcal H\cap\{W_s\in p^m\}\subset\mathcal K\subset\mathcal E^c$，所以此相减合法。

先拉回 $D_s$，再用完整 W 核和 (10)。原帽在 $D_s$ 下保持，实际观察的缩放是 s，而非只剩 $\zeta/\alpha$。准确得到
$$
\boxed{
\begin{aligned}
\mathcal A_{s,m}(w)
 &=\alpha^{-1}\lambda^m
       \langle r_\alpha\rangle^{d_pw}\,\mathcal F_\alpha(w),\\
\mathcal U_{s,m}(w)
 &=\alpha^{-1}\lambda^m
       \langle r_\alpha\rangle^{d_pw}\,\mathcal G_\alpha(w),
\end{aligned}}
\tag{17}
$$
其中固定有限来源上的两行是
$$
\mathcal F_\alpha(w)
 =\int_{\mathcal D^\circ}f_w(Y)q\,d\nu_{\mathcal Q_\alpha B_1},
\qquad
\mathcal G_\alpha(w)
 =\int_{\mathcal E^c\setminus\mathcal D^\circ}
                         f_w(Y)q\,d\nu_{\mathcal Q_\alpha B_1}.
\tag{18}
$$
$\mathcal F_\alpha(0)=\mu_\alpha^Y$，不是 $\mu_\alpha^\circ$。
E 被两个返回都固定，而 $\mathcal D^\circ\subset\mathcal E^c$，支付了 (18) 第二行的完整域。

六个角分支在 (17) 中可合并。令
$$
b_{j,k}=\frac{\omega^{2j}(-\omega)^k}{36\alpha_{j,k}},\qquad
c_N=\frac{(52/3)\beta^N-\lambda^{2N}}{1-\omega^2}.
$$
R784 的完整第三中央式在本深度范围准确成为一条固定有限恒等式
$$
\boxed{
\sum_{j,k} b_{j,k}\langle r_\alpha\rangle^{d_pw}
       \{\mathcal F_\alpha(w)+\mathcal G_\alpha(w)\}
=c_N\langle2\rangle^{-d_pw}J_U(w).
}
\tag{19}
$$
它保留全部 36 个 raw traces，即原 216 个完整来源；没有为参考或外谱单独添零。

其局部导数明确含
$$
\alpha^{-1}\lambda^m
 \left\{\mathcal F_\alpha'(0)
       +d_p\log\langle r_\alpha\rangle\,\mu_\alpha^Y\right\},
\tag{20}
$$
以及 $\mathcal G_\alpha$ 的相同尺度项。只有整个右侧可用 $J_U(0)=0$ 删除总尺度质量。

置深度差算子
$$
\Delta_2 F_m=F_{m+2}-\lambda^2F_m.
\tag{21}
$$
由 (17)，对每个完整来源、作为整个 w 函数，
$$
\boxed{\Delta_2\mathcal A_{s,m}=0,\qquad
       \Delta_2\mathcal U_{s,m}=0.}
\tag{22}
$$
这是有限深度稳定后来源和观察的恒等式，不需假定 $J_U'(0)=0$。
因此不能把不同 m 的 (19) 当成新的独立中央约束。

## 5. 固定观察的角平均必须保留其负六起始项

对一个固定 raw $\alpha$ 来源，若观察始终是同一个物理 $t/P$，拉回 $D_s$ 后为 $t/(b_Y\zeta r_\alpha Y+Z_0)$。准确角平均是
$$
\boxed{
\frac16\sum_{\zeta\in\mu_6}
 \frac{t}{b_Y\zeta r_\alpha Y+Z_0}
=\frac{tZ_0^5}{Z_0^6-(r_\alpha b_YY)^6}.
}
\tag{23}
$$
帽上分母为单位，右侧在 $p^{5N}\mathcal O$，且其完整展开为
$$
-\frac{tZ_0^5}{(r_\alpha b_Y)^6Y^6}
 \sum_{h\ge0}\left(\frac{Z_0}{r_\alpha b_YY}\right)^{6h}.
\tag{24}
$$
它读的是带 $Z_0^5$ 的负六及随后负 $6h+6$ 行，不是原未平均的负一。

同样，对 $z\in p\mathcal O$，帽/t-unit 上
$$
\frac16\sum_\zeta
 \log\left(1-\frac{z(b_Y\zeta r_\alpha Y+Z_0)}{at}\right)
=\frac16\log
 \frac{(at-zZ_0)^6-z^6(r_\alpha b_YY)^6}{(at)^6}.
\tag{25}
$$
所有对数的参数都在 $1+p\mathcal O$，有限乘积允许准确相加。对真正的 t 扰动则为
$$
\frac16\sum_\zeta
 \log\frac{b_Y\zeta r_\alpha Y+Z_0-a\kappa^m t}
              {b_Y\zeta r_\alpha Y+Z_0}
=\frac16\log
 \frac{(Z_0-a\kappa^m t)^6-(r_\alpha b_YY)^6}
      {Z_0^6-(r_\alpha b_YY)^6}.
\tag{26}
$$
$m\ge N$ 时此式属于 $p^{m+5N}\mathcal O$；逐项展开六次差即可验证。它的首 t 项仍带 $Z_0^5$。

(23)—(26) 不作用于 (17) 的移动逆 Y：后者拉回时 s 从逆观察准确提出，$\zeta$ 在主 Mellin 因子中已经消去。两种角平均不能交换使用。

## 6. 原帽固定观察的完整 W-deep Mellin 芽

保 R783 的同一函数
$$
\mathcal C_N(z)=
 \int_{\mathcal K}\log\left(1-\frac{zP}{at}\right)q\,dB_0,
\qquad z\in p\mathcal O.
\tag{27}
$$
原 $\mathcal T$ 特征给整个基准行
$$
\int_{\mathcal K}f_w(-at)q\,dB_0=0.
\tag{28}
$$
因此
$$
\mathcal T(z,w):=\int_{\mathcal K}f_w(zP-at)q\,dB_0
$$
满足
$$
\mathcal T(z,0)=0,\qquad
\mathcal T'(z,0)=d_p\mathcal C_N(z).
\tag{29}
$$
这里及以下，带撇号表示 w 导数。R783 已证明：对其合格 p、所有充分大的固定 N，$\mathcal C_N$ 非零；于是所有充分大的 $\ell$ 有 $\mathcal C_N(\kappa^\ell)\ne0$。

将 (29) 精确分成 W 深 m 与其整个补集：
$$
\begin{aligned}
\mathcal B_m(z,w)
 &=\int_{\mathcal H,\ W\in p^m}f_w(zP-at)q\,dB_0,\\
\mathcal O_m(z,w)
 &=\int_{\mathcal K,\ W\notin p^m}f_w(zP-at)q\,dB_0,\\
\mathcal T(z,w)&=\mathcal B_m(z,w)+\mathcal O_m(z,w).
\end{aligned}
\tag{30}
$$
第一域自动 t-unit。此处 W 深条件针对原未改变的 W，观察却是显示的 $zP-at$；二者都保留。

设
$$
A(z)=\frac{7+29z}{36a(1-z)},\qquad B=\frac7{36a},\qquad x=\kappa^m.
\tag{31}
$$
(8) 给逐点恒等式
$$
(zP-at)\circ P_{W,x}
=-a t^\circ(1-z)
       \left(1-xA(z)\frac W{t^\circ}\right).
\tag{32}
$$
因此整个 Mellin 行准确返回为
$$
\boxed{
\mathcal B_m(z,w)=
\lambda^m\langle1-z\rangle^{d_pw}
 \int_{\mathcal D^\circ}f_w(-at^\circ)
       \left\langle1-\kappa^mA(z)\frac W{t^\circ}\right\rangle^{d_pw}
                                     q\,dB_1.
}
\tag{33}
$$
这是同一个有限来源、固定域上的解析芽。没有换成其质量或删除 t-log。

定义全部整正矩及固定对数项
$$
M_r=\int_{\mathcal D^\circ}(W/t^\circ)^r q\,dB_1\quad(r\ge0),
\qquad
L_0=\int_{\mathcal D^\circ}\log\langle-at^\circ\rangle q\,dB_1.
\tag{34}
$$
$M_0=\mu_1^\circ$，与 (20) 中的 $\mu_1^Y$ 不同。由于 $t^\circ$-unit，$M_r\in\mathcal O$，$L_0\in p\mathcal O$。
由 (33) 得
$$
\mathcal B_m(z,0)=\lambda^mM_0,
$$
$$
\boxed{
\frac{\mathcal B_m'(z,0)}{d_p}
=\lambda^m\left[
 L_0+\log(1-z)M_0
 -\sum_{r\ge1}\frac{\kappa^{mr}A(z)^r}{r}M_r\right].
}
\tag{35}
$$
该级数一致收敛。两个前项都必须保留，且都由 (21) 准确消去。

## 7. 质量为零、中央非零的完整外部差

由 (29)、(30)、(35)，不使用任何中央失败假设，就有
$$
\boxed{(\Delta_2\mathcal O_m)(z,0)=0}
\tag{36}
$$
以及准确全级数
$$
\boxed{
\frac{(\Delta_2\mathcal O_m)'(z,0)}{d_p}
=(1-\lambda^2)\mathcal C_N(z)
+\lambda^{m+2}\sum_{r\ge1}
 \frac{\kappa^{mr}(\kappa^{2r}-1)A(z)^r}{r}M_r.
}
\tag{37}
$$
局部 $M_0$、$L_0$ 并未被假定为零；它们在这个显示的有限差中严格抵消。

对 $z\in p\mathcal O$，$A(z)$ 是单位。对任意 $r\ge1$，
$rm-v_p(r)\ge m$，而 $r\ge2$ 时 $rm-v_p(r)\ge2m$。
故 (37) 给
$$
\boxed{
\frac{(\Delta_2\mathcal O_m)'(z,0)}{d_p}
=(1-\lambda^2)\mathcal C_N(z)+p^m\mathcal O.
}
\tag{38}
$$
其精确第一误差项为
$\lambda^{m+2}\kappa^m(\kappa^2-1)A(z)M_1$，其余在 $p^{2m}\mathcal O$；
不假设 $M_1$ 非零。

固定一个使 $\mathcal C_N(z)\ne0$ 的 z。若 m 为奇数、
$m\ge n$ 且
$$
m>v_p(\mathcal C_N(z)),
\tag{39}
$$
则 $1-\lambda^2$、$d_p$ 为单位，因而
$$
\boxed{
v_p\bigl((\Delta_2\mathcal O_m)'(z,0)\bigr)
=v_p(\mathcal C_N(z))<\infty.
}
\tag{40}
$$
这是两个有限真实域的整 Mellin 差：其质量为零，中央导数严格非零。
$\lambda^m$ 在 p-adic 意义下是单位，本证明没有将它作为收缩量。

### 返回到原物理 W 观察

取 $z=\kappa^\ell$。定义实际原六变量域
$$
\mathcal X_{\ell,m}^{\rm out}
=P_{P,\kappa^\ell}
 \bigl(\mathcal K\cap\{W\notin p^m\}\bigr),
\qquad
\mathscr O_{\ell,m}(w)
=\int_{\mathcal X_{\ell,m}^{\rm out}} f_w(W)q\,dB_0.
\tag{41}
$$
原 P 核是 $\beta^\ell$，q 与 P 正交，故
$$
\boxed{
\mathscr O_{\ell,m}(w)=\beta^\ell\mathcal O_m(\kappa^\ell,w).
}
\tag{42}
$$
因此 (36)、(40) 对 $\Delta_2\mathscr O_{\ell,m}$ 原样成立。

为完全显示此域，置
$$
R_P=Y-\frac{17-3\omega}{29}P,\quad
\vartheta=\frac{144}{493},\quad
Z_\ell=\vartheta\kappa^{-\ell}P-b_YR_P .
$$
则 (41) 准确为
$$
\boxed{
\left\{
\begin{array}{l}
R_P,t\ {\rm unit},\ J,Z_\ell\in p^N,\
                   u_JJ+u_ZZ_\ell\notin p^n,\\
\kappa^{-\ell}P-at\notin p^m
\end{array}
\right\}.
}
\tag{43}
$$
它自动 $v_p(P)=\ell$，属于 R783 的原 CD 全失败帽像；物理 W 为单位。
最后一行是原像中 W 的失败条件，不能改成物理 $W\notin p^m$。
R783 的三个 E 深盘与全 E 浅补集在 (43) 中全部保留，没有按质量合并。

写 R783 的首非零项为 $\mathcal C_N(z)=c_{s_N,N}z^{s_N}+\cdots$。
对每个固定合格 p、N，先取充分大的 $\ell$，再取任一奇 m 满足
$$
m\ge n,\qquad m>s_N\ell+v_p(c_{s_N,N}),
$$
就有完全有限的结论
$$
\boxed{
(\Delta_2\mathscr O_{\ell,m})(0)=0,\qquad
v_p\bigl((\Delta_2\mathscr O_{\ell,m})'(0)\bigr)
=s_N\ell+v_p(c_{s_N,N}).
}
\tag{44}
$$
没有新增算术零。原完整 T 中央等式仍须保 (43) 之外的全部域。

## 8. 同一固定来源的相对 log：更精确的误差及质量差别

若只读 $\mathcal C_N$ 本身，将 (27) 的 W 深部分记为
$$
F_m(z)=\int_{\mathcal H,\ W\in p^m}
            \log\left(1-\frac{zP}{at}\right)q\,dB_0,
\qquad R_m(z)=\mathcal C_N(z)-F_m(z).
$$
由 (8)，逐点准确为
$$
\log\left(1-z\frac{P\circ P_{W,x}}{a\,t\circ P_{W,x}}\right)
=\log(1-z)+\log\left(1-xA(z)\frac W{t^\circ}\right)
              -\log\left(1-xB\frac W{t^\circ}\right).
$$
故
$$
\boxed{
F_m(z)=\lambda^m\left[
\log(1-z)M_0-
 \sum_{r\ge1}\frac{\kappa^{mr}}r
                     (A(z)^r-B^r)M_r\right].
}
\tag{45}
$$
此处仍是 $\mu_1^\circ$；逆 Y 测试额外的 Y-unit 不可插入 (45)。

若 $z\ne0$，则
$$
A(z)-B=\frac{z}{a(1-z)},\qquad
\frac{A(z)}B=1+\frac{36z}{7(1-z)}.
$$
p 为奇数，原常数均为单位，单位群上的对数或二项式给
$$
v_p\!\left(\frac{A(z)^r-B^r}{r}\right)=v_p(z)
\quad(r\ge1).
\tag{46}
$$
于是
$$
\boxed{
\Delta_2R_m(z)
=(1-\lambda^2)\mathcal C_N(z)+p^{m+v_p(z)}\mathcal O.
}
\tag{47}
$$
这比 (38) 的误差深，但它是两个同域单位观察相减的相对行。
(33)—(44) 才是不作这个基准相减的完整原 W Mellin 版本。
两者都已保质量，不能用 (47) 的较强误差去替换 (38)。

## 9. 其余 215 个固定 CM 外部的真实强制补偿

现在对所有 s 使用**同一个固定物理观察**，定义
$$
\begin{aligned}
\mathcal T_s(z,w)&=\int_{\mathcal K}f_w(zP-at)q\,d\sigma_{s,0},\\
\mathcal B_{s,m}(z,w)&=
 \int_{\mathcal K,\ W_s\in p^m}f_w(zP-at)q\,d\sigma_{s,0},\\
\mathcal O_{s,m}(z,w)&=
 \int_{\mathcal K,\ W_s\notin p^m}f_w(zP-at)q\,d\sigma_{s,0}.
\end{aligned}
\tag{48}
$$
由完整来源 (13)，对整个 w 函数
$$
\sum_s a_s\mathcal T_s(z,w)=0,\qquad
\boxed{
\sum_s a_s\Delta_2\mathcal O_{s,m}
=-\sum_s a_s\Delta_2\mathcal B_{s,m}.
}
\tag{49}
$$
这一步使用相同测试，故合法；它不是把 (16) 的随 s 逆 Y 观察硬换为固定观察。

其全部近管仍在同一个固定域上。置
$$
P_s^\circ=b_Ys y^\circ+z^\circ,\qquad
L_s=\frac{b_Ys\alpha_W}{36}+\frac4{17}.
$$
先拉回 $D_s$，再用 W 核，准确得到
$$
\boxed{
\mathcal B_{s,m}(z,w)=\frac{\lambda^m}{\alpha}
 \int_{\mathcal D^\circ}
 f_w\!\left(
 z(P_s^\circ+\kappa^mL_sW)
        -a(t^\circ-\bar a\kappa^mW/36)\right)
                              q\,d\nu_{\mathcal Q_\alpha B_1}.
}
\tag{50}
$$
其中全部 canonical lifts、原固定 finite 源与伙伴保持。
$z\in p\mathcal O$、$x\in p\mathcal O$ 时，(50) 中的观察是单位，
且 x 系数整。对数在这个单位邻域的变化是 $x\mathcal O$。
所以
$$
(\Delta_2\mathcal B_{s,m})(z,0)=0,\qquad
\frac{(\Delta_2\mathcal B_{s,m})'(z,0)}{d_p}
\in p^m\mathcal O.
\tag{51}
$$
这也可直接从 (50) 的固定 x-解析芽相减证明，不依赖任何新非零输入。
216 项有限，所有系数和 $1/\alpha$ 在当前 p 都整且为单位。

$s=1$ 的 (48) 正是第6—7节的原行。因此 (37)、(49)—(51) 给
$$
\boxed{
\sum_{s\ne1}a_s
       \frac{(\Delta_2\mathcal O_{s,m})'(z,0)}{d_p}
=-\frac{1-\lambda^2}{216}\mathcal C_N(z)+p^m\mathcal O.
}
\tag{52}
$$
其整个有限组合的质量为零。若 (39) 成立，则 (52) 严格非零，
赋值恰为 $v_p(\mathcal C_N(z))$。
故恒等分支的原非零外部确实迫其余 215 个真实来源的外部作非零补偿。

这没有把每个非恒等来源分别赋值或赋零，也没有认其为裸 $B_0$。
只有恒等分支使用第7节的原 P 核返回到 (43)；
对其余 $\sigma_{s,0}$，本篇始终保 (48)、(50) 的原观察和来源，
没有擅自给它们增加 P 单轴核。

若对相对 log 作同样分割，(51)、(52) 的误差可换为
$p^{m+v_p(z)}\mathcal O$。这是 (45)—(47) 的同源形式，
仍不允许删除全部 215 项或替换成原负一矩。

## 10. 四个真实格子及两种补域的位置

令 $\mathcal L_{s,m}=\{W_s\in p^m\}$。因为 $\mathcal K\subset\mathcal E^c$，
整个 E 浅域有如下完整、不交分割：

| 实际域 | 本篇所用的完整行 |
| --- | --- |
| $\mathcal K\cap\mathcal L_{s,m}$ | 同时承载 (16) 的逆 Y 帽行与 (48) 的固定观察近管；两种观察不同 |
| $(\mathcal E^c\setminus\mathcal K)\cap\mathcal L_{s,m}$ | (16) 的整个第三中央 E 浅补域 |
| $\mathcal K\cap\mathcal L_{s,m}^c$ | (48) 的固定观察帽内外部 |
| $(\mathcal E^c\setminus\mathcal K)\cap\mathcal L_{s,m}^c$ | 仍保留的第四块，未由本篇赋零 |

原 $\mathcal H\cap\mathcal L_{s,m}\subset\mathcal K$，
故第二行准确等于 R784 的原补域，不是新选补域。
第二与第三行互不相交。
(22) 精确杀第二行的逆 Y 深度差；
(40)、(52) 给第三行的固定观察组合非零。
这些事实完全相容，不得从其中一个等式减去另一个不同域或不同观察的行。

R784 非恒等近管确在原 P/t/W/Vt 四-unit 域，但它们携带完整 $\sigma_{s,0}$ 与 $Y_s^{[-m]}$。
第9节只在相同固定观察上使用 (13)，所以保持这个物理位置与实际来源之间的区别。

## 11. 已支付的接口和主缺口

本篇给出的新有限接口是：

- 原逆 Y 第三中央帽族在奇 $m\ge n$ 时已经是 (17)—(19) 的固定 finite 源，全部局部尺度质量明确。
- 原完整 W 外部有 (43) 的实际六变量域，以及 (44) 的质量零、中央非零有限差；原 E 深三支和全 E 浅均未删。
- 完整 CM 源迫其余 215 个外部满足非零补偿 (52)，不是只给一个形式和式。
- 固定角平均的真正低行是 (23)—(26)，而移动逆 Y 的角因子按 (17) 消去；二者绝不混用。

原 $J_S'(0)=J_T'(0)=J_U'(0)=0$ 尚未与这些完整补偿发生矛盾。
(19) 只给已有第三中央的有限源式，(49) 来自原 whole 来源零，
(44) 的其余原 T 外部也必须保留。
下一步若要消元，须处理第10节显示的第四块或支付同观察的额外返回，
而不是把第二、第三格子相认。主目标仍开放。

## 依赖及执行范围

- [R410](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)：固定射线与原 Euler 单位因子。
- [R483](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)、[R493](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)：原第一态和 h 的完整 new 投影为零、保 Y 的真实五伙伴变换及全部 canonical 相位交换。
- [R695](R695-original-cm-word-domains-and-a-z-carries.md)：完整 CM 纤维、中心和真实 W 共轭返回。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：原最终 q、整性和完整来源适配。
- [R777](R777-original-b-sector-p-t-core-and-complete-central-renewal.md)、[R778](R778-original-degree174-full-characters-and-unramified-seventeen-point-fields.md)：原 B 两态及 P/W 核。
- [更正后的 R780](R780-original-third-central-b-state-and-true-w-deep-return.md)：E 浅与 E 深的正确分割、原 U 规范。
- [R783](R783-native-hat-images-and-nonzero-cd-exterior-central-row.md)：同一 $\mathcal C_N$ 的实际非零、P 帽像与全部 CD/E 补域。
- [R784](R784-third-central-shallow-hats-and-four-unit-cm-tubes.md)：216 个完整第三中央来源与实际逆 Y 管。
- [R785](R785-original-three-state-even-frames-and-exact-e-gate.md)：三态偶核、原三维 Gram 和 E 的 J 截距。

所有新结论由显示的原行恒等式、已付整核、有限同余和收敛的单位对数展开直接证明。
本篇没有执行新数值计算、扫描或生成可重算数据；不新增数据文件。
