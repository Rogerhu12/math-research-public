# R133：固定停止尾的实际 D0、完整有源 Schur 与全非线性 incoming 接线

2026-11-14，visible-exact / newton_source。

**状态：已证明。** 本篇在
[固定第四 connector 的新对象](R133-supplement-fixed-stop-connector-and-complete-regular-ports.md)
上重新构造完整原点 Schur 逆，保留第四线的真实非零缺口。
新对象的 raw404、全部两迹、有限 connector、弱源和 mean 都在下文
逐项消费。结果包括有明确角宽损失的内部 Green、同宽的完整边界投影、
真正非线性 incoming 固定点及其未消去的完整剩余。

本篇不证明更新后非径向尾的同权相对逆，也不将 incoming 固定点
称为完整远端方程的解。所有源/边界范围和未闭合的方程在正文中明列。

## 1. 唯一对象、一次 good-angle 选择和真实空间

固定前篇 F.1–F.4 的同一基点、停止长度、尺度、完整 connector 和
baseline 双 bump 曲线。安装第53束的实际控制
$\Pi=(\Gamma,s,\Xi)$，仍令
$$
 \varepsilon_d=2^{-193532}
       +2^{-22}\|\gamma_1-\gamma_1^0\|_\infty
       +2^{-8}\|\gamma_2-\gamma_2^0\|_\infty<2^{-35}.
 \tag{D.1}
$$
这是 cut128 的物理高度对数斜率误差。前篇已经将它经过同一个
不再重停的全部 connector 和实际双 bump，给出
$$
 p_B=-\lambda_4(B)/4\in[5/4,8/5],\qquad
 |p_B-\omega|\le60\omega\varepsilon_d .
 \tag{D.2}
$$
第四模不是被重新设置成 $p_B=\omega$。

对每个固定实际径向参数，前篇重新证明了新全部允许线的 good-angle
集合 $G_\Pi$，其测度至少 $1-83/16384$；第四模始终不在坏集。
取一个真正 $t\in G_\Pi$，随后固定它。这里不使用旧 retuned 对象的
good parameter。

也可以在控制参数与 $t$ 的产品空间上选择一次。真实允许线对参数的
已付连续性和逐模角不等式使好集合可测；对任一 admissible 控制
Borel 概率测度，Fubini 给产品好集合测度至少 $1-83/16384$。
选择一个 $(\Pi,t)$ 后，局部控制微分保持 $t$ 不变。
这不构造一个所有控制共用的 good $t$，也不声称有连续 good-$t$ 选择。
无限模式的原点好角没有被免费转授给每个非零标签背景。

所有数字覆盖前篇的完整仿射 $\eta$ 区间。有限 body/自然 graft、
$a_*,z_*,\omega$ 和
$$
 B=2^{24}-25/8,\qquad L=\omega B
 \tag{D.3}
$$
与已证真实长段完全相同。主体 $\nu$ bump 的支持在 $(.05,.18)$，
不改变这些入口。下面非mean频率为 $m\in4\mathbb Z\setminus\{0\}$，
$M=|m|$。

内部标签、强两迹和残差空间分别为
$$
 \|\mathbf a\|_\beta=\sum_{m\ne0}e^{\beta M}|a_m|,\qquad
 \|(f,k)\|_{\mathfrak C_\sigma}
   =\sum_{m\ne0}e^{\sigma M}(M^2|f_m|+M|k_m|),
$$
$$
 \|g\|_{\mathfrak Z_\sigma}
   =\sum_{m\ne0}e^{\sigma M}M|g_m|.
 \tag{D.4}
$$
内部标签仍在真正的层 $b_m$ 上定义，不是 $B$ 切口的任意高度。
逐模 Euclidean 两迹会在证明中显示；将其换为 (D.4) 时付完整
$\sqrt2$ 因子。mean 高度、mean 总通量和 holonomy 行单独保留。

第53束 C.1、C.24–C.28 给本对象自己的全两行算子
$$
 X=\mathcal H\mathbf a+\mathcal G\mathfrak f,\quad
 \ell\mathcal H=I,\quad \ell\mathcal G=0,\qquad
 \|\mathcal H\|<9,\quad \|\mathcal G\|<2^{16}.
 \tag{D.5}
$$
这里先取径向 supremum 再作全 Fourier 求和；全部 high 区、
两次接缝和真实低窗都在内。仅有限 connector 的停止规则改变，
不改变这个 cut128 以内的已证构造。

## 2. 新第四行和其余全部行的真正横截

令 $Y=(y,y_u/M)^T$。在 $B$ 的正参考高度两迹仍准确为
$$
 \binom f{k/M}=-16\omega h(B)^2J_MY,\qquad
 J_M=\begin{pmatrix}\omega&-1/M\\ \omega/M&-1\end{pmatrix}.
 \tag{D.6}
$$
若改用物理 $Z$ 高度，两个状态、标签、源同时取反；
下面线性算子与范数不变。不能只翻高度一行。

设 $c_M=\coth(ML)$。真正长段零外 Dirichlet 行是
$$
 (\mathsf D_0\mathbf a)_m=k_m+Mc_M f_m,\qquad
 \mathsf D_0=E\mathcal H,\quad E(f,k)=k+\mathsf C_L f,\quad
 (\mathsf C_L f)_m=Mc_Mf_m .
 \tag{D.7}
$$
这里保留有限 $L$ 的 $c_M$；准确有 $0<c_M-1<2^{-100}$。

第四模由 (D.2) 给 $y_u=-4p_By$，且 $y$ 不消失，所以
$$
 t_4:=\frac{k_4}{4f_4}
     =\frac{\omega/4+p_B}{\omega+p_B/4}>0,\qquad
 |t_4-1|\le45\varepsilon_d .
 \tag{D.8}
$$
分母严格大于 $\omega$。对于任意 $t>0,c\ge1$，
$(c+t)^2-(1+t^2)=c^2-1+2ct\ge0$，故
$$
 |c_4f_4+k_4/4|
 \ge (|f_4|^2+|k_4/4|^2)^{1/2}.
 \tag{D.9}
$$
这条横截比后面的统一门更强，而且使用的是实际 $t_4$。

对于 $M\ge8$，新 good-angle 给
$|\sin\angle(Y,(1,\omega))|\ge2^{-39}$。
准确有
$$
 (1,1)J_M=(1+1/M)(\omega,-1),\qquad
 \|J_M\|_{2\to2}\le\sqrt{(1+\omega^2)(1+M^{-2})}.
$$
于是
$|f+k/M|\ge2^{-39}|(f,k/M)|_2$。
再保留 $(c_M-1)f$，
$$
 |c_Mf+k/M|
 \ge(2^{-39}-2^{-100})|(f,k/M)|_2
 >2^{-40}|(f,k/M)|_2 .
 \tag{D.10}
$$
(D.9)–(D.10) 给本对象的完整逐模结果
$$
 |(f_m,k_m/M)|_2\le2^{40}|(\mathsf D_0\mathbf a)_m|/M .
 \tag{D.11}
$$
它没有除以可能为零的高模高度，也没有把新单位标签列的振幅换成旧值。

## 3. raw404 到真正内部标签：全部1850角宽重新支付

从 (D.6) 直接有
$$
 \|J_M^{-1}\|_\infty\le4/3,\qquad
 h(B)^2\|Y(B)\|_\infty
 \le\frac5{84}|(f,k/M)|_2
 <\frac1{16}|(f,k/M)|_2
 \le2^{36}|g_m|/M .
 \tag{D.12}
$$
极小半径在完整两迹中准确消去。以下是本对象实际路径的每一段：

* 完整双 bump 长度 $25/8$，费用 $e^{4M(25/8)}$。
* 固定的整个 connector 仍满足 R74 §5 的原显示宽盒，费用 $e^{1143M}$；
  包括准备段、放大段、所有 quintic 和最后停止段。
* 真 cut128 转换为
  $\zeta_{128}^{-1}\|V^{\rm ref}_{m,128}\|_\infty
  \le16\delta_{\rm tail}^{-15/4}
  H^2\omega_e^2b_{\rm tail}^{-10}M^4\|Z_m\|_\infty$。
* 固定几何仍有
  $H^2\omega_e^2<8(2^{360})^3h(T)^2$、
  $h(T)^2/h(B)^2\le e^{3(25/8)}$、$b_{\rm tail}>1$、
  $\delta_{\rm tail}>2^{-132}$。
* 新控制 profile 自己的 C.35 已证
  $1/9<\mathfrak w_{m,\Pi}<e^{391M}$，
  $\tau_{128}+391<404$；所以这里使用新 raw404，
  包含所有新坏前缀，不引用旧尾的允许线。

逐项相乘，得到
$$
 |a_m|\le
 2^{1618}M^4 e^{(3119/2)M+75/8}|g_m|/M .
 \tag{D.13}
$$
二进制指数为 $7+495+1080+36=1618$；
线性角宽为 $1143+25/2+404=3119/2$。
对全部 $M\ge4$，$\log M/M$ 递减，$\log2<7/10$，故
$$
 \frac{3119}{2}+\frac{5663}{20}+\frac75+\frac{75}{32}
 =\frac{295423}{160}<1850 .
$$
从而每个实际对角系数不为零，逐项反解给
$$
 |a_m|\le e^{1850M}|g_m|/M,\qquad
 \boxed{\ \|\mathsf D_0^{-1}g\|_\beta
       \le\frac1{16}\|g\|_{\mathfrak Z_{\beta+1850}}\ } .
 \tag{D.14}
$$
序列不等式对 $\beta\ge0$ 成立。后文构造具有真实正角宽的完整
finite-connector 场时取 $\beta\ge224$。这不是无角宽损失的逆；
新第四系数也没有与旧系数做未支付的振幅比较。

## 4. 同宽完整两迹投影与全部有限传播

将强两迹记为 $x_m=(M^2f_m,Mk_m)^T$，
$e_M=(c_M,1)$，$x_{H,m}$ 是本对象自己的单位标签列在 $B$ 的值。
(D.11) 给
$$
 \frac{\|x_{H,m}\|_1}{|e_Mx_{H,m}|}
 <2^{42},\qquad
 \Pi_m=I-\frac{x_{H,m}e_M}{e_Mx_{H,m}},
$$
$$
 \Pi_m^2=\Pi_m,\quad e_M\Pi_m=0,\quad\Pi_mx_{H,m}=0,
 \qquad \|\Pi_m\|_{1\to1}<2^{44}.
 \tag{D.15}
$$
同一个极小标签振幅在分子分母中相消。
对所有 Fourier–Wiener 权常数相同；两分量 Hilbert norm 可取 $2^{45}$。
没有将仅径向标签逆的1850宽差插入这个已经闭合的边界商。

固定 connector 的真实 balanced 四态证明只依赖其几何盒，
不依赖某一输入属于允许线。第 W.12–W.18 所用
$L_a<505/4,L_s<1/2,L_b<75/16$、
平台 $A=3$、短段 $A\in[-7,3]$、双 bump $A\in[7/8,9/8]$、
$w<1,w/a<5/18,a<7\cdot10^{-6}$ 全部未变。
其 cut128 小因子 $2^{-467}$ 与完整有限增长 $2^{20}$ 仍给
$$
 \|T_BX\|_{\mathfrak C_{s_\beta}}<2^{-447}\|X\|_{\mathcal X_\beta},
 \qquad s_\beta=\beta-\frac{88823}{400}.
 \tag{D.16}
$$
该证明保完整两行、mean 根及有限导数的 $2683/800>3$ 宽度余量。
在复标签球上，固定的实有限系数不改变该全纯收缩的球与费用。

对 $X^p=\mathcal G\mathfrak f$，
$$
 \|T_BX^p\|_{\mathfrak C_{s_\beta}}<2^{-431}\|\mathfrak f\|_{\mathcal F_\beta},
 \qquad
 \|\Pi T_BX^p\|_{\mathfrak C_{s_\beta}}
 <2^{-387}\|\mathfrak f\|_{\mathcal F_\beta}.
 \tag{D.17}
$$
$\Pi T_BX^p$ 是真实零外 Dirichlet 条件的完整 $B$ 两迹。
它不是将 particular 丢弃后留下的齐次线。

## 5. 新 controlled 尾的准确 weak 源及两种通量

采用本对象的物理变量
$a_{\rm phys}=\rho r,h=\rho H,t_{\rm raw}=\log r,y=\sqrt{12}t_{\rm raw}$、
$w=\mu_jp_*/r^7$、$\mu_0=w/(\rho r)$，并固定源号数
$$
 (\mu_0h_t)_t+\mu_0Qm^2h=f-(F^t)_t-imF^\theta .
 \tag{D.18}
$$
总通量为 $\pi=\mu_0h_t+F^t$。
对 $\nu_m=m^2(m^2-1)/12$，完整 canonical 两行源准确为
$$
 \mathcal J_m=
 \binom{-\nu_mr^4F^t/(\sqrt{12}\mu_jp_*)}
 {r^4(f-imF^\theta+m^2F^t)/(12\mu_j)} .
 \tag{D.19}
$$
这是第53束 C.40–C.43 的直接微分：把
$r^4F^t/(\sqrt{12}\mu_j)$ 加入第二状态后，
所有 $F^t_t$ 项准确相消，第一行同时产生显示的源。
ordinary $f=w^2e,F=0$ 时，
$\mathcal J=(0,\mu_jp_*^2e/(12r^{10}))$，两个 $p_*$ 都在。

采用 C.44 的完整 norm
$$
 \|\mathcal J\|_{\mathcal S^w_{1,\beta}}
 =\sum_{m\ne0}(1+M)^{312}
 \sup_{j>128}\frac{e^{M(\tau_{j-1}+\beta+\beta_j^c)}}{\zeta_{j-1}}
             \int_{I_j}\|\mathcal J_m(y)\|_\infty\,dy ,
 \tag{D.20}
$$
未改层用原 $\beta_j$。新 C.45 给
$$
 \|\mathfrak f\|_{\mathcal F_\beta}
 \le2^{482}\|\mathcal J\|_{\mathcal S^w_{1,\beta}} .
 \tag{D.21}
$$
这里是 $2^{482}$，不能继续使用旧 profile 的 $2^{450}$。
(D.17) 的两个 source-boundary 费用因此分别是 $2^{51}$ 和 $2^{95}$。

若输入需要 bare flux，须给真实端点 $F^t$。在 canonical 状态中令
$Q_F=(0,r^4F^t/(\sqrt{12}\mu_j))$，连同每层准确规范；
则
$$
 X^{\rm tot}=X^{\rm bare}+Q_F,\qquad
 \mathbf a^{\rm tot}=\mathbf a^{\rm bare}+\ell(Q_F),\qquad
 \|\ell(Q_F)\|_\beta\le2\|Q_F\|_{\mathcal X_\beta}.
 \tag{D.22}
$$
先解总通量方程，再减 $Q_F$ 与 $\ell(Q_F)$。
裸端点荷不能从内部 $L^1$ weak-source norm 自动取得。
以下数值源传播假设源在实际 mixed tail 中，finite connector 与长段无源；
包含所有当前 compact/浅层 $\Gamma$ metric 方向。
另给有限段源时须另加其真实传播列，不能从本假设删除它。

mean 在原变量中独立满足
$$
 \pi_0(t)=\int_{t_f}^t f_0(s)\,ds,\qquad
 H_0(t)=\lambda+\int_{t_f}^t\frac r w(\pi_0-F^t_0)\,dt .
 \tag{D.23}
$$
$\lambda$ 是唯一平盘高度。固定有限无源段继续同一 flux；
未改长段的物理 mean 高度 $h$ 跨度含准确 $4\omega L\,\pi_0$，没有指数筛选。
仅这些积分收敛只授 mean 解；$C^2$ 平端须另满足 C.46 的端点衰减。
ordinary 源可用完整 C.47 的 $\mathcal S_1,\mathcal S_2$ 条件，
其含 mean 的二 jet 界为
$2^{512}626^{313}\epsilon\delta_j^{19/4}
(\|X\|+\mathcal S_1+\mathcal S_2)$。不能由任意 weak $L^1$ 源声称 $C^2$。

## 6. 新真实 regular affine 列：完整 Wronskian 费用

取本对象的真实平尾解 $q_m$，在长段外端按 grounded 两迹归一
$v(q_m;0)=1,p(q_m;0)=-\gamma_m^\ddagger$。
前篇新 good-angle 与未改长段给
$\|Y(q_m;B)\|_2<2^{42}e^{-ML}$，第四模也在内。

准确同一两迹转换为
$$
 v=A_0y-4y_u/M^2,\quad p=-y+4y_u/A_0,\qquad
 h=4\omega y-4y_u/M^2,\quad p_h=y-y_u/\omega .
$$
相对于 $Y=(y,y_u/M)$，两行 determinant 的绝对值是
$4M(1-M^{-2})$；不能遗漏这个 $M$。于是
$$
 r_m:=p_m(0)+\gamma_m^\ddagger v_m(0)
 =4M(1-M^{-2})\det(Y(q_m;B),Y^p_m(B))
 =-(h_qp_h-p_qh)(B).
 \tag{D.24}
$$
加任意齐次允许线不改变该值。完整源的另一表示为
$$
 r_m=-\int_{\rm mixed\ tail}
 [q_hf-imq_hF^\theta+(q_h)_tF^t]\,dt ,
 \tag{D.25}
$$
内部点荷加其真实 Wronskian 跳量。若使用 $q_H=q_h/\rho$，
右边整体乘 $\rho$；无量纲与物理高度不能混用。

积分绝对收敛时用显示公式。一般 (D.20) 数据沿实际
$\mathcal G_0$ 每个绝对可和输出行、再沿 norm 收敛的 Neumann 级数
取极限，指定同一外 functional。这里不假设有限径向支集在
$\ell^\infty$ 中稠密；有限 Fourier 截断才用已给 $\ell^1$ 收敛。

由真两迹逆
$\|Y^p(B)\|_2<a(B)^2(|f^p|+|k^p|/M)/8$ 和 $a(B)^2<1$，
$$
 M|r_m|<2^{41}e^{-ML}(M^2|f^p_m|+M|k^p_m|).
$$
代入 (D.17)、(D.21)，得本对象新的完整合同
$$
 \boxed{\ 
 \|r\|_{\mathfrak Z_{L+s_\beta}}
 <2^{-390}\|\mathfrak f\|_{\mathcal F_\beta}
 <2^{92}\|\mathcal J\|_{\mathcal S^w_{1,\beta}}\ } .
 \tag{D.26}
$$
旧 weak 源的 $2^{60}$ 在这里被正确替换；affine 列没有置零。
外 $\gamma_m^\ddagger$ 含实际第四缺口及其全部参数导数。

## 7. 真正内部 exterior Green、完整强源及边界荷

在 $\mathcal F_{\beta+2080}$ 上定义
$$
 X^{\rm reg}=\mathcal G\mathfrak f
       -\mathcal H\mathsf D_0^{-1}E\mathcal G\mathfrak f,\qquad
 \mathbf a^{\rm tot}=-\mathsf D_0^{-1}E\mathcal G\mathfrak f .
 \tag{D.27}
$$
代入 (D.5)、(D.7) 同时恢复全部内部两行和 $EX^{\rm reg}=0$。
齐次唯一性来自真实 $\mathsf D_0$ 无零对角。
非zero exterior 负荷 $g$ 分别加
$\mathcal H\mathsf D_0^{-1}g$ 与 $\mathsf D_0^{-1}g$；
bare 状态再按 (D.22) 转回。

实际输出宽为
$\beta+2080-88823/400=\beta+1850+3177/400$。
由 $c_M<2$，$\|E\mathcal G\|<2^{-430}$，并且
$$
 \frac1{16}e^{-4(3177/400)}<2^{-49}
$$
（$4(3177/400)>45(7/10)>45\log2$）。
因此全部真正强合同是
$$
 \|\mathbf a^{\rm tot}\|_\beta
 <2^{-479}\|\mathfrak f\|_{\mathcal F_{\beta+2080}},\qquad
 \|X^{\rm reg}\|_{\mathcal X_\beta}
 <2^{17}\|\mathfrak f\|_{\mathcal F_{\beta+2080}},
$$
$$
 \|\mathbf a^{\rm tot}\|_\beta
 <8\|\mathcal J\|_{\mathcal S^w_{1,\beta+2080}},\qquad
 \|X^{\rm reg}\|_{\mathcal X_\beta}
 <2^{499}\|\mathcal J\|_{\mathcal S^w_{1,\beta+2080}} .
 \tag{D.28}
$$
mean 按 (D.23) 联立，不乘1850角宽。

若同时有真实长段 Jacobi 源 $e$，令
$q_D=(\mathcal G_De)_t(0)$ 是其实际内端 Neumann particular。
尾源的真正 $B$ 两迹记为 $(f^p,k^p)$。联立标签行准确为
$$
 \mathsf D_0\mathbf a
 =\mathsf S_L f_*+q_D-(k^p+\mathsf C_Lf^p)+g_{\rm interface},
 \quad(\mathsf S_Lf)_m=Me^{2L}\operatorname{csch}(ML)f_m .
 \tag{D.29}
$$
$g_{\rm interface}$ 按物理迹号数输入，不能删除。
若给定 grounded density 源，须先作已经证明的实际 normal/shear
转换；(D.29) 不把任意标量源冒作完整向量源。

## 8. 同 fixed-stop 对象上的全非线性 joint 图

现在将控制限制到第55束的 phase-annihilator 域
$\|\Xi\|_{\ell^\infty(C^4)}<2^{-64}$ 并作其真实两参数径向补偿。
该内部两相位/KAM 及全标签构造位于 cut128 以内，所以固定
外 connector 的停止规则不改变其证明。保留其实际联合小球
$$
 A_*=2^{-262148},\qquad
 \|\mathbf a\|_{224}<A_*,\qquad \|X\|<16\|\mathbf a\|_{224},
$$
$$
 \Gamma^*(T_\phi\mathbf a,\Omega)=\Gamma^*(\mathbf a,\Omega),
 \qquad D_{\mathbf a}\Gamma^*(0,\Omega)=0 .
 \tag{D.30}
$$
最后一式由全部非mean基、相位不变性和标签空间稠密性得到；
没有删除 mean 小根。

在 radial $\bar\Gamma(\Omega)$ 处按第1节选择 $t$ 一次，
之后固定 $t$ 和停止长度。对于所有非zero $\mathbf a$，
沿**同一固定 finite geometry** 传播真实 cut128 数据。
(D.16) 的 nonlinear 收缩输入和球保持，故
$$
 \|f_B(\mathbf a)\|_{\dot A^2_{\sigma_B}}
 +\|k_B(\mathbf a)\|_{\dot A^1_{\sigma_B}}
 <2^{-443}\|\mathbf a\|_{224},\qquad \sigma_B=777/400 .
 \tag{D.31}
$$
这一步同时付全未知 Fourier 尾和 mean，不靠原第四等式。
因 (D.30)，
$D_{\mathbf a}(k_B+\mathsf C_Lf_B)(0)=\mathsf D_0$
正是前面重新支付的径向 Jacobi 行。
当外 incoming 非zero 时，整个 $\mathcal F_c$ 的导数还含 incoming
反馈，不能把该导数直接叫 $\mathsf D_0$。

## 9. 真正 incoming 首消、帽反馈与准确剩余

先允许 $c$ 是已证周期正帽的完整输入。对当前 ac1d5b98… 中心的
$R=25/8$ 输入，须另付真正解析角宽；只有小 $A_0$ 不能免费转授旧
$\sigma>.069$ 的帽输入。下面实际完成这一步。

[当前完整物理系数包络](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)
S.7 给两种频率号的全部模式
$|\widehat Z_{4j}|\le4|j|P e^{-4|j|d}/5.8$，
$P=1.480385\cdot10^{-11}$、$d>.124999999985$。
取 $\sigma_a=1/16$、$x=779/1000$；准确正 Taylor 下界证明
$e^{-4(d-\sigma_a)}<x$，故
$
 \|Z\|_{A^0_{\sigma_a}}
 \le\frac{8P}{5.8}\frac{x}{(1-x)^2}
 <3.26\cdot10^{-10}<z_a:=3.3\cdot10^{-10}.       \tag{D.31a}
$
这里不是有限 moving Fourier 估计，而是原物理无限尾的完整求和。

在这个明确解析球取 $r_B=2^{-60},r_f=10^{-8},F=r_f+r_B$。
同一 $C\to f_*$ 真长段方程的 Fourier 指数权满足卷积常数1，
原 mean 小根/全部 Green 因此保持其原费用。实际有理门为
$
 9z_a+2^{-512}r_B+9\,2^{12}F^2<r_f,\quad
 36\,2^{12}F<1/512,\quad
 2F<2^{-25},\quad6F<2^{-20}.                    \tag{D.31b}
$
直接在 $A^0_{\sigma_a}\to\dot A^2_{\sigma_a}$ 构造完整收缩。
所得解同时属于原 unweighted 大球；完整 $C$ 逆与原 long-BVP
唯一性把它识别为当前已存在的真实端口图。
所以原更紧的实际 $A_0$、Robin 和 mean 残差原样成立，
不是把新较宽球的粗值替换成较小的实际数。

两类输入现在都具有真正的完整周期长段图
$$
 f_*=\Phi(c,f_B),\qquad
 \|f_*\|_{\dot A^2_\sigma}\le r_f=10^{-8},\quad
 \|f_B\|_{\dot A^2_\sigma}\le2^{-60},\quad
 \|D_{f_B}\Phi\|<2^{35}.
 \tag{D.32}
$$
旧帽取其原 $\sigma$；当前 ac1 输入取新支付的 $\sigma=\sigma_a=1/16$。
$\sigma<1/8<\sigma_B$ 是原物理角宽，不是标签空间权。
$D_{f_B}\Phi$ 的 Cauchy 圆只在实际独立 $f_B$ 的半球取值；
所有实际 incoming 反馈都严格在此半球。
当前实际端口的独立 mean/Robin 残差按前篇保留，
不因本 incoming 构造已经消失。

相同的真实长段给完整 nonlinear incoming
$$
 g_*(f_*)=K_{B,\perp}(0,f_*),\quad
 \|g_*\|_{\mathfrak Z_S}<18\|f_*\|,\quad \|Dg_*\|<24,
$$
$$
 S=\sigma+7L/16>10724906.836755168,\qquad
 7L/16>10724906.774255168 .
 \tag{D.33}
$$
这是已构造的变角宽全 PDE 解及其唯一性识别，不是有限模推断。
把 (D.14) 用于新实际 $g_*$，最小非零频率4给
$$
 \|\mathsf D_0^{-1}g_*(f_*)\|_{224}
 <2^{-60000000}\|f_*\|,\qquad
 \|D(\mathsf D_0^{-1}g_*)\|<2^{1-60000000}.
 \tag{D.34}
$$
例如
$4(S-2074)>42891331.347020672$，
$\log(9/8)<1/8$、$\log2<7/10$ 已足付这些严格指数；
没有将下溢数值0当上界。

(D.31) 在真实 $A_*$ 复球全纯；在 $A_*/4$ 球取
$A_*/2$ Cauchy 圆，得 $\|Df_B\|<2^{-442}$。
于 $R_a=2^{-60000000}$ 球重新定义
$$
 \mathcal I_c(\mathbf a)
 =\mathsf D_0^{-1}g_*(\Phi(c,f_B(\mathbf a))).
$$
其像小于 $R_ar_f$，反馈率小于
$2^{1-60000000+35-442}=2^{-60000406}$。
故存在唯一真正全频
$\mathbf a_c^{\rm inc}$，与同一尾图、帽图和长段在实际
$f_B(\mathbf a_c^{\rm inc})$ 上同时取值。其相位族保留同一目标，
因 (D.30) 与唯一性成立。

写 $f=f_B(\mathbf a)$。未解完整方程准确为
$$
 \mathcal F_c(\mathbf a)
 =k_B(\mathbf a)-K_{B,\perp}(f,\Phi(c,f))
 =R_T(\mathbf a)-E_B(f)-M_B(f,f_*),
$$
$$
 R_T=k_B+\mathsf C_Lf_B-\mathsf D_0\mathbf a,\quad
 E_B=K_{B,\perp}(f,0)+\mathsf C_Lf,\quad
 M_B=K_{B,\perp}(f,f_*)-K_{B,\perp}(f,0)-g_*(f_*).
 \tag{D.35}
$$
完整剩余三项按实际空间分别估计：

* (D.31) 与真实 $A_*$ 球的 Cauchy 余项给
  $\|R_T\|_{\mathfrak Z_{\sigma_B}}
  <2^{261710}\|\mathbf a\|_{224}^2$。
  不能借旧固定参数 $1/64$ 大球缩小该常数。
* 同一个真实 long Green 的16 lift和 $2^{14}r_*=1/64$ 反馈
  给 $\|h(f,0)\|_{\mathcal Y}<17\|f\|$；
  原完整两端迹 $2^{13}\|h\|^2$ 因而给
  $\|E_B(f)\|_{\mathfrak Z_\sigma}<2^{22}\|f\|_{\dot A^2_\sigma}^2$。
* 同一个实际 S.29 的全纯 mixed 列给
  $\|M_{B,\perp}\|_{\mathfrak Z_\sigma}+|M_{B,0}|
  \le25\,2^{27}e^{-7L/4}r_f\|f\|_{\dot A^2_\sigma}$。
  这是包含 mean 的真混合项，不是将 $f_B$ 置0。

由 $\|\mathbf a_c^{\rm inc}\|<R_ar_f$，这些新实际项满足
$$
 \boxed{\ \|\mathcal F_c(\mathbf a_c^{\rm inc})\|_{\mathfrak Z_\sigma}
          <2^{-119738000}\ } .
 \tag{D.36}
$$
该量没有被置0。$R_T$ 只在 $\sigma_B$ 支付，mixed 项在 $\sigma$；
它们均不是 (D.14) 所需的2074角宽输入。
所以 (D.36) 不能再次直接送入 $\mathsf D_0^{-1}$ 来声称完整收缩。

## 10. 平均行、fixed-stop 控制源和真正的剩余任务

非线性尾与长段各自的 mean 斜率都是完整非mean两迹的同一个
holonomy 小根。只有 (D.35) 真正为0时，同 $f_B$、同 $k_B$
才使两小根相等；不能预先删除这个 mean 缺口。

平均高度保留
$$
 v_{0,B}=\lambda+\int_{\rm flat}^{B}awK_0\,dt,\qquad
 \Delta[v_0(L)-v_0(0)]=\int_0^L aw\,\Delta\mu\,dt ,
$$
$$
 |\Delta[v_0(L)-v_0(0)]|
 \le\frac{aw(L)}{165}(1-e^{-15L/4})\|f_*\|,\qquad
 |\Delta K_{B,0}|\le e^{-7L/4}\|f_*\|/44.
 \tag{D.37}
$$
高度跨度不乘远端的指数。唯一 $\lambda$ 只对齐一个整体高度；
另一端高度与真实 flux 是输出。

固定物理 $t_{\rm raw}$ 和固定尺度时，所有 compact/slide/两 $\Gamma$
方向用第53束的真正
$$
 \psi=\delta\log p_*,\quad
 \delta Q=-\psi_t,\quad
 \delta G=\mu_0\operatorname{diag}(\psi,\psi_t-Q\psi),\quad
 P\delta h=-\operatorname{div}(\delta G\nabla h).
 \tag{D.38}
$$
其中 slide 的 $\psi=(Q-7)\delta\ell$ 包括当前 profile；
形状项和两参数项都加回。现在 connector 停止与 $\rho$ 的导数为0，
但 $\delta G$、mean 电阻
$-\int\psi\mu_0^{-1}dt$、完整 weak 两行 (D.19) 及平盘高度变化
均不为0。若另改 $t$，其双 bump/高度源也须另外加入。
在非径向背景必须微分完整 Darboux 方程与 mean 小根；
径向 (D.38) 不能冒充更新后 Jacobi 系数。

本篇已在新 fixed-stop 对象上闭合原点强逆、完整 radial affine source、
同宽 $B$ 投影、2080宽差的内部 Green 和全 nonlinear incoming 首消。
下一实际方程仍是 (D.35) 在正确完整空间中的消除，并与主体两迹、
真实外 mean 和整体几何联立。这里没有把旧 retuned 逆或原点
$\mathsf D_0$ 当作未证明的 updated mixed inverse。

## 11. 可重算的精确预算

配套程序
[完整有理预算](../scripts/fourfold_regular_fixed_stop_D0_sources.mjs)
仅使用 BigInt 准确有理数、严格交叉相乘和已证明的单调指数比较。
其
[实际 V8 执行报告](../notes/2026-11-14-R133-fixed-stop-D0-and-complete-source-budget.json)
绑定本篇、前篇及全部实际输入的 SHA256/Git blob。
指数 $2^{-60000000}$ 等保留为带指数的严格界，不转成浮点0。

原 unavailable Python 环境没有被声称恢复。此报告只证明本篇明确的
代数、宽度和数值预算；没有新 finite body BVP、adjoint trial 或
updated nonlinear inverse 的执行主张。
