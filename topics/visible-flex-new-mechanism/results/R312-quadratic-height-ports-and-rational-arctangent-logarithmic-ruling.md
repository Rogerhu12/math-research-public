# R312：可安装的二次 h 偶端芽及完整有理—反正切—对数 ruling 接口

日期：2026-11-15。**完整纸面推导与有限维安装证明；没有运行求积、符号程序、profile 扫描、人工测试或研究计算。**

[R304](R304-positive-one-history-remainder-excludes-disjoint-real-rank-one-circles.md) 与 [R311](R311-continuous-rank-one-profile-orbits-are-rigid-under-the-complete-low-order-gates.md) 已排除旧小共振 Gaussian 端芽上的整个固定实 rank-one 包路线，不能再用非圆幅值曲线或增加同族高频预算修复。本稿从**实际几何的初始设计**改选一个明确的非 Gaussian 偶端芽。它仍可按已有真实桥和有限约束安装，但其完整 history 的函数代数真正不同。

新端芽的第二 history 只有一个反正切方向。完整第三恢复另产生一个对数项；全偶 ruling 因而准确落在 $1,E,E^2,L$ 四种函数类型上，系数有理。本文证明它们在有理函数域上线性独立，并列出原 $E^2$、$L$、$E$ 与纯有理余式的全部必要门。特别给出反正切的真实八矩方向，不把“函数种类减少”冒称门已支付。

这是**新设计几何**。安装完成以后才冻结其度量。本文不称沿此次端芽替换保持旧 $g$，也不授新圆、完整 fourth、嵌入或 reach。

来源：[R70 原桥](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R73 原逐点八矩与 chain](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R218 偶端口的完整安装](R218-common-even-nonflat-germs-and-exact-universal-pure-control.md)、[R223 受约束 Morse](R223-Morse-closed-hooks-with-exact-pure-and-eight-flux-constraints.md)、[R227 真实 scalar/frame 接口](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)、[R243 同中心偶部商](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md)、[R296 完整零／一层恢复](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md)及 [R302 正则共享原语](R302-regular-chi-prototypes-shared-reversal-and-enhanced-Morse-control.md)。

## 1. 选定一个准确的非 Gaussian 端芽

在真实物理距离 $\sigma=s-s_e$ 上规定
$$
\boxed{
h(\sigma)=h_e(1+\varepsilon\sigma^2),\qquad
k(\sigma)=\kappa,\qquad
\omega(\sigma)=\omega_e,\qquad
h_e>0,\quad \varepsilon>0,\quad \kappa\ne0.
}
\tag{1}
$$
只在一个固定正长度核心邻域要求这个准确公式；真实闭路径不必在其他地方采用它。所有端口参数在构造之初选择。

原水平方程严格成立：
$$
\omega_s=0=k_s/(2h).
$$
全部 scalar 奇阶 jets 为零，
$$
h_s(0)=k_s(0)=\omega_s(0)=0,\qquad
h_{ss}=2\varepsilon h_e>0.
\tag{2}
$$
所以核心里的 $h$ 只有一个非退化临界点。它不是 R216 的四阶平点。对真倒行 $\sigma\mapsto-\sigma$，整个 germ 保持，不只端状态保持。

正仿射作用
$$
h\mapsto Hh,\qquad k\mapsto k,\qquad
\omega\mapsto(\omega+c)/H,\qquad H>0
$$
仍送到同一(1)类别，且不改变 $\varepsilon$ 或物理 $s$。不同端状态的桥在两端分别使用相应参数，不能在已冻结坐标下忽略实际时长。

## 2. 真实安装：保持原结构，明确改变设计度量

从 R218/R223/R302 已具有正则参数的一个**有限**原语库开始，先固定整数词、共享重复及紧参数盒。所有标记的原常值 collar 采用
$$
h_{\varepsilon}^{\rm pre}
=h^{\rm old}+
\sum_e h_e\,\varepsilon(s-s_e)^2\chi_e(s-s_e),
\tag{3}
$$
其中 $\chi_e$ 偶、核心恒1、支撑在原常值 collar 内。接口位置和端值随该次真实原语参数一起评价；$s-s_e$ 是物理距离。

在修改支撑上原 $k_s=0$，所以预修改不改变 $\omega_s$。$k$ 和原 frame ODE 也没有预修改，故无需额外声称一个零成本 frame 桥。矩阵、第三与第四成本仍会改变，必须按新几何全部恢复。

R218 的原八矩参数 $a\in\mathbb R^8$、内部 $h$ 校正 $z\zeta$ 及自由 masked 扰动 $\eta$ 给真实约束
$$
\mathcal G(a,z,\eta,\varepsilon)
=(M-M_*,\ \omega_{\rm end}-\omega_+).
$$
在 $\eta=\varepsilon=z=0$，(3)连同其原语参数导数都为零，故准确的导数仍是
$$
D_{(a,z)}\mathcal G=
\begin{pmatrix}
D_aM&D_zM\\
0&-\frac12\int k_s\zeta/h^2
\end{pmatrix},
\tag{4}
$$
原两个对角块可逆。有限维参数 IFT 因而准确恢复完整 $M$ 与末 $\omega$；原语 frame 端点继续由其已付族保持。$\zeta,\eta$ 的支持与保护核心分开，所以(1)没有在恢复中被破坏。

端速度为零仍给 R129 的 $P_1,P_{3,a},P_{3,v},N_2$ 全零。$N_0$ 保留并由整块 $M=0$ 的原初势修正消去。因此修改后的完整 M0 成本仍属于同一个原空间 $U$。共享真倒行、R71/R101/R302 的完整第三结构词、原 finite pure／已正则有限观察的截面于是继续使用真实修改后成本；在 $\varepsilon=0$ 恢复原满秩导数，再由同一个有限 IFT 恢复那些已经具有正则截面的目标。

这不授权保持任意未经证明可控的新增观察，也不把某个内部子块的第三量固定不动。共享原语和其真倒行必须使用同一个修改后的实际族；所有入历史逐块传递。

对闭 hook，按修改后的真实 prototype 位移作原 Klein 求和，所以空间闭合和 frame 闭合保持。核心由(2)已经 Morse；其余区域保留 R223 的 masked 自由扰动和有限约束补偿，原两 jet 横截论证仍可选取全域 Morse $h$。正 $h$、共同物理支和原紧参数余量在小固定正 $\varepsilon$ 下保持。

这里使用的是 R218 安装证明中“平滑小的偶 $h$ 修改、端速度为零、核心受保护”这些实际条件；该证明不依赖指数的特殊微分方程。新的式(3)逐项满足这些条件。所有真实 costs 均在改变后的几何上定义，不能称本节为旧 fixed-$g$ 圆的连续修补。

## 3. $\omega_e$、物理域和原偶部空间

令 $y=x+\omega_e$，并同时平移全部 profiles、积分区间和右锚。这只是同一个物理 $z=y>0$ 的坐标写法，不是把 profile 留在旧坐标而单独改 $\omega_e$。在 $y$ 坐标中，
$$
e=hy-\kappa,\qquad d=-\kappa,\qquad
\gamma=2h_e\varepsilon\sigma,\qquad e_s=\gamma y.
\tag{5}
$$
以下为简洁把 $y$ 再记为 $x$；所有原算子和右积分都在这个共同平移后的坐标中。

三矩权准确为
$$
\boxed{
\mathcal E_\sigma(a,b)
=\frac{1+\kappa^2}{4h}I_0(a,b)
-\frac{\kappa}{2}I_1(a,b)
+\frac h4I_2(a,b).
}
\tag{6}
$$
在任意正 $\varepsilon$ 下，$1,h,h^{-1}$ 真独立；故
$$
\boxed{\mathcal W_e=\operatorname{span}\{1,h,h^{-1}\}.}
\tag{7}
$$
特别，
$$
\sigma^2=\frac{h/h_e-1}{\varepsilon}\in\mathcal W_e.
\tag{8}
$$
这是固定正 $\varepsilon$ 的准确身份，不是极限近似。

若在未平移的原坐标选择 $\omega_e=\kappa/h_e$，只是令中心 $d(0)=0$。此时
$$
d(\sigma)=\kappa\varepsilon\sigma^2
=\kappa(h/h_e-1).
\tag{9}
$$
所以旧 Gaussian 稿中使用的 $h$ 与 $\sigma^2$ 的超越分离不再成立。R304 的指定 $\sigma h^{-2}j^0$ 行不能作为一个独立旧行移植到(1)：既改变了真实 elementary history，也存在(9)的精确代数关系。

其他 $\omega_e$ 只改变原三矩权的常线性组合。在坐标一致平移后，本文的基函数和全部门完全相同。共同物理区间仍须事先满足 $x+\omega_e>0$；不能用这个坐标事实免付实际包络。

### 3.1 同中心比较的原式证明：不借用 Gaussian 的特殊方程

这里需要的范围是：$h$ 为任意正偶函数，而 $k=\kappa,\omega=\omega_e$ 为常数；不声称任意仅满足部分奇偶的几何都自动适用。以下复用 [R224 §§2、4 的完整恢复式](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)，逐项说明该证明没有使用 $h_s/h=2\varepsilon\sigma$。

由 R73 的六项原式，$M_{\rm raw}$ 的速度项只有 $\gamma e_s,\gamma^2,\lambda\gamma,\lambda d_s$ 等两个奇因子的乘积，其中 $\lambda=e_s/h^2$；其余状态项偶。因此 $M_{\rm raw}$ 偶。真实全字累计矩阵准确写成
$
\mathsf m(\sigma)=\mathsf m_*+\mathsf o(\sigma),\qquad
\mathsf o(\sigma)=\int_0^\sigma M_{\rm raw}(\tau)\,d\tau,
\qquad \mathsf o(-\sigma)=-\mathsf o(\sigma).
\tag{10a}
$
原 R221 的完整局部 $\mathcal T_\sigma(c;a,b)$ 每项恰含一个 $\gamma$ 或 $e_s$，其余几何因子偶，所以它为奇函数。这里用的是保留真实右尾转置的原 $\mathcal T$，没有只取 local principal。

合法第一轨道满足三个原二次矩
$\mathbf I(D)=\mathbf I(f,f)-\mathbf I(\phi,\phi)=0$。故
$w^*=\Phi_{\mathsf m_*}D$ 真正同 collar 紧支撑：R73 的局部部分在两端为零，其三个左尾也由这三个零矩全部消去。定义同右锚中心模型
$
\widehat Z=K_\sigma(D)-Y_{\Phi_{\mathsf o}D},
$
并由原 R56 forcing $-2H(Y_\phi,\widehat Z)$ 恢复 $\widehat U$，仅令中心 characteristic 初值为零，不把 local normal 或 $\eta$ 同时置零。原恢复的线性性直接给
$
Z=\widehat Z-Y_{w^*},\qquad
U=\widehat U+2\widehat Z_B(\phi,w^*)+Y_{\chi^*}.
\tag{10b}
$
其中 $\chi^*$ 是与 $\sigma$ 无关的真实齐次初值差。它可以有左尾；不将它先授为合法全局 gauge。外槽 $\phi$ 真紧，故 R221 已付的真实端项仍给
$\mathfrak b(Y_\phi,Y_{\chi^*})=\mathcal E_\sigma(\phi,\chi^*)$。

将(10b)代入完整第四组合 $-\mathfrak b(Z,Z)-2\mathfrak b(Y_\phi,U)$，得到
$
\mathscr K^0-\widehat{\mathscr K}
=\widehat{\mathcal B}(w^*)-\mathcal E_\sigma(w^*,w^*)
-2\mathcal E_\sigma(\phi,\chi^*),
\tag{10c}
$
其中四项 mixed 响应准确为
$
\begin{aligned}
\widehat{\mathcal B}(w)
={}&2\mathcal T_\sigma(w;D)
-4\mathcal T_\sigma(\phi;\phi,w)\\
&-2\mathcal E_\sigma(\Phi_{\mathsf o}D,w)
+4\mathcal E_\sigma\{\phi,\Phi_{\mathsf o}(\phi,w)\}.
\end{aligned}
\tag{10d}
$
$\mathcal E_\sigma$ 的三个权偶；(10a)与 $\mathcal T$ 奇性使(10d)全部为奇。因而(10c)的偶部只剩
$
\operatorname{Ev}(\mathscr K^0-\widehat{\mathscr K})
=-\mathcal E_\sigma(w^*,w^*)-2\mathcal E_\sigma(\phi,\chi^*)
\in\mathcal W_e.
\tag{10e}
$
这显式保留了常二阶入场的平方，以及真实第三初值；它们没有仅凭“偶”被删掉。

中心模型自身为偶，也可直接从原 R56 恢复核对：第一场 TB 分量偶；第二场 N 偶、TB 奇；第三场 TB 偶、N 奇。这里的 $s$ 导数使用原 frame 联络，TB/N 的交换已经计入。等价地，后文完整(22)–(23)给出相同偶性，而非仅局部项的偶性。因此准确有
$
\boxed{
[\operatorname{Ev}\mathscr K_\theta^0]
=[\widehat{\mathscr K}_\theta]\pmod{\mathcal W_e}.
}
\tag{10}
$

任意允许的固定二阶 profile gauge $w_\theta$ 也由同一个原式处理：真实 $\mathsf m_*+\mathsf o$ 替代(10d)的 $\mathsf o$ 后，其偶部只多两个 $\mathsf m_*$ 的 $\mathcal E_\sigma$ 配对；原额外平方 $-\mathcal E_\sigma(w_\theta,w_\theta)$ 和第三齐次项亦在 $\mathcal W_e$。所以这是全部原 gauge 的必要偶部商，既没有重置真实 history，也不要求中心模型自身通过全局第三 range。新空间(7)并不自动包含新的 canonical 目标。

## 4. 第二 history 的唯一反正切方向：给出真实八矩系数

写
$$
H_q=1+\varepsilon\sigma^2,\qquad K=1+\kappa^2,\qquad
E(\sigma)=\int_0^\sigma\frac{d\tau}{1+\varepsilon\tau^2}
=\frac{\arctan(\sqrt\varepsilon\,\sigma)}{\sqrt\varepsilon}.
\tag{11}
$$
在本文每个固定正 $\varepsilon$ 上，$E$ 是原同中心真实积分。

把(5)直接代 R73(9)–(10)，得到全部非零坐标：
$$
\begin{aligned}
p_0&=-\frac{\kappa K}{2h_eH_q},&
s_1&=\frac{\kappa K}{4h_eH_q},\\
p_1&=\kappa^2,&
p_2&=-\frac{\kappa h_eH_q}{2},\\
r_1&=\frac K{8h_e^2}
\{-K H_q^{-2}+4\varepsilon(H_q^{-3}-H_q^{-4})\},\\
t_1&=-\frac K8-\frac{\varepsilon}{2}(H_q^{-1}-H_q^{-2}),
\qquad r_0=s_0=0.
\end{aligned}
\tag{12}
$$
迹条件 $t_0=p_0/4+s_1/2=0$ 仍准确成立。特别没有通过删坐标来假设矩阵只在一个预定子代数内。

置 $I_n=\int_0^\sigma H_q(\tau)^{-n}d\tau$。原积分的准确递推是
$$
I_n=\frac{\sigma}{2(n-1)H_q^{n-1}}
+\frac{2n-3}{2(n-1)}I_{n-1}\quad(n\ge2).
\tag{13}
$$
所以 $I_1,I_2,I_3,I_4$ 的 $E$ 系数依次为 $1,1/2,3/8,5/16$。由(12)–(13)，整个 centered 第二历史准确分解为
$$
\boxed{\mathsf m(\sigma)=\mathsf Q(\sigma)+E(\sigma)B_\varepsilon.}
\tag{14}
$$
其中原常矩阵方向是
$$
\boxed{
B_\varepsilon=
\frac{K(\varepsilon-2K)}{32h_e^2}\,\Phi_{r_1}
-\frac{\kappa K}{2h_e}\,\Phi_{p_0}
+\frac{\kappa K}{4h_e}\,\Phi_{s_1}
-\frac{\varepsilon}{4}\,\Phi_{t_1}.
}
\tag{15}
$$
它对所有正 $\varepsilon$ 都非零，因为最后一项非零。$\mathsf Q$ 是准确奇有理算子：
$$
\begin{aligned}
\mathsf Q={}&q_R\Phi_{r_1}
+\kappa^2\sigma\,\Phi_{p_1}
+q_T\Phi_{t_1}
-\frac{\kappa h_e}{2}
\left(\sigma+\frac{\varepsilon\sigma^3}{3}\right)\Phi_{p_2},\\
q_R={}&\frac{K\sigma}{8h_e^2}
\left\{
\frac{-K/2+\varepsilon/4}{H_q}
+\frac{\varepsilon}{6H_q^2}
-\frac{2\varepsilon}{3H_q^3}
\right\},\\
q_T={}&-\frac{K\sigma}{8}+\frac{\varepsilon\sigma}{4H_q}.
\end{aligned}
\tag{16}
$$
所有真实初值 $\mathsf Q(0)=E(0)=\mathsf m(0)=0$。这里只对原中心模型分解，实际全路径的入值仍按(10)保留。

## 5. 完整第三恢复只再添一个对数：不能删 chain

沿 R296 的原记号，
$$
(W_C)'=\mathscr C_\sigma(\phi;D)
-\mathsf M(\phi,\mathsf mD),\qquad
\mathsf M=\mathsf Q'+B_\varepsilon E'.
\tag{17}
$$
$\mathscr C_\sigma=\ell_\sigma-\Psi_\sigma(\phi,\mathsf MD)$ 包含整个局部恢复的真实 $\sigma$ 导数与原 chain。对(1)，它是奇有理的几何系数乘有限个真实 profile 表达；没有含未记录的 s-history。

用真实同中心 IBP，
$$
\int_0^\sigma\mathsf Q'(\phi,B_\varepsilon D)E
=\mathsf Q(\phi,B_\varepsilon D)E
-\int_0^\sigma E'\mathsf Q(\phi,B_\varepsilon D).
$$
于是准确有
$$
\boxed{
W_C=
U(\sigma)-E\,\mathsf Q(\phi,B_\varepsilon D)
-\frac{E^2}{2}B_\varepsilon(\phi,B_\varepsilon D),
}
\tag{18}
$$
其中
$$
\boxed{
U'=
\mathscr C_\sigma(\phi;D)
-\mathsf Q'(\phi,\mathsf QD)
+E'\{\mathsf Q(\phi,B_\varepsilon D)
-B_\varepsilon(\phi,\mathsf QD)\},\qquad U(0)=0.
}
\tag{19}
$$
最后一对项是原两个不同次序，不能因只有一个 transcendental 字母就删除它们。

右侧每个几何系数属于
$\sigma\mathbb R[\sigma^2,H_q^{-1}]$。其真实积分唯一写成偶有理部分加
$$
L(\sigma)=\log H_q
$$
的常系数。因此
$$
\boxed{U(\sigma)=U_{\rm rat}(\sigma)+L(\sigma)\,\mathscr D(\phi;D),}
\tag{20}
$$
$U_{\rm rat}(0)=0$。这里的 $\mathscr D$ 是由(19)给定的完整三次 profile 算子，不是独立可选的尾。

一个可直接核对的原定义如下。若(19)某项几何系数写成 $\sigma R(\sigma^2)$，则该项在 $\mathscr D$ 中的系数是
$$
\boxed{\frac12\operatorname{Res}_{t=-1/\varepsilon}R(t).}
\tag{21}
$$
其余高阶 pole 原函数、普通多项式和真实中心常数全留在 $U_{\rm rat}$。式(21)只是原有限有理函数的系数抽取，不要求新的求积，不把 $\mathscr D$ 预设为零。

所有 profile 右原函数、左多项式尾和 Green 项继续保在 R56 的 $\mathscr C_\sigma,\mathsf Q,B_\varepsilon$ 内。这里的“有理”只指几何变量 $\sigma$，不是将真实 profile history 局域化。

## 6. 整个偶 ruling 的四类真实函数

令
$$
Z_0=K_\sigma(D)-Y_{\mathsf QD},
$$
$$
C_0=K_\sigma^{(0)}(\phi;D)
-K_\sigma(\phi,\mathsf QD)
-J_\sigma^{\rm ch}(\phi,\mathsf MD).
$$
它们与 R296 是同一完整恢复。将(18)–(20)代回
$-\mathfrak b(Z,Z)+4\mathfrak b(Y_\phi,C)$，准确得到
$$
\boxed{
\widehat{\mathscr K}_\theta
=\mathscr R_{\rm rat,\theta}
+E\,\mathscr R_{E,\theta}
+E^2\,\mathscr R_{2,\theta}
+L\,\mathscr R_{L,\theta}.
}
\tag{22}
$$
四个系数均为有理函数；第一、第三、第四个偶，第二个奇。完整表达是
$$
\begin{aligned}
\mathscr R_{\rm rat,\theta}
&=-\mathfrak b(Z_0,Z_0)
+4\mathfrak b(Y_\phi,C_0)
-4\mathcal E_\sigma(\phi,U_{\rm rat}),\\
\mathscr R_{E,\theta}
&=2\mathcal T_\sigma(B_\varepsilon D;D)
-4\mathcal T_\sigma(\phi;\phi,B_\varepsilon D)\\
&\quad-2\mathcal E_\sigma(\mathsf QD,B_\varepsilon D)
+4\mathcal E_\sigma\{\phi,\mathsf Q(\phi,B_\varepsilon D)\},\\
\mathscr R_{2,\theta}
&=-\mathcal E_\sigma(B_\varepsilon D,B_\varepsilon D)
+2\mathcal E_\sigma\{\phi,B_\varepsilon(\phi,B_\varepsilon D)\},\\
\mathscr R_{L,\theta}
&=-4\mathcal E_\sigma\{\phi,\mathscr D(\phi;D)\}.
\end{aligned}
\tag{23}
$$
$\mathsf MD$ 出现在 $J^{\rm ch}$ 中；没有以 $\mathsf Q'D$ 替代它。完整变化 profile 的 chain 因而仍在纯有理项。

原式只含有限次乘法、微分和已列有理原函数，因此每个有理系数有一个由原有限公式确定的有限 pole 阶数与多项式次数。清掉共同 $H_q$ 的有限次幂，就得到有限多项式系数门。本文没有运行其展开或宣称某个尚未计算的行数、秩。

## 7. 四类在有理函数域上的真实独立性

在固定正 $\varepsilon$ 下，取复变量 $\sigma$ 的原局部分支：
$$
E=\frac{1}{2i\sqrt\varepsilon}
\{\log(1+i\sqrt\varepsilon\,\sigma)
-\log(1-i\sqrt\varepsilon\,\sigma)\},
$$
$$
L=\log(1+i\sqrt\varepsilon\,\sigma)
+\log(1-i\sqrt\varepsilon\,\sigma).
$$
两复点 $\sigma_\pm=\pm i/\sqrt\varepsilon$ 周围的小圈分别给
$$
(\Delta E,\Delta L)
=(\pi/\sqrt\varepsilon,2\pi i),\qquad
(-\pi/\sqrt\varepsilon,2\pi i).
\tag{24}
$$
这两个平移向量独立。

若有理系数满足
$$
A(\sigma)+B(\sigma)E+C(\sigma)E^2+D(\sigma)L=0,
$$
先沿同一圈取两次有限差分，得到
$2C(\pi/\sqrt\varepsilon)^2=0$，所以 $C=0$。再分别沿两个圈作一次差分，由(24)得到 $B=D=0$，最后 $A=0$。有理函数沿这些圈没有 monodromy；路径可避开其其他有限极点。

因此
$$
\boxed{1,\ E,\ E^2,\ L\quad
\text{在 }\mathbb C(\sigma)\text{ 上线性独立}.}
\tag{25}
$$
这里仅以解析延拓判定原 germ 的函数身份，没有把实际闭路径延伸到复域。$\varepsilon=0$ 的退化不属于(25)；安装 IFT 的平滑极限使用真实原函数，而非在退化点强求这个独立基保持。

## 8. 第一批真正的完整门，尚未支付

由(7)、(22)、(25)，原偶部通过 $\mathcal W_e$ 当且仅当逐角满足
$$
\boxed{
\mathscr R_{2,\theta}=0,\qquad
\mathscr R_{L,\theta}=0,\qquad
\mathscr R_{E,\theta}=0,\qquad
\mathscr R_{\rm rat,\theta}\in\operatorname{span}\{1,h,h^{-1}\}.
}
\tag{26}
$$

这些不是四个自由标量。前两类因(6)三权独立，可更准确写成以下六个原 profile 门：
$$
\boxed{
-I_j(B_\varepsilon D,B_\varepsilon D)
+2I_j\{\phi,B_\varepsilon(\phi,B_\varepsilon D)\}=0,
\quad j=0,1,2,
}
\tag{27}
$$
$$
\boxed{
I_j\{\phi,\mathscr D(\phi;D)\}=0,
\quad j=0,1,2.
}
\tag{28}
$$
$B_\varepsilon$ 已由(15)完全给定，$\mathscr D$ 已由原(19)、(21)完全给定。后一组保留真正 local-third 和有序 commutator 的 residue，不可只检查某个 elementary self。

一层使用(23)的完整 directed 与 $\mathcal T$，不能仅用 $\alpha_{B_\varepsilon}$ 的 principal。有理余式则须保完整 $Z_0,C_0,U_{\rm rat}$，不由(27)、(28)自动消去。

与旧 Gaussian 情况的实质区别是：只有一个 $E$ 字母，其二重字准确为 $E^2/2$，所以没有六个彼此独立的 Gaussian 反对称面积可分别施门。但原不同算子次序没有消失，它们已经进入(19)的对数 residue 和有理余式。这是**改变了真实待解方程**，不是忽略原尾或删约束。

当前尚未证明存在一个非退化 profile 轨道同时满足(26)，也没有证明(27)本身无解。下一步必须直接评价(27)与原 residue(28)的完整 self／cross 兼容，尤其检查它们与一层低阶 annihilator 的关系；只增加这个有限表示本身不构成主目标的完成。

## 9. 这一设计接口已经付清与仍欠的部分

已经付清的是：真实水平方程、全偶匹配、正 $h$ 与核心 Morse、同 k 真倒行、原有限结构词、实际 frame／位移闭合、既有正则 finite pure／有限观察截面的安装，以及完整同中心 history 的(14)、(18)、(22)。原自由 h 扰动仍可在保护核心之外作受约束 Morse 选择。

仍欠的是同一实际 profile 轨道的(26)、完整 period 与同一 gauge 的联合成员门，以及有限等距族、嵌入、reach 和宏观幅度。尤其(8)只说明旧常态 $\sigma^2$ 项在新三矩空间中；它不证明其余目标在该空间里。

本稿由(15)、(21)、(27)、(28)给出下一原式计算的明确输入。后继若发现新的正余量，应按这些真实门限定范围；后继若提出构造，也须在本次从最初安装的新几何上支付它们，不能把旧 Gaussian 圆或旧 fixed-$g$ 回执直接改名继承。
