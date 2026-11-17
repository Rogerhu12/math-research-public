# 固定 J8 真嵌套 M12：前会话未登记运行的实际终态

维护会话 Astra-held10-7322d0de-20261118，分工 n4_round_core。状态：**数值证据，未成功**。

直接接读前会话已生成的终态；没有重新求解已经执行过的案例。源码仍是 `scripts/even_circle/double_nested_refinement/refine_nested_prefix.py`，来源包和初态与前一篇双模嵌套笔记相同，原物理端口、rho 守卫、BVP 误差门均未更改。

固定 $J=8$、$\lambda=.05$，从实际 $M=8$ 设计态进行 $M=12$ 同物理度量求解，完整核心和初始全图保持误差均不超过 $4.44\times10^{-16}$。物理 $\delta=.02840636891770959$、$v_d=.2645235084352783$，$v_u=.4$、ramp $.45$、原 K4/peak .2 桥与端口均不变。

实际终态为第二轮节点上限：当前 1334 个节点，拟增加 2365 个，超过原上限 2400。最大 RMS 为 $.00235530002159$，scaled BC 为 $.0394791951799$。参数 $q$ 从 $.005$ 降至 $.000396165648603$。求解耗时 379.59 秒，域守卫拒绝 3 次，merit 拒绝 53 次，接受 9 步；两轮均出现无可接受步情形。

这次初值完整核心嵌套已支付，因此不能归因于旧的 $M$ 依赖投影换核。但终态并未成功，且幅度大降，不能称保幅收敛，更不是圆弧构造不存在性的证据。对失败态不作等距、嵌入或 reach 验收。

精确历史参数、原源码 SHA-256 和四个运行输出 SHA-256 见 `../scripts/resume_n4/nested_terminal_provenance.json`。大数组不入仓库。可按前一篇恢复包重新生成初态后执行：

```bash
python -u refine_nested_prefix.py --source-topic SOURCE/bundle/topics/visible-flexible-closed-surface --checkpoint double-small-lambda-lam0.05.json.gz --out nested-M12 --modes 12 --tol 1e-6 --max-nodes 2400 --angular 768
```

下一方向是保持较高阶的近圆弧双谐波，并把圆化限定在必要区域，以减少原目标在圆弧外的大形状变化；改变目标后的求解属于设计步骤，必须另外冻结度量和完整核心族再做加密。
