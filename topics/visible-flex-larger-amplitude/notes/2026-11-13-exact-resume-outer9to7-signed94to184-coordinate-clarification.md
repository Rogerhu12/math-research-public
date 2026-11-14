# 新94至184列的 P、K 单位澄清

作者：exact_closure（GPT-6 Astra Pro，AI 协助），2026-11-13。

本补充绑定实际主包 SHA `bda654d0d8a4710ba927213e3482958838712c02fafea05bf10df8383de427b4` 和已冻结完整证明 SHA `85c0e83718399291476ef1ea65d02dfc20b8de3f15cdb13e6d84ebb3b3e3b319`，原数值与字节均不变。

严格沿 R93、R101 原记号，外侧未知为
\[
 P=h_\theta/(rw),\qquad K=h_{\perp,r}/w.
\]
因此新矩阵和特别解的坐标是 $Y=\sqrt{rw^3}(P,K)$。源也是 R106 的相对源，强迫为 $\sqrt{rw^3}(sN_s+\ell N_\ell)$。

旧惯例 JSON 字段 `physical_P_initial`、`physical_K_initial`、`physical_particular_PK` 中的 physical 只区分这套实际 P/K 与 canonical Q/Xi 或人为 projective归一列；它不表示未除w的 $(h_\theta/r,h_{\perp,r})$。保存的两初列已经是 node10的上述相对 P/K 单位到目标相对 P/K 单位，准确转换为 $F(node10)\Phi/F(x)$。

原外侧 local-$V_I$ 范数同样用于上述 P/K。因此一个已证 node10单模强 pair帽 $q_m$ 给初 K帽 $V_I q_m/((1+m)e^{m\sigma})$，可直接消费保存的 K初列；此时不再乘或除w。如果输入改用未除w的物理 $(p,\kappa)$ 帽，则必须先在真实 node10除w转换，不能混用。非低模式在原node10 prescribed高度下 P初值为零，K仍须由真实场帽支付。

本条仅澄清单位，不新增源、frame、初值误差或非线性证明。全部零入口特别解、原数值门和未完成范围保持。
