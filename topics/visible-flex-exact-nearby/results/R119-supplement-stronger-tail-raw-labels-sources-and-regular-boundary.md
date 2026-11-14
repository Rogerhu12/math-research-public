# R119 续篇：强首剪切新尾的真实 raw 权、完整连续源和 regular 外边界

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对第8192层后首剪切为 $2^{128}$ 的新候选，
重新证明共同 cut128 到全部内部标签的 raw404 费用，重新选择
实际有限 connector 与双 bump，并由新的无限允许线定义真正的
外 Robin。连续 ordinary source 的两个非mean迹、mean flux 和
独立高度常数在同一零标签径向线性参考上一起保留。
新对象的实际 R74 线性输入确实落入
$\|X\|<2^{-262144}$ 的条件球；本文不称这为给定非线性
外输入已经匹配，也不代替更新后同宽网络逆。

## 1. 新对象、完整标签线和真正新的锥

全篇固定一个实 $\Gamma$，采用
[新强全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
的全部实际几何、规范 $\zeta_j$、角宽、cap 低窗和标签。
线性齐次单位标签列记为 $H_m^\ddagger$，令
$$
 u_m=H_m^\ddagger(128),\qquad
 \mathfrak w_m=\|u_m\|_\infty^{-1},\qquad
                   m\in4\mathbb N.
 \tag{V.1}
$$
有限真流可逆且标签为1，故 $u_m\ne0$；全标签列 norm 小于9
立即给 $\mathfrak w_m>1/9$。以下证明上界，未由低图偷换高输入。
第1--4节逐模式以正 $m$ 书写，负模使用 $|m|$ 的相同矩阵和界；
后面的强 Fourier source norm 始终同时包括正负频率及 mean。

新低窗 $m^4\sqrt\delta\le2^{-160}$ 上，真实矩阵误差为
$2^{272}m^8\sqrt\delta$。实际理想大根满足
$\Lambda_{m,\mathsf K,C}>\mathsf K m^4/16$，且
$\|E\|\|E^{-1}\|<(17/16)^2<2$。因此
$$
 \frac{\|-E^{-1}B_{m,j}E-\operatorname{diag}(\Lambda,\lambda)\|}
      {\Lambda}<2^{149}m^4\sqrt\delta\le2^{-11}.
 \tag{V.2}
$$
对锥 $|v|\le|u|/2$，一个真实同基胞元的像在
$|v/u|<1/1024$，且大分量至少为
$(1-3\cdot2^{-12})\Lambda|u|$；这里还使用完整
$\lambda/\Lambda<2^{-24}$ 和真实 $\det B=1/C$。
第二接缝 $Q_2$ 的四个准确界已在前篇证明。它把这个小锥送入
$|v/u|<1/512$，第一行增益至少为 $1-1/(63\cdot1024)$。
因为新规范大因子 $2^{-131}\Lambda_4>5/2$，包括新接缝的
真实大行都有
$$
 |u_{j-1}|\ge e^{-mh_j}|u_j|                            \tag{V.3}
$$
作为安全下界。这里保留了接缝的交叉行与两侧 source 为0的事实。
旧窄锥与第一接缝仍使用上一 raw 权证明的完整两行界。

## 2. raw404 仍成立，新增坏前缀没有被略去

原43对浅模的标签仍在128。其余 $m\ge176$ 的旧窄锥起点可取
$j_0^{\rm old}(m)=\lceil56+8\log_2m\rceil$。
新起点可取
$$
 j_0^{\rm new}(m)=\lceil320+8\log_2m\rceil.
 \tag{V.4}
$$
当 $m\le M_*:=2^{-40}\delta_{8193}^{-1/8}$，新锥从8193起
就成立，旧锥与 $Q_2$ 在同一真实允许线上相接。
新接缝的 (V.3) 不增加原坏前缀费用。

若 $m>M_*$，则 $\log m>600$。在 $j_0^{\rm new}$ 处，
$h_j$ 的准确式给 $mh_j>3m^{31/32}$，而规范大根小于 $m^4$。
因 $m^4e^{-3m^{31/32}}<1$，标签层在新窄锥起点之后。
从那里到 cut128 可以完整使用真实逆矩阵。
这段坏前缀比旧起点最多增加264层；前篇的 monotone cap
意味着这些巨大频率在旧段一直保留真高块，不是假定它们
在缩窗时仍属于理想低块。

新的全模真流给所有修改层
$$
 \|A_{m,j}^{-1}\|<2^{600}(1+m)^{312}e^{m(h_j+\beta_{\mathsf K,j})}.
 \tag{V.5}
$$
其中真实逆流 $2^{450}$、规范逆 $2^{131}$ 和端口换算均已付；
旧段仍可用更小的 $2^{96}$。原坏前缀的额外每频费用小于
$$
 B_{\rm old}:=(3/8)^6(55917/5)=40763493/1310720<32.
$$
令 $x=\log m>600$。保留新增264层以及所有旧坏层中
$2^{600}/2^{96}$ 的放宽，新增每频对数费用至多
$$
 [12(x-6)\,504\log2+
       264(600\log2+312\log(1+e^x))]e^{-x}
 <(88416x+240768)e^{-x}<1/1000.                           \tag{V.6}
$$
最后的包络在 $x\ge600$ 递减。它与 $B_{\rm old}$ 的和仍
严格小于32；并非把新巨大常数直接当作旧 $2^{96}$。

全部实际 $\sum h_j$ 加新旧 $\sum\beta_j$ 仍小于358。
新增尾角费由 $1024\beta_{\mathsf K,j}<h_j$ 和8193以后
真正的几何和直接支付。回到共同 raw 两行所需的完整基 norm
也小于2。因此和旧证明同样的逐模逆乘积现在给
$$
 \boxed{\quad
 1/9<\mathfrak w_m<e^{391m},\qquad
                   \tau_{128}+391<404.\quad}             \tag{V.7}
$$
这证明的是本篇新允许线的权，包括第一改动前的完整有限前缀。

## 3. 第四线重新停止、完整尺度和所有 mean 端项

新真实第四物理斜率满足 $14<d_4^\ddagger<15$，且相对于
上一候选的差小于 $2^{-193532}$。令
$R_*^\ddagger=(1-d_4^\ddagger)/(16-d_4^\ddagger)$。
使用同一真正的最后 $q=-1$ Riccati 段重新选择停止长度，
其完整两端 germ 与最后 quintic 一起匹配。已证导数
$|dR_*/dd|<16$、$|d\ell/dR_*|<1/512$ 给
$$
 |\ell^\ddagger-\ell^\dagger|<2^{-193537},\qquad
 \epsilon_{\rm tail}^\ddagger=\epsilon_{\rm tail}^\dagger,
 \qquad\rho^\ddagger/\rho^\dagger
                    =e^{-(\ell^\ddagger-\ell^\dagger)}.
 \tag{V.8}
$$
$H_e\omega_e$ 的准确不变量使第二式成立。
固定物理 $a$ 的变分仍含 $A_\Gamma\delta\ell$ 尺度项。
完整 mean 高度是
$$
 Z_\Gamma(a)=Z_e(\Gamma)-\int_{a_e(\Gamma)}^a w_\Gamma(s)ds,
 \quad
 \delta Z=\delta Z_e+w_e\delta a_e-\int_{a_e}^a\delta w(s)ds.
 \tag{V.9}
$$
移动 cut 端项不能删除。有限 connector 与双 bump 的全部
$A$、长度、尺度和二 jet 仍在原实际有理盒内：新第四停止值
在同一个严格 $14<d<15$ 盒，且 (V.8) 远小于已付边距。

## 4. 先重新选择全模好集，再定义真正新 Robin

新的第四线经 (V.8) 回传到 $u=T$ 后再次准确为
$(1,-\omega)$。双 bump 的第四保持曲线仍是同一条
$s=s(2^{-17}t)$，但其它模的右线必须用本篇的新无限尾线
经新 connector 回传。对这些真实非零右线重新应用完整
R11 坏集证明，得到
$$
 G_\Gamma^\ddagger=\{t\in[0,1]:
 |\sin\angle(\Lambda_m^\ddagger(B;t),(1,\omega))|
       \ge2^{-39}\ \hbox{for every }m\in4\mathbb N\},
 \qquad |G_\Gamma^\ddagger|\ge1-83/16384.
 \tag{V.10}
$$
这是重新作的逐点选择；没有宣称最小好参数连续，也没有
把旧选定参数自动搬到新尾。此后固定一个真正的好参数。

同一个未改的 $a_*,z_*,\omega$ 与
$B=2^{24}-25/8$、$L=\omega B$ 给新的准确齐次斜率
$$
 |\lambda_m^\ddagger+m\omega|
       <2^{41}m\omega e^{-2mL},\qquad
 \lambda_4^\ddagger=-4\omega.
$$
保留完整 grounded 两迹
$$
 v=A_0y-4y_u/m^2,\quad p=-y+4y_u/A_0,\qquad
 A_0=4\omega+a_*^2/z_*.
$$
本篇真实外 Robin 因而是
$$
 \gamma_m^\ddagger=
 \frac{1-4\lambda_m^\ddagger/A_0}
      {A_0-4\lambda_m^\ddagger/m^2},\qquad
 \gamma_0^\ddagger=0.                                    \tag{V.11}
$$
mean 行单独来自真实平移与零 holonomy flux。重新代入同一
R74 完整入口代数，得到所有非零四重模的
$$
 m/7<\gamma_m^\ddagger<m/5,
 \qquad
 \big\||D|^{-1/2}(\Gamma^\ddagger-\Gamma^\dagger)|D|^{-1/2}\big\|
              <2^{43}e^{-8L}<2^{-2^{27}}.                 \tag{V.12}
$$
新的自伴、非负、阶1闭边界图及准确常数槽再次允许在未改
有限正帽上重新实例化 R45 的 form/局部 Airy/contact 证明。
其 $C_w<70.378782$、$C_s<140.771775$ 不依赖把新旧 Poisson
算子视为相等。任意粗 Sobolev 外迹到完整尾的 $C^2$ 重建权限
仍不由这个有限帽闭图自动取得。

## 5. 真 continuous source 空间和完整平坦 realization

本节是同一新径向零标签参考的线性方程，$m\ne0$ 的 ordinary source
准确按
$$
 h=\rho H,\quad
 N_m=\frac{\mu_jp_*^2}{12r^{10}}e_m
    =\frac{p_*}{12r^2}F_m
    =\frac{p_*}{\sqrt{12}r^3}e_{\mathcal E,m},\qquad
 F=we/r,\quad e_{\mathcal E}=we/\sqrt{12}                 \tag{V.13}
$$
换算。新的 $p_*$ 含 $\mathsf K$，两个 $p_*$ 因子没有省去。
令 $\beta_j$ 在未改层为旧值、在修改层为前篇
$\beta_{\mathsf K}(\delta_j)$，并取 $\sigma=\tau_{128}-1$。
定义完整强源 norm
$$
 \|N\|_{\mathcal S_{1,\beta}}=
 \sum_{m\in4\mathbb Z}(1+|m|)^{312}
 \sup_{j>128}\frac{e^{|m|(\tau_{j-1}+\beta+\beta_j)}}{\zeta_{j-1}}
                  \int_{I_j}|N_m(y)|dy,
$$
$$
 \|N\|_{\mathcal S_{2,\beta}}=
 \sum_{m\in4\mathbb Z}\sup_{j>128}
       \frac{\delta_j^4}{\zeta_j}
       e^{|m|(\sigma+\beta)}\sup_{I_j}|N_m|.              \tag{V.14}
$$
常数模包括在内。先逐模取径向上确界再求和，未换序。
实际 Duhamel 两行和端口 $\operatorname{diag}(1,1/c_j)$ 给
$$
 \|f\|_{\mathcal F_\beta}\le2^{450}\|N\|_{\mathcal S_{1,\beta}},
 \quad
 \|X\|_{\mathcal X_\beta}
      <9\|a\|_\beta+2^{466}\|N\|_{\mathcal S_{1,\beta}}.
 \tag{V.15}
$$
没有只取第一行或只保高度 particular。

mean 仍准确为
$$
 p_0=(w/r)(H_t)_0,\qquad
 (p_0)_y=\sqrt{12}\,\mu_jr^{-4}N_0,\qquad
 p_0(y)=\int_{y_f}^y\sqrt{12}\,\mu r^{-4}N_0dy,
$$
$$
 H_0(t)=\lambda+\int_{t_f}^t(r/w)p_0dt.                 \tag{V.16}
$$
平端的 flux 为0，cut128 的 flux 则是输出，不可再置0。
只有 $\lambda$ 一个独立高度常数。

为了验证真实平坦性，可以保留较粗但统一的旧规范
$\zeta_j^{\rm old}=\epsilon\delta_j^{39/4}$ 作为物理包络。
准确有 $\zeta_j\le\zeta_j^{\rm old}$、
$\zeta_{j-1}\le\zeta_{j-1}^{\rm old}=2^{39/4}\zeta_j^{\rm old}$，
且修改层 $p_*^\ddagger\ge p_*^\dagger$（逐点比较同一 log
插值和同一 bump）。故所有 mean primitive 的旧绝对包络
继续成立，而非错误地以 $\zeta_{j-1}/\zeta_j<2^{10}$ 计算。
新全模内部流的固定增加费由 $2^{450}/2^{80}$ 支付，
其余 canonical 到 physical 的 $p_*^{-1}$、$A$ 门不增加。
一个包括 mean 的完整安全界为
$$
 \|H-\lambda\|_{C^2_{r,\theta},\mathcal A_{\sigma+\beta}(I_j)}
 <2^{480}626^{313}\epsilon\delta_j^{19/4}
       (\|X\|_{\mathcal X_\beta}+\|N\|_{\mathcal S_{1,\beta}}
                                    +\|N\|_{\mathcal S_{2,\beta}}).
 \tag{V.17}
$$
连续物理源保证接缝两阶迹按方程匹配；全部平端 jets 因而趋0。
这是真正 source-dependent 线性全频 $C^2$ realization。

## 6. 新全有源两迹和实际外 affine 列

令 $g_m(N)=(\mathcal G^\ddagger f)_{m,128}$。
一个 cut128 两分量 $v_m$ 可由同一个实际全尾线性方程实现，当且仅当
$$
 v_m-g_m(N)\in\operatorname{span}u_m,\qquad
 \sum_{m\ne0}e^{\beta|m|}\mathfrak w_m
                 \|v_m-g_m(N)\|_\infty<\infty.           \tag{V.18}
$$
后一个和准确是标签 norm。mean 则必须等于 (V.16)，不是
任意另指定的一对数。

现在源只支持于 mixed tail，有限 connector、双 bump 和长段
无源，并取具体充分合同
$S_*:=\|N\|_{\mathcal S_{1,2304}}+
\|N\|_{\mathcal S_{2,2304}}$。
零标签 particular 满足 $\|X^p\|_{2304}<2^{466}S_*$。
以新真实 connector 和新好 bump 的相同完整有理窗口传播，得
$$
 \|(f_B^p,k_B^p)\|_{\mathfrak C_{\sigma_B}}
 <2^{-447}\|X^p\|<2^{19}S_*,\qquad
 \sigma_B=\tau_{128}+2304-235=832777/400>2074.
 \tag{V.19}
$$
$f_B=h_\perp/(a_Bw_B)$、$k_B=(h_a)_\perp/w_B$，两行一起保留。
新的真 raw404、增长线夹角和完整第四保持曲线重新满足
实际 Schur1850 证明，故
$$
 \|(\mathsf D_0^\ddagger)^{-1}g\|_{\ell^1_\beta}
 \le\frac1{16}\|g\|_{\mathfrak Z_{\beta+1850}},\qquad
 \mathsf D_0^\ddagger a=k_B^{\rm lin}+M\coth(ML)f_B^{\rm lin}.
 \tag{V.20}
$$
这一步每个输入已由本篇新线证明，未把旧算子原样转授。
特别令外端非mean raw Dirichlet 为0，取
$$
 a^N=-(\mathsf D_0^\ddagger)^{-1}
                  [k_B^p+M\coth(ML)f_B^p],\qquad
 \|a^N\|_{224}<2^{18}S_*,\quad\|X^{\rm total}\|_{224}<2^{467}S_*.
 \tag{V.21}
$$
尾、有限 connector 和真实长段 Dirichlet 解的两条非mean迹
因此准确匹配；particular 未被删掉。

定义新的真齐次 regular 解 $q_m$，外端
$v(q;0)=1,p(q;0)=-\gamma_m^\ddagger$。
由新实际增长线夹角，$\|Y(q;B)\|_2<2^{42}e^{-ML}$，
$Y=(y,y_u/M)$。全两迹矩阵的行列式仍准确是
$4(1-M^{-2})$，所以真实外 affine 列为
$$
 r_m(N)=p_m(0)+\gamma_m^\ddagger v_m(0)
       =4(1-M^{-2})M\det(Y(q_m;B),Y^p_m(B)).             \tag{V.22}
$$
加上任何齐次真允许线不改变此式。完整 source-free 长段的
Wronskian 常数性在此合法。仍有
$\|Y^p(B)\|_2<h(B)^{-2}(|f_B|+|k_B|/M)/8$；此处
$h(B)=1/a(B)$，所以 $h(B)^{-2}=a(B)^2<1$，与 raw 高度不同。
由 (V.19)，对真实物理窗口 $\sigma_o=1/512$ 得
$$
 \boxed{\quad
 \|r(N)\|_{\mathcal A_{\sigma_o},1}<2^{80}e^{-4L}S_*.
 \quad}                                                     \tag{V.23}
$$
新的 $2^{450}$ 源传播费在此明确保留，未沿用旧 $2^{-300}$。

## 7. 完整 mean 外行与真正线性输入入球

外部无源时，(V.16) 的 $p_0$ 沿全有限部分保持。平均 raw
高度准确为
$$
 h_0(0)=\rho\lambda+\rho\int_{t_f}^{t_e}(r/w)p_0dt
                 +p_0\int_{t_e}^{t_B}(a/w)dt+4\omega Lp_0.
 \tag{V.24}
$$
同一个 $\mu_j$、$\zeta_j\le\zeta_j^{\rm old}$ 以及
$p_*^\ddagger\ge p_*^\dagger$ 给尾 primitive 的旧绝对包络；
新 connector 又保持原 $w\ge2^{-6}w_e$、总时间小于132等
实际门。因此真实输出仍有
$$
 |h_0(0)-\rho\lambda|<2^{-400}S_*,\qquad
 |p_0|<2^{-1200}\epsilon S_*.
 \tag{V.25}
$$
这两行没有被非mean的 $e^{-4L}$ 免费替代。

零尾源时，全部新有限几何、raw404 和真增长线夹角均已重建。
因此对 R74 原本允许的真实外输入及普通帽源（$B$ 后齐次），
把 R74 允许范围内的源 Lebesgue 指数另记为 $q_{\rm src}$，
以区别于胞元 profile $p_*$。按原完整量
$$
 A_m=h(0)^2|f_m|+M^{1/q_{\rm src}}F_{m,q_{\rm src}}
$$
（这里 R74 的 $h(u)=1/a(u)$ 仍是参考半径的倒数）
重新进行线性传播，得到本篇新对象的
$$
 \|a^{\rm lin,\ddagger}\|_{224}
       \le e^{-33545404}\sum_{m\ne0}A_m,\qquad
 \|X^{\rm lin,\ddagger}\|_{224}
       <16e^{-33545404}\sum_{m\ne0}A_m.
 \tag{V.26}
$$
所以 $\sum A_m\le1$ 的真正新线性输入严格在
$\|X\|<2^{-262144}$ 内，支付前篇全部尾有限前缀的条件
乘法账。这是实际传播结果，而不是任意再缩一个抽象球。
但把这些标签送入新非线性尾图后，外部完整两迹会产生真实
二次变化；(V.26) 没有断言该变化已经由更新后 regular
边界解消掉。给定非线性输入的可达性和同宽相对逆仍须继续。

若 source 来自 metric tensor $T$，必须在本篇的新实际 $w$
上使用
$e_{\mathcal E,T}=-ED^{-3/2}D_g\mathcal P(g_0,z)[T]/(\sqrt{12}w)$，
再检查 (V.13)--(V.14)，并保留完整 tensor jets、normal/shear
端项、角周期及 mean holonomy 条件。任意 scalar source 解
不自动授予全局单值的水平重建。

## 8. 证据与继续项

`scripts/fourfold_stronger_tail_boundary_sources_20261113.py` 和
`notes/2026-11-13-R119-stronger-tail-boundary-sources-budget.json`
验证全模窄锥、额外坏前缀、实际全部角和、第四停止差、全源
归一化、两迹行列式、完整 mean 以及新真实线性入球的数字门。
本篇是新径向参考及其完整连续源接口。新非零标签处的实际
Airy/root/strict 同宽比较、联立相位参数与最终 mixed-network
逆并没有在这些门中被省略。
