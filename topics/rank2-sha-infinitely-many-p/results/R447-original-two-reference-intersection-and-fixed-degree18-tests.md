# R447 — 原两参考交域与固定十八次完整第二输出测试

日期：2026-11-14。**状态：已证明。**

R443 的四维第一 principal 来源格虽然不含原 $S$，却与
R307 已完整识别的三条原算术来源有一个准确的二维交域。
本篇给其完整基，以及两个固定十八次第二输出测试，分别抽回
$H_3-840bS$ 和 $H_5-672bS$。
两个测试在原 $G_{18}$ 上的积分恰好相同，均为 $1512b$。
全部矩阵、来源和原周期规范均保留；参考的非零中央质量
不被当作其中央导数已知。

## 1. 原六维格和两条真实参考

固定原 $b=17$、同一普通周期 $\Omega$、同一 ray 和
$$
\lambda=-\bar\pi_0^{-1},\qquad d=p-1,\qquad p>19.
$$
为写恒等式暂保参数 $b$。以下 $\mathsf X=x^3$ 是椭圆函数变量，
与测度的第二输出 $X$ 区分。

R307 已识别的三条原来源为
$$
S=\sigma^{34}x^2P_1(\mathsf X),
$$
$$
P_1(\mathsf X)=
\mathsf X^4-\frac{53b}{7}\mathsf X^3
-\frac{12b^2}{7}\mathsf X^2-\frac{80b^3}{7}\mathsf X
-\frac{128b^4}{7},
$$
$$
H_3=\sigma^{34}x^2P_3(\mathsf X),\qquad
P_3=\mathsf X^5-208b\mathsf X^4+400b^2\mathsf X^3
       +8128b^3\mathsf X^2+12032b^4\mathsf X-2048b^5,
$$
$$
H_5=\sigma^{34}x^2P_5(\mathsf X),\qquad
P_5=\mathsf X^5+272b\mathsf X^4-272b^2\mathsf X^3
       -14912b^3\mathsf X^2-6784b^4\mathsf X+1024b^5.
\tag{1}
$$
在原 $b=17$，$H_3,H_5$ 是 R307 的两条秩零 Hecke 来源，
保留该篇的原 Schwartz、共同 frame 及全部周期常数。
其质量均为 $1$；只有 $S$ 是此三条中的原秩二来源。

沿用 R443 的四条实际来源和四条第二轴来源
$$
A_j=\frac{\sigma^{34}x^2}{252}
       \sum_{a=0}^5E_2[a,j]\,b^{7-a-j}\mathsf X^a,
\qquad E_j=\sigma^{18}\mathsf X^j,\qquad0\le j\le3.
\tag{2}
$$
这里完整整数块是
$$
E_2=
\begin{pmatrix}
-90112&-407552&-19456&768\\
-75776&-397312&-128384&-2112\\
-37888&-60800&-37312&-4464\\
-10624&-163328&-61072&480\\
6592&12656&5104&-123\\
-16&-32&11&0
\end{pmatrix}.
\tag{3}
$$
R443 已在完整第一 $\mu_6$ 投影上证明
$$
\Pi_{Y,0}\mathcal K_1
 =\Pi_{Y,0}\mathcal K_R
 =\sum_{j=0}^3A_j\otimes E_j.
\tag{4}
$$
不是只在某个有限阶 Taylor 截断上成立。

## 2. 完整二维交域

直接比较 (1)–(3) 的全部六个系数，得到
$$
\boxed{
H_3-840bS=
-\frac{287}{12b^2}A_0-\frac7{3b}A_1
-\frac{56}{3}A_2-\frac{448b}{3}A_3,}
\tag{5}
$$
$$
\boxed{
H_5-672bS=
\frac{28}{3b^2}A_0-\frac{28}{3b}A_1
+\frac{28}{3}A_2+\frac{2240b}{3}A_3.}
\tag{6}
$$
所有系数在当前原普通处都是整的。

R443 已证明 $\langle A_0,A_1,A_2,A_3\rangle$ 的秩为四，
加上 $S$ 后秩为五，且两次秩在每个当前剩余域中都保持。
由于 (5)、(6) 把 $H_3,H_5$ 放进这个秩五格，
对于任意整系数 $\alpha,\beta,\gamma$，准确有
$$
\boxed{
\alpha S+\beta H_3+\gamma H_5
\in\langle A_0,A_1,A_2,A_3\rangle
\quad\Longleftrightarrow\quad
\alpha+840b\beta+672b\gamma=0.}
\tag{7}
$$
其中必要性使用的正是 R443 已付的饱和增广格，
不是仅在分式域中的维数计数。
条件右侧的 $\alpha$ 系数是 $1$，所以其核为饱和秩二格。
因此完整交域恰由 (5)、(6) 两条生成；
不存在把原 $S$ 单独抽出的未经证明步骤。

## 3. 原周期下的全部十八次测试矩阵

对测度第二输出写
$$
\xi=X/\Omega,\qquad
\phi_k(\xi)=\frac{\xi^{6k}}{(6k)!},\qquad0\le k\le3.
\tag{8}
$$
原 $\Omega$ 是当前普通处的单位。
由于 $p>19$，这些除阶乘以及下文所有有理分母都是单位。
因此每个固定组合 $\sum c_k\phi_k$ 是原 $\mathbf Z_p$ 上的
整连续测试；没有重置原测度的周期。

令
$$
\mathcal T_{k,j}=\int\phi_k(X/\Omega)\,d\nu_{E_j}(X).
$$
因为 $\nu_{E_j}$ 的实际指数生成函数是 $E_j(\Omega z)$，
矩阵项恰为 $E_j(z)$ 的 $z^{6k}$ 系数。
准确得到
$$
\boxed{
\mathcal T=
\begin{pmatrix}
0&0&0&1\\
0&0&1&-\frac65b\\
0&1&-\frac{27}{35}b&\frac{1236}{1925}b^2\\
1&-\frac{12}{35}b&\frac{43011}{175175}b^2&
                         -\frac{2997734}{14889875}b^3
\end{pmatrix},
\qquad \det\mathcal T=1.}
\tag{9}
$$

为核定每个常数，令 $w=z^6$。同一曲线的微分关系给
$$
x(z)=z^{-2}\left(
1-\frac b7w+\frac{b^2}{637}w^2-\frac{b^3}{84721}w^3+O(w^4)
\right),
$$
$$
\log\frac{\sigma(z)}z
=\frac b{210}w-\frac{b^2}{84084}w^2
  +\frac{b^3}{25924626}w^3+O(w^4).
\tag{10}
$$
第一式由 $x''=6x^2$ 及原曲线常数确定；
第二式由 $(\log\sigma)''=-x$ 和 $\sigma'(0)=1$ 确定。
将它们代入 $\sigma^{18}x^{3j}$ 即给 (9) 的每一个系数。
测试的次数至多十八，所以高阶尾在这些测试中严格不出现。

反向三角形的四个首项均为 $1$，故 (9) 也直接证明：
任意整四元组 $(v_0,v_1,v_2,v_3)$ 都可由一个整的固定十八次测试
准确实现为 $(\int h\,d\nu_{E_j})_j$。
这没有付出任何新的 $p$ 饱和损失。

## 4. 两个显示的固定十八次测试

在 (8) 的基中定义
$$
\boxed{
h_3(\xi)=
-\frac{4031937b}{23375}
-\frac{6282301}{300300}\frac{\xi^6}{6!}
-\frac{158}{15b}\frac{\xi^{12}}{12!}
-\frac{287}{12b^2}\frac{\xi^{18}}{18!},}
\tag{11}
$$
$$
\boxed{
h_5(\xi)=
\frac{17654112b}{23375}
+\frac{173444}{75075}\frac{\xi^6}{6!}
-\frac{92}{15b}\frac{\xi^{12}}{12!}
+\frac{28}{3b^2}\frac{\xi^{18}}{18!}.}
\tag{12}
$$
所有数值分母的素因子都不超过 $19$，并保原 $b=17$。
实际测试是 $h_a(X/\Omega)$，不把 $\Omega$ 从测度中删掉。

用 (9) 直接相乘得到
$$
\boxed{
\left(\int h_3(X/\Omega)\,d\nu_{E_j}\right)_{j=0}^3
 =\left(-\frac{287}{12b^2},-\frac7{3b},
        -\frac{56}{3},-\frac{448b}{3}\right),}
\tag{13}
$$
$$
\boxed{
\left(\int h_5(X/\Omega)\,d\nu_{E_j}\right)_{j=0}^3
 =\left(\frac{28}{3b^2},-\frac{28}{3b},
        \frac{28}{3},\frac{2240b}{3}\right).}
\tag{14}
$$
所以 (4)–(6) 给完整测度级第一投影身份
$$
\boxed{
(Y)_*\!\left(h_3(X/\Omega)\Pi_{Y,0}\nu_{\mathcal K_1}\right)
 =\nu_{H_3}-840b\nu_S,}
\tag{15}
$$
$$
\boxed{
(Y)_*\!\left(h_5(X/\Omega)\Pi_{Y,0}\nu_{\mathcal K_1}\right)
 =\nu_{H_5}-672b\nu_S.}
\tag{16}
$$
对 $\mathcal K_R$ 与 R446 的偶来源 $E$，两式同样成立。
这是完整第一输出测度身份，随后可以施加任意第一输出测试，
不只一个中央系数。

## 5. 完整 Mellin 行、真实参考质量与未知斜率

令
$$
J_F(u)=\int_{\mathbf Z_p^\times}
                    \langle Y\rangle^{du}\,d\nu_F(Y),
$$
并记 $\Gamma_i(u,h)$ 为 $\mathcal K_i$ 上的同一第一 principal
测试乘完整第二输出测试 $h$。
由 (15)、(16)，整条权函数满足
$$
\boxed{
\Gamma_1(u,h_3)=\Gamma_R(u,h_3)
 =J_{H_3}(u)-840bJ_S(u),}
\tag{17}
$$
$$
\boxed{
\Gamma_1(u,h_5)=\Gamma_R(u,h_5)
 =J_{H_5}(u)-672bJ_S(u).}
\tag{18}
$$
这里 $\Gamma_i(u,h_a)$ 的第二测试始终是 (11)、(12)
在 $X/\Omega$ 上的值。

整个 $\mathcal S_{34}$ 的真实核心在当前 ray 上为普通反射
（R443）。三条实际来源都偶，因此其完整核心均为 $+\lambda$。
结合质量 $S(0)=0$、$H_3(0)=H_5(0)=1$，
$$
\boxed{
J_S(0)=0,\qquad
J_{H_3}(0)=J_{H_5}(0)=1-\lambda\in\mathcal O^\times.}
\tag{19}
$$
这些量和 R307、R308 的真实算术规范相同。

在中央求导只得到
$$
\Gamma'_1(0,h_3)=J'_{H_3}(0)-840bJ'_S(0),\qquad
\Gamma'_1(0,h_5)=J'_{H_5}(0)-672bJ'_S(0).
\tag{20}
$$
若原 $J'_S(0)=0$，右侧分别是两条真实秩零参考的未知导数。
本篇没有把 (19) 的单位质量升级为它们的导数非零，
也没有将它们作为新的秩二曲线。

## 6. 两个测试在原小核上恰有同一返回

R426 的同一原第二来源满足
$$
G_{18}=E_3-30bE_2-144b^2E_1-32b^3E_0.
\tag{21}
$$
代入 (13)、(14)，完整相消给
$$
\boxed{
\int h_3(X/\Omega)\,d\nu_{G_{18}}
=\int h_5(X/\Omega)\,d\nu_{G_{18}}
=1512b\in\mathcal O^\times.}
\tag{22}
$$
因此 R430 的完整条件中央身份成为
$$
\boxed{
\Gamma_0(u,h_3)=\Gamma_0(u,h_5)=-1008bJ_S(u).}
\tag{23}
$$
特别，对差测试 $h_3-h_5$，原 $\mathcal K_0$ 的这条完整权函数
恒为零；不需要任何算术失败假设。

在 R446 的实际三态基 $E,V,O$ 中，(17)、(18)、(23) 给
$$
\boxed{
\begin{array}{c|cc}
&h_3&h_5\\ \hline
\Gamma_E&J_{H_3}-840bJ_S&J_{H_5}-672bJ_S\\
\Gamma_V&-J_{H_3}-168bJ_S&-J_{H_5}-336bJ_S\\
\Gamma_O&0&0 .
\end{array}}
\tag{24}
$$
残余 $Q$ 核心准确交换 $V,O$，但它作用在保独立 sigma 的真实
来源上，附带原输入深度条件；不能直接用该交换将表中第一列
或第二列的参考导数赋零。

同一层的三条真实 carry 也可使用这两个固定测试。
由 R446 (26)，其完整组合在两个测试上都准确返回
$-1008b\lambda(1+\eta\lambda)(1+\lambda^2)J_S(u)$。
同一个原算术中央因此通过两条已识别参考行重新进入实际
三态闭包，但新增的参考斜率仍按 (20)、(24) 保留。

## 7. 精确证书与后续接口

[check-r447-two-original-reference-tests.py](../scripts/check-r447-two-original-reference-tests.py)
在 $\mathbf Q(b)$ 上检查全部六维多项式身份、矩阵 (9)、
两个测试的四个完整矩、两个 $1512b$ 返回及所有分母。
输出完整常数在
[check-r447-two-original-reference-tests.json](../scripts/check-r447-two-original-reference-tests.json)。
核算不作目标素数扫描、不作有限点插值，也不改变 R443 的证书。

本篇提供的新增接口是：实际四维 principal 格中的两条方向
已有原算术身份，且可用固定、整、无额外饱和损失的第二输出测试抽取。
还须将这些准确行与保独立伴随输入的完整核心、原非零隐藏域
及其补集相接；秩零参考的质量不能代替那一步。

## 依赖

- [R307：三条原算术来源与全部参考常数](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)。
- [R308：真实参考完整核心与中央质量](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)。
- [R430：原小核的完整条件中央](R430-original-integral-second-output-division-and-degree18-mixed-rows.md)。
- [R443：完整四列和饱和增广格](R443-original-residual-quarter-source-and-complete-central-return.md)。
- [R446：实际三态闭包及完整一层 carry](R446-original-three-state-quarter-closure-and-one-layer-full-carry.md)。
