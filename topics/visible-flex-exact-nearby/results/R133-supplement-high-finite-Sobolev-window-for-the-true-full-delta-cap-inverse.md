# R133：完整真实外帽逆的高阶 Sobolev 窗口与共同辅助权

2026-11-15，visible-exact-astra-0df9。

**已证明。** 同一修补中心、固定 eta0、原整个实参数区间
$Q_\delta=Q_0+\delta Z$、$|\delta|\le10^{-8}$ 的完整帽逆，可以从
[X 篇](R133-supplement-complete-real-delta-true-outer-finite-Sobolev-cap-inverse.md)
的 $-3/2\le s\le2114$ 延伸到
$$
                 -3/2\le s\le8212. \tag{Q.1}
$$
所有真实变动 long 外行、内端非mean C、完整 mean、one-sided 源、jump、
兼容性荷和独立 height gauge 仍在原单位中。未知方向保留全部 Fourier 模。

本篇只重新选择证明中的 shifted weight；不改物理对象、原截断、
原数值输入或实际参数。新结果为
$$
 \|\mathcal G_\delta^{\rm true}:
          \mathfrak D_s\longrightarrow\mathfrak M_s\|
                 <2^{4194304},                            \tag{Q.2}
$$
以及实际反射方向的真实 moving 读出
$$
 \|h\|_{L^\infty_rH^s_\varphi}
                 <2^{4718592}\|d\|_{\mathfrak D_s}.        \tag{Q.3}
$$
这些是高阶安全上界；原低阶真实反馈 $<3/8$ 及相对逆因子 $<8/5$
继续使用，不用粗大高阶常数替代精细97方向计算。

## 1. 全部实际源与已经证明的算子族

沿用 X.1 的 $\mathfrak M_s$：每个 Fourier 系数先在完整
$[9/10,25/8]$ 上取径向 supremum，再作带权平方和，两分量取和。
不交换 supremum 和 Fourier 和。

$\mathfrak D_s$ 完整保留 ordinary $L^2_rH^s$、angular-divergence
势 $\mathfrak M_s$、原端荷/jump 和全部 mean/height 输入。
外高度仍为原物理 $f_B\in H^{s+2}$；其常数槽独立保留。
$\mathfrak D_s^\flat$ 只把这一列改用
$$
 y_B=P_{\perp,x}(f_B\circ\tau_\delta),\qquad
                   g_B=|D_x|^2y_B.                       \tag{Q.4}
$$
不对零频使用 $|D|^{-2}$。

原完整固定角方程仍是
$$
 x=T_\delta x+L_\delta d,\qquad
 T_\delta=T_{{\rm body},\delta}+T_{{\rm out},\delta}.        \tag{Q.5}
$$
X.5–X.7 已在整个原实参数区间给出
$$
 \|T_\delta\|<3/8,\quad
 \sup_{|\operatorname{Im}z|\le\sigma_*}\|T_{\delta,z}\|<2^{129},
 \quad
 \sup_{|\operatorname{Im}z|\le\sigma_*}\|L_{\delta,z}\|<2^{128},
 \qquad \sigma_*=2^{-128}.                               \tag{Q.6}
$$
这些族在原径向 Banach 模块上已成立；long 的真实 pullback、weighted
mean、primitive、holonomy 小根、真实 $C_R$ inverse 和原残差 Hessian
都已计入。这里没有对一个未知有限光滑场作复角求值。

## 2. 较小的辅助 shift 足以覆盖实际所需高阶窗口

现在取
$$
 M=2^{416},\qquad W_{s,M}(n)=(1+n^2/M^2)^{s/2},
 \qquad \tau=|s|/(2M)<2^{-403}.                           \tag{Q.7}
$$
最后一步只用 $|s|\le8212<2^{14}$。
原完整 signed-lag lemma 直接给
$$
 \|W_{s,M}T_\delta W_{s,M}^{-1}-T_\delta\|
       \le8\,2^{129}\tau\sigma_*^{-2}<2^{-15}.             \tag{Q.8}
$$
真实 $3/8$ 加此数仍小于 $1/2$，所以
$$
 \|(I-W_{s,M}T_\delta W_{s,M}^{-1})^{-1}\|<2.              \tag{Q.9}
$$
没有要求证明中的 shift 至少为 $2^{1024}$；X 的更大选择是安全余量，
不是对象定义或数值输入。

完整 source 列也满足
$$
 \|W_{s,M}L_\delta W_{s,M}^{-1}\|
 \le2^{128}\sum_{\ell\in4\mathbb Z}
               e^{-(\sigma_*-\tau)|\ell|}<2^{259}.         \tag{Q.10}
$$
与 X.11 相同，使用所有整数的宽放
$\sum_\ell e^{-\sigma_*|\ell|/2}<2^{131}$ 即可。
全部原 many-jump 列的范数已在 $L_\delta$ 中，不重新逐行无偿计数。

通常 Sobolev 权与 shifted 权的总转换只付一次 $M^{|s|}$。
正 $s$ 时输出付 $M^s$、输入为收缩；负 $s$ 时相反。
因此
$$
 \|\mathcal G_\delta^{\rm true}:
      \mathfrak D_s^\flat\to\mathfrak M_s\|
                  <2^{416\cdot8212+260}.                 \tag{Q.11}
$$
mean 的权始终准确为1。负阶解先在有限 Fourier 数据上定义，再在其原
模块完成；零阶唯一性识别所有重叠定义，不把正阶结论形式倒推为负阶。

## 3. 真实实角及密度的高阶费用

X.13–X.14 中两个实际圆周图
$\vartheta=\tau_\delta,\tau_\delta^{-1}$ 已满足
$$
 1/2<\vartheta'<2,\qquad
 |\vartheta^{(k)}|/k!<1024^k\quad(k\ge2).                 \tag{Q.12}
$$
其 inverse 在原支付的 strip 内解析。这只用于已知图的实角导数。

整数 $0\le q\le8220$ 时，原 Faà di Bruno 组合给
$$
 \|f\circ\vartheta\|_{H^q}
 \le2^{2q+2}q!\,1024^q\|f\|_{H^q}
 <2^{262144}\|f\|_{H^q}.                                \tag{Q.13}
$$
确有 $q!<(2^{14})^q$，显示指数至多 $26q+2<262144$。
常数 $q=0$ 用真实 Jacobian 界直接支付。

实 $L^2$ 伴随仍准确为
$$
 C_\vartheta^*g=(g\circ\vartheta^{-1})(\vartheta^{-1})'.
$$
密度的前 $q$ 阶导数按原 $2k!\,2048^k$ 逐项计入，
Leibniz 与整数范数等价的费用同样小于 $2^{262144}$：
可用 $2^{3q+4}q!\,2048^q$ 的宽放，指数
$28q+4<262144$。双对偶和相邻整数复插值于是给
$$
 \|C_\vartheta:H^a\to H^a\|<2^{524288},
                         \quad |a|\le8216.               \tag{Q.14}
$$
完整 source 高度列因此满足
$$
 \|g_B\|_{H^s}
       \le2^{524288}\|f_B\|_{H^{s+2}},\qquad
                         -3/2\le s\le8212.               \tag{Q.15}
$$
整个所用 $s+2$ 窗口都严格落在 Q.14 内。

结合 Q.11 和 Q.15，
$$
 416\cdot8212+260+524288<4194304,
$$
得到 Q.2。所有费用都是原解析族和有限阶实链式法则的符号预算；
没有新增数值生产或重算任何原 grid、Gram、ODE、FFT。

## 4. 实际反射场的原 moving 读出

保持原固定 $D\Psi_0^{-1}$ 的完整公式，不替换成逐分量乘法。
X 第5节援引的 [S 第6节](R133-supplement-shifted-Sobolev-complete-gauge-Hessian-and-cap-tail-Schur.md)
给正阶角 pullback 费 $2^{43q/2+3}$、已合并系数乘法费
$2^{20q+34}$，以及完整 inverse 中的三个合并系数、primitive、
weighted mean 和负阶的真实密度因子。
同一推导现在取整数 $q\le8214$，其完整总费仍满足
$$
                    2^{123q/2+73}<2^{524288}.             \tag{Q.16}
$$
各系数来自已支付的同一 joint strip，故延长有限导数窗口不需要
未知背景的额外解析性。对当前反射方向原额外角相位按旧证明为0；
一般四重周期方向仍须保原完整角相位方程。

先用 $\sup_r\|x(r)\|_{H^s}\le\|x\|_{\mathfrak M_s}$，
再在每个实半径作真实角换元，由 Q.2 和 Q.16 得 Q.3。
它是 $L^\infty_rH^s$ 读出，不声称 moving $\ell^2(\sup_r)$ 的
未知角复合保持该范数。

## 5. 对后续有限正则邻域的准确接口

本窗口留出了 H8196 四态、有限次角/径向重建所需的角余量。
径向导数仍须由实际方程、真实单侧 traces 和源正则性另外支付；
一个 ordinary $L^2_r$ 源没有因此变成 $C_t^4$。

Q.2 的背景仍是显式 $Q_\delta$，外端仍是 T 已构造的同一真实
long 背景。它本身不把任意未知附近状态的 principal、角图或
非线性外边界当作已处理。下一项使用完整 conservative 多项式
和 $\mathfrak M_s$ 的有限 Sobolev 乘法，建立明确附近状态球；
真实非线性 long 图、全无限尾、中低 Schur 及精细 nu 方向继续分别付费。
