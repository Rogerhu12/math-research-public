# R778 — 原全部 S174 的完整有限角色、所有 physical finite-χ 负一平方与十七不分歧点域

日期：2026-11-15。**状态：已证明。**

本篇接齐 R772 的整个实际 degree174 来源，而非只处理其中的 degree58 拉回子空间。全部二处、三处、二十九处有限 Weil 方向、原半特征、角型、primitive Euler 因子、普通周期和 finite-p 门都保留。

对本篇每一个存活的 finite-character 负一值，给出其自己的完整 type-(1,0) 角色 ν，证明其 root number 准确为 −1，并将原值乘共同周期后放入
$$
\overline{\mathbf Q}\log_{\omega_0}
 \bigl(E_0(H)_{\mathbf Q}\otimes_K\overline{\mathbf Q}\bigr),
\qquad E_0:y^2=x^3+1,
$$
其中点坐标域 H 在17处不分歧。标量系数可在17处分歧；它们不属于 point-factor Galois 动作。

此结论覆盖 R772 的全部实际有限门及正交伙伴 jets。没有宣称这些值逐个非零，没有从原中央零赋它们为零，也没有将 point-factor 投影交换到任意无限 p-adic 极限。

## 1. 原标准空间和符号

沿 R772、R776，固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad \delta^2=-3,\quad
\alpha=87,\quad N_\theta=174.
\tag{1}
$$
原有限加性角色为
$$
\psi_{\ell,\mathrm{add}}(x)=e^{-2\pi i\{x\}_\ell},
$$
无穷处为 e^{2πix}，Yang 极化是 X=Qδ。记 ψ0 为
E0 的 type-(1,0) Hecke 角色，取原2δ-primary 规范。
其 unitary 部分在2处为 Teich、uniformizer2值−1；
在3处单位为 residue quadratic、δ值+i；在其余 inert 好素数的
有理 uniformizer 上值−1。

R776 已支付整个标准空间的精确有限模型
$$
\mathscr V_2\otimes\mathscr V_3\otimes\mathscr V_{29},
\qquad \dim=2\cdot3\cdot29=174.
\tag{2}
$$
二处
$$
\mathscr V_2=\operatorname{span}(f_A,f_B),\quad
f_A=e_0-e_2,\quad f_B=e_1+e_3,\quad
e_j=\mathbf1_{j/2+2\mathbf Z_2}.
$$
三处的三个实向量为 R776 的
$$
\phi_0,\quad \phi_{\mathrm e},\quad\phi_{\mathrm o},
\qquad \|\phi_0\|^2=3,\quad
\|\phi_{\mathrm e}\|^2=\|\phi_{\mathrm o}\|^2=6.
\tag{3}
$$
二十九处是全部
e_c=\mathbf1_{c/29+\mathbf Z_{29}}，c∈F29。
R776 的实际支撑 n/522、半特征
(-1)^n a_{n+174}=−a_n，将 (2) 单射且满射地识别为
H0(E0,O(174[0]))。本篇所有局部谱都在这个同一模型中进行。

## 2. 二处绝对矩阵：α87 的两线次序与 α17 不同

取 ζ8=e^{πi/4}、t±=(1±√3)/√2。以原 χ2^0=Teich、χ2^0(2)=−1
作 Hecke splitting。在 (fA,fB) 上，α87 的真实矩阵为
$$
\boxed{
M_\omega^{(87)}
 =\frac{\omega^2}{\sqrt2}
    \begin{pmatrix}
    -\zeta_8^{-1}&-i\\
    -i&-i\zeta_8^{-1}
    \end{pmatrix}
 =\omega\,\overline{M_\omega^{(17)}} .
}
\tag{4}
$$
因而
$$
v_0=f_A+t_-f_B,\quad M_\omega^{(87)}v_0=v_0,
\qquad
v_1=f_A+t_+f_B,\quad M_\omega^{(87)}v_1=\omega v_1.
\tag{5}
$$
不能沿用 α17 的两个标签次序。范数仍为
$$
n_{2,e}:=\|v_e\|^2=3+(2e-1)\sqrt3,\qquad e=0,1.
\tag{6}
$$

这里的绝对号可直接从 R290 使用的 Rao–Yang 公式核定。
在 g=ω，αy(1−x)=261/4，其原二次 Weil 指数为 ζ8^-1，
所以 μ(ω)=−ω²ζ8^-1。四陪集 kernel 与 α17 的 kernel 互为共轭，
因为87+17=104，代入四陪集后的差为整相位；这给 (4)。

对
$$
g_*=\frac{-11+4\delta}{13},
$$
原积分的非零输出指标仍是 a≡3b+2 mod4。
此时 μ(g*)=ζ8³；偶输入指标的 kernel 相位为 ζ8^{-87}，
奇输入指标为 ζ8^{3\cdot87}。相乘依次是 −1,+1,−1,+1。
所以真实四陪集矩阵仍为
$$
\begin{pmatrix}
0&0&-1&0\\0&1&0&0\\-1&0&0&0\\0&0&0&1
\end{pmatrix}.
\tag{7}
$$
它逐个固定 fA、fB。对 −g* 同一个偶函数 kernel 与同一个
μ=ζ8³ 给相同作用，因此 −1 也固定整个二处子空间。

R290 的原 μ3、−1、g* 拓扑生成 K2^1 的证明不依赖 α。
故 (4)—(7) 支付整个本地环面。将单位角色改为
Teich^{1+e} 时，splitting 在 ω 上多乘 ω^{2e}，
在 g*、−1 上不变，于是 ve 准确成为不变向量。
这是全局正权表中二处角色的来源。

## 3. 二十九处：完整有限环面、缺失标签和实向量

设
$$
T_{29}=\{x+y\delta\in\mathbf F_{29^2}^{\times}:x^2+3y^2=1\}.
$$
它为30阶循环群。选生成元 g29 使 g29^{10}=ω，
并固定 τj(g29)=ζ30^j，ζ30=e^{2πi/30}。

在 (2) 的原二十九陪集上，Yang 奇-conductor lattice 的
μ4 splitting 是
$$
\boxed{
W(x+y\delta)_{ab}
 =-\frac{(y/29)}{\sqrt{29}}\,
   e_{29}^{\,\frac9{2y}\{x(a^2+b^2)-2ab\}}\quad(y\ne0),
\quad W(1)=I,\quad W(-1)e_a=e_{-a}.
}
\tag{8}
$$
分子9是原 −Δ·(α/29)=9。不能把 α17 的分子3原样搬来。
Gauss 归一中的 (9/2\,/29)=−1 给出显示的负号。

公式 (8) 也可直接由有限合成核定：两次 kernel 的中间二次项系数为
9y3/(2y1y2)，其中 y3=x1y2+x2y1；完整二次 Gauss 和正好恢复
(8) 的 prefactor。退化的 y3=0 给 I 或反射，不丢中心项。
其 character 为
$$
\operatorname{tr}W(1)=29,\qquad
\operatorname{tr}W(g)=-\tau_{15}(g)\quad(g\ne1).
\tag{9}
$$
故
$$
\Pi_j=\frac1{30}\sum_{g\in T_{29}}\tau_j(g)^{-1}W(g),
\qquad
\operatorname{rank}\Pi_j=
\begin{cases}1,&j\ne15,\\0,&j=15.\end{cases}
\tag{10}
$$
这也是 Yang 的“缺失唯一 quadratic torus character”在本实际模型中的精确形式。

对每个 j≠15，选最小 a_j 使 Πj e_{a_j}≠0，并定义
$$
f_j=\Pi_j e_{a_j},\qquad
n_{29,j}=\sum_{a\bmod29}|f_j(a)|^2>0.
\tag{11}
$$
不把 n29,j 规范成1。由 (8)，
overline(W(g))=W(g^-1)，所以 Πj 是实矩阵；
又 W(−1)f_j=(−1)^j f_j。因此 fj 是非零的实向量，奇偶性准确为 (−1)^j。

对于未分歧基 Hecke 角色，真实 Hecke splitting 与 (8) 的差是
τ15。若令
$$
\vartheta_j(u)=(u\bmod29)^{28(j-15)}
\tag{12}
$$
并使用 g29↦ζ30 的根单位提升，则 Hilbert90
u/bar u=u^-28 给出相对角色 τ15-j。
所以真正 Hecke splitting 作用为 τ15·τ15-j=τ_-j，
恰好取消 fj 的 τj。特别 (12) 是完整本地单位角色，
不是从某个 CM13/CM19 特征猜得。

其几个值为
$$
\vartheta_j|_{\mathbf F_{29}^{\times}}=1,\quad
\vartheta_j(\omega)=\omega^j,\quad
\vartheta_j(\delta)=(-1)^{j+1};
\tag{13}
$$
j≠15 保证它非平凡。

## 4. 全部174个标签与真实全局有限角色

用
$$
\ell=(e,a,\sigma,j),\qquad
e\in\{0,1\},\quad
(a,\sigma)\in\{(0,+1),(1,+1),(1,-1)\},\quad
j\in\mathbf Z/30,\ j\ne15
\tag{14}
$$
标记原全部线。三处 (a,σ) 分别对应 φ0、φe、φo。
其角 r=rℓ∈{0,…,5}由
$$
\boxed{
r\equiv-e-a-j\pmod3,\qquad
(-1)^r=\sigma(-1)^j
}
\tag{15}
$$
唯一确定。

令 γ3 为三处单位的真正 conductor-δ² cubic 角色：
$$
\gamma_3(\epsilon\omega^b\bmod\delta^2)=\omega^b.
$$
定义固定有限 Hecke 角色 ηℓ 的单位表
$$
\boxed{
\eta_{\ell,2}=\operatorname{Teich}^{\,r+e}
             =\operatorname{Teich}^{-a-j},\quad
\eta_{\ell,3}=\gamma_3^a,\quad
\eta_{\ell,29}=\vartheta_j .
}
\tag{16}
$$
其余有限处不分歧。在 ω 上三因子乘积为
ω^{r+e+a+j}=1，在 −1 上都为1。
hK=1 因而给出无歧义的完整定义：
对素于2·3·29的主理想 (z)，
$$
\eta_\ell((z))
 =\bigl(\operatorname{Teich}(z\bmod2)^{-a-j}
          \gamma_3(z)^a\vartheta_j(z)\bigr)^{-1}.
\tag{17}
$$
全部指定 uniformizer 由主 idèle 积关系确定为
$$
\eta_{\ell,2}(2)=1,\qquad
\eta_{\ell,29}(29)=1,\qquad
\eta_{\ell,3}(\delta)=(-1)^{j+1}.
\tag{18}
$$
例如 δ 在2处为1模2，而在29处有 (13) 的值；
这给最后一式，不能任意取1。

完整 ηℓ 在有理 idèle 上平凡，且
ηℓ^*=ηℓ^-1。它只在2、3、29处分歧。
不同角线可能有相同 ηℓ；其完整来源仍由 (14)、(15) 区分，
不把174个线标签误说成174个不同有限角色。

对于每一个非负 m≡r mod6，真正的正权角色是
$$
\boxed{\Phi_{\ell,m}=\eta_\ell\psi_0^{\,2m+1}.}
\tag{19}
$$
它的 unitary 有限表为
$$
\begin{array}{c|c|c}
v&\text{单位值}&\text{uniformizer 值}\\ \hline
2&\operatorname{Teich}^{1+e}&-1\text{ 于 }2\\
3&(\epsilon\omega^b)\mapsto\epsilon\omega^{ab}
       &-i\sigma\text{ 于 }\delta\\
29&\vartheta_j&-1\text{ 于 }29 .
\end{array}
\tag{20}
$$
三处的 uniformizer 是
i^{2m+1}(-1)^{j+1}=−i(-1)^{m+j}=−iσ。
所以 (20) 精确包含 R776 的两个相反 δ 符号。

其完整 primitive conductor 为
$$
\mathfrak f_\ell=(58\delta^{\,1+a}).
\tag{21}
$$
二处、二十九处均真正分歧；三处指数分别为1或2。
(19) 是固定有限扭曲的全权族，通常不等于某个固定
type-(1,0) 角色的 (2m+1) 次幂。

## 5. 原全 theta、角型及代数规范

取有限 tensor
$$
v_e\otimes\phi_{a,\sigma}\otimes
 \left(\sum_{c\bmod29}f_j(c)\mathbf1_{c/29+\mathbf Z_{29}}\right),
\tag{22}
$$
其它有限处用原球。其真实系数按 R776 是
$$
a_{\ell,n}
 =v_e(n\bmod4)\,v_{a,\sigma}(n\bmod3)\,f_j(21n\bmod29).
\tag{23}
$$
它非零、实，奇偶性为 (−1)^r，并保全原半特征。
其 theta
$$
S_{\ell,\Lambda}(Z)
 =e^{174\sqrt3\pi Z^2}
  \sum_{n\in\mathbf Z}a_{\ell,n}
       e^{\pi i(\delta/3)n^2/348+2\pi inZ}
\tag{24}
$$
属于原标准 O(174[0])。几何 ω 的实际局部标签为 ω²；
二处、三处和二十九处的乘积特征是
ω^{2(e+a+j)}=ω^r，给出 (15) 的三次角型。
全局 −1 则给其第二个条件。

(10)、(14) 及 R776 的满维识别证明，(24) 的174条线构成整个
原标准空间。未只保裸 type5，也未丢掉三处 odd 方向。

在 E0 的原实周期 Ω0Λ 上，按首个非零 Taylor 系数定义
$$
S_{\ell,\Lambda}(Z)=s_\ell F_{\ell,1}(\Omega_0Z),\qquad
[z^{d_\ell}]F_{\ell,1}=1,\qquad
d_\ell\equiv r\pmod6,\quad0\le d_\ell\le174.
\tag{25}
$$
代数 theta 群及 (4)、(8)、R776 的原有限投影说明 Fℓ,1 是代数截面；
第一非零系数归一不引入任意 Cp 系数。其原 Fourier 序列实，
故 sℓ 是实数或纯虚数，取决于 dℓ 的奇偶。
没有预设 dℓ=r，也没有据截面非零推出其负一矩非零。

在原 b=17 曲线上，令 θ=17^{1/6}，准确取
$$
F_{\ell,17}(z)=\theta^{-d_\ell}F_{\ell,1}(\theta z),\qquad
\Omega_{p,0}=\theta\Omega_p.
\tag{26}
$$
于是原物理测度在同一个 x 变量上满足
$$
\nu_{F_{\ell,1}}=\theta^{d_\ell}\nu_{F_{\ell,17}}.
\tag{27}
$$
单位域没有被 θ 缩放。

## 6. 全权实平方和固定代数常数

令
$$
\mathcal G=261\sqrt3,\qquad
h_\infty=\frac{\sqrt{261\sqrt3}}{1044\pi i},\qquad
d_{\ell,m}=[z^m]F_{\ell,1}.
$$
按原 Hermite 规范
exp(xT−T²/(8π))=ΣHm(x)T^m/m!，有
$$
\begin{aligned}
b_{\ell,m}
 &=\sum_n a_{\ell,n}
 H_m(\sqrt{\mathcal G}\,n/522)
 e^{-\pi\sqrt3 n^2/1044}\in\mathbf R,\\
b_{\ell,m}&=m!s_\ell(\Omega_0h_\infty)^m d_{\ell,m}.
\end{aligned}
\tag{28}
$$
只保 m≡r mod6。完整有限平方范数是
$$
n_{2,e}\,n_{3,a}\,n_{29,j},
\qquad n_{3,0}=3,\quad n_{3,1}=6.
$$
连同无穷处，原范数为
$$
\mathcal N_{\ell,m}
 =\frac{n_{2,e}n_{3,a}n_{29,j}}{\sqrt{522\sqrt3}}
      \frac{m!}{(4\pi)^m}.
\tag{29}
$$

Yang 原 S1={2,29}，而 ramified prime3 不在 S1 中；
即使其 conductor 是 δ²，也不将它添成 inert Euler 因子。
所以
$$
c(0)=(1+2^{-1})^{-1}(1+29^{-1})^{-1}=29/45.
$$
类数一及六个单位给同 R290 的完整体积比6。
Yang Theorems2.6、2.15 因此给
$$
\boxed{
L(\Phi_{\ell,m},m+1)
 =C_\ell\frac{(4\pi)^m}{m!}b_{\ell,m}^{\,2},\qquad
C_\ell=\frac{5\pi\sqrt{522\sqrt3}}
 {29\sqrt3\,n_{2,e}n_{3,a}n_{29,j}}>0 .
}
\tag{30}
$$
这保留了两个新增三处向量的范数6，及全部原二十九范数。
由于 (23) 实，(30) 是同一个原 theta 来源的实平方，
不是两条未经识别的共轭来源之积。

令 s0=(1−ω)^-1、varpi0=s0Ω0。由
s0^-2=−3ω 和原 h∞，
$$
\frac{(2\pi/\sqrt3)^mL(\eta_\ell\psi_0^{2m+1},m+1)}
 {m!\varpi_0^{2m+1}}
 =c_\ell\,174^{-m}d_{\ell,m}^{\,2},
\tag{31}
$$
其中
$$
\boxed{
c_\ell
 =\frac{C_\ell s_\ell^2}{\Omega_0s_0}\omega^{r}
 =174^{d_\ell}
 \frac{(2\pi/\sqrt3)^{d_\ell}
       L(\eta_\ell\psi_0^{2d_\ell+1},d_\ell+1)}
      {d_\ell!\varpi_0^{2d_\ell+1}}
 \in\overline{\mathbf Q}^{\times}.
}
\tag{32}
$$
后一个式子的非零来自真实首系数1和 (30)，代数性是原 CM 临界周期代数性。
cℓ 在取目标 p 和有限 χ 以前已经固定；没有一个未定的 Iwasawa unit。

## 7. 全部 physical finite-χ 与精确 primitive Katz 平方

令 p 为原合格 ordinary 素数，p∤2·3·17·29；
所有 p-adic avatars、reciprocity 和周期沿原规范。置
$$
\Gamma_0=\widehat\psi_0/\widehat{\bar\psi}_0,\qquad
M_{\ell,m}=\int_{\mathbf Z_p}x^m\,d\nu_{F_{\ell,1}}
 =\Omega_{p,0}^{m}m!d_{\ell,m}.
$$
设 απ=ψ0(𝔭)、barαπ=ψ0(bar𝔭)，v_p(απ)=1、v_p(barαπ)=0。
对 (19) 的正权，Katz primitive 插值准确为
$$
\mathcal K_{\mathfrak f_\ell}
 (\widehat\eta_\ell\widehat\psi_0^{m+1}
                         \widehat{\bar\psi}_0^{-m})
 =c_\ell\Omega_{p,0}174^{-m}
   \left(1-\eta_\ell(\mathfrak p)
                 \frac{\alpha_\pi^m}{\bar\alpha_\pi^{m+1}}\right)^2
     M_{\ell,m}^{\,2}.
\tag{33}
$$
两个 ordinary Euler 因子严格相同，因为 ηℓ^*=ηℓ^-1。
(21) 的三个坏处均真正分歧，所以此处没有另外删去的坏点 Euler 因子。

给定正整数 m0≡r mod6，取
m_h=m0+(p−1)p^h。它们实趋无穷、p进趋 m0。
有界测度的非单位矩趋零；(33) 显示的 Euler 因子趋1。
因此同一 Katz 函数在 m0 的值等于同一个原 unit 矩的平方。
在每个允许的 tame 权分支，正整数权有内积聚点，
于是原两完整解析函数相等，包含其中所有 finite wild-character 点。
这不是把 wild 根单位写成整数幂的极限。

对任意有限 χ:Zp×→Qbar×，定义原实际负一值
$$
I_{\ell,\chi}
 =\int_{\mathbf Z_p^\times}x^{-1}\chi(x)
                         \,d\nu_{F_{\ell,17}}(x).
\tag{34}
$$
准确角选择为
$$
\boxed{
I_{\ell,\chi}=0
\quad\text{除非}\quad
\chi(\zeta)=\zeta^{r+1}\quad(\zeta\in\mu_6).
}
\tag{35}
$$
特别只有 type5 允许 χ=1；其余角型仍可通过有限 χ 存活。

对存活的 χ，令
$$
\rho_{\ell,\chi}
 =\eta_\ell\,(\chi\circ\Gamma_0),\qquad
\nu_{\ell,\chi}=\psi_0\rho_{\ell,\chi}^{-1}.
\tag{36}
$$
这是完整的全局有限角色定义，保所有 tame/wild 以及好位 uniformizer；
不是只指定 p 惯性。由 (27)、(33) 的同一解析延拓，
$$
\boxed{
\mathcal K_{\mathfrak f_\ell}
  (\widehat{\bar\psi}_0\rho_{\ell,\chi})
 =174\,c_\ell\,\theta^{2d_\ell+1}\Omega_p\,
      \chi(174)^{-1}\,I_{\ell,\chi}^{\,2}.
}
\tag{37}
$$
χ(174) 不能删掉。正导子 p 分支用 Katz 的真实 ramified Gauss 因子，
不插入未分歧 Euler 因子。式(37)包括零值。

## 8. 逐项 root 核定：δ 的两个符号都保留

νℓ,χ 是 type-(1,0)，满足
$$
\nu_{\ell,\chi}\nu_{\ell,\chi}^*=\mathbf N_K,\qquad
\nu_{\ell,\chi}|_{\mathbf A_{\mathbf Q}^{\times}}
 =\epsilon_K\mathbf N_{\mathbf Q}.
\tag{38}
$$
由 (35)，χ(−1)=(−1)^{r+1}。
Γ0 在2处单位为 Teich²，在3处单位平凡、δ值−1，
在29处单位与有理 uniformizer 上平凡。
所以 νℓ,χ 的原 unitary 坏处表准确为
$$
\boxed{
\begin{array}{c|c|c}
2&\operatorname{Teich}^{\,2-e}&-1\text{ 于 }2\\
3&(\epsilon\omega^b)\mapsto\epsilon\omega^{-ab}
       &+i\sigma\text{ 于 }\delta\\
29&\vartheta_j^{-1}&-1\text{ 于 }29 .
\end{array}}
\tag{39}
$$
它是 (20) 在每一个坏处的 unitary 共轭，包含 σ=−1 时 δ 值的反转。

给出完整 epsilon 计算，不能只按角型猜号。
(20) 在2、3、29处的 epsilon 因子分别为
$$
+1,\qquad -i\sigma,\qquad(-1)^j.
\tag{40}
$$
二处是原两逆 cubic Gauss 和同为2；三处由 R776 的实际
splitting/dichotomy 和 χ3(δ)=−iσ 得到 −iσ。
二十九处对非平凡、在 F29× 上平凡的 ϑj，
完整加性 Gauss 和为29ϑj(δ)=29(−1)^{j+1}；
乘 uniformizer 的−1得到 (−1)^j。
所以全部正权有限 epsilon 乘积是
−iσ(−1)^j=−i(−1)^r。

对 (39)，Tate 的反演关系
ε(χ^-1,ψ)=χ(−1)overline(ε(χ,ψ))
逐处适用。三个坏处的 χ(−1)乘积为−1，
因此它们在 (39) 中的总乘积仍为 −i(−1)^r。
无穷处 type1 给 i。
新增 split-p 两处的完整 Gauss 乘积为 χ(−1)；
原 unramified 参数相消，正导子的 Gauss 不被删掉。
若 χ=1，该乘积也是1，与下式一致。故
$$
\boxed{
w(\nu_{\ell,\chi})
 =[-i(-1)^r]\cdot i\cdot(-1)^{r+1}
 =-1 .
}
\tag{41}
$$
这是全部174个 sector 与所有存活 finite χ 的同一完整计算。
没有从 root− 推出任何解析秩恰一或负一非零。

## 9. 实际点特征、周期和十七处

取
$$
H_{\ell,\chi}=K^{\ker\rho_{\ell,\chi}}.
\tag{42}
$$
其明确惯性数据为
$$
\begin{array}{c|c}
\text{地方}&\rho_{\ell,\chi}\text{ 的单位值}\\ \hline
2&\operatorname{Teich}^{\,e-1}\\
3&\gamma_3^a\\
29&\vartheta_j\\
\mathfrak p&\chi^{-1}\\
\bar{\mathfrak p}&\chi\\
v\nmid2\cdot3\cdot29\cdot p&1 .
\end{array}
\tag{43}
$$
三处 uniformizer 的值准确为
$$
\rho_{\ell,\chi}(\delta)=\sigma .
\tag{44}
$$
所以 φe、φo 的有限点角色也不能合并。
特别
$$
\boxed{H_{\ell,\chi}/K\text{ 在17处不分歧}.}
\tag{45}
$$
这来自整个角色 (16)、(36)，而不是“度数不含17”的推测。

(38)、(41) 正是 R774 的完整假设，包括 δ² conductor 情形。
其原 good pair、真正 critical companion、所有有限 local Q、
两个 CM period 的同一嵌入及有限 twist 下降给
$$
P_{\ell,\chi}\in
 E_0(H_{\ell,\chi})_{\mathbf Q}\otimes_K\overline{\mathbf Q},
\qquad
g_{\mathrm{pt}}P_{\ell,\chi}
 =\rho_{\ell,\chi}(g)P_{\ell,\chi},
\tag{46}
$$
以及 εℓ,χ,p∈Qbar×，使
$$
\Omega_{p,0}
 \mathcal K_{\mathfrak f_\ell}
       (\widehat{\bar\psi}_0\rho_{\ell,\chi})
 =\epsilon_{\ell,\chi,p}
       \log_{\omega_0}(P_{\ell,\chi})^2.
\tag{47}
$$
零值可取零点。点本身的非挠和秩一只在 R774 所述的非零情形
由实际 Heegner 点、Gross–Zagier–Kolyvagin 得出；
本篇不另加 analytic-rank 或 Sha 假设。

将 (37)、(47) 和 Ωp,0=θΩp 合并，得到原一次 logarithm：
$$
\boxed{
\Omega_p I_{\ell,\chi}
 =A_{\ell,\chi,p}\log_{\omega_0}(P_{\ell,\chi}),\qquad
A_{\ell,\chi,p}^{\,2}
 =\frac{\epsilon_{\ell,\chi,p}\chi(174)}
        {174c_\ell\,\theta^{2d_\ell+2}}
 \in\overline{\mathbf Q}^{\times}.
}
\tag{48}
$$
符号按实际相等选择；不主张这些符号已给一个预先指定的 universal 线性映射。
有限 point-log 空间的实际线性运算仍可使用 R749 的 logarithm 单射。

(45) 指点坐标域。式(48)及原 theta 归一中的代数标量可以包含
θ、roots of unity 和其它代数数；point-only 惯性投影不作用于它们。

## 10. 原 finite-p translations 和所有实际门都被覆盖

固定 p、N、n 及 R772 的整个有限域 D，包括 CD、失败门、E 门、
原单位条件与所附 finite 环带。
R772 的准确来源是
$$
\nu_{\mathcal D}
 =\Omega_p^{-1}(P_0)_*
       (1_{\mathcal D}\,\mathfrak t q_N^*e_0),\qquad P_0=\delta P.
\tag{49}
$$
q* 与 t 的 P 正交性使所有正多项式只给伙伴 jets，
没有 P 法向的隐含导数。所有实际门先作六变量有限加性 Fourier；
随后用原 Mumford lift/Bannai–Kobayashi 式。它们在 (49) 的
第一变量作用为真正的
$$
\nu_F\longmapsto\zeta_{p^M}^{\,c x}\nu_F .
\tag{50}
$$
伙伴高层 p-torsion 和所有正阶 jets 的系数为代数数；
它们不被当作随意 Cp 标量。

将 R772 的全174代数基改写到 (25) 的完整本征基，得到
$$
\nu_{\mathcal D}
 =\sum_{\ell}\Phi_{\ell,\mathcal D}(x)
                            \nu_{F_{\ell,17}}(x),
\tag{51}
$$
每个 Φ 是某个实际有限模 p^M 的代数值函数。
这一步保所有原 additive phases 和伙伴系数，
不是把任意 abstract p-Weil vector 直接称为 physical χ 测试。

再只在原单位域作有限乘法 Fourier：
$$
\Phi_{\ell,\mathcal D}(x)
 =\sum_{\chi\bmod p^M}
       c_{\ell,\chi,\mathcal D}\chi(x),\qquad
c_{\ell,\chi,\mathcal D}
 =\frac1{\varphi(p^M)}
   \sum_{u\bmod p^M}^{\times}
       \Phi_{\ell,\mathcal D}(u)\chi(u)^{-1}
 \in\overline{\mathbf Q}.
\tag{52}
$$
仅按 (35) 删除确实为零的角分支，其余 tame/wild 全保。

R772 的物理 P 负一行准确为
$$
\mathcal L_P(\mathcal D)
 =\delta\Omega_p
     \int_{\mathbf Z_p^\times}x^{-1}\,d\nu_{\mathcal D}
 =\delta\sum_{\ell,\chi}
       c_{\ell,\chi,\mathcal D}\,
       A_{\ell,\chi,p}\log_{\omega_0}(P_{\ell,\chi}).
\tag{53}
$$
因此
$$
\boxed{
\mathcal L_P(\mathcal D)
 \in
 \overline{\mathbf Q}\log_{\omega_0}
 \bigl(E_0(H_{\mathcal D})_{\mathbf Q}
                           \otimes_K\overline{\mathbf Q}\bigr),
\quad H_{\mathcal D}/K\text{ 有限且在17处不分歧}.
}
\tag{54}
$$
取 (42) 中实际出现的有限多个点域的合成即可。
(53) 既保 (49) 的原外部/失败门，也保物理 δ 和共同周期；
它不是未切边际的替代式。

这个结论同样用于任何已严格付入 R772 同一有限来源池的代数线性组合，
包括逐项保完整系数的两态来源。它不自动扩大到未支付的来源格。

## 11. 与原 Y 行及全中央的边界

R767 的未切 Y 推前仍为
$$
\Omega_p^{-1}Y_*(\mathfrak t q_N^*e_0)
 =-\frac{22}{21}\beta^N D_\omega .
\tag{55}
$$
其原 Y-unit 负一非零，且在17处属于真实 nontrivial cubic 点角色。
本篇 (54) 为实际 P 行给出相反的点域性质，但没有删掉两者之间的
真实分母、门或补域：
$$
\frac{\mathfrak t}{P}-\frac{\mathfrak t}{b_YY}
 =-\frac{\mathfrak t(a\widehat{\mathfrak s}+2\widehat d)}
          {b_YY\,P}
$$
及 Y-unit\D 的完整积分仍须按 R772 保留。

只有一个已经成立的、有限代数来源的 point-log 线性等式，
才能在 R749 的意义下施加 point-only 惯性幂等元。
原 JS′=JT′=0 是原完整 scalar 中央条件；
本篇没有把它重新解释成一个未支付的 point-factor 等式。

当 N、n、m 改变时，(51) 的有限池和代数系数可以改变。
R753 关于 point-only 投影不连续的限制继续成立；
本篇不对任意无限 p-adic 和或 log 展开交换投影。

## 12. 原 ordinary whole S174 scalar 的定号接口

这里单列与实际 ordinary core 的接合，避免从有限 Weil 范数猜号。
[R777](R777-original-b-sector-p-t-core-and-complete-central-renewal.md) 的原 Heisenberg/两 sigma 锚已经给：
在同一 ordinary ray 上，whole S174 的 core 为
$$
\mu=\chi_P\lambda,\qquad \chi_P^2=1,\qquad
\kappa=p\lambda^2,\qquad\beta=-\lambda=\bar\pi_0^{-1}.
\tag{56}
$$
其 g≡1+174 mod348 是完整中心条件，本篇不重作该 whole-core 证明。

原固定射线（R410 的原2/3类及 R488 的29细分）还给
π0≡1 mod2、π0≡1 mod3、π0≡2 mod29。由 (16)、(17)，所有本篇 ηℓ 在所选 𝔭 上准确为1。
因此 (33) 的 Euler 因子就是 1−βκ^m。

同第7节的高正权极限在每个合法正整数 m 给
$$
M_{\ell,m}^{\times\,2}
   =(1-\beta\kappa^m)^2 M_{\ell,m}^{\,2}.
\tag{57}
$$
另一方面，实际全 core (56) 给
$$
M_{\ell,m}^{\times}
   =(1-\chi_P\lambda\kappa^m)M_{\ell,m}.
\tag{58}
$$
至少有一条真实本征线的 m=1 矩非零：
原完整空间含 σ^174 yx^85，其首阶为1，
而 (25) 是该整个空间的本征基。
在这条线上约去非零矩，使用 χP²=1、β=−λ，
(57)—(58) 立刻得到
$$
\boxed{\chi_P=-1,\qquad \mu=\beta.}
\tag{59}
$$
如果 χP=+1，两边平方的差就是
−4λκ，不可能为零。

(59) 使用完整原 Schwartz/primitive Euler 与真实 ordinary core，
没有使用负一非零，也没有使用原三个中央中的任一个零假设。
它可以代回 R777 的实际 P/t 全域返回；那里的所有门仍按原式运输。

## 依赖与计算范围

- [R772](R772-original-p58-orthogonal-weight-and-full-finite-schwartz-source.md)：
  P0 整轴、全174来源、P正交权、全部 finite 门、period及17整格。
- [R776](R776-original-degree174-three-primary-absolute-weil-spectrum.md)：
  三处绝对 splitting、三个原球、范数及 δ² 精确角色。
- [R774](R774-ramified-discriminant-good-pairs-and-exact-point-factors.md)：
  已识别完整 root-negative 角色的一般3导子点公式、local Q及真实点域。
- [R777](R777-original-b-sector-p-t-core-and-complete-central-renewal.md)：
  原 whole S174 scalar、两 sigma 锚和完整 P/t 域；
  本篇主结论 (1)—(54) 不依赖其定号接口。
- [R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)：
  原 additive/Schrödinger 规范、二处积分和完整 Yang norm。
- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)、
  [R746](R746-original-type-five-all-finite-p-character-squares.md)、
  [R751](R751-second-dyadic-character-point-fields-and-inertia-extraction.md)：
  原周期、physical finite-character 解析延拓与角型处理。
- [R745](R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)、
  [R749](R749-point-factor-projectors-and-finite-character-extraction.md)、R753：
  有限源代数性、point-only动作和极限边界。
- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math.485 (1997), 25–53，
  Theorem1.11、Theorems2.6、2.15；
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- T. Yang, *Eigenfunctions of the Weil representation of unitary group of one variable*,
  Trans. Amer. Math. Soc.350 (1998), 2393–2407，
  Theorems0.1、0.4；
  <https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*,
  Compositio Math.117 (1999), 337–359，
  Proposition1.2、Proposition1.5、Appendix(A1)—(A11)；
  <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- Bertolini–Darmon–Prasanna, *p-adic Rankin L-series and rational points on CM elliptic curves*,
  Pacific J. Math.260 (2012)，Theorem3.1、Proposition3.5，原一般 prime-to-p ideal modulus；
  正导子 p 的 Gauss 因子按 de Shalit II, Theorem4.14，亦保于 R774 的完整 local comparison。

本篇为原显示矩阵、完整有限 Gauss 合成、已付代数 theta 来源及原插值的直接证明。
没有新素数扫描、数值近零判定或需保存的重算数据。
