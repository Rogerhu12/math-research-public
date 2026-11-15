# R780 — 原 U136 的第三中央在 B 第二态、W 深支和共同帽上的完整返回

日期：2026-11-15。**状态：已证明。**

本篇恢复第三条原算术来源的真实六变量入口，并将它接到 R777 的同一个 B 分量及其 W 核第二态。新增的中央观察确实含原 U136；它不是 R777 已有的原 T 行的重新分区。原全部有限门、归一和补域同时保留。

具体地，在原 EYW 深 N 门上，B 第一态的完整 Y 来源为零，而 W 核后的 B 第二态的完整 Y 来源为原 S 与 [1/2] U136 的明确组合。其 W 来源仍为原 T。把这条第三行通过真实 W 核搬回，得到原 B 第一态在 W 深支上的另一个归一观察。本文还给它在 R777 的 W 近相消部分和 R773 共同帽中的准确分割；这些部分不被各自赋零。

## 1. 第三来源的绝对规范

沿原 b=17 模型、微分 dz=dx/(2y)、sigma首项z以及同一普通周期Ω。固定
$$
U_b(z)=\sigma_b(z)^{136}x_b(z)^2P_{21}(x_b(z)^3;b),
\qquad U_b(z)=z^6+O(z^{12}).
\tag{1}
$$
这里 P21 是 R466/R469 的同一个固定多项式；在 b=1 时为
$$
\begin{aligned}
P_{21}(X;1)={}&(X+1)(X^2+20X-8)(7X^2-4X+16)\\
&\cdot(X^4+40X^3+2112X^2+3136X+1792)\\
&\cdot(13X^4+52X^3+1536X^2+1024X+256)\\
&\cdot(X^8+1232X^7-58688X^6-49408X^5-439040X^4\\
&\hspace{12mm}-2111488X^3-1949696X^2-851968X-32768)/91 .
\end{aligned}
\tag{2}
$$
每个因子按其总次数齐次化恢复 b。因此 U_b=b^-1 U_1(b^{1/6}z)。
下文 U=U17 正是 R702/R734 的 Snew，未附额外52/3或另外的二倍尺度。

其原曲线为
$$
E_D:y^2=x^3+D,\qquad D=2312=8\cdot17^2.
$$
若 u_D=136^{1/6}，R469 的目标来源及相容周期准确是
$$
F_D(z)=136^{-1}U_{17}(u_Dz),\qquad
\Omega_{p,D}=u_D^{-1}\Omega,\qquad
\nu_{D,p}=136^{-1}\nu_U .
\tag{3}
$$
所以这条曲线的原 ordinary 中央零，等价于本篇使用的 JU 中央零。
该等价只涉及所示非零尺度；没有从一个其他 degree136 来源的质量零认出此曲线。

用
$$
f_w(x)=1_{x\in\mathcal O^\times}\langle x\rangle^{d_pw},
\quad d_p=p-1,\qquad
J_F(w)=\int f_w(x)\,d\nu_F(x).
\tag{4}
$$
这里 J_U(0)=J_S(0)=J_T(0)=0，三原失败假设为
$$
J_S'(0)=J_T'(0)=J_U'(0)=0.
\tag{5}
$$
R469 的 Iwasawa 参数 T 与 (4) 由
T=(1+p)^{d_pw}-1 连接，其导数乘 d_p log(1+p)；
故 (5) 确为原完整第三中央，而非另一个 Mellin 方向。

## 2. 同一六变量、三个态和最终测试

使用原输入 (ξ1,ξ2,ξ3,x,c,d)。置
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad N\in4\mathbf Z_{>0}.
\tag{6}
$$
所有旧射线、固定坏集、整逆和 p>163 保持。记
$$
\begin{aligned}
A&=\delta\xi_1+2\delta\xi_2+(3+\omega)\xi_3+(2-\omega)x,\\
Y&=A+c+2d,\qquad W=A+3\delta c+4d,\\
E&=E_{YW}=(5+6\omega)A-29c-(58+87\omega)d,\qquad
\mathcal E_N=\{E\in p^N\}.
\end{aligned}
\tag{7}
$$
最终测试始终是 R734(19) 的同一个 q=q_N*，不再重新适配。

从原 e0=−νσ^⊠6/84 出发，令 ft 为 W 方向 E[4] 的完整 canonical 平移。原三态是
$$
e_1=\frac14\sum_{\tau\in E[4]}f_\tau
       -\frac12\sum_{\tau\in E[2]}f_\tau,\qquad
e_2=-\frac14\sum_{\tau\in E[4]}f_\tau,\qquad h=e_1+e_2.
\tag{8}
$$
所有中心和半特征沿 R465/R692。W 的真实 normalized 核 K 满足
$$
Ke_0=e_1,\qquad Ke_1=e_0,\qquad
Ke_2=-e_0-e_1-e_2,\qquad Kh=-h .
\tag{9}
$$
(8)—(9) 是整来源身份，保原全部五伙伴，不是边际矩阵。

也可统一施加 R767 的纯 C 六角平均。它与 Y、W、E及q相容，并与 K 交换；以下所有式同时用于这个原平均。本文不把一个未平均单支偷换成平均支。

R734 所保的 R702/R715 完整 E 深表是
$$
\boxed{
\begin{aligned}
Y_*(1_{\mathcal E_N}q e_0)&=\lambda^{2N}\nu_S,\\
Y_*(1_{\mathcal E_N}q e_1)&=\lambda^{2N}
       \left(\frac{\omega^2}{2}\nu_S+[1/2]_*\nu_U\right),\\
Y_*(1_{\mathcal E_N}q e_2)&=\lambda^{2N}
       \left(\frac{\omega^2}{2}\nu_S-[1/2]_*\nu_U\right),\\
W_*(1_{\mathcal E_N}q(e_0,e_1,e_2))
 &=\lambda^{2N}6\delta(\nu_T,\nu_T,-\nu_T).
\end{aligned}}
\tag{10}
$$
其中第一2Y的原目标是
ω²S(2z)/2+U(z)，所以换成物理Y后确为 [1/2]U。
这不是 R692 未附 E 门的 CM 投影质量52/3；两个来源规范不可混用。

### 2.1 G 和 HV 的准确含义

原 π4=(Y,W,W′,G) 中
$$
H_1=B+2\xi_2,\qquad
F=s-B+\omega^2\xi_2+(2+3\omega)d,\qquad
G=13H_1+(3-2\omega)F .
$$
由 R773 的 N(H1)=7、N(F)=13、〈F,H1〉=−(5+2ω)，得
$$
N(G)=13^2\cdot7+19\cdot13-2\cdot13\cdot19=936.
\tag{11}
$$
G 是原隐藏伙伴，不是 U136 的第一观察。

R737 的 HaV 则是 V 深核返回后的实际条件积分，来源为 e1、观察为 zV/yV，并带全部移动斜门。它不是 JU，也不能从其名称认成第三中央。第三来源的无条件入口是完整表 (10)，或 R483 保全部CM纤维的真投影行。

## 3. R777 第二态中的真实第三来源

令
$$
c_B=1-\omega^2,\qquad
B_0=\frac{e_0-\omega h}{c_B},\qquad B_1=K B_0 .
\tag{12}
$$
B0 就是 R777 的 eB；若使用纯 C 平均，则把两态同时平均。
置 v=(e1−e2)/2。由 (9)、
1/2+ω=δ/2，有整来源恒等式
$$
\boxed{B_1=\frac{e_1+\omega h}{c_B}
             =\frac{v+\delta h/2}{c_B}.}
\tag{13}
$$
这一步不假定 v 的单P或单t核心；quarter格仍是 (8)。

直接把 (10) 代入 (12)—(13)，得到
$$
\boxed{
\begin{aligned}
Y_*(1_{\mathcal E_N}q B_0)&=0,\\
Y_*(1_{\mathcal E_N}q B_1)
 &=\frac{\lambda^{2N}}{c_B}
      \left([1/2]_*\nu_U+\frac{\delta\omega^2}{2}\nu_S\right),\\
W_*(1_{\mathcal E_N}q B_0)
 =W_*(1_{\mathcal E_N}q B_1)
 &=\frac{\lambda^{2N}6\delta}{c_B}\nu_T .
\end{aligned}}
\tag{14}
$$
因此第三算术行确实跨入 R777 的 W 核第二态，而非仍留在一个与 B 无关的来源池。

为保全部质量和scale，写
$$
A_i(w)=\int_{\mathcal E_N}f_w(Y)q\,dB_i,\qquad
C_i(w)=\int_{\mathcal E_N}f_w(W)q\,dB_i .
$$
完整 Mellin 等式是
$$
\boxed{
A_0(w)=0,\qquad
A_1(w)=\frac{\lambda^{2N}}{c_B}
 \left(\langle2\rangle^{-d_pw}J_U(w)
                      +\frac{\delta\omega^2}{2}J_S(w)\right),
\quad
C_0(w)=C_1(w)=\frac{\lambda^{2N}6\delta}{c_B}J_T(w).
}
\tag{15}
$$
特别
$$
A_1'(0)=\frac{\lambda^{2N}}{c_B}
 \left(J_U'(0)+\frac{\delta\omega^2}{2}J_S'(0)
                 -d_p\log\langle2\rangle J_U(0)\right).
\tag{16}
$$
最后项是原尺度质量项；因原 JU(0)=0 才消失。

在 JS′=0 下，A1′=0准确等价于JU′=0，系数λ2N/cB非零。
故 (15) 的额外行不是只有 JT 的旧式：它明确读取第三中央。
同时 A0 是整函数零，不能从它给 B0 的其它观察或其它cut赋零。


### 3.1 E 浅的完整原来源仍在

令Ξ为R465未加权第二态的整个第一2Y来源。原π4返回给
$
Y_*(qB_1)=\frac{\beta^N}{c_B}([1/2]_*\nu_\Xi+\nu_S).
$
所以E浅来源准确为
$
\boxed{
Y_*(1_{\mathcal E_N^c}qB_1)
=\frac{\beta^N}{c_B}([1/2]_*\nu_\Xi+\nu_S)
-\frac{\lambda^{2N}}{c_B}
 \left([1/2]_*\nu_U+\frac{\delta\omega^2}{2}\nu_S\right).
}
\tag{16a}
$
其中Ξ的全部rank0参考和外谱保留。该式没有被三原中央同时零消去。
同一E浅下B0的Y来源仍为零，两个W来源均为
(βN−λ2N)6δT/cB；这些是完整表的相减，不授权另外删除mixed cuts。

## 4. 搬回 B 第一态的真实 W 深支

对实际行 L 写
$$
P_{L,z}=I+\frac{z-1}{N(L)}\bar L^{\,t}L .
$$
q和E均与W正交，R777 的完整W两态核给
$$
(qB_i)|_{W\in p^m}
=\lambda^m(P_{W,\kappa^m})_*(qB_{i+m\bmod2}),
\qquad m\ge0 .
\tag{17}
$$
E 门逐点不动。定义原受限域上的准确逆观察
$$
Y^{[-m]}=Y\circ P_{W,\kappa^{-m}}.
$$
它只在 W∈p^m 的整像上使用。令
$$
\alpha=17-3\omega,\qquad
V_Y=36Y-\alpha W .
$$
因〈Y,W〉=2α，显示式为
$$
\boxed{
Y^{[-m]}
 =Y+\frac{\alpha}{36}(\kappa^{-m}-1)W
 =\frac{V_Y+\alpha\kappa^{-m}W}{36}.
}
\tag{18}
$$
VY 是 R692/R737 的旧 W 伙伴，与下一节的 Vt 不同。

完整第三返回于是为
$$
\boxed{
\begin{aligned}
&\int_{\mathcal E_N,\ W\in p^m}
       f_w(Y^{[-m]})q\,dB_0\\
&\quad=
\begin{cases}
0,&m\text{ 偶},\\[1mm]
\displaystyle\frac{\lambda^{m+2N}}{c_B}
 \left(\langle2\rangle^{-d_pw}J_U(w)
                  +\frac{\delta\omega^2}{2}J_S(w)\right),&m\text{ 奇}.
\end{cases}
\end{aligned}}
\tag{19}
$$
特别m=1已给一个真正新的有限门中央式。
其unit条件是 Y^{[-m]}-unit，不是原Y-unit、W-unit或P-unit。
由于使用完整逆观察，(19)没有未记的κ/p尺度；若另改观察，必须重新运输全部unit cut及相应log质量。

在三原假设 (5) 下，(19)的完整中央导数为零。
这不把W深域内的某个环带或交域各自置零。

## 5. 进入 R777 真正的 W 近相消支

使用 R777 的原
$$
a=1+3\omega,\quad N(a)=7,\qquad
P=A_0+(2+3\omega)s+4d,\qquad t=r-c ,
$$
$$
W=P-at,\qquad V_t=\bar aP+29t,\qquad
P\perp t,\quad N(P)=58,\quad N(t)=2 .
\tag{20}
$$
W、Vt正交；全部反变换为
$$
P=\frac{29W+aV_t}{36},\qquad
t=\frac{V_t-\bar aW}{36}.
\tag{21}
$$
因此在W深、Vt单位时，P和t都准确为单位。
这正是R777的P/t单位平面内W近相消部分，不是另造同范数轴。

R778 已定 P 核为β。R777 的W/Vt两态核及共同深身份因此为
$$
(qB_i)|_{W,V_t\in p}
=\lambda^2(P_{\rm pl})_*(qB_i),\qquad
P_{\rm pl}=P_{W,\kappa}P_{V_t,\kappa}
           =P_{P,\kappa}P_{t,\kappa}.
\tag{22}
$$
(22)在B1上只使用已付的整个共同核，不宣称其单P/t核心与B0相同。

取m=1。将(19)的整个W深域精确分成Vt-unit及Vt-deep，得
$$
\boxed{
\begin{aligned}
\mathcal A_{\rm near}(w)
 &:=
 \int_{\mathcal E_N,\ W\in p,\ V_t\ {\rm unit}}
         f_w(Y^{[-1]})q\,dB_0\\
 &=\lambda A_1(w)-\lambda^2\mathcal B_{\rm sh}(w),\\
\mathcal B_{\rm sh}(w)
 &:=
 \int 1_{E\circ P_{\rm pl}\in p^N}
       f_w(Y\circ P_{V_t,\kappa})q\,dB_0 .
\end{aligned}}
\tag{23}
$$
因为 PW与PVt正交，
Y^{[-1]}∘Ppl=Y∘PVt,κ。这支付了第二项的完整观察，而非只返回来源。

为使移动门不含省略，令
$$
h_0=17+3\omega,\qquad
Y_\perp=Y-\frac{\alpha}{29}P,\qquad
E_\perp^{P,t}=E-\frac{h_0}{29}V_t .
\tag{24}
$$
两条带垂标的行均正交于P,t；
第二式由E⊥W和〈E,t〉=2h0直接得到。
于是(23)的实际两行是
$$
\boxed{
\begin{aligned}
E\circ P_{\rm pl}
 &=E_\perp^{P,t}+\frac{h_0\kappa}{29}V_t,\\
Y\circ P_{V_t,\kappa}
 &=Y_\perp+\frac{\alpha}{36}W
                  +\frac{\alpha a\kappa}{1044}V_t .
\end{aligned}}
\tag{25}
$$
1044=36·29。它们不能被改回旧E和Y。

特别在(5)下，完整式只是
$$
\mathcal A_{\rm near}'(0)=-\lambda^2\mathcal B_{\rm sh}'(0).
\tag{26}
$$
两个局部质量也只满足
$
\mathcal A_{\rm near}(0)=-\lambda^2\mathcal B_{\rm sh}(0),
$
不能各自删掉。
如果把(25)中的unit观察提出一个常数，必须保该常数的log乘实际局部质量。
本文始终直接使用完整f_w，已自动保这些项。

## 6. 与 R773 共同帽域的准确有限交集

写
$$
\hat s=s-Y/17,\qquad \hat d=d-Y/17,\qquad
U_{\rm fail}=\hat s/2-3\hat d,
$$
$$
\mathcal D^\infty_{n,N}
=\{Y\ {\rm unit},\ \hat s,\hat d\in p^N,\
                        U_{\rm fail}\notin p^n\}.
\tag{27}
$$
此处Ufail是原失败轴，不是曲线来源U136。
R773 已证明D∞上E∈pN，而且
$$
P=b_YY+(1+3\omega)\hat s+2\hat d,\qquad
b_Y=(20+3\omega)/17
$$
为单位。因此对m≥1，
$$
\boxed{
\mathcal D^\infty_{n,N}\cap\{W\in p^m\}
\subset\mathcal E_N\cap
 \{P,t,V_t\ {\rm unit},\,W\in p^m\}.
}
\tag{28}
$$
这是(23)真实近相消支中的一个原共同帽子域。

但它的逆返回不保帽门。由原Gram系数，令 $z=\kappa^m$，有
$$
\boxed{
\begin{aligned}
Y\circ P_{W,z}&=Y+\frac{\alpha}{36}(z-1)W,\\
\hat s\circ P_{W,z}
 &=\hat s-\frac{17+24\omega}{306}(z-1)W,\\
\hat d\circ P_{W,z}
 &=\hat d+\frac{17+3\omega}{612}(z-1)W,\\
U_{\rm fail}\circ P_{W,z}
 &=U_{\rm fail}-\frac{68+33\omega}{612}(z-1)W .
\end{aligned}}
\tag{29}
$$
例如〈hat s,W〉=−4(17+24ω)/17、
〈hat d,W〉=2(17+3ω)/17；除N(W)=72给显示系数。

对奇m，(17)从而给
$$
\boxed{
\int_{\mathcal D^\infty_{n,N},\,W\in p^m}
 f_w(Y^{[-m]})q\,dB_0
 =\lambda^m\int_{\mathcal D^\infty_{n,N}\circ P_{W,\kappa^m}}
 f_w(Y)q\,dB_1 .
}
\tag{30}
$$
右边须同时保(29)第一行unit，以及f_w(Y)自己的Y-unit；
这两个unit条件不能相认。偶m将B1换回B0。

(19)减去(30)，给其余整个
E深∩W深∖D∞补域，且观察仍是同一个Y[-m]。
因此第三中央进入共同帽时，精确给“(30)+该补域”的零。
未再附帽门的整行(19)已经是新约束；不能由它或R773的条件正矩
单独删掉补域。

## 7. 已付的新算术信息与尚余的实际关系

第三曲线确实经过当前原六变量池：它在原W-quarter态中，
而且R734保的同一E深适配使它成为(14)的完整第一来源。
这里没有新增中央假设、测试或辅助曲线。

相对于R777只有βN JT的P/t边际，(15)、(19)支付了独立的原JU观察。
在JS′=0时，其导数零与JU′=0等价。
它使用Y及E；这两者不能从P/t二维边际恢复。
因此原仅P/t分区不会自动看到它，但原完整六变量来源确实携带它。

与R777四-unit余域或R773共同帽的下一比较，应使用
(23)—(30)的真实域、Y[-m]观察和第二态，连同原T行。
这些式子没有使四-unit行、shadow项或帽补域分别为零。
当前主目标仍未由本文关闭。

## 依赖与证明范围

- [R469](R469-e2312-full-weight-square-ordinary-inert-sha-bridges.md)：U136的全角色、周期及第三原中央桥。
- [R465](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)、[R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)：原完整quarter、三态及真实W核。
- [R702](R702-forty-five-neutral-tests-and-complete-three-state-arithmetic-gate.md)、[R715](R715-complete-first-z-source-and-fifty-neutral-returns.md)、[R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：同一实际q的完整E深三态表及原混次归一。
- [R737](R737-common-depth-elimination-and-native-primitive-strips.md)：HV的实际移动门与观察范围。
- [R773](R773-native-common-hat-domain-and-five-conditional-moment-return.md)：共同帽域、E深性质及原失败轴。
- [R777](R777-original-b-sector-p-t-core-and-complete-central-renewal.md)、[R778](R778-original-degree174-full-characters-and-unramified-seventeen-point-fields.md)：同B两态、P/t与W/Vt完整共同核及P的绝对符号。

本文是既有完整来源、显示Gram系数及有限域恒等式的直接代数推导，
没有新增数值执行、素数扫描或生成数据。
