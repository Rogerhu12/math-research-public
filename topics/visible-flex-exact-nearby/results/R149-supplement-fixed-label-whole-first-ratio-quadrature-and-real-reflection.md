# 已证明：真实不变标签上的首比值有符号求积与原四支反射

本结果使用 [真实一阶首比值](R149-supplement-first-order-genuine-ray-ratio-by-signed-wave-integration.md) 的 $U_\sigma=R_\sigma-c_\sigma L_{-\sigma}w_0$。原先从正根到 $c$ 的真 $R_\sigma(c)$ 全部保留。严格域使用同一 GPR 真相位载体的系数、角导误差及原不变提升；求积无需再解一次射线或另拟合一个待证的 $R$。

## 一条实函数保留四个真的有符号入口

写 $\epsilon=\operatorname{sgn} j$。原实参数上 $d$ 为奇、$b$ 为径向偶，$X$ 奇、$\omega$ 偶，故
$P_{-\sigma}(r,-\phi)=-P_\sigma(r,\phi)$、$p_{-\sigma}(r,-\phi)=p_\sigma(r,\phi)$。由原系数定义，$T_0,V_0$ 实偶，$\vartheta$ 实奇；$w_0$ 的第一分量实偶，第二分量为 $i\epsilon$ 乘实奇。WUA.13 的首强迫 $F_b$ 实偶，$F_a$ 为 $i\epsilon$ 乘实奇，其中 $-\vartheta H^{-1}H_D= i\epsilon\vartheta Q_f K_T$ 保持该奇偶性。用两原真特征、原 $R_\sigma$ 的零根起点和唯一性得
$$
 R_{\sigma,\epsilon}(r,\phi)=i\epsilon\sigma R(r,\sigma\phi),
 \qquad R=-iR_{+,+}\ \text{为实函数}.
$$
分部积分校正和 $U$ 有相同反射。若 $r_{m,\sigma,\epsilon}$ 是原 GCS 在 $\sigma\phi$ 处保存的 $m$ 阶归一化角导，则 $R^{(m)}(c,\phi)$ 同时属于 $\epsilon\sigma^{m+1}\operatorname{Im}r_{m,\sigma,\epsilon}$ 四个原区间。数值入口检查每一个原矩形的实部包含零，四个真实入口逐格逐阶交取后，才将原 2048 个细角格并入完整 128 个粗角格。没有从一个 branch 假造另一个原有观测。

## 不变标签的全部六角导

以下用 $P=P_+$、$p=P_\phi$，并将 $U=U_{+,+}/i$、$S_U=L_+U$ 和 $C=(R_{+,+}-U_{+,+})/i$ 全部按实数表出。真实不变标签 $\xi=P(r,\phi)$ 的逆记为 $H(r,\xi)$。那么
$$
 \partial_\rho[U(r,H(r,\xi))]=S_U(r,H(r,\xi)),\qquad
 \frac{\partial_\xi^m}{m!}[S_U(r,H(r,\xi))]
 =\left[\frac{(p^{-1}\partial_\phi)^m}{m!}S_U\right](r,H(r,\xi)).
$$
其证明是 $L_+P=0$、$H_\xi=1/(p\circ H)$ 和链式法则。每次归一化递推从 $m-1$ 阶到 $m$ 阶另除以 $m$。收集物理角的真实值后，提取 $C$ 的边界费用，并在固定标签上对这七个有符号源逐原片积分。真实归一化标签导在接缝连续，因为 $P$、$U$ 和已用角导连续。返回物理角时，先用 $P$ 的精确归一化角导作六阶合成，再在同一物理角加回 $C$。

设物理角格和不变标签格均采用中心 $j l/M$、半宽 $l/(2M)$，$l=\pi/2,M=128$。若真实物理格 $j$ 上 $P-\phi\in D$，所有可能标签格指标均在整数区间
$$
 [\lceil j-1+M\inf D/l\rceil,\ \lfloor j+1+M\sup D/l\rfloor]
$$
中，确定这个一致提升的区间后才取模。对每个标签格取所有可能物理原像方盒的有符号 hull；不需要猜一个唯一角格。它包住该标签中每条特征的真实源。于是宽 $h$ 的原子格上，若整格源 $S\in I$、入口 $u\in J$，则端点在 $J+hI$、全格在 $J\cup(J+hI)$ 的区间包络。此式来自沿每条固定标签积分，只有普通体源乘 $h$。入端已有被减的实际 $C(c)$，全格/末端还原支付相同 $C$。没有重新积分一项跨缝冲量。反射取得 $r_-=-R(r,-\phi)$、$r_+=R(r,\phi)$ 后，
$$
 a_1= i\epsilon G(p_+^2 r_++p_-^2r_-)/2,\qquad
 b_1= G(p_+^2 r_+-p_-^2r_-)/(2s).
$$
$G=E A^{1/6}k^{-1/4}$ 中 $E$ 是径向标量。原 GCS 已存完整 $G(c)/(-T(c))^{1/4}$，故 $E(c)=[G(c)/(-T(c))^{1/4}](-K(c))^{1/4}$，各角格给同一径向量可交取；逐真片用 $(\log E)_\rho=2\beta\Pi S$。这只在还原首幅时收费，并没有往首比值体强迫中重新引入一个指数误差。

## 完整可执行的有向对象

四个新文件 `fourfold_codazzi_true_ratio_label_mesh.py`、`fourfold_codazzi_true_ratio_physical_packets.py`、`fourfold_codazzi_true_ratio_cut_and_reference.py`、`fourfold_codazzi_true_ratio_label_quadrature.py` 分别实现角格与标签、一次真实强迫及正权矩、全部原初值/相位流读取、全域自然求积。GCS 首次成功为 46132087372/1，原私件 11131542 bytes，SHA256 `9af56c23e91a021f0463aa01b68ea93916ba11d374ecd7323ce4c4b51b3da9ba`。GPR 必须提供第一次成功的完整 receipt SHA 及其对应私件的压缩与展开 SHA；原全格定量成功门与原两支相位均接受后，方可出真正首幅。原 WGS 的严格 $p>1/27$ 和 GCS 全格共同 $\omega>4\times10^{-8}$ 仅作已证降界；共同漂移的正源还按实际 $b\min x$ 逐格更新。

每一原 scalar/cubic/control 接缝都在 GPR 计划中；再仅在 $h>(r_--r_R)/16$ 时向内二分，以控制根附近的相对径宽。逐格实际 Fourier 模不截，节点 DFT 保留全部 alias，归一化角导在整个角格由真实角 Taylor 及下一阶全频余项包围。作用量 $A_1$ 兼用 [正权接收](R149-supplement-positive-moment-reception-and-sharp-one-sided-direction-cost.md) 和有符号同点恒等式；$k_1$ 直接与标量正权矩交取。输出保存 128 个原物理角/不变标签格上的七角级数：整步 $U$ 标签、真实标签体源、真实物理 $R_{+,+}/i$、$a_1/i$ 及 $b_1$ 的原正频。最多 4500 原子格，五场每格 $5\cdot128\cdot7\cdot16=71680$ bytes，总私有展开硬限 365 MB。所有新有向双精度上下端点逐格完整读回并验证 SHA，实际求积上界由首次成功运行给出。全文不把算术入口等同于已测得的真 $C_{\rm phys}$。
