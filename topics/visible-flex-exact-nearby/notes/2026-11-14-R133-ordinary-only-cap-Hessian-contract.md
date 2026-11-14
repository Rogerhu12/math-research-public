# R133：完整同向 Hessian 的 ordinary-only 消费合同

2026-11-14。只对原完整物理试解 $t=T w_0$ 收紧已知 Hessian 源。$T$、97 个正交输入槽、257 个物理输出槽、原 Hessian feedback 和未知输入误差算子均保持原对象。

## 1. 直接使用精确已知方向

[原局部 Hessian 正文](../results/R133-supplement-local-triangular-cap-Hessian-and-trial-source.md) 的 L.8 给完整恒等式
$$
 D^2\Psi[R,t]=-e\,\partial_\theta t+{\cal Z}t. \tag{O.1}
$$
既成局部 native bf42a295c892ec3bc606efaa9a94f2870609b73226f2034a9cbc172f187186bd 的每个原胞元 $I_i$ 已支付
$$
 \|e\|_{L^\infty(I_i\times S^1)}\le E_{\infty,i},
 \qquad E_{\infty,i}=\pi C_* r_{V,0}/8, \tag{O.2}
$$
以及 $Z_{BB,i},Z_{BC,i},Z_{CC,i}$。因此直接有
$$
 O_{B,i}\le E_{\infty,i}\|t_{B,\theta}\|_{L^2(I_i\times S^1)}
    +Z_{BB,i}\|t_B\|_{L^2}
    +Z_{BC,i}\|t_C\|_{L^2}, \tag{O.3}
$$
$$
 O_{C,i}\le E_{\infty,i}\|t_{C,\theta}\|_{L^2(I_i\times S^1)}
    +Z_{CC,i}\|t_C\|_{L^2}. \tag{O.4}
$$
这里按原归一圆周测度和真实 $dr$ 取范数。乘法使用真实 $L^\infty\times L^2$，保留乘积的全部角输出，不在 128 模处截掉新高输出。

本分解没有将 $-e t_\theta$ 写成 $\partial_\theta(-et)+e_\theta t$，因此不另收 $E_1t$，也不出现 divergence 两列。它和原四通道表示是同一完整源的两个合法表示，不能逐个 ordinary 项取 min 后再删原 divergence 项。

## 2. 真 angular Gram 和原径向积分

原四倍频非 mean 的 Gram 权重为 $1/2$，独立 even mean 权重为 1。对原 Hermite 多项式的每个完整 Fourier 槽，$\partial_\theta$ 乘频率 $4j$；odd/cosine 的相互转换不改变其 $L^2$ Gram。mean 的导数是零，但原 $t_C$ 中的 mean 及其 $Z$ 反应全部保留。

令 $a_{k,j}$ 为一个原真实子格上经准确 monomial-to-Legendre 变换的物理幅度；所有 Box 舍入半径均保留。其角导平方范数按
$$
 \int_{I}\|\partial_\theta t\|^2\,dr
 = |I|\sum_{k,j}\frac{\mathrm{Gram}_j(4j)^2|a_{k,j}|^2}{2k+1} \tag{O.5}
$$
有向上包络。该式已含格长，不再额外乘 $dr$。原 $t_B,t_C$ 的完整格范数直接复用成功 run 43616252389 保存的行，不重新计算。

原最内 Hermite 节点是 binary64(.9)，真实入口是 $9/10$；第一格按原试解延拓保留这一极短区间。全部 1341 个原局部胞元及 1977 个真实 Hermite 交集逐项核对，原节点/数组/源 SHA 不变。

## 3. 完整帽误差与允许的 min

置
$$
 O_B=\left(\sum_iO_{B,i}^2\right)^{1/2},\qquad
 O_C=\left(\sum_iO_{C,i}^2\right)^{1/2}. \tag{O.6}
$$
只消费原已付的两个 ordinary Green 增益：
$$
 E_H^{\rm ord}=G_{o,B}O_B+G_{o,C}O_C. \tag{O.7}
$$
原全 Hessian feedback $\chi_H$ 不变，故同一 $w_0$ 的新桥为
$$
 \varepsilon_{\rm mov}(w_0)
 \le \frac{\varepsilon_{\rm phys}(w_0)+E_H^{\rm ord}}{1-\chi_H}. \tag{O.8}
$$
只在这个**完整 additive**和此前成功四通道的完整 additive 之间取 min。它不改善未知输入的 $\chi_H$ 或完整 moving 误差算子；$Z_{\rm even}-w_0$ 仍须乘原误差算子 norm。真正 cut 的 odd、独立 mean、known high 及 waist 源随后还须由同一完整边界消费者接回。

## 4. 身份与公开执行

此前成功完整特定 Hessian 的 native 为
9360555293def4b1803da05c5c432a8f737ed4f3d62ea2b84c89e7e236ff7650，
其 1341 个完整原行、1977 个交集及同一准确 $w_0$ 被逐条核验。
新增工作只计算这些真实交集的 angular Legendre 范数与 O.3–8；
没有重新调用 target、primitive、原物理残差或外端计算。

全部新数学只在本公开仓库 Actions。成功行每 64 行保留 prefix，恢复核新 source、全部原输入、原行 SHA，不重复已成行。成功数学若遇发布失败，由真实 child0 与完整 native/输入/门恢复，不要求失败快照的 process.complete=true。新 plaintext summary 写前核 UTF-8 小于 60,000 bytes，完整行保留在 native。

本合同只证明同向已知 Hessian 源的合法消费形式；数值必须等待实际运行。它不自动证明完整响应误差、未知 high 反馈、全 PDE 逆或主目标。
