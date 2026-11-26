# 新高角模的同场对数因子与13个完整 jet

日期：2026-11-26。实现纸证；不增加新的低模科学重复，不授数值传播证书。

本接口仅供后继真正新增的18/20/22等角模使用。
准确内尾存在范围是 [R600](../results/R600-same-mild-tail-flat-kernels-through-thirty-two.md)；
同一 $y$-方程、DtN末条件、有限 $M$、外传分段及核心匹配均不因此改变。
旧已付2至16模仍按已冻结口数据和必要的同场 dense 重建继续。

## 1. 原显式幂不能作为高模中间量

原 helper 先形成 $r^\mu y$ 再乘外部对数显示尺度，$\mu=j^2$。
在共同内口 $r<.222<1/4$，$j=24$ 已有
$r^{576}<2^{-1152}$，小于 binary64 的最小正次正规数 $2^{-1074}$。
若先舍成0，再加对数尺度不能恢复同一个非零场。
$j=22$ 亦至少进入次正规区：$r^2<1/20$、
$20^4>2^{17}$ 给 $r^{484}<2^{-1028.5}<2^{-1022}$。
这些是格式与整数不等式的纸证，不是一次旧科学重跑。

## 2. 共同因子抽出后，导数仍是原场的导数

保持 $F=r^\mu y$。帽变量 $u$ 下的状态为 $(y,z)$，原完整方程给
$$
y_u=\varepsilon z,\quad
y_{uu}=-g y_u-\varepsilon y,\quad
y_{uuu}=-g' y_u-g y_{uu}-\varepsilon(\log\varepsilon)'y-\varepsilon y_u .
$$
同原 $u=\ell/(r-r_c)$，
$$
u_r=-u^2/\ell,\quad u_{rr}=2u^3/\ell^2,\quad u_{rrr}=-6u^4/\ell^3.
$$
按链式定义 $y_r,y_{rr},y_{rrr}$，再定义
$$
\begin{aligned}
\widehat F&=y,\\
\widehat F_r&=\mu y/r+y_r,\\
\widehat F_{rr}&=\mu(\mu-1)y/r^2+2\mu y_r/r+y_{rr},\\
\widehat F_{rrr}&=\mu(\mu-1)(\mu-2)y/r^3+
3\mu(\mu-1)y_r/r^2+3\mu y_{rr}/r+y_{rrr}.
\end{aligned}
$$
这里下标表示“原导数除以共同 $r^\mu$”，
**不是** 对帽号函数直接求导；准确有
$F^{(k)}=r^\mu\widehat F_{r^k}$。

对同一个线性模，原 $A=W(\mu F-rF_r)/(\mu-1)$、$A_r=WF_r$ 给
$$
\widehat A=-\frac{Wr\,y_r}{\mu-1},\qquad
\widehat A_r=W\widehat F_r,\qquad
\widehat A_{rr}=W_r\widehat F_r+W\widehat F_{rr}.
$$
第一式直接消掉两个 $\mu y$ 项，不先形成相减的大数。

原单位切向场的两个分量为 $U=(\mu-1)A/(jr)$、$V=-jF/r$。
其全部二 jets 同样写成
$$
\begin{aligned}
\widehat U&=\frac{\mu-1}{j}\frac{\widehat A}{r},\\
\widehat U_r&=\frac{\mu-1}{j}
 \left(\frac{\widehat A_r}{r}-\frac{\widehat A}{r^2}\right),\\
\widehat U_{rr}&=\frac{\mu-1}{j}
 \left(\frac{\widehat A_{rr}}r-\frac{2\widehat A_r}{r^2}
                         +\frac{2\widehat A}{r^3}\right),\\
\widehat V&=-j\widehat F/r,\\
\widehat V_r&=-j(\widehat F_r/r-\widehat F/r^2),\\
\widehat V_{rr}&=-j(\widehat F_{rr}/r-2\widehat F_r/r^2+2\widehat F/r^3).
\end{aligned}
$$
13个量依次为 $F,F_r,F_{rr},F_{rrr},A,A_r,A_{rr},U,U_r,U_{rr},V,V_r,V_{rr}$；
每个原量都等于对应帽号量乘 **同一个** $r^\mu$。

## 3. 显示尺度和外口归一的准确身份

若某 dense cell 的原累计对数幅为 $L$、固定显示尺度为 $D$，
则每个完整输出为
$$
J_k=\operatorname{sgn}(\widehat J_k)
 \exp\{\log|\widehat J_k|+L+\mu\log r-D\}.
$$
零帽号分量继续给0；不能先形成 $r^\mu$。
外口的同一正 Cauchy 归一为
$$
D=L+\mu\log r_0+
 \log\operatorname{hypot}(\widehat F(r_0),(.08)\widehat F_r(r_0)).
$$
所以这只是原 $D=L+\log\operatorname{hypot}(F,.08F_r)$ 的准确重写。
核心 $A$ 归一仍由原完整外传/核心方程计算，不从帽号尺度另造一个核心值。

本次声明只为新模构造这份 helper，不替换已付低模的 evaluator，
不增加旧低模 baseline/parity/directional gate。
其在新 run 的实际次数、inner/outer RHS、13外口与 core匹配误差全部照录。
浮点下溢若发生在最终正确的极小物理量上，也不能因此声称它在准确模型中恒零；
准确无限尾、有限DtN误差和ODE误差仍按原范围分别结算。
