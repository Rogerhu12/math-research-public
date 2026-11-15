# R315：二次高度端芽的全角反正切平方门与真实有序 history 支付

日期：2026-11-15。**完整纸面存在性证明；没有运行求积、符号程序、频率扫描、人工检查或研究计算。**

[R312](R312-quadratic-height-ports-and-rational-arctangent-logarithmic-ruling.md)从实际几何起点安装
$h=h_e(1+\varepsilon\sigma^2),k=\kappa,\omega=\omega_e$，并将完整偶 ruling 分成有理、$E$、$E^2$、$\log(1+\varepsilon\sigma^2)$ 四类。其三条 $E^2$ 门并非因为“只有一个字母”自动为零。

本稿在同一个新实际几何上，给出真紧、非退化第一圆，准确支付**全部角度的三条 $E^2$ 门**。关键是原尾补偿后的新有限 $C^2$ 观测，以及四个真实交替微包产生的三维正锥。所有幅度和频率最终均有限，旧三矩和完整第三 range 同时保留。

从构造之初还可保持原 E8 全部交换子面积为零。于是新对数门中由有序第二 history 产生的部分全部清掉；剩下的原 local-third residue 仍明确保留。没有把这一步称为完整 fourth、period 或主几何目标完成。

来源：[R73 原八矩与 chain](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R183 完整第三复制](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R259 原 tail 与 sl2 表](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R277 低阶观测纤维](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md)、[R280 三个真实矩面积](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R281 解析母包](R281-analytic-packet-fibers-and-finite-canonical-end-germ-conditions.md)、[R293 任意初选有限观测](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)、[R294 原 Green 补偿](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)及 R312。

## 1. 固定新端芽及第一批原门

固定 R312 从起点选定、实际安装的正参数 $h_e,\varepsilon$ 与 $\kappa\ne0$。共同平移 profile 坐标后，$\omega=0,d=-\kappa$，记
$$
K=1+\kappa^2,\qquad
E(\sigma)=\frac{\arctan(\sqrt\varepsilon\,\sigma)}{\sqrt\varepsilon}.
$$
采用原八方向
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\
P_1=\Phi_{p_1},\ T=\Phi_{t_1},\ V=\Phi_{p_2}.
$$
唯一反正切方向准确为
$$
\boxed{
B=aR-2eL+eU+tT,\quad
a=\frac{K(\varepsilon-2K)}{32h_e^2},\
e=\frac{\kappa K}{4h_e},\
t=-\frac{\varepsilon}{4}\ne0.
}
\tag{1}
$$
这里 $e,t$ 是本稿常系数，不是 R56 的移动 $e=hx-\kappa$ 或物理参数。

原三个 profile 配对为
$$
I_0(u,v)=\int u''v'',\quad
I_1(u,v)=\int xu''v'',\quad
I_2(u,v)=\int(x^2u''v''+2u'v').
\tag{2}
$$
同一个右锚 $Jw(x)=\int_x^{r_*}w$ 始终保留。令
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f^2-\phi_\theta^2.
$$
要支付的三个完整门为
$$
\boxed{
q_j(\theta)=-I_j(BD_\theta,BD_\theta)
+2I_j\{\phi_\theta,B(\phi_\theta,BD_\theta)\}=0,
\quad j=0,1,2.
}
\tag{3}
$$
它们正是 R312 的 $E^2$ 系数，不加入旧 Gaussian 幂独立性或旧单字系数。

## 2. 新方向的真实尾及全部 polynomial outer 作用

对实紧微包 $u$，记 $\mathbf m=(m_0,m_1,m_2)=\mathbf I(u,u)$。R259 原八表直接给
$$
\boxed{
p_B(\mathbf m)(x)=\frac{e m_0}{2}x^2+b(\mathbf m)x,\qquad
b(\mathbf m)=a m_0+e m_1+t m_2.
}
\tag{4}
$$
常项准确相消；没有把整个输出 $Bu^2$ 假称为这个多项式。它仅在微包左侧等于(4)，右侧为零。

为补足 R294 先前六方向表中未单列的 $T$，其原式为
$$
T(u,u)=x^2(u')^2+xJ(x^2(u'')^2+2(u')^2),\qquad
p_T(\mathbf m)=m_2x.
$$
对任意二次 $p=A_px^2+B_px+C_p$，原共同锚给
$$
T(u,p)=B_pD_+u,\qquad
D_-u=u',\ D_0u=xu'-u,\ D_+u=x^2u'-2xu.
$$
连同原 $R,L,U$ 表，准确得到
$$
\boxed{
B(u,p)=(aB_p-eC_p)D_-u+eB_pD_0u+tB_pD_+u.
}
\tag{5}
$$
$A_p$ 项在 $-2eL+eU$ 之间抵消。特别
$B(u,p_B(\mathbf n))=b(\mathbf n)(aD_-+eD_0+tD_+)u$。

原三配对满足
$$
2\mathbf I(u,D_-u)=(0,-m_0,-2m_1),\quad
2\mathbf I(u,D_0u)=(m_0,0,-m_2),\quad
2\mathbf I(u,D_+u)=(2m_1,m_2,0).
\tag{6}
$$
这完全规定了新方向的真实跨包 history，包含 $I_2$ 的一阶导项。

## 3. 原 Green 项和校正 self

对 $p=A_px^2+B_px+C_p$、$q=A_qx^2+B_qx+C_q$，保原左端 $\ell$：
$$
\begin{aligned}
\beta_0(p,q)&=-2A_q(2A_p\ell+B_p),\\
\beta_1(p,q)&=-2A_q(A_p\ell^2-C_p),\\
\beta_2(p,q)&=-2A_q\ell^2(2A_p\ell+B_p)
-2B_q(A_p\ell^2+B_p\ell+C_p).
\end{aligned}
\tag{7}
$$
这些不是可忽略的边界项。若 outer 包在 inner 包左侧，
$I_j(Bu_i^2,Bu_k^2)=\beta_j(p_B(\mathbf m_i),p_B(\mathbf m_k))$。

令
$$
\begin{aligned}
d_0(\mathbf m)&=e m_0+2t m_1,\\
d_1(\mathbf m)&=-a m_0+t m_2,\\
d_2(\mathbf m)&=-2a m_1-e m_2.
\end{aligned}
$$
完整平方与第三尾的有序核是
$$
\boxed{
\Gamma_j^B(\mathbf m,\mathbf n)
=2\beta_j(p_B(\mathbf m),p_B(\mathbf n))
+b(\mathbf n)d_j(\mathbf m).
}
\tag{8}
$$
其反对称部分的三个 wedge 系数，按
$\gamma_{rs}=(M_{rs}-M_{sr})/2$，为
$$
\begin{array}{c|ccc}
j&\gamma_{01}&\gamma_{02}&\gamma_{12}\\ \hline
0&(3e^2-2at)/2&3et/2&t^2\\
1&-ae/2&-at&-et/2\\
2&a^2&ae/2&(e^2-2at)/2
\end{array}.
\tag{9}
$$
原 $\ell$ 项在这个反对称差中消去；在(8)之前没有删除它们。

定义 nonlegal 单包 self
$$
K_j^B(u)=I_j(Bu^2,Bu^2)+2I_j\{u,B(u,Bu^2)\},
$$
$$
\boxed{\widehat K_j^B(u)=K_j^B(u)-\tfrac12\Gamma_j^B(\mathbf m,\mathbf m).}
\tag{10}
$$
内场允许真实左尾。R259 的原 cubic local 密度
$F_{B,j}(u)=I_j(u,Bu^2)=\int f_{B,j}(x,u,u',u'')$
与 cutoff adjoint，连同(7)，给
$$
\boxed{
\widehat K_j^B(u)
=D_{\rm loc}F_{B,j}(u)[Bu^2]-\tfrac12b(\mathbf m)d_j(\mathbf m).
}
\tag{11}
$$
式中 $D_{\rm loc}$ 是密度的形式变分，不把 $Bu^2$ 当作可加入紧输入空间的方向。原两个 Green 项先保全，再按(8)准确相消。

由原二次式，
$(Bu^2)''=\alpha_Bu'''+\beta_B$，
其中 $\beta_B$ 只含 $C^2$ 数据与原三个右 primitive。因而(11)唯一可能的三阶导项是
$A(x,u,u',u'')u'''$，没有平方。对最后变量取多项式原函数并作一次真 IBP，全部边界因 $u,u',u''$ 的零 collar 消失。故(10)是**连续四次 polynomial/$C^2$ 观测**。同锚平移后次数至多十，理由仍是原八表的有限坐标次数；不需 profile 的十阶微分。

## 4. 从起点规定的新有限观测及全部八矩交换子

本稿不在已冻结旧圆上暗加观测。从最初规定 $\mathcal F_{\rm new}$，含：
- 原三个矩 $\mathbf m$；
- 原 E8 全部 $X<Y$、$j=0,1,2$ 的真实
  $2I_j\{u,[X,Y](u;u^2)\}$ 的全部平移系数；
- 三个(10)的全部平移系数。

至多有 $28\cdot3\cdot11+3\cdot11+3$ 个所列标量，可以冗余；这个数不是秩。所有方向都用原 R73/R259 八表，$T$ 与 $P_1$ 不省略。

面积 self 的 $C^2$ 性也须保其真尾。准确式为
$$
2I_j\{u,[X,Y](u;u^2)\}
=D_{\rm loc}F_{X,j}[Yu^2]-D_{\rm loc}F_{Y,j}[Xu^2]
+\beta_j(p_X,p_Y)-\beta_j(p_Y,p_X).
\tag{12}
$$
右边只线性含 $u'''$，按与(11)相同的原函数 IBP 化为 $C^2$；三个真实 primitive 不删。全部平移次数仍不超过十。

使用 R277 的实际等背景格点布局：
$$
b_i^2=B_0>0,\quad
R_i=a_i^2-b_i^2\in\{-B_0/2,8B_0\},\quad T_i=a_ib_i,
$$
$$
\sum_iR_it_i^k=\sum_iT_it_i^k=0\quad(0\le k\le10),\qquad
R_i^2-4T_i^2=\tfrac{7B_0}{2}R_i.
\tag{13}
$$
先置共同偶母包，然后允许每个包在同一个 $\mathcal F_{\rm new}$ 纤维内变化。其全部实际矩和上述 self 在原位置的值准确保持。

任意 E8 pair 的 cross 核，由原二次尾与 sl2 表给出一个真实三矩双线性型 $\Gamma(\mathbf m,\mathbf n)$。不要求它等于旧 Gaussian 表中的某一条。全角 even 中，$E_{04}$ 准确为
$$
B_0\sum_kR_k\left\{S_k+\sum_{i<k}\Gamma(\mathbf m_i,\mathbf m_k)\right\}.
$$
同形等距参考矩至多二次，左 prefix 和至多三次，所以 cross 括号是格点参数的至多五次多项式；$S_k$ 至多十次。纤维保持后仍按(13)为零。

另一 even 系数减去 $E_{04}$ 后为
$$
\begin{aligned}
&\sum_i(R_i^2-4T_i^2)
\{S_i-\tfrac12\Gamma(\mathbf m_i,\mathbf m_i)\}\\
&\qquad+\sum_{r<s}\gamma_{rs}\mathcal A_{rs},
\end{aligned}
\tag{14}
$$
其中
$$
\mathcal A_{rs}
=\sum_{i<k}(R_iR_k-4T_iT_k)
(m_{r,i}m_{s,k}-m_{s,i}m_{r,k}).
\tag{15}
$$
第一行由(13)清掉。采用 R280 的五个真实完整 block 正权，三个实际(15)同时为零；这里 $m_2$ 是(2)，不是中心点替代矩。不同完整 block 的三矩各自为零，跨 block wedge 确实消失。

原八完整副本先支付全部第三 range，十二完整正幅副本清 odd 角项。每一步使用真实 finite 平移、多项式次数和同一个右锚；非均匀的实际母包仍逐一共享其所有复制。于是当前构造对**全部 E8 pair**准确有
$$
\boxed{I_j\{\phi_\theta,[X,Y](\phi_\theta;D_\theta)\}=0
\quad\text{对全部 }\theta,\quad j=0,1,2.}
\tag{16}
$$
这是原 R280/R294 有序证明的有限八方向扩展，不称为旧 Gaussian 词独立性的新推论。

## 5. 同一个纤维先支付 B² 的额外角项

原四次槽代数给，odd 项已由上述完整副本清掉后，
$$
q_j(\theta)=\sin^2\theta\,q_j(\pi/2)
+\sin^2\theta\cos^2\theta\,\Xi_j.
\tag{17}
$$
真实 self/尾展开与(8)–(10)给
$$
\Xi_j=\sum_i(R_i^2-4T_i^2)\widehat K_j^B(u_i)
+\sum_{r<s}\gamma^B_{rs,j}\mathcal A_{rs}.
\tag{18}
$$
前项由 $\mathcal F_{\rm new}$ 保持原同母平移值，再由(13)清掉；后项由同一个(15)清掉。故
$$
\boxed{\Xi_j=0\qquad(j=0,1,2).}
\tag{19}
$$
没有因 $q_j(\pi/2)$ 尚未为零而预授(3)。接下来恰需同时解三个原特殊角值。

## 6. 三个真实 principal 多项式：不借用旧 Gaussian 秩

原二导给
$$
\alpha_R=2u'-2xu'',\quad
\alpha_L=u-xu',\quad
\alpha_U=2xu'-3x^2u'',\quad
\alpha_T=2x^2u'-2x^3u''.
$$
因此
$$
\boxed{
\alpha_B(x,u,v,r)
=-2eu+(2a+4ex+2tx^2)v
-(2ax+3ex^2+2tx^3)r.
}
\tag{20}
$$
特别其最高坐标项是 $-2t x^3r$，且 $t\ne0$。

在第 i 个真实微包，$\theta=\pi/2$ 时记
$\lambda_i=-a_i^2R_i$。原完整主项分解给
$$
q_j(\pi/2)
=\sum_i\lambda_i\int x^j\alpha_B(u_i)^2(u_i''')^2
+\text{真实 }C^2\text{ 余项}.
\tag{21}
$$
$j=2$ 的 $2u'v'$ 只进入后面的真实余项。所有二次尾与跨包项同样保在该余项；不把(21)当纯 principal 定义。

取母坐标 y，选同源非零偶 $\chi$，使
$\int(u_0'')^2\chi^2>0$。全部实际复制的正四次权为 $w_c>0$、偏移 $d_c$。对一个基本包的原位置 X，准确 principal 向量为
$$
P_j(X)=\sum_cw_c\int
(X+d_c+y)^j
\alpha_B(X+d_c+y,u_0,u_0',u_0'')^2\chi^2\,dy.
\tag{22}
$$
每个 $d_c,w_c$ 都是已选有限实际副本数据，不把复制当无成本平移。三个多项式的次数准确为 $6,7,8$，共同首系数
$$
A=4t^2\Big(\sum_cw_c\Big)\int(u_0'')^2\chi^2>0.
\tag{23}
$$
故其 Wronskian 在共同大正位置 C 的首项为 $2A^3C^{18}$。对任意三个固定递增偏移 $\xi_1<\xi_2<\xi_3$，
$$
\det(P_j(C+\xi_i))_{j=0,1,2;i=1,2,3}
=A^3C^{18}\prod_{i<k}(\xi_k-\xi_i)+O(C^{17}).
\tag{24}
$$
这里已除去 Taylor 中 $0!1!2!$，不能把 Wronskian 的因子2直接沿用到(24)。

有限个实际三点 minor 因而在一次足够大但有限的共同 C 后全部同正。此时才固定共同正物理 I；不声称任意预先窄定的 I 都容纳它。

## 7. 四个真实包的正锥和有限 N 真根

R277 实际布局中可取索引 $0,1,33,34$，依次是 high、low、high、low，真实位置递增。对应
$$
\lambda_{\rm high}=-72B_0^2<0,\qquad
\lambda_{\rm low}=B_0^2/4>0.
$$
它们在整包装中的权仍为正，所以符号不变。由(24)，$3\times4$ 的四个 ordered minor 同号；其一维 cofactor 核交替。乘上交替的 $\lambda_i$ 后，四个真实列
$$
v_i=\tfrac12\lambda_i(P_0(X_i),P_1(X_i),P_2(X_i))
$$
有一个**各项严格正**的核向量，并且秩3。因此其正锥等于整个 $\mathbb R^3$：先取任意线性表示，再加足够大的正核便可让全部四个系数正。

从起点对 $\mathcal F_{\rm new}$ 使用 R293 的有限 $C^2$ polynomial 最大秩纤维版本，选一个非零 even $u_0$ 和有限光滑纠正方向。在解析版本可全部选为 $\psi$ 乘偶多项式，$\chi$ 亦同源。这里只需(23)非零；不需要移植旧 rank30 子式。

在四个选中基本包同时用
$$
u_{i,N,z}=u_0+z_iN^{-3}\chi\cos(Ny)
+\text{同一有限纠正方向的真实 IFT 校正},
\tag{25}
$$
并在每个原完整副本同步使用同一修改后的母包。校正使
$\mathcal F_{\rm new}(u_{i,N,z})=\mathcal F_{\rm new}(u_0)$
准确成立。对固定有限正幅盒，校正及参数导数的 $C^3$ 范数为 $O(N^{-1})$；这是有限个固定光滑方向的结果，不是将原振荡的 $C^3$ 大小当小量。

原(21)及真实低阶连续性给整个三值映射的 $C^1$ 极限
$$
(q_0,q_1,q_2)(\pi/2)
\longrightarrow b+\sum_{i=1}^4 z_i^2v_i,
\tag{26}
$$
其中 b 是全部未改包、原高阶能量、实际尾与 local 低阶项的完整有限基线。三阶振荡平方的平均是 $1/2$，已经记入 $v_i$；一次振荡与固定光滑背景的交叉趋零。

正锥给严格正 $z_i^*$，使右侧为零。固定其中一个幅度，选三个独立列；其余三变量的 Jacobian 是相应列乘 $2z_i^*$，可逆。由(26)的统一 $C^1$ 收敛，某个足够大但**有限**的 N 上存在附近真根。没有以 $N=\infty$ 或仅 principal 为零替代真实原式。

由(17)、(19)，这个同一实际有限频率圆满足
$$
\boxed{q_j(\theta)=0\quad\text{对所有 }\theta,\quad j=0,1,2.}
\tag{27}
$$
三矩、完整第三与(16)均由同一纤维和原共享包装准确保留。所有最终支持间隙、宽度、幅度和参数都有限正；共同归一化只按齐次次数缩放已零项。

这证明新 R312 芽的 $E^2$ 三门本身不是 rank-one 类中的不可解正障碍。没有将它与旧 R304 的 Gaussian 一层正余量混为一题。

## 8. 下一对数门：明确消掉哪一部分，保哪一部分

为了把(16)真正接到下一原门，用 h 作几何变量，写
$$
\mathsf Q(\sigma)=\sigma\mathsf A(h),\qquad
\mathsf A(h)=\sum_{p=-3}^{1}A_ph^p.
$$
R312 的准确有理式给
$$
\begin{aligned}
A_{-3}&=-K\varepsilon h_eR/12,&
A_{-2}&=K\varepsilon R/48,\\
A_{-1}&=h_eaR+\varepsilon h_eT/4,&
A_0&=\kappa^2P_1-KT/8-\kappa h_eV/3,&
A_1&=-\kappa V/6.
\end{aligned}
\tag{28}
$$
因为 $\gamma=2h_e\varepsilon\sigma$，
$$
\mathsf Q'=\mathsf A+2(h-h_e)\mathsf A_h.
$$
R312 的完整对数算子分为
$$
\mathscr D=\mathscr D_{\rm loc}+\mathscr D_{\rm hist},\qquad
\mathscr D_{\rm loc}
=\operatorname{Res}_{h=0}\frac{\mathscr C_\sigma}{\gamma}.
\tag{29}
$$
$\mathscr C_\sigma$ 仍是原 $\ell_\sigma-\Psi_\sigma(\phi,\mathsf MD)$，不是仅 local principal。其商在本端芽上是 h 的有理算子。$\sigma=0$ 的可去因子由原 odd 性支付；在复 h=0 取 residue 只是原函数系数法，不改物理路径。

完整有序历史部分则准确为
$$
\boxed{
\begin{aligned}
\mathscr D_{\rm hist}
={}&\frac1{2\varepsilon}[A_0,B-A_{-1}/h_e]
+\frac1{\varepsilon}[A_1,A_{-1}]\\
&-\frac3{2h_e\varepsilon}[A_1,A_{-2}].
\end{aligned}}
\tag{30}
$$
每个括号是原完整外槽交换子，非只对角值。

核对(30)：R312 的原 U′ 除以 $\gamma$ 后，history 部分是
$$
-\frac{(\mathsf A+2(h-h_e)\mathsf A_h)
(\phi,\mathsf A D)}{2h_e\varepsilon}
+\frac{[\mathsf A,B](\phi;D)}{2\varepsilon h}.
$$
第一项 residue 内的 $p+q=-1$ 对给
$3[A_1,A_{-2}]+[A_0,A_{-1}]$，
而 $p+q=0$ 对给 $-2h_e[A_1,A_{-1}]$。
第二项只取 $A_0$。这正是(30)，保留两种不同次序；没有给任意单包第三尾另选常数。

由(16)，同一个当前构造准确有
$$
I_j\{\phi,\mathscr D_{\rm hist}(\phi;D)\}=0.
$$
因此 R312 的完整 log 门在这里严格归约为
$$
\boxed{I_j\{\phi_\theta,\mathscr D_{\rm loc}(\phi_\theta;D_\theta)\}=0,
\quad j=0,1,2,\quad\text{全部 }\theta.}
\tag{31}
$$
本文没有证明(31)为零，也没有把它偷换为一个可任选的三阶齐次 profile。它仍包含真实 local-third 和变化 profile 的 chain。

## 9. 已付范围与下一真实缺口

本稿已经实际存在性支付：新非 Gaussian 端芽上非退化实紧圆的原三矩、完整第三、全部 E8 交换子面积、整角 $E^2$ 三门。用的是从起点规定的新 $\mathcal F_{\rm new}$、真实包布局、有限正幅与有限频率；不称旧圆或旧 fixed-g 计算结果无偿继承。

当前明确未付的是(31)、完整单 E 系数、纯有理余式在同一个 $\operatorname{span}\{1,h,h^{-1}\}$ 中的成员条件，以及全路径 period、同一 gauge joint 条件和更高阶/有限几何目标。尤其 $\mathscr D_{\rm hist}$ 已清不意味着整个 $\mathscr D$ 已清。

下一步应从(29)的原局部 residue 和 R312 的完整单 E 表达直接推导其 self/cross 与低阶兼容；不能以继续增大本稿 N 代替一个新的相容机制。本稿没有派发或重复任何研究运行。
