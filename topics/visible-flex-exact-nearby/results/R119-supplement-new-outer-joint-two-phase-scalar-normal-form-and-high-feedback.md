# R119 续篇：新外两相位的联合选择、固定标量行及完整高反馈

2026-11-14，visible-exact / tail_connector。

**状态：解析证明。** 本篇把新外分量 $o=(129,2)$ 的
真实第二 $\Gamma$ 行加入原无限联合系统，在同一个真实背景上固定全部
principal 与完整 $1/n$ 相位。随后将新外负散射和真实 positive 响应
写入原固定标量表示，给含新增有限行的完整高块。
所有 mean、完整低历史、独立 $C_R$ 与原 ordinary/weak 源继续保留。
该高块仍须与完整中间系统及实际帽约束联立，不能单独当作课题完成。
Hilbert 酉性及强算子门固定真实背景与实控制；参数选择、标量相位和
其导数使用所列复盒中的全纯延拓，不将复背景的算子称为酉。

## 1. 新外相位的实际原点与固定算术目标

使用 [外 principal 的完整无限 KAM](R119-supplement-new-outer-two-root-complete-principal-return-and-joint-KAM.md)
O.1--O.32，以及
[外两根完整强散射与首相位](R119-supplement-new-outer-two-root-strong-scattering-and-complete-first-phase.md)
F.1--F.39，分别记为 O、F。
仍有
$$
 \mathcal I_+=\{(j,k):j\ge129,\ k=1,2\},\quad
 A_*=2^{-262148},\quad \mathcal X=16\|a\|_{224}\le2^{-262144}.
 \tag{J.1}
$$
最终工作球 $\mathcal X\le2^{-8388608}$ 不变。

外行主角 $\omega_o$ 是 O.13 按新完整 $\Theta_o$ 选定的二次目标。
写 $\alpha_o=\omega_o/(2\pi)$，原准确连分数消元给
$$
 A_o\alpha_o^2-B_o\alpha_o+C_o=0,\quad
 B_o^2-4A_oC_o=5,\quad
 1\le A_o<2^{28}\kappa_o^{-2}<2^{291}.
 \tag{J.2}
$$
$A_o,B_o,C_o$ 是同一 primitive 奇整数多项式；
不使用有限主体另一个旋转数的 gap。

在 $\Xi_o=0,\gamma_{2,o}=0$ 时，用真实第一逆实现 $\omega_o$，
所得 $|\gamma_{1,o}^{\rm pre}|<2^{-24}$。
记此时完整 F.31--F.32 的首相位为 $\beta_o^{\rm pre}$。
F.34 真实给出
$$
 B_{*,o}=2^{1024}>|\beta_o^{\rm pre}|+1,\qquad
 N_o=\left\lceil64(A_o+1)(B_{*,o}+1)\right\rceil<2^{1325}.
 \tag{J.3}
$$
这里的完整 $\beta_o^{\rm pre}$ 包含新根与新增平台，未替成旧截断值。

在 $[\beta_o^{\rm pre}-1,\beta_o^{\rm pre}+1]$ 中使用原
[完整相位算术](R119-supplement-actual-two-parameter-complete-phase-arithmetic.md)
Q.7--Q.11 的两个明确坏集：
距 $\pi(2\mathbb Z+1)/(2\sqrt5)$ 小于 $1/64$，
以及对某 $1\le n\le N_o$ 的
$|\beta+\pi n(2n\alpha_o-p)|<1/(64N_o)$，$p$ 为奇整数。
两类总长度至多 $1/8+1/16$，剩余闭好集测度至少 $29/16$。
一次固定其最小实值为 $\beta_o^0$。

同一准确整数范数证明给所有非zero $n$：
$$
 |e^{in\omega_o}-1|>{\kappa_o\over4096|n|},\qquad
 |1+e^{i(n\omega_o+\beta_o^0/n)}|>{1\over128N_o|n|}.
 \tag{J.4}
$$
当 $|n|>N_o$ 时还有更强的、没有 $N_o$ 因子的门
$$
 |1+e^{i(n\omega_o+\beta_o^0/n)}|^{-1}
                                      <2^{10}\langle4n\rangle .
 \tag{J.5}
$$
其证明仍是
$Q=A_op^2-B_op(2n)+C_o(2n)^2\in2\mathbb Z+1$，
$Q=A_o\varepsilon^2-\sigma\sqrt5(2n)\varepsilon$。
所有新的数值只是显示整数上界；未通过扫描有限模推断无限频率。

## 2. 同一真实两 bump 确实实现新目标

F.36 是原实际局部 Jacobian 的同一个积分。沿准确保持 $\Theta_o$
的曲线，$|\partial_{\gamma_2}\beta_o|>2^{-9}\sqrt{\mathcal B_o}$，
且 $0<T_2/T_1<1$，
$$
 \mathcal B_o=\sqrt{12}\Delta_o/\eta_{129}>2^{190}.
$$
因此完整 $\beta$ 单位窗口中的新目标由唯一实点实现，满足
$$
 |\bar\gamma_{2,o}|<2^{-86},\qquad
 |\bar\gamma_{1,o}-\gamma_{1,o}^{\rm pre}|<2^{-86},
 \qquad |\bar\gamma_{1,o}|<2^{-23}.
 \tag{J.6}
$$
原 roots、两 positive germ 和所有原端 jets 准确保持。
这一步只选择径向原点，未对非径向标签重新选一个不连续好集。

外行的五个 compact 参数采用浅前缀 P.14 的同一三个不交支集和半径。
其准确局部曲线分别保持
$-2\int\sqrt Q\,dt$ 与
$\frac12\int V_w\sqrt Q\,dt$ 的变化为0。
对完整外行，它们因此也保持 F.32 的 $\omega_o,\beta_o$：
两根、剩余 strict 片和正区完全不随这些支集改变，分部积分的边界原函数
$\sqrt Q/2-Q_t/(8Q^{3/2})$ 两端 jets 准确相同。
故实际五盒是该新原点的合法子族，不需要用一个自由 phase 参数取代度量变化。

这只建立五盒的身份和 radial phase 保持；把其局部正型送到新两根
完整输入所需的新 Cauchy 费用，将在相应全网络谱选择中单独消费。
本篇没有沿用旧外分量尚不存在时的 generator 下界。

## 3. 全部第二变量的真实径向局部逆

旧内部行用已经证明的受控径向曲线和目标；外行用 (J.6)。
统一令
$$
 \Theta_i(\chi_i(q_i,\Omega),\bar\gamma_{2,i}+q_i,\Omega)
                  =\omega_i/4,\qquad |q_i|<2^{-32}.
 \tag{J.7}
$$
全部 $\chi_i$ 都是同一真实第一 inverse，$|\partial_q\chi_i|<2$。
对外行这一门来自 O.9--O.14 与 F.36；剩余新增平台和根的 phase 是常数，
不参与这个局部逆的任何导数。

定义归一化完整径向第二行
$$
 f_i^\Omega(q)=
 {\beta_i(0,\chi_i(q,\Omega),\bar\gamma_{2,i}+q,\Omega)
                         -\beta_i^0\over\sqrt{\mathcal B_i}} .
 \tag{J.8}
$$
$f_i^\Omega(0)=0$。原真实 Jacobian、同一复参数半径和支集分离给
$$
 |(f_i^\Omega)'(0)|>2^{-9},\quad
 |(f_i^\Omega)''|<2^{36},\qquad
 f_i^\Omega(\varphi_i^\Omega(z))=z,
$$
$$
 |z|<2^{-267},\quad
 |\varphi_i^\Omega(z)|<2^{-256},\quad
 |(\varphi_i^\Omega)'|<2^{10}.
 \tag{J.9}
$$
外行的这些导数逐字等于原局部两 bump 公式的导数；
新增完整相位只改变常数项，已经由 (J.6) 扣去。
因此这里复用的是同一个局部积分与同一个 inverse 证明，
没有重用一个不属于新对象的 $\beta$ 值。

## 4. 第一 KAM 后的完整第二误差及无限交叉行

先在 $\|q\|_{\ell^\infty}<2^{-34}$ 上做 O 的同一次全 principal KAM，
得到 $\gamma_1^*(a,q,\Omega)$。
所有 $i\in\mathcal I_+$ 同时定义
$$
 E_i(a,q,\Omega)=
 {\beta_i(a,\gamma_1^*,\bar\gamma_2+q,\Omega)
 -\beta_i(0,\chi_i(q_i,\Omega),
                        \bar\gamma_{2,i}+q_i,\Omega)
          \over\sqrt{\mathcal B_i}} .
 \tag{J.10}
$$

必须使用正确的 controlled 费用：
[受控联立篇](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)
N.11--N.12 给旧完整集合
$$
 \sum_{i\ne o}|E_i|<2^{160056}\mathcal X,\qquad
 \|D_q E_{\rm old}\|_{\ell^\infty\to\ell^\infty}
                                      <2^{160091}\mathcal X .
 \tag{J.11}
$$
不把较早未 controlled 的 $2^{160040}$ 预算替代此式。

为何扩大集合后仍能消费 (J.11)：原全标签复盒 U.1 本来就包含
第129胞第二下降坡的两个参数；它们原先只在内部 KAM 枚举中固定。
旧内部区间的径向系数、根 germ 和实际状态权均不变。
O.25 的新平均矩阵在同一个加权 $\ell^\infty$ norm 中仍有 Neumann
逆小于2，逐行 $|p_i^*|<16\varepsilon_i\bar a$ 仍相同。
故旧 N.9、N.11 的每一行用的是同一个实际局部界；
新增外参数只增加已保留的 Banach 方向，不产生漏掉的列和。
完整 fixed-stop 物理尺度在密度相位恒等式中准确抵消，
不把 source 的物理缩放也删去。

F.37 给新增外行
$|E_o|<2^{2048}\mathcal X$、
$\|D_qE_o\|<2^{2083}\mathcal X$。
合并后
$$
 \sum_{i\in\mathcal I_+}|E_i|<2^{160057}\mathcal X,\qquad
 \|D_qE\|_{\ell^\infty\to\ell^\infty}
                                      <2^{160092}\mathcal X
                 \quad(\|q\|\le2^{-256}).
 \tag{J.12}
$$
第二门也可直接在完整方向盘余半径 $2^{-35}$ 上 Cauchy 得出。
它不是逐坐标导数的 supremum。

现在一次联立
$$
                  q_i=\varphi_i^\Omega(-E_i(a,q,\Omega)),
                         \qquad i\in\mathcal I_+ .
 \tag{J.13}
$$
在闭球 $\|q\|_\infty\le2^{-256}$，其像与 Lipschitz 常数分别小于
$$
 2^{160067}\mathcal X\le2^{-102077},\qquad
 2^{160102}\mathcal X\le2^{-102042}<1/2 .
 \tag{J.14}
$$
每个 $\varphi_i$ 的输入也严格小于 $2^{-267}$。
同一无限收缩因此给唯一 $q^*(a,\Omega)$，并且
$\sum_i|q_i^*|<2^{160067}\mathcal X$。
令
$$
 \Gamma^*(a,\Omega)=
      (\gamma_1^*(a,q^*,\Omega),\,\bar\gamma_2+q^*).
$$
对所有新完整分量，包括 $o$，准确有
$$
 \boxed{\quad
 R_i(a,\Gamma^*,\Omega)\circ K_i=K_i\circ T_{\omega_i/4},
 \qquad \beta_i(a,\Gamma^*,\Omega)=\beta_i^0 .
 \quad}
 \tag{J.15}
$$
这是同一个实际全频图上的两行选择，不是分别选择每一局部参数后忽略反馈。

## 5. 真参数导数、固定目标及完整源

微分 (J.13) 的正确有序式是
$$
 Dq^*=\bigl[I+D\varphi^\Omega(-E)\,D_qE\bigr]^{-1}
 \left\{(D_{\rm ext}\varphi^\Omega)(-E)
                 -D\varphi^\Omega(-E)\,D_{\rm ext}E\right\}.
 \tag{J.16}
$$
逆的 norm 小于2。这里第一项是在固定标量输入时微分真实径向 inverse；
标签方向固定 $\Omega$ 时该项为0，控制方向一般不能删。
$\varphi^\Omega(0)=0$ 对整个控制盒恒成立，所以该项的 control Cauchy
门仍含真实输入 $E$ 的小量和原控制半径费用。
第一列必须随后使用
$$
 D\gamma_1^*
   =(\partial_{\rm ext}\gamma_1^*)_{q}
        +D_q\gamma_1^*\,Dq^* .
 \tag{J.17}
$$
这明确保留外行、全部交叉行及两列 $D\Gamma^*$，
不能以 radial 五盒的相位变化为0而令它们为0。

角平移与原完整图、密度有限部、两个平均方程及唯一固定点交换，
所以
$$
 \Gamma^*(T_\varphi a,\Omega)=\Gamma^*(a,\Omega),\qquad
 D_a\Gamma^*(0,\Omega)=0 .
 \tag{J.18}
$$
第二式仅对原非zero Fourier 标签方向使用其真实表示和 $\ell^1$ 稠密性；
两个 mean 方程没有删去。一个最终标签的整条相位轨道共用同一目标度量。

metric/source 列仍是
$\delta w=w(\sum\psi_1\delta\gamma_1^*+
\sum\psi_2\delta\gamma_2^*+\delta\Xi)$、
$\delta g_{aa}=2w\delta w$ 及其真实参考高度积分。
新 stop 固定，$D\ell^0=0$；不引入旧重停公式。
原 $\nu$、ordinary/weak 两行和 bare endpoint 费用继续按 S.27--S.29、
F.38--F.39 及正区 P.27--P.32 的真实单位消费。

## 6. 新外首相位的完整固定标量正常形

外负段模型 F.23 是真实 unitary word。
令在正角锥 $V_o=-M_C^*M_B$，负锥采用原共轭次序；
模型 mean 上取 $-I$，实际 mean 行仍另保。

[固定标量正常形](R119-supplement-fixed-scalar-normal-form-and-slope-unit-high-network.md)
Z.9--Z.29 的代数只用以下已重付输入：
完整 principal KAM (J.15)、真实首平均 $\beta_o^0$、
root/graph/strict 的同支 phase、
原 signed-density 两侧 Green/polar 恒等式和有限角域。
外行按 F.8、F.19、F.21--F.25 可以取
$$
 \|A_k:H^r\to H^{r+1}\|<2^{512}\Lambda_o,\quad r=0,1,\qquad
 \|e^{itA_k}\|_{H^r\to H^r}<2,\quad |r|\le2 ,
$$
$$
 \epsilon_o^c=2^{32768}\mathcal X,\qquad
 2^{2048}\Lambda_o\epsilon_o^c<1/64 .
 \tag{J.19}
$$
大的 radial 平均先移走，不放进绝对 Gronwall 指数。
原 finite word 的全部有序变换与 mean-rank-one 项因此仍可逐项消费；
phase 系数至多32个，变换次数也至多32。

具体地，在固定标准角 $x=4\theta$ 上，
$$
 U_K^{-1}A_\epsilon(a)U_K
 =A_\epsilon((a\circ K^{-1})(K^{-1})')+R,\qquad
 A_\epsilon(a)=\Pi_\epsilon|D|^{-1/2}M_a|D|^{-1/2}\Pi_\epsilon .
$$
$R$ 保留跨锥和完整 mean 泛函；
原两次有序 Duhamel 给其总两阶费用
$2^{6600}\Lambda_o^2$。
真实右置首系数与 symmetric 约定的差仍是两阶，包含于该门。
这不改变 F.31 识别的准确平均。

求同一个 scalar cohomological 方程
$$
 q_o-q_o\circ T_{-\omega_o}=\beta_o^0-B_o(x),\qquad\langle q_o\rangle=0 .
 \tag{J.20}
$$
此处 $B_o(x)$ 是完整 operator first-phase 函数，
不是 (J.2) 的二次多项式整数。其非mean有实际解析角域和小量。
(O.13) 的除数与固定角余宽给所需26阶门，已含在 $\epsilon_o^c$ 中。
用原 signed symmetric $Q_o$、$Q_o\Pi_0=0$，令
$\mathcal W_o=U_{K_o}^{-1}e^{iQ_o}$。
它是真 unitary，$H^r$ 正逆 norm 小于4，$|r|\le2$，准确保留模型 mean。
于是
$$
 \widetilde V_o=\mathcal W_o^*V_o\mathcal W_o,\qquad
 \mathcal U_o^0=
  \Pi_{\ne0}e^{i\omega_oD}e^{i\beta_o^0D^{-1}}-\Pi_0,
$$
$$
 \|\widetilde V_o-\mathcal U_o^0:H^0\to H^2\|
                                      <2^{6700}\Lambda_o^2 .
 \tag{J.21}
$$
两个比较对象均酉；输出插值给
$H^0\to H^{4/3}$ 界 $2^{4500}\Lambda_o^{4/3}$。
准确恒等式
$R^*=-(\mathcal U_o^0)^*R\,\widetilde V_o^*$
再给 adjoint 强窗，不能靠未付的高阶实际 Cauchy 条件数。
两个 mean 的真实传播没有由 $\mathcal U_o^0|_{\rm mean}=-I$ 替代。

## 7. 真两行表示、有限受影响集合和所有外列

沿原 Z.30--Z.33 的准确 unitary 两行预条件，再仅在非mean行乘
$$
 \mathcal A_o^0=\begin{pmatrix}I&-I\\\mathcal U_o^0&I\end{pmatrix},
$$
模型两行成为
$$
 (\mathcal D_o)_n=
 [1+e^{i(n\omega_o+\beta_o^0/n)}]I_2,\qquad n\ne0 .
 \tag{J.22}
$$
mean 上行操作取恒等；不使用其奇异的模型 mean 块。

这必须放回完整未消元网络，而非只看孤立外行。
新外根 $e_X$ 是第129胞第二个上升 quintic 的外根，
它的 positive 伙伴是同一上升片的内根，属于 $(129,1)$。
另一端 $e_0$ 接新外 positive—long 组件，其远端 $C_R$ 仍独立。
因此真正含新负因素或新 positive 因素的有限行集合是
$$
                         \mathcal J_o=\{(129,1),(129,2)\}.
 \tag{J.23}
$$
这个枚举由实际上升片的两个根得到，不把 cut128 的编号当成某个远端 B。

F.2 的完整两个基础窗、新 P 的完整 $R_++I$ 门及其 adjoint，
以及原相邻 positive 的真实两端门给
$$
 (\mathcal D+\mathcal E)z=\mathfrak g,\qquad
 \|\mathcal E_i:H^s(\text{相邻完整端口})\to H^{s+4/3}\|
 <\begin{cases}
 2^{24000},&i\in\mathcal J_o,\\
 2^{20000}\lambda_i^{4/3},&i\notin\mathcal J_o,
 \end{cases}
 \quad -4/3\le s\le0 .
 \tag{J.24}
$$
$\lambda_i=2^{32}\sqrt{j+5}\,\delta_j^{-9/4}$ 是原内部尺度。
外行的所有模和原相邻行的输入也保留。
不能在 adjoint 窗仍给 $(129,1)$ 写旧较小常数：
其真实 positive cross 可接到新外负段的完整 error。

为核 (J.24) 的次序，forward 窗将误差写成
$(R_++I)S_- -(S_--S_-^{(1)})$；
第一项右侧只消费真实 $S_-$ 的 $H^0$ norm1。
反向基础窗改写成
$R_+(S_--S_-^{(1)})+(R_++I)S_-^{(1)}$，
第一项左侧只用 $R_+$ 的 $H^0$ 门，第二项右侧是模型的
$H^{-4/3}$ 门。新实际外 positive 不必在未匹配背景上自伴，
它已付 $\|R_+\|<2$ 和两个强窗即足够。
每行最多8个真实端口，原模型正逆有限乘积费 $2^{64}$，
最后行操作 norm 小于2；F 的 $2^{9000}\Lambda_o^{4/3}$ 与
(J.21) 合计小于 $2^{20000}\Lambda_o^{4/3}<2^{24000}$。
两个基础窗之间用 Hilbert 插值得到所列 $s$，不授未付的正 $s$。

若原波源为 $\gamma=q_++R_+q_-$，真实新源准确按原顺序为
$$
 \mathfrak g_i=
 [\Pi_{\ne0}\mathcal A_i^0+\Pi_0I]\,
                 \mathbf W_i^*\mathcal R_i\gamma_i .
 \tag{J.25}
$$
同一矩阵作用所有真实外输入列，包括独立 $C_R$、$\nu$、两列
$D\Gamma^*$ 和 weak endpoint 荷。参数微分还要加入这些矩阵自身的
真实导数。原物理两迹通过原 $\alpha_e$、normal shear、density
角图及 total 通量恢复；它们没有变成裸 scalar 标签。

## 8. 完整高块与所有低历史的准确位置

取
$$
 T_i^+=
 \begin{cases}
 2^{131072},&i\in\mathcal J_o,\\
 2^{65536}\lambda_i^4,&i\notin\mathcal J_o,
 \end{cases}
 \qquad P_{H,i}=\mathbf1_{\{|m|\ge T_i^+\}},\quad P_L=I-P_H .
 \tag{J.26}
$$
全部 mean 属于 $P_L$。外列仍是其原独立源/边界端口，
没有因不赋 $P_H$ 就获得任何额外高频收益。

对 $o$，(J.3) 给 $T_o^+>4N_o$。
对 $(129,1)$，原 Q.14 给同样严格不等式；
其余行仍是原 Z.36。因此真正高行均可用没有 $N_i$ 因子的
$|\mathcal D_i^{-1}|<2^{10}\langle m\rangle$。
新有限两行的全输入费用为
$$
 \|P_{H,i}\mathcal D_i^{-1}\mathcal E_i\|
 <2^{24010}(T_i^+)^{-1/3}
                         =2^{-59042/3}<2^{-19680}.
 \tag{J.27}
$$
原所有其他行保持 $2^{-5506/3}$ 的门。
双向基础窗保留的真实行列估计、每行每列至多8个端口，
故在无层权的 $\ell^p(\mathcal I_+;H^s)$，$1\le p\le\infty$、
$-4/3\le s\le0$，完整 HH feedback norm仍小于 $2^{-1024}$。

于是准确高解是
$$
 z_H=
 [I+P_H\mathcal D^{-1}\mathcal E P_H]^{-1}
 P_H\mathcal D^{-1}
                 [\mathfrak g-\mathcal E P_Lz_L] ,
 \tag{J.28}
$$
其 Neumann 逆 norm 小于2。完整低历史和 mean 通过所显示的真列进入；
没有添加未知高模为0的边界条件。
一般层权版本必须再次检查真实相邻比，不能由本篇无层权结论自动授予。

现在新外主相位、完整首相位、两 $\Gamma$ 联立、
两基础强窗、固定 scalar 行和完整高反馈已经在同一个新对象上接通。
接下来是按实际新 Cauchy 常数支付外五盒 generator 与中间谱权，
消费全部低/外 Schur，并恢复原强标签与完整帽/mean条件。
这些步骤不能由高块的 norm2或局部酉性替代。
