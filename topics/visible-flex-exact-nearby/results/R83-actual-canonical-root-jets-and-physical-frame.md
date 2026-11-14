# R83：实际 canonical 根 jet、首两个 Airy 势系数与物理通量框架

2026-11-12，independent-audit。

**状态：完整证明并完成同一公共参数盒上的真实全角有向覆盖。**
本篇针对当前真实非径向参数族，计算 R53 校正 Airy 试解中的
\(v_0=V(0,\phi)\)、\(v_1=V_\xi(0,\phi)\)，同时保留物理高度、根源
因子和真实 Cauchy 动量的 shear。本篇不把这两个根系数当成整个 collar
上的势、完整试解残差或全反馈逆常数；最后一节明确它们如何接入这些尚待
实际支付的量。

## 1. 同一准确公共参数盒和真正根

使用当前 R57 准确仿射族，中心与范围为
\[
 \delta_5=-\frac{7789843107295549}{4611686018427387904},\qquad
 |\delta-\delta_5|\le\frac1{2500000}.
 \tag{83.1}
\]
这正是
`notes/2026-11-12-common-core-exterior-parameter-interval.json`
所记录的公共盒，严格包含于 R80 的 \(\delta_5\pm5\,10^{-7}\) 与
R69/R81 的 \(\delta_4\pm5\,10^{-7}\) 两个已付盒中。

实际根采用
`data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json`
的准确有理传输区间。本程序检查 origin、direction 的 SHA 及整个参数盒
包含关系；各参数仍使用自己的真正根 \(t=t(\delta)\)，没有把其中点当
成所有参数的根。正根严格位于一个实际共同 spline span 内；每个 scalar
及其径向反射的 span 都另外准确检查并记录。

原始 phase 和 mean direction 先形成准确多项式 germ，再乘同一个实
参数球。所有后续积分原函数都是 R33 的真实无限角频原函数，不是有限
primitive 的另一个对象。

## 2. 先消去真实密度中的重复因子

采用 [R64](R64-actual-positive-collar-source-and-dn-input.md) 的同一个
全 \(\ell\) 零阶口径，正侧 \(Y=Y_z=F_z/|F|>0\)，使
\[
 Y\widehat P(Yu)=\operatorname{div}(B\nabla u).
 \tag{83.2}
\]
这里 \(\widehat P\) 是 [R37](R37-fixed-type-metric-defect-newton-interface.md)
的实际目标型别算子，并未用旧径向背景替换其系数。

向量以旋转柱坐标基表示。令 \(X=F_r\)、
\(T=(-\cos\gamma\sin\beta,\cos\gamma\cos\beta,\sin\gamma)\)，所以
\(F_\theta=aT\)。置
\[
\begin{split}
 h&=-\sin\beta X_1+\cos\beta X_2,&
 v&=-\cos\beta X_1-\sin\beta X_2,\\
 Q&=\cos\gamma X_3-\sin\gamma h,&
 W&=Q^2+v^2,\\
 D&=(1+\beta_\theta)\cos\gamma Q-\gamma_\theta v,&
 M&=\beta_r\cos\gamma Q-\gamma_r v,\\
 H&=(T\times X)\cdot F.
\end{split}
\tag{83.3}
\]
其中物理角导数的 \(1+\beta_\theta\) 包含旋转基的变化。R64 的准确式是
\[
 B=\begin{pmatrix}
 \alpha&-\alpha M/D\\
 -\alpha M/D&\alpha(M/D)^2+\eta K_0
 \end{pmatrix},\quad
 \alpha=\frac{F_z^2D}{H^2},\qquad
 \eta=\frac{F_z^2W^2}{DH^2}.
 \tag{83.4}
\]
在正根令
\[
 \kappa(r)=\frac{K_0(r)}{r-t},\quad
 q=\frac MD,\quad
 U=\alpha\kappa\eta=\frac{\kappa F_z^4W^2}{H^4},\quad
 V_* =\frac{\kappa\eta}{\alpha}=\frac{\kappa W^2}{D^2}.
 \tag{83.5}
\]
这里 \(V_*\) 是正主系数比，**不是** canonical 势 \(V\)。实际计算
先使用右侧已消去的表达式，再取
\[
 u=\log U=\log\kappa+4\log F_z+2\log W-4\log H,
 \qquad w=\log V_* =\log\kappa+2\log W-2\log D.
 \tag{83.6}
\]
每一个正因子都单独验证。这样避免将本来完全抵消的 \(F_z,H\) 因子
在区间运算中独立除乘；没有删去实际零阶项或改变高度共轭。

## 3. 真正根锚定 shear 的有限 jet

负侧取 \(x=t-r\ge0\)。根锚定角流为
\[
 \Theta_x=q(t-x,\Theta),\qquad \Theta(0,\zeta)=\zeta,
 \qquad J=\Theta_\zeta>0.
 \tag{83.7}
\]
将原 \((r,\theta)\) 密度准确拉回 \((x,\zeta)\)，得到
\[
 \operatorname{diag}(A,-xB_1),\qquad
 A=(\alpha\circ\Theta)J,\quad
 B_1=(\kappa\eta)\circ\Theta/J.
 \tag{83.8}
\]
因此对固定 \(\zeta\) 的真实横向微分是
\[
 \mathscr D=-\partial_r+q\partial_\theta,
 \qquad \partial_x\log J=q_\theta\circ\Theta.
 \tag{83.9}
\]
所有下式在实际根 \((t,\zeta)\) 取值，且 Taylor 系数采用除以阶乘的
规范。对 \(j=1,2,3\) 定义
\[
 s_j=\frac{\mathscr D^ju}{j!},\qquad
 h_j=\frac{\mathscr D^jw}{2j!}
        -\frac{\mathscr D^{j-1}q_\theta}{j!}.
 \tag{83.10}
\]
这给出两个准确展开
\[
 \log\frac{AB_1}{A_0B_{10}}=s_1x+s_2x^2+s_3x^3+O(x^4),
 \qquad
 \frac12\log\frac{B_1/B_{10}}{A/A_0}
   =h_1x+h_2x^2+h_3x^3+O(x^4).
 \tag{83.11}
\]
特别是 \(\log J\) 在第一个式子准确抵消，在第二个式子留下真实的
\(-\mathscr D^{j-1}q_\theta/j!\)。不能只算径向导数而丢掉这个实际
非径向 shear。

## 4. 根角、高度和它产生的零阶导数

按 [R39](R39-finite-component-airy-transfer-input.md) 定义
\[
 y=Y_0(\zeta),\quad Y_0'=\sqrt{A_0/B_{10}}=e^{-w_0/2},\quad
 \ell=\int_0^{2\pi}Y_0'\,d\zeta,\qquad
 t_0=(A_0B_{10})^{-1/4}=e^{-u_0/4}.
 \tag{83.12}
\]
这里下标 0 表示在根上取值；\(Y_0\) 是角坐标，不能与球面高度
\(Y=F_z/|F|\) 混淆。先作角换元，再置旧未知量 \(u=t_0v\) 并左乘
\(t_0\)。新主系数 \(a=A/A_0,b=B_1/B_{10}\) 在根上同为 1。
尽管 (83.2) 的 grounded 算子无零阶，新高度产生准确零阶
\[
 q_*(x,y)=-x\,t_0\partial_y(B_1Y_0'\partial_y t_0).
 \tag{83.13}
\]
令 \(g=\log t_0=-u_0/4\)，则
\[
 q_*(0)=0,\qquad
 q_1:=\partial_xq_*(0)
 =-e^{w_0}\left[g_{\zeta\zeta}+g_\zeta^2
                  +\frac12(u_0+w_0)_\zeta g_\zeta\right].
 \tag{83.14}
\]
证明为 \(\partial_y=(Y_0')^{-1}\partial_\zeta\) 直接代入；系数
\(t_0^2B_{10}/Y_0'=B_{10}/A_0=e^{w_0}\)。这个二阶角项也没有用角平均
或径向公式替换。

## 5. 不解完整流也能准确取得前三阶 canonical 系数

置 \(d=\sqrt{b/a}\)。由 (83.11)，
\[
 d=1+d_1x+d_2x^2+d_3x^3+O(x^4),\qquad
 d_1=h_1,\quad d_2=h_2+\frac12h_1^2,\quad
 d_3=h_3+h_1h_2+\frac16h_1^3.
 \tag{83.15}
\]
R39 的准确逆特征标签满足
\(S_{\pm,z}\pm2z^2d(z^2,y)S_{\pm,y}=0\)，\(S_\pm(0,y)=y\)，
其中 \(x=z^2\)。逐系数代入给
\[
 S_\pm=y\mp\frac23z^3\mp\frac25d_1z^5
       \mp\frac27d_2z^7+\frac1{10}(d_1)_y z^8
       \mp\frac29d_3z^9+O(z^{10}).
 \tag{83.16}
\]
例如 \(z^8\) 项来自
\(-2\partial_y(-2d_1/5)/8=(d_1)_y/10\)；两个分支的此项相同。
常数 \(d(0,y)=1\) 的角导数为零，因而没有遗漏更早的反射平均项。

由 R39 的
\(\phi=(S_++S_-)/2\)、
\(\xi=x[3(S_--S_+)/(4z^3)]^{2/3}\)，有
\[
 \phi=y+O(x^4),\qquad
 \xi=x+cx^2+ex^3+fx^4+O(x^5),
 \tag{83.17}
\]
其中
\[
 \boxed{
 c=\frac25d_1,\quad
 e=\frac27d_2-\frac1{25}d_1^2,\quad
 f=\frac29d_3-\frac2{35}d_1d_2+\frac4{375}d_1^3.}
 \tag{83.18}
\]
这些是准确 Taylor 恒等式，没有把短流的样本拟合成导数。
\(\phi-y=O(x^4)\) 说明它不影响下面 \(\log\alpha_c\) 的前三阶
系数；这里 \(\alpha_c\) 是 canonical 密度因子，不是 (83.4) 的
物理 \(\alpha\)。

R39 给 \(\alpha_c=\sqrt{xab/\xi}\)。先以 \(x\) 为自变量，写
\[
\begin{split}
 l_1&=\tfrac12(s_1-c),\\
 l_2&=\tfrac12(s_2-e+c^2/2),\\
 l_3&=\tfrac12(s_3-f+ce-c^3/3).
\end{split}
\tag{83.19}
\]
再用 \(x=\xi-c\xi^2+(2c^2-e)\xi^3+O(\xi^4)\)，得到
\[
 \log\alpha_c=L_1\xi+L_2\xi^2+L_3\xi^3+O(\xi^4),
\quad L_1=l_1,\quad L_2=l_2-cl_1,\quad
 L_3=l_3-2cl_2+(2c^2-e)l_1.
 \tag{83.20}
\]

## 6. 实际首两个 Airy 势系数和全部根 frame

R39 的完整势恒等式为
\[
 V=\frac{q_0}{\alpha_c}-\frac12(\log\alpha_c)_{\xi\xi}
   -\frac14(\log\alpha_c)_\xi^2
   +\xi\left[\frac12(\log\alpha_c)_{\phi\phi}
             +\frac14(\log\alpha_c)_\phi^2\right],
 \tag{83.21}
\]
\(q_0\) 包含完整坐标 Jacobian。根处 \(\alpha_c=1\)、坐标 Jacobian
为 1、\(q_*=0\)、\(\log\alpha_c=0\)；最后一项到一次 \(\xi\) 都无
贡献。由 (83.14)、(83.20) 准确得到
\[
 \boxed{v_0=-L_2-\tfrac14L_1^2,\qquad
 v_1=q_1-3L_3-L_1L_2.}
 \tag{83.22}
\]
正侧的 R53 口径 \(V_+(s,\phi)=-V(-s,\phi)\) 因而满足
\(V_+(0)=-v_0\)、\(\partial_sV_+(0)=v_1\)。真实 common-root shear
\(\Gamma^{-1}M_{v_0}\Gamma^{-1}\) 使用的是这个实际 \(v_0\)。

根上的 physical-to-canonical height 为
\[
 h_{\rm ph}=Yt_0,\qquad w_{\rm ph}=h_{\rm ph}U.
 \tag{83.23}
\]
以 \(x\) 指向负曲率核心，令 \(\pi_g\) 为 grounded 算子在
\((x,\zeta)\) 中的 Cauchy 动量。它与原物理 \(r\) 动量的准确关系为
\(\pi_g=-(Y\pi_w-w\pi_Y)\)。根角变换、高度和最后
\(\alpha_c^{-1/2}\) 共轭给
\[
 \boxed{\quad U_\xi=\frac{t_0}{Y_0'}\pi_g+\frac{L_1}{2}U.\quad}
 \tag{83.24}
\]
证明：角密度使动量乘 \((Y_0')^{-1}\)，第一高度乘 \(t_0\)；最后
\(v=\alpha_c^{-1/2}U\) 的动量在根上为
\(U_\xi-(L_1/2)U\)。这一实 shear 不能当作“主半密度相同”而略去。
若换成外法向 DN 动量，须按该端的外法向同步换符号。

对物理密度源 \(f\)，根上的准确因子为
\[
 f_{\rm can}|_0=\frac{t_0Y}{Y_0'}f|_0.
 \tag{83.25}
\]
这是两次左乘高度、两个坐标密度 Jacobian 的直接结果；不声称根上的
乘子界已控制整个体源。程序同时记录 (83.22)–(83.25) 以及
\(t_0/Y_0'\) 的 canonical 角导数，保持零模及各 Fourier lag，不删
真实平均行或 source/contact 项。

## 7. 有向有限 jet 实现及无限原函数费用

实现为 `scripts/fourfold_phase_canonical_root_jets.py`。内部径向变量
\(z_r\) 满足 \(r=t-\rho z_r\)、\(\rho=1/1024\)。所以
\(\mathscr D=\rho^{-1}\partial_{z_r}+q\partial_\theta\)。实际根曲率
Taylor 系数先由真实无限 \(E=\langle|F_r|^2\rangle\) 计算，再使用
\[
 \kappa^{[j]}=-K_0^{[j+1]}/\rho.
 \tag{83.26}
\]
这里准确关系 \(K_0(t)=0\) 只用于去掉常数项，绝不将包含零的区间除以
\(z_r\)。输入的高径向阶全部来自根所在的同一个实际多项式 germ；
并不由全域 C⁴ 样条推断跨 knot 的高径向光滑。

Q512 有限 Fourier 原函数先加上 [R52](R52-root-taylor-finite-part-and-directed-budget.md)
的无限 alias/tail 和径向 Cauchy 费用，再作任何角导数。较大径向复盘
只用于这个多项式 germ 的解析延拓和其导数费用，不声称越过 knot 后
仍是实际全域 spline。

还有一个比逐 Fourier 相位盒更紧的真实连续角覆盖。对每个径向 Taylor
系数，旋转柱坐标恒等式仍为
\[
 F_\theta=aT-J_{\rm rot}F,\qquad
 J_{\rm rot}(F_1,F_2,F_3)=(-F_2,F_1,0).
 \tag{83.27}
\]
在一个实角盒中心 \(c\) 先付真实无限 \(F(c)\)，令
\(Z=F-F(c)\)、\(G=aT-J_{\rm rot}F(c)\)。则
\(Z'=G-J_{\rm rot}Z\)、\(Z(c)=0\)。若半宽为 \(h\)，在全盒内
\(|G_j|\le M_j\)，实旋转的 Duhamel 式给
\[
 |Z_1|\le hM_1+h^2M_2/2,\quad
 |Z_2|\le hM_2+h^2M_1/2,\quad |Z_3|\le hM_3.
 \tag{83.28}
\]
这对每个真实径向系数分别成立。然后由 (83.27) 逐角阶递推，生成
真实混合 jet；没有对截断 primitive 直接求角导来代替无限对象。

有限 jet 的矩形乘法使用已付 TimeAngleJet 的防 carry Kronecker stride。
每次微分准确缩小已知的径向、角向范围，未知系数从不补零。初等函数
采用系数递推，常数项先在 Arb 中取真实分支。例如
\[
 (e^f)_0=e^{f_0},\quad
 (e^f)_j=\frac1j\sum_{k=1}^j kf_k(e^f)_{j-k};\qquad
 (f^{-1})_j=-f_0^{-1}\sum_{k=1}^j f_k(f^{-1})_{j-k}.
 \tag{83.29}
\]
\(\log f\) 由 \((\log f)'=f'/f\) 同样递推。先在径向系列中作此递推，
再按角阶作同一递推，故没有由区间 Newton 中“一个球减去自身”产生的
虚假常数项损失。初等函数分支始终由已验证的实际正因子固定。

整个物理 quarter \([0,\pi/2]\) 用准确有理比例的角盒覆盖，失败盒只
能细分，不能忽略。数值部分可以只覆盖 \([0,\pi/4]\)，再按下节的
准确反射推导另一半。两部分都用 Fraction 检查无缝、无重叠覆盖，
再由实际四重周期覆盖全 \(2\pi\)。canonical 角导数始终通过
\[
 \partial_\phi=(Y_0')^{-1}\partial_\zeta=e^{w_0/2}\partial_\zeta
 \tag{83.30}
\]
重复计算，不能误用物理 \(\theta\) 导数或少乘四倍。

对两根，准确径向反射给 \(\alpha,\eta,K_0\) 偶、\(M/D\) 奇。
在负根取 \(x=t+r\) 指向核心，并用正 ground state \(-Y_z\)。其根
锚定方程和上述所有标量 jet 与正根相同；没有额外角 involution。
因此一份完整 quarter 证书同时支付两个真实转折的这些有限数据。

### 7.1. 同一对象的准确半 quarter 反射

当前准确族的 \(\beta,\gamma\) 都是 \(\sin(4k\theta)\) 的有限和。
其系数包含完整的参数盒；这条恒等式不依赖参数取中心。由 R33 的
无限原函数及真实对称 mean，
\[
 (F_1,F_2,F_z)(r,-\theta)=(F_1,-F_2,F_z)(r,\theta)
\]
在旋转柱坐标中成立，\(F_r\) 也满足相同恒等式。逐项代入 (83.3)
可知 \(h\) 为奇函数，\(v,Q,W,D,H,F_z\) 为偶函数，而 \(M,q\) 为
奇函数。因此 \(\alpha,\kappa\eta,u,w\) 为偶函数。
\(\mathscr D=-\partial_r+q\partial_\theta\) 保持偶性，\(q_\theta\)
为偶函数，故 (83.10)–(83.25) 中记录的六个标量及所有正因子都为
偶函数。这里使用完整的实际密度、height 与 shear，没有只反射主符号。

同时所有这些旋转柱坐标标量都具有 \(\pi/2\) 周期。因此
\(\theta\mapsto\pi/2-\theta\) 保持上述偶标量。选 \(Y_0(0)=0\)，
由 \(Y_0'\) 的偶性与周期性，准确有
\[
 Y_0(\pi/2-\theta)=\ell/4-Y_0(\theta).
 \tag{83.30a}
\]
于是记录的第 \(j\) 个 canonical 角导数在反射时只乘
\((-1)^j\)，其绝对上界保持不变。

程序 `fourfold_phase_canonical_root_symmetry_cover.py` 将这项代数
恒等式与真正数值数据分开记录。它只取原报告中准确 quarter 比例
\([0,1/2]\) 上的已完成叶，检查每个叶的源、对象、参数盒及正因子，
再检查原叶与反射叶 \([a,b]\mapsto[1-b,1-a]\) 准确铺满 \([0,1]\)。
原始 native 报告保留其 partial 标志；另一个完整报告明确记录
哪些半圈叶经过计算、哪些由准确对称推出。它不把没有计算的叶伪造
成新的区间运行，也不把反射用于一个不同的近似对象。

同样，若半 quarter 上 \(Y_0'\) 的逐叶界为 \(m_i,M_i\)，
且叶的准确 quarter 比例长度为 \(b_i-a_i\)，则
\[
 2\sum_i(b_i-a_i)m_i
 \le \frac{\ell}{2\pi}\le
 2\sum_i(b_i-a_i)M_i.
 \tag{83.30b}
\]
倒数给完整物理圆频率 \(q=2\pi/\ell\)；四重输入的真实频率仍为
\(4q|j|\)，不把 quarter 的归一指标误当物理角频率。

## 8. 与 R53 首阶校正及仍需实际支付的余项

本篇精确计算的是 R53 正侧多项式
\[
 B_+(s,\phi)=-v_0(\phi)+\frac13v_1(\phi)s,\qquad
 C_+(s,\phi)=\frac12(v_0)_\phi s^2
 \tag{83.31}
\]
及其 common-root shear 所需的真实系数。若报告给
\(M_{j,0}=\|\partial_\phi^jv_0\|_\infty\)、
\(M_{j,1}=\|\partial_\phi^jv_1\|_\infty\)，则任意明确
\(0\le s\le h\) 上已有可直接代入的准确费用
\[
\begin{split}
 \|\partial_\phi^jB_+\|_\infty&\le M_{j,0}+hM_{j,1}/3,&
 \|\partial_s\partial_\phi^jB_+\|_\infty&\le M_{j,1}/3,\\
 \|\partial_\phi^jC_+\|_\infty&\le h^2M_{j+1,0}/2,&
 \|\partial_s\partial_\phi^jC_+\|_\infty&\le hM_{j+1,0},\\
 \|\partial_s^2\partial_\phi^jC_+\|_\infty&\le M_{j+1,0}.
\end{split}
\tag{83.32}
\]
这直接控制 R53 中真实 \(C_{+,ss}\) 项，并显示为何不能把该项假定为
零而声称更高 source 增益。

但是完整 R53 源常数还需要：实际有限坐标延拓的
\(E=s^5e\)、\(E_s=s^4\widetilde e\) 全 collar 界；势的对应全 collar
Taylor 余项；实际 cutoff 导数；(83.23)–(83.25) 的整个体域转换。
本篇根 jet 没有自动支付这些量。R81 约 \(10^{60}\) 的四阶粗接触费
也不能据此静默替换为一个小常数。后续高频 cutoff 必须把这些实际余项
与同一有限低块联合检查，而不是只给一个不可执行的巨大 cutoff。

## 9. 完整覆盖输出与重放

归档中原生 gzip 报告为 8,008,151 字节，超过仓库单文件上限，
所以永久保存为两个均小于 5 MB 的准确二进制片段。它们位于
`notes/2026-11-12-R83-native-root-jets-parts/`；同目录 manifest
记录准确字节偏移、各片 SHA 和原始完整 SHA。重组只拼接原字节，
不重新压缩或重写 JSON，因此严格恢复本节下方引用的原报告：

```bash
python scripts/fourfold_phase_root_jets_reassemble.py
```

原 8 MB 文件只是可删除、可按字节重建的本地缓存，不列入提交清单。
若需要从真实输入重新运行区间计算，而非重组已有原始证据，命令为：

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_phase_canonical_root_jets.py \
  --cells 256 --last-cell 128 --order 4 \
  --out notes/2026-11-12-actual-canonical-root-jets.json.gz
python scripts/fourfold_phase_canonical_root_symmetry_cover.py \
  --raw notes/2026-11-12-actual-canonical-root-jets.json.gz \
  --out notes/2026-11-12-actual-canonical-root-full-cover.json.gz
```

完整证书使用 **2882 个真正计算的半 quarter 叶**，以 (83.30a)
推导另半，得到 **5764 个 quarter 覆盖叶**，再由准确四重周期覆盖
整个圆。原 native 文件还包含若干已算的后半叶；完整证书只引用前
半的准确逐叶 SHA，原文件的 partial 标志原样保留。

同一参数盒、两根和所有角的严格安全界如下。导数是实际 canonical
\(\phi\) 导数，表中都是向外放宽的绝对上界：

| 实际根标量 | 0 阶 | 1 阶 | 2 阶 | 3 阶 | 4 阶 |
|---|---:|---:|---:|---:|---:|
| \(v_0\) | \(1.821\,10^4\) | \(3.936\,10^7\) | \(1.964\,10^{11}\) | \(1.539\,10^{15}\) | \(1.595\,10^{19}\) |
| \(v_1\) | \(1.971\,10^7\) | \(7.117\,10^{10}\) | \(4.191\,10^{14}\) | \(3.615\,10^{18}\) | \(4.216\,10^{22}\) |
| \(L_1/2\) | \(37.684\) | \(2.833\,10^4\) | \(1.227\,10^8\) | \(8.367\,10^{11}\) | \(7.508\,10^{15}\) |
| \(Yt_0\) | \(0.346098\) | \(2.008\) | \(2360\) | \(8.317\,10^6\) | \(4.711\,10^{10}\) |
| \(Yt_0/Y_0'\) | \(7.05023\) | \(4353\) | \(1.652\,10^7\) | \(9.290\,10^{10}\) | \(7.247\,10^{14}\) |
| \(t_0/Y_0'\) | \(28.76172\) | \(17773\) | \(6.735\,10^7\) | \(3.789\,10^{11}\) | \(2.956\,10^{15}\) |

正因子与圆长另外得到
\[
\begin{gathered}
 .02835622<\alpha<.13299382,\qquad
 1.59157635<\kappa\eta<15.64702428,\\
 .04262662<Y_0'<.28888848,\qquad
 1.20504609<t_0<1.47475935,\\
 .53830570<\ell<.75447538,\qquad
 8.32788647<q<11.67215063.
\end{gathered}
\tag{83.33}
\]
这里的圆长界由 (83.30b) 的逐叶积分获得，不是把全局 \(Y_0'\) 极值
直接乘 \(2\pi\)。表中高导数仍有明显区间依赖放大；它们是有效上界，
不是实际导数量级的数值猜测，也不保证据此得到的最终低块规模可行。

完整文件 `notes/2026-11-12-actual-canonical-root-full-cover.json.gz`
的 SHA256 为
`addf217533bed260fa7860613cc3246db0eb57f0e6d727361aa27d7f116462d8`。
其引用的原始有向叶文件 SHA256 为
`bf809f858696892b02f3d82420bad89be535e0d9df15677826140346b05f00e6`。
原生源、对称闭合源、准确对象、moving-root 输入、无限原函数依赖和
逐叶 SHA 都在完整证书中逐项记录并检查。

这个已经完成的实际输入继续接 §8 的完整 collar 源预算；单角诊断
或表中根值本身仍不能替代该体域预算。
