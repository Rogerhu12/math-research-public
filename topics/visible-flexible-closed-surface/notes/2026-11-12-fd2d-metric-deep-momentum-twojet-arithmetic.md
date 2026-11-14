# 深尾有限动量方程：物理二 jet 的稳定组合与归一化缺陷

## 1. 实际问题和本文件范围

新物理输入 `2026-11-12-fd2d-layered64-wc01-recovery02-config.json` 的 SHA256 为
`d4d41047c5afa1df90e17e3814e896a7cd91f64c79d0e11116e071cb97e17994`。
在它的真实 raw cell159/segment3/x=1，数值侧直接求值给出

\[
 r=.32,\quad \log w=-423.7456058685332,\quad
 w=9.324415992003524\cdot10^{-185},
\]

而 binary64 中先算 `w*w` 或 `exp(2*logw)` 得零。
原动量 root 的 `mu/w²`、逆转换的 `w²/mu`、含 `r_x` 的 flux prefactor，
以及物理 Darboux 缺陷再除 w² 的 audit，不能继续以这些分离中间量实现。
这不是原实数方程失去意义，也不是该物理 profile 的不可行性结论。

另名模块 `fd2d-metric-deep-momentum-physical-jets.mjs` 实现**同一有限动量
root 和完整 flux 的实际物理二 jet**。原冻结源不改，普通区间保留其运算顺序。
深处分支仅作以下实数恒等式的重新排列。它仍是浮点求值器，不是区间证书；有限
angular projection、root residual、径向离散误差和无限尾问题都没有因此自动支付。
本模块不启动 DN 或径向 ODE。

## 2. 记号与准确因子组合

设圆周模态频率 m_j=spacing·j，o∈{−1,1}，μ>0 在一个原 cell 内固定。
计算变量为 x，r_x≠0，定义

\[
 \sigma=r_x/r,\quad k=(\log w)_x,\quad W=w^2,\quad E=1+W,
\]
\[
 T_\pi=\frac{o\sqrt6\mu}{r^4w^2},\quad
 P_\pi=\frac{o r^3r_xw^2}{\sqrt6\mu},\quad
 C=\frac{r^3}{\sqrt2w}.
\]

T_π 是非零动量 Fourier 分量的 target factor，P_π 是未乘频率的 flux factor。
不要把 P_π 与下文角函数 P 混同。令 λ=logμ−2logw，三因子及 T_π 的逆均可由
完整的对数组合求值。P_π 的组合必须包括 log|r_x| 及 sign(r_x)，不能先生成
w²/μ 再乘已经很小的 r_x。

在实数中准确有

\[
 T_\pi P_\pi=\sigma,\quad
 P_\pi C=\frac{o r^6r_xw}{\sqrt{12}\mu},
\]
\[
 \frac{\sigma\sqrt2w}{r^3P_\pi}
 =\frac{o\sqrt{12}\mu}{r^7w},\qquad
 \frac{r_xw}{P_\pi}=\frac{o\sqrt6\mu}{r^3w}.
\]

这些恒等式也给数值侧 analytic JVP 的组合：若原 root 导数矩阵为 B，令
\(\bar D=P_\pi\,dL\)，则解 `B Dbar = Ppi * right`，在形成右端之前以
P_πT_π=σ、P_πC 的组合替换两个分离因子。π 列的投影项直接含 σ；Q 列直接含
P_πC。最后 Q 行和 mean-height 行分别使用上式两个商。这样不需要先制造一个
可能下溢的 P_π 再乘很大的 dL。此 JVP 的实现归数值侧；本模块消费其同一个 root。

## 3. 两个关键导数恒等式

令

\[
 p_j=-m_j C Q_j,\quad
 P(\theta)=\sum_jp_j\sqrt2\sin(m_j\theta),
\]
\[
 L(\theta)=L_0+\sum_jL_j\sqrt2\cos(m_j\theta),\quad
 K=L-P_\theta,
\]
\[
 U=\sum_j[-m_jL_j+(m_j^2-1)p_j]\sqrt2\sin(m_j\theta).
\]

原方程的实际完整（linear+nonlinear）flux 分量记为 f_j，尚未乘 P_π。
它不是只取 nonlinear correction。原 ODE 是

\[
 \dot\pi_j=4\sigma\pi_j+P_\pi m_jf_j,\qquad
 \dot Q_j=\sigma[(m_j^2-4)Q_j+\sqrt2wL_j/r^3].
\]

target 导数中的原表达直接化为

\[
 T_\pi[\dot\pi_j-(4\sigma+2k)\pi_j]
 =\sigma m_jf_j-2k(T_\pi\pi_j).
\]

故新模块不用先求很小的 π_dot，再减两个近量，最后乘很大的 T_π。
若 engine 保存 `root.target`，直接使用它；否则由同一 state 与组合因子求
T_ππ_j。不能用 root 的近似 moment 偷换 target，因为这会无声忽略 root residual。

由 C_dot/C=3σ−k 可得

\[
 \dot p_j=[(m_j^2-1)\sigma-k]p_j-m_j\sigma L_j,
 \qquad \dot P=\sigma U-kP.
\]

这避免 `Qdot+(3σ−k)Q` 先下溢，再乘 1/w。
在对 root 作隐式求导时，固定 L 的显式导数满足
`dK = −d(P_theta)`。先把这部分从 root 的投影非线性项中求出，再解同一正定 B 得 L_dot。

## 4. 显式非线性 root 导数的无孤立 W 表达

记

\[
 w_P=wP,\quad w_K=wK,\quad w_T=wP_\theta,\quad
 u=2w w_K+w_K^2+Ew_P^2,
\]
\[
 S=1-w_P^2,\quad s_D=\sqrt{1-u},\quad A=1+L+w w_T.
\]

先乘 w 再平方，例如 W P²=(wP)²、W K²=(wK)²；不能把浮点 W=0 当作所有
这些乘积均为零。若缩放后的真正最终量超出浮点范围，模块报错；不把数值范围失败
改称数学无解。

原 root 二次 correction 是

\[
 q=\tfrac12(K^2+EP^2)+KP_\theta+T f_c+(1+K)P_\theta g_c,
\]
\[
 T=2K+K^2+EP^2,\quad
 f_c=u f(s_D),\quad f(s)=\frac{2+s}{2s(1+s)^2},
\]
\[
 g_c=\frac{w_P^2+Su/(1+s_D)}{S s_D}.
\]

为避免形成 T² 再乘 W，定义

\[
 V=wT=2w_K+K w_K+EPw_P.
\]

于是 T f_c=V²f(s_D)。在固定 L 的显式导数中，令 dP=σU−kP、
dP_θ 由上述每模态 p_dot 求和、dK=−dP_θ。逐项微分给

\[
 du=2ku+2(w+w_K)(w\,dK)+2Ew_P(w\,dP)+2k(ww_P)^2,
\]
\[
 dS=-2kw_P^2-2w_P(w\,dP),\qquad ds_D=-du/(2s_D),
\]
\[
 dV=kV+2(w+w_K)dK+2kw w_P^2+2Ew_PdP.
\]

写 N=w_P²+Su/(1+s_D)，则

\[
 dN=2w_P(kw_P+w\,dP)
 +\frac{(dS)u+Sdu}{1+s_D}-\frac{Su\,ds_D}{(1+s_D)^2},
\]
\[
 dg_c=\frac{dN}{S s_D}-g_c\left(\frac{dS}{S}+\frac{ds_D}{s_D}\right),
\]
\[
 d(Tf_c)=2V(dV)f+V^2f
 \left(\frac1{2+s_D}-\frac1{s_D}-\frac2{1+s_D}\right)ds_D.
\]

特别地，二次项导数可以先用 dK=−dP_θ 消掉 K 的抵消项：

\[
 d[\tfrac12(K^2+EP^2)+KP_\theta]
 =EPdP-P_\theta dP_\theta+kw_P^2.
\]

故完整 dq 就是此式加 d(Tf_c)，再加

\[
 (dK)P_\theta g_c+(1+K)(dP_\theta)g_c+(1+K)P_\theta dg_c.
\]

代码以同一 N 点投影把 dq 移到右端，与 §3 的 target 导数合并，解同一 B；
没有改变有限投影方程，也没有添加角模态或用点值 K 代替有限 root。

## 5. 实际物理二 jet 和归一化 Darboux 缺陷

记

\[
 b=kK+\dot L-\dot P_\theta,\qquad
 G=\sigma EU^2-kL+k(w_Kw_T-w_P^2).
\]

**归一化缺陷**直接定义为

\[
 D_{\rm norm}=A b-G.
\]

物理 Darboux 值才是

\[
 D_{\rm phys}=\frac{w^2}{r_x r E^2}D_{\rm norm}.
\]

新 API 每个 `perAngle` 同时返回 `normalizedDarboux`，audit 直接消费它；不再从
可能已经下溢为零的 D_phys 除以已下溢为零的 W。对 D_phys 的最终求值把
`2 logw − log|r_x| − log r − 2 log E + log|Dnorm|` 合并后一次指数，保留 sign(r_x)；
若最后的物理值确实小到不可表示，返回零并计入 `physicalDarbouxUnderflowCount`。
这不把归一化缺陷报成零。

以下以 h 表示实际高度函数（区别于 §4 的辅助标量 u；输出 keys 仍叫 ur、ut 等）。
同样用 `logw−log|r_x|` 与最终乘子的对数合并，得到

\[
 h_r=w+w_K,\quad h_\theta=r w_P,
\]
\[
 h_{rr}=\frac w{r_x}(k+b),\quad
 h_{r\theta}=wU+w_P,\quad h_{\theta\theta}=r w_T.
\]

H 的 Fourier 归一化与旧源保持一致：Q 是 plain-cos 高度系数的 r⁻⁴ 倍，
p/L 使用 sqrt2 归一化基；代码没有把两者混用。原 mean-height 两状态也全部保留。

物理 holonomy 的稳定被积式为

\[
 \frac{u}{s_D(1+s_D)}+
 \frac{(w+w_K)w_T}{S s_D},
\]

而 normalized holonomy 直接由同一角投影的 mean(L+q) 给出。
普通分支保留旧输出的全部 key；新增 normalized 信息不改变旧值的定义。

## 6. 相邻消费者中应保留的组合

这张表定位已读冻结源中的问题。它是公式交接，不声称本模块已经替换所有相邻消费者；
root/JVP/retraction/core 的另名实现由数值侧负责。

| 冻结源/部位 | 会坏掉的中间量 | 同一实数公式的稳定入口 |
| --- | --- | --- |
| `general_root_tail_momentum.mjs` geometry/root/init | `w2>0` gate、μ/W、W/μ | w>0 与 logw 保留，§2 的合并因子 |
| 同文件及 `f6tail_fast_momentum.mjs` analytic JVP | `pref * targetFac`、`pref * pFac`，最后乘很大的 dL | §2 的准确组合及 B·Dbar 方程 |
| `f6tail_momentum_split_flux.mjs` | W(K²+EP²) 与分离 pref | 先 wK/wP，再完整 log pref；完整 flux 返回给二 jet |
| `f6tail_momentum_physical_jets.mjs` | target×抵消后的 π_dot、(Q_dot+…) /w | §3、§4 的准确导数 |
| `f6tail_compact_dn.mjs` audit | physical Darboux×…/W 的 0/0 | 直接 `normalizedDarboux` |
| 同文件 cutJets、relative spatial jets | `w*(k+Ldot)/r_x`、`2Wk/r_x` | 合并 w/r_x，E_r=2w w_r |
| `f6tail_relative_development.mjs` | 先丢失物理 Darboux 再重缩放 | 从 D_norm 直接合并 W/r_x 和所需几何因子 |

例如第 m 模高度 H_m=r⁴Q_m 的准确第二径向导数可化为

\[
 H_{m,rr}=m^2(m^2-1)r^2Q_m
 +\sqrt2m^2\frac wr L_m
 +\sqrt2\frac w{r_x}(\dot L_m+kL_m),
\]

而 mean correction 的二阶导数为
`(w/r_x)*(Ldot0+k*L0)`。这些式子避免一个未除 r_x 的中间分子先下溢。
如果某个状态本身已经不可表示，单凭重排不能恢复它；本次实际最深局部输入仍在可表示范围。

## 7. 实际已完成的检查及边界

本模块源 SHA256：
`c1edc34d514d661b9282a9715b603ed4d436acf3708244a11c455be999b6a5d3`。
冻结 root、legacy raw 和物理 jet 源的准确 SHA 由独立点检查报告逐项绑定。

`fd2d-metric-deep-physical-jet-point-check.mjs` 是普通重叠区的可复现入口。
其实际 `point-check-02` 自然 exit 0，仅求一次有限点 root：所有旧二 jet/height/Ldot
在普通分支与冻结源逐项差精确为零；强制 deep 重排同一点后，最大 h_rr 差为
`1.1102230246251565e−15`，Ldot 差为 `5.421010862427522e−20`。
早先 stdin 点检查 `point-check-01` 原样保留；新入口的固定因子/求和顺序在 deep
重叠区最后几位可能不同，未覆盖或改写旧记录。

数值侧另外已真实连接**准确新 profile 的最深点**，见
`2026-11-12-fd2d-numerical-gc-deep-arithmetic-check-02.json` 及其 completion receipt
（session57472，true exit0，4.34s）。其 raw 是 checker v2 明确给出的局部小向量，
不是求解所得的完整 DN 状态。实际 r_x=`5.836462807474886e−76`、
μ=`1.3088461770207387e−137`、W 的浮点值为零，所有 root/RHS/Jacobian/物理 jets
和 Ldot 均 finite；minA=`.9971725728747538`，normalized Darboux 上的有限角诊断
为 `3.6148474078500437e−88`。64 个最终物理 Darboux 下溢均如实计数。

该检查还把同一局部算术抬到普通可表示的 w/μ 比例作独立比较，root 绝对差
`1.1362438767648086e−16`、Jacobian 绝对差 `2.204051907791789e−38`、
Ldot 绝对差 `6.519889758598543e−91`；近零高模的相对差并不小，报告完整保留。
这个抬升仅用于算术诊断，未作为新物理 g、未替代实际全尾求解。

因此本文件解决的是实际深尾中间量的可计算性以及二 jet 的正确公式交接。
全尾 DN、完整切口匹配、连续后验和强闭面仍以各自的实际输出为准。
