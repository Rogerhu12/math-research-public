# 同一实际根势去常数界与一阶径向势的完整复角证书

2026-11-12，independent-audit。

## 已完成范围

本记录使用 R83/R87 的准确同一族
\[
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le1/2500000,
\]
以及同一真正参数根，覆盖全部物理角复条带
\(|\Im\theta|\le1/256\)。完成报告含 4096 个连续复矩形：
半 quarter 上 256 个角格、16 个虚向 slab，准确 Schwarz 共轭及
D4 反射补齐其余域；没有失败、遗漏或待处理格。
完整源码、对象、依赖、根及 circumference 报告 SHA 均在结果内。

实现与完成报告为

- scripts/fourfold_phase_root_potential_complex_variation.py
- notes/2026-11-12-actual-root-complex-potential-variation.json.gz

已有 R87 的 complex-strip 源保持不变。这是新运行，没有用旧叶与
新叶拼成一次未经覆盖检查的报告。

## 精确量与证明接线

沿用 R83 的真实量
\[
 q=M/D,\quad U=\kappa F_z^4W^2/H^4,\quad
 V_*=\kappa W^2/D^2,\quad Y_0'=D/(\sqrt\kappa\,W).
\]
每个复矩形直接证明 \(F_z,W,D,H,\kappa\) 落在右半平面，
完整保留复值、真实无限原函数费用和分支。
相位使用已付的中心八阶有限三角 Taylor 加准确线段余项；
位置使用真实中点原函数加复角 ODE 积分界，未丢掉虚部。

\(v_0\) 采用 R83 的准确 shear-log 公式。
一阶径向势 \(v_1\) 通过冻结
fourfold_phase_canonical_collar_finite.py 的
root_potential_coefficients 得到；其公式只使用加乘、导数、log 和
exp，没有实部投影，所以同一个解析恒等式在本复域中继续成立。
这里的符号是 R87 的
\[
                       V(0,\phi)=-v_0(\phi),\qquad
                       V_y(0,\phi)=v_1(\phi).
\]
因此不能把 \(v_0>0\) 写成 canonical 零阶势为正。

每个格保存 \(v_0\) 的实球、虚球和 \(|v_0-5050|\)；
\(v_1\) 只保存其模界，没有保存实、虚球。下面没有从它推断一个
未计算的 \(v_1\) 去常数界。

## 完整有向结论

可取安全值
\[
 \begin{split}
 \sup_{|\Im\theta|\le1/256}|v_0(\theta)-5050|
       &<467.112549,\\
 \sup_{|\Im\theta|\le1/256}|v_0(\theta)|
       &<5467.370339,\\
 \sup_{|\Im\theta|\le1/256}|v_1(\theta)|
       &<2380464.991,\\
 \inf_{|\Im\theta|\le1/256}\Re Y_0'(\theta)
       &>.0560082272894397.
 \end{split}
\]
同一根 circumference 证书保持
\[
 8.32788647674253<q<11.67215062130776.
\]
按已证明的解析注入与像域包含论证，真实归一根角
\(\psi=qY_0(\theta)\) 的逆定义在
\[
                    |\Im\psi|<s_\psi,\qquad
                    s_\psi=.0009109964035743.
\]
此处使用的安全宽度为
\(q_-\inf\Re Y_0'/(2\cdot256)\)。它由真实曲边像域包含得到，
并非把相位采样插值当成真逆图。

写
\(\widetilde v_i(\psi)=v_i(Y_0^{-1}(\psi/q))\)。
四重周期给出准确 Fourier 结论：对 \(k\ne0\)，
\[
 \boxed{\quad
 |\widehat{\widetilde v_0}(4k)|
       \le467.112549\,e^{-4s_\psi|k|}.
 \quad}
\]
均值满足
\[
 |\widehat{\widetilde v_0}(0)-5050|\le467.112549.
\]
而对全部 \(k\)，
\[
 |\widehat{\widetilde v_1}(4k)|
       \le2380464.991\,e^{-4s_\psi|k|}.
\]
这是从全条带 sup 经 Fourier 积分移线得到的完整尾，
不是有限角网格 DFT 的经验衰减。

## 与有限秩 root shear 的准确关系

在 R92 的记号 \(B=UE,\ C=U\Gamma_*^{-1}M_{v_0}E\) 中，
\[
 C=5050\,B\,(\Gamma_*^{-1}|_E)
       +U\Gamma_*^{-1}M_{v_0-5050}E.
\]
第一项是明确的有限 canonical 对角系数与真实物理列 \(B\)；
第二项可使用上面的 467.112549 去常数界。两项仍有其真实物理
Fourier 尾，不能因为 canonical 列数有限就直接放入物理 \(N64\)。
这里没有计算尚未保存的全部有限列条目、height/shear frame，
没有宣称完整高频反馈、有限 Schur 可逆或非线性零解已完成。

重放命令：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python -u scripts/fourfold_phase_root_potential_complex_variation.py \
      --out notes/2026-11-12-actual-root-complex-potential-variation.json.gz
