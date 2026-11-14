# R68 有限参考 Yx 门：独立核查

2026-11-12，independent_audit。完整读核
[fourfold_reference_derivative_gate.py](../scripts/fourfold_reference_derivative_gate.py)，
最终绑定 SHA256

    a947f3b6bb93f254c22f8d9f526964899a4708cd4286b6029ddda0d5a1dcaa65

最后小改（positive-frequency 表述、拒非 float64 数组、未通过门的
resume 防御、真实 Q 相邻端控逐位比较）已逐项回看。本记录核数学和精确系数口径，没有再跑作者
已经通过的 toy，也不提供尚未完成的真实参考全分片证书。

## 1. 两边界与局部 Taylor

归一初始标签为 \(x\)，周期 \(2\pi\)；物理角参考
\(Y=x/4+U\)。若
\[
 U(x)=U_0+\sum_{k=1}^K(U_ke^{ikx}+\overline U_ke^{-ikx}),
\]
则准确
\[
 \operatorname{Re}Y_x(x\pm iS)
 =\frac14+2\operatorname{Re}
             \sum_{k=1}^K ikU_k\cosh(kS)e^{ikx}.
\]
两边界的实部相同。代码的常数 \(1/4\) 和频率 \(k\) 均正确；
这里不能额外乘物理 phase 中使用的4。

令 \(h=\pi/N\)。每阶正频率系数乘
\((ikh)^l/l!\)，负频取这一完整系数的准确共轭，因此 inverse DFT
的第 \(l\) 列恰是节点处真实实函数的 \(h^l/l!\) Taylor 系数。
\(N>2K\) 排除频率重合；NativeSeriesFFT 的 inverse 后乘 \(N\)
与已有归一吻合。float64 数组按准确 dyadic 输入，不把区间中点
冒称原精确输入。每个结果的虚部须含0且有限。

在节点左右闭半格内，Taylor 余项严格由
\[
 \frac{2}{p!}\sum_{k=1}^K |ikU_k|\cosh(kS)(kh)^p
\]
控制。代码用常项下界减去全部非恒定 Taylor 系数模与这项完整余项。
所有闭角格覆盖完整周期；没有把节点最小值当作整条边界下界。
条带内模数 \(1/4+2\sum|ikU_k|e^{kS}\) 也与定义一致。

## 2. 实时间凸性与 retarget

八个 Bernstein 控制函数若各有正边界实部，则对实 normalized time
的凸组合也有同一下界。再由周期 strip 上的调和最小值原理得到
整个闭初始标签带的正实部，因而 \(Y_x\ne0\)。
反向时间的 oriented 端点不改变 Bernstein 非负权这个事实。

真实 retarget 参考按已经定义的有限乘积 \(Q(t,x)b(x)\) 处理，
其完整一阶费用是
\[
 \|Q_x\|_{A_S}\|b\|_{A_S}+\|Q\|_{A_S}\|b_x\|_{A_S}.
\]
forward 使用 \(b=a\)，backward 使用
\(b=Q_{\rm forward,end}a\)，并先支付
\(\|b_x\|\le\|Q_{\rm end,x}\|\|a\|+\|Q_{\rm end}\|\|a_x\|\)。
因此无须截断乘积 Fourier 系数，也未把有限 \(Q\) 声称为真实流
Jacobian。费用按各 Bernstein control 支付后才取最小值。

## 3. 状态与证书边界

内部 control 在某节点的负值，只说明这个充分条件无法通过；
它不证明真实时间插值有零点。代码的 negative 标记名称与停止逻辑
保留这个区别。增加 N 不可能克服已证明负的 base control 再减一个
非负 retarget 费用，因此这种提前停止是合法的充分门诊断。

完整实际输出必须覆盖请求的全部 segment，全部宽度均通过，且
full_branch_nonzero_proved 另检查首末覆盖。共享 endpoint 系数按准确
数组比较；retarget 的 Q 也逐段比较实部与虚部端控，resume 会先载入
前段末端，故没有只相信 descriptor 中的连续性标记。
源分片和参数写进报告；未通过充分门的历史输出不能被
resume 当成已付记录。当前输入生成状态不由本审核替代。

未发现上述有限 Fourier、Taylor、调和/Bernstein 或产品费用中的
实质缺口。此门只认证明确有限参考的 \(Y_x\)，不认证真实流误差、
KAM 小量或完整 PDE 逆。
