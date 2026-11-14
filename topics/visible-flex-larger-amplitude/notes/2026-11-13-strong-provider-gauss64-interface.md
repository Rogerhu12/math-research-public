# 强前缀 profile 的 64 点 Gauss 原函数：严格参考规则与两阶误差接口

日期：2026-11-13。本条继续固定 g 的 mean/finite-field 比较。M28 尚未启动，本条不改原 provider/MJS、不重解 q096，不把下面的参考规则证书冒称为完整 neck 的区间包围。

## 1. 读源发现的真实区分

alternative-neck-flatturn.py 的 integral 对每个 ramp/flat 子段用固定 64 点 Gauss。alternative-neck-provider.py 的 piece_jet 与 strong_angle_boost.py 同时返回：

\[
 \widehat a(s)=a_0+\hbox{有限 Gauss 原函数},\quad
 a_1(s)=\sin\phi,\quad a_2(s)=\cos\phi\,\phi_s.
\]

有限 Gauss 原函数的导数不严格等于后两项，即使忽略 binary64 运算误差也是如此。所以不能直接把原三元组的三个独立采样界当作同一精确 C² 函数的 jets。严格路线应先选明同一解析 profile，再同时包围原函数近似、Gauss 表偏差、浮点求值和接缝/参数表示误差。当前 full-mean 条件消费器确实要求同一个 a,a_s,a_ss；它没有付掉这一层。

当前 pinned 入口里 Gauss 由 alternative-neck-excursion.py 的下式生成：

    gx,gw=np.polynomial.legendre.leggauss(64)
    gu=(gx+1)/2

各子段使用 width/2 乘以 gw 加权和。下文把权重记成 gw/2；这是精确表达式的记法，未修改原 NumPy 运算次序。

## 2. 实际完成的参考 Gauss64 证书

新源 strong_provider_gauss64_exact.js 使用独立 exact rational helper strong_exact_rational_fast.js。后者只在 Euclid gcd 前精确抽掉两个整数的 2 因子，依据
\[
 \gcd(2^rA,2^sB)=2^{\min(r,s)}\gcd(A,B),\quad A,B\ {\rm odd}.
\]
它与原有理类的 49 组四则、零/符号和一个 512-bit dyadic case 已逐值核对。没有数值舍入或改变域门。

准确整数多项式为
\[
 2^{64}P_{64}(x)=
 \sum_{k=0}^{32}(-1)^k
 \binom{64}{k}\binom{128-2k}{64}x^{64-2k}.
\]
Math.cos 只提出初始区间；每个端点符号、112 次二分和最终不交性均使用 BigInt 有理数。32 个正根盒反射后给 64 个互不相交的严格符号变化盒，全部在 (−1,1)。次数 64 因而保证每盒恰有一根且无遗漏。

对导数，逐多项式系数验证了
\[
 P_n'=\sum_{\substack{k<n\\n-k\ {\rm odd}}}(2k+1)P_k
\]
的再次求导展开。二阶导数展开的系数全为非负。由 \(|P_k(x)|\le1\) 得
\[
 |P'_{64}|\le2080,\qquad
 |P''_{64}|\le2162160,\quad -1\le x\le1.
\]
这里 \(|P_k|\le1\) 也可直接由 Laplace 积分
\[
 P_k(\cos\theta)=\frac1\pi\int_0^\pi
 (\cos\theta+i\sin\theta\cos t)^k\,dt
\]
得到：括号模不超过 1，二项式展开给同一个 Legendre 多项式。

在每个根盒中心准确评价 P′，用 2162160 乘盒半径扩张，确认不跨零。归一到 u∈[0,1] 的节点和权为
\[
 u_i=(1+x_i)/2,\qquad
 w_i=\frac1{(1-x_i^2)P'_{64}(x_i)^2}>0.
\]
最终输出区间向外舍入到 128-bit dyadic，同时保存未舍入区间的 SHA。根盒端点仍保原准确有理数。

权公式与精确度无需数值拟合：以 \(l_i(x)=P_{64}(x)/((x-x_i)P'_{64}(x_i))\)，Christoffel–Darboux 恒等式积分给 \(\int_{-1}^1l_i=2/((1-x_i^2)P'_{64}(x_i)^2)\)。对次数≤127 的 p，除法 p=P64 q+r，deg q≤63、deg r≤63；P64 与 q 正交，剩余 r 由 l_i 插值。因此原归一规则对所有次数≤127 多项式精确，且正权之和为 1。

本次实际执行额外检查 normalized x^0、x²、x^64、x^126 的区间加权和分别包含 1、1/3、1/65、1/127，避免归一因子错误。共 11 组门全部通过，最终纯 JavaScript isolate 计算 2.201 秒，0 Node/RHS/BVP。原慢 gcd 实现的首次纯代数尝试曾由代理主动终止，未返回证书；最终证书独立重算，不使用未完成结果。

**这是真 Gauss64 参考规则的证书，实际 NumPy 表尚未读取。**

## 3. 相位多项式给原函数及两阶导数的明确界

在每个原 ramp/flat 子段，φ 关于整段归一变量 u 的次数≤4。设先严格付
\[
 |\phi|\le\Phi,\quad|\phi_u|\le P_1,\quad
 |\phi_{uu}|\le P_2,\quad|\phi_{uuu}|\le P_3.
\]
令 S31 是 sin 的 31 次 Taylor 多项式。S31(φ(u)) 的次数≤124，真 Gauss64 对它精确。对 \(R=\sin\phi-S31(\phi)\)：
\[
 |R|\le T_0=\Phi^{33}/33!,\qquad
 |R_u|\le T_1=P_1\Phi^{32}/32!,
\]
\[
 |R_{uu}|\le T_2=
 P_1^2\Phi^{31}/31!+P_2\Phi^{32}/32!.
\]
这些界也适用于任意部分子段，不依赖离散采样。

对于子段 left≤u≤right，写 h=right−left≤1、w=u−left。准确有限规则给原函数
\[
 G(u)=w\sum_iw_i\sin\phi({\rm left}+wu_i),
\]
而准确积分 \(I(u)=\int_{\rm left}^{u}\sin\phi(x)\,dx\)。对剩余 R 使用正权和为 1：
\[
 |G-I|\le2hT_0,\qquad
 |G_u-I_u|\le2T_0+hT_1,
\]
\[
 |G_{uu}-I_{uu}|\le3T_1+hT_2.
\]
将整段物理长度记成 L，s=s0+Lu，完成子段的原函数常数累加后：
\[
 |\Delta a|\le2LT_0,\quad
 |\Delta a_s|\le2T_0+T_1,\quad
 |\Delta a_{ss}|\le(3T_1+T_2)/L.
\]
后两项是 variable-limit Gauss 原函数的真导数与解析 derivative 的差，不只是积分值误差。

本产物提供条件参数 \((\Phi,P_1,P_2,P_3)=(8/5,4,65,3300)\) 的准确有理数常数：
\[
 |\Delta a|<1.255\times10^{-30}L,\quad
 |\Delta a_s|<5.299\times10^{-29},\quad
 |\Delta a_{ss}|<5.135\times10^{-27}/L.
\]
原 frozen neck 的每个实际 phase panel 还没有在本条核过这四项，actual_phase_bounds_verified 保持 false。Hermite/原 cubic 速度的半径积分是低次多项式，应按原式另算，不需要套相位模型。

## 4. 实际有限表到参考表的单独误差

令 \(\hat u_i,\hat w_i\) 是原 NumPy 表的精确 binary64 实数，设已严格求出
\[
 \eta=\max_i|\hat u_i-u_i|,\qquad
 \omega=\sum_i|\hat w_i-w_i|.
\]
要求原节点仍在 [0,1]；不将原权和重新归一成 1。

对 \(|\phi_u|\le4,|\phi_{uu}|\le65,|\phi_{uuu}|\le3300\)，有
\[
 |f_u|\le4,\quad |f_{uu}|\le81,\quad|f_{uuu}|\le4144,
 \quad f=\sin\phi.
\]
比较部分积分的节点/权，并对 u 真求导，得到完整单段的额外界：
\[
 |\widehat a-a_{\rm exact\ Gauss}|
 \le L(\omega+4\eta),
\]
\[
 |\widehat a_s-(a_{\rm exact\ Gauss})_s|
 \le5\omega+89\eta,
\]
\[
 |\widehat a_{ss}-(a_{\rm exact\ Gauss})_{ss}|
 \le(89\omega+4476\eta)/L.
\]
证明只需对 kernels f、f+wuf′、2uf′+wu²f″ 依节点分别微分；其节点 Lipschitz 常数为 4h、8h+81h²、8+324h+4144h²。对已完成 ramp 子段仅累加原函数误差，因各子段宽之和为 1，上述整段界仍成立。

独立准备源 strong_provider_gauss64_table.py 会记录本地原 gu 和 gw/2 的全部 binary64 有理数、数组 SHA、NumPy/Python/函数文件身份。它不导入 Flow、不求新 BVP。其生成值只能证明**该次观察的运行环境**，不能只因版本相同就冒称已恢复旧 CI 的位同表。

参考证书的 compareTable 入口随后给全部 64 项的 η/ω。当前表提取器和真实 table comparison 尚未执行：

    python computations/strong_provider_gauss64_table.py --out <fresh-local-table.json>
    node computations/strong_provider_gauss64_exact.js --certificate <gauss64-certificate.json> --table <fresh-local-table.json> --out <fresh-table-comparison.json>

## 5. 没有付掉的内容

这里没有把多个段的 rounded a0、s0、L、asin/atan、K 与 phase slope 的差、浮点 sin/matmul 求值误差或精确接缝自动消掉。phase-integral 理想 profile 与原计算三元组的对应必须有明确的同一 g 解释和误差记录；不能因为其预期很小就改标签。

严格 all-s neck 盒还需原完整 segment 参数及其身份、每 panel 的相位多项式区间、原输入到 exact analytic profile 的映射，以及此前 mean/finite-field 所需的连续域。此参考规则与条件尾项只是其中可先实际完成的一层。原同 g M28 的完整求解仍优先，不以此 prepared table 观察作为运行前审批门。
