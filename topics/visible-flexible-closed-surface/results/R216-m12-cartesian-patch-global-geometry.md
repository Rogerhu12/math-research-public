# R216：真实 Cartesian 上行补丁的全域几何传递

2026-11-26，Astra-visible-flex-6a65e705-20261126 / g5-and-exact。

**状态：下列有限候选的几何及保守度量界已证明；有理预算实际 exit 0。
未声称完整度量误差下降或固定 g 的趋零收敛。**
对象是 R21 的原 M12 图加上冻结的真实位置补丁，
不是 R114 的同像材料修复图。

## 1. 唯一对象与结论

记 $X_\alpha$ 为 [R21](R21-m12-whole-map-and-actual-metric-decrease.md)
的唯一 common-cut M12 闭族，目标仍为其原固定 $g$。
R21 已给实际闭图的 C² 接合、全时材料相位、正支撑、曲率及度量证书。
[R25](R25-m12-sharper-enclosing-ball.md) 给同一图的包围球

$$
R_P=\frac{2131902881202937}{1125899906842624}<1.9.
$$

采用 [冻结参数文件](../notes/2026-11-26-6a65-m12-up-patch-parameters.json)，
SHA256 为
1e0659207c6d0e70f709f25e835aa2e76c99048c63168c4e77e5a06e4f1e1ae7。
其 24 个 binary64 十六进制值按精确二进制有理数解释，
前 12 个为径向、后 12 个为竖直，频数均为 $k=3,6,\ldots,36$。

原参数 $\delta,v_u,\varepsilon$ 使用 metadata 的精确二进制值；
$\varepsilon=\mathrm{ramp}=0.4$，不是 ramp_eta。
置 $T_u=\delta/[v_u(1-\varepsilon)]$，

$$
a=T_u[\varepsilon+(1-2\varepsilon)/20],\quad
b=T_u[\varepsilon+19(1-2\varepsilon)/20],\quad L=b-a.
$$

显示 $a\approx.2916001781596422,\ b\approx.4196197685711923$。
令 $\tau=(s-a)/L$，在 $[a,b]$ 取
$\chi=\tau^3(1-\tau)^3$，其它处取零。定义

$$
W(s,u)=\chi(s)\sum_{k=3,6,\ldots,36}
\cos(ku)[c_{r,k}e_r(u)+c_{z,k}e_z].                \tag{1}
$$

下半图按 R21 的完整镜像延拓。活动相位取
$\widehat X_\alpha=R_\alpha(X_0+W)\circ\tau_{-\alpha}$，两完整帽固定。
记 $D'=\operatorname{diam}\widehat X_0(S^2)$。

**结论。** 该族为 C² 拓扑连续的连通闭 C² 嵌入族，同一固定帽集合 $H$ 有内点，且

$$
\sup_{\alpha,p}\|g^{-1/2}(\widehat X_\alpha^*e-g)g^{-1/2}\|_{\rm op}
<4.4\cdot10^{-8}<10^{-6},                         \tag{2}
$$
$$
\frac{\operatorname{reach}(\widehat X_\alpha(S^2))}{D'}>.0312,\quad
\frac{\delta_{\rm hold}}{D'}>.05278,\quad
\frac{\operatorname{diam}\widehat X_0(H)}{D'}>.93. \tag{3}
$$

含反射的 $\delta_E>0$。这些仍是基本尺度的有限候选结论，
没有支付更强 held 20%、$\delta_E$ 5% 或 README 第 5 条。

本文直接复用 R10 的全局管定理和 R16 的非全等不变量，
逐一验证它们对改变后的实际图所需的假设。

## 2. C² 支撑与有理位移预算

$\chi,\chi',\chi''$ 在 $a,b$ 均为零，所以 (1) 延零为 C²。
支撑严格在上行恒速段内部，并在 common-cut correction_start_index 2303 以前；
它不碰中央镜像、共同 cut、尾、圆领或固定帽。
使用的是直接 Cartesian 基，没有假设原 C² 图的法向也为 C²。
镜像与相位规则保持全部接缝的两 jets。

令

$$
S_0=\sum_k(|c_{r,k}|+|c_{z,k}|),\quad
S_1=\sum_k[(k+1)|c_{r,k}|+k|c_{z,k}|],
$$
$$
S_2=\sum_k[(k+1)^2|c_{r,k}|+k^2|c_{z,k}|].
$$

由 $\chi\le1/64,\ |\chi'|\le3/(16L)$ 及
$\chi''=6\tau(1-\tau)(1-5\tau+5\tau^2)/L^2$，有

$$
|W|\le S_0/64,\quad |W_s|\le3S_0/(16L),\quad |W_u|\le S_1/64,
$$
$$
|W_{ss}|\le3S_0/(2L^2),\quad |W_{su}|\le3S_1/(16L),\quad
|W_{uu}|\le S_2/64.                              \tag{4}
$$

角基的 $e_r,e_\theta$ 导数一起计入，故径向项用 $k+1$，不能仅用 $k$。
对准确冻结系数的 Fraction 比较给：

| 量 | 严格上界 |
|---|---:|
| $|W|$ | $4.1\cdot10^{-11}$ |
| $|W_s|$ | $3.84\cdot10^{-9}$ |
| $|W_u|$ | $1.2\cdot10^{-9}$ |
| $|W_{ss}|$ | $2.4\cdot10^{-7}$ |
| $|W_{su}|$ | $1.13\cdot10^{-7}$ |
| $|W_{uu}|$ | $3.65\cdot10^{-8}$ |

以下记准确有理上界 $\eta=S_0/64<4.1\cdot10^{-11}$。

原物理坐标是 $\sigma=s/\lambda$。
原精确桥证书 notes/2026-11-09-db6f-root-exact-bridge-m12.json
的 arclength_rescale 有理区间直接给 $0<\lambda<2$。
原 $g=d\sigma^2+f^2du^2$ 在本支撑 $f\ge2/5$：
[R114](R114-actual-noncircular-repair-to-original-tolerance.md) §4
的目标界覆盖原前缀字段支撑和连线段，本支撑为其内部子集。
于是

$$
\|dW\|_{g,F}^2\le4|W_s|^2+\frac{25}{4}|W_u|^2
<(9\cdot10^{-9})^2.                              \tag{5}
$$

这是 Frobenius 上界，也控制算子范数。
令 $d=2.57212\cdot10^{-8},\ p=9\cdot10^{-9}$。
R21 及准确恒等式
$(X+W)^*e-g=(X^*e-g)+2\operatorname{sym}\langle dX,dW\rangle+
\langle dW,dW\rangle$
给全域误差至多 $d+2\sqrt{1+d}\,p+p^2$。
用 $\sqrt{1+d}\le1+d$，最后与 $4.4\cdot10^{-8}$ 的比较也是有理比较。
这证明 (2) 和浸入性；所有 $X+\theta W,\ 0\le\theta\le1$
同样满足这项预算。

## 3. 原位置图真正的二 jets 全区间界

新曲率还需要原位置图实际 Cartesian 二阶导数的界。
单有旧曲率界不足以界定材料坐标中全部二 jets。

[精确预算脚本](../scripts/6a65-m12-up-patch-exact-geometry-budget.py)
把原 binary64 nodal two-jets 和 mean_increments 重新解释为 Fraction。
对每个 quintic Hermite cell，
$P(\xi)=\sum_{j=0}^5p_j\xi^j,\ 0\le\xi\le1$，cell 长为 $h$，有

$$
|P^{(r)}(s)|\le h^{-r}\sum_{j=r}^5
\frac{j!}{(j-r)!}|p_j|,\qquad r=0,1,2.            \tag{6}
$$

$p_j$ 来自准确共享 two-jets；高度差直接用准确 mean_increment。
所需导数中均值高度本身总被正阶 $s$ 导数或角导数杀掉，
不需要用不准确累计高度计算它们。

脚本覆盖与 $[a,b]$ 相交的全部 **73 个源 cells**。
一阶角导数的坐标绝对和权重为 $k+1$（水平）和 $k$（竖直），
二阶为 $(k+1)^2$ 和 $k^2$；都包含旋转标架导数。
用坐标绝对和控制向量范数，得到 native
$B_\psi,B_{ss},B_{s\psi},B_{\psi\psi}$；
它们的显示近似分别为 $2.3111281,.1690762,2.3592368,6.1668949$。

材料角为 $u=\psi-e(s)\sin(3\psi)/3$。
原 clamped cubic spline 用准确有理解，覆盖相交的
**5 个完整 spline 片**，得到 $|e|,|e'|,|e''|$ 的有理上界
$E_0,E_1,E_2$，显示近似为

$$
.6604461903,\quad1.1694717898,\quad1.6429452598.
$$

正式计算一直使用未截断的 Fraction。特别地 $\rho_0=1-E_0>0$。
隐函数微分给

$$
|\psi_s|\le A:=E_1/(3\rho_0),\qquad |\psi_u|\le1/\rho_0,
$$
$$
|\psi_{ss}|\le C_{ss}:=(E_2/3+2E_1A+3E_0A^2)/\rho_0,
$$
$$
|\psi_{su}|\le C_{su}:=(E_1+3E_0A)/\rho_0^2,\qquad
|\psi_{uu}|\le C_{uu}:=3E_0/\rho_0^3.
$$

链式法则给材料坐标二 jets 界

$$
H_{ss}=B_{ss}+2AB_{s\psi}+A^2B_{\psi\psi}+C_{ss}B_\psi,
$$
$$
H_{su}=(B_{s\psi}+AB_{\psi\psi})/\rho_0+C_{su}B_\psi,\quad
H_{uu}=B_{\psi\psi}/\rho_0^2+C_{uu}B_\psi.
$$

因此物理目标标架中所需的坐标二 jets 绝对和满足

$$
C_X:=|X_{\sigma\sigma}|+2|X_{\sigma u}|/f+|X_{uu}|/f^2
\le4H_{ss}+10H_{su}+\frac{25}{4}H_{uu}<10^6.       \tag{7}
$$

实际准确有理上界约 $2247.66355$，这里只需松界 $10^6$。
同理由 (4) 有

$$
C_W:=|W_{\sigma\sigma}|+2|W_{\sigma u}|/f+|W_{uu}|/f^2
\le4B_{ss}^W+10B_{su}^W+\frac{25}{4}B_{uu}^W
<2.4\cdot10^{-6}.                                \tag{8}
$$

这些界覆盖 cell 内部与 C² 接缝，不是采样二 jets 的最大值。

## 4. 法向、实际曲率和支撑

在目标有向正交标架中，旧、新位置微分列为 $V_i,V_i+U_i$。
R21 给 $|V_i|\le\sqrt{1+d}$，(5) 给
$|U_1|^2+|U_2|^2\le p^2$。
两叉积的差至多
$\sqrt{2(1+d)}p+p^2/2$，旧叉积长度至少 $1-d$。
归一化映射的三角不等式于是给同向法向

$$
|n'-n|\le\frac{2\sqrt{2(1+d)}p+p^2}{1-d}
<\frac{3p+p^2}{1-d}=:\epsilon_n<4\cdot10^{-8}.    \tag{9}
$$

其中 $2(1+d)<9/4$ 已作有理核查，不依赖最近点投影的高阶正则性。

旧前缀主曲率绝对值 $K_P<5.547266$，
故旧第二基本形式相对于目标标架的算子范数至多 $K_P(1+d)$。
由
$n'\cdot(X_{ij}+W_{ij})-n\cdot X_{ij}=
(n'-n)\cdot X_{ij}+n'\cdot W_{ij}$，得新**实际**主曲率

$$
|\kappa_i'|\le
\frac{5.547266(1+d)+\epsilon_n C_X+C_W}{1-4.4\cdot10^{-8}}<6. \tag{10}
$$

直接用实际 $X_{ij},W_{ij}$，没有替换成背景曲率或形式 Hessian。
程序以未截断的 $C_X,C_W$ 算出右边约 $5.5473293835$。

旧完整图 $X\cdot n>.7370435198982138>.737$ 且 $|X|<1.9$，所以

$$
(X+W)\cdot n'\ge.737-1.9\epsilon_n-\eta>.736.      \tag{11}
$$

未动部分保持原界。以上证明对全部 $\theta W,\ 0\le\theta\le1$
以及下半镜像都成立。

## 5. R10 全部假设与全域比例

新参数曲面仍为原 $S^2$，所有接口准确 C²，(2) 给浸入，
(11) 给对同一中心 $0$ 的正支撑。
改变片曲率由 (10) 控制；未动前缀保持旧界；
帽保持 $10/3$，尾及圆领完全不变。
因此全图实际曲率仍可取

$$
K=\frac{4763997235009095}{562949953421312}>6.
$$

$.736>1/K$，故 [R10](R10-positive-support-offset-reach.md)
作用于这个真实闭 C² 浸入，给嵌入及
$\operatorname{reach}\ge1/K$。
没有以 surface C² 自动推断环境 C¹,¹ 延拓，也没有声称重做过全点对扫描。

球界给 $D'\le2(R_P+\eta)$。
每个相位新旧像的 Hausdorff 距离至多 $\eta$，
旧 held 见证仅需扣除 $2\eta$：

$$
\delta_{\rm hold}'\ge.19989114-2\eta.
$$

这里将 R21 下界保守截断为 $.19989114$。
固定帽没动，仍有 $\operatorname{diam}\widehat X_0(H)>3.5426$。
三个下界除以同一 $2(R_P+\eta)$，准确 Fraction 比较得到 (3)。

所有相位使用同一空间旋转及材料角平移；
$\tau_\alpha^*g=g$，曲率、支撑、球界对 $R_\alpha$ 不变，
帽固定且接口两 jets 不变。因此结论覆盖全部相位，
没有以有限时刻抽样代替全时间。

## 6. 实际体积矩正性与含反射非全等

按 [R16](R16-fixed-cap-volume-moment-noncongruence.md)
去掉三个固定帽凸起，记原、改后未标记实体为 $\Omega,\Omega'$。
去掉凸起只将上帽变回平圆帽。
帽轴心不在三个凸起盘内，原全图支撑在那里给高度 $H>.737$。
平帽支撑为 $H$、曲率为零，且因 $H>0$ 其点范数不超过对应有凸起点。
故原、改后未标记图仍有同一支撑、球界和 $K$ 界。
R10 给法向管半径至少 $1/K>h_0=1/2000$。
因此 R16 的三个固定凸起体仍处于平帽外侧管内，彼此不相交，
且与活动实体仅沿边界相接；标记实体仍是
$R_\alpha\Omega'\cup B$。

下面比较真实的体积矩。
原未标记边界 $S=\partial\Omega$ 是正径向图 $x=r(\omega)\omega$，
径向投影 Jacobian 为
$d\omega=(x\cdot n)|x|^{-3}dA$，故

$$
\operatorname{Area}(S)=\int_{S^2}\frac{r^3}{x\cdot n}\,d\omega
<4\pi\frac8{.7}<150.                              \tag{12}
$$

这用了 $r<2,\ x\cdot n>.7,\ \pi<22/7$，都是安全松界。

§2–5 已证明全部 $X+\theta W$ 为嵌入。
距原 $S$ 大于 $\eta$ 的点从未被该同伦边界经过，
其边界映射次数不变，故内外归属不变。因此
$\Omega\triangle\Omega'$ 在原 $S$ 的闭 $\eta$ 管内。
$\eta<1/K$ 时，R10 的法向管坐标单射；
$x+t n(x)$ 的 Jacobian 是
$(1-t\kappa_1)(1-t\kappa_2)$，绝对值至多 $(1+K\eta)^2$。
从 (12)、$K<9$ 得

$$
\operatorname{Vol}(\Omega\triangle\Omega')
\le2\eta\cdot150(1+9\eta)^2.
$$

管内 $|x+iy|<R_P+\eta<2$，于是实际活动三阶复体积矩满足

$$
|A_3'-A_3|
\le2\eta\cdot150(1+9\eta)^2\cdot8<10^{-7}.         \tag{13}
$$

最后严格不等式已对冻结系数的准确 $\eta$ 作有理比较，
显示值约 $9.81167635\cdot10^{-8}$。
由 R21 的
$\operatorname{Re}A_3>.4401644538270965>.44016$，得到

$$
\operatorname{Re}A_3'>.44016-10^{-7}>.44>0.        \tag{14}
$$

补丁只含 $3\mathbb Z$ 模，保持三重对称；
cosine 奇偶性和 $e_r(u)$ 的正确镜像保持 $y\mapsto-y$ 对称，
所以 $A_3'$ 为正实数。
固定帽凸起矩仍是同一个准确正数
$B_3=3\pi a_{\rm cap}^3b_{\rm cap}^2h_0/4>0$。
R16 的三阶中心矩张量恒等式遂给

$$
\|T(0)\|_F^2-\|T(\pi/3)\|_F^2=A_3'B_3>0.
$$

该张量范数在全部 $E(3)$ 下不变，包括反射，
故初相与半三重周期相位不能全等。
若刚体对齐 Hausdorff 下确界为零，
平移部分有界、正交部分在紧群 $O(3)$ 中有收敛子列，
极限会给真正全等，矛盾。
因此 $\delta_E>0$；本文不声称 $\delta_E/D'\ge5\%$。

## 7. 实际执行与范围

精确预算脚本 SHA256：
f5e53071668fb99d1d721b7303b52327ebdd11ddc20d6b0dcd267a3d85315dec。

原 payload SHA256：
359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0。
其来源见 [弱矩和补丁记录](../notes/2026-11-26-6a65-exact-weak-moment-cartesian-up-patch.md)。
companion 数值源码 SHA256：
fdf510d186d7fe7dfc9a9b7679838c811f20a69e31873c270cd9e7af4a1e724b。

实际命令：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flexible-closed-surface/scripts/6a65-m12-up-patch-exact-geometry-budget.py \
  --data /tmp/visible-flex-6a65e705/exact-work/m12-prefix-data.npz.gz \
  --parameters topics/visible-flexible-closed-surface/notes/2026-11-26-6a65-m12-up-patch-parameters.json \
  --out /tmp/visible-flex-6a65e705/exact-work/weak-v2-up-exact-geometry-budget.json
~~~

自然 exit 0，0.6443154559965478 秒，全部 17 项有理比较为真。
报告 SHA256：
d3f0646cdc0c6f9c03f121c22565b6963f86c2ad2cd77a3d2738285e030fa42f。
报告是可再生输出，未收入仓库；脚本、准确参数及本证明足够重生。

此传递支付真实改像补丁的全域几何预算。
它未将有限弱矩消失等同完整等距，
也未将 R114 的尖度量证书无偿移植到 $X+W$。
后续继续计算 $(X+W)\circ\Phi$ 的真实 Gram，并增添独立径向应力块。

