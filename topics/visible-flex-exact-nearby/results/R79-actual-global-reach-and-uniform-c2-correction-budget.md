# R79：当前完整闭背景的全局 reach 与同一 C² 校正预算

**状态：已证明并实际完成全域有向认证；主课题仍未完成。**
`2026-11-12-actual-closed-reach-certificate.json.gz` 已达到
`complete=true`，含 1679 个主体叶和 64 个自然 graft 叶；准确覆盖检查
通过，待处理和失败队列均为空。真实远尾包含 R74 的实际双 bump、
connector、无限累积层和两个平盘。对同一准确参数族，当前 reach/直径
严格大于 0.03266314；满足本文统一 intrinsic C² 预算的校正后，仍严格
大于 0.03256961。本篇没有把尚有度量残差的闭背景称为精确等距族。

## 1. 同一对象与已经支付的实际门

固定 [R69](R69-actual-closed-approximate-exterior-and-two-held-disks.md)、
[R74](R74-actual-full-tail-robin-and-augmented-positive-cap.md) 与
[R78](R78-actual-diameter-and-whole-surface-phase-witness.md) 的同一闭近似背景
\(F_\delta:S^2\to\mathbb R^3\)。准确参数为
\[
 \delta_c=-\frac{7789866024620307}{4611686018427387904},
 \qquad |\delta-\delta_c|\le\frac1{2000000}.
 \tag{79.1}
\]
这包含实际 \(\delta_5=-7789843107295549/4611686018427387904\)。
先对原始 scalar spline germ 和 direction 作准确仿射组合，再包络此整个
实参数区间；没有先把某个新参数图物化成一份舍入 NPZ。

有限主体为 \(|r|\le3\) 的真实 R33 无限原函数；随后接 R66 的自然权
\(C^4\) graft \(3\le|r|\le25/8\)。远端是 R74 的实际双 bump、R69 的
全 connector、准确物理缩放后的无限 R72 尾，以及两个平盘。R74 的
好参数逐 \(\delta\) 选择；本文所有几何常数对该选择一致，**没有证明这项
选择随 \(\delta\) 连续**。

记一致外法向为 \(n\)，本次区间计算逐域验证
\[
 \sigma:=\inf_{S^2}F_\delta\cdot n>\frac1{10},
 \qquad K:=\sup_{S^2}\max_i|\kappa_i|<12.
 \tag{79.2}
\]
R78 对同一对象已给 \(D=\operatorname{diam}F_\delta(S^2)<2.553\)。
第 6 节证明 (79.2) 确实控制全局法向管，而不只是局部曲率半径；于是
\[
 \operatorname{reach}(F_\delta(S^2))>\frac1{12},
 \qquad \frac{\operatorname{reach}(F_\delta(S^2))}{D}
 >\frac{250}{7659}>0.0326.
 \tag{79.3}
\]
第 9 节记录完整证书及比上述粗界稍强的实际有向常数。

## 2. 真实法向与正交标架中的形算子

所有向量分量均以旋转柱坐标基 \((e_r,e_\theta,e_z)\) 表示。令
\[
 T=(-\cos\gamma\sin\beta,\ \cos\gamma\cos\beta,\ \sin\gamma),
 \qquad F_\theta=aT,\quad X=F_r,\quad X_2=F_{rr}.
 \tag{79.4}
\]
因此 \(|T|=1\)。定义
\[
 \begin{split}
 h&=-\sin\beta\,X_1+\cos\beta\,X_2^{\rm comp},\\
 v&=-\cos\beta\,X_1-\sin\beta\,X_2^{\rm comp},\\
 Q&=\cos\gamma\,X_3-\sin\gamma\,h,\qquad
 R=\cos\gamma\,h+\sin\gamma\,X_3=T\cdot X,\\
 W&=Q^2+v^2=|X-RT|^2.
 \end{split}
 \tag{79.5}
\]
这里 \(X_2^{\rm comp}\) 专指 \(X\) 的第二分量，避免与二阶导数
\(X_2=F_{rr}\) 混淆。实际计算验证 \(a>0,W>0\)，并使用
\[
 e_1=T,\qquad e_2=(X-RT)/\sqrt W,\qquad
 n=(T\times X)/\sqrt W.
 \tag{79.6}
\]
这个取向在旋转末端给向外法向，并沿整个连通面延续。

真实物理角导数包含柱坐标基的变化。准确地，
\[
 \begin{split}
 T_r={}&(-\cos\gamma\cos\beta\,\beta_r+
            \sin\gamma\sin\beta\,\gamma_r,\\
 &-\cos\gamma\sin\beta\,\beta_r-
            \sin\gamma\cos\beta\,\gamma_r,\ \cos\gamma\,\gamma_r),\\
 T_\theta={}&(-\cos\gamma\cos\beta(1+\beta_\theta)+
            \sin\gamma\sin\beta\,\gamma_\theta,\\
 &-\cos\gamma\sin\beta(1+\beta_\theta)-
            \sin\gamma\cos\beta\,\gamma_\theta,\ \cos\gamma\,\gamma_\theta).
 \end{split}
 \tag{79.7}
\]
特别是 \(1+\beta_\theta\) 中的常数 1 不能丢掉。
记 \(b=n\cdot T_\theta,c=n\cdot T_r,d=n\cdot F_{rr}\)，则正交标架
(79.6) 中的真实第二基本形式矩阵为
\[
 \boxed{\quad
 k_{11}=\frac ba,\qquad
 k_{12}=\frac{c-Rb/a}{\sqrt W},\qquad
 k_{22}=\frac{d-2Rc+R^2b/a}{W}.
 \quad}
 \tag{79.8}
\]
证明只需将参数切向量代入第二基本形式：
\(e_1=a^{-1}\partial_\theta F\)、
\(e_2=W^{-1/2}(\partial_rF-(R/a)\partial_\theta F)\)，以及
\(F_{r\theta}=a_rT+aT_r\)、\(F_{\theta\theta}=aT_\theta\)、\(n\cdot T=0\)。
该矩阵实对称，故
\[
 \max_i|\kappa_i|
 \le\max\{|k_{11}|+|k_{12}|,\ |k_{22}|+|k_{12}|\}.
 \tag{79.9}
\]
源程序还分别保存三个矩阵项的绝对值上界，不从有限特征值样本推断
连续主曲率界。

## 3. 有限主体的全角度及无限原函数预算

### 3.1 准确 scalar 分片

取所有实际 scalar knots 与它们的负反射，在 \([0,3]\) 中合并为
准确 `Fraction` 分点。每个多项式 germ 的 selector 也使用准确中点。
在所有真实 scalar spline 的共同有效域及其反射交中检查
\([-3,3]\)；没有延用无效端点外的 polynomial extrapolation。
原始共同分片为 1477 段，后续仅在一段内部作准确二分。
相邻 binary64 knots 形成的极小段仍保留，没有按浮点近似合并。

原始相位含有限个 \(4k\) 模，但 \(\sin\beta,\cos\beta,\sin\gamma,
\cos\gamma\) 及 \(F\) 是无限 Fourier 对象。下面两种方法均控制该真实
无限对象，并且都覆盖整个参数盒 (79.1)。

### 3.2 全角 Wiener 上界

记正规化径向 jet 为 \(f^{[j]}=\partial_r^jf/j!\)。在一个整实径向
区间上，对 \(0\le j\le2\) 构造非负系数幂级数
\[
 B(z)=\sum_{j=0}^2\sum_{k\ge1}|\beta_k^{[j]}|z^j,
 \quad G(z)=\sum_{j=0}^2\sum_{k\ge1}|\gamma_k^{[j]}|z^j,
 \quad A(z)=\sum_{j=0}^2|a^{[j]}|z^j.
 \tag{79.10}
\]
这里每项绝对值都是整个径向区间和参数盒上的上包络。记
\[
 \begin{split}
 C_B&=\cosh B-1,\quad C_G=\cosh G-1,\\
 D_h&=(1+C_G)\sinh B+C_B+C_G+C_BC_G,\\
 D_v&=\tfrac14\sinh G,\qquad E_h=AD_h,\quad E_v=AD_v.
 \end{split}
 \tag{79.11}
\]
所有幂级数在 jet 意义下保留到所需阶数。Wiener 范数的乘法性和
正系数三角级数给出 \(T_1\) 与 \(T_2-1\) 的两项和由 \(D_h\) 控制，
垂直项 \(T_3\) 由 \(\sinh G\) 控制。

旋转基下，水平原函数在频率 \(m\in4\mathbb Z\) 的逆矩阵为
\[
 \frac1{1-m^2}
 \begin{pmatrix}im&1\\-1&im\end{pmatrix}.
 \tag{79.12}
\]
对 \(m=0\)，每行的绝对值和为 1；对 \(|m|\ge4\)，该和为
\(1/(|m|-1)\le1/3\)。因此把两个输入水平分量的 Wiener 范数相加
即可控制每一个输出分量。垂直非零原函数乘子为 \((im)^{-1}\)，
模至多 \(1/4\)；垂直零模准确等于保存的高度 \(Z\)。于是对
\(j=0,1,2\)，全角度成立
\[
 \begin{split}
 |\partial_r^jF_1-\partial_r^ja|,
 |\partial_r^jF_2|&\le j![z^j]E_h,\\
 |\partial_r^jF_3-\partial_r^jZ|&\le j![z^j]E_v.
 \end{split}
 \tag{79.13}
\]
真实有限相位及其一阶导数另用
\(\sum|\beta_k|,\sum|\partial_r\beta_k|,
\sum4k|\beta_k|\) 和相应 \(\gamma\) 界包络。将这些量直接代入
(79.5)--(79.9) 及 \(F\cdot n\)，即得整段全角界。
实现采用 \(\cosh B-1=2\sinh^2(B/2)\)，避免极小相位的数值相消。

### 3.3 核心所需的连续角细分

若 Wiener 包络丢失角相关性，改用保存的真实有限相位在一个
\(\pi/2\) 物理周期上的有向 DFT。归一角 \(x=4\theta\) 使用
\(N=256\) 节点，角覆盖使用 \(A=512\) 个中心及半宽 \(\pi/A\)。
先准确减去圆周切向量 \(T(0,0)\)，对切向量差作 directed FFT，
再按 (79.12) 及垂直非零乘子恢复有限原函数；圆周项和真实高度项
最后准确加回。

对大复角带 \(|\Im x|\le0.32\) 和当前 polynomial germ 的外径向盘
（余量 \(0.003\)），真实切向量差的模由
\[
 A_*\,P_*e^{P_*},\qquad
 P_*\ge\sum_k(|\beta_k|+|\gamma_k|)\cosh(0.32k)
 \tag{79.14}
\]
控制。R52 的实际 Fourier alias 几何和及无限尾预算对它适用。
径向导数尾另乘 \(j!/0.003^j\)，角度使用整个中心半格，而不只节点。
具体地，有限系数的角间隙费用为
\(\sum_k|c_k||k|\pi/A\)，无限尾在更大内带
\(|\Im x|\le\pi/A\) 上支付。这些费用逐 \(F,F_r,F_{rr}\) 分量加回。

每个实际有限相位在整角格上的 \(\sin,\cos\) 由有向三角函数包络，
其真实物理角导数含 \(4k\) 因子。因而 (79.7) 和 (79.8) 的每个
分母、每次平方、每个平方根都在整个径向格、整个角格、整个参数盒上
成立。平方根端点经 Arb 求值后再向外转成 binary64；不能依赖普通
`libm` 的正确舍入假设。

实际 D4 反射允许只存归一角半周期的格；所有角均由反射和四重旋转覆盖。
若任一连续格未达到 (79.2)，程序准确二分径向区间。到深度门仍失败
则存入失败队列，并禁止 `complete=true`。

## 4. 自然 graft、反射及接缝

graft 使用 R66 保存的同一 \(\log a\)、\(c=z'/a^2\)、
\(a^{-3}\beta\)、\(a^{-2}\gamma\) 四阶入口 jet 及同一个 \(1/8\)
长度。真实函数是
\[
 \beta=a^3\chi P_\beta,\quad \gamma=a^2\chi P_\gamma,
 \quad z'=a^2c,\qquad
 \chi(u)=(1-u)^5(1+5u+15u^2+35u^3+70u^4).
 \tag{79.15}
\]
它在入口准确匹配主体，在出口使两个相位的 0--4 阶径向 jet 全零。
径向高度按实际积分定义，不能把一个 Taylor 截断当作高度本身。
本次每个 graft 格使用 R66 已付的真实整段高度包络，以及准确
\(z',z''\)，再用 (79.10)--(79.13) 和形矩阵 (79.8) 支付支撑、曲率。
原始 64 个准确偏移区间完整覆盖 \([0,1/8]\)，需要时仍只作准确二分。

主体及 graft 的负侧由
\[
 F(-r,\theta)=P_zF(r,\theta),\qquad P_z=\operatorname{diag}(1,1,-1)
 \tag{79.16}
\]
定义。由于 \(F_r(-r)=-P_zF_r(r)\)、\(T(-r)=P_zT(r)\) 和
\(\det P_z=-1\)，(79.6) 给 \(n(-r)=P_zn(r)\)。所以支撑值相同、
主曲率绝对值相同，外法向与正侧一致。角反射同理；没有在反射后
随意翻转法向来强造正支撑。

所有接缝至少 \(C^2\)，两侧有限导数极限一致，因此格上曲率及支撑
界延至接缝。无限尾接平盘的 \(C^2\) 极限由 R69 的真实全部层证明；
轴心属于平盘的普通 Cartesian chart，不需要退化 Sturm 坐标通过轴心。

## 5. R74 真双 bump、全 connector、无限尾和平盘

令 \(a_*,z_*\) 为 \(r=25/8\) 的真实入口。当前完整包给出安全量
\[
 a_*+\epsilon_b<6.563766\,10^{-6},\qquad
 z_*-\epsilon_b>0.9661986699,
 \tag{79.17}
\]
其中 \(\epsilon_b\) 是 R74 的准确 Cartesian 位移上界，严格小于
\(2^{-100}\)。这个小位移不能单独代付曲率：对真实双 bump，R74 已证
\[
 |\psi'|\le15/16384,\quad |\psi''|\le3/16,
 \quad\widetilde\omega=\omega+\psi'>0,
 \quad|\kappa_i|<1/5.
 \tag{79.18}
\]
其准确公式是
\(|\kappa_\theta|\le(4\widetilde\omega)^{-1}\)、
\(|\kappa_s|\le(1+|\widetilde\omega_u/\widetilde\omega^2|)
/(4\widetilde\omega)\)。未改常径向段的曲率界、整个 connector 的
\(5/6\) 界，以及真无限尾的 \(1/8\) 界均来自 R69 的实际对象。
两个 bump 之后 connector 和尾只作竖直平移，因此其曲率保持。

把 \(a^+=a_*+\epsilon_b\)、\(z^-=z_*-\epsilon_b\) 作为共同包络，
径向和 connector 的 \(\omega\ge9/10\)，且向外 \(a\) 递减、高度递增。
它们的真实支撑为
\[
 \frac{a^2+4z\omega}{\sqrt{a^2+16\omega^2}}
 \ge\frac{z^-}{\sqrt{1+(a^+/(4\cdot9/10))^2}}.
 \tag{79.19}
\]
R69 对全部无限尾的准确物理缩放给
\(\max\{|W|/a,|W_a|\}<0.07152558<1/8\)。于是
\(W_*:=a^+\cdot0.07152558\) 包络真实图斜率。即使不使用其正号，
\[
 F\cdot n=\frac{z+aW}{\sqrt{1+W^2}}
 \ge\frac{z^- -a^+W_*}{\sqrt{1+W_*^2}}.
 \tag{79.20}
\]
平盘的支撑为其正高度、曲率为零。反射负帽保留这些数值。
源程序用实际更紧的有向入口和斜率界得到整个远域
\[
 F\cdot n>0.96619866999>9/10,\qquad |\kappa_i|\le5/6<1.
 \tag{79.21}
\]
这里覆盖所有平台、过渡、无穷累积层、两平盘及其接缝，不把一个有限
切口上的 \(W_a\) 值当作整条真尾的曲率界。

## 6. 正支撑控制正、负法向管的全局单射

下面给出独立证明，范围包括一般闭连通 \(C^2\) 浸入；不要求 \(C^3\)
或曲率导数。

**引理。** 设 \(F:M\to\mathbb R^3\) 是紧、连通、无边界的 \(C^2\)
浸入，有全局单位法向 \(n\)，满足
\(F\cdot n\ge\sigma_0>0\)、\(\max_i|\kappa_i|\le K_0\)。那么 \(F\)
是嵌入，且
\[
 \operatorname{reach}(F(M))\ge\min\{\sigma_0,1/K_0\}.
 \tag{79.22}
\]
若 \(K_0=0\)，将 \(1/K_0\) 理解为无穷；实际上闭面不会全平。

**证明。** 任取 \(0<b<\min\{\sigma_0,1/K_0\}\)。对**两个符号**的
\(-b<t<b\)，令 \(F_t=F+tn\)。形算子满足
\[
 dF_t=dF(I-tS),\qquad F_t\cdot n=F\cdot n+t>0.
 \tag{79.23}
\]
所以 \(F_t\) 是 \(C^1\) 浸入，且其切空间仍与同一个 \(n\) 正交。
从 \(t=0\) 连续延续的法向没有改变符号，因为 \(I-tS\) 无零特征值。
其径向投影 \(\pi_t=F_t/|F_t|\) 的微分秩为 2：若一个非零切向量
投影为零，则 \(dF_t(v)\) 与 \(F_t\) 平行，点乘 \(n\) 与
\(F_t\cdot n>0\) 矛盾。故 \(\pi_t\) 为局部微分同胚。

紧性使 \(\pi_t\) 为真映射；其像既开又闭且非空，故覆盖 \(S^2\)。
紧连通局部微分同胚是有限覆盖，而 \(S^2\) 单连通，所以该覆盖只有
一层。于是每个 \(F_t\)，包括 \(F_0\)，都是一张全局径向嵌入。

这一步还不足以说明不同 \(t\) 的面不相交。由联合反函数定理，
映射 \((p,t)\mapsto(\pi_t(p),t)\) 是局部 \(C^1\) 微分同胚；前述
各层唯一性使其局部逆拼成全局 \(C^1\) 函数 \(p=p(t,u)\)。写
\[
 F_t(p(t,u))=R(t,u)u,\qquad u\in S^2.
\]
固定 \(u\) 求导，再点乘 \(n(p(t,u))\)，切向项消去，给
\[
 \partial_tR(t,u)=\frac1{u\cdot n(p(t,u))}>0,
 \tag{79.24}
\]
分母正号来自 \(F_t\cdot n=R,u\cdot n>0\)。故同一射线上的半径随
\(t\) 严格递增。任何不同 \((p,t)\)、\((q,s)\) 的法向偏移点若相同，
就有同一射线、同一半径；(79.24) 先迫使 \(t=s\)，再由单层嵌入迫使
\(p=q\)。所以整个 \(M\times(-b,b)\) 法向管单射。

最后，任一点与紧集 \(F(M)\) 的距离小于 \(b\)，都有最近点；最近点
的一阶必要条件给它的法向表示 \(F(p)+tn(p)\)，且 \(|t|<b\)。
法向管单射保证最近点唯一。令 \(b\) 递增到右端即得 (79.22)。证毕。

这个论证同时排除远处不同曲面部分的靠近，包含负 offset；没有把
“主曲率有界”单独写成 reach 下界。把当前全域 (79.2) 代入即得 (79.3)。

## 7. 统一 Cartesian C² 校正门与各时间的法向

令 \(S=F_\delta(S^2)\)，对一般 Cartesian 向量场 \(V:S\to\mathbb R^3\)
取
\[
 G(x)=x+V(x),\qquad
 \|V\|_\infty\le a_0,\quad
 \|dV\|_{\rm op}\le b_0<1,\quad
 \|\nabla_S^2V\|_{\rm op}\le c_0.
 \tag{79.25}
\]
二阶范数指使用参考面 Levi-Civita 联络、值域平直联络的向量 Hessian：
\(\nabla_S^2V(u,v)=D_udV(v)-dV(\nabla^S_uv)\)。它是双线性 operator
范数，**不是**在退化尾坐标中的普通系数最大值；后续 PDE 重建必须
真实支付这个范数转换。

沿 \(G_\lambda=x+\lambda V\)、\(0\le\lambda\le1\)，
\(|dG_\lambda u|\ge(1-\lambda b_0)|u|\)，故保持浸入。取从参考法向
\(n\) 连续延续的单位法向 \(n_\lambda\)。由
\(n_\lambda\cdot(u+\lambda dV(u))=0\)，有
\(|P_{T_xS}n_\lambda|\le\lambda b_0<1\)。连续性排除负法向分支，因此
\[
 |n_\lambda-n|\le\sqrt2\lambda b_0
 \le\frac{2\lambda b_0}{1-\lambda b_0}.
 \tag{79.26}
\]
R78 的准确中心反演对参考面给 \(\sup|x|=D/2\)。所以统一地
\[
 G\cdot n_G\ge\sigma-a_0-\frac{Db_0}{1-b_0},
 \qquad D_G\le D+2a_0.
 \tag{79.27}
\]
从二阶导数减去新切向量 \(dG(\nabla^S_uv)\) 后，
\[
 \mathrm{II}_G(dG(u),dG(v))
 =n_G\cdot\bigl(\mathrm{II}_S(u,v)n+\nabla_S^2V(u,v)\bigr).
 \tag{79.28}
\]
结合 \(dG\) 的最小奇异值下界即得
\[
 K_G\le\frac{K+c_0}{(1-b_0)^2}.
 \tag{79.29}
\]
只要 (79.27) 的支撑下界为正，第 6 节适用于每个 \(G_\lambda\)，
而不须预先假设校正后是嵌入。

取与 R78 相同的端点位移预算，并同时规定
\[
 \boxed{a_0=b_0=c_0=1/1000.}
 \tag{79.30}
\]
仅代入 \(\sigma>1/10,K<12,D<2553/1000\) 已给
\[
 \begin{split}
 \sigma_G&>\frac{217}{2250}>0.09644,\\
 K_G&<\frac{12001000}{998001},\qquad D_G<\frac{511}{200},\\
 \operatorname{reach}(G(S))&>\frac{998001}{12001000}>0.08315,\\
 \boxed{\quad
 \frac{\operatorname{reach}(G(S))}{D_G}
 >\frac{998001}{30662555}>0.03254>0.03.
 \quad}
 \end{split}
 \tag{79.31}
\]
支撑下界大于倒曲率下界，故没有遗漏取最小值这一步。

若有一个时间族的参考像均为当前像的环境旋转，其 \(D,\sigma,K\)
相同。对每个时间分别拉回 (79.25) 的 intrinsic 范数；若三个预算对
时间一致，则 (79.31) 对所有时间一致。取向始终由同一
\(\lambda\)-同伦从对应参考外法向延续；没有逐时间任意改法向符号。
这项结论不要求 \(V\) 先是法向场，也没有引入任何曲率导数。

R74 的两个平盘之并给 \(\operatorname{diam}F(H)>1.932397339\)。
即使仅使用 (79.30) 的点值界，
\[
 \operatorname{diam}G(H)>1.930397339>\tfrac34(2.555)
 >\tfrac15D_G.
 \tag{79.32}
\]
实际固定 H 仍须满足 \(V|_H=0\) 及 R71 的同一局部修复条件；
尺寸大不等于已经固定。

## 8. 与可见位移及主完成的准确关系

R78 已从一个见证点到**整张曲面**的有向距离得到当前相位图之间的
Hausdorff 下界 \(>0.13\)，没有使用 reach。若未来这两个端点各满足
(79.30)，三角不等式给真实端点 Hausdorff 距离 \(>0.128\)，新初始
直径 \(<2.555\)，因此严格大于 \(0.05D\)。第 7 节同时保证全程
reach 比例 \(>0.03\)，两项是同一对象和同一校正预算。

当前参考相位像本身是环境旋转，不能据此宣称严格非全等；当前闭背景
也仍有度量残差。完整非径向强逆、有限低块、保帽重建、非线性收敛、
精确同一度量族和严格非全等性仍须按 open 项逐项闭合。本结果支付
的是全域几何门及其可执行稳定邻域，没有把这些尚欠输入改成已证结论。

## 9. 重放、准确覆盖与完整实际记录

源：`scripts/fourfold_phase_reach_certificate.py`。固定命令：

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_phase_reach_certificate.py \
  --out notes/2026-11-12-actual-closed-reach-certificate.json.gz
```

中断时只有使用同一 source、全部 dependency/input hash、参数区间、
精度、节点和角格的 `--resume` 才可延续。程序每十次尝试保存全部
准确待处理区间，既不丢失败格，也不以部分报告拼接成完整结论。
本次已对主体 \([0,3]\) 与 graft \([3,25/8]\) 分别作 Fraction
无缝、无重叠覆盖检查，再连同第 5 节真远域取全局最小/最大值。
报告保存每个叶的实际方法、准确端点、三项形矩阵界、支撑、面积分母和
无限原函数误差；最终全局界在 192-bit Arb 中向外聚合。

实际运行使用 192-bit Arb、Q256 无限原函数和需要时的 512 个连续角盒。
1945 次尝试给出 1679 个主体叶和 64 个自然 graft 叶，待处理与失败均为
零，总运行约 4004 秒。整个报告保存上述所有叶，未以样本替代连续覆盖。
向外放宽后的便于引用常数如下；每个端点都严格包住报告中的有向数值。

| 量 | 当前完整闭背景 | intrinsic 三档均不超过 0.001 的校正后 |
|---|---:|---:|
| 正支撑下界 | \(>0.5777371941815192\) | \(>0.5741816620724809\) |
| 主曲率绝对值上界 | \(<11.992097849862842\) | \(<12.017120072888546\) |
| 直径上界 | \(<2.552976576929253\) | \(<2.554976576929253\) |
| 全局 reach 下界 | \(>0.08338824553632519\) | \(>0.08321461331289093\) |
| reach/直径下界 | \(>0.03266314555718544\) | \(>0.03256961886237878\) |

源、完整报告、本文及固定四标记的条件迁移说明，统一列于
`notes/2026-11-12-R79-actual-global-reach-ready-manifest.json`。其中每个文件
都记录完整 SHA256；本篇实际源为
`71b55617d7133966ac2f917cb5acd3a1f47e6071f692f4ca50563ef498cdea21`。
固定四标记的说明只在后续取得一个保帽精确零解后适用；本次全域几何
认证并未免除这个非线性零解及其完整强逆、低块条件。
