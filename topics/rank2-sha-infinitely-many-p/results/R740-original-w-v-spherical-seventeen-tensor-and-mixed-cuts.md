# R740 — 原 W/V 联合在十七处的完整球张量与混合切集下的三次投影

日期：2026-11-15。**状态：已证明。**

本篇保持 R734 的同一个实际 $q_N^*$ 和 R737 的全部 primitive 条带。
在原六输入上给出一个十七处整的完整正交框架，
证明原三个 W-quarter 来源在十七处保有同一个 W 球因子及 V 球因子。
这个结论在附加原 p 处的全部门、负矩、有限词及其精确拉回后仍成立。
因此两条返回支的**W/V 方向本地 Hecke 三次投影**确实为零；
这里所用的是完整张量，未从一条 T 边际推断整个来源。

该本地结论没有把任一条件积分识别成代数点 logarithm。
R737 的四-unit 部分继续保原 Y 观察；Y 的十七处正交分解恰有非平凡 gluing。
尤其不能将本篇的 W/V 环面投影换成 R735 的 Y 投影，
也不能删掉两返回支的条件质量和原配对外部。

## 1. 规范、同一个原来源与六条完整轴

仍用
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad
\gamma_7=3+\omega,\quad\bar\gamma_7=2-\omega .
\tag{1}
$$
原六输入按 $(\xi_1,\xi_2,\xi_3,x,c,d)$ 排列。定义
$$
A=\delta\xi_1+2\delta\xi_2+\gamma_7\xi_3+\bar\gamma_7x,
\quad Y=A+c+2d,\quad W=A+3\delta c+4d,
$$
$$
\alpha=17-3\omega,\quad
V=36Y-\alpha W,\qquad
E=(5+6\omega)A-29c-(58+87\omega)d .
\tag{2}
$$
这是 R686、R692、R737 的同一个 E，不是另外一个纯 Y 伙伴。

取三个原 A 伙伴
$$
\begin{aligned}
R_2&=2\xi_1-\xi_2,\\
R_3&=\bar\gamma_7\delta\xi_1+
                  2\bar\gamma_7\delta\xi_2-15\xi_3,\\
R_4&=\gamma_7\delta\xi_1+
                  2\gamma_7\delta\xi_2+\gamma_7^2\xi_3-22x .
\end{aligned}
\tag{3}
$$
此处 $\gamma_7^2=8+5\omega$；第三系数不能误写成7。
对行向量采用 $\langle a,b\rangle=\sum a_j\bar b_j$。
逐项有
$$
\operatorname{Gram}(A,R_2,R_3,R_4)
       =\operatorname{diag}(29,5,330,638),
\tag{4}
$$
以及
$$
\boxed{\operatorname{Gram}(W,V,E,R_2,R_3,R_4)
 =\operatorname{diag}(72,18936,7627,5,330,638).}
\tag{5}
$$

(4) 可不依赖数值矩阵核验而直接计算。
前两个 A 系数的范数和为15，前三个为22，四个总和为29；
故 $R_3$、$R_4$ 的范数分别为 $15\cdot22$、$22\cdot29$。
共轭系数的选择给所有交叉项为零。
R686 的 $(A,c,d)\mapsto(W,V,E)$ 行列式为 $-18936$，
其 Gram 为前三个显示值；(3) 同时正交于 A、c、d，故得到 (5)。

令 $\mathfrak o=\mathcal O_{K,17}$。17 在 K 中惰性，
$\mathfrak o/\!17\mathfrak o=\mathbf F_{289}$。
(5) 的六个对角元全为 $\mathfrak o^\times$。
因此完整六乘六换基矩阵及其逆都在 $\mathrm{GL}_6(\mathfrak o)$：
其行列式范数是 (5) 六个对角元之积，所以十七处赋值为零。
这同时支付整个格，而不是只核 W 的一个单位系数。
由此
$$
\boxed{
\mathfrak o^6
 =\mathfrak o W^\vee\ \perp\
  \mathfrak o V^\vee\ \perp\
  \mathfrak o E^\vee\ \perp\
  \mathfrak o R_2^\vee\ \perp\
  \mathfrak o R_3^\vee\ \perp\
  \mathfrak o R_4^\vee ,
}
\tag{6}
$$
其中 $L^\vee=\bar L^{\,t}/\langle L,L\rangle$，
并在各轴使用与原 Hermitian 形式相容的对偶坐标。
所有秩一格均自对偶；原 symplectic 形式中的 $2,\delta$ 在17处也是单位。

## 2. 原六 sigma 的十七处向量及绝对 splitting

先在 $b=1$ 的同一复格模型中看原 sigma。
它的标准 Fourier 表示是奇 theta 的指数归一；
有限半特征及符号只在2处出现。
十七处的实际 Schrödinger 向量准确为
$$
\phi_{17}^{\sigma}=\mathbf1_{\mathbf Z_{17}},
\qquad
\phi_{17}^{(6)}=\mathbf1_{\mathbf Z_{17}^6}.
\tag{7}
$$
例如半整数支撑 $\mathbf Z+1/2$ 在17处就是 $\mathbf Z_{17}$，
其二次中心符号在那里平凡。
无穷处 Gaussian 归一和 sigma 的前导常数不改变 (7)。

这并未把原 $b=17$ 改成另一个 p 进测度。
令 $\theta=17^{1/6}$、$\Omega_{p,0}=\theta\Omega_p$，
原整函数恒等式为
$$
\sigma_{17}(z)=\theta^{-1}\sigma_1(\theta z).
\tag{8}
$$
将原 Amice 变量 $\Omega_p\log(1+T)$ 代入后，
六输入只产生一个共同代数常数 $\theta^{-6}=17^{-1}$，
并保持每个原物理变量。
原混次测试的 $b,\Omega_p$ 归一同样逐项按 (8) 转换；
它们是全局代数或已显示 period 标量，不将十七处 (7) 扭成另一个有限角色。
这与 R735 §1、§7 使用的共同周期规范一致。

在 (6) 的正交极化中，(7) 严格变成
$$
\boxed{
\phi_{17}^{(6)}
=\phi_{17,W}^{\rm sph}\otimes\phi_{17,V}^{\rm sph}
 \otimes\phi_{17,E}^{\rm sph}
 \otimes\phi_{17,R_2}^{\rm sph}
 \otimes\phi_{17,R_3}^{\rm sph}
 \otimes\phi_{17,R_4}^{\rm sph},
\qquad \phi_{17,L}^{\rm sph}=\mathbf1_{\mathbf Z_{17}} .
}
\tag{9}
$$
这里的等式使用自对偶 Haar 测度和原未分歧 splitting，
不是仅模一个未知 Weil 相位的等式。

具体地，(6) 的整等距变换保持自对偶 symplectic 格。
标准未分歧 metaplectic lift 在格的球向量上为恒等：
整对称上三角元的作用相位在该格上为一，
整单位的线性换基保持其指示函数，
自对偶 Fourier 变换也把 $\mathbf1_{\mathbf Z_{17}^6}$ 送到自身。
这些生成元给整个格稳定子的同一个 splitting。
所以转模不附加一个待猜的三次或二次相位。

对每个秩一因子，全部未分歧假设都可逐项检查：
$K_{17}/\mathbf Q_{17}$ 未分歧、原加性角色的 conductor 为
$\mathbf Z_{17}$、原 splitting 角色在单位上平凡，
且原 Hermitian 系数及 $2\delta^2$ 为单位。
Yang《Theta liftings and Hecke L-functions》Lemma 2.7
因此给该球向量对整个 $K_{17}^1$ 的准确特征1。
这里引用的是**惰性未分歧**引理，不将该文仅处理 split 情形的
Corollary 2.14 当作十七处证明。

## 3. 原 C 平均与全部 W-quarter 来源

原 C 的实际整行可从 R686 的已发表生成脚本直接读取：
$$
C_0=(1,0,-1,1,0,0),\qquad N(C_0)=3,\quad
\langle C_0,A\rangle=0 .
\tag{10}
$$
原使用的 $C=C_0/\delta$ 只差一个十七处单位。
其实际 $\mu_3$ 旋转在原六输入上为
$$
I+\frac{\omega-1}{3}\bar C_0^{\,t}C_0 .
\tag{11}
$$
(11) 及其逆属于十七处的整 unitary 群。
由上节的绝对 splitting，原 C 角平均逐项保留 (7)。
这里是对原实际平均的每一项作判断，
没有从加权 C-unit 的某条边际反推整个向量。

同样，R692 的来源
$$
e_0=\mu_0,\qquad
e_1=\sum_{t\in E[4]}a_t\,\mathsf T^{72}_{W,t}\mu_0,\qquad
e_2=-\frac14\sum_{t\in E[4]}\mathsf T^{72}_{W,t}\mu_0
\tag{12}
$$
保全部16个 canonical lift 及原系数 $a_t$。
在17处，四挠 Heisenberg 参数、72的对偶投影及其中心均整。
整平移保持格的指示函数，整 modulation 的加性相位为一；
$1/2,1/4,1/72$ 全是十七处单位。
因此各 t 在17处都作用为恒等，而非仅其总和偶然相消。

于是三个**完整**来源在 (9) 的 W/V 因子上完全相同。
它们的区别仍留在其它有限处、无穷处及原系数中。
下文绝不以十七处相同将三个全局来源互相认同。

## 4. 所有原 p 门与 p-primary 平移的范围

固定原 ordinary 素数 $p>163$，尤其 $p\ne17$。
先对任意有限层局部常值测试 $f$ 作原六输入的 additive Fourier 展开。
它准确是原 $p^m$ 挠点 Heisenberg 平移的有限线性组合。
这些是 p-primary 平移；在17处这些分母为 $p^m$ 的参数全整，
逐项固定原球；其它坏处的原 canonical lift 仍完整保留。
所以它逐项保留 (9)。

这里允许 $f$ 依赖完整六个原物理变量。
特别包括：

- 原 C-unit、D/E/G 全 carry、$q_N^*$ 的全部两 C 分支；
- 原 $Y,Z,W,V,E$ 单位或深度指示；
- $b_i z_V+e_iE$、$b_i z_W+e_iE$ 两类真实移动门；
- 原 $\kappa$ 词的完整逆像与任何原输入交域。

原多项式、单位域上的负幂和 logarithm 都是该紧集上的连续有界测试，
可按其真实定义取局部常值近似。
由此得到的 p 进完成空间仍保 (9) 的固定十七处因子。
所需的有限三次投影只有18项，分母18在 p 处为单位，
所以它连续并与这些极限交换。
这一步是在局部 Weil/Schwartz 模块上作完成；
没有假定十七处 Galois 自同构连续作用于 $\mathbf C_p$。

特别，R737 的
$$
\rho_{i,N}=\Phi_N e_i,\qquad
\Phi_N=\sum_{a=0}^{30}E^a\phi_{a,N}
\tag{13}
$$
及该篇所有受限来源均在这个完成空间中。
每个 $\lambda,\kappa,u$、旧整逆及混次 period 规范原样保留。
无需将它们换成与 p 无关的测试，也没有增加一个射线。

这句话只论**有限17因子及算子的交换**。
在全标量积分中，其它伙伴的积分系数仍可能是一般 p 进数；
(9) 不会把这些系数自动变成代数数。

## 5. 实际 W/V 三次投影

令 $\mathcal T_{17}=\mathfrak o^1$。
对 $L=W$ 或 V，写
$$
G_L(g)=I+(g-1)\frac{\bar L^{\,t}L}{N(L)},
\qquad g\in\mathcal T_{17}.
\tag{14}
$$
其作用把 L 乘 g，并逐个固定 L 的全部正交伙伴。
因为 $N(W)=72$、$N(V)=18936$ 都是十七处单位，
(14) 及其逆均整，属于上面已经定标的格稳定子。
故对 (9)、(12) 和 §4 的全部实际来源有
$$
\boxed{\omega_{17}(G_W(g))\Phi_{17}=\Phi_{17},\qquad
       \omega_{17}(G_V(g))\Phi_{17}=\Phi_{17}.}
\tag{15}
$$

取 $\mathbf F_{289}^{\,1}$ 的原生成元
$\bar g_0=2+4\delta$，阶18，
令 $g_0$ 为其 norm-one Teichmüller 提升。
两条非平凡三次角色取为
$$
\eta_\pm(g_0)=\omega^{\pm1}.
$$
定义完整有限投影
$$
\boxed{
\Pi^{L}_{17,\pm}
 =\frac1{18}\sum_{j=0}^{17}
    \eta_\pm(g_0)^{-j}\,\omega_{17}(G_L(g_0^j)),
 \qquad L=W,V .
}
\tag{16}
$$
(15) 立刻给出
$$
\boxed{\Pi^W_{17,+}\Phi=\Pi^W_{17,-}\Phi
       =\Pi^V_{17,+}\Phi=\Pi^V_{17,-}\Phi=0}
\tag{17}
$$
对 §4 的全部完成来源成立。
这是同一 full tensor 的算子恒等式；并非有限好素数的谱猜测。

R735(6)、(9) 的十七处 Hecke 单位角色为
$(u\bmod17)^{\pm96}$。
经 Hilbert 90 到 norm-one 环面，恰是 (16) 的两条非平凡三次角色。
R735(13) 的具体有限矩阵特征还含已付的 quadratic splitting
$g_0^9=-1$；它不能作为一个额外符号塞入本篇的球模型。
此处使用的是 Hecke 角色及其实际未分歧 splitting。
所以 (17) 的确排除了那两条 **W/V-Hecke** 三次分量。

## 6. V 深条带的精确剪切，保全部条件质量

沿用 R737 的 $b_i,e_i$，$i=1,3$，并置
$$
z_V=\frac{263W-\bar\alpha\kappa V}{612},\qquad
y_V=\frac{\kappa V+\alpha W}{36},\qquad
d_i=\frac{b_i\bar\alpha}{612e_i}.
\tag{18}
$$
在原合格 p 上 $d_i$ 整且为单位。
对第 i 支仅在 p 处实施真正的可逆剪切
$$
S_i:\quad(W,V,E,\mathbf R)\longmapsto
          (W,V,E-\kappa d_iV,\mathbf R).
\tag{19}
$$
这里 $\mathbf R=(R_2,R_3,R_4)$。
令 $E'=E-\kappa d_iV$、$e_1^{(i)}=(S_i)_*e_1$。
于是严格地
$$
b_i z_V+e_iE=\frac{263b_i}{612}W+e_iE',
\quad E\ {\rm unit}\ \Longleftrightarrow\ E'\ {\rm unit}.
\tag{20}
$$
两个 i 使用不同剪切和不同返回来源；不将它们合为同一个 e1。

第 a 次的原单门 V 深返回积分准确成为
$$
\begin{aligned}
H_{i,a}^V(\ell)=
 \int_{\substack{W,E'\ {\rm unit}\\
        263b_iW/612+e_iE'\in p^\ell}}
 \frac{263W-\bar\alpha\kappa V}{17(\kappa V+\alpha W)}
 (E'+\kappa d_iV)^a\phi_{a,N}\,de_1^{(i)} .
\end{aligned}
\tag{21}
$$
其它三个伙伴逐个固定，C 两项及所有高矩都在 $\phi_{a,N}$ 中。
(21) 的剪切是一个 p 处操作；
没有擅自在17处实施分母612的同名有理剪切。
即使只讨论全局形式，它也只动 W 的伙伴；
但本篇 (17) 对 (21) 的直接依据是 §4 的 p-local 交换。

记 (21) 相同域和权、去掉有理观察后的完整质量为 $M_{i,a}$，
并记
$$
K_{i,a,h}
=\int_{\text{(21)同域}}
  V^{h+1}W^{-h-1}(E'+\kappa d_iV)^a\phi_{a,N}\,de_1^{(i)} .
$$
则同一个原积分的完整收敛展开是
$$
\boxed{
H_{i,a}^V(\ell)=
 \frac{263}{17\alpha}M_{i,a}
 -36\sum_{h\ge0}
     \frac{(-1)^h\kappa^{h+1}}{\alpha^{h+2}}K_{i,a,h}.
}
\tag{22}
$$
(22) 保质量、全部 $h$ 以及 $(E'+\kappa d_iV)^a$；
其首项确是原 W-unit 上的 V/W 负一行。
它没有给任一个 $K_{i,a,h}$ 赋算术零。

只有在先完整积分全部伙伴、且未附 W/E 混门时，
第一个 V 矩才落在原 $\mathcal S_{72}$ 的型五11维空间。
保 E 伙伴并附 (20) 的门时，W 的六个角块会经该门耦合。
因此不能只留11个裸坐标来取代 (21)。
有限层 Fourier 展开会出现真正 $p^\ell$ 挠平移；
它们的十七处因子仍由 (17) 控制，但其全部 p 处数据必须保留。

W 深返回支以 W、V 对换作同样的 p-local 处理；
其原单位负幂轴为 V，而不是 W。
(17) 对它同样成立，R737(27) 的常数质量仍不得删除。

## 7. Y 的非整 gluing 与仍在原总行中的部分

本篇没有支付 Y 的球性。事实上它准确失败：
$$
N(Y)=34,\qquad
G_Y(g)=I+(g-1)\frac{\bar Y^{\,t}Y}{34}.
\tag{23}
$$
取 $g\in\mathcal T_{17}$ 且 $g-1$ 为单位。
Y 的 c 系数是1，所以 (23) 的 $(c,c)$ 项含
$(g-1)/34$，在17处非整。
同一现象在原整行框架上是
$$
\det\frac{(Y,17Z,E)}{(A,c,d)}=8942=17\cdot526.
\tag{24}
$$
因此 Y 的秩一格及其正交伙伴之间有真实的十七处 gluing；
不能将 (9) 挪到这个非整分解后仍认作球张量。
R735 的两条原三次来源正是在这个 Y 型五模型中识别的。

所以 R737 的四-unit 原项
$$
G_a(\ell)=\int_{\{Y,Z,W,V,E\ {\rm unit}\}}
 \Delta_\ell\,\frac ZY\,E^a\phi_{a,N}\,de_0
\tag{25}
$$
仍持有完整 Y-unit 负一观察。
本篇的 $\Pi^W_{17,\pm}$ 或 $\Pi^V_{17,\pm}$
不能在 (25) 中改写成 Y 的三次投影；
两个不同环面的局部算子不是同一个标量投影。

原精确关系继续是
$$
P_{a,1}(\ell)=G_a(\ell)+\lambda H_a^W(\ell)
                            +\gamma\lambda H_a^V(\ell),
\qquad \gamma=\chi_A\chi_E,
\tag{26}
$$
连同 R737 的有限 primitive 消元及
$\mathcal O_{\rm pair}^T=-\mathcal I_{\rm pair}^T$。
所有 $E$ 浅门、条件质量、两返回源、两个 unit cut 和两个外部都在 (21)–(26) 内。

### 7.1 两个完整返回分母仍是范数34的退化轴

这里还有一个不能由首项展开省略的事实。实际
$$
\kappa=p\lambda^2=\pi_0/\bar\pi_0,\qquad
\mathrm N_{K/\mathbf Q}(\kappa)=1 .
\tag{27}
$$
故 $P_{W,\kappa}$、$P_{V,\kappa}$ 是全局有理 unitary 变换。
它们在17处整，且都保持 (9) 的球向量。两条完整分母
$$
Y_\kappa^V=\frac{\kappa V+\alpha W}{36},\qquad
Y_\kappa^W=\frac{V+\alpha\kappa W}{36}
\tag{28}
$$
的 Hermitian 范数**仍准确为34**：
$$
N(Y_\kappa^V)=N(Y_\kappa^W)
 =\frac{18936+349\cdot72}{36^2}=34 .
\tag{29}
$$
所以它们没有因在某个 p 处单位域中接近 W 或 V，
就成为一个十七处不退化的 W/V 轴。

更准确地，若 $P=P_{V,\kappa}$ 或 $P_{W,\kappa}$，
$Y_\kappa=YP$，则其真实局部环面及投影为
$$
G_{Y_\kappa}(g)=P^{-1}G_Y(g)P,\qquad
\Pi^{Y_\kappa}_{17,\pm}
 =\omega_{17}(P)^{-1}\Pi^Y_{17,\pm}\omega_{17}(P).
\tag{30}
$$
这是 canonical lift 的共轭等式，中心相位在共轭中准确抵消。
由于 $\omega_{17}(P)\Phi_{17}=\Phi_{17}$，
$$
\boxed{
\Pi^{Y_\kappa}_{17,\pm}\Phi_{17}
 =\omega_{17}(P)^{-1}\Pi^Y_{17,\pm}\Phi_{17}.
}
\tag{31}
$$
原 Y 的 gluing 被整共轭运输，而没有被 (17) 杀掉。

因此完整 $z_V/y_V$ 或 $z_W/y_W$ 行不能据 (17)
改认成一条“无 cubic17 的 E24 负一值”。
(22) 的首非恒定项使用裸 W-unit 负一，
但全部 $\kappa^m V^mW^{-m}$ 合起来恢复的是 (28) 的完整分母。
固定 p 后，$\kappa$ 不随 N 变小；
增加 N 不能把 $m\ge2$ 各项免费删成原 $p^{2N}$ 尾。
本篇的本地结论只消 W/V 环面的三次分量，
同时以 (30)–(31) 完整保留实际返回观察的 Y 型三次分量。


## 8. 与 R739 的准确接口

[R739](R739-seventeen-inertia-and-relative-algebraic-logarithm-separation.md)
已证明：R735 两个 Kummer17点的椭圆 logarithm，
相对所有在17处不分歧扩张上的 $E_1$ 代数点 logarithm，
仍在 $\overline{\mathbf Q}$ 上线性独立。
它也允许先把17单位 sextic 曲线的点搬到 $E_1$。

本篇付的是使用该引理前的一个实际必要输入：
两条返回支的 W/V 方向没有那两种 ramified-cubic17
**本地 Hecke 分量**，而且这在原混合 p 门中仍为真；
但 (28) 的完整分母仍保 (31) 的 Y 型 gluing。
要进一步应用 R739，仍须把所需的同域返回积分，
连同 (22) 的全部质量和伴随系数，
识别为代数系数乘17-unramified代数点的对数，或已付的代数/乘法对数项。
本篇未把一般 p 进条件系数误认作代数系数。

也未给 (25) 的 Y 观察作这个识别。
因此这里没有将局部无三次分量提升为主中央非零，
而是给原同一补偿式提供了可直接使用的完整17张量约束。

本篇为确切格与局部算子的证明，不产生新的可重算数据文件，
不改变原 $q_N^*$、射线或任何深度门。

### 依赖与原文

- [R686](R686-original-yz-core-and-same-source-st-unit-failures.md)，
  原完整框架及所有纯伴随；其脚本
  [check-r686-original-yz-core-and-st-unit-carries.js](../scripts/check-r686-original-yz-core-and-st-unit-carries.js)
  给 (10) 的原整行。
- [R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)，
  原16个 W-quarter lift、三态及全部实际词。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)、
  [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)、
  [R737](R737-common-depth-elimination-and-native-primitive-strips.md)。
- Tonghai Yang,
  [Theta liftings and Hecke L-functions](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf),
  J. reine angew. Math. 485 (1997), 25–53：
  §0 的“everything unramified”定义、Lemma 2.1 的 splitting
  及 Lemma 2.7 的 inert 球向量。
