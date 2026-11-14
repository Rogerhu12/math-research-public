# R133：从已存准确系数到完整 193 方阵及方向 Green 的接口

## 对象与范围

本合同固定物理 $\eta_0$、原 $\nu$ 及连续修补 M32 中心
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47。
原 5970 格证书中，状态顺序为 96 个 odd 非均值、独立 even mean、
96 个 even 非均值。每个非均值槽均使用真实圆周 $L^2$ 正交归一，
mean 槽的 Gram 为 1。径向状态为
$$
 y=R(r)h,\qquad R(r)=\operatorname{diag}(I_{96},\rho(r)I_{97}).
 \tag{M.1}
$$
原每格正权 $\rho$ 连续、分片线性；全部 $R'R^{-1}$ 项保留。

原 $193\times96$ 的 $Q$ 锚与对应局部多项式只定义 regular 子空间。
它们不是完整 $193\times193$ 传播子。本次新对象从 $I_{193}$ 出发，
保留全部 193 个输入列。首批仅处理旧索引 $0,76,3300,5969$ 四格。
原 target、候选、修补、scalar germ、primitive、projector 与原
6391 个连续 Green 片均不重算。

四个原公开摘要保存了完整的数学行、准确系数定义、原 native SHA。
这些原字节全部固定。它们不是通过抽样还原的矩阵。

## 准确系数重建

旧格 $[l,r]$ 使用 $s=(x-r)/(l-r)$。其准确参考 $\mathcal A_{\rm old}(s)$
已由原定义固定：完整 65 槽物理三次式、四个 intrinsic scalar
的 dyadic Taylor 系数、每次运算都作 degree 3 径向截断、全部
128 个 primitive 中间模、完整 mean-rank 列及准确 $\rho$ 与
$\rho^{-1}$ 的参考多项式。原证书已付
$$
 \|A_{\rm true}(x)-\mathcal A_{\rm old}(s)\|_2\le\epsilon_{\rm old}.
 \tag{M.2}
$$
这里 $A_{\rm true}$ 是 (M.1) 坐标的完整有限 193 生成元。

重建程序只把已存 dyadic 系数交回原 directed Fourier/Arb
有限代数，**不调用**原 scalar target。重建时 Field 的 error 可置零，
因为这一步只定义原准确参考多项式；原全部真实误差
$\epsilon_{\rm old}$ 随后原样加入。此次重建所产生的径向弃项费用
不再加第二次，它们已经属于 (M.2)。每个参考矩阵的数值 enclosure
本身仍保留 directed FFT 和矩阵算术的所有舍入。

改用 $t=(x-l)/(r-l)=1-s$，在 Arb 中展开
$\mathcal A_{\rm old}(1-t)$，然后逐矩阵条目选取新的 binary64 中点。
新的选取明确构成另一组准确 dyadic 矩阵 $A_0,\ldots,A_3$。
程序保存原始数组字节和每个数组 SHA，并另付
$$
 \epsilon_{\rm new}
 =\epsilon_{\rm old}
   +\sum_{j=0}^3\|[t^j]\mathcal A_{\rm old}(1-t)-A_j\|_2.
 \tag{M.3}
$$
故 $A_*(t)=\sum_jA_jt^j$ 满足完整同域误差门
$\|A_{\rm true}-A_*\|_2\le\epsilon_{\rm new}$。
新 reference 不假设原未存 BLAS 矩阵跨硬件逐字相同。
原准确 $\rho'$ 与 inverse-$\rho$ 系数必须与重建值逐项相等。

## 完整方阵多项式及连续逆门

令 $h=r-l$。选取 degree 24 的完整方阵多项式
$F(t)=\sum_{n=0}^{24}F_nt^n$，$F_0=I_{193}$。
对每个递推项先计算
$$
 \frac{h}{n+1}\sum_{j=0}^{\min(3,n)} A_jF_{n-j},
 \tag{M.4}
$$
再选取并保存准确 binary64 矩阵 $F_{n+1}$。这些新增舍入不会被称成
“递推准确为零”。程序在选取完成后重新直接计算全部残差系数：
$$
 d_F\ge
 \sum_{k=0}^{27}\left\|
 \frac{k+1}{h}F_{k+1}
 -\sum_{\substack{0\le j\le3\\0\le k-j\le24}}A_jF_{k-j}
 \right\|_2,
 \tag{M.5}
$$
其中 $k\ge24$ 时导数项为零。矩阵二范数上界均是完整
$\min(\|\cdot\|_F,\sqrt{\|\cdot\|_1\|\cdot\|_\infty})$，
不使用 sampled SVD 代替完整界。

记 $M=\sum_{j=0}^3\|A_j\|_2$。令 $\Phi_*$ 是 $A_*$ 的准确初值传播子。
Duhamel 与正反向 Gronwall 给出
$$
 \|F-\Phi_*\|_{\infty}\le h e^{hM}d_F,\qquad
 \sigma_{\min}(F(t))\ge
 \ell_F:=e^{-hM}-h e^{hM}d_F.
 \tag{M.6}
$$
实际 gate 必须严格证明 $\ell_F>0$。它覆盖整个闭格，不能用端点
可逆性替代。于是 $F$ 定义的准确有理生成元
$\widetilde A=F_xF^{-1}$ 满足
$$
 \|\widetilde A-A_{\rm true}\|_\infty
 \le\epsilon_{\rm new}+d_F/\ell_F.
 \tag{M.7}
$$
本式没有把 $\epsilon_{\rm new}$ 再乘一次不必要的
$\|F\|\|F^{-1}\|$，因为 $A_*-A_{\rm true}$ 是直接的算子差。

同时保留
$$
 \|F\|_\infty\le
 \min\left\{\sum_n\|F_n\|_2,\ e^{hM}(1+hd_F)\right\}.
 \tag{M.8}
$$
若需相对于真实生成元的完整初值传播子误差，另有
$$
 \|\Phi_{\rm true}-F\|_\infty
 \le h e^{h(M+\epsilon_{\rm new})}
       \bigl(d_F+\epsilon_{\rm new}\|F\|_\infty\bigr).
 \tag{M.9}
$$
这些门均保全部输出与全部输入，包含独立 mean。

反方向不是另换数学背景。它准确使用同一 $A_*(1-s)$、
signed step $-h$，再对新的 backward 多项式完整执行 (M.5)–(M.9)。
两端矩阵乘积 $F(1)B(1)-I$ 与 $B(1)F(1)-I$ 均直接付完整矩阵误差。
新增 endpoint inverse proposal $C$ 也验证
$\|I-F(1)C\|<1$ 和 $\|I-CF(1)\|<1$；保存真实方阵及其准确字节。
端点与整格门各自保留。

## 保留实际频率方向

定义完整正交分拆
$$
 L_{65}=\{u_j:1\le j\le32;\ v_0,v_j:1\le j\le32\},
 \qquad
 E_{128}=\{u_j,v_j:33\le j\le96\}.
 \tag{M.10}
$$
它们恰好覆盖 193 槽，mean 位于 $L_{65}$。对于固定 M32 背景，
已付的 $A_{LH}$ 输出只位于 $E_{128}$。本次保存的方阵使后继
消费者能够保留这 128 个实际方向，避免把它们先合成为任意
193 状态的 scalar source 负荷。

程序当前记录四个 endpoint block 的完整矩阵范数；它们是
**新准确多项式**的局部 block，不被标为全局 Green 或任意径向源
的 controllability Gram。若要转为真实局部传播子 block，须加
(M.9)。没有由 128 个固定径向 forcing 试验替代无限维
$L^2_r(\mathbb R^{128})$ 源空间。

## 后继双端矩阵 Green 的准确接线

以下为可供后继消费者使用的恒等式，首批四格通过不表示其全部
数值前提已经完成。设全区间上构成 $U(x)\in\mathbb R^{193\times97}$
和 $V(x)\in\mathbb R^{193\times96}$，分别满足名义左 96 行和右
97 行边界；$Y=[U,V]$ 处处可逆，二者由同一分片连续有理生成元传播。
给定实际 source 矩阵 $B(x)$，写
$Y(s)^{-1}B(s)=(c_U(s),c_V(s))^{\mathsf T}$。准确两端 kernel 为
$$
 K_B(x,s)=
 \begin{cases}
 -U(x)c_U(s),&x<s,\\
 V(x)c_V(s),&x>s.
 \end{cases}
 \tag{M.11}
$$
其对角跳为 $Uc_U+Vc_V=B$，并非只验证任意固定径向 load。

若各胞元采用新的多项式 $F_i$，可先选择准确端点
$Y_i=[U_i,V_i]$ 与可逆坐标转换 $T_{U,i},T_{V,i}$，再用完整 endpoint
patch 满足
$$
 F_i(1)Y_i
 =Y_{i+1}\operatorname{diag}(T_{U,i},T_{V,i}).
 \tag{M.12}
$$
随后重新支付这个 patched 多项式的全部 (M.5)–(M.9) 门。只有该
真实连续匹配成立时，才可免去归一化 $Q$ 所产生的虚接口负荷；
否则全部真实矩阵跳仍应付入原接口源列。旧 $Q$ 的 projector 证书
不会自动给 (M.12) 或给完整 $Y$ 可逆性。

设 $\mathcal D=(\partial_x-A_{\rm true},B_{\rm left},B_{\rm right})$
是已有完整 finite193 逆 $G_L$ 的问题。任意已构造 $K_B$ 满足
准确 source 对角跳，定义
$$
 E_B=(\partial_x-A_{\rm true})K_B-B.
$$
则
$$
 G_L B=K_B-G_L(E_B,\ B_{\rm left}K_B,\ B_{\rm right}K_B).
 \tag{M.13}
$$
因此只需逐项支付真实 ordinary-$L^2$ 源缺陷和两端真实边界缺陷，
即可获得新的方向上界；本后验恒等式不另要求新的 Neumann
收缩门。两端缺陷必须分别乘原两端 Poisson/源列，不能只乘
ordinary-source 的逆常数。若存在真实分片跳，还须完整加入
其原接口列。所有 norm 恢复均用 (M.1) 与准确 $dx$。

完整 controllability/observability 消费者还需保留径向 source
核的真实平方积分或 Schur 界。当前 local pilot 不宣称已执行这一步。

## 原件、恢复与发布

四个输入为原 run 43591378059 目录 evidence 下的
validated-cell-00000/00076/03300/05969-summary.json，各自 SHA、
原 native SHA、完整 row canonical SHA 都保留。原模型 source SHA 为
b30eb7299d5803856712134947f3d7899961cc3ab7597ce961b9bf0cf5205183。

完整新增方阵只存公开 Actions artifact 的 matrices 目录，逐文件及
逐数组保存 SHA、shape、dtype 与真实 run/attempt；仓库小 native
保存完整严格界及数组收据。当前或之前成功 prefix 的数学行按同
source/输入/精度/degree 身份复用。即使数学 child 已成功而后续
发布失败，也不得以 process.complete 为由重新计算成功行。
若数组属于旧 artifact，继续保存其原 run/attempt 路由，不伪称
新 artifact 已重新包含这些旧数组。

本合同不授未知高 BVP、全低高 Schur、非零 $\delta$、真无限
$\nu$ 响应或主课题完成。真实帽的全部低高 cross-block 与独立 mean
行继续保留。
