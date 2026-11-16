# R857 — 原全三层 Scholl 对应、八十一倍逆与泛纤维 CM 循环判据

日期：2026-11-16。**状态：下述实际三同源、完整 Scholl 投影、精确 Chow 同构、原泛纤维迹及局部化判据已证明。** 未证明该迹为零，未将所得条件性 CM 循环呈示认作 R814 的指定 canonical orbit。

本篇继续 R851–R854 的原端点循环及其全部有限 Artin 数据。核心是先到真正的 full-level-3 Kuga–Sato 模型，再使用包含全部三挠平移的 Scholl 投影。原双三次空间上的裸八项算子不被冒认为全局 cuspidal projector。

## 1. 原双三次模型的实际椭圆族及微分

保持 R851 的有理坐标及 residue 规范：
$$
P=(x^2+xy^2+y)rs-(r^2+rs^2+s)xy=0,\qquad
\tau=\frac{x}{y}+y+\frac1x=\frac r s+s+\frac1r,
$$
$$
\Omega_W=\frac{dx\wedge dy\wedge dr}{P_s}.
\tag{1}
$$
置
$$
(U_1,V_1)=(-x,xy),\qquad (U_2,V_2)=(-r,rs).
$$
两对坐标准确位于同一族
$$
\mathcal E_\tau:\quad V^2+\tau UV+V=U^3.
\tag{2}
$$
令
$$
D_i=2V_i+\tau U_i+1,\qquad
\varpi_i=\frac{dU_i}{D_i}
$$
为相对不变微分。则
$$
\boxed{\Omega_W=d\tau\wedge\varpi_1\wedge\varpi_2.}
\tag{3}
$$

确实，$D_1=x(y^2-x)/y=xy\,\partial_y\tau$，同理
$D_2=rs\,\partial_s\tau$；在 $P=0$ 上
$P_s=-xyD_2$。把 $dU_1=-dx,dU_2=-dr$ 代入即得(3)，没有额外的2、3或符号。

(2) 的判别式是 $\tau^3-27$。其最小椭圆曲面在三个有限根处为 $I_1$，在无穷远为 $I_9$。以下所有泛纤维论证在
$$
B=\mathbf P^1-\{\infty,3,3\omega,3\omega^2\}
$$
上进行；紧化时保持完整图形及坏纤维。

## 2. 显式三同源及真正的 full3 结构

$P_3=(0,0)$ 是(2)的非零三挠点，$-P_3=(0,-1)$。定义
$$
\begin{aligned}
U'&=U+\frac{\tau}{U}+\frac1{U^2},\\
D'&=\left(1-\frac{\tau}{U^2}-\frac2{U^3}\right)(2V+\tau U+1),\\
V'&=\frac{D'-\tau U'-1}{2}.
\end{aligned}
\tag{4}
$$
直接代入(2)得到
$$
\mathcal E'_\tau:\quad
V'^2+\tau U'V'+V'
=U'^3-5\tau U'-(\tau^3+7).
\tag{5}
$$
式(4)给实际 quotient isogeny
$$
\phi:\mathcal E\longrightarrow\mathcal E'=\mathcal E/\langle P_3\rangle,
\qquad \deg\phi=3.
$$
例如将(4)分母清掉后，其所用恒等式就是
$$
\left(1-\frac{\tau}{U^2}-\frac2{U^3}\right)^2
(4U^3+\tau^2U^2+2\tau U+1)
=
4U'^3+\tau^2U'^2-18\tau U'-4\tau^3-27.
$$
$U'$ 的极除子在 $O,P_3,-P_3$ 各为二阶，故映射次数为3，核恰为所列三点。微分规范准确为
$$
\boxed{\phi^*\varpi'=\varpi,\qquad
\varpi'=\frac{dU'}{2V'+\tau U'+1}.}
\tag{6}
$$
这里只取相对微分；在总空间微分中出现的 $d\tau$ 项经(3)外积后也严格消失。

必须验证 full3，不能只比较 $j$。令 $\delta^2=-3$。曲线(5)的三除多项式因式分解为
$$
\psi_3(U')=
3\left(U'+\frac{\tau^2}{3}\right)
\left(U'^3-9\tau U'-\tau^3-27\right).
\tag{7}
$$
后三次式的三个根为
$$
u_i=\tau\omega^i+3\omega^{-i}\quad(i=0,1,2),
$$
对应的六点为
$$
(u_i,4),\qquad (u_i,-\tau u_i-5).
\tag{8}
$$
余下两点的 $U'=-\tau^2/3$，且
$$
2V'+\tau U'+1=\pm\frac{\delta(\tau^3-27)}9.
\tag{9}
$$
连同原点，(8)–(9)列出全部九个三挠点，均在
$K(\tau)$ 上，$K=\mathbf Q(\omega)$。不同 $u_i$ 的两点不是互为正负，故可选作三挠基；必要时将第二基点取负，使 Weil pairing 等于固定的 $\omega$。

此外
$$
\Delta'=(\tau^3-27)^3,\qquad
j'=\frac{\tau^3(\tau^3+216)^3}{(\tau^3-27)^3}.
\tag{10}
$$
$j'$ 作为 $\mathbf P^1$ 的映射次数为12。full3 模曲线的 $j$ 映射次数同为12；(8)已给实际 symplectic full3 level structure，故其分类映射次数为1。这证明(5)是 full3 通用族在一个实际底坐标中的呈示，排除了仅由相同 $j$ 猜同构所可能遗漏的扭曲。其四个坏纤维全为 $I_3$。

特别，可直接取 Gordon–Murre/Scholl 的 full3 紧化：先紧化(5)的椭圆曲面，再对其同底自乘的全部 ordinary double points 吹起。记该光滑射影三fold为 $W_3$。全部三挠平移、两因子逆及因子交换都正则作用在这个模型上。

## 3. 全群平均的真正 Scholl 投影

令 $\iota_1,\iota_2$ 为两椭圆因子的 $[-1]$，$s$ 为两因子交换，令
$$
\vartheta_1=\frac19\sum_{T\in\mathcal E'[3]}[\Gamma_{\tau_{(T,0)}}],
\qquad
\vartheta_2=\frac19\sum_{T\in\mathcal E'[3]}[\Gamma_{\tau_{(0,T)}}].
$$
在 $CH^3(W_3\times W_3)_{\mathbf Q}$ 中定义
$$
\boxed{
\varepsilon_3=
\frac{1-s}{2}\,
\frac{1-\iota_1}{2}\,
\frac{1-\iota_2}{2}\,
\vartheta_1\vartheta_2.
}
\tag{11}
$$
这里和以后自同构以其完整图形对应作用。(11)是
$$
(\mathcal E'[3]\rtimes\{\pm1\})^2\rtimes S_2
$$
的648项 character projector：在平移上取1，在每个单独逆及交换上取 $-1$。所以
$$
\varepsilon_3^2=\varepsilon_3,\qquad
{}^t\varepsilon_3=\varepsilon_3.
\tag{12}
$$
三挠基改变或 $K/\mathbf Q$ 共轭只置换全部平移；故合并的对应在 $\mathbf Q$ 上定义。

这就是 Gordon–Murre v2 §3.3.3、§3.3.12、§4.1 中 $S_2\widetilde\pi_{1,1}$ 的 full3 特例，不是只在泛纤维上写出的八项式。该原文的 §5.1 给其实现仅为
$$
H^1\!\left(X(3),j_*\operatorname{Sym}^2R^1\pi_*\mathbf Q\right)
\subset H^3(W_3).
\tag{13}
$$
$X(3)$ 的 genus 为0、cusps为4且无 elliptic points，因此
$\dim S_4(\Gamma(3))=1$；(13)准确为两维，Hodge 型为 $(3,0),(0,3)$。

在下面的全局对应和边界论证中始终使用(11)。只有限制到光滑泛纤维的指定 Chow 群后，才证明其三挠平均可以去掉。

## 4. 同一原图形的第二个九次映射

R852 的原对应为
$$
\Gamma=\mathscr G\alpha:(A,\Pi)\longrightarrow h(W_9),
\quad A=E_0^3,\quad E_0:Y^2=X^3+1,
$$
其中全部 $b_9^*,\Pi_Z$、异常交数、原 $q_0/q_2$ 与有限系数都包含在 $\Gamma$ 中。原式为
$$
{}^t\Gamma\Gamma=9\Pi,\qquad
\Gamma_*\Omega_A=-\frac12\Omega_W,\qquad
({}^t\Gamma)_*\Omega_W=-18\Omega_A.
\tag{14}
$$

在光滑底 $B$ 上，$\phi\times_B\phi$ 的次数为9。取它的完整射影图形解消，并记对应
$$
\mathscr C:h(W_9)\longrightarrow h(W_3).
\tag{15}
$$
对两边所需的模型使用共同等变解消；$\mathscr C$ 是完整推拉，不删除基点处或坏纤维上的异常分量。置
$$
\Omega_3=d\tau\wedge\varpi'_1\wedge\varpi'_2.
$$
由(6)，在图形上准确有
$$
\boxed{\mathscr C^*\Omega_3=\Omega_W,\qquad
\mathscr C_*\Omega_W=9\Omega_3.}
\tag{16}
$$
第二式是第一式与泛型 degree9 的推拉公式。等式在全纯形式上成立，故未在延拓时引入未记录的 cusp 常数。

定义本篇的真正 Scholl 对应
$$
\boxed{\Theta=\varepsilon_3\,\mathscr C\,\Gamma.}
\tag{17}
$$
$W_9$ 的原九次来源及(15)的新九次来源不同：合成有理映射
$A\dashrightarrow W_3$ 的泛型次数为81，不能仍把它记作9。

为核交叉块，保 R852 的实际 $u=([\omega],1,1)$。在(2)和(5)上，
目标作用分别为
$$
\tau\mapsto\omega^2\tau,\qquad U_i\mapsto\omega U_i,\quad V_i\mapsto V_i,
$$
以及同式的 $U_i',V_i'$。式(4)逐项与它交换；该作用置换完整三挠群，故也与(11)交换。使用等变的完整图形，$\Theta$ 与原 $u$ 相容，而不是只在一个 affine 开集相容。

## 5. 精确八十一倍自复合及整个 Scholl 因子的 Chow 逆

R852 已在 Chow 范畴中支付
$$
(A,\Pi)_{\mathcal E}=M_+\oplus M_-,\qquad
\operatorname{End}(M_\pm)=\mathcal E,
$$
其中两条实际可逆 CM 线上的 $u^*$ 特征为 $\omega,\omega^2$。第4节的等变性因此杀去
${}^t\Theta\Theta$ 的两个交叉块；两个对角块是真正的 Chow 标量。

(11)在 $\Omega_3$ 上为1。结合(14)–(16)，
$$
\Theta_*\Omega_A=-\frac92\Omega_3,\qquad
({}^t\Theta)_*\Omega_3=-18\Omega_A.
\tag{18}
$$
同一复嵌入及其共轭分别读取两条 CM 线，所以准确有
$$
\boxed{{}^t\Theta\Theta=81\Pi.}
\tag{19}
$$
这里未以一般的实现忠实性消去未知 Chow 误差。

令
$$
Q_3=\frac1{81}\Theta\,{}^t\Theta.
$$
由(19)，$Q_3$ 为自对偶幂等元，且
$\varepsilon_3Q_3=Q_3\varepsilon_3=Q_3$。两者的实现都是(13)。为了证明它们作为 Chow 对应相同，还需支付有限维性：

合成 $A\dashrightarrow W_3$ 的次数为81；在三维特征零中解消该映射，可把来源取为从阿贝尔三fold $A$ 逐次吹起光滑点、曲线所得的 $T$，并有实际泛型有限态射 $f:T\to W_3$。吹起公式、曲线及阿贝尔动机的 Kimura 有限维性给 $h(T)$ 有限维。实际
$f_*f^*=81$ 使 $h(W_3)$ 为 $h(T)$ 的直和因子。因此 $\varepsilon_3-Q_3$ 是有限维动机上的同调平凡幂等元；Kimura 幂零定理使其为零。故
$$
\boxed{
\Theta\,{}^t\Theta=81\varepsilon_3,\qquad
(A,\Pi)
\ \underset{{}^t\Theta/81}{\stackrel{\Theta}{\rightleftarrows}}\
(W_3,\varepsilon_3).
}
\tag{20}
$$
第二处使用幂零定理的对象是已明确构造的零实现幂等元，不能推广为任意 Chow 态射的忠实性。

(20)给真正 Scholl 因子中的同构，不声称 R852 的特定 $P_9$ 与另一模型上某个预选的全局八项 projector 字面相同。

## 6. 原循环、角色与 period 全部按同一规范运输

令 $\mathcal Z_{\rm orig}$ 是 R831–R852 的实际端点最高类，保持原三个有序对、全部 Hom 系数和固定 Artin trace。令
$$
\mathcal Z_9=\Gamma\mathcal Z_{\rm orig},\qquad
\boxed{\mathcal Z_{\rm Sch}=\varepsilon_3\mathscr C\mathcal Z_9.}
\tag{21}
$$
则
$$
\boxed{\mathcal Z_{\rm orig}
=\frac1{81}\,{}^t\Theta\,\mathcal Z_{\rm Sch}.}
\tag{22}
$$
全部映射及合并投影在 $\mathbf Q$ 上定义，所以与原 finite Artin 的 point-factor 作用交换；代数系数始终作为标量。原 $\eta_j$ 的 order18 与2/3/17局部数据没有因为 full3 几何而被替换。

由(18)的 AJ 对偶方向，
$$
\Theta^*\Omega_3=-18\Omega_A,\qquad
\left(\frac1{81}{}^t\Theta\right)^*\Omega_A=-\frac1{18}\Omega_3.
$$
所以
$$
\boxed{
AJ_{W_3}(\mathcal Z_{\rm Sch})(-\Omega_3/18)
=AJ_A(\mathcal Z_{\rm orig})(\Omega_A).
}
\tag{23}
$$
原 $X_0$ 来源的3、old 返回的 $6^{-2}$、$X_1$ 的 $12^{-2}$、
$D_X=1632,D_C=816$ 继续留在 $\mathcal Z_{\rm orig}$ 和 $\mathcal Z_9$ 中。
(23)既不重选原周期，也不把 ambient degree81 当作任何一条来源曲线的次数。

## 7. 原泛纤维的完整反对称迹

取包含原固定 Artin 数据的一个有限域 $H$，令 $F=H(\tau)$。把(21)中**完整** $\mathcal Z_9$ 限制到(2)的泛纤维：
$$
z_\eta=\operatorname{res}_\eta(\mathcal Z_9)
=\sum_\rho c_\rho\operatorname{Tr}_{L_\rho/F}[P_\rho,Q_\rho]
\in CH_0(\mathcal E_\eta^2)_{\mathbf Q}\otimes\mathcal E.
\tag{24}
$$
$L_\rho/F$ 为各闭点的有限剩余域。这里的有限和来自原图形作用后的实际循环；若异常部分还有水平分量，也包含在(24)，不能只取严格变换的主曲线。所有原 source3及有限 trace 系数均已在 $c_\rho$ 中。

仅在这个 Chow 群中，可证明三挠平移恒等。对椭圆曲线 $E/L$ 及挠点 $T$，
$$
[P+T]-[P]
$$
在 $CH_0(E)=\operatorname{Pic}(E)$ 中是挠类，因而在有理系数下为零。对 $E^2$ 的任意闭点先过其剩余域写为 $(P,Q)$，分别外积上述等式再作有限迹，得到两因子的挠平移在
$CH_0(E^2)_{\mathbf Q}$ 上恒等。这个论证有指定的椭圆乘积和有理系数范围，不是对任意紧化、任意 Chow 群的断言。

同时
$$
[P]-[-P]=2([P]-[O])
$$
在椭圆的 $CH_0$ 中成立。记
$$
\langle P,Q\rangle
=([P]-[O])\times([Q]-[O]).
$$
因此真正 projector 的泛纤维限制准确给
$$
\boxed{
\operatorname{res}_\eta(\mathcal Z_{\rm Sch})
=
\frac12\sum_\rho c_\rho\operatorname{Tr}_{L_\rho/F}
\left(
\langle\phi P_\rho,\phi Q_\rho\rangle
-\langle\phi Q_\rho,\phi P_\rho\rangle
\right).
}
\tag{25}
$$
这时才可以写出裸八项式；全局的(11)仍未改变。

定义原未作三同源的迹
$$
\boxed{
\mathfrak T_\eta=
\frac12\sum_\rho c_\rho\operatorname{Tr}_{L_\rho/F}
\left(
\langle P_\rho,Q_\rho\rangle-\langle Q_\rho,P_\rho\rangle
\right).
}
\tag{26}
$$
式(25)就是 $(\phi\times\phi)_*\mathfrak T_\eta$。在光滑泛纤维，实际 isogeny 的
$$
(\phi\times\phi)^*(\phi\times\phi)_*
=\sum_{T_1,T_2\in\langle P_3\rangle}\tau_{(T_1,T_2),*}
=9
\quad\text{在 }CH_0(\mathcal E_\eta^2)_{\mathbf Q}
\tag{27}
$$
成立；最后一个等号仅用刚证明的椭圆乘积挠平移事实。因此
$$
\boxed{
\operatorname{res}_\eta(\mathcal Z_{\rm Sch})=0
\iff \mathfrak T_\eta=0.
}
\tag{28}
$$
没有用任意 chosen lift 代替闭点迹，也没有把原 finite Artin trace 与此函数域迹相混。

## 8. 从迹零到有限垂直代表：真正的 localization

对 $W_3\to\mathbf P^1_H$ 使用 Chow localization 并对开集取极限：
$$
\bigoplus_{s\in(\mathbf P^1_H)^{(1)}}
CH_1((W_3)_s)_{\mathbf Q}
\longrightarrow CH^2(W_3)_{\mathbf Q}
\longrightarrow CH_0((\mathcal E'_\eta)^2)_{\mathbf Q}
\longrightarrow0.
\tag{29}
$$
每个代表只需有限个闭点 $s$。所以(28)等价于
$\mathcal Z_{\rm Sch}$ 可由有限个 fibre divisor 推前表示。
因为(11)保持底参数且
$\varepsilon_3\mathcal Z_{\rm Sch}=\mathcal Z_{\rm Sch}$，
可再对该有限代表施同一个 $\varepsilon_3$；这不会改变类，也不会把有限和改成无限极限。

下一节精确识别此时可以留下哪些 fibre divisor。

## 9. cusp 两 ruling 与非 CM 光滑纤维全部消去

### 9.1 四个 $I_3$ cusp

full3 模型在每个 cusp 的自乘节点处有局部方程
$$
xy-uv=0.
$$
吹起该节点的异常 quadric 记为
$$
Q:\det
\begin{pmatrix}x&u\\v&y\end{pmatrix}=0
\subset\mathbf P^3.
\tag{30}
$$
其两 ruling 类记为 $\ell_+,\ell_-$。

先作全部三挠平移平均。三挠的 component 部分在各 $I_3$ 的三个分量和节点上传递作用，故平均后的 cusp $CH_1$ 由原分量的两 ruling 类，以及异常 quadrics 的两 ruling 类生成。原分量是 $\mathbf P^1\times\mathbf P^1$ 的角点吹起；其额外 Picard 生成元就是与这些 quadrics 相交的边界曲线，已包含在后一组中。

对原 ruling 子商，每个因子逆是相应 $\mathbf P^1$ 的自同构，不改变 ruling 类；平移平均后分量指标也相同。因此两反号部分在此子商为零。

异常部分必须保精确交换作用。第一个因子逆在(30)上为 $x\leftrightarrow y$，第二个为 $u\leftrightarrow v$；二者分别交换两 ruling。因子交换则为
$$
(x,y,u,v)\mapsto(u,v,x,y),\qquad
\begin{pmatrix}x&u\\v&y\end{pmatrix}
\mapsto
\begin{pmatrix}x&u\\v&y\end{pmatrix}
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{31}
$$
右换列保持每一 ruling 家族。因此两反号可能留下的
$\ell_+-\ell_-$ 被最后的 $(1-s)/2$ 严格杀掉。

这些生成元与其关系给 group-module 的稳定子群及商；character projector 在有理系数下是正合函子。因此上述两个部分都无该 character，已经证明
$$
\boxed{
\varepsilon_3\,i_{c,*}CH_1((W_3)_c)_{\mathbf Q}=0
\quad\text{对全部四个 cusp }c.
}
\tag{32}
$$
没有把“实现纯在 $H^3$”本身当成边界 Chow 群为零的理由。

### 9.2 光滑纤维的准确 Rosati 部分

对一个光滑纤维 $E_s^2$，先有限扩域使所需 endomorphism 定义。对 $CH^1(E_s^2)_{\mathbf Q}=\operatorname{Pic}(E_s^2)_{\mathbf Q}$：

- 两因子的 Picard 零部分分别来自单轴，被另一轴反号杀掉；
- 两轴的 Néron–Severi 类同样被杀；
- 余下 cross 部分由 $\operatorname{End}(E_s)_{\mathbf Q}$ 给出，交换两因子对应主极化的 Rosati 对偶。

挠平移在此 Picard 群有理系数下也恒等：其与原线丛的差由极化同态把挠点送入挠 Picard 类。因而(11)在 cross 部分的像准确为
$$
\boxed{
\operatorname{End}(E_s)_{\mathbf Q}^{\dagger=-1}.
}
\tag{33}
$$
若 $E_s$ 无 CM，此空间为零。若有 CM，则为其虚二次 endomorphism 域的 trace-zero 一维子空间。

具体选一个非零整 endomorphism $\xi_s$ 满足
$\xi_s^\dagger=-\xi_s$，以有理系数表示相应 cross divisor 为
$$
D_{\xi_s}=
\Gamma_{\xi_s}-E_s\times[O_s]
-\deg(\xi_s)[O_s]\times E_s.
\tag{34}
$$
若先用有理 endomorphism，可先乘整再归一。标准 Picard cross 对应使
$D_{\xi_s}$ 在有理系数下随 $\xi_s$ 线性，且交换两轴给
$D_{\xi_s^\dagger}=-D_{\xi_s}$；故
$\varepsilon_3i_{s,*}D_{\xi_s}=i_{s,*}D_{\xi_s}$。
这与 R854 的 trace-zero CM graph 规范相同；例如其特定阶上可取原 $c\delta$，不要求它是整 trace-zero 模的本原生成元。

把有限扩域的代表作迹并除以扩域次数，(33)–(34)也给原剩余域上的完整结论。

## 10. 同一原迹的有限 Heegner 代表判据及实际剩余门

结合(28)–(34)，得到
$$
\boxed{
\mathfrak T_\eta=0
\iff
\mathcal Z_{\rm Sch}
\text{ 在 }CH^2(W_3)_{\mathbf Q}\otimes\mathcal E
\text{ 中是有限个 CM fibre 类 }
\operatorname{Tr}(i_{s,*}D_{\xi_s})\text{ 的线性组合}.
}
\tag{35}
$$
这是一条对原实际端点的等价判据。若右侧成立，所有 cusp 项及光滑非 CM 项已按同一个完整投影消去；并非另行假定它们的 regulator 为零。

(35)仍没有证明其任一边成立。它也没有将允许出现的所有 CM fields、orders、各个有限 trace 系数缩成 R814 的指定 $K$、order34及其固定非 Dirichlet good-pair orbit。后者还需要实际循环比较；同一两维 Scholl 动机或(20)的可逆性不能替代该比较。

原 R831/R841 的 Hecke 与翻转关系可以作用在(24)的全来源上，但要使它们成为(26)的同一个函数域迹的相消，必须支付它们对真实 $\tau$、两纤维点以及全部有限系数的作用。没有将原 $W_4$ 的端点反号直接认成保持 $\tau$ 的 fibre swap；也没有从物理坐标的一个交换就推出 $\mathfrak T_\eta=0$。

本篇无新增数值计算、目标素数扫描或可重算数据。

## 11. 原文与引用范围

- [R851](R851-original-schoen-map-and-horizontal-cycle-transport.md)、[R852](R852-original-schoen-correspondence-and-exact-chow-inverse.md)：原完整图形、$-18$、九次自复合、实际 CM 可逆线及 finite Artin 运输。
- [R854](R854-original-canonical-cm-contraction-and-threefold-heegner-cycles.md)：原固定 canonical 来源的 CM graph 规范。本文没有将两个循环认同。
- B. Gordon–J. P. Murre, *Chow motives of elliptic modular surfaces and threefolds*, [作者预印本 v2](https://arxiv.org/pdf/alg-geom/9610007)，§3.3.3、§3.3.12、§4.1、§5.1；边界图形的具体处理另见 §4.4–4.5。发表题名为 *Chow motives of elliptic modular threefolds*, J. reine angew. Math. 514 (1999), 145–164，[DOI](https://doi.org/10.1515/crll.1999.069)。本篇直接读取并使用的编号是上述 v2。
- A. J. Scholl, *Motives for modular forms*, Invent. Math. 100 (1990), 419–430，Theorem1.2.1。这里所需的 $k=2$ 全群 projector 及实现结论，也由前一原文明确重建；不依赖一个未读取的扫描页。
- A. S. I. Anema–J. Top–A. Tuijp, *Hesse Pencils and 3-Torsion Structures*, SIGMA 14 (2018), 102，[作者稿](https://www.math.rug.nl/~top/HessePencil.pdf)，Theorem1.1及§§2–4。本文的实际 full3 基及三同源由(4)–(10)独立给出，不仅引用 Hesse 的一般存在性。
- S.-I. Kimura, *Chow groups are finite dimensional, in some sense*, Math. Ann. 331 (2005), 173–201，[DOI](https://doi.org/10.1007/s00208-004-0577-3)。第5节使用曲线/阿贝尔动机、吹起与直和因子的有限维性及零实现幂等元的幂零性；仍保持 R839、R852 已付的同一 Chow 范畴。
- U. Jannsen, *On finite-dimensional motives and Murre’s conjecture*, [作者机构预印本](https://epub.uni-regensburg.de/556/1/05-2006.pdf)，Theorem2.6、Proposition2.7与Corollary3.4：曲线有限维、直和/张量/直和因子封闭，以及数值平凡对应的幂零性。root亲读这些条款，供第5节可直接核查的原研究来源。
- W. Fulton, *Intersection Theory*, §1.8：第8节为该 localization 序列对底曲线开集取极限的直接应用。
