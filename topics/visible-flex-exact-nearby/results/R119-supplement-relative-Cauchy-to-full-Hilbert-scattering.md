# R119 续篇：真实相对 Cauchy 到完整 Hilbert 散射，不重复付参考条件数

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 把已经支付的真实 strict interaction 门转换成完整
incoming/outgoing 散射时，不需要再乘参考 Cauchy 条件数。
在真正包含两个 mean 的 Hilbert 空间，若
$\|C_0^{-1}C-I\|\le\epsilon\le1/16$，则对应的完整酉散射满足
$\|S-S_0\|\le8\epsilon$。
这对无限 Fourier 空间成立，不依赖 finite-mode truncation，
也没有倒一个可能极小的 transmission 块。

对本题受控新尾的同一真实 strict 分量，这给
$$
 \|S_{H,i}-S_{0,i}\|\le64\eta_i,\qquad
 \sum_i\|S_{H,i}-S_{0,i}\|
             <2^{192022}\|X\|_{\mathcal X_{224}} .
 \tag{R.1}
$$
$\eta_i$ 是原已付的同空间 interaction 费用，两个全局深尾因子仍在。
这个比较使用各自准确的 principal 端口坐标。它没有把真正端角图
改成恒等，没有自动比较整个物理网络，也没有将一个 scalar
Wronskian 阈值冒充非径向谱隙。

## 1. 实际 strict 完整状态的强 symplectic 形式

使用
[真实 strict 密度 Cauchy](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
的原物理角 $\theta$、周期 $\pi/2$、全部 $m\in4\mathbb Z$。
其完整固定标签状态是
$$
 Y=(c,\alpha,Z_+,Z_-),\qquad \langle Z_\pm\rangle=0,
$$
$$
 w=c+\alpha(S_+-S_-)
       +\sum_{\sigma=\pm}C_{S_\sigma}\partial_\theta^{-1}Z_\sigma .
 \tag{R.2}
$$
两条实际 $H_\sigma$ 和 $S_\sigma=H_\sigma^{-1}$ 按原有向 flow 定义，
没有用参考平移代替。
$c$ 是独立高度坐标，$\alpha$ 是独立通量 mean。
在左端 $H_\pm=\mathrm{id}$ 时，
$$
 w=c+\partial_\theta^{-1}(Z_++Z_-),\qquad
 \zeta=Z_+-Z_-+2\alpha .
$$
故真实 Green 形式
$\int(w\widetilde\zeta-\zeta\widetilde w)d\theta$ 准确等于
$$
 \boxed{\quad
 \Omega_0(Y,\widetilde Y)=
 2(c\widetilde\alpha-\alpha\widetilde c)
 +2\sum_{\sigma=\pm}\sigma
      \langle\partial_\theta^{-1}Z_\sigma,\widetilde Z_\sigma\rangle .
 \quad}                                                   \tag{R.3}
$$
两个交叉波项因 $\partial_\theta^{-1}$ 反自伴准确抵消；
mean 行不是在事后加上的占位符。

定义实际实 Hilbert 空间
$$
 \mathcal H=\mathbb R^2\oplus
  \dot H^{-1/2}_0\oplus\dot H^{-1/2}_0,
$$
其中 $Z_\pm$ 的 norm 为
$\||D_\theta|^{-1/2}Z_\pm\|_2$，完整 Hilbert norm 使用四项平方和。
在坐标 $(c,\alpha,V_+,V_-)$、
$V_\sigma=|D_\theta|^{-1/2}Z_\sigma$ 中，
$\Omega_0=2\langle\mathbb JY,\widetilde Y\rangle$，且
$$
 \mathbb J(c,\alpha)=(-\alpha,c),\qquad
 \mathbb JV_\sigma=\sigma |D_\theta|\partial_\theta^{-1}V_\sigma .
$$
所以 $\mathbb J^*=-\mathbb J$、$\mathbb J^2=-I$。
这是一条非退化的强 symplectic 形式，含完整高度/flux mean。

## 2. 真实 principal flow 的 mean 完成使 interaction 确实 canonical

不能仅因两支 density pullback 各自保积分，就省略其对高度 mean
的补偿。这里使用原完整方程给出准确理由。

将真实密度方程中的 potential $\kappa$ 暂置0，保留实际 $d,\nu$，
则原 (S.14)–(S.17) 给
$$
 Z_\sigma'=0,\quad\alpha'=0,\quad c'=0.
$$
(R.2) 重建的 $w$ 和真实 $\zeta$ 正是
$\operatorname{div}(\widehat G\nabla w)=0$ 的完整 Cauchy 解。
记其从左端初始坐标到时刻 $t$ 的映射为 $\mathcal P_H(t)$。
该散度方程系数实对称；Green identity 给
$\mathcal P_H(t)$ 准确保留 (R.3)。
这也证明两个 mean 的完成是原物理的 canonical 完成，
并非在不同支 pullback 后继续沿用一个错误的裸平均高度。

实际含 $\kappa$ 的齐次 Cauchy 同样保 Green 形式。
因此
$$
 \mathcal U_H(t,s)=
 \mathcal P_H(t)^{-1}\mathcal U_{\rm phys}(t,s)\mathcal P_H(s)
$$
是 $(\mathcal H,\mathbb J)$ 上的完整 symplectic 演化。
径向参考 $\mathcal U_0$ 使用同一 $\Gamma$、同一真实几何及其参考
principal flow，具有同样性质。
于是已经付出的
$$
                         E=\mathcal U_0(s,t)\mathcal U_H(t,s)
 \tag{R.4}
$$
确实满足 $E^*\mathbb JE=\mathbb J$。
物理端口的密度乘子、normal shear、真实角图和方向仍完整留在
$\mathcal P_H$ 及原 height/flux 恢复矩阵中。
本节没有要求这些裸 pullback 的同空间差很小。

## 3. 无限 Hilbert 图的完整 incoming/outgoing 散射

以下只用一条真实 Hilbert 线性事实。
令 $C$ 是 $\mathcal H$ 上有界可逆且
$C^*\mathbb JC=\mathbb J$。
在复化的双端空间
$\mathcal K=\mathcal H_L^\mathbb C\oplus\mathcal H_R^\mathbb C$
取
$$
 \mathbb J_\partial=\operatorname{diag}(-\mathbb J,\mathbb J),
 \qquad
 P_\pm=\frac{I\pm i\mathbb J_\partial}{2}.
$$
$\mathcal L_C=\{(v,Cv)\}$ 是闭的 maximal neutral 子空间。
对任意 $z\in\mathcal L_C$，
$\|P_+z\|=\|P_-z\|=\|z\|/\sqrt2$。
$P_+|_{\mathcal L_C}$ 的像闭且 onto：
若某个 $u_+\in\operatorname{ran}P_+$ 垂直该像，
则它在 $\mathbb J_\partial$ 配对下垂直整个 $\mathcal L_C$；
maximality 强迫 $u_+\in\mathcal L_C$，而正定子空间与 neutral
子空间只能相交于0。另一侧同理。

所以存在真正 onto 的酉算子
$$
 S_C:\operatorname{ran}P_+\longrightarrow\operatorname{ran}P_-,
 \qquad P_-z=S_CP_+z\quad(z\in\mathcal L_C).
 \tag{R.5}
$$
没有使用“有界下方所以酉”的不充分论证。
各 Fourier helicity 可用固定单位ary置换接到原
$(Y_1+iY_2)/\sqrt2$ 的 incoming/outgoing 约定；
mean 是同一个完整双端图的有限维部分。

## 4. 相对 Cauchy 小差的 Möbius 公式

设 $C=C_0E$，$E$ 为 symplectic 且
$\|E-I\|\le\epsilon\le1/16$。
准确有
$$
 \mathcal L_C=\mathcal B\mathcal L_{C_0},\qquad
 \mathcal B=\operatorname{diag}(E^{-1},I),\qquad
 \|\mathcal B-I\|\le\delta:=\epsilon/(1-\epsilon).
$$
按 $P_+\oplus P_-$ 写 $\mathcal B=(B_{ij})$。
若原图为 $(z,S_0z)$，新图的两行是
$$
 Dz=(B_{11}+B_{12}S_0)z,\qquad
 Nz=(B_{21}+B_{22}S_0)z .
$$
$\|D-I\|\le2\delta<1$，所以
$$
                  S_C=(B_{21}+B_{22}S_0)
                            (B_{11}+B_{12}S_0)^{-1}.
 \tag{R.6}
$$
完整差的分子为
$$
 B_{21}+(B_{22}-I)S_0
            -S_0(B_{11}-I)-S_0B_{12}S_0 ,
$$
其 norm 小于 $4\delta$。因此
$$
 \boxed{\quad
 \|S_C-S_0\|
 \le\frac{4\epsilon}{1-3\epsilon}
 \le\frac{64}{13}\epsilon<8\epsilon .
 \quad}                                                   \tag{R.7}
$$
证明中完全没有 $\|C_0\|$ 或 $\|C_0^{-1}\|$。
一个很小的 transmission 仍在 $S_C$ 的完整交叉块中，未被反解或删除。

若两端都另乘一个真实近恒等 symplectic 矩阵，可用
$\operatorname{diag}(E_L^{-1},E_R)$ 直接作同一证明；
各实际误差相加进入 $\delta$。
未近恒等的真实 principal 图只可按其准确双端坐标保留，
不能以本节为由把它换成 $I$。

## 5. 消费本题实际 strict 费用

原完整空间 $\mathcal F_{-1/2}$ 使用四项和 norm 和
$(1+|m|)^{-1/2}$ 波权。
对 $|m|\ge4$，
$1\le[(1+|m|)/|m|]^{1/2}<2$。
故它与本篇兼容 Hilbert norm 的两个方向均可安全取因子2。
原已证
$$
 \|E-I\|_{\mathcal F_{-1/2}\to\mathcal F_{-1/2}}
                        \le e^{\eta_i}-1
$$
因而给
$$
 \|E-I\|_{\mathcal H\to\mathcal H}
                  \le4(e^{\eta_i}-1)\le8\eta_i .
 \tag{R.8}
$$
实际 $\eta_i<1/128$，可直接进入 (R.7)。

在第55束控制后对象上，原 strict 门的真实输入替换为
$$
 N_j^c=2^{200}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2},
 \qquad (N_j^c)^\#=N_j^c+\mathbf1_{j\ge130}N_{j-1}^c .
$$
同一完整式 (S.22)、(S.28)、(S.29) 给
$$
 \eta_i=2^{1280}(j+4)^{13}\delta_j^{-25}
                     (N_j^c)^\#\|X\| .
 \tag{R.9}
$$
所有 profile 宽盒由第53、55束重新支付。
相对原 $N_j$ 只多16 bits，故原全129–8193前缀和几何尾求和
准确放宽为
$$
 \sum_i\eta_i<2^{192016}\|X\| .
$$
这仍包括 $\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}$；
第一新深层的旧/新邻胞也没有合成一个假的统一深幂。
对 $\|X\|\le2^{-262144}$，
$$
 \sum_i\|S_{H,i}-S_{0,i}\|
 <2^{192022}\|X\|\le2^{-70122}.                          \tag{R.10}
$$
同一 sum 门也控制 direct-sum 的 norm。
真正 actual incoming 的更小输入当然在此球内。

这里 $S_0$ 是**同一当前 $\Gamma$** 的 radial reference；
并非在改变 $\Gamma^*(a,\Omega)$ 后继续使用旧基点参考。
真正 principal 返回、root/positive 端图及 KAM 的组合仍须按原顺序
放回整网。这一范围是 (R.10) 的组成部分。

## 6. 完整 affine、ordinary/weak 源及两 mean

若实际 total-flux Cauchy 为
$Y_R=CY_L+g$，其图是 $\mathcal L_C+(0,g)$。
更一般的已付两端 weak/height charge 记成完整向量
$b=(b_L,b_R)$，并令 $b_\pm=P_\pm b$。
真实散射关系准确为
$$
 z_-=S_Cz_++q,\qquad q=b_--S_Cb_+,\qquad
 \boxed{\ \|q\|\le\sqrt2\|b\|.\ }                        \tag{R.11}
$$
两个独立 mean 参加 $P_\pm$、$S_C$ 和 $b$，不被截掉。
(R.11) 不替代实际 source producer 的 norm：
原 $f_d,F_d^t,F_d^\theta$、weak ordinary correction、
两端 $F^t$ 的真实迹、独立高度和 mean flux 按原 strict/根图公式组成
$g,b_L,b_R$。只有先支付这些真实源列，才可使用本节额外的
$\sqrt2$ 散射费用。
内部 $L^2$ weak norm 本身不授予 bare 端迹。

参数若只已知强可微且其导数确为有界算子，同一准确 Möbius 恒等式
可逐向量微分。保持完整次序有
$$
 DS=(DB_{21}+DB_{22}S_0
          -S(DB_{11}+DB_{12}S_0))D^{-1}
       +(B_{22}-SB_{12})(DS_0)D^{-1}.
$$
由 $\|E-I\|\le1/16$ 得一个安全的全部列门
$$
 \|DS-DS_0\|
       \le16\|E-I\|\,\|DS_0\|+16\|DE\| .                \tag{R.12}
$$
$Dq=Db_--DS\,b_+-S\,Db_+$ 同样保留。
本篇没有从裸角复合的全纯性免费授予 $\|DE\|$：
其实际 $\Omega$、标签或 metric-source 导数仍需原方程单独支付。
因此 (R.12) 是明确的消费者，不是未完成导数的替代。

## 7. 真实整网消费边界

本篇解决的是此前把相对 Cauchy 转为酉散射时可能重复乘参考条件数
的问题，且完整包含无限 Fourier、两个 mean 和 affine 源。
它允许在实际完整 Hilbert 端口上与全 positive DN Cayley 图接合。

尚须保持：真实两根的高度/density/shear；严格输出的
$\mathcal P_H$；正型两端 cross；外 regular 行及其真实源；
actual principal KAM 的有序识别；内部标签 $\mathcal X_\beta$ 的单位。
scalar radial 小 Wr 阈值与 whole-network unitary 谱距离并不自动相同。
这些识别、非径向 near-resonant cluster 控制及同权完整 Green 仍是
正在继续的任务，没有由 (R.10) 宣称 $\mathcal F_c=0$ 已解。

[严格小预算](../scripts/fourfold_relative_Cauchy_full_Hilbert_scattering_20261114.js)
和[实际执行记录](../notes/2026-11-14-R119-relative-Cauchy-full-Hilbert-scattering-budget.json)
核查 norm 等价、完整 Möbius 常数、真实所有层费用和 affine/导数门。
无限维存在与 onto 的证明在上文给出，计算没有以有限 Fourier 代替它。
