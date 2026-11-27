# R150：余 W 的原均值全局多项式坐标与明确首一 w 六次环境

**状态：已证明。** 在已经完整排除 J19 的当前 W 余权域，旧原均值恢复可以加强为一个不倒置 y−1 的多项式环同构。三个原二次式的已刊常数 cofactor 随之成为一条明确的首一 w 六次式；结合已刊首一 Y 二次式，得到一个明确的十二维有限自由环境，原必要商是它的商。本页不声称整个 W 排空。

会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

## 1. 准确系数环与原均值

A 取整个 J19 排除定理所明列的 W 权参数局部环，再倒置已完整排除的 J19。沿用

$$u=e+1,\quad Q=ek,\quad V=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV},\quad d=1-Q,$$

$$M=4bcd=\ell(2u-\ell Q)-u^2,\qquad
N=u(2-2u-Q)+\ell Q(2u-1)=-e^2uH/V,$$

$$H=4ek-k^2-4k-8,\qquad x_*=1+u-u/\ell.$$

本页使用的 u,d,M,ell,N 及 J19 都是这个明确系数环中的单位。此前权排除定理有其原域；这里不把它们外推到尚未覆盖的一般 hU=kU 碰撞，也没有另外要求物理 D 可逆。

令同一个原 Gram 的两条 singleton 均值为 EBe、EBo，并记

$$L=(u-\ell)E_{B,e}+\ell d E_{B,o},$$

$$c_0=\frac{2e}{u}+\frac{T_0\ell d}{uM},\qquad
\beta=\frac{\ell N}{uM},\qquad \gamma=\beta^{-1}. \tag{1}$$

已刊完整有限均值的 compact_t 身份等价于以下原多项式恒等式：

$$L=M(y-1)\left(t-\frac{2x}{u}+\frac{2dy}{u}-c_0\right)
-\frac{\ell N}{u}(x-x_*). \tag{2}$$

(2) 是完整有限式，包含全部低次项。其来源为已刊原恢复源 27ad028d 的 meancombo、精确 Y 因子取消及 compactWorkingFormulaVerified=true；不是由最高次项推断有限关系。也可将该源的 compact_t 代回两边逐项获得 (2)。

## 2. 不需要 y−1 逆的完整坐标同构

定义两个多项式坐标

$$Y=y-1,\qquad
w=\gamma\left(t-\frac{2x}{u}+\frac{2dy}{u}-c_0\right). \tag{3}$$

由 (2)，

$$L=\frac{\ell N}{u}\{Yw-(x-x_*)\}. \tag{4}$$

括号外系数是 A 的单位。因此在 L=0 的整个原均值超曲面上，反向公式为

$$x=x_*+Yw,\qquad y=1+Y,$$

$$t=\frac{2(x_*+Yw)}u-\frac{2d(1+Y)}u+c_0+\beta w. \tag{5}$$

将 (5) 代入 (3)，两个新坐标逐项原样返回；将 (3) 代入 (5)，x 的差恰为 (4) 的单位倍数，y 无差，t 的差为 x 差的 2/u 倍。因此

$$A[x,y,t]/(L)\ \simeq\ A[w,Y]. \tag{6}$$

这是环同构，包括非约化商和 Y=0 的整个纤维。(3) 没有 y−1 分母。旧表达 w=(x−x*)/(y−1) 在 y−1 可逆时与 (3) 一致，但 (3) 已在整个 L 商内定义该元素。

在 (6) 中，EBo 由 L=0 与 EBe 恢复：

$$E_{B,o}=-(u-\ell)E_{B,e}/(\ell d).$$

故六条原 Gram 必要式定义的商，准确等同于 A[w,Y] 中五条原式 E1,EBe,N1,Ns,Ps 的商。个别原 N/P 和原值等式仍由完整原系统另外保留；这里没有用 weighted 式替代所有原值条件。

## 3. 原二次头与 w 六次首项的准确恒等式

记 G1、GB、GN 为 (5) 代回后的三条完整原二次式 E1,EBe,N1，保持原尺度。它们对 w,Y 分别至多二次。写

$$G_i=C_{i0}(w)+C_{i1}(w)Y+C_{i2}(w)Y^2,\qquad
C=(C_{ij})_{i=1,B,N;\ j=0,1,2}. \tag{7}$$

令 H 为原 E1,EBe,N1 的二次头在 y=0 上、按 x²,xt,t² 排列的系数矩阵。已刊原 binary 头给出

$$H_1=2(1-2\ell)x^2+4bc\,xt,\qquad
H_B=\frac{\ell}{2}(t^2-2xt),$$

$$H_N=uH_1-\frac{4ubc}{\ell}H_B
-4P_{02}\lambda_h(\lambda-T)_h,$$

$$\lambda_h=\frac{T_0x+2bcQt}{2P_{02}},\qquad
(\lambda-T)_h=\frac{\ell T_0x+2bc(Q+2e)t}{P_{02}}.$$

因此，设

$$Z=4bcQ(Q+2e)+T_0(Q+2e+\ell Q),$$

则直接展开给

$$\Delta_H:=\det H
=\frac{4\ell bc}{P_{02}}\{(1-2\ell)Z-\ell T_0^2\}
=-\frac{4\ell bc\,e^4u(k+2)}{kV^3dP_{02}}J_{19}. \tag{8}$$

(8) 最后一步只是上述 W 权公式的代入、清分母和多项式恒等式；所有外因子均为 A 单位。因此 Delta_H 在当前域已是单位。

现在 (5) 中的 w 最高系数分别为

$$[w]x=Y,\qquad [w]t=(2/u)Y+\beta,\qquad [w]y=0.$$

故 C 的 w² 系数矩阵等于 H 乘以

$$
S_\beta=
\begin{pmatrix}
0&0&1\\
0&\beta&2/u\\
\beta^2&4\beta/u&4/u^2
\end{pmatrix}.
$$

列次序仍为 1,Y,Y²，且

$$\det S_\beta=-\beta^3.$$

于是对完整有限 determinant

$$D_6(w)=\det C(w)$$

有准确的首项身份

$$[w^6]D_6=-\beta^3\Delta_H\in A^\times. \tag{9}$$

没有用任何未付的投影首项。这也解释了此前实际 D6 首项在剥已付因子后恰剩 16J19 的结果；不是重新计算一次旧 determinant。

## 4. 一条明确的首一 w 六次原式

令 cof_i 为 C 第 i 行、常数列的余子式。完整三列恒等式为

$$\sum_i\operatorname{cof}_i C_{ij}
=\begin{cases}D_6,&j=0,\\0,&j=1,2.\end{cases}$$

因此

$$D_6=\sum_i\operatorname{cof}_i G_i$$

是真实原组合。由 (9) 定义

$$q_w(w)=\frac{D_6(w)}{-\beta^3\Delta_H}
=w^6+a_5w^5+\cdots+a_0\in A[w]. \tag{10}$$

这给出可再生的明确六个系数：

$$a_j=\frac{[w^j]\det C(w)}{-\beta^3\Delta_H},\qquad 0\le j<6.$$

每个分母都由已刊结论支付。所有 cofactor 和原行的定义都在 (1)、(5)、(7) 中固定，故 (10) 是实际首一式，并非仅用 determinant trick 宣称某个首一式存在。无需再展开、保存或重复运行那 2043 项的旧 primitive D6。

此前执行的归一化 D6 对 e,k,w 次数为 (19,26,6)，2043 项，SHA256：

03ead359b4ef10233f22120e5b0e742e5375a25a70fd730b80b1e5ef3e7afdff。

其归一化只除以前已付权因子，故与这里保持原尺度的 D6 相差 A 单位；(9) 与 (10) 在两种尺度下相同。

## 5. 明确的十二维有限自由环境

已刊全图原首一 Y 定理给出同五条原式的真实组合

$$q_Y=Y^2+\mathcal A(w)Y+\mathcal C(w),\qquad
\mathcal A,\mathcal C\in A[w],\quad
\deg_w\mathcal A,\deg_w\mathcal C\le4. \tag{11}$$

该定理在 J19 尚未支付时已经全图成立，所以在当前进一步局部化的 A 上继续成立。取

$$R=A[w]/(q_w),\qquad
C_{\mathrm{amb}}=R[Y]/(q_Y). \tag{12}$$

(10) 首一六次，故 R 对 A 自由，基底 1,w,...,w^5；(11) 首一二次，故 C_amb 对 R 自由，基底 1,Y。因此 C_amb 对 A 自由，明确十二个基元为

$$1,w,\ldots,w^5,\quad Y,wY,\ldots,w^5Y.$$

这不要求任一多项式不可约、无重根或任何系数环为域。所有乘法都可先按 (10)、再按 (11) 作首一除法；这些规则的相容性来自迭代商环本身。

五条完整原式在 C_amb 的像仍须全部施加。因为 q_w、q_Y 均在原五式理想内，原必要商准确是

$$C_{\mathrm{amb}}/
(\overline E_1,\overline E_{B,e},\overline N_1,
 \overline N_s,\overline P_s). \tag{13}$$

原必要商不因此被声称自由；只有 (12) 的明确环境是自由十二维。后续可在此固定环境中作实际原组合、有限常数代数返回或参数 cofactor，所有非单位 pivot 和规范表示范数零纤维仍须保留。

## 6. 已有实际证据与本页新证明的界限

本页是对已刊原身份的解析推论，没有重新运行旧成功门，也没有将新 A[y] 三生成源的未执行状态写成成功。

原均值和 D6 源：

notes/2026-11-27-unit211-generic-LS-W-y-not-one-original-mean-bivariate-system-8542.py

blob 58c1a8fea5fd6c09e1b4614a1fe4b91b9f8fb742，
SHA256 27ad028d628b57855fe3b4587ead848f171e035a6128142745ecafc2d0fc3303。
实际 run45975400648，driver 2.495136965 秒，RSS 65100 KiB，内层 exit 0；完整均值恢复和 D6 原三列乘回均已记录。

原首一 Y 源：

notes/2026-11-27-unit211-generic-LS-W-global-monic-Y-original-linear-system-8542.py

blob 86bd0e68eed8cbbf2053603b136decbc406067b9，
SHA256 0e3be45e5daccec0e03c8caef3d868557f7d2da5eb2e3abede3ee71a82c5aad4。
实际 run45979307745/job140438859151，driver 9.457148185 秒，RSS 145092 KiB，内层 exit 0。其 qY 完整原迹 SHA256 为
078013c6106077b0e12f68a645b1165a81978d0128593bea4eb6db840d84d9eb。

原 binary 头来自已刊整个 J19 四次原 Gram 输入，及随后完整 J19 排除定理。J19 的 568 次整有限自由提升与五个低次 QQ 直接返 1 已单独完成，不在此重放。

本页的新内容是 (2)–(6) 的全局原坐标同构、(9) 的准确首项变换和 (10)–(13) 的明确首一环境。它没有关闭剩余 W、R150 或普通不变子空间问题。
