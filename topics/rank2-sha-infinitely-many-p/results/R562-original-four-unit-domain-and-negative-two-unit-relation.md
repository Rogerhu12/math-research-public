# R562 — 原六度双输出四单位域与负二矩的整单位关系

日期：2026-11-14。**状态：已证明。**

在 R533 的同一个原 sigma / odd degree3 双输入中，保留输入及和差两个输出同时为单位的真实域。本篇证明：原 $f_4$ 的负二单位矩与一个明确的混合四单位积分不能同时落入 $p\mathcal O$。特别，如果负二矩为零，则这个实际四单位积分是单位。两个被删去的深度补集均逐项计算；其中三度输入深的非零首项完整保留。

这还没有把该混合积分识别成原 $S/T$ 的已知中央零。因此既不证明负二矩本身非零，也不完成固定曲线无穷素数目标。

## 1. 同一来源、完整核心与物理坐标

沿用 [R529](R529-original-low-j-k-core-and-complete-st-carry.md)、
[R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md) 的原普通射线和周期：
$$
b=17,\qquad \omega^2+\omega+1=0,\qquad \delta=1+2\omega,\quad
a=2+\omega=-\omega\delta,
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda=\bar\pi_0^{-1},\qquad
\kappa=p\lambda^2,\qquad \Omega=\Omega_p\in\mathcal O^\times.
\tag{1}
$$
所有已有有限坏集和射线细分保留，不加新的同余条件。$\mathcal O$ 为原系数整数环；下述物理输入、单位及 $p$ 倍子群均取原普通测度的实际紧致输入格。固定 CM 单位给该格的自同构。

为避免与物理输出 $H$ 混淆，记
$$
B=-y_\wp\sigma^3,\qquad P=\sigma^3,\qquad
\mathcal H=(x_\wp^3-2b)\sigma^6,
$$
$$
f_1=-x_\wp y_\wp\sigma^6,\quad
f_3=-y_\wp\sigma^6,\quad
f_4=x_\wp\sigma^6.
\tag{2}
$$
这里 $B$ 是 R522/R533 的 $B_3$，也就是 R559 的质量一 $B_0$；
$P$ 是 R533 的 $P_3$。这些名字不改变来源。

整测度 $\nu_F$ 仍满足
$$
\int z^j\,d\nu_F(z)=\Omega^jF^{(j)}(0).
\tag{3}
$$
R529 §2 的整个 odd degree3 核和整个 even degree6 核，以及原 sigma 核，准确给
$$
\boxed{\quad
\nu_F|_{p\mathcal O}=\beta[\kappa]_*\nu_F
\quad}
\tag{4}
$$
对 $F=\sigma,B,\mathcal H,f_1,f_3,f_4$ 全部成立。
这里是原物理规范 (1)，不是把 R540 的基曲线 Hecke 生成元直接换进来。
R533 §3 已完整支付 degree6 的中心、半特征与绝对锚；不从单个 $\mu_6$ 型猜 (4)。

取真正独立输入
$$
\mu_B=\nu_\sigma(c)\otimes\nu_B(v),\qquad
\boxed{\ H=\delta c-v,\quad K=\delta c+v,\quad
c=\frac{H+K}{2\delta},\quad v=\frac{K-H}{2}.\ }
\tag{5}
$$
矩阵行列式为 $2\delta$，是当前处单位。两个输出的完整极化均为 $6$，交叉项 $N(\delta)-3=0$；这是 R533 两输出的固定单位旋转及反射，保整个实际联合。

其生成函数是
$$
G_B(h,k)=\sigma(\delta(h+k))B(k-h).
\tag{6}
$$
若 R559 中写 $H=\delta(c-\zeta C),K=\delta(c+\zeta C)$，
则 (5) 的三度输入是 $v=\delta\zeta C$；不能在已经采用 $v$ 后再把 $\delta$ 重复乘入。

设 $m_F(j)=\int z^j\,d\nu_F$，$m_F^\times(j)=\int_{z\ {\rm unit}}z^j\,d\nu_F$。
后一式对任意整数 $j$ 都是有界整积分。原展开给
$$
B(0)=\mathcal H(0)=1,\quad
m_\sigma(1)=m_{f_1}(1)=\Omega,\quad
m_{f_3}(3)=6\Omega^3,
$$
$$
m_\sigma(7)=24b\Omega^7,\qquad m_B(6)=216b\Omega^6.
\tag{7}
$$
$\sigma$ 的非零矩仅可能在 $1\bmod6$，$B$ 的仅可能在 $0\bmod6$。
由 (4)，记
$$
A_0=1-\beta,\qquad
A_1=\Omega(1-\beta\kappa),\qquad
A_3=6\Omega^3(1-\beta\kappa^3),
$$
$$
I_4=m_{f_4}^\times(-2).
\tag{8}
$$
$I_4$ 始终是 R533 的负二矩，不是正四矩。

## 2. 完整双输出与双单位积分

R533 的全函数公式，利用 $\delta=-\omega^2a$ 及
$\sigma(\zeta z)=\zeta\sigma(z)$，给
$$
G_B(h,k)=-\omega^2F_B(-h,k)
$$
$$
=\delta\{\mathcal H(h)f_1(k)+f_1(h)\mathcal H(k)
-6b[f_3(h)f_4(k)+f_4(h)f_3(k)]\}.
\tag{9}
$$
这同时是完整测度恒等式；不是只对某条边际或低阶 jet 的识别。

令
$$
\mathscr D=\{H,K\ {\rm unit}\},\qquad
J_{\mathscr D}=\int_{\mathscr D}\frac{c^3}{H^2}\,d\mu_B.
$$
在该域上
$$
\frac{c^3}{H^2}
=\frac1{8\delta^3}
\left(H+3K+3H^{-1}K^2+H^{-2}K^3\right).
\tag{10}
$$
由 (9) 的完整 $\mu_6$ 型，四项对应积分依次为
$$
\delta A_1A_0,\qquad
3\delta A_0A_1,\qquad
0,\qquad
-6b\delta I_4A_3.
$$
第三项为零使用的是第一轴没有型 $5$、相应第二轴没有所需型，
并非把负幂从积分中删掉。因此
$$
\boxed{
J_{\mathscr D}
=\frac{\Omega(1-\beta\kappa)(1-\beta)}{2\delta^2}
-\frac{9b\Omega^3(1-\beta\kappa^3)}{2\delta^2}I_4.
}
\tag{11}
$$

## 3. 两个真实补集的全部级数

目标域同时保四个单位条件：
$$
\boxed{\ \mathscr B=\{c,v,H,K\ {\rm unit}\},\qquad
J_{\mathscr B}=\int_{\mathscr B}\frac{c^3}{H^2}\,d\mu_B.\ }
\tag{12}
$$
在 $\mathscr D$ 上，若 $c$ 非单位则 $v$ 必为单位，反之亦然；
两者同时非单位不可能。因此真正不交分解为
$$
\mathscr D=\mathscr B\ \sqcup\
\{c\in p\mathcal O,\ v\ {\rm unit}\}\ \sqcup\
\{c\ {\rm unit},\ v\in p\mathcal O\}.
\tag{13}
$$
右边后两域已自动满足 $H,K$ 单位，故没有遗漏额外输出限制。

### 3.1 sigma 输入深

在第一个补集，$|\delta c/v|\le |p|$，均匀收敛展开
$$
\frac{c^3}{H^2}
=\frac{c^3}{v^2}\left(1-\frac{\delta c}{v}\right)^{-2}
=\sum_{j\ge0}(j+1)\delta^j c^{j+3}v^{-j-2}.
$$
整测度允许逐项积分。用 (4) 及 sigma 的全 $\mu_6$ 型，精确得到
$$
\boxed{
C_\sigma=
\beta\sum_{r\ge0}(6r+5)\delta^{6r+4}
\kappa^{6r+7}\,
m_\sigma(6r+7)\,m_B^\times(-6r-6)
\ \in\ \kappa^7\mathcal O.
}
\tag{14}
$$
第一项是
$120b\beta\delta^4\kappa^7\Omega^7m_B^\times(-6)$。
负阶 $B$ 单位矩完整保留。

### 3.2 三度输入深

在第二个补集，$|v/(\delta c)|\le|p|$，同样
$$
\frac{c^3}{H^2}
=\sum_{j\ge0}(j+1)\delta^{-j-2}c^{1-j}v^j.
$$
$B$ 的全型给精确式
$$
\boxed{
C_B=\frac{\beta\Omega(1-\beta\kappa)}{\delta^2}
+\beta\sum_{r\ge1}(6r+1)\delta^{-6r-2}\kappa^{6r}
m_B(6r)\,m_\sigma^\times(1-6r).
}
\tag{15}
$$
记第二项为 $T_B\in\kappa^6\mathcal O$。特别
$$
T_B=1512b\beta\delta^{-8}\kappa^6\Omega^6
m_\sigma^\times(-5)+\kappa^{12}\mathcal O.
\tag{16}
$$
这里的首项必须是
$\beta\Omega(1-\beta\kappa)/\delta^2$。
若在保留 $O(p^6)$ 的同时把它替换成 $\beta\Omega/\delta^2$，
就会漏掉一个真实的一阶项。

(14)–(16) 的整性来自原有界整测度、单位域负幂有界和 $\kappa$ 的正赋值。
没有使用无限深度的负矩求和，也没有假设负矩非零。

## 4. 整单位关系

由 (11)、(13)–(15) 严格得到
$$
\boxed{
J_{\mathscr B}
=\frac{\Omega(1-\beta\kappa)(1-3\beta)}{2\delta^2}
-\frac{9b\Omega^3(1-\beta\kappa^3)}{2\delta^2}I_4
-C_\sigma-T_B.
}
\tag{17}
$$
因此
$$
\boxed{
J_{\mathscr B}
+\frac{9b\Omega^3(1-\beta\kappa^3)}{2\delta^2}I_4
\equiv
\frac{\Omega(1-\beta\kappa)(1-3\beta)}{2\delta^2}
\pmod{\kappa^6\mathcal O}.
}
\tag{18}
$$
可更细保留 (16) 的原 sigma 负五矩：
$$
J_{\mathscr B}
=\frac{\Omega(1-\beta\kappa)(1-3\beta)}{2\delta^2}
-\frac{9b\Omega^3(1-\beta\kappa^3)}{2\delta^2}I_4
-1512b\beta\delta^{-8}\kappa^6\Omega^6m_\sigma^\times(-5)
+\kappa^7\mathcal O.
\tag{19}
$$

右边 (18) 的显示常数是单位。只需核 $1-3\beta$：
若它模 $p$ 为零，则 $\bar\pi_0\equiv3\bmod\mathfrak p$，
从而整数迹 $t=\pi_0+\bar\pi_0$ 满足 $t\equiv3\bmod p$。
由 $|t|\le2\sqrt p$ 和 $p>19$，
$$
|t-3|\le2\sqrt p+3<p,
$$
故 $t=3$。而当前固定射线 $\pi_0\equiv1\bmod2$ 给偶数迹，
矛盾。其余因子由 $p>19$、$b=17$、$\Omega,\delta,\beta$ 为单位及
$\kappa\in p\mathcal O^\times$ 直接为单位。

于是有以下无条件的实际两个积分判据：
$$
\boxed{\ (I_4,J_{\mathscr B})=\mathcal O.\ }
\tag{20}
$$
更准确地，(18) 的左边本身为单位。特别
$$
I_4\in p\mathcal O\ \Longrightarrow\ J_{\mathscr B}\in\mathcal O^\times,
\qquad
J_{\mathscr B}\in p\mathcal O\ \Longrightarrow\ I_4\in\mathcal O^\times.
\tag{21}
$$
其中第一条包含 $I_4=0$ 的情形。这里 $p\mathcal O=\kappa\mathcal O$，
(18) 的误差已经是六阶，不只是模 $p$ 的形式猜测。

## 5. 同一域上的反对称测试及另一真实核

域 $\mathscr B$ 在 $v\mapsto-v$ 下不变，此变换交换 $H,K$，
而 $B$ 为偶函数，所以可以把同一积分写成
$$
\boxed{
J_{\mathscr B}
=\int_{\mathscr B}
\frac{c^3}{2}\left(H^{-2}+K^{-2}\right)d\mu_B.
}
\tag{22}
$$
此测试在原独立 sigma 反射 $c\mapsto-c$ 下变号；
该反射把 $(H,K)$ 送至 $(-K,-H)$。
所以 (22) 保留了原输入反射及其实际两个单位输出，没有仅作边际比较。

对另一原完整核
$$
G_P(h,k)=\sigma(\delta(h+k))P(k-h)
=-\omega^2F_P(-h,k)
$$
及其同一物理域，(22) 的积分严格为零：
$G_P$ 总 $\mu_6$ 型为 $4$，测试的总次数为 $1$，
而四单位域在同时乘 $\mu_6$ 下不变。这个型消去只施于完整两输入；
不能在另加未同时运输的混合 $Y/W$ 条件后照抄。

因此若某个已付完整联合确为
$G_B\otimes\Lambda_B+G_P\otimes\Lambda_P$，
则 (22) 乘任意仅依赖其余伴随的连续测试 $g$，准确返回
$J_{\mathscr B}\Lambda_B(g)$。
$\Lambda_B,\Lambda_P$ 不必相等；本篇没有把实际依赖 $H,K$ 的
旧中央测试当作这样的独立 $g$。

## 6. 适用范围与下一真实接口

(17) 是同一原来源、同一普通地点和同一四单位域上的非齐次关系。
它没有使用复功能方程、反射到另一普通地点、有限个素数扫描，
或 R540 的正四特殊值替代负二矩。

要由 (21) 推出负二矩非零，仍须从原 $S/T$ 条件中央支付
$J_{\mathscr B}\in p\mathcal O$，或支付其他实际补域关系。
目前没有这样赋零。R559/R560 中的原 $Y/W$、独立深度和移动测试
均需继续保留；这里只为其中真实 $G_B$ 核提供可直接代入的完整单位域计算。
本篇也不由 (20) 宣称 $I_4$ 与原负五矩 $I_1$ 不同时零。

随附证书
[check-r562-four-unit-negative-moment-relation.mjs](../scripts/check-r562-four-unit-negative-moment-relation.mjs)
核对完整外积的型消去、所有常数、精确补集尾阶、(17) 的多项式关系与
迹界所用因式。全域分解、完整核心和均匀收敛的证明均在正文，不以有限测试替代。
