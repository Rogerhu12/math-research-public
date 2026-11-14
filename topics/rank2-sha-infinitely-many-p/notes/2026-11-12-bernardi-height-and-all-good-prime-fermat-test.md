# Bernardi 型整高度与任意好素数的全局 Fermat 商证书

日期：2026-11-12。**状态：已证明，已独立复核；R131。实际测试的无穷非零性仍开。**

固定 \(E:y^2=x^3-17x\)、\(F=\mathbb Q(\sqrt{-15})\)，以及 R119 的真实
\(L/F\)、\(\Gamma=C_p\)、非挠 \(Q\in A(F)\)，其中
\(A=\ker(\operatorname{Res}_{L/F}E\to E)\)。
假设 \(p\ge7\)、\(p\ne17\)，并删去整除固定有限群
\(\Sha(E^{(-15)}/\mathbb Q)\) 阶数的素数。这里不要求 \(p\) 在 \(F\) 或
\(\mathbb Q(i)\) 分裂，不要求普通约化。

本文构造一个具体、整的全局 \(p\) 进双线性高度，使 R127 的两个 Fermat 商矩
测试可用于这些全部好素数，包括 R126 的无穷输入。证明只用该高度的二次性、
Galois 不变性和整性；不预设它非退化。

## 1. 一份固定有理 sigma 及其充分收敛盘

取 \(t=-x/y\)、\(\omega=dx/(2y)=f(t)\,dt\)。在本短模型的形式盘中，
\[
 x(t)=\frac{1+\sqrt{1+68t^4}}{2t^2}
       \in t^{-2}+t^2\mathbb Z_p[[t]],\qquad
 f(t)=\frac1{\sqrt{1+68t^4}}\in1+t^4\mathbb Z_p[[t]].
 \tag{1}
\]
令 \(D=f(t)^{-1}d/dt\)。直接微分给
\[
 D^2\log t=68t^2-t^{-2},\qquad
 g(t)=-x(t)-D^2\log t\in t^2\mathbb Z_p[[t]].
 \tag{2}
\]
定义零常数项的两次形式积分
\[
 H_\sigma(t)=\int_0^t f(s)
                  \left(\int_0^s g(r)f(r)\,dr\right)ds,
 \qquad \sigma_0(t)=t\exp H_\sigma(t).
 \tag{3}
\]
于是
\[
 D^2\log\sigma_0=-x,\qquad
 \sigma_0(t)=t-\frac{85}{12}t^5+\cdots\in t\mathbb Q[[t]].
 \tag{4}
\]
所有对象先在特征零有理形式级数中定义。(4) 的初项也可从
\(g(t)=-85t^2+\cdots\) 直接得到。因 \(f,g\) 为偶级数，\(H_\sigma\) 为偶级数，
\(\sigma_0(-t)=-\sigma_0(t)\)。
这正是短模型、补方向 \(\eta=x\omega\) 的 Bernardi sigma。

这里不需要 \(\sigma_0\) 的全部系数都 \(p\) 整。
若 \(H_\sigma(t)=\sum_{n\ge4}h_nt^n\)，(3) 每项至多经历两次除以不大于 \(n\)
的正整数；其余乘子在 \(\mathbb Z_p\)。因此
\[
                       v_p(h_n)\ge-2\lfloor\log_p n\rfloor.
 \tag{5}
\]
对任一不分歧有限扩张 \(K/\mathbb Q_p\)、\(t\in p\mathcal O_K\)，
每项的赋值至少 \(n-2\lfloor\log_p n\rfloor\)，趋于无穷且对 \(p\ge7,n\ge4\)
不小于 \(4\)。故
\[
 H_\sigma(t)\in p^4\mathcal O_K,\qquad
                 \frac{\sigma_0(t)}t\in1+p^4\mathcal O_K.
 \tag{6}
\]
这同时证明所用点处的收敛、非零性及需要的模 \(p^2\) 近似。没有将超奇异 sigma
宣称在整个几何形式群上整或收敛。

## 2. 形式恒等式确实给全局二次高度

在复形式参数 \(z=\int\omega\) 中，(4) 的解是具有
\(g_2=68,g_3=0\) 的 Weierstrass sigma 与 \(z=z(t)\) 的复合：
它满足同一个微分方程、奇性和一次项。因而其乘法、加法恒等式是
\(\mathbb Q\) 上的形式恒等式，特别有
\[
 \frac{\sigma_0(P+R)\sigma_0(P-R)}
       {\sigma_0(P)^2\sigma_0(R)^2}=x(R)-x(P),
 \tag{7}
\]
以及
\[
                  \sigma_0(mP)=\sigma_0(P)^{m^2}f_m(P),
 \tag{8}
\]
其中 \(f_m\) 为相应规范的除法多项式；任何固定符号不影响 Iwasawa 对数。
在 (6) 的共同收敛盘中，这些恒等式成立于实际点。

令 \(\mathfrak d(P)\) 为最小模型上 \(x(P)\) 的分母理想平方根，
\(d_w(P)=\operatorname{ord}_w\mathfrak d(P)\)。
下面明确坏位也成立的理由。对任一有限位 \(w\)，在最小模型的
Néron 恒等组件 \(\mathcal E^0\) 上，\(d_w(P)\) 正是点截面与零截面
的交数：形式盘中由 \(x=t^{-2}\cdot\text{unit}\) 得到，盘外均为零。
在 \(\mathcal E^0\times\mathcal E^0\) 上，\(x(R)-x(P)\) 的 Cartier 除子是
\[
 (P+R)^*(O)+(P-R)^*(O)-2P^*(O)-2R^*(O).
\]
没有额外的垂直分量：特殊纤维的 generic \(x(R)-x(P)\) 非零，
而恒等组件的特殊纤维及其乘积均几何连通、光滑且不可约。
这也适用于剩余特征 \(2\)，在那里两对角线的特殊纤维可以重合，
但 Cartier 重数已经保留。取点截面的交数即给
\[
 d_w(P+R)+d_w(P-R)-2d_w(P)-2d_w(R)
                         =v_w(x(R)-x(P)).                 \tag{8a}
\]
这里先取 \(P,R,P\pm R\ne O\)，其余情形通过二次延拓处理。

乘法的垂直项也可以直接核清，不能只假定 \(m\) 在剩余域是单位。
标准恒等式 \(x([m]P)=\phi_m(P)/f_m(P)^2\) 中，
\(t^{2m^2}\phi_m\) 是常数项为 \(1\) 的整形式单位。
又 \(x([m]P)t([m]P)^2\) 是整形式单位。因此
\[
 \left(\frac{f_m(P)t(P)^{m^2}}{t([m]P)}\right)^2
   =\frac{t(P)^{2m^2}\phi_m(P)}{x([m]P)t([m]P)^2}
\]
为形式单位。正规整环中的比值本身也是单位，且其常数项为 \(1\)，
因为 \(f_m\sim m t^{1-m^2}\)、\(t([m]P)\sim mt\)。
它确定了零截面附近的垂直系数为零；恒等组件特殊纤维不可约，
故在整个 \(\mathcal E^0\) 上没有额外垂直修正。于是
\[
                 d_w(mP)-m^2d_w(P)=v_w(f_m(P)).             \tag{8b}
\]
特别是 \(w\mid m\) 时，\(m\) 的真实赋值已经包含在右边，没有删去它。
这些证明涵盖本题的坏位 \(2,17\)，并未只核好约化位。

令 \(B(P)\) 表示下面 (10) 的花括号，先在全部 \(p\) 处 formal、
全部坏位恒等组件的共同子群上定义。由 (7)、(8a)，
\(B(P+R)+B(P-R)-2B(P)-2B(R)\) 等于
\[
 \sum_{v\mid p}\log_pN_{L_v/\mathbb Q_p}(x(R)-x(P))
 -\sum_{w\nmid p}v_w(x(R)-x(P))\log_p\#k_w=0.
\]
这是全局有理 norm 的乘积公式；\(p\) 上理想因子因
\(\log_p p=0\) 不贡献。用 (8)、(8b) 同样得到
\(B(mP)=m^2B(P)\)。共同子群在 \(p\) 处无挠，故所用非零点的
除法多项式不为零；在零点定义 \(B(O)=0\)。取共同整数倍后，
此齐次性同时证明 (10) 对允许的 \(M\) 独立，并将平行四边形律
延拓到全部 \(E(L)\)。这与 Mazur–Stein–Tate §§2.3–2.8
的地方公式证明一致，解析输入已由 (6)–(8) 单独支付。

特别地，这一步没有使用 Frobenius 的普通单位根。原 Bernardi 高度的
二次性也在 Stein–Wuthrich（2013）§4 开头、印页 1769–1770
对 \(\eta\) 方向的高度中明确表述；该文 §4.3、印页 1772
随后讨论超奇异向量高度，并非这里 sigma 定义的原位置。

## 3. 可用与 p 互素的整数倍，保全部地方的整性

\(L/F\) 在 \(p\) 不分歧，\(F/\mathbb Q\) 在 \(p\ge7\) 也不分歧。
若 \(p\) 在 \(F\) 分裂，\(L\) 的 \(p\) 处剩余次数是 \(1\) 或 \(p\)。
若 \(p\) 在 \(F\) 惰性，理想 \((p)\) 有有理生成元，所以其环类 Artin 元平凡，
\(p\) 在 \(L/F\) 完全分裂，剩余次数为 \(2\)。

对 \(p\ge7\)，有理二挠点使 \(a_p\) 偶，而 Hasse 界给
\(|a_p|<p-1\)，所以 \(a_p\not\equiv\pm1\pmod p\)。
因此，对上述 \(f\in\{1,2,p\}\)，
\[
                 \#E(\mathbb F_{p^f})\equiv1-a_p^f\ne0\pmod p.
 \tag{9}
\]
这也包括超奇异 \(a_p=0\) 的情形。
故存在与 \(p\) 互素的一个整数 \(M\)，把所有 \(E(L)\) 点同时送入全部 \(p\) 处形式群；
再乘一个整除 \(12\) 的组件指数，保证坏位的恒等组件条件。

定义
\[
 H_0(P)=\frac1{2pM^2}\left\{
 \sum_{v\mid p}\log_p N_{L_v/\mathbb Q_p}\sigma_0(MP)
 -\sum_{w\nmid p}d_w(MP)\log_p\#k_w\right\}.
 \tag{10}
\]
\([L:\mathbb Q]=2p\)。第 2 节证明该值与允许的 \(M\) 无关，是二次函数。
定义其双线性极化
\[
 h_0(P,R)=\tfrac12\bigl(H_0(P+R)-H_0(P)-H_0(R)\bigr).
 \tag{11}
\]
它对 \(\Gamma\) 不变，因为 \(\sigma_0\) 的系数在 \(\mathbb Q\)，全部地方在式中同时保留。

每个 \(p\) 处 norm 都在 \(\mathbb Q_p^\times\)，其 Iwasawa log 属于 \(p\mathbb Z_p\)；
每个非 \(p\) 处项也属于 \(p\mathbb Z_p\)。由于 \(M\) 是 \(p\) 单位，
\[
               H_0(E(L))\subset\mathbb Z_p,\qquad
               h_0(W,W)\subset\mathbb Z_p,\quad
               W=A(F)\otimes\mathbb Z_p.
 \tag{12}
\]
这里包括不分歧次数 \(p\) 的地方，未额外删除该处的一层 \(p\)。

## 4. 全约化型的两个有理 Fermat 商矩

对已经满足形式群及恒等组件条件的实际非零点 \(P\)，定义
\[
             \nu(P)=\frac{N_{L/\mathbb Q}t(P)}
                            {N_{L/\mathbb Q}\mathfrak d(P)}
                    \in\mathbb Q^\times.
 \tag{13}
\]
在 \(v\mid p\)，有 \(\operatorname{ord}_v t(P)=d_v(P)\)，所以 \(\nu(P)\) 是 \(p\) 单位。
由 (6)，sigma 与 \(t\) 的 log norm 之差在 \(p^4\mathbb Z_p\)。
全部 \(p\) 处 norm 的乘积是全局 norm，而分母理想的 \(p\) 因子被 \(\log_p p=0\) 消去，
所以
\[
                      H_0(P)\equiv\frac{\log_p\nu(P)}{2p}\pmod p.
 \tag{14}
\]

设 \(\tau\) 生成 \(\Gamma\)，令 \(R\) 为 \(Q\) 的一个保持 \(\delta\) 指数的
整群环单位倍，并已满足上述局部条件。第 5 节给出这样的明确 \(R\)。
设
\[
 z_j=\frac{\nu(R+\tau^jR)}{\nu(R)^2},\qquad
 q_p(z)=\frac{z^{p-1}-1}{p}\pmod p,\qquad
 b_j=h_0(R,\tau^jR).
 \tag{15}
\]
所有和点均非零：\(1+\zeta_p^j\) 在非平凡有理循环表示上可逆。
由 \(\log_p z/p\equiv-q_p(z)\pmod p\)，
\[
                            b_j\equiv-\tfrac14q_p(z_j)\pmod p.
 \tag{16}
\]
这只需非零有理 \(p\) 单位的分子、分母模 \(p^2\)，无需近似整条 sigma。

令 \(\mathcal O=\mathbb Z_p[\zeta_p]\)、平衡
\(\delta=\zeta_p^{(p-1)/2}(\zeta_p-1)\)、\(d=(p-1)/2\)，
写 \(R=\delta^a\epsilon w\) 于实际秩一 \(W=\mathcal O w\)。
第 12 式、对称性及 \(\Gamma\) 不变性给
\[
 h_0(xw,yw)=\operatorname{Tr}_{\mathbb Q_p(\zeta_p)/\mathbb Q_p}
                   (c_wx\bar y),\qquad c_w=\bar c_w.
 \tag{17}
\]
\(c_w\) 可以为零。若不为零，整性与 different 指数 \(p-2\) 给
\(v_\delta c_w\ge-(p-3)\)；零的情形以无穷赋值解释。
所以
\[
 \mathcal R_R=\frac{\sum_{j=0}^{p-1}b_j\zeta_p^j}{\delta^2}
             =\frac{pc_R}{\delta^2}\in\mathcal O^+,\qquad
               v_\delta\mathcal R_R\ge2a.
 \tag{18}
\]
这完全不依赖非退化性。

由于 \(N_\Gamma R=0\)，有 \(b_j=b_{p-j}\)、\(\sum b_j=0\)。
把 \(\vartheta=\delta^2\) 代入整 Chebyshev 多项式，
\[
 \frac{\zeta_p^j+\zeta_p^{-j}-2}{\vartheta}
     =j^2+\frac{j^2(j^2-1)}{12}\vartheta+O(\vartheta^2).
 \tag{19}
\]
\(p\ge7\) 使 \(p\in\vartheta^d(\mathcal O^+)^\times\)、\(d\ge3\)，
故前两个系数分别模 \(p\) 读取。因此
\[
 \left(\sum_{j=1}^d j^2q_p(z_j),\
       \sum_{j=1}^d j^4q_p(z_j)\right)\ne(0,0)
       \quad\Longrightarrow\quad
                  v_\delta\mathcal R_R<4
       \quad\Longrightarrow\quad a\le1.
 \tag{20}
\]
R127 的短整证明只用 R122、R125，适用于此处任意好素数：
\(a=0\) 或 \(a=1\) 都迫
\[
                              \boxed{\Sha(E/\mathbb Q)[p^\infty]=0.}
 \tag{21}
\]
无需假设 \(r_-=1\) 或 \(a\) 偶；对 R126 的两符号选择，\(a\le1\) 当然进一步变成 \(a=0\)。

## 5. 所需整群环倍数，不增加 ordinary 假设

若 \(p\) 在 \(F\) 分裂，令 \(s\in\Gamma\) 为一个 \(p\) 上素位的算术 Frobenius，
另一个为 \(s^{-1}\)。取
\[
         D_p=(s^2-a_ps+p)(s^{-2}-a_ps^{-1}+p).
 \tag{22}
\]
有限域 Frobenius 特征多项式逐个地方说明 \(D_pQ\) 全在形式群；
\[
                       D_p\equiv(1-a_p)^2\ne0\pmod{(p,\tau-1)}.
 \tag{23}
\]
该计算允许 \(s=1\)，也允许 \(s\) 生成 \(\Gamma\)，并允许 \(a_p=0\)。

若 \(p\) 在 \(F\) 惰性，上述 Artin 元平凡，所有 \(p\) 处的剩余域为
\(\mathbb F_{p^2}\)。直接取
\[
                  D_p=\#E(\mathbb F_{p^2})=(p+1)^2-a_p^2.
 \tag{24}
\]
它杀掉全部剩余点，且 \(D_p\equiv1-a_p^2\ne0\pmod p\)。
两种情形下 \(D_p\) 均为 \(\mathcal O\) 单位，并且是实际整群环算子。
于是
\[
                                  R=12D_pQ
 \tag{25}
\]
满足第 4 节的全部条件且保留 \(a\)。组件清除只涉及固定坏位 \(2,17\)，
不引入 \(p\) 因子。若使用 R128，可统一取 \(\tau=\operatorname{Art}_{L/F}(1+2\sqrt{-15})\)。

## 6. 已完成的量词与尚缺输入

本篇已把 R127 的全局有理 Fermat 商测试扩展到 R126 的全部合法好素数，
所以无需另证其无穷输入与 ordinary 子集的交无限。
并没有证明 (20) 的两个实际加权和在无穷多个输入中不同时为零。
若 \(a\ge2\)，(18) 恰允许二者同时为零；此处没有隐藏一个非退化或单位猜想。
接下来须对原始 Heegner 轨道证明真正的非零，不能替换成环境局部模中的任意非零向量。

## 一手来源与本篇的直接证明

- W. Stein, C. Wuthrich, *Algorithms for the arithmetic of elliptic curves using
  Iwasawa theory*, Math. Comp. **82** (2013), 1757–1792，
  [出版社作者抽印本](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf)，
  §4 开头，印页 1769–1770（PDF 页 12–13）：
  \(\eta\) 方向的 Bernardi sigma、其收敛盘和二次高度；
  §4.3、印页 1772 另论超奇异向量高度。本文 (1)–(6)
  对本短模型直接给出在所用不分歧盘上的更明确整性估计。
- B. Mazur, W. Stein, J. Tate, *Computation of p-Adic Heights and Log Convergence*，
  [作者全文](https://wstein.org/papers/pheight/pheight.pdf)，§§2.3–2.8：
  完整地方 norm、分母项与二次律。本文使用 (7)–(8) 重作所需推导，
  不把 ordinary sigma 的整系数定理外推到超奇异情形。
- D. Bernardi, *Hauteur p-adique sur les courbes elliptiques*，
  Séminaire de Théorie des Nombres, Paris 1979–80，Progress in Mathematics **12**
  (1981), 1–14；此处通过上项已发表的精确重述使用，并保留直接构造。
- R122、R125、R127：真实有限 Sha、整上界及 \(a\le1\) 的充分性；
  R128 提供固定 Artin 规范。没有引用未证的 BSD 或高度非退化性。
