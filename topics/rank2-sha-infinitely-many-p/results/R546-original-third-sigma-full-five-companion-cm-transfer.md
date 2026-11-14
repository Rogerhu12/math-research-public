# R546 — 原第三 σ 支的完整五伴随 CM 转移与真实中央行

日期：2026-11-14。**状态：已证明。** R542 对 R541 的第三支
\(\eta=\omega^2H_*\rho_0\) 已给完整第一边际的算术分解。
本篇把其中原 \(S\)、\(S_{\rm new}\)、\(H_{\rm ref}\) 三条投影
提升到同一个六输入联合：三条伴随都是五变量整卷积单位。
两条原秩二曲线的中央零因而控制这些投影后的全部独立五伴随测试。

所有 CM 分支与混合管仍逐项保留。特别，R544 的混合 \(Y/W/L\)
测试不能只因这里有五伴随单位就被赋中央零。
参考的未知导数保留，两个实际环带的非齐次差则准确非零。

## 1. 同一个实际来源和整数六轴框架

沿用 R465、R541、R542 的全部周期、reduced sigma 和 \(b=17\)。
置
\[
\delta=1+2\omega,\quad\omega^2+\omega+1=0,\quad
\gamma=3+\omega,\quad\gamma_{13}=4+\omega,\quad
\gamma_{19}=5+2\omega.
\]
原六个未缩放输入为 \((\xi_1,\xi_2,\xi_3,x,c,d_0)\)，
\[
(t_1,t_2,t_3,t_4)=(\delta\xi_1,2\delta\xi_2,\gamma\xi_3,\bar\gamma x),
\qquad A=t_1+t_2+t_3+t_4.
\]
在 \((t_1,t_2,t_3,t_4,c,d_0)\) 上，
\[
\rho_0=-\frac1{84}
([\delta]_*\nu_\sigma)\otimes([2\delta]_*\nu_\sigma)
\otimes([\gamma]_*\nu_\sigma)\otimes([\bar\gamma]_*\nu_\sigma)
\otimes\nu_\sigma\otimes\nu_\sigma.
\tag{1}
\]
保原实际输出
\[
Y_s=A+c+2d_0,\qquad W=A+3\delta c+4d_0.
\tag{2}
\]
R541 的 \(H\) 固定前四输入，在后两输入上为
\[
H_{c,d}=\frac12
\begin{pmatrix}
-1-\omega&-1-2\omega\\
2+\omega&-1-\omega
\end{pmatrix},
\quad H\bar H^{\,t}=I,\quad\det H=\omega.
\tag{3}
\]
定义完整第三来源
\[
\eta=\omega^2H_*\rho_0.
\tag{4}
\]
这里的标量 \(\omega^2\) 是原 σ 身份的一部分，不删去。

使用 R465 的同一六轴坐标
\[
\begin{aligned}
L={}&(2Y_s,2Q_s,2U_s,R_1,R_2,R_3),\\
Q_s={}&A-29c,\qquad U_s=A+c-15d_0,\\
R_1={}&4t_1-t_2,\\
R_2={}&7(t_1+t_2)-15t_3,\\
R_3={}&7(t_1+t_2+t_3)-22t_4.
\end{aligned}
\tag{5}
\]
记 \(L_*\eta\) 的完整生成来源为 \(\mathcal F_\eta\)，第一生成变量
为 \(z\)，五伴随变量为 \(\mathbf z\)；实际第一物理输出是
\(Y=2Y_s\)，五伴随物理输出记为 \(\mathbf Z=(Z_1,\ldots,Z_5)\)。

**引理 1。** 在同一个原整格内，
\[
\boxed{
\mathcal F_\eta\in
\mathcal S_{136}\otimes\mathcal S_{3480}\otimes\mathcal S_{1020}
\otimes\mathcal S_{60}\otimes\mathcal S_{2310}\otimes\mathcal S_{4466}.
}
\tag{6}
\]
其六轴同时 CM 转移可使用 norm \(13,19\)。

**证明。** 直接将 (3) 乘入 (5)，\(LH\) 的前四列与 \(L\)
相同，最后两列准确为
\[
\begin{pmatrix}
3+\omega&-3-4\omega\\
29+29\omega&29+58\omega\\
-31-16\omega&14+13\omega\\
0&0\\0&0\\0&0
\end{pmatrix}.
\tag{7}
\]
因此 \(LH\) 是 CM 整矩阵；没有在 trace 的有限纤维中使用
一个未清分母的半整矩阵。其行列式和完整 Gram 为
\[
\det(LH)=-13015200\,\omega,
\]
\[
(LH)\operatorname{diag}(3,12,7,7,1,1)
\overline{(LH)}^{\,t}
=\operatorname{diag}(136,3480,1020,60,2310,4466).
\tag{8}
\]
回到六个未缩放的 σ 输入时，行列式再乘
\(\delta(2\delta)\gamma\bar\gamma=-42\)。
这些行列式都与 \(13\cdot19\) 互素，且在当前普通 \(p\) 处为单位。

半特征也完整核实如下。前三行的前四个未缩放 σ 系数均为偶；
(7) 每行两个后系数模二皆非零。因此前三行各有两个奇 CM
系数，后三行各有 \(0,2,2\) 个。
模二的非零 CM 单位保持唯一奇 σ 半特征，偶数个相乘为标准偶
半特征。结合 (8) 的全部交叉项为零，得到 (6)。
原测度整有界且 \(LH\) 是普通整自同构，R465 的完整首阶单位
张量基消元给整性；未用大阶乘除法推断。

最后，(8) 使 \(LH\) 在 \(E[a]^6\) 上为双射，
\(a=\gamma_{13},\gamma_{19}\) 或其共轭，故可作完整六重 CM
纤维重排。证毕。

## 2. 全六轴 trace 身份和旧五伴随算子

沿用固定 canonical division trace
\(N_a=\mathscr M_a/a\)。R483 已从原奇 \(\mathcal S_1\) 的完整
纤维计算确定绝对相位
\[
N_{\gamma_{13}}\sigma=-\sigma,\qquad
N_{\gamma_{19}}\sigma=\sigma,
\tag{9}
\]
共轭方向也按同一个 canonical 规范读取。

对 (1) 的六输入 simultaneously 施加 \(N_a\)，(9) 的六次方为一。
按引理 1 的双射重排六重有限和，(8) 消去所有 Gaussian 交叉项，
第1节的半特征核实保证逐项中心相位相同，两边总规范均为
\(a^{-6}\)。所以完整地
\[
\boxed{
N_{a,Y}\prod_{\ell=1}^5N_{a,Z_\ell}\mathcal F_\eta
=\mathcal F_\eta
\quad(a=\gamma_{13},\gamma_{19},\bar\gamma_{13},\bar\gamma_{19}).
}
\tag{10}
\]
常数 \(\omega^2\) 原样保留；这不是从单个 Y 边际推出来的身份。

六个奇 σ 的总角型是零，\(H\) 与 CM 标量交换，故第一轴
principal 平均 \(\Pi_{0,Y}\) 在此实际来源上等于其余五轴同时
平均 \(\Pi_{\mathbf Z}\)。
R483 在整个 \(\mathcal S_{136}\) 上用真实非零锚 \(S(2z)\)
定标了
\[
N_aN_{\bar a}=I,\qquad a=\gamma_{13},\gamma_{19}.
\tag{11}
\]
定义真正只动旧五伴随的算子
\[
B_{13}=\prod_{\ell=1}^5N_{\bar\gamma_{13},Z_\ell},
\qquad
B_{19}=\prod_{\ell=1}^5N_{\bar\gamma_{19},Z_\ell}.
\tag{12}
\]
对 (10) 的共轭方向乘第一轴逆 (11)，并迭代，得到
\[
\boxed{
N_{13,Y}^{j}N_{19,Y}^{k}\Pi_{0,Y}\mathcal F_\eta
=B_{13}^{j}B_{19}^{k}\Pi_{\mathbf Z}\mathcal F_\eta.
}
\tag{13}
\]
这是完整六变量等式。右边保持实际 \(Y=2Y_s\) 及其单位条件。

在第一 principal 空间，R466/R483 的绝对身份是
\[
N_{13}=N_7^5,\qquad N_7=N_{13}^{11},\qquad N_7^{18}=I.
\tag{14}
\]
因此不用与 \(\det L\) 不互素的 norm7 直接重排原输入；
全部 norm7 第一投影均由合法的 norm13 五伴随操作实现。

## 3. 三条完整张量分离与准确单位质量

定义三个有限五伴随算子
\[
\begin{aligned}
\mathcal C_S&=\frac1{18}\sum_{j=0}^{17}(-1)^jB_{13}^j\Pi_{\mathbf Z},\\
\mathcal C_{\rm new}&=\frac{I-\omega B_{19}}{36}
 \sum_{j=0}^{17}\omega^{2j}B_{13}^j\Pi_{\mathbf Z},\\
\mathcal C_H&=\frac{I-\omega^2B_{19}}{36}
 \sum_{j=0}^{17}B_{13}^j\Pi_{\mathbf Z}.
\end{aligned}
\tag{15}
\]
(13) 将它们逐字转成第一轴投影。
R483 的完整二十三维秩计算给三像恰分别为
\(\langle S_2\rangle,\langle S_{\rm new}\rangle,\langle H_{\rm ref}\rangle\)，
其中
\[
S_2(z)=S(2z),\quad [z^6]S_2=64,\quad
[z^6]S_{\rm new}=1,\quad H_{\rm ref}(0)=1.
\tag{16}
\]
\(S_{\rm new}\) 是原 \(E_{2312}\) 来源；
\(H_{\rm ref}\) 是原 \(E_{668168}\) 的质量一来源。

由于每个第一像为一维，存在唯一完整五变量来源
\(A_\eta,\Lambda_\eta,\Lambda_{H,\eta}\)，准确有
\[
\boxed{
\begin{aligned}
\mathcal C_S\mathcal F_\eta&=S_2\otimes A_\eta,\\
\mathcal C_{\rm new}\mathcal F_\eta&=S_{\rm new}\otimes\Lambda_\eta,\\
\mathcal C_H\mathcal F_\eta&=H_{\rm ref}\otimes\Lambda_{H,\eta}.
\end{aligned}}
\tag{17}
\]
这是先由整个第一轴的秩一像得到的分离；此后才用边际计算质量。

把五伴随生成变量设零，R542 的全部坐标投影给
\[
\boxed{
A_\eta(0)=-\frac12,\qquad
\Lambda_\eta(0)=\frac{26}{3}(1-\delta),\qquad
\Lambda_{H,\eta}(0)=-\frac1{1008b}.
}
\tag{18}
\]
所有值均在当前 \(p>19\) 和原固定坏集之外为单位。

(15) 是完整 prime-to-p canonical trace、角平均和单位分母的
整算子，故 (17) 左边整有界。前两条分别取第一 Amice 六阶矩，
除以 \(64\cdot720\Omega_p^6\)、\(720\Omega_p^6\)，第三条取常数，
给三条伴随的整有界测度。分母在当前处均为单位。因此
\[
\nu_{A_\eta},\nu_{\Lambda_\eta},\nu_{\Lambda_{H,\eta}}
\in\mathcal O[[\mathbb Z_p^5]]
\tag{19}
\]
且由 (18)，三者都是完整五变量 Amice 卷积单位。
这项结论只关于完整卷积；任何混合 cut 的测试仍须实际转置。

R542 另外三条已识别参考及十二条外谱仍存在。
(17) 没有把 \(\mathcal F_\eta\) 宣称为三条之和，更没有使其余
完整张量投影或中央导数为零。

## 4. 原两中央零现在控制的全部条件行

令 \(d=p-1\)，对单轴来源记
\[
J_G(u)=\int_{\mathbb Z_p^\times}\langle y\rangle^{du}\,d\nu_G(y).
\tag{20}
\]
(17) 对任意完整连续五伴随测试 \(h(\mathbf Z)\) 给整个 Mellin
函数身份
\[
\begin{aligned}
\int_{Y\ {\rm unit}}\langle Y\rangle^{du}h(\mathbf Z)
 \,d\nu_{\mathcal C_S\mathcal F_\eta}
 &=\langle2\rangle^{du}J_S(u)\nu_{A_\eta}(h),\\
\int_{Y\ {\rm unit}}\langle Y\rangle^{du}h(\mathbf Z)
 \,d\nu_{\mathcal C_{\rm new}\mathcal F_\eta}
 &=J_{\rm new}(u)\nu_{\Lambda_\eta}(h).
\end{aligned}
\tag{21}
\]
任意紧开伴随事件可包含在 \(h\) 中，且保原三条 \(R_i\) 输入。
因为 \(J_S(0)=J_{\rm new}(0)=0\)，若原反证输入为
\(J'_S(0)=J'_{\rm new}(0)=0\)，(21) 的两个完整中央行均为零。
若 \(h=h_u\) 解析依赖 \(u\)，乘积导数的第二项也由这两个
零质量消失；原 \([2]\) 尺度同样没有遗漏质量对数。

R536 的 \(C,F,G_{\rm hid}\) 三条实际输出均与 \(Y_s\) 正交。
(5) 是同一 Hermitian 空间的一组完整正交基，所以这些输出
准确属于 \(\mathbf Z\) 的线性张成；其变换在当前处整。
因此只依赖这三输出的原 \(q_n\)、它的伴随紧开条件及连续测试，
均在 (21) 的合法范围内。额外的原输入 \(D_n\)、\(W\) 或混合
\(L\) 条件若还依赖 \(Y\)，则不能混入这个断言。

## 5. 全六深与五伴随共同深的真实核心

当前普通参数仍为
\[
\lambda=-\bar\pi_0^{-1},\qquad\beta=-\lambda,\qquad
\kappa=p\lambda^2.
\]
六个原 σ 同时深的标量是 \(\beta^6=\lambda^6\)。
(3)、(5) 在当前 \(p\) 是整自同构，故其像的六个输出同时深
等价于六原输入同时深。因此
\[
\nu_{\mathcal F_\eta}|_{(p\mathbb Z_p)^6}
=\lambda^6[\kappa I_6]_*\nu_{\mathcal F_\eta}.
\tag{22}
\]
prime-to-p 的完整 CM 对应与这个 simultaneous ordinary
对应可重排全部互素纤维；canonical 中心与总规范相同。
这正是 R483 §6.1 的全部对应，作用于引理1的同一完整张量格，
所以 (22) 经 (15) 保留。

(17) 三个第一来源的 scalar core 分别是
\(\lambda,-\lambda,-\lambda\)。在整 Amice 环中约消非零第一因子，
得到
\[
\boxed{
\begin{aligned}
\nu_{A_\eta}|_{(p\mathbb Z_p)^5}
 &=\lambda^5[\kappa I_5]_*\nu_{A_\eta},\\
\nu_{\Lambda_\eta}|_{(p\mathbb Z_p)^5}
 &=-\lambda^5[\kappa I_5]_*\nu_{\Lambda_\eta},\\
\nu_{\Lambda_{H,\eta}}|_{(p\mathbb Z_p)^5}
 &=-\lambda^5[\kappa I_5]_*\nu_{\Lambda_{H,\eta}}.
\end{aligned}}
\tag{23}
\]
仅声明五伴随共同深，不免费赋每个伴随一个单独标量核。

对第一来源 \(G=S_2,S_{\rm new},H_{\rm ref}\)，置其标量为 \(c_G\)。
所有 \(n\ge0\) 的第一环带准确满足
\[
\int_{y\in p^n\mathbb Z_p^\times}
 \langle y/p^n\rangle^{du}\,d\nu_G(y)
=c_G^n\langle\lambda^2\rangle^{ndu}J_G(u).
\tag{24}
\]
可同时附任意五伴随测试及 (23) 的共同深限制。
原两零中央于是对这些完整环带仍为零；这使用零质量消去
(24) 的尺度导数，不能对参考照抄。

## 6. 参考保留未知导数，实际环带差非零

由 (17)，对完整 \(u\)-依赖伴随测试，
\[
\int_{Y\ {\rm unit}}\langle Y\rangle^{du}h_u(\mathbf Z)
\,d\nu_{\mathcal C_H\mathcal F_\eta}
=J_H(u)\nu_{\Lambda_{H,\eta}}(h_u).
\tag{25}
\]
质量一和核心 \(-\lambda\) 给 \(J_H(0)=1+\lambda\)，故准确导数为
\[
J'_H(0)\nu_{\Lambda_{H,\eta}}(h_0)
+(1+\lambda)\nu_{\Lambda_{H,\eta}}(\partial_u h_0).
\tag{26}
\]
两项都保持。

记 \(\mathcal L_{\eta,H,n}\) 为伴随测试一、第一输出限制
\(p^n\mathbb Z_p^\times\)、权取 \(\langle Y/p^n\rangle^{du}\)
的中央导数。(18)、(24) 消去未知 \(J'_H(0)\) 后给
\[
\boxed{
(-\lambda)^{-n}\mathcal L_{\eta,H,n}-\mathcal L_{\eta,H,0}
=-\frac1{1008b}\,
n\,d\,\log_p\langle\lambda^2\rangle(1+\lambda).
}
\tag{27}
\]
对每个正 \(n\)，右边非零。R483/R533 的原射线论证已给
\(1+\lambda\) 为单位；其余固定因子也是单位。
若 \(\log_p\langle\lambda^2\rangle=0\)，这个普通嵌入中的
\(\lambda^2\) 是根单位；同一代数数即为根单位，但其全局范数
为 \(p^{-2}\)，矛盾。

(27) 位于 R541 的同一个真实第三 σ 支及完整五伴随操作中。
它不使 (25) 的任一未知导数为零，尚不能单独与 (21) 矛盾。

## 7. 每条真实 CM 分支上的混合单位域

为明确剩余接口，令
\(\alpha=\gamma_{13}^{j}\gamma_{19}^{k}\)，
逐次展开 (12) 中的完整 canonical trace。R483 的有限分支式
在同一 \(\mathcal F_\eta\) 上原样为
\[
\nu_{B_{13}^{j}B_{19}^{k}\mathcal F_\eta}
=\bar\alpha^{-5}[I_Y,\bar\alpha^{-1}I_5]_*
\sum_{\mathbf t\in E[\bar\alpha]^5}
\nu_{(\mathcal F_\eta)_{\alpha,\mathbf t}}.
\tag{28}
\]
每个 \((\mathcal F_\eta)_{\alpha,\mathbf t}\) 保对应
\(\mathsf T_{\alpha t_\ell}^{(N_\ell)}\) 的完整中心，以及伴随
生成变量的 \(\alpha\) 拉回；所有 torsion 支均保留。
再附 (15) 的角分支 \(\zeta\)，任意完整测试 \(f\) 必须读为
\[
\boxed{f(Y,\mathbf Z)\longmapsto f(Y,\zeta\mathbf Z/\bar\alpha).}
\tag{29}
\]
第一轴本身不缩放，因而没有额外的第一轴
\(\langle\alpha\rangle^{-du}\)；但任何实际混合测试或其 \(u\)
导数都要按 (29) 保留。

同一坐标中原 \(W\) 精确为
\[
W=c_Y Y+r(\mathbf Z),\quad
c_Y=\frac{37+3\delta}{68},\quad
r=\frac{1-3\delta}{60}Z_1+\frac{-31+3\delta}{510}Z_2.
\tag{30}
\]
R539 的 \(L_{\rm mix}=(W-Y_s)/2\) 则为
\[
L_{\rm mix}=\frac{3(1+\delta)}{136}Y+\frac12r(\mathbf Z).
\tag{31}
\]
所以每个实际 CM 分支的 \(W\)-deep 与 \(L_{\rm mix}\)-unit
分别是
\[
c_Y Y+\frac{\zeta}{\bar\alpha}r(\mathbf Z)\in p^m\mathbb Z_p,
\]
\[
\frac{3(1+\delta)}{136}Y+
\frac{\zeta}{2\bar\alpha}r(\mathbf Z)\in\mathbb Z_p^\times.
\tag{32}
\]
这些仍混第一轴。对 R544 的实际 \(P_{C_j,\kappa}\)，先按
\(L P_{C_j,\kappa}L^{-1}\) 变换完整测试，再按 (29) 展开；
测试的每个单位条件、\(q_n\) 与 logarithm 一并运输。
(17) 的五伴随卷积逆不能删掉 (32) 或把它当独立伴随事件。

如需返回原六 σ 输入，(4) 的每个测试还须按 \(H\) 拉回并保
\(\omega^2\)。这与 R541 的另外 \(G/R\) 两支仍在固定 \([4]\)
覆盖上的事实相容；本篇没有缩减它们的实际域。

## 8. 已付结论和下一条未付条件

本篇已支付同一第三支的完整六输入 CM 转移、三条五伴随单位、
两秩二曲线的全部独立伴随中央行、五伴随共同深及参考真实非零
环带差。全证明只用既有完整 CM 秩结论和显示整数矩阵，
不需要新增数值取样或独立复跑。

还须将 R544 的实际混合测试差及唯一余域，连同 (28)–(32)
的全部分支、四参考和十二外谱，送入原完整中央比较。
局部非零、伴随单位或一个参考差都不替代该步骤。
固定曲线、无穷不同 \(p\) 两个量词保持，主目标尚未完成。

## 依赖

- [R465：原六输入及完整 L 框架](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R483：完整 CM13/19 绝对转移与三条秩一算子](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)。
- [R541：真实第三 σ 支与三支域](R541-original-degree8-second-state-and-exact-sigma-transport.md)。
- [R542：第三支全部坐标及实际三条投影系数](R542-original-third-sigma-arithmetic-projections-and-affine-core.md)。
- [R536：完整 C/F/G 隐藏测试](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)。
