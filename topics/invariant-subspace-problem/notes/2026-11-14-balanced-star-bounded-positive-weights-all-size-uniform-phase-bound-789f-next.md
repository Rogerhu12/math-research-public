# 平衡 star：有界正权区间上的全尺寸统一相位预算

日期：2026-11-14；工作标识：789f。

## 0. 定理、真实源与范围

固定 \(0<a\le b<\infty\)。任取正整数 \(q_1,\ldots,q_m\)，令
\(Q=\sum_iq_i\)，并取 \(a\le z_i\le b\)。在 \(2Q\) 位的真实加权 Boolean 模型中，主组长度为 \(Q\)、权平方为 \(1\)，其余组长度为 \(q_i\)、权平方为 \(z_i\)。限制到各组的实际对称 reducing 模块，保留该模块的整个 \(m\) 维低 primitive 源及一维硬 primitive 源。

其完整相位使用同一概率实现
\[
 F(t)=\prod_i(1-t+z_it)^{q_i},\qquad
 \rho(t)=F(t)/\int_0^1F,
\]
\[
 K_i\mid T=t\sim\operatorname{Bin}(q_i,p_i(t))
 \quad\hbox{条件独立},\qquad
 p_i(t)=\frac{z_it}{1-t+z_it},\qquad X_i=K_i/q_i.
\]
记
\[
 G=\operatorname{Cov}X,\quad
 H=\mathbb E\frac{1-T}{T}XX^*,\quad
 L=\mathbb E\frac{T}{1-T}(\mathbf1-X)(\mathbf1-X)^*,
\]
\[
 y=2\mathbb EX-\mathbf1,\qquad
 J=HG^{-1}L-2G-yy^*,\qquad
 \Phi=H^{-1/2}J^*L^{-1}JH^{-1/2}.                       \tag{0.1}
\]
全部逆都是这整个真实源上的完整逆。三个 Gram 严格正定，因为在
\(0<T<1\) 上，每个条件二项噪声的方差均严格正，且 \(\rho>0\)。

**定理。** 存在只依赖 \(a,b\) 的有限常数 \(\kappa(a,b)\)，使所有上述有限模型都满足
\[
 \boxed{\quad J^*L^{-1}J\preceq\kappa(a,b)H,
                    \qquad \Phi\preceq\kappa(a,b)I.\quad} \tag{0.2}
\]
等价地，
\[
 \begin{pmatrix}\kappa(a,b)H&J^*\\J&L\end{pmatrix}\succeq0.
\]
常数不依赖 \(Q,m\)、组比例、\(\min q_i\)、累计平方偏差或总漂移；允许全部小组均为单个位。

本稿把已经完成的真实全源估计按有限阈值拼合。它没有再假设一个尚未证明的“所有参数上的紧性”，也没有把逐点渐近常数当作统一常数。定理限于上述平衡 star 的完整 reducing 模块；尚未证明权区间退化时有绝对统一常数，亦未直接支付一般出生或原无限 graph 的源费用。

## 1. 已证明的六个输入

以下输入都控制同一个有序差 (0.1)，而不是分别比较单高度 Gram。

1. [有界累计平方偏差、任意总漂移](2026-11-14-balanced-star-bounded-spread-endpoint-decay-and-unrestricted-drift-789f-next.md)。对固定正权区间和 \(S_0<\infty\)，若
   \[
   S=\sum_iq_i(z_i-1)^2\le S_0,
   \]
   则 \(\Phi\preceq K_{\rm bd}(a,b,S_0)I\)，其中 \(K_{\rm bd}<\infty\) 不依赖其他参数。它包含原有限中央窗口与两个有界偏差端峰的完整拼合。

2. [大总曲率的高斯窗口](2026-11-14-balanced-star-large-total-curvature-gaussian-window-contraction-789f-next.md)。对每个固定 \(\Lambda<\infty\)，存在 \(S_{\rm G}(a,b,\Lambda)<\infty\)，使
   \[
   S\ge S_{\rm G},\qquad
   |D|\le\Lambda\sqrt S,\qquad D=\sum_iq_i(z_i-1)
   \]
   蕴含 \(\Phi\preceq I\)。原结论实际给共同严格收缩。

3. [总曲率控制的紧内峰](2026-11-14-balanced-star-dimension-free-interior-total-curvature-bound-789f-next.md)。对固定 \(0<\eta<1/2\)，若真实内峰 \(t\in[\eta,1-\eta]\)，且
   \[
   M=\sum_iq_i\left(\frac{z_i-1}{1+t(z_i-1)}\right)^2
       \ge M_{\rm I}(a,b,\eta),
   \]
   则 \(\Phi\preceq2I\)。这里 \(M_{\rm I}<\infty\) 可通过原
   \(1+CM^{-1/2}\) 估计及其起始阈值取得。

4. [近端内峰的光滑角点](2026-11-14-balanced-star-near-end-interior-smooth-corner-uniform-bound-789f-next.md)。存在 \(u_{\rm N},r_{\rm N}>0\)，仅依赖权区间，使
   \[
   0<\sqrt t\le u_{\rm N},\qquad
   0<(t\sqrt M)^{-1}\le r_{\rm N}
   \]
   蕴含 \(\Phi\preceq2I\)。这是原 \(1+C(\sqrt t+(t\sqrt M)^{-1})\)
   的有限阈值版本。联合正实计数延拓、完整归一 Gram 的一致高阶混合导数、两条坐标轴上的消 jet，均已在该稿内证明。

5. [严格端峰的大二阶亮方向角点](2026-11-14-balanced-star-large-second-bright-endpoint-corner-uniform-decay-789f-next.md)。存在 \(K_{\rm E},\delta_{\rm E}>0\)，仅依赖权区间，使在
   \[
   R=-D>0,\qquad S/R\ge K_{\rm E},\qquad S/R^2\le\delta_{\rm E}
   \]
   时有 \(\Phi\preceq I\)。原结论为 \(C(S/R^2)^2I\)，故缩小
   \(\delta_{\rm E}\) 即得此形式。这里使用实际的 \(R,S\)，其与光滑角点坐标的准确换算已在原稿支付。

6. [严格端峰的有界二阶亮方向](2026-11-14-balanced-star-bounded-second-bright-endpoint-uniform-decay-789f.md)。对每个固定 \(K_0<\infty\)，存在 \(R_{\rm E}(a,b,K_0)<\infty\)，使
   \[
   R=-D\ge R_{\rm E},\qquad S/R\le K_0
   \]
   蕴含 \(\Phi\preceq I\)。这是该稿的 \(C/R^2\) 衰减及起始阈值的直接推论，允许 \(S\to\infty\)，不能只以输入1代替。

上述六条完整证明均已入主线；本稿只按它们的实际量词作阈值接合。

## 2. 真实端点反射及曲率比较

先把原权区间扩成倒数封闭的正区间
\[
 A=\min\{a,b^{-1},1\},\qquad B=A^{-1}.
                                                               \tag{2.1}
\]
以后所有输入都在 \([A,B]\) 上选取常数。

改成倒数权 \(z_i'=z_i^{-1}\)，并同时令
\(T'=1-T,\ X'=\mathbf1-X\)。其真实密度只差一个归一化常数，故
\[
 H'=L,\quad L'=H,\quad G'=G,\quad y'=-y,\quad J'=J^*.
\]
相应标准化交叉算子互为伴随：
\[
 L'^{-1/2}J'H'^{-1/2}
       =(L^{-1/2}JH^{-1/2})^*.
\]
因此相位的最大特征值准确保持。这里不声称 \(H\) 或 \(L\) 与其他矩阵交换。

倒数权仍位于 \([A,B]\)，而累计平方偏差满足
\[
 B^{-2}S\le S'=\sum_iq_i(z_i^{-1}-1)^2\le B^2S.          \tag{2.2}
\]

若 \(S>0\)，令
\[
 \varphi(t)=\log F(t),\qquad
 \varphi'(t)=\sum_i\frac{q_i(z_i-1)}{1+t(z_i-1)}.
\]
在 \([0,1]\) 上
\[
 \varphi''(t)
     =-\sum_i\frac{q_i(z_i-1)^2}{(1+t(z_i-1))^2}<0.
\]
所以有唯一最大点 \(t_*\in[0,1]\)。必要时作上述反射，可令
\(0\le t_*\le1/2\)。

在严格内峰 \(0<t=t_*<1\)，令 \(M=-\varphi''(t)\)。因为
\(A\le1+t(z_i-1)\le B\)，有
\[
                   B^{-2}S\le M\le A^{-2}S.             \tag{2.3}
\]
而 \(\varphi'(t)=0\) 给实际漂移的准确公式
\[
 D=t\sum_i\frac{q_i(z_i-1)^2}{1+t(z_i-1)}>0.             \tag{2.4}
\]
因此
\[
 \frac D{\sqrt S}
   \le \frac tA\sqrt S
   \le \frac BA\,t\sqrt M.                              \tag{2.5}
\]
这是将近端内峰中尚未进入角点的小 \(t\sqrt M\) 区域送入输入2的关键。
不能只按“峰很靠近端点”而忽略这个中间范围。

若 \(t_*=0\)，则 \(D=\varphi'(0)\le0\)。当 \(D=0\) 时直接属于
高斯窗口；只有 \(D<0\) 才需要严格端峰参数 \(R=-D>0\)。

## 3. 按固定次序选择有限阈值

以下选择只依赖 \([A,B]\)，且没有循环依赖。

首先按输入4缩小 \(u_{\rm N}\)，使 \(u_{\rm N}\le1/2\)，并置
\[
                    \eta=u_{\rm N}^2\le1/4.
\]
取输入3在 \([\eta,1-\eta]\) 上的阈值
\[
                    M_0=M_{\rm I}(A,B,\eta).
\]

按输入5选择 \(K_{\rm E}\)、\(\delta_{\rm E}\)，令
\[
 K_0=\max\{K_{\rm E},1\},\qquad
 \delta_0=\min\{\delta_{\rm E},1\}.
\]
再按输入6取
\[
                    R_1=\max\{R_{\rm E}(A,B,K_0),1\}.
\]
随后定义
\[
 \Lambda=\max\left\{1,\delta_0^{-1/2},
                          \frac B{A r_{\rm N}}\right\},
 \qquad S_{\rm G}=S_{\rm G}(A,B,\Lambda).                \tag{3.1}
\]
最后取
\[
 T_0=\max\{1,S_{\rm G},B^2M_0,K_0R_1\},\qquad
                         S_0=B^2T_0.                  \tag{3.2}
\]
所求的一个有限常数可选为
\[
                \boxed{\kappa(a,b)=
                  \max\{K_{\rm bd}(A,B,S_0),\,2\}.}     \tag{3.3}
\]
这些常数的保守数值没有在此最优化。它们都由已证明的有限导数界、
正谱阈值及明确的顺序选择取得，不是对无限维参数空间直接取一个
未经证明有限的上确界。

## 4. 穷尽所有有限模型

若原模型的 \(S\le S_0\)，输入1与 (3.3) 已给结论，包括
\(S=0\)、所有权为 \(1\) 的情形。

以下设原 \(S>S_0\)。必要时作 §2 的端点反射，使最大点
\(t_*\le1/2\)。仍把反射后的量写为 \(z,S,D,M\)。由 (2.2)、(3.2)，
这个方向的实际平方偏差仍满足
\[
                              S>T_0.                  \tag{4.1}
\]

### 4.1 最大点为严格内峰

若 \(t_*\ge\eta\)，则
\(t_*\in[\eta,1-\eta]\)，且由 (2.3)、(4.1)
\[
                         M\ge B^{-2}S>M_0.
\]
输入3给 \(\Phi\preceq2I\)。

若 \(0<t_*=t<\eta\)，分两种实际尺度：

- 若 \(t\sqrt M\ge r_{\rm N}^{-1}\)，则
  \(\sqrt t\le u_{\rm N}\) 且 \((t\sqrt M)^{-1}\le r_{\rm N}\)，
  输入4给 \(\Phi\preceq2I\)。
- 若 \(t\sqrt M<r_{\rm N}^{-1}\)，(2.5) 给
  \(0<D/\sqrt S\le B/(Ar_{\rm N})\le\Lambda\)。
  结合 \(S>T_0\ge S_{\rm G}\)，输入2给 \(\Phi\preceq I\)。

这包括 \(t\to0\) 与 \(M\to\infty\) 的任意相对速度；特别没有漏掉
\(t\sqrt M\) 有界但 \(S\) 任意大的区域。

### 4.2 最大点在左端点

此时 \(D\le0\)。若 \(-D\le\Lambda\sqrt S\)，输入2立即适用，
包含 \(D=0\)、\(-D\) 有限而 \(S\to\infty\) 等情形。

否则记 \(R=-D>\Lambda\sqrt S\)。于是
\[
                    \frac S{R^2}<\Lambda^{-2}\le\delta_0.
                                                               \tag{4.2}
\]
若 \(S/R\ge K_0\)，输入5给 \(\Phi\preceq I\)。

余下 \(S/R<K_0\) 时，由 (4.1)、(3.2)
\[
                         R>S/K_0>T_0/K_0\ge R_1.
\]
故输入6给 \(\Phi\preceq I\)。这一分支包含 \(S/R\to0\)，即使
\(S\to\infty\) 也不遗漏；它使用有界二阶亮方向定理，不使用较窄的
“\(S\) 有界”结论。

§4.1–4.2 穷尽唯一最大点的位置和全部尺度。所有反射都保相位范数，
所以返回原方向便得 (0.2)。

## 5. 可以使用的结论与尚未支付的接口

本稿的新结论是同一个真实平衡 star 全源在每个固定正权区间上的
**全尺寸、全漂移、全曲率统一有限预算**。它超出了任何固定组数、
固定 profile 或固定累计平方偏差的结果。

但 \(\kappa(a,b)\) 仍允许在 \(a\downarrow0\) 或 \(b\uparrow\infty\)
时增长。原连续尾的增长窗口若导致权比发散，必须另付此增长费用。
此外，主组长度等于其余有效长度总和的结构，使本模块的硬 primitive
只有一维；一般高出生模块具有更大的硬源与更深 nuisance。
未给出保持完整逆和物理源度量的 reducing 嵌入或 Schur 支配之前，
不能把 (0.2) 自动用于这些源。

后续应在原 graph 的同一物理分拆中逐项识别能否出现本模块、
其权区间怎样随窗口变化，以及有限相位预算如何进入已有跨出生
和 moving-source 费用。本稿没有改变本课题 README 的完成标准。
