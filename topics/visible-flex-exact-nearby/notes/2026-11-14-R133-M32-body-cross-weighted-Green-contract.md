# R133：固定 repaired M32 主体的双向边缘频带费用与既成 $L^2$ 核消费合同

## C.1 对象和唯一范围

本合同的系数是 ac1 原候选的同一连续 M32 修补，中心定义 SHA256 为
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47，
固定物理 $\eta_0$ 和原始 $\nu$，参数方向偏移 $\delta=0$。它不是 M96 非零 $\delta$ 家族的转移合同。

令 $Q=(u,v)^T$，$m=\langle v\rangle$，$W=(u,Kv)^T$，
$S=u^2+Kv^2$，$J_K=\left(\begin{smallmatrix}0&K\\-1&0\end{smallmatrix}\right)$。
Fourier 指数为 $e^{4ij\phi}$，$I=\partial_\phi^{-1}P_{\ne0}$。
真实 moving Jacobi 径向生成元为

$$
Ah=d\,\partial_\phi h+\gamma mJ_K\partial_\phi h
+\{\beta\operatorname{diag}(-1,1)-\beta[S\,1_2+2QW^T]\}h
-2\beta Q_\phi I(W^Th)+\gamma\langle h_2\rangle J_KQ_\phi,
\qquad d=-\beta IS. \tag{C.1}
$$

主体方程为 $\partial_r h-Ah=f$。圆周测度归一化；真实 odd/even 反射类和 even mean 保留。

## C.2 跨频率项的准确支撑

设 $P_L=P_{|j|\le96}$，$P_H=1-P_L$，
$E=P_{33\le|j|\le96}$，$F=P_{97\le|j|\le160}$。在 M32 背景上，

$$
P_HAP_L=F A E,\qquad P_LAP_H=E A F. \tag{C.2}
$$

每个乘法路径的总角频带最多为 64；$I$ 不扩大支撑。
$\gamma mJ_K\partial_\phi$ 与 $\beta\operatorname{diag}(-1,1)$ 都按频率对角，不产生两个投影之间的反馈。
独立 mean rank 对高输入为零，其输出支撑最多 32，亦无跨频率输出；这只说明该项的两个交叉块为零，不删除低方程中的 mean。

式 (C.2) 最初在光滑有限 Fourier 和上成立，随后由下述有界估计延拓到普通 $L^2$。因此不对未知无限高输入假设额外角导正则性。$E,F$ 各有 128 个真实正交反射槽。

primitive 的两向路径都可以准确插入 $P_{|\ell|\ge65}$。从高向低时，输入 $|j|\ge97$ 先乘 M32 的 $W$ 后仍有 $|\ell|\ge65$；从低向高时，最后的 $P_HM_{Q_\phi}$ 只可能看见 $|\ell|\ge65$。故两向都使用

$$
\|I P_{|\ell|\ge65}\|_{L^2\to L^2}\le\frac1{260}. \tag{C.3}
$$

这一步不把低向高时完整中间乘积的低频分量误当消失；它只在准确输出投影后插入该投影。

## C.3 去除常角 mean 的零交叉项

在每个原闭径向格上，已有
$B\ge|\beta|$，$K_*\ge\max(1,|K|)$，
$Q_0\ge\|Q\|_{A_0}$，$Q_1\ge\|Q_\phi\|_{A_0}$。
另令 $Q=m e_2+w$，取 $q\ge\|w\|_{A_0}$。完整 pair Wiener 范数支配乘法的 Euclidean $L^2$ 范数。

常角矩阵 $Km^2\,1_2$ 与 $Km^2e_2e_2^T$ 均与投影对易，故可以仅在交叉块中去除。余项满足

$$
\|S-Km^2\|_{A_0}\le K_*(2|m|q+q^2),\qquad
\|QW^T-Km^2e_2e_2^T\|_{A_0}
\le K_*(2|m|q+q^2). \tag{C.4}
$$

因为 $|m|\le Q_0$，并且不减去常角项时原 $Q_0^2$ 估计也合法，可使用

$$
D=\min\{Q_0^2,\;2Q_0q+q^2\}. \tag{C.5}
$$

这里的 $q$ 来自原候选 cubic 的精确 Fourier 遮罩：仅把第 32 个零起始 even mean 槽置零，保持 odd 槽 0–31 和 even 非零槽 33–64。对整格作原 Bernstein 包络，乘精确物理 $\alpha=6890507429876859/9007199254740992$，再加原全局 centre repair $E_0$。本构造不以两个独立上界相减估计 nonmean，也不从完整低方程中删掉修补的 mean。原 intrinsic $s$ 是纯 mean，故在这个 nonmean 遮罩中准确消失。

## C.4 两向 ordinary 源费用

由 (C.1)–(C.5)，高输入的实际频率上限为 $4\cdot160=640$，低输入的上限为 $4\cdot96=384$。drift、完整 local reaction 和 primitive 的费用给出

$$
\|P_LAP_Hh\|_{L^2_\phi}
\le c_{LH}(r)\,\|Fh\|_{L^2_\phi},\quad
c_{LH}=BK_*\left(163D+\frac{Q_0Q_1}{130}\right), \tag{C.6}
$$

$$
\|P_HAP_Lh\|_{L^2_\phi}
\le c_{HL}(r)\,\|Eh\|_{L^2_\phi},\quad
c_{HL}=BK_*\left(99D+\frac{Q_0Q_1}{130}\right). \tag{C.7}
$$

其中 $163=640/4+3$，$99=384/4+3$。primitive 中的完整 $Q$ 仍保留，外导 $Q_\phi$ 的 mean 自动为零，费用 $2/260=1/130$ 没有删除两次卷积中的任何路径。

每个标量上界只应用于其实际闭径向格。完整 $L^2_rL^2_\phi$ 乘法范数可用对应窗口上的最大值；原点到安全固定负窗的右端仍是
$2383968743003/10000000000000$。该端点不转授到非零 $\delta$ 或新非线性背景。

## C.5 原输入与精确缓存

新的数值消费者只读取：

1. 原 candidate index ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413 及原五个分片。
2. 实际已成 known-high native 5ad8aaada967f4626a33e978b1c81adf640ee1abaf0876f54ffd22d6dbd107fd 的 7721 个完整系数行及 centre repair 费用。原数学 run 43628921664 的 child 返回 0、8 门全成；后来的可选诊断大小失败由独立零数学 run 43630093667 的 6 门原字节 receipt 保存。
3. 原 finite193 Green native fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6。
4. 已实际完成的 ordinary $L^2$ 核 native ac4441cb98afabbbc646697434caebf464a22f702e2d0fa7d8e5910efd7ef448，run 43633074696，含全部 6391 个 signed Lyapunov Gram、5970 个接口及 whole-cell 标量积分。

读取并核验实际 artifact 过程与 native 身份。仓库快照和 artifact 过程可以因出版记录不同而有不同 SHA，消费者记录实际读到的字节，不能猜测它们相同。

本次不调用 target，不重算旧 residual、mean flow、帽数组、frame、Riccati、4×4 Gram 或原 scalar exponential。新增数学只有 nonmean cubic 包络、双向标量费用和下述对同一正核的径向加权消费。全部只在公开 Actions 执行。

## C.6 用同一已认证 $G_L$ 消费真实径向费用

令 $G_L$ 为原完整有限 193 维主体、96 腰约束、真实低 97 帽约束和独立 mean 的 inverse。我们界定仅主体反馈

$$
\mathcal T_{\mathrm{body}}=G_L(P_LAP_H), \tag{C.8}
$$

其中齐次腰与齐次有限帽边界由同一个 $G_L$ 处理。无论高输入是否还满足某种高方程，(C.6) 都给出普通 $L^2$ 输入估计。新的逐格权重不把无限维帽交叉项并入 (C.8)。

原 transformed 状态为 $\operatorname{diag}(1,\rho)h$。在每个真实连续片，原输入权重
$w_i=\max(1,\rho_{\mathrm{left}},\rho_{\mathrm{right}})$；
用完整相交的 (C.6) 行上界 $c_i$ 后，替换为 $\widetilde w_i=w_i c_i$。
原输出恢复权重 $\max(1,\rho_{\min}^{-1})$ 保留。

设原局部端口上界为 $a_i,b_i,k_i$，原右锥为 $r_i$，原 signed
$A_i=\left(\begin{smallmatrix}\mu_i&c_i^{\,0}\\-e_i&-\nu_i\end{smallmatrix}\right)$。
这里 $c_i^{\,0}$ 是原 comparison coupling，勿与新反馈乘法上界 $c_i$ 混同。
原 Gram

$$
G_i=\int_0^{h_i}e^{tA_i}e^{tA_i^T}\,dt \tag{C.9}
$$

从原 native 原样读取。先对完整 signed 二次型作区间运算，再取上端；不能先把 $G_{12}$ 取独立正上界再乘负系数。

向后独立源支集的平方递推为

$$
Z_{i,L}^2=a_i^2 Z_{i,R}^2+
\widetilde w_i^2a_i^2(r_i,-1)G_i(r_i,-1)^T. \tag{C.10}
$$

无新接口源，因此接口只保留原 sec/tan 放大。初始外端 $Z_R=0$。
腰闭合使用原正 margin，$v_0=D_0/(1-D_0\rho_0)$，$W_0^2=0$。

向前令

$$
v_R=b_iv_La_i+k_i,\quad
W_R^2=b_i^2W_L^2+
\widetilde w_i^2(1+r_iv_R,-v_R)G_i(1+r_iv_R,-v_R)^T. \tag{C.11}
$$

$v$ 与输入权重无关，因此也可以直接使用原已存同一端点的向上包络，不再求解齐次端口。后项仍是同一局部源的相关组合，不将两个项冒称独立。

## C.7 节点、whole-cell 与真实径向积分

节点两行 Gram 仍由 past/future 的真正不相交支集得到

$$
\Gamma_{pp}=W^2+v^2Z^2,\quad
\Gamma_{pq}=\rho W^2+v(1+\rho v)Z^2,\quad
\Gamma_{qq}=\rho^2W^2+(1+\rho v)^2Z^2. \tag{C.12}
$$

whole-cell 使用原完整锥包络 $\rho_i$，原 signed rates 的合法上端
$\lambda_z=\nu+c^0\rho_i$、$\lambda_p=\mu+c^0\rho_i$。
原 native 已存三个完整标量积分的上界 $\widehat I_{2\lambda_z}$、$\widehat I_{\lambda_p}$、$\widehat I_{2\lambda_p}$，
$I_\lambda(h)=\int_0^h e^{\lambda t}dt$。这些记录是积分上界，不能当成包含真积分的双侧球后乘负 $\lambda$。

不重算指数。所需增长因子使用准确的安全不等式

$$
\max(1,e^{\lambda h})\le
1+\max(0,\lambda_{\mathrm{up}})\widehat I_\lambda(h). \tag{C.12a}
$$

当原率 $\lambda\le0$ 时左边就是 1；当 $\lambda\ge0$ 时用
$e^{\lambda h}=1+\lambda I_\lambda(h)$ 和原积分上界。
式中 $\lambda_{\mathrm{up}}$ 包含原同一率，不改变已认证 Gram 中的 signed 生成元。
以下 (C.13)–(C.14) 的积分用对应已存上界，指数增长因子用 (C.12a)。

$$
Z_{\mathrm{whole}}^2
\le\max(1,e^{2\lambda_zh})Z_R^2+
\widetilde w_i^2(1+\rho_i^2)I_{2\lambda_z}, \tag{C.13}
$$

$$
P_{\mathrm{whole}}
\le\max(1,e^{\lambda_ph})P_L+
c^0I_{\lambda_p}Z_{\mathrm{whole}}+
\widetilde w_i\sqrt{I_{2\lambda_p}},\qquad
Q_{\mathrm{whole}}\le\rho_iP_{\mathrm{whole}}+Z_{\mathrm{whole}}. \tag{C.14}
$$

(C.13) 的 future/local 支集按平方相加；(C.14) 只作一次合法 Minkowski，因为 $P_L$ 已可能依赖当前格的源。最后按原物理恢复权重和真实 $dr$ 积分，给出 (C.8) 到全主体或固定负窗的普通 $L^2$，以及完整 $C^0_rL^2_\phi$ 上界。全部 6391 连续片、5970 接口、腰 $0^-$ 虚接口和两端原边界单位列均完整绑定。固定负窗端点必须仍是原显式分割点。

## C.8 完成与不转授事项

实际新 native 保存所有 7721 双向费用行、原行 SHA、完整新的加权前后扫及断点恢复前缀。每个已成功 prefix 只在完全相同的输入、源码、行序和覆盖身份下复用。成功数学与后续出版失败分开，不能因可选摘要失败而重新执行已成行。

本次可授 (C.6)、(C.7) 及仅主体 (C.8) 的实际常数。它不授完整无限维 inverse，不授高 BVP $G_H$，不授
$I-G_LT_{LH}G_HT_{HL}$ 可逆，也不把正区 given-head 图当成负区 high inverse。
真实帽 DN 的完整低高交叉、未知 high 输入、完整 source/mean/边界列及非零 $\delta$ 背景转移仍是独立门。尤其 $h_H(9/10)$ 是独立高频 trace 坐标；普通径向 $L^2$ 高解范数本身不控制这个 trace。本条的加权主体消费不能删除该额外边界输入，也不能替它收费。
