# R144 实际场读取与冻结参考的解析二阶角导数

本文件闭存 R144 新 lifting 的独立原生消费者。它消费真实保存的 P1/Fourier correction、明确的 `coast_reference_definition` 和原有物理 bump 参数，不重求 BVP，也不把新初场视为已合格曲面。

## 1. 对象与身份

新入口为

```python
from fd2d_gc_bump_coast_native_field import RawBumpCoastNativeField

field = RawBumpCoastNativeField(
    actual_field_npz, actual_base_candidate_json,
    reference_inlet=actual_R139_inlet_npz,
    reference_cache=closed_first_jet_cache_npz,
)
jet = field.evaluate_native(physical_s, computational_xi)
physical = field.physical(physical_s, material_u)
```

它沿用原生接口的 `n,m,l`、`_x`、`_xi`、`_xixi`、`_x_xi`，以及 `physical` 的 `_s`、`_u`、`_uu`。`x=s` 是保存的真实物理坐标；在保存节点处 `side` 只选择 P1 的左右径向导数，值及角导数保持共同迹。

消费者要求 NPZ 或调用参数明确保存 `coast_reference_definition`。它逐项核对 reference binding、candidate SHA、支撑、rim fraction、权重公式、lifting 公式及冻结参数声明。它还核对 reference 与当前字段的同一 moments/means 身份。不得按文件名猜测新 lifting，不得把新 correction 交给只知道旧 seed plateau 的 reader。

当前 R139 第一 jet 缓存的静态 binding 为

```
5a0fbc11024e0b73e2956e29520334418c4da357bfc854fa9969deb7cd15cfce
```

缓存计数与绝对路径不是数学身份。新 reader 的定义文件另外绑定真实入口、可选缓存和全部源 SHA，因而无需改写活动求解器保存的 NPZ。第一 jet 缓存、`SavedNativeCoast`、旧 readers 以及活动 solver 源均保持原字节。

## 2. 准确的新有限场

设实际保存 correction 为 $C=P_1(y_j)(s)$ 的有限 Fourier 展开，旧完整 lifting 为 $L$，R139 冻结参考为 $R(s,u)$。权重是 R144 的

$$
w(s)=S_5((s-c)/r)S_5((c+L_c-s)/r),\qquad r=.12L_c,
$$

其中 $S_5$ 在单位区间外截断延拓。新实际字段的定义是

$$
f=C+(1-w)L+wR(s,U(s,\xi)). \tag{1}
$$

**读取时不再给 $C$ 乘 $(1-w)$。** 主求解器选择新初猜时已经按 R144 对节点 correction 作过一次明确变换；之后保存的这些新系数就是新的 P1 定义。在节点之间也不以 $(1-w)P_1(y_j)$ 替代所存 P1 函数。

实现用一个只含零 correction 的轻量只读视图求旧 $L$，然后单独加入真实 $C$；这不生成或保存任何伪造的零场。所有保存节点、原系数和参数数组均不变。

若 $\widetilde R=R(s,U(s,\xi))$，则

$$
\begin{aligned}
f_s&=C_s+(1-w)L_s+w\widetilde R_s+w'(\widetilde R-L),\\
f_\xi&=C_\xi+(1-w)L_\xi+w\widetilde R_\xi,\\
f_{\xi\xi}&=C_{\xi\xi}+(1-w)L_{\xi\xi}+w\widetilde R_{\xi\xi},\\
f_{s\xi}&=C_{s\xi}+(1-w)L_{s\xi}+w\widetilde R_{s\xi}
              +w'(\widetilde R_\xi-L_\xi).
\end{aligned} \tag{2}
$$

这里没有使用当前未知三场的 Gauss 消元；实际 $l$ 始终独立。

## 3. 冻结入口的三阶材料导数

R139 入口的 $n_c,m_c$ 是明确保存的有限 cosine/sine 函数，计算角为固定 seed 法向角 $\phi$。其材料角 $t$ 满足

$$
h=\frac{dt}{d\phi}=\frac{\rho_*(\phi)}{a_0}>0.
$$

记 $f_j=\partial_\phi^j f$，则逐次使用 $\partial_t=h^{-1}\partial_\phi$ 得到

$$
\begin{aligned}
f_t&=f_1/h,\\
f_{tt}&=f_2/h^2-f_1h_\phi/h^3,\\
f_{ttt}&=f_3/h^3-3f_2h_\phi/h^4-f_1h_{\phi\phi}/h^4
                       +3f_1h_\phi^2/h^5.
\end{aligned} \tag{3}
$$

有限 Fourier 函数的前三阶 $f_j$ 直接求和。$h,h_\phi,h_{\phi\phi}$ 由原准确 moment 定义的 seed radius 及其解析导数给出，没有把离散 DFT 或有限差分当成导数定义。

令 $k=m_c/n_c$。由 $n_ck=m_c$ 逐阶求导，得到

$$
\begin{aligned}
k_t&=(m_{c,t}-n_{c,t}k)/n_c,\\
k_{tt}&=(m_{c,tt}-n_{c,tt}k-2n_{c,t}k_t)/n_c,\\
k_{ttt}&=(m_{c,ttt}-n_{c,ttt}k-3n_{c,tt}k_t-3n_{c,t}k_{tt})/n_c.
\end{aligned} \tag{4}
$$

这里除的是 R139 已证明严格正的**冻结入口** $n_c$，并没有要求未知 raw $n$ 为正。

## 4. 固定 coast 的解析二阶 $u$ 导数

固定 $\sigma=s-c$，设 $r_0=a_c/v$、$r=r_0+\sigma$、$\Delta=\sigma(2r_0+\sigma)$。R139 的准确函数为

$$
Q=\sqrt{r_0^2+(1+k^2)\Delta},\quad
w_0=\frac{\Delta}{r_0+Q},\quad
B=v(1+k^2)-k_t,\quad D=a_c+w_0B.
$$

此处 $w_0$ 是 ruling 参数，不是 (1) 的支撑权重。对入口材料角 $t$ 求导：

$$
\begin{aligned}
Q_t&=\Delta k k_t/Q,\\
Q_{tt}&=\Delta(k_t^2+k k_{tt})/Q-\Delta^2k^2k_t^2/Q^3,\\
(w_0)_t&=-\Delta Q_t/(r_0+Q)^2,\\
(w_0)_{tt}&=-\Delta Q_{tt}/(r_0+Q)^2+2\Delta Q_t^2/(r_0+Q)^3,\\
B_t&=2vkk_t-k_{tt},\qquad
B_{tt}=2v(k_t^2+kk_{tt})-k_{ttt},\\
D_t&=(w_0)_tB+w_0B_t,\\
D_{tt}&=(w_0)_{tt}B+2(w_0)_tB_t+w_0B_{tt}.
\end{aligned} \tag{5}
$$

再令

$$
n=\frac{a_cn_cQ^2}{Dr^2},\qquad q=kr_0/Q,\qquad m=nq,\qquad l=nq^2.
$$

用 $\partial_t\log n=n_{c,t}/n_c+2Q_t/Q-D_t/D$ 及其真导数计算 $n_t,n_{tt}$；对 $q,m,l$ 使用乘除法即可得到其真一、二阶导数。计算中没有除以可能为零的 $k,m,q$。

R139 的新材料角映射满足

$$
U_t=\frac{D}{vQ}>0,\qquad
U_{tt}=U_t\left(\frac{D_t}{D}-\frac{Q_t}{Q}\right).
$$

因此对于上述任一分量 $f$，准确有

$$
f_{uu}=\frac{f_{tt}U_t-f_tU_{tt}}{U_t^3}. \tag{6}
$$

新 helper 用 (3)–(6) 提供 `physical_uu`。材料逆映射仍使用原 `SavedNativeCoast` 的明确容差；这个浮点实现不是区间证书。原 value、$s$/$u$ 一 jet 保留原计算路径，其与 (5) 新公式的差单独记录。

## 5. 混合导数与旧计算角链式法则

在原冻结 base coast 上，令 $a=a_c+v\sigma$、$c_0=v/a$。R139 的准确 Codazzi 方程为

$$
n_s=m_u/a+c_0(l-n),\qquad m_s=l_u/a-2c_0m.
$$

因 $a,c_0$ 不依赖 $u$，可直接微分得到

$$
n_{su}=m_{uu}/a+c_0(l_u-n_u),\qquad
m_{su}=l_{uu}/a-2c_0m_u. \tag{7}
$$

对冻结参考的 $q=m/n$，有

$$
l_s=2qm_s-q^2n_s,\qquad
l_{su}=2q_um_s+2qm_{su}-2qq_un_s-q^2n_{su}. \tag{8}
$$

(7)–(8) 只用于冻结参考，绝不用于强迫当前未知字段满足方程；当前物理 bump 目标的完整缺陷仍用其实际 $a,a',a''$ 计算。

最后回到实际保存的固定计算角 $u=U(s,\xi)$：

$$
\begin{aligned}
\widetilde R_s&=R_s+U_sR_u,\qquad
\widetilde R_\xi=U_\xi R_u,\\
\widetilde R_{\xi\xi}&=U_\xi^2R_{uu}+U_{\xi\xi}R_u,\\
\widetilde R_{s\xi}&=U_\xi R_{su}+U_sU_\xi R_{uu}+U_{s\xi}R_u.
\end{aligned} \tag{9}
$$

(9) 与 (2) 是消费者返回全部 jets 的公式。

## 6. 连续性与实际位置定义

保存的 correction 在每个径向节点具有共同的值和全部角导数。冻结参考在其已证明 $D>0,n>0$ 的紧 coast 上光滑；权重在支撑端点满足 $w=w'=w''=0$。所以 (1) 的三场及其所需角导数连续。径向一导数可在 P1 节点跳变，由 `side` 明确选择，逐 cell 消费 Codazzi。

R119/R124 按固定材料 $u$ 解

$$
F_s=FA(l,m),\qquad X_s=Fe_1.
$$

由于 $l,m$ 连续，$F$ 为 $C^1$，$X$ 有连续径向二导数；连续角 jets 给相应混合导数与 $X_{uu}$。因此该原生定义适配原 $C^2$ 位置图的后处理，不要求 raw II 的全局径向一导数共同迹，更不增加 $C^3$ 门槛。实际曲率仍必须从所定义位置的 Gram、法向和两 jet 计算，不能直接把三场当成已验证的实际第二基本形式。

## 7. 真实小核，完整保存原输入

实际命令见 `fd2d-metric-coast-native-jet-check.py`。输入为已闭不可变

```
2026-11-12-fd2d-raw-bump-coast09-b0001-initial.npz
SHA256 897ecba1f6eaf69252c12236cffae324058b3aeec5fdee817000245224ba3b56
```

它有 122 个原保存节点。核验用此前真实预填的两个 Gauss2 点：

| $s$ | 支撑权重 | 角点数 |
|---|---:|---:|
| 0.600318454492792 | 0.1051860914737172 | 8 |
| 0.6396818037931371 | 1 | 8 |

工具 session `72016`、完成 chunk `f19b24`，**实际 exit 0**；3.74777 秒，峰 RSS 76024 KiB。结果为：

- 新值、$s$ 和 $\xi$ 一 jet 对原第一 jet 参考公式，最大差准确为浮点 0。
- 对解析 $s,\xi,\xi\xi,s\xi$ 导数，用 $h=2\times10^{-5}$ 和 $h/2$ 做有限差分；细步最大 scaled error 为 $2.732170413237047\times10^{-7}$，所有八组误差随半步约缩至四分之一。
- 支撑外及两个准确支撑端点，对旧完整场的五 jet 最大差 $1.4210854715202004\times10^{-14}$，来自明确不同的浮点加法次序。
- 写入定义文件并重新加载后，两个点的全部五 jet 逐项差为浮点 0。
- 冻结参考材料逆残差最大 $5.1993565702845856\times10^{-14}$；新的第一 $u$ 导公式与原路径最大差 $6.303985111699717\times10^{-15}$。
- 输入 NPZ 与所有源字节未变；未求 BVP、未构造大矩阵、未积分 body。

报告为 `2026-11-12-fd2d-metric-coast-native-jet-check-01-report.json`，SHA256

```
02131ba47f7838893d2de3801cbf095ee4d98eb3943a1db3bd227df740da385f
```

这是实际原生读取和解析导数的小范围核验。它不证明主态收敛、全域残差、全局位置闭合、reach 或强比例；这些仍由本课题的完整后续证据支付。
