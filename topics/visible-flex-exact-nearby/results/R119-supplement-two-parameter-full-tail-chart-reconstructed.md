# R119 续篇：双参数全标签图及真实 regular 线的重建证明

2026-11-13，visible-exact / tail_connector。

**状态：已证明（数学证明的独立重建）。** 本文在云环境失效后，依据已推送的完整前置证明重新写出第47束的结论。它不是原未推证明的逐字副本，也不声称附带原丢失 native。原会话记录的 proof/source/native SHA256 分别为
`be004e06a13a5ac98b57841840df3933df34c51d875a528574fbcf53b7018323`、
`44d568f3d7eaf4403ddefd1cea8ad2246caa1d57470e0c35cffafcd3ad055c12`、
`7822dcf1b53b5cfe82be4360999ae9fdd7eef3ab6cc6e04b3c538c7a0722ae88`。

这些值只标识历史记录，不作为本重建的数值证据。本篇配套的新 Fraction 程序重新验证下列新增有理门；其运行报告须由实际运行生成。

## 1. 结论、同一对象及前置权限

对每个实际下降 quintic 加入
$$
 \log p_\Gamma=\log p_0+\gamma_1\psi_1+\gamma_2\psi_2,
 \qquad
 \psi_s=64z_s^3(1-z_s)^3,
$$
其中 $z_1=8(x-1/4)$、支集 $[1/4,3/8]$，
$z_2=32(x-3/16)$、支集 $[3/16,7/32]$，支集外为0。
每个胞元的两个下降段各有这样一对独立参数。
所有参数共同取复盒
$$
 |\gamma_1|<2^{-15},\qquad|\gamma_2|<2^{-29},
 \tag{U.1}
$$
实几何盒为其半径的一半。本文使用强首剪切候选：
$K_j=64$ 至8192，之后 $K_j=2^{128}$；
$c_j=64$ 至4096，之后 $c_j=16\sqrt2$。
$\delta_j=(2/25)2^{-j}$，
$\eta_j=\delta_j^{3/2}/(4\sqrt2)$，$\alpha=65/64$。
$\mu,\zeta,h,\tau$ 完全采用
[强首剪切全标签篇](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)，特别
$$
 \zeta_j=
 \begin{cases}
 \epsilon\delta_j^{39/4},&j\le8192,\\
 \epsilon\delta_{8192}^{-485/4}\delta_j^{131},&j>8192.
 \end{cases}
$$
两个全局因子 $\delta_{4096}^{-3/2}$ 和
$\delta_{8192}^{-485/4}$ 始终保留。

本篇证明在这个**新双参数对象**上
$$
 \|\mathcal G_\Gamma\|<2^{16},\quad
 \|\mathcal H_\Gamma\|<9,\quad
 \|X_\Gamma(a)\|_{\mathcal X_\beta}<16\|a\|_\beta,
 \quad \|a\|_\beta<1/64,\quad\beta\ge0.                 \tag{U.2}
$$
这里 $\mathcal X_\beta$ 是先逐 Fourier 模取径向上确界再求
$\ell^1$ 和的真实两行标签范数。所有高模、完整 holonomy mean、
两端高度/通量与唯一整体高度常数均在解图内。

每个固定实参数可用新的实际第四方向重调有限 connector，再重新选择外双 bump 好参数。所得真实 regular 线满足
$$
 \lambda_4=-4\omega_*,
 \qquad
 |\lambda_m+m\omega_*|
 <2^{41}m\omega_*e^{-2mL},
 \quad m\in4\mathbb N,\quad L=\omega_*B.                \tag{U.3}
$$
因此
$$
 q_m(R)=-\frac{\lambda_m}{m\omega_*\sqrt{1+w_R^2}},
 \qquad q_4(R)=\frac1{\sqrt{1+w_R^2}}.                 \tag{U.4}
$$
这是 actual 新尾的结论，不把旧 $q$ 向量未经证明转授。全非线性外匹配
$F(a,f_*)=0$、内部同权 Green 及非径向完整次相位反项仍未由本文证明。

## 2. 新复参数盒的全部 profile 门

两个支集相离；各 bump 的0、1、2阶端 jet 准确为0。
第一支集上沿用原界
$$
 1<S'<3375/2048,\quad |S''|\le45/8,\quad
 |\psi_1'|\le96,\quad|\psi_1''|\le6144.
$$
第二支集上 $S''>0$，直接算两个端点得
$$
 1/2<S'<1,\quad |S''|<29/5,\quad
 |\psi_2'|\le384,\quad|\psi_2''|\le98304.                \tag{U.5}
$$
真实全层 $\Delta>80$。故在整个复盒，$|p_\Gamma|$
严格按原方向单调，且逐点有
$$
 |(\log p_\Gamma)_x|<(15/8)\Delta,\qquad
 |(\log p_\Gamma)_{xx}|<6\Delta.                       \tag{U.6}
$$
例如第二支集只需
$384\,2^{-29}<80/2$、
$80+384\,2^{-29}<15\cdot80/8$、
$(29/5)80+98304\,2^{-29}<6\cdot80$。
第一支集为原相同有理门。支集外准确未变。

各胞元有两个下降段，完整复 log 变差的新增量至多
$4(2^{-15}+2^{-29})$。这仍在原
$6|\log\delta|+2\log128$（深段改成同一原 $2\log(2K)$）
上界之内：旧常数 $c_R<5$，而 $2\log128>28/3$。
不把复变差当作实变差。

由于支集相离，逐点 $|\log(p_\Gamma/p_0)|\le2^{-15}$，
不是两个半径之和。原统一图的材料积分乘 $\delta^2$ 后小于10；
新增第二 bump 的变差费小于 $8\,2^{-29}$，故完整
$$
 \int(1+|\lambda_\Gamma|)(1+|p_\Gamma|^{-2})\,dy
 <64\delta^{-2},\qquad
 \lambda_\Gamma=(\log p_\Gamma)_y-7/\sqrt{12}.           \tag{U.7}
$$
保持。所有实际端值、三大平台与六小段长度未变。
第二 bump 的 $k$ 阶 jet 对第一同形 bump 的比例是 $4^k$；
$0\le k\le4$ 时新增复参数 jet 比原盒上界不超过
$4^k2^{-29}/2^{-15}\le1/64$。
根所在的上升 quintic、两侧正型区及其完整 raw 密度准确未改。

## 3. 真矩阵和完整局部非线性图

[原统一参数篇](R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md)
§§3–4的复杂参数 Dyson/Gauss 证明只使用：
模长单调、完整有序面积上界、(U.6) 的各段 $m_*$、
(U.7) 的材料积分以及同一正平方根邻域。这些门已逐项保持。
它不要求复面积有符号，也不除可能相消的面积。

因此129–8192层的 actual 低窗误差仍为
$32768m^8\sqrt{\delta_j}$；新强首剪切深段仍为
$2^{272}m^8\sqrt{\delta_j}$。这些式子只用于
$m\in4\mathbb Z\setminus\{0\}$，mean 另由完整小根恢复。
整个新真实低窗仍为
$$
 \widehat M_j=
 \begin{cases}
 \min(2^{-5/4}\delta_j^{-1/8},\,2^{-40}\delta_{8193}^{-1/8}),
       &j\le8192,\\
 2^{-40}\delta_j^{-1/8},&j>8192 .
 \end{cases}                                             \tag{U.8}
$$
窗外使用随 $\Gamma$ 更新的**真实矩阵**，以原粗标量能量得
$\|A_{m,j,\Gamma}\|<1/4$。不将其替换为理想矩阵。
因为大平台准确未动，参考特征基、两个真实接缝消元与标签层均未变。

规范后的低窗扰动为
$$
 e_j\le
 \begin{cases}
 32768\,2^{-39/4}\sqrt{\delta_j}(8/(eh_j))^8,&j\le8192,\\
 2^{141}\sqrt{\delta_j}(8/(eh_j))^8,&j>8192.
 \end{cases}                                             \tag{U.9}
$$
原强首剪切篇完整全模/全层账给
$2^{15}\sup_j e_j<1/32$，因此同一 Neumann 构造得前两条(U.2)。
前篇非线性局部球、完整 mean 归一化及强 Taylor 卷积同样只用
已保持的门，故
$$
 2^{16}K_*<2^{-52},\qquad
 X=\mathcal H_\Gamma a+\mathcal G_\Gamma\mathscr R_\Gamma(X)
                                                               \tag{U.10}
$$
在 $\|a\|_\beta<1/64$、单位 $\mathcal X_\beta$ 球中收缩，给最后一条(U.2)。

这不是仅端口的有限截断解：每个 local map 是原完整
Galerkin/Volterra 校正后的零残差角向解；实际两迹匹配恢复二阶高度迹。
完整 mean 仍在同一 holonomy-one 小根上，保留一次高度积分。

所有有限流、均值小根和强 Neumann 级数在复盒上一致全纯。
令
$$
 \|\dot\Gamma\|_{\mathcal P}
 =\max(2^{16}\|\dot\gamma_1\|_\infty,
       2^{30}\|\dot\gamma_2\|_\infty).
$$
实盒距复边界至少一个单位方向半径；Banach Cauchy 公式给
$$
 \|D_\Gamma X_\Gamma(a)[\dot\Gamma]\|_{\mathcal X_\beta}
 <32\|a\|_\beta\|\dot\Gamma\|_{\mathcal P}.               \tag{U.11}
$$
乘积拓扑连续性使用(U.9)深层规范包络
$O(\delta_j^{15/32})\to0$、真实高块包络和规范余项的正幂。
不能用未规范的 $m^8\sqrt\delta$ 在全低窗直接取上确界。
强首剪切篇的完整物理二阶包络及两个全局逆幂均未改，
故同一逐层极限给真 $C^2$ 平盘接合、参数乘积拓扑 $C^2$ 连续性。

## 4. ordinary、完整 weak 与 mean 的准确单位

本节固定 $\Gamma$，不把 metric-change 列误当齐次 Jacobi 列。
令 $t=\log r$、$y=\sqrt{12}\,t$、$w=\mu_jp_\Gamma/r^7$，
$\mathfrak m=w/r$，采用真实 raw 高度 $H$ 的源约定
$$
 \partial_t(\mathfrak m H_t)+
 \partial_\theta(\mathfrak m A H_\theta)
 =s-\partial_tF^t-\partial_\theta F^\theta .
$$
ordinary $s=w^2e$。canonical 两态定义及全源准确为
$$
 W_1=\nu_m H/r^4,\quad
 W_2=\frac{p_\Gamma}{\sqrt{12}r^4}(H_t-m^2H),\quad
 W^{\rm total}=W+(0,cF^t),
$$
$$
 c=\frac{r^4}{\sqrt{12}\mu_j},\quad q=\frac{r^4}{12\mu_j},
 \qquad
 J=\binom{-\nu_mcF^t/p_\Gamma}
             {q(s-imF^\theta+m^2F^t)}.                  \tag{U.12}
$$
ordinary 第二行是
$N=\mu_jp_\Gamma^2e/(12r^{10})$。完整 weak 合同没有
$\partial_tF^t$ 费用。强源空间和已证 source Green 使用 actual
$p_\Gamma$；参数微分时它的分子/分母变化必须保留。

零模为
$$
 \pi_0(t)=\int_{t_f}^t s_0(\tau)d\tau,\qquad
 H_0(t)=\lambda+
       \int_{t_f}^t\frac r w(\pi_0-F^t_0)d\tau .         \tag{U.13}
$$
只有一个独立 $\lambda$。cut128通量是输出，不能再设为0。
端点 total/bare 差、真实 $F^t$ 两端荷和 holonomy 源全部按同一公式保留。
只有满足原完整源 norm 的输入获得相应界，本文未声称任意粗 weak 源有 bare 端迹。

## 5. 新双参数真正第四线

深处完整实际 Möbius cone 与前篇相同，因此真第四允许线在
cut4096进入 $|s|<1/16$。从4096到128的3968个胞元均为
$c=K=64$，但这里每个矩阵随**两个** bump 更新。其实际误差和行列式为
$$
 B^\infty_4=
 \begin{pmatrix}-1299&325/16\\1235/64&-309/1024\end{pmatrix},
 \quad\det B_{4,j,\Gamma}=1/64,\quad
 \|B_{4,j,\Gamma}-B^\infty_4\|_\infty\le e_j,
 \quad e_j=2^{31}\sqrt{\delta_j}.                        \tag{U.14}
$$
准确 $\sqrt{\delta_{129}}=2^{-64}/5$，故
$e_{129}=2^{-33}/5<2^{-35}$。
在 $|s|\le1/16$，分母模大于1297，像严格在同一盘内，
并且
$$
 |T'_{j,\Gamma}(s)|<\frac1{64\cdot1297^2}<2^{-26}.
$$
理想大线 $s_4$ 满足 $-1/64<s_4<-7/480$，
$|T_{j,\Gamma}(s_4)-s_4|<e_j/1000$。
将3968次真实 map 完整组合，得到
$$
 |s_{128,\Gamma}-s_4|
 <e_{129}/999+\tfrac18\,2^{-26\cdot3968}.               \tag{U.15}
$$
初值差小于 $1/16+1/64<1/8$；误差和的比小于
$2^{-26}/\sqrt2$，故分母999有余量。
这是完整无限尾线，因为深端线与强标签图的唯一性已在前篇证明；
不是把理想深线直接当实际线。

真实物理斜率 $d_4=16+20\sqrt{12}\,s_{128,\Gamma}$。
由 $69<20\sqrt{12}<70$，
$$
 |d_4-d_4^{\rm ideal}|<2^{-38},\qquad14<d_4<15.          \tag{U.16}
$$
在两个实参数方向分别有
$$
 \|D_{\gamma_1}d_4\|<2^{-22},\qquad
 \|D_{\gamma_2}d_4\|<2^{-8}.                            \tag{U.17}
$$
这些是复盒 Cauchy 费用，允许同时改变整个参数序列。
不能引用前篇“仅在8193以后改变profile”才有的
$2^{-193532}$ 新旧差，因为当前第二 bump 在浅层也存在。

## 6. 实际停止点、尺度、全 mean 及 metric 列

令新真实目标
$R_*(\Gamma)=(1-d_4)/(16-d_4)$。
采用[原重调 connector 证明](R119-supplement-retuned-fourth-connector-and-common-bumps.md)
的准确最后短流 $\Phi$，先取唯一
$\Phi(R_e^{\rm in})=R_*(\Gamma)$，再设
$$
 \ell(\Gamma)=
 \log\frac{P_e(1+16P_b)}{P_b(1+16P_e)},
 \qquad P_e=-R_e^{\rm in},\quad P_b=-R_b .               \tag{U.18}
$$
原完整盒 $14<d_4<15$ 已保持，所以同一实际流给
$0<\ell<\log(9/8)$、$|\ell_{R_*}|<1/512$。
由 $|R_*'|<15$ 和(U.16)，相对于该强尾零参数值，
$|\ell(\Gamma)-\ell(0)|<2^{-41}$。
有限流和停止式的分母均有原非零余量，故参数全纯性保持。

$q=-1$ 主段上 $H_v/H=1$、$\omega_v/\omega=-1$，
所以 $H\omega$ 准确不变；其后固定过渡也给同一个乘子。
因此
$$
 \epsilon_{\rm tail}(\Gamma)=\epsilon_{\rm tail}(0),\qquad
 \rho(\Gamma)=\rho(0)e^{-[\ell(\Gamma)-\ell(0)]}.         \tag{U.19}
$$
实际相对四态 $P,K,U,V$、角图及完整两个 phase
$\Theta,b,\beta$ 在这个整体等比缩放下不变。
它是构造一个新最终公共度量的步骤，不是固定旧度量中的齐次变化。

固定物理 $a$ 时必须使用
$$
 \delta w^{\rm phys}
 =w_\Gamma\left(\sum_i\psi_i\delta\gamma_i+
                         A_\Gamma\delta\ell\right),
 \qquad
 \delta g_{aa}=2w_\Gamma\,\delta w^{\rm phys}.           \tag{U.20}
$$
同时
$Z_\Gamma(a)=Z_e(\Gamma)-\int_{a_e(\Gamma)}^a w_\Gamma^{\rm phys}$，
故
$\delta Z=\delta Z_e+w_e\delta a_e-\int\delta w^{\rm phys}$。
connector的长度变化源、移动切口端项、唯一 mean 平移均保留。

原有限几何盒及强尾二阶衰减仍成立。新增实参数费由
$e^{2(2^{-16}+2^{-30})}(1+8\cdot2^{-16}+32\cdot2^{-30})
9375/131072<1/8$
控制；该有理验证可用 $e^x\le(1-x)^{-1}$，不依赖浮点指数。

## 7. 新对象上的共同外好集及真实 lambda

(U.18)使 $u=T$ 处新实际第四线恰为
$\operatorname{span}(1,-\omega_*)$。
外双 bump的背景、其右端状态及所有二 jets 未变，
故保持第四线的唯一曲线 $s=s(\gamma_0t)$
仍是原 R74 的**同一个函数**。
其它频率的非零右线则来自本篇新实际尾，必须重新输入好集证明。

对每个固定实 $\Gamma$，定义新闭好集
$$
 G_\Gamma=\{t\in[0,1]:
 |\sin\angle(\Lambda_m(B;\Gamma,t),(1,\omega_*))|
 \ge2^{-39}\ \text{对所有 }m\in4\mathbb N\}.
$$
原R11附录A的全模坏集证明只使用：
非零右线与外bump参数独立、相同第四右线及保持曲线、相同实际正区盒。
这些假设已逐项满足，因此
$|G_\Gamma|\ge1-83/16384>0$。
可逐点取一个 $t_\Gamma$；不声称最小元随任意 $\Gamma$ 连续。

此时 $[0,B]$ 的指数段完全相同。准确回传而非近似得
$$
 |c_+/c_-|\le2^{39}e^{-2mL},\quad
 |\lambda_m+m\omega_*|<2^{41}m\omega_*e^{-2mL},
 \quad \lambda_4=-4\omega_* .                           \tag{U.21}
$$
真实 grounded矩阵仍是
$v=A_0y-4y'/m^2$、$p=-y+4y'/A_0$，
$A_0=4\omega_*+a_*^2/z_*$。故
$$
 \gamma_m=\frac{1-4\lambda_m/A_0}{A_0-4\lambda_m/m^2},
 \qquad m/7<\gamma_m<m/5,\qquad\gamma_0=0.              \tag{U.22}
$$
完整非mean grounded两迹、raw两迹和参数项不能互换后漏掉高度剪切。
物理曲率接口准确给(U.4)，从而原较宽
$2^{42}e^{-2mL}$盒可在这个新候选上重新实例化。
ordinary源的 affine Robin 两端项仍必须单独使用(U.12)及完整W​​ronskian；
齐次(U.21)不消除它们。

## 8. 本篇关闭的缺口与仍须解的方程

本篇关闭“第二 compact bump后是否仍有完整标签图、真实第四线、
有限connector/尺度以及全频regular选择”的对象身份缺口。
完整新尾的外匹配仍是
$$
 k_B^{\Gamma,t}(a)+\mathsf C_L f_B^{\Gamma,t}(a)
 -\mathsf S_L f_*
 -\mathcal E_D(f_B^{\Gamma,t}(a),f_*)=0.                 \tag{U.23}
$$
保留全部非zero $f_B$ 混合项、mean斜率小根、普通/weak源、
移动参数列以及唯一平均高度。径向参考的高块算术逆不等于完整低Schur，
而内部标签图也不等于 arbitrary共同cut高输入图。
若最终联合参数选择在标签相位轨道上不变，则同一个
$\Gamma,t,\ell,\rho$适用于整轨道；本文未据此提前授予最终匹配点存在。

## 9. 重建程序与可追溯依赖

运行（从仓库根）：
```
python topics/visible-flex-exact-nearby/scripts/fourfold_two_parameter_tail_chart_reconstructed_20261113.py --output topics/visible-flex-exact-nearby/notes/2026-11-13-R119-two-parameter-tail-chart-reconstructed-budget.json
```

仅需 Python 标准库。程序使用 Fraction 对新增有理门逐项验证，
并记录本证明、程序及真实前置文件的当前 SHA256。
它不会创建或复制原丢失 native，也不把前置证明的无限量词改成有限数值样本。
实际输出的 passed/failed 门和新哈希以真正运行报告为准。
