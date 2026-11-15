# R796 — 全六变量半周期身份与原 E 深门的一阶混合消去

日期：2026-11-15。**状态：以下完整来源、首矩零与补域身份已证明。**

本篇保持 R734 的原测试 $q=q_N^*$，不更改任何列或目标。
R702 的 W/Y 半周期关系可以在全六变量中证明：两 canonical
prefactor 与 sigma 准周期的线性项准确相消，余下同一个固定根单位。
因此原 $h_W$ 是作用在第一 Y 轴上的明确算子，
而不只是有一个相同 Y 边际。

结合 R719 已付的整个 (Y,Z) cd 返回和 R715/R734 的完整
$\mathscr Z_1=0$，得到物理 E 深门上 B0 的整个 Z 首矩为零。
R794 的 J 深首矩因此由同门的 J 浅首矩准确补消。
原全中央条件、所有 unit 切集和高阶对数尾保持；本篇没有给一个
未计算的二阶负矩赋非零。

## 1. 同一原格、半周期代表与完整 canonical 算子

沿 R702 的原六 sigma 生成函数、$-1/84$、C 角平均、普通周期及
所有原参数：
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad N\in4\mathbf Z_{>0}.
$$
记原六输入输出行
$$
Y=A+c+2d,\qquad W=A+3\delta c+4d,\qquad
L_\Delta=(W-Y)/2=(1+3\omega)c+d.
\tag{1}
$$
其 Hermitian 数据为
$$
N(Y)=34,\quad N(W)=72,\quad N(L_\Delta)=8,\quad
\langle Y,L_\Delta\rangle=-3\omega,\quad
\langle L_\Delta,Y\rangle=-3\omega^2.
\tag{2}
$$
取 R702 的同一 primitive 周期代表
$$
t\in\{0,\Omega_0/2,\omega\Omega_0/2,(1+\omega)\Omega_0/2\}.
\tag{3}
$$
首先在 $b=-1$ 的原 primitive 规范写式，再按原 CM homothety
将所有周期、准周期、半特征和算子一起运输到 b=17。
该运输不改变下面的标量相位。

令 $\mathbf z=(z_1,\ldots,z_6)$ 为六个独立生成变量，
$\mathcal F(\mathbf z)=-\prod_{\nu=1}^6\sigma(z_\nu)/84$。
对原整行 L，沿用 canonical lift
$$
(\mathsf T_{L,t}\mathcal F)(\mathbf z)
=\exp\{-\eta_t(\langle\mathbf z,L\rangle+N(L)t/2)\}
                         \mathcal F(\mathbf z+Lt).
\tag{4}
$$
这里 Hermitian 配对对第一变量线性；
$\eta_t$ 按(3)的实际代表取值，不任意重选准周期。
在第一 L 正交坐标中，(4)就是原 degree $N(L)$ 的平移。
若经过原固定覆盖再写此式，全部 flat 标签一并保持。

由于 $2L_\Delta t$ 逐输入是原格周期，sigma 准周期给
$$
\begin{aligned}
\mathcal F(\mathbf z+Wt)
={}&\prod_{\nu=1}^6\chi(2(L_\Delta)_\nu t)\\
&\quad{}\times
\exp\{2\eta_t\langle\mathbf z,L_\Delta\rangle
       +2\eta_tt\langle Y,L_\Delta\rangle
       +2\eta_ttN(L_\Delta)\}\,
                       \mathcal F(\mathbf z+Yt).
\end{aligned}
\tag{5}
$$
将(5)放入(4)，与 $\mathsf T_{Y,t}$ 比较。
关于全部六个变量的线性项为
$$
-\eta_t\langle\mathbf z,W-Y\rangle
       +2\eta_t\langle\mathbf z,L_\Delta\rangle=0.
$$
余下指数为
$$
\eta_tt\left\{
-\frac{N(W)-N(Y)}2+
2\langle Y,L_\Delta\rangle+2N(L_\Delta)\right\}
=-3\delta\eta_tt .
$$
故准确有
$$
\boxed{
\mathsf T_{W,t}\mathcal F
=\vartheta_t\mathsf T_{Y,t}\mathcal F,\qquad
\vartheta_t=
\prod_{\nu=1}^6\chi(2(L_\Delta)_\nu t)\,
                        e^{-3\delta\eta_tt}.}
\tag{6}
$$
(6)是全六变量恒等式，没有先将伙伴设为零，
也没有要求一个隐藏变量在微分后仍正交于 W。
全部相位和 R702(22) 相同；本证明明确了被其共同隐藏条件简化的
全变量 canonical 线性项如何相消。

R702 的 primitive 规范
$\delta\eta_{\Omega_0}\Omega_0=2\pi i$ 与原半特征给
$$
\vartheta_0=1,\qquad \vartheta_t=i\quad(t\ne0).
\tag{7}
$$
这沿同一 b=17 缩放运输；不重新选择 i 的符号。
原 C 角平均逐个固定 Y、W，因而与(6)交换。
所以(6)也适用于本文的原 $e_0$，保所有原 sigma 输入。

## 2. h_W 的 whole Y 算子及真正可交换的权

原 $h_W=e_1+e_2=-\frac12\sum_{t\in E[2]}\mathsf T_{W,t}e_0$。
定义固定第一 Y 算子
$$
\mathcal H_Y=-\frac12\sum_{t\in E[2]}
                       \vartheta_t\mathsf T_{Y,t}.
$$
由(6)得到完整来源身份
$$
\boxed{h_W=\mathcal H_Ye_0.}
\tag{8}
$$
这不是只写 $Y_*h_W=\omega^2S$。
其绝对规范仍由 R702 的 $\mathcal H_Y(S)=\omega^2S$ 校准。

在完整 Y 正交 theta 张量中，$\mathsf T_{Y,t}$ 只作用第一 Y 轴。
所以任意只依真实 $Y^\perp$ 伙伴的有界权、有限 p 门及其正矩
都与 $\mathcal H_Y$ 交换。
用六变量(4)也可直接检查：伙伴微分的额外 prefactor 项正比
$\langle L,Y\rangle$，在 $L\perp Y$ 时为零。
原有限门按实际 p-Schwartz 算子使用，仍只作用伙伴；
不是用“相同边际”推导交换。

特别，本文的原
$$
Z=W-b_YY,\quad b_Y=(20+3\omega)/17,\qquad
E=E_{YW},\quad J,\quad q
$$
都属于 $Y^\perp$。因此
$$
\boxed{
Z^k1_{E\in p^N}q\,h_W
=\mathcal H_Y\bigl(Z^k1_{E\in p^N}q\,e_0\bigr)
\qquad(k\ge0).
}
\tag{9}
$$
亦可附原 J 深或浅门。若附 W-unit、P-unit 或另一个混合 Y 的 cut，
则不能继续把该门穿过 $\mathcal H_Y$；其完整平移必须保留。

## 3. 使用已经支付的全 (Y,Z) 返回

令 $\rho_{cd,N}$ 为 R715(3) 的同一个完整 cd 端点来源。
它保原两条 C 分支、全部 E 次数逆、最高三十次权，
及各块 $b^{d/6}\Omega^d$。
它不是原未返回的 CD 指示测度。

R719(25)已经证明整个平面身份
$$
\boxed{
(Y,Z)_*(1_{E\in p^N}q e_0)
=\lambda^{2N}\rho_{cd,N}^{YZ}.}
\tag{10}
$$
该证明比较同一 $\{Y,Z,E\in p^N\}$ 的 cd 返回与整个 Y/Z 矩形，
在真实单射推前上约消；不是从两条边际提升。
R734 的 q 是原50行及两核列的完整线性组合，故(10)原样适用。
它还严格保留
$$
\mathscr Z_1(q)(z)
=\Omega^{-1}\int Z e^{Yz/\Omega}\,d\rho_{cd,N}=0
\tag{11}
$$
作为整个五维来源的零，而不只是五个未经完整性证明的 jet。

由(10)、(11)，
$$
\boxed{
\Omega^{-1}Y_*(Z\,1_{E\in p^N}q e_0)=0.}
\tag{12}
$$
再用(9)，该完整来源的 $\mathcal H_Y$ 像亦为零，故
$$
\boxed{
\Omega^{-1}Y_*(Z\,1_{E\in p^N}q h_W)=0.}
\tag{13}
$$
令 $c_B=1-\omega^2$、$B_0=(e_0-\omega h_W)/c_B$，
便得本篇首要的实际门身份
$$
\boxed{
\Omega^{-1}Y_*(Z\,1_{E\in p^N}q B_0)=0.}
\tag{14}
$$
其量词是任意完整 Y 测试，因而包括原 Y-unit 负一观察；
不包括在右边另加一个未转置的混合 W 单位门。

R702/R734 同时给
$$
Y_*(1_{E\in p^N}qB_0)=0,\qquad
W_*(1_{E\in p^N}qB_0)
=\lambda^{2N}6\delta\,\nu_T/c_B .
\tag{15}
$$
(14)是原已适配的混合约束与(8)的后果，不是从 $J'_T=0$ 推出。
原强中央假设始终仍只有原 S/T/U 的完整中央零。

## 4. J 浅补域的整个五维首矩被准确确定

沿 R794 记
$$
\mathcal L_N^J=\Omega^{-1}Y_*(t\,1_{J\in p^N}qB_0),\qquad
M_J=\int_{\substack{J\in p^N\\Y\ {\rm unit}}}tY^{-1}q\,dB_0 .
$$
R794(18)给
$$
\Omega^{-1}Y_*(Z\,1_{E,J\in p^N}qB_0)
=-a\lambda^N\mathcal L_N^J,\qquad a=1+3\omega .
\tag{16}
$$
现在从(14)减去该真实深交域，得到
$$
\boxed{
\Omega^{-1}Y_*(Z\,1_{\{E\in p^N,\ J\notin p^N\}}qB_0)
=+a\lambda^N\mathcal L_N^J.}
\tag{17}
$$
这是同 q、同物理 E、同 Z、同第一 Y 源的精确补偿。
R791 已证明 $\mathcal L_N^J$ 的两条算术幅度均为单位，
其负一行 $M_J\ne0$，全部 primitive 块保持。
所以
$$
\boxed{
\begin{aligned}
\int_{\substack{E,J\in p^N\\Y\ {\rm unit}}}ZY^{-1}q\,dB_0
 &=-a\lambda^NM_J\ne0,\\
\int_{\substack{E\in p^N,\ J\notin p^N\\Y\ {\rm unit}}}
                     ZY^{-1}q\,dB_0
 &=+a\lambda^NM_J\ne0 .
\end{aligned}}
\tag{18}
$$
两行准确相反，不能引用 R791 的另一对“全 J 深/浅的 t 首矩独立”
将它们误称独立。观察和 E 条件已经改变。

原 Z 偶核同时固定 E、J、Y、q。
故在(18)两域再附 $Z\in p^j$（j 偶）时，两行同乘
$\lambda^j\kappa^j$；
附真实两层环带 $v_p(Z)\in\{j,j+1\}$ 时，同乘
$\lambda^j\kappa^j(1-\lambda^2\kappa^2)$。
这完整支付对应实际浅条带的首项，不仅规定它的某个总质量。

## 5. 全 E 深 W 相对行从二阶开始，全部尾与原中央保留

定义
$$
G_N^{\rm all}(z,w)
=\int_{E\in p^N}f_w(b_YY+zZ)\,q\,dB_0,\qquad
f_w(x)=1_{x\ {\rm unit}}\langle x\rangle^{d_pw}.
$$
当 $z\in p\mathcal O$ 时，单位条件准确是 Y-unit。
由(14)、(15)，原常数项和整条一阶项都为零。
因此完整式为
$$
\boxed{
\partial_wG_N^{\rm all}(z,0)
=d_p\sum_{k\ge2}\frac{(-1)^{k+1}z^k}{k b_Y^k}
 \int_{\substack{E\in p^N\\Y\ {\rm unit}}}
                         Z^kY^{-k}q\,dB_0 .}
\tag{19}
$$
特别准确的二阶系数是
$$
-\frac{d_p}{2b_Y^2}
 \int_{\substack{E\in p^N\\Y\ {\rm unit}}}Z^2Y^{-2}q\,dB_0 .
\tag{20}
$$
本篇没有给(20)非零或某一算术点身份。
R719 的固定混合单位组合只同时涉及 k=2至5，
并不能代替这个指定的 B0 负二条件行。
因此不把 O(z²)写成“恰二阶非零”。

在实际 $z=\kappa^j$、j≥2偶的范围，整有界性给
$$
\partial_wG_N^{\rm all}(\kappa^j,0)\in p^{2j}\mathcal O.
\tag{21}
$$
R794 的 J 深部分和(17)的 J 浅部分分别有非零一阶项；
它们在同一个原域分割中严格消掉，留下(19)全部尾。
(21)不是将两个非零部分各自赋零。

由完整 Z 偶核，
$$
\int_{\substack{E\in p^N\\Z\in p^j}}f_w(W)q\,dB_0
=\lambda^jG_N^{\rm all}(\kappa^j,w).
\tag{22}
$$
其余整个 E 深/Z 浅行定义为
$$
\mathscr X_{N,j}^{\rm all}(w)
=\int_{\substack{E\in p^N\\Z\notin p^j}}f_w(W)q\,dB_0 .
$$
原 W 来源(15)准确给
$$
\boxed{
\mathscr X_{N,j}^{\rm all}(w)
+\lambda^jG_N^{\rm all}(\kappa^j,w)
=\lambda^{2N}6\delta\,J_T(w)/c_B .}
\tag{23}
$$
只有在原 $J'_T(0)=0$ 下，两个完整中央导数才由(23)相反。
本篇既没有把(19)的全部无限尾作有限点投影，
也没有把 R780/R784 的 CM 逆 Y、原 cd/U 失败或 E 浅参考项混入
(23)后删除。

## 6. 依赖与执行范围

(5)–(9)由原 sigma 准周期与完整 canonical lift 直接证明；
(10)是已经付清的联合来源，不由边际猜测。
未新增数值运行、射线、测试或可重算输出文件。
本篇的具体非零只使用 R791/R794 已识别的同一五维来源。
下一需要单独支付的是(20)或更高有限混合来源的实际算术行，
及其与(23)完整中央的独立关系。

- [R702](R702-forty-five-neutral-tests-and-complete-three-state-arithmetic-gate.md)：固定半周期代表、绝对相位和原三态。
- [R715](R715-complete-first-z-source-and-fifty-neutral-returns.md)：整个原 cd-Z 首矩为零。
- [R719](R719-native-second-fibre-and-exact-mixed-source-relation.md)：式(25)的完整 (Y,Z) 平面返回与全高阶混合范围。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：本文未修改的 q 与全部50行。
- [R791](R791-original-j-depth-negative-moments-and-two-e-sectors.md)：原 J 首矩的两算术幅度和负一非零。
- [R794](R794-original-e-j-intersection-and-native-w-annuli.md)：物理 E/J 交域、全两输出及真实 Z 环带。
