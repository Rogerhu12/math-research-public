# R149 GSR：selected 的两列真实有符号普通源与全格 hybrid 响应

**已证明下述恒等式、包含及有向计算合同。尚无两列响应的实际数值。** 固定 [TC](R149-supplement-true-root-continuous-PDE-trials-and-complete-residuals.md) 的 $Q_0=(u,v)$、$Z=(a,b)$、$Q_\delta=Q_0+\delta Z$、$\nu_\delta=\nu_0+\delta$ 与同一个 $\delta_*$。在 $[r_*,25/8]$，compact 控制严格为零，$\beta,K,\gamma$ 及 rotational $s$ 都取原同一 complete intrinsic row。下文的 $m=\Pi v$、$n=\Pi b$ 是完整场与方向的均值。

## 同时形成全部 577 行

对 affine 参数定义
$$
 S_0=u^2+Kv^2,\qquad S_1=2(ua+Kvb),\qquad S_2=a^2+Kb^2,\qquad d_k=-\beta I S_k ,
$$
其中 $I=\partial_\phi^{-1}(1-\Pi)$，$J=\begin{pmatrix}0&K\\-1&0\end{pmatrix}$，$E=\mathrm{diag}(-1,1)$。完整 moving vector field 为
$$
 \mathcal F(Q)=d_0 Q_\phi+\gamma m JQ_\phi +\beta EQ-\beta S_0Q.
$$
直接逐幂展开 $\mathcal F(Q_\delta)-(Q_\delta)_r=T_0+\delta T_1+\delta^2T_2+\delta^3T_3$ 得
$$
\begin{aligned}
T_0&=\mathcal F(Q_0)-(Q_0)_r,\\
T_1&=d_0Z_\phi+d_1(Q_0)_\phi+\gamma J(mZ_\phi+n(Q_0)_\phi)+\beta EZ-\beta(S_0Z+S_1Q_0)-Z_r,\\
T_2&=d_2(Q_0)_\phi+d_1Z_\phi+\gamma n JZ_\phi-\beta(S_1Z+S_2Q_0),\\
T_3&=d_2 Z_\phi-\beta S_2Z .
\end{aligned}
$$
因此 **Newton 普通源** 为 $-f_\delta=T_0+\delta(T_1+\delta(T_2+\delta T_3))$，**$\nu$ proposal defect** 为 $s_\delta=T_1+\delta(2T_2+3\delta T_3)$。第二式由对同一参数求导得到，具有其真正的 $-Z_r$ 符号。它供计算 $q_\nu-Z$ 使用；未知 $q_\nu$ 的边界数据仍须在物理边界上减去 $Z$ 的对应数据。

为避免把 rotational residual 作为两个无关宽区间相减，令 $w=v-s$。由同一 rotational 解 $s'=\beta s(1-Ks^2)$，反应第二行减去 $s'$ 精确等于 $\beta[w-u^2v-Kw(v^2+vs+s^2)]$。故只需对原 signed cubic $w$ 本身求 $w_r$。原 6144 段 base65 整体乘 $\alpha$ 一次，direction193 本身是 physical，均使用原完整连续 repair 的逐 piece signed offsets；不得用 offset sup 代值。两端连续使分片常数修补的径向分布导无 Dirac。程序在全部原 scalar 行与 cubic 相交的每片上采用原 signed Fourier/radial arithmetic。三次角积至多 $|j|=288$，完整 1024 点无混叠。对归一化 $\sqrt2\sin4j\phi,\sqrt2\cos4j\phi,1$，两 signed 非零频行是 $-\sqrt2\Im\widehat x_j$ 和 $\sqrt2\Re\widehat y_j$；独立 mean 是 $\Re\widehat y_0$。原余项在取每个系数时仍以完整 Wiener 误差包围。全部 $288+1+288=577$ 行两列先形成，最后才取原 low193；其余行供 full high correction。程序用原完整 $|\delta_*|$ 区间而非中心取值。

## 已恢复同一个 GG model 时的双列求解

设原 GG 全矩阵与 frame 定义来自同一工作内的私有模型，或在另一个工作中按完整 whole identity 成功恢复。源计算的 `source_roles=()`，不调用四个已付 source-map 的 covariance 或 trace。给两列完整初端 $l_{96}$、外端 charted $r_{97}$；先把 $r$ 的96个非均值分量各除 $\Theta_j$，mean 不缩放。以 $\widetilde r$ 记还原后的原 Robin 加独立 mean。设 $d_i$ 是原格 $i$ 起点零值的完整物理强迫递增量。用 GG 的节点基与双基 $L,R,\ell,\rho$ 写 $x_i=L_i a_i+R_i b_i$。边界给
$$
 b_0=(B_aR_0)^{-1}l_{96},\qquad a_N=(B_bL_N)^{-1}\widetilde r_{97}.
$$
上述有向逆还须实际验证。对 $i=N-1,\ldots,0$ 和 $i=0,\ldots,N-1$，分别解
$$
 a_i=C_i(a_{i+1}-\ell_{i+1}d_i),\qquad
 b_{i+1}=D_i b_i+\rho_{i+1}d_i .
$$
理由为 $F_iL_i=L_{i+1}C_i^{-1}$、$F_iR_i=R_{i+1}D_i$ 及 $x_{i+1}=F_ix_i+d_i$。两方向是同一有向等式在真实共同系数上的包含。命题并未把两个源范数当作有符号列，也未把边界自由输入设成零。

对每个子盒，$A,f$ 是其整盒全部系数、两列源，$h$ 是完整真正时长，$X$ 是左端两列实际状态。令
$$
 t_1=h(AX+f),\qquad t_{k+1}=hAt_k/(k+1).
$$
所有后续 $A$ 可取不同时刻的真实值：迭代积分的第 $k$ 阶有序单纯形体积为 $h^k/k!$，区间矩阵乘积允许各时刻独立。端点用 $X+\sum_{k=1}^{16}t_k$；全盒状态用 $X+\sum_{k=1}^{16}[0,1]t_k$。令 $\beta=\|hA\|_\infty^+$，两者同一剩余每个条目都不超过
$$
 \frac{\|t_1\|_\infty^+\beta^{16}}{17!}\frac1{1-\beta/18}
$$
（实际分母严格大于零）。若某盒有向分母未过，先二分该未积分盒，最细仍不通过即如实失败。首项 $AX+f$ 在同一最内积分时刻组成，保留其符号抵消；证明不需 $f_r$。先以 $X=0$ 得完整 $d_i$，求解节点后以真正 $X=x_i$ 得全格真实状态。内部 balance 在两端精确换回，不代替物理 $S$ 或 NGA 的 $P$。

把 $17/20,9/10,19/20$ 插在其真实固定物理格内。在 $9/10$ 读 raw 193 条 signed endpoint，按原正交归一化求各列 $L^2_\phi$。在整个 $[17/20,19/20]$ 按相邻无隙全盒遍历，原 $P=\operatorname{diag}(K^{-1/4},K^{1/4})$ 作用一次。因此普通 $dr$ 的非负积分上界是各格 $h^+$ 乘
$$
 (K^{-1/2})^+\sum_j|x^o_j|^2+(K^{1/2})^+\sum_j|x^e_j|^2 .
$$
low 取所有 $j\le96$ 与独立 mean；shell 只取 $33\le j\le96$。反射强迫子空间中 odd mean 为结构零，even mean 明确保留。最后按列开方。两个观测是同一全格解的真实接收量，但当前对象仍是 $G_c$：全 family 的 $\Delta A_L,\Delta C,G_H$ 返回、物理边界、独立 mean 以及最终非线性 residual-zero 条件必须分别付清，才是 NGA/FWT 的同态 $c_L,Z_L,Z_S$。

源码为 `fourfold_codazzi_selected_positive_signed_sources.py` 和 `fourfold_codazzi_grassmann_signed_response.py`。数值执行还需真正恢复全 GG 模型、原 40-part/7721 行及完整 base/direction 载体，并指定来自同一完整问题的两列 $l,r$。未声称已有全负窗 ordinary $\|q_\nu-Z\|\le1/200$。
