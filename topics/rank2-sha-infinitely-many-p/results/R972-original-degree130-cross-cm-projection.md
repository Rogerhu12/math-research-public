# R972 — 原交叉项的完整 degree130 算术投影及其实际剩余分量

日期：2026-11-27。**已证明，并由同次完整公开计算通过。** 原 degree390 的66列、degree130 的22列（含质量列）、完整 $\delta$-pull/trace 和两种 CM 对应全部保留。R970 所指定的固定曲线 $E_*:y^2=x^3+65^3$ 的真实算术线在共同核中唯一；新六 sigma 来源和原交叉迹都向该线非零投影：

$$
\boxed{\Pi_*\mathscr H_{130}=-\frac{11}{405}\Phi_{*,1},\qquad
\Pi_*F_*=-\frac{11}{2}\Phi_{*,1}.}
\tag{1}
$$

这里 $[z^6]\Phi_{*,1}=1$，全系数有理，最小公共分母为385。另一方面，$\mathscr H_{130}$ 本身不在该算术线；原 $SZ$ 也不在 $KZ+K[\delta]^*\Phi_{*,1}$。后者整个空间加入 $SZ$ 后的秩准确由二升为三。因而 (1) 付了一个新的实际算术分量及其五伴随条件，但没有消去原全部 mixed 交叉读数。

## 1. 原完整空间和两个方向的有限同源

全部规范来自 R966/R970：

$$
E_1:y^2=x^3+1,\quad dz=dx/(2y),\quad
K=\mathbf Q(\delta),\quad\delta^2=-3,\quad
\omega=(-1+\delta)/2,\quad X=x^3.
$$

置

$$
V_{390}=\sigma^{390}K[X]_{\le65},\qquad
V_{130}=\sigma^{130}x^2K[X]_{\le21}.
$$

二者维数为66和22；最高列均为质量列。原
$Z=\sigma^{390}P_Z(X)$ 保其全部65个非质量坐标，$[X^{64}]P_Z=1$。
此来源仍由同次完整 CM7/CM19 纤维重新生成，未读取旧输出表。

写 $E=[\delta]^*:V_{130}\to V_{390}$。完整除法式

$$
\sigma(\delta z)=\delta x(z)\sigma(z)^3,\qquad
x(\delta z)=-\frac{x(z)^3+4}{3x(z)^2}
$$

给全列公式

$$
E(\sigma^{130}x^2X^j)=\sigma^{390}I_j(X),\qquad
\boxed{I_j=(-1)^{j+1}3^{63-3j}X^{42-2j}(X+4)^{3j+2}}
\quad(0\le j\le21).
\tag{2}
$$

各列次数为 $44+j$，严格递增，故 $E$ 单射。不能删掉 $j=21$ 再称为完整空间的限制。

令 $T=\mathrm T_{\delta,130}$ 为 R966 的原线丛 trace。若 $w=\delta z$，其完整定义是

$$
T(\sigma^{390}P(X))(w)=
\delta^{-130}\sigma(w)^{130}
\operatorname{Tr}_{K(E)/\delta^*K(E)}
\{x(z)^{-130}P(x(z)^3)\}.
\tag{3}
$$

目标横坐标记为 $a=x(w)$，纤维全部三根满足
$x^3+3ax^2+4=0$。其正幂迹 $q_n$ 和负幂迹 $r_n$ 分别为

$$
q_0=3,\ q_1=-3a,\ q_2=9a^2,\qquad
q_n=-3a\,q_{n-1}-4q_{n-3}\quad(n\ge3),
$$

$$
r_0=3,\ r_1=0,\ r_2=-3a/2,\qquad
r_n=-3a\,r_{n-2}/4-r_{n-3}/4\quad(n\ge3).
\tag{4}
$$

这是三根多项式和其倒数多项式 $u^3+3au/4+1/4$ 的 Newton 恒等式。对原第 $j$ 列取指数 $3j-130$，在 (4) 中依正负选择完整迹；乘 $\delta^{-130}=(-3)^{-65}$，再读取所有 $a^{2+3i}$，就得到 $T$ 的22乘66矩阵。所有其他次数系数为零：递推保持次数模三的类型；最高次数至多65。所以这里构造的是全列 trace，而非只取某个低 jet。

有限平坦同源的 trace/pullback 恒等式给

$$
\boxed{TE=3I_{22},\qquad Q_\delta=\frac13ET,\qquad
Q_\delta^2=Q_\delta,\quad\operatorname{rank}Q_\delta=22.}
\tag{5}
$$

同次计算另在完整矩阵上直接回乘 (5)，并返回原 $TZ=0$。由此有完整分解
$V_{390}=EV_{130}\oplus\ker T$，后者维数44。

## 2. 原两种 CM 对应在全部22列上的准确限制

记 $A_7,A_{19}$ 为同次原生产器的完整66列矩阵，规范始终是

$$
N_\gamma=[\gamma]_*[\bar\gamma]^*/\gamma,\qquad
\gamma_7=3+\omega,\quad\gamma_{19}=4+\delta.
$$

$\delta$ 与两种 $\gamma,\bar\gamma$ 互素。把完整有限纤维按两种同源重排，原 pull/trace 的 Cartesian 基变换给

$$
A_\ell E=EB_\ell,\qquad
TA_\ell=B_\ell T,\qquad
A_\ell Q_\delta=Q_\delta A_\ell,
\quad \ell=7,19.
\tag{6}
$$

此处标准 sigma carrier 的常数不被省去：组合恒等式
$r_\gamma(\delta z)r_\delta(z)^{N\gamma}
=r_\delta(\gamma z)r_\gamma(z)^3$
来自同一个 $\sigma(\gamma\delta z)$；两条式子中的 $1/\gamma$ 也相同。

本次用 (2) 的严格次数三角性从 $A_\ell E$ 恢复 $B_\ell$，随即对全部66行回乘。再独立以完整 $T$ 检验 (6)，并核

$$
B_7B_{19}=B_{19}B_7,\qquad B_\ell\bar B_\ell=I_{22}.
\tag{7}
$$

没有只在 $\Phi_{*,1}$ 或候选 $F_*$ 上检查这些恒等式。

## 3. 唯一原算术线和完整多项式投影

R970 的全部 $2,3,5$ 和两支13局部角色、Schwartz 及全权平方已先验给非零算术来源，且其绝对本征值为 $(\omega,-1)$。本次并不根据两好位任选一个角色。

完整22列的特征多项式经平方自由化，得到

$$
\boxed{m_7(U)=U^{12}-1,}
$$

$$
\boxed{m_{19}(U)=U^{10}-U^8+U^6-U^4+U^2-1
=\frac{U^{12}-1}{U^2+1}.}
\tag{8}
$$

两个 $m_\ell(B_\ell)=0$ 都在全部矩阵上直接检验。因此相应特征投影准确是

$$
P_7=\frac{(m_7(U)/(U-\omega))(B_7)}{12\omega^2},
\qquad
P_{19}=\frac{(m_{19}(U)/(U+1))(B_{19})}{-6}.
\tag{9}
$$

每个投影完整幂等，且秩均为二；它们交换。实际共同投影

$$
\boxed{\Pi_*=P_7P_{19}}
\tag{10}
$$

为有理矩阵，秩恰为一，两侧完整本征身份及幂等性均返回。以其像中的第20列坐标归一为一，得到

$$
\Phi_{*,1}=\sigma^{130}x^2\sum_{j=0}^{20}u_jX^j,\qquad
u_{20}=1,\qquad u_j\in\mathbf Q,\qquad
\operatorname{lcm}\{\operatorname{den}(u_j)\}=385.
\tag{11}
$$

第21质量坐标确为零。R970 的先验非零来源必落在这条完整一维共同核中，故 (11) 才唯一识别那条算术线。其首阶准确为六。

## 4. 原实际 H130 和真六 sigma 候选的非零投影

原 $S=X(X-8)/(7X^2-4X+16)$，而 $P_Z$ 含完整 $X(X+1)(7X^2-4X+16)$ 因子。先作整多项式除法得到

$$
SZ=\sigma^{390}\frac{X(X-8)P_Z(X)}{7X^2-4X+16}.
\tag{12}
$$

全部除法系数回乘后，以完整 (3) 得
$\mathscr H_{130}=T(SZ)$。实际首项比 R966 的非零判据更精确：

$$
\boxed{[z^6]\mathscr H_{130}=-\frac1{105}.}
\tag{13}
$$

结合 R966 (53)，这也给原准确低次系数

$$
\boxed{[X]P_Z=-\frac{2^{126}}{35}\ne0.}
\tag{14}
$$

新 $F_*$ 取 R971 的真实六 sigma 输入及完整 $P_S\mathcal J_5$，没有以目标共同核替代候选。将两者施以 (10)，全部22坐标以及两条66坐标 pullback 都准确返回

$$
\boxed{\Pi_*\mathscr H_{130}=-\frac{11}{405}\Phi_{*,1},
\qquad \Pi_*F_*=-\frac{11}{2}\Phi_{*,1}.}
\tag{15}
$$

所有多项式、两种绝对 CM 相位和原22列都在同一公开 run 中，故没有把不同规范的向量拼接为此身份。

式 (15) 使 R971 (15)–(16) 的实际非零前提全部成立。其完整五伴随满足

$$
\mathcal C_*\mathcal F_*=\Phi_{*,1}\otimes\Lambda_*,
\qquad \boxed{\Lambda_*(0)=-11/2.}
\tag{16}
$$

当前普通 $p>211$ 上，(9)、385、R971 的整框架和 $\Lambda_*(0)$ 所涉及分母/分子全为单位；读取第一变量六阶矩并除以 $720\Omega_p^6$ 给完整五伴随整性。故 $\Lambda_*$ 是整 Amice 卷积单位。

R970 的真实物理曲线仍是 $b_*=65^3$，不能把它写成 $65$。若取本次准确整归一 $\widehat\Phi=385\Phi$，相容的原周期和 (35) 给

$$
\boxed{\nu_{\Phi_{*,17},p}
=\frac{65^3}{17\cdot385}\,\widehat\nu_{*,p}.}
\tag{17}
$$

这只是在同一原微分规范中的模型运输。新算术中央导数零因而杀 (16) 上的完整独立伴随中央行；它仍不杀带任意旧单位/深度/logarithm 的混合测试。R970 的惰性 signed 通常 Selmer 桥也保其原范围；本文没有把 ordinary 伴随整测度身份自动移到惰性位。

## 5. 两个原剩余分量都实际非零

令

$$
\mathscr H_\perp=(1-\Pi_*)\mathscr H_{130}
=\mathscr H_{130}+\frac{11}{405}\Phi_{*,1}.
$$

由 (11)、(13)，

$$
\boxed{[z^6]\mathscr H_\perp
=-\frac1{105}+\frac{11}{405}=\frac{10}{567}\ne0.}
\tag{18}
$$

所以并非只“尚未识别”$\mathscr H$ 本身：它已经被精确排除为单条新算术来源。候选 $F_*-\Pi_*F_*$ 的首项同样为 $13/2\ne0$。

原另一个剩余项定义为

$$
R_{\rm new}=(1-Q_\delta)(SZ).
$$

由 $[z^6]SZ=1/7$、$\delta^6=-27$ 和 (5)、(13)，

$$
\boxed{[z^6]Q_\delta(SZ)=3/35,\qquad
[z^6]R_{\rm new}=2/35\ne0.}
\tag{19}
$$

完整66列另直接返回 $Q_\delta R_{\rm new}=0$ 及
$SZ=Q_\delta SZ+R_{\rm new}$。因此整个原 cross 的准确分解为

$$
\boxed{SZ=-\frac{11}{1215}[\delta]^*\Phi_{*,1}
+\frac13[\delta]^*\mathscr H_\perp+R_{\rm new}.}
\tag{20}
$$

两个右侧余项都不可删除。

还可完全排除“旧 $Z$ 加新 $\Phi$ 已经张成原 cross”。(2) 中质量零的 $j\le20$ 列全部含 $X^2$，(12) 也含 $X^2$，但 $Z$ 的 $X^1$ 系数由 (14) 非零。因此在关系
$aZ+b[\delta]^*\Phi_{*,1}+cSZ=0$ 中先有 $a=0$。若 $c\ne0$，施 $T$ 就使 $\mathscr H_{130}$ 成为 $\Phi_{*,1}$ 的倍数，与 (18) 矛盾；于是 $b=c=0$。所以

$$
\boxed{\dim_K\langle Z,[\delta]^*\Phi_{*,1}\rangle=2,\qquad
\dim_K\langle Z,[\delta]^*\Phi_{*,1},SZ\rangle=3.}
\tag{21}
$$

同次消费者另在132行忠实有理矩阵上独立返回这两个完整秩。

最后，R966 的 $\Pi_0(C_1J)=(9SZ-Z)/2$ 与 $TZ=0$ 给

$$
T\Pi_0(C_1J)=\frac92\mathscr H_{130},\qquad
\boxed{\frac13[\delta]^*\Pi_*T\Pi_0(C_1J)
=-\frac{11}{270}[\delta]^*\Phi_{*,1}.}
\tag{22}
$$

式 (22) 是原 cross 的一个实际算术投影，不等于其完整中央读数。后继任务必须处理 (18) 的全部剩余谱和 (19) 的真正 $\delta$-new 分量，以及原 mixed cut；不是把 (15) 的非零重报为无穷素数结论。

## 6. 公开来源、完整回执与数据范围

- 源提交 cd89412822ef2497f97891969248bfdcc23b52fe。
- [run45881262820](https://github.com/Rogerhu12/math-research-public/actions/runs/45881262820)，job140120885384，2026-11-26 19:13:45 UTC 实际 success；整个原生产入口356.840560475秒，本消费者0.7112437179999915秒。
- 原入口参数为 --workers=4、python-flint0.9.0；原 E65/E89、全部局部 Schwartz、六低 jet、旧六 sigma/原 h、固定 p227 C24 和所有既有门都在同次保持。没有启动另一份原306几何。
- 新消费者 scripts/check-original-degree130-cross-cm-projection.py：19027 B，SHA256 35b8c679cad5c33a78ae90340a063ee95259e1678dbaf9eda595ce39a1bb7ccd。
- 15源 manifest SHA256 3474f1be63d5d4584ce3e36a4187511dcde0664d11659012e3ff934899d23fb6。
- 原完整390矩阵 SHA256 e80e5777735077da004012b5abe8dfd2ba246b9404fd53899502c453242d1fff；完整130矩阵 SHA256 aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113。
- 全22列嵌入 SHA256 a2f4998c058d946ae45a86557e79aca353d6f69e96543bb8c9a724ffb63c1e38；完整 trace SHA256 46f506ace8442d99e02e5bc17445eec427fd3c92e45d717931c55177b9035106。
- 完整目标投影 SHA256 7affd5fd88cbc0711f963681490a0be160ebca7021dd7c4ded998015706403d3；首项一算术向量 SHA256 510b32718ce9ff51aee4a4de86cc5c362f7f0242a94b7d72df4effc0f95a4497。
- 原 $H_{130}$ SHA256 f779062d6ced732b0ef093e37b1f821248ae6cfb90f8f6a160c6a333d839df06；其算术线外完整残差 SHA256 bdfe375bd29185b174ea81e7fcc4d525ff8e22c53c709271f19ec7085e0e0be2。
- 原 $SZ$ 的完整 $\delta$-new 残差 SHA256 2ddcb766e96d65797aad20c430d3ab4efc6ca20a3fa58fa59aba44fb37d9184a。
- 原程序 stdout30495 B，SHA256 a93e8b686ae90c95fa9fe2391bb484ec2ce085ce5bfa16e1af06d2162258ce0e；完整 job 日志81659 B，SHA256 9ff63727c2ec2348628fc89d6d9d5520ccc8e19ea244e570808327de71759c54。

只保源码、参数、来源/run/hash及上述结论；生成向量、矩阵和日志不入库。本次给出的完整精确身份是有限特征零计算，主目标的跨无穷素数中央非零仍未证明。
