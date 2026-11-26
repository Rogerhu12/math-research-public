# R961 — 原同六 sigma 中的 E65 全66维投影与五伴随中央行

日期：2026-11-26。**状态：本篇全部结构身份与真正非零投影已经证明，并由同次完整公开运行通过。**
R959 的原 $E_{65}$ 来源、全部有限 Schwartz、普通与惰性通常
Selmer 桥已经证明。本篇只接受它在本次 run 重生的完整66维
CM7/CM19 矩阵及唯一原向量，不把其旧65项输出表当输入。

本篇候选是实际六 sigma 乘积，公开 run45818310281 已返回
$\alpha_{65}=25\omega/(72\gamma_{37})\ne0$，并在全部66行回乘。
测度及五伴随中央结论使用原共同 ordinary 射线、$p>211$ 和原固定坏集；
特征零的完整投影身份不依赖目标素数。R959 的惰性 signed 桥保持其原规范。
这里得到同一来源上的真实条件中央行，尚未消去全部混合切域或证明无穷非零。

## 1. 同一原输入与正确的 degree390

沿用 R958 的共同 $E_1:y^2=x^3+1$、原微分
$dz=dx/(2y)$、$x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、
$\sigma=z+\cdots$。置
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma_7=3+\omega,\quad
\gamma_{19}=5+2\omega=4+\delta,\quad a=\gamma_{37}=7+3\omega.
$$
原未缩放六输入仍为
$$
\rho_{\rm raw}=-\frac1{84}\nu_\sigma^{\otimes6}.
$$
固定实际轴
$$
A_{65}=(\delta,2\delta,\gamma_7,\bar\gamma_7,a,18)
\tag{1}
$$
及完整来源
$$
\boxed{F(z)=-\frac{1}{84\cdot9a}
 \sigma(\delta z)\sigma(2\delta z)\sigma(\gamma_7z)
 \sigma(\bar\gamma_7z)\sigma(az)\sigma(18z).}
\tag{2}
$$
它是 $(9a)^{-1}(A_{65})_*\rho_{\rm raw}$，没有删去任何输入。

六个系数的范数依次为
$$
3,\ 12,\ 7,\ 7,\ 37,\ 324,
$$
总和390，且原首项乘积为 $-84\cdot9a\,z^6$。
所以 $[z^6]F=1$。四个奇 CM 系数
$\delta,\gamma_7,\bar\gamma_7,a$ 与两个偶系数给标准偶半特征。
这使用原奇 sigma 半特征在
$\mathcal O_K/2\simeq\mathbf F_4$ 的三个非零类上均为 $-1$，
而不是检查系数和模二。
全部 Gaussian 由 $\eta_{v\lambda}=\bar v\eta_\lambda$ 与范数和390
消去，共同六次旋转给角型零。故
$$
F\in\sigma^{390}K[X]_{\le65},\qquad X=x^3.
\tag{3}
$$
第3节还给完整函数域身份；(3) 不只依赖 degree 和首项。

## 2. 原 division 函数与九倍点的完整组合

R958 的完整 CM 群律构造给
$$
r_a=\frac{\sigma(az)}{\sigma(z)^{37}}
      =aR_{37}(X),\qquad R_{37}\text{ 首一，次数6}.
\tag{4}
$$
本次 reader 从群律重新生成它，再核整条曲线方程、微分恒等式、
约分后的精确分子分母次数，以及全部平方分母。
没有读取 R958 的生成系数表。

九倍点不需要另做一遍大有理函数消元。原三倍点为
$$
r_3=3x(X+4),\qquad
x(3z)=\frac{B(X)}{9x^2(X+4)^2},\qquad
B(X)=X^3-96X^2+48X+64.
\tag{5}
$$
reader 先用实际 $[3]$ 群律和完整 division 除子核 (5)。
然后使用准确的组合身份
$$
r_9(z)=r_3(3z)\,r_3(z)^9.
$$
代入 (5) 得
$$
\boxed{r_9=9xR_{13}(X),\qquad
R_{13}(X)=(X+4)B(X)
  \{B(X)^3+2916X^2(X+4)^6\}.}
\tag{6}
$$
$R_{13}$ 是首一13次多项式；此下标是次数，不是 norm13。

所有常数都由同一个原 sigma 确定。若将实际约分的
$x(3z)=N_3/D_3$ 写入，reader 对整个多项式直接回乘
$$
3N_3(N_3^3+4D_3^3)\,r_3^9=r_9D_3^4.
\tag{7}
$$
这支付的是整个 $[3]\circ[3]$ 组合，包含全部核点和重数；
不是核几项 Laurent 系数。这里从未假定整数9的 normalized
CM trace 在奇 sigma 上是根单位；本篇使用的有限 trace 仅是
norm7、norm19，九倍点只作为实际 division 乘法。

## 3. 候选的全部66坐标

保原
$$
S=\sigma^{34}x^2P_S(X),\qquad
P_S(X)=X^4-\frac{53}{7}X^3-\frac{12}{7}X^2
                  -\frac{80}{7}X-\frac{128}{7}.
$$
写 $R_{13}(X)=\sum_{j=0}^{13}r_jX^j$。
用原
$$
\sigma(2z)=-2y\sigma(z)^4,\qquad
x(2z)=\frac{x(X-8)}{4(X+1)}
$$
和 (6)，准确得到
$$
\frac{\sigma(18z)}{9\sigma(2z)}
 =\sigma(z)^{320}xJ_9(X),
$$
$$
J_9(X)=\sum_{j=0}^{13}r_j64^{13-j}
 X^j(X-8)^{3j+1}(X+1)^{3(13-j)}.
\tag{8}
$$
全部分母在显示式中消去，$J_9$ 首一、次数53。
结合 (4) 与原六 sigma 的 $S$ 恒等式，
$$
\boxed{F=\sigma^{390}\,X\,P_S(X)R_{37}(X)J_9(X).}
\tag{9}
$$
因此完整向量的 X 次数为
$1+4+6+53=64$，第64坐标为一，第65质量坐标为零，
并属于 R959 的原66维基
$\sigma^{390}(1,X,\ldots,X^{65})$。

特别这里的 degree 是390、Gaussian charge 是195。
(6) 的 $x$ 因子没有因原 R958 使用 norm $1\bmod6$ 而漏掉。
本候选也没有被先验地称作一个 degree130 的 $\delta$-拉回。

## 4. 原完整算子的真实多项式投影

令 $A_7,A_{19}$ 是现有390入口在同一次 run 生成的完整矩阵，
字段为 $\mathbf Q(\delta)$。所有66列、68个完整纤维、原
CM19 theta 平方锚、两算子的交换和共轭逆都由原 producer 保持。
R959 已独立用四个坏有理位的完整 Schwartz 确定原算术线；
本篇沿用其两个真实本征值
$$
e_7=\omega^2,\qquad e_{19}=-1.
\tag{10}
$$
不是用两个特征值重新猜 E65 的全部角色。

helper 只接收本次的 $A_7,A_{19},H$ 和65个原系数。
它不调用任何 producer，也不重复 E89 的重建。
原系数补上第66个零质量坐标，仍逐行回乘 (10)。

对 $A=A_\ell$，从整个矩阵求特征多项式 $\chi_A$，置
$$
m_A=\frac{\chi_A}{\gcd(\chi_A,\chi_A')}.
$$
本次已在全矩阵检查
$$
m_A(A)=0.
\tag{11}
$$
所以没有从目标一条线推断整个算子半单。
再令
$$
q_\ell(X)=\frac{m_{A_\ell}(X)}{X-e_\ell},\qquad
d_\ell=q_\ell(e_\ell)\ne0,\qquad
P_\ell=\frac{q_\ell(A_\ell)}{d_\ell}.
\tag{12}
$$
每一个 $P_\ell$ 都完整检查幂等、与其真实算子交换、
像满足本征值 $e_\ell$、并固定原算术向量。
两个 $P_\ell$ 交换，所以
$$
\boxed{\Pi_{65}=P_7P_{19}}
\tag{13}
$$
是一个显示的有限 CM 多项式算子。
reader 再核 $\Pi_{65}^2=\Pi_{65}$、整个秩恰为一、
两边的完整本征恒等式及其固定原向量。
它还核该完整投影矩阵在有理域上；这也由原两个共轭逆和
$e_\ell\bar e_\ell=1$ 的谱投影唯一性推出。

令 R959 的原首项一来源为
$$
F_{65,1}=\sigma^{390}\sum_{j=0}^{64}c_jX^j.
$$
本次实际通过的完整非零身份是
$$
\boxed{\Pi_{65}F=\alpha_{65}F_{65,1},\qquad
       \alpha_{65}=\frac{-25+175\delta}{5328}
       =\frac{25\omega}{72\gamma_{37}}\ne0.}
\tag{14}
$$
等号已在全部66个坐标回乘，系数从第64行读取；原第65质量坐标为零。
实际两个单算子投影的秩都是6，合成秩准确为1，且整个合成矩阵有理。
准确的投影分母为
$$
d_7=-6+6\delta=12\omega,\qquad d_{19}=-12.
\tag{14a}
$$

这些是整 CM 多项式。确切地，两个原对应在完整 degree390 的有限
Heisenberg 群上诱导有限阶自同构；某个幂遂由不可约性成为标量。
原 $F_{65,1}$ 的真实本征值 $\omega^2,-1$ 把该标量定为根单位，
所以整个对应具有有限阶。其所有本征值都是根单位，完整特征多项式及
平方自由根积在 $\mathcal O_K[X]$ 中；除去实际根所得 $q_7,q_{19}$
亦整。这使用整个 Heisenberg 交织与真实非零锚，不只在一个目标向量上
推断半单性；本次 (11) 又独立回乘了完整66维矩阵。

另有
$$
N_{K/\mathbf Q}(\alpha_{65})
=\frac{625}{2^6\,3^4\,37}.
\tag{14b}
$$
因而当前 $p>211$ 时，(14a)、所有投影系数的必要分母和
$\alpha_{65}$ 均为单位；这项投影不再增加新的目标坏素数。

## 5. 一个兼容原 norm7、norm19 的完整整框架

使用 R958(22) 的整 Hermitian 消元，但本次从行 (1) 开始，
按零起始指标
$$
5,\ 1,\ 0,\ 2,\ 3
$$
删除，最后留下第4项 $a=\gamma_{37}$。
准确的剩余范数链为
$$
\boxed{390,\ 66,\ 54,\ 51,\ 44,\ 37.}
\tag{15}
$$
对应整矩阵 $L$ 的第一行为 (1)，其余行为
$$
R_Ie_i-\overline{(A_{65})_i}\,A_{65}|_I.
$$
因此完整 Gram 为
$$
\boxed{L\bar L^t=
\operatorname{diag}(390,25740,3564,2754,2244,1628).}
\tag{16}
$$
其行列式范数为
$$
37(390\cdot66\cdot54\cdot51\cdot44)^2,
\tag{17}
$$
素于 $7\cdot19$，全部素因子不超过37。
所有 theta degrees 都是偶数。
reader 逐行核奇 CM 系数个数为偶、全部交叉 Gaussian 为零，
并回乘由
$$
(L^{-1})_{ji}=\overline{L_{ij}}/N_i
$$
给出的两个方向的完整逆。

所以
$$
\mathcal F=(9a)^{-1}L_*\rho_{\rm raw}
 \in\mathcal S_{390}\otimes\mathcal S_{25740}
 \otimes\mathcal S_{3564}\otimes\mathcal S_{2754}
 \otimes\mathcal S_{2244}\otimes\mathcal S_{1628}.
\tag{18}
$$
其第一边际是 (2)。整性沿用原 sigma 整有界和每个完整 theta 基
的互异首阶单位消元，不除去大阶乘。原 $p>211$ 使 (17) 的
所有分母为单位。

## 6. norm19 的真实奇 sigma 相位及整个六输入转移

两个 odd sigma 单支必须分别用完整纤维核，不能套用 R958 中
norm13 的负号。本次用实际 CM 群律重新生成
$$
r_{\gamma_7},\quad r_{\gamma_{19}},
$$
并将后者与原 R466/R480 的首一多项式及其 leading constant
$\gamma_{19}$ 整体比较。在目标 $x=1,2,3$ 的完整可分纤维中，
用原 normalized trace
$$
N_\gamma\sigma=
\gamma^{-1}\sigma\,
 \operatorname{Tr}_{[\gamma]}(r_{\bar\gamma}/r_\gamma)
\tag{19}
$$
读出两个方向的绝对相位。
其商是椭圆函数且在 $O$ 至多一阶极点，故必为常数；
完整纤维是在读该已知的常数，不是凭三个样点猜函数身份。

reader 对本次实际两个方向完整返回的结果为
$$
N_{\gamma_7}\sigma=N_{\bar\gamma_7}\sigma=\sigma,\qquad
N_{\gamma_{19}}\sigma=N_{\bar\gamma_{19}}\sigma=\sigma.
\tag{20}
$$
这四个绝对相位已由本次各三个完整纤维返回；没有改用历史归一化。

由 (17)，$L$ 在这四种 CM 核的六重积上均为双射。
完整重排六重 trace，(16) 与逐行半特征支付所有中心，
两边保总规范 $\gamma^{-6}$，而 (20) 的六次方为一。
故整个联合满足
$$
N_{\gamma,Y}\prod_{i=1}^5N_{\gamma,Z_i}\mathcal F=\mathcal F
\quad(\gamma=\gamma_7,\bar\gamma_7,\gamma_{19},\bar\gamma_{19}).
\tag{21}
$$
这是整个联合的关系，不是仅由第一边际推出。

第一轴上的 $N_\gamma N_{\bar\gamma}$ 实现原 Heisenberg 恒等
自同构，因为 $7,19$ 素于 $2\cdot390$。
整个不可约空间上它是标量；原 $F_{65,1}$ 的有理性与
(10) 的范数一把该标量定为一。
因此设
$$
B_7=\prod_{i=1}^5N_{\bar\gamma_7,Z_i},\qquad
B_{19}=\prod_{i=1}^5N_{\bar\gamma_{19},Z_i},
$$
同 R958 一样得到原整个来源上的
$$
N_{7,Y}^jN_{19,Y}^k\Pi_{0,Y}\mathcal F
=B_7^jB_{19}^k\Pi_{\mathbf Z}\mathcal F.
\tag{22}
$$
第一 principal 平均转为五伴随同时平均，使用六个 sigma 的总
角型零，保持物理 $Y$ 不变。

令
$$
\mathcal C_{65}=
 \frac{q_7(B_7)q_{19}(B_{19})}{d_7d_{19}}\Pi_{\mathbf Z}.
\tag{23}
$$
先由整个第一轴秩一像得到张量分离，再以 (14) 取伴随质量：
$$
\boxed{\mathcal C_{65}\mathcal F=F_{65,1}\otimes\Lambda_{65},
       \qquad\Lambda_{65}(0)=\alpha_{65}.}
\tag{24}
$$
由 (14a)–(14b)，原固定坏集外的当前 $p>211$ 使 (23) 为整算子，
且伴随质量是单位。读取第一变量六阶矩并除以
$720\Omega_p^6$，给 $\Lambda_{65}$ 的整有界测度；
其单位质量使它成为完整五变量 Amice 卷积单位。
这是完整加法卷积的陈述，不删除混合条件。

## 7. R959 的真实175缩放、周期和通常中央

本篇 (14) 使用首项一的 $F_{65,1}$。
R959 的全整数格使用
$$
\widehat F_{65,1}=175F_{65,1},\qquad
\widehat\Phi_{65}=175\Phi_{65}.
$$
这些尺度必须保留。对同一个 $b$ 模型，
$$
F_{65,b}(z)=b^{-1}F_{65,1}(b^{1/6}z),\qquad
F_b(z)=b^{-1}F_1(b^{1/6}z).
\tag{25}
$$
(24) 同时运输到原 $b=17$ 六输入。
取 $\Omega_{p,b}=b^{-1/6}\Omega_{p,1}$ 的相容原微分和周期，
R959(55) 准确给
$$
\boxed{\nu_{F_{65,17},p}
  =\frac{65}{17\cdot175}\widehat\nu_{65,p}.}
\tag{26}
$$
不能把390的 Gaussian charge写成65，也不能在此省去175。

全部二、三、五及两个十三位的角色、Schwartz、uniformizer 和
primitive 因子，均继承 R959 中已经识别的**同一**原来源。
特别三处是 $\delta^2$ 导子的 even 方向，十三处是分裂坏位；
本篇没有用本候选的六次首项或两 CM 特征值重做一个新的局部识别。

记原实际
$$
\widehat J_{65,p}(v)=
 \int_{\mathbf Z_p^\times}\langle Y\rangle^{(p-1)v}
                           d\widehat\nu_{65,p}(Y).
$$
对任意完整独立五伴随测试 $h$，(24)–(26) 给
$$
\boxed{\int_{Y\ {\rm unit}}\langle Y\rangle^{(p-1)v}h(\mathbf Z)
  \,d\nu_{\mathcal C_{65}\mathcal F_{17}}
 =\frac{65}{17\cdot175}\widehat J_{65,p}(v)
                              \nu_{\Lambda_{65,17}}(h).}
\tag{27}
$$
R959 已证明单位质量
$\widehat J_{65,p}(0)=0$，及首导数非零推出通常全 Sha 初级部分
有限的完整桥。所以原反证输入
$\widehat J'_{65,p}(0)=0$ 使 (27) 的完整条件中央行为零。
若 $h$ 解析依赖 $v$，额外导数项仍由同一个单位质量零消去。

## 8. 每个有限支和旧四条输出的完整返回

把 (23) 中两个多项式逐项展开。
第 $j,k$ 项令 $\beta=\gamma_7^j\gamma_{19}^k$，其完整五伴随
trace 必须包含所有
$$
\mathbf t\in E[\bar\beta]^5,
$$
总系数 $\bar\beta^{-5}$、原对称 lift 的全部中心，
以及伴随变量的 $\beta$ 拉回。
角平均还含全部 $\zeta\in\mu_6$。
每一个完整测试都准确变成
$$
\boxed{f(Y,\mathbf Z)\longmapsto
                    f(Y,\zeta\mathbf Z/\bar\beta).}
\tag{28}
$$
此操作保持第一 $Y$；没有额外的第一变量单位尺度对数。

返回原六输入时是 $L^{-1}(Y,\mathbf Z)^t$。
对旧实际四条行
$$
\begin{aligned}
a_S&=(\delta,2\delta,\gamma_7,\bar\gamma_7,1,2),\\
a_T&=(\delta,2\delta,\gamma_7,\bar\gamma_7,3\delta,4),\\
a_{W,+}&=(\delta,2\delta,\gamma_7,\bar\gamma_7,1,2\gamma_{37}),\\
a_{W,-}&=(\delta,2\delta,\gamma_7,\bar\gamma_7,1,2\bar\gamma_{37}),
\end{aligned}
$$
reader 逐个全行回乘 $(rL^{-1})L=r$。它们在该分支的单位条件、
深管条件及 logarithm 都使用
$$
(rL^{-1})_0Y+
 \frac{\zeta}{\bar\beta}\sum_{i=1}^5(rL^{-1})_i Z_i.
\tag{29}
$$
旧 $T$ 来源的 $6\delta$ 不变；旧 $W$ 的
$89/17$ 比较也不变。
(27) 不会使这些混合第一轴的条件自动成为独立伴随测试，
更没有把原六来源的乘积赋中央零。

## 9. 公开执行和准确状态

新增独立 helper 为
$\texttt{check-original-e65-six-sigma-projection.py}$，只接收
同一次 $\texttt{construct_complete_source}$ 返回的
$A_7,A_{19},H$、完整矩阵哈希和原65个系数。
原函数的默认两项返回保持；入口用
$\texttt{return_context=True}$ 才取出同一次已经生成的矩阵。
它不重跑390、E89或任何旧源 producer。

本次与 R960 的角消费者共用现有
$\texttt{rank2-sha-e65-full-cm-source.yml}$，无新 workflow、
无第二个重型运行。源清单、原 pin、原局部 Schwartz、旧六 jet
以及两消费者的完整回执均保留；不保存生成系数或矩阵文件。

root 已从本次原始 job 日志独立回读并核对：

1. 原完整66维 source 矩阵的同次哈希与唯一原向量；
2. (7)、(9) 的全部多项式恒等式；
3. (11)–(14) 的全矩阵身份与精确非零 $\alpha_{65}$；
4. (20) 的 norm7/norm19 两方向完整 sigma 相位；
5. (15)–(17) 的全部 Gram、半特征、两边逆和 (29) 的旧行返回；
6. 本次源提交、run/job 标识和 stdout 哈希。

这些门已全部 PASS，本文增加的是同原六 sigma 上的一个明确
固定条件中央族。混合余域、跨所有原来源传播以及无穷不同 $p$
的最终量词继续处理。

### 9.1 本次完整公开回执

- 源提交：`9144dc0062fd9423f8a9f94978643787b863eb36`。
- [run45818310281](https://github.com/Rogerhu12/math-research-public/actions/runs/45818310281)，job139903674795，2026-11-26 12:23:50 UTC 实际 success。
- 原入口参数 `--workers=4`，python-flint0.9.0；全部12源清单及10个Python AST通过；完整64个局部Schwartz门、66维原390和同次原178重建、六低jet均保持。
- 整体355.919856256秒；本篇消费者38.16617227099999秒。
- helper：21428 bytes，SHA256 `bac8a8109ef029d4665586427fe331e76fc2299848e2cea2bf85e7abb74487f3`。
- 原入口：16401 bytes，SHA256 `bd0f2220e47b529927f089452e556481aa40b97e9d86896fc16f339266877844`。
- 原完整390矩阵 SHA256 `e80e5777735077da004012b5abe8dfd2ba246b9404fd53899502c453242d1fff`；原向量 SHA256 `3cedb9c16e797086890bd0fd4a2d760d49ce3fd78a204b45d2a5318aff636318`，均与R959独立首次构造相同。
- 真实六sigma候选 SHA256 `85aa12d19e321597fb2857a1e2cb1cf16029b2288514df18b66813eddb25295d`；完整秩一投影 SHA256 `06bb52165121f3e156223541c576ccf974f5984402e2128ad02aba364ebc34d0`。
- 两个完整特征多项式均66次，平方自由annihilator均12次，显示投影多项式均11次；各自全部回乘和rank6、合成rank1、两侧本征及原源返回通过。
- 整框架 SHA256 `8c31dcd174e93dd6be7964415dc48dd6de23ad2d0459d0130d7ab4cb8058ba12`；整逆 SHA256 `84ff6614d0395ac70278c5d72994eb5f36c684f56369af7887dfb07a33e18abb`。行列式范数359958168995985331200，奇CM个数依次4、0、0、4、2、2；全部旧S/T/W±读数逐行返回。
- manifest SHA256 `c348470b3e911b7cd9c1af1e7fe103bdc175a18f0d52aca90be047d2d338752f`。
- 原程序 stdout **16550 bytes**，SHA256 `a96cd6c06d334178bf61dc0e3eb0c6d962aede4bde6e461bfd6d6b24c5aba2bb`；这是未加script/result包装的原stdout，root按原字节切片独立复核。
- 完整job日志54187 bytes，SHA256 `3fb9db7ae82af87c4e7c97c6403fefcda61f4ec4a159d8ed35087ece3aabfff2`。

全部源及其余旧pin、工作流和请求哈希见[同次消费者记录](../notes/2026-11-26-e65-six-source-consumers.md)。按根规则15，只保存源码、参数、run、哈希及上述数学结论；不保存生成矩阵或系数表。


## 依赖

- [R958：原 E89 同六 sigma 全投影及全部伴随/有限支规范](R958-original-e89-common-six-sigma-cm-projection.md)。
- [R959：原 E65 全局部来源、完整CM与通常Selmer桥](R959-original-e65-two-independent-points.md)。
- [R465：原六输入和原 S/T 完整尺度](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R546：完整五伴随 CM 转移和混合切域](R546-original-third-sigma-full-five-companion-cm-transfer.md)。
