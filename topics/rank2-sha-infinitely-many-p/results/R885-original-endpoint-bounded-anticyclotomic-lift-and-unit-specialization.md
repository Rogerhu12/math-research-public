# R885. 原 q/q⁴ 端点的有界反循环提升与单位特殊化

日期：2026-11-16。**状态：已证明。** 本篇只处理 R831/R832 的原端点循环及其原三个最高 CM 分量。它把这些指定循环的 p-adic étale Abel–Jacobi 类放入一个真实的、有界的反循环 Iwasawa 类中，并付清增广特殊化的非零单位因子。它不证明原循环或其 Abel–Jacobi 像非零，不把 R814 的 canonical 循环换成这个端点循环，也不把普通三槽调节器当作最高 CM 槽的调节器。

以下 p 属于原普通 ray，特别 p>211、p∤6·17。全部有限角色、原系数嵌入、q/q⁴ 两退化映射、X₀/X₁ 次数与原 CM 投影均保持。本文没有数学数值执行。

## 1. 原对象及准确结论

置 K=Q(ω)、ω²+ω+1=0、δ=1+2ω。沿 R806、R826，令 η=η₁₀ 为原十八阶角色，且
$$
\eta_4=\eta^{13},\qquad \eta_{10}=\eta,\qquad
\eta_{16}=\eta^7,\qquad
\psi_{17}=\eta^3\psi_0,\qquad
\beta_j=\eta_j^{-2}\psi_0 .
\tag{1}
$$
这里 ψ₀ 是 E₀:y²=x³+1 的原 CM 角色；ψ₁₇ 是 E₁₇:y²=x³+17 的角色。三个固定形式为
$$
f=\theta_{\psi_{17}},\qquad g_j=\theta_{\beta_j}.
$$
其原最小层分别是 10404 和 2601；共有层固定为 M=10404。

最高角色与实际两槽顺序为
$$
\begin{array}{c|c|c}
\ell&(j,k)&\lambda_\ell\\ \hline
4&(10,16)&\eta_4^{-1}\psi_0^3\\
10&(16,4)&\eta_{10}^{-1}\psi_0^3\\
16&(4,10)&\eta_{16}^{-1}\psi_0^3 .
\end{array}
\tag{2}
$$
逐项有 ψ₁₇βⱼβₖ=λℓ，不能改成任意三个同 Hodge 权的角色。

记 Z₀₂,ℓ 为 R831 的唯一端点循环经 R832 的原 λℓ 投影所得的循环。其 g、h 向量是原
$$
g_j(q),\qquad 4g_k(q^4)
\tag{3}
$$
对应的微分向量；4 是退化映射对微分的真实倍率。本文不改成两个同一退化映射的向量，后者已由 R829 证明给零循环。

用 R832 的固定 Chow 对应，将其 étale 类送到选定 K-CM 符号：
$$
z^{\rm end}_{\ell,p}
=\operatorname{AJ}_{p,\lambda_\ell}(Z_{02,\ell})
\in H^1(K,V_\ell),\qquad
V_\ell=E_{\mathfrak P}(1)\widehat\nu_\ell^{-1},
\quad
\nu_\ell=\eta_\ell\psi_0^{-1}\bar\psi_0^2 .
\tag{4}
$$
这正是 R804/R811 的表示；所改变的是指定全局类的来源，不是目标表示。

令 K∞/K 为反循环 Zp 扩张，Γ=Gal(K∞/K)，Λ=O[[Γ]]。则存在由原对角循环构造得到的类
$$
\boxed{\quad
\mathfrak D_{\ell,p}\in
 H^1_{\rm Iw}(K_\infty,T_\ell)\otimes_{\mathcal O}E_{\mathfrak P},
\qquad
\operatorname{sp}_0\mathfrak D_{\ell,p}
=\mathscr E_p\,z^{\rm end}_{\ell,p}.
\quad}
\tag{5}
$$
Tℓ 为 Vℓ 中的任一固定稳定格；改格只改变一个固定 p 分母。因此(5)中的 Iwasawa 类是**有界系数**的类，不是仅在增广点存在的形式幂级数。

原根规范是
$$
(\alpha_f,\beta_f)=(-\bar\pi,-\pi),\qquad
(\alpha_{g_j},\beta_{g_j})=(\bar\pi,\pi),
\qquad \pi\bar\pi=p,\quad v_{\mathfrak P}(\pi)=1.
\tag{6}
$$
在此规范下，
$$
\boxed{\quad
\mathscr E_p=
\frac{(1+\bar\pi^{-1})^3(1+\pi/\bar\pi^2)}
     {(1-\pi/\bar\pi)^3}
\in\mathcal O_{\mathfrak P}^{\times}.
\quad}
\tag{7}
$$
(5)在三个 ℓ 上使用同一个标量(7)。完整复共轭符号由真实共轭运输，而不是在同一 p-adic 嵌入中任意把 π 和 barπ 交换。

## 2. 原四个 CM 角色与所有必要残余条件

在 K 上，原三形式的八维张量先按 f 的一个 CM 符号取四维。该四维表示的有限十七处角色指数如下；共同的 Tate 扭曲不影响十七处惯性：
$$
\begin{array}{c|c|c|c|c}
(j,k)&(++ )&(-- )&(+ -)&(- +)\\ \hline
(10,16)&5&1&15&9\\
(16,4)&17&7&15&9\\
(4,10)&11&13&9&15 .
\end{array}
\tag{8}
$$
例如第一行由 3−2−14、3+2+14、3−2+14、3+2−14 模18逐项得到。为保留所有范数幂，令 (a₄,a₁₀,a₁₆)=(13,1,7)，则四条**表示角色**准确为
$$
\begin{array}{c|c}
++&\eta^{3-2a_j-2a_k}\psi_0^3\mathbf N^{-1}\\
--&\eta^{3+2a_j+2a_k}\bar\psi_0\\
+-&\eta^{3-2a_j+2a_k}\psi_0\\
-+&\eta^{3+2a_j-2a_k}\psi_0 .
\end{array}
\tag{8a}
$$
这里使用 \(\psi_0\bar\psi_0=\mathbf N\)。因此第一列的动机角色为 λℓ，而进入本篇上同调的表示为 λℓ/N；后三列是 R826/R832 原来的三个 mixed 分量。本文未删掉它们再应用大维构造。

η 在十七处惯性上的像确为 μ₁₈，而 ψ₀ 在17处不分歧。p>211，所以(8)中没有一条角色在模 p 后变为平凡的惯性角色。对任意 ACR 使用的 K[npˢ]/K，扩张是 p 扩张；它不能杀掉这些阶数与 p 互素的惯性。于是对四维原格 T 及所有该层，
$$
H^0(K[np^s],V/T)=0.
\tag{9}
$$
由 0→T→V→V/T→0 的上同调正合列，H¹(K[npˢ],T) 无 O-torsion。这支付 ACR Theorem 6.5 明列的无挠假设，未借其后续非 CM“大像”应用。

f 及 gⱼ的二元诱导表示也残余绝对不可约：在17惯性上，诱导的两个字符分别是原字符和它的逆，二者之比在 f 上有三阶像，在 gⱼ上有九阶像，模 p 后仍不相同。在 p 位，两个普通字符在惯性上分别含一次 cyclotomic 字符与零次，p>3 时残余相异。因此 DR 的 residual irreducibility 和所需 ordinary/distinguished 条件都成立。

## 3. 真正的 Hida 分支与有界 Shapiro 同构

本文使用两个已发表构造的不同部分：

- DR §2、Definition 5.2 构造原模块曲线塔上的全对角类；其 Theorem 4.1 给最低权 (2,2,2) 的精确特殊化。
- ACR §6 的实际 CM 模同构(6.4)，把同一普通 CM 分支改写为反循环 Iwasawa 系数。该同构是 Λ 模同构，不是只有分式域中的表示同构。

这一区分避免先把两篇采用不同归一的同名 κ 直接相认。

ACR 在其几何互反约定中将原 ψ=ψ₁₇ 记为 infinity type (−1,0)。令 ψp,0 为其 §6 开头的 p-primary 角色，取
$$
\alpha=\psi_{17}/\psi_{p,0}.
\tag{10}
$$
α 是有限角色，其导子允许含 𝔭，确切地整除原导子乘 𝔭。ACR(6.2)明确保留这个有限 p-tame 分量，得到原 f 的普通 Hida 分支。在权2特殊化，
$$
\alpha\psi_{p,0}=\psi_{17}
$$
精确成立。因此没有把原 nebentype 为1的 f 换到另一条带 ωp⁻¹ 的 tame 分支。

对该第一因子，ACR(6.4)在 k=2 时成为
$$
H^1(\psi,1)\simeq
\operatorname{Ind}_{G_K}^{G_{\mathbf Q}}
 \Lambda\bigl(\psi_{\mathfrak P}^{-1}
                   \boldsymbol\kappa_{\rm ac}^{-1}\bigr).
\tag{11}
$$
它来自其 §3 的原 CM Hecke 商及 §5 的有界分布对偶；§6 在取 inverse limit 后仍在 O[[Γ]] 上工作。取 Γ 的生成元规范
$$
((1+p)^{-1/2},(1+p)^{1/2})\longmapsto[1+p],
\tag{12}
$$
平方根是 pro-p 群中的唯一平方根。

DR 的真实自对偶扭曲为
$$
\mathbb V_f\otimes\mathbb V_g\otimes\mathbb V_h
 \bigl(\varepsilon_{\rm cyc}^{-1}
       \boldsymbol\varepsilon_f^{-1/2}
       \boldsymbol\varepsilon_g^{-1/2}
       \boldsymbol\varepsilon_h^{-1/2}\bigr).
\tag{13}
$$
将 g、h 固定在原权2点，并把 f 取为(10)的 CM 分支，(11)精确给
$$
H^1\!\left(\mathbf Q,\mathbb V_{fgh}^{\dagger}\right)
\simeq
H^1\!\left(K,\Lambda(\boldsymbol\kappa_{\rm ac}^{-1})
                    \widehat\otimes T^\psi_{g,h}\right)\otimes E
\simeq H^1_{\rm Iw}(K_\infty,T^\psi_{g,h})\otimes E .
\tag{14}
$$
k−2=0，所以 ACR 一般式中 κac^((k−2)/2) 的额外算术扭曲在这里确为1。

其目标在原算术互反下为
$$
T^\psi_{g,h}\otimes E
=(V_g\otimes V_h)\,\widehat\psi_{17}\,
 \varepsilon_{\rm cyc}^{-1}.
\tag{15}
$$
第一最高符号的字符因而为
$$
\widehat\psi_{17}\widehat\beta_j\widehat\beta_k
 \varepsilon_{\rm cyc}^{-1}
=\widehat\lambda_\ell\varepsilon_{\rm cyc}^{-1}
=\varepsilon_{\rm cyc}\widehat\nu_\ell^{-1},
\tag{16}
$$
正是(4)，不是 λℓ 的逆、另一个 Artin 标签或未经 Tate 归一的 weight4 表示。

(11)的格同构和固定两因子的有限层映射，可在开始时统一清一个常数分母；此分母与反循环层数无关。由此(14)给的是(5)所用的有界 Iwasawa 类。这里只需固定稳定格的有理系数版本，不声称原循环在任意所选格中本原。

## 4. 原 q/q⁴ 来源、辅助对应与有限层归一

在共同 tame 层 M 上保留原第一因子和两个实际退化向量(3)。所有 tame 退化映射、Hecke 对应、固定有限 Artin 幂等元及 X₁→X₀ 推前，都与 p-level 塔的投影和 corestriction 交换。因此可以在 DR 全对角类及(14)之前施这些原对应。

更明确地，令 C₀₂,ℓ 表示 R831/R832 中从共同层 h¹⊗h¹⊗h¹ 到原 λℓ 动机的**那一个固定对应**。它包括：

1. 原 f 新因子；
2. 第二槽 q₀ 与第三槽 q₂:z↦4z；
3. R831 的 oldcopy 归一，特别其原 X₀/X₁ 次数；
4. R832 的最高 CM 投影及原系数嵌入。

在模块曲线的 p 塔上逐层使用同一个 C₀₂,ℓ。本文不重新选择一个只与它同 Galois 表示的对应，也不删去(3)中的4。R880 的真实 Artin 三映射换基若用来实现该对应，仍只是在这同一个 C₀₂,ℓ 内展开。

DR 为使循环同调平凡而使用
$$
\vartheta_q=(T_q-(q+1))^{\otimes3}.
$$
本题可以一次固定 q=5。三个形式都 CM 于 K，而5在 K 中惰性，故
$$
a_5(f)=a_5(g_j)=a_5(g_k)=0,\qquad
C_5=(a_5(f)-6)(a_5(g_j)-6)(a_5(g_k)-6)=-216.
\tag{17}
$$
三个分支取各自原 CM Hida 分支；惰性处的 T₅ 系数在整个分支恒为零，所以 C₅ 在塔系数环中也是同一个常数 −216。T₅与原 q/q⁴ 退化对应交换，所以(17)在原 old 向量上仍精确成立。p>211 时 C₅ 是单位。于是 DR 的 θ₅/C₅ 在原三 h¹ 投影上恰为恒等；与原 cuspidal modified diagonal 的投影相同。这里的 −216 不是 R804 椭圆单位的30平滑因子，后者不进入本篇循环定义。

在(11)的有限层 CM 识别上，固定增广点与原 C₀₂,ℓ 的同一 Tate 模识别。ACR 的 CM 识别可由一个常数 E× 标量作此校准；其在所有塔层的使用一致，故不制造任何 T 因子或随层增长的分母。等价地，可先保留原对应的全部常数，在(14)后再作同一个常数基变换。本文不因此断言该常数在任意格上是 p 单位；“单位特殊化”专指下节中明示的 p-stabilization 因子。

这样归一后，将 DR Definition 5.2 的原全类固定 g、h 的权2，再施 C₀₂,ℓ及(14)，定义本文的 𝔇ℓ,p。不同 CM 塔基若在增广点仍与该原识别相同，只会给增广值1的可逆基变换；不会改(5)或本文的增广阶结论。

## 5. 最低权特殊化与全部正负根

DR Theorem 3.1及 Corollary 3.3直接把权(2,2,2)的 specialized class 识别为原有限层 étale AJ；并非从只对高权成立的公式取极限。其 Theorem 4.1给
$$
(\varpi_1,\varpi_1,\varpi_1)_*\kappa_1
=
\frac{\mathcal E^{\rm bal}}
     {\mathcal E(f_\alpha)\mathcal E(g_\alpha)\mathcal E(h_\alpha)}
\,\kappa(f,g,h),
\tag{18}
$$
其中本题 c=(2+2+2−2)/2=2，
$$
\begin{split}
\mathcal E^{\rm bal}
={}&(1-\alpha_f\beta_g\beta_h p^{-2})
(1-\beta_f\alpha_g\beta_h p^{-2})\\
&\cdot(1-\beta_f\beta_g\alpha_h p^{-2})
(1-\beta_f\beta_g\beta_h p^{-2}),\\
\mathcal E(f_\alpha)&=1-\beta_f^2/p
\end{split}
\tag{19}
$$
且 g、h 类似。原 nebentype 为1，因此这里无需省略任何非平凡 χ(p)。

代入(6)，前三个括号各为 1+barπ⁻¹，第四个为 1+π/barπ²，三个分母各为 1−π/barπ。得到(7)。所有 C₀₂,ℓ与(18)的 p-forget 映射交换，所以(18)在原循环及其全部有限角色上仍成立。这证明(5)，没有附加一个未显示的 p³、p−1 或原 oldcopy 因子。

现在证明单位性。1−π/barπ 和1+π/barπ²均为单位。若1+barπ⁻¹不是单位，则
$$
p\mid a_p(E_0)+1,\qquad a_p(E_0)=\pi+\bar\pi\in\mathbf Z.
$$
Hasse 界在 p≥7 时给 |aₚ(E₀)+1|<p，故 aₚ(E₀)=−1。但 E₀ 上 (−1,0) 为二挠点、(0,1) 为三挠点，良好约化且 p>3 保持这六个挠点，故
$$
p+1-a_p(E_0)\equiv0\pmod6.
$$
p在 K 中分裂给 p≡1 mod6，于是 aₚ(E₀)≡2 mod6，矛盾。故所有(7)中的因子均为 p 单位。

这项证明使用 E₀ 的原 trace；不能换成 E₁₇ 的 trace 后忽略(6)的负号。

## 6. 原 λ 的 balanced 位置与没有额外增广零的读数

ACR Proposition 6.6、DR Proposition 5.8给上述几何类的 balanced 局部条件。对此本题无需借其非 CM“大像”应用。

在选定的 𝔭 位，原最高 λℓ 分量是
$$
V_f^+\otimes V_{g_j}^+\otimes V_{g_k}^+(-1),
\tag{20}
$$
其 Tate 指数为2；在 bar𝔭 上为−1。它因此在 𝔭 的 balanced 部分中保留，在 bar𝔭 的 balanced 部分中为零。原三个普通三重积 regulator 所读的是
$$
V_f^-\otimes V_g^+\otimes V_h^+,\quad
V_f^+\otimes V_g^-\otimes V_h^+,\quad
V_f^+\otimes V_g^+\otimes V_h^-,
\tag{21}
$$
它们不等于(20)。本文未把(21)中任一已知因子分解搬到(20)。

把(5)送入 R811 的同一系数扩张及增广完成环
$$
\mathscr R=\mathscr F[[T]],\qquad T=\gamma-1.
$$
R811 §4已由 Castella Theorem4.2.1的**有限余核**证明：原 Vℓ 在 𝔭 的规定 Coleman 映射在反演 p、再作此完成后是同构
$$
\operatorname{Col}_{\ell,\mathfrak p}:
\mathcal H_{\ell,\mathfrak p}\xrightarrow{\sim}\mathscr R .
\tag{22}
$$
用这同一个映射定义
$$
\mathscr D_{\ell,p}(T)
=\operatorname{Col}_{\ell,\mathfrak p}
  (\operatorname{loc}_{\mathfrak p}\mathfrak D_{\ell,p}).
\tag{23}
$$
它不是 DR(21)的普通三槽函数，亦没有被定义成原 Katz 函数。

局部导出特殊化给单射
$$
\mathcal H_{\ell,\mathfrak p}/T\mathcal H_{\ell,\mathfrak p}
\hookrightarrow H^1(K_{\mathfrak p},V_\ell).
\tag{24}
$$
目标维数为1：Vℓ及其 Tate-dual 在此都没有不变向量，局部 Euler 特征公式给出该维数。结合(22)，(24)为实际局部群的一维同构。记它所确定的线性坐标为 lℓ,p，则
$$
\boxed{\quad
\mathscr D_{\ell,p}(0)
=\mathscr E_p\,l_{\ell,p}
   (\operatorname{loc}_{\mathfrak p}z^{\rm end}_{\ell,p}).
\quad}
\tag{25}
$$
若改用 R804 的原 de Rham/Artin 周期基，(25)的两边按同一非零常数基变换。这类常数不会改变 T-adic 阶。本文没有删除原 √17、CM 周期或把它们称为全局有限角色的平凡化。

因此没有来自 p-stabilization 或这个已规定 Coleman 映射的额外一阶增广因子：
$$
\operatorname{loc}_{\mathfrak p}z^{\rm end}_{\ell,p}=0
\quad\Longleftrightarrow\quad
\mathscr D_{\ell,p}(T)\in T\mathscr R .
\tag{26}
$$
真正待判的是指定函数 𝒟ℓ,p 自身的阶，不是一个已知 Euler 零。

## 7. 与原 canonical 类的已付同模关系，以及不能约去的阶

R811 已给同表示的原 canonical 椭圆单位类 cℓ和同一 relaxed、torsion-free、秩一 Iwasawa 模。真实 τ/Γ 反演按 R811 §2–6运输后，𝔇ℓ,p和 cℓ都落在该同模中：在 p 外保原未分歧条件，在两个 p 位只放宽；本题来源的坏位仍为2、3、17。对最终一维 Vℓ，2、17惯性非平凡故局部 H¹ 为零；其它非 p 位上惯性像有限，若取不变部分，则其 Frobenius 权排除特征值1和该位的范数，局部 Euler 序列同样给 H¹=0。因此本篇几何类不会在这些位额外贡献一个未放宽的局部条件。

用同一个(22)记
$$
\mathscr C_{\ell,p}
=\operatorname{Col}_{\ell,\mathfrak p}
       (\operatorname{loc}_{\mathfrak p}\mathbf c_\ell).
$$
R811 所付的 Iwasawa 局部化单射于是给出真实全局恒等式
$$
\boxed{\quad
\mathscr C_{\ell,p}\,\mathfrak D_{\ell,p}
=\mathscr D_{\ell,p}\,\mathbf c_\ell .
\quad}
\tag{27}
$$
所有角色、τ、Γ反演和周期基在两边一致时才写(27)。这里不另设一个未知 Cp 系数把两个有限层循环相认。

(27)是完整提升后的关系，而非有限层的非零比例。即使 𝒞ℓ,p 非零作为 Iwasawa 函数，它在 T=0 仍可能有正阶；不能在特殊化前将这个 T 因子当单位约掉。尤其(5)、(26)、(27)没有证明：

- z^endℓ,p 的有限层局部化单射；
- 原 Z₀₂,ℓ与 R814 canonical Heegner 循环成非零比例；
- R817在7993的 canonical 检测也检测了 Z₀₂,ℓ；
- 三条 Iℓ,−2,p 或原三个中央 Mellin 导数中任一非零。

准确的新输入是：原 Z₀₂,ℓ的指定 AJ 类现在确由同一原来源的有界反循环类特殊化而来；它的局部零等价于(23)这一个实际 Iwasawa 函数在增广点有零。后续必须计算这个来源的增广阶或证明额外的实际全局关系。本篇只构造 n=1 的真实 wild 提升；尚未把它与另一篇论文的整套 tame Euler system 类相认，任何后续 norm-system 应用仍须付清同来源比较及 n=1 归一。

## 8. 来源与核验位置

1. R826、R831、R832：三个原形式、完整 finite η、原 q/q⁴ 向量与 fixed Chow 投影。R829 排的是同一退化向量；本文保不同端点。
2. R804、R811：目标 Vℓ、原 Artin/CM 周期、有限余核 Coleman 同构、同一 relaxed Iwasawa 模及 τ/Γ 反演。
3. Alonso–Castella–Rivero, *The diagonal cycle Euler system for GL₂×GL₂*, J. Inst. Math. Jussieu, doi:10.1017/S1474748023000221。
   [正式刊本](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)；
   [作者全文](https://web.math.ucsb.edu/~castella/ACR1.pdf)。
   刊本 §6、(6.1)–(6.5)、Theorem6.5和Proposition6.6；特别 α 的真实含𝔭导子、原 test vectors、Λ模的(6.4)与有界 Definition6.4。
   其 §9 的 non-CM、大像及后续非零结论未被本篇使用。
4. Darmon–Rotger, *p-adic families of diagonal cycles*, Astérisque434 (2022),29–75, doi:10.24033/ast.1175。
   [独立作者全文](https://arxiv.org/pdf/2207.01314)；
   [SMF正式全卷](https://smf.emath.fr/system/files/filepdf/smf_ast_434.pdf)。
   §2的实际全塔类；Theorem3.1、Corollary3.3；§4、Theorem4.1；Definition5.2、(5.3)和Proposition5.8。
   Theorem4.1在独立稿printed34/正式全卷printed65；它真覆盖(2,2,2)，不借另一个仅高权命题。
