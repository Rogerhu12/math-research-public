# R435 — 原 degree16 平方核心与对称核的真实双轴深度转移

日期：2026-11-14。**状态：已证明。** 在原固定普通 ray 上，整个
\(\mathcal S_{16}\) 的规范核心准确满足
\[
\boxed{K_{16}^2=\frac12\sum_{t\in E[2]}T_t^{(16)}-I,
\qquad K_{16}^4=I.}
\]
R424 的同一个 \(\mathcal R\in\mathcal S_{16}\boxtimes\mathcal S_{16}\)
在对角二挠平移下固定。因此它的原第一轴偶深限制与第二轴偶深限制
有一个完整可逆域运输；四倍深度时，单轴缩放本身也精确等于一个
真实隐藏输入限制乘单位。本文不把该隐藏限制从其它联合中删去。
主目标未完成。

## 1. 原规范及整个 degree16 的核心

沿用 R410/R413 的原普通 ray，或 R431 的固定十三模细分。
保持
\[
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad p>19.
\]
原全 theta 空间、规范 lift 和 division trace 是
\[
\mathcal S_N=\sigma^N L(NO),\qquad
T_t^{(N)}F(z)=e^{-N\eta_t(z+t/2)}F(z+t),
\]
\[
K_N=\frac{\bar\pi_{17}}p\mathscr M_{\pi_{17}},\qquad
\boxed{\nu_F|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_{K_NF}.}
\tag{1}
\]
R413 第3节已对任意偶 degree 支付完整整格、全部奇偶部分和
含中心交织。这不是只对 \(\mathcal R\) 的边际指定一个核心。
全部有限根单位可在同一个整扩张中计算，最后恒等式回到原系数域。

直接把 R410 的代表约化到完整中心模数 \(32\)，得到
\[
\boxed{g=\pi_0/\bar\pi_0\equiv27+8\omega\pmod {32},
\quad g^2\equiv25+16\omega\pmod {32}.}
\tag{2}
\]
其中 \(\omega^2+\omega+1=0\)。例如 \(g^2\) 的两系数是
\(27^2-8^2\equiv25\)、\(2\cdot27\cdot8-8^2\equiv16\)。
不能只把 \(g^2\) 读成模十六的整数九而省去中心相位。

## 2. 含两个负号的平方交织

在整个十六维 Schrödinger 基中取
\[
Xe_j=\zeta_{16}^j e_j,\qquad Ze_j=e_{j+1},\qquad j\bmod16.
\]
对称 Heisenberg lift 的交叉相位使用完整 \(32\) 次根单位。
(2) 作用于格基的两个向量分别给
\[
g^2\cdot1=25+16\omega,\qquad
g^2\cdot\omega=-16+9\omega.
\]
其交叉指数 \(25\cdot16\) 和 \((-16)\cdot9\) 模三十二均为十六。
故真实平方交织为
\[
\boxed{K_{16}^2X(K_{16}^2)^{-1}=-X^9,
\qquad K_{16}^2Z(K_{16}^2)^{-1}=-Z^9.}
\tag{3}
\]
这两个负号是原完整 lift 的一部分。

对于 \(t=(s+r\omega)/2\)、\(s,r\in\{0,1\}\)，degree16 的完整式为
\[
T_t^{(16)}e_j=(-1)^{sj}e_{j+8r}.
\tag{4}
\]
这里交叉二挠相位为一，因为 \(16/4=4\) 为偶数。
定义实际整算子
\[
B_2=\frac12\sum_{t\in E[2]}T_t^{(16)}-I.
\]
对 (4) 求和给
\[
\boxed{B_2e_j=(-1)^j e_{9j+8},\qquad B_2^2=I.}
\tag{5}
\]
逐个作用于基向量即验证 \(B_2XB_2^{-1}=-X^9\)、
\(B_2ZB_2^{-1}=-Z^9\)。所以 \(B_2^{-1}K_{16}^2\) 同时与
\(X,Z\) 交换，必为标量：与 \(X\) 交换迫其在显示基中对角，
再与 \(Z\) 交换迫所有对角系数相等。

## 3. 用原 odd sigma 锚固定绝对标量

使用真正的非零来源
\[
A_*(z)=\sigma(4z)\in\mathcal S_{16}.
\tag{6}
\]
对每个二挠 \(t\)，\(4t\in2\Lambda\)，原 odd sigma 在偶格点的
半特征为正，规范指数与拉回指数相消。因此
\[
T_t^{(16)}A_*=A_*\quad(t\in E[2]),\qquad B_2A_*=A_*.
\tag{7}
\]
R316 的原 sigma core 在当前 ray 为 \(\bar\pi_0^{-1}=-\lambda\)。
因尺度四是当前普通处的单位，它与原深度限制交换，(1) 给
\[
K_{16}A_*=-A_*,\qquad K_{16}^2A_*=A_*.
\]
第2节的标量于是为一，得到整个空间的准确身份
\[
\boxed{K_{16}^2=B_2=\frac12\sum_{E[2]}T_t^{(16)}-I,
\qquad K_{16}^4=I.}
\tag{8}
\]
它保整格且可逆，分母只有二；没有用未知中央量定标。

## 4. 同一个 R16,16 的完整对角二挠不变性

令
\[
\Sigma(y,v)=\sigma(y-v)\sigma(y+v)
=\sigma(y)^2\Theta(v)-\Theta(y)\sigma(v)^2.
\]
R424、R426 的完整来源式为
\[
\Sigma\mathcal R=-\frac23
\{F_{18}(y)G_{18}(v)-G_{18}(y)F_{18}(v)\}.
\tag{9}
\]
任一非零二挠平移在真实 \(\langle F_{18},G_{18}\rangle\) 中的
行列式为 \(-1\)，所以 (9) 右边在两个输入同时平移时乘 \(-1\)。

分母 \(\Sigma\) 的完整符号也必须保留。
若 \(e=x(t),e^3=-b\)，并用原 \(c_t^4=(3e^2)^{-1}\)，则在
\((\sigma^2,\Theta)\) 上按列的真实矩阵为
\[
\boxed{T_t^{(2)}=c_t^2
\begin{pmatrix}-e&2e^2\\1&e\end{pmatrix},
\qquad\det T_t^{(2)}=-3e^2c_t^4=-1.}
\tag{10}
\]
这由 \(\sigma_t^2=(x-e)\sigma^2\) 与原半周期的
\(x(z+t)=e(x+2e)/(x-e)\) 直接得到。
因此 \(\Sigma\) 在同一对角平移下也乘 \(-1\)。
按规范乘法 lift 约去 (9) 中的 \(\Sigma\)，先在其非零开集再延拓，
得到全来源身份
\[
\boxed{(T_t^{(16)}\otimes T_t^{(16)})\mathcal R=\mathcal R
\qquad(t\in E[2]).}
\tag{11}
\]
degree16 的这些二挠算子构成真实四元群，各自平方为一。
所以 (11) 等价于
\[
(T_t^{(16)}\otimes I)\mathcal R=(I\otimes T_t^{(16)})\mathcal R.
\]
结合 (8)，准确有
\[
\boxed{(K_{16,Y}^{2n})\mathcal R=(K_{16,X}^{2n})\mathcal R
\qquad(n\ge0).}
\tag{12}
\]
这里始终是同一个实际九维偶核及其完整联合，而非按两个相同边际
重新拼出的张量。

## 5. 偶深度的真实双轴域运输

用 \((r,s)\) 表示 \(\nu_{\mathcal R}\) 的两个原输出。
迭代 (1) 的完整联合式，对 \(n\ge0\) 有
\[
\nu_{\mathcal R}|_{r\in p^{2n}\mathbf Z_p}
=\lambda^{2n}[\kappa^{2n},1]_*\nu_{K_Y^{2n}\mathcal R},
\]
\[
\nu_{\mathcal R}|_{s\in p^{2n}\mathbf Z_p}
=\lambda^{2n}[1,\kappa^{2n}]_*\nu_{K_X^{2n}\mathcal R}.
\]
(12) 使右侧来源完全相同，故
\[
\boxed{\nu_{\mathcal R}|_{r\in p^{2n}\mathbf Z_p}
=[\kappa^{2n},\kappa^{-2n}]_*
       (\nu_{\mathcal R}|_{s\in p^{2n}\mathbf Z_p}).}
\tag{13}
\]
\(\lambda^{2n}\) 在两条相同身份中准确相消。
逆尺度只在 \(s\in p^{2n}\mathbf Z_p\) 的真限制上使用，所以像仍在
\(\mathbf Z_p^2\)，并未定义一个对整个第二轴不整的操作。

等价地，对任意连续 \(\Phi\colon\mathbf Z_p^2\to\mathcal O\)，
\[
\boxed{\int_{r\in p^{2n}}\Phi(r,s)\,d\nu_{\mathcal R}
=\int_{s\in p^{2n}}\Phi(\kappa^{2n}r,\kappa^{-2n}s)
                         \,d\nu_{\mathcal R}.}
\tag{14}
\]
它保两个输出的全部域、权及额外连续测试；允许另与固定独立输入
张量后使用。若 \(\Phi\) 中含有相加总输出、单位条件或移动中心，
必须按 (14) 共同变换，不能只移动显示的深度指示函数。

## 6. 四倍深度把人为缩放准确换成原隐藏限制

由整个 \(K_{16}^4=I\)，对 \(n\in4\mathbf Z_{\ge0}\) 直接有
\[
\boxed{\nu_{\mathcal R}|_{r\in p^n\mathbf Z_p}
=\lambda^n[\kappa^n,1]_*\nu_{\mathcal R},\qquad
\nu_{\mathcal R}|_{s\in p^n\mathbf Z_p}
=\lambda^n[1,\kappa^n]_*\nu_{\mathcal R}.}
\tag{15}
\]
因此第一轴缩放 \([\kappa^n,1]_*\nu_{\mathcal R}\) 恰等于真实
第一输出深度限制乘 \(\lambda^{-n}\)。这是同一原联合的等式，
可以放回 R430 的 \(G_{16}\Sigma\mathcal R\) 卷积表示，保其它
sigma、Theta 输入原样。

R429 的二变量解析网格论证允许深度限制在任一固定倍数的子网格，
因为 \(\{\kappa^{4n}:n\ge n_0\}\) 仍为趋于盘内零点的无限序列。
所以若一个新表示的非零系数已经独立付清，可在四倍深子网格上
使用 (15)，不需猜测某一个预定深度的数值。
本句只支付子网格的解析推理，未将不同输入表示的受限域自动相认。

尤其 (13)–(15) 仍保留真实 \(r\) 或 \(s\) 深条件。
R430 对整个第二输出 \(X=s-c+d\) 的任意测试，不自动等于对内部
\(s\) 的任意测试；相关的 \(c,d\) 与完整补域仍须另行运输。
本篇不由这些深度转移预支原 rank-two 中央非零。

## 依赖与规范

- [R413：任意偶 degree 的原整 trace、全核心及中心交织](R413-original-three-output-core-and-eight-source-central-return.md)。
- [R424：同一个原对称 Bezout 核](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。
- [R426：实际 F18/G18 的完整二挠矩阵](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。
- [R430：小核的原卷积输出与完整测试范围](R430-original-integral-second-output-division-and-degree18-mixed-rows.md)。
- [R429：两深度解析网格的原非零系数](R429-original-two-depth-grid-and-reciprocal-sigma-nonvanishing.md)。

以上核心平方、绝对相位、对角不变及真实域等式均由显示的有限
Heisenberg 运算和原整测度身份直接证明，不设额外机械重跑门槛。
