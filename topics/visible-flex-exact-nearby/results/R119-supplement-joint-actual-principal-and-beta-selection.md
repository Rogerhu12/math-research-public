# R119 续篇：真实主角与非径向首相位的无限联立参数选择

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在已经选定的两参数强尾候选上，全部真实非径向
principal return 和第49束识别的真实首相位可以同时保持原来的固定
\((\omega_i,\beta_i^0)\)。选择对完整标签联合全纯、在实标签上为实，
并且在标签的角平移轨道上准确不变。两个参数都由同一次无限联立
收缩确定，没有先冻结一个深层再修改另一个层。

全标签、第四停止、外端两个 bump、mean 与实际帽—长段外匹配 map
继续保留。这个结果消除了先前“只有径向 \(\beta\)”的缺口；它**不**
把已付主模型的小除数或逐分量余项直接称作完整网络 inverse。

## 1. 固定同一候选和两个真实目标

采用
[完整两参数算术](R119-supplement-actual-two-parameter-complete-phase-arithmetic.md)
已经一次选定的径向 \(\Gamma^0=(\gamma_{1,i}^0,\gamma_{2,i}^0)\)。
对每个完整内部负分量 \(i\)，目标满足
\[
 |e^{in\omega_i}-1|>{\kappa_i\over4096|n|},\qquad
 |1+e^{i(n\omega_i+\beta_i^0/n)}|>{1\over128N_i|n|},
 \quad n\ne0.                                             \tag{J.1}
\]
这些数从此固定，不随标签重新择取好集最小值。实际基点有
\[
 |\gamma_{1,i}^0|<2^{-24}+2^{-86},\qquad
 |\gamma_{2,i}^0|<2^{-86}.                                 \tag{J.2}
\]
\(\kappa_i,N_i\) 以及第二式的物理频率换算均与该篇相同。

由
[两参数全尾重建](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)，
完整局部 map、全标签图、真实第四线、停止长度与 raw 两迹在
\[
 |\gamma_{1,i}|<2^{-15},\qquad|\gamma_{2,i}|<2^{-29}         \tag{J.3}
\]
联合全纯。最外截断分量 \((129,2)\) 的两个内部参数仍固定为0；
该分量以及 finite connector/regular 行保留在完整外匹配方程。

写
\[
 A_*=2^{-262148},\quad \|a\|_{224}<A_*,
 \quad \mathcal X(a)=16\|a\|_{224}\le2^{-262144}.             \tag{J.4}
\]
任何下面使用的复参数点都满足
\(\|X(a,\Gamma)\|_{\mathcal X_{224}}<\mathcal X(a)\)。
实际逐层状态界 \(n_i=4N_j^\#\|X\|\)、\(N_j\) 以及两个全局逆幂，
均采用第49束，不以更深的最终正幂替代有限前缀。

## 2. 保持径向主角的复曲线，含准确局部逆域

令
\[
 \mathcal B_i=\sqrt{12}\Delta_i/\eta_j,\quad
 T_s=\sqrt{\mathcal B_i}\,\partial_{\gamma_s}\Theta_i,\quad
 B_s=\mathcal B_i^{-1/2}\partial_{\gamma_s}\mathfrak b_i .
\]
第43/45束的完整有向积分给真实实盒中
\[
 .085<T_1<.087,\quad .058<T_2<.061,\quad
 -.023<B_1<-.021,\quad -.010<B_2<-.008,
\]
\[
 \det\begin{pmatrix}T_1&T_2\\B_1&B_2\end{pmatrix}>2^{-11},
 \qquad {\det\mathcal M\over T_1}>2^{-8}.                  \tag{J.5}
\]
这里 \(\mathfrak b_i\) 已由第45束和
[真实非径向首密度相位](R119-supplement-actual-nonradial-first-density-phase.md)
识别为完整 PDE 的系数，不是仅严格内部的形式积分。

为明确复逆所需余量，直接使用原准确无量纲 integrand。
在两个支集上，整个所需复域都有
\[
 |u|>\tfrac12,\quad |u_x|<7,\quad |u_{xx}|<64,\quad
 d=1/\Delta<1/80,\quad e_{\mathcal B}=1/\mathcal B<1.
\]
这些界由 \(u=S'+7/\mathcal B-d\gamma_s\psi_s'\) 给出：
两个支集的 \(S'\) 最小值大于 \(1/2\)，\(|S''|<6\)，
\(|S'''|<25\)，而参数项按 (J.3) 直接支付。
\(\psi_1',\psi_2'\) 分别至多 \(96,384\)，
\(\psi_1'',\psi_2''\) 分别至多 \(6144,98304\)；
所需三阶导均小于 \(2^{24}\)。

两个支集相离，故 \(T_1\) 只依赖 \(\gamma_1\)，\(T_2\) 只依赖
\(\gamma_2\)。准确微分
\[
 T_s=\tfrac12\int\psi_s u_xu^{-3/2}dx
\]
给
\[
 |\partial_{\gamma_1}T_1|<32,\qquad
 |\partial_{\gamma_2}T_2|<64.                              \tag{J.6}
\]
例如第一式不超过
\[
 {1\over2\cdot80\cdot8}
 [6144\cdot3+\tfrac32\,7\cdot96\cdot6]=153/8<32 ;
\]
第二式相同计算得 \(2493/40<64\)。
这里使用 \(u^{-3/2},u^{-5/2}\) 的模分别小于3、6，未对复参数
使用一个仅实序意义的分母比较。

在
\[
 |\gamma_1-\gamma_1^0|<2^{-20},\qquad
 |\gamma_2-\gamma_2^0|<2^{-32}
\]
上，(J.5)--(J.6) 给 \(|T_1|>1/16,\ |T_2|<1/8\)。
第一个变量的积分是单值全纯局部双射，其边界像包含半径
\(2^{-25}\) 的标准化角盘；第二个变量在整个 \(2^{-32}\) 盘产生的
标准化角改动小于 \(2^{-35}\)。用该逆定义真实复曲线
\[
 \Theta_i(\chi_i(s),\gamma_{2,i}^0+s)=\omega_i/4,\qquad
 \chi_i(0)=\gamma_{1,i}^0,\quad |s|<2^{-32}.                \tag{J.7}
\]
它满足
\[
                         |\chi_i'(s)|<2.                 \tag{J.8}
\]
全部曲线有同一个复域，因而组成 \(\ell^\infty\) 参数球上的联合全纯
对角 map；实际全标签解对这些参数仍有全部交叉依赖。

定义真正径向第二行
\[
 f_i(s)={\beta_i(0,\chi_i(s),\gamma_{2,i}^0+s)-\beta_i^0
                                      \over\sqrt{\mathcal B_i}}.
                                                                    \tag{J.9}
\]
由于 \(\beta=-\mathfrak b/2\)，
\[
 f_i'(0)=-\frac12\left(B_2-B_1{T_2\over T_1}\right)
        =-{\det\mathcal M\over2T_1}<-2^{-9}.               \tag{J.10}
\]
原完整 \(B_s\) 公式在上述复域直接给 \(|B_s|<2\)：
第一积分至多 \(399/512\)，第二积分至多 \(3357/25600\)；
较短第二支集只改善第一项。因此 (J.8) 给 \(|f_i'|<3\)。
在 \(|s|\le2^{-33}\)，Cauchy 给
\[
                         |f_i''|<2^{36}.                 \tag{J.11}
\]
特别取 \(r=2^{-256}\)，则
\(|f_i'(s)-f_i'(0)|<2^{-220}\) 于 \(|s|\le r\)。
写 \(f_i(s)=a_i s+R_i(s)\)，用
\(s=z/a_i-R_i(s)/a_i\) 收缩，得到准确全纯逆
\[
 f_i(\varphi_i(z))=z,\quad |z|<2^{-267},\quad
 |\varphi_i'(z)|<2^{10},\quad \varphi_i(0)=0.               \tag{J.12}
\]
这个逆在真实参数坐标中给出，而不是把 \(\beta\) 当作免费独立输入。

## 3. 每个第二参数向量上的真实 principal KAM

现在让完整向量 \(s=(s_i)\) 在 \(\|s\|_\infty<2^{-34}\) 变化。
径向基点用 (J.7)。对每个这样的 \(s\)，在相同真实全标签解上联立
调整全部第一参数，得到
\[
 \gamma_{1,i}^*(a,s),\qquad \gamma_{2,i}=\gamma_{2,i}^0+s_i,
\]
使真实两射线 return 准确共轭到同一 \(\omega_i\)。
这个 KAM 是
[第48束](R119-supplement-actual-finite-Schur-14400-head-and-full-sources.md)
§1 的真正再实例化：第二 bump 不进入
\(\partial_{\gamma_1}\Theta_i\)，所以原第一参数复逆和它的每行尺度保持；
所有非径向误差在 (J.3) 上统一。

使用 \(\gamma_i^{\rm D}=\kappa_i/4096\) 的二阶 Diophantine 形式，
原小除数平方费增加准确的 \(64^2=2^{12}\)，故
\[
 \mu_{\rm KAM}<2^{288}A_*=2^{-261860}<2^{-64}.              \tag{J.13}
\]
原完整参数平均行在当前 \(h_i\) 处评价
\((D_pF_i[q])\circ h_i\)，包括所有 \(p\) 及 \(s\) 的依赖。
先解这一真正无限平均行，再解全部非零 Fourier cohomological 行；
原二次收敛证明确实给
\[
 R_i(a,\gamma_1^*(a,s),\gamma_2^0+s)\circ h_i
          =h_i\circ T_{\omega_i/4}
\]
（此式写在物理角；标准角为 \(x=4\theta\)），并且
\[
 |\gamma_{1,i}^*(a,s)-\chi_i(s)|
 <2^{39}(j+4)\sqrt j\,\delta_j^{-3/4}N_j^\#\mathcal X(a).
                                                                    \tag{J.14}
\]
参数平均行的逐行改动仍由 \(\varepsilon_i/\kappa_i\) 支付；
新的较小 \(\gamma_i^{\rm D}\) 只改角 cohomological 费用，未改变
(J.14) 的参数单位。其证明可直接从
\(|p_i^*|<16\varepsilon_i\|a\|/A_*\) 和真实 \(G_i'\) 读出。

这些真实 \(h_i\)、\(\gamma_1^*\) 对 \((a,s)\) 联合全纯，所有层的
参数列都保留；不是把 \(\gamma_1^*\) 视为只依赖本层 \(s_i\)。

## 4. 真正非径向第二行及完整无限收缩

定义
\[
 E_i(a,s)=
 {\beta_i(a,\gamma_1^*(a,s),\gamma_2^0+s)
       -\beta_i(0,\chi_i(s),\gamma_{2,i}^0+s_i)
                         \over\sqrt{\mathcal B_i}}.       \tag{J.15}
\]
分子第一项是第49束证明的实际非径向完整返回首系数，含两根、
正型双端反射及原固定 \(t\) 端口。第二项仍是实际同一族的径向值。
不能把第一项换成某个固定标签角图中的绝对 Cauchy 误差。

第49束的完整无限层差界给直接非径向部分小于
\(2^{160032}\mathcal X(a)\)。此外实际径向
\[
 \left|\partial_{\gamma_1}{\beta_i(0,\Gamma)\over
                                  \sqrt{\mathcal B_i}}\right|
             =|B_1|/2<1 .
\]
所以 (J.14) 给 principal KAM 所改第一参数的完整首相位费用。
它逐层被第49束的
\(2^{144}(j+5)^3\delta_j^{-17/4}N_j^\#\mathcal X(a)\)
包络严格覆盖。保留全部交叉参数后仍有
\[
 \boxed{\quad
 \sum_i |E_i(a,s)|<2^{160040}\mathcal X(a),
                 \qquad\|s\|_\infty<2^{-34} .
 \quad}                                                     \tag{J.16}
\]
两个全局 inverse 因子及129--8192的全部前缀已在原
\(\sum(K_j^{\rm ref})^2N_j<2^{160000}\) 内支付。

沿任意 \(\|q\|_\infty\le1\) 的复方向，在
\(\|s\|_\infty\le2^{-256}\) 可以使用半径 \(2^{-35}\) 的参数盘。
Banach 空间 Cauchy 直接给整个交叉导数，而不是逐列后忘记求和：
\[
 \|D_s E(a,s)\|_{\ell^\infty\to\ell^\infty}
           <2^{160075}\mathcal X(a).                      \tag{J.17}
\]
要求两真实目标同时成立，准确等价于
\[
 f_i(s_i)+E_i(a,s)=0,\qquad
 s_i=\varphi_i(-E_i(a,s)).                                 \tag{J.18}
\]
在闭 \(\ell^\infty\) 球 \(\|s\|\le2^{-256}\) 上，
(J.4)、(J.12)、(J.16) 给每个输入仍在 \(\varphi_i\) 的真定义域，
并给完整 self-map 界
\[
 \|\varphi(-E(a,s))\|_\infty
 <2^{160050}\mathcal X(a)\le2^{-102094}<2^{-256}.            \tag{J.19}
\]
其 Lipschitz 常数为
\[
 2^{10+160075}\mathcal X(a)
       \le2^{-102059}<\tfrac12.                            \tag{J.20}
\]
故实际无限向量方程有唯一解 \(s^*(a)\)，
\[
 \|s^*(a)\|_\infty<2^{160050}\mathcal X(a).                 \tag{J.21}
\]
这是一次真正的无限 \(\ell^\infty\) 收缩，不是对有限层解后取一个
未经证明的子序列。uniform 收缩及已有联合全纯性给局部联合全纯解，
真实数据的共轭唯一性给实解。

最终定义
\[
 \Gamma_i^*(a)=
 \big(\gamma_{1,i}^*(a,s^*(a)),\
                       \gamma_{2,i}^0+s_i^*(a)\big).       \tag{J.22}
\]
于是对所有完整内部负分量，准确有
\[
 \boxed{\quad
 R_i(a,\Gamma^*(a))\circ K_i
       =K_i\circ T_{\omega_i/4},\qquad
 \beta_i(a,\Gamma^*(a))=\beta_i^0 .
 \quad}                                                     \tag{J.23}
\]
这里 \(K_i\) 是实际物理角图；本节没有用一个径向导数去替代非径向行。

## 5. 同一最终度量、相位等变和原点一阶

对标签角平移
\(T_\varphi a=(e^{im\varphi}a_m)_m\)，全标签解及真实 principal 流只
作相同物理角平移。第49束 \(\kappa\,dt\,d\theta\) 的有限部积分也
准确不变；两根 canonical cuts 随同一图平移。因此整个 (J.15) 的
标量行保持不变。第一 KAM 的 mean-zero 规范、完整参数平均行与
cohomological 逆同样和该平移交换。两次唯一性给
\[
                     \Gamma^*(T_\varphi a)=\Gamma^*(a).  \tag{J.24}
\]
固定任何最终标签后，整个相位轨道因此共用一个实际固定目标度量，
而非在一个声称固定目标的 Newton 步内暗换度量。

在 \(a=0\) 处，\(E=0,s^*=0,\Gamma^*(0)=\Gamma^0\)。
\(D_a\Gamma^*(0)\) 是连续线性且对所有角平移不变；标签仅含
\(m\in4\mathbb Z\setminus0\)，故它对每个 Fourier 基向量为0。
有限支撑向量在标签 \(\ell^1\) 中稠密，所以
\[
                             D_a\Gamma^*(0)=0.             \tag{J.25}
\]
这个论证保留了真实 mean 方程；没有因为删掉 mean 才得到零平均。
它说明新的双参数选择不改变原点固定度量的 Jacobi 方向。

原 profile 的 \(C^2\) 平端、uniform 标签图及物理系数的参数连续性
在整个 (J.3) 已证明。新选择落在该盒内；因此它定义同一个真实无限尾，
不是仅有任意有限层的构造。

## 6. 第四线、两个外 bump 和真正全匹配 map

每个 \(\Gamma^*(a)\) 都消费该参数下的真实第四允许线，并按原准确
\(q=-1\) 停止公式调整 \(\ell(\Gamma)\)。采用同一
\(H\omega\) 不变量，\(\varepsilon_{\rm tail}\) 准确不变；
\(\rho=\rho_0e^{-(\ell-\ell_0)}\) 的变化保留。
两个外部 bump 的第四保持曲线仍是重建篇的同一条曲线。

第48束在 \(\Gamma^0\) 上已经选定的外参数 \(t_0\) 从此固定。
这里不随 \(\Gamma^*(a)\) 重选逐点好集，也不声称 \(t_0\) 在每个
非zero背景都自动满足原径向好角门。原点 \(D_0\) 使用其真实好角；
非零背景的全逆仍是后续任务。

可以重新在这一**双参数选择后的真实 map**上定义
\[
 \mathcal F_c(a)=
 k(a)-K_{B,\perp}\big(f(a),\Phi(c,f(a))\big).                \tag{J.26}
\]
\(\Phi\) 是同一个已经实际接合的周期帽—长段图，独立物理角
\(f_B=f(a)\)、完整非mean slope、mean 小根和高度积分均保留。
因为整个选择在 (J.3) 全纯，原 uniform raw 迹界可直接复合。
对 \(\beta\in[65536,262144]\)，
\[
 \|a\|_{224}\le e^{-4(\beta-224)}\|a\|_\beta
                  <2^{-5(\beta-224)}\|a\|_\beta .
\]
最后不等式使用 \(e^4>32\)；故 \(\|a\|_\beta<1/64\) 的整个复球
严格落在 (J.4)，不只是在最终极小实标签上定义。

原 complete-composition Cauchy 证明于是给同一显示合同
\[
 s_\beta=\beta-88823/400,\qquad
 \|f(a)\|_{\dot A^2_{s_\beta}}
       +\|k(a)\|_{\dot A^1_{s_\beta}}<2^{-443}\|a\|_\beta,
\]
\[
 \|[D\mathcal F_c(a)-D_0]b\|_{\mathfrak Z_{s_\beta}}
 <2^{-400}(\|a\|_\beta+e^{-7L/4})\|b\|_\beta,               \tag{J.27}
\]
\[
 \|D_0^{-1}g\|_\beta\le\frac1{16}
                              \|g\|_{\mathfrak Z_{\beta+1850}}.
                                                                    \tag{J.28}
\]
这里 \(D_0\) 仍是同一 \(\Gamma^0,t_0\) 的实际全模导数；
(J.25) 给固定度量的一阶身份。
(J.27) 已包含 \(\Gamma^*(a)\)、停止长度及帽反馈的所有导数列：
它由实际复合的完整复球界和 Cauchy 得出，未把新增参数列设为0。

因此第48束的有限 head \(0<|m|\le14400\) 的完整 Schur 收缩可在
本篇新 map 上重新执行，其 \(2^{-96000}\) 费用不变；
94步有效宽度链也可按原公式**重新**执行。旧 map 的标签迭代值不能
未经重做当作新 map 的标签，但完整输入及每步充分门不变。
这仍不把有限94步解释为无限 Newton 收敛。

## 7. 全部 source、mean 与下一真正算子缺口

本篇的 \(\beta\) 是固定度量齐次 Jacobi 首系数；全 \(D_a\mathcal F_c\)
当然还含 \(\dot\Gamma\) 的度量源。材料坐标的完整参数变化为
\[
 \delta\log w=\sum_{i,s}\psi_{i,s}\delta\gamma_{i,s},
\]
而在固定物理半径还须加入 \(A\,\delta\ell\)。参考 mean height 准确为
\[
 Z_\Gamma(a)=Z_e(\Gamma)-\int_{a_e(\Gamma)}^a w_\Gamma(\rho)\,d\rho,
\quad
 \delta Z=\delta Z_e+w_e\delta a_e-\int_{a_e}^a\delta w\,d\rho.
                                                                    \tag{J.29}
\]
独立 \(\lambda\) 和完整 mean flux 不另置0。
actual ordinary/weak density 仍由第49束 (B.30)--(B.32) 变换；
弱源的真实法向端迹仍按原合同另付，没有 \(F^t_t\)。
两端高度和通量始终分别为 \(f\circ K\)、\(K'p\circ K\)；
正型完整双端 DN 的 off-diagonal 不删除。

(J.23) 使实际主模型准确保留 (J.1) 的两个算术门。现尚缺的是：
在真实共同参数和全部源空间中，把第49束的局部 \(4/3\) 阶余项
量化、装配到移动中频 Schur 及内部 Green，并证明真正全
\(H D_0^{-1}EG\) 同权有界和非零背景逆。不能仅由 \(\omega,\beta\)
已固定就把局部余项除以一个未经支付的全网络分母。
完整外方程 \(\mathcal F_c(a)=0\) 因此仍作为当前继续目标保留。

## 8. 严格小预算

新的纯 JavaScript BigInt 程序
\(\texttt{scripts/fourfold_joint_actual_principal_and_beta_selection_20261113.js}\)
核查复曲线、两参数归一导数、真实无限收缩及标签嵌入的全部显示门。
输出为
\(\texttt{notes/2026-11-13-R119-joint-actual-principal-and-beta-selection-budget.json}\)。
这是在仍无终端环境时实际执行的新严格实现；不冒充旧 Python/native。
