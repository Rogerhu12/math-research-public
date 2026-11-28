# 已证明：同一选定成员的完整有符号射线速度可从已存 193 个包络恢复

在 [CRW](R149-supplement-correlated-ray-wave-forcing-and-signed-cut-seed.md) 的严格负域 $0\le r\le c=76285779072683/320000000000000$，仍取原 $|\delta_*|\le9368259853002/10^{23}$、$\eta_0$、角周期 $\pi/2$、物理频率 $4j$。以下给出同时覆盖正负特征的完整源。只须读原方向的值包络，无须取得全部方向的浮点 Hermite 矩阵。原物理导数的限定见末节。

## 原始对象及作用域

原 SN 清单 97309 bytes，SHA256 `f6e5f9fe938d897c2b57d3d34e42391455fc6cea9804576d4dcc90b2021a8351`。原方向 native 的 `complete_negative_interval_direction_coefficient_suprema` 含完整 193 个真实修复后坐标，$u$ 的 96 个 sine，$v$ 的一个 mean 和 96 个 cosine。其 `exact_phase_interval` 覆盖整个 $[0,c]$，`derived_direction_definition_sha256` 为 `6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。原 base 两个完整分片有 2692 个 cubic，包含实际根片 2549。中心物理系数乘原 $\alpha=6890507429876859/9007199254740992$ 一次。修复 native 中的 65 个 `exact_cumulative_coefficient_suprema` 已是物理单位。每个坐标使用相应上界包围对称区间，保留 sine/cosine 的两 Fourier 符号及相位。

使用同一 169 个原标量 germ 的全部 626 格。原 $q=\sqrt{-K_0},\beta,\gamma,s$ 有已证 degree-seven Taylor 数据。220 个紧支撑 $T_{\rm met}$ 格保留原 scalar SHA。准入程序 `fourfold_codazzi_true_phase_original_inputs.py` 对 176 个自然整件（两原候选分片含在内）核验 bytes、SHA256、来源和参数。对原 Git 内容做的只读准入已通过，总计 10624293 bytes。这里使用从旧对象读取的数学结论，没有运行旧的生产代码。

## 保留小差的速度

令 $u,v$ 是未加 value repair 的原中心，$v$ 含原轴对称 $s$。令 $U,V$ 是各基修复加 $\delta_* Z$，$m=\Pi v$。在每一原片取
$$
 w=4096 t^6(1-t)^6,\qquad t=(r-1/20)/(9/50-1/20)
$$
于支撑内，外面 $w=w'=0$。令 $W=q^2-\delta_* T_{\rm met}w'$、$Q=\sqrt W$、$g=e^{-\delta_*w}$。原 metric 关系恰为 $q_\delta^2=g W$ 与 $\gamma_\delta=\gamma e^{\delta_*w/2}$，所以 $\gamma_\delta q_\delta=\gamma Q$。正根域使用原 $q>0$ 和每格的 $W>0$。设
$$
 k_\Delta=q^2(-\delta_*w)\int_0^1e^{-s\delta_*w}ds
             -g\delta_*T_{\rm met}w',\qquad H=2vV+V^2 .
$$
则 $k_\Delta=q_\delta^2-q^2$。若 $d_0=-\beta I(u^2-q^2v^2)$、$b_0=-\gamma qm$，原真实速度满足
$$
\begin{split}
 d_\delta-d_0&=-\beta I\left(2uU+U^2-q^2H-k_\Delta(v^2+H)\right),\\
 b_\delta-b_0&=-\gamma\left((\Pi V)Q-
                      m\frac{\delta_*T_{\rm met}w'}{Q+q}\right).
\end{split}
$$
第一式展开两个物理平方并保留原 primitive 的零均值定义。第二式用 $Q-q=-\delta_*T_{\rm met}w'/(Q+q)$，原外侧不作两个近等正根相减。所有带号 mode 在取范数前完成线性组合，积使用非循环全卷积。名义 $d_0$ 的支撑至 $|j|=64$，全 $d_\delta-d_0$ 至 $192$；径向 $b$ 只占零模。$U,V$ 的有向区间同时包含原固定 $\delta_*$ 的真实值，无须假设各坐标可以独立取端点。积分指数的范围取沿 $s\in[0,1]$ 的整段。

原 scalar/cubic/control 三类端点的并集构成全域覆盖。给每片 $h=r_R-r_L$，$\tau=(r_R-r)/h\in[0,1]$。以 $(-h)^j$ 乘原真正的 $j$ 阶归一化导数即可得到名义速度的 $\tau$ 导数。对原 scalar 模型在节点 $x$ 的 $j$ 阶导，归一化后已知精确中心多项式之外的误差项为
$$
 \sum_{k=j}^6 {k\choose j}(p_k-c_k)x^{k-j}
  +{7\choose j}(D_7/7!-c_7)x^{7-j}.
$$
这里 $p_k$ 为原 point jet 的归一化值，$D_7$ 为原整格最后一阶未归一化导数，$x$ 从原 Taylor 中心量起。每个 Fourier mode 的四阶 Taylor 积分余项均由同 mode 的整片四阶导数包住。固有角谱保持不截。最后把 $h(d_\delta-d_0)$ 和 $h(b_\delta-b_0)$ 作为独立完整整片的值加到名义 $h(d_0+\sigma b_0)$。对所选真实速度的径向误差不用求导。具体核为 `fourfold_codazzi_true_phase_signed_speed.py`。联合原全圆误差传播时，交换子用 $\partial_\phi^j(hd_\delta)/j!$ 的完整包络，反向速度均使用同一原角；$\sigma b$ 的非零角阶消失。

## 同一原 cubic 的径向费用

后续涉及强迫中的 $\partial_r Z$ 时，可以从相同方向原件得到真实单侧界。设 $z$ 是某一已修复 Fourier 实坐标，于实际 cubic 与原有值界的交 $I=[a,b]$ 上有 $|z|\le M$。修复是片内常数，故 $z$ 在 $I$ 是 degree $\le3$ 多项式。在仿射归一化 $x=(2r-a-b)/(b-a)$ 写成 Chebyshev 基。由 $T_j(\cos\theta)=\cos(j\theta)$ 的正交性，各 $j\ge1$ 系数绝对值 $\le 2M$。直接对 $T_1=x,T_2=2x^2-1,T_3=4x^3-3x$ 求导，得到
$$
 |z^{(p)}(r)|\le M\left(\frac{2}{b-a}\right)^p C_p,
 \qquad (C_1,C_2,C_3)=(28,56,48).
$$
选择最大的已覆盖同一原片 $I$，然后限制到该片的每一子格，避免因细分而虚增导数。对端点双方分别用合法原片的一侧值；不据此宣称一阶径向导数跨缝连续。该估计是候选上界，可与真正已付的同坐标导数界交取。因只有前两原候选分片、原方向的小 native、原 scalar 等整件参与，以上输入不需要重新创建 BLAS 依赖的方向载体。它没有给出沿路数值或全高响应的值。
