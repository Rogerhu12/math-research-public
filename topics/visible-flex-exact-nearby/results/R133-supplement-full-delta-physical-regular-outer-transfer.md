# 同一完整实参数族的固定物理外图转移

本合同使用 $Q_\delta=Q_0+\delta Z$、$|\delta|\le10^{-8}$。$Q_0$ 是原完整连续 M32 修补，$Z$ 是原 full193 连续方向（degree96，含独立 mean）；内禀 $\eta_0,\nu_0$ 不变。全体未知 Fourier 输入和物理坐标中由复合产生的无限尾都保留。

原外图 43601149891 的完整 25 门与本次精确右端 43611611635 的 14 门是已完成输入。新 consumer 只支付新的标量转移和完整外图费用，不重做旧端点、目标、帽矩阵或 nonlinear long solve。以下拟外图常数必须由新公开 Actions 真正执行后方为数值结论。

## 1. 同一方向、全部端点与均值

原连续方向定义为 6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04，真实末值 native 为 8f6019cefaa96da64eadb3b19a98110dc81a0d5760a091e6fdffe538c971e606。其 full193 Fraction Horner、六条带和角阶0..4已全部保存。没有 $\alpha$ 缩放或去掉 even mean。

用原数据提供的整球端点上界 $m_-\le|m_\delta|\le m_+$ 和 $U_\sigma,V_\sigma,P_\sigma$。完整真实终端
$$
p_*(\delta)=q_*/(-m_\delta(R))
$$
须重新核 $(1/8,1/5)$，仍对每个物理频率使用同一 $p_*$。该参数不是把一个旧 reference 改名。

## 2. 固定物理角的完整 $C$ 差

在任一真实线段 $Q_0+t\delta Z$ 上，令 $m=\langle v\rangle<0$、$v=m+\widetilde v$、$\theta=\phi+\psi(\phi)$，则 $\theta_\phi=v/m$、$\psi_\phi=\widetilde v/m$。物理曲率是 $C(\theta)=1/v(\phi(\theta))$。

取输入宽度 $1/32$、输出宽度 $1/64$。旧非均值 $A_{1/8}$ 上界在 $A_{1/32}$ 的一阶导数可用16倍，因为实际宽度差为 $3/32$ 且 $32/3<16$；新方向一阶导数直接使用原精确端点数据。记
$$
w=V_{1/32}/m_-,\qquad
w_1=(16V_{0,1/8}+|\delta|\|Z_{v,\phi}\|_{A_{1/32}})/m_-.
$$
须验证 $w<1/4$ 和 $P_{1/32}/(1-w)<1/64$。于是整个同伦的真实逆角在所付条带存在，且
$$
\|C\|_{A_{1/64}}\le C_*=\frac1{m_-(1-w)},\qquad
\|C_\theta\|_{A_{1/64}}\le C_{*,1}=\frac{w_1}{m_-(1-w)^3}.
$$

不取同阶 composition minus identity 的虚假小界。准确微分为
$$
\dot\theta=\frac1m I\!\left(\dot v-\frac v m\dot m\right),\qquad
\dot C|_\theta=-C^2\dot v-C_\theta\dot\theta .
$$
原 normalized mean 和非均值 Fourier 槽正交；$I$ 在非零四倍频率上收费 $1/4$，因此在 $w<1$ 时
$$
\|\dot\theta\|_{A_{1/32}}
\le\frac{\|\dot v_{\ne0}\|+w|\dot m|}{4m_-}
\le\frac{C_*}{4}\|\dot v\|_{A_{1/32}}.
$$
由整个同伦积分，
$$
d_C=\|C_\delta-C_0\|_{A_{1/64}}
\le(C_*^2+C_{*,1}C_*/4)\,|\delta|\,\|Z_v\|_{A_{1/32}}. \tag{O.1}
$$
这里 $\|Z_v\|$ 含独立 mean，实际复合的全部无限 physical tail 都包含在 Banach 条带估计中。

真实物理均值另有准确恒等式 $\langle C\rangle_\theta=1/m$，故
$$
|\Delta\langle C\rangle_\theta|
\le\frac{|\delta\langle Z_v\rangle|}{m_{0,-}m_-}. \tag{O.2}
$$
此项保留，不设为零。原外图非均值输入记为 $\mathcal Z$，区别于方向 $Z$；它满足
$$
\|\mathcal Z_\delta\|_{A^0}
 \le \|\mathcal Z_0\|_{A^0}+d_C,\qquad
\|\partial_\theta\mathcal Z_\delta\|_{A^0}
 \le \|\partial_\theta\mathcal Z_0\|_{A^0}+64d_C. \tag{O.3}
$$

## 3. 重新消费完整 nonlinear、Sobolev、mean 与外 port

把 (O.3) 及新 $U_{1/8},V_{1/8},P_{1/8},m_\pm$ 代入原完整外图的相同有序公式。原 genuine long fixed point 的两个复输入球、其 Cauchy 余宽、square-zero translation commutator 都保留；只有新的标量参数重新计算，旧解不重跑。消费者依次验证：

1. 整个新物理输入在原 $10^{-12}$ 小球及 wider complex domain 内；原 nonlinear long contraction 和 holonomy 小根仍支付。
2. 完整 $L^2$、$H^1$ DN 导数、独立 mean 与同一算子的 $H^{1/6}$ 插值。
3. 真角朝向、Hilbert 共轭、$B^1$ 乘子与 reciprocal gap；原 Cauchy 费用9、136、以及角导系数全部照实际新上界支付。
4. full moving graph lift、物理 recovery、onto nonmean even chart 和真实 mean rank。
5. 两 Robin 行、实际 high reflection、全部 low96-to-high 列、height/Robin/mean affine ports 和 mean 输出。

拟使用原已经宽放的 $E_{1/6}=2.6\cdot10^{-6}$，必须先实际证明新 Robin 缺陷仍小于该数；不能因原 $\delta=0$ 通过就继承。相应 high reflection 拟小于 $2.22\cdot10^{-5}$，low-to-high 小于 $2.35\cdot10^{-5}$，其他每项亦须实际新门通过。

真实 high reference 的 backward terminal 等于 $q_*/(-m_\delta)$；forward branch 是从根以 $M^{-1/3}$ 启动的 genuine global reference，外图允许它的任意正末值。这只给 $H^{1/6}$ 外图；正区 order1 若需要 $H^{7/6}$ physical exterior，仍必须保独立右 high port，不能凭插值扩大。

本合同没有将未知校正限制为96模。新 real-$\delta$ 外图、4650格正区 high inverse、完整 finite head Schur 与最终 nonlinear PDE 分支是不同的量词，必须依次完成。
