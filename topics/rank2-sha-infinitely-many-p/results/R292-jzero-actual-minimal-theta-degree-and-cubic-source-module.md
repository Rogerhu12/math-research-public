# R292 — 新 j=0 实际来源的最小 theta 次数、三次 Heisenberg 模与全纯根补偿

日期：2026-11-13。**状态：以下原 Schwartz 来源的准确 degree-$34$ 下降、完整 Gaussian/sigma frame、实际 $\mu_6$ 角色、最小次数、三次覆盖上的完整截面模及原来源的全纯 $v^{\pm2}$ 补偿均已证明。补偿来源没有被认作原 Hecke 特征的同一条线，也没有把有限窗口中的 Frobenius 因子删成全局恒等式。**

这里使用 R288 的固定曲线 $E:y^2=x^3+17$ 和真实三次同源，并使用 R290 已构造的原二、三、十七处 Schwartz 函数。所有出现的 theta 线丛和有限群作用均来自该实际函数。

## 1. 原 Schwartz 级数的真实下降

写 $\delta=i\sqrt3$、$\omega=(-1+\delta)/2$。R290 的原有限函数给
$$
a_n=v_2(n\bmod4)\,f_{17}(3n\bmod17),\qquad
v_2=(1,t,-1,t),\quad t=\frac{1+\sqrt3}{\sqrt2}.
\tag{1}
$$
$f_{17}$ 是原 nonsplit torus 的 $g^{12}$ 特征线，已经用精确有限 Weil 矩阵构造，且是非零实偶函数。其真实有理支撑为 $n/102$。置
$$
\tau_0=\delta/3,\qquad
F(Z)=\sum_{n\in\mathbf Z}a_n
 \exp\left(\frac{\pi i\tau_0n^2}{68}+2\pi inZ\right).
\tag{2}
$$
因为 $a_n$ 的周期为 $68$，原矩形格上的准周期为
$$
F(Z+1)=F(Z),\qquad
F(Z+\tau_0)=e^{-68\pi i\tau_0-136\pi iZ}F(Z).
\tag{3}
$$
所以 (2) 首先是 degree-$68$ 的实际截面。

原二处向量还准确满足
$$
(-1)^na_{n+34}=-a_n.
\tag{4}
$$
十七处在这次位移中不变，因为 $3\cdot34\equiv0\pmod {17}$。令
$$
s=\frac{1+\tau_0}{2}=\frac1{1-\omega}.
$$
在 (2) 中将 $n$ 改成 $n-34$，由 (4) 得
$$
\boxed{F(Z+s)=e^{-34\pi is-68\pi iZ}F(Z).}
\tag{5}
$$
例如先沿 $(1-\tau_0)/2$ 移位得到
$-e^{68\pi iZ-17\pi i\tau_0}$，再使用 (3)，负号恰与
$e^{-17\pi i}$ 相合。因此 (5) 没有未指定的半特征。

格
$$
\Lambda=\mathbf Z+s\mathbf Z=(1-\omega)^{-1}\mathbf Z[\omega]
\tag{6}
$$
是最大整环的实际 CM 格。原来源在此格上准确为 degree-$34$ 的标准零特征截面。这是由 (1) 证明的下降，而不是另外选择一个次数相同的 theta 幂。

## 2. 原 Hermite Gaussian 正是 reduced sigma frame

设 $\sigma_\Lambda$ 取导数一的 Weierstrass 规范。由于 $\omega\Lambda=\Lambda$，其准周期满足
$\eta(\omega\lambda)=\omega^{-1}\eta(\lambda)$，故 $\eta(\lambda)=B\bar\lambda$。
Legendre 关系
$\eta(1)s-\eta(s)=2\pi i$ 给
$$
\eta_1=\frac\pi{\operatorname{Im}s}=2\sqrt3\pi.
\tag{7}
$$
由 (3)、(5)，
$$
S_\Lambda(Z)=e^{17\eta_1Z^2}F(Z)
=e^{34\sqrt3\pi Z^2}F(Z)
\tag{8}
$$
与 $\sigma_\Lambda^{34}$ 具有相同自动因子。因为 $34$ 为偶数，标准零特征对应的除子类恰为 $34(O)$；没有残留二挠 twist。

R290 原 Hermite 生成函数是
$$
\mathcal B(t)=e^{-t^2/(8\pi)}F\left(
\frac{\sqrt{51\sqrt3}}{204\pi i}t\right).
$$
若 $Z=\sqrt{51\sqrt3}\,t/(204\pi i)$，则准确有
$$
-\frac{t^2}{8\pi}=34\sqrt3\pi Z^2.
\tag{9}
$$
所以原 Hermite 函数就是 (8)，没有需要另行猜测的指数一次或二次因子。

取固定周期尺度 $\Omega$，使 R288 的 $E:y^2=x^3+17$ 的格为 $\Omega\Lambda$，并置 $z=\Omega Z$。于是
$$
\sigma_E(z)=\Omega\sigma_\Lambda(Z),\qquad
x_E(z)=\Omega^{-2}x_\Lambda(Z).
\tag{10}
$$
下文均使用 R288 的 $z,x,y,\sigma$。整体非零标量不影响截面所在的原特征线；(9)、(10) 明确保留了从真实 Hermite 参数到此规范的全部尺度。

## 3. 实际 $\mu_6$ 特征与五维原源

原 $a_n$ 为偶函数，故 (8) 是偶函数。$\mu_3$ 的相位也由实际 Schwartz 数据确定：R290 的原二处 $\omega$ 算子在 (1) 的线上的特征值为一；三处的函数对其已指定的整个紧环面不变；十七处的生成元为 $g_0=2+4\delta$，有
$$
g_0^6=\omega\quad(\bmod17),\qquad
(g^{12})(g_0^6)=1.
$$
其余有限好处的标准球不变。全局有理 $\omega$ 的 theta 不变性和原 archimedean Hermite 特征因子于是迫使非三倍权为零。结合偶性，原生成函数只有 $t^{6j}$ 项。因此在 (8) 的已付 frame 中，准确有
$$
\boxed{S(\omega z)=S(z),\qquad S(-z)=S(z).}
\tag{11}
$$

又 R288 已证明 $\operatorname{rank}E(\mathbf Q)\ge2$。由 CM 曲线 $L(E,1)\ne0\Rightarrow\operatorname{rank}E(\mathbf Q)=0$ 及 R290 的原完整范数公式，实际来源满足 $S(0)=0$。这里不是从若干小数系数猜测消失。

在 $H^0(E,\mathcal O(34O))$ 中，偶截面准确为
$\sigma^{34}\mathbf C[x]_{\le17}$。由于 $\sigma(\omega z)=\omega\sigma(z)$、$x(\omega z)=\omega x(z)$，(11) 只留下 $x^{2+3j}$，$0\le j\le5$。$j=5$ 的一列原点值为一，其他五列原点值为零。所以
$$
\boxed{
S=\sigma^{34}x^2P_4(x^3),\qquad \deg P_4\le4,
\qquad S\ne0.
}
\tag{12}
$$
原点阶至少六。$S\ne0$ 也直接由 (1) 的非零 Fourier 系数得到，而不是来自一个未证明的正秩特殊值非零。

将整个来源乘一个固定非零标量后，可使 $P_4$ 的系数位于固定数域中。一个不依赖周期近似的证明是：在 $E[34]$ 的固定 torsion 域上，用有理除子函数及有限次单位根选取原 theta 结构；二处和十七处的有限 Weil 矩阵都是代数矩阵，原两条特征线各一维。其张量线因而是一维代数线。实际解析来源已处于这条线，归一任一非零系数即得代数系数。没有预先断言 $P_4$ 有理；其具体识别另由真实 CM 迹完成。

## 4. degree $34$ 的最小性

**定理 1。** 原来源 (8) 在最大整环椭圆曲线上不能再沿任何非平凡同源下降为较低次数的截面。其最小 theta 次数为 $34$。

**证明。** 若截面从同源商下降，其核平移必保持截面的射影线，且核包含在 $E[34]$ 中。原 theta 结构分成二处二维块与十七处十七维块，来源为两条给定向量的纯张量。

先看二处。下降后的坐标可写作 $(a,b)$，原向量是 $(1,t)$。三个非零二挠点的射影作用可取
$$
Z_2(a,b)=(a,-b),\qquad X_2(a,b)=(b,ia),\qquad Z_2X_2(a,b)=(b,-ia).
\tag{13}
$$
它们直接由 (2) 沿 $1/2,s/2,(1+s)/2$ 的移位得到；省去的仅是与 $(a,b)$ 无关的非零标量。其与 $(1,t)$ 的三个行列式为
$$
-2t,\qquad i-t^2,\qquad -i-t^2,
\qquad t^2=2+\sqrt3,
\tag{14}
$$
都不为零。因此没有非零二挠平移保持原线。

十七处可不用列举向量系数。若某个非零 Weyl 平移 $W_h$ 保持 $f_{17}$ 的线，由 $f_{17}$ 是 $g_0$ 的本征向量，$W_{g_0h}$ 也保持它的线。两个 Weyl 算子的交换子为
$\zeta_{17}^{\langle h,g_0h\rangle}$。而 $g_0$ 的迹为四，特征多项式判别式为 $12$；$12^8\equiv-1\pmod {17}$，所以 $g_0$ 在 $\mathbf F_{17}$ 上没有特征线。于是 $h,g_0h$ 独立，交换子不等于一，矛盾。

对纯张量，若 $W_{h_2}\otimes W_{h_{17}}$ 保持其线，则每个因子都保持相应的线。前两段迫使 $h_2=h_{17}=0$。所以原截面的射影平移稳定群平凡，不能再下降。$\square$

这项最小性针对实际 Schwartz 截面及真实同源下降；不限制另外改换来源或用有极函数人为重写。

## 5. 三次覆盖上的完整线丛和 Heisenberg 基

继续 R288 的 $c^2=17,a^3=2c,T=(0,c)$，并令
$$
\varphi:\mathcal C\to E,\qquad \mathcal C:u^3+v^3=1,\qquad O'=(0,1),
$$
$$
u=a\sigma/\theta_-,\qquad v=\theta_+/\theta_-.
$$
这是已经证明的未分歧范数三 CM 同源。它的对偶核是 $\langle T\rangle$，所以 $\varphi^*\mathcal O(T-O)$ 平凡。三个真实 theta 截面
$$
\boxed{A=a\sigma,\qquad B=\theta_+,\qquad C=\theta_-}
\tag{15}
$$
在覆盖上因此属于同一 degree-three 线丛 $\mathcal L$，且
$$
A^3+B^3=C^3.
$$
在 $O'$ 的切线 $B-C=0$ 与三次曲线的交为 $3O'$，故 $\mathcal L\simeq\mathcal O_{\mathcal C}(3O')$。由此得到完整、真实的截面环
$$
\boxed{\bigoplus_{N\ge0}H^0(\mathcal C,\mathcal L^N)
=k[A,B,C]/(A^3+B^3-C^3).}
\tag{16}
$$
特别 $H^0(\mathcal C,\mathcal L^{34})$ 维数为 $102$，标准基可取总次数 $34$、$C$ 次数为 $0,1,2$ 的单项式。原 source 的三次拉回 degree 准确为 $102$，没有把它继续写成 base 上的 degree $34$ 而省去三次覆盖成本。

原三次 Heisenberg 群可以在 (15) 上显式实现为
$$
X(A,B,C)=(B,-C,-A),\qquad
Z(A,B,C)=(A,\omega B,\omega^2C).
\tag{17}
$$
两者都保持三次方程、三次为一，坐标矩阵满足 $XZ=\omega ZX$。它们在光滑三次曲线上没有不动点：对 $X$ 的任一特征向量，方程左边为 $3A^3$；$Z$ 的三个坐标特征点也不在曲线上。故它们是两个真实三挠平移，生成整个 $\mathcal C[3]$。

在次数 $N$ 的截面上采用直接代换的拉回，则矩阵次序相反：
$$
X^*Z^*=\omega^{-N}Z^*X^*.
\tag{18}
$$
$N=34$ 时中心特征非平凡，(16) 分成 $34$ 个三维不可约 Heisenberg 模。
规范 deck 平移为 $(u,v)\mapsto(\omega u,\omega^2v)$，正是 $Z$ 的射影作用。

基曲线上 $\theta_-^{34}$ 的平坦除子类为 $T$，与原 $S$ 的 untwisted 类不同；直到 (15) 的真实覆盖后二者才在同一线丛中比较。这一点不能从 theta 次数相等省略。

## 6. 对真实原源的等次数全纯补偿

**定理 2。** 对 (12) 的实际来源，两个三次根补偿都全纯，而且准确为
$$
\boxed{
S_+=v^2S=\sigma^{30}\theta_+^4P_4(x^3),\qquad
S_-=v^{-2}S=\sigma^{30}\theta_-^4P_4(x^3).
}
\tag{19}
$$
它们在基曲线上分别具有 $-T$、$T$ 的平坦 twist，拉回后与 $S$ 属于同一个 (16) 中的 degree-$34$ 齐次块。

**证明。** R288 的原恒等式 $\theta_+\theta_-=x\sigma^2$ 给
$x^2\sigma^4=(\theta_+\theta_-)^2$，直接相乘便得 (19)。等价地，原 $S$ 在 $T,-T$ 各至少消失二阶，恰好支付 $v^{\pm2}$ 的全部极。这里使用的是实际来源的因子 $x^2$，不是用一个任意 $\theta_-^{34}$ 代替来源。$\square$

具体地，(12) 的五个基单项式在 (15) 中是非零标量倍的
$$
A^{30-6j}B^{3j+2}C^{3j+2}\qquad(0\le j\le4).
$$
两个补偿的单项式则是
$$
A^{30-6j}B^{3j+4}C^{3j},\qquad
A^{30-6j}B^{3j}C^{3j+4}.
\tag{20}
$$
所以三者分别位于 $Z^*$ 特征 $1,\omega,\omega^2$ 的三个五维空间，直和维数为十五。全体 (16) 是保持实际 Heisenberg 作用的固定有限模；这十五维空间只用于本次根补偿，不被无证宣称对所有乘法封闭。

真实 $\mu_3$ 和负号分别为
$$
R(A,B,C)=(\omega A,B,C),\qquad
\iota(A,B,C)=(-A,C,B).
\tag{21}
$$
因此 $S,S_+,S_-$ 均 $R$ 不变，$\iota$ 固定 $S$ 并交换 $S_+,S_-$。需要原偶分支时，应取相应的真正偶组合，不能把两条不同 deck 特征直接认作同一原零行。

还有一个精确的角色区别：$X^*S$、$(X^*)^2S$ 在 $R$ 下都取特征 $\omega^2$，而 $S_+,S_-$ 在 $R$ 下取一。因此它们不属于原 $S$ 的三维 Heisenberg 轨道。根补偿确实给同一有限全纯截面模中的来源，但没有保持原十七处来源的同一条线。

## 7. 完整 Frobenius 因子恢复原角色，并带有实际极成本

R288 的惰性素数写作 $p=3r-1$。其实际多项式 $D$ 满足
$$
D=\frac{a_0}{3}(1-q)^{r-1}\quad(\bmod p),\qquad q=u^3.
$$
在全局特征 $p$ 函数域中，准确有
$$
\boxed{D^{-1}S=\frac3{a_0}v^{2-p}S
=\frac3{a_0}\frac{S_+}{v^p}.}
\tag{22}
$$
只有在已付的原点窗口 $q^p$ 以下，$v^p=v(q^p)\equiv1$，(22) 才返回 (19) 的固定全纯补偿。全局的 $v^p$ 还恰好恢复原 deck 特征：$2-p$ 被三整除，所以 $v^{2-p}S$ 与 $S$ 具有同一特征；单独的 $S_+$ 则没有。

令 $j_0$ 为 $P_4(X)$ 的最小非零次数，$0\le j_0\le4$。在每个位于 $-T$ 上的点，$x$ 为一阶参数、$v$ 一阶零，故 (22) 的准确极阶在正时为
$$
\boxed{p-4-3j_0.}
\tag{23}
$$
特别 $p>17$ 时必有真实极。这不是三次覆盖额外引入的分歧，而是不能删除的实际 Frobenius 分母。后续完整中央比较必须一起转置它；本篇的固定全纯十五维比较只支付其明确的有限窗口部分。

## 8. 证书

- [check-jzero-actual-theta-degree-and-cubic-source-module.py](../scripts/check-jzero-actual-theta-degree-and-cubic-source-module.py)
- [check-jzero-actual-theta-degree-and-cubic-source-module.json](../scripts/check-jzero-actual-theta-degree-and-cubic-source-module.json)

脚本核对原半周期身份、最大整环格、完整 Hermite/sigma Gaussian、三个二挠非本征子式、十七处 nonsplit 判别式及 $\omega$ 的实际角色、三次 Heisenberg 的精确矩阵、(20) 的十五维独立性和所有次数/角色。没有目标素数实验，也没有由这些 finite source 身份新增一条未经支付的中央零。
