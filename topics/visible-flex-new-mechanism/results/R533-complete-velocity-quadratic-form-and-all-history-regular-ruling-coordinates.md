# R533：同一原母库的完整速度二次型与覆盖全部八矩历史的正则 ruling 坐标

日期：2026-11-16。**完整原式纸面证明；没有执行数值、符号、profile、秩、开发检查或新的科学任务。**

本文从起点加强选择 R520/R459 的同一种可变母库，在原二十个完整目标以外加入十三个实际高阶目标。它们在原允许物理窗口、原共同外 cap 和全部真实正权复制中有同一个有限准确正根。所得完整第四 ruling 关于两真实速度的二次型，在任意预先指定的合法 scalar 紧盒上严格不定；这一性质对全部八维第二历史都相同，亦不依赖后来一次固定的第三规范。

因此完整 ruling 可用一个非零自由输入写成全八矩历史上的光滑速度图。其正则分母不再因累计矩阵增大而消失。这个结论严格强于只在常态前缀附近验证一个速度偏导非零，但仍不是全局存在、任意历史可达、八矩返回或闭路结论。原 $M_{\rm raw}$、第三历史、frame、位置和第四成本始终沿真正恢复积分。

本稿不改变原物理窗口。下文的 $\xi_{\rm tar}=-\omega_c/2$ 只是指定十三个实目标时的代数编码，既不是实际包中心，也不是要求加入的点质量。它不需要落在物理窗口内。

直接来源：
[R520](R520-variable-mother-constant-ruling-and-same-gauge-nonconstant-local-departure.md)、
[R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)、
[R527](R527-finite-amplitude-same-gauge-ruling-paths-with-complete-matrix-memory.md)、
[R531](R531-real-negative-p1-segments-in-the-three-zero-library-with-one-fixed-gauge.md)；
实际正根使用
[R447](R447-twenty-common-profile-targets-and-a-nonzero-highest-P-gauge-direction.md)、
[R455](R455-four-natural-moments-with-one-common-degenerate-pair-and-twenty-targets.md)
的同一受限图册与有号集中。两条原最低有理行直接取自
[R324](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md)
与 [R321](R321-complete-single-arctangent-gates-and-ten-dimensional-joint-control.md)。

## 1. 先固定原窗口、scalar 盒和完整初端

原物理区间 $I=[\ell,r_*]$、共同右锚、严格不交布局、共同物理宽度、原有理保护芽参数及全部复制先固定。沿 R520 选
$$
S_c=(h_c,0,\omega_c),\qquad h_c>0,\quad \omega_c\ne0,\qquad
x+\omega_c>0\quad(x\in I).
\tag{1}
$$
不把 $I$ 平移到负坐标去迁就稍后的目标数。

另预选一个包含 $S_c$ 的合法紧 scalar 盒 $\mathcal B$，使其某个开邻域内
$$
0<h_-\le h\le h_+,\qquad
x+\omega\ge z_->0\quad(x\in I),
\tag{2}
$$
并使 $k,\omega$ 有界。盒的大小可以任意预先指定为有限合法大小；母库随后依这个盒选择。没有声称一份固定母同时适用所有无界 scalar 状态。

继续用原记号
$$
S=(h,k,\omega),\quad d=h\omega-k,\quad e=hx+d,\quad Q=1+e^2,
$$
$$
\gamma=h_s,\quad \upsilon=k_s,\qquad
\omega_s=\frac{\upsilon}{2h},\qquad
e_s=\gamma(x+\omega)-\frac{\upsilon}{2}.
\tag{3}
$$
八矩和第二算子为
$$
m_s=M_{\rm raw}(S,\gamma,\upsilon),\qquad A=\Phi_m .
\tag{4}
$$
$m$ 不是独立控制；本稿的全部实际路径都满足(4)。

严格不交圆仍是
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
\phi_\theta=f\cos\theta+g\sin\theta,
$$
$$
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta,\qquad
R_i=a_i^2-b_i^2,\qquad \lambda_i=-a_i^2R_i .
\tag{5}
$$
全部微包、八/十二副本、五个正权 block 和原八宏 copy 均在这份实际名单中。每个 $u_i$ 关于自己的真实中心为偶函数，保持原共同外 cap 及全部端 jets。

原二十行完整值保持
$$
\mathbf T_{20}=(\mathcal V_{19},d_f(P))=(0,\eta_P),\qquad \eta_P\ne0 .
\tag{6}
$$
没有在最后求根后缩放全圆。四自然约束、共同低阶纤维、三矩、种子和实际归一全部按原构造一同冻结。

本稿使用 R520 的完整有限 $C^2$ 观察表 $\mathcal F_{\rm path}$，其中保留全部 $W$ outer、校正 pure self、真有序尾以及两个完整加速度系数的全部平移/几何系数。于是同一圆上、同一真实初端下
$$
\mathscr K(s,\theta)=\sin^2\theta\,F(S,m,\gamma,\upsilon),
\tag{7}
$$
且两个加速度的完整系数为零。这里的第三商势仍是
$$
P^{\rm end}=\Theta_0+\Pi(j^1S)-\Pi(j^1S_{\rm initial});
\tag{8}
$$
不在中间前缀重新置零。下面取全局第二规范 $w_\theta=0$，第三规范 $\chi_\theta$ 只选择一次。

## 2. 完整速度次数，不只常态的一阶导数

固定当前 $S,m$，先在原场中保留真实加速度，再按(7)消去其完整系数。下面的次数均是两速度 $(\gamma,\upsilon)$ 的次数，$s$ 导仍包含真实水平关系。

| 原完整对象 | $TB$ 分量的速度次数 | $N$ 分量的速度次数 |
|---|---|---|
| $Y,Y_x$ | $0$ | 无 |
| $\nabla_sY$ | $1$ | $0$ |
| 第二局部 $K,K_x$ | $1$ | $0$ |
| $\nabla_sK$ | $0,2$，另加加速度一次 | $1$ |

这就是 R520 §9 的分量表，但这里使用其完整次数上界，而非仅取零速度导数。

对完整 forcing $H(Y,K)$，$P_C,B_C$ 是速度一次，$T_{sx}$ 只有速度零次、二次和加速度一次。原
$$
\eta_C=-\frac{T_{sx}}{2h}
+\frac{e_s(P_C)_x}{2h}
+\frac{\gamma(B_C)_x}{2h}
-\frac{(P_C)_s}{2}
\tag{9}
$$
也恰有同样次数。求 $(P_C)_s$ 时既保几何系数的一阶导数与速度的乘积，也保真实加速度；没有提前令加速度为零。

R482(22)的三个来源分别是 $|V_K'|^2$、原完整 $\eta_-$ 和变化-profile chain
$$
v=\Phi_{M_{\rm raw}}D .
$$
第一项由于 $TB\perp N$ 只有零、二次。第二项按(9)只有零、二次及加速度。第三项由 R73 原八坐标只有
$\gamma^2,\gamma e_s,e_s^2$ 三类速度二次项，亦只有零、二次。R482 的 $P_{\rm acc}$ 是速度二次，$P_h+\bar F$ 仅依赖当前 scalar，初端值是固定常量。

因此整个不含累计 $m$ 的部分准确是速度零次加二次，而非一个只在零速度附近的 Taylor 近似。另一方面，R221/R482 的
$\mathcal L_S(\Phi_mD)$ 对速度一次、对 $m$ 一次；完整
$$
q_S(A)=-\mathcal E_S(AD,AD)
+2\mathcal E_S\{\phi,A(\phi,AD)\}
\tag{10}
$$
对 $m$ 二次且不含速度。固定 $\chi$ 的贡献是
$-2\mathbf w(S)\cdot\nu$，也不含速度。

故取任意可逆的、只依赖 $S$ 的两速度线性坐标 $z$，完整方程准确为
$$
\boxed{
F(S,m,z)=z^{\mathsf T}\mathsf H(S)z+
\mathsf l(S,m)^{\mathsf T}z+\mathsf c_\nu(S,m).
}
\tag{11}
$$
$\mathsf l$ 对 $m$ 线性；$\mathsf c_\nu$ 保当前几何的完整常数项、真初端势、固定第三规范以及完整历史平方。尤其
$$
\boxed{\mathsf H\text{ 不依赖 }m\text{，也不依赖固定 }\chi.}
\tag{12}
$$
严格的速度 Hessian 是 $2\mathsf H$；下文称 $\mathsf H$ 为速度二次型矩阵。即使实际 $m$ 是沿过去速度产生的，当前有限状态方程的速度偏导仍按(4)的状态约定取；不能将过去路径变分混入这个偏导。

## 3. 完整平方 principal 与所需十四个生成量

令
$$
L_c=p-(x+\omega_c)r,\qquad p=u',\quad r=u'',\quad t=u''',
$$
$$
\eta=\omega-\omega_c,\qquad
z=\binom{\gamma}{\delta},\qquad
\delta=\frac{\upsilon}{2}-\eta\gamma .
\tag{13}
$$
此变换在所有合法状态可逆，$\upsilon=2(\delta+\eta\gamma)$。

R520(20a)–(21)从 second square、第三 local、完整第三 characteristic 及变化-profile chain 一起给
$$
\sum_i\lambda_i\int\frac Qh
\left(\frac{\alpha_m}{2}+\beta\right)^2t_i^2,
\qquad
\beta=\frac{Q(\gamma L_c+\delta r)}{8h^3}.
\tag{14}
$$
剩余项在保持所有 primitives、Green 项及左尾以后，准确降为有限的连续 polynomial/$C^2$ 表达。不能把(14)整个当成 $C^2$，也不能用单独的 second square 替代它。

本稿的新生成量**不带** R527(8)的额外 $Q_c$ 权：
$$
\begin{aligned}
\mathsf A_j&=\sum_i\lambda_i\int x^jL_{c,i}^2t_i^2,\\
\mathsf B_j&=\sum_i\lambda_i\int x^jL_{c,i}r_it_i^2,
\qquad 0\le j\le6 .
\end{aligned}
\tag{15}
$$
另记尚未指定的
$$
\mathsf C_j=\sum_i\lambda_i\int x^jr_i^2t_i^2,\qquad 0\le j\le6 .
\tag{16}
$$
对次数不超过6的 $P$，按系数线性定义 $\mathsf A[P],\mathsf B[P],\mathsf C[P]$。

只抽取(14)的速度二次系数，结合(11)(12)，准确得
$$
\boxed{
\mathsf H(S)=\frac1{64h^7}
\begin{pmatrix}
\mathsf A[Q^3]&\mathsf B[Q^3]\\
\mathsf B[Q^3]&\mathsf C[Q^3]
\end{pmatrix}
+\mathsf E(S).
}
\tag{17}
$$
$\mathsf E$ 是完整低阶余矩阵。其界不需要也不宣称整个 source 对无界 $m$ 一致有界：因为(12)，可在 $m=0$、有限几个固定速度值处提取二次系数。R520 的完整 $C^2$ 降阶遂给
$$
\sup_{S\in\mathcal B}\|\mathsf E(S)\|\le C_{\rm low}
\tag{18}
$$
于一个预先固定的共同 $C^2$ profile 小邻域。这个常数在下面的高阶目标增大时保持不变。物理 $x$ 积分仍只在原 $I$ 中进行。

## 4. 新十四生成与原二十行恰只有一条关系

沿原 R324/R447 写
$$
W=p-xr,\qquad C=u-xp+\frac{x^2r}{2},\qquad L_c=W-\omega_cr .
\tag{19}
$$
旧十九个 principal 只含 $x,W,C$，旧第20个是 $2x^4Cr$。
对所有真实偶点对成立的普遍二次零核，准确只有
$$
\alpha up+\beta pr,\qquad \alpha,\beta\text{ 为实常数}.
\tag{20}
$$
这一已付恒等适用于实际中心和内部点的任意非空开集，不把偶母中心的 $p=0$ 当成自由 jet。

若(15)的一项组合落在旧二十行模(20)的像中，其新增部分为
$$
A(x)L_c^2+B(x)L_cr,\qquad \deg A,\deg B\le6 .
$$
先比较 $Cr$，得旧第20行及 $\alpha up$ 的系数同时为零，因为
$2c_{20}x^4=\alpha x$ 必为多项式恒等。再比较 $rW,r^2$，必须有
$$
B-2\omega_cA=\beta,\qquad
\omega_c^2A-\omega_cB=\beta x.
\tag{21}
$$
由 $\omega_c\ne0$，
$$
A=-\frac{\beta}{\omega_c^2}(x+\omega_c),\qquad
B=-\frac{\beta}{\omega_c}(2x+\omega_c).
\tag{22}
$$
反过来，原恒等式
$$
\boxed{
(x+\omega_c)L_c^2+\omega_c(2x+\omega_c)L_cr
=(x+\omega_c)W^2-\omega_c^2pr
}
\tag{23}
$$
正给这个候选关系。

还须确认右边的 $W^2,xW^2$ 真在旧十九主像，而不是臆设。用原保护芽记号
$H_e>0,\varepsilon>0,\kappa\ne0,K_g=1+\kappa^2$。
R321(8)及 R324(14)给
$$
\Psi_h=p_hW+q_hC,\quad
p_h=\frac{K_g\varepsilon H_e}{3h^3}
+\frac{K_g\varepsilon/24-\kappa H_e\varepsilon x}{h^2}
+O(h^{-1}),\quad q_h=O(1),
$$
$$
\sum h^m\mathcal Z_m
=\frac{(h-H_e)(K_g-2\kappa hx+h^2x^2)}
{4H_e\varepsilon h}\Psi_h^2 .
$$
逐取最低两幂即
$$
\mathcal Z_{-7}=-\frac{K_g^3\varepsilon H_e^2}{36}W^2,
$$
$$
\mathcal Z_{-6}=
\left\{\frac{K_g^3\varepsilon H_e}{48}
+\frac{2\kappa K_g^2\varepsilon H_e^2}{9}x\right\}W^2.
\tag{24}
$$
两个对角系数都非零，所以确张成 $W^2,xW^2$。

因此旧二十主像与(15)十四生成的相交恰为(23)这一维。删去 $\mathsf B_1$ 即去掉唯一关系：它在(23)中的系数是 $2\omega_c\ne0$。于是
$$
\boxed{\mathbf T_{20}\text{ 加 }
\mathsf A_0,\ldots,\mathsf A_6,
\mathsf B_0,\mathsf B_2,\ldots,\mathsf B_6
\text{ 有 }33\text{ 维真实偶配对主像}.}
\tag{25}
$$
新位置次数至多8；旧二十行的统一次数仍是10。

## 5. 用三个完整平方值替换低三行

令
$$
Q_c=1+h_c^2(x+\omega_c)^2,\qquad
Q_c^2=\sum_{r=0}^4 d_rx^r,\qquad d_0>0 .
$$
仍按 R527 原完整定义使用
$$
q_j(A_c)=-I_j(A_cD,A_cD)
+2I_j\{\phi,A_c(\phi,A_cD)\},\quad j=0,1,2,
$$
$$
A_c=-R_{x+\omega_c}/(8h_c^2)-T_{x+\omega_c}/8.
$$
原 $(A_cu^2)''=-Q_cL_ct/(4h_c^2)+C^2$ 及其完整跨包尾给
$$
\boxed{
q_j(A_c)=\frac1{16h_c^4}
\sum_{r=0}^4d_r\mathsf A_{j+r}+e_j,\qquad j=0,1,2.
}
\tag{26}
$$
$e_j$ 保全部真 Green、ordered、primitive 和 $I_2$ 一导项，是完整 $C^2$ 余值。它们在上述预定 profile 邻域内一致有界。

本次十三行取为
$$
q_0(A_c),q_1(A_c),q_2(A_c),\quad
\mathsf A_3,\mathsf A_4,\mathsf A_5,\mathsf A_6,\quad
\mathsf B_0,\mathsf B_2,\mathsf B_3,\mathsf B_4,\mathsf B_5,\mathsf B_6 .
\tag{27}
$$
因 $d_0>0$，从 $j=2,1,0$ 倒序消元说明其 principal 与(25)十三行等价。因此(27)与原二十行仍是同一个33维主系统。

## 6. 原固定窗口中的真实正锥与同一有限根

本节逐项支付(25)，不以 signed span 代替实际正幅。

先在 R455 的同一共同-cap、四自然约束图册内，取完整
$\mathcal F_{\rm path}$ 的限制最大秩。四正常支撑放在原中心 $A_u<0$ 区的一组小窗，主点对见证放在另外的有限分离小窗。与 R447 完全相同的偶 Hermite 扰动和正常纠正给任意有限主二阶 jets；纠正窗不改变主点 jets。

把四正常 minor、限制最大低阶 minor 与第4节的33阶主 minor 放在同一个有限解析族内。各非零解析 minor 的有限乘积不恒零，可以同时选非零，再冻结新 $\mathcal F_{\rm path}$ 值。所有变化留在原严格内区；共同外 cap、两个原简单 $A_u$ 根的整个邻域、原简单 $p$ 根、四自然约束及严格开条件保留。

原正布局 block 的第二层有2048个可用层，故至多33个形状组仍放在原编码内。每组使用原十二个第一层位置
$$
j_\ell\in\{0,1,33,34,49,50,65,66,81,82,97,98\}.
\tag{28}
$$
其真实 $\lambda_\ell$ 依次为负、正交替。各完整 copy 的平移与正四次权给
$$
(\mathcal TP)(X)=\sum_\nu\omega_\nu P(X+d_\nu),\qquad \omega_\nu>0.
$$
它在 $\operatorname{Pol}_{\le10}$ 上是主对角为 $\sum_\nu\omega_\nu>0$ 的可逆三角算子。高低布局、真实宽度、偶点对集中质量及原归一都保留在实际列中。

对每组十二个真实递增中心 $X_\ell$，
$$
\beta_\ell=\frac1{\prod_{j\ne\ell}(X_\ell-X_j)},\qquad
\sum_{\ell=0}^{11}\beta_\ell P(X_\ell)=0
\quad(\deg P\le10).
\tag{29}
$$
$\operatorname{sgn}\beta_\ell=\operatorname{sgn}\lambda_\ell$，故除入所有共同正因子后，实际33维列
$v_\ell=\lambda_\ell\mathbf P(X_\ell)$ 具有每分量严格正的核向量。
十二点评价张成该形状的全部位置系数像；有限多个形状由(25)联合张满 $\mathbb R^{33}$。各组正核相加得一个全分量正核。因此
$$
\boxed{\operatorname{cone}_{\rm finite}\{v_i\}=\mathbb R^{33}.}
\tag{30}
$$
证明是有限的：任意目标先作实线性表示，再加足够大的同一个严格正核，使所有系数变正。

在同一有号集中和低阶纠正中，完整33目标映射有
$$
\mathbf T_{33,N}(z)=b+\sum_i z_i^2v_i+o_{C^1}(1)
\tag{31}
$$
于每个先固定的有限正幅盒。这里 $b$ 保全部非活动 block、旧二十数值、真实跨包/Green、原初端及所有低阶余值。没有把任何实际基准置零。

由(30)先选正平方幅满足极限目标，再固定33个独立幅度方向，最后选一个充分大但有限的共同集中频率，以原有限维 IFT 得准确根。四自然约束、整个受限低阶纤维、全部实际副本和(6)同时保持。这不是移动一个旧冻结圆，也不继承 R527 用于另一条叶的额外十个数值目标；本稿重新从同一允许母库类型初选。

特别，(30)允许任意有限实目标。$\xi_{\rm tar}=-\omega_c/2$ 只是下面用于写这些数的一种方式。它不是(28)里的位置，没有将原正物理窗口移到负 $x$，也没有要求在 $\xi_{\rm tar}$ 放一个负幅或点质量。实现目标的仍是原 $I$ 内各实际列的**正平方幅**，其有号 $\lambda_i$ 来自已经合法的 high/low 布局。

## 7. 一个带统一三导能量界的真实正根选择

为了控制尚未指定的 $\mathsf C_j$，不能仅说它们对每个固定母有限。本节在原构造内给随高阶目标大小的明确界。

固定第6节的有限列矩阵 $V$、其一个右逆 $R$ 和一个严格正核向量 $\kappa$。若完整目标 $y(\Lambda)$ 对 $\Lambda\ge1$ 仿射，则可选固定常数 $c>0$，使
$$
s^*(\Lambda)=R\{y(\Lambda)-b\}+c(1+\Lambda)\kappa
\tag{32}
$$
逐分量满足
$$
c_0(1+\Lambda)\le s_i^*(\Lambda)\le C_0(1+\Lambda).
\tag{33}
$$
先固定一个有限 $\Lambda$，再将(31)的实际根选在
$s_i^*/2<s_i<2s_i^*$ 的正盒内。因此实际平方幅总和为 $O(1+\Lambda)$，常数与 $\Lambda$ 无关。

R447(24)–(26)的实际母导数为
$$
u_{i,N}'''=u_0'''+\epsilon_0 z_i\chi_0u_0g_{N,b_i}+e_{i,N},
$$
$$
g_{N,b}(y)=\sqrt N\{e^{-N^2(y-b)^2}-e^{-N^2(y+b)^2}\}.
\tag{34}
$$
直接换元给 $\|g_{N,b}\|_{L^2}\le C_g$，与 $N$ 无关。所有低阶纠正方向先固定；对每个先固定的 $\Lambda$，再取有限 $N$ 使
$\|e_{i,N}\|_\infty\le1$，并使全 profile 落在前述同一个 $C^2$ 小邻域。由(33)(34)及有限真实 copy、宽度、振幅因子，
$$
\boxed{\sum_i\|u_i'''\|_{L^2(I)}^2\le C_*(1+\Lambda).}
\tag{35}
$$
这里不要求一个固定频率适用全部无界 $\Lambda$；选择顺序始终是有限 $\Lambda$、有限正盒、再有限 $N$。原有号高项仍使中心 $A_u$ 只下降，外 cap 和根 germs 不变。

在固定 $C^2$ 邻域内 $u_i''$ 一致有界，实际 $x,\lambda_i$ 及复制数均已固定，所以(35)进一步给
$$
|\mathsf C_j|\le C_C(1+\Lambda)\quad(0\le j\le6),
$$
$$
\sup_{S\in\mathcal B}|\mathsf C[Q(S,\cdot)^3]|
\le C_{\mathcal B}(1+\Lambda).
\tag{36}
$$
这一步明确保了 $\mathsf C_j$；没有将未控制的第三平方放进一个虚假的统一 $O(1)$ 余项。

## 8. 十三个具体目标与缺失 $\mathsf B_1$ 的完整恢复

现在选
$$
\xi_{\rm tar}=-\frac{\omega_c}{2},
$$
并指定同一个完整目标
$$
\boxed{
\begin{gathered}
q_0(A_c)=q_1(A_c)=q_2(A_c)=0,\\
\mathsf A_3=\mathsf A_4=\mathsf A_5=\mathsf A_6=0,\\
\mathsf B_j=-\Lambda\xi_{\rm tar}^{\,j},
\qquad j\in\{0,2,3,4,5,6\}.
\end{gathered}}
\tag{37}
$$
原二十行仍为(6)。第6、7节对每个有限 $\Lambda$ 给带(35)的准确真实根。

由(26)从 $j=2,1,0$ 倒序解出
$$
|\mathsf A_0|+|\mathsf A_1|+|\mathsf A_2|\le C_A,
\tag{38}
$$
常数不随 $\Lambda$ 增长；完整 $e_j$ 没有被删去。

记
$$
\mathsf W_j=\sum_i\lambda_i\int x^jW_i^2t_i^2,\qquad j=0,1.
$$
原完整 $Z_{-7}=Z_{-6}=0$，结合(24)的非退化两行及其完整 $C^2$ 余项，给
$$
|\mathsf W_0|+|\mathsf W_1|\le C_W.
\tag{39}
$$
这不是只由旧 principal 得 $\mathsf W_j=0$；两个真余项均留在界内。

每个物理偶包都有
$$
\int p_i r_i t_i^2=0
\tag{40}
$$
因为相对其真实中心，$p_i$ 为奇、$r_i,t_i^2$ 为偶。将(23)乘 $t_i^2$ 后作完整实际加权积分，(40)给准确等式
$$
\mathsf A_1+\omega_c\mathsf A_0
+2\omega_c\mathsf B_1+\omega_c^2\mathsf B_0
=\mathsf W_1+\omega_c\mathsf W_0.
\tag{41}
$$
于是
$$
\mathsf B_1=-\frac{\omega_c}{2}\mathsf B_0
+\frac{\mathsf W_1+\omega_c\mathsf W_0-\mathsf A_1-\omega_c\mathsf A_0}
{2\omega_c}
=-\Lambda\xi_{\rm tar}+O(1).
\tag{42}
$$
对任意系数有界、次数不超过6的 $P$，
$$
\boxed{\mathsf A[P]=O(1),\qquad
\mathsf B[P]=-\Lambda P(\xi_{\rm tar})+O(1).}
\tag{43}
$$
因此所需的缺失一次矩是由**完整**旧值、真实偶性和新目标恢复；不是另加一条不能独立求解的第34行。

## 9. 完整二次型在整个合法盒上一致严格不定

由(17)(18)(36)(43)，
$$
\mathsf H_{11}=O(1),\qquad
\mathsf H_{12}=-\Lambda c(S)+O(1),\qquad
\mathsf H_{22}=O(1+\Lambda),
$$
$$
c(S)=\frac{Q(S,\xi_{\rm tar})^3}{64h^7}>0.
\tag{44}
$$
这些界在 $\mathcal B$ 上一致，且
$$
c_*=\inf_{S\in\mathcal B}c(S)>0
\tag{45}
$$
因为 $Q(S,\xi)=1+(h\xi+h\omega-k)^2\ge1$，$h$ 有有限正上下界。这里只在一个多项式中代入实数 $\xi_{\rm tar}$；物理合法性仍由(2)在真实 $x\in I$ 上保证。

由固定常数 $C_1,C_2,C_3$，
$$
\det\mathsf H
\le C_1C_2(1+\Lambda)-(\Lambda c_*-C_3)^2.
\tag{46}
$$
故先选一个充分大但有限的 $\Lambda$，再按第7节取最终有限频率，即在同一个真实圆上有
$$
\boxed{\det\mathsf H(S)<-c_{\det}\Lambda^2<0
\quad(S\in\mathcal B).}
\tag{47}
$$
取稍小常数可使其在 $\mathcal B$ 的一个合法开邻域上继续成立。因为(12)，(47)同时适用于所有 $m\in\mathbb R^8$ 和任何一次固定的 $\nu$。

另外在参考常态，由原 R520(34)或 R527(12)的完整一次项，
$$
\ell_{k,c}
=-\frac{\mathsf B[Q_c^3]}{64h_c^6}+e_k
=\frac{\Lambda Q_c(\xi_{\rm tar})^3}{64h_c^6}+O(1)>0.
\tag{48}
$$
三个完整 $q_j(A_c)$ 已准确为零。故 R531 后续真实前缀、一次固定第三 Gram 和负 $p_1$ 段的假设，都可以在这同一33行初选母上满足。所引用的是 R531 在 $q_j=0,\ell_{k,c}>0$ 后的实际路径证明；没有将另一份已冻结30行母与本母拼接。

## 10. 全历史光滑 null 坐标可以显式构造

不只逐点说一个不定二次型有零向量。由(44)取一个固定充分小的 $\epsilon>0$，再增大有限 $\Lambda$，可在整个盒的开邻域保证
$$
q_S(e_+)>0,\quad q_S(e_-)<0,\qquad
e_+=(1,-\epsilon),\quad e_-=(1,\epsilon),
$$
其中 $q_S(z)=z^{\mathsf T}\mathsf H(S)z$。例如先使
$\epsilon C_2<c_*/2$，再让线性 $\Lambda$ 项支配固定常数，即得上述两式。

写 $B_S(v,w)=v^{\mathsf T}\mathsf H(S)w$，定义
$$
p_S=\frac{e_+}{\sqrt{q_S(e_+)}},\qquad
n_S^0=e_--B_S(p_S,e_-)p_S,\qquad
n_S=\frac{n_S^0}{\sqrt{-q_S(n_S^0)}}.
\tag{49}
$$
由于
$q_S(n_S^0)=q_S(e_-)-B_S(p_S,e_-)^2<0$，这些都是整盒上同一个光滑选择，且
$$
q_S(p_S)=1,\qquad q_S(n_S)=-1,\qquad B_S(p_S,n_S)=0.
$$
令
$$
n_+=\frac{p_S+n_S}{\sqrt2},\qquad
n_-=\frac{p_S-n_S}{\sqrt2}.
\tag{50}
$$
则两者均为 null，$B_S(n_+,n_-)=1$。

对(11)完成平方：
$$
z_c(S,m)=-\frac12\mathsf H^{-1}\mathsf l,\qquad
\Delta(S,m)=\frac14\mathsf l^{\mathsf T}\mathsf H^{-1}\mathsf l
-\mathsf c_\nu.
\tag{51}
$$
用同一全局 smooth frame 写
$$
z=z_c+Xn_++Yn_- .
$$
完整 ruling 恰为
$$
\boxed{F=2XY-\Delta(S,m).}
\tag{52}
$$
因此任取一个光滑非零自由输入 $a(s)$，就有准确速度图
$$
\boxed{
X=a(s),\qquad Y=\frac{\Delta(S,m)}{2a(s)},\qquad
z=z_c+a\,n_++\frac{\Delta}{2a}n_- .
}
\tag{53}
$$
其所解方向的偏导是
$$
\frac{\partial F}{\partial Y}=2a(s)\ne0,
\tag{54}
$$
不依赖 $m$ 的大小。这不是将 history 项删掉：$z_c$ 保所有线性历史，$\Delta$ 保全部历史平方、固定 $\chi$、当前与初端势。

特别，固定 $a=1$ 已给每个 $S\in\mathcal B,m\in\mathbb R^8$ 上一份非临界实速度解。若一个原实际 regular 解在这份坐标中 $X=0,Y\ne0$，可交换两 null 标签使用 $Y$ 为自由输入。顶点 $X=Y=0$ 是完整速度梯度零的点；本稿的非零输入图不声称覆盖该奇点。

## 11. 真正的八矩演化与同一规范下的平滑接入

将(53)的两分量记作 $(\gamma,\delta)$，实际闭合约化系统是
$$
\boxed{
h_s=\gamma,\quad
k_s=2\{\delta+(\omega-\omega_c)\gamma\},\quad
\omega_s=\frac{k_s}{2h},\quad
m_s=M_{\rm raw}(S,\gamma,k_s).
}
\tag{55}
$$
第三场、frame、位置和第四成本随后按原恢复真实积分。第三商势的作用只是在 ruling 配对中用(8)给出准确同值表达；没有使第三 history 本身为零。

当 $S$ 留在合法开邻域、$a$ 离零且状态有限时，(55)是普通光滑有限维 ODE，故有局部唯一真路径，且整个原第四 ruling 对全部相位为零。这一句只从一个已经实现的完整入状态延拓。虽然(53)作为代数式定义于全部 $m$，它不证明每个指定 $m$ 都已能由前缀产生。

在同一母上选 R531 的一次固定 $\nu,\chi$，其常态前缀和真实负 $p_1$ 入口仍成立。取该路径任意 regular 点，使用(50)的一对 null 标签，使该点实际自由坐标非零。沿原真路径短延续读出其实际 $a_{\rm old}(s)$，再用左开集为1、右开集为0的平滑 cutoff，把它改接到同号的固定 $a_0\ne0$。左开集上两约化系统完全相同，唯一性保持全部原 germ；过渡可取足够短，使标量合法、$a$ 非零并保持原严格 $p_1<0$。

这里不在切口重选 $\chi$，也不重置 $m,T$。完整第三系统可能读取加速度和输入导数；只主张按实际 smooth 输入作真实恢复，不附加未经证明的同阶误差估计。

这给一个具体改进：以后延拓不必依赖旧坐标中特定的 $F_\upsilon$ 或 $F_\upsilon+R F_\gamma$ 始终不为零。只要还在本稿合法 scalar 域，就能用完整 null 坐标继续消去一速度；大的八矩历史本身不会使(54)失去正则性。

## 12. 已付范围与下一真实返回问题

本稿完成的是同一个真实有限母库上的三件事：

1. 原二十行、四自然约束、整个 $\mathcal F_{\rm path}$、共同 cap/宽度/种子和十三新值由一个原窗口内的有限正根同时支付。
2. 完整速度二次型在预定合法 scalar 盒上严格不定，且独立于全部八矩和固定第三规范；未付的第三平方量有(35)(36)的真实能量上界。
3. 同一完整 source 有全八矩代数域上的正则速度图，并能从同母 R531 的真实负 $p_1$ 段平滑接入，完整继承前缀。

这些结论不使(55)自动成为完备流。其 $m$ 方程仍含真实速度平方，$\Delta$ 可以随 $m$ 二次增长；有限时间爆破、scalar 离开预定盒、端口及 pose 配平仍需实际控制。也没有从局部负 $p_1$ 推出整段负积分、总 $M=0$、第三返回、原 period 或同一十三规范。

特别，(55)的任意自由输入不会自动把八矩当成可任意指定的八个控制量。后继真实问题已经准确变为：在这个不因历史而丢失速度正则性的同一个系统内，选择一个实际非零输入及必要的 chart 交换，完成有界路径、全八矩与末 germ/pose 的配平。它仍保完整原基准，不能借 R518 的无 ruling 桥代替。

独核说明：root全文纸读；literature独立回读R520完整低阶表并核过全history速度次数、唯一关系及删除系数、原Z最低两行、固定I内33列正锥、有限Λ后有限N的三导能量界、完整B1恢复、全盒不定式与null坐标。全部仅纸审，没有新科学执行；未把正则图当作完备流、任意m可达、总M0或闭合证明。
