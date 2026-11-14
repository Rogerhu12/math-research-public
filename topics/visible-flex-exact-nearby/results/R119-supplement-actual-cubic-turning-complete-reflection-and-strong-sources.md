# R119 续篇：真实三阶负转折的全频反射、截断通量极限及完整强源

2026-11-14，visible-exact / tail_connector。

**状态：解析证明。** 固定停止的实际 connector 不作任何修改。
本篇把其最后 $q=-1\to-8$ quintic 与已经证明的整个非负
$C\to B$ 段接起来，在真实 cut128 得到一个完整 $L^2$ 波反射。
它包括所有 Fourier 模、当前非径向卷积和两个 mean 状态。

证明不把有限截断的酉性直接传给弱极限。三阶端点的反向能量给
$H_C\in H^{-1/8}$；完整正区 DN 的角交换子和体区的一阶交换子
共同证明极限没有丢失虚通量。随后才由范数相等得到强极限与满射。

该结论的外端条件是给定原 $B$ 高度；齐次反射取该高度为零。
本文另给真实强 ordinary/weak 源和端荷的仿射映射。
它不将 cut128 认作开放网络的 $e_X$，不把所得反射本身称作最终
returned 方程可逆，也不授任意原 $L^2$ 端荷一个未付的角增益。

## 1. 不同端点、实际方向与三阶退化

沿用
[实际非负 connector 两端定理](R119-supplement-actual-nonnegative-connector-complete-two-port-and-weak-sources.md)
(E.1)--(E.35)。$C$ 是最后 $q=-1$ 主平台的内端；
$B$ 是原完整双 bump 外端；$D$ 在本文专指真实 cut128。
$e_X$ 是未完整分量 $(129,2)$ 的另一端，仍不同于这三点。

从 $C$ 向内取
$$
 s=\log(r_C/r),\qquad 0\le s\le\eta,\qquad
 \eta=2^{-24}.
 \tag{T.1}
$$
[R11](R11-matched-mode-four-physical-tail-connector.md) (4.1)、
§5 的固定最后 quintic 准确给
$$
 Q(s)=7S(s/\eta),\qquad S(x)=10x^3-15x^4+6x^5,
$$
$$
 Q(0)=0,\quad Q(\eta)=7,\quad Q'\ge0,\quad
 Q'(s)\ge32s^2/\eta^3\quad(0\le s\le\eta/2).
 \tag{T.2}
$$
后一式由 $S'(x)=30x^2(1-x)^2$ 得到。
因此该根是三阶退化；简单 Airy 根的初值归一不能直接代入。

原向外通量为 $\pi$，向内通量是 $\pi_s=-\pi$。
令 $\widetilde d=-d$，解实际漂移流
$$
 \Phi_s=-\widetilde d(s,\Phi),\qquad \Phi(0,\theta)=\theta,
 \qquad j=\Phi_\theta.
$$
置 $\mu_*=\mu_0(C)$，保持准确的 $\mu_0=w/r=1/(4\omega)$，
并定义
$$
 H=h\circ\Phi,\quad P={j(\pi_s\circ\Phi)\over\mu_*},\quad
 A={(\mu\circ\Phi)j\over\mu_*},\quad
 C_1={c\circ\Phi\over\mu_*j},\quad a=A^{-1}.
 \tag{T.3}
$$
$C_1$ 是系数，$C$ 是端点，二者不混用。齐次方程准确为
$$
 H_s=aP,\qquad P_s=Q\partial_\theta(C_1H_\theta).
 \tag{T.4}
$$
这些是完整物理方程的 Piola 变换，不是逐模模型。

原
[固定停止完整源定理](R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md)
(D.16) 的 $2^{-447}X_\beta$ 与三单位以上角余宽，及
[实际 Hamiltonian 恒等式](R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md)
(J.1)--(J.8)、(J.17)，给当前全实标签球上
$$
 {1\over4}<A,C_1,a<4,\qquad
 |a_s|\le32a,\quad |(C_1)_s|\le32C_1,
 \tag{T.5}
$$
$$
 \sum_{\ell\in4\mathbb Z}(1+|\ell|)^6
 \left(|\widehat {a-a_0}(\ell)|+
       |\widehat {C_1-C_{1,0}}(\ell)|\right)<2^{80}n<2^{-360}.
 \tag{T.6}
$$
这里 $n<2^{-440}$，$a_0,C_{1,0}$ 是同一 $s$ 上的径向量。
说明这些常数的来源：$\partial_s\log\mu_0=Q+1\le8$，
整个短段的径向比小于 $e^{8\eta}<2$。商法则只用
$J/w=1+K+EP_\theta$、$D-1$ 和其角导；原三单位余宽补六阶
角导的阶乘小于 $2^{16}$。倒数、平方根及流的两个变分方程
各在半径 $1/8$ 的同一绝对级数内计算，连同全部分量可用
$2^{80}n$。径向导数用 (J.1)，只含 $Q$，不含 $Q'$；
径向部分的 8 和这些小项由 32 覆盖。
这同时解释为什么没有在 (T.5) 中误收 $\eta^{-1}$。

## 2. 相邻完整正区给出的同一个边界图

齐次 $B$ 高度为零时，(E.17)--(E.19) 的真实 DN 给
$$
 P(0)=\mathcal N H(0),\qquad
 \mathcal N=\mu_*^{-1}\mathcal N_{CC}.
 \tag{T.7}
$$
正号来自 $C$ 端的正区外法向通量 $-\pi=\pi_s$。
$\mathcal N$ 是完整自伴算子；没有删除 mean 或非对角 Fourier 项。
原 (E.1)、$2^{-363}<\mu_*<1$ 给其有限的正上下界。

还需实付它的角正则性。对于实角平移 $\tau$，同时平移
(E.10) 的两个完整系数，仍取外端高度零。其 DN 恰是
$e^{\tau\partial_\theta}\mathcal N e^{-\tau\partial_\theta}$。
系数在 $|\operatorname{Im}\tau|<1/4$ 内解析；
除径向实部分外的相对变化由原 $2^{80}n$ 支付。
复变分型仍有原能量至少一半的实部，原零平台 lift 仍有效。
对 lift 作一次复 Lax--Milgram 反演，给
$$
 \|\mathcal N(\tau)\|_{L^2\to L^2}<2^{379}
 \quad (|\tau|<1/4).
 \tag{T.8}
$$
例如未除 $\mu_*$ 的复 DN 可用 $2^{16}$：
lift 能量小于16，修正后的完整解能量小于128，复型连续常数小于2。
再除 $\mu_*>2^{-363}$ 正好给显示数。

令 $D_\theta=-i\partial_\theta$。Cauchy 估计逐项给
$$
 \|\operatorname{ad}_{D_\theta}^{\,k}\mathcal N\|_{2\to2}
 \le k!\,4^k2^{379},\qquad 0\le k\le4.
 \tag{T.9}
$$
这是真实完整端口算子的四个交换子，不只是形式阶数。
在 Fourier 基中取矩阵元，并同时使用 $k=0,4$，得到
$$
 |\mathcal N_{mn}|
 \le {2^{400}\over(1+|m-n|)^4}.
 \tag{T.10}
$$
因而它在 $H^s$ 上有有界延拓，$|s|\le1$，可统一用 $2^{416}$。
这里使用
$\langle m\rangle^s/\langle n\rangle^s
 \le2(1+|m-n|)^{|s|}$ 及绝对行、列 Schur 和。
下文的负阶边界图就是这个唯一延拓。

## 3. 有限截断只用于构造，尚不从它直接取酉极限

置 $\Lambda=(1-\partial_\theta^2)^{1/2}$，
$\Pi_L$ 为 $|m|\le L$ 的完整正交截断，包含 mean。
压缩 (T.4) 的两个完整系数和 (T.7) 的完整 $\mathcal N$。
对 $D$ 端定义
$$
 x=\Lambda^{1/2}H(\eta),\quad y=\Lambda^{-1/2}P(\eta),
 \qquad \alpha=x+iy,\quad\beta=x-iy.
 \tag{T.11}
$$
有限维 Green 恒等式给
$$
 \operatorname{Im}\langle P(\eta),H(\eta)\rangle
 =\operatorname{Im}\langle \Pi_L\mathcal N\Pi_LH(0),H(0)\rangle=0.
$$
若 $\alpha=0$，则 $\beta=0$，于是 $D$ 端两个状态都为零，
有限维常微分方程的唯一性给整个解为零。因此每个完整有限边界
系统确实可解；其 $\alpha\mapsto\beta$ 是酉矩阵。
这一论证不需要任何频率特定分母，也没有隐藏的零输入外部解。

以下证明这些有限解在原无限空间中的同一极限保通量。
在此之前，不能从酉矩阵的弱收敛推出酉算子。

## 4. 同一完整 Galerkin 解的反向半阶能量

记
$$
 v=\Lambda^{-1/2}H,\qquad w=\Lambda^{-1/2}P,\qquad
 \mathcal R_b=[\Lambda^{-1/2},M_b]\Lambda^{1/2}.
$$
直接逐 Fourier 项有
$$
 \|\mathcal R_b:L^2\to H^1\|
 \le\sum_\ell|\ell|\,|\widehat b(\ell)|.
 \tag{T.12}
$$
事实上矩阵比满足
$\langle m\rangle
 |\sqrt{\langle n\rangle/\langle m\rangle}-1|
 \le|m-n|$。所有 $\Pi_L$ 与 $\Lambda,\partial_\theta$ 对易，
所以同一界对压缩系统成立。

取真实能量
$$
 E(s)=\langle aw,w\rangle+
 Q\langle C_1v_\theta,v_\theta\rangle+\|v\|_2^2.
 \tag{T.13}
$$
前两项的主交叉项准确抵消，包括压缩投影的原次序。
余项来自 $\mathcal R_a,\mathcal R_{C_1}$、两个径向系数导数，
以及最后的 $\|v\|_2^2$。由 (T.5)、(T.6)、(T.12)，
$$
 E'(s)\ge {Q'(s)\over4}\|v_\theta\|_2^2-2^{10}E(s).
 \tag{T.14}
$$
例如额外下行项为
$Q\partial_\theta\mathcal R_{C_1}\partial_\theta v$，
其 $L^2$ 范数不超过
$Q\,2^{-360}\|v_\theta\|_2$；上行梯度余项不超过
$2^{-360}\|w\|_2$。两者只付 $\sqrt Q$，无额外频率因子。

由于 $2^{10}\eta=2^{-14}$，
$$
 \sup_{0\le s\le\eta}E(s)<2E(\eta),\qquad
 \int_0^\eta Q'\|v_\theta\|_2^2\,ds<8E(\eta).
 \tag{T.15}
$$
(T.11) 及有限酉性给 $E(\eta)\le32\|\alpha\|_2^2$。
于是可同时采用
$$
 \|H(s)\|_{H^{-1/2}}\le8\|\alpha\|_2,\qquad
 \|P(s)\|_{H^{-1/2}}\le16\|\alpha\|_2,
$$
$$
 \|H_s(s)\|_{H^{-1/2}}\le80\|\alpha\|_2,\qquad
 \int_0^\eta Q'\|v_\theta\|_2^2\,ds\le256\|\alpha\|_2^2.
 \tag{T.16}
$$
所有常数与 $L$ 无关。能量中的 $\|v\|_2^2$ 正是保留 mean
及零平台高度所需的项。

## 5. 三阶端点的可和负八分之一迹

把非mean 按 $\langle m\rangle\in[N,2N)$ 分成 dyadic 带 $H_N$。
对 $N\ge2$，(T.16) 给
$$
 \int_0^\eta Q'\|H_N(s)\|_2^2\,ds
 \le {512\over N}\|\alpha\|_2^2,\qquad
 \sup_s\|(H_N)_s\|_2\le80\sqrt{2N}\|\alpha\|_2 .
$$
任意 $0<\tau\le\eta/2$，先用
$H_N(0)=H_N(s)-\int_0^s(H_N)_u\,du$，
再在 $[\tau/2,\tau]$ 上平均，并用 (T.2)，得到
$$
 \|H_N(0)\|_2^2
 \le2^{15}\left({\eta^3\over N\tau^3}+N\tau^2\right)
                    \|\alpha\|_2^2.
 \tag{T.17}
$$
取
$\tau=(\eta/2)\min(1,(N\eta)^{-2/5})$。保守地，
$$
 \|H_N(0)\|_2^2\le
 2^{19}\|\alpha\|_2^2
 \begin{cases}
 N^{-1},&N\eta\le1,\\
 \eta^{6/5}N^{1/5},&N\eta\ge1 .
 \end{cases}
 \tag{T.18}
$$
乘 $N^{-1/4}$ 后求 dyadic 和；高带的余幂是 $N^{-1/20}$，
其几何级数小于64。低带与 mean 也可和，因此
$$
 \boxed{\ \|H(0)\|_{H^{-1/8}}<2^{13}\|\alpha\|_2.\ }
 \tag{T.19}
$$
该负阶迹不是最优 Bessel 幅度，但已经严格优于 $H^{-1/2}$。
由 (T.7)、(T.10)，$P(0)$ 也在同一 $H^{-1/8}$。
没有把这个结论改写为 $H_C\in L^2$。

## 6. 边界与体区的真正截断交换子

固定实偶 $C^\infty$ 函数 $\chi$，$0\le\chi\le1$，
在 $[-1,1]$ 为1、在 $[-2,2]$ 外为0，且 $|\chi'|\le4$。
记 $\chi_R=\chi(D_\theta/R)$，$R\ge1$。

由 (T.10)，若 $\chi(m/R)-\chi(n/R)\ne0$，至少一个频率不超过
$2R$，且该差不超过 $4|m-n|/R$。加上两个 $1/8$ 权后，
绝对行列和给
$$
 \|[\chi_R,\mathcal N]:H^{-1/8}\to H^{1/8}\|
 <2^{416}R^{-3/4}\longrightarrow0 .
 \tag{T.20}
$$
所求和的 lag 至少以 $(1+|\ell|)^{-11/4}$ 衰减。
这一步使用同一完整 $\mathcal N$，没有用径向 DN 代替它。

对任一 $b=a,C_1$，另有
$$
 \sup_R\|[\chi_R,M_b]:H^{-1/2}\to H^{1/2}\|
 \le32\sum_\ell(1+|\ell|)^2|\widehat b(\ell)|,
 \tag{T.21}
$$
且对每个固定的 $z\in H^{-1/2}$，
$[\chi_R,M_b]z\to0$ 于 $H^{1/2}$。
逐矩阵项证明：差不为零时一个频率不超过 $2R$，
$\langle m\rangle^{1/2}\langle n\rangle^{1/2}
 |\chi(m/R)-\chi(n/R)|\le32(1+|m-n|)^2$。
先对有限 Fourier 的 $z$ 用系数尾和，再用统一界作稠密逼近，
即得 strong 收敛。此处不声称该交换子范数趋零。

## 7. 真实弱解极限、通量无损及满射

对任意 $\alpha\in L^2$，用 $\Pi_L\alpha$ 作有限输入。
(T.15)--(T.19) 给一致有界子列。$H(0)$ 的 $H^{-1/8}$ 界使其
在 $H^{-1/2}$ 中紧；(T.10) 使同一结论适用于 $P(0)$。
体区中 $H_s$ 在 $H^{-1/2}$ 有界，$P_s$ 在 $H^{-3/2}$ 有界。
先在较弱 Sobolev 空间作时间紧性，再作弱能量极限，得到
满足完整 (T.4)、(T.7)、(T.11) 的解。每个有限测试 Fourier 模的
方程直接通过极限；实际系数没有截为有限频带。

所得解类为
$$
 H\in C_sH^{-1/2},\quad
 P\in L^\infty_sH^{-1/2}\cap C_sH^{-3/2},\quad
 \sqrt Q\,H\in L^\infty_sH^{1/2},\quad
 H(0),P(0)\in H^{-1/8},
 \tag{T.22}
$$
并保留 (T.15)--(T.19)。$D$ 端的 $H^{1/2}\times H^{-1/2}$ 迹
由 (T.11) 的弱极限确定。

对这个固定的极限解，计算
$\operatorname{Im}\langle\chi_RP,\chi_RH\rangle$ 的径向导数。
主项为实数；两个剩余项分别含
$[\chi_R,a]P$ 和 $Q[\chi_R,C_1]H_\theta$。
(T.21) 使它们的积分被
$C(\|P\|_{H^{-1/2}}^2+Q\|H_\theta\|_{H^{-1/2}}^2)$ 控制，
后者由能量可积。对每个固定 $s$ 的 strong 收敛和支配收敛，
给这两个积分趋零。

在 $C$ 端，(T.7) 的自伴性给
$$
 \operatorname{Im}\langle\chi_RP(0),\chi_RH(0)\rangle
 =\operatorname{Im}
   \langle[\chi_R,\mathcal N]H(0),\chi_RH(0)\rangle
 \longrightarrow0
 \tag{T.23}
$$
（按对偶配对解释；整体符号不影响零极限）。
(T.20) 正好支付两个 $H^{-1/8}$ 因子。
在 $D$ 端，$\chi_R$ 在真实 $H^{1/2}\times H^{-1/2}$ 中强收敛。
所以
$$
 \operatorname{Im}\langle P(\eta),H(\eta)\rangle=0,\qquad
 \|\beta\|_2=\|\alpha\|_2.                              \tag{T.24}
$$
有限输出弱收敛，且其范数趋于该极限的范数，故强收敛。

唯一性也已经付清。零输入解由 (T.24) 有零输出，故 $D$ 端两个
Cauchy 数据均零。对任何 $\epsilon>0$，在 $[\epsilon,\eta]$
上 $Q>0$，同一能量的双向 Gronwall 给零解；再用 (T.22) 的
真实端点迹得到 $C$ 数据为零。于是所有子列给同一个解。

最后从任意给定 $\beta$ 出发，在每个有限系统反向指定该输出。
仍是同一真实边界图 (T.7)，且完全相同的能量、迹、通量极限
证明可用。这给每个 $\beta\in L^2$ 一个真实 $\alpha$，所以
$$
 \boxed{\ \mathscr S_D:L^2\longrightarrow L^2,\qquad
          \beta=\mathscr S_D\alpha,\quad
          \mathscr S_D^*\mathscr S_D
          =\mathscr S_D\mathscr S_D^*=I.\ }             \tag{T.25}
$$
这里保留 mean；没有另加“无隐藏 unitary kernel”的假设。

## 8. 普通源、weak 源、端荷与 affine 跳

在同一归一和角图中写
$$
 H_s=aP+f,\qquad
 P_s=Q\partial_\theta(C_1H_\theta)+g_1,\qquad
 P(0)=\mathcal N H(0)+e_C .
 \tag{T.26}
$$
一个明确充分的完整源空间是
$$
 e_C\in H^{1/8},\qquad
 f,g_1\in\mathcal M_s(H^{1/2}),
 \quad
 \mathfrak F=\|e_C\|_{H^{1/8}}+
              \|f\|_{\mathcal M H^{1/2}}+
              \|g_1\|_{\mathcal M H^{1/2}} .
 \tag{T.27}
$$
原强源有足够角导时消费这个空间；任意 $L^2$ 的 $e_C$ 不免费
属于这里。径向测度只取开区间，端点 atom 单独计入边界条件。

对齐次测试解 $Z=(U,V)$，采用第一变量线性的配对，
完整 Green 恒等式是
$$
 [\langle P,U\rangle-\langle H,V\rangle]_0^\eta
 =\int(\langle g_1,U\rangle-\langle f,V\rangle).
 \tag{T.28}
$$
若源解的 $\alpha=0$，则
$$
 \langle\beta,\beta_Z\rangle
 =-2i\left\{\langle e_C,U(0)\rangle+
       \int(\langle g_1,U\rangle-\langle f,V\rangle)\right\}.
 \tag{T.29}
$$
(T.16)、(T.19)、(T.25) 和 Riesz 定理给
$$
 \|\beta_{\rm src}\|_2<2^{15}\mathfrak F,\qquad
 \beta=\mathscr S_D\alpha+\beta_{\rm src}.              \tag{T.30}
$$
有限 Galerkin 的同一 Green 式给相同源界。
反向能量中，$f$ 的增量按
$\|\Lambda^{-1/2}f\|+\sqrt Q\|\partial_\theta\Lambda^{-1/2}f\|$
收费，$g_1$ 按 $\|\Lambda^{-1/2}g_1\|$ 收费；
它们均由 (T.27) 控制。有限维问题用完整 Stieltjes 变分公式；
连续测度部分用能量的变差不等式，每个 atom 用真实两态跳。
这些界只依赖总变差，故由 Fourier 极限得到同一实际源解，
不需要把任意测度假称作有限 atom 的总变差极限。端点迹证明中
$H(s)-H(0)=\int_0^s aP+\int_{[0,s)}f$；
新增 dyadic 项至多为
$N^{-1}\|f\|_{\mathcal M H^{1/2}}^2$，仍可和。
这同时证明 (T.30) 不是只有形式输出而无真实源解。

原向外物理源 $(g,F^t,F^\theta)$ 的准确输入是
$$
 f={a\,j(F^t\circ\Phi)\over\mu_*},\qquad
 g_1={j(g\circ\Phi)-
       \partial_\theta((F^\theta+dF^t)\circ\Phi)\over\mu_*}.
 \tag{T.31}
$$
因此无需 $F^t$ 的径向导数。用原角 $H^{3/2}$ 链式界及
$\mu_*^{-1}<2^{363}$，一个充分的原物理预算是
$$
 \|f\|_{\mathcal M H^{1/2}}+
 \|g_1\|_{\mathcal M H^{1/2}}
 <2^{380}\left(
 \|g\|_{\mathcal M H^{1/2}}+
 \|F^t\|_{\mathcal M H^{3/2}}+
 \|F^\theta\|_{\mathcal M H^{3/2}}\right).
 \tag{T.32}
$$
实际流及逆流的 $C^2$ 小性由 (T.5)--(T.6) 同一变分方程给，
这些乘法和复合费用小于 $2^{16}$，已包含在显示余量中。

内部真正的 affine 跳
$H^+-H^-=a_s,\ P^+-P^-=b_s$
正是 $f=a_s\delta_s,\ g_1=b_s\delta_s$；
它们各按原 $H^{1/2}$ 范数收费，未称作单位 Poisson 输入。
bare 通量需再减去原 $F^t$ 的端点值；若没有该真实迹，
不宣称 bare/total 两种源域相同。

## 9. 原 B 数据、正区源及输出范围

非零 $B$ 高度和相邻整个正区的源产生
$$
 e_C=\mu_*^{-1}\bigl(\mathcal N_{CB}f_B+\ell_C\bigr).
 \tag{T.33}
$$
两个项都必须保留。为给一个无需额外椭圆平滑结论的显式强输入，
可取 $f_B\in H^2$，以及正区 Piola 源
$$
 \mathfrak P_+^{(1)}
 =\|\widetilde g\|_{\mathcal M H^1}
  +\|\widetilde F^t\|_{\mathcal M H^2}
  +\|\widetilde F^\theta\|_{\mathcal M H^2}.
$$
对 (E.25)--(E.33) 作一次真实角平移差分：
一项是相同源算子作用于角导源，另一项是系数平移导数。
后一项由与 (T.8) 相同的复变分反演和 Cauchy 界控制。
原 $2^{400}$ weak 源常数乘这次有限复能量/一阶导费用可用
$2^{420}$；原外端 Poisson 列也在此界内。因此
$$
 \|e_C\|_{H^1}
 <2^{800}\bigl(\|f_B\|_{H^2}+\mathfrak P_+^{(1)}\bigr).
 \tag{T.34}
$$
这里已经除过 $\mu_*$，且 $H^1\hookrightarrow H^{1/8}$。
原强解析标签和源可直接在任意已付正角宽处支付这些有限角导；
本式不增加一个 $e^{c|m|}$ 的未知 Cauchy 因子。

反射的未知输入只假设 $L^2$，所以本证明只给
$H_C\in H^{-1/8}$。正区 Poisson 与 DN 按上述角平移界延拓后，
完整 $B$ 输出至少落在 $H^{-9/8}$，并保留原 $H^2$ 外输入和
全部正区源。这来自 $\Lambda_B^{-1}\mathcal N_{BC}$ 的同一角平移
交换子界及 Fourier Schur 延拓。对应正区场是该 Poisson 算子的
负角阶分布延拓；没有声称粗 $H_C$ 自动具有原有限能量。
这里没有把 $B$ 输出无说明地提升到 (E.17) 的 $H^{-1}$，
也没有将它当成已经支付的最终帽耦合空间。
对本篇的固定 $f_B$ 条件，$B$ 通量并不参与反射构造，
故这个明确的输出损失不影响 (T.25)。

## 10. 物理归一、mean、参数列及尚余接线

(T.11) 使用的是真实流角。原物理 Green pairing 是其 $\mu_*$ 倍；
若需单位物理波，只须把 $\alpha,\beta$ 同时乘 $\sqrt{\mu_*}$。
角回拉对高度用函数 pullback，对通量用完整密度 $j$。
这两个变换及 $\mu_*^{\pm1/2}$ 必须在接 $e_X$ 的根波图时同时
消费，不能把原物理半径切口当成同一个根端口。

准确的平均行仍是
$$
 (P_0)_s=(g_1)_0,\qquad
 (H_0)_s=\langle aP+f\rangle.                          \tag{T.35}
$$
非径向时第二式包含完整非mean乘积。所有压缩和极限包含这个
mean；常高度没有被删掉，两个 mean 状态也没有互相识别。

当前真实 $\Gamma^*$ 两列及全部 compact 参数列，应把它们的
实际 ordinary/weak 源和外端荷逐列代入 (T.26)、(T.31)、(T.33)。
参数不改变固定 connector 系数的情形，并不使其真实输入状态或
由内部传来的 affine 列消失。若允许的新参数确实改变该有限段，
其系数变分源也按同一完整 Green 式收费，不预先置零。

本篇已关闭 cut128 向外的齐次 $L^2$ 波反射存在、唯一、满射和
强源仿射映射。仍需把未完整 $(129,2)$ 的真实
$e_X\to\mathrm{cut128}$ 传播、其当前根图和源归一接上，
并与开放内部逆的 actual returned 条件共同求解。
若最终外帽要求比 $H^{-9/8}$ 更强的 $B$ 输出，还须另外支付
真实跨正区平滑或相应强输入恢复。没有把这些事项包含在
(T.25) 的酉性结论中。
