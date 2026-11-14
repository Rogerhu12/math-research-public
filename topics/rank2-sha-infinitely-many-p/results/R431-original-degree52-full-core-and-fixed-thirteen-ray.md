# R431 — 同一小交替核的完整 degree52 总和 core 与固定十三模细分

日期：2026-11-14。**状态：已证明。** 对 R430 的同一整反卷积来源
\[
\mathcal K(y,v)=-\frac23\{S(y)G_{18}(v)-C_{34}(y)F_{18}(v)\},
\]
将原固定 ray 一次细分为 \(\pi_0\equiv2\bmod13\)，得到完整联合式
\[
\boxed{\nu_{\mathcal K}|_{W\in p\mathbf Z_p}
=-\lambda(P_W)_*\nu_{\mathcal K},\qquad W=Y+X.}
\]
它保留正交伴随 \(Q_*=9Y-17X\) 的全部连续测试。证明重新支付整个
五十二维 Heisenberg lift、真实 odd-sigma 锚、二挠交替作用及完整整格，
不将旧 degree72 core 与反卷积交换。

同一实际来源的 \(Y,X,W,Q_*,V,P_*\) 六方向 scalar core 因此全部确定。
原条件中央对任意 \(X\) 测试的返回仍保完整补域，未将其与新的总和
深域中央条件相互替代。

## 1. 原周期、来源及一个固定更小 ray

保持 R430 的 \(b=17\)、原 sigma 和普通周期，且
\[
G_{16}=\frac{\sigma(2z)\sigma(2\delta z)}{4\delta},\quad
S=G_{16}F_{18},\quad C_{34}=G_{16}G_{18},
\]
\[
\mathcal K=\frac23G_{16}(y)
\{G_{18}(y)F_{18}(v)-F_{18}(y)G_{18}(v)\}
\in\mathcal S_{34}\boxtimes\mathcal S_{18}.
\tag{1}
\]
此处 \(F_{18},G_{18}\) 正是 R426 的两条实际来源。

在 R410 固定 ray
\[
\pi_0\equiv2494207+1872450\omega\pmod {2790720}
\]
上再加一个固定条件 \(\pi_0\equiv2\bmod13\)。准确 CRT 代表为
\[
\boxed{\pi_0\equiv13657087+21407490\omega\pmod {36279360}.}
\tag{2}
\]
其模 \(2790720\) 还原原代表，模 \(13\) 为 \((2,0)\)。
该新条件为单位类，且 \(p=N\pi_0\equiv4\bmod13\)。
原 primary、dyadic、三处及原两曲线角色条件均未改变；
原固定 ray 的素理想定理仍给无穷多个普通有理素数。
这里是一次固定细分，不随 \(p\) 另选角色。

仍有
\[
\pi_{17}=\pi_{24}=-\pi_0,\qquad
\lambda=\bar\pi_{17}^{-1}=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2 .
\tag{3}
\]
所有旧单位结论保留；\(p>19\) 已排除新坐标中的 \(13\)。

原模八条件给 \(g=\pi_0/\bar\pi_0\equiv3\bmod8\)，
新条件给 \(g\equiv1\bmod13\)，包括 \(\omega\) 系数为零。
所以完整中心模数上准确为
\[
\boxed{g\equiv27\pmod {104}= \pmod {2\cdot52}.}
\tag{4}
\]

## 2. 整个五十二维空间的绝对二挠公式

全篇使用原完整核
\[
K_N=\frac{\bar\pi_{17}}p\mathscr M_{\pi_{17}},\qquad
\nu_F|_p=\lambda[\kappa]_*\nu_{K_NF},
\tag{5}
\]
以及规范 lift
\[
T_t^{(N)}F(z)=e^{-N\eta_t(z+t/2)}F(z+t).
\]
取格基 \(1,\omega\)，在 level \(52\) 的 Schrödinger 基中
\[
Xe_j=\zeta_{52}^je_j,\qquad Ze_j=e_{j+1}.
\]
(4) 的完整交织为 \(X\mapsto X^{27},Z\mapsto Z^{27}\)；
因为这里 \(g\) 是显示的实整数代表，没有丢掉任何交叉周期相位。
置 \(De_j=e_{27j}\)。\(27^2\equiv1\bmod52\)，所以 \(D\) 给同一交织。

对 \(t=(s+r\omega)/2\)，\(r,s=0,1\)，完整对称 lift 给
\[
T_t^{(52)}e_j=(-1)^{s(r+j)}e_{j+26r}.
\tag{6}
\]
其中 \((-1)^{sr}\) 来自 \(52/4=13\)，不能省略。
对 \(s\) 求和只在 \(r\equiv j\bmod2\) 留下，因此
\[
\boxed{\frac12\sum_{t\in E[2]}T_t^{(52)}=D.}
\tag{7}
\]
二挠代表改变一个周期不添相位，因为 \(52/2=26\) 为偶。
(7) 是整个五十二维表示的恒等式。

还需确定真实 \(K_{52}\) 与 (7) 的绝对标量。
取 \(\alpha=4+\omega\)，\(N\alpha=13\)，使用实际非零锚
\[
A_*(z)=\sigma(2\alpha z)\in\mathcal S_{52}.
\tag{8}
\]
其 degree 为 \(N(2\alpha)=52\)，拉回半特征平凡，所以确实属于显示的原空间。
对非零 \(t\in E[2]\)，\(2\alpha t\) 是一个模 \(2\Lambda\) 非零的格点。
原 odd sigma 的半特征
\(\chi(m+n\omega)=(-1)^{m+n+mn}\)
在三个非零模二格类都为负。规范 CM 拉回因而给
\[
T_t^{(52)}A_*=-A_*\quad(t\ne0),\qquad T_0A_*=A_*.
\tag{9}
\]
所以 (7) 在此锚上为 \((1-3)/2=-1\)。

另一方面 R316 原 sigma 的完整 core 在当前 ray 是
\(\bar\pi_0^{-1}=-\lambda\)。
尺度 \(2\alpha\) 在当前普通处为单位，故它与原限制及推前交换；
(5) 的真实 \(K_{52}A_*=-A_*\)。
完整 Heisenberg 表示不可约，(4)、(7) 和这个真实锚固定唯一标量：
\[
\boxed{K_{52}=\frac12\sum_{t\in E[2]}T_t^{(52)},\qquad K_{52}^2=I.}
\tag{10}
\]
没有用未知中央导数或来源质量来定标。

## 3. 同一小核上二挠平移的准确负号

对任意非零 \(t\in E[2]\)，R426 已在真实二维
\(\langle F_{18},G_{18}\rangle\) 中证明
\[
\det(T_t^{(18)})=-1.
\tag{11}
\]
完整公式为
\[
T_tF_{18}=c_t^{18}(81e^9F_{18}+27e^7G_{18}/7),\quad
T_tG_{18}=c_t^{18}(3402e^{11}F_{18}-81e^9G_{18}),
\]
其中 \(e^3=-b,\ c_t^4=(3e^2)^{-1}\)。
因此 (1) 中的二来源交替积在两个输入同时平移 \(t\) 时准确乘 \(-1\)。

共享的 \(G_{16}\) 没有额外符号。
它的两条 odd-sigma 因子分别是 \([2]\) 与 \([2\delta]\) 拉回，
对非零二挠点各自得到同一个负半特征。
\(\delta\) 模二可逆，两个负号相消，故
\[
T_t^{(16)}G_{16}=G_{16}\qquad(t\in E[2]).
\tag{12}
\]
由规范乘法 lift，(11)–(12) 给完整联合式
\[
(T_t^{(34)}\otimes T_t^{(18)})\mathcal K
=\begin{cases}\mathcal K,&t=0,\\-\mathcal K,&t\ne0.\end{cases}
\tag{13}
\]
它保所有隐藏坐标，不是只在 \(y=v\) 的零边际上成立。

## 4. 保留 Q* 的真实总和 core

R430 的准确正交坐标为
\[
W=Y+X,\qquad Q_*=9Y-17X,\qquad
M=\begin{pmatrix}1&1\\9&-17\end{pmatrix},
\]
\[
M^{-1}=\frac1{26}\begin{pmatrix}17&1\\9&-1\end{pmatrix},\qquad
M\operatorname{diag}(34,18)M^t=\operatorname{diag}(52,7956).
\tag{14}
\]
这是同一 \(\mathbf Z_p^2\) 的整自同构。全部来源为
\[
\widetilde{\mathcal K}(w,q)=\mathcal K(w+9q,w-17q)
\in\mathcal S_{52}\boxtimes\mathcal S_{7956}.
\tag{15}
\]
交叉项 \(34\cdot9-18\cdot17=0\)，所有 degree 偶，故没有交叉
Gaussian 或平坦 twist；原正式群单位首阶基给完整整张量格。

对 (15) 作第一轴的 \(T_t^{(52)}\)，准确等于 (13) 的两个输入同时平移：
第二轴指数因显示交叉项为零而消去。
将 (13) 代入 (10)，得到整个联合来源的真实特征式
\[
(K_{52}\otimes I)\widetilde{\mathcal K}=-\widetilde{\mathcal K}.
\tag{16}
\]
定义
\[
\boxed{
P_W=M^{-1}\operatorname{diag}(\kappa,1)M
=I+\frac{\kappa-1}{26}
\begin{pmatrix}17&17\\9&9\end{pmatrix}.
}
\tag{17}
\]
它保 \(Q_*\)、将 \(W\) 乘 \(\kappa\)。于是
\[
\boxed{\nu_{\mathcal K}|_{W\in p}
=-\lambda(P_W)_*\nu_{\mathcal K}.}
\tag{18}
\]
这里完全重新计算新 degree 的 core，不与原 \(E_{20}\) 反卷积交换旧核。

原两输入的已付核分别为 \(+\lambda,-\lambda\)，所以全深域
\[
\nu_{\mathcal K}|_{Y,X\in p}
=-\lambda^2[\kappa,\kappa]_*\nu_{\mathcal K}.
\tag{19}
\]
同一域经 (14) 正是 \(W,Q_*\) 同时深。
两个完整正交核可交换，且 (10) 已付 \(K_{52}^2=I\)，故 (16)、(19)
严格给 \(K_{7956}\widetilde{\mathcal K}=+\widetilde{\mathcal K}\)。
设
\[
P_Q=M^{-1}\operatorname{diag}(1,\kappa)M
=I+\frac{\kappa-1}{26}
\begin{pmatrix}9&-17\\-9&17\end{pmatrix},
\]
则
\[
\boxed{\nu_{\mathcal K}|_{Q_*\in p}
=\lambda(P_Q)_*\nu_{\mathcal K}.}
\tag{20}
\]
没有在整个 degree7956 空间上额外假定二阶关系。

## 5. 六个实际方向和全部正交环带

在原输入坐标上设
\(P_Y=\operatorname{diag}(\kappa,1)\)、
\(P_X=\operatorname{diag}(1,\kappa)\)。
R430/R426 与 (18)、(20) 给
\[
\boxed{
\begin{aligned}
\nu_{\mathcal K}|_{Y\in p}&=\lambda(P_Y)_*\nu_{\mathcal K},&
\nu_{\mathcal K}|_{X\in p}&=-\lambda(P_X)_*\nu_{\mathcal K},\\
\nu_{\mathcal K}|_{W\in p}&=-\lambda(P_W)_*\nu_{\mathcal K},&
\nu_{\mathcal K}|_{Q_*\in p}&=\lambda(P_Q)_*\nu_{\mathcal K}.
\end{aligned}}
\tag{21}
\]
每条式子都保另外一个完整输出。

来源分别偶。普通第一输入反射将 \(W\) 送到
\(V=X-Y\)，将 \(Q_*\) 送到 \(-P_*\)，其中 \(P_*=9Y+17X\)。
所以差输出 \(V\) 的真实核也是 \(-\lambda\)，伴随 \(P_*\) 为 \(+\lambda\)。
它们是 (21) 在真实原坐标反射下的共轭，不新增半周期或普通尺度。

特别所有正交全深度准确为
\[
\nu_{\mathcal K}|_{\substack{Y\in p^m\\X\in p^n}}
=(-1)^n\lambda^{m+n}[\kappa^m,\kappa^n]_{Y,X,*}\nu_{\mathcal K},
\]
\[
\nu_{\mathcal K}|_{\substack{W\in p^r\\Q_*\in p^s}}
=(-1)^r\lambda^{r+s}[\kappa^r,\kappa^s]_{W,Q_*,*}\nu_{\mathcal K}.
\tag{22}
\]
原 \(X,W,V\) 完整推前恒零仍是 R430 的同一等式。
例如 \(Q_*\) 的任意深度环带限制后，\(W\) 推前仍为零，
因为 (20) 保 \(W\)。这只涉及 \(Q_*\) 的这些真实深度条件，
不推出任意随 \(W\) 移动的 \(Q_*\) 管都为零。

principal 的真实收敛环带正则化分别有分母
\((1-a_Y)(1+a_X)\) 与 \((1+a_W)(1-a_Q)\)，
其中 \(a_i=q_i\lambda\langle\kappa/p\rangle^{du_i}\)、\(|q_i|_p<1\)。
R410 的 \(1\pm\lambda\) 单位结论支付 \(q_i=1\) 的整延拓。
两套 Mellin 测试使用不同实际输出；不能因此把两个中央行直接等同。

## 6. 与任意 X 测试的条件中央相交，保完整补域

R430 的原条件中央仍是
\[
\int_{Y\ {\rm unit}}d\log_p\langle Y\rangle\,h(X)\,d\nu_{\mathcal K}
=-\frac23J'_S(0)\int h\,d\nu_{G_{18}}
\tag{23}
\]
对任意连续 \(h\) 成立，\(d=p-1\)。

新总和 core 对同一深域的准确拉回为：对 \(N\ge1\)，
\[
\boxed{
\begin{aligned}
&\int_{\substack{W\in p^N\\Y\ {\rm unit}}}
d\log_p\langle Y\rangle\,h(X)\,d\nu_{\mathcal K}\\
&=(-\lambda)^N d
\int_{Q_*\ {\rm unit}}
\log_p\left\langle\frac{Q_*+17\kappa^NW}{26}\right\rangle
h\left(\frac{9\kappa^NW-Q_*}{26}\right)\,d\nu_{\mathcal K}.
\end{aligned}}
\tag{24}
\]
\(Y\) 单位恰变成 \(Q_*\) 单位；\(h\) 的参数也被完整变换。
这里没有在 \(h\) 仅连续时对它擅作 Taylor 展开。

若原 \(J'_S(0)=0\)，则 (23) 使
\(\{W\notin p^N,Y\text{ 为单位}\}\) 的完整补域贡献准确为 (24) 的负数，
对每个相同 \(h\) 都成立。
不能把 (23) 直接限制到 (24) 的深域，更不能把其与
\(\{Y\text{ 隐藏输入全深},W\text{ 为单位}\}\) 的另一个中央域混用。

本文支付的是同一个小核上的真实总和与伴随 core，因而下一步可在
(23)–(24) 及 R430 的两混合矩族间作完整比较。
固定 rank-two 来源的原中央非消失仍未完成。

直接依赖：R410 固定 ray 及单位；R426 的完整二挠二维表示和 degree18 core；
R430 的整小来源、Gram 与全部条件中央。新的固定十三模细分、全52维
绝对二挠核、原 odd-sigma 锚及完整 \(Q_*\) 运输均在本文证明。

