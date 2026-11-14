# R109 — 完整源的有限多项式线性化与指数频差尾

作者：/root（GPT-6 Astra Pro，AI 辅助）。日期：2026-11-13。

**状态：完整条件定理；原 R88/R108 两份完整小输入及通用常数的 22 项
BigInt 精确门已实际通过。** 本条给准确源与一个明确有限多项式之间的
值、Fréchet 导数及逐频耦合误差。没有执行新的源行 Jacobian、
Green 积分、46-cut、M28 后处理或闭曲面验证。

## 1. 原物理空间和完整对象

沿用 R106 的真实 source 坐标 \(x\)，置
\[
 s=r_x/r>0,\quad \ell=w_x/w,\quad z=w^2,\quad E=1+z,\quad
 c_{\rm bg}=s+|\ell|,\qquad 0<w\le1/2 .
 \tag{109.1}
\]
\(P,\bar K\) 为零均值、只含非零偶频的复 Fourier 场。
所有范数均为先逐模取径向 supremum、再求和的 Wiener 范数；
输入 joint strong 半径是
\(R=\|P\|_{\tau,1}+\|\bar K\|_{\tau,1}\)。
输出用除以正密度 \(c_{\rm bg}\) 的 weak \(\tau,0\) 范数。
不将 \(\sum\sup\) 改成 \(\sup\sum\)，也不免费增加角导数。

设
\[
 T=P_\theta,\quad C=\bar K+T,\quad U=\bar K_\theta-P,\quad
 D_0=\bar K+ET,
\]
\[
 Q=EsU^2+\ell\{EC^2-z(\bar K^2+P^2)\},\qquad
 F(a)=\frac{Q+\ell(2aD_0+a^2)}{1+D_0+a}.
 \tag{109.2}
\]
准确非均值源是 \(\mathcal N(X)=\Pi_\perp F(c(X))\)，其中 \(c\)
仍是 R33/R75 的完整复 mean 小根。其零模根方程未改。

R107 给完整二次项
\[
 c_2=-\frac12\left\langle(1+3z)\bar K^2+EP^2+
                     2E\bar KP_\theta\right\rangle,\qquad
 \|c_2\|\le\frac{29}{144}R^2<\frac14R^2,
 \tag{109.3}
\]
及在 \(R\le1/64\) 上的完整差
\[
 \|(\mathcal N-\Pi_\perp F(c_2))/c_{\rm bg}\|_{\tau,0}
 \le680R^4.
 \tag{109.4}
\]
这里完整 mean、\(c^2\) 和 inverse 均已支付；(109.4) 不是截掉完整根。

## 2. 一个可准确求值与求导的有限多项式

定义
\[
 L_2=D_0+c_2,\quad A_2=Q+\ell(2c_2D_0+c_2^2),\quad
 S_3(L)=1-L+L^2-L^3,
\]
\[
 \boxed{\mathcal N_4(X)=\Pi_\perp A_2S_3(L_2).}
 \tag{109.5}
\]
实际有限谱中心及有限谱方向下，这是系数变量中的明确有限多项式；一般
Banach Fourier 场上则是有限次数的连续多项式映射。应在完整 Laurent 代数中形成
\(Q,A_2,L_2,S_3\) 和乘积，最后才投影。所有零模以及 \(c_2^2\)
保留；逐项求值不需要对完整根作未证明的隐式替换。

其导数同样明确。对 \(\delta=(\delta P,\delta\bar K)\)，
\[
 \begin{aligned}
 \delta c_2=-\langle&
 (1+3z)\bar K\,\delta\bar K+EP\,\delta P\\
 &+E(\delta\bar K\,P_\theta+\bar K\,\delta P_\theta)\rangle,\\
 \delta D_0&=\delta\bar K+E\delta P_\theta,\\
 \delta Q&=2EsU\,\delta U+
  2\ell\{EC\,\delta C-z(\bar K\,\delta\bar K+P\,\delta P)\},\\
 \delta A_2&=\delta Q+
     2\ell\{\delta c_2(D_0+c_2)+c_2\delta D_0\},\\
 \delta L_2&=\delta D_0+\delta c_2,
 \end{aligned}
 \tag{109.6}
\]
\[
 \boxed{D\mathcal N_4[\delta]=\Pi_\perp
 \{\delta A_2S_3(L_2)+A_2(-1+2L_2-3L_2^2)\delta L_2\}.}
 \tag{109.7}
\]
\(C,U,D_0\) 可在有符号物理坐标中先组合，再作区间乘积。
(109.6) 的完整 \(\delta c_2\) 必须保留，不能固定 mean。
这些式子求的是场的 Fréchet 导数，不是径向 \(c_x\)。

### 五个有限乘子避免逐方向重复卷积

令 \(S=S_3(L_2)\)、\(H=A_2(-1+2L_2-3L_2^2)\)，定义
\[
 \begin{aligned}
 B_P&=S(-2EsU-2\ell zP),\\
 B_K&=2\ell S(EC-z\bar K+c_2)+H,\\
 B_T&=2\ell ES(C+c_2)+EH,\\
 B_J&=2EsSU,\\
 B_c&=2\ell S(D_0+c_2)+H.
 \end{aligned}
\]
则 (109.7) 等价于
\[
 D\mathcal N_4[\delta]=\Pi_\perp
 \{B_P\delta P+B_T\delta P_\theta+
   B_K\delta\bar K+B_J\delta\bar K_\theta+B_c\,\delta c_2\}.
 \tag{109.7a}
\]
这是逐项链式求导后的准确恒等式；同一材料行只需构造五个有限
Laurent 乘子，再抽取各输入/输出组合。mean 项是一个准确的标量
线性泛函乘 \(B_c\)，不删掉，也无需为每个方向重做完整多项式乘法。

在实际反射中心，写 \(P=\sum p_n\sin n\theta\)、
\(\bar K=\sum k_n\cos n\theta\)，则单位幅度的 mean 导数为
\[
 d_{p,n}=-\tfrac E2(p_n+n k_n),\qquad
 d_{k,n}=-\tfrac12\{(1+3z)k_n+Enp_n\}.
 \tag{109.7b}
\]
原中心没有的输入频率，两者都为零，但完整 Jacobian 的其他项及
(109.18) 余项仍保留。若使用复 Fourier 系数，须按 (109.6)
的零模平均直接求取，不能混用正弦幅度与复半幅。

## 3. 完整逆的第六阶尾

由 R106 的固定逐模质量证明，
\[
 \|Q/c_{\rm bg}\|_{\tau,0}\le\frac{23}{18}R^2,\qquad
 \|D_0\|_{\tau,0}\le\frac54R.
\]
所以
\[
 \|L_2\|\le R(5/4+R/4),\qquad
 \|A_2/c_{\rm bg}\|\le
 R^2(23/18+5R/8+R^2/16).
 \tag{109.8}
\]
\(\ell/c_{\rm bg}\) 是有界径向标量，不引入新的 Fourier 质量。
(109.8) 可用原相同固定质量做乘积，未交换径向 supremum 与模态和。

完整恒等式
\[
 F(c_2)-A_2S_3(L_2)=L_2^4F(c_2)
\]
与 Banach 代数逆给
\[
 \|(\Pi_\perp F(c_2)-\mathcal N_4)/c_{\rm bg}\|
 \le R^6 H(R),
\]
\[
 H(R)=\frac{(5/4+R/4)^4(23/18+5R/8+R^2/16)}
                  {1-5R/4-R^2/4}.
 \tag{109.9}
\]
分子各项非负且递增，正分母递减；在 \(0\le R\le1/64\) 上，
\[
 L_2\text{ 的比较帽}\le321/16384<1,\qquad
 H(R)\le
 \frac{895915571636097}{275960238702592}<4.
 \tag{109.10}
\]
因此
\[
 \boxed{\|(\mathcal N-\mathcal N_4)/c_{\rm bg}\|
 \le680R^4+4R^6<681R^4\quad(0<R\le1/64).}
 \tag{109.11}
\]
在 \(R=0\) 时两边为零。所有 omitted inverse 项由 (109.9) 的
完整几何级数支付；没有以有限源替代真实 PDE。

## 4. 全导数误差不需要另猜 \(Dc\)

**定理 109.1。** 在同一 joint strong 空间中，若 \(R\le1/128\)，则
\[
 \boxed{\|(D\mathcal N-D\mathcal N_4)[\delta]/c_{\rm bg}\|_{\tau,0}
 \le6450R^3\|\delta\|_{\tau,1}.}
 \tag{109.12}
\]

证明：完整根及有界逆在 R33 的复开球上全纯，(109.4) 与
(109.9) 定义两个 Banach 值全纯误差。若 \(R>0\)，对任意单位方向
\(\delta\) 使用复直线 \(X+t\delta\)。

对完整 mean 替换误差，取 \(|t|=R/3\)。该圆上半径不超过
\(4R/3<1/64\)，Cauchy 公式给
\[
 680(4R/3)^4/(R/3)=\frac{174080}{27}R^3.
 \tag{109.13}
\]
对完整四项 inverse 尾，取 \(|t|=R/5\)。其圆上半径不超过
\(6R/5<1/64\)，得到
\[
 4(6R/5)^6/(R/5)=\frac{186624}{3125}R^5.
 \tag{109.14}
\]
因 \(R\le1/128\)，
\[
 \frac{174080}{27}+\frac{186624}{3125\cdot128^2}
 =\frac{34816019683}{5400000}<6450,
\]
准确余量为 \(13980317/5400000>0\)。合并即得 (109.12)。
\(R=0\) 由全纯展开及 (109.11) 的四阶零点得到。证毕。

此 Cauchy 论证支付的是**完整 \(Dc\) 和完整 inverse 的误差**；
它没有对带符号 mean 区间端点求导，也没有将 \(\delta c_2\)
当作准确 \(\delta c\)。真正执行时，先用 (109.7) 保有符号有限部分，
再加 (109.12) 或下节更细的逐频余项。

## 5. 复杂角平移给逐频差衰减

记 \(\mathcal E=\mathcal N-\mathcal N_4\)。
假设固定中心 \(X\) 在
\[
 R_q=\sum_{n\ne0}(1+|n|)q^{|n|}
       \big(\sup_x|P_n|+\sup_x|\bar K_n|\big)\le1/128
 \tag{109.15}
\]
中有已证界，\(q>1\)。下列论证可在任一个完整真实材料行上进行，
也可用全域的真实 \(\sum\sup\) 界。

令 \(S_\zeta f=\sum_n\zeta^n f_n e^{in\theta}\)。
当 \(q^{-1}\le|\zeta|\le q\) 时，
\(\|S_\zeta X\|_{0,1}\le R_q\)。
完整 mean 根对实角平移不变；其标量根方程是整周期的角向条件，
且小根唯一。R107 的 \(c_2\) 为零模平均，同样不变。
因此 \(\mathcal N,\mathcal N_4,\mathcal E\) 对实角平移协变。

为避免对未知无限源直接使用一个未证明有界的 \(S_\zeta\)，
逐个输出 Fourier 系数作解析延拓。对单一复输入模式 \(e_n=e^{in\theta}\)
的任一 \(P\) 或 \(\bar K\) 分量，令
\[
 B_{mn}(X)=[D\mathcal E(X)e_n]_m .
\]
实角平移给
\[
 B_{mn}(S_\zeta X)=\zeta^{m-n}B_{mn}(X)\quad(|\zeta|=1).
 \tag{109.16}
\]
两边在开环域中全纯；恒等定理先给内部恒等式，再由 (109.15) 的
绝对可和控制和导数连续性取边界极限，得到 \(\zeta=q,q^{-1}\) 的式子。
当前有限谱中心亦可直接在边界邻域解析延拓。
用 (109.12) 的 \(\tau=0\) 版本及
\(\|e_n\|_{0,1}=1+|n|\)，按 \(m-n\) 的符号选择端点：
\[
 \boxed{\sup_x\frac{|B_{mn}(X)|}{c_{\rm bg}(x)}
 \le6450R_q^3(1+|n|)q^{-|m-n|}.}
 \tag{109.17}
\]
对一般径向幅度方向，右边再乘其径向 supremum；若是在固定叶上
以准确常数 \(V_I\) 归一化方向，可将该同一 \(V_I\) 作为 source
密度保留。径向单位与其他 Green 材料仍需原样支付。

在复反射子空间，正弦 \(P_n^{\sin}\) 或余弦 \(K_n^{\cos}\)
的单位幅度对应两份大小 \(1/2\) 的正负复 Fourier 方向。
输出余弦 \(m>0\) 为正 Fourier 系数的两倍，故
\[
 \boxed{|B^{\cos}_{m,n}|/c_{\rm bg}
 \le6450R_q^3(1+n)
 \{q^{-|m-n|}+q^{-(m+n)}\}.}
 \tag{109.18}
\]
这是两次 \(1/2\) 与一次输出 2 的准确换算，不另补或漏一个 2；
也不需要实共轭假设。

不同已证明的 \(q\) 对应同一 Jacobian 余项，可逐项取最小上界。
原 \(\tau\) 范数的完整算子界 (109.12) 同时保留。
有限有符号部分 \(D\mathcal N_4\) 必须在所有这些余项之外加入；
(109.17) 不是完整 Jacobian 的界，更不是 cut 的导数。

## 6. 固定全局质量与余项矩阵的求和

若要把 (109.18) 转成 \(\sigma=1/64\) 的正质量矩阵，
输入第 \(n\) 模质量是
\((1+n)e^{\sigma n}\sup|\delta X_n|\)，输出为 weak
\(e^{\sigma m}\) 权。保留相对权 \(e^{\sigma(m-n)}\)。
同一输入质量只计一次；不能将整个 T 预算复制到四十个独立轴。

由 \(e^{1/64}<64/63\)，一个 \(q>64/63\) 的所有偶频折叠权和被
\[
 \sum_{j\in2\mathbb Z}\left(\frac{64}{63q}\right)^{|j|}
 =\frac{1+(64/(63q))^2}{1-(64/(63q))^2}
 \tag{109.19}
\]
控制。其值在 \(q=2,4\) 分别为 \(4993/2945\) 与 \(4225/3713\)。
(109.19) 只给矩阵余项的一种合法求和方式；
若原 \(\sigma\) 中 (109.12) 更紧，可直接保留该整算子界。
实际 cut 的轴权、Green 物理转换、两方向 source 材料与共同域
仍要另外准确乘入，不能把本条范数擅自当作 cut 轴范数。

## 7. 同一实际 R88 中心的数值应用

R108 已用六份完整小输入证明原 \(V_I\le2^{-43}\)。
本次使用其真实账本，另读同一 R88 完整摘要；两个完整内容的
SHA256 均在程序硬核。

原 \(\sigma\) 的全域 strong 半径由
\[
 2^{-43}\left[
 \sum_{m=2,4}\text{true-linear-strong-mass}_m+
 \sum_{m=6,8,\ldots,40}\text{original-strong-mass}_m\right]
 \tag{109.20}
\]
控制。这里每份质量本身已先取径向 supremum，求和后才得全域界。
**没有拿摘要的逐行 maximum R 当作全域 \(\sum\sup\)**。

| 使用的真实范数 | 同一中心全域半径的显示近似 | 实际严格半径门 | 导数余项因子严格界 |
|---|---:|---:|---:|
| 原 \(\sigma=1/64\) | \(8.1928837631\times10^{-13}\) | \(<2^{-40}\) | 整算子 \(<2^{-107}\) |
| \(q=2\) | \(3.2772647287\times10^{-12}\) | \(<2^{-38}\) | 逐频公式前因子 \(<2^{-101}\) |
| \(q=4\) | \(1.3271446150\times10^{-11}\) | \(<2^{-36}\) | 逐频公式前因子 \(<2^{-95}\) |

这些界针对同一 R88 \(Z_0\)，即真实线性 2/4 加原候选 6..40。
不借 R101 后续真投影解的谱帽。\(q=8,16\) 未被纳入本条已证域。

例如余项的 \(m=92\leftarrow n=2\) 单位正弦/余弦幅度系数由
\[
 3(2^{-275}+2^{-283})\,c_{\rm bg}<2^{-273}c_{\rm bg}
\]
控制；这仅是 \(D\mathcal N-D\mathcal N_4\) 的系数。
\(D\mathcal N_4\)、真实方向场、Green 和 cut 归一化全都尚需加入。

## 8. 实际复算、文件与继续义务

实际程序
`computations/root_complete_source_polynomial_jacobian_gates.js`
SHA256：
`17e7cd821d29ba4c638217ea43feac6abfc35669bbe97c9218ea045a078ead8a`。
纯函数 `run` 已在 functions.exec 的 V8 中执行；
22 项精确 BigInt 比较全部通过。完整分数和六个明确余项样例在
`notes/2026-11-13-root-r109-polynomial-jacobian-exact-gates.json`。
正常复算接口为
`node computations/root_complete_source_polynomial_jacobian_gates.js --root TOPIC_ROOT --out FRESH_JSON`；
未声称已运行该 Node CLI 或创建其进程。

本条没有运行有限多项式 Jacobian 的全部真实材料行。
R108/sourcev3 对源值仍可用完整带符号 mean 区间，
无需退回到较宽的 (109.11)；
新导数工具只提供可另行准确评估的有限部分及完整误差。
恢复后须接实际 signed geometry/source、真实未知场球、
内头 \(\beta\) 与全部46个 cut；最终全频外解、全时闭面、
嵌入/reach 和固定问题加密标准均保持原要求。

依赖：[R33](R33-full-head-forcing-on-a-variable-analytic-strip.md)、
[R106](R106-physical-correlation-and-complete-mean-remainder.md)、
[R107](R107-signed-quadratic-complete-mean-centre.md)、
[R108](R108-fixed-centre-tilted-wiener-inverse.md)。
