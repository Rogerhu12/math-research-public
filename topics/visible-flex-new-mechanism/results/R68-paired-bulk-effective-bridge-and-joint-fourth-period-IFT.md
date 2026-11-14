# R68：互反 bulk 后共同二阶与第四周期的有效桥方程

日期：2026-11-14。root 全文核对、repo_sources 独立纸核的准确约简，不含新的研究数值或已求出的桥。本稿接 R62、R65 及 [R67](R67-complete-fourth-period-cubic-bulk-count-and-bridge-control.md) 的准确递推。最后的存在结论明确是一个带尚未验证秩假设的条件定理，不是已构造第四解。

## 1. 最高项可直接用静态 profile 算子传播

固定 profile 目标 $f$ 与第一 profile $\phi$。按真实控制词的次序列出所有被共同放大 N 的常态，状态 i 的静态双线性算子记为 $R_i=\mathscr R_{k_i,h_i,\omega_i}$，基准真实长度为 $\ell_i$。

最高第二、第三及第四标量历史分别写作 $Nw,N^2u,N^3v$。长度固定的桥不改变 $w,u$ 的这些最高系数，也没有直接 $N^3$ 积分。因此仅为计算最高函数 $P_3$，可按有序常态在缩短后的变量 $\tau$ 中传播

$$w_\tau=d_i,\qquad
u_\tau=2R_i(\phi,w),\qquad
v_\tau=-R_i(w,w)+2R_i(\phi,u),$$

$$d_i=R_i(f,f)-R_i(\phi,\phi).\tag{1}$$

这里每个 $R_i$ 都用同一个右端锚；输入 $w,u$ 允许有尚未支付的左尾，不能每个常态重新置零。局部 normal 和 mixed 漂移仍属于完整恢复，但只进入更低的 N 次数，不在 (1) 中。

一个长度 $\ell$ 的常态给以下准确更新，所有右侧均使用入段的 $w,u,v$：

$$w_{\rm out}=w+\ell d,$$

$$u_{\rm out}=u+2\ell R(\phi,w)+\ell^2R(\phi,d),\tag{2}$$

$$\begin{aligned}
v_{\rm out}=v
&+\ell\{-R(w,w)+2R(\phi,u)\}\\
&+\ell^2\{-R(w,d)+2R(\phi,R(\phi,w))\}\\
&+\frac{\ell^3}{3}\{-R(d,d)+2R(\phi,R(\phi,d))\}.
\end{aligned}\tag{3}$$

证明只需在 (1) 中依次代入 $w(\tau)=w+\tau d$、$u(\tau)=u+2\tau R(\phi,w)+\tau^2R(\phi,d)$，逐项积分。最终 $v$ 是完整第四 characteristic 周期的最高系数函数 $P_3$，不是其范数。

因此计算 $P_3$ 不需要重新积分全部桥，也不必构造完整四阶大 DAG。按 R62 的显示式，静态 $R_i$ 只含 profile 的前两导数及一个真实右 Volterra 原函数；为传播 (2)–(3) 所需的输入 jet，最高只用原始 $f,\phi$ 的第四导数。这个结论只是精确接口，目前没有运行这个新的 profile 评价器。

## 2. R62 八常圈在极限参数处自动支付最高函数

R62 在四个固定 $(h_i,d_i)$ 状态各放一对 $k=+1,-1$ 完整圈，同组真实长度相同。二阶算子满足

$$R_{i,-}=-R_{i,+}.$$

因此 (1) 的**整个三角向量场**在这两个常态间变号。先走正态再走负态，同长后对任意共同右零的入值准确返回 $w,u,v$。

长度固定的真实桥可位于两常态之间；在最高 N 系数层，桥不改变 $w,u$，也不贡献 $v$。所以保持次序后，这四个相邻互反对仍给

$$M_{\rm bulk}(0)=0,\qquad
\boxed{P_3(0,\xi)=0\quad\text{对全部 }\xi.}\tag{4}$$

这里的 0 是 R62 八个 bulk 修正参数的极限值。该等式对同一 profile 和相位的全部函数成立，不依赖选取一个特殊 profile 去近似消除最高项。它不说桥被消掉：桥从 $P_2$ 开始有真实贡献。

R65 的无桥纯漂移也没有与 (4) 矛盾。没有固定长度桥且没有 bulk 修正时，理想互反对的历史部分返回，剩余完整漂移是 N 倍的局部 $\mathcal J_++\mathcal J_-$，属于 $P_1$，并非 $P_3$。

## 3. 八个二阶参数不能再自由用于第四补偿

令 $p\in\mathbb R^8$ 为 R62 的 bulk 参数，$\beta$ 为一个真实平滑桥控制族。假设这个族已经通过真实控制保证所要求的 frame/scalar 端状态及光滑接缝，并在固定 p 时保持 bulk 端状态不受桥参数改变；参数依赖在一个有界邻域光滑，桥长度不随 N 增长，并满足 R67 的同一合法坐标域及恢复分母统一远离零条件。

在同一准确八维零算子坐标中写

$$M_N(p,\beta)=N M_{\rm bulk}(p)+M_{\rm bridge}(p,\beta).$$

R62 的准确秩给

$$A=D_pM_{\rm bulk}(0):\mathbb R^8\longrightarrow\mathbb R^8
\quad\text{可逆}.\tag{5}$$

设 $\varepsilon=1/N$。对

$$M_{\rm bulk}(p)+\varepsilon M_{\rm bridge}(p,\beta)=0$$

使用有限维隐函数定理，得到局部唯一的准确二阶修正

$$p(\varepsilon,\beta)=\varepsilon a(\beta)+O(\varepsilon^2),
\qquad a(\beta)=-A^{-1}M_{\rm bridge}(0,\beta).\tag{6}$$

所以 $a$ 已被完整二阶条件固定，不是可另行随意调节的第四参数。

## 4. 准确有效桥函数

完整第四周期写成已有的准确多项式

$$\Pi_4(N,p,\beta)
=N^3P_3(p)+N^2P_2(p,\beta)+NP_1(p,\beta)+P_0(p,\beta).$$

这里所有 $P_j$ 均为 $\xi$ 的完整函数（及所需相位 Fourier 通道）；$P_3$ 在固定 bulk 端状态的前提下不依赖桥内部路径。将 (4)、(6) 代入，得

$$\Pi_4(N,p(1/N,\beta),\beta)
=N^2\mathcal C_{\rm eff}(\beta)+O(N),$$

$$\boxed{\mathcal C_{\rm eff}(\beta)
=P_2(0,\beta)
-D_pP_3(0)A^{-1}M_{\rm bridge}(0,\beta).}\tag{7}$$

第一项包括桥的直接 $N^2$ 积分及其对后续常态的历史作用。第二项是二阶修正必然引起的 bulk 最高项变化。只求 $P_2=0$ 而漏掉第二项，不是共同二阶/第四设计。

因此在这个族中，第一项有待准确支付的桥方程是

$$\mathcal C_{\rm eff}(\beta)(\xi)=0
\quad\text{对全部 }\xi\text{ 和全部所需 Fourier 模式}.\tag{8}$$

它不是八个标量方程，也不是令某个分离系数范数变小。对固定 profile，R56 给一个有限维真实函数空间容纳所有这些输出；具体分离式可能冗余，应在真实函数空间或其准确商空间中处理。

## 5. 一个足以支付有限 N 完整第四周期的条件

以下只是把后续秩任务写清楚。

假定固定 profile 的全部第四周期落在一个固定有限维实函数空间 $\mathcal V$ 中，复模式按实虚部分组成。假定存在真实桥参数 $\beta_*$，满足 (8)，且在保持上述 frame/scalar 端条件的可用桥参数方向上

$$D_\beta\mathcal C_{\rm eff}(\beta_*):\mathbb R^m\to\mathcal V
\quad\text{满射}.\tag{9}$$

这必须是准确函数空间的秩，不能用冗余展开的系数数目或未经验证的数值小奇异值替代。

定义

$$\begin{aligned}
G(\varepsilon,\beta)=\varepsilon^{-1}\big{&P_3(p(\varepsilon,\beta))
+\varepsilon P_2(p(\varepsilon,\beta),\beta)\\
&+\varepsilon^2P_1(p(\varepsilon,\beta),\beta)
+\varepsilon^3P_0(p(\varepsilon,\beta),\beta)\big}.
\end{aligned}$$

因 $P_3(0)=0$，该表达式在 $\varepsilon=0$ 光滑延拓，且

$$G(0,\beta)=\mathcal C_{\rm eff}(\beta).$$

由 (9)，固定适当的参数补空间后，隐函数定理给 $\beta(\varepsilon)$ 使 $G=0$。于是对充分大的有限整数 N，同一个真实控制族中可同时支付准确二阶零算子及**全部第四周期函数**。

这个条件定理没有支付第四 ruling、较低阶 collar/ruling、无穷阶收敛或有限等距族。这些仍须与所用 profile 构造及 R56 的全局 gauge 条件共同满足。它也没有证明 (8) 存在解或 (9) 满射；这两项是下一个可实际检验的真实桥控制任务。

## 6. 对计算设计的直接要求

先用同一冻结 profile 和有序静态算子核最高函数 (4)，再编译真实桥对 (7) 的响应，才有依据增加桥参数。评价 $D_pP_3$ 时必须保留同一 profile、同一右锚和真实常态周期变化；评价 $M_{\rm bridge}$ 与 $P_2$ 必须采用同一个真实连接，不能分别重拟合 frame 或 omega。

这提供了可用的正向层次：互反 bulk 先准确支付最高次数，二阶 IFT 消去其八个参数，然后在共同端约束下寻找真实桥的完整函数补偿。当前只有这一准确约简，尚无满足 (8)–(9) 的桥实例。任何实际积分、优化或完整目标编译仍仅允许在公开仓库 Actions 中执行。
