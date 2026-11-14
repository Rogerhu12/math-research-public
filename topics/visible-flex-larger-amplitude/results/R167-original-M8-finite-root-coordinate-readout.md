# R167 — 原 M8 有限根坐标读出

作者：/root（GPT-6 Astra Pro；AI 辅助），2026-11-13。

## 已实际完成的结论

原 q003/M8 完成响应 SHA `054044cae617b440eae24b4bad3d54a8e14ded554f3f46861730c2d6ae46ca78` 保存 433 个 16 维状态。原 residual 为 $2.1825665269857528\times10^{-11}$，满足原 `solveTolerance=2e-9`。在原 cell9..7 的 109 个全部保存节点解完整有限 root；实际 owned exit0，11.37358665 秒，峰值 117928 KiB，447 门全过。

保存节点上的最大 $\sum_m(1+m)e^{m/64}(|P_m|+|K_m|)$ 为 0.012627137767697444，位于 node268/cell7/segment5。最大原 root 相对残差为 $6.497785676872963\times10^{-14}$；最大 $|\Xi-\Pi|$ 为 $2.0708862895476676\times10^{-19}$。这些是原 q003 的有限节点诊断，不能用作较强 M20/R39 中心的界。

## 两次实际启动失败保留

第一次代码把显示用舍入 residual 当作精确二进制值做相等比较，在任何模型/root计算前 exit1。v2 改为原完成状态、有限 residual 与原 solveTolerance；第二次因导入 subdivision 之前缺少原 `CLOSING_TAIL_CACHE` 环境项而 exit1。第三次仅显式提供原缓存源目录，原 v2 源与全部科学容差不改，正式成功。三次原 argv、resource、stdout及两版本源均归档；没有把失败资源记录改成成功。

## 坐标与原有限角向根

原保存 shooting state 的后半部为非线性 connection $\Pi$，不能直接当作 canonical $\Xi$。设 $h_\perp=r^4\sum_j Q_j\cos(m_j\theta)$，$m_j=2(j+1)$。相对坐标为

$$P_{m_j}=-m_jr^3Q_j/w,\qquad K_{m_j}=\sqrt2 L_j-m_jP_{m_j},\qquad c=L_0.$$

这里 $L$ 来自原有限角向 momentum root，使用正交归一余弦基；其非零模目标为 $\sqrt{12}\mu\Pi_j/(\sqrt2r^4w^2)$，零模目标为零。真正的 canonical 量为

$$\Xi_j=\frac{\sqrt2r^4w^2L_j}{\sqrt{12}\mu}.$$

原 `toRaw` 的第二半部 $\sqrt2wL_j/(\sqrt{12}r^3)$ 也不是 $\Xi$。所有比较均保留完整原有限根、均值和分支，未线性化根、略去高次项或重复 ODE。

保存节点 $i$ 的主读法使用前一 stage 的 inner endpoint $x=0$，不缩放 $\Pi$；另一读法使用当前 stage 的 outer endpoint $x=1$，须先乘回原 `portRatio`。这来自原 `cellFlow` 对输出 $\Pi$ 的除法。两读法的浮点差异只登记为诊断，不称精确接缝证明。

## 范围

原 root Newton 容差、roundoff fallback、quadrature 和原背景二进制计算都保持不变。有限 quadrature 根尚非完整连续角向证书；节点值尚非整个径向区间的范数；原二进制背景不自动等同 R26 精确实背景；未证明这些有限解等于 R143 唯一实际解。后续必须支付连续候选的原方程 residual、真实入口识别、完整 mean/逆算子及正无穷尾，才能用于同一实际场的存在结论。

