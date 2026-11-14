# R463 — 原连接函数的 \(\pi_0\) 分布、division-log 范数及完整 carry

日期：2026-11-14。**状态：已证明。**

原连接函数 \(\mathfrak q=(\Theta^{17})'/\Theta^{17}\) 的普通
深输入尺度是 \(\pi_0\)，并非 theta 伴随的 \(\kappa\)。
本文从已发表的完整平移、分布公式支付这个差别，并在原独立
\(\nu_{\mathfrak q}\otimes\nu_C\) 中计算实际 carry。
同一个未知 \(C'\) 消去后，剩余是原 \(G=S-a_{1j}H_j\)
和一个明确的 \(p\) 级有理 division-log 来源。

这个有理来源在原点盘给整有界测度，却有真正全局极点，
不在 R460 的固定六维全纯格中。将伴随沿同一个 étale 同源
拉回后，全部极点才被支付；该新全纯来源的完整 étale 迹为零。
原 division 单位的范数准确为一，原点对数为
\(-(p-1)\log_p3/2\ne0\)，其余 étale 支完整补偿它。
没有把全迹零当成原点分支中央零。主目标未完成。

## 1. 原规范与真实连接函数

保持 R454、R460 的普通 ray、原 \(b=17\) 和周期 \(\Omega\)。
为区分端同源与连接常数，记
\[
a=\bar\pi_0,\quad \pi=\pi_0,\quad a\pi=p,\qquad
\lambda=-a^{-1},\quad \kappa=p/a^2,\quad d=p-1.
\tag{1}
\]
当前 \(a\) 是普通处单位，\(\pi\) 是连通方向。
令 \(C=C_{13}\) 或 \(C_{15}\)，并写连接常数为
\[
c_C=a_{13}=-37/(33936b)\quad\text{或}\quad
c_C=a_{15}=-37/(53760b).
\]
原完整连接是
\[
\boxed{
G=S-c_CH_j=C'-\mathfrak q C,\qquad C'(0)=-c_C,\quad j=3\ \text{或}\ 5.
}
\tag{2}
\]
所有来源、tame 分支及周期都是 R307、R460 的实际对象。

取 \(\delta=1+2\omega\)，\(\delta^2=-3\)。原 sigma 恒等式给
\[
\Theta(z)=x(z)\sigma(z)^2=\frac{\sigma(\delta z)}{\delta\sigma(z)},
\quad F_0=\Theta^{17},\quad
\boxed{\mathfrak q(z)=17\{\delta\zeta(\delta z)-\zeta(z)\}.}
\tag{3}
\]
\(j=0\) 的 reduced theta 等于原 sigma；重量二指数修正为零。
\(\Theta(0)=1\)，\(\mathfrak q\) 在原点解析。R307 已付
\(\mathfrak q(\Omega\log(1+T))\in\mathcal O[[T]]\)，所以
\(\nu_{\mathfrak q}\) 是整有界测度；本篇没有把 Coleman log
本身未经说明地当作有界测度。

## 2. 已发表分布公式给原 \(\pi\) 尺度

使用 Bannai–Furusho–Kobayashi,
*p-adic Eisenstein–Kronecker series for CM elliptic curves and the
Kronecker limit formulas*, Nagoya Math. J. **219** (2015), 269–302：
[作者全文](https://www.math.nagoya-u.ac.jp/~furusho/paper/BFK.pdf)，
DOI [10.1215/00277630-2891995](https://doi.org/10.1215/00277630-2891995)。
其 Proposition 3.10 的 \(b=1\) 分布式与 Lemma 3.12 的连通挠点
正式平移式用于下面同一来源；Proposition 3.11 支付所用展开
在原盘的收敛。这里的模型采用 \(dx/(2y)\)，相当于该文
\(dx/y_{\rm BFK}\) 中 \(y_{\rm BFK}=2y\)，微分没有改变。

写 \(F_{z_0,1}\) 为其 reduced zeta 平移。
在 \(j=0\)，\(F_{0,1}=\zeta\)，且完整公式给
\[
\sum_{\tau\in E[\pi]}F_{\tau,1}(z)
=\pi F_{0,1}(\pi z).
\tag{4}
\]
正式平移 \(\tau\) 时，(3) 变为
\[
17\{\delta F_{\delta\tau,1}(\delta z)-F_{\tau,1}(z)\}.
\]
这是保 reduced 平移常数的式子，不能将挠点正式对数代零。
因为 \((\delta,\pi)=1\)，\(\delta\) 在整个 \(E[\pi]\) 上是置换。
对全部支求和后，(4) 严格给
\[
\boxed{
\sum_{\tau\in E[\pi]}\mathfrak q(t\oplus\tau)
=\pi\,\mathfrak q([\pi]t).
}
\tag{5}
\]
这里左侧用原正式群变量表示，右侧同一个不变微分下的
对数变量乘 \(\pi\)。若以 \(E_{17}\) 的实际 Frobenius
\(-\pi_0\) 写，两个负号由 \(\mathfrak q\) 的奇性相消，
仍是 (5)；连通核没有改变。

原正式同构将乘法 \(\mu_p\) 送至此连通核。根单位完整平均
因此等于测度限制，且 \(\pi/p=a^{-1}\)。得到完整身份
\[
\boxed{
\nu_{\mathfrak q}|_{p\mathbf Z_p}
=a^{-1}[\pi]_*\nu_{\mathfrak q}
=-\lambda[\pi_0]_*\nu_{\mathfrak q}.
}
\tag{6}
\]
比较 R460 同一原奇伴随：
\[
\boxed{\nu_C|_{p\mathbf Z_p}=a^{-1}[\kappa]_*\nu_C.}
\tag{7}
\]
(6)、(7) 的系数相同，尺度不同，
\(\pi/\kappa=a\) 是一个真正的单位 dilation。

## 3. 真实 division 单位及全部常数

对非零 CM 整数 \(A\)，保持首项规范
\[
r_A(z)=\frac{\sigma(Az)}{\sigma(z)^{N(A)}}\in K(E),
\quad r_A(z)\sim A z^{1-N(A)}.
\tag{8}
\]
本篇先取 \(A=a^n\)、\(n\ge1\)，\(N(A)=p^n=:N\)。
定义原有理单位与对数导数
\[
\boxed{
u_A(z)=\frac{r_A(\delta z)}{r_A(z)},\qquad
R_A(z)=\partial_z\log u_A(z).
}
\tag{9}
\]
由 (3)、(8)，准确为
\[
\boxed{
u_A=\delta^{1-N}\frac{\Theta(Az)}{\Theta(z)^N},\qquad
A\mathfrak q(Az)-N\mathfrak q(z)=17R_A(z).
}
\tag{10}
\]
全部首项常数已保，没有一个未定 theta 相位。
特别 \(n=1\) 时
\[
\boxed{
\mathfrak q(az)=\pi\mathfrak q(z)+17a^{-1}R_a(z)
=\pi\mathfrak q(z)-17\lambda R_a(z).
}
\tag{11}
\]
此处 \(R_a\) 后文也记 \(R_p\)；它不是原 \(34\) 次来源中的
一个免费有限矩阵列。

乘法除法函数还给完整 cocycle
\[
\boxed{
u_{AB}(z)=u_A(Bz)\,u_B(z)^{N(A)},\qquad
R_{AB}(z)=B R_A(Bz)+N(A)R_B(z).
}
\tag{12}
\]
例如
\(R_{a^{n+1}}=aR_{a^n}(az)+p^nR_a(z)\)。
这不删除其中的单位 dilation。

## 4. 完整除子：E[a] 本身的极点确实抵消

记原非零三挠点为 \(T_\pm=(0,\pm\sqrt b)\)，并令
\(D=T_++T_-\)。原 \(\Theta\) 的零除子恰为 \(D\)，原点值为一。
由 (10)，准确得到
\[
\boxed{\operatorname{div}(u_A)=[A]^*D-ND.}
\tag{13}
\]
也可从
\(\operatorname{div}r_A=E[A]-N(O)\) 直接读取：
\(\delta\) 在 \(E[A]\) 上可逆，所以分子、分母的 \(E[A]\)
零完整相消。不能把这些点再算成 \(R_A\) 的极点。

因 \((A,\delta)=1\)，\(A\) 置换 \(T_\pm\)。
因此 \(R_A\,dz\) 在以下位置有准确简单极：
\[
\begin{array}{c|c|c}
\text{位置}&\text{个数}&\text{留数}\\ \hline
[A]^{-1}\{T_+,T_-\}\setminus\{T_+,T_-\}&2(N-1)&+1\\
T_+,T_-&2&1-N .
\end{array}
\tag{14}
\]
原点及 \(E[A]\) 都没有极点。

原 \(C_{13},C_{15}\) 在 \(T_\pm\) 各恰有三阶零、在原点
恰有一阶零。前者由 R460 的 \(P_0=0,P_1\ne0\) 给出，
后者由 \(C'(0)=-c_C\ne0\) 给出。
它作为 degree34 全纯截面的总零次数为三十四，
所以在这三个点以外最多有二十七个零。
因此
\[
\boxed{
R_A C\ \text{至少有}\ 2N-29\ \text{个未消去的真简单极}.
}
\tag{15}
\]
特别当前 \(p\ge71\)，\(R_pC\) 绝不是整个
\(\langle C'\rangle+\mathcal S_{34}\) 中的来源；
该格的函数在复平面上整个全纯，不能容纳 (15)。
R460 的六个正 Tc 矩不能凭维数理由抽回这条新 \(p\) 级行。

## 5. 原点盘的整性与有界测度

全局极点并不妨碍原点盘的整测度。当前好普通模型中，
\(A=a^n\) 的微分为单位，故 \([A]\) 是 étale 方向；
它在原正式群上是整自同构。
\(T_\pm\) 的约化不是原点，所以 (13) 的零、极支都不进入
原点正式盘。由 (8) 的首项
\[
\boxed{u_A(O)=\delta^{1-N}\in\mathcal O^\times.}
\tag{16}
\]
在良好整模型上，(13) 支持于与原点盘不相交的除子；
(16) 也排除额外的竖直常数因子。因此
\[
u_A,\ u_A^{-1}\in\mathcal O[[t]],\qquad
R_A\in\mathcal O[[t]],
\tag{17}
\]
其中 \(R_A\) 的微分是原 \(dx/(2y)\)，与 \(dt\) 相差一个整单位。
代入同一个整正式同构给
\[
\boxed{
R_A(\Omega\log(1+T)),\quad
(R_A C)(\Omega\log(1+T))
\in\mathcal O[[T]].
}
\tag{18}
\]
故 \(\nu_{R_A}\)、\(\nu_{R_AC}\) 是整有界测度，
没有在此改用一个未经估计的伪测度。
本篇用 \(\log u_A\) 作 Coleman 函数及代数点对数；
不声称它本身必是有界 Amice 变换。

首项也完全明确。原级数给
\[
\Theta(z)=1-\frac{2b}{15}z^6+\cdots,\qquad
\mathfrak q(z)=-\frac{68b}{5}z^5+\cdots.
\]
由 (10)，
\[
\boxed{
[z^5]R_A=-\frac{4b}{5}(A^6-N),\qquad
[z^6](R_AC)=\frac{4c_Cb}{5}(A^6-N).
}
\tag{19}
\]
当前 \(A\) 是单位、\(N\in p\)，这些系数在固定分母排除后均
为单位。它们给真实正矩，不给中央导数非零。

## 6. 原独立 q 与 C 的一层及全深 carry

现在保 **原独立表示**
\[
\mu=\nu_{\mathfrak q}(x)\otimes\nu_C(y),\qquad W=x+y.
\tag{20}
\]
其完整和输出是
\(\nu_{\mathfrak q C}=\nu_{C'}-\nu_G\)。
R460 的同一表示只认同这个完整第一推前；
下面 \(x,y\) 的独立条件始终在 (20) 中定义。

对 \(n\ge1\)，令
\[
\mathscr B_n=
\{W\in p^n,\ (x,y)\notin p^n\mathbf Z_p^2\},
\]
\[
\boxed{
\mathfrak b_{n,C}
=(W/\kappa^n)_*(\mathbf1_{\mathscr B_n}\mu).
}
\tag{21}
\]
\(n=1\) 时两原输入均为单位；一般 \(n\) 精确包含
\(v_p(x)=v_p(y)<n\) 的全部 carry 层。
归一除以 \(\kappa^n\) 只在 (21) 的整像域中使用。

由 (7)，微分来源 \(C'\) 的完整核心为
\(a^{-1}\kappa[\kappa]_*\)，而 \(G\) 的为
\(\lambda[\kappa]_*\)。所有 \(W\) 深 \(n\) 的归一来源是
\[
\frac{p^n}{a^{3n}}\nu_{C'}-\frac{(-1)^n}{a^n}\nu_G.
\tag{22}
\]
另一方面，(6)、(7) 给两个输入同时深 \(n\) 的归一来源
\[
a^{-2n}\nu_{\mathfrak q(a^n z)C(z)}.
\tag{23}
\]
这里正是 \(\pi^n/\kappa^n=a^n\)；不能把 (23) 换成
\(a^{-2n}\nu_{\mathfrak q C}\)。

置 \(A=a^n,N=p^n\)，将 (10) 代入 (22) 减 (23)，
同一个未知 \(C'\) 完整消去，得到
\[
\boxed{
\mathfrak b_{n,C}
=\left(\frac{N}{A^3}-\frac{(-1)^n}{A}\right)\nu_G
-\frac{17}{A^3}\nu_{R_AC}.
}
\tag{24}
\]
特别一层是
\[
\boxed{
\mathfrak b_{1,C}
=-\lambda(1+\kappa)\nu_G+17\lambda^3\nu_{R_pC}.
}
\tag{25}
\]
这是同一个实际 unit-unit carry 的完整有界测度式，
不只是一组系数或某个中央值。

(24) 的总质量可以直接读出：
\[
\boxed{
\mathfrak b_{n,C}(\mathbf Z_p)
=-c_C\left(\frac{N}{A^3}-\frac{(-1)^n}{A}\right).
}
\tag{26}
\]
因为 \(R_AC\) 在原点的总质量为零。
总质量与下面归一输出单位域的质量仍须区别。

令 \(J_{\mathfrak b_n}(u)\)、\(J_{R_AC}(u)\) 为各自真正
归一输出单位域上的 principal 行。逐项测试 (24)，准确得到
\[
\boxed{
\{N-(-1)^nA^2\}\{J_S(u)-c_CJ_{H_j}(u)\}
=A^3J_{\mathfrak b_n}(u)+17J_{R_AC}(u).
}
\tag{27}
\]
左侧系数是单位。式子在完整 \(u\) 参数及其中央导数上都成立，
但两个右侧行均未被声称为零。
特别 (26) 不能被当成
\(J_{\mathfrak b_n}(0)\)；限制归一 \(W/\kappa^n\) 为单位后，
实际域还要求 \(v_p(W)=n\)。

## 7. 拉回 C 后的全纯来源与精确 étale 迹零

与 (15) 不同，令
\[
\boxed{W_{n,C}(z)=R_A(z)C(Az),\qquad A=a^n.}
\tag{28}
\]
在所有 \([A]^{-1}T_\pm\) 上，\(C(Az)\) 都至少三阶零；
它支付 (14) 的全部简单极。因 \(R_A\) 是椭圆有理函数，
\[
\boxed{W_{n,C}\in\mathcal S_{34p^n}}
\tag{29}
\]
是整个全纯来源，保原 even 半特征，没有另添 Gaussian。
其原点首六阶系数是
\[
[z^6]W_{n,C}=\frac{4c_CbA}{5}(A^6-N),
\tag{30}
\]
仍为单位。

还可以绝对确定有理范数。由
\(\operatorname{div}r_A=E[A]-N(O)\)，
\(\operatorname{Norm}_{[A]}r_A\) 的除子为零，故是非零常数。
\((A,\delta)=1\) 使 \(\delta\) 逐纤维置换整个核，因而
\[
\operatorname{Norm}_{[A]}(r_A\circ[\delta])
=\bigl(\operatorname{Norm}_{[A]}r_A\bigr)\circ[\delta]
=\operatorname{Norm}_{[A]}r_A .
\]
两个常数是同一个，不留未定相位。因此
\[
\boxed{
\operatorname{Norm}_{[A]}u_A=1,\qquad
\operatorname{Tr}_{[A]}R_A=0.
}
\tag{31}
\]
后一式也由对完整范数取不变微分得到：
\(d\log\operatorname{Norm}u_A=(1/A)\operatorname{Tr}R_A\,dz\)。

把 \(C(Az)\) 看作同一线丛的真正 pullback，投影公式给
\[
\boxed{
\operatorname{Tr}_{[A]}\bigl(R_A[A]^*C\bigr)
=C\,\operatorname{Tr}_{[A]}R_A=0.
}
\tag{32}
\]
这是 **通常 étale 同源的全部 \(p^n\) 支** 的线丛迹；
不是 R300 的 \(\mathscr M_A\)，也不是普通连通核的原点
根单位平均。特别不能从 (32) 推出原点分支
\(J_{W_{n,C}}\) 的质量或中央为零。

## 8. 绝对原点对数及其余全部 étale 支

\(u_A\) 在 \(E[A]\) 的每一点均无零极，故 (31) 在零纤维给
\[
\prod_{P\in E[A]}u_A(P)=1.
\tag{33}
\]
所有值为非零代数数，原点值是 (16)。当前
\(N=p^n\equiv1\pmod6\)、\(\delta^6=-27\)，因此
\[
u_A(O)=(-27)^{-(p^n-1)/6},\qquad
\boxed{\log_pu_A(O)=-\frac{p^n-1}{2}\log_p3\ne0.}
\tag{34}
\]
\(\log_p3\ne0\)，因为 \(3\in\mathbf Z_p^\times\) 不是根单位。
这里没有声称它除以 \(p\) 后必是单位。

对完整 (33) 取同一分支的加法对数，得到准确补偿
\[
\boxed{
\sum_{P\in E[A]\setminus\{O\}}\log_pu_A(P)
=\frac{p^n-1}{2}\log_p3.
}
\tag{35}
\]
这些是其余 \(p^n-1\) 个 étale 支，不能删去。
原点盘的非零对数与全范数一同时成立，不构成矛盾。
本文只在这里对一个真实有理单位取代数点对数；
没有将它与 principal 测度中央偷偷相认。

## 9. 全纯拉回来源的完整连接及非齐次中央比较

(10) 和原连接 (2) 还给整个 charge \(34N\) 的关系
\[
\boxed{
\left(\partial_z-N\mathfrak q(z)\right)C(Az)
=A\,G(Az)+17W_{n,C}(z).
}
\tag{36}
\]
所有可能极均由同一 \(C(Az)\) 支付，所以这是全纯来源式。
令
\[
Q_C(u)=J_{\mathfrak q C}(u)=D_C(u)-\{J_S(u)-c_CJ_{H_j}(u)\}.
\]
R460 已付其单位质量
\[
Q_C(0)=-c_C\lambda(1+\kappa)\in\mathcal O^\times.
\tag{37}
\]
把 (36) 作为原测度式完整测试第一单位群，得
\[
\boxed{
17J_{W_{n,C}}(u)
=A\langle A\rangle^{du}Q_C(u)
-p^n\mathcal K_{\mathfrak q,[A]C}(u).
}
\tag{38}
\]
这里
\[
\mathcal K_{\mathfrak q,[A]C}(u)
=\iint\mathbf1_{x+Ay\ {\rm unit}}\langle x+Ay\rangle^{du}
                  \,d\nu_{\mathfrak q}(x)d\nu_C(y)
\tag{39}
\]
保其真正相加单位域，不是两个 Mellin 函数的积。

单位 dilation \([A]\) 保原有界范数；所以 (39) 的质量整、
中央导数属于 \(p\mathcal O\)，且界对全部 \(n\) 一致。
因此完整微分给
\[
\boxed{
17J'_{W_{n,C}}(0)
=A\{Q_C'(0)+nd\log_p\langle a\rangle Q_C(0)\}
-p^n\mathcal K'_{\mathfrak q,[A]C}(0).
}
\tag{40}
\]
特别右侧最后一项在 \(p^{n+1}\mathcal O\) 中。
这是保所有输入的准确高精度比较；其中的
\(nd\log_p\langle a\rangle Q_C(0)\) 是已知非齐次项。
未知 \(Q_C'(0)\) 和其余 étale 分支仍保留。
(32) 的全迹零不能替这两个未知项自动赋零。

## 10. 已付接口与固定小同源的后续区别

本篇付清的对象依次是：
原 \(\mathfrak q\) 的 \(\pi_0\) 尺度、真实独立 carry (24)、
原有理 division 单位的精确除子和范数、完整全纯 pullback
来源 (28)，以及同一中央的全部输入比较 (38)。

\(R_pC\) 的实际 \(p\) 级极点是新的来源成本，不能塞回 R460
的六维格。固定小 CM 同源可以另产生固定 degree 的全纯
\(R_A C(Az)\)，但那是另一条需要完整算术识别的来源；
这里不由质量、全迹零或 CM 角型替它赋秩二身份或中央零。

R460 的两输入表示与本篇 (20) 仅有同一完整第一推前。
若要在其内部 carry 之间运输，仍须支付整个联合来源；
(24)、(27) 已明确保留缺失的 \(R_AC\) 行。

## 精确证书与依赖

- [精确符号证书](../scripts/check-r463-original-division-log-carry.py)
  核原 \(\Theta,\mathfrak q\) 首项、全部常数及一般
  \(A=a^n,N=p^n\) 的 carry 消元，不扫描素数。
- [完整输出](../scripts/check-r463-original-division-log-carry.json)。
- [R307：原连接和形式盘有界性](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)。
- [R460：同一伴随、tame-one 行及完整质量](R460-original-odd-companion-tests-and-same-domain-connection-carries.md)。
- BFK 上述作者全文，Proposition 3.10、Proposition 3.11、
  Lemma 3.12；本篇 (5)–(6) 是保持原 \(\delta\) 及微分后的具体推论。

