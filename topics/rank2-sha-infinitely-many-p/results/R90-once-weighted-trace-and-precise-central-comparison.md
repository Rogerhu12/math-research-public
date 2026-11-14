# R90：一次权域迹的准确格、有限输入与中央比较

日期：2026-11-12。状态：全文独审及精确有限环脚本根端复跑通过。
证明见[一次权迹与中央 jet](../notes/2026-11-12-once-weighted-canonical-trace-and-central-jet.md)，
算术证书见[复算脚本](../scripts/check-canonical-neighbor-primitive-traces.py)。

令 $d=p+1$，$L_p=B(\varpi)$、$\varpi^d=p$，$r$ 为实际 $K$ 根，
$S_p=\operatorname{Tr}_{L_p/B}(I(r)/L(r))$。
实际微分权迹为 $b^{-1}S_p$，$b$ 为既定晶体单位。

## 1. 迹对偶保留全部高阶项

准确的迹理想是

$$
\operatorname{Tr}_{L_p/B}(\varpi^j\mathcal O_{L_p})
=p^{\lceil j/d\rceil}\mathcal O_B.
$$

R89 给 $I(r)/L(r)\in\varpi^2\mathcal O_{L_p}$，所以 $S_p\in p\mathcal O_B$。
若 $P_p(T)$ 是 $r$ 的 Eisenstein 最小多项式，则

$$
\operatorname{Tr}F(r)
=[T^{d-1}]\operatorname{rem}_{P_p}(P_p'F),
$$

且

$$
S_p=\sum_{K(r)=0}\operatorname{Res}_r\frac{IK'}{LK}\,dt
=-\sum_{K(r)=0}\operatorname{Res}_r\frac{Is(K')^2}{K}\,dt.
$$

两被积式之差在整个闭盘解析。中央量却是另一个指定留数

$$
\Gamma_{i,p}=C_d/p
=\frac1p\operatorname{Res}_{t=0}\frac{M_eK^d}{sL^{d+1}}\,dt.
$$

前者的极点为 $K=0$，后者为 $L=0$；不能自动等同。

## 2. 任意精度的实际有限算法

对 $q=1,3$、$F_q=I/L^q$，完整周期和积分界给

$$
v_p([t^n]F_q)+n/d
\ge\frac nd\left(\frac34-\frac1p\right)-1
\qquad(n\ge8d).
$$

故模 $p^N$ 只需次数小于 $B_N=2d\max(N+1,4)$。
$K$ 有同样足够的尾界；缩放根的导数为单位，
有限环 Newton 求根后取 $d$ 倍 $\varpi^0$ 坐标准确给完整域迹。
脚本从原整数 theta 流生成全部输入，根端复算得到

| $p$ | $\Gamma_{i,p}\bmod p$ | $S_p\bmod p^3$ | $S_p/p\bmod p$ | $\operatorname{Tr}(I/L^3)\bmod p^3$ |
|---:|---:|---:|---:|---:|
| 7 | 2 | 84 | 5 | 325 |
| 11 | 9 | 429 | 6 | 771 |

## 3. 指定中央 jet 不能代替整个迹行

扰动 $\Delta M=t^{p+3}$ 保留实际首项、整性及 $\Gamma_{i,p}$，
但同一完整算法给

$$
\operatorname{Tr}(\Delta I/L)/p
\equiv3\pmod7,\qquad\equiv4\pmod{11}.
$$

所以仅凭周期方程、邻点几何、首项及已证整性，
不能声称一次权迹只由中央 jet 决定。
这个扰动未保留原实际 Hecke 特征，因而不排除利用该额外约束的精细比较。
后续应构造能准确提取中央行的迹权或 Hermite 导数数据。
