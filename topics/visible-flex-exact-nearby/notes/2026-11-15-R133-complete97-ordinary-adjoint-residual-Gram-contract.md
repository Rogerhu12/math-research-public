# R133：由已存本征 jets 验证物理伴随残差的完整 97 维 Gram

## 1. 对象与此次范围

本文只消费实际固定物理 $\eta_0$、原 $\nu$ 的完整连续 M32 修补中心。
原候选 index SHA256 是
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，
修补定义 SHA256 是
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
输入物理伴随试件由公开 Actions 的 complete257-state/97-input 提案保存：
每个节点的 binary64 值、每片两端导数及实际节点都解释为准确有理数据；
相邻片共享节点值，故形成准确连续的分片 Hermite 函数 $z$。
右、左导数不必跨接缝相同。此次不会把浮点 collocation 检查称为连续残差验证。

97 个输入坐标是 moving 的归一化 odd 模式 $1,\ldots,96$ 加独立 mean。
物理输出是 odd128 与 even129，圆周积分归一为 $1$；非零 sine/cosine 幅度的
Parseval 权是 $1/2$，独立 even mean 权是 $1$。所有矩阵都保留完整 97 列及符号交叉项。
本文的四个 quarter pilot 只证明所列闭区间上的界，不是全帽误差或全频逆。

完整伴随后验恒等式及真 Robin/mean/边界项，使用
`R133-supplement-full-cap-adjoint-high-to-low-boundary-grams.md` 的 A.1–A.29。
本消费者只准备其中普通体残差与 Hessian 残差的方向 Gram；不得删去其余项。

## 2. 完整形式伴随与普通残差

设已证物理系数为 $Q_B,Q_C,\beta,\gamma$，$\ell=Ks^2$。
所用完整形式伴随是

$$
(A_{\rm phys}^*z)_B
 =-2\beta z_B-\gamma Q_B\,\partial_\theta z_B
  -\gamma\partial_\theta z_C+\beta Q_Bz_C,
\tag{G.1}
$$

$$
(A_{\rm phys}^*z)_C
 =-\gamma(Q_C-\ell)\partial_\theta z_B
  +\beta(Q_C-\ell-1)z_C.
\tag{G.2}
$$

因此 $r_D=-z_r-A_{\rm phys}^*z$ 的两行准确是

$$
r_{D,B}=-z_{B,r}+2\beta z_B+
 \gamma Q_Bz_{B,\theta}+\gamma z_{C,\theta}-\beta Q_Bz_C,
\tag{G.3}
$$

$$
r_{D,C}=-z_{C,r}+\gamma Q_Cz_{B,\theta}
 -\gamma\ell z_{B,\theta}-\beta Q_Cz_C
 +\beta(\ell+1)z_C.
\tag{G.4}
$$

这里是 forward divergence 项整体取伴随，故没有额外的 $Q_{B,\theta}$ 或
$Q_{C,\theta}$。所有余项都作为普通 $L^2$ 源消费，不对未知 divergence 余项求导。

## 3. 仅复用原 7908 个标量域

原完整 quarter 与64个补齐原生点包围，分别由真实已成
`43626024582`、`43623547711` 的八份范围和 `43635264409` 供给。
producer 逐项核原 plan、四切行哈希、完整 native/process/worker/source 身份。
64 个点只替换原来缺失的 midpoint 包围，其全域 third jets 仍是原字节。
实际 graft 的正半宽 $10^{-9}$ 仅作为包含固定 $\eta_0$ 的合法包围；
不会据此把本结论扩成一个参数族。

每个原 quarter 的准确 scalar germ、完整 third jets 和 midpoint jets
足以按原 `PhysicalCapCoefficientJets` 的 directed inverse-angle、
完整 alias、无限 Fourier tail、三阶径向 Taylor 公式，构造一次新的
$Q_B,Q_C$ 有限多项式与完整误差。只重建新的物理系数包围，**零 intrinsic target 调用**；
旧帽解、旧 validator、旧 forward 列都不重算或转置。

原有限物理系数保留 $|j|\le128$。由于试件也到128，其准确有限乘积至
$|j|\le256$，在1024点 directed FFT 上完整解析。
真实物理 $Q_B,Q_C$ 的无限尾始终留在完整误差，不能据有限乘积的支撑删尾。

### 3.1 真 Hermite 节点交段

新的 binary64 Hermite 节点可能落在原 quarter 内部，故每个 quarter
按这些准确有理节点切成互不重叠交段。若原局部坐标是 $x$，新坐标是 $t$，
准确写 $x=a+bt$，其中 $b>0$、$|a|+b\le1$。
有限多项式按二项式定理准确限制；原完整 uniform error 原样保留。
系数的径向 $\ell^1$ 范数满足

$$
\sum_j\left|\sum_{k\ge j}{k\choose j}c_k a^{k-j}b^j\right|
 \le \sum_k|c_k|(|a|+b)^k \le \sum_k|c_k|.
\tag{G.5}
$$

因此无需新增 scalar target 或 midpoint，原乘积误差门仍适用。
计算中的区间只是该准确限制多项式的包围，不把其独立中点选成新函数。
首次入口以准确 $L=9/10$ 求原首 Hermite 多项式，允许且仅允许原
$[9/10,\operatorname{float}(9/10)]$ 极短延拓；不得直接拿 state[0] 冒充真入口。

## 4. 普通残差的完整系数误差

把每个 scalar 写为已选准确有限多项式加完整 uniform error，
$g=g_f+\varepsilon_g$，$|\varepsilon_g|\le E_g$，且
$\|g_f\|\le N_g$。对物理系数 $Q=Q_f+\varepsilon_Q$ 同理。
完整乘积余项满足

$$
E_{gQ}=E_gN_Q+(N_g+E_g)E_Q.
\tag{G.6}
$$

$\gamma\ell$ 与 $\beta(\ell+1)$ 的 finite scalar 系数若截至三阶，
每个被移出的高阶系数范数都加进原 uniform error，不能忽略。
在每个真实交段，以 $G_B,G_C,G_{B_\theta},G_{C_\theta}$ 表示
已知试件四个函数的准确97维普通 $L^2$ Gram，则第一行余项由

$$
2E_\beta z_B,\quad E_{\gamma Q_B}z_{B,\theta},\quad
 E_\gamma z_{C,\theta},\quad E_{\beta Q_B}z_C
\tag{G.7}
$$

共同上界；第二行由

$$
(E_{\gamma Q_C}+E_{\gamma\ell})z_{B,\theta},\qquad
(E_{\beta Q_C}+E_{\beta(\ell+1)})z_C
\tag{G.8}
$$

共同上界。它们均允许全部真实无限系数误差。

若有限个算子 $T_i$ 满足 $\|T_i\lambda\|^2\le\lambda^TG_i\lambda$，
对任何预先选定的正数 $\alpha_i$，

$$
\left\|\sum_i c_iT_i\lambda\right\|^2
 \le \lambda^T\left[(\sum_i\alpha_i)
      \sum_i\frac{c_i^2G_i}{\alpha_i}\right]\lambda.
\tag{G.9}
$$

程序从非负 trace 界选取 binary64 正权，并把它们解释为准确 dyadic，
全过程对同一个完整97维输入成立。两个输出分量的 Gram 可以相加；
同一输出的不同残差项不能误称相互正交。
每段 finite Gram 与完整 remainder Gram 分开存储，最后如需合并仍用(G.9)。

## 5. 真径向积分、完整 mean 与有向矩阵包围

所有有限 Fourier/径向系数都用原 directed Box 算术和 pairwise reduction。
设在真实长为 $h$ 的区间上，$F(r)=\sum_kF_kP_k(t)$ 是 Legendre 展开。
准确完整 Gram 是

$$
G_F=\sum_k\frac{h}{2k+1}F_k^T W_{\rm phys}F_k,
\qquad
W_{\rm phys}=\operatorname{diag}
(\tfrac12,\ldots,\tfrac12,1,\tfrac12,\ldots,\tfrac12).
\tag{G.10}
$$

每个乘法及求和都保留符号，禁止先把非对角项取绝对值再称其为 Gram。
物理角导数乘 $4j$，独立 mean 的角导数准确为零，其反应项和 Gram 从未删去。
公开运行先用非零 signed cross、独立 mean、真径向 Legendre 比例与 $4j$
作四个明确代数门；这些门只是检查实现归一，不代替实际矩阵残差。

对真实对称 Gram 的逐项区间包围，取一个准确 dyadic 对称中点矩阵 $C$，
并用 directed 最大绝对行和 $\delta$ 包围完整差矩阵的谱范数。
则

$$
G_F\preceq C+\delta I.
\tag{G.11}
$$

保存的上三角 binary64 数组和 dyadic 对角 slack 准确定义右侧；
完整原生数组只在公开 Actions artifact，repository只保存原始SHA、范围和小摘要。
这与把逐项 upper 当正半定矩阵不同。

## 6. 同一修补中心的 Hessian 伴随

原1341格完整Hessian合同给出

$$
H_R x=-e\,x_\theta+Zx,\qquad
Z=\begin{pmatrix}Z_{BB}&Z_{BC}\\0&Z_{CC}\end{pmatrix}
\tag{G.12}
$$

的真实完整 component 算子范数界。已成64原生点最终报告
`41156aa8ac5b124b2ccca96e2f52b210edf1a3f5c170fdf839e66bf0602725b8`
保存全部1341行的 `merged_residual` 与 `ordinary_zero_order`。
它们是同一完整中心残差的系数界，不依赖旧特定帽试件的输入方向；
本消费者只复用这些系数，重新积分当前97列 $z$。

若该行原 $R_V$ 界为 $R_V^*$，已有物理 $C$ 界为 $C_*$，则

$$
E_\infty=\pi C_*R_V^*/8,\qquad E_1=2C_*R_V^*.
\tag{G.13}
$$

取伴随后，第一行的完整范数源是
$E_\infty z_{B,\theta}+(E_1+Z_{BB})z_B$；
第二行是
$E_\infty z_{C,\theta}+Z_{BC}z_B+(E_1+Z_{CC})z_C$。
每行分别用(G.9)，再加两个输出的 Gram。完整 primitive、均值和物理 measure
费用均已在原 coefficient 门内；没有删除或微分未知无限余项。
原背景 native `35db98d4...`、local native `bf42a295...` 逐SHA绑定。

## 7. 发布和后继范围

每个已成原 quarter 恢复时必须同时匹配原 proposal native/process/七数组SHA、
原25输入、原子保存的 row 与 covariance/model 数组。出版失败不否定先前 child0
的数学结果，但任何数学门失败保留其真实原件，不无修改重算。
小summary写前严格检查60000B；大矩阵与完整64点数据不经connector。

本四格成功至多授予对应闭区间的完整普通体残差和Hessian方向Gram；
全7908覆盖、真左输入误差、外端全Robin/mean、完整高输出 trial Gram、
相应全帽伴随误差、以及与真正97右Poisson的矩阵合成仍各自必须支付。
不得把此pilot、已存在的finite193逆或一个更小known-source上界
当作完整无限BVP、真实参数Schur或本课题最终完成。
