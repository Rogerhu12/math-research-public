# R147：有证辅助延拓与实际 coast 的短弦正常球

2026-11-12，fd2d geometry，接 R145。**完整证明及带区间误差的实际计算均已完成。**

本文在 R145 的同一个有限 Cartesian 位置公式上作数学辅助延拓，原物理片及其输入均不改变。该延拓解决“短测地线可能离开带边 patch”的缺口，进而证明一批明确点对的实际正常球不等式。它不把未覆盖的远点对、其它曲面片或新的非零 $\delta$ 目标场计入。

## 1. 已证输入与准确结论

R145 原片用 $(\sigma,u)\in[0,L]\times\mathbb R/(2\pi\mathbb Z)$ 表示。目标度量为
$$
g_0=d\sigma^2+(a+v\sigma)^2du^2,
\quad \rho_c=a/v,
$$
实际位置仍是 R137 的
$$
F(\phi,w)=X(\phi)+w\left(e_1(\phi)-\frac{m(\phi)}{n(\phi)}e_2(\phi)\right).
\tag{1}
$$
完整 Fourier 字节、材料图册和 $a,v,L$ 的定义与 R145 相同。设
$$
\varepsilon=10^{-6},\qquad K=73/10,\qquad \rho=17/125.
\tag{2}
$$
本次严格计算将同一公式 (1) 延拓到
$$
-\eta\le\sigma\le L+\eta,\qquad \eta=1/1000,
\tag{3}
$$
并在该完整域上证明
$$
(1-\varepsilon)g_0\le g_F\le(1+\varepsilon)g_0,
\qquad \max_i|\kappa_i(F)|<K,
\tag{4}
$$
以及处处浸入、坐标单值和
$$
\rho_c>39/10,\qquad 1/4<v<3/10.
\tag{5}
$$
证明和实际计算身份见第2节。它不要求辅助延拓在原片外等于将来实际闭核的其它部分；它仅为原片端点之间提供比较曲线。

对原片的两个材料点 $p=(\sigma_p,u_p)$、$q=(\sigma_q,u_q)$，令
$\Delta u\in[-\pi,\pi]$ 是最短材料角差，$r_p=\rho_c+\sigma_p$、$r_q=\rho_c+\sigma_q$。定义发展平面的短弦长 d：
$$
\boxed{d^2=(r_q-r_p)^2+4r_pr_q\sin^2(v\Delta u/2).}
\tag{6}
$$
这是真实材料坐标的量，不能将入口法向角 $\phi$ 直接代入 u。

**结论。** 若 $d\le1/10$，则对两个实际空间点 $P=F(p)$、$Q=F(q)$、任一端的实际单位法向和两种正常球符号，都有
$$
\boxed{|Q-P|^2-2\sigma\rho N_P\cdot(Q-P)
\ge\frac{d^2}{160},\qquad \sigma\in\{-1,1\}.}
\tag{7}
$$
把 P、Q 交换后相同结论成立。因此所有满足 (6) 的这批原片点对已经支付半径 .136 的两向正常球。若 $d>0$，(7) 还说明这两个参数点的实际像不同。

本文不声称 $d>1/10$ 的点对已通过。既有全径向凸二次 screen 仍只是这些剩余点对的有限角证据，不能与 (7) 混写成完整同片 reach。

## 2. 同一公式的有证辅助延拓

在 $\sigma\in[-\eta,L+\eta]$ 上定义
$$
Q_\sigma=\sqrt{\rho_c^2+(1+k^2)\sigma(2\rho_c+\sigma)},
\quad
w_\sigma=\frac{\sigma(2\rho_c+\sigma)}{\rho_c+Q_\sigma},
\qquad k=m/n.
\tag{8}
$$
取与 $w_0=0$ 连通的这一支。实际区间计算证明全角 $Q_\sigma>0$ 及两端 D 正，其中
$$
D=a+w\left(v(1+k^2)-k_\phi/h\right),\qquad h=U_0'(\phi)>0.
$$
由于 D 关于 w 仿射，端点下界给出全部 $w\in[w_{-\eta},w_{L+\eta}]$ 的正性。
又 $w_{-\eta}>-2\eta$，故 $\rho_c+w>0$。R137 的变换公式继续给
$$
u=t-\frac1v\arctan\frac{wk}{\rho_c+w},\quad
\frac{\partial u}{\partial t}\bigg|_\sigma=\frac D{vQ_\sigma}>0,
\quad t=U_0(\phi).
$$
它的全圈增量是 $2\pi$，所以每个 $\sigma$ 上均为圆周微分同胚；不存在把错误逆分支当成延拓的步骤。

实际 Cartesian 曲率仍由 R145 的真实 I、II 和二次多项式公式计算；没有用形式可展曲率替代它。对 metric，R145 的全角 Laurent 卷积缺陷 $H,C,B,M^TC,M^TB$ 与 w 无关，可以原样复用；只将其公式中的 $L/n_*$ 替换为
$\max(|w_{-\eta}|,|w_{L+\eta}|)/n_*$，并对新两端 D 重新给下界。因而延拓后的 (4) 仍是这个实际 F 的界。

实际执行：session29554 / 最终 chunk `989918` / 自然 exit0，72.169570554秒。
Arb160 位，520个角盒覆盖完整圆周，每个角盒16个完整径向条带，共8320盒，无未决。原 Cartesian 有限 Fourier 的全部剩余模及材料 h 的无限尾均按 R145 支付。

| 已完成的连续量 | 本次实际界的范围 |
|---|---:|
| 诱导度量相对目标的误差 | 小于 $10^{-6}$；实际盒上界约 $8.70421\times10^{-9}$ |
| 实际主曲率绝对值 | 小于 $73/10$；最大盒上界约7.28620 |
| 实际面积 | 所有盒严格正 |
| D | 全域严格正，最小盒下界约 .210942 |
| n | 全角严格正，最小盒下界约 .207514 |

短小数只供阅读，严格数值在保存的二进制端点字段中。

源码 `scripts/fd2d_k0_ruling_extension_certificate.py`，SHA256
`4cd50b777db34eaa817456bc8d0c95c7a46f046dbacfb1aba49d26baedc49232`。
报告 `notes/2026-11-12-fd2d-k0-ruling-extension-certificate-01.json.gz`，SHA256
`25e6664304ea2c5a528252ba5ad62d0b899fb254f616d1f2353597f3259facc5`，316204B。
报告同时绑定 R145 的真实卷积残差包及所有实际 helper 源。没有重新求解 BVP，也没有更换原片的 g。

## 3. 把近欧氏度量写到一个单值平面域

将 $u_p$ 的升起选为0。目标度量的平面发展是
$$
Y(\sigma,u)=(\rho_c+\sigma)(\cos(vu),\sin(vu)).
\tag{9}
$$
在辅助区域
$$
\mathcal A=\{ -\eta\le\sigma\le L+\eta,\ |u|\le1/2\}
\tag{10}
$$
中，角宽为 $v<.3<\pi$，所以 (9) 单值且一一对应于一个闭环扇形。$g_0$ 在 Y 坐标中准确为 Euclidean 度量，(4) 即
$$
(1-\varepsilon)|dY|^2\le g_F\le(1+\varepsilon)|dY|^2.
\tag{11}
$$

先证明 q 也位于 (10) 的角向内部。若最短角差满足 $|\Delta u|\ge1/2$，则
$|v\Delta u|/2\in[v/4,v\pi/2]\subset(1/16,\pi/2)$。由 (6)，
$$
d\ge2\rho_c\sin(|v\Delta u|/2)
>2\frac{39}{10}\frac3{50}=\frac{117}{250}>\frac1{10},
$$
矛盾。这里 $\sin(1/16)>3/50$ 由 $\sin x\ge x-x^3/6$ 得到。因此 $|\Delta u|<1/2$。

把两个平面端点仍记为 $Y_p,Y_q$。它们的连接线段在扇形角锥中，因为角锥宽度小于 $\pi$ 而凸。对线段上任意点 $Y_t=(1-t)Y_p+tY_q$，
$$
|Y_t|^2=(1-t)r_p^2+tr_q^2-t(1-t)d^2
\ge\rho_c^2-d^2/4.
$$
利用 $\sqrt{R^2-x}\ge R-x/R$，得到
$$
|Y_t|\ge\rho_c-\frac{d^2}{4\rho_c}
>\rho_c-\frac1{1560}>\rho_c-\eta.
\tag{12}
$$
另一方面，范数凸性给 $|Y_t|\le\rho_c+L$。所以整条平面线段在辅助区域内，由 (11)，其实际长度不超过
$$
\sqrt{1+\varepsilon}\,d.
\tag{13}
$$

## 4. 最短曲线不能碰辅助边界

在紧区域 (10) 上取 p、q 的实际度量最短曲线。存在性可由直接法得到：对有统一长度界的极小序列按弧长重新参数化，(11) 给统一 Euclidean Lipschitz 界；取一致收敛子列，长度下半连续性给极小曲线。

设其长度为 $\ell$。由 (13) 及 (11)，
$$
\sqrt{1-\varepsilon}\,d\le\ell\le\sqrt{1+\varepsilon}\,d.
\tag{14}
$$
对这条曲线上任何 Y，把曲线从 Y 分成两段并用 (11)，得
$$
|Y-Y_p|+|Y-Y_q|\le\frac{\ell}{\sqrt{1-\varepsilon}}
\le R d,
\quad R=\sqrt{\frac{1+\varepsilon}{1-\varepsilon}}.
\tag{15}
$$
所以整条最短曲线落在以 $Y_p,Y_q$ 为焦点、长轴长 Rd 的椭圆内。其半短轴 b 满足
$$
b=\frac d2\sqrt{R^2-1},\qquad
b^2\le\frac1{199999800}<\frac1{14000^2}.
\tag{16}
$$
这个椭圆的每一点到焦点连接线段的距离不超过 b：在焦点轴中写标准椭圆方程即可验证；轴向越过焦点的部分到最近焦点的距离也不超过 b。

于是 (12) 加 (16) 给曲线上的全部点
$$
|Y|>\rho_c-\frac1{1560}-\frac1{14000}>\rho_c-\eta,
\qquad
|Y|<\rho_c+L+\frac1{14000}<\rho_c+L+\eta.
\tag{17}
$$
径向两条辅助边界均碰不到。

角向边界也碰不到。由 (15)，曲线上各点到 $Y_p$ 的距离小于 $Rd<101/1000$。而点 $Y_p$ 到角度 $\pm v/2$ 的任一边界射线的距离至少
$$
r_p\sin(v/2)>\frac{39}{10}\sin(1/8)
>\frac{39}{10}\frac3{25}=\frac{117}{250}>\frac{101}{1000}.
$$
因此最短曲线除端点外完全位于 (10) 内部，端点本身也在内部。它遂是一条真正的光滑曲面测地线，不是沿 patch 边界行走的受限最短路。

这一步使用的是已认证的辅助 F，不要求曲线始终留在原片 $0\le\sigma\le L$。由于辅助公式与原片的 F 完全相同，端点位置和实际法向均不变，故它可以用于这两个原片端点的 Euclidean 正常球比较。

## 5. 空间测地线的正常球比较

按实际弧长参数化这条测地线为 $\gamma:[0,\ell]\to\mathbb R^3$，单位切向为 T。曲面测地线的空间加速度只有法向分量，由 (4)，
$$
|T'(s)|\le K.
$$
又由 (14)，
$$
\ell\le\sqrt{1+10^{-6}}/10<101/1000<\frac{15}{73}<\frac\pi{2K}.
\tag{18}
$$
最后用 $\pi>3$ 即可。

T 在单位球面上的弧长控制其夹角，因此
$$
T(s)\cdot T(t)\ge\cos(K|s-t|).
$$
对正方形 $[0,\ell]^2$ 积分得到
$$
|Q-P|^2=\int_0^\ell\int_0^\ell T(s)\cdot T(t)\,dsdt
\ge\frac{4\sin^2(K\ell/2)}{K^2}.
\tag{19}
$$
同时 $T(0)\perp N_P$，$Ks\le\pi/2$，故
$|T(s)\cdot N_P|\le\sin(Ks)$。积分给
$$
|N_P\cdot(Q-P)|\le\frac{1-\cos(K\ell)}K
\le\frac K2|Q-P|^2.
\tag{20}
$$
因此两种法向符号均有
$$
|Q-P|^2-2\sigma\rho N_P\cdot(Q-P)
\ge(1-\rho K)|Q-P|^2
=\frac9{1250}|Q-P|^2.
\tag{21}
$$
反向参数化同一测地线即得到以 $N_Q$ 为中心法向的版本。

## 6. 定量余量及参数点的区别

由 (14)、(19) 和正弦在相应范围的单调性，
$$
|Q-P|^2\ge\frac4{K^2}
\sin^2\left(\frac K2\sqrt{1-\varepsilon}\,d\right).
$$
括号内的数不超过 $73/200<37/100$。在这个范围，
$\sin x\ge x-x^3/6\ge(19/20)x$。所以
$$
|Q-P|^2\ge\frac{361}{400}(1-\varepsilon)d^2.
$$
结合 (21)，
$$
\Phi_\sigma(P,Q)\ge
\frac9{1250}\frac{361}{400}\frac{999999}{1000000}d^2
>\frac1{160}d^2,
$$
即 (7)。当 $d=0$ 时同样以等号成立。

最短材料角升起在本近区唯一，平面图 (9) 单值，因此 $d=0$ 只对应相同的原片材料点。对于不同的这批材料点，$d>0$，(7) 的正下界排除实际像重合。这里没有以一个非严格正常球不等式自动排除任意多重覆盖。

## 7. 可直接消费的接口和范围

`scripts/fd2d_k0_short_pair_normal_balls.py` 提供：

- `developed_distance_squared(a,v,sigma_p,u_p,sigma_q,u_q)`：按 (6) 计算最短材料角升起的浮点值；这只是分类 screen。
- `conditional_normal_ball_bound(d2_lower,d2_upper)`：对调用者已经认证的准确有理区间，若 $0\le d2_{low}\le d2_{up}\le1/100$，返回两向正常球平方余量下界 $d2_{low}/160$；不替调用者认证输入区间，也不把该定理转给别的 g。
- `rational_constants()`：用 `Fraction` 准确验证 (16)–(18) 和最终系数所需的全部有理比较。

入口必须使用真实材料 u；R137/R139 的全圈坐标逆或 R141 的明确 U 图册都可提供它。若使用有限浮点评值，必须把求值误差并入 d² 区间后才能引用 (7)。

最小 consumer 实际 session59621 / 最终 chunk `4d4948` / 自然 exit0，内部0.391245541秒。它核验有理常数、包含与不包含阈值的条件接口，以及材料角周期移位的有限例子；有限例子并不承担连续几何证书。
源码 SHA256 `66148cbcb9527608aea1b0a57b5d35205d5219e40a38bc32f4fc05fbf60a9733`。
报告 `notes/2026-11-12-fd2d-k0-short-pair-normal-balls-01.json`，SHA256
`317edc7ccf01e5c4466444fd4dd6719e9a65a1d789ef69b66997364f74351c45`。

**剩余范围明确不变：** 原片 $d>1/10$ 的同片点对、与其它上片的跨片正常球、未知前缀/尾的完整两 jet 接合、非零 $\delta$ 设计场的实际重建与共同 g 加密都未由本结果完成。已经证明的镜像分离可以另行合并，不能因其中一块完成而收尾整个强目标。
