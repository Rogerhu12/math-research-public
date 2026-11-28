# R150：正确碰撞 Delta 零的两个整谱域原单位返回与完整排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

**结论：当前正确、对称归一的 $h_U=k_U$ 原图上，整个 $\Delta=0$ 分支没有原解。** 最后两个完整 QQ 不可约谱域 $K_{99},K_{300}$ 均已由本次唯一实际运行的原单位返回排除。结合先前独立正确的 $C_1,C_2,C_4$ 全支排除，正确十七阶覆盖的全部谱支持已关闭。

本次不是仅排两个有限域点。下面用已刊同域唯一 $u,Q$、各自的有限 DVR 整模型、完整九来源 Bézout 一及 Nakayama，证明两个 QQ 域的所有复嵌入同时排除。$\Delta\ne0$ 仍开放；本条不证明整个碰撞图或普通 Hilbert ISP 完成。

## 1. 准确原图、单位及正确覆盖

沿[三个小因子的独立原排除](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)第2节和[原 Pf 来源静审](../notes/2026-11-28-unit211-h-equals-k-Pf-true-original-static-audit-8542.md)，本图使用已付原支持

$$
A B\lambda(2\lambda-1)\,u(u-1)\,Q(1-Q)\,bc\,P_{02}\,P_f\,S\ne0,
\tag{1}
$$

其中

$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\quad \ell=A^3/B^2,
$$

$$
T=A^2/B,\quad
w=\lambda-1-T,\quad h_U=k_U=1+\xi,\quad
S=2\xi+3-2\lambda,\quad P_f=T_0(J-Q).
$$

$M=4bc(1-Q)$ 也是原单位。(1) 的支付来自此碰撞图本身的真原来源；没有把不同值 W 的单位或 $D\ne0$ 搬入。物理碰撞 $D=0$ 在本篇始终保留；没有任何 D 的负幂。

原两条同点线性关系是

$$
P_f f+bc\Phi z+P_c=0,\qquad
N_F f+bcS\xi z+N_C=0,\qquad z=Qt,
$$

$$
\Delta=\Phi N_F-S\xi P_f,\qquad
T_{\rm num}=P_fN_C-P_cN_F .
\tag{2}
$$

因此在 $\Delta=0$ 上，$T_{\rm num}=0$；又 $\Phi N_F=S\xi P_f\ne0$，该支不缺漏两线同时退化的情形。

[正确固定十七阶覆盖](R150-appendix-unit211-h-equals-k-corrected-fixed-seventeen-lambda-cover-and-5640-points.md)只从正确原输入

$$
P(\lambda,u),\quad M_{\rm true}(\lambda,u),\qquad
\deg_{\lambda,u}P=(28,3),\quad
\deg_{\lambda,u}M_{\rm true}=(110,14)
$$

得到已付谱支持剥除后的完整必要式

$$
C_1^{19}C_2^{14}C_4^6F_{99}F_{300}=0.
\tag{3}
$$

$F_{99},F_{300}$ 是不同的 QQ 不可约因子，均重数一。前述小因子论文已分别在整个 $C_1,C_2,C_4$ 条件下返回真原单位，不依赖撤回的错误 compact 均值。故此前准确剩余是 $F_{99}F_{300}=0$，本次正处理这两个完整域。

## 2. 已刊特征零基结构

[约化谱基](R150-appendix-unit211-hk-Delta-zero-reduced-base-and-4788-coordinate-Artin-envelope.md)证明，在已付纯谱支持局部化后，

$$
\mathbb Q[\lambda,u]/(P,M_{\rm true})
\simeq K_{99}\times K_{300},
\qquad K_d=\mathbb Q[\lambda]/(F_d).
\tag{4}
$$

准确地说，局部化也包含该文记号 $\Sigma^{-1}$。各域内的原 u 唯一：

$$
u=\eta_d\in K_d.
\tag{5}
$$

[原 P 判别式及同 Q 唯一约化](R150-appendix-unit211-hk-independent-P-discriminant-unique-reduced-Q-and-2394-Artin-envelope.md)进一步证明，在 (1) 保留的每个域内，

$$
Q=\theta_d\in K_d
\tag{6}
$$

唯一且约化。该证明使用原 fixed $4\times4$ Q Sylvester 的赋值一；原 $T_{\rm num}$ 的 Q 头即使下降也完整保留，不把裸 P 的简单根单独当作 Q 恢复依据。

(4)–(6) 是本次真正的特征零前提。它们不提供大系数形式的 $\eta_d,\theta_d$，但足够构造一个良好整模型。冻结 ad00 的 QQ 整域联合 u-gcd 仍未返回；本次没有重新执行它。

## 3. 两个固定第一剩余点与全部 p 整性

源在任何原 z 理想构造之前固定素数列表和每个 p 内 $\bar\lambda=0,\ldots,p-1$ 的次序。选择条件仅为：

- 两个首一谱因子和原 P/M、Delta/Tnum、所列原权有理式的全部常数系数 p 整；
- 目标谱因子的简单根、另一谱因子非零；
- P 的 u 三次头非零，完整模 u-gcd 恰一次；
- 原 Delta 的 Q 二次头非零，完整模 Q-gcd 恰一次；
- 所有实际原权分母和 Loww 常数项非零。

选择函数没有读取原 z gcd、理想秩或任何目标结果。两域都在列表第一个素数1009、自己的第一个简单谱候选处通过全部条件：

| 完整 QQ 域 | p | $\bar\lambda$ | $\bar u$ | $\bar Q$ | Loww 常数 $\bar c_0$ | P 三次头 | Delta 分子二次头 |
|---|---:|---:|---:|---:|---:|---:|---:|
| $K_{99}$ | 1009 | 158 | 99 | 956 | 745 | 586 | 346 |
| $K_{300}$ | 1009 | 217 | 846 | 926 | 838 | 684 | 763 |

每域检查2786个有理常数系数的分母为 p 单位。两个完整模 Bézout 准确给 $u-\bar u$、$Q-\bar Q$，全部商积和两乘回完成，没有保留另一个未识别的 u/Q 分支。

原权单位的实际剩余值如下；它们全非零：

| 原量 | $K_{99}$ 所选点 | $K_{300}$ 所选点 |
|---|---:|---:|
| A | 172 | 917 |
| B | 545 | 307 |
| $\lambda$ | 158 | 217 |
| $2\lambda-1$ | 315 | 433 |
| u | 99 | 846 |
| $u-1$ | 98 | 845 |
| Q | 956 | 926 |
| $1-Q$ | 54 | 84 |
| $P_f$ | 254 | 869 |
| bc | 830 | 425 |
| $P_{02}$ | 237 | 492 |
| S | 761 | 681 |
| M | 687 | 531 |

目标返回后没有再选任何点、素数或有限域分量。

## 4. 这些剩余点确属同一完整域的整模型

固定 $d=99$ 或300，将 $F_d$ 首一化。第3节给简单根 $\bar a$，定义

$$
\mathcal O_d=
\left(\mathbb Z_{(1009)}[\lambda]/(F_d)\right)_{(1009,\lambda-\bar a)}.
\tag{7}
$$

$F_d$ 在 QQ 不可约，所以该环是分式域 $K_d$ 内的域序局部化。模下简单根使 (7) 为未分歧 DVR，剩余域 $\mathbb F_{1009}$。只需所选局部点简单；不要求整个 $F_d\bmod1009$ 不可约或整体无重根。

P 的所有系数在 $\mathcal O_d$，其 u 三次头是单位。已知 $\eta_d\in K_d$ 满足 P，故 $\eta_d$ 在 $\mathcal O_d$ 上整。DVR 整闭，得

$$
\eta_d\in\mathcal O_d.
\tag{8}
$$

Mtrue 同样 p 整，所以 $\bar\eta_d$ 必为两个特化多项式的公共 u 根。第3节完整线性 gcd 唯一识别 $\bar\eta_d=\bar u$；没有从某个未证明属于该域的模分支开始。

原 Delta 的 Q 二次系数是

$$
-\frac{2(B^2-A^3)(\lambda^2+\lambda-1)}{B^2}.
\tag{9}
$$

它在所选点非零，故在 $\mathcal O_d$ 为单位。由已知 $\theta_d\in K_d$ 及 Delta，$\theta_d$ 也整，故

$$
\theta_d\in\mathcal O_d.
\tag{10}
$$

完整原 Delta/Tnum 模 Q-gcd 再唯一识别其剩余值为表中的 $\bar Q$。Tnum 的 Q 首项不用反演。所选表中各原量的分子/分母非零，连同 (8)、(10)，证明所有实际恢复系数在 $\mathcal O_d$ 正则。

这一步是由同一特征零域、首一原方程及整闭性得到的；“有限域没有点”本身不参与推理。

## 5. 完整原 Gram、八原 z 行及反转容量

在整个 $\mathcal O_d$ 使用同一点恢复

$$
f=-\frac{P_c+bc\Phi z}{P_f},\quad
V=\frac{Jf-G+bcz}{Q},\quad t=z/Q,\quad W_1=T_0/2+2uf,
$$

$$
x=\frac{(u-\ell Q)V-(u-\ell)W_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad A_1=2f-2V+2bc\,t .
\tag{11}
$$

再以 $\rho^2=1-Q$、$b=\ell/2+(u-\ell)\rho/[2(1-Q)]$、$c=\bar b$、
$p=1+\rho,q=1-\rho,X=x+\rho y,Y=\bar X$ 重建四原 Gram 行。源明确使用

$$
\operatorname{vm}(v,w)_1=v_0w_1+v_1w_0
$$

的真双数乘法；完整 E0、N0、P1、三值矩与 $N_4(V)=0$ 同点返回，没有错误 compact mean 的依赖。

八条原值是

$$
F_1=E_1,\ F_2=E_{B,e},\ F_3=E_{B,o},\ F_4=N_1,\quad
F_5=N_{B,e},\ F_6=N_{B,o},\ F_7=P_{B,e},\ F_8=P_{B,o}.
\tag{12}
$$

源在两个所选点都完整构造了全部八条；实际次数分别为

$$
(2,2,2,2,3,3,3,3).
$$

原 B/C 共轭及 $1-Q$ 单位使偶、奇两系数都是必要条件。两个有序 rho 符号完整保留，不选择其中之一。

结构次数上界记为 $d_i=(2,2,2,2,3,3,3,3)$。后文采用固定容量

$$
\widetilde F_i(\zeta)=\zeta^{d_i}F_i(1/\zeta),
\tag{13}
$$

而不是依某次模下降的实际次数更改反转。因 (11) 仅除表中已付单位及2、4，(12)、(13) 全在同一 $\mathcal O_d$ 上定义。

## 6. Loww 的原组合与首一三次

[完整 Loww 原纤维](R150-appendix-unit211-h-equals-k-Delta-zero-complete-Loww-fibers-8664-cover.md)给准确恒等式。置 $m=u-\ell,\delta=1-Q$，

$$
\begin{aligned}
E_{W,2}&=(2u-u\ell-V)E_{B,e}
+[2(u-\ell Q)-um-mx-\ell\delta y]E_{B,o},\\
N_S&=\ell N_{B,e}+mN_{B,o},\quad
P_S=\ell P_{B,e}+mP_{B,o},\\
L_w&=N_S-P_S+E_{W,2}\\
&=2P_{02}(2\lambda-1)w
-bc\,t\,[K_w+4(f-u)(t-2)],
\end{aligned}
\tag{14}
$$

$$
K_w=2[t^2+(5u-4x-2)t+2(x^2-\delta y^2)
+4x+4\delta y-4ux+2u^2-6u+Q].
$$

本次实际完整返回 (14)，包含自由 f 修正。故在原八式理想中有

$$
L_w(z)=c_0+c_1z+c_2z^2+c_3z^3,\qquad
c_0=-2P_{02}\lambda^2(2\lambda-1)^2/B\in\mathcal O_d^\times .
\tag{15}
$$

取 $\zeta=1/z$，定义

$$
q_\zeta=
\zeta^3+(c_1/c_0)\zeta^2+(c_2/c_0)\zeta+c_3/c_0.
\tag{16}
$$

这是首一三次；从未反演 $c_3$。因此

$$
C_d=\mathcal O_d[\zeta]/(q_\zeta)
\tag{17}
$$

在 DVR 上自由秩三，且包含所有原首项下降和可能的模下 $\zeta=0$ 分量。

## 7. 两次实际完整原单位返回

在每个已经固定的剩余域中，源对 $\bar q_\zeta$ 与反转八式做普通一元多项式 Bézout，始终保留全部九个原来源。两个域均在第一条 $\widetilde E_1$ 就已经返回

$$
a_0\bar q_\zeta+a_1\overline{\widetilde E_1}=1.
\tag{18}
$$

其余七个来源的最终乘子为零；源仍以完整九项向量全部乘回，得到准确常数一。没有用模 D 幂零、正 z 幂或仅一个秩猜测替代 (18)。

| 谱域 | 实际倒 z 三次 SHA256 | 完整九源证书字节数 | 完整九源证书 SHA256 |
|---|---|---:|---|
| $K_{99}$ | 42777d0e174683e00d18f462c2fc771982ffb7f953a08aaf1f24d51eb4bc0e84 | 241 | 71df90839458df2994b442a9fdf11c64a372f08a41f5a5c90816f6a29ef8a31d |
| $K_{300}$ | 02debd59c36da757811382d10e86e12e5d8c4ff80de93114365bcc27af7b70d1 | 242 | 5c366f65afdf4c023387b63d371eac56daf1c05c0241cf3c8995c60f30acfd9e |

证书系数不另存；完整定义、所选四个小参数及源保留，所有实际乘积已在唯一首次运行返回。

## 8. 有限模提升排除整个 QQ 域

令 $J_d\subset C_d$ 为八个 $\widetilde F_i$ 生成的理想。由 (17)，$C_d/J_d$ 是有限 $\mathcal O_d$ 模。(18) 准确给

$$
(C_d/J_d)/\mathfrak m_d(C_d/J_d)=0.
$$

Nakayama 引理于是给

$$
C_d/J_d=0.
\tag{19}
$$

张量到分式域 $K_d$，原倒 z 理想为单位。由于 $K_d$ 是整个 QQ 不可约域，(19) 排其全部复嵌入，不是只排表中的一个模点。

从倒 z 返回原 z 也没有遗漏。令 $I_d=(F_1,\ldots,F_8)\subset K_d[z]$，由 (14)、(15)，

$$
z\left[-(c_1+c_2z+c_3z^2)/c_0\right]=1
\quad\text{于 }K_d[z]/I_d .
$$

所以 z 已在这个原商中为单位。倒 z 的单位返回强制

$$
K_d[z]/I_d=0.
\tag{20}
$$

故 $F_{99}$、$F_{300}$ 上的整个原同点条件同时排除，所有几何重数、头零和共轭符号均保留到这个结论。不存在由“模 D=0”升为特征零 D=0 的推理。

## 9. 合成整个当前 Delta 零分支

现在 (3) 的五类支持均已在其完整原图中排除：

| 谱支持 | 完整原排除来源 |
|---|---|
| $C_1=0$ | 独立有理权点上的真自由 f Gram Bézout 一 |
| $C_2=0$ | 完整四维常数代数上的真原 f Bézout 一 |
| $C_4=0$ | 完整十二维常数代数上的真原 f Bézout 一 |
| $F_{99}=0$ | 本篇有限 DVR 原单位返回，全部99个复嵌入 |
| $F_{300}=0$ | 本篇有限 DVR 原单位返回，全部300个复嵌入 |

前三条的正确来源和错误 compact 后段的隔离已由[完整小因子论文](R150-appendix-unit211-h-equals-k-corrected-small-factor-exclusions-and-4788-points.md)逐项证明，本次没有恢复旧848/578/七 lambda覆盖。

(3) 的 $19,14,6$ 重数也不留下幂零原分量：若模一个因子 $C$ 已有原单位关系，模 $C^n$ 的单位由有限几何级数提升；再按五个互素谱支持作 CRT 合成即可。两个大因子本来重数一，本篇 (19)、(20) 是完整理想结论，不只点集排除。

因此，当前正确碰撞图的整个 $\Delta=0$ 原支关闭。原 $P_f=0$ 等前置支付沿第1节独立真原结果，不把本次计算登记成那些分支的新运行。$\Delta\ne0$ 仍需新的原条件；整个碰撞及普通 ISP 仍未完成。

## 10. 唯一实际执行及再生边界

源：[两个整谱域 finite-DVR 原倒 z 单位返回](../notes/2026-11-28-unit211-hk-two-spectral-fields-finite-DVR-original-inverse-z-unit-8542.py)。
[完整首次输入](../notes/2026-11-28-unit211-hk-two-spectral-fields-finite-DVR-original-inverse-z-unit-8542-input.md)；
[小实际收据](../notes/2026-11-28-unit211-hk-two-spectral-fields-finite-DVR-original-inverse-z-unit-8542-execution.json)。

- 源 blob：eb63f13d8b7e2d9d6752ea19f52b81daae6b2648；20013字节；
- 源 SHA256：c3d60e3048e197a7ebe908f0d4e6c1b6f2bcd435dd0718cec3d3ae41d280523a；
- 唯一 run46150595117 / job140996178796，attempt1；
- source 与执行前真实 pull 均 dfc2ab4ab7d8c8125d9ff9f94145b84285575497；
- pull 时间2026-11-28T13:38:26.602749+00:00，两份 README 不变；
- 首次180秒、4 GiB，外195秒；实际2.70292276秒，最大RSS70392 KiB，源 exit0；
- 数学末阶段2.624109349秒；stdout10432字节；
- stdout SHA256：1b74aae872a4e1613450ffd6f1d25a2726da152e13bf094980390be1c00cb773。

统计：84个常数逆乘回、20个多项式商积、6次完整两项 Bézout、42个整模型标量检查、52个原 Gram 返回、14个原矩返回、16条原 z 行、2次完整倒 z 单位返回。

必要旧定义仅截到 ad00 第4728字节的 P/M/F 参数尾，SHA
f3de7830b2ff98c6f4e7df0a891eb7fe2bff61c8ccf6ba6ae83134316ae82f59。
其内正确 RWO 的6055/5121字节前缀及全部源码 SHA 也逐一核定。历史 P 只由 runner 终端从固定 commit 临时读取并选择准确 SHA；错误第二曲线不读、不执行。

已刊 P/M/F 的直接定义再生不是新的覆盖门；没有进入冻结 QQ 整域 u-gcd、旧同 Q 返回或旧八 z 门。本次新计算是一个有已证明整模型的有限剩余域原单位目标。没有增时、换点、重跑成功域或保存可重算大系数缓存。
