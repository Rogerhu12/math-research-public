# R548 — 原第三支的整来源 CM 反射、完整正谱与同一混合补域

日期：2026-11-14。**状态：已证明。**

本篇保留 R541/R544 的同一个原六输入与 R546 的全部五伴随。
原第三来源 $\eta$ 的二挠平均准确等于 $-\rho _0/2$；一个固定的
norm13 九次完整 CM 对应在整个来源上准确实现原输入 $c$ 的反射。
因此原 $S$ 块的五伴随也准确为原来源伴随的 $-1/2$，不只是质量相同。

除去这一块后，剩余 principal 来源恰有十七条共同谱线。
五条已有算术身份的线和十二条外谱全部给出真实五变量卷积单位，
不删去参考导数或外谱。R544 唯一的 $\eta$ 测试差随后精确改写成
这个完整正来源对一个实际反对称测试的积分；所有混合单位域、原
测试 $q$、CM 纤维中心和唯一余域仍保留。

## 1. 规范及同一完整六轴

沿用 R541、R544、R546 的
$$
\omega^2+\omega+1=0,\qquad \delta=1+2\omega,\qquad
\gamma=3+\omega,\qquad \gamma_{13}=4+\omega,\qquad b=17,
$$
$$
\lambda=-\bar\pi _0^{-1},\qquad \beta=-\lambda,\qquad
\kappa=p\lambda^2,\qquad d=p-1.
\tag{1}
$$
当前普通射线及固定坏集全部保持，特别 $p\ge71$。
原六输入为 $(\xi _1,\xi _2,\xi _3,x,c,d_0)$，来源和两个观察为
$$
\rho _0=-\frac1{84}\nu_\sigma^{\otimes6},\qquad
A=\delta\xi _1+2\delta\xi _2+\gamma\xi _3+\bar\gamma x,
$$
$$
Y_s=A+c+2d_0,\qquad W=A+3\delta c+4d_0.
\tag{2}
$$
$Y_{s*}\rho _0=S$，$W_*\rho _0=6\delta T$，常数不改变。

$H$ 固定前四个输入，在后两输入上是
$$
H=\frac12
\begin{pmatrix}
-1-\omega&-1-2\omega\\
2+\omega&-1-\omega
\end{pmatrix},
\qquad \eta=\omega^2H_*\rho _0 .
\tag{3}
$$
令 $R_c$ 只反射原 $c$。R544 的完整两态身份给
$$
(R_c)_*\rho _0=-\rho _0,\qquad
(R_c)_*\eta=\eta+\rho _0.
\tag{4}
$$

使用同一个整框架
$$
\begin{aligned}
L&=(2Y_s,2Q_s,2U_s,R_1,R_2,R_3),\\
Q_s&=A-29c,\qquad U_s=A+c-15d_0,\\
R_1&=4t_1-t_2,\qquad R_2=7(t_1+t_2)-15t_3,\\
R_3&=7(t_1+t_2+t_3)-22t_4,
\end{aligned}
\quad
(t_1,t_2,t_3,t_4)=(\delta\xi _1,2\delta\xi _2,\gamma\xi _3,\bar\gamma x).
\tag{5}
$$
以下第一物理坐标为 $Y=2Y_s$，五伴随为
$\mathbf Z=(Z_1,\ldots,Z_5)$。当不致混淆时，同样以 $\rho _0,\eta$
记它们在该框架中的完整推前。R546 §1 已付
$$
\mathcal S_{136}\otimes\mathcal S_{3480}\otimes
\mathcal S_{1020}\otimes\mathcal S_{60}\otimes
\mathcal S_{2310}\otimes\mathcal S_{4466}
\tag{6}
$$
中的完整张量身份、整性、所有半特征与零 Gaussian 交叉项。
本文的操作始终在 (6) 中进行。

## 2. 二挠平均的完整来源身份

在第一 $Y$ 轴定义 canonical 平移平均
$$
P_{2,Y}=\frac14\sum_{t\in E[2]}\mathsf T^{(136)}_{Y,t},
\qquad B_{2,Y}=2P_{2,Y}-I.
\tag{7}
$$

**定理 1。** 在保留五个伴随变量的完整张量格内，
$$
\boxed{
P_{2,Y}\rho _0=\rho _0,\qquad
P_{2,Y}\eta=-\frac12\rho _0.
}
\tag{8}
$$
从而
$$
\boxed{
B_{2,Y}\rho _0=\rho _0,\qquad
B_{2,Y}\eta=-\eta-\rho _0.
}
\tag{9}
$$

**证明。** 第一生成变量平移 $t\in E[2]$ 时，前四个原 sigma
分别平移 $2\delta t,4\delta t,2\gamma t,2\bar\gamma t$。
它们都是全周期平移，留下的半特征乘积为
$$
\epsilon(t)=\chi_\sigma(2t)=
\begin{cases}1&t=0,\\-1&t\ne0.\end{cases}
\tag{10}
$$
确切地，$\delta,\gamma,\bar\gamma$ 模二非零，$2\delta$ 模二为零；
三个非零因子保留一个标准奇半特征。这个计算包含全周期 lift，
没有只按点的置换计算。

后两输入共同作 $[2]$ 后属于 $\mathcal S_4\otimes\mathcal S_4$。
若该共同覆盖的生成变量为 $(u,v)$，上面的第一轴平移正好是
$(u,v)\mapsto(u+t,v+2t)$。第二变量的 $2t$ 是 degree4 的整周期，
其 canonical lift 为恒等。第一变量的四个完整 lift，在
Schrödinger 基 $e_j,\ j\in\mathbb Z/4\mathbb Z$ 中为
$$
\mathsf T^{(4)}_{(s+r\omega)/2}e_j
=(-1)^{s(j+r)}e_{j+2r}\qquad(s,r\in\{0,1\}).
\tag{11}
$$
因此逐列恰有
$$
\frac14\sum_{s,r}\epsilon((s+r\omega)/2)
\mathsf T^{(4)}_{(s+r\omega)/2}
=\frac{I-R}{2},\qquad Re_j=e_{-j}.
\tag{12}
$$
右边是完整 $\mathcal S_4$ 的奇线投影；不是省略中心后的有限点平均。
该 $R$ 在原来源上就是 $R_c$。结合 (10) 与 (12)，
$P_{2,Y}\eta=(I-(R_c)_*)\eta/2=-\rho _0/2$。
对 $\rho _0$，后两原 sigma 的半特征乘积也为 $\epsilon(t)$，
与 (10) 相乘为一，故四个第一轴平移逐个固定 $\rho _0$。

(6) 中所有 Gaussian 交叉项为零，以上全周期相位正是完整张量
lift 的乘积；五伴随没有被取零、积分或限制。因此证明的是 (8)
的六变量等式。测度身份由同一整 Amice 对应得到。证毕。

## 3. 固定 norm13 九次对应的绝对标量

仍使用固定规范 $N_a=\mathscr M_a/a$，并以 $N_{13}$ 表示
$a=\gamma_{13}$ 的实际 CM 对应。

在 degree136 的 canonical 基中，(7) 的整个算子为
$$
B_{2,Y}e_j=(-1)^j e_{69j+68},\qquad j\pmod {136}.
\tag{13}
$$
故其完整 Heisenberg 交织为
$$
X\longmapsto-X^{69},\qquad Z\longmapsto-Z^{69}.
\tag{14}
$$
这里两处负号均保留。相应 CM 数为 $69+136\omega$ 模 $272$。

当前普通比值及固定 norm13 比值为
$$
g_p=\pi_0/\bar\pi_0\equiv203+136\omega\pmod {272},
\qquad
g_{13}=\gamma_{13}/\bar\gamma_{13}
\equiv43+147\omega\pmod {272}.
\tag{15}
$$
准确有
$$
g_{13}^9\equiv205+136\omega
\equiv137(69+136\omega)\pmod {272}.
\tag{16}
$$
不能把 (16) 误写成 $203+136\omega$。中心因子 $137=1+136$
在完整 Weyl 算子上为恒等：
$$
\frac{137^2-1}{136}=138\equiv0\pmod2.
\tag{17}
$$
因此 $N_{13}^9$ 与 $B_{2,Y}$ 具有相同的完整 Heisenberg 交织。

取真实非零锚 $S_2(z)=S(2z)$。它在 (7) 下固定，且已付的
principal CM 身份 $N_{13}=N_7^5$ 与 $N_7S_2=-S_2$ 给
$N_{13}^9S_2=-S_2$。不可约 Heisenberg 表示于是确定绝对标量：
$$
\boxed{N_{13,Y}^9=-B_{2,Y}\quad\hbox{于整个 }\mathcal S_{136}.}
\tag{18}
$$
它不限于 principal 空间。

类似地，$R_YB_{2,Y}$ 的完整交织为 (15) 的 $g_p$，
其中 $R_Y$ 是保持五伴随、反射第一轴的实际几何反射。
同一锚的普通核心为 $+1$，所以
$$
\boxed{K_{136}=R_YB_{2,Y}.}
\tag{19}
$$
外部测度标量仍为 $\lambda$。

R546 的六轴同时 CM 身份 (10) 与全空间逆 (11)，在加入
principal 投影以前已经成立。因此定义只作用于旧五伴随的
$$
B_{13}=\prod_{\ell=1}^5N_{\bar\gamma_{13},Z_\ell},
\qquad \mathcal B=B_{13}^{\,9},
\tag{20}
$$
对 $\rho=\rho _0,\eta$ 有整个来源身份
$N_{13,Y}^9\rho=\mathcal B\rho$。结合 (4)、(9)、(18) 得
$$
\boxed{
\mathcal B\rho _0=-\rho _0=(R_c)_*\rho _0,\qquad
\mathcal B\eta=\eta+\rho _0=(R_c)_*\eta.
}
\tag{21}
$$
(21) 用固定的完整 norm13 九次伴随对应实现了一个实际混 $Y$ 的
原输入反射。它不是逐支的几何映射身份；有限 CM 和式中的每个
torsion 纤维仍须保留。

## 4. 完整正来源与原 S 伴随的精确关系

置
$$
\boxed{h=\eta+\frac12\rho _0.}
\tag{22}
$$
则整来源上
$$
\boxed{
P_{2,Y}h=0,\qquad \mathcal Bh=h,\qquad(R_c)_*h=h.
}
\tag{23}
$$
第三支的整个负块为 $-\rho _0/2$，包括其所有第一角型和五伴随。

特别，若 R483/R546 的原 $S_2$ 秩一投影写成
$$
\mathcal C_S\rho _0=S_2\otimes A_0,\qquad
\mathcal C_S\eta=S_2\otimes A_\eta,
$$
由于 $S_2$ 在 $P_{2,Y}$ 的像中，(8) 给
$$
\boxed{A_\eta=-A_0/2}
\tag{24}
$$
作为完整五变量整测度；并非只有 $A_\eta(0)=-1/2$。

(19) 同时给
$$
K_Y\rho _0=(R_Y)_*\rho _0,\qquad
K_Y\eta=-(R_Y)_*(\eta+\rho _0),\qquad
\boxed{K_Yh=-(R_Y)_*h.}
\tag{25}
$$
$R_Y$ 不能在未投影联合中删去。实际深度身份例如为
$$
h|_{Y\in p\mathbb Z_p}
=-\lambda(P_{Y,\kappa}R_Y)_*h,
\tag{26}
$$
其中 $P_{Y,\kappa}$ 只缩放 $Y$、保五伴随。

令 $\Pi_{r,Y}$ 是第一 $\mu_6$ 型 $r$ 的完整投影，$h_r=\Pi_{r,Y}h$。
因为 $R_Y$ 在型 $r$ 为 $(-1)^r$，(26) 逐块为
$$
h_r|_{Y\in p\mathbb Z_p}
=-(-1)^r\lambda(P_{Y,\kappa})_*h_r.
\tag{27}
$$
$\mathcal S_{136}$ 的六个型维数为 $(23,23,23,22,23,22)$；
$P_{2,Y}$ 的像是 $[2]^*\mathcal S_{34}$，六个维数为
$(6,6,6,5,6,5)$。所以 $\ker P_{2,Y}$ 在每个型都准确有
十七维，总计一百零二维。五个非 principal 型不能因 (24)
或原中央使用 principal 权而在混合测试中删除。

## 5. 正 principal 来源的全部十七条张量线

在第一 principal 空间写
$$
M=N_7,\qquad D=\omega^{-1}N_{19}M^{-2}.
\tag{28}
$$
R466/R483 给 $M^{18}=I,D^2=I$ 及绝对的
$N_{13}=M^5,\ M=N_{13}^{11}$。$h_0=\Pi_{0,Y}h$ 的第一系数空间
包含其真实第一边际的完整共同 $(M,D)$ 循环空间。R542 的全二十三
坐标证书表明，后者在 (22) 后准确是十七维：
$D=+$ 九维、$D=-$ 八维。

另一方面，(23) 将该第一系数空间包含在十七维的
$(\ker P_{2,Y})_{\mu_6=0}$ 中。由 (20) 及 norm19 的同样完整伴随
转移，该空间在 $N_{13},N_{19}$ 下稳定，因而在 $M,D$ 下稳定。
上下界相同，故它就是这整个十七维空间。共同谱逐线单重，
因此每条投影不是仅有一个非零边际，而有真实张量分离。

五条已有算术身份的线如下。$H_k$ 取 R466 的固定质量一规范，
$S_{\rm new}$ 取首项 $z^6$ 系数一的原 $E_{2312}$ 规范。

|第一来源|$M$|$D$|五伴随质量|
|---|---|---|---|
|$H_1$，$E_{-136}$|$1$|$+$|$-\delta/(9072b)$|
|$H_3$，$E_{-39304}$|$\omega$|$+$|$(3-\delta)/(9072b)$|
|$H_5$，$E_{-11358856}$|$\omega^2$|$+$|$(-3-\delta)/(9072b)$|
|$H_4=H_{\rm ref}$，$E_{668168}$|$1$|$-$|$-1/(1008b)$|
|$S_{\rm new}$，$E_{2312}$|$\omega^2$|$-$|$26(1-\delta)/3$|

其余十二条以 $\varepsilon=D\in\{+,-\}$、
$\tau\in\{\omega,\omega^2\}$、$\theta^3=\tau$ 标记。
令 $m_j$ 是相应完整三维块第一边际经 $M^j$ 后的质量，
$j=0,1,2$。R542 的准确数值为

|$\varepsilon,\tau$|$6048b\,m_0$|$6048b\,m_1$|$6048b\,m_2$|
|---|---|---|---|
|$+,\omega$|$-3+\delta$|$6+2\delta$|$-2\delta$|
|$+,\omega^2$|$3+\delta$|$3-\delta$|$-2\delta$|
|$-,\omega$|$3+3\delta$|$0$|$-6$|
|$-,\omega^2$|$3-3\delta$|$-3-3\delta$|$-6$|

每条单根线的质量准确为
$$
m_{\varepsilon,\theta}
=\frac13(m_0+\theta^{-1}m_1+\theta^{-2}m_2).
\tag{29}
$$
在固定的六次域 $\mathbb Q(\delta,\theta)$ 中，其全局范数为
$$
\boxed{
N_{\mathbb Q(\delta,\theta)/\mathbb Q}(m_{\varepsilon,\theta})
=
\begin{cases}
(b^6\,2^{24}3^{21}7^6)^{-1}&\varepsilon=+,\\
(b^6\,2^{24}3^{18}7^6)^{-1}&\varepsilon=-.
\end{cases}}
\tag{30}
$$
附证书以 $\theta^3=\tau$ 的准确三维乘法矩阵计算 (30)。
分子均为一；所以十二条质量在当前普通射线全部是单位，不需要
另删一个未显示的大素数。

把每条外谱第一来源除以 (29)，记所得固定质量一来源为
$V_{\varepsilon,\theta}$。它们是实际整 theta 来源，本篇没有给它们
新增椭圆曲线身份或中央零。完整分解为
$$
\boxed{
h_0=S_{\rm new}\otimes\Lambda_{\rm new}
+\sum_{k\in\{1,3,5,4\}}H_k\otimes\Lambda_k
+\sum_{\varepsilon,\tau,\theta^3=\tau}
V_{\varepsilon,\theta}\otimes\Lambda_{\varepsilon,\theta}.
}
\tag{31}
$$
这里每条 $\Lambda$ 是不同的真实五变量来源；不能用它们的质量
把它们认成同一伴随。质量分别由上表和 (29) 给出。

所有投影都由完整 prime-to-$p$ trace、根单位以及分母 $2,3,18$
组成，因而保持整测度。对于质量一的第一来源，取第一轴质量即可
读取整的 $\Lambda$；对 $S_{\rm new}$ 取第六矩并除以
$720\Omega^6$，当前 $p\ge71$ 使分母为单位。因此 (31) 中全部
十七个 $\Lambda$ 都属于 $\mathcal O[[\mathbb Z_p^5]]$，并由其
单位质量知它们都是完整 Amice 卷积单位。

(31) 加上 (24) 是原第三支 principal 部分的全谱分解。
参考导数和十二条外谱的中央仍未知；原 $S,S_{\rm new}$ 中央零
只控制相应已识别算术行。特别不能用 (30) 的非零质量代替这些
导数，或从有限维分解推出目标中央非零。

## 6. 同一正来源上的完整 Q 单位逆

R551 的两个原 Norm5 轴
$$
R=c+2d_0,\qquad Q=2c-d_0
\tag{32}
$$
在 $(\rho _0,\eta)$ 上的完整核心为
$\chi_{65}\lambda\mathsf B$，$\mathsf B=-(R_c)_*$。
故令 $\chi=\chi_{65}$，(23) 直接给
$$
\boxed{h|_{Q\in p\mathbb Z_p}
=-\chi\lambda(P_{Q,\kappa})_*h.}
\tag{33}
$$
同一框架中
$$
\boxed{Q=(Z_2-Z_1)/30.}
\tag{34}
$$
因此 $Q$ 真正保持第一 $Y$，并属于原五伴随，而不是新加的第七输入。
它的完整普通对应与第一轴的 CM 及角投影交换；这可在 (6) 的
独立第一轴上逐个互素纤维重排。因此 (33) 对所有 $h_r$ 保留，
在 (31) 中成为每个 $\Lambda$ 的同一个 $Q$ 核
$-\chi\lambda$。每条 $\Lambda$ 的 $Q$ 单位限制质量为
$(1+\chi\lambda)\Lambda(1)$，仍为单位。

为明确作用于任意连续混合测试的逆，设
$$
\mathcal S_Qg=g\circ P_{Q,\kappa},\qquad
\mathcal E_Qg=g\circ P_{Q,0}.
$$
R410 的分母单位与 R551 的全连续逆给
$$
\boxed{
\mathcal U_hg=
\frac{\mathcal E_Qg}{1+\chi\lambda}
+\sum_{n\ge0}(-\chi\lambda)^n
\mathcal S_Q^n(g-\mathcal E_Qg).
}
\tag{35}
$$
连续性使级数在测试空间一致收敛；$(35)$ 是
$(I+\chi\lambda\mathcal S_Q)^{-1}$，并且
$$
\boxed{\int_{Q\ {\rm unit}}\mathcal U_hg\,dh=\int g\,dh.}
\tag{36}
$$
$\mathcal U_h$ 与第一角投影交换。故 (36) 可以同时用于 (31) 的
全部十七条及其他五个完整角块，不需要逐谱增加新逆。

$Q$ 保 $Y$，却不保 $W$ 或后文的实际 $L_{\rm mix}$ 条件。
(35) 中每次真实缩放都作用于整个 $g$，包括 logarithm、$q$、
其他紧开限制及其参数依赖；不能只缩放一个多项式权。

## 7. R544 同一唯一余域的精确替换

回到未双倍的实际观察 $Y_s$。置
$$
\alpha=1+3\omega,\qquad L_{\rm mix}=\alpha c+d_0=(W-Y_s)/2.
$$
沿用 R544 的
$$
u_j=cH^{-j},\qquad P_j=P_{u_j,\kappa},\qquad j=0,1,2,
$$
及原 R536 的完整测试 $q$。定义同一个实际函数
$$
f=1_{L_{\rm mix}\ {\rm unit}}q
\left(1_{Y_s\ {\rm unit}}d\log\langle Y_s\rangle
-1_{W\ {\rm unit}}d\log\langle W\rangle\right),
\qquad \Phi_j=f\circ P_j.
\tag{37}
$$
所有 $q$ 的 $\lambda,\kappa$ 系数和既有 $\kappa^{-n}$ 权原样保留。
R544 三个不交环带之外的唯一实际余域是
$$
\mathcal V=\{L_{\rm mix},u_0,u_1,u_2\in\mathbb Z_p^\times\}.
\tag{38}
$$

为同时记录 R541 的另一真实支，设
$$
a=-3\omega/8,\qquad b_M=-(1+6\omega)/8,
$$
$$
Y_\kappa^G=A+\kappa a(\gamma c+d_0)+b_M(c-\bar\gamma d_0),
\qquad W_\kappa^G=Y_\kappa^G+2\kappa(\gamma c+d_0).
$$
这两观察具有同一单位域 $\mathcal U_\kappa$，并定义
$$
\mathcal J=\int_{\mathcal U_\kappa}
d\log(Y_\kappa^G/W_\kappa^G)\,(q\circ G)\,d\rho _0,
\tag{39}
$$
其中 $G$ 仍是 R541 的实际矩阵，不替成反射或标量缩放。

在原 $J'_S(0)=J'_T(0)=0$ 反证条件下，R544 的完整身份为
$$
\int_\mathcal V f\,d\rho _0
=\lambda\{\mathcal J-\rho _0(\Phi_1-\Phi_0)-\eta(\Phi_1-\Phi_2)\}.
$$
代入 (22)，精确变成
$$
\boxed{
\int_\mathcal V f\,d\rho _0
=\lambda\left\{
\mathcal J-\rho _0\!\left(\frac{\Phi_1+\Phi_2}{2}-\Phi_0\right)
-h(\Phi_1-\Phi_2)\right\}.
}
\tag{40}
$$
(40) 是同一旧域上的身份，没有把任何非零子管从补域中删除。

原两轴满足 $u_1R_c=\omega^2u_2$，单位倍不改变正交缩放，
因此 $P_2R_c=R_cP_1$。利用 (23) 的真实反射不变性，
$$
\boxed{
h(\Phi_1-\Phi_2)
=h\!\left((f-f\circ R_c)\circ P_1\right).
}
\tag{41}
$$
右边是先取原 $c$ 反对称测试、再作真实 $P_1$ 的积分。
$P_1$ 不与 $R_c$ 交换，故不能因 $h$ 在 $R_c$ 下为偶就把 (41)
置零。式 (35) 可进一步把 (41) 准确放在 $Q$ 单位域，所得仍是
整个测试的逐项转置。

## 8. 原五伴随 CM 分支上的确切矩阵顺序

为使 (41) 可直接代入完整纤维，记 $\mathcal R_c=LR_cL^{-1}$。
其首三维块准确为
$$
\mathcal R_c=
\begin{pmatrix}
16/17&1/15&-2/255\\
29/17&-14/15&58/255\\
-1/17&1/15&253/255
\end{pmatrix}\oplus I_3,
\tag{42}
$$
而 $LR_YL^{-1}=\operatorname{diag}(-1,1,1,1,1,1)$。
特别 $c=Y/68-Z_1/60+Z_2/510$，$d_0=(Y-Z_2)/34$。

写 $\mathcal A_j=LP_jL^{-1}=I+(\kappa-1)b_jq_j$。两个真实列/行是
$$
\begin{aligned}
b_1&=(3+\omega,\ 29+29\omega,\ -31-16\omega,\ 0,0,0)^t,\\
q_1&=((2-\omega)/136,\ -\omega/120,\
(-15+16\omega)/1020,\ 0,0,0),\\
b_2&=(-2-5\omega,\ 29\omega,\ 15+29\omega,\ 0,0,0)^t,\\
q_2&=((3+5\omega)/136,\ -(1+\omega)/120,\
(-14-29\omega)/1020,\ 0,0,0).
\end{aligned}
\tag{43}
$$
它们保留全部实际第一轴变化；没有把 $P_j$ 误写成只动伴随。

对固定 $a=\gamma_{13}^{\,9}$，(20) 的完整 CM 分支为
$$
\nu_{\mathcal B\rho}
=\bar a^{-5}[I_Y,\bar a^{-1}I_5]_*
\sum_{\mathbf t\in E[\bar a]^5}\nu_{\rho_{a,\mathbf t}},
\qquad \rho=\rho _0,\eta,h.
\tag{44}
$$
每个 $\rho_{a,\mathbf t}$ 使用 R546 (28) 的同一个 canonical
division lift，保五个 torsion 中心与生成变量的 $a$ 拉回。
令 $\mathcal D_a=\operatorname{diag}(1,\bar a^{-1}I_5)$。
则 (37) 的 $\Phi_j$ 在每条真实分支上必须读取为
$$
f(\mathcal A_j\mathcal D_a(Y,\mathbf Z)),
\tag{45}
$$
而 (41) 必须逐支读取为
$$
\boxed{
f(\mathcal A_1\mathcal D_a(Y,\mathbf Z))
-f(\mathcal R_c\mathcal A_1\mathcal D_a(Y,\mathbf Z)).
}
\tag{46}
$$
$\mathcal A_j$ 和 $\mathcal D_a$ 一般不交换。
式 (42)–(46) 同时运输旧 $Y_s,W,L_{\rm mix}$ 单位条件和全部 $q$；
不从只保持 $Y$ 的 (44) 推断混合切集已相同。

最后，对任意这样的完整测试 $g$，真正的全部角分解是
$$
h(g)=\sum_{r=0}^5 h_r(\Pi_{r,Y}^*g).
\tag{47}
$$
$r=0$ 项使用 (31) 的全部十七个不同张量；$r=1,\ldots,5$ 项各保留
其在相应十七维格中的完整实际来源，未宣称这些块的系数秩均为十七。
即使原 Mellin 权属于 principal，
先经过 $\mathcal A_j$ 或 (42) 后的实际测试也不能自动删除这五项。

## 9. 证书、已付范围与尚余条件

附脚本与 JSON 支付以下准确有限计算：

- 全部四个 degree4 半周期 lift 和加权奇投影 (11)–(12)；
- 全部一百三十六列的 (13)–(14)，包括中心负号；
- 模 $272$ 的完整 norm13 九次幂、中心因子 $137$ 及绝对锚；
- 六个完整角维数、(42)–(43) 的真实框架转置和 (34)；
- 四个三维外谱的准确根质量及 (30) 的全域范数。

脚本读取既有 R542 全坐标证书和完整 degree136 CM7 矩阵，
没有从有限 $p$ 样本判断谱或算术身份。相关有限计算已经在同一
精确有理/CM 算术中完成，不设置额外独立复跑门槛。

本篇新付的是整个 $\eta$ 负块、固定 CM 对应实现的完整反射、
全部正 principal 十七线及其五伴随单位、和同一唯一余域的
精确正来源测试 (40)–(46)。参考与外谱的中央导数、五个非
principal 角块、实际余域 $\mathcal V$ 均仍保留。要结束普通反证，
仍须把这些同一实际域中的项与原合格曲线的中央条件联立消去；
质量单位、有限谱或单个非零子管均没有完成这一步。

## 依赖与可复现文件

- [R541：原 degree8 第二态与第三 sigma 支](R541-original-degree8-second-state-and-exact-sigma-transport.md)。
- [R544：完整 S3 两态与三个实际环带](R544-original-s3-and-exact-mixed-unit-complement.md)。
- [R542：第三支全部第一边际谱](R542-original-third-sigma-arithmetic-projections-and-affine-core.md)。
- [R546：完整五伴随 CM 转移](R546-original-third-sigma-full-five-companion-cm-transfer.md)。
- [R551：Norm5 两态完整核心及连续单位逆](R551-original-norm5-two-state-core-and-complete-unit-inverse.md)。
- [精确证书脚本](../scripts/check-r548-whole-third-source-cm-reflection.js)。
- [证书输出](../scripts/check-r548-whole-third-source-cm-reflection.json)。
