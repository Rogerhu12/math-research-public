# R119 续篇：更深首剪切的真实几何、全模矩阵与完整局部 Darboux 图

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇在已有 $b=9/2$ 新尾的第8192层之后，
把第一主剪切准确改为 $\mathsf K=2^{128}$。其余三个平台值、
末端幅度比和所有真实接缝保留。下面重新证明这个对象的
$C^2$ 平尾、真实全频矩阵、含 mean 的完整非线性局部图，
并逐项验证无频率损失参考 Airy 定理的前提。

这又是一个明确的新候选公共度量族，并不是沿一次固定度量
Newton 迭代偷偷改变背景。旧的全标签图、齐次/仿射外 Robin、
全模好集和 KAM 选择尚不能只因本篇成立就转授。末节把下一次
全标签规范所需的两个全局因子以及真实切换层的大费用全部列明。

## 1. 准确新 profile 和不变的接缝

采用 [上一新尾](R119-supplement-new-deep-profile-and-actual-homogeneous-Robin.md)
的所有胞元位置，并固定
$$
 J_*=4096,\quad J_2=8192,\quad \mathsf K=2^{128},\quad
 C=16\sqrt2,\quad \alpha=65/64,
$$
$$
 \delta_j=\frac2{25}2^{-j},\qquad
 \eta_j=\frac{\delta_j^{3/2}}{4\sqrt2},\qquad
 \mu_j=\begin{cases}
 \epsilon\delta_j^6,&j\le J_*,\\
 \epsilon\delta_{J_*}^{3/2}\delta_j^{9/2},&j>J_*.
 \end{cases}                                                \tag{T.1}
$$
令 $K_j=64$ 于 $j\le J_2$，$K_j=\mathsf K$ 于 $j>J_2$。
第 $j$ 个胞元的五个平台准确为
$$
 1,\qquad K_j/\delta_j,\qquad\delta_j/\alpha,
       \qquad1/\delta_j,\qquad c_j,
 \quad c_j=64\ (j\le J_*),\quad c_j=C\ (j>J_*).            \tag{T.2}
$$
三个中间平台各长 $\delta_j$，四个 log-quintic 过渡和两个
端平台各长 $\eta_j$。沿用同一 $S(x)=10x^3-15x^4+6x^5$
以及两下降坡内原有的 $\gamma_{j,k}\psi_{j,k}$。
实参数盒仍是 $\|\Gamma\|_\infty<2^{-16}$，复盒为 $2^{-15}$。
定义
$$
 w^\ddagger_\Gamma(r)=\mu_jp^\ddagger_{j,\Gamma}(r)/r^7,
 \qquad y=\sqrt{12}\log r,\quad1\le r\le2.                \tag{T.3}
$$

新首平台没有改变胞元的两个端值。故准确恒等式
$c_j\mu_j=\mu_{j-1}$ 仍在每一个接缝成立，包括 $J_2+1$。
所有 log 插值的端一、二导数和参数 bump 的二 jet 都为0，
所以 $w,w_r,w_{rr}$ 真实匹配。用 $z_r=-w$ 积分一次给共同
高度，不另指定深端高度。

对所有修改层 $j>J_2$，四个 log 跳幅的和准确是
$$
 6|\log\delta_j|+c_{\mathsf K},\qquad
 c_{\mathsf K}=2\log(\mathsf K\alpha)-\log C<175.          \tag{T.4}
$$
每一实际跳幅仍在 $j/2$ 和 $3(j+4)$ 之间，且每次不超过
$3|\log\delta_j|$。原两个下降 bump 的导数符号与支集证明
因此仍逐项满足其同一较宽门；复参数时使用 $|p|$ 的真正单调性。
本文没有将复面积当作正实面积。

## 2. 完整几何与两转向参考前提

令 $L_j=1+|\log\delta_j|$。直接微分 (T.3) 并用
$|S'|\le15/8$、$|S''|\le6$、$|\psi_x|\le96$、
$|\psi_{xx}|\le6144$，可取修改层上的完整界
$$
 |w|<2\mathsf K\mu_j\delta_j^{-1},\quad
 |w_r|<2^{10}\mathsf K\mu_jL_j\delta_j^{-5/2},\quad
 |w_{rr}|<2^{21}\mathsf K\mu_jL_j^2\delta_j^{-4}.         \tag{T.5}
$$
相应深端幂仍是 $7/2,2,1/2$。固定的 $\mathsf K$ 不改变
三者趋0，参数差同样满足乘 $\|\Gamma-\widetilde\Gamma\|$
的二阶包络。由此在平盘内延成0仍为真正的 $C^2$ 函数，
而且乘积拓扑给参考面的 $C^2$ 连续性。

更明确地，修改层第一层的 $w_r$ 包络相对于原第128层的
旧完整包络，至多
$$
 2^{128}\frac{L_{8193}}{L_{128}}
      \delta_{4096}^{3/2}\delta_{8193}^{2}\delta_{128}^{-7/2}<1.
 \tag{T.6}
$$
以后相邻比严格小于1。所有新增曲率仍由原有限浅端包络
控制，R69 的几何严格余量保留。本句只证明新参考几何，
没有赋予尚未构造的非径向解 reach。

以下参考 Airy 结论取实参数；复参数盒只用于后面的完整全纯图。
每个完整负分量令 $Q=-A$、$A=w_t/w$、$t=\log r$、
$\mu_0=w/(\rho e^t)$。实际 $Q$ 先不减后不增，其两个根
仍在真实上升 quintic 内。第一个上升落差现在为
$\log\mathsf K-\log\delta$，第二个仍为
$\log\alpha-2\log\delta$；不能说它们的旧根位置未变。
由刚证明的跳幅门、同一 bump 三阶分段界和真实长度，可取
$$
 \delta_j/4<|I|<4\delta_j,\quad
 Q_{\max}<2^{12}(j+4)\delta_j^{-3/2},
$$
$$
 |Q_t|<2^{18}(j+4)\delta_j^{-3},\quad
 |Q_{tt}|<2^{26}(j+4)\delta_j^{-9/2},\quad
 \mu_0(t_-)/\mu_0(t_+)<2^{132}\delta_j^{-2}.
 \tag{T.7}
$$
$Q_t$ 连续，$Q_{tt}$ 取分段 $L^\infty$，不引入接缝原子。
密度比直接由首峰 $p\le\mathsf K/\delta$、谷值
$p\ge\delta/\alpha$ 和 $r^{-8}$ 因子得到。
它小于全频参考篇允许的 $2^{272}\delta^{-2}$。

对两个实际上升根重新代入其精确
$z=(7\eta/(30\sqrt{12}\Delta))^{1/2}$，仍有
$z<2^{-20}$ 和 $\delta^{-9/4}<|Q_t(t_e)|<
2^{16}\sqrt{j+4}\delta^{-9/4}$。因此
[全频参考 Airy 证明](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)
的完整 quartic、复势、两行 Airy 以及严格段证明可在这个新对象
上重新实例化，得到
$$
 \|\mathcal U_j^\ddagger(t,s)\|
 \le2^{5000}(j+4)^5\delta_j^{-10}.                          \tag{T.8}
$$
这是同宽的所有 Fourier 模（含 mean）与完整两态的参考界；
参数导数和非线性网络逆仍不是它的推论。

## 3. 真 canonical 方程、理想矩阵和低窗绝对误差

本节及第4--5节的 canonical 两行矩阵、$m^4$ 和 $m^8$ 界，
量词准确限定为 $m\in4\mathbb Z\setminus\{0\}$（以 $|m|\ge4$
使用）。第2节参考 Airy 两态的 mean 与这里不同，仍已包含。
本节物理普通源的 mean 另按真实恒等式
$$
 p_0=\frac wr(H_t)_0,\qquad
 (p_0)_t=\langle w^2e\rangle,\qquad
 (H_0)_t=\frac rwp_0
$$
携带；不能在 $\nu_0=0$ 的 canonical 式中代 $m=0$。
完整非线性 mean 小根及压缩 leading matrix 在第6节另付，
独立高度常数仍保留。

物理 raw 高度为 $h=\rho H$。所有修改层仍准确满足
$$
 W_y=\begin{pmatrix}k_m&\nu_m/p_*\\-p_*&-k_m\end{pmatrix}W
       +\binom0{N_m},\quad
 \nu_m=\frac{m^2(m^2-1)}{12},\quad k_m=\frac{m^2-4}{\sqrt{12}},
$$
$$
 W=\left(\frac{\nu_mH}{r^4},
         \frac{p_*}{\sqrt{12}r^4}(H_t-m^2H)\right),\qquad
 N_m=\frac{\mu_jp_*^2}{12r^{10}}e_m.                      \tag{T.9}
$$
这里 $p_*=p^\ddagger_{j,\Gamma}$。末端状态换到下一胞元时
准确除第二分量以 $c_j=C$，不是除以 $\mathsf K$。
故理想矩阵和真实行列式为
$$
 B_{m,\mathsf K,C}^{\infty}
 =\begin{pmatrix}
 1-\mathsf K\alpha\nu&\alpha\nu\\
 (\mathsf K\alpha\nu-\mathsf K-1)/C&(1-\alpha\nu)/C
 \end{pmatrix},\qquad \det B_{m,j}^\ddagger=1/C.           \tag{T.10}
$$

在
$$
 |m|\le M_j^\ddagger=2^{-40}\delta_j^{-1/8}                \tag{T.11}
$$
内，$m^4\sqrt\delta\le2^{-160}$、$m^2\delta<1$。
六个短段的完整 generator 积分之和不超过
$16\mathsf K m^4\sqrt\delta\le2^{-28}$。
三个真实平台用准确 $A_m^2=-(7m^2-16)I/12$ 的 sin/cos
式估计，其范数分别小于 $2\mathsf K,4\nu,3$。
它们和相应三个剪切的总有序乘积差小于
$2^8\mathsf K m^8\delta$：各单个平台差可分别用
$4\mathsf K m^4\delta,4m^4\delta,4m^4\delta$，再乘另外
两个真实/理想平台的界。六个短段插回实际位置，望远镜差至多
$$
 24\mathsf K\nu
       (e^{16\mathsf K m^4\sqrt\delta}-1).
$$
同一乘积中每个真实平台只出现一次，没有额外重复大首剪切。
末端 $\operatorname{diag}(1,1/C)$ 不增大范数，故得到安全界
$$
 \boxed{\quad
 \|B_{m,j}^\ddagger-B_{m,\mathsf K,C}^{\infty}\|_\infty
       <2^{272}m^8\sqrt{\delta_j}.
 \quad}                                                     \tag{T.12}
$$
所有面积和 generator 的绝对值界同时覆盖完整复参数盒。
这不是把旧 $32768$ 改个标签，新的 $\mathsf K^2$ 已在
$2^{272}$ 中真实支付。

## 4. 任意内部低窗流，不把大剪切指数化

完整 Galerkin 仍使用较大的实际内部窗
$|m|\le2^{-5}\delta^{-3/8}$。置
$\varrho_m=\sqrt\delta+k_m\delta+\nu_m\eta<2^{-24}$。
R38 的准确单调 Gauss 分解逐段只依赖 $k,\nu,\eta$，
所以其对角共轭后的面积相对误差仍小于 $25k\delta$，
总对角积 norm 小于2。

有序乘积是 $D P_+C_*P_-$。第一组仍准确为
$P_-=L_4L_3U_3L_2U_2L_1U_1$。
将相邻 $L_4L_3$ 合并，保留 $1+a_4+a_3$，其值小于
$1+(1+25/1024)\mathsf K(1+\eta/\delta)$。
其余小面积满足
$$
 a_2<2\mathsf K\eta/\delta,\quad a_1<2\eta,\quad
 \nu(b_1+b_2)<4\nu\eta,\quad
 \nu b_3<2\nu\delta^2/\mathsf K.
$$
它们的和小于 $1/16$（首项由 $j>8192$ 支付），故
$\|P_-\|<2\mathsf K$。这里没有使用错误的 $e^{\mathsf K}$。
中央因子仍准确是
$C_*=U(\nu b_6)L(a_5)U(\nu(b_5+b_4))$；它的完整两行
R72 面积式不含第一首峰，仍给 $\|C_*\|<4\nu$。
末侧仍有 $\|P_+\|<4$。于是任意截短真实子区间及其逆满足
$$
 \boxed{\quad
 \|\Psi(s,t)\|_\infty<8\mathsf K m^4=2^{131}m^4,
 \qquad\|\Psi(t,s)\|_\infty<2^{132}m^4.
 \quad}                                                     \tag{T.13}
$$
实际因子顺序、每个平台的小反剪切和全部端平台都保留。

## 5. 真全频内部流和角费

定义
$$
 \beta_{\mathsf K}(\delta)=3\delta+6\eta+
 \sqrt{\frac{15}{2}\eta
       (2\log(2\mathsf K)+6|\log\delta|)},\qquad
 C_M=1+\frac{15}{8c_\eta}(2+\log(2\mathsf K))<2^{10},
 \quad c_\eta=1/(4\sqrt2).                                \tag{T.14}
$$
若 $m\le\delta^{-1/16}$，六短段任意 prefix/逆的总费小于
$e^6$，三个精确平台至多 $(\mathsf K+4)^3(1+m)^{12}$。
其前提 $c_\eta(\mathsf K+68)\delta^{1/4}<1$ 在8193层
成立并向深处改善。

其余模消去第二分量，得到
$Q''+bQ'+(d_m-k_mb)Q=0$。在各段以
$(m\sqrt{1+\sup|b|}\,Q,Q')$ 估计。
完整 $\int|b|$ 费用至多 $4\mathsf K^2\delta^{-6}$，
八次内部能量转换至多 $C_M^4\delta^{-10}$，两次真正
canonical 端点转换至多
$2\mathsf K(\sqrt{C_M}+3)(1+m)^3\delta^{-9/4}$。
剩下角指数准确是 $m\beta_{\mathsf K}$。
用 $m>\delta^{-1/16}$ 吸收 $\delta^{-19}$，再将
$(Q,pQ')$ 换回 (T.9) 的 $\nu Q$ 第一行，得到所有模、
所有内部子区间及逆的统一界
$$
 \boxed{\quad
 \|\Psi(s,t)\|_\infty,\ \|\Psi(t,s)\|_\infty
 <2^{450}(1+|m|)^{312}e^{|m|\beta_{\mathsf K}(\delta)}.
 \quad}                                                     \tag{T.15}
$$
例如未取粗幂前的常数可用
$64[e^6(\mathsf K+4)^3+
8\mathsf K^3C_M^4(\sqrt{C_M}+3)]<2^{440}$；其余 norm
及 $\nu$ 转换由额外 $2^{10}(1+m)^4$ 支付。
此式保留真实高模，未用 (T.12) 的理想矩阵替代它们。

## 6. 完整 mean、有限近解和零 residual 全角修正

新的局部方程仍是 R72 (2.4)--(2.7) 的实际内向方程，以
新 $w=\mu_jp_*/r^7$ 代入。特别必须使用完整压缩 leading
matrix 的逆
$$
 \kappa_y=\bigl(\Pi_J[\rho_D(1+n_{\rm ph})]\Pi_J\bigr)^{-1}
                 \Pi_J(\rho_D\mathscr G_+).               \tag{T.16}
$$
完整角通量 $M=1$ 保持，初始 mean 用同一个小根，不能置0。
材料证明的 $|w|<1$、$p_*\ge\delta/2$、
$w_{\min}\ge\mu\delta/256$ 已由 (T.1)--(T.5) 支付。
带 $p_*^{-2}$ 的 log 变差仍以准确端值积分；增大首峰只
减小该峰的倒平方项。加上 (T.4)，实际完整材料积分仍有
$$
 \int(1+|\lambda|)(1+|p_*|^{-2})dy<64\delta^{-2}.
 \tag{T.17}
$$
因此同一逐项源证明给 $2^{24}Z^2/(\mu\delta^2)$ 和
$2^{26}Z_0\|\Delta W\|/(\mu\delta^2)$，含 mean 与压缩逆。

取 $0<h\le1$、$4\le J\le2^{-5}\delta^{-3/8}$ 且
$$
 Jh/4\ge4096(1+|\log\delta|),\qquad
 1024\beta_{\mathsf K}(\delta)\le h.
 \tag{T.18}
$$
由 (T.13)，齐次强范数小于 $2^{148}h^{-5}B$。
取 $Z_0=2^{149}h^{-5}B$ 以及
$$
 R_j^\ddagger=2^{-320}\mu_j\delta_j^2h^5J^{-5}.           \tag{T.19}
$$
则完整有限积分方程的 Lipschitz 常数不超过
$2^{131+26+149-320}=2^{-14}$，初始/全程 mean 和压缩逆
相对量小于 $2^{18+149-320}J^{-5}$。这先支付真实小球，
没有先假定其解存在。

随后解准确强迫差方程
$V_y=\mathcal F(W_{\rm app}+V)-\mathcal F(W_{\rm app})-(0,e)$。
九段径向增益仍小于 $2^{38}e^{480c_{\mathsf K}}\delta^{-2890}$，
角费为 $256\beta_{\mathsf K}$。与旧有限近解相比，$Z_0$
多出的125个二进制幂逐项进入 residual，给
$S_e\le2^{172}\delta^{-7/2}h^{-5}B e^{-Jh/4}$。
在所有 $j>8192$ 上有准确门
$$
 e^{480c_{\mathsf K}}<\delta_j^{-16}.                     \tag{T.20}
$$
所以全部强修正 physical norm 小于
$2^{214}\delta^{2373/2}h^{-5}B$，回到真实 canonical
输出并付剩余角宽后可取
$$
 L_{\rm corr}^\ddagger
       =2^{224}\delta^{4743/4}h^{-5}.                     \tag{T.21}
$$
原四分之一宽的转换还使用 $h\ge\delta^{3/8}$，由
(T.18) 和实际 $J$ 上界推出。源项的低模与 mean 没有删除。
用 (T.19) 检查强修正与 $w_{\min}$ 的比，其上界已小于
$640\,2^{-106}\delta^{2375/2}J^{-5}<10^{-6}/4$。
因此整个全角修正确实留在原正分支。

对有限 Duhamel 二次项，在真实输出宽差内使用
$2^{131}\sup m^4e^{-hm/4}<2^{144}h^{-4}$；结合上面的
完整源和强解差量给二次 Lipschitz 系数小于
$2^{472}(\mu\delta^2)^{-1}h^{-14}$。
全纯修正减去其真实一次项后的附加比至多
$2^{51}\delta^{9471/8}<1$。故完整局部 map 满足
$$
 \boxed{\quad
 \Phi_j^\ddagger:B_{\mathcal A_{\tau+h}}(R_j^\ddagger)
          \longrightarrow\mathcal A_\tau,\qquad
 \|\Phi_j^\ddagger(U)\|\le2^{149}h^{-5}\|U\|,
 \quad G_j^\ddagger=2^{480}(\mu_j\delta_j^2)^{-1}h^{-14}.
 \quad}                                                     \tag{T.22}
$$
$G_j^\ddagger$ 同时控制真实二次余项和二次 Lipschitz 差。
这两项二次估计在 $R_j^\ddagger/4$ 输入球内成立；局部 map
本身定义在 (T.22) 的完整球上。常数与任意绝对角宽 $\tau\ge0$ 无关。
这是全频零 Darboux residual 的局部图，包含真正 mean；
$D\Phi_j^\ddagger(0)$ 是 (T.9) 的完整九段矩阵。

方程本身给 $\|\kappa_y\|\le16m_*Y$，故同一全角图的完整
物理二 jet 可取
$$
 \|v\|_{C^2_{r,\theta},\mathcal A_\tau}
       <2^{184}\delta^{-4}h^{-5}\|U\|.                   \tag{T.23}
$$
在已付的输出宽内，真实相对梯度/角导 $(P,K,U,V)$ 也由
$2^{184}(\mu\delta^2)^{-1}h^{-5}\|U\|$ 控制。
独立 mean 高度常数仍只通过最后一次统一积分确定。

## 7. 下一全标签规范及不能删除的切换层费用

本篇尚不从局部图直接宣布全尾图。为使随后全标签图的范数
在 $J_2$ 准确连续，唯一采用的候选规范是
$$
 \zeta_j^\ddagger=\begin{cases}
 \epsilon\delta_j^{39/4},&j\le J_2,\\
 \epsilon\delta_{J_2}^{39/4-131}\delta_j^{131},&j>J_2.
 \end{cases}                                               \tag{T.24}
$$
所以修改层的规范端因子是 $2^{-131}$。
理想负迹及大根为
$$
 T_m=\alpha\nu_m(\mathsf K+1/C)-(1+1/C),\qquad
 \Lambda_m=(T_m+\sqrt{T_m^2-4/C})/2.
$$
直接代 $m=4$ 得 $2^{-131}\Lambda_4>5/2>\sqrt2$；
实际大主剪切已经足够支撑新规范，而非任意挑一个更快的权。

最关键的真实比例准确是
$$
 \boxed{\quad
 \frac{\zeta_j^\ddagger}{\mu_j\delta_j^2}
 =\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}
                         \delta_j^{249/2},\qquad j>8192.
 \quad}                                                     \tag{T.25}
$$
两个全局逆幂都必须保留。尤其首修改层并不自动获得
$\delta_j^{249/2}$ 所暗示的绝对小量；它与8192层的旧比例
按准确一层因子 $2^{-249/2}$ 相接。
在 $h_j=8\delta_j^{1/256}$ 后，相对状态幂为
$249/2-5/256=31867/256$，仍须先付 (T.25)。

已有参考 Cauchy 的平方费是
$2^{10000}(j+4)^{10}\delta_j^{-20}$。仅把它乘 (T.23)
的相对量，在第一修改层会出现一个很大的有限常数。
因此后续实际 inverse/input 证明将显式保留有限 prefix 和
一个例如 $\|X\|\le2^{-262144}$ 的真实标签限制。
上一线性普通源篇给出的 $e^{-33545404}$ regular 输入
比这一量小，但那只是上一候选的线性结果；新候选必须重新
证明标签权、外端 good-set 与实际传播，而且非线性输入
仍须独立闭合。本篇不据此声称完整相对逆或主课题完成。

## 8. 可复跑证据

脚本
`scripts/fourfold_stronger_deep_first_shear_20261113.py`
以精确有理数、符号恒等式和 Arb256 重核实际8193层与全部
单调包络端点、两个真实根、材料/修正门、主谱与新归一化。
报告为
`notes/2026-11-13-R119-stronger-deep-first-shear-budget-v2.json`。
原报告与修改前 proof 字节分别保留为同名 v1 报告和
`notes/2026-11-13-R119-stronger-deep-first-shear-pre-scope-clarification.md`；
此次只明确 canonical 非零模与独立 mean 的范围。
程序不把有限模采样当成无限频率证明；全模与完整 PDE 量词
分别由第3--6节的有序乘积、真实高模能量和统一复球提供。
